from abc import ABC
from collections.abc import Callable
from collections.abc import Iterator
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Tuple
from typing import TypeVar
from typing import overload

from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from System.ActivationContext import ContextForm
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
from System.Environment import SpecialFolder
from System.Environment import SpecialFolderOption
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
from System.Security.Util.Tokenizer import StringMaker
from System.Text import Encoding
from System.Text import NormalizationForm
from System.Text import StringBuilder
from System.Threading import CancellationToken
from System.Threading import HostExecutionContextManager
from System.Threading import LazyThreadSafetyMode
from System.Threading import WaitHandle
from System.TimeZoneInfo import AdjustmentRule

T = TypeVar("T")
T1 = TypeVar("T1")
T10 = TypeVar("T10")
T11 = TypeVar("T11")
T12 = TypeVar("T12")
T13 = TypeVar("T13")
T14 = TypeVar("T14")
T15 = TypeVar("T15")
T16 = TypeVar("T16")
T17 = TypeVar("T17")
T18 = TypeVar("T18")
T19 = TypeVar("T19")
T2 = TypeVar("T2")
T20 = TypeVar("T20")
T21 = TypeVar("T21")
T3 = TypeVar("T3")
T4 = TypeVar("T4")
T5 = TypeVar("T5")
T6 = TypeVar("T6")
T7 = TypeVar("T7")
T8 = TypeVar("T8")
T9 = TypeVar("T9")
TEventArgs = TypeVar("TEventArgs")
TInput = TypeVar("TInput")
TKey = TypeVar("TKey")
TOutput = TypeVar("TOutput")
TRest = TypeVar("TRest")
TResult = TypeVar("TResult")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class AccessViolationException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

Action: Callable[[T], None] = ...
"""

:param obj: 
"""
Action: Callable[[T1, T2], None] = ...
"""

:param arg1: 
:param arg2: 
"""
Action: Callable[[T1, T2, T3], None] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
"""
Action: Callable[[T1, T2, T3, T4], None] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
"""
Action: Callable[[T1, T2, T3, T4, T5], None] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:param arg5: 
"""
Action: Callable[[T1, T2, T3, T4, T5, T6], None] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:param arg5: 
:param arg6: 
"""
Action: Callable[[T1, T2, T3, T4, T5, T6, T7], None] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:param arg5: 
:param arg6: 
:param arg7: 
"""
Action: Callable[[T1, T2, T3, T4, T5, T6, T7, T8], None] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:param arg5: 
:param arg6: 
:param arg7: 
:param arg8: 
"""
Action: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9], None] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:param arg5: 
:param arg6: 
:param arg7: 
:param arg8: 
:param arg9: 
"""
Action: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10], None] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:param arg5: 
:param arg6: 
:param arg7: 
:param arg8: 
:param arg9: 
:param arg10: 
"""
Action: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11], None] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:param arg5: 
:param arg6: 
:param arg7: 
:param arg8: 
:param arg9: 
:param arg10: 
:param arg11: 
"""
Action: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12], None] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:param arg5: 
:param arg6: 
:param arg7: 
:param arg8: 
:param arg9: 
:param arg10: 
:param arg11: 
:param arg12: 
"""
Action: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13], None] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:param arg5: 
:param arg6: 
:param arg7: 
:param arg8: 
:param arg9: 
:param arg10: 
:param arg11: 
:param arg12: 
:param arg13: 
"""
Action: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14], None] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:param arg5: 
:param arg6: 
:param arg7: 
:param arg8: 
:param arg9: 
:param arg10: 
:param arg11: 
:param arg12: 
:param arg13: 
:param arg14: 
"""
Action: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15], None] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:param arg5: 
:param arg6: 
:param arg7: 
:param arg8: 
:param arg9: 
:param arg10: 
:param arg11: 
:param arg12: 
:param arg13: 
:param arg14: 
:param arg15: 
"""
Action: Callable[
    [T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16], None
] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:param arg5: 
:param arg6: 
:param arg7: 
:param arg8: 
:param arg9: 
:param arg10: 
:param arg11: 
:param arg12: 
:param arg13: 
:param arg14: 
:param arg15: 
:param arg16: 
"""
Action: Callable[[], None] = ...
""""""

class ActivationContext(Object, ISerializable, IDisposable):
    """"""

    @property
    def ApplicationManifestBytes(self) -> Array[int]:
        """:return:"""
    @property
    def DeploymentManifestBytes(self) -> Array[int]:
        """:return:"""
    @property
    def Form(self) -> ActivationContext.ContextForm:
        """:return:"""
    @property
    def Identity(self) -> ApplicationIdentity:
        """:return:"""
    @classmethod
    @overload
    def CreatePartialActivationContext(cls, identity: ApplicationIdentity) -> ActivationContext:
        """:param identity:
        :return:
        """
    @classmethod
    @overload
    def CreatePartialActivationContext(
        cls, identity: ApplicationIdentity, manifestPaths: Array[str]
    ) -> ActivationContext:
        """:param identity:
        :param manifestPaths:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

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
        """:param assemblyName:
        :param typeName:
        :return:
        """
    @classmethod
    @overload
    def CreateComInstanceFrom(
        cls,
        assemblyName: str,
        typeName: str,
        hashValue: Array[int],
        hashAlgorithm: AssemblyHashAlgorithm,
    ) -> ObjectHandle:
        """:param assemblyName:
        :param typeName:
        :param hashValue:
        :param hashAlgorithm:
        :return:
        """
    @classmethod
    @overload
    def CreateInstance(cls) -> T:
        """:return:"""
    @classmethod
    @overload
    def CreateInstance(cls, activationContext: ActivationContext) -> ObjectHandle:
        """:param activationContext:
        :return:
        """
    @classmethod
    @overload
    def CreateInstance(cls, type: Type) -> object:
        """:param type:
        :return:
        """
    @classmethod
    @overload
    def CreateInstance(
        cls, activationContext: ActivationContext, activationCustomData: Array[str]
    ) -> ObjectHandle:
        """:param activationContext:
        :param activationCustomData:
        :return:
        """
    @classmethod
    @overload
    def CreateInstance(cls, assemblyName: str, typeName: str) -> ObjectHandle:
        """:param assemblyName:
        :param typeName:
        :return:
        """
    @classmethod
    @overload
    def CreateInstance(cls, type: Type, args: Array[object]) -> object:
        """:param type:
        :param args:
        :return:
        """
    @classmethod
    @overload
    def CreateInstance(cls, type: Type, nonPublic: bool) -> object:
        """:param type:
        :param nonPublic:
        :return:
        """
    @classmethod
    @overload
    def CreateInstance(cls, domain: AppDomain, assemblyName: str, typeName: str) -> ObjectHandle:
        """:param domain:
        :param assemblyName:
        :param typeName:
        :return:
        """
    @classmethod
    @overload
    def CreateInstance(
        cls, assemblyName: str, typeName: str, activationAttributes: Array[object]
    ) -> ObjectHandle:
        """:param assemblyName:
        :param typeName:
        :param activationAttributes:
        :return:
        """
    @classmethod
    @overload
    def CreateInstance(
        cls, type: Type, args: Array[object], activationAttributes: Array[object]
    ) -> object:
        """:param type:
        :param args:
        :param activationAttributes:
        :return:
        """
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
        """:param type:
        :param bindingAttr:
        :param binder:
        :param args:
        :param culture:
        :return:
        """
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
        """:param type:
        :param bindingAttr:
        :param binder:
        :param args:
        :param culture:
        :param activationAttributes:
        :return:
        """
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
        """:param assemblyName:
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
        """:param domain:
        :param assemblyName:
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
        """:param assemblyName:
        :param typeName:
        :param ignoreCase:
        :param bindingAttr:
        :param binder:
        :param args:
        :param culture:
        :param activationAttributes:
        :param securityInfo:
        :return:
        """
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
        """:param domain:
        :param assemblyName:
        :param typeName:
        :param ignoreCase:
        :param bindingAttr:
        :param binder:
        :param args:
        :param culture:
        :param activationAttributes:
        :param securityAttributes:
        :return:
        """
    @classmethod
    @overload
    def CreateInstanceFrom(cls, assemblyFile: str, typeName: str) -> ObjectHandle:
        """:param assemblyFile:
        :param typeName:
        :return:
        """
    @classmethod
    @overload
    def CreateInstanceFrom(
        cls, domain: AppDomain, assemblyFile: str, typeName: str
    ) -> ObjectHandle:
        """:param domain:
        :param assemblyFile:
        :param typeName:
        :return:
        """
    @classmethod
    @overload
    def CreateInstanceFrom(
        cls, assemblyFile: str, typeName: str, activationAttributes: Array[object]
    ) -> ObjectHandle:
        """:param assemblyFile:
        :param typeName:
        :param activationAttributes:
        :return:
        """
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
        """:param assemblyFile:
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
        """:param domain:
        :param assemblyFile:
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
        """:param assemblyFile:
        :param typeName:
        :param ignoreCase:
        :param bindingAttr:
        :param binder:
        :param args:
        :param culture:
        :param activationAttributes:
        :param securityInfo:
        :return:
        """
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
        """:param domain:
        :param assemblyFile:
        :param typeName:
        :param ignoreCase:
        :param bindingAttr:
        :param binder:
        :param args:
        :param culture:
        :param activationAttributes:
        :param securityAttributes:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @classmethod
    @overload
    def GetObject(cls, type: Type, url: str) -> object:
        """:param type:
        :param url:
        :return:
        """
    @classmethod
    @overload
    def GetObject(cls, type: Type, url: str, state: object) -> object:
        """:param type:
        :param url:
        :param state:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
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
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def ToString(self) -> str:
        """:return:"""

class AggregateException(Exception, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, innerExceptions: IEnumerable[Exception]):
        """:param innerExceptions:"""
    @overload
    def __init__(self, innerExceptions: Array[Exception]):
        """:param innerExceptions:"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerExceptions: IEnumerable[Exception]):
        """:param message:
        :param innerExceptions:
        """
    @overload
    def __init__(self, message: str, innerExceptions: Array[Exception]):
        """:param message:
        :param innerExceptions:
        """
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def InnerExceptions(self) -> ReadOnlyCollection[Exception]:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def Flatten(self) -> AggregateException:
        """:return:"""
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    def Handle(self, predicate: Func[Exception, bool]) -> None:
        """:param predicate:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class AppContext(ABC, Object):
    """"""

    @classmethod
    @property
    def BaseDirectory(cls) -> str:
        """:return:"""
    @classmethod
    @property
    def TargetFrameworkName(cls) -> str:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    def GetData(cls, name: str) -> object:
        """:param name:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def SetSwitch(cls, switchName: str, isEnabled: bool) -> None:
        """:param switchName:
        :param isEnabled:
        """
    def ToString(self) -> str:
        """:return:"""
    @classmethod
    def TryGetSwitch(cls, switchName: str, isEnabled: bool) -> Tuple[bool, bool]:
        """:param switchName:
        :param isEnabled:
        :return:
        """

class AppContextDefaultValues(ABC, Object):
    """"""

    @classmethod
    def PopulateDefaultValues(cls) -> None:
        """"""
    @classmethod
    def TryGetSwitchOverride(cls, switchName: str, overrideValue: bool) -> Tuple[bool, bool]:
        """:param switchName:
        :param overrideValue:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class AppContextSwitches(ABC, Object):
    """"""

    @classmethod
    @property
    def BlockLongPaths(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def DoNotAddrOfCspParentWindowHandle(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def DoNotMarshalOutByrefSafeArrayOnInvoke(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def EnforceJapaneseEraYearRanges(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def EnforceLegacyJapaneseDateParsing(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def FormatJapaneseFirstYearAsANumber(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def IgnorePortablePDBsInStackTraces(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def NoAsyncCurrentCulture(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def PreserveEventListnerObjectIdentity(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def SetActorAsReferenceWhenCopyingClaimsIdentity(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def ThrowExceptionIfDisposedCancellationTokenSource(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def UseConcurrentFormatterTypeCache(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def UseLegacyExecutionContextBehaviorUponUndoFailure(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def UseLegacyFipsThrow(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def UseLegacyPathHandling(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def UseNetCoreTimer(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def UseNewMaxArraySize(cls) -> bool:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class AppDomain(MarshalByRefObject, IEvidenceFactory, _AppDomain):
    """"""

    @property
    def ActivationContext(self) -> ActivationContext:
        """:return:"""
    @property
    def ApplicationIdentity(self) -> ApplicationIdentity:
        """:return:"""
    @property
    def ApplicationTrust(self) -> ApplicationTrust:
        """:return:"""
    @property
    def BaseDirectory(self) -> str:
        """:return:"""
    @classmethod
    @property
    def CurrentDomain(cls) -> AppDomain:
        """:return:"""
    @property
    def DomainManager(self) -> AppDomainManager:
        """:return:"""
    @property
    def DynamicDirectory(self) -> str:
        """:return:"""
    @property
    def Evidence(self) -> Evidence:
        """:return:"""
    @property
    def Evidence(self) -> Evidence:
        """:return:"""
    @property
    def FriendlyName(self) -> str:
        """:return:"""
    @property
    def Id(self) -> int:
        """:return:"""
    @property
    def IsFullyTrusted(self) -> bool:
        """:return:"""
    @property
    def IsHomogenous(self) -> bool:
        """:return:"""
    @classmethod
    @property
    def MonitoringIsEnabled(cls) -> bool:
        """:return:"""
    @classmethod
    @MonitoringIsEnabled.setter
    def MonitoringIsEnabled(cls, value: bool) -> None: ...
    @property
    def MonitoringSurvivedMemorySize(self) -> int:
        """:return:"""
    @classmethod
    @property
    def MonitoringSurvivedProcessMemorySize(cls) -> int:
        """:return:"""
    @property
    def MonitoringTotalAllocatedMemorySize(self) -> int:
        """:return:"""
    @property
    def MonitoringTotalProcessorTime(self) -> TimeSpan:
        """:return:"""
    @property
    def PermissionSet(self) -> PermissionSet:
        """:return:"""
    @property
    def RelativeSearchPath(self) -> str:
        """:return:"""
    @property
    def SetupInformation(self) -> AppDomainSetup:
        """:return:"""
    @property
    def ShadowCopyFiles(self) -> bool:
        """:return:"""
    def AppendPrivatePath(self, path: str) -> None:
        """:param path:"""
    def ApplyPolicy(self, assemblyName: str) -> str:
        """:param assemblyName:
        :return:
        """
    def ClearPrivatePath(self) -> None:
        """"""
    def ClearShadowCopyPath(self) -> None:
        """"""
    @overload
    def CreateComInstanceFrom(self, assemblyName: str, typeName: str) -> ObjectHandle:
        """:param assemblyName:
        :param typeName:
        :return:
        """
    @overload
    def CreateComInstanceFrom(
        self,
        assemblyFile: str,
        typeName: str,
        hashValue: Array[int],
        hashAlgorithm: AssemblyHashAlgorithm,
    ) -> ObjectHandle:
        """:param assemblyFile:
        :param typeName:
        :param hashValue:
        :param hashAlgorithm:
        :return:
        """
    @classmethod
    @overload
    def CreateDomain(cls, friendlyName: str) -> AppDomain:
        """:param friendlyName:
        :return:
        """
    @classmethod
    @overload
    def CreateDomain(cls, friendlyName: str, securityInfo: Evidence) -> AppDomain:
        """:param friendlyName:
        :param securityInfo:
        :return:
        """
    @classmethod
    @overload
    def CreateDomain(
        cls, friendlyName: str, securityInfo: Evidence, info: AppDomainSetup
    ) -> AppDomain:
        """:param friendlyName:
        :param securityInfo:
        :param info:
        :return:
        """
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
        """:param friendlyName:
        :param securityInfo:
        :param info:
        :param grantSet:
        :param fullTrustAssemblies:
        :return:
        """
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
        """:param friendlyName:
        :param securityInfo:
        :param appBasePath:
        :param appRelativeSearchPath:
        :param shadowCopyFiles:
        :return:
        """
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
        """:param friendlyName:
        :param securityInfo:
        :param appBasePath:
        :param appRelativeSearchPath:
        :param shadowCopyFiles:
        :param adInit:
        :param adInitArgs:
        :return:
        """
    @overload
    def CreateInstance(self, assemblyName: str, typeName: str) -> ObjectHandle:
        """:param assemblyName:
        :param typeName:
        :return:
        """
    @overload
    def CreateInstance(
        self, assemblyName: str, typeName: str, activationAttributes: Array[object]
    ) -> ObjectHandle:
        """:param assemblyName:
        :param typeName:
        :param activationAttributes:
        :return:
        """
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
        """:param assemblyName:
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
        """:param assemblyName:
        :param typeName:
        :param ignoreCase:
        :param bindingAttr:
        :param binder:
        :param args:
        :param culture:
        :param activationAttributes:
        :param securityAttributes:
        :return:
        """
    @overload
    def CreateInstanceAndUnwrap(self, assemblyName: str, typeName: str) -> object:
        """:param assemblyName:
        :param typeName:
        :return:
        """
    @overload
    def CreateInstanceAndUnwrap(
        self, assemblyName: str, typeName: str, activationAttributes: Array[object]
    ) -> object:
        """:param assemblyName:
        :param typeName:
        :param activationAttributes:
        :return:
        """
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
        """:param assemblyName:
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
        """:param assemblyName:
        :param typeName:
        :param ignoreCase:
        :param bindingAttr:
        :param binder:
        :param args:
        :param culture:
        :param activationAttributes:
        :param securityAttributes:
        :return:
        """
    @overload
    def CreateInstanceFrom(self, assemblyFile: str, typeName: str) -> ObjectHandle:
        """:param assemblyFile:
        :param typeName:
        :return:
        """
    @overload
    def CreateInstanceFrom(
        self, assemblyFile: str, typeName: str, activationAttributes: Array[object]
    ) -> ObjectHandle:
        """:param assemblyFile:
        :param typeName:
        :param activationAttributes:
        :return:
        """
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
        """:param assemblyFile:
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
        """:param assemblyFile:
        :param typeName:
        :param ignoreCase:
        :param bindingAttr:
        :param binder:
        :param args:
        :param culture:
        :param activationAttributes:
        :param securityAttributes:
        :return:
        """
    @overload
    def CreateInstanceFromAndUnwrap(self, assemblyName: str, typeName: str) -> object:
        """:param assemblyName:
        :param typeName:
        :return:
        """
    @overload
    def CreateInstanceFromAndUnwrap(
        self, assemblyName: str, typeName: str, activationAttributes: Array[object]
    ) -> object:
        """:param assemblyName:
        :param typeName:
        :param activationAttributes:
        :return:
        """
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
        """:param assemblyFile:
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
        """:param assemblyName:
        :param typeName:
        :param ignoreCase:
        :param bindingAttr:
        :param binder:
        :param args:
        :param culture:
        :param activationAttributes:
        :param securityAttributes:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """:param requestedType:
        :return:
        """
    @overload
    def DefineDynamicAssembly(
        self, name: AssemblyName, access: AssemblyBuilderAccess
    ) -> AssemblyBuilder:
        """:param name:
        :param access:
        :return:
        """
    @overload
    def DefineDynamicAssembly(
        self,
        name: AssemblyName,
        access: AssemblyBuilderAccess,
        assemblyAttributes: IEnumerable[CustomAttributeBuilder],
    ) -> AssemblyBuilder:
        """:param name:
        :param access:
        :param assemblyAttributes:
        :return:
        """
    @overload
    def DefineDynamicAssembly(
        self, name: AssemblyName, access: AssemblyBuilderAccess, evidence: Evidence
    ) -> AssemblyBuilder:
        """:param name:
        :param access:
        :param evidence:
        :return:
        """
    @overload
    def DefineDynamicAssembly(
        self, name: AssemblyName, access: AssemblyBuilderAccess, dir: str
    ) -> AssemblyBuilder:
        """:param name:
        :param access:
        :param dir:
        :return:
        """
    @overload
    def DefineDynamicAssembly(
        self,
        name: AssemblyName,
        access: AssemblyBuilderAccess,
        assemblyAttributes: IEnumerable[CustomAttributeBuilder],
        securityContextSource: SecurityContextSource,
    ) -> AssemblyBuilder:
        """:param name:
        :param access:
        :param assemblyAttributes:
        :param securityContextSource:
        :return:
        """
    @overload
    def DefineDynamicAssembly(
        self,
        name: AssemblyName,
        access: AssemblyBuilderAccess,
        dir: str,
        evidence: Evidence,
    ) -> AssemblyBuilder:
        """:param name:
        :param access:
        :param dir:
        :param evidence:
        :return:
        """
    @overload
    def DefineDynamicAssembly(
        self,
        name: AssemblyName,
        access: AssemblyBuilderAccess,
        requiredPermissions: PermissionSet,
        optionalPermissions: PermissionSet,
        refusedPermissions: PermissionSet,
    ) -> AssemblyBuilder:
        """:param name:
        :param access:
        :param requiredPermissions:
        :param optionalPermissions:
        :param refusedPermissions:
        :return:
        """
    @overload
    def DefineDynamicAssembly(
        self,
        name: AssemblyName,
        access: AssemblyBuilderAccess,
        dir: str,
        isSynchronized: bool,
        assemblyAttributes: IEnumerable[CustomAttributeBuilder],
    ) -> AssemblyBuilder:
        """:param name:
        :param access:
        :param dir:
        :param isSynchronized:
        :param assemblyAttributes:
        :return:
        """
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
        """:param name:
        :param access:
        :param evidence:
        :param requiredPermissions:
        :param optionalPermissions:
        :param refusedPermissions:
        :return:
        """
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
        """:param name:
        :param access:
        :param dir:
        :param requiredPermissions:
        :param optionalPermissions:
        :param refusedPermissions:
        :return:
        """
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
        """:param name:
        :param access:
        :param dir:
        :param evidence:
        :param requiredPermissions:
        :param optionalPermissions:
        :param refusedPermissions:
        :return:
        """
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
        """:param name:
        :param access:
        :param dir:
        :param evidence:
        :param requiredPermissions:
        :param optionalPermissions:
        :param refusedPermissions:
        :param isSynchronized:
        :return:
        """
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
        """:param name:
        :param access:
        :param dir:
        :param evidence:
        :param requiredPermissions:
        :param optionalPermissions:
        :param refusedPermissions:
        :param isSynchronized:
        :param assemblyAttributes:
        :return:
        """
    def DoCallBack(self, theDelegate: CrossAppDomainDelegate) -> None:
        """:param theDelegate:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """:param other:
        :return:
        """
    @overload
    def ExecuteAssembly(self, assemblyFile: str) -> int:
        """:param assemblyFile:
        :return:
        """
    @overload
    def ExecuteAssembly(self, assemblyFile: str, assemblySecurity: Evidence) -> int:
        """:param assemblyFile:
        :param assemblySecurity:
        :return:
        """
    @overload
    def ExecuteAssembly(self, assemblyFile: str, args: Array[str]) -> int:
        """:param assemblyFile:
        :param args:
        :return:
        """
    @overload
    def ExecuteAssembly(
        self, assemblyFile: str, assemblySecurity: Evidence, args: Array[str]
    ) -> int:
        """:param assemblyFile:
        :param assemblySecurity:
        :param args:
        :return:
        """
    @overload
    def ExecuteAssembly(
        self,
        assemblyFile: str,
        args: Array[str],
        hashValue: Array[int],
        hashAlgorithm: AssemblyHashAlgorithm,
    ) -> int:
        """:param assemblyFile:
        :param args:
        :param hashValue:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def ExecuteAssembly(
        self,
        assemblyFile: str,
        assemblySecurity: Evidence,
        args: Array[str],
        hashValue: Array[int],
        hashAlgorithm: AssemblyHashAlgorithm,
    ) -> int:
        """:param assemblyFile:
        :param assemblySecurity:
        :param args:
        :param hashValue:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def ExecuteAssemblyByName(self, assemblyName: str) -> int:
        """:param assemblyName:
        :return:
        """
    @overload
    def ExecuteAssemblyByName(self, assemblyName: AssemblyName, args: Array[str]) -> int:
        """:param assemblyName:
        :param args:
        :return:
        """
    @overload
    def ExecuteAssemblyByName(self, assemblyName: str, assemblySecurity: Evidence) -> int:
        """:param assemblyName:
        :param assemblySecurity:
        :return:
        """
    @overload
    def ExecuteAssemblyByName(self, assemblyName: str, args: Array[str]) -> int:
        """:param assemblyName:
        :param args:
        :return:
        """
    @overload
    def ExecuteAssemblyByName(
        self, assemblyName: AssemblyName, assemblySecurity: Evidence, args: Array[str]
    ) -> int:
        """:param assemblyName:
        :param assemblySecurity:
        :param args:
        :return:
        """
    @overload
    def ExecuteAssemblyByName(
        self, assemblyName: str, assemblySecurity: Evidence, args: Array[str]
    ) -> int:
        """:param assemblyName:
        :param assemblySecurity:
        :param args:
        :return:
        """
    def GetAssemblies(self) -> Array[Assembly]:
        """:return:"""
    @classmethod
    def GetCurrentThreadId(cls) -> int:
        """:return:"""
    def GetData(self, name: str) -> object:
        """:param name:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetLifetimeService(self) -> object:
        """:return:"""
    @overload
    def GetLifetimeService(self) -> object:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
    @overload
    def InitializeLifetimeService(self) -> object:
        """:return:"""
    @overload
    def InitializeLifetimeService(self) -> object:
        """:return:"""
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
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsCompatibilitySwitchSet(self, value: str) -> bool | None:
        """:param value:
        :return:
        """
    def IsDefaultAppDomain(self) -> bool:
        """:return:"""
    def IsFinalizingForUnload(self) -> bool:
        """:return:"""
    @overload
    def Load(self, assemblyRef: AssemblyName) -> Assembly:
        """:param assemblyRef:
        :return:
        """
    @overload
    def Load(self, rawAssembly: Array[int]) -> Assembly:
        """:param rawAssembly:
        :return:
        """
    @overload
    def Load(self, assemblyString: str) -> Assembly:
        """:param assemblyString:
        :return:
        """
    @overload
    def Load(self, assemblyRef: AssemblyName, assemblySecurity: Evidence) -> Assembly:
        """:param assemblyRef:
        :param assemblySecurity:
        :return:
        """
    @overload
    def Load(self, rawAssembly: Array[int], rawSymbolStore: Array[int]) -> Assembly:
        """:param rawAssembly:
        :param rawSymbolStore:
        :return:
        """
    @overload
    def Load(self, assemblyString: str, assemblySecurity: Evidence) -> Assembly:
        """:param assemblyString:
        :param assemblySecurity:
        :return:
        """
    @overload
    def Load(
        self,
        rawAssembly: Array[int],
        rawSymbolStore: Array[int],
        securityEvidence: Evidence,
    ) -> Assembly:
        """:param rawAssembly:
        :param rawSymbolStore:
        :param securityEvidence:
        :return:
        """
    def ReflectionOnlyGetAssemblies(self) -> Array[Assembly]:
        """:return:"""
    def SetAppDomainPolicy(self, domainPolicy: PolicyLevel) -> None:
        """:param domainPolicy:"""
    def SetCachePath(self, s: str) -> None:
        """:param s:"""
    @overload
    def SetData(self, name: str, data: object) -> None:
        """:param name:
        :param data:
        """
    @overload
    def SetData(self, name: str, data: object, permission: IPermission) -> None:
        """:param name:
        :param data:
        :param permission:
        """
    def SetDynamicBase(self, path: str) -> None:
        """:param path:"""
    def SetPrincipalPolicy(self, policy: PrincipalPolicy) -> None:
        """:param policy:"""
    def SetShadowCopyFiles(self) -> None:
        """"""
    def SetShadowCopyPath(self, s: str) -> None:
        """:param s:"""
    def SetThreadPrincipal(self, principal: IPrincipal) -> None:
        """:param principal:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @classmethod
    def Unload(cls, domain: AppDomain) -> None:
        """:param domain:"""
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
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

AppDomainInitializer: Callable[[Array[str]], None] = ...
"""

:param args: 
"""

class AppDomainInitializerInfo(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class AppDomainManager(MarshalByRefObject):
    """"""

    def __init__(self):
        """"""
    @property
    def ApplicationActivator(self) -> ApplicationActivator:
        """:return:"""
    @property
    def EntryAssembly(self) -> Assembly:
        """:return:"""
    @property
    def HostExecutionContextManager(self) -> HostExecutionContextManager:
        """:return:"""
    @property
    def HostSecurityManager(self) -> HostSecurityManager:
        """:return:"""
    @property
    def InitializationFlags(self) -> AppDomainManagerInitializationOptions:
        """:return:"""
    @InitializationFlags.setter
    def InitializationFlags(self, value: AppDomainManagerInitializationOptions) -> None: ...
    def CheckSecuritySettings(self, state: SecurityState) -> bool:
        """:param state:
        :return:
        """
    def CreateDomain(
        self, friendlyName: str, securityInfo: Evidence, appDomainInfo: AppDomainSetup
    ) -> AppDomain:
        """:param friendlyName:
        :param securityInfo:
        :param appDomainInfo:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """:param requestedType:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetLifetimeService(self) -> object:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def InitializeLifetimeService(self) -> object:
        """:return:"""
    def InitializeNewDomain(self, appDomainInfo: AppDomainSetup) -> None:
        """:param appDomainInfo:"""
    def ToString(self) -> str:
        """:return:"""

class AppDomainManagerInitializationOptions(Enum):
    """"""

    _None: AppDomainManagerInitializationOptions = ...
    """"""
    RegisterWithHost: AppDomainManagerInitializationOptions = ...
    """"""

class AppDomainPauseManager(Object):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def Paused(self) -> None:
        """"""
    def Pausing(self) -> None:
        """"""
    def Resumed(self) -> None:
        """"""
    def Resuming(self) -> None:
        """"""
    def ToString(self) -> str:
        """:return:"""

class AppDomainSetup(Object, IAppDomainSetup):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, activationArguments: ActivationArguments):
        """:param activationArguments:"""
    @overload
    def __init__(self, activationContext: ActivationContext):
        """:param activationContext:"""
    @property
    def ActivationArguments(self) -> ActivationArguments:
        """:return:"""
    @ActivationArguments.setter
    def ActivationArguments(self, value: ActivationArguments) -> None: ...
    @property
    def AppDomainInitializer(self) -> AppDomainInitializer:
        """:return:"""
    @AppDomainInitializer.setter
    def AppDomainInitializer(self, value: AppDomainInitializer) -> None: ...
    @property
    def AppDomainInitializerArguments(self) -> Array[str]:
        """:return:"""
    @AppDomainInitializerArguments.setter
    def AppDomainInitializerArguments(self, value: Array[str]) -> None: ...
    @property
    def AppDomainManagerAssembly(self) -> str:
        """:return:"""
    @AppDomainManagerAssembly.setter
    def AppDomainManagerAssembly(self, value: str) -> None: ...
    @property
    def AppDomainManagerType(self) -> str:
        """:return:"""
    @AppDomainManagerType.setter
    def AppDomainManagerType(self, value: str) -> None: ...
    @property
    def ApplicationBase(self) -> str:
        """:return:"""
    @ApplicationBase.setter
    def ApplicationBase(self, value: str) -> None: ...
    @property
    def ApplicationName(self) -> str:
        """:return:"""
    @ApplicationName.setter
    def ApplicationName(self, value: str) -> None: ...
    @property
    def ApplicationTrust(self) -> ApplicationTrust:
        """:return:"""
    @ApplicationTrust.setter
    def ApplicationTrust(self, value: ApplicationTrust) -> None: ...
    @property
    def CachePath(self) -> str:
        """:return:"""
    @CachePath.setter
    def CachePath(self, value: str) -> None: ...
    @property
    def ConfigurationFile(self) -> str:
        """:return:"""
    @ConfigurationFile.setter
    def ConfigurationFile(self, value: str) -> None: ...
    @property
    def DisallowApplicationBaseProbing(self) -> bool:
        """:return:"""
    @DisallowApplicationBaseProbing.setter
    def DisallowApplicationBaseProbing(self, value: bool) -> None: ...
    @property
    def DisallowBindingRedirects(self) -> bool:
        """:return:"""
    @DisallowBindingRedirects.setter
    def DisallowBindingRedirects(self, value: bool) -> None: ...
    @property
    def DisallowCodeDownload(self) -> bool:
        """:return:"""
    @DisallowCodeDownload.setter
    def DisallowCodeDownload(self, value: bool) -> None: ...
    @property
    def DisallowPublisherPolicy(self) -> bool:
        """:return:"""
    @DisallowPublisherPolicy.setter
    def DisallowPublisherPolicy(self, value: bool) -> None: ...
    @property
    def DynamicBase(self) -> str:
        """:return:"""
    @DynamicBase.setter
    def DynamicBase(self, value: str) -> None: ...
    @property
    def LicenseFile(self) -> str:
        """:return:"""
    @LicenseFile.setter
    def LicenseFile(self, value: str) -> None: ...
    @property
    def LoaderOptimization(self) -> LoaderOptimization:
        """:return:"""
    @LoaderOptimization.setter
    def LoaderOptimization(self, value: LoaderOptimization) -> None: ...
    @property
    def PartialTrustVisibleAssemblies(self) -> Array[str]:
        """:return:"""
    @PartialTrustVisibleAssemblies.setter
    def PartialTrustVisibleAssemblies(self, value: Array[str]) -> None: ...
    @property
    def PrivateBinPath(self) -> str:
        """:return:"""
    @PrivateBinPath.setter
    def PrivateBinPath(self, value: str) -> None: ...
    @property
    def PrivateBinPathProbe(self) -> str:
        """:return:"""
    @PrivateBinPathProbe.setter
    def PrivateBinPathProbe(self, value: str) -> None: ...
    @property
    def SandboxInterop(self) -> bool:
        """:return:"""
    @SandboxInterop.setter
    def SandboxInterop(self, value: bool) -> None: ...
    @property
    def ShadowCopyDirectories(self) -> str:
        """:return:"""
    @ShadowCopyDirectories.setter
    def ShadowCopyDirectories(self, value: str) -> None: ...
    @property
    def ShadowCopyFiles(self) -> str:
        """:return:"""
    @ShadowCopyFiles.setter
    def ShadowCopyFiles(self, value: str) -> None: ...
    @property
    def TargetFrameworkName(self) -> str:
        """:return:"""
    @TargetFrameworkName.setter
    def TargetFrameworkName(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetConfigurationBytes(self) -> Array[int]:
        """:return:"""
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def SetCompatibilitySwitches(self, switches: IEnumerable[str]) -> None:
        """:param switches:"""
    def SetConfigurationBytes(self, value: Array[int]) -> None:
        """:param value:"""
    def SetNativeFunction(
        self, functionName: str, functionVersion: int, functionPointer: IntPtr
    ) -> None:
        """:param functionName:
        :param functionVersion:
        :param functionPointer:
        """
    def ToString(self) -> str:
        """:return:"""

class AppDomainUnloadedException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class ApplicationException(Exception, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class ApplicationId(Object):
    """"""

    def __init__(
        self,
        publicKeyToken: Array[int],
        name: str,
        version: Version,
        processorArchitecture: str,
        culture: str,
    ):
        """:param publicKeyToken:
        :param name:
        :param version:
        :param processorArchitecture:
        :param culture:
        """
    @property
    def Culture(self) -> str:
        """:return:"""
    @property
    def Name(self) -> str:
        """:return:"""
    @property
    def ProcessorArchitecture(self) -> str:
        """:return:"""
    @property
    def PublicKeyToken(self) -> Array[int]:
        """:return:"""
    @property
    def Version(self) -> Version:
        """:return:"""
    def Copy(self) -> ApplicationId:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class ApplicationIdentity(Object, ISerializable):
    """"""

    def __init__(self, applicationIdentityFullName: str):
        """:param applicationIdentityFullName:"""
    @property
    def CodeBase(self) -> str:
        """:return:"""
    @property
    def FullName(self) -> str:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class ArgIterator(ValueType):
    """"""

    @overload
    def __init__(self, arglist: RuntimeArgumentHandle):
        """:param arglist:"""
    @overload
    def __init__(self, arglist: RuntimeArgumentHandle, ptr: None):
        """:param arglist:
        :param ptr:
        """
    def End(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetNextArg(self) -> TypedReference:
        """:return:"""
    @overload
    def GetNextArg(self, rth: RuntimeTypeHandle) -> TypedReference:
        """:param rth:
        :return:
        """
    def GetNextArgType(self) -> RuntimeTypeHandle:
        """:return:"""
    def GetRemainingCount(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class ArgumentException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @overload
    def __init__(self, message: str, paramName: str):
        """:param message:
        :param paramName:
        """
    @overload
    def __init__(self, message: str, paramName: str, innerException: Exception):
        """:param message:
        :param paramName:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def ParamName(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class ArgumentNullException(ArgumentException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, paramName: str):
        """:param paramName:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @overload
    def __init__(self, paramName: str, message: str):
        """:param paramName:
        :param message:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def ParamName(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class ArgumentOutOfRangeException(ArgumentException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, paramName: str):
        """:param paramName:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @overload
    def __init__(self, paramName: str, message: str):
        """:param paramName:
        :param message:
        """
    @overload
    def __init__(self, paramName: str, actualValue: object, message: str):
        """:param paramName:
        :param actualValue:
        :param message:
        """
    @property
    def ActualValue(self) -> object:
        """:return:"""
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def ParamName(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class ArithmeticException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class Array(
    Generic[T],
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
        """:return:"""
    @property
    def IsFixedSize(self) -> bool:
        """:return:"""
    @property
    def IsReadOnly(self) -> bool:
        """:return:"""
    @property
    def IsSynchronized(self) -> bool:
        """:return:"""
    @property
    def Item(self) -> T:
        """:return:"""
    @Item.setter
    def Item(self, value: T) -> None: ...
    @property
    def Length(self) -> int:
        """:return:"""
    @property
    def LongLength(self) -> int:
        """:return:"""
    @property
    def Rank(self) -> int:
        """:return:"""
    @property
    def SyncRoot(self) -> object:
        """:return:"""
    def Add(self, value: T) -> int:
        """:param value:
        :return:
        """
    @classmethod
    def AsReadOnly(cls, array: Array[T]) -> ReadOnlyCollection[T]:
        """:param array:
        :return:
        """
    @classmethod
    @overload
    def BinarySearch(cls, array: Array, value: object) -> int:
        """:param array:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def BinarySearch(cls, array: Array[T], value: T) -> int:
        """:param array:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def BinarySearch(cls, array: Array, value: object, comparer: IComparer) -> int:
        """:param array:
        :param value:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def BinarySearch(cls, array: Array[T], value: T, comparer: IComparer[T]) -> int:
        """:param array:
        :param value:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def BinarySearch(cls, array: Array, index: int, length: int, value: object) -> int:
        """:param array:
        :param index:
        :param length:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def BinarySearch(cls, array: Array[T], index: int, length: int, value: T) -> int:
        """:param array:
        :param index:
        :param length:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def BinarySearch(
        cls, array: Array, index: int, length: int, value: object, comparer: IComparer
    ) -> int:
        """:param array:
        :param index:
        :param length:
        :param value:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def BinarySearch(
        cls, array: Array[T], index: int, length: int, value: T, comparer: IComparer[T]
    ) -> int:
        """:param array:
        :param index:
        :param length:
        :param value:
        :param comparer:
        :return:
        """
    @overload
    def Clear(self) -> None:
        """"""
    @classmethod
    @overload
    def Clear(cls, array: Array, index: int, length: int) -> None:
        """:param array:
        :param index:
        :param length:
        """
    def Clone(self) -> object:
        """:return:"""
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """:param other:
        :param comparer:
        :return:
        """
    @classmethod
    def ConstrainedCopy(
        cls,
        sourceArray: Array,
        sourceIndex: int,
        destinationArray: Array,
        destinationIndex: int,
        length: int,
    ) -> None:
        """:param sourceArray:
        :param sourceIndex:
        :param destinationArray:
        :param destinationIndex:
        :param length:
        """
    def Contains(self, value: T) -> bool:
        """:param value:
        :return:
        """
    @classmethod
    def ConvertAll(
        cls, array: Array[TInput], converter: Converter[TInput, TOutput]
    ) -> Array[TOutput]:
        """:param array:
        :param converter:
        :return:
        """
    @classmethod
    @overload
    def Copy(cls, sourceArray: Array, destinationArray: Array, length: int) -> None:
        """:param sourceArray:
        :param destinationArray:
        :param length:
        """
    @classmethod
    @overload
    def Copy(cls, sourceArray: Array, destinationArray: Array, length: int) -> None:
        """:param sourceArray:
        :param destinationArray:
        :param length:
        """
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
        """:param sourceArray:
        :param sourceIndex:
        :param destinationArray:
        :param destinationIndex:
        :param length:
        """
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
        """:param sourceArray:
        :param sourceIndex:
        :param destinationArray:
        :param destinationIndex:
        :param length:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """:param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """:param array:
        :param index:
        """
    @classmethod
    @overload
    def CreateInstance(cls, elementType: Type, lengths: Array[int]) -> Array:
        """:param elementType:
        :param lengths:
        :return:
        """
    @classmethod
    @overload
    def CreateInstance(cls, elementType: Type, lengths: Array[int]) -> Array:
        """:param elementType:
        :param lengths:
        :return:
        """
    @classmethod
    @overload
    def CreateInstance(cls, elementType: Type, length: int) -> Array:
        """:param elementType:
        :param length:
        :return:
        """
    @classmethod
    @overload
    def CreateInstance(
        cls, elementType: Type, lengths: Array[int], lowerBounds: Array[int]
    ) -> Array:
        """:param elementType:
        :param lengths:
        :param lowerBounds:
        :return:
        """
    @classmethod
    @overload
    def CreateInstance(cls, elementType: Type, length1: int, length2: int) -> Array:
        """:param elementType:
        :param length1:
        :param length2:
        :return:
        """
    @classmethod
    @overload
    def CreateInstance(cls, elementType: Type, length1: int, length2: int, length3: int) -> Array:
        """:param elementType:
        :param length1:
        :param length2:
        :param length3:
        :return:
        """
    @classmethod
    def Empty(cls) -> Array[T]:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """:param other:
        :param comparer:
        :return:
        """
    @classmethod
    def Exists(cls, array: Array[T], match: Predicate[T]) -> bool:
        """:param array:
        :param match:
        :return:
        """
    @classmethod
    def Find(cls, array: Array[T], match: Predicate[T]) -> T:
        """:param array:
        :param match:
        :return:
        """
    @classmethod
    def FindAll(cls, array: Array[T], match: Predicate[T]) -> Array[T]:
        """:param array:
        :param match:
        :return:
        """
    @classmethod
    @overload
    def FindIndex(cls, array: Array[T], match: Predicate[T]) -> int:
        """:param array:
        :param match:
        :return:
        """
    @classmethod
    @overload
    def FindIndex(cls, array: Array[T], startIndex: int, match: Predicate[T]) -> int:
        """:param array:
        :param startIndex:
        :param match:
        :return:
        """
    @classmethod
    @overload
    def FindIndex(cls, array: Array[T], startIndex: int, count: int, match: Predicate[T]) -> int:
        """:param array:
        :param startIndex:
        :param count:
        :param match:
        :return:
        """
    @classmethod
    def FindLast(cls, array: Array[T], match: Predicate[T]) -> T:
        """:param array:
        :param match:
        :return:
        """
    @classmethod
    @overload
    def FindLastIndex(cls, array: Array[T], match: Predicate[T]) -> int:
        """:param array:
        :param match:
        :return:
        """
    @classmethod
    @overload
    def FindLastIndex(cls, array: Array[T], startIndex: int, match: Predicate[T]) -> int:
        """:param array:
        :param startIndex:
        :param match:
        :return:
        """
    @classmethod
    @overload
    def FindLastIndex(
        cls, array: Array[T], startIndex: int, count: int, match: Predicate[T]
    ) -> int:
        """:param array:
        :param startIndex:
        :param count:
        :param match:
        :return:
        """
    @classmethod
    def ForEach(cls, array: Array[T], action: Action[T]) -> None:
        """:param array:
        :param action:
        """
    def GetEnumerator(self) -> IEnumerator:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    def GetLength(self, dimension: int) -> int:
        """:param dimension:
        :return:
        """
    def GetLongLength(self, dimension: int) -> int:
        """:param dimension:
        :return:
        """
    def GetLowerBound(self, dimension: int) -> int:
        """:param dimension:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetUpperBound(self, dimension: int) -> int:
        """:param dimension:
        :return:
        """
    @overload
    def GetValue(self, indices: Array[int]) -> T:
        """:param indices:
        :return:
        """
    @overload
    def GetValue(self, indices: Array[int]) -> T:
        """:param indices:
        :return:
        """
    @overload
    def GetValue(self, index: int) -> T:
        """:param index:
        :return:
        """
    @overload
    def GetValue(self, index: int) -> T:
        """:param index:
        :return:
        """
    @overload
    def GetValue(self, index1: int, index2: int) -> T:
        """:param index1:
        :param index2:
        :return:
        """
    @overload
    def GetValue(self, index1: int, index2: int) -> T:
        """:param index1:
        :param index2:
        :return:
        """
    @overload
    def GetValue(self, index1: int, index2: int, index3: int) -> T:
        """:param index1:
        :param index2:
        :param index3:
        :return:
        """
    @overload
    def GetValue(self, index1: int, index2: int, index3: int) -> T:
        """:param index1:
        :param index2:
        :param index3:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def IndexOf(cls, array: Array, value: object) -> int:
        """:param array:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def IndexOf(cls, array: Array[T], value: T) -> int:
        """:param array:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def IndexOf(cls, array: Array, value: object, startIndex: int) -> int:
        """:param array:
        :param value:
        :param startIndex:
        :return:
        """
    @classmethod
    @overload
    def IndexOf(cls, array: Array[T], value: T, startIndex: int) -> int:
        """:param array:
        :param value:
        :param startIndex:
        :return:
        """
    @classmethod
    @overload
    def IndexOf(cls, array: Array, value: object, startIndex: int, count: int) -> int:
        """:param array:
        :param value:
        :param startIndex:
        :param count:
        :return:
        """
    @classmethod
    @overload
    def IndexOf(cls, array: Array[T], value: T, startIndex: int, count: int) -> int:
        """:param array:
        :param value:
        :param startIndex:
        :param count:
        :return:
        """
    def Initialize(self) -> None:
        """"""
    def Insert(self, index: int, value: T) -> None:
        """:param index:
        :param value:
        """
    @classmethod
    @overload
    def LastIndexOf(cls, array: Array, value: object) -> int:
        """:param array:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def LastIndexOf(cls, array: Array[T], value: T) -> int:
        """:param array:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def LastIndexOf(cls, array: Array, value: object, startIndex: int) -> int:
        """:param array:
        :param value:
        :param startIndex:
        :return:
        """
    @classmethod
    @overload
    def LastIndexOf(cls, array: Array[T], value: T, startIndex: int) -> int:
        """:param array:
        :param value:
        :param startIndex:
        :return:
        """
    @classmethod
    @overload
    def LastIndexOf(cls, array: Array, value: object, startIndex: int, count: int) -> int:
        """:param array:
        :param value:
        :param startIndex:
        :param count:
        :return:
        """
    @classmethod
    @overload
    def LastIndexOf(cls, array: Array[T], value: T, startIndex: int, count: int) -> int:
        """:param array:
        :param value:
        :param startIndex:
        :param count:
        :return:
        """
    def Remove(self, value: T) -> None:
        """:param value:"""
    def RemoveAt(self, index: int) -> None:
        """:param index:"""
    @classmethod
    def Resize(cls, array: T, newSize: int) -> None:
        """:param array:
        :param newSize:
        """
    @classmethod
    @overload
    def Reverse(cls, array: Array) -> None:
        """:param array:"""
    @classmethod
    @overload
    def Reverse(cls, array: Array, index: int, length: int) -> None:
        """:param array:
        :param index:
        :param length:
        """
    @overload
    def SetValue(self, value: T, indices: Array[int]) -> None:
        """:param value:
        :param indices:
        """
    @overload
    def SetValue(self, value: T, indices: Array[int]) -> None:
        """:param value:
        :param indices:
        """
    @overload
    def SetValue(self, value: T, index: int) -> None:
        """:param value:
        :param index:
        """
    @overload
    def SetValue(self, value: T, index: int) -> None:
        """:param value:
        :param index:
        """
    @overload
    def SetValue(self, value: T, index1: int, index2: int) -> None:
        """:param value:
        :param index1:
        :param index2:
        """
    @overload
    def SetValue(self, value: T, index1: int, index2: int) -> None:
        """:param value:
        :param index1:
        :param index2:
        """
    @overload
    def SetValue(self, value: T, index1: int, index2: int, index3: int) -> None:
        """:param value:
        :param index1:
        :param index2:
        :param index3:
        """
    @overload
    def SetValue(self, value: T, index1: int, index2: int, index3: int) -> None:
        """:param value:
        :param index1:
        :param index2:
        :param index3:
        """
    @classmethod
    @overload
    def Sort(cls, array: Array) -> None:
        """:param array:"""
    @classmethod
    @overload
    def Sort(cls, array: Array[T]) -> None:
        """:param array:"""
    @classmethod
    @overload
    def Sort(cls, array: Array, comparer: IComparer) -> None:
        """:param array:
        :param comparer:
        """
    @classmethod
    @overload
    def Sort(cls, keys: Array, items: Array) -> None:
        """:param keys:
        :param items:
        """
    @classmethod
    @overload
    def Sort(cls, keys: Array[TKey], items: Array[TValue]) -> None:
        """:param keys:
        :param items:
        """
    @classmethod
    @overload
    def Sort(cls, array: Array[T], comparer: IComparer[T]) -> None:
        """:param array:
        :param comparer:
        """
    @classmethod
    @overload
    def Sort(cls, array: Array[T], comparison: Comparison[T]) -> None:
        """:param array:
        :param comparison:
        """
    @classmethod
    @overload
    def Sort(cls, keys: Array, items: Array, comparer: IComparer) -> None:
        """:param keys:
        :param items:
        :param comparer:
        """
    @classmethod
    @overload
    def Sort(cls, array: Array, index: int, length: int) -> None:
        """:param array:
        :param index:
        :param length:
        """
    @classmethod
    @overload
    def Sort(cls, keys: Array[TKey], items: Array[TValue], comparer: IComparer[TKey]) -> None:
        """:param keys:
        :param items:
        :param comparer:
        """
    @classmethod
    @overload
    def Sort(cls, array: Array[T], index: int, length: int) -> None:
        """:param array:
        :param index:
        :param length:
        """
    @classmethod
    @overload
    def Sort(cls, keys: Array, items: Array, index: int, length: int) -> None:
        """:param keys:
        :param items:
        :param index:
        :param length:
        """
    @classmethod
    @overload
    def Sort(cls, array: Array, index: int, length: int, comparer: IComparer) -> None:
        """:param array:
        :param index:
        :param length:
        :param comparer:
        """
    @classmethod
    @overload
    def Sort(cls, keys: Array[TKey], items: Array[TValue], index: int, length: int) -> None:
        """:param keys:
        :param items:
        :param index:
        :param length:
        """
    @classmethod
    @overload
    def Sort(cls, array: Array[T], index: int, length: int, comparer: IComparer[T]) -> None:
        """:param array:
        :param index:
        :param length:
        :param comparer:
        """
    @classmethod
    @overload
    def Sort(cls, keys: Array, items: Array, index: int, length: int, comparer: IComparer) -> None:
        """:param keys:
        :param items:
        :param index:
        :param length:
        :param comparer:
        """
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
        """:param keys:
        :param items:
        :param index:
        :param length:
        :param comparer:
        """
    def ToString(self) -> str:
        """:return:"""
    @classmethod
    def TrueForAll(cls, array: Array[T], match: Predicate[T]) -> bool:
        """:param array:
        :param match:
        :return:
        """
    def __contains__(self, value: T) -> bool:
        """:param value:
        :return:
        """
    def __getitem__(self, index: int) -> T:
        """:param index:
        :return:
        """
    def __iter__(self) -> Iterator[T]:
        """:return:"""
    def __len__(self) -> int:
        """:return:"""
    def __setitem__(self, index: int, value: T) -> None:
        """:param index:
        :param value:
        """

class ArraySegment(
    Generic[T],
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
    def __init__(self, array: Array[T]):
        """:param array:"""
    @overload
    def __init__(self, array: Array[T], offset: int, count: int):
        """:param array:
        :param offset:
        :param count:
        """
    @property
    def Array(self) -> Array[T]:
        """:return:"""
    @property
    def Count(self) -> int:
        """:return:"""
    @property
    def Count(self) -> int:
        """:return:"""
    @property
    def IsReadOnly(self) -> bool:
        """:return:"""
    @property
    def Item(self) -> T:
        """:return:"""
    @Item.setter
    def Item(self, value: T) -> None: ...
    @property
    def Item(self) -> T:
        """:return:"""
    @property
    def Offset(self) -> int:
        """:return:"""
    def Add(self, item: T) -> None:
        """:param item:"""
    def Clear(self) -> None:
        """"""
    def Contains(self, item: T) -> bool:
        """:param item:
        :return:
        """
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """"""
    @overload
    def Equals(self, obj: ArraySegment[T]) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """:return:"""
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def IndexOf(self, item: T) -> int:
        """:param item:
        :return:
        """
    def Insert(self, index: int, item: T) -> None:
        """:param index:
        :param item:
        """
    def Remove(self, item: T) -> bool:
        """:param item:
        :return:
        """
    def RemoveAt(self, index: int) -> None:
        """:param index:"""
    def ToString(self) -> str:
        """:return:"""
    def __contains__(self, value: T) -> bool:
        """:param value:
        :return:
        """
    def __eq__(self, other: ArraySegment[T]) -> bool:
        """:param other:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> T:
        """:param index:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> T:
        """:param index:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """:return:"""
    @overload
    def __iter__(self) -> Iterator[T]:
        """:return:"""
    def __len__(self) -> int:
        """:return:"""
    def __ne__(self, other: ArraySegment[T]) -> bool:
        """:param other:
        :return:
        """
    def __setitem__(self, index: int, value: T) -> None:
        """:param index:
        :param value:
        """
    @classmethod
    def op_Equality(cls, a: ArraySegment[T], b: ArraySegment[T]) -> bool:
        """:param a:
        :param b:
        :return:
        """
    @classmethod
    def op_Inequality(cls, a: ArraySegment[T], b: ArraySegment[T]) -> bool:
        """:param a:
        :param b:
        :return:
        """

class ArrayTypeMismatchException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class AssemblyLoadEventArgs(EventArgs):
    """"""

    def __init__(self, loadedAssembly: Assembly):
        """:param loadedAssembly:"""
    @property
    def LoadedAssembly(self) -> Assembly:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

AssemblyLoadEventHandler: Callable[[object, AssemblyLoadEventArgs], None] = ...
"""

:param sender: 
:param args: 
"""
AsyncCallback: Callable[[IAsyncResult], None] = ...
"""

:param ar: 
"""

class Attribute(ABC, Object, _Attribute):
    """"""

    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttribute(cls, element: Assembly, attributeType: Type) -> Attribute:
        """:param element:
        :param attributeType:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttribute(cls, element: MemberInfo, attributeType: Type) -> Attribute:
        """:param element:
        :param attributeType:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttribute(cls, element: Module, attributeType: Type) -> Attribute:
        """:param element:
        :param attributeType:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttribute(cls, element: ParameterInfo, attributeType: Type) -> Attribute:
        """:param element:
        :param attributeType:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttribute(cls, element: Assembly, attributeType: Type, inherit: bool) -> Attribute:
        """:param element:
        :param attributeType:
        :param inherit:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttribute(
        cls, element: MemberInfo, attributeType: Type, inherit: bool
    ) -> Attribute:
        """:param element:
        :param attributeType:
        :param inherit:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttribute(cls, element: Module, attributeType: Type, inherit: bool) -> Attribute:
        """:param element:
        :param attributeType:
        :param inherit:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttribute(
        cls, element: ParameterInfo, attributeType: Type, inherit: bool
    ) -> Attribute:
        """:param element:
        :param attributeType:
        :param inherit:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: Assembly) -> Array[Attribute]:
        """:param element:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: MemberInfo) -> Array[Attribute]:
        """:param element:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: Module) -> Array[Attribute]:
        """:param element:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: ParameterInfo) -> Array[Attribute]:
        """:param element:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: Assembly, inherit: bool) -> Array[Attribute]:
        """:param element:
        :param inherit:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: Assembly, attributeType: Type) -> Array[Attribute]:
        """:param element:
        :param attributeType:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: MemberInfo, inherit: bool) -> Array[Attribute]:
        """:param element:
        :param inherit:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: MemberInfo, type: Type) -> Array[Attribute]:
        """:param element:
        :param type:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: Module, inherit: bool) -> Array[Attribute]:
        """:param element:
        :param inherit:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: Module, attributeType: Type) -> Array[Attribute]:
        """:param element:
        :param attributeType:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: ParameterInfo, inherit: bool) -> Array[Attribute]:
        """:param element:
        :param inherit:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: ParameterInfo, attributeType: Type) -> Array[Attribute]:
        """:param element:
        :param attributeType:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(
        cls, element: Assembly, attributeType: Type, inherit: bool
    ) -> Array[Attribute]:
        """:param element:
        :param attributeType:
        :param inherit:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(
        cls, element: MemberInfo, type: Type, inherit: bool
    ) -> Array[Attribute]:
        """:param element:
        :param type:
        :param inherit:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(
        cls, element: Module, attributeType: Type, inherit: bool
    ) -> Array[Attribute]:
        """:param element:
        :param attributeType:
        :param inherit:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(
        cls, element: ParameterInfo, attributeType: Type, inherit: bool
    ) -> Array[Attribute]:
        """:param element:
        :param attributeType:
        :param inherit:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
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
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    @classmethod
    @overload
    def IsDefined(cls, element: Assembly, attributeType: Type) -> bool:
        """:param element:
        :param attributeType:
        :return:
        """
    @classmethod
    @overload
    def IsDefined(cls, element: MemberInfo, attributeType: Type) -> bool:
        """:param element:
        :param attributeType:
        :return:
        """
    @classmethod
    @overload
    def IsDefined(cls, element: Module, attributeType: Type) -> bool:
        """:param element:
        :param attributeType:
        :return:
        """
    @classmethod
    @overload
    def IsDefined(cls, element: ParameterInfo, attributeType: Type) -> bool:
        """:param element:
        :param attributeType:
        :return:
        """
    @classmethod
    @overload
    def IsDefined(cls, element: Assembly, attributeType: Type, inherit: bool) -> bool:
        """:param element:
        :param attributeType:
        :param inherit:
        :return:
        """
    @classmethod
    @overload
    def IsDefined(cls, element: MemberInfo, attributeType: Type, inherit: bool) -> bool:
        """:param element:
        :param attributeType:
        :param inherit:
        :return:
        """
    @classmethod
    @overload
    def IsDefined(cls, element: Module, attributeType: Type, inherit: bool) -> bool:
        """:param element:
        :param attributeType:
        :param inherit:
        :return:
        """
    @classmethod
    @overload
    def IsDefined(cls, element: ParameterInfo, attributeType: Type, inherit: bool) -> bool:
        """:param element:
        :param attributeType:
        :param inherit:
        :return:
        """
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

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

    def __init__(self, validOn: AttributeTargets):
        """:param validOn:"""
    @property
    def AllowMultiple(self) -> bool:
        """:return:"""
    @AllowMultiple.setter
    def AllowMultiple(self, value: bool) -> None: ...
    @property
    def Inherited(self) -> bool:
        """:return:"""
    @Inherited.setter
    def Inherited(self, value: bool) -> None: ...
    @property
    def TypeId(self) -> object:
        """:return:"""
    @property
    def ValidOn(self) -> AttributeTargets:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
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
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class BCLDebug(ABC, Object):
    """"""

    @classmethod
    def Assert(cls, condition: bool, message: str) -> None:
        """:param condition:
        :param message:
        """
    @classmethod
    def DumpStack(cls, switchName: str) -> None:
        """:param switchName:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    @overload
    def Log(cls, message: str) -> None:
        """:param message:"""
    @classmethod
    @overload
    def Log(cls, switchName: str, message: str) -> None:
        """:param switchName:
        :param message:
        """
    @classmethod
    @overload
    def Log(cls, switchName: str, level: LogLevel, messages: Array[object]) -> None:
        """:param switchName:
        :param level:
        :param messages:
        """
    def ToString(self) -> str:
        """:return:"""
    @classmethod
    @overload
    def Trace(cls, switchName: str, messages: Array[object]) -> None:
        """:param switchName:
        :param messages:
        """
    @classmethod
    @overload
    def Trace(cls, switchName: str, format: str, messages: Array[object]) -> None:
        """:param switchName:
        :param format:
        :param messages:
        """

class BadImageFormatException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, inner: Exception):
        """:param message:
        :param inner:
        """
    @overload
    def __init__(self, message: str, fileName: str):
        """:param message:
        :param fileName:
        """
    @overload
    def __init__(self, message: str, fileName: str, inner: Exception):
        """:param message:
        :param fileName:
        :param inner:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def FileName(self) -> str:
        """:return:"""
    @property
    def FusionLog(self) -> str:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class Base64FormattingOptions(Enum):
    """"""

    _None: Base64FormattingOptions = ...
    """"""
    InsertLineBreaks: Base64FormattingOptions = ...
    """"""

class BaseConfigHandler(ABC, Object):
    """"""

    def __init__(self):
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
        """:param size:
        :param subType:
        :param nType:
        :param terminal:
        :param text:
        :param textLength:
        :param prefixLength:
        """
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
        """:param size:
        :param subType:
        :param nType:
        :param terminal:
        :param text:
        :param textLength:
        :param prefixLength:
        """
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
        """:param size:
        :param subType:
        :param nType:
        :param terminal:
        :param text:
        :param textLength:
        :param prefixLength:
        """
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
        """:param fEmpty:
        :param size:
        :param subType:
        :param nType:
        :param terminal:
        :param text:
        :param textLength:
        :param prefixLength:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
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
        """:param size:
        :param subType:
        :param nType:
        :param terminal:
        :param text:
        :param textLength:
        :param prefixLength:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def NotifyEvent(self, nEvent: ConfigEvents) -> None:
        """:param nEvent:"""
    def ToString(self) -> str:
        """:return:"""

class BitConverter(ABC, Object):
    """"""

    IsLittleEndian: Final[ClassVar[bool]] = ...
    """
    
    :return: 
    """
    @classmethod
    def DoubleToInt64Bits(cls, value: float) -> int:
        """:param value:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    @overload
    def GetBytes(cls, value: bool) -> Array[int]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def GetBytes(cls, value: Char) -> Array[int]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def GetBytes(cls, value: float) -> Array[int]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def GetBytes(cls, value: int) -> Array[int]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def GetBytes(cls, value: int) -> Array[int]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def GetBytes(cls, value: int) -> Array[int]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def GetBytes(cls, value: float) -> Array[int]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def GetBytes(cls, value: int) -> Array[int]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def GetBytes(cls, value: int) -> Array[int]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def GetBytes(cls, value: int) -> Array[int]:
        """:param value:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def Int64BitsToDouble(cls, value: int) -> float:
        """:param value:
        :return:
        """
    @classmethod
    def ToBoolean(cls, value: Array[int], startIndex: int) -> bool:
        """:param value:
        :param startIndex:
        :return:
        """
    @classmethod
    def ToChar(cls, value: Array[int], startIndex: int) -> Char:
        """:param value:
        :param startIndex:
        :return:
        """
    @classmethod
    def ToDouble(cls, value: Array[int], startIndex: int) -> float:
        """:param value:
        :param startIndex:
        :return:
        """
    @classmethod
    def ToInt16(cls, value: Array[int], startIndex: int) -> int:
        """:param value:
        :param startIndex:
        :return:
        """
    @classmethod
    def ToInt32(cls, value: Array[int], startIndex: int) -> int:
        """:param value:
        :param startIndex:
        :return:
        """
    @classmethod
    def ToInt64(cls, value: Array[int], startIndex: int) -> int:
        """:param value:
        :param startIndex:
        :return:
        """
    @classmethod
    def ToSingle(cls, value: Array[int], startIndex: int) -> float:
        """:param value:
        :param startIndex:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """:return:"""
    @classmethod
    @overload
    def ToString(cls, value: Array[int]) -> str:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: Array[int], startIndex: int) -> str:
        """:param value:
        :param startIndex:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: Array[int], startIndex: int, length: int) -> str:
        """:param value:
        :param startIndex:
        :param length:
        :return:
        """
    @classmethod
    def ToUInt16(cls, value: Array[int], startIndex: int) -> int:
        """:param value:
        :param startIndex:
        :return:
        """
    @classmethod
    def ToUInt32(cls, value: Array[int], startIndex: int) -> int:
        """:param value:
        :param startIndex:
        :return:
        """
    @classmethod
    def ToUInt64(cls, value: Array[int], startIndex: int) -> int:
        """:param value:
        :param startIndex:
        :return:
        """

class Boolean(ValueType, IComparable, IComparable[Boolean], IConvertible, IEquatable[Boolean]):
    """"""

    FalseString: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    TrueString: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    @overload
    def CompareTo(self, other: bool) -> int:
        """:param other:
        :return:
        """
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: bool) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeCode(self) -> TypeCode:
        """:return:"""
    @classmethod
    def Parse(cls, value: str) -> bool:
        """:param value:
        :return:
        """
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """:param provider:
        :return:
        """
    def ToByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToChar(self, provider: IFormatProvider) -> Char:
        """:param provider:
        :return:
        """
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """:param provider:
        :return:
        """
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """:param provider:
        :return:
        """
    def ToDouble(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    def ToInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSingle(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """:param provider:
        :return:
        """
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """:param conversionType:
        :param provider:
        :return:
        """
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    @classmethod
    def TryParse(cls, value: str, result: bool) -> Tuple[bool, bool]:
        """:param value:
        :param result:
        :return:
        """

class Buffer(ABC, Object):
    """"""

    @classmethod
    def BlockCopy(cls, src: Array, srcOffset: int, dst: Array, dstOffset: int, count: int) -> None:
        """:param src:
        :param srcOffset:
        :param dst:
        :param dstOffset:
        :param count:
        """
    @classmethod
    def ByteLength(cls, array: Array) -> int:
        """:param array:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    def GetByte(cls, array: Array, index: int) -> int:
        """:param array:
        :param index:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    @overload
    def MemoryCopy(
        cls,
        source: None,
        destination: None,
        destinationSizeInBytes: int,
        sourceBytesToCopy: int,
    ) -> None:
        """:param source:
        :param destination:
        :param destinationSizeInBytes:
        :param sourceBytesToCopy:
        """
    @classmethod
    @overload
    def MemoryCopy(
        cls,
        source: None,
        destination: None,
        destinationSizeInBytes: int,
        sourceBytesToCopy: int,
    ) -> None:
        """:param source:
        :param destination:
        :param destinationSizeInBytes:
        :param sourceBytesToCopy:
        """
    @classmethod
    def SetByte(cls, array: Array, index: int, value: int) -> None:
        """:param array:
        :param index:
        :param value:
        """
    def ToString(self) -> str:
        """:return:"""

class Byte(
    ValueType,
    IComparable,
    IComparable[Byte],
    IConvertible,
    IEquatable[Byte],
    IFormattable,
):
    """"""

    MaxValue: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MinValue: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @overload
    def CompareTo(self, other: int) -> int:
        """:param other:
        :return:
        """
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: int) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeCode(self) -> TypeCode:
        """:return:"""
    @classmethod
    @overload
    def Parse(cls, s: str) -> int:
        """:param s:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles) -> int:
        """:param s:
        :param style:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider) -> int:
        """:param s:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles, provider: IFormatProvider) -> int:
        """:param s:
        :param style:
        :param provider:
        :return:
        """
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """:param provider:
        :return:
        """
    def ToByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToChar(self, provider: IFormatProvider) -> Char:
        """:param provider:
        :return:
        """
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """:param provider:
        :return:
        """
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """:param provider:
        :return:
        """
    def ToDouble(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    def ToInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSingle(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self, format: str) -> str:
        """:param format:
        :return:
        """
    @overload
    def ToString(self, format: str, formatProvider: IFormatProvider) -> str:
        """:param format:
        :param formatProvider:
        :return:
        """
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """:param conversionType:
        :param provider:
        :return:
        """
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    @classmethod
    @overload
    def TryParse(cls, s: str, result: int) -> Tuple[bool, int]:
        """:param s:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryParse(
        cls, s: str, style: NumberStyles, provider: IFormatProvider, result: int
    ) -> Tuple[bool, int]:
        """:param s:
        :param style:
        :param provider:
        :param result:
        :return:
        """

class CLRConfig(Object):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class CLSCompliantAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, isCompliant: bool):
        """:param isCompliant:"""
    @property
    def IsCompliant(self) -> bool:
        """:return:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
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
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class CannotUnloadAppDomainException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class Char(ValueType, IComparable, IComparable[Char], IConvertible, IEquatable[Char]):
    """"""

    MaxValue: Final[ClassVar[Char]] = ...
    """
    
    :return: 
    """
    MinValue: Final[ClassVar[Char]] = ...
    """
    
    :return: 
    """
    @overload
    def CompareTo(self, other: Char) -> int:
        """:param other:
        :return:
        """
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @classmethod
    def ConvertFromUtf32(cls, utf32: int) -> str:
        """:param utf32:
        :return:
        """
    @classmethod
    @overload
    def ConvertToUtf32(cls, highSurrogate: Char, lowSurrogate: Char) -> int:
        """:param highSurrogate:
        :param lowSurrogate:
        :return:
        """
    @classmethod
    @overload
    def ConvertToUtf32(cls, s: str, index: int) -> int:
        """:param s:
        :param index:
        :return:
        """
    @overload
    def Equals(self, other: Char) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    @classmethod
    @overload
    def GetNumericValue(cls, c: Char) -> float:
        """:param c:
        :return:
        """
    @classmethod
    @overload
    def GetNumericValue(cls, s: str, index: int) -> float:
        """:param s:
        :param index:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeCode(self) -> TypeCode:
        """:return:"""
    @classmethod
    @overload
    def GetUnicodeCategory(cls, c: Char) -> UnicodeCategory:
        """:param c:
        :return:
        """
    @classmethod
    @overload
    def GetUnicodeCategory(cls, s: str, index: int) -> UnicodeCategory:
        """:param s:
        :param index:
        :return:
        """
    @classmethod
    @overload
    def IsControl(cls, c: Char) -> bool:
        """:param c:
        :return:
        """
    @classmethod
    @overload
    def IsControl(cls, s: str, index: int) -> bool:
        """:param s:
        :param index:
        :return:
        """
    @classmethod
    @overload
    def IsDigit(cls, c: Char) -> bool:
        """:param c:
        :return:
        """
    @classmethod
    @overload
    def IsDigit(cls, s: str, index: int) -> bool:
        """:param s:
        :param index:
        :return:
        """
    @classmethod
    @overload
    def IsHighSurrogate(cls, c: Char) -> bool:
        """:param c:
        :return:
        """
    @classmethod
    @overload
    def IsHighSurrogate(cls, s: str, index: int) -> bool:
        """:param s:
        :param index:
        :return:
        """
    @classmethod
    @overload
    def IsLetter(cls, c: Char) -> bool:
        """:param c:
        :return:
        """
    @classmethod
    @overload
    def IsLetter(cls, s: str, index: int) -> bool:
        """:param s:
        :param index:
        :return:
        """
    @classmethod
    @overload
    def IsLetterOrDigit(cls, c: Char) -> bool:
        """:param c:
        :return:
        """
    @classmethod
    @overload
    def IsLetterOrDigit(cls, s: str, index: int) -> bool:
        """:param s:
        :param index:
        :return:
        """
    @classmethod
    @overload
    def IsLowSurrogate(cls, c: Char) -> bool:
        """:param c:
        :return:
        """
    @classmethod
    @overload
    def IsLowSurrogate(cls, s: str, index: int) -> bool:
        """:param s:
        :param index:
        :return:
        """
    @classmethod
    @overload
    def IsLower(cls, c: Char) -> bool:
        """:param c:
        :return:
        """
    @classmethod
    @overload
    def IsLower(cls, s: str, index: int) -> bool:
        """:param s:
        :param index:
        :return:
        """
    @classmethod
    @overload
    def IsNumber(cls, c: Char) -> bool:
        """:param c:
        :return:
        """
    @classmethod
    @overload
    def IsNumber(cls, s: str, index: int) -> bool:
        """:param s:
        :param index:
        :return:
        """
    @classmethod
    @overload
    def IsPunctuation(cls, c: Char) -> bool:
        """:param c:
        :return:
        """
    @classmethod
    @overload
    def IsPunctuation(cls, s: str, index: int) -> bool:
        """:param s:
        :param index:
        :return:
        """
    @classmethod
    @overload
    def IsSeparator(cls, c: Char) -> bool:
        """:param c:
        :return:
        """
    @classmethod
    @overload
    def IsSeparator(cls, s: str, index: int) -> bool:
        """:param s:
        :param index:
        :return:
        """
    @classmethod
    @overload
    def IsSurrogate(cls, c: Char) -> bool:
        """:param c:
        :return:
        """
    @classmethod
    @overload
    def IsSurrogate(cls, s: str, index: int) -> bool:
        """:param s:
        :param index:
        :return:
        """
    @classmethod
    @overload
    def IsSurrogatePair(cls, highSurrogate: Char, lowSurrogate: Char) -> bool:
        """:param highSurrogate:
        :param lowSurrogate:
        :return:
        """
    @classmethod
    @overload
    def IsSurrogatePair(cls, s: str, index: int) -> bool:
        """:param s:
        :param index:
        :return:
        """
    @classmethod
    @overload
    def IsSymbol(cls, c: Char) -> bool:
        """:param c:
        :return:
        """
    @classmethod
    @overload
    def IsSymbol(cls, s: str, index: int) -> bool:
        """:param s:
        :param index:
        :return:
        """
    @classmethod
    @overload
    def IsUpper(cls, c: Char) -> bool:
        """:param c:
        :return:
        """
    @classmethod
    @overload
    def IsUpper(cls, s: str, index: int) -> bool:
        """:param s:
        :param index:
        :return:
        """
    @classmethod
    @overload
    def IsWhiteSpace(cls, c: Char) -> bool:
        """:param c:
        :return:
        """
    @classmethod
    @overload
    def IsWhiteSpace(cls, s: str, index: int) -> bool:
        """:param s:
        :param index:
        :return:
        """
    @classmethod
    def Parse(cls, s: str) -> Char:
        """:param s:
        :return:
        """
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """:param provider:
        :return:
        """
    def ToByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToChar(self, provider: IFormatProvider) -> Char:
        """:param provider:
        :return:
        """
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """:param provider:
        :return:
        """
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """:param provider:
        :return:
        """
    def ToDouble(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    def ToInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    @classmethod
    @overload
    def ToLower(cls, c: Char) -> Char:
        """:param c:
        :return:
        """
    @classmethod
    @overload
    def ToLower(cls, c: Char, culture: CultureInfo) -> Char:
        """:param c:
        :param culture:
        :return:
        """
    @classmethod
    def ToLowerInvariant(cls, c: Char) -> Char:
        """:param c:
        :return:
        """
    def ToSByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSingle(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """:return:"""
    @classmethod
    @overload
    def ToString(cls, c: Char) -> str:
        """:param c:
        :return:
        """
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """:param provider:
        :return:
        """
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """:param conversionType:
        :param provider:
        :return:
        """
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    @classmethod
    @overload
    def ToUpper(cls, c: Char) -> Char:
        """:param c:
        :return:
        """
    @classmethod
    @overload
    def ToUpper(cls, c: Char, culture: CultureInfo) -> Char:
        """:param c:
        :param culture:
        :return:
        """
    @classmethod
    def ToUpperInvariant(cls, c: Char) -> Char:
        """:param c:
        :return:
        """
    @classmethod
    def TryParse(cls, s: str, result: Char) -> Tuple[bool, Char]:
        """:param s:
        :param result:
        :return:
        """

class CharEnumerator(Object, IEnumerator[Char], IEnumerator, ICloneable, IDisposable):
    """"""

    @property
    def Current(self) -> object:
        """:return:"""
    def Clone(self) -> object:
        """:return:"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def MoveNext(self) -> bool:
        """:return:"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """:return:"""

class ClientUtils(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    def GetBitCount(cls, x: int) -> int:
        """:param x:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def IsCriticalException(cls, ex: Exception) -> bool:
        """:param ex:
        :return:
        """
    @classmethod
    @overload
    def IsEnumValid(cls, enumValue: Enum, value: int, minValue: int, maxValue: int) -> bool:
        """:param enumValue:
        :param value:
        :param minValue:
        :param maxValue:
        :return:
        """
    @classmethod
    @overload
    def IsEnumValid(
        cls,
        enumValue: Enum,
        value: int,
        minValue: int,
        maxValue: int,
        maxNumberOfBitsOn: int,
    ) -> bool:
        """:param enumValue:
        :param value:
        :param minValue:
        :param maxValue:
        :param maxNumberOfBitsOn:
        :return:
        """
    @classmethod
    def IsEnumValid_Masked(cls, enumValue: Enum, value: int, mask: int) -> bool:
        """:param enumValue:
        :param value:
        :param mask:
        :return:
        """
    @classmethod
    def IsEnumValid_NotSequential(cls, enumValue: Enum, value: int, enumValues: Array[int]) -> bool:
        """:param enumValue:
        :param value:
        :param enumValues:
        :return:
        """
    @classmethod
    def IsSecurityOrCriticalException(cls, ex: Exception) -> bool:
        """:param ex:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

Comparison: Callable[[T, T], int] = ...
"""

:param x: 
:param y: 
:return: 
"""

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
        """:return:"""
    @classmethod
    @property
    def IsAppEarlierThanWindowsPhone8(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def IsAppEarlierThanWindowsPhoneMango(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def IsCompatibilityBehaviorDefined(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def IsNetFx40LegacySecurityPolicy(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def IsNetFx40TimeSpanLegacyFormatMode(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def IsNetFx45LegacyManagedDeflateStream(cls) -> bool:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

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
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

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

    def __init__(self):
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
        """:param size:
        :param subType:
        :param nType:
        :param terminal:
        :param text:
        :param textLength:
        :param prefixLength:
        """
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
        """:param size:
        :param subType:
        :param nType:
        :param terminal:
        :param text:
        :param textLength:
        :param prefixLength:
        """
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
        """:param size:
        :param subType:
        :param nType:
        :param terminal:
        :param text:
        :param textLength:
        :param prefixLength:
        """
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
        """:param fEmpty:
        :param size:
        :param subType:
        :param nType:
        :param terminal:
        :param text:
        :param textLength:
        :param prefixLength:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
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
        """:param size:
        :param subType:
        :param nType:
        :param terminal:
        :param text:
        :param textLength:
        :param prefixLength:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def NotifyEvent(self, nEvent: ConfigEvents) -> None:
        """:param nEvent:"""
    def ToString(self) -> str:
        """:return:"""

class Console(ABC, Object):
    """"""

    @classmethod
    @property
    def BackgroundColor(cls) -> ConsoleColor:
        """:return:"""
    @classmethod
    @BackgroundColor.setter
    def BackgroundColor(cls, value: ConsoleColor) -> None: ...
    @classmethod
    @property
    def BufferHeight(cls) -> int:
        """:return:"""
    @classmethod
    @BufferHeight.setter
    def BufferHeight(cls, value: int) -> None: ...
    @classmethod
    @property
    def BufferWidth(cls) -> int:
        """:return:"""
    @classmethod
    @BufferWidth.setter
    def BufferWidth(cls, value: int) -> None: ...
    @classmethod
    @property
    def CapsLock(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def CursorLeft(cls) -> int:
        """:return:"""
    @classmethod
    @CursorLeft.setter
    def CursorLeft(cls, value: int) -> None: ...
    @classmethod
    @property
    def CursorSize(cls) -> int:
        """:return:"""
    @classmethod
    @CursorSize.setter
    def CursorSize(cls, value: int) -> None: ...
    @classmethod
    @property
    def CursorTop(cls) -> int:
        """:return:"""
    @classmethod
    @CursorTop.setter
    def CursorTop(cls, value: int) -> None: ...
    @classmethod
    @property
    def CursorVisible(cls) -> bool:
        """:return:"""
    @classmethod
    @CursorVisible.setter
    def CursorVisible(cls, value: bool) -> None: ...
    @classmethod
    @property
    def Error(cls) -> TextWriter:
        """:return:"""
    @classmethod
    @property
    def ForegroundColor(cls) -> ConsoleColor:
        """:return:"""
    @classmethod
    @ForegroundColor.setter
    def ForegroundColor(cls, value: ConsoleColor) -> None: ...
    @classmethod
    @property
    def In(cls) -> TextReader:
        """:return:"""
    @classmethod
    @property
    def InputEncoding(cls) -> Encoding:
        """:return:"""
    @classmethod
    @InputEncoding.setter
    def InputEncoding(cls, value: Encoding) -> None: ...
    @classmethod
    @property
    def IsErrorRedirected(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def IsInputRedirected(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def IsOutputRedirected(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def KeyAvailable(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def LargestWindowHeight(cls) -> int:
        """:return:"""
    @classmethod
    @property
    def LargestWindowWidth(cls) -> int:
        """:return:"""
    @classmethod
    @property
    def NumberLock(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def Out(cls) -> TextWriter:
        """:return:"""
    @classmethod
    @property
    def OutputEncoding(cls) -> Encoding:
        """:return:"""
    @classmethod
    @OutputEncoding.setter
    def OutputEncoding(cls, value: Encoding) -> None: ...
    @classmethod
    @property
    def Title(cls) -> str:
        """:return:"""
    @classmethod
    @Title.setter
    def Title(cls, value: str) -> None: ...
    @classmethod
    @property
    def TreatControlCAsInput(cls) -> bool:
        """:return:"""
    @classmethod
    @TreatControlCAsInput.setter
    def TreatControlCAsInput(cls, value: bool) -> None: ...
    @classmethod
    @property
    def WindowHeight(cls) -> int:
        """:return:"""
    @classmethod
    @WindowHeight.setter
    def WindowHeight(cls, value: int) -> None: ...
    @classmethod
    @property
    def WindowLeft(cls) -> int:
        """:return:"""
    @classmethod
    @WindowLeft.setter
    def WindowLeft(cls, value: int) -> None: ...
    @classmethod
    @property
    def WindowTop(cls) -> int:
        """:return:"""
    @classmethod
    @WindowTop.setter
    def WindowTop(cls, value: int) -> None: ...
    @classmethod
    @property
    def WindowWidth(cls) -> int:
        """:return:"""
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
        """:param frequency:
        :param duration:
        """
    @classmethod
    def Clear(cls) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
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
        """:param sourceLeft:
        :param sourceTop:
        :param sourceWidth:
        :param sourceHeight:
        :param targetLeft:
        :param targetTop:
        """
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
        """:param sourceLeft:
        :param sourceTop:
        :param sourceWidth:
        :param sourceHeight:
        :param targetLeft:
        :param targetTop:
        :param sourceChar:
        :param sourceForeColor:
        :param sourceBackColor:
        """
    @classmethod
    @overload
    def OpenStandardError(cls) -> Stream:
        """:return:"""
    @classmethod
    @overload
    def OpenStandardError(cls, bufferSize: int) -> Stream:
        """:param bufferSize:
        :return:
        """
    @classmethod
    @overload
    def OpenStandardInput(cls) -> Stream:
        """:return:"""
    @classmethod
    @overload
    def OpenStandardInput(cls, bufferSize: int) -> Stream:
        """:param bufferSize:
        :return:
        """
    @classmethod
    @overload
    def OpenStandardOutput(cls) -> Stream:
        """:return:"""
    @classmethod
    @overload
    def OpenStandardOutput(cls, bufferSize: int) -> Stream:
        """:param bufferSize:
        :return:
        """
    @classmethod
    def Read(cls) -> int:
        """:return:"""
    @classmethod
    @overload
    def ReadKey(cls) -> ConsoleKeyInfo:
        """:return:"""
    @classmethod
    @overload
    def ReadKey(cls, intercept: bool) -> ConsoleKeyInfo:
        """:param intercept:
        :return:
        """
    @classmethod
    def ReadLine(cls) -> str:
        """:return:"""
    @classmethod
    def ResetColor(cls) -> None:
        """"""
    @classmethod
    def SetBufferSize(cls, width: int, height: int) -> None:
        """:param width:
        :param height:
        """
    @classmethod
    def SetCursorPosition(cls, left: int, top: int) -> None:
        """:param left:
        :param top:
        """
    @classmethod
    def SetError(cls, newError: TextWriter) -> None:
        """:param newError:"""
    @classmethod
    def SetIn(cls, newIn: TextReader) -> None:
        """:param newIn:"""
    @classmethod
    def SetOut(cls, newOut: TextWriter) -> None:
        """:param newOut:"""
    @classmethod
    def SetWindowPosition(cls, left: int, top: int) -> None:
        """:param left:
        :param top:
        """
    @classmethod
    def SetWindowSize(cls, width: int, height: int) -> None:
        """:param width:
        :param height:
        """
    def ToString(self) -> str:
        """:return:"""
    @classmethod
    @overload
    def Write(cls, buffer: Array[Char]) -> None:
        """:param buffer:"""
    @classmethod
    @overload
    def Write(cls, value: bool) -> None:
        """:param value:"""
    @classmethod
    @overload
    def Write(cls, value: Char) -> None:
        """:param value:"""
    @classmethod
    @overload
    def Write(cls, value: Decimal) -> None:
        """:param value:"""
    @classmethod
    @overload
    def Write(cls, value: float) -> None:
        """:param value:"""
    @classmethod
    @overload
    def Write(cls, value: int) -> None:
        """:param value:"""
    @classmethod
    @overload
    def Write(cls, value: int) -> None:
        """:param value:"""
    @classmethod
    @overload
    def Write(cls, value: object) -> None:
        """:param value:"""
    @classmethod
    @overload
    def Write(cls, value: float) -> None:
        """:param value:"""
    @classmethod
    @overload
    def Write(cls, value: str) -> None:
        """:param value:"""
    @classmethod
    @overload
    def Write(cls, value: int) -> None:
        """:param value:"""
    @classmethod
    @overload
    def Write(cls, value: int) -> None:
        """:param value:"""
    @classmethod
    @overload
    def Write(cls, format: str, arg: Array[object]) -> None:
        """:param format:
        :param arg:
        """
    @classmethod
    @overload
    def Write(cls, format: str, arg0: object) -> None:
        """:param format:
        :param arg0:
        """
    @classmethod
    @overload
    def Write(cls, buffer: Array[Char], index: int, count: int) -> None:
        """:param buffer:
        :param index:
        :param count:
        """
    @classmethod
    @overload
    def Write(cls, format: str, arg0: object, arg1: object) -> None:
        """:param format:
        :param arg0:
        :param arg1:
        """
    @classmethod
    @overload
    def Write(cls, format: str, arg0: object, arg1: object, arg2: object) -> None:
        """:param format:
        :param arg0:
        :param arg1:
        :param arg2:
        """
    @classmethod
    @overload
    def Write(cls, format: str, arg0: object, arg1: object, arg2: object, arg3: object) -> None:
        """:param format:
        :param arg0:
        :param arg1:
        :param arg2:
        :param arg3:
        """
    @classmethod
    @overload
    def WriteLine(cls) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, buffer: Array[Char]) -> None:
        """:param buffer:"""
    @classmethod
    @overload
    def WriteLine(cls, value: bool) -> None:
        """:param value:"""
    @classmethod
    @overload
    def WriteLine(cls, value: Char) -> None:
        """:param value:"""
    @classmethod
    @overload
    def WriteLine(cls, value: Decimal) -> None:
        """:param value:"""
    @classmethod
    @overload
    def WriteLine(cls, value: float) -> None:
        """:param value:"""
    @classmethod
    @overload
    def WriteLine(cls, value: int) -> None:
        """:param value:"""
    @classmethod
    @overload
    def WriteLine(cls, value: int) -> None:
        """:param value:"""
    @classmethod
    @overload
    def WriteLine(cls, value: object) -> None:
        """:param value:"""
    @classmethod
    @overload
    def WriteLine(cls, value: float) -> None:
        """:param value:"""
    @classmethod
    @overload
    def WriteLine(cls, value: str) -> None:
        """:param value:"""
    @classmethod
    @overload
    def WriteLine(cls, value: int) -> None:
        """:param value:"""
    @classmethod
    @overload
    def WriteLine(cls, value: int) -> None:
        """:param value:"""
    @classmethod
    @overload
    def WriteLine(cls, format: str, arg: Array[object]) -> None:
        """:param format:
        :param arg:
        """
    @classmethod
    @overload
    def WriteLine(cls, format: str, arg0: object) -> None:
        """:param format:
        :param arg0:
        """
    @classmethod
    @overload
    def WriteLine(cls, buffer: Array[Char], index: int, count: int) -> None:
        """:param buffer:
        :param index:
        :param count:
        """
    @classmethod
    @overload
    def WriteLine(cls, format: str, arg0: object, arg1: object) -> None:
        """:param format:
        :param arg0:
        :param arg1:
        """
    @classmethod
    @overload
    def WriteLine(cls, format: str, arg0: object, arg1: object, arg2: object) -> None:
        """:param format:
        :param arg0:
        :param arg1:
        :param arg2:
        """
    @classmethod
    @overload
    def WriteLine(cls, format: str, arg0: object, arg1: object, arg2: object, arg3: object) -> None:
        """:param format:
        :param arg0:
        :param arg1:
        :param arg2:
        :param arg3:
        """
    CancelKeyPress: EventType[ConsoleCancelEventHandler] = ...
    """"""

class ConsoleCancelEventArgs(EventArgs):
    """"""

    @property
    def Cancel(self) -> bool:
        """:return:"""
    @Cancel.setter
    def Cancel(self, value: bool) -> None: ...
    @property
    def SpecialKey(self) -> ConsoleSpecialKey:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

ConsoleCancelEventHandler: Callable[[object, ConsoleCancelEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

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

    def __init__(self, keyChar: Char, key: ConsoleKey, shift: bool, alt: bool, control: bool):
        """:param keyChar:
        :param key:
        :param shift:
        :param alt:
        :param control:
        """
    @property
    def Key(self) -> ConsoleKey:
        """:return:"""
    @property
    def KeyChar(self) -> Char:
        """:return:"""
    @property
    def Modifiers(self) -> ConsoleModifiers:
        """:return:"""
    @overload
    def Equals(self, obj: ConsoleKeyInfo) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def __eq__(self, other: ConsoleKeyInfo) -> bool:
        """:param other:
        :return:
        """
    def __ne__(self, other: ConsoleKeyInfo) -> bool:
        """:param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, a: ConsoleKeyInfo, b: ConsoleKeyInfo) -> bool:
        """:param a:
        :param b:
        :return:
        """
    @classmethod
    def op_Inequality(cls, a: ConsoleKeyInfo, b: ConsoleKeyInfo) -> bool:
        """:param a:
        :param b:
        :return:
        """

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
        """:param requestedType:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetLifetimeService(self) -> object:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def InitializeLifetimeService(self) -> object:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class ContextMarshalException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, inner: Exception):
        """:param message:
        :param inner:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class ContextStaticAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
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
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class Convert(ABC, Object):
    """"""

    DBNull: Final[ClassVar[object]] = ...
    """
    
    :return: 
    """
    @classmethod
    @overload
    def ChangeType(cls, value: object, conversionType: Type) -> object:
        """:param value:
        :param conversionType:
        :return:
        """
    @classmethod
    @overload
    def ChangeType(cls, value: object, typeCode: TypeCode) -> object:
        """:param value:
        :param typeCode:
        :return:
        """
    @classmethod
    @overload
    def ChangeType(cls, value: object, conversionType: Type, provider: IFormatProvider) -> object:
        """:param value:
        :param conversionType:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ChangeType(cls, value: object, typeCode: TypeCode, provider: IFormatProvider) -> object:
        """:param value:
        :param typeCode:
        :param provider:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    def FromBase64CharArray(cls, inArray: Array[Char], offset: int, length: int) -> Array[int]:
        """:param inArray:
        :param offset:
        :param length:
        :return:
        """
    @classmethod
    def FromBase64String(cls, s: str) -> Array[int]:
        """:param s:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def GetTypeCode(cls, value: object) -> TypeCode:
        """:param value:
        :return:
        """
    @classmethod
    def IsDBNull(cls, value: object) -> bool:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToBase64CharArray(
        cls,
        inArray: Array[int],
        offsetIn: int,
        length: int,
        outArray: Array[Char],
        offsetOut: int,
    ) -> int:
        """:param inArray:
        :param offsetIn:
        :param length:
        :param outArray:
        :param offsetOut:
        :return:
        """
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
        """:param inArray:
        :param offsetIn:
        :param length:
        :param outArray:
        :param offsetOut:
        :param options:
        :return:
        """
    @classmethod
    @overload
    def ToBase64String(cls, inArray: Array[int]) -> str:
        """:param inArray:
        :return:
        """
    @classmethod
    @overload
    def ToBase64String(cls, inArray: Array[int], options: Base64FormattingOptions) -> str:
        """:param inArray:
        :param options:
        :return:
        """
    @classmethod
    @overload
    def ToBase64String(cls, inArray: Array[int], offset: int, length: int) -> str:
        """:param inArray:
        :param offset:
        :param length:
        :return:
        """
    @classmethod
    @overload
    def ToBase64String(
        cls,
        inArray: Array[int],
        offset: int,
        length: int,
        options: Base64FormattingOptions,
    ) -> str:
        """:param inArray:
        :param offset:
        :param length:
        :param options:
        :return:
        """
    @classmethod
    @overload
    def ToBoolean(cls, value: bool) -> bool:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToBoolean(cls, value: int) -> bool:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToBoolean(cls, value: Char) -> bool:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToBoolean(cls, value: DateTime) -> bool:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToBoolean(cls, value: Decimal) -> bool:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToBoolean(cls, value: float) -> bool:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToBoolean(cls, value: int) -> bool:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToBoolean(cls, value: int) -> bool:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToBoolean(cls, value: int) -> bool:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToBoolean(cls, value: object) -> bool:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToBoolean(cls, value: int) -> bool:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToBoolean(cls, value: float) -> bool:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToBoolean(cls, value: str) -> bool:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToBoolean(cls, value: int) -> bool:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToBoolean(cls, value: int) -> bool:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToBoolean(cls, value: int) -> bool:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToBoolean(cls, value: object, provider: IFormatProvider) -> bool:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToBoolean(cls, value: str, provider: IFormatProvider) -> bool:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToByte(cls, value: bool) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToByte(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToByte(cls, value: Char) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToByte(cls, value: DateTime) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToByte(cls, value: Decimal) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToByte(cls, value: float) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToByte(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToByte(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToByte(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToByte(cls, value: object) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToByte(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToByte(cls, value: float) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToByte(cls, value: str) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToByte(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToByte(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToByte(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToByte(cls, value: object, provider: IFormatProvider) -> int:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToByte(cls, value: str, provider: IFormatProvider) -> int:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToByte(cls, value: str, fromBase: int) -> int:
        """:param value:
        :param fromBase:
        :return:
        """
    @classmethod
    @overload
    def ToChar(cls, value: bool) -> Char:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToChar(cls, value: int) -> Char:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToChar(cls, value: Char) -> Char:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToChar(cls, value: DateTime) -> Char:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToChar(cls, value: Decimal) -> Char:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToChar(cls, value: float) -> Char:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToChar(cls, value: int) -> Char:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToChar(cls, value: int) -> Char:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToChar(cls, value: int) -> Char:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToChar(cls, value: object) -> Char:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToChar(cls, value: int) -> Char:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToChar(cls, value: float) -> Char:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToChar(cls, value: str) -> Char:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToChar(cls, value: int) -> Char:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToChar(cls, value: int) -> Char:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToChar(cls, value: int) -> Char:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToChar(cls, value: object, provider: IFormatProvider) -> Char:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToChar(cls, value: str, provider: IFormatProvider) -> Char:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToDateTime(cls, value: bool) -> DateTime:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDateTime(cls, value: int) -> DateTime:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDateTime(cls, value: Char) -> DateTime:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDateTime(cls, value: DateTime) -> DateTime:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDateTime(cls, value: Decimal) -> DateTime:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDateTime(cls, value: float) -> DateTime:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDateTime(cls, value: int) -> DateTime:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDateTime(cls, value: int) -> DateTime:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDateTime(cls, value: int) -> DateTime:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDateTime(cls, value: object) -> DateTime:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDateTime(cls, value: int) -> DateTime:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDateTime(cls, value: float) -> DateTime:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDateTime(cls, value: str) -> DateTime:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDateTime(cls, value: int) -> DateTime:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDateTime(cls, value: int) -> DateTime:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDateTime(cls, value: int) -> DateTime:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDateTime(cls, value: object, provider: IFormatProvider) -> DateTime:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToDateTime(cls, value: str, provider: IFormatProvider) -> DateTime:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToDecimal(cls, value: bool) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDecimal(cls, value: int) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDecimal(cls, value: Char) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDecimal(cls, value: DateTime) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDecimal(cls, value: Decimal) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDecimal(cls, value: float) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDecimal(cls, value: int) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDecimal(cls, value: int) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDecimal(cls, value: int) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDecimal(cls, value: object) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDecimal(cls, value: int) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDecimal(cls, value: float) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDecimal(cls, value: str) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDecimal(cls, value: int) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDecimal(cls, value: int) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDecimal(cls, value: int) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDecimal(cls, value: object, provider: IFormatProvider) -> Decimal:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToDecimal(cls, value: str, provider: IFormatProvider) -> Decimal:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToDouble(cls, value: bool) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDouble(cls, value: int) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDouble(cls, value: Char) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDouble(cls, value: DateTime) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDouble(cls, value: Decimal) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDouble(cls, value: float) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDouble(cls, value: int) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDouble(cls, value: int) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDouble(cls, value: int) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDouble(cls, value: object) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDouble(cls, value: int) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDouble(cls, value: float) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDouble(cls, value: str) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDouble(cls, value: int) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDouble(cls, value: int) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDouble(cls, value: int) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToDouble(cls, value: object, provider: IFormatProvider) -> float:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToDouble(cls, value: str, provider: IFormatProvider) -> float:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToInt16(cls, value: bool) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt16(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt16(cls, value: Char) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt16(cls, value: DateTime) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt16(cls, value: Decimal) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt16(cls, value: float) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt16(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt16(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt16(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt16(cls, value: object) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt16(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt16(cls, value: float) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt16(cls, value: str) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt16(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt16(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt16(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt16(cls, value: object, provider: IFormatProvider) -> int:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToInt16(cls, value: str, provider: IFormatProvider) -> int:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToInt16(cls, value: str, fromBase: int) -> int:
        """:param value:
        :param fromBase:
        :return:
        """
    @classmethod
    @overload
    def ToInt32(cls, value: bool) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt32(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt32(cls, value: Char) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt32(cls, value: DateTime) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt32(cls, value: Decimal) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt32(cls, value: float) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt32(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt32(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt32(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt32(cls, value: object) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt32(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt32(cls, value: float) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt32(cls, value: str) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt32(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt32(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt32(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt32(cls, value: object, provider: IFormatProvider) -> int:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToInt32(cls, value: str, provider: IFormatProvider) -> int:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToInt32(cls, value: str, fromBase: int) -> int:
        """:param value:
        :param fromBase:
        :return:
        """
    @classmethod
    @overload
    def ToInt64(cls, value: bool) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt64(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt64(cls, value: Char) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt64(cls, value: DateTime) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt64(cls, value: Decimal) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt64(cls, value: float) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt64(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt64(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt64(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt64(cls, value: object) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt64(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt64(cls, value: float) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt64(cls, value: str) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt64(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt64(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt64(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToInt64(cls, value: object, provider: IFormatProvider) -> int:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToInt64(cls, value: str, provider: IFormatProvider) -> int:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToInt64(cls, value: str, fromBase: int) -> int:
        """:param value:
        :param fromBase:
        :return:
        """
    @classmethod
    @overload
    def ToSByte(cls, value: bool) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSByte(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSByte(cls, value: Char) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSByte(cls, value: DateTime) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSByte(cls, value: Decimal) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSByte(cls, value: float) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSByte(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSByte(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSByte(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSByte(cls, value: object) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSByte(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSByte(cls, value: float) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSByte(cls, value: str) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSByte(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSByte(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSByte(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSByte(cls, value: object, provider: IFormatProvider) -> int:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToSByte(cls, value: str, provider: IFormatProvider) -> int:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToSByte(cls, value: str, fromBase: int) -> int:
        """:param value:
        :param fromBase:
        :return:
        """
    @classmethod
    @overload
    def ToSingle(cls, value: bool) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSingle(cls, value: int) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSingle(cls, value: Char) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSingle(cls, value: DateTime) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSingle(cls, value: Decimal) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSingle(cls, value: float) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSingle(cls, value: int) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSingle(cls, value: int) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSingle(cls, value: int) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSingle(cls, value: object) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSingle(cls, value: int) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSingle(cls, value: float) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSingle(cls, value: str) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSingle(cls, value: int) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSingle(cls, value: int) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSingle(cls, value: int) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSingle(cls, value: object, provider: IFormatProvider) -> float:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToSingle(cls, value: str, provider: IFormatProvider) -> float:
        """:param value:
        :param provider:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """:return:"""
    @classmethod
    @overload
    def ToString(cls, value: bool) -> str:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: int) -> str:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: Char) -> str:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: DateTime) -> str:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: Decimal) -> str:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: float) -> str:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: int) -> str:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: int) -> str:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: int) -> str:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: object) -> str:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: int) -> str:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: float) -> str:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: str) -> str:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: int) -> str:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: int) -> str:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: int) -> str:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: bool, provider: IFormatProvider) -> str:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: int, provider: IFormatProvider) -> str:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: int, toBase: int) -> str:
        """:param value:
        :param toBase:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: Char, provider: IFormatProvider) -> str:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: DateTime, provider: IFormatProvider) -> str:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: Decimal, provider: IFormatProvider) -> str:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: float, provider: IFormatProvider) -> str:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: int, provider: IFormatProvider) -> str:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: int, toBase: int) -> str:
        """:param value:
        :param toBase:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: int, provider: IFormatProvider) -> str:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: int, toBase: int) -> str:
        """:param value:
        :param toBase:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: int, provider: IFormatProvider) -> str:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: int, toBase: int) -> str:
        """:param value:
        :param toBase:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: object, provider: IFormatProvider) -> str:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: int, provider: IFormatProvider) -> str:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: float, provider: IFormatProvider) -> str:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: str, provider: IFormatProvider) -> str:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: int, provider: IFormatProvider) -> str:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: int, provider: IFormatProvider) -> str:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: int, provider: IFormatProvider) -> str:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToUInt16(cls, value: bool) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt16(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt16(cls, value: Char) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt16(cls, value: DateTime) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt16(cls, value: Decimal) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt16(cls, value: float) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt16(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt16(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt16(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt16(cls, value: object) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt16(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt16(cls, value: float) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt16(cls, value: str) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt16(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt16(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt16(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt16(cls, value: object, provider: IFormatProvider) -> int:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToUInt16(cls, value: str, provider: IFormatProvider) -> int:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToUInt16(cls, value: str, fromBase: int) -> int:
        """:param value:
        :param fromBase:
        :return:
        """
    @classmethod
    @overload
    def ToUInt32(cls, value: bool) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt32(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt32(cls, value: Char) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt32(cls, value: DateTime) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt32(cls, value: Decimal) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt32(cls, value: float) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt32(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt32(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt32(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt32(cls, value: object) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt32(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt32(cls, value: float) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt32(cls, value: str) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt32(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt32(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt32(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt32(cls, value: object, provider: IFormatProvider) -> int:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToUInt32(cls, value: str, provider: IFormatProvider) -> int:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToUInt32(cls, value: str, fromBase: int) -> int:
        """:param value:
        :param fromBase:
        :return:
        """
    @classmethod
    @overload
    def ToUInt64(cls, value: bool) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt64(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt64(cls, value: Char) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt64(cls, value: DateTime) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt64(cls, value: Decimal) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt64(cls, value: float) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt64(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt64(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt64(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt64(cls, value: object) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt64(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt64(cls, value: float) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt64(cls, value: str) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt64(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt64(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt64(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToUInt64(cls, value: object, provider: IFormatProvider) -> int:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToUInt64(cls, value: str, provider: IFormatProvider) -> int:
        """:param value:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToUInt64(cls, value: str, fromBase: int) -> int:
        """:param value:
        :param fromBase:
        :return:
        """

Converter: Callable[[TInput], TOutput] = ...
"""

:param input: 
:return: 
"""
CrossAppDomainDelegate: Callable[[], None] = ...
""""""
CtorDelegate: Callable[[object], None] = ...
"""

:param instance: 
"""

class CultureAwareComparer(
    StringComparer,
    IComparer[String],
    IEqualityComparer[String],
    IComparer,
    IEqualityComparer,
    IWellKnownStringEqualityComparer,
):
    """"""

    @classmethod
    @property
    def CurrentCulture(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def CurrentCultureIgnoreCase(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def InvariantCulture(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def InvariantCultureIgnoreCase(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def Ordinal(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def OrdinalIgnoreCase(cls) -> StringComparer:
        """:return:"""
    @overload
    def Compare(self, x: object, y: object) -> int:
        """:param x:
        :param y:
        :return:
        """
    @overload
    def Compare(self, x: str, y: str) -> int:
        """:param x:
        :param y:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """:param x:
        :param y:
        :return:
        """
    @overload
    def Equals(self, x: str, y: str) -> bool:
        """:param x:
        :param y:
        :return:
        """
    def GetEqualityComparerForSerialization(self) -> IEqualityComparer:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def GetHashCode(self, obj: str) -> int:
        """:param obj:
        :return:
        """
    def GetRandomizedEqualityComparer(self) -> IEqualityComparer:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class CultureAwareRandomizedComparer(
    StringComparer,
    IComparer[String],
    IEqualityComparer[String],
    IComparer,
    IEqualityComparer,
    IWellKnownStringEqualityComparer,
):
    """"""

    @classmethod
    @property
    def CurrentCulture(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def CurrentCultureIgnoreCase(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def InvariantCulture(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def InvariantCultureIgnoreCase(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def Ordinal(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def OrdinalIgnoreCase(cls) -> StringComparer:
        """:return:"""
    @overload
    def Compare(self, x: object, y: object) -> int:
        """:param x:
        :param y:
        :return:
        """
    @overload
    def Compare(self, x: str, y: str) -> int:
        """:param x:
        :param y:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """:param x:
        :param y:
        :return:
        """
    @overload
    def Equals(self, x: str, y: str) -> bool:
        """:param x:
        :param y:
        :return:
        """
    def GetEqualityComparerForSerialization(self) -> IEqualityComparer:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def GetHashCode(self, obj: str) -> int:
        """:param obj:
        :return:
        """
    def GetRandomizedEqualityComparer(self) -> IEqualityComparer:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class Currency(ValueType):
    """"""

    def __init__(self, value: Decimal):
        """:param value:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    def FromOACurrency(cls, cy: int) -> Currency:
        """:param cy:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def ToDecimal(cls, c: Currency) -> Decimal:
        """:param c:
        :return:
        """
    def ToOACurrency(self) -> int:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class CurrentSystemTimeZone(TimeZone):
    """"""

    @classmethod
    @property
    def CurrentTimeZone(cls) -> TimeZone:
        """:return:"""
    @property
    def DaylightName(self) -> str:
        """:return:"""
    @property
    def StandardName(self) -> str:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetDaylightChanges(self, year: int) -> DaylightTime:
        """:param year:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def GetUtcOffset(self, time: DateTime) -> TimeSpan:
        """:param time:
        :return:
        """
    def IsDaylightSavingTime(self, time: DateTime) -> bool:
        """:param time:
        :return:
        """
    def ToLocalTime(self, time: DateTime) -> DateTime:
        """:param time:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""
    def ToUniversalTime(self, time: DateTime) -> DateTime:
        """:param time:
        :return:
        """

class DBNull(Object, ISerializable, IConvertible):
    """"""

    Value: Final[ClassVar[DBNull]] = ...
    """
    
    :return: 
    """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeCode(self) -> TypeCode:
        """:return:"""
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """:param provider:
        :return:
        """
    def ToByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToChar(self, provider: IFormatProvider) -> Char:
        """:param provider:
        :return:
        """
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """:param provider:
        :return:
        """
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """:param provider:
        :return:
        """
    def ToDouble(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    def ToInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSingle(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """:param provider:
        :return:
        """
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """:param conversionType:
        :param provider:
        :return:
        """
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """

class DTSubString(ValueType):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

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
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

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

    MaxValue: Final[ClassVar[DateTime]] = ...
    """
    
    :return: 
    """
    MinValue: Final[ClassVar[DateTime]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, ticks: int):
        """:param ticks:"""
    @overload
    def __init__(self, ticks: int, kind: DateTimeKind):
        """:param ticks:
        :param kind:
        """
    @overload
    def __init__(self, year: int, month: int, day: int):
        """:param year:
        :param month:
        :param day:
        """
    @overload
    def __init__(self, year: int, month: int, day: int, calendar: Calendar):
        """:param year:
        :param month:
        :param day:
        :param calendar:
        """
    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int):
        """:param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        """
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
    ):
        """:param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param calendar:
        """
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
    ):
        """:param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param kind:
        """
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
    ):
        """:param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        """
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
    ):
        """:param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :param calendar:
        """
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
    ):
        """:param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :param kind:
        """
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
    ):
        """:param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :param calendar:
        :param kind:
        """
    @property
    def Date(self) -> DateTime:
        """:return:"""
    @property
    def Day(self) -> int:
        """:return:"""
    @property
    def DayOfWeek(self) -> DayOfWeek:
        """:return:"""
    @property
    def DayOfYear(self) -> int:
        """:return:"""
    @property
    def Hour(self) -> int:
        """:return:"""
    @property
    def Kind(self) -> DateTimeKind:
        """:return:"""
    @property
    def Millisecond(self) -> int:
        """:return:"""
    @property
    def Minute(self) -> int:
        """:return:"""
    @property
    def Month(self) -> int:
        """:return:"""
    @classmethod
    @property
    def Now(cls) -> DateTime:
        """:return:"""
    @property
    def Second(self) -> int:
        """:return:"""
    @property
    def Ticks(self) -> int:
        """:return:"""
    @property
    def TimeOfDay(self) -> TimeSpan:
        """:return:"""
    @classmethod
    @property
    def Today(cls) -> DateTime:
        """:return:"""
    @classmethod
    @property
    def UtcNow(cls) -> DateTime:
        """:return:"""
    @property
    def Year(self) -> int:
        """:return:"""
    def Add(self, value: TimeSpan) -> DateTime:
        """:param value:
        :return:
        """
    def AddDays(self, value: float) -> DateTime:
        """:param value:
        :return:
        """
    def AddHours(self, value: float) -> DateTime:
        """:param value:
        :return:
        """
    def AddMilliseconds(self, value: float) -> DateTime:
        """:param value:
        :return:
        """
    def AddMinutes(self, value: float) -> DateTime:
        """:param value:
        :return:
        """
    def AddMonths(self, months: int) -> DateTime:
        """:param months:
        :return:
        """
    def AddSeconds(self, value: float) -> DateTime:
        """:param value:
        :return:
        """
    def AddTicks(self, value: int) -> DateTime:
        """:param value:
        :return:
        """
    def AddYears(self, value: int) -> DateTime:
        """:param value:
        :return:
        """
    @classmethod
    def Compare(cls, t1: DateTime, t2: DateTime) -> int:
        """:param t1:
        :param t2:
        :return:
        """
    @overload
    def CompareTo(self, other: DateTime) -> int:
        """:param other:
        :return:
        """
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @classmethod
    def DaysInMonth(cls, year: int, month: int) -> int:
        """:param year:
        :param month:
        :return:
        """
    @overload
    def Equals(self, other: DateTime) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    @overload
    def Equals(cls, t1: DateTime, t2: DateTime) -> bool:
        """:param t1:
        :param t2:
        :return:
        """
    @classmethod
    def FromBinary(cls, dateData: int) -> DateTime:
        """:param dateData:
        :return:
        """
    @classmethod
    def FromFileTime(cls, fileTime: int) -> DateTime:
        """:param fileTime:
        :return:
        """
    @classmethod
    def FromFileTimeUtc(cls, fileTime: int) -> DateTime:
        """:param fileTime:
        :return:
        """
    @classmethod
    def FromOADate(cls, d: float) -> DateTime:
        """:param d:
        :return:
        """
    @overload
    def GetDateTimeFormats(self) -> Array[str]:
        """:return:"""
    @overload
    def GetDateTimeFormats(self, format: Char) -> Array[str]:
        """:param format:
        :return:
        """
    @overload
    def GetDateTimeFormats(self, provider: IFormatProvider) -> Array[str]:
        """:param provider:
        :return:
        """
    @overload
    def GetDateTimeFormats(self, format: Char, provider: IFormatProvider) -> Array[str]:
        """:param format:
        :param provider:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeCode(self) -> TypeCode:
        """:return:"""
    def IsDaylightSavingTime(self) -> bool:
        """:return:"""
    @classmethod
    def IsLeapYear(cls, year: int) -> bool:
        """:param year:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str) -> DateTime:
        """:param s:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider) -> DateTime:
        """:param s:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider, styles: DateTimeStyles) -> DateTime:
        """:param s:
        :param provider:
        :param styles:
        :return:
        """
    @classmethod
    @overload
    def ParseExact(cls, s: str, format: str, provider: IFormatProvider) -> DateTime:
        """:param s:
        :param format:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ParseExact(
        cls,
        s: str,
        formats: Array[str],
        provider: IFormatProvider,
        style: DateTimeStyles,
    ) -> DateTime:
        """:param s:
        :param formats:
        :param provider:
        :param style:
        :return:
        """
    @classmethod
    @overload
    def ParseExact(
        cls, s: str, format: str, provider: IFormatProvider, style: DateTimeStyles
    ) -> DateTime:
        """:param s:
        :param format:
        :param provider:
        :param style:
        :return:
        """
    @classmethod
    def SpecifyKind(cls, value: DateTime, kind: DateTimeKind) -> DateTime:
        """:param value:
        :param kind:
        :return:
        """
    @overload
    def Subtract(self, value: DateTime) -> TimeSpan:
        """:param value:
        :return:
        """
    @overload
    def Subtract(self, value: TimeSpan) -> DateTime:
        """:param value:
        :return:
        """
    def ToBinary(self) -> int:
        """:return:"""
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """:param provider:
        :return:
        """
    def ToByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToChar(self, provider: IFormatProvider) -> Char:
        """:param provider:
        :return:
        """
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """:param provider:
        :return:
        """
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """:param provider:
        :return:
        """
    def ToDouble(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    def ToFileTime(self) -> int:
        """:return:"""
    def ToFileTimeUtc(self) -> int:
        """:return:"""
    def ToInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToLocalTime(self) -> DateTime:
        """:return:"""
    def ToLongDateString(self) -> str:
        """:return:"""
    def ToLongTimeString(self) -> str:
        """:return:"""
    def ToOADate(self) -> float:
        """:return:"""
    def ToSByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToShortDateString(self) -> str:
        """:return:"""
    def ToShortTimeString(self) -> str:
        """:return:"""
    def ToSingle(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self, format: str) -> str:
        """:param format:
        :return:
        """
    @overload
    def ToString(self, format: str, formatProvider: IFormatProvider) -> str:
        """:param format:
        :param formatProvider:
        :return:
        """
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """:param conversionType:
        :param provider:
        :return:
        """
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUniversalTime(self) -> DateTime:
        """:return:"""
    @classmethod
    @overload
    def TryParse(cls, s: str, result: DateTime) -> Tuple[bool, DateTime]:
        """:param s:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryParse(
        cls, s: str, provider: IFormatProvider, styles: DateTimeStyles, result: DateTime
    ) -> Tuple[bool, DateTime]:
        """:param s:
        :param provider:
        :param styles:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryParseExact(
        cls,
        s: str,
        formats: Array[str],
        provider: IFormatProvider,
        style: DateTimeStyles,
        result: DateTime,
    ) -> Tuple[bool, DateTime]:
        """:param s:
        :param formats:
        :param provider:
        :param style:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryParseExact(
        cls,
        s: str,
        format: str,
        provider: IFormatProvider,
        style: DateTimeStyles,
        result: DateTime,
    ) -> Tuple[bool, DateTime]:
        """:param s:
        :param format:
        :param provider:
        :param style:
        :param result:
        :return:
        """
    def __add__(self, other: TimeSpan) -> DateTime:
        """:param other:
        :return:
        """
    def __eq__(self, other: DateTime) -> bool:
        """:param other:
        :return:
        """
    def __ge__(self, other: DateTime) -> bool:
        """:param other:
        :return:
        """
    def __gt__(self, other: DateTime) -> bool:
        """:param other:
        :return:
        """
    def __le__(self, other: DateTime) -> bool:
        """:param other:
        :return:
        """
    def __lt__(self, other: DateTime) -> bool:
        """:param other:
        :return:
        """
    def __ne__(self, other: DateTime) -> bool:
        """:param other:
        :return:
        """
    @overload
    def __sub__(self, other: DateTime) -> TimeSpan:
        """:param other:
        :return:
        """
    @overload
    def __sub__(self, other: TimeSpan) -> DateTime:
        """:param other:
        :return:
        """
    @classmethod
    def op_Addition(cls, d: DateTime, t: TimeSpan) -> DateTime:
        """:param d:
        :param t:
        :return:
        """
    @classmethod
    def op_Equality(cls, d1: DateTime, d2: DateTime) -> bool:
        """:param d1:
        :param d2:
        :return:
        """
    @classmethod
    def op_GreaterThan(cls, t1: DateTime, t2: DateTime) -> bool:
        """:param t1:
        :param t2:
        :return:
        """
    @classmethod
    def op_GreaterThanOrEqual(cls, t1: DateTime, t2: DateTime) -> bool:
        """:param t1:
        :param t2:
        :return:
        """
    @classmethod
    def op_Inequality(cls, d1: DateTime, d2: DateTime) -> bool:
        """:param d1:
        :param d2:
        :return:
        """
    @classmethod
    def op_LessThan(cls, t1: DateTime, t2: DateTime) -> bool:
        """:param t1:
        :param t2:
        :return:
        """
    @classmethod
    def op_LessThanOrEqual(cls, t1: DateTime, t2: DateTime) -> bool:
        """:param t1:
        :param t2:
        :return:
        """
    @classmethod
    @overload
    def op_Subtraction(cls, d1: DateTime, d2: DateTime) -> TimeSpan:
        """:param d1:
        :param d2:
        :return:
        """
    @classmethod
    @overload
    def op_Subtraction(cls, d: DateTime, t: TimeSpan) -> DateTime:
        """:param d:
        :param t:
        :return:
        """

class DateTimeFormat(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

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

    MaxValue: Final[ClassVar[DateTimeOffset]] = ...
    """
    
    :return: 
    """
    MinValue: Final[ClassVar[DateTimeOffset]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, dateTime: DateTime):
        """:param dateTime:"""
    @overload
    def __init__(self, dateTime: DateTime, offset: TimeSpan):
        """:param dateTime:
        :param offset:
        """
    @overload
    def __init__(self, ticks: int, offset: TimeSpan):
        """:param ticks:
        :param offset:
        """
    @overload
    def __init__(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        offset: TimeSpan,
    ):
        """:param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param offset:
        """
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
    ):
        """:param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :param offset:
        """
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
    ):
        """:param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :param calendar:
        :param offset:
        """
    @property
    def Date(self) -> DateTime:
        """:return:"""
    @property
    def DateTime(self) -> DateTime:
        """:return:"""
    @property
    def Day(self) -> int:
        """:return:"""
    @property
    def DayOfWeek(self) -> DayOfWeek:
        """:return:"""
    @property
    def DayOfYear(self) -> int:
        """:return:"""
    @property
    def Hour(self) -> int:
        """:return:"""
    @property
    def LocalDateTime(self) -> DateTime:
        """:return:"""
    @property
    def Millisecond(self) -> int:
        """:return:"""
    @property
    def Minute(self) -> int:
        """:return:"""
    @property
    def Month(self) -> int:
        """:return:"""
    @classmethod
    @property
    def Now(cls) -> DateTimeOffset:
        """:return:"""
    @property
    def Offset(self) -> TimeSpan:
        """:return:"""
    @property
    def Second(self) -> int:
        """:return:"""
    @property
    def Ticks(self) -> int:
        """:return:"""
    @property
    def TimeOfDay(self) -> TimeSpan:
        """:return:"""
    @property
    def UtcDateTime(self) -> DateTime:
        """:return:"""
    @classmethod
    @property
    def UtcNow(cls) -> DateTimeOffset:
        """:return:"""
    @property
    def UtcTicks(self) -> int:
        """:return:"""
    @property
    def Year(self) -> int:
        """:return:"""
    def Add(self, timeSpan: TimeSpan) -> DateTimeOffset:
        """:param timeSpan:
        :return:
        """
    def AddDays(self, days: float) -> DateTimeOffset:
        """:param days:
        :return:
        """
    def AddHours(self, hours: float) -> DateTimeOffset:
        """:param hours:
        :return:
        """
    def AddMilliseconds(self, milliseconds: float) -> DateTimeOffset:
        """:param milliseconds:
        :return:
        """
    def AddMinutes(self, minutes: float) -> DateTimeOffset:
        """:param minutes:
        :return:
        """
    def AddMonths(self, months: int) -> DateTimeOffset:
        """:param months:
        :return:
        """
    def AddSeconds(self, seconds: float) -> DateTimeOffset:
        """:param seconds:
        :return:
        """
    def AddTicks(self, ticks: int) -> DateTimeOffset:
        """:param ticks:
        :return:
        """
    def AddYears(self, years: int) -> DateTimeOffset:
        """:param years:
        :return:
        """
    @classmethod
    def Compare(cls, first: DateTimeOffset, second: DateTimeOffset) -> int:
        """:param first:
        :param second:
        :return:
        """
    @overload
    def CompareTo(self, other: DateTimeOffset) -> int:
        """:param other:
        :return:
        """
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: DateTimeOffset) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    @overload
    def Equals(cls, first: DateTimeOffset, second: DateTimeOffset) -> bool:
        """:param first:
        :param second:
        :return:
        """
    def EqualsExact(self, other: DateTimeOffset) -> bool:
        """:param other:
        :return:
        """
    @classmethod
    def FromFileTime(cls, fileTime: int) -> DateTimeOffset:
        """:param fileTime:
        :return:
        """
    @classmethod
    def FromUnixTimeMilliseconds(cls, milliseconds: int) -> DateTimeOffset:
        """:param milliseconds:
        :return:
        """
    @classmethod
    def FromUnixTimeSeconds(cls, seconds: int) -> DateTimeOffset:
        """:param seconds:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    def GetType(self) -> Type:
        """:return:"""
    def OnDeserialization(self, sender: object) -> None:
        """:param sender:"""
    @classmethod
    @overload
    def Parse(cls, input: str) -> DateTimeOffset:
        """:param input:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, input: str, formatProvider: IFormatProvider) -> DateTimeOffset:
        """:param input:
        :param formatProvider:
        :return:
        """
    @classmethod
    @overload
    def Parse(
        cls, input: str, formatProvider: IFormatProvider, styles: DateTimeStyles
    ) -> DateTimeOffset:
        """:param input:
        :param formatProvider:
        :param styles:
        :return:
        """
    @classmethod
    @overload
    def ParseExact(cls, input: str, format: str, formatProvider: IFormatProvider) -> DateTimeOffset:
        """:param input:
        :param format:
        :param formatProvider:
        :return:
        """
    @classmethod
    @overload
    def ParseExact(
        cls,
        input: str,
        formats: Array[str],
        formatProvider: IFormatProvider,
        styles: DateTimeStyles,
    ) -> DateTimeOffset:
        """:param input:
        :param formats:
        :param formatProvider:
        :param styles:
        :return:
        """
    @classmethod
    @overload
    def ParseExact(
        cls,
        input: str,
        format: str,
        formatProvider: IFormatProvider,
        styles: DateTimeStyles,
    ) -> DateTimeOffset:
        """:param input:
        :param format:
        :param formatProvider:
        :param styles:
        :return:
        """
    @overload
    def Subtract(self, value: DateTimeOffset) -> TimeSpan:
        """:param value:
        :return:
        """
    @overload
    def Subtract(self, value: TimeSpan) -> DateTimeOffset:
        """:param value:
        :return:
        """
    def ToFileTime(self) -> int:
        """:return:"""
    def ToLocalTime(self) -> DateTimeOffset:
        """:return:"""
    def ToOffset(self, offset: TimeSpan) -> DateTimeOffset:
        """:param offset:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, formatProvider: IFormatProvider) -> str:
        """:param formatProvider:
        :return:
        """
    @overload
    def ToString(self, format: str) -> str:
        """:param format:
        :return:
        """
    @overload
    def ToString(self, format: str, formatProvider: IFormatProvider) -> str:
        """:param format:
        :param formatProvider:
        :return:
        """
    def ToUniversalTime(self) -> DateTimeOffset:
        """:return:"""
    def ToUnixTimeMilliseconds(self) -> int:
        """:return:"""
    def ToUnixTimeSeconds(self) -> int:
        """:return:"""
    @classmethod
    @overload
    def TryParse(cls, input: str, result: DateTimeOffset) -> Tuple[bool, DateTimeOffset]:
        """:param input:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryParse(
        cls,
        input: str,
        formatProvider: IFormatProvider,
        styles: DateTimeStyles,
        result: DateTimeOffset,
    ) -> Tuple[bool, DateTimeOffset]:
        """:param input:
        :param formatProvider:
        :param styles:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryParseExact(
        cls,
        input: str,
        formats: Array[str],
        formatProvider: IFormatProvider,
        styles: DateTimeStyles,
        result: DateTimeOffset,
    ) -> Tuple[bool, DateTimeOffset]:
        """:param input:
        :param formats:
        :param formatProvider:
        :param styles:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryParseExact(
        cls,
        input: str,
        format: str,
        formatProvider: IFormatProvider,
        styles: DateTimeStyles,
        result: DateTimeOffset,
    ) -> Tuple[bool, DateTimeOffset]:
        """:param input:
        :param format:
        :param formatProvider:
        :param styles:
        :param result:
        :return:
        """
    def __add__(self, other: TimeSpan) -> DateTimeOffset:
        """:param other:
        :return:
        """
    def __eq__(self, other: DateTimeOffset) -> bool:
        """:param other:
        :return:
        """
    def __ge__(self, other: DateTimeOffset) -> bool:
        """:param other:
        :return:
        """
    def __gt__(self, other: DateTimeOffset) -> bool:
        """:param other:
        :return:
        """
    def __le__(self, other: DateTimeOffset) -> bool:
        """:param other:
        :return:
        """
    def __lt__(self, other: DateTimeOffset) -> bool:
        """:param other:
        :return:
        """
    def __ne__(self, other: DateTimeOffset) -> bool:
        """:param other:
        :return:
        """
    @overload
    def __sub__(self, other: DateTimeOffset) -> TimeSpan:
        """:param other:
        :return:
        """
    @overload
    def __sub__(self, other: TimeSpan) -> DateTimeOffset:
        """:param other:
        :return:
        """
    @classmethod
    def op_Addition(cls, dateTimeOffset: DateTimeOffset, timeSpan: TimeSpan) -> DateTimeOffset:
        """:param dateTimeOffset:
        :param timeSpan:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: DateTimeOffset, right: DateTimeOffset) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    def op_GreaterThan(cls, left: DateTimeOffset, right: DateTimeOffset) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    def op_GreaterThanOrEqual(cls, left: DateTimeOffset, right: DateTimeOffset) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Implicit(cls, dateTime: DateTime) -> DateTimeOffset:
        """:param dateTime:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: DateTimeOffset, right: DateTimeOffset) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    def op_LessThan(cls, left: DateTimeOffset, right: DateTimeOffset) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    def op_LessThanOrEqual(cls, left: DateTimeOffset, right: DateTimeOffset) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def op_Subtraction(cls, left: DateTimeOffset, right: DateTimeOffset) -> TimeSpan:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def op_Subtraction(cls, dateTimeOffset: DateTimeOffset, timeSpan: TimeSpan) -> DateTimeOffset:
        """:param dateTimeOffset:
        :param timeSpan:
        :return:
        """

class DateTimeParse(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class DateTimeRawInfo(ValueType):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class DateTimeResult(ValueType):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class DateTimeToken(ValueType):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

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

    MaxValue: Final[ClassVar[Decimal]] = ...
    """
    
    :return: 
    """
    MinValue: Final[ClassVar[Decimal]] = ...
    """
    
    :return: 
    """
    MinusOne: Final[ClassVar[Decimal]] = ...
    """
    
    :return: 
    """
    One: Final[ClassVar[Decimal]] = ...
    """
    
    :return: 
    """
    Zero: Final[ClassVar[Decimal]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, bits: Array[int]):
        """:param bits:"""
    @overload
    def __init__(self, value: float):
        """:param value:"""
    @overload
    def __init__(self, value: int):
        """:param value:"""
    @overload
    def __init__(self, value: int):
        """:param value:"""
    @overload
    def __init__(self, value: float):
        """:param value:"""
    @overload
    def __init__(self, value: int):
        """:param value:"""
    @overload
    def __init__(self, value: int):
        """:param value:"""
    @overload
    def __init__(self, lo: int, mid: int, hi: int, isNegative: bool, scale: int):
        """:param lo:
        :param mid:
        :param hi:
        :param isNegative:
        :param scale:
        """
    @classmethod
    def Add(cls, d1: Decimal, d2: Decimal) -> Decimal:
        """:param d1:
        :param d2:
        :return:
        """
    @classmethod
    def Ceiling(cls, d: Decimal) -> Decimal:
        """:param d:
        :return:
        """
    @classmethod
    def Compare(cls, d1: Decimal, d2: Decimal) -> int:
        """:param d1:
        :param d2:
        :return:
        """
    @overload
    def CompareTo(self, other: Decimal) -> int:
        """:param other:
        :return:
        """
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @classmethod
    def Divide(cls, d1: Decimal, d2: Decimal) -> Decimal:
        """:param d1:
        :param d2:
        :return:
        """
    @overload
    def Equals(self, other: Decimal) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    @overload
    def Equals(cls, d1: Decimal, d2: Decimal) -> bool:
        """:param d1:
        :param d2:
        :return:
        """
    @classmethod
    def Floor(cls, d: Decimal) -> Decimal:
        """:param d:
        :return:
        """
    @classmethod
    def FromOACurrency(cls, cy: int) -> Decimal:
        """:param cy:
        :return:
        """
    @classmethod
    def GetBits(cls, d: Decimal) -> Array[int]:
        """:param d:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeCode(self) -> TypeCode:
        """:return:"""
    @classmethod
    def Multiply(cls, d1: Decimal, d2: Decimal) -> Decimal:
        """:param d1:
        :param d2:
        :return:
        """
    @classmethod
    def Negate(cls, d: Decimal) -> Decimal:
        """:param d:
        :return:
        """
    def OnDeserialization(self, sender: object) -> None:
        """:param sender:"""
    @classmethod
    @overload
    def Parse(cls, s: str) -> Decimal:
        """:param s:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles) -> Decimal:
        """:param s:
        :param style:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider) -> Decimal:
        """:param s:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles, provider: IFormatProvider) -> Decimal:
        """:param s:
        :param style:
        :param provider:
        :return:
        """
    @classmethod
    def Remainder(cls, d1: Decimal, d2: Decimal) -> Decimal:
        """:param d1:
        :param d2:
        :return:
        """
    @classmethod
    @overload
    def Round(cls, d: Decimal) -> Decimal:
        """:param d:
        :return:
        """
    @classmethod
    @overload
    def Round(cls, d: Decimal, decimals: int) -> Decimal:
        """:param d:
        :param decimals:
        :return:
        """
    @classmethod
    @overload
    def Round(cls, d: Decimal, mode: MidpointRounding) -> Decimal:
        """:param d:
        :param mode:
        :return:
        """
    @classmethod
    @overload
    def Round(cls, d: Decimal, decimals: int, mode: MidpointRounding) -> Decimal:
        """:param d:
        :param decimals:
        :param mode:
        :return:
        """
    @classmethod
    def Subtract(cls, d1: Decimal, d2: Decimal) -> Decimal:
        """:param d1:
        :param d2:
        :return:
        """
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """:param provider:
        :return:
        """
    @classmethod
    @overload
    def ToByte(cls, value: Decimal) -> int:
        """:param value:
        :return:
        """
    @overload
    def ToByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToChar(self, provider: IFormatProvider) -> Char:
        """:param provider:
        :return:
        """
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """:param provider:
        :return:
        """
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """:param provider:
        :return:
        """
    @classmethod
    @overload
    def ToDouble(cls, d: Decimal) -> float:
        """:param d:
        :return:
        """
    @overload
    def ToDouble(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    @classmethod
    @overload
    def ToInt16(cls, value: Decimal) -> int:
        """:param value:
        :return:
        """
    @overload
    def ToInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    @classmethod
    @overload
    def ToInt32(cls, d: Decimal) -> int:
        """:param d:
        :return:
        """
    @overload
    def ToInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    @classmethod
    @overload
    def ToInt64(cls, d: Decimal) -> int:
        """:param d:
        :return:
        """
    @overload
    def ToInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    @classmethod
    def ToOACurrency(cls, value: Decimal) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToSByte(cls, value: Decimal) -> int:
        """:param value:
        :return:
        """
    @overload
    def ToSByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    @classmethod
    @overload
    def ToSingle(cls, d: Decimal) -> float:
        """:param d:
        :return:
        """
    @overload
    def ToSingle(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self, format: str) -> str:
        """:param format:
        :return:
        """
    @overload
    def ToString(self, format: str, formatProvider: IFormatProvider) -> str:
        """:param format:
        :param formatProvider:
        :return:
        """
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """:param conversionType:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def ToUInt16(cls, value: Decimal) -> int:
        """:param value:
        :return:
        """
    @overload
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    @classmethod
    @overload
    def ToUInt32(cls, d: Decimal) -> int:
        """:param d:
        :return:
        """
    @overload
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    @classmethod
    @overload
    def ToUInt64(cls, d: Decimal) -> int:
        """:param d:
        :return:
        """
    @overload
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    @classmethod
    def Truncate(cls, d: Decimal) -> Decimal:
        """:param d:
        :return:
        """
    @classmethod
    @overload
    def TryParse(cls, s: str, result: Decimal) -> Tuple[bool, Decimal]:
        """:param s:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryParse(
        cls, s: str, style: NumberStyles, provider: IFormatProvider, result: Decimal
    ) -> Tuple[bool, Decimal]:
        """:param s:
        :param style:
        :param provider:
        :param result:
        :return:
        """
    def __add__(self, other: Decimal) -> Decimal:
        """:param other:
        :return:
        """
    def __eq__(self, other: Decimal) -> bool:
        """:param other:
        :return:
        """
    def __ge__(self, other: Decimal) -> bool:
        """:param other:
        :return:
        """
    def __gt__(self, other: Decimal) -> bool:
        """:param other:
        :return:
        """
    def __le__(self, other: Decimal) -> bool:
        """:param other:
        :return:
        """
    def __lt__(self, other: Decimal) -> bool:
        """:param other:
        :return:
        """
    def __mod__(self, other: Decimal) -> Decimal:
        """:param other:
        :return:
        """
    def __mul__(self, other: Decimal) -> Decimal:
        """:param other:
        :return:
        """
    def __ne__(self, other: Decimal) -> bool:
        """:param other:
        :return:
        """
    def __neg__(self) -> Decimal:
        """:return:"""
    def __pos__(self) -> Decimal:
        """:return:"""
    def __sub__(self, other: Decimal) -> Decimal:
        """:param other:
        :return:
        """
    def __truediv__(self, other: Decimal) -> Decimal:
        """:param other:
        :return:
        """
    @classmethod
    def op_Addition(cls, d1: Decimal, d2: Decimal) -> Decimal:
        """:param d1:
        :param d2:
        :return:
        """
    @classmethod
    def op_Decrement(cls, d: Decimal) -> Decimal:
        """:param d:
        :return:
        """
    @classmethod
    def op_Division(cls, d1: Decimal, d2: Decimal) -> Decimal:
        """:param d1:
        :param d2:
        :return:
        """
    @classmethod
    def op_Equality(cls, d1: Decimal, d2: Decimal) -> bool:
        """:param d1:
        :param d2:
        :return:
        """
    @classmethod
    @overload
    def op_Explicit(cls, value: Decimal) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def op_Explicit(cls, value: float) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def op_Explicit(cls, value: float) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    def op_GreaterThan(cls, d1: Decimal, d2: Decimal) -> bool:
        """:param d1:
        :param d2:
        :return:
        """
    @classmethod
    def op_GreaterThanOrEqual(cls, d1: Decimal, d2: Decimal) -> bool:
        """:param d1:
        :param d2:
        :return:
        """
    @classmethod
    @overload
    def op_Implicit(cls, value: int) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def op_Implicit(cls, value: Char) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def op_Implicit(cls, value: int) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def op_Implicit(cls, value: int) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def op_Implicit(cls, value: int) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def op_Implicit(cls, value: int) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def op_Implicit(cls, value: int) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def op_Implicit(cls, value: int) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def op_Implicit(cls, value: int) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    def op_Increment(cls, d: Decimal) -> Decimal:
        """:param d:
        :return:
        """
    @classmethod
    def op_Inequality(cls, d1: Decimal, d2: Decimal) -> bool:
        """:param d1:
        :param d2:
        :return:
        """
    @classmethod
    def op_LessThan(cls, d1: Decimal, d2: Decimal) -> bool:
        """:param d1:
        :param d2:
        :return:
        """
    @classmethod
    def op_LessThanOrEqual(cls, d1: Decimal, d2: Decimal) -> bool:
        """:param d1:
        :param d2:
        :return:
        """
    @classmethod
    def op_Modulus(cls, d1: Decimal, d2: Decimal) -> Decimal:
        """:param d1:
        :param d2:
        :return:
        """
    @classmethod
    def op_Multiply(cls, d1: Decimal, d2: Decimal) -> Decimal:
        """:param d1:
        :param d2:
        :return:
        """
    @classmethod
    def op_Subtraction(cls, d1: Decimal, d2: Decimal) -> Decimal:
        """:param d1:
        :param d2:
        :return:
        """
    @classmethod
    def op_UnaryNegation(cls, d: Decimal) -> Decimal:
        """:param d:
        :return:
        """
    @classmethod
    def op_UnaryPlus(cls, d: Decimal) -> Decimal:
        """:param d:
        :return:
        """

class DefaultBinder(Binder):
    """"""

    def __init__(self):
        """"""
    def BindToField(
        self,
        bindingAttr: BindingFlags,
        match: Array[FieldInfo],
        value: object,
        culture: CultureInfo,
    ) -> FieldInfo:
        """:param bindingAttr:
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
        """:param bindingAttr:
        :param match:
        :param args:
        :param modifiers:
        :param culture:
        :param names:
        :param state:
        :return:
        """
    def ChangeType(self, value: object, type: Type, culture: CultureInfo) -> object:
        """:param value:
        :param type:
        :param culture:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    def ExactBinding(
        cls,
        match: Array[MethodBase],
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodBase:
        """:param match:
        :param types:
        :param modifiers:
        :return:
        """
    @classmethod
    def ExactPropertyBinding(
        cls,
        match: Array[PropertyInfo],
        returnType: Type,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> PropertyInfo:
        """:param match:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ReorderArgumentArray(self, args: object, state: object) -> None:
        """:param args:
        :param state:
        """
    def SelectMethod(
        self,
        bindingAttr: BindingFlags,
        match: Array[MethodBase],
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodBase:
        """:param bindingAttr:
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
        """:param bindingAttr:
        :param match:
        :param returnType:
        :param indexes:
        :param modifiers:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class Delegate(ABC, Object, ISerializable, ICloneable):
    """"""

    @property
    def Method(self) -> MethodInfo:
        """:return:"""
    @property
    def Target(self) -> object:
        """:return:"""
    def Clone(self) -> object:
        """:return:"""
    @classmethod
    @overload
    def Combine(cls, delegates: Array[Delegate]) -> Delegate:
        """:param delegates:
        :return:
        """
    @classmethod
    @overload
    def Combine(cls, a: Delegate, b: Delegate) -> Delegate:
        """:param a:
        :param b:
        :return:
        """
    @classmethod
    @overload
    def CreateDelegate(cls, type: Type, method: MethodInfo) -> Delegate:
        """:param type:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def CreateDelegate(cls, type: Type, method: MethodInfo, throwOnBindFailure: bool) -> Delegate:
        """:param type:
        :param method:
        :param throwOnBindFailure:
        :return:
        """
    @classmethod
    @overload
    def CreateDelegate(cls, type: Type, firstArgument: object, method: MethodInfo) -> Delegate:
        """:param type:
        :param firstArgument:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def CreateDelegate(cls, type: Type, target: object, method: str) -> Delegate:
        """:param type:
        :param target:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def CreateDelegate(cls, type: Type, target: Type, method: str) -> Delegate:
        """:param type:
        :param target:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def CreateDelegate(
        cls,
        type: Type,
        firstArgument: object,
        method: MethodInfo,
        throwOnBindFailure: bool,
    ) -> Delegate:
        """:param type:
        :param firstArgument:
        :param method:
        :param throwOnBindFailure:
        :return:
        """
    @classmethod
    @overload
    def CreateDelegate(cls, type: Type, target: object, method: str, ignoreCase: bool) -> Delegate:
        """:param type:
        :param target:
        :param method:
        :param ignoreCase:
        :return:
        """
    @classmethod
    @overload
    def CreateDelegate(cls, type: Type, target: Type, method: str, ignoreCase: bool) -> Delegate:
        """:param type:
        :param target:
        :param method:
        :param ignoreCase:
        :return:
        """
    @classmethod
    @overload
    def CreateDelegate(
        cls,
        type: Type,
        target: object,
        method: str,
        ignoreCase: bool,
        throwOnBindFailure: bool,
    ) -> Delegate:
        """:param type:
        :param target:
        :param method:
        :param ignoreCase:
        :param throwOnBindFailure:
        :return:
        """
    @classmethod
    @overload
    def CreateDelegate(
        cls,
        type: Type,
        target: Type,
        method: str,
        ignoreCase: bool,
        throwOnBindFailure: bool,
    ) -> Delegate:
        """:param type:
        :param target:
        :param method:
        :param ignoreCase:
        :param throwOnBindFailure:
        :return:
        """
    def DynamicInvoke(self, args: Array[object]) -> object:
        """:param args:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetInvocationList(self) -> Array[Delegate]:
        """:return:"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def Remove(cls, source: Delegate, value: Delegate) -> Delegate:
        """:param source:
        :param value:
        :return:
        """
    @classmethod
    def RemoveAll(cls, source: Delegate, value: Delegate) -> Delegate:
        """:param source:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""
    def __eq__(self, other: Delegate) -> bool:
        """:param other:
        :return:
        """
    def __ne__(self, other: Delegate) -> bool:
        """:param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, d1: Delegate, d2: Delegate) -> bool:
        """:param d1:
        :param d2:
        :return:
        """
    @classmethod
    def op_Inequality(cls, d1: Delegate, d2: Delegate) -> bool:
        """:param d1:
        :param d2:
        :return:
        """

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
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    def GetRealObject(self, context: StreamingContext) -> object:
        """:param context:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class DivideByZeroException(ArithmeticException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class DllNotFoundException(TypeLoadException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, inner: Exception):
        """:param message:
        :param inner:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @property
    def TypeName(self) -> str:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class DomainNameHelper(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class Double(
    ValueType,
    IComparable,
    IComparable[Double],
    IConvertible,
    IEquatable[Double],
    IFormattable,
):
    """"""

    Epsilon: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    MaxValue: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    MinValue: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    NaN: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    NegativeInfinity: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    PositiveInfinity: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    @overload
    def CompareTo(self, other: float) -> int:
        """:param other:
        :return:
        """
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: float) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeCode(self) -> TypeCode:
        """:return:"""
    @classmethod
    def IsInfinity(cls, d: float) -> bool:
        """:param d:
        :return:
        """
    @classmethod
    def IsNaN(cls, d: float) -> bool:
        """:param d:
        :return:
        """
    @classmethod
    def IsNegativeInfinity(cls, d: float) -> bool:
        """:param d:
        :return:
        """
    @classmethod
    def IsPositiveInfinity(cls, d: float) -> bool:
        """:param d:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str) -> float:
        """:param s:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles) -> float:
        """:param s:
        :param style:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider) -> float:
        """:param s:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles, provider: IFormatProvider) -> float:
        """:param s:
        :param style:
        :param provider:
        :return:
        """
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """:param provider:
        :return:
        """
    def ToByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToChar(self, provider: IFormatProvider) -> Char:
        """:param provider:
        :return:
        """
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """:param provider:
        :return:
        """
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """:param provider:
        :return:
        """
    def ToDouble(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    def ToInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSingle(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self, format: str) -> str:
        """:param format:
        :return:
        """
    @overload
    def ToString(self, format: str, formatProvider: IFormatProvider) -> str:
        """:param format:
        :param formatProvider:
        :return:
        """
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """:param conversionType:
        :param provider:
        :return:
        """
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    @classmethod
    @overload
    def TryParse(cls, s: str, result: float) -> Tuple[bool, float]:
        """:param s:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryParse(
        cls, s: str, style: NumberStyles, provider: IFormatProvider, result: float
    ) -> Tuple[bool, float]:
        """:param s:
        :param style:
        :param provider:
        :param result:
        :return:
        """
    def __eq__(self, other: float) -> bool:
        """:param other:
        :return:
        """
    def __ge__(self, other: float) -> bool:
        """:param other:
        :return:
        """
    def __gt__(self, other: float) -> bool:
        """:param other:
        :return:
        """
    def __le__(self, other: float) -> bool:
        """:param other:
        :return:
        """
    def __lt__(self, other: float) -> bool:
        """:param other:
        :return:
        """
    def __ne__(self, other: float) -> bool:
        """:param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: float, right: float) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    def op_GreaterThan(cls, left: float, right: float) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    def op_GreaterThanOrEqual(cls, left: float, right: float) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: float, right: float) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    def op_LessThan(cls, left: float, right: float) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    def op_LessThanOrEqual(cls, left: float, right: float) -> bool:
        """:param left:
        :param right:
        :return:
        """

class DuplicateWaitObjectException(ArgumentException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, parameterName: str):
        """:param parameterName:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @overload
    def __init__(self, parameterName: str, message: str):
        """:param parameterName:
        :param message:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def ParamName(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class Empty(Object, ISerializable):
    """"""

    Value: Final[ClassVar[Empty]] = ...
    """
    
    :return: 
    """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class EntryPointNotFoundException(TypeLoadException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, inner: Exception):
        """:param message:
        :param inner:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @property
    def TypeName(self) -> str:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class Enum(ABC, ValueType, IComparable, IConvertible, IFormattable):
    """"""

    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    def Format(cls, enumType: Type, value: object, format: str) -> str:
        """:param enumType:
        :param value:
        :param format:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    @classmethod
    def GetName(cls, enumType: Type, value: object) -> str:
        """:param enumType:
        :param value:
        :return:
        """
    @classmethod
    def GetNames(cls, enumType: Type) -> Array[str]:
        """:param enumType:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeCode(self) -> TypeCode:
        """:return:"""
    @classmethod
    def GetUnderlyingType(cls, enumType: Type) -> Type:
        """:param enumType:
        :return:
        """
    @classmethod
    def GetValues(cls, enumType: Type) -> Array:
        """:param enumType:
        :return:
        """
    def HasFlag(self, flag: Enum) -> bool:
        """:param flag:
        :return:
        """
    @classmethod
    def IsDefined(cls, enumType: Type, value: object) -> bool:
        """:param enumType:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, enumType: Type, value: str) -> object:
        """:param enumType:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, enumType: Type, value: str, ignoreCase: bool) -> object:
        """:param enumType:
        :param value:
        :param ignoreCase:
        :return:
        """
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """:param provider:
        :return:
        """
    def ToByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToChar(self, provider: IFormatProvider) -> Char:
        """:param provider:
        :return:
        """
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """:param provider:
        :return:
        """
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """:param provider:
        :return:
        """
    def ToDouble(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    def ToInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    @classmethod
    @overload
    def ToObject(cls, enumType: Type, value: int) -> object:
        """:param enumType:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def ToObject(cls, enumType: Type, value: int) -> object:
        """:param enumType:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def ToObject(cls, enumType: Type, value: int) -> object:
        """:param enumType:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def ToObject(cls, enumType: Type, value: int) -> object:
        """:param enumType:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def ToObject(cls, enumType: Type, value: object) -> object:
        """:param enumType:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def ToObject(cls, enumType: Type, value: int) -> object:
        """:param enumType:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def ToObject(cls, enumType: Type, value: int) -> object:
        """:param enumType:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def ToObject(cls, enumType: Type, value: int) -> object:
        """:param enumType:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def ToObject(cls, enumType: Type, value: int) -> object:
        """:param enumType:
        :param value:
        :return:
        """
    def ToSByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSingle(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self, format: str) -> str:
        """:param format:
        :return:
        """
    @overload
    def ToString(self, format: str, formatProvider: IFormatProvider) -> str:
        """:param format:
        :param formatProvider:
        :return:
        """
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """:param conversionType:
        :param provider:
        :return:
        """
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    @classmethod
    @overload
    def TryParse(cls, value: str, result: TEnum) -> Tuple[bool, TEnum]:
        """:param value:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryParse(cls, value: str, ignoreCase: bool, result: TEnum) -> Tuple[bool, TEnum]:
        """:param value:
        :param ignoreCase:
        :param result:
        :return:
        """

class Environment(ABC, Object):
    """"""

    @classmethod
    @property
    def CommandLine(cls) -> str:
        """:return:"""
    @classmethod
    @property
    def CurrentDirectory(cls) -> str:
        """:return:"""
    @classmethod
    @CurrentDirectory.setter
    def CurrentDirectory(cls, value: str) -> None: ...
    @classmethod
    @property
    def CurrentManagedThreadId(cls) -> int:
        """:return:"""
    @classmethod
    @property
    def ExitCode(cls) -> int:
        """:return:"""
    @classmethod
    @ExitCode.setter
    def ExitCode(cls, value: int) -> None: ...
    @classmethod
    @property
    def HasShutdownStarted(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def Is64BitOperatingSystem(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def Is64BitProcess(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def MachineName(cls) -> str:
        """:return:"""
    @classmethod
    @property
    def NewLine(cls) -> str:
        """:return:"""
    @classmethod
    @property
    def OSVersion(cls) -> OperatingSystem:
        """:return:"""
    @classmethod
    @property
    def ProcessorCount(cls) -> int:
        """:return:"""
    @classmethod
    @property
    def StackTrace(cls) -> str:
        """:return:"""
    @classmethod
    @property
    def SystemDirectory(cls) -> str:
        """:return:"""
    @classmethod
    @property
    def SystemPageSize(cls) -> int:
        """:return:"""
    @classmethod
    @property
    def TickCount(cls) -> int:
        """:return:"""
    @classmethod
    @property
    def UserDomainName(cls) -> str:
        """:return:"""
    @classmethod
    @property
    def UserInteractive(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def UserName(cls) -> str:
        """:return:"""
    @classmethod
    @property
    def Version(cls) -> Version:
        """:return:"""
    @classmethod
    @property
    def WorkingSet(cls) -> int:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    def Exit(cls, exitCode: int) -> None:
        """:param exitCode:"""
    @classmethod
    def ExpandEnvironmentVariables(cls, name: str) -> str:
        """:param name:
        :return:
        """
    @classmethod
    @overload
    def FailFast(cls, message: str) -> None:
        """:param message:"""
    @classmethod
    @overload
    def FailFast(cls, message: str, exception: Exception) -> None:
        """:param message:
        :param exception:
        """
    @classmethod
    def GetCommandLineArgs(cls) -> Array[str]:
        """:return:"""
    @classmethod
    @overload
    def GetEnvironmentVariable(cls, variable: str) -> str:
        """:param variable:
        :return:
        """
    @classmethod
    @overload
    def GetEnvironmentVariable(cls, variable: str, target: EnvironmentVariableTarget) -> str:
        """:param variable:
        :param target:
        :return:
        """
    @classmethod
    @overload
    def GetEnvironmentVariables(cls) -> IDictionary:
        """:return:"""
    @classmethod
    @overload
    def GetEnvironmentVariables(cls, target: EnvironmentVariableTarget) -> IDictionary:
        """:param target:
        :return:
        """
    @classmethod
    @overload
    def GetFolderPath(cls, folder: Environment.SpecialFolder) -> str:
        """:param folder:
        :return:
        """
    @classmethod
    @overload
    def GetFolderPath(
        cls, folder: Environment.SpecialFolder, option: Environment.SpecialFolderOption
    ) -> str:
        """:param folder:
        :param option:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    @classmethod
    def GetLogicalDrives(cls) -> Array[str]:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    @overload
    def SetEnvironmentVariable(cls, variable: str, value: str) -> None:
        """:param variable:
        :param value:
        """
    @classmethod
    @overload
    def SetEnvironmentVariable(
        cls, variable: str, value: str, target: EnvironmentVariableTarget
    ) -> None:
        """:param variable:
        :param value:
        :param target:
        """
    def ToString(self) -> str:
        """:return:"""

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
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

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

    Empty: Final[ClassVar[EventArgs]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

EventHandler: Callable[[object, TEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""
EventHandler: Callable[[object, EventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class Exception(Object, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

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
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class ExternDll(ABC, Object):
    """"""

    Activeds: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Advapi32: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Clr: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Comctl32: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Comdlg32: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Crypt32: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Fxassert: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Gdi32: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Gdiplus: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Hhctrl: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Imm32: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Kernel32: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Loadperf: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Mqrt: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Mscoree: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Msi: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Ntdll: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Ole32: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Oleacc: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Oleaut32: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Olepro32: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    PerfCounter: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Powrprof: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Psapi: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    ShCore: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Shell32: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Shlwapi: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    User32: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Uxtheme: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Version: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Vsassert: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    WinMM: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Winspool: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Wldp: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Wtsapi32: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class FieldAccessException(MemberAccessException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, inner: Exception):
        """:param message:
        :param inner:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class FileStyleUriParser(UriParser):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class FlagsAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
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
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class FormatException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class FormattableString(ABC, Object, IFormattable):
    """"""

    @property
    def ArgumentCount(self) -> int:
        """:return:"""
    @property
    def Format(self) -> str:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetArgument(self, index: int) -> object:
        """:param index:
        :return:
        """
    def GetArguments(self) -> Array[object]:
        """:return:"""
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def Invariant(cls, formattable: FormattableString) -> str:
        """:param formattable:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, formatProvider: IFormatProvider) -> str:
        """:param formatProvider:
        :return:
        """
    @overload
    def ToString(self, format: str, formatProvider: IFormatProvider) -> str:
        """:param format:
        :param formatProvider:
        :return:
        """

class FtpStyleUriParser(UriParser):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

Func: Callable[[T], TResult] = ...
"""

:param arg: 
:return: 
"""
Func: Callable[[T1, T2], TResult] = ...
"""

:param arg1: 
:param arg2: 
:return: 
"""
Func: Callable[[T1, T2, T3], TResult] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:return: 
"""
Func: Callable[[T1, T2, T3, T4], TResult] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:return: 
"""
Func: Callable[[T1, T2, T3, T4, T5], TResult] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:param arg5: 
:return: 
"""
Func: Callable[[T1, T2, T3, T4, T5, T6], TResult] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:param arg5: 
:param arg6: 
:return: 
"""
Func: Callable[[T1, T2, T3, T4, T5, T6, T7], TResult] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:param arg5: 
:param arg6: 
:param arg7: 
:return: 
"""
Func: Callable[[T1, T2, T3, T4, T5, T6, T7, T8], TResult] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:param arg5: 
:param arg6: 
:param arg7: 
:param arg8: 
:return: 
"""
Func: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9], TResult] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:param arg5: 
:param arg6: 
:param arg7: 
:param arg8: 
:param arg9: 
:return: 
"""
Func: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10], TResult] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:param arg5: 
:param arg6: 
:param arg7: 
:param arg8: 
:param arg9: 
:param arg10: 
:return: 
"""
Func: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11], TResult] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:param arg5: 
:param arg6: 
:param arg7: 
:param arg8: 
:param arg9: 
:param arg10: 
:param arg11: 
:return: 
"""
Func: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12], TResult] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:param arg5: 
:param arg6: 
:param arg7: 
:param arg8: 
:param arg9: 
:param arg10: 
:param arg11: 
:param arg12: 
:return: 
"""
Func: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13], TResult] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:param arg5: 
:param arg6: 
:param arg7: 
:param arg8: 
:param arg9: 
:param arg10: 
:param arg11: 
:param arg12: 
:param arg13: 
:return: 
"""
Func: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14], TResult] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:param arg5: 
:param arg6: 
:param arg7: 
:param arg8: 
:param arg9: 
:param arg10: 
:param arg11: 
:param arg12: 
:param arg13: 
:param arg14: 
:return: 
"""
Func: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15], TResult] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:param arg5: 
:param arg6: 
:param arg7: 
:param arg8: 
:param arg9: 
:param arg10: 
:param arg11: 
:param arg12: 
:param arg13: 
:param arg14: 
:param arg15: 
:return: 
"""
Func: Callable[
    [T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16], TResult
] = ...
"""

:param arg1: 
:param arg2: 
:param arg3: 
:param arg4: 
:param arg5: 
:param arg6: 
:param arg7: 
:param arg8: 
:param arg9: 
:param arg10: 
:param arg11: 
:param arg12: 
:param arg13: 
:param arg14: 
:param arg15: 
:param arg16: 
:return: 
"""
Func: Callable[[], TResult] = ...
"""

:return: 
"""

class GC(ABC, Object):
    """"""

    @classmethod
    @property
    def MaxGeneration(cls) -> int:
        """:return:"""
    @classmethod
    def AddMemoryPressure(cls, bytesAllocated: int) -> None:
        """:param bytesAllocated:"""
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
        """:param generation:"""
    @classmethod
    @overload
    def Collect(cls, generation: int, mode: GCCollectionMode) -> None:
        """:param generation:
        :param mode:
        """
    @classmethod
    @overload
    def Collect(cls, generation: int, mode: GCCollectionMode, blocking: bool) -> None:
        """:param generation:
        :param mode:
        :param blocking:
        """
    @classmethod
    @overload
    def Collect(
        cls, generation: int, mode: GCCollectionMode, blocking: bool, compacting: bool
    ) -> None:
        """:param generation:
        :param mode:
        :param blocking:
        :param compacting:
        """
    @classmethod
    def CollectionCount(cls, generation: int) -> int:
        """:param generation:
        :return:
        """
    @classmethod
    def EndNoGCRegion(cls) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    def GetAllocatedBytesForCurrentThread(cls) -> int:
        """:return:"""
    @classmethod
    @overload
    def GetGeneration(cls, obj: object) -> int:
        """:param obj:
        :return:
        """
    @classmethod
    @overload
    def GetGeneration(cls, wo: WeakReference) -> int:
        """:param wo:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    @classmethod
    def GetTotalMemory(cls, forceFullCollection: bool) -> int:
        """:param forceFullCollection:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def KeepAlive(cls, obj: object) -> None:
        """:param obj:"""
    @classmethod
    def ReRegisterForFinalize(cls, obj: object) -> None:
        """:param obj:"""
    @classmethod
    def RegisterForFullGCNotification(
        cls, maxGenerationThreshold: int, largeObjectHeapThreshold: int
    ) -> None:
        """:param maxGenerationThreshold:
        :param largeObjectHeapThreshold:
        """
    @classmethod
    def RemoveMemoryPressure(cls, bytesAllocated: int) -> None:
        """:param bytesAllocated:"""
    @classmethod
    def SuppressFinalize(cls, obj: object) -> None:
        """:param obj:"""
    def ToString(self) -> str:
        """:return:"""
    @classmethod
    @overload
    def TryStartNoGCRegion(cls, totalSize: int) -> bool:
        """:param totalSize:
        :return:
        """
    @classmethod
    @overload
    def TryStartNoGCRegion(cls, totalSize: int, disallowFullBlockingGC: bool) -> bool:
        """:param totalSize:
        :param disallowFullBlockingGC:
        :return:
        """
    @classmethod
    @overload
    def TryStartNoGCRegion(cls, totalSize: int, lohSize: int) -> bool:
        """:param totalSize:
        :param lohSize:
        :return:
        """
    @classmethod
    @overload
    def TryStartNoGCRegion(cls, totalSize: int, lohSize: int, disallowFullBlockingGC: bool) -> bool:
        """:param totalSize:
        :param lohSize:
        :param disallowFullBlockingGC:
        :return:
        """
    @classmethod
    @overload
    def WaitForFullGCApproach(cls) -> GCNotificationStatus:
        """:return:"""
    @classmethod
    @overload
    def WaitForFullGCApproach(cls, millisecondsTimeout: int) -> GCNotificationStatus:
        """:param millisecondsTimeout:
        :return:
        """
    @classmethod
    @overload
    def WaitForFullGCComplete(cls) -> GCNotificationStatus:
        """:return:"""
    @classmethod
    @overload
    def WaitForFullGCComplete(cls, millisecondsTimeout: int) -> GCNotificationStatus:
        """:param millisecondsTimeout:
        :return:
        """
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

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def Register(cls, callback: Func[object, bool], targetObj: object) -> None:
        """:param callback:
        :param targetObj:
        """
    def ToString(self) -> str:
        """:return:"""

class GenericUriParser(UriParser):
    """"""

    def __init__(self, options: GenericUriParserOptions):
        """:param options:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

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

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class Guid(ValueType, IComparable, IComparable[Guid], IEquatable[Guid], IFormattable):
    """"""

    Empty: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, b: Array[int]):
        """:param b:"""
    @overload
    def __init__(self, g: str):
        """:param g:"""
    @overload
    def __init__(self, a: int, b: int, c: int, d: Array[int]):
        """:param a:
        :param b:
        :param c:
        :param d:
        """
    @overload
    def __init__(
        self,
        a: int,
        b: int,
        c: int,
        d: int,
        e: int,
        f: int,
        g: int,
        h: int,
        i: int,
        j: int,
        k: int,
    ):
        """:param a:
        :param b:
        :param c:
        :param d:
        :param e:
        :param f:
        :param g:
        :param h:
        :param i:
        :param j:
        :param k:
        """
    @overload
    def __init__(
        self,
        a: int,
        b: int,
        c: int,
        d: int,
        e: int,
        f: int,
        g: int,
        h: int,
        i: int,
        j: int,
        k: int,
    ):
        """:param a:
        :param b:
        :param c:
        :param d:
        :param e:
        :param f:
        :param g:
        :param h:
        :param i:
        :param j:
        :param k:
        """
    @overload
    def CompareTo(self, other: Guid) -> int:
        """:param other:
        :return:
        """
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: Guid) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def NewGuid(cls) -> Guid:
        """:return:"""
    @classmethod
    def Parse(cls, input: str) -> Guid:
        """:param input:
        :return:
        """
    @classmethod
    def ParseExact(cls, input: str, format: str) -> Guid:
        """:param input:
        :param format:
        :return:
        """
    def ToByteArray(self) -> Array[int]:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, format: str) -> str:
        """:param format:
        :return:
        """
    @overload
    def ToString(self, format: str, formatProvider: IFormatProvider) -> str:
        """:param format:
        :param formatProvider:
        :return:
        """
    @classmethod
    def TryParse(cls, input: str, result: Guid) -> Tuple[bool, Guid]:
        """:param input:
        :param result:
        :return:
        """
    @classmethod
    def TryParseExact(cls, input: str, format: str, result: Guid) -> Tuple[bool, Guid]:
        """:param input:
        :param format:
        :param result:
        :return:
        """
    def __eq__(self, other: Guid) -> bool:
        """:param other:
        :return:
        """
    def __ne__(self, other: Guid) -> bool:
        """:param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, a: Guid, b: Guid) -> bool:
        """:param a:
        :param b:
        :return:
        """
    @classmethod
    def op_Inequality(cls, a: Guid, b: Guid) -> bool:
        """:param a:
        :param b:
        :return:
        """

class HResults(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class HttpStyleUriParser(UriParser):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class IAppDomainSetup:
    """"""

    @property
    def ApplicationBase(self) -> str:
        """:return:"""
    @ApplicationBase.setter
    def ApplicationBase(self, value: str) -> None: ...
    @property
    def ApplicationName(self) -> str:
        """:return:"""
    @ApplicationName.setter
    def ApplicationName(self, value: str) -> None: ...
    @property
    def CachePath(self) -> str:
        """:return:"""
    @CachePath.setter
    def CachePath(self, value: str) -> None: ...
    @property
    def ConfigurationFile(self) -> str:
        """:return:"""
    @ConfigurationFile.setter
    def ConfigurationFile(self, value: str) -> None: ...
    @property
    def DynamicBase(self) -> str:
        """:return:"""
    @DynamicBase.setter
    def DynamicBase(self, value: str) -> None: ...
    @property
    def LicenseFile(self) -> str:
        """:return:"""
    @LicenseFile.setter
    def LicenseFile(self, value: str) -> None: ...
    @property
    def PrivateBinPath(self) -> str:
        """:return:"""
    @PrivateBinPath.setter
    def PrivateBinPath(self, value: str) -> None: ...
    @property
    def PrivateBinPathProbe(self) -> str:
        """:return:"""
    @PrivateBinPathProbe.setter
    def PrivateBinPathProbe(self, value: str) -> None: ...
    @property
    def ShadowCopyDirectories(self) -> str:
        """:return:"""
    @ShadowCopyDirectories.setter
    def ShadowCopyDirectories(self, value: str) -> None: ...
    @property
    def ShadowCopyFiles(self) -> str:
        """:return:"""
    @ShadowCopyFiles.setter
    def ShadowCopyFiles(self, value: str) -> None: ...

class IAsyncResult:
    """"""

    @property
    def AsyncState(self) -> object:
        """:return:"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """:return:"""
    @property
    def CompletedSynchronously(self) -> bool:
        """:return:"""
    @property
    def IsCompleted(self) -> bool:
        """:return:"""

class ICloneable:
    """"""

    def Clone(self) -> object:
        """:return:"""

class IComparable:
    """"""

    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """

class IComparable(Generic[T]):
    """"""

    def CompareTo(self, other: T) -> int:
        """:param other:
        :return:
        """

class IConvertible:
    """"""

    def GetTypeCode(self) -> TypeCode:
        """:return:"""
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """:param provider:
        :return:
        """
    def ToByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToChar(self, provider: IFormatProvider) -> Char:
        """:param provider:
        :return:
        """
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """:param provider:
        :return:
        """
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """:param provider:
        :return:
        """
    def ToDouble(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    def ToInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSingle(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    def ToString(self, provider: IFormatProvider) -> str:
        """:param provider:
        :return:
        """
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """:param conversionType:
        :param provider:
        :return:
        """
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """

class ICustomFormatter:
    """"""

    def Format(self, format: str, arg: object, formatProvider: IFormatProvider) -> str:
        """:param format:
        :param arg:
        :param formatProvider:
        :return:
        """

class IDisposable:
    """"""

    def Dispose(self) -> None:
        """"""

class IEquatable(Generic[T]):
    """"""

    def Equals(self, other: T) -> bool:
        """:param other:
        :return:
        """

class IFormatProvider:
    """"""

    def GetFormat(self, formatType: Type) -> object:
        """:param formatType:
        :return:
        """

class IFormattable:
    """"""

    def ToString(self, format: str, formatProvider: IFormatProvider) -> str:
        """:param format:
        :param formatProvider:
        :return:
        """

class IObservable(Generic[T]):
    """"""

    def Subscribe(self, observer: IObserver[T]) -> IDisposable:
        """:param observer:
        :return:
        """

class IObserver(Generic[T]):
    """"""

    def OnCompleted(self) -> None:
        """"""
    def OnError(self, error: Exception) -> None:
        """:param error:"""
    def OnNext(self, value: T) -> None:
        """:param value:"""

class IProgress(Generic[T]):
    """"""

    def Report(self, value: T) -> None:
        """:param value:"""

class IPv4AddressHelper(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class IPv6AddressHelper(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class IRuntimeFieldInfo:
    """"""

    @property
    def Value(self) -> RuntimeFieldHandleInternal:
        """:return:"""

class IRuntimeMethodInfo:
    """"""

    @property
    def Value(self) -> RuntimeMethodHandleInternal:
        """:return:"""

class IServiceProvider:
    """"""

    def GetService(self, serviceType: Type) -> object:
        """:param serviceType:
        :return:
        """

class ITupleInternal(ITuple):
    """"""

    @property
    def Item(self) -> object:
        """:return:"""
    @property
    def Length(self) -> int:
        """:return:"""
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    def ToString(self, sb: StringBuilder) -> str:
        """:param sb:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """:param index:
        :return:
        """

class IValueTupleInternal(ITuple):
    """"""

    @property
    def Item(self) -> object:
        """:return:"""
    @property
    def Length(self) -> int:
        """:return:"""
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    def ToStringEnd(self) -> str:
        """:return:"""
    def __getitem__(self, index: int) -> object:
        """:param index:
        :return:
        """

class IWellKnownStringEqualityComparer:
    """"""

    def GetEqualityComparerForSerialization(self) -> IEqualityComparer:
        """:return:"""
    def GetRandomizedEqualityComparer(self) -> IEqualityComparer:
        """:return:"""

class IndexOutOfRangeException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class InsufficientExecutionStackException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class InsufficientMemoryException(OutOfMemoryException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class Int16(
    ValueType,
    IComparable,
    IComparable[Int16],
    IConvertible,
    IEquatable[Int16],
    IFormattable,
):
    """"""

    MaxValue: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MinValue: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @overload
    def CompareTo(self, other: int) -> int:
        """:param other:
        :return:
        """
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: int) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeCode(self) -> TypeCode:
        """:return:"""
    @classmethod
    @overload
    def Parse(cls, s: str) -> int:
        """:param s:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles) -> int:
        """:param s:
        :param style:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider) -> int:
        """:param s:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles, provider: IFormatProvider) -> int:
        """:param s:
        :param style:
        :param provider:
        :return:
        """
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """:param provider:
        :return:
        """
    def ToByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToChar(self, provider: IFormatProvider) -> Char:
        """:param provider:
        :return:
        """
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """:param provider:
        :return:
        """
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """:param provider:
        :return:
        """
    def ToDouble(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    def ToInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSingle(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self, format: str) -> str:
        """:param format:
        :return:
        """
    @overload
    def ToString(self, format: str, formatProvider: IFormatProvider) -> str:
        """:param format:
        :param formatProvider:
        :return:
        """
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """:param conversionType:
        :param provider:
        :return:
        """
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    @classmethod
    @overload
    def TryParse(cls, s: str, result: int) -> Tuple[bool, int]:
        """:param s:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryParse(
        cls, s: str, style: NumberStyles, provider: IFormatProvider, result: int
    ) -> Tuple[bool, int]:
        """:param s:
        :param style:
        :param provider:
        :param result:
        :return:
        """

class Int32(
    ValueType,
    IComparable,
    IComparable[Int32],
    IConvertible,
    IEquatable[Int32],
    IFormattable,
):
    """"""

    MaxValue: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MinValue: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @overload
    def CompareTo(self, other: int) -> int:
        """:param other:
        :return:
        """
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: int) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeCode(self) -> TypeCode:
        """:return:"""
    @classmethod
    @overload
    def Parse(cls, s: str) -> int:
        """:param s:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles) -> int:
        """:param s:
        :param style:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider) -> int:
        """:param s:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles, provider: IFormatProvider) -> int:
        """:param s:
        :param style:
        :param provider:
        :return:
        """
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """:param provider:
        :return:
        """
    def ToByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToChar(self, provider: IFormatProvider) -> Char:
        """:param provider:
        :return:
        """
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """:param provider:
        :return:
        """
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """:param provider:
        :return:
        """
    def ToDouble(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    def ToInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSingle(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self, format: str) -> str:
        """:param format:
        :return:
        """
    @overload
    def ToString(self, format: str, formatProvider: IFormatProvider) -> str:
        """:param format:
        :param formatProvider:
        :return:
        """
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """:param conversionType:
        :param provider:
        :return:
        """
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    @classmethod
    @overload
    def TryParse(cls, s: str, result: int) -> Tuple[bool, int]:
        """:param s:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryParse(
        cls, s: str, style: NumberStyles, provider: IFormatProvider, result: int
    ) -> Tuple[bool, int]:
        """:param s:
        :param style:
        :param provider:
        :param result:
        :return:
        """

class Int64(
    ValueType,
    IComparable,
    IComparable[Int64],
    IConvertible,
    IEquatable[Int64],
    IFormattable,
):
    """"""

    MaxValue: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MinValue: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @overload
    def CompareTo(self, other: int) -> int:
        """:param other:
        :return:
        """
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: int) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeCode(self) -> TypeCode:
        """:return:"""
    @classmethod
    @overload
    def Parse(cls, s: str) -> int:
        """:param s:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles) -> int:
        """:param s:
        :param style:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider) -> int:
        """:param s:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles, provider: IFormatProvider) -> int:
        """:param s:
        :param style:
        :param provider:
        :return:
        """
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """:param provider:
        :return:
        """
    def ToByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToChar(self, provider: IFormatProvider) -> Char:
        """:param provider:
        :return:
        """
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """:param provider:
        :return:
        """
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """:param provider:
        :return:
        """
    def ToDouble(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    def ToInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSingle(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self, format: str) -> str:
        """:param format:
        :return:
        """
    @overload
    def ToString(self, format: str, formatProvider: IFormatProvider) -> str:
        """:param format:
        :param formatProvider:
        :return:
        """
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """:param conversionType:
        :param provider:
        :return:
        """
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    @classmethod
    @overload
    def TryParse(cls, s: str, result: int) -> Tuple[bool, int]:
        """:param s:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryParse(
        cls, s: str, style: NumberStyles, provider: IFormatProvider, result: int
    ) -> Tuple[bool, int]:
        """:param s:
        :param style:
        :param provider:
        :param result:
        :return:
        """

class IntPtr(ValueType, ISerializable):
    """"""

    Zero: Final[ClassVar[IntPtr]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, value: int):
        """:param value:"""
    @overload
    def __init__(self, value: int):
        """:param value:"""
    @overload
    def __init__(self, value: None):
        """:param value:"""
    @classmethod
    @property
    def Size(cls) -> int:
        """:return:"""
    @classmethod
    def Add(cls, pointer: IntPtr, offset: int) -> IntPtr:
        """:param pointer:
        :param offset:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def Subtract(cls, pointer: IntPtr, offset: int) -> IntPtr:
        """:param pointer:
        :param offset:
        :return:
        """
    def ToInt32(self) -> int:
        """:return:"""
    def ToInt64(self) -> int:
        """:return:"""
    def ToPointer(self) -> None:
        """"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, format: str) -> str:
        """:param format:
        :return:
        """
    def __add__(self, other: int) -> IntPtr:
        """:param other:
        :return:
        """
    def __eq__(self, other: IntPtr) -> bool:
        """:param other:
        :return:
        """
    def __ne__(self, other: IntPtr) -> bool:
        """:param other:
        :return:
        """
    def __sub__(self, other: int) -> IntPtr:
        """:param other:
        :return:
        """
    @classmethod
    def op_Addition(cls, pointer: IntPtr, offset: int) -> IntPtr:
        """:param pointer:
        :param offset:
        :return:
        """
    @classmethod
    def op_Equality(cls, value1: IntPtr, value2: IntPtr) -> bool:
        """:param value1:
        :param value2:
        :return:
        """
    @classmethod
    @overload
    def op_Explicit(cls, value: int) -> IntPtr:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def op_Explicit(cls, value: int) -> IntPtr:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def op_Explicit(cls, value: IntPtr) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def op_Explicit(cls, value: None) -> IntPtr:
        """:param value:
        :return:
        """
    @classmethod
    def op_Inequality(cls, value1: IntPtr, value2: IntPtr) -> bool:
        """:param value1:
        :param value2:
        :return:
        """
    @classmethod
    def op_Subtraction(cls, pointer: IntPtr, offset: int) -> IntPtr:
        """:param pointer:
        :param offset:
        :return:
        """

class Internal(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

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
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @overload
    def __init__(self, message: str, errorCode: int):
        """:param message:
        :param errorCode:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class InvalidOperationException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class InvalidProgramException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, inner: Exception):
        """:param message:
        :param inner:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class InvalidTimeZoneException(Exception, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class InvariantComparer(Object, IComparer):
    """"""

    def Compare(self, x: object, y: object) -> int:
        """:param x:
        :param y:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class IriHelper(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class LazyHelpers(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class Lazy(Generic[T], Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, mode: LazyThreadSafetyMode):
        """:param mode:"""
    @overload
    def __init__(self, isThreadSafe: bool):
        """:param isThreadSafe:"""
    @overload
    def __init__(self, valueFactory: Func[T]):
        """:param valueFactory:"""
    @overload
    def __init__(self, valueFactory: Func[T], mode: LazyThreadSafetyMode):
        """:param valueFactory:
        :param mode:
        """
    @overload
    def __init__(self, valueFactory: Func[T], isThreadSafe: bool):
        """:param valueFactory:
        :param isThreadSafe:
        """
    @property
    def IsValueCreated(self) -> bool:
        """:return:"""
    @property
    def Value(self) -> T:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class LdapStyleUriParser(UriParser):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

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
    def __init__(self, value: int):
        """:param value:"""
    @overload
    def __init__(self, value: LoaderOptimization):
        """:param value:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    @property
    def Value(self) -> LoaderOptimization:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
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
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class LocalAppContext(ABC, Object):
    """"""

    @classmethod
    def IsSwitchEnabled(cls, switchName: str) -> bool:
        """:param switchName:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class LocalAppContextSwitches(ABC, Object):
    """"""

    @classmethod
    @property
    def AesCryptoServiceProviderDontCorrectlyResetDecryptor(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def AllocateOverlappedOnDemand(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def DisableEventLogRegistryKeysFiltering(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def DisableTempFileCollectionDirectoryFeature(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def DoNotCatchSerialStreamThreadExceptions(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def DoNotUseNativeZipLibraryForDecompression(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def DoNotValidateX509KeyStorageFlags(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def DontCheckCertificateEKUs(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def DontCheckCertificateRevocation(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def DontEnableSchSendAuxRecord(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def DontEnableSchUseStrongCrypto(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def DontEnableStrictRFC3986ReservedCharacterSets(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def DontEnableSystemDefaultTlsVersions(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def DontEnableTls13(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def DontEnableTlsAlerts(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def DontKeepUnicodeBidiFormattingCharacters(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def DontReliablyClonePrivateKey(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def MemberDescriptorEqualsReturnsFalseIfEquivalent(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def SymmetricCngAlwaysUseNCrypt(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def UseLegacyFipsThrow(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def UseLegacyPublicKeyBehavior(cls) -> bool:
        """:return:"""
    @classmethod
    @property
    def UseLegacyTimeoutCheck(cls) -> bool:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class LocalDataStore(Object):
    """"""

    def __init__(self, mgr: LocalDataStoreMgr, InitialCapacity: int):
        """:param mgr:
        :param InitialCapacity:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetData(self, slot: LocalDataStoreSlot) -> object:
        """:param slot:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def SetData(self, slot: LocalDataStoreSlot, data: object) -> None:
        """:param slot:
        :param data:
        """
    def ToString(self) -> str:
        """:return:"""

class LocalDataStoreElement(Object):
    """"""

    def __init__(self, cookie: int):
        """:param cookie:"""
    @property
    def Cookie(self) -> int:
        """:return:"""
    @property
    def Value(self) -> object:
        """:return:"""
    @Value.setter
    def Value(self, value: object) -> None: ...
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class LocalDataStoreHolder(Object):
    """"""

    def __init__(self, store: LocalDataStore):
        """:param store:"""
    @property
    def Store(self) -> LocalDataStore:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class LocalDataStoreMgr(Object):
    """"""

    def __init__(self):
        """"""
    def AllocateDataSlot(self) -> LocalDataStoreSlot:
        """:return:"""
    def AllocateNamedDataSlot(self, name: str) -> LocalDataStoreSlot:
        """:param name:
        :return:
        """
    def CreateLocalDataStore(self) -> LocalDataStoreHolder:
        """:return:"""
    def DeleteLocalDataStore(self, store: LocalDataStore) -> None:
        """:param store:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def FreeNamedDataSlot(self, name: str) -> None:
        """:param name:"""
    def GetHashCode(self) -> int:
        """:return:"""
    def GetNamedDataSlot(self, name: str) -> LocalDataStoreSlot:
        """:param name:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def ValidateSlot(self, slot: LocalDataStoreSlot) -> None:
        """:param slot:"""

class LocalDataStoreSlot(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

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

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
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
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class MarshalByRefObject(ABC, Object):
    """"""

    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """:param requestedType:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetLifetimeService(self) -> object:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def InitializeLifetimeService(self) -> object:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class Math(ABC, Object):
    """"""

    E: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    PI: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    @classmethod
    @overload
    def Abs(cls, value: Decimal) -> Decimal:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def Abs(cls, value: float) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def Abs(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def Abs(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def Abs(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def Abs(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def Abs(cls, value: float) -> float:
        """:param value:
        :return:
        """
    @classmethod
    def Acos(cls, d: float) -> float:
        """:param d:
        :return:
        """
    @classmethod
    def Asin(cls, d: float) -> float:
        """:param d:
        :return:
        """
    @classmethod
    def Atan(cls, d: float) -> float:
        """:param d:
        :return:
        """
    @classmethod
    def Atan2(cls, y: float, x: float) -> float:
        """:param y:
        :param x:
        :return:
        """
    @classmethod
    def BigMul(cls, a: int, b: int) -> int:
        """:param a:
        :param b:
        :return:
        """
    @classmethod
    @overload
    def Ceiling(cls, d: Decimal) -> Decimal:
        """:param d:
        :return:
        """
    @classmethod
    @overload
    def Ceiling(cls, a: float) -> float:
        """:param a:
        :return:
        """
    @classmethod
    def Cos(cls, d: float) -> float:
        """:param d:
        :return:
        """
    @classmethod
    def Cosh(cls, value: float) -> float:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def DivRem(cls, a: int, b: int, result: int) -> Tuple[int, int]:
        """:param a:
        :param b:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def DivRem(cls, a: int, b: int, result: int) -> Tuple[int, int]:
        """:param a:
        :param b:
        :param result:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    def Exp(cls, d: float) -> float:
        """:param d:
        :return:
        """
    @classmethod
    @overload
    def Floor(cls, d: Decimal) -> Decimal:
        """:param d:
        :return:
        """
    @classmethod
    @overload
    def Floor(cls, d: float) -> float:
        """:param d:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def IEEERemainder(cls, x: float, y: float) -> float:
        """:param x:
        :param y:
        :return:
        """
    @classmethod
    @overload
    def Log(cls, d: float) -> float:
        """:param d:
        :return:
        """
    @classmethod
    @overload
    def Log(cls, a: float, newBase: float) -> float:
        """:param a:
        :param newBase:
        :return:
        """
    @classmethod
    def Log10(cls, d: float) -> float:
        """:param d:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, val1: int, val2: int) -> int:
        """:param val1:
        :param val2:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, val1: Decimal, val2: Decimal) -> Decimal:
        """:param val1:
        :param val2:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, val1: float, val2: float) -> float:
        """:param val1:
        :param val2:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, val1: int, val2: int) -> int:
        """:param val1:
        :param val2:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, val1: int, val2: int) -> int:
        """:param val1:
        :param val2:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, val1: int, val2: int) -> int:
        """:param val1:
        :param val2:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, val1: int, val2: int) -> int:
        """:param val1:
        :param val2:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, val1: float, val2: float) -> float:
        """:param val1:
        :param val2:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, val1: int, val2: int) -> int:
        """:param val1:
        :param val2:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, val1: int, val2: int) -> int:
        """:param val1:
        :param val2:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, val1: int, val2: int) -> int:
        """:param val1:
        :param val2:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, val1: int, val2: int) -> int:
        """:param val1:
        :param val2:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, val1: Decimal, val2: Decimal) -> Decimal:
        """:param val1:
        :param val2:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, val1: float, val2: float) -> float:
        """:param val1:
        :param val2:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, val1: int, val2: int) -> int:
        """:param val1:
        :param val2:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, val1: int, val2: int) -> int:
        """:param val1:
        :param val2:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, val1: int, val2: int) -> int:
        """:param val1:
        :param val2:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, val1: int, val2: int) -> int:
        """:param val1:
        :param val2:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, val1: float, val2: float) -> float:
        """:param val1:
        :param val2:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, val1: int, val2: int) -> int:
        """:param val1:
        :param val2:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, val1: int, val2: int) -> int:
        """:param val1:
        :param val2:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, val1: int, val2: int) -> int:
        """:param val1:
        :param val2:
        :return:
        """
    @classmethod
    def Pow(cls, x: float, y: float) -> float:
        """:param x:
        :param y:
        :return:
        """
    @classmethod
    @overload
    def Round(cls, d: Decimal) -> Decimal:
        """:param d:
        :return:
        """
    @classmethod
    @overload
    def Round(cls, a: float) -> float:
        """:param a:
        :return:
        """
    @classmethod
    @overload
    def Round(cls, d: Decimal, decimals: int) -> Decimal:
        """:param d:
        :param decimals:
        :return:
        """
    @classmethod
    @overload
    def Round(cls, d: Decimal, mode: MidpointRounding) -> Decimal:
        """:param d:
        :param mode:
        :return:
        """
    @classmethod
    @overload
    def Round(cls, value: float, digits: int) -> float:
        """:param value:
        :param digits:
        :return:
        """
    @classmethod
    @overload
    def Round(cls, value: float, mode: MidpointRounding) -> float:
        """:param value:
        :param mode:
        :return:
        """
    @classmethod
    @overload
    def Round(cls, d: Decimal, decimals: int, mode: MidpointRounding) -> Decimal:
        """:param d:
        :param decimals:
        :param mode:
        :return:
        """
    @classmethod
    @overload
    def Round(cls, value: float, digits: int, mode: MidpointRounding) -> float:
        """:param value:
        :param digits:
        :param mode:
        :return:
        """
    @classmethod
    @overload
    def Sign(cls, value: Decimal) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def Sign(cls, value: float) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def Sign(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def Sign(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def Sign(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def Sign(cls, value: int) -> int:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def Sign(cls, value: float) -> int:
        """:param value:
        :return:
        """
    @classmethod
    def Sin(cls, a: float) -> float:
        """:param a:
        :return:
        """
    @classmethod
    def Sinh(cls, value: float) -> float:
        """:param value:
        :return:
        """
    @classmethod
    def Sqrt(cls, d: float) -> float:
        """:param d:
        :return:
        """
    @classmethod
    def Tan(cls, a: float) -> float:
        """:param a:
        :return:
        """
    @classmethod
    def Tanh(cls, value: float) -> float:
        """:param value:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""
    @classmethod
    @overload
    def Truncate(cls, d: Decimal) -> Decimal:
        """:param d:
        :return:
        """
    @classmethod
    @overload
    def Truncate(cls, d: float) -> float:
        """:param d:
        :return:
        """

class Mda(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class MemberAccessException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, inner: Exception):
        """:param message:
        :param inner:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class MethodAccessException(MemberAccessException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, inner: Exception):
        """:param message:
        :param inner:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class MidpointRounding(Enum):
    """"""

    ToEven: MidpointRounding = ...
    """"""
    AwayFromZero: MidpointRounding = ...
    """"""

class MissingFieldException(MissingMemberException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, inner: Exception):
        """:param message:
        :param inner:
        """
    @overload
    def __init__(self, className: str, fieldName: str):
        """:param className:
        :param fieldName:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class MissingMemberException(MemberAccessException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, inner: Exception):
        """:param message:
        :param inner:
        """
    @overload
    def __init__(self, className: str, memberName: str):
        """:param className:
        :param memberName:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class MissingMethodException(MissingMemberException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, inner: Exception):
        """:param message:
        :param inner:
        """
    @overload
    def __init__(self, className: str, methodName: str):
        """:param className:
        :param methodName:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class ModuleHandle(ValueType):
    """"""

    EmptyHandle: Final[ClassVar[ModuleHandle]] = ...
    """
    
    :return: 
    """
    @property
    def MDStreamVersion(self) -> int:
        """:return:"""
    @overload
    def Equals(self, handle: ModuleHandle) -> bool:
        """:param handle:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetRuntimeFieldHandleFromMetadataToken(self, fieldToken: int) -> RuntimeFieldHandle:
        """:param fieldToken:
        :return:
        """
    def GetRuntimeMethodHandleFromMetadataToken(self, methodToken: int) -> RuntimeMethodHandle:
        """:param methodToken:
        :return:
        """
    def GetRuntimeTypeHandleFromMetadataToken(self, typeToken: int) -> RuntimeTypeHandle:
        """:param typeToken:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ResolveFieldHandle(self, fieldToken: int) -> RuntimeFieldHandle:
        """:param fieldToken:
        :return:
        """
    @overload
    def ResolveFieldHandle(
        self,
        fieldToken: int,
        typeInstantiationContext: Array[RuntimeTypeHandle],
        methodInstantiationContext: Array[RuntimeTypeHandle],
    ) -> RuntimeFieldHandle:
        """:param fieldToken:
        :param typeInstantiationContext:
        :param methodInstantiationContext:
        :return:
        """
    @overload
    def ResolveMethodHandle(self, methodToken: int) -> RuntimeMethodHandle:
        """:param methodToken:
        :return:
        """
    @overload
    def ResolveMethodHandle(
        self,
        methodToken: int,
        typeInstantiationContext: Array[RuntimeTypeHandle],
        methodInstantiationContext: Array[RuntimeTypeHandle],
    ) -> RuntimeMethodHandle:
        """:param methodToken:
        :param typeInstantiationContext:
        :param methodInstantiationContext:
        :return:
        """
    @overload
    def ResolveTypeHandle(self, typeToken: int) -> RuntimeTypeHandle:
        """:param typeToken:
        :return:
        """
    @overload
    def ResolveTypeHandle(
        self,
        typeToken: int,
        typeInstantiationContext: Array[RuntimeTypeHandle],
        methodInstantiationContext: Array[RuntimeTypeHandle],
    ) -> RuntimeTypeHandle:
        """:param typeToken:
        :param typeInstantiationContext:
        :param methodInstantiationContext:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""
    def __eq__(self, other: ModuleHandle) -> bool:
        """:param other:
        :return:
        """
    def __ne__(self, other: ModuleHandle) -> bool:
        """:param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: ModuleHandle, right: ModuleHandle) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: ModuleHandle, right: ModuleHandle) -> bool:
        """:param left:
        :param right:
        :return:
        """

class MulticastDelegate(ABC, Delegate, ISerializable, ICloneable):
    """"""

    @property
    def Method(self) -> MethodInfo:
        """:return:"""
    @property
    def Target(self) -> object:
        """:return:"""
    def Clone(self) -> object:
        """:return:"""
    def DynamicInvoke(self, args: Array[object]) -> object:
        """:param args:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetInvocationList(self) -> Array[Delegate]:
        """:return:"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def __eq__(self, other: MulticastDelegate) -> bool:
        """:param other:
        :return:
        """
    def __ne__(self, other: MulticastDelegate) -> bool:
        """:param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, d1: MulticastDelegate, d2: MulticastDelegate) -> bool:
        """:param d1:
        :param d2:
        :return:
        """
    @classmethod
    def op_Inequality(cls, d1: MulticastDelegate, d2: MulticastDelegate) -> bool:
        """:param d1:
        :param d2:
        :return:
        """

class MulticastNotSupportedException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, inner: Exception):
        """:param message:
        :param inner:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class NetPipeStyleUriParser(UriParser):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class NetTcpStyleUriParser(UriParser):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class NewsStyleUriParser(UriParser):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class NonSerializedAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
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
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class NotFiniteNumberException(ArithmeticException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, offendingNumber: float):
        """:param offendingNumber:"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, offendingNumber: float):
        """:param message:
        :param offendingNumber:
        """
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @overload
    def __init__(self, message: str, offendingNumber: float, innerException: Exception):
        """:param message:
        :param offendingNumber:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def OffendingNumber(self) -> float:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class NotImplementedException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, inner: Exception):
        """:param message:
        :param inner:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class NotSupportedException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class NullReferenceException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class Nullable(ABC, Object):
    """"""

    @classmethod
    def Compare(cls, n1: T | None, n2: T | None) -> int:
        """:param n1:
        :param n2:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    @overload
    def Equals(cls, n1: T | None, n2: T | None) -> bool:
        """:param n1:
        :param n2:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def GetUnderlyingType(cls, nullableType: Type) -> Type:
        """:param nullableType:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class Nullable(Generic[T], ValueType):
    """"""

    def __init__(self, value: T):
        """"""
    @property
    def HasValue(self) -> bool:
        """"""
    @property
    def Value(self) -> T:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetValueOrDefault(self) -> T:
        """"""
    @overload
    def GetValueOrDefault(self, defaultValue: T) -> T:
        """"""
    def ToString(self) -> str:
        """:return:"""
    @classmethod
    def op_Explicit(cls, value: T | None) -> T:
        """"""
    @classmethod
    def op_Implicit(cls, value: T) -> T | None:
        """"""

class Number(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    def FormatDecimal(cls, value: Decimal, format: str, info: NumberFormatInfo) -> str:
        """:param value:
        :param format:
        :param info:
        :return:
        """
    @classmethod
    def FormatDouble(cls, value: float, format: str, info: NumberFormatInfo) -> str:
        """:param value:
        :param format:
        :param info:
        :return:
        """
    @classmethod
    def FormatInt32(cls, value: int, format: str, info: NumberFormatInfo) -> str:
        """:param value:
        :param format:
        :param info:
        :return:
        """
    @classmethod
    def FormatInt64(cls, value: int, format: str, info: NumberFormatInfo) -> str:
        """:param value:
        :param format:
        :param info:
        :return:
        """
    @classmethod
    def FormatSingle(cls, value: float, format: str, info: NumberFormatInfo) -> str:
        """:param value:
        :param format:
        :param info:
        :return:
        """
    @classmethod
    def FormatUInt32(cls, value: int, format: str, info: NumberFormatInfo) -> str:
        """:param value:
        :param format:
        :param info:
        :return:
        """
    @classmethod
    def FormatUInt64(cls, value: int, format: str, info: NumberFormatInfo) -> str:
        """:param value:
        :param format:
        :param info:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def NumberBufferToDecimal(cls, number: int, value: Decimal) -> bool:
        """:param number:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class Object:
    """"""

    def __init__(self):
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    @overload
    def Equals(cls, objA: object, objB: object) -> bool:
        """:param objA:
        :param objB:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def ReferenceEquals(cls, objA: object, objB: object) -> bool:
        """:param objA:
        :param objB:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class ObjectDisposedException(InvalidOperationException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self, objectName: str):
        """:param objectName:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @overload
    def __init__(self, objectName: str, message: str):
        """:param objectName:
        :param message:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def ObjectName(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class ObsoleteAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, error: bool):
        """:param message:
        :param error:
        """
    @property
    def IsError(self) -> bool:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
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
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class OleAutBinder(DefaultBinder):
    """"""

    def __init__(self):
        """"""
    def BindToField(
        self,
        bindingAttr: BindingFlags,
        match: Array[FieldInfo],
        value: object,
        culture: CultureInfo,
    ) -> FieldInfo:
        """:param bindingAttr:
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
        """:param bindingAttr:
        :param match:
        :param args:
        :param modifiers:
        :param culture:
        :param names:
        :param state:
        :return:
        """
    def ChangeType(self, value: object, type: Type, culture: CultureInfo) -> object:
        """:param value:
        :param type:
        :param culture:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ReorderArgumentArray(self, args: object, state: object) -> None:
        """:param args:
        :param state:
        """
    def SelectMethod(
        self,
        bindingAttr: BindingFlags,
        match: Array[MethodBase],
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodBase:
        """:param bindingAttr:
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
        """:param bindingAttr:
        :param match:
        :param returnType:
        :param indexes:
        :param modifiers:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class OperatingSystem(Object, ISerializable, ICloneable):
    """"""

    def __init__(self, platform: PlatformID, version: Version):
        """:param platform:
        :param version:
        """
    @property
    def Platform(self) -> PlatformID:
        """:return:"""
    @property
    def ServicePack(self) -> str:
        """:return:"""
    @property
    def Version(self) -> Version:
        """:return:"""
    @property
    def VersionString(self) -> str:
        """:return:"""
    def Clone(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class OperationCanceledException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, token: CancellationToken):
        """:param token:"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, token: CancellationToken):
        """:param message:
        :param token:
        """
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @overload
    def __init__(self, message: str, innerException: Exception, token: CancellationToken):
        """:param message:
        :param innerException:
        :param token:
        """
    @property
    def CancellationToken(self) -> CancellationToken:
        """:return:"""
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class OrdinalComparer(
    StringComparer,
    IComparer[String],
    IEqualityComparer[String],
    IComparer,
    IEqualityComparer,
    IWellKnownStringEqualityComparer,
):
    """"""

    @classmethod
    @property
    def CurrentCulture(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def CurrentCultureIgnoreCase(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def InvariantCulture(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def InvariantCultureIgnoreCase(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def Ordinal(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def OrdinalIgnoreCase(cls) -> StringComparer:
        """:return:"""
    @overload
    def Compare(self, x: object, y: object) -> int:
        """:param x:
        :param y:
        :return:
        """
    @overload
    def Compare(self, x: str, y: str) -> int:
        """:param x:
        :param y:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """:param x:
        :param y:
        :return:
        """
    @overload
    def Equals(self, x: str, y: str) -> bool:
        """:param x:
        :param y:
        :return:
        """
    def GetEqualityComparerForSerialization(self) -> IEqualityComparer:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def GetHashCode(self, obj: str) -> int:
        """:param obj:
        :return:
        """
    def GetRandomizedEqualityComparer(self) -> IEqualityComparer:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class OrdinalRandomizedComparer(
    StringComparer,
    IComparer[String],
    IEqualityComparer[String],
    IComparer,
    IEqualityComparer,
    IWellKnownStringEqualityComparer,
):
    """"""

    @classmethod
    @property
    def CurrentCulture(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def CurrentCultureIgnoreCase(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def InvariantCulture(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def InvariantCultureIgnoreCase(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def Ordinal(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def OrdinalIgnoreCase(cls) -> StringComparer:
        """:return:"""
    @overload
    def Compare(self, x: object, y: object) -> int:
        """:param x:
        :param y:
        :return:
        """
    @overload
    def Compare(self, x: str, y: str) -> int:
        """:param x:
        :param y:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """:param x:
        :param y:
        :return:
        """
    @overload
    def Equals(self, x: str, y: str) -> bool:
        """:param x:
        :param y:
        :return:
        """
    def GetEqualityComparerForSerialization(self) -> IEqualityComparer:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def GetHashCode(self, obj: str) -> int:
        """:param obj:
        :return:
        """
    def GetRandomizedEqualityComparer(self) -> IEqualityComparer:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class OutOfMemoryException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class OverflowException(ArithmeticException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class ParamArrayAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
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
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class ParamsArray(ValueType):
    """"""

    @overload
    def __init__(self, args: Array[object]):
        """:param args:"""
    @overload
    def __init__(self, arg0: object):
        """:param arg0:"""
    @overload
    def __init__(self, arg0: object, arg1: object):
        """:param arg0:
        :param arg1:
        """
    @overload
    def __init__(self, arg0: object, arg1: object, arg2: object):
        """:param arg0:
        :param arg1:
        :param arg2:
        """
    @property
    def Item(self) -> object:
        """:return:"""
    @property
    def Length(self) -> int:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def __getitem__(self, index: int) -> object:
        """:param index:
        :return:
        """

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
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def IntToString(cls, l: int, radix: int, width: int, paddingChar: Char, flags: int) -> str:
        """:param l:
        :param radix:
        :param width:
        :param paddingChar:
        :param flags:
        :return:
        """
    @classmethod
    def LongToString(cls, l: int, radix: int, width: int, paddingChar: Char, flags: int) -> str:
        """:param l:
        :param radix:
        :param width:
        :param paddingChar:
        :param flags:
        :return:
        """
    @classmethod
    @overload
    def StringToInt(cls, s: str, radix: int, flags: int) -> int:
        """:param s:
        :param radix:
        :param flags:
        :return:
        """
    @classmethod
    @overload
    def StringToInt(cls, s: str, radix: int, flags: int, currPos: int) -> int:
        """:param s:
        :param radix:
        :param flags:
        :param currPos:
        :return:
        """
    @classmethod
    @overload
    def StringToInt(cls, s: str, radix: int, flags: int, currPos: int) -> int:
        """:param s:
        :param radix:
        :param flags:
        :param currPos:
        :return:
        """
    @classmethod
    @overload
    def StringToLong(cls, s: str, radix: int, flags: int) -> int:
        """:param s:
        :param radix:
        :param flags:
        :return:
        """
    @classmethod
    @overload
    def StringToLong(cls, s: str, radix: int, flags: int, currPos: int) -> int:
        """:param s:
        :param radix:
        :param flags:
        :param currPos:
        :return:
        """
    @classmethod
    @overload
    def StringToLong(cls, s: str, radix: int, flags: int, currPos: int) -> int:
        """:param s:
        :param radix:
        :param flags:
        :param currPos:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

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
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class PinnableBufferCache(Object):
    """"""

    def __init__(self, cacheName: str, numberOfElements: int):
        """:param cacheName:
        :param numberOfElements:
        """
    def AllocateBuffer(self) -> Array[int]:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def FreeBuffer(self, buffer: Array[int]) -> None:
        """:param buffer:"""
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class PinnableBufferCacheEventSource(EventSource, IDisposable):
    """"""

    Log: Final[ClassVar[PinnableBufferCacheEventSource]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def ConstructionException(self) -> Exception:
        """:return:"""
    @classmethod
    @property
    def CurrentThreadActivityId(cls) -> Guid:
        """:return:"""
    @property
    def Guid(self) -> Guid:
        """:return:"""
    @property
    def Name(self) -> str:
        """:return:"""
    @property
    def Settings(self) -> EventSourceSettings:
        """:return:"""
    def AgePendingBuffersResults(
        self, cacheName: str, promotedToFreeListCount: int, heldBackCount: int
    ) -> None:
        """:param cacheName:
        :param promotedToFreeListCount:
        :param heldBackCount:
        """
    def AllocateBuffer(
        self,
        cacheName: str,
        objectId: int,
        objectHash: int,
        objectGen: int,
        freeCountAfter: int,
    ) -> None:
        """:param cacheName:
        :param objectId:
        :param objectHash:
        :param objectGen:
        :param freeCountAfter:
        """
    def AllocateBufferAged(self, cacheName: str, agedCount: int) -> None:
        """:param cacheName:
        :param agedCount:
        """
    def AllocateBufferCreatingNewBuffers(
        self, cacheName: str, totalBuffsBefore: int, objectCount: int
    ) -> None:
        """:param cacheName:
        :param totalBuffsBefore:
        :param objectCount:
        """
    def AllocateBufferFreeListEmpty(self, cacheName: str, notGen2CountBefore: int) -> None:
        """:param cacheName:
        :param notGen2CountBefore:
        """
    def AllocateBufferFromNotGen2(self, cacheName: str, notGen2CountAfter: int) -> None:
        """:param cacheName:
        :param notGen2CountAfter:
        """
    def Create(self, cacheName: str) -> None:
        """:param cacheName:"""
    def DebugMessage(self, message: str) -> None:
        """:param message:"""
    def DebugMessage1(self, message: str, value: int) -> None:
        """:param message:
        :param value:
        """
    def DebugMessage2(self, message: str, value1: int, value2: int) -> None:
        """:param message:
        :param value1:
        :param value2:
        """
    def DebugMessage3(self, message: str, value1: int, value2: int, value3: int) -> None:
        """:param message:
        :param value1:
        :param value2:
        :param value3:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def FreeBuffer(
        self, cacheName: str, objectId: int, objectHash: int, freeCountBefore: int
    ) -> None:
        """:param cacheName:
        :param objectId:
        :param objectHash:
        :param freeCountBefore:
        """
    def FreeBufferNull(self, cacheName: str, freeCountBefore: int) -> None:
        """:param cacheName:
        :param freeCountBefore:
        """
    def FreeBufferStillTooYoung(self, cacheName: str, notGen2CountBefore: int) -> None:
        """:param cacheName:
        :param notGen2CountBefore:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetTrait(self, key: str) -> str:
        """:param key:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def IsEnabled(self) -> bool:
        """:return:"""
    @overload
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords) -> bool:
        """:param level:
        :param keywords:
        :return:
        """
    @overload
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords, channel: EventChannel) -> bool:
        """:param level:
        :param keywords:
        :param channel:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""
    def TrimCheck(
        self,
        cacheName: str,
        totalBuffs: int,
        neededMoreThanFreeList: bool,
        deltaMSec: int,
    ) -> None:
        """:param cacheName:
        :param totalBuffs:
        :param neededMoreThanFreeList:
        :param deltaMSec:
        """
    def TrimExperiment(
        self, cacheName: str, totalBuffs: int, freeListCount: int, numTrimTrial: int
    ) -> None:
        """:param cacheName:
        :param totalBuffs:
        :param freeListCount:
        :param numTrimTrial:
        """
    def TrimFlush(
        self,
        cacheName: str,
        totalBuffs: int,
        freeListCount: int,
        notGen2CountBefore: int,
    ) -> None:
        """:param cacheName:
        :param totalBuffs:
        :param freeListCount:
        :param notGen2CountBefore:
        """
    def TrimFree(self, cacheName: str, totalBuffs: int, freeListCount: int, toBeFreed: int) -> None:
        """:param cacheName:
        :param totalBuffs:
        :param freeListCount:
        :param toBeFreed:
        """
    def TrimFreeSizeOK(self, cacheName: str, totalBuffs: int, freeListCount: int) -> None:
        """:param cacheName:
        :param totalBuffs:
        :param freeListCount:
        """
    def WalkFreeListResult(
        self, cacheName: str, freeListCount: int, gen0BuffersInFreeList: int
    ) -> None:
        """:param cacheName:
        :param freeListCount:
        :param gen0BuffersInFreeList:
        """
    @overload
    def Write(self, eventName: str) -> None:
        """:param eventName:"""
    @overload
    def Write(self, eventName: str, data: T) -> None:
        """:param eventName:
        :param data:
        """
    @overload
    def Write(self, eventName: str, options: EventSourceOptions) -> None:
        """:param eventName:
        :param options:
        """
    @overload
    def Write(self, eventName: str, options: EventSourceOptions, data: T) -> None:
        """:param eventName:
        :param options:
        :param data:
        """
    @overload
    def Write(self, eventName: str, options: EventSourceOptions, data: T) -> None:
        """:param eventName:
        :param options:
        :param data:
        """
    @overload
    def Write(
        self,
        eventName: str,
        options: EventSourceOptions,
        activityId: Guid,
        relatedActivityId: Guid,
        data: T,
    ) -> None:
        """:param eventName:
        :param options:
        :param activityId:
        :param relatedActivityId:
        :param data:
        """
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
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, inner: Exception):
        """:param message:
        :param inner:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

Predicate: Callable[[T], bool] = ...
"""

:param obj: 
:return: 
"""

class ProgressStatics(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class Progress(Generic[T], Object, IProgress[T]):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, handler: Action[T]):
        """:param handler:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def Report(self, value: T) -> None:
        """:param value:"""
    def ToString(self) -> str:
        """:return:"""
    ProgressChanged: EventType[EventHandler[T]] = ...
    """"""

class Random(Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, Seed: int):
        """:param Seed:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def Next(self) -> int:
        """:return:"""
    @overload
    def Next(self, maxValue: int) -> int:
        """:param maxValue:
        :return:
        """
    @overload
    def Next(self, minValue: int, maxValue: int) -> int:
        """:param minValue:
        :param maxValue:
        :return:
        """
    def NextBytes(self, buffer: Array[int]) -> None:
        """:param buffer:"""
    def NextDouble(self) -> float:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class RankException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

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
        """:return:"""
    @property
    def AssemblyQualifiedName(self) -> str:
        """:return:"""
    @property
    def Attributes(self) -> TypeAttributes:
        """:return:"""
    @property
    def BaseType(self) -> Type:
        """:return:"""
    @property
    def ContainsGenericParameters(self) -> bool:
        """:return:"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """:return:"""
    @property
    def DeclaredConstructors(self) -> IEnumerable[ConstructorInfo]:
        """:return:"""
    @property
    def DeclaredEvents(self) -> IEnumerable[EventInfo]:
        """:return:"""
    @property
    def DeclaredFields(self) -> IEnumerable[FieldInfo]:
        """:return:"""
    @property
    def DeclaredMembers(self) -> IEnumerable[MemberInfo]:
        """:return:"""
    @property
    def DeclaredMethods(self) -> IEnumerable[MethodInfo]:
        """:return:"""
    @property
    def DeclaredNestedTypes(self) -> IEnumerable[TypeInfo]:
        """:return:"""
    @property
    def DeclaredProperties(self) -> IEnumerable[PropertyInfo]:
        """:return:"""
    @property
    def DeclaringMethod(self) -> MethodBase:
        """:return:"""
    @property
    def DeclaringType(self) -> Type:
        """:return:"""
    @property
    def DeclaringType(self) -> Type:
        """:return:"""
    @classmethod
    @property
    def DefaultBinder(cls) -> Binder:
        """:return:"""
    @property
    def FullName(self) -> str:
        """:return:"""
    @property
    def GUID(self) -> Guid:
        """:return:"""
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes:
        """:return:"""
    @property
    def GenericParameterPosition(self) -> int:
        """:return:"""
    @property
    def GenericTypeArguments(self) -> Array[Type]:
        """:return:"""
    @property
    def GenericTypeParameters(self) -> Array[Type]:
        """:return:"""
    @property
    def HasElementType(self) -> bool:
        """:return:"""
    @property
    def ImplementedInterfaces(self) -> IEnumerable[Type]:
        """:return:"""
    @property
    def IsAbstract(self) -> bool:
        """:return:"""
    @property
    def IsAnsiClass(self) -> bool:
        """:return:"""
    @property
    def IsArray(self) -> bool:
        """:return:"""
    @property
    def IsAutoClass(self) -> bool:
        """:return:"""
    @property
    def IsAutoLayout(self) -> bool:
        """:return:"""
    @property
    def IsByRef(self) -> bool:
        """:return:"""
    @property
    def IsCOMObject(self) -> bool:
        """:return:"""
    @property
    def IsClass(self) -> bool:
        """:return:"""
    @property
    def IsConstructedGenericType(self) -> bool:
        """:return:"""
    @property
    def IsContextful(self) -> bool:
        """:return:"""
    @property
    def IsEnum(self) -> bool:
        """:return:"""
    @property
    def IsExplicitLayout(self) -> bool:
        """:return:"""
    @property
    def IsGenericParameter(self) -> bool:
        """:return:"""
    @property
    def IsGenericType(self) -> bool:
        """:return:"""
    @property
    def IsGenericTypeDefinition(self) -> bool:
        """:return:"""
    @property
    def IsImport(self) -> bool:
        """:return:"""
    @property
    def IsInterface(self) -> bool:
        """:return:"""
    @property
    def IsLayoutSequential(self) -> bool:
        """:return:"""
    @property
    def IsMarshalByRef(self) -> bool:
        """:return:"""
    @property
    def IsNested(self) -> bool:
        """:return:"""
    @property
    def IsNestedAssembly(self) -> bool:
        """:return:"""
    @property
    def IsNestedFamANDAssem(self) -> bool:
        """:return:"""
    @property
    def IsNestedFamORAssem(self) -> bool:
        """:return:"""
    @property
    def IsNestedFamily(self) -> bool:
        """:return:"""
    @property
    def IsNestedPrivate(self) -> bool:
        """:return:"""
    @property
    def IsNestedPublic(self) -> bool:
        """:return:"""
    @property
    def IsNotPublic(self) -> bool:
        """:return:"""
    @property
    def IsPointer(self) -> bool:
        """:return:"""
    @property
    def IsPrimitive(self) -> bool:
        """:return:"""
    @property
    def IsPublic(self) -> bool:
        """:return:"""
    @property
    def IsSealed(self) -> bool:
        """:return:"""
    @property
    def IsSecurityCritical(self) -> bool:
        """:return:"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """:return:"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """:return:"""
    @property
    def IsSerializable(self) -> bool:
        """:return:"""
    @property
    def IsSpecialName(self) -> bool:
        """:return:"""
    @property
    def IsUnicodeClass(self) -> bool:
        """:return:"""
    @property
    def IsValueType(self) -> bool:
        """:return:"""
    @property
    def IsVisible(self) -> bool:
        """:return:"""
    @property
    def MemberType(self) -> MemberTypes:
        """:return:"""
    @property
    def MemberType(self) -> MemberTypes:
        """:return:"""
    @property
    def MetadataToken(self) -> int:
        """:return:"""
    @property
    def Module(self) -> Module:
        """:return:"""
    @property
    def Module(self) -> Module:
        """:return:"""
    @property
    def Name(self) -> str:
        """:return:"""
    @property
    def Name(self) -> str:
        """:return:"""
    @property
    def Namespace(self) -> str:
        """:return:"""
    @property
    def ReflectedType(self) -> Type:
        """:return:"""
    @property
    def ReflectedType(self) -> Type:
        """:return:"""
    @property
    def StructLayoutAttribute(self) -> StructLayoutAttribute:
        """:return:"""
    @property
    def TypeHandle(self) -> RuntimeTypeHandle:
        """:return:"""
    @property
    def TypeInitializer(self) -> ConstructorInfo:
        """:return:"""
    @property
    def UnderlyingSystemType(self) -> Type:
        """:return:"""
    @property
    def UnderlyingSystemType(self) -> Type:
        """:return:"""
    def AsType(self) -> Type:
        """:return:"""
    def Clone(self) -> object:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, o: Type) -> bool:
        """:param o:
        :return:
        """
    def FindInterfaces(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """:param filter:
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
        """:param memberType:
        :param bindingAttr:
        :param filter:
        :param filterCriteria:
        :return:
        """
    def GetArrayRank(self) -> int:
        """:return:"""
    @overload
    def GetConstructor(self, types: Array[Type]) -> ConstructorInfo:
        """:param types:
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
        """:param bindingAttr:
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
        """:param bindingAttr:
        :param binder:
        :param callConvention:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetConstructors(self) -> Array[ConstructorInfo]:
        """:return:"""
    @overload
    def GetConstructors(self, bindingAttr: BindingFlags) -> Array[ConstructorInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """:param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """:param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """:param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """:param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """:param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """:param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """:return:"""
    def GetDeclaredEvent(self, name: str) -> EventInfo:
        """:param name:
        :return:
        """
    def GetDeclaredField(self, name: str) -> FieldInfo:
        """:param name:
        :return:
        """
    def GetDeclaredMethod(self, name: str) -> MethodInfo:
        """:param name:
        :return:
        """
    def GetDeclaredMethods(self, name: str) -> IEnumerable[MethodInfo]:
        """:param name:
        :return:
        """
    def GetDeclaredNestedType(self, name: str) -> TypeInfo:
        """:param name:
        :return:
        """
    def GetDeclaredProperty(self, name: str) -> PropertyInfo:
        """:param name:
        :return:
        """
    def GetDefaultMembers(self) -> Array[MemberInfo]:
        """:return:"""
    def GetElementType(self) -> Type:
        """:return:"""
    def GetEnumName(self, value: object) -> str:
        """:param value:
        :return:
        """
    def GetEnumNames(self) -> Array[str]:
        """:return:"""
    def GetEnumUnderlyingType(self) -> Type:
        """:return:"""
    def GetEnumValues(self) -> Array:
        """:return:"""
    @overload
    def GetEvent(self, name: str) -> EventInfo:
        """:param name:
        :return:
        """
    @overload
    def GetEvent(self, name: str, bindingAttr: BindingFlags) -> EventInfo:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetEvents(self) -> Array[EventInfo]:
        """:return:"""
    @overload
    def GetEvents(self, bindingAttr: BindingFlags) -> Array[EventInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """:param name:
        :return:
        """
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """:return:"""
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """:param bindingAttr:
        :return:
        """
    def GetGenericArguments(self) -> Array[Type]:
        """:return:"""
    def GetGenericParameterConstraints(self) -> Array[Type]:
        """:return:"""
    def GetGenericTypeDefinition(self) -> Type:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetInterface(self, name: str) -> Type:
        """:param name:
        :return:
        """
    @overload
    def GetInterface(self, name: str, ignoreCase: bool) -> Type:
        """:param name:
        :param ignoreCase:
        :return:
        """
    def GetInterfaceMap(self, interfaceType: Type) -> InterfaceMapping:
        """:param interfaceType:
        :return:
        """
    def GetInterfaces(self) -> Array[Type]:
        """:return:"""
    @overload
    def GetMember(self, name: str) -> Array[MemberInfo]:
        """:param name:
        :return:
        """
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMember(
        self, name: str, type: MemberTypes, bindingAttr: BindingFlags
    ) -> Array[MemberInfo]:
        """:param name:
        :param type:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMembers(self) -> Array[MemberInfo]:
        """:return:"""
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """:param name:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """:param name:
        :param types:
        :return:
        """
    @overload
    def GetMethod(
        self, name: str, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> MethodInfo:
        """:param name:
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
        """:param name:
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
        """:param name:
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
        """:param name:
        :param bindingAttr:
        :param binder:
        :param callConvention:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """:return:"""
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetNestedType(self, name: str) -> Type:
        """:param name:
        :return:
        """
    @overload
    def GetNestedType(self, name: str, bindingAttr: BindingFlags) -> Type:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetNestedTypes(self) -> Array[Type]:
        """:return:"""
    @overload
    def GetNestedTypes(self, bindingAttr: BindingFlags) -> Array[Type]:
        """:param bindingAttr:
        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetProperties(self) -> Array[PropertyInfo]:
        """:return:"""
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str) -> PropertyInfo:
        """:param name:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, types: Array[Type]) -> PropertyInfo:
        """:param name:
        :param types:
        :return:
        """
    @overload
    def GetProperty(self, name: str, returnType: Type) -> PropertyInfo:
        """:param name:
        :param returnType:
        :return:
        """
    @overload
    def GetProperty(self, name: str, returnType: Type, types: Array[Type]) -> PropertyInfo:
        """:param name:
        :param returnType:
        :param types:
        :return:
        """
    @overload
    def GetProperty(
        self,
        name: str,
        returnType: Type,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> PropertyInfo:
        """:param name:
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
        """:param name:
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
        """:param name:
        :param bindingAttr:
        :param binder:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetTypeInfo(self) -> TypeInfo:
        """:return:"""
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
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
        """:param dispIdMember:
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
        """:param dispIdMember:
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
        """:param name:
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
        """:param name:
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
        """:param name:
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
        """:param name:
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
        """:param typeInfo:
        :return:
        """
    @overload
    def IsAssignableFrom(self, c: Type) -> bool:
        """:param c:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """:param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """:param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """:param attributeType:
        :param inherit:
        :return:
        """
    def IsEnumDefined(self, value: object) -> bool:
        """:param value:
        :return:
        """
    def IsEquivalentTo(self, other: Type) -> bool:
        """:param other:
        :return:
        """
    def IsInstanceOfType(self, o: object) -> bool:
        """:param o:
        :return:
        """
    def IsSubclassOf(self, c: Type) -> bool:
        """:param c:
        :return:
        """
    @overload
    def MakeArrayType(self) -> Type:
        """:return:"""
    @overload
    def MakeArrayType(self, rank: int) -> Type:
        """:param rank:
        :return:
        """
    def MakeByRefType(self) -> Type:
        """:return:"""
    def MakeGenericType(self, typeArguments: Array[Type]) -> Type:
        """:param typeArguments:
        :return:
        """
    def MakePointerType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class ResId(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class ResolveEventArgs(EventArgs):
    """"""

    @overload
    def __init__(self, name: str):
        """:param name:"""
    @overload
    def __init__(self, name: str, requestingAssembly: Assembly):
        """:param name:
        :param requestingAssembly:
        """
    @property
    def Name(self) -> str:
        """:return:"""
    @property
    def RequestingAssembly(self) -> Assembly:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

ResolveEventHandler: Callable[[object, ResolveEventArgs], Assembly] = ...
"""

:param sender: 
:param args: 
:return: 
"""

class Resolver(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class RuntimeArgumentHandle(ValueType):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class RuntimeFieldHandle(ValueType, ISerializable):
    """"""

    @property
    def Value(self) -> IntPtr:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, handle: RuntimeFieldHandle) -> bool:
        """:param handle:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def __eq__(self, other: RuntimeFieldHandle) -> bool:
        """:param other:
        :return:
        """
    def __ne__(self, other: RuntimeFieldHandle) -> bool:
        """:param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: RuntimeFieldHandle, right: RuntimeFieldHandle) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: RuntimeFieldHandle, right: RuntimeFieldHandle) -> bool:
        """:param left:
        :param right:
        :return:
        """

class RuntimeFieldHandleInternal(ValueType):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class RuntimeFieldInfoStub(Object, IRuntimeFieldInfo):
    """"""

    def __init__(self, methodHandleValue: IntPtr, keepalive: object):
        """:param methodHandleValue:
        :param keepalive:
        """
    @property
    def Value(self) -> RuntimeFieldHandleInternal:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class RuntimeMethodHandle(ValueType, ISerializable):
    """"""

    @property
    def Value(self) -> IntPtr:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, handle: RuntimeMethodHandle) -> bool:
        """:param handle:
        :return:
        """
    def GetFunctionPointer(self) -> IntPtr:
        """:return:"""
    def GetHashCode(self) -> int:
        """:return:"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def __eq__(self, other: RuntimeMethodHandle) -> bool:
        """:param other:
        :return:
        """
    def __ne__(self, other: RuntimeMethodHandle) -> bool:
        """:param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: RuntimeMethodHandle, right: RuntimeMethodHandle) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: RuntimeMethodHandle, right: RuntimeMethodHandle) -> bool:
        """:param left:
        :param right:
        :return:
        """

class RuntimeMethodHandleInternal(ValueType):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class RuntimeMethodInfoStub(Object, IRuntimeMethodInfo):
    """"""

    m_value: Final[RuntimeMethodHandleInternal] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, methodHandleValue: IntPtr, keepalive: object):
        """:param methodHandleValue:
        :param keepalive:
        """
    @overload
    def __init__(self, methodHandleValue: RuntimeMethodHandleInternal, keepalive: object):
        """:param methodHandleValue:
        :param keepalive:
        """
    @property
    def Value(self) -> RuntimeMethodHandleInternal:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

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
        """:return:"""
    @property
    def AssemblyQualifiedName(self) -> str:
        """:return:"""
    @property
    def Attributes(self) -> TypeAttributes:
        """:return:"""
    @property
    def BaseType(self) -> Type:
        """:return:"""
    @property
    def ContainsGenericParameters(self) -> bool:
        """:return:"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """:return:"""
    @property
    def DeclaredConstructors(self) -> IEnumerable[ConstructorInfo]:
        """:return:"""
    @property
    def DeclaredEvents(self) -> IEnumerable[EventInfo]:
        """:return:"""
    @property
    def DeclaredFields(self) -> IEnumerable[FieldInfo]:
        """:return:"""
    @property
    def DeclaredMembers(self) -> IEnumerable[MemberInfo]:
        """:return:"""
    @property
    def DeclaredMethods(self) -> IEnumerable[MethodInfo]:
        """:return:"""
    @property
    def DeclaredNestedTypes(self) -> IEnumerable[TypeInfo]:
        """:return:"""
    @property
    def DeclaredProperties(self) -> IEnumerable[PropertyInfo]:
        """:return:"""
    @property
    def DeclaringMethod(self) -> MethodBase:
        """:return:"""
    @property
    def DeclaringType(self) -> Type:
        """:return:"""
    @property
    def DeclaringType(self) -> Type:
        """:return:"""
    @classmethod
    @property
    def DefaultBinder(cls) -> Binder:
        """:return:"""
    @property
    def FullName(self) -> str:
        """:return:"""
    @property
    def GUID(self) -> Guid:
        """:return:"""
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes:
        """:return:"""
    @property
    def GenericParameterPosition(self) -> int:
        """:return:"""
    @property
    def GenericTypeArguments(self) -> Array[Type]:
        """:return:"""
    @property
    def GenericTypeParameters(self) -> Array[Type]:
        """:return:"""
    @property
    def HasElementType(self) -> bool:
        """:return:"""
    @property
    def ImplementedInterfaces(self) -> IEnumerable[Type]:
        """:return:"""
    @property
    def IsAbstract(self) -> bool:
        """:return:"""
    @property
    def IsAnsiClass(self) -> bool:
        """:return:"""
    @property
    def IsArray(self) -> bool:
        """:return:"""
    @property
    def IsAutoClass(self) -> bool:
        """:return:"""
    @property
    def IsAutoLayout(self) -> bool:
        """:return:"""
    @property
    def IsByRef(self) -> bool:
        """:return:"""
    @property
    def IsCOMObject(self) -> bool:
        """:return:"""
    @property
    def IsClass(self) -> bool:
        """:return:"""
    @property
    def IsConstructedGenericType(self) -> bool:
        """:return:"""
    @property
    def IsContextful(self) -> bool:
        """:return:"""
    @property
    def IsEnum(self) -> bool:
        """:return:"""
    @property
    def IsExplicitLayout(self) -> bool:
        """:return:"""
    @property
    def IsGenericParameter(self) -> bool:
        """:return:"""
    @property
    def IsGenericType(self) -> bool:
        """:return:"""
    @property
    def IsGenericTypeDefinition(self) -> bool:
        """:return:"""
    @property
    def IsImport(self) -> bool:
        """:return:"""
    @property
    def IsInterface(self) -> bool:
        """:return:"""
    @property
    def IsLayoutSequential(self) -> bool:
        """:return:"""
    @property
    def IsMarshalByRef(self) -> bool:
        """:return:"""
    @property
    def IsNested(self) -> bool:
        """:return:"""
    @property
    def IsNestedAssembly(self) -> bool:
        """:return:"""
    @property
    def IsNestedFamANDAssem(self) -> bool:
        """:return:"""
    @property
    def IsNestedFamORAssem(self) -> bool:
        """:return:"""
    @property
    def IsNestedFamily(self) -> bool:
        """:return:"""
    @property
    def IsNestedPrivate(self) -> bool:
        """:return:"""
    @property
    def IsNestedPublic(self) -> bool:
        """:return:"""
    @property
    def IsNotPublic(self) -> bool:
        """:return:"""
    @property
    def IsPointer(self) -> bool:
        """:return:"""
    @property
    def IsPrimitive(self) -> bool:
        """:return:"""
    @property
    def IsPublic(self) -> bool:
        """:return:"""
    @property
    def IsSealed(self) -> bool:
        """:return:"""
    @property
    def IsSecurityCritical(self) -> bool:
        """:return:"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """:return:"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """:return:"""
    @property
    def IsSerializable(self) -> bool:
        """:return:"""
    @property
    def IsSpecialName(self) -> bool:
        """:return:"""
    @property
    def IsUnicodeClass(self) -> bool:
        """:return:"""
    @property
    def IsValueType(self) -> bool:
        """:return:"""
    @property
    def IsVisible(self) -> bool:
        """:return:"""
    @property
    def MemberType(self) -> MemberTypes:
        """:return:"""
    @property
    def MemberType(self) -> MemberTypes:
        """:return:"""
    @property
    def MetadataToken(self) -> int:
        """:return:"""
    @property
    def Module(self) -> Module:
        """:return:"""
    @property
    def Module(self) -> Module:
        """:return:"""
    @property
    def Name(self) -> str:
        """:return:"""
    @property
    def Name(self) -> str:
        """:return:"""
    @property
    def Namespace(self) -> str:
        """:return:"""
    @property
    def ReflectedType(self) -> Type:
        """:return:"""
    @property
    def ReflectedType(self) -> Type:
        """:return:"""
    @property
    def StructLayoutAttribute(self) -> StructLayoutAttribute:
        """:return:"""
    @property
    def TypeHandle(self) -> RuntimeTypeHandle:
        """:return:"""
    @property
    def TypeInitializer(self) -> ConstructorInfo:
        """:return:"""
    @property
    def UnderlyingSystemType(self) -> Type:
        """:return:"""
    @property
    def UnderlyingSystemType(self) -> Type:
        """:return:"""
    def AsType(self) -> Type:
        """:return:"""
    def Clone(self) -> object:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, o: Type) -> bool:
        """:param o:
        :return:
        """
    def FindInterfaces(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """:param filter:
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
        """:param memberType:
        :param bindingAttr:
        :param filter:
        :param filterCriteria:
        :return:
        """
    def GetArrayRank(self) -> int:
        """:return:"""
    @overload
    def GetConstructor(self, types: Array[Type]) -> ConstructorInfo:
        """:param types:
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
        """:param bindingAttr:
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
        """:param bindingAttr:
        :param binder:
        :param callConvention:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetConstructors(self) -> Array[ConstructorInfo]:
        """:return:"""
    @overload
    def GetConstructors(self, bindingAttr: BindingFlags) -> Array[ConstructorInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """:param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """:param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """:param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """:param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """:param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """:param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """:return:"""
    def GetDeclaredEvent(self, name: str) -> EventInfo:
        """:param name:
        :return:
        """
    def GetDeclaredField(self, name: str) -> FieldInfo:
        """:param name:
        :return:
        """
    def GetDeclaredMethod(self, name: str) -> MethodInfo:
        """:param name:
        :return:
        """
    def GetDeclaredMethods(self, name: str) -> IEnumerable[MethodInfo]:
        """:param name:
        :return:
        """
    def GetDeclaredNestedType(self, name: str) -> TypeInfo:
        """:param name:
        :return:
        """
    def GetDeclaredProperty(self, name: str) -> PropertyInfo:
        """:param name:
        :return:
        """
    def GetDefaultMembers(self) -> Array[MemberInfo]:
        """:return:"""
    def GetElementType(self) -> Type:
        """:return:"""
    def GetEnumName(self, value: object) -> str:
        """:param value:
        :return:
        """
    def GetEnumNames(self) -> Array[str]:
        """:return:"""
    def GetEnumUnderlyingType(self) -> Type:
        """:return:"""
    def GetEnumValues(self) -> Array:
        """:return:"""
    @overload
    def GetEvent(self, name: str) -> EventInfo:
        """:param name:
        :return:
        """
    @overload
    def GetEvent(self, name: str, bindingAttr: BindingFlags) -> EventInfo:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetEvents(self) -> Array[EventInfo]:
        """:return:"""
    @overload
    def GetEvents(self, bindingAttr: BindingFlags) -> Array[EventInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """:param name:
        :return:
        """
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """:return:"""
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """:param bindingAttr:
        :return:
        """
    def GetGenericArguments(self) -> Array[Type]:
        """:return:"""
    def GetGenericParameterConstraints(self) -> Array[Type]:
        """:return:"""
    def GetGenericTypeDefinition(self) -> Type:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetInterface(self, name: str) -> Type:
        """:param name:
        :return:
        """
    @overload
    def GetInterface(self, name: str, ignoreCase: bool) -> Type:
        """:param name:
        :param ignoreCase:
        :return:
        """
    def GetInterfaceMap(self, interfaceType: Type) -> InterfaceMapping:
        """:param interfaceType:
        :return:
        """
    def GetInterfaces(self) -> Array[Type]:
        """:return:"""
    @overload
    def GetMember(self, name: str) -> Array[MemberInfo]:
        """:param name:
        :return:
        """
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMember(
        self, name: str, type: MemberTypes, bindingAttr: BindingFlags
    ) -> Array[MemberInfo]:
        """:param name:
        :param type:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMembers(self) -> Array[MemberInfo]:
        """:return:"""
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """:param name:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """:param name:
        :param types:
        :return:
        """
    @overload
    def GetMethod(
        self, name: str, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> MethodInfo:
        """:param name:
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
        """:param name:
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
        """:param name:
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
        """:param name:
        :param bindingAttr:
        :param binder:
        :param callConvention:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """:return:"""
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetNestedType(self, name: str) -> Type:
        """:param name:
        :return:
        """
    @overload
    def GetNestedType(self, name: str, bindingAttr: BindingFlags) -> Type:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetNestedTypes(self) -> Array[Type]:
        """:return:"""
    @overload
    def GetNestedTypes(self, bindingAttr: BindingFlags) -> Array[Type]:
        """:param bindingAttr:
        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetProperties(self) -> Array[PropertyInfo]:
        """:return:"""
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str) -> PropertyInfo:
        """:param name:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, types: Array[Type]) -> PropertyInfo:
        """:param name:
        :param types:
        :return:
        """
    @overload
    def GetProperty(self, name: str, returnType: Type) -> PropertyInfo:
        """:param name:
        :param returnType:
        :return:
        """
    @overload
    def GetProperty(self, name: str, returnType: Type, types: Array[Type]) -> PropertyInfo:
        """:param name:
        :param returnType:
        :param types:
        :return:
        """
    @overload
    def GetProperty(
        self,
        name: str,
        returnType: Type,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> PropertyInfo:
        """:param name:
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
        """:param name:
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
        """:param name:
        :param bindingAttr:
        :param binder:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetTypeInfo(self) -> TypeInfo:
        """:return:"""
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
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
        """:param dispIdMember:
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
        """:param dispIdMember:
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
        """:param name:
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
        """:param name:
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
        """:param name:
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
        """:param name:
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
        """:param typeInfo:
        :return:
        """
    @overload
    def IsAssignableFrom(self, c: Type) -> bool:
        """:param c:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """:param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """:param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """:param attributeType:
        :param inherit:
        :return:
        """
    def IsEnumDefined(self, value: object) -> bool:
        """:param value:
        :return:
        """
    def IsEquivalentTo(self, other: Type) -> bool:
        """:param other:
        :return:
        """
    def IsInstanceOfType(self, o: object) -> bool:
        """:param o:
        :return:
        """
    def IsSubclassOf(self, c: Type) -> bool:
        """:param c:
        :return:
        """
    @overload
    def MakeArrayType(self) -> Type:
        """:return:"""
    @overload
    def MakeArrayType(self, rank: int) -> Type:
        """:param rank:
        :return:
        """
    def MakeByRefType(self) -> Type:
        """:return:"""
    def MakeGenericType(self, typeArguments: Array[Type]) -> Type:
        """:param typeArguments:
        :return:
        """
    def MakePointerType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    def __eq__(self, other: RuntimeType) -> bool:
        """:param other:
        :return:
        """
    def __ne__(self, other: RuntimeType) -> bool:
        """:param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: RuntimeType, right: RuntimeType) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: RuntimeType, right: RuntimeType) -> bool:
        """:param left:
        :param right:
        :return:
        """

class RuntimeTypeHandle(ValueType, ISerializable):
    """"""

    @property
    def Value(self) -> IntPtr:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, handle: RuntimeTypeHandle) -> bool:
        """:param handle:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetModuleHandle(self) -> ModuleHandle:
        """:return:"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    @overload
    def __eq__(self, other: object) -> bool:
        """:param other:
        :return:
        """
    @overload
    def __eq__(self, other: RuntimeTypeHandle) -> bool:
        """:param other:
        :return:
        """
    @overload
    def __ne__(self, other: object) -> bool:
        """:param other:
        :return:
        """
    @overload
    def __ne__(self, other: RuntimeTypeHandle) -> bool:
        """:param other:
        :return:
        """
    @classmethod
    @overload
    def op_Equality(cls, left: object, right: RuntimeTypeHandle) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def op_Equality(cls, left: RuntimeTypeHandle, right: object) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def op_Inequality(cls, left: object, right: RuntimeTypeHandle) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def op_Inequality(cls, left: RuntimeTypeHandle, right: object) -> bool:
        """:param left:
        :param right:
        :return:
        """

class SByte(
    ValueType,
    IComparable,
    IComparable[SByte],
    IConvertible,
    IEquatable[SByte],
    IFormattable,
):
    """"""

    MaxValue: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MinValue: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: int) -> int:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: int) -> bool:
        """:param other:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeCode(self) -> TypeCode:
        """:return:"""
    @classmethod
    @overload
    def Parse(cls, s: str) -> int:
        """:param s:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles) -> int:
        """:param s:
        :param style:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider) -> int:
        """:param s:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles, provider: IFormatProvider) -> int:
        """:param s:
        :param style:
        :param provider:
        :return:
        """
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """:param provider:
        :return:
        """
    def ToByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToChar(self, provider: IFormatProvider) -> Char:
        """:param provider:
        :return:
        """
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """:param provider:
        :return:
        """
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """:param provider:
        :return:
        """
    def ToDouble(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    def ToInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSingle(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self, format: str) -> str:
        """:param format:
        :return:
        """
    @overload
    def ToString(self, format: str, formatProvider: IFormatProvider) -> str:
        """:param format:
        :param formatProvider:
        :return:
        """
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """:param conversionType:
        :param provider:
        :return:
        """
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    @classmethod
    @overload
    def TryParse(cls, s: str, result: int) -> Tuple[bool, int]:
        """:param s:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryParse(
        cls, s: str, style: NumberStyles, provider: IFormatProvider, result: int
    ) -> Tuple[bool, int]:
        """:param s:
        :param style:
        :param provider:
        :param result:
        :return:
        """

class SR(Object):
    """"""

    @classmethod
    @property
    def Resources(cls) -> ResourceManager:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    @classmethod
    def GetObject(cls, name: str) -> object:
        """:param name:
        :return:
        """
    @classmethod
    @overload
    def GetString(cls, name: str) -> str:
        """:param name:
        :return:
        """
    @classmethod
    @overload
    def GetString(cls, name: str, usedFallback: bool) -> Tuple[str, bool]:
        """:param name:
        :param usedFallback:
        :return:
        """
    @classmethod
    @overload
    def GetString(cls, name: str, args: Array[object]) -> str:
        """:param name:
        :param args:
        :return:
        """

class SRCategoryAttribute(CategoryAttribute, _Attribute):
    """"""

    def __init__(self, category: str):
        """:param category:"""
    @classmethod
    @property
    def Action(cls) -> CategoryAttribute:
        """:return:"""
    @classmethod
    @property
    def Appearance(cls) -> CategoryAttribute:
        """:return:"""
    @classmethod
    @property
    def Asynchronous(cls) -> CategoryAttribute:
        """:return:"""
    @classmethod
    @property
    def Behavior(cls) -> CategoryAttribute:
        """:return:"""
    @property
    def Category(self) -> str:
        """:return:"""
    @classmethod
    @property
    def Data(cls) -> CategoryAttribute:
        """:return:"""
    @classmethod
    @property
    def Default(cls) -> CategoryAttribute:
        """:return:"""
    @classmethod
    @property
    def Design(cls) -> CategoryAttribute:
        """:return:"""
    @classmethod
    @property
    def DragDrop(cls) -> CategoryAttribute:
        """:return:"""
    @classmethod
    @property
    def Focus(cls) -> CategoryAttribute:
        """:return:"""
    @classmethod
    @property
    def Format(cls) -> CategoryAttribute:
        """:return:"""
    @classmethod
    @property
    def Key(cls) -> CategoryAttribute:
        """:return:"""
    @classmethod
    @property
    def Layout(cls) -> CategoryAttribute:
        """:return:"""
    @classmethod
    @property
    def Mouse(cls) -> CategoryAttribute:
        """:return:"""
    @classmethod
    @property
    def WindowStyle(cls) -> CategoryAttribute:
        """:return:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
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
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class SRDescriptionAttribute(DescriptionAttribute, _Attribute):
    """"""

    def __init__(self, description: str):
        """:param description:"""
    @property
    def Description(self) -> str:
        """:return:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
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
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class STAThreadAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
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
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class SZArrayHelper(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class SafeTypeNameParserHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def IsClosed(self) -> bool:
        """:return:"""
    @property
    def IsInvalid(self) -> bool:
        """:return:"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """:param success:"""
    def DangerousGetHandle(self) -> IntPtr:
        """:return:"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """:return:"""

class SecurityUtils(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class SerializableAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
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
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class SharedStatics(Object):
    """"""

    @classmethod
    @property
    def Remoting_Identity_IDGuid(cls) -> str:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    @classmethod
    def GetSharedStringMaker(cls) -> Tokenizer.StringMaker:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def ReleaseSharedStringMaker(cls, maker: StringMaker) -> None:
        """:param maker:"""
    def ToString(self) -> str:
        """:return:"""

class Signature(Object):
    """"""

    @overload
    def __init__(self, fieldHandle: IRuntimeFieldInfo, declaringType: RuntimeType):
        """:param fieldHandle:
        :param declaringType:
        """
    @overload
    def __init__(self, methodHandle: IRuntimeMethodInfo, declaringType: RuntimeType):
        """:param methodHandle:
        :param declaringType:
        """
    @overload
    def __init__(self, pCorSig: None, cCorSig: int, declaringType: RuntimeType):
        """:param pCorSig:
        :param cCorSig:
        :param declaringType:
        """
    @overload
    def __init__(
        self,
        method: IRuntimeMethodInfo,
        arguments: Array[RuntimeType],
        returnType: RuntimeType,
        callingConvention: CallingConventions,
    ):
        """:param method:
        :param arguments:
        :param returnType:
        :param callingConvention:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class Single(
    ValueType,
    IComparable,
    IComparable[Single],
    IConvertible,
    IEquatable[Single],
    IFormattable,
):
    """"""

    Epsilon: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    MaxValue: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    MinValue: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    NaN: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    NegativeInfinity: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    PositiveInfinity: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: float) -> int:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: float) -> bool:
        """:param other:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeCode(self) -> TypeCode:
        """:return:"""
    @classmethod
    def IsInfinity(cls, f: float) -> bool:
        """:param f:
        :return:
        """
    @classmethod
    def IsNaN(cls, f: float) -> bool:
        """:param f:
        :return:
        """
    @classmethod
    def IsNegativeInfinity(cls, f: float) -> bool:
        """:param f:
        :return:
        """
    @classmethod
    def IsPositiveInfinity(cls, f: float) -> bool:
        """:param f:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str) -> float:
        """:param s:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles) -> float:
        """:param s:
        :param style:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider) -> float:
        """:param s:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles, provider: IFormatProvider) -> float:
        """:param s:
        :param style:
        :param provider:
        :return:
        """
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """:param provider:
        :return:
        """
    def ToByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToChar(self, provider: IFormatProvider) -> Char:
        """:param provider:
        :return:
        """
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """:param provider:
        :return:
        """
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """:param provider:
        :return:
        """
    def ToDouble(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    def ToInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSingle(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self, format: str) -> str:
        """:param format:
        :return:
        """
    @overload
    def ToString(self, format: str, formatProvider: IFormatProvider) -> str:
        """:param format:
        :param formatProvider:
        :return:
        """
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """:param conversionType:
        :param provider:
        :return:
        """
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    @classmethod
    @overload
    def TryParse(cls, s: str, result: float) -> Tuple[bool, float]:
        """:param s:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryParse(
        cls, s: str, style: NumberStyles, provider: IFormatProvider, result: float
    ) -> Tuple[bool, float]:
        """:param s:
        :param style:
        :param provider:
        :param result:
        :return:
        """
    def __eq__(self, other: float) -> bool:
        """:param other:
        :return:
        """
    def __ge__(self, other: float) -> bool:
        """:param other:
        :return:
        """
    def __gt__(self, other: float) -> bool:
        """:param other:
        :return:
        """
    def __le__(self, other: float) -> bool:
        """:param other:
        :return:
        """
    def __lt__(self, other: float) -> bool:
        """:param other:
        :return:
        """
    def __ne__(self, other: float) -> bool:
        """:param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: float, right: float) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    def op_GreaterThan(cls, left: float, right: float) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    def op_GreaterThanOrEqual(cls, left: float, right: float) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: float, right: float) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    def op_LessThan(cls, left: float, right: float) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    def op_LessThanOrEqual(cls, left: float, right: float) -> bool:
        """:param left:
        :param right:
        :return:
        """

class SizedReference(Object, IDisposable):
    """"""

    def __init__(self, target: object):
        """:param target:"""
    @property
    def ApproximateSize(self) -> int:
        """:return:"""
    @property
    def Target(self) -> object:
        """:return:"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class StackOverflowException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

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

    Empty: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, value: Array[Char]):
        """:param value:"""
    @overload
    def __init__(self, value: Char):
        """:param value:"""
    @overload
    def __init__(self, value: int):
        """:param value:"""
    @overload
    def __init__(self, c: Char, count: int):
        """:param c:
        :param count:
        """
    @overload
    def __init__(self, value: Array[Char], startIndex: int, length: int):
        """:param value:
        :param startIndex:
        :param length:
        """
    @overload
    def __init__(self, value: Char, startIndex: int, length: int):
        """:param value:
        :param startIndex:
        :param length:
        """
    @overload
    def __init__(self, value: int, startIndex: int, length: int):
        """:param value:
        :param startIndex:
        :param length:
        """
    @overload
    def __init__(self, value: int, startIndex: int, length: int, enc: Encoding):
        """:param value:
        :param startIndex:
        :param length:
        :param enc:
        """
    @property
    def Chars(self) -> Char:
        """:return:"""
    @property
    def Length(self) -> int:
        """:return:"""
    def Clone(self) -> object:
        """:return:"""
    @classmethod
    @overload
    def Compare(cls, strA: str, strB: str) -> int:
        """:param strA:
        :param strB:
        :return:
        """
    @classmethod
    @overload
    def Compare(cls, strA: str, strB: str, ignoreCase: bool) -> int:
        """:param strA:
        :param strB:
        :param ignoreCase:
        :return:
        """
    @classmethod
    @overload
    def Compare(cls, strA: str, strB: str, comparisonType: StringComparison) -> int:
        """:param strA:
        :param strB:
        :param comparisonType:
        :return:
        """
    @classmethod
    @overload
    def Compare(cls, strA: str, strB: str, culture: CultureInfo, options: CompareOptions) -> int:
        """:param strA:
        :param strB:
        :param culture:
        :param options:
        :return:
        """
    @classmethod
    @overload
    def Compare(cls, strA: str, strB: str, ignoreCase: bool, culture: CultureInfo) -> int:
        """:param strA:
        :param strB:
        :param ignoreCase:
        :param culture:
        :return:
        """
    @classmethod
    @overload
    def Compare(cls, strA: str, indexA: int, strB: str, indexB: int, length: int) -> int:
        """:param strA:
        :param indexA:
        :param strB:
        :param indexB:
        :param length:
        :return:
        """
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
    ) -> int:
        """:param strA:
        :param indexA:
        :param strB:
        :param indexB:
        :param length:
        :param ignoreCase:
        :return:
        """
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
        """:param strA:
        :param indexA:
        :param strB:
        :param indexB:
        :param length:
        :param comparisonType:
        :return:
        """
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
        """:param strA:
        :param indexA:
        :param strB:
        :param indexB:
        :param length:
        :param culture:
        :param options:
        :return:
        """
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
        """:param strA:
        :param indexA:
        :param strB:
        :param indexB:
        :param length:
        :param ignoreCase:
        :param culture:
        :return:
        """
    @classmethod
    @overload
    def CompareOrdinal(cls, strA: str, strB: str) -> int:
        """:param strA:
        :param strB:
        :return:
        """
    @classmethod
    @overload
    def CompareOrdinal(cls, strA: str, indexA: int, strB: str, indexB: int, length: int) -> int:
        """:param strA:
        :param indexA:
        :param strB:
        :param indexB:
        :param length:
        :return:
        """
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: str) -> int:
        """:param other:
        :return:
        """
    @classmethod
    @overload
    def Concat(cls, values: IEnumerable[T]) -> str:
        """:param values:
        :return:
        """
    @classmethod
    @overload
    def Concat(cls, values: IEnumerable[str]) -> str:
        """:param values:
        :return:
        """
    @classmethod
    @overload
    def Concat(cls, args: Array[object]) -> str:
        """:param args:
        :return:
        """
    @classmethod
    @overload
    def Concat(cls, values: Array[str]) -> str:
        """:param values:
        :return:
        """
    @classmethod
    @overload
    def Concat(cls, arg0: object) -> str:
        """:param arg0:
        :return:
        """
    @classmethod
    @overload
    def Concat(cls, arg0: object, arg1: object) -> str:
        """:param arg0:
        :param arg1:
        :return:
        """
    @classmethod
    @overload
    def Concat(cls, str0: str, str1: str) -> str:
        """:param str0:
        :param str1:
        :return:
        """
    @classmethod
    @overload
    def Concat(cls, arg0: object, arg1: object, arg2: object) -> str:
        """:param arg0:
        :param arg1:
        :param arg2:
        :return:
        """
    @classmethod
    @overload
    def Concat(cls, str0: str, str1: str, str2: str) -> str:
        """:param str0:
        :param str1:
        :param str2:
        :return:
        """
    @classmethod
    @overload
    def Concat(cls, arg0: object, arg1: object, arg2: object, arg3: object) -> str:
        """:param arg0:
        :param arg1:
        :param arg2:
        :param arg3:
        :return:
        """
    @classmethod
    @overload
    def Concat(cls, str0: str, str1: str, str2: str, str3: str) -> str:
        """:param str0:
        :param str1:
        :param str2:
        :param str3:
        :return:
        """
    def Contains(self, value: str) -> bool:
        """:param value:
        :return:
        """
    @classmethod
    def Copy(cls, str: str) -> str:
        """:param str:
        :return:
        """
    def CopyTo(
        self,
        sourceIndex: int,
        destination: Array[Char],
        destinationIndex: int,
        count: int,
    ) -> None:
        """:param sourceIndex:
        :param destination:
        :param destinationIndex:
        :param count:
        """
    @overload
    def EndsWith(self, value: str) -> bool:
        """:param value:
        :return:
        """
    @overload
    def EndsWith(self, value: str, comparisonType: StringComparison) -> bool:
        """:param value:
        :param comparisonType:
        :return:
        """
    @overload
    def EndsWith(self, value: str, ignoreCase: bool, culture: CultureInfo) -> bool:
        """:param value:
        :param ignoreCase:
        :param culture:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: str) -> bool:
        """:param other:
        :return:
        """
    @classmethod
    @overload
    def Equals(cls, a: str, b: str) -> bool:
        """:param a:
        :param b:
        :return:
        """
    @overload
    def Equals(self, value: str, comparisonType: StringComparison) -> bool:
        """:param value:
        :param comparisonType:
        :return:
        """
    @classmethod
    @overload
    def Equals(cls, a: str, b: str, comparisonType: StringComparison) -> bool:
        """:param a:
        :param b:
        :param comparisonType:
        :return:
        """
    @classmethod
    @overload
    def Format(cls, format: str, args: Array[object]) -> str:
        """:param format:
        :param args:
        :return:
        """
    @classmethod
    @overload
    def Format(cls, format: str, arg0: object) -> str:
        """:param format:
        :param arg0:
        :return:
        """
    @classmethod
    @overload
    def Format(cls, provider: IFormatProvider, format: str, args: Array[object]) -> str:
        """:param provider:
        :param format:
        :param args:
        :return:
        """
    @classmethod
    @overload
    def Format(cls, provider: IFormatProvider, format: str, arg0: object) -> str:
        """:param provider:
        :param format:
        :param arg0:
        :return:
        """
    @classmethod
    @overload
    def Format(cls, format: str, arg0: object, arg1: object) -> str:
        """:param format:
        :param arg0:
        :param arg1:
        :return:
        """
    @classmethod
    @overload
    def Format(cls, provider: IFormatProvider, format: str, arg0: object, arg1: object) -> str:
        """:param provider:
        :param format:
        :param arg0:
        :param arg1:
        :return:
        """
    @classmethod
    @overload
    def Format(cls, format: str, arg0: object, arg1: object, arg2: object) -> str:
        """:param format:
        :param arg0:
        :param arg1:
        :param arg2:
        :return:
        """
    @classmethod
    @overload
    def Format(
        cls,
        provider: IFormatProvider,
        format: str,
        arg0: object,
        arg1: object,
        arg2: object,
    ) -> str:
        """:param provider:
        :param format:
        :param arg0:
        :param arg1:
        :param arg2:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """:return:"""
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeCode(self) -> TypeCode:
        """:return:"""
    @overload
    def IndexOf(self, value: Char) -> int:
        """:param value:
        :return:
        """
    @overload
    def IndexOf(self, value: str) -> int:
        """:param value:
        :return:
        """
    @overload
    def IndexOf(self, value: Char, startIndex: int) -> int:
        """:param value:
        :param startIndex:
        :return:
        """
    @overload
    def IndexOf(self, value: str, startIndex: int) -> int:
        """:param value:
        :param startIndex:
        :return:
        """
    @overload
    def IndexOf(self, value: str, comparisonType: StringComparison) -> int:
        """:param value:
        :param comparisonType:
        :return:
        """
    @overload
    def IndexOf(self, value: Char, startIndex: int, count: int) -> int:
        """:param value:
        :param startIndex:
        :param count:
        :return:
        """
    @overload
    def IndexOf(self, value: str, startIndex: int, count: int) -> int:
        """:param value:
        :param startIndex:
        :param count:
        :return:
        """
    @overload
    def IndexOf(self, value: str, startIndex: int, comparisonType: StringComparison) -> int:
        """:param value:
        :param startIndex:
        :param comparisonType:
        :return:
        """
    @overload
    def IndexOf(
        self, value: str, startIndex: int, count: int, comparisonType: StringComparison
    ) -> int:
        """:param value:
        :param startIndex:
        :param count:
        :param comparisonType:
        :return:
        """
    @overload
    def IndexOfAny(self, anyOf: Array[Char]) -> int:
        """:param anyOf:
        :return:
        """
    @overload
    def IndexOfAny(self, anyOf: Array[Char], startIndex: int) -> int:
        """:param anyOf:
        :param startIndex:
        :return:
        """
    @overload
    def IndexOfAny(self, anyOf: Array[Char], startIndex: int, count: int) -> int:
        """:param anyOf:
        :param startIndex:
        :param count:
        :return:
        """
    def Insert(self, startIndex: int, value: str) -> str:
        """:param startIndex:
        :param value:
        :return:
        """
    @classmethod
    def Intern(cls, str: str) -> str:
        """:param str:
        :return:
        """
    @classmethod
    def IsInterned(cls, str: str) -> str:
        """:param str:
        :return:
        """
    @overload
    def IsNormalized(self) -> bool:
        """:return:"""
    @overload
    def IsNormalized(self, normalizationForm: NormalizationForm) -> bool:
        """:param normalizationForm:
        :return:
        """
    @classmethod
    def IsNullOrEmpty(cls, value: str) -> bool:
        """:param value:
        :return:
        """
    @classmethod
    def IsNullOrWhiteSpace(cls, value: str) -> bool:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def Join(cls, separator: str, values: IEnumerable[T]) -> str:
        """:param separator:
        :param values:
        :return:
        """
    @classmethod
    @overload
    def Join(cls, separator: str, values: IEnumerable[str]) -> str:
        """:param separator:
        :param values:
        :return:
        """
    @classmethod
    @overload
    def Join(cls, separator: str, values: Array[object]) -> str:
        """:param separator:
        :param values:
        :return:
        """
    @classmethod
    @overload
    def Join(cls, separator: str, value: Array[str]) -> str:
        """:param separator:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def Join(cls, separator: str, value: Array[str], startIndex: int, count: int) -> str:
        """:param separator:
        :param value:
        :param startIndex:
        :param count:
        :return:
        """
    @overload
    def LastIndexOf(self, value: Char) -> int:
        """:param value:
        :return:
        """
    @overload
    def LastIndexOf(self, value: str) -> int:
        """:param value:
        :return:
        """
    @overload
    def LastIndexOf(self, value: Char, startIndex: int) -> int:
        """:param value:
        :param startIndex:
        :return:
        """
    @overload
    def LastIndexOf(self, value: str, startIndex: int) -> int:
        """:param value:
        :param startIndex:
        :return:
        """
    @overload
    def LastIndexOf(self, value: str, comparisonType: StringComparison) -> int:
        """:param value:
        :param comparisonType:
        :return:
        """
    @overload
    def LastIndexOf(self, value: Char, startIndex: int, count: int) -> int:
        """:param value:
        :param startIndex:
        :param count:
        :return:
        """
    @overload
    def LastIndexOf(self, value: str, startIndex: int, count: int) -> int:
        """:param value:
        :param startIndex:
        :param count:
        :return:
        """
    @overload
    def LastIndexOf(self, value: str, startIndex: int, comparisonType: StringComparison) -> int:
        """:param value:
        :param startIndex:
        :param comparisonType:
        :return:
        """
    @overload
    def LastIndexOf(
        self, value: str, startIndex: int, count: int, comparisonType: StringComparison
    ) -> int:
        """:param value:
        :param startIndex:
        :param count:
        :param comparisonType:
        :return:
        """
    @overload
    def LastIndexOfAny(self, anyOf: Array[Char]) -> int:
        """:param anyOf:
        :return:
        """
    @overload
    def LastIndexOfAny(self, anyOf: Array[Char], startIndex: int) -> int:
        """:param anyOf:
        :param startIndex:
        :return:
        """
    @overload
    def LastIndexOfAny(self, anyOf: Array[Char], startIndex: int, count: int) -> int:
        """:param anyOf:
        :param startIndex:
        :param count:
        :return:
        """
    @overload
    def Normalize(self) -> str:
        """:return:"""
    @overload
    def Normalize(self, normalizationForm: NormalizationForm) -> str:
        """:param normalizationForm:
        :return:
        """
    @overload
    def PadLeft(self, totalWidth: int) -> str:
        """:param totalWidth:
        :return:
        """
    @overload
    def PadLeft(self, totalWidth: int, paddingChar: Char) -> str:
        """:param totalWidth:
        :param paddingChar:
        :return:
        """
    @overload
    def PadRight(self, totalWidth: int) -> str:
        """:param totalWidth:
        :return:
        """
    @overload
    def PadRight(self, totalWidth: int, paddingChar: Char) -> str:
        """:param totalWidth:
        :param paddingChar:
        :return:
        """
    @overload
    def Remove(self, startIndex: int) -> str:
        """:param startIndex:
        :return:
        """
    @overload
    def Remove(self, startIndex: int, count: int) -> str:
        """:param startIndex:
        :param count:
        :return:
        """
    @overload
    def Replace(self, oldChar: Char, newChar: Char) -> str:
        """:param oldChar:
        :param newChar:
        :return:
        """
    @overload
    def Replace(self, oldValue: str, newValue: str) -> str:
        """:param oldValue:
        :param newValue:
        :return:
        """
    @overload
    def Split(self, separator: Array[Char]) -> Array[str]:
        """:param separator:
        :return:
        """
    @overload
    def Split(self, separator: Array[Char], count: int) -> Array[str]:
        """:param separator:
        :param count:
        :return:
        """
    @overload
    def Split(self, separator: Array[Char], options: StringSplitOptions) -> Array[str]:
        """:param separator:
        :param options:
        :return:
        """
    @overload
    def Split(self, separator: Array[str], options: StringSplitOptions) -> Array[str]:
        """:param separator:
        :param options:
        :return:
        """
    @overload
    def Split(self, separator: Array[Char], count: int, options: StringSplitOptions) -> Array[str]:
        """:param separator:
        :param count:
        :param options:
        :return:
        """
    @overload
    def Split(self, separator: Array[str], count: int, options: StringSplitOptions) -> Array[str]:
        """:param separator:
        :param count:
        :param options:
        :return:
        """
    @overload
    def StartsWith(self, value: str) -> bool:
        """:param value:
        :return:
        """
    @overload
    def StartsWith(self, value: str, comparisonType: StringComparison) -> bool:
        """:param value:
        :param comparisonType:
        :return:
        """
    @overload
    def StartsWith(self, value: str, ignoreCase: bool, culture: CultureInfo) -> bool:
        """:param value:
        :param ignoreCase:
        :param culture:
        :return:
        """
    @overload
    def Substring(self, startIndex: int) -> str:
        """:param startIndex:
        :return:
        """
    @overload
    def Substring(self, startIndex: int, length: int) -> str:
        """:param startIndex:
        :param length:
        :return:
        """
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """:param provider:
        :return:
        """
    def ToByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToChar(self, provider: IFormatProvider) -> Char:
        """:param provider:
        :return:
        """
    @overload
    def ToCharArray(self) -> Array[Char]:
        """:return:"""
    @overload
    def ToCharArray(self, startIndex: int, length: int) -> Array[Char]:
        """:param startIndex:
        :param length:
        :return:
        """
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """:param provider:
        :return:
        """
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """:param provider:
        :return:
        """
    def ToDouble(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    def ToInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    @overload
    def ToLower(self) -> str:
        """:return:"""
    @overload
    def ToLower(self, culture: CultureInfo) -> str:
        """:param culture:
        :return:
        """
    def ToLowerInvariant(self) -> str:
        """:return:"""
    def ToSByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSingle(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """:param provider:
        :return:
        """
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """:param conversionType:
        :param provider:
        :return:
        """
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    @overload
    def ToUpper(self) -> str:
        """:return:"""
    @overload
    def ToUpper(self, culture: CultureInfo) -> str:
        """:param culture:
        :return:
        """
    def ToUpperInvariant(self) -> str:
        """:return:"""
    @overload
    def Trim(self) -> str:
        """:return:"""
    @overload
    def Trim(self, trimChars: Array[Char]) -> str:
        """:param trimChars:
        :return:
        """
    def TrimEnd(self, trimChars: Array[Char]) -> str:
        """:param trimChars:
        :return:
        """
    def TrimStart(self, trimChars: Array[Char]) -> str:
        """:param trimChars:
        :return:
        """
    def __eq__(self, other: str) -> bool:
        """:param other:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """:return:"""
    @overload
    def __iter__(self) -> Iterator[Char]:
        """:return:"""
    def __ne__(self, other: str) -> bool:
        """:param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, a: str, b: str) -> bool:
        """:param a:
        :param b:
        :return:
        """
    @classmethod
    def op_Inequality(cls, a: str, b: str) -> bool:
        """:param a:
        :param b:
        :return:
        """

class StringComparer(
    ABC,
    Object,
    IComparer[String],
    IEqualityComparer[String],
    IComparer,
    IEqualityComparer,
):
    """"""

    @classmethod
    @property
    def CurrentCulture(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def CurrentCultureIgnoreCase(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def InvariantCulture(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def InvariantCultureIgnoreCase(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def Ordinal(cls) -> StringComparer:
        """:return:"""
    @classmethod
    @property
    def OrdinalIgnoreCase(cls) -> StringComparer:
        """:return:"""
    @overload
    def Compare(self, x: object, y: object) -> int:
        """:param x:
        :param y:
        :return:
        """
    @overload
    def Compare(self, x: str, y: str) -> int:
        """:param x:
        :param y:
        :return:
        """
    @classmethod
    def Create(cls, culture: CultureInfo, ignoreCase: bool) -> StringComparer:
        """:param culture:
        :param ignoreCase:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """:param x:
        :param y:
        :return:
        """
    @overload
    def Equals(self, x: str, y: str) -> bool:
        """:param x:
        :param y:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def GetHashCode(self, obj: str) -> int:
        """:param obj:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

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
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    @overload
    def IsNormalized(cls, value: str) -> bool:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def IsNormalized(cls, value: str, normalizationForm: NormalizationForm) -> bool:
        """:param value:
        :param normalizationForm:
        :return:
        """
    @classmethod
    @overload
    def Normalize(cls, value: str) -> str:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def Normalize(cls, value: str, normalizationForm: NormalizationForm) -> str:
        """:param value:
        :param normalizationForm:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class StringSplitOptions(Enum):
    """"""

    _None: StringSplitOptions = ...
    """"""
    RemoveEmptyEntries: StringSplitOptions = ...
    """"""

class SwitchStructure(ValueType):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class SystemException(Exception, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class System_LazyDebugView(Generic[T], Object):
    """"""

    def __init__(self, lazy: Lazy[T]):
        """:param lazy:"""
    @property
    def IsValueCreated(self) -> bool:
        """:return:"""
    @property
    def IsValueFaulted(self) -> bool:
        """:return:"""
    @property
    def Mode(self) -> LazyThreadSafetyMode:
        """:return:"""
    @property
    def Value(self) -> T:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class ThreadStaticAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
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
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class ThrowHelper(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class TimeSpan(ValueType, IComparable, IComparable[TimeSpan], IEquatable[TimeSpan], IFormattable):
    """"""

    MaxValue: Final[ClassVar[TimeSpan]] = ...
    """
    
    :return: 
    """
    MinValue: Final[ClassVar[TimeSpan]] = ...
    """
    
    :return: 
    """
    TicksPerDay: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    TicksPerHour: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    TicksPerMillisecond: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    TicksPerMinute: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    TicksPerSecond: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    Zero: Final[ClassVar[TimeSpan]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, ticks: int):
        """:param ticks:"""
    @overload
    def __init__(self, hours: int, minutes: int, seconds: int):
        """:param hours:
        :param minutes:
        :param seconds:
        """
    @overload
    def __init__(self, days: int, hours: int, minutes: int, seconds: int):
        """:param days:
        :param hours:
        :param minutes:
        :param seconds:
        """
    @overload
    def __init__(self, days: int, hours: int, minutes: int, seconds: int, milliseconds: int):
        """:param days:
        :param hours:
        :param minutes:
        :param seconds:
        :param milliseconds:
        """
    @property
    def Days(self) -> int:
        """:return:"""
    @property
    def Hours(self) -> int:
        """:return:"""
    @property
    def Milliseconds(self) -> int:
        """:return:"""
    @property
    def Minutes(self) -> int:
        """:return:"""
    @property
    def Seconds(self) -> int:
        """:return:"""
    @property
    def Ticks(self) -> int:
        """:return:"""
    @property
    def TotalDays(self) -> float:
        """:return:"""
    @property
    def TotalHours(self) -> float:
        """:return:"""
    @property
    def TotalMilliseconds(self) -> float:
        """:return:"""
    @property
    def TotalMinutes(self) -> float:
        """:return:"""
    @property
    def TotalSeconds(self) -> float:
        """:return:"""
    def Add(self, ts: TimeSpan) -> TimeSpan:
        """:param ts:
        :return:
        """
    @classmethod
    def Compare(cls, t1: TimeSpan, t2: TimeSpan) -> int:
        """:param t1:
        :param t2:
        :return:
        """
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: TimeSpan) -> int:
        """:param other:
        :return:
        """
    def Duration(self) -> TimeSpan:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: TimeSpan) -> bool:
        """:param other:
        :return:
        """
    @classmethod
    @overload
    def Equals(cls, t1: TimeSpan, t2: TimeSpan) -> bool:
        """:param t1:
        :param t2:
        :return:
        """
    @classmethod
    def FromDays(cls, value: float) -> TimeSpan:
        """:param value:
        :return:
        """
    @classmethod
    def FromHours(cls, value: float) -> TimeSpan:
        """:param value:
        :return:
        """
    @classmethod
    def FromMilliseconds(cls, value: float) -> TimeSpan:
        """:param value:
        :return:
        """
    @classmethod
    def FromMinutes(cls, value: float) -> TimeSpan:
        """:param value:
        :return:
        """
    @classmethod
    def FromSeconds(cls, value: float) -> TimeSpan:
        """:param value:
        :return:
        """
    @classmethod
    def FromTicks(cls, value: int) -> TimeSpan:
        """:param value:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def Negate(self) -> TimeSpan:
        """:return:"""
    @classmethod
    @overload
    def Parse(cls, s: str) -> TimeSpan:
        """:param s:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, input: str, formatProvider: IFormatProvider) -> TimeSpan:
        """:param input:
        :param formatProvider:
        :return:
        """
    @classmethod
    @overload
    def ParseExact(
        cls, input: str, formats: Array[str], formatProvider: IFormatProvider
    ) -> TimeSpan:
        """:param input:
        :param formats:
        :param formatProvider:
        :return:
        """
    @classmethod
    @overload
    def ParseExact(cls, input: str, format: str, formatProvider: IFormatProvider) -> TimeSpan:
        """:param input:
        :param format:
        :param formatProvider:
        :return:
        """
    @classmethod
    @overload
    def ParseExact(
        cls,
        input: str,
        formats: Array[str],
        formatProvider: IFormatProvider,
        styles: TimeSpanStyles,
    ) -> TimeSpan:
        """:param input:
        :param formats:
        :param formatProvider:
        :param styles:
        :return:
        """
    @classmethod
    @overload
    def ParseExact(
        cls,
        input: str,
        format: str,
        formatProvider: IFormatProvider,
        styles: TimeSpanStyles,
    ) -> TimeSpan:
        """:param input:
        :param format:
        :param formatProvider:
        :param styles:
        :return:
        """
    def Subtract(self, ts: TimeSpan) -> TimeSpan:
        """:param ts:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, format: str) -> str:
        """:param format:
        :return:
        """
    @overload
    def ToString(self, format: str, formatProvider: IFormatProvider) -> str:
        """:param format:
        :param formatProvider:
        :return:
        """
    @classmethod
    @overload
    def TryParse(cls, s: str, result: TimeSpan) -> Tuple[bool, TimeSpan]:
        """:param s:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryParse(
        cls, input: str, formatProvider: IFormatProvider, result: TimeSpan
    ) -> Tuple[bool, TimeSpan]:
        """:param input:
        :param formatProvider:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryParseExact(
        cls,
        input: str,
        formats: Array[str],
        formatProvider: IFormatProvider,
        result: TimeSpan,
    ) -> Tuple[bool, TimeSpan]:
        """:param input:
        :param formats:
        :param formatProvider:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryParseExact(
        cls, input: str, format: str, formatProvider: IFormatProvider, result: TimeSpan
    ) -> Tuple[bool, TimeSpan]:
        """:param input:
        :param format:
        :param formatProvider:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryParseExact(
        cls,
        input: str,
        formats: Array[str],
        formatProvider: IFormatProvider,
        styles: TimeSpanStyles,
        result: TimeSpan,
    ) -> Tuple[bool, TimeSpan]:
        """:param input:
        :param formats:
        :param formatProvider:
        :param styles:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryParseExact(
        cls,
        input: str,
        format: str,
        formatProvider: IFormatProvider,
        styles: TimeSpanStyles,
        result: TimeSpan,
    ) -> Tuple[bool, TimeSpan]:
        """:param input:
        :param format:
        :param formatProvider:
        :param styles:
        :param result:
        :return:
        """
    def __add__(self, other: TimeSpan) -> TimeSpan:
        """:param other:
        :return:
        """
    def __eq__(self, other: TimeSpan) -> bool:
        """:param other:
        :return:
        """
    def __ge__(self, other: TimeSpan) -> bool:
        """:param other:
        :return:
        """
    def __gt__(self, other: TimeSpan) -> bool:
        """:param other:
        :return:
        """
    def __le__(self, other: TimeSpan) -> bool:
        """:param other:
        :return:
        """
    def __lt__(self, other: TimeSpan) -> bool:
        """:param other:
        :return:
        """
    def __ne__(self, other: TimeSpan) -> bool:
        """:param other:
        :return:
        """
    def __neg__(self) -> TimeSpan:
        """:return:"""
    def __pos__(self) -> TimeSpan:
        """:return:"""
    def __sub__(self, other: TimeSpan) -> TimeSpan:
        """:param other:
        :return:
        """
    @classmethod
    def op_Addition(cls, t1: TimeSpan, t2: TimeSpan) -> TimeSpan:
        """:param t1:
        :param t2:
        :return:
        """
    @classmethod
    def op_Equality(cls, t1: TimeSpan, t2: TimeSpan) -> bool:
        """:param t1:
        :param t2:
        :return:
        """
    @classmethod
    def op_GreaterThan(cls, t1: TimeSpan, t2: TimeSpan) -> bool:
        """:param t1:
        :param t2:
        :return:
        """
    @classmethod
    def op_GreaterThanOrEqual(cls, t1: TimeSpan, t2: TimeSpan) -> bool:
        """:param t1:
        :param t2:
        :return:
        """
    @classmethod
    def op_Inequality(cls, t1: TimeSpan, t2: TimeSpan) -> bool:
        """:param t1:
        :param t2:
        :return:
        """
    @classmethod
    def op_LessThan(cls, t1: TimeSpan, t2: TimeSpan) -> bool:
        """:param t1:
        :param t2:
        :return:
        """
    @classmethod
    def op_LessThanOrEqual(cls, t1: TimeSpan, t2: TimeSpan) -> bool:
        """:param t1:
        :param t2:
        :return:
        """
    @classmethod
    def op_Subtraction(cls, t1: TimeSpan, t2: TimeSpan) -> TimeSpan:
        """:param t1:
        :param t2:
        :return:
        """
    @classmethod
    def op_UnaryNegation(cls, t: TimeSpan) -> TimeSpan:
        """:param t:
        :return:
        """
    @classmethod
    def op_UnaryPlus(cls, t: TimeSpan) -> TimeSpan:
        """:param t:
        :return:
        """

class TimeZone(ABC, Object):
    """"""

    @classmethod
    @property
    def CurrentTimeZone(cls) -> TimeZone:
        """:return:"""
    @property
    def DaylightName(self) -> str:
        """:return:"""
    @property
    def StandardName(self) -> str:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetDaylightChanges(self, year: int) -> DaylightTime:
        """:param year:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def GetUtcOffset(self, time: DateTime) -> TimeSpan:
        """:param time:
        :return:
        """
    @overload
    def IsDaylightSavingTime(self, time: DateTime) -> bool:
        """:param time:
        :return:
        """
    @classmethod
    @overload
    def IsDaylightSavingTime(cls, time: DateTime, daylightTimes: DaylightTime) -> bool:
        """:param time:
        :param daylightTimes:
        :return:
        """
    def ToLocalTime(self, time: DateTime) -> DateTime:
        """:param time:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""
    def ToUniversalTime(self, time: DateTime) -> DateTime:
        """:param time:
        :return:
        """

class TimeZoneInfo(Object, IDeserializationCallback, ISerializable, IEquatable[TimeZoneInfo]):
    """"""

    @property
    def BaseUtcOffset(self) -> TimeSpan:
        """:return:"""
    @property
    def DaylightName(self) -> str:
        """:return:"""
    @property
    def DisplayName(self) -> str:
        """:return:"""
    @property
    def Id(self) -> str:
        """:return:"""
    @classmethod
    @property
    def Local(cls) -> TimeZoneInfo:
        """:return:"""
    @property
    def StandardName(self) -> str:
        """:return:"""
    @property
    def SupportsDaylightSavingTime(self) -> bool:
        """:return:"""
    @classmethod
    @property
    def Utc(cls) -> TimeZoneInfo:
        """:return:"""
    @classmethod
    def ClearCachedData(cls) -> None:
        """"""
    @classmethod
    @overload
    def ConvertTime(cls, dateTime: DateTime, destinationTimeZone: TimeZoneInfo) -> DateTime:
        """:param dateTime:
        :param destinationTimeZone:
        :return:
        """
    @classmethod
    @overload
    def ConvertTime(
        cls, dateTimeOffset: DateTimeOffset, destinationTimeZone: TimeZoneInfo
    ) -> DateTimeOffset:
        """:param dateTimeOffset:
        :param destinationTimeZone:
        :return:
        """
    @classmethod
    @overload
    def ConvertTime(
        cls,
        dateTime: DateTime,
        sourceTimeZone: TimeZoneInfo,
        destinationTimeZone: TimeZoneInfo,
    ) -> DateTime:
        """:param dateTime:
        :param sourceTimeZone:
        :param destinationTimeZone:
        :return:
        """
    @classmethod
    @overload
    def ConvertTimeBySystemTimeZoneId(
        cls, dateTime: DateTime, destinationTimeZoneId: str
    ) -> DateTime:
        """:param dateTime:
        :param destinationTimeZoneId:
        :return:
        """
    @classmethod
    @overload
    def ConvertTimeBySystemTimeZoneId(
        cls, dateTimeOffset: DateTimeOffset, destinationTimeZoneId: str
    ) -> DateTimeOffset:
        """:param dateTimeOffset:
        :param destinationTimeZoneId:
        :return:
        """
    @classmethod
    @overload
    def ConvertTimeBySystemTimeZoneId(
        cls, dateTime: DateTime, sourceTimeZoneId: str, destinationTimeZoneId: str
    ) -> DateTime:
        """:param dateTime:
        :param sourceTimeZoneId:
        :param destinationTimeZoneId:
        :return:
        """
    @classmethod
    def ConvertTimeFromUtc(cls, dateTime: DateTime, destinationTimeZone: TimeZoneInfo) -> DateTime:
        """:param dateTime:
        :param destinationTimeZone:
        :return:
        """
    @classmethod
    @overload
    def ConvertTimeToUtc(cls, dateTime: DateTime) -> DateTime:
        """:param dateTime:
        :return:
        """
    @classmethod
    @overload
    def ConvertTimeToUtc(cls, dateTime: DateTime, sourceTimeZone: TimeZoneInfo) -> DateTime:
        """:param dateTime:
        :param sourceTimeZone:
        :return:
        """
    @classmethod
    @overload
    def CreateCustomTimeZone(
        cls,
        id: str,
        baseUtcOffset: TimeSpan,
        displayName: str,
        standardDisplayName: str,
    ) -> TimeZoneInfo:
        """:param id:
        :param baseUtcOffset:
        :param displayName:
        :param standardDisplayName:
        :return:
        """
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
        """:param id:
        :param baseUtcOffset:
        :param displayName:
        :param standardDisplayName:
        :param daylightDisplayName:
        :param adjustmentRules:
        :return:
        """
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
        """:param id:
        :param baseUtcOffset:
        :param displayName:
        :param standardDisplayName:
        :param daylightDisplayName:
        :param adjustmentRules:
        :param disableDaylightSavingTime:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: TimeZoneInfo) -> bool:
        """:param other:
        :return:
        """
    @classmethod
    def FindSystemTimeZoneById(cls, id: str) -> TimeZoneInfo:
        """:param id:
        :return:
        """
    @classmethod
    def FromSerializedString(cls, source: str) -> TimeZoneInfo:
        """:param source:
        :return:
        """
    def GetAdjustmentRules(self) -> Array[AdjustmentRule]:
        """:return:"""
    @overload
    def GetAmbiguousTimeOffsets(self, dateTime: DateTime) -> Array[TimeSpan]:
        """:param dateTime:
        :return:
        """
    @overload
    def GetAmbiguousTimeOffsets(self, dateTimeOffset: DateTimeOffset) -> Array[TimeSpan]:
        """:param dateTimeOffset:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @classmethod
    def GetSystemTimeZones(cls) -> ReadOnlyCollection[TimeZoneInfo]:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetUtcOffset(self, dateTime: DateTime) -> TimeSpan:
        """:param dateTime:
        :return:
        """
    @overload
    def GetUtcOffset(self, dateTimeOffset: DateTimeOffset) -> TimeSpan:
        """:param dateTimeOffset:
        :return:
        """
    def HasSameRules(self, other: TimeZoneInfo) -> bool:
        """:param other:
        :return:
        """
    @overload
    def IsAmbiguousTime(self, dateTime: DateTime) -> bool:
        """:param dateTime:
        :return:
        """
    @overload
    def IsAmbiguousTime(self, dateTimeOffset: DateTimeOffset) -> bool:
        """:param dateTimeOffset:
        :return:
        """
    @overload
    def IsDaylightSavingTime(self, dateTime: DateTime) -> bool:
        """:param dateTime:
        :return:
        """
    @overload
    def IsDaylightSavingTime(self, dateTimeOffset: DateTimeOffset) -> bool:
        """:param dateTimeOffset:
        :return:
        """
    def IsInvalidTime(self, dateTime: DateTime) -> bool:
        """:param dateTime:
        :return:
        """
    def OnDeserialization(self, sender: object) -> None:
        """:param sender:"""
    def ToSerializedString(self) -> str:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

    class AdjustmentRule(
        Object,
        IDeserializationCallback,
        ISerializable,
        IEquatable[TimeZoneInfo.AdjustmentRule],
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
            """:param obj:
            :return:
            """
        @overload
        def Equals(self, other: TimeZoneInfo.AdjustmentRule) -> bool:
            """:param other:
            :return:
            """
        def GetHashCode(self) -> int:
            """:return:"""
        def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
            """:param info:
            :param context:
            """
        def GetType(self) -> Type:
            """:return:"""
        def OnDeserialization(self, sender: object) -> None:
            """:param sender:"""
        def ToString(self) -> str:
            """:return:"""

    class TransitionTime(
        ValueType,
        IDeserializationCallback,
        ISerializable,
        IEquatable[TimeZoneInfo.TransitionTime],
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
            """:param obj:
            :return:
            """
        @overload
        def Equals(self, other: TimeZoneInfo.TransitionTime) -> bool:
            """:param other:
            :return:
            """
        def GetHashCode(self) -> int:
            """:return:"""
        def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
            """:param info:
            :param context:
            """
        def GetType(self) -> Type:
            """:return:"""
        def OnDeserialization(self, sender: object) -> None:
            """:param sender:"""
        def ToString(self) -> str:
            """:return:"""
        def __eq__(self, other: TimeZoneInfo.TransitionTime) -> bool:
            """"""
        def __ne__(self, other: TimeZoneInfo.TransitionTime) -> bool:
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

class TimeZoneInfoOptions(Enum):
    """"""

    _None: TimeZoneInfoOptions = ...
    """"""
    NoThrowOnInvalidTime: TimeZoneInfoOptions = ...
    """"""

class TimeZoneNotFoundException(Exception, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class TimeoutException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

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
    def Create(cls, item1: T1) -> Tuple[T1]:
        """:param item1:
        :return:
        """
    @classmethod
    @overload
    def Create(cls, item1: T1, item2: T2) -> Tuple[T1, T2]:
        """:param item1:
        :param item2:
        :return:
        """
    @classmethod
    @overload
    def Create(cls, item1: T1, item2: T2, item3: T3) -> Tuple[T1, T2, T3]:
        """:param item1:
        :param item2:
        :param item3:
        :return:
        """
    @classmethod
    @overload
    def Create(cls, item1: T1, item2: T2, item3: T3, item4: T4) -> Tuple[T1, T2, T3, T4]:
        """:param item1:
        :param item2:
        :param item3:
        :param item4:
        :return:
        """
    @classmethod
    @overload
    def Create(
        cls, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5
    ) -> Tuple[T1, T2, T3, T4, T5]:
        """:param item1:
        :param item2:
        :param item3:
        :param item4:
        :param item5:
        :return:
        """
    @classmethod
    @overload
    def Create(
        cls, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6
    ) -> Tuple[T1, T2, T3, T4, T5, T6]:
        """:param item1:
        :param item2:
        :param item3:
        :param item4:
        :param item5:
        :param item6:
        :return:
        """
    @classmethod
    @overload
    def Create(
        cls, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7]:
        """:param item1:
        :param item2:
        :param item3:
        :param item4:
        :param item5:
        :param item6:
        :param item7:
        :return:
        """
    @classmethod
    @overload
    def Create(
        cls,
        item1: T1,
        item2: T2,
        item3: T3,
        item4: T4,
        item5: T5,
        item6: T6,
        item7: T7,
        item8: T8,
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8]]:
        """:param item1:
        :param item2:
        :param item3:
        :param item4:
        :param item5:
        :param item6:
        :param item7:
        :param item8:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class TupleExtensions(ABC, Object):
    """"""

    @classmethod
    @overload
    def Deconstruct(cls, value: Tuple[T1], item1: T1) -> Tuple[None, T1]:
        """:param value:
        :param item1:
        """
    @classmethod
    @overload
    def Deconstruct(cls, value: Tuple[T1, T2], item1: T1, item2: T2) -> Tuple[None, T1, T2]:
        """:param value:
        :param item1:
        :param item2:
        """
    @classmethod
    @overload
    def Deconstruct(
        cls, value: Tuple[T1, T2, T3], item1: T1, item2: T2, item3: T3
    ) -> Tuple[None, T1, T2, T3]:
        """:param value:
        :param item1:
        :param item2:
        :param item3:
        """
    @classmethod
    @overload
    def Deconstruct(
        cls, value: Tuple[T1, T2, T3, T4], item1: T1, item2: T2, item3: T3, item4: T4
    ) -> Tuple[None, T1, T2, T3, T4]:
        """:param value:
        :param item1:
        :param item2:
        :param item3:
        :param item4:
        """
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[T1, T2, T3, T4, T5],
        item1: T1,
        item2: T2,
        item3: T3,
        item4: T4,
        item5: T5,
    ) -> Tuple[None, T1, T2, T3, T4, T5]:
        """:param value:
        :param item1:
        :param item2:
        :param item3:
        :param item4:
        :param item5:
        """
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
    ) -> Tuple[None, T1, T2, T3, T4, T5, T6]:
        """:param value:
        :param item1:
        :param item2:
        :param item3:
        :param item4:
        :param item5:
        :param item6:
        """
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
    ) -> Tuple[None, T1, T2, T3, T4, T5, T6, T7]:
        """:param value:
        :param item1:
        :param item2:
        :param item3:
        :param item4:
        :param item5:
        :param item6:
        :param item7:
        """
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
    ) -> Tuple[None, T1, T2, T3, T4, T5, T6, T7, T8]:
        """:param value:
        :param item1:
        :param item2:
        :param item3:
        :param item4:
        :param item5:
        :param item6:
        :param item7:
        :param item8:
        """
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9],
        item1: T1,
        item2: T2,
        item3: T3,
        item4: T4,
        item5: T5,
        item6: T6,
        item7: T7,
        item8: T8,
        item9: T9,
    ) -> Tuple[None, T1, T2, T3, T4, T5, T6, T7, T8, T9]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10],
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
    ) -> Tuple[None, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11],
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
    ) -> Tuple[None, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12],
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
    ) -> Tuple[None, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13],
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
    ) -> Tuple[None, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14],
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
    ) -> Tuple[None, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14]:
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
    ) -> Tuple[None, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple, T16],
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
    ) -> Tuple[None, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[
            T1,
            T2,
            T3,
            T4,
            T5,
            T6,
            T7,
            Tuple,
            T9,
            T10,
            T11,
            T12,
            T13,
            T14,
            Tuple,
            T16,
            T17,
        ],
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
    ) -> Tuple[None, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[
            T1,
            T2,
            T3,
            T4,
            T5,
            T6,
            T7,
            Tuple,
            T9,
            T10,
            T11,
            T12,
            T13,
            T14,
            Tuple,
            T16,
            T17,
            T18,
        ],
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
    ) -> Tuple[
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
    ]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[
            T1,
            T2,
            T3,
            T4,
            T5,
            T6,
            T7,
            Tuple,
            T9,
            T10,
            T11,
            T12,
            T13,
            T14,
            Tuple,
            T16,
            T17,
            T18,
            T19,
        ],
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
    ) -> Tuple[
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
    ]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[
            T1,
            T2,
            T3,
            T4,
            T5,
            T6,
            T7,
            Tuple,
            T9,
            T10,
            T11,
            T12,
            T13,
            T14,
            Tuple,
            T16,
            T17,
            T18,
            T19,
            T20,
        ],
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
    ) -> Tuple[
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
        value: Tuple[
            T1,
            T2,
            T3,
            T4,
            T5,
            T6,
            T7,
            Tuple,
            T9,
            T10,
            T11,
            T12,
            T13,
            T14,
            Tuple,
            T16,
            T17,
            T18,
            T19,
            T20,
            T21,
        ],
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
    ) -> Tuple[
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
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    @classmethod
    @overload
    def ToTuple(
        cls,
        value: ValueTuple[
            T1,
            T2,
            T3,
            T4,
            T5,
            T6,
            T7,
            ValueTuple,
            T9,
            T10,
            T11,
            T12,
            T13,
            T14,
            ValueTuple,
            T16,
            T17,
            T18,
            T19,
            T20,
            T21,
        ],
    ) -> Tuple[
        T1,
        T2,
        T3,
        T4,
        T5,
        T6,
        T7,
        Tuple,
        T9,
        T10,
        T11,
        T12,
        T13,
        T14,
        Tuple,
        T16,
        T17,
        T18,
        T19,
        T20,
        T21,
    ]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToTuple(
        cls,
        value: ValueTuple[
            T1,
            T2,
            T3,
            T4,
            T5,
            T6,
            T7,
            ValueTuple,
            T9,
            T10,
            T11,
            T12,
            T13,
            T14,
            ValueTuple,
            T16,
            T17,
            T18,
            T19,
            T20,
        ],
    ) -> Tuple[
        T1,
        T2,
        T3,
        T4,
        T5,
        T6,
        T7,
        Tuple,
        T9,
        T10,
        T11,
        T12,
        T13,
        T14,
        Tuple,
        T16,
        T17,
        T18,
        T19,
        T20,
    ]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToTuple(
        cls,
        value: ValueTuple[
            T1,
            T2,
            T3,
            T4,
            T5,
            T6,
            T7,
            ValueTuple,
            T9,
            T10,
            T11,
            T12,
            T13,
            T14,
            ValueTuple,
            T16,
            T17,
            T18,
            T19,
        ],
    ) -> Tuple[
        T1,
        T2,
        T3,
        T4,
        T5,
        T6,
        T7,
        Tuple,
        T9,
        T10,
        T11,
        T12,
        T13,
        T14,
        Tuple,
        T16,
        T17,
        T18,
        T19,
    ]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToTuple(
        cls,
        value: ValueTuple[
            T1,
            T2,
            T3,
            T4,
            T5,
            T6,
            T7,
            ValueTuple,
            T9,
            T10,
            T11,
            T12,
            T13,
            T14,
            ValueTuple,
            T16,
            T17,
            T18,
        ],
    ) -> Tuple[
        T1,
        T2,
        T3,
        T4,
        T5,
        T6,
        T7,
        Tuple,
        T9,
        T10,
        T11,
        T12,
        T13,
        T14,
        Tuple,
        T16,
        T17,
        T18,
    ]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToTuple(
        cls,
        value: ValueTuple[
            T1,
            T2,
            T3,
            T4,
            T5,
            T6,
            T7,
            ValueTuple,
            T9,
            T10,
            T11,
            T12,
            T13,
            T14,
            ValueTuple,
            T16,
            T17,
        ],
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple, T16, T17]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToTuple(
        cls,
        value: ValueTuple[
            T1,
            T2,
            T3,
            T4,
            T5,
            T6,
            T7,
            ValueTuple,
            T9,
            T10,
            T11,
            T12,
            T13,
            T14,
            ValueTuple,
            T16,
        ],
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple, T16]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToTuple(
        cls,
        value: ValueTuple[
            T1,
            T2,
            T3,
            T4,
            T5,
            T6,
            T7,
            ValueTuple,
            T9,
            T10,
            T11,
            T12,
            T13,
            T14,
            ValueTuple[T15],
        ],
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple[T15]]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToTuple(
        cls,
        value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9, T10, T11, T12, T13, T14],
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToTuple(
        cls,
        value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9, T10, T11, T12, T13],
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToTuple(
        cls,
        value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9, T10, T11, T12],
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToTuple(
        cls, value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9, T10, T11]
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToTuple(
        cls, value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9, T10]
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToTuple(
        cls, value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9]
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToTuple(
        cls, value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8]]
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8]]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToTuple(
        cls, value: ValueTuple[T1, T2, T3, T4, T5, T6, T7]
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToTuple(cls, value: ValueTuple[T1, T2, T3, T4, T5, T6]) -> Tuple[T1, T2, T3, T4, T5, T6]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToTuple(cls, value: ValueTuple[T1, T2, T3, T4, T5]) -> Tuple[T1, T2, T3, T4, T5]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToTuple(cls, value: ValueTuple[T1, T2, T3, T4]) -> Tuple[T1, T2, T3, T4]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToTuple(cls, value: ValueTuple[T1, T2, T3]) -> Tuple[T1, T2, T3]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToTuple(cls, value: ValueTuple[T1, T2]) -> Tuple[T1, T2]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToTuple(cls, value: ValueTuple[T1]) -> Tuple[T1]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToValueTuple(
        cls,
        value: Tuple[
            T1,
            T2,
            T3,
            T4,
            T5,
            T6,
            T7,
            Tuple,
            T9,
            T10,
            T11,
            T12,
            T13,
            T14,
            Tuple,
            T16,
            T17,
            T18,
            T19,
            T20,
            T21,
        ],
    ) -> ValueTuple[
        T1,
        T2,
        T3,
        T4,
        T5,
        T6,
        T7,
        ValueTuple,
        T9,
        T10,
        T11,
        T12,
        T13,
        T14,
        ValueTuple,
        T16,
        T17,
        T18,
        T19,
        T20,
        T21,
    ]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToValueTuple(
        cls,
        value: Tuple[
            T1,
            T2,
            T3,
            T4,
            T5,
            T6,
            T7,
            Tuple,
            T9,
            T10,
            T11,
            T12,
            T13,
            T14,
            Tuple,
            T16,
            T17,
            T18,
            T19,
            T20,
        ],
    ) -> ValueTuple[
        T1,
        T2,
        T3,
        T4,
        T5,
        T6,
        T7,
        ValueTuple,
        T9,
        T10,
        T11,
        T12,
        T13,
        T14,
        ValueTuple,
        T16,
        T17,
        T18,
        T19,
        T20,
    ]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToValueTuple(
        cls,
        value: Tuple[
            T1,
            T2,
            T3,
            T4,
            T5,
            T6,
            T7,
            Tuple,
            T9,
            T10,
            T11,
            T12,
            T13,
            T14,
            Tuple,
            T16,
            T17,
            T18,
            T19,
        ],
    ) -> ValueTuple[
        T1,
        T2,
        T3,
        T4,
        T5,
        T6,
        T7,
        ValueTuple,
        T9,
        T10,
        T11,
        T12,
        T13,
        T14,
        ValueTuple,
        T16,
        T17,
        T18,
        T19,
    ]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToValueTuple(
        cls,
        value: Tuple[
            T1,
            T2,
            T3,
            T4,
            T5,
            T6,
            T7,
            Tuple,
            T9,
            T10,
            T11,
            T12,
            T13,
            T14,
            Tuple,
            T16,
            T17,
            T18,
        ],
    ) -> ValueTuple[
        T1,
        T2,
        T3,
        T4,
        T5,
        T6,
        T7,
        ValueTuple,
        T9,
        T10,
        T11,
        T12,
        T13,
        T14,
        ValueTuple,
        T16,
        T17,
        T18,
    ]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToValueTuple(
        cls,
        value: Tuple[
            T1,
            T2,
            T3,
            T4,
            T5,
            T6,
            T7,
            Tuple,
            T9,
            T10,
            T11,
            T12,
            T13,
            T14,
            Tuple,
            T16,
            T17,
        ],
    ) -> ValueTuple[
        T1,
        T2,
        T3,
        T4,
        T5,
        T6,
        T7,
        ValueTuple,
        T9,
        T10,
        T11,
        T12,
        T13,
        T14,
        ValueTuple,
        T16,
        T17,
    ]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToValueTuple(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple, T16],
    ) -> ValueTuple[
        T1,
        T2,
        T3,
        T4,
        T5,
        T6,
        T7,
        ValueTuple,
        T9,
        T10,
        T11,
        T12,
        T13,
        T14,
        ValueTuple,
        T16,
    ]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToValueTuple(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple[T15]],
    ) -> ValueTuple[
        T1,
        T2,
        T3,
        T4,
        T5,
        T6,
        T7,
        ValueTuple,
        T9,
        T10,
        T11,
        T12,
        T13,
        T14,
        ValueTuple[T15],
    ]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToValueTuple(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14],
    ) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9, T10, T11, T12, T13, T14]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToValueTuple(
        cls, value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13]
    ) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9, T10, T11, T12, T13]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToValueTuple(
        cls, value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12]
    ) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9, T10, T11, T12]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToValueTuple(
        cls, value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11]
    ) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9, T10, T11]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToValueTuple(
        cls, value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10]
    ) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9, T10]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToValueTuple(
        cls, value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9]
    ) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToValueTuple(
        cls, value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8]]
    ) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8]]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToValueTuple(
        cls, value: Tuple[T1, T2, T3, T4, T5, T6, T7]
    ) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToValueTuple(
        cls, value: Tuple[T1, T2, T3, T4, T5, T6]
    ) -> ValueTuple[T1, T2, T3, T4, T5, T6]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToValueTuple(cls, value: Tuple[T1, T2, T3, T4, T5]) -> ValueTuple[T1, T2, T3, T4, T5]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToValueTuple(cls, value: Tuple[T1, T2, T3, T4]) -> ValueTuple[T1, T2, T3, T4]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToValueTuple(cls, value: Tuple[T1, T2, T3]) -> ValueTuple[T1, T2, T3]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToValueTuple(cls, value: Tuple[T1, T2]) -> ValueTuple[T1, T2]:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def ToValueTuple(cls, value: Tuple[T1]) -> ValueTuple[T1]:
        """:param value:
        :return:
        """

class Tuple(
    Generic[T1, T2, T3, T4, T5, T6, T7, TRest],
    Object,
    IStructuralComparable,
    IStructuralEquatable,
    ITuple,
    IComparable,
    ITupleInternal,
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
    ):
        """:param item1:"""
    @property
    def Item(self) -> object:
        """:return:"""
    @property
    def Item1(self) -> T1:
        """:return:"""
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
        """:return:"""
    @property
    def Rest(self) -> TRest:
        """"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, sb: StringBuilder) -> str:
        """:param sb:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """:param index:
        :return:
        """

class Tuple(
    Generic[T1, T2, T3, T4, T5, T6, T7],
    Object,
    IStructuralComparable,
    IStructuralEquatable,
    ITuple,
    IComparable,
    ITupleInternal,
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
    ):
        """:param item1:"""
    @property
    def Item(self) -> object:
        """:return:"""
    @property
    def Item1(self) -> T1:
        """:return:"""
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
        """:return:"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, sb: StringBuilder) -> str:
        """:param sb:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """:param index:
        :return:
        """

class Tuple(
    Generic[T1, T2, T3, T4, T5, T6],
    Object,
    IStructuralComparable,
    IStructuralEquatable,
    ITuple,
    IComparable,
    ITupleInternal,
):
    """"""

    def __init__(self, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6):
        """:param item1:"""
    @property
    def Item(self) -> object:
        """:return:"""
    @property
    def Item1(self) -> T1:
        """:return:"""
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
        """:return:"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, sb: StringBuilder) -> str:
        """:param sb:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """:param index:
        :return:
        """

class Tuple(
    Generic[T1, T2, T3, T4, T5],
    Object,
    IStructuralComparable,
    IStructuralEquatable,
    ITuple,
    IComparable,
    ITupleInternal,
):
    """"""

    def __init__(self, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5):
        """:param item1:"""
    @property
    def Item(self) -> object:
        """:return:"""
    @property
    def Item1(self) -> T1:
        """:return:"""
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
        """:return:"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, sb: StringBuilder) -> str:
        """:param sb:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """:param index:
        :return:
        """

class Tuple(
    Generic[T1, T2, T3, T4],
    Object,
    IStructuralComparable,
    IStructuralEquatable,
    ITuple,
    IComparable,
    ITupleInternal,
):
    """"""

    def __init__(self, item1: T1, item2: T2, item3: T3, item4: T4):
        """:param item1:"""
    @property
    def Item(self) -> object:
        """:return:"""
    @property
    def Item1(self) -> T1:
        """:return:"""
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
        """:return:"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, sb: StringBuilder) -> str:
        """:param sb:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """:param index:
        :return:
        """

class Tuple(
    Generic[T1, T2, T3],
    Object,
    IStructuralComparable,
    IStructuralEquatable,
    ITuple,
    IComparable,
    ITupleInternal,
):
    """"""

    def __init__(self, item1: T1, item2: T2, item3: T3):
        """:param item1:"""
    @property
    def Item(self) -> object:
        """:return:"""
    @property
    def Item1(self) -> T1:
        """:return:"""
    @property
    def Item2(self) -> T2:
        """"""
    @property
    def Item3(self) -> T3:
        """"""
    @property
    def Length(self) -> int:
        """:return:"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, sb: StringBuilder) -> str:
        """:param sb:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """:param index:
        :return:
        """

class Tuple(
    Generic[T1, T2],
    Object,
    IStructuralComparable,
    IStructuralEquatable,
    ITuple,
    IComparable,
    ITupleInternal,
):
    """"""

    def __init__(self, item1: T1, item2: T2):
        """:param item1:"""
    @property
    def Item(self) -> object:
        """:return:"""
    @property
    def Item1(self) -> T1:
        """:return:"""
    @property
    def Item2(self) -> T2:
        """"""
    @property
    def Length(self) -> int:
        """:return:"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, sb: StringBuilder) -> str:
        """:param sb:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """:param index:
        :return:
        """

class Tuple(
    Generic[T1],
    Object,
    IStructuralComparable,
    IStructuralEquatable,
    ITuple,
    IComparable,
    ITupleInternal,
):
    """"""

    def __init__(self, item1: T1):
        """:param item1:"""
    @property
    def Item(self) -> object:
        """:return:"""
    @property
    def Item1(self) -> T1:
        """:return:"""
    @property
    def Length(self) -> int:
        """:return:"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, sb: StringBuilder) -> str:
        """:param sb:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """:param index:
        :return:
        """

class Type(ABC, MemberInfo, ICustomAttributeProvider, IReflect, _MemberInfo, _Type):
    """"""

    Delimiter: Final[ClassVar[Char]] = ...
    """
    
    :return: 
    """
    EmptyTypes: Final[ClassVar[Array[Type]]] = ...
    """
    
    :return: 
    """
    FilterAttribute: Final[ClassVar[MemberFilter]] = ...
    """
    
    :return: 
    """
    FilterName: Final[ClassVar[MemberFilter]] = ...
    """
    
    :return: 
    """
    FilterNameIgnoreCase: Final[ClassVar[MemberFilter]] = ...
    """
    
    :return: 
    """
    Missing: Final[ClassVar[object]] = ...
    """
    
    :return: 
    """
    @property
    def Assembly(self) -> Assembly:
        """:return:"""
    @property
    def AssemblyQualifiedName(self) -> str:
        """:return:"""
    @property
    def Attributes(self) -> TypeAttributes:
        """:return:"""
    @property
    def BaseType(self) -> Type:
        """:return:"""
    @property
    def ContainsGenericParameters(self) -> bool:
        """:return:"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """:return:"""
    @property
    def DeclaringMethod(self) -> MethodBase:
        """:return:"""
    @property
    def DeclaringType(self) -> Type:
        """:return:"""
    @property
    def DeclaringType(self) -> Type:
        """:return:"""
    @classmethod
    @property
    def DefaultBinder(cls) -> Binder:
        """:return:"""
    @property
    def FullName(self) -> str:
        """:return:"""
    @property
    def GUID(self) -> Guid:
        """:return:"""
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes:
        """:return:"""
    @property
    def GenericParameterPosition(self) -> int:
        """:return:"""
    @property
    def GenericTypeArguments(self) -> Array[Type]:
        """:return:"""
    @property
    def HasElementType(self) -> bool:
        """:return:"""
    @property
    def IsAbstract(self) -> bool:
        """:return:"""
    @property
    def IsAnsiClass(self) -> bool:
        """:return:"""
    @property
    def IsArray(self) -> bool:
        """:return:"""
    @property
    def IsAutoClass(self) -> bool:
        """:return:"""
    @property
    def IsAutoLayout(self) -> bool:
        """:return:"""
    @property
    def IsByRef(self) -> bool:
        """:return:"""
    @property
    def IsCOMObject(self) -> bool:
        """:return:"""
    @property
    def IsClass(self) -> bool:
        """:return:"""
    @property
    def IsConstructedGenericType(self) -> bool:
        """:return:"""
    @property
    def IsContextful(self) -> bool:
        """:return:"""
    @property
    def IsEnum(self) -> bool:
        """:return:"""
    @property
    def IsExplicitLayout(self) -> bool:
        """:return:"""
    @property
    def IsGenericParameter(self) -> bool:
        """:return:"""
    @property
    def IsGenericType(self) -> bool:
        """:return:"""
    @property
    def IsGenericTypeDefinition(self) -> bool:
        """:return:"""
    @property
    def IsImport(self) -> bool:
        """:return:"""
    @property
    def IsInterface(self) -> bool:
        """:return:"""
    @property
    def IsLayoutSequential(self) -> bool:
        """:return:"""
    @property
    def IsMarshalByRef(self) -> bool:
        """:return:"""
    @property
    def IsNested(self) -> bool:
        """:return:"""
    @property
    def IsNestedAssembly(self) -> bool:
        """:return:"""
    @property
    def IsNestedFamANDAssem(self) -> bool:
        """:return:"""
    @property
    def IsNestedFamORAssem(self) -> bool:
        """:return:"""
    @property
    def IsNestedFamily(self) -> bool:
        """:return:"""
    @property
    def IsNestedPrivate(self) -> bool:
        """:return:"""
    @property
    def IsNestedPublic(self) -> bool:
        """:return:"""
    @property
    def IsNotPublic(self) -> bool:
        """:return:"""
    @property
    def IsPointer(self) -> bool:
        """:return:"""
    @property
    def IsPrimitive(self) -> bool:
        """:return:"""
    @property
    def IsPublic(self) -> bool:
        """:return:"""
    @property
    def IsSealed(self) -> bool:
        """:return:"""
    @property
    def IsSecurityCritical(self) -> bool:
        """:return:"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """:return:"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """:return:"""
    @property
    def IsSerializable(self) -> bool:
        """:return:"""
    @property
    def IsSpecialName(self) -> bool:
        """:return:"""
    @property
    def IsUnicodeClass(self) -> bool:
        """:return:"""
    @property
    def IsValueType(self) -> bool:
        """:return:"""
    @property
    def IsVisible(self) -> bool:
        """:return:"""
    @property
    def MemberType(self) -> MemberTypes:
        """:return:"""
    @property
    def MemberType(self) -> MemberTypes:
        """:return:"""
    @property
    def MetadataToken(self) -> int:
        """:return:"""
    @property
    def Module(self) -> Module:
        """:return:"""
    @property
    def Module(self) -> Module:
        """:return:"""
    @property
    def Name(self) -> str:
        """:return:"""
    @property
    def Name(self) -> str:
        """:return:"""
    @property
    def Namespace(self) -> str:
        """:return:"""
    @property
    def ReflectedType(self) -> Type:
        """:return:"""
    @property
    def ReflectedType(self) -> Type:
        """:return:"""
    @property
    def StructLayoutAttribute(self) -> StructLayoutAttribute:
        """:return:"""
    @property
    def TypeHandle(self) -> RuntimeTypeHandle:
        """:return:"""
    @property
    def TypeInitializer(self) -> ConstructorInfo:
        """:return:"""
    @property
    def UnderlyingSystemType(self) -> Type:
        """:return:"""
    @property
    def UnderlyingSystemType(self) -> Type:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, o: Type) -> bool:
        """:param o:
        :return:
        """
    def FindInterfaces(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """:param filter:
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
        """:param memberType:
        :param bindingAttr:
        :param filter:
        :param filterCriteria:
        :return:
        """
    def GetArrayRank(self) -> int:
        """:return:"""
    @overload
    def GetConstructor(self, types: Array[Type]) -> ConstructorInfo:
        """:param types:
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
        """:param bindingAttr:
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
        """:param bindingAttr:
        :param binder:
        :param callConvention:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetConstructors(self) -> Array[ConstructorInfo]:
        """:return:"""
    @overload
    def GetConstructors(self, bindingAttr: BindingFlags) -> Array[ConstructorInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """:param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """:param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """:param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """:param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """:param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """:param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """:return:"""
    def GetDefaultMembers(self) -> Array[MemberInfo]:
        """:return:"""
    def GetElementType(self) -> Type:
        """:return:"""
    def GetEnumName(self, value: object) -> str:
        """:param value:
        :return:
        """
    def GetEnumNames(self) -> Array[str]:
        """:return:"""
    def GetEnumUnderlyingType(self) -> Type:
        """:return:"""
    def GetEnumValues(self) -> Array:
        """:return:"""
    @overload
    def GetEvent(self, name: str) -> EventInfo:
        """:param name:
        :return:
        """
    @overload
    def GetEvent(self, name: str, bindingAttr: BindingFlags) -> EventInfo:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetEvents(self) -> Array[EventInfo]:
        """:return:"""
    @overload
    def GetEvents(self, bindingAttr: BindingFlags) -> Array[EventInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """:param name:
        :return:
        """
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """:return:"""
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """:param bindingAttr:
        :return:
        """
    def GetGenericArguments(self) -> Array[Type]:
        """:return:"""
    def GetGenericParameterConstraints(self) -> Array[Type]:
        """:return:"""
    def GetGenericTypeDefinition(self) -> Type:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetInterface(self, name: str) -> Type:
        """:param name:
        :return:
        """
    @overload
    def GetInterface(self, name: str, ignoreCase: bool) -> Type:
        """:param name:
        :param ignoreCase:
        :return:
        """
    def GetInterfaceMap(self, interfaceType: Type) -> InterfaceMapping:
        """:param interfaceType:
        :return:
        """
    def GetInterfaces(self) -> Array[Type]:
        """:return:"""
    @overload
    def GetMember(self, name: str) -> Array[MemberInfo]:
        """:param name:
        :return:
        """
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMember(
        self, name: str, type: MemberTypes, bindingAttr: BindingFlags
    ) -> Array[MemberInfo]:
        """:param name:
        :param type:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMembers(self) -> Array[MemberInfo]:
        """:return:"""
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """:param name:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """:param name:
        :param types:
        :return:
        """
    @overload
    def GetMethod(
        self, name: str, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> MethodInfo:
        """:param name:
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
        """:param name:
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
        """:param name:
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
        """:param name:
        :param bindingAttr:
        :param binder:
        :param callConvention:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """:return:"""
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetNestedType(self, name: str) -> Type:
        """:param name:
        :return:
        """
    @overload
    def GetNestedType(self, name: str, bindingAttr: BindingFlags) -> Type:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetNestedTypes(self) -> Array[Type]:
        """:return:"""
    @overload
    def GetNestedTypes(self, bindingAttr: BindingFlags) -> Array[Type]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetProperties(self) -> Array[PropertyInfo]:
        """:return:"""
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str) -> PropertyInfo:
        """:param name:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """:param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, types: Array[Type]) -> PropertyInfo:
        """:param name:
        :param types:
        :return:
        """
    @overload
    def GetProperty(self, name: str, returnType: Type) -> PropertyInfo:
        """:param name:
        :param returnType:
        :return:
        """
    @overload
    def GetProperty(self, name: str, returnType: Type, types: Array[Type]) -> PropertyInfo:
        """:param name:
        :param returnType:
        :param types:
        :return:
        """
    @overload
    def GetProperty(
        self,
        name: str,
        returnType: Type,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> PropertyInfo:
        """:param name:
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
        """:param name:
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
        """:param name:
        :param bindingAttr:
        :param binder:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    @overload
    def GetType(cls, typeName: str) -> Type:
        """:param typeName:
        :return:
        """
    @classmethod
    @overload
    def GetType(cls, typeName: str, throwOnError: bool) -> Type:
        """:param typeName:
        :param throwOnError:
        :return:
        """
    @classmethod
    @overload
    def GetType(cls, typeName: str, throwOnError: bool, ignoreCase: bool) -> Type:
        """:param typeName:
        :param throwOnError:
        :param ignoreCase:
        :return:
        """
    @classmethod
    @overload
    def GetType(
        cls,
        typeName: str,
        assemblyResolver: Func[AssemblyName, Assembly],
        typeResolver: Func[Assembly, str, bool, Type],
    ) -> Type:
        """:param typeName:
        :param assemblyResolver:
        :param typeResolver:
        :return:
        """
    @classmethod
    @overload
    def GetType(
        cls,
        typeName: str,
        assemblyResolver: Func[AssemblyName, Assembly],
        typeResolver: Func[Assembly, str, bool, Type],
        throwOnError: bool,
    ) -> Type:
        """:param typeName:
        :param assemblyResolver:
        :param typeResolver:
        :param throwOnError:
        :return:
        """
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
        """:param typeName:
        :param assemblyResolver:
        :param typeResolver:
        :param throwOnError:
        :param ignoreCase:
        :return:
        """
    @classmethod
    def GetTypeArray(cls, args: Array[object]) -> Array[Type]:
        """:param args:
        :return:
        """
    @classmethod
    def GetTypeCode(cls, type: Type) -> TypeCode:
        """:param type:
        :return:
        """
    @classmethod
    @overload
    def GetTypeFromCLSID(cls, clsid: Guid) -> Type:
        """:param clsid:
        :return:
        """
    @classmethod
    @overload
    def GetTypeFromCLSID(cls, clsid: Guid, throwOnError: bool) -> Type:
        """:param clsid:
        :param throwOnError:
        :return:
        """
    @classmethod
    @overload
    def GetTypeFromCLSID(cls, clsid: Guid, server: str) -> Type:
        """:param clsid:
        :param server:
        :return:
        """
    @classmethod
    @overload
    def GetTypeFromCLSID(cls, clsid: Guid, server: str, throwOnError: bool) -> Type:
        """:param clsid:
        :param server:
        :param throwOnError:
        :return:
        """
    @classmethod
    def GetTypeFromHandle(cls, handle: RuntimeTypeHandle) -> Type:
        """:param handle:
        :return:
        """
    @classmethod
    @overload
    def GetTypeFromProgID(cls, progID: str) -> Type:
        """:param progID:
        :return:
        """
    @classmethod
    @overload
    def GetTypeFromProgID(cls, progID: str, throwOnError: bool) -> Type:
        """:param progID:
        :param throwOnError:
        :return:
        """
    @classmethod
    @overload
    def GetTypeFromProgID(cls, progID: str, server: str) -> Type:
        """:param progID:
        :param server:
        :return:
        """
    @classmethod
    @overload
    def GetTypeFromProgID(cls, progID: str, server: str, throwOnError: bool) -> Type:
        """:param progID:
        :param server:
        :param throwOnError:
        :return:
        """
    @classmethod
    def GetTypeHandle(cls, o: object) -> RuntimeTypeHandle:
        """:param o:
        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
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
        """:param dispIdMember:
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
        """:param dispIdMember:
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
        """:param name:
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
        """:param name:
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
        """:param name:
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
        """:param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param modifiers:
        :param culture:
        :param namedParameters:
        :return:
        """
    def IsAssignableFrom(self, c: Type) -> bool:
        """:param c:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """:param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """:param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """:param attributeType:
        :param inherit:
        :return:
        """
    def IsEnumDefined(self, value: object) -> bool:
        """:param value:
        :return:
        """
    def IsEquivalentTo(self, other: Type) -> bool:
        """:param other:
        :return:
        """
    def IsInstanceOfType(self, o: object) -> bool:
        """:param o:
        :return:
        """
    def IsSubclassOf(self, c: Type) -> bool:
        """:param c:
        :return:
        """
    @overload
    def MakeArrayType(self) -> Type:
        """:return:"""
    @overload
    def MakeArrayType(self, rank: int) -> Type:
        """:param rank:
        :return:
        """
    def MakeByRefType(self) -> Type:
        """:return:"""
    def MakeGenericType(self, typeArguments: Array[Type]) -> Type:
        """:param typeArguments:
        :return:
        """
    def MakePointerType(self) -> Type:
        """:return:"""
    @classmethod
    def ReflectionOnlyGetType(cls, typeName: str, throwIfNotFound: bool, ignoreCase: bool) -> Type:
        """:param typeName:
        :param throwIfNotFound:
        :param ignoreCase:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    def __eq__(self, other: Type) -> bool:
        """:param other:
        :return:
        """
    def __ne__(self, other: Type) -> bool:
        """:param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: Type, right: Type) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: Type, right: Type) -> bool:
        """:param left:
        :param right:
        :return:
        """

class TypeAccessException(TypeLoadException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, inner: Exception):
        """:param message:
        :param inner:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @property
    def TypeName(self) -> str:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

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

    def __init__(self, fullTypeName: str, innerException: Exception):
        """:param fullTypeName:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @property
    def TypeName(self) -> str:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class TypeLoadException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, inner: Exception):
        """:param message:
        :param inner:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @property
    def TypeName(self) -> str:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

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
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class TypeUnloadedException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class TypedReference(ValueType):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    @classmethod
    def GetTargetType(cls, value: TypedReference) -> Type:
        """:param value:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def MakeTypedReference(cls, target: object, flds: Array[FieldInfo]) -> TypedReference:
        """:param target:
        :param flds:
        :return:
        """
    @classmethod
    def SetTypedReference(cls, target: TypedReference, value: object) -> None:
        """:param target:
        :param value:
        """
    @classmethod
    def TargetTypeToken(cls, value: TypedReference) -> RuntimeTypeHandle:
        """:param value:
        :return:
        """
    @classmethod
    def ToObject(cls, value: TypedReference) -> object:
        """:param value:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class UInt16(
    ValueType,
    IComparable,
    IComparable[UInt16],
    IConvertible,
    IEquatable[UInt16],
    IFormattable,
):
    """"""

    MaxValue: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MinValue: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: int) -> int:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: int) -> bool:
        """:param other:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeCode(self) -> TypeCode:
        """:return:"""
    @classmethod
    @overload
    def Parse(cls, s: str) -> int:
        """:param s:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles) -> int:
        """:param s:
        :param style:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider) -> int:
        """:param s:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles, provider: IFormatProvider) -> int:
        """:param s:
        :param style:
        :param provider:
        :return:
        """
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """:param provider:
        :return:
        """
    def ToByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToChar(self, provider: IFormatProvider) -> Char:
        """:param provider:
        :return:
        """
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """:param provider:
        :return:
        """
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """:param provider:
        :return:
        """
    def ToDouble(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    def ToInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSingle(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self, format: str) -> str:
        """:param format:
        :return:
        """
    @overload
    def ToString(self, format: str, formatProvider: IFormatProvider) -> str:
        """:param format:
        :param formatProvider:
        :return:
        """
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """:param conversionType:
        :param provider:
        :return:
        """
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    @classmethod
    @overload
    def TryParse(cls, s: str, result: int) -> Tuple[bool, int]:
        """:param s:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryParse(
        cls, s: str, style: NumberStyles, provider: IFormatProvider, result: int
    ) -> Tuple[bool, int]:
        """:param s:
        :param style:
        :param provider:
        :param result:
        :return:
        """

class UInt32(
    ValueType,
    IComparable,
    IComparable[UInt32],
    IConvertible,
    IEquatable[UInt32],
    IFormattable,
):
    """"""

    MaxValue: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MinValue: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: int) -> int:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: int) -> bool:
        """:param other:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeCode(self) -> TypeCode:
        """:return:"""
    @classmethod
    @overload
    def Parse(cls, s: str) -> int:
        """:param s:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles) -> int:
        """:param s:
        :param style:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider) -> int:
        """:param s:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles, provider: IFormatProvider) -> int:
        """:param s:
        :param style:
        :param provider:
        :return:
        """
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """:param provider:
        :return:
        """
    def ToByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToChar(self, provider: IFormatProvider) -> Char:
        """:param provider:
        :return:
        """
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """:param provider:
        :return:
        """
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """:param provider:
        :return:
        """
    def ToDouble(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    def ToInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSingle(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self, format: str) -> str:
        """:param format:
        :return:
        """
    @overload
    def ToString(self, format: str, formatProvider: IFormatProvider) -> str:
        """:param format:
        :param formatProvider:
        :return:
        """
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """:param conversionType:
        :param provider:
        :return:
        """
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    @classmethod
    @overload
    def TryParse(cls, s: str, result: int) -> Tuple[bool, int]:
        """:param s:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryParse(
        cls, s: str, style: NumberStyles, provider: IFormatProvider, result: int
    ) -> Tuple[bool, int]:
        """:param s:
        :param style:
        :param provider:
        :param result:
        :return:
        """

class UInt64(
    ValueType,
    IComparable,
    IComparable[UInt64],
    IConvertible,
    IEquatable[UInt64],
    IFormattable,
):
    """"""

    MaxValue: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MinValue: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: int) -> int:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: int) -> bool:
        """:param other:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeCode(self) -> TypeCode:
        """:return:"""
    @classmethod
    @overload
    def Parse(cls, s: str) -> int:
        """:param s:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles) -> int:
        """:param s:
        :param style:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider) -> int:
        """:param s:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles, provider: IFormatProvider) -> int:
        """:param s:
        :param style:
        :param provider:
        :return:
        """
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """:param provider:
        :return:
        """
    def ToByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToChar(self, provider: IFormatProvider) -> Char:
        """:param provider:
        :return:
        """
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """:param provider:
        :return:
        """
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """:param provider:
        :return:
        """
    def ToDouble(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    def ToInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSByte(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToSingle(self, provider: IFormatProvider) -> float:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """:param provider:
        :return:
        """
    @overload
    def ToString(self, format: str) -> str:
        """:param format:
        :return:
        """
    @overload
    def ToString(self, format: str, formatProvider: IFormatProvider) -> str:
        """:param format:
        :param formatProvider:
        :return:
        """
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """:param conversionType:
        :param provider:
        :return:
        """
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """:param provider:
        :return:
        """
    @classmethod
    @overload
    def TryParse(cls, s: str, result: int) -> Tuple[bool, int]:
        """:param s:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryParse(
        cls, s: str, style: NumberStyles, provider: IFormatProvider, result: int
    ) -> Tuple[bool, int]:
        """:param s:
        :param style:
        :param provider:
        :param result:
        :return:
        """

class UIntPtr(ValueType, ISerializable):
    """"""

    Zero: Final[ClassVar[UIntPtr]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, value: int):
        """:param value:"""
    @overload
    def __init__(self, value: int):
        """:param value:"""
    @overload
    def __init__(self, value: None):
        """:param value:"""
    @classmethod
    @property
    def Size(cls) -> int:
        """:return:"""
    @classmethod
    def Add(cls, pointer: UIntPtr, offset: int) -> UIntPtr:
        """:param pointer:
        :param offset:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def Subtract(cls, pointer: UIntPtr, offset: int) -> UIntPtr:
        """:param pointer:
        :param offset:
        :return:
        """
    def ToPointer(self) -> None:
        """"""
    def ToString(self) -> str:
        """:return:"""
    def ToUInt32(self) -> int:
        """:return:"""
    def ToUInt64(self) -> int:
        """:return:"""
    def __add__(self, other: int) -> UIntPtr:
        """:param other:
        :return:
        """
    def __eq__(self, other: UIntPtr) -> bool:
        """:param other:
        :return:
        """
    def __ne__(self, other: UIntPtr) -> bool:
        """:param other:
        :return:
        """
    def __sub__(self, other: int) -> UIntPtr:
        """:param other:
        :return:
        """
    @classmethod
    def op_Addition(cls, pointer: UIntPtr, offset: int) -> UIntPtr:
        """:param pointer:
        :param offset:
        :return:
        """
    @classmethod
    def op_Equality(cls, value1: UIntPtr, value2: UIntPtr) -> bool:
        """:param value1:
        :param value2:
        :return:
        """
    @classmethod
    @overload
    def op_Explicit(cls, value: int) -> UIntPtr:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def op_Explicit(cls, value: int) -> UIntPtr:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def op_Explicit(cls, value: UIntPtr) -> None:
        """:param value:"""
    @classmethod
    @overload
    def op_Explicit(cls, value: None) -> UIntPtr:
        """:param value:
        :return:
        """
    @classmethod
    def op_Inequality(cls, value1: UIntPtr, value2: UIntPtr) -> bool:
        """:param value1:
        :param value2:
        :return:
        """
    @classmethod
    def op_Subtraction(cls, pointer: UIntPtr, offset: int) -> UIntPtr:
        """:param pointer:
        :param offset:
        :return:
        """

class UnSafeCharBuffer(ValueType):
    """"""

    def __init__(self, buffer: Char, bufferSize: int):
        """:param buffer:
        :param bufferSize:
        """
    @property
    def Length(self) -> int:
        """:return:"""
    def AppendString(self, stringToAppend: str) -> None:
        """:param stringToAppend:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class UnauthorizedAccessException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, inner: Exception):
        """:param message:
        :param inner:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class UncNameHelper(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

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

    def __init__(self, exception: object, isTerminating: bool):
        """:param exception:
        :param isTerminating:
        """
    @property
    def ExceptionObject(self) -> object:
        """:return:"""
    @property
    def IsTerminating(self) -> bool:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

UnhandledExceptionEventHandler: Callable[[object, UnhandledExceptionEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class UnitySerializationHolder(Object, IObjectReference, ISerializable):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    def GetRealObject(self, context: StreamingContext) -> object:
        """:param context:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class Uri(Object, ISerializable):
    """"""

    SchemeDelimiter: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    UriSchemeFile: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    UriSchemeFtp: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    UriSchemeGopher: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    UriSchemeHttp: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    UriSchemeHttps: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    UriSchemeMailto: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    UriSchemeNetPipe: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    UriSchemeNetTcp: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    UriSchemeNews: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    UriSchemeNntp: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, uriString: str):
        """:param uriString:"""
    @overload
    def __init__(self, uriString: str, dontEscape: bool):
        """:param uriString:
        :param dontEscape:
        """
    @overload
    def __init__(self, uriString: str, uriKind: UriKind):
        """:param uriString:
        :param uriKind:
        """
    @overload
    def __init__(self, baseUri: Uri, relativeUri: str):
        """:param baseUri:
        :param relativeUri:
        """
    @overload
    def __init__(self, baseUri: Uri, relativeUri: Uri):
        """:param baseUri:
        :param relativeUri:
        """
    @overload
    def __init__(self, baseUri: Uri, relativeUri: str, dontEscape: bool):
        """:param baseUri:
        :param relativeUri:
        :param dontEscape:
        """
    @property
    def AbsolutePath(self) -> str:
        """:return:"""
    @property
    def AbsoluteUri(self) -> str:
        """:return:"""
    @property
    def Authority(self) -> str:
        """:return:"""
    @property
    def DnsSafeHost(self) -> str:
        """:return:"""
    @property
    def Fragment(self) -> str:
        """:return:"""
    @property
    def Host(self) -> str:
        """:return:"""
    @property
    def HostNameType(self) -> UriHostNameType:
        """:return:"""
    @property
    def IdnHost(self) -> str:
        """:return:"""
    @property
    def IsAbsoluteUri(self) -> bool:
        """:return:"""
    @property
    def IsDefaultPort(self) -> bool:
        """:return:"""
    @property
    def IsFile(self) -> bool:
        """:return:"""
    @property
    def IsLoopback(self) -> bool:
        """:return:"""
    @property
    def IsUnc(self) -> bool:
        """:return:"""
    @property
    def LocalPath(self) -> str:
        """:return:"""
    @property
    def OriginalString(self) -> str:
        """:return:"""
    @property
    def PathAndQuery(self) -> str:
        """:return:"""
    @property
    def Port(self) -> int:
        """:return:"""
    @property
    def Query(self) -> str:
        """:return:"""
    @property
    def Scheme(self) -> str:
        """:return:"""
    @property
    def Segments(self) -> Array[str]:
        """:return:"""
    @property
    def UserEscaped(self) -> bool:
        """:return:"""
    @property
    def UserInfo(self) -> str:
        """:return:"""
    @classmethod
    def CheckHostName(cls, name: str) -> UriHostNameType:
        """:param name:
        :return:
        """
    @classmethod
    def CheckSchemeName(cls, schemeName: str) -> bool:
        """:param schemeName:
        :return:
        """
    @classmethod
    def Compare(
        cls,
        uri1: Uri,
        uri2: Uri,
        partsToCompare: UriComponents,
        compareFormat: UriFormat,
        comparisonType: StringComparison,
    ) -> int:
        """:param uri1:
        :param uri2:
        :param partsToCompare:
        :param compareFormat:
        :param comparisonType:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    def EscapeDataString(cls, stringToEscape: str) -> str:
        """:param stringToEscape:
        :return:
        """
    @classmethod
    def EscapeUriString(cls, stringToEscape: str) -> str:
        """:param stringToEscape:
        :return:
        """
    @classmethod
    def FromHex(cls, digit: Char) -> int:
        """:param digit:
        :return:
        """
    def GetComponents(self, components: UriComponents, format: UriFormat) -> str:
        """:param components:
        :param format:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetLeftPart(self, part: UriPartial) -> str:
        """:param part:
        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def HexEscape(cls, character: Char) -> str:
        """:param character:
        :return:
        """
    @classmethod
    def HexUnescape(cls, pattern: str, index: int) -> Char:
        """:param pattern:
        :param index:
        :return:
        """
    def IsBaseOf(self, uri: Uri) -> bool:
        """:param uri:
        :return:
        """
    @classmethod
    def IsHexDigit(cls, character: Char) -> bool:
        """:param character:
        :return:
        """
    @classmethod
    def IsHexEncoding(cls, pattern: str, index: int) -> bool:
        """:param pattern:
        :param index:
        :return:
        """
    def IsWellFormedOriginalString(self) -> bool:
        """:return:"""
    @classmethod
    def IsWellFormedUriString(cls, uriString: str, uriKind: UriKind) -> bool:
        """:param uriString:
        :param uriKind:
        :return:
        """
    def MakeRelative(self, toUri: Uri) -> str:
        """:param toUri:
        :return:
        """
    def MakeRelativeUri(self, uri: Uri) -> Uri:
        """:param uri:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""
    @classmethod
    @overload
    def TryCreate(cls, uriString: str, uriKind: UriKind, result: Uri) -> Tuple[bool, Uri]:
        """:param uriString:
        :param uriKind:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryCreate(cls, baseUri: Uri, relativeUri: str, result: Uri) -> Tuple[bool, Uri]:
        """:param baseUri:
        :param relativeUri:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryCreate(cls, baseUri: Uri, relativeUri: Uri, result: Uri) -> Tuple[bool, Uri]:
        """:param baseUri:
        :param relativeUri:
        :param result:
        :return:
        """
    @classmethod
    def UnescapeDataString(cls, stringToUnescape: str) -> str:
        """:param stringToUnescape:
        :return:
        """
    def __eq__(self, other: Uri) -> bool:
        """:param other:
        :return:
        """
    def __ne__(self, other: Uri) -> bool:
        """:param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, uri1: Uri, uri2: Uri) -> bool:
        """:param uri1:
        :param uri2:
        :return:
        """
    @classmethod
    def op_Inequality(cls, uri1: Uri, uri2: Uri) -> bool:
        """:param uri1:
        :param uri2:
        :return:
        """

class UriBuilder(Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, uri: str):
        """:param uri:"""
    @overload
    def __init__(self, uri: Uri):
        """:param uri:"""
    @overload
    def __init__(self, schemeName: str, hostName: str):
        """:param schemeName:
        :param hostName:
        """
    @overload
    def __init__(self, scheme: str, host: str, portNumber: int):
        """:param scheme:
        :param host:
        :param portNumber:
        """
    @overload
    def __init__(self, scheme: str, host: str, port: int, pathValue: str):
        """:param scheme:
        :param host:
        :param port:
        :param pathValue:
        """
    @overload
    def __init__(self, scheme: str, host: str, port: int, path: str, extraValue: str):
        """:param scheme:
        :param host:
        :param port:
        :param path:
        :param extraValue:
        """
    @property
    def Fragment(self) -> str:
        """:return:"""
    @Fragment.setter
    def Fragment(self, value: str) -> None: ...
    @property
    def Host(self) -> str:
        """:return:"""
    @Host.setter
    def Host(self, value: str) -> None: ...
    @property
    def Password(self) -> str:
        """:return:"""
    @Password.setter
    def Password(self, value: str) -> None: ...
    @property
    def Path(self) -> str:
        """:return:"""
    @Path.setter
    def Path(self, value: str) -> None: ...
    @property
    def Port(self) -> int:
        """:return:"""
    @Port.setter
    def Port(self, value: int) -> None: ...
    @property
    def Query(self) -> str:
        """:return:"""
    @Query.setter
    def Query(self, value: str) -> None: ...
    @property
    def Scheme(self) -> str:
        """:return:"""
    @Scheme.setter
    def Scheme(self, value: str) -> None: ...
    @property
    def Uri(self) -> Uri:
        """:return:"""
    @property
    def UserName(self) -> str:
        """:return:"""
    @UserName.setter
    def UserName(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

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
    def __init__(self):
        """"""
    @overload
    def __init__(self, textString: str):
        """:param textString:"""
    @overload
    def __init__(self, textString: str, e: Exception):
        """:param textString:
        :param e:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class UriHelper(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

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
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def IsKnownScheme(cls, schemeName: str) -> bool:
        """:param schemeName:
        :return:
        """
    @classmethod
    def Register(cls, uriParser: UriParser, schemeName: str, defaultPort: int) -> None:
        """:param uriParser:
        :param schemeName:
        :param defaultPort:
        """
    def ToString(self) -> str:
        """:return:"""

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

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """:param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """:param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """:param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """:param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """:param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """:param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """:param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """:param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """:param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """:param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """:param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """:param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """:param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """:param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """:param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """:param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """:param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """:param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """:param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """:param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """:return:"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """:param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """:param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """:param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self,
        context: ITypeDescriptorContext,
        value: object,
        attributes: Array[Attribute],
    ) -> PropertyDescriptorCollection:
        """:param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """:return:"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """:param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """:return:"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """:param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """:return:"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """:param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """:return:"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """:param context:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def IsValid(self, value: object) -> bool:
        """:param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """:param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class Utf8String(ValueType):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

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
        """:return:"""
    @property
    def Length(self) -> int:
        """:return:"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: ValueTuple) -> int:
        """:param other:
        :return:
        """
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """:param other:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def Create(cls) -> ValueTuple:
        """:return:"""
    @classmethod
    @overload
    def Create(cls, item1: T1) -> ValueTuple[T1]:
        """:param item1:
        :return:
        """
    @classmethod
    @overload
    def Create(cls, item1: T1, item2: T2) -> ValueTuple[T1, T2]:
        """:param item1:
        :param item2:
        :return:
        """
    @classmethod
    @overload
    def Create(cls, item1: T1, item2: T2, item3: T3) -> ValueTuple[T1, T2, T3]:
        """:param item1:
        :param item2:
        :param item3:
        :return:
        """
    @classmethod
    @overload
    def Create(cls, item1: T1, item2: T2, item3: T3, item4: T4) -> ValueTuple[T1, T2, T3, T4]:
        """:param item1:
        :param item2:
        :param item3:
        :param item4:
        :return:
        """
    @classmethod
    @overload
    def Create(
        cls, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5
    ) -> ValueTuple[T1, T2, T3, T4, T5]:
        """:param item1:
        :param item2:
        :param item3:
        :param item4:
        :param item5:
        :return:
        """
    @classmethod
    @overload
    def Create(
        cls, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6
    ) -> ValueTuple[T1, T2, T3, T4, T5, T6]:
        """:param item1:
        :param item2:
        :param item3:
        :param item4:
        :param item5:
        :param item6:
        :return:
        """
    @classmethod
    @overload
    def Create(
        cls, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7
    ) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7]:
        """:param item1:
        :param item2:
        :param item3:
        :param item4:
        :param item5:
        :param item6:
        :param item7:
        :return:
        """
    @classmethod
    @overload
    def Create(
        cls,
        item1: T1,
        item2: T2,
        item3: T3,
        item4: T4,
        item5: T5,
        item6: T6,
        item7: T7,
        item8: T8,
    ) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8]]:
        """:param item1:
        :param item2:
        :param item3:
        :param item4:
        :param item5:
        :param item6:
        :param item7:
        :param item8:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: ValueTuple) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def ToStringEnd(self) -> str:
        """:return:"""
    def __getitem__(self, index: int) -> object:
        """:param index:
        :return:
        """

class ValueTuple(
    Generic[T1, T2, T3, T4, T5, T6, T7, TRest],
    ValueType,
    IStructuralComparable,
    IStructuralEquatable,
    ITuple,
    IComparable,
    IComparable[ValueTuple, T2, T3, T4, T5, T6, T7, TRest],
    IEquatable[ValueTuple, T2, T3, T4, T5, T6, T7, TRest],
    IValueTupleInternal,
):
    """"""

    Item1: Final[T1] = ...
    """
    
    :return: 
    """
    Item2: Final[T2] = ...
    """"""
    Item3: Final[T3] = ...
    """"""
    Item4: Final[T4] = ...
    """"""
    Item5: Final[T5] = ...
    """"""
    Item6: Final[T6] = ...
    """"""
    Item7: Final[T7] = ...
    """"""
    Rest: Final[TRest] = ...
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
    ):
        """:param item1:"""
    @property
    def Item(self) -> object:
        """:return:"""
    @property
    def Length(self) -> int:
        """:return:"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: ValueTuple[T1, T2, T3, T4, T5, T6, T7, TRest]) -> int:
        """:param other:
        :return:
        """
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: ValueTuple[T1, T2, T3, T4, T5, T6, T7, TRest]) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def ToStringEnd(self) -> str:
        """:return:"""
    def __getitem__(self, index: int) -> object:
        """:param index:
        :return:
        """

class ValueTuple(
    Generic[T1, T2, T3, T4, T5, T6, T7],
    ValueType,
    IStructuralComparable,
    IStructuralEquatable,
    ITuple,
    IComparable,
    IComparable[ValueTuple, T2, T3, T4, T5, T6, T7],
    IEquatable[ValueTuple, T2, T3, T4, T5, T6, T7],
    IValueTupleInternal,
):
    """"""

    Item1: Final[T1] = ...
    """
    
    :return: 
    """
    Item2: Final[T2] = ...
    """"""
    Item3: Final[T3] = ...
    """"""
    Item4: Final[T4] = ...
    """"""
    Item5: Final[T5] = ...
    """"""
    Item6: Final[T6] = ...
    """"""
    Item7: Final[T7] = ...
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
    ):
        """:param item1:"""
    @property
    def Item(self) -> object:
        """:return:"""
    @property
    def Length(self) -> int:
        """:return:"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: ValueTuple[T1, T2, T3, T4, T5, T6, T7]) -> int:
        """:param other:
        :return:
        """
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: ValueTuple[T1, T2, T3, T4, T5, T6, T7]) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def ToStringEnd(self) -> str:
        """:return:"""
    def __getitem__(self, index: int) -> object:
        """:param index:
        :return:
        """

class ValueTuple(
    Generic[T1, T2, T3, T4, T5, T6],
    ValueType,
    IStructuralComparable,
    IStructuralEquatable,
    ITuple,
    IComparable,
    IComparable[ValueTuple, T2, T3, T4, T5, T6],
    IEquatable[ValueTuple, T2, T3, T4, T5, T6],
    IValueTupleInternal,
):
    """"""

    Item1: Final[T1] = ...
    """
    
    :return: 
    """
    Item2: Final[T2] = ...
    """"""
    Item3: Final[T3] = ...
    """"""
    Item4: Final[T4] = ...
    """"""
    Item5: Final[T5] = ...
    """"""
    Item6: Final[T6] = ...
    """"""
    def __init__(self, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6):
        """:param item1:"""
    @property
    def Item(self) -> object:
        """:return:"""
    @property
    def Length(self) -> int:
        """:return:"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: ValueTuple[T1, T2, T3, T4, T5, T6]) -> int:
        """:param other:
        :return:
        """
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: ValueTuple[T1, T2, T3, T4, T5, T6]) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def ToStringEnd(self) -> str:
        """:return:"""
    def __getitem__(self, index: int) -> object:
        """:param index:
        :return:
        """

class ValueTuple(
    Generic[T1, T2, T3, T4, T5],
    ValueType,
    IStructuralComparable,
    IStructuralEquatable,
    ITuple,
    IComparable,
    IComparable[ValueTuple, T2, T3, T4, T5],
    IEquatable[ValueTuple, T2, T3, T4, T5],
    IValueTupleInternal,
):
    """"""

    Item1: Final[T1] = ...
    """
    
    :return: 
    """
    Item2: Final[T2] = ...
    """"""
    Item3: Final[T3] = ...
    """"""
    Item4: Final[T4] = ...
    """"""
    Item5: Final[T5] = ...
    """"""
    def __init__(self, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5):
        """:param item1:"""
    @property
    def Item(self) -> object:
        """:return:"""
    @property
    def Length(self) -> int:
        """:return:"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: ValueTuple[T1, T2, T3, T4, T5]) -> int:
        """:param other:
        :return:
        """
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: ValueTuple[T1, T2, T3, T4, T5]) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def ToStringEnd(self) -> str:
        """:return:"""
    def __getitem__(self, index: int) -> object:
        """:param index:
        :return:
        """

class ValueTuple(
    Generic[T1, T2, T3, T4],
    ValueType,
    IStructuralComparable,
    IStructuralEquatable,
    ITuple,
    IComparable,
    IComparable[ValueTuple, T2, T3, T4],
    IEquatable[ValueTuple, T2, T3, T4],
    IValueTupleInternal,
):
    """"""

    Item1: Final[T1] = ...
    """
    
    :return: 
    """
    Item2: Final[T2] = ...
    """"""
    Item3: Final[T3] = ...
    """"""
    Item4: Final[T4] = ...
    """"""
    def __init__(self, item1: T1, item2: T2, item3: T3, item4: T4):
        """:param item1:"""
    @property
    def Item(self) -> object:
        """:return:"""
    @property
    def Length(self) -> int:
        """:return:"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: ValueTuple[T1, T2, T3, T4]) -> int:
        """:param other:
        :return:
        """
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: ValueTuple[T1, T2, T3, T4]) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def ToStringEnd(self) -> str:
        """:return:"""
    def __getitem__(self, index: int) -> object:
        """:param index:
        :return:
        """

class ValueTuple(
    Generic[T1, T2, T3],
    ValueType,
    IStructuralComparable,
    IStructuralEquatable,
    ITuple,
    IComparable,
    IComparable[ValueTuple, T2, T3],
    IEquatable[ValueTuple, T2, T3],
    IValueTupleInternal,
):
    """"""

    Item1: Final[T1] = ...
    """
    
    :return: 
    """
    Item2: Final[T2] = ...
    """"""
    Item3: Final[T3] = ...
    """"""
    def __init__(self, item1: T1, item2: T2, item3: T3):
        """:param item1:"""
    @property
    def Item(self) -> object:
        """:return:"""
    @property
    def Length(self) -> int:
        """:return:"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: ValueTuple[T1, T2, T3]) -> int:
        """:param other:
        :return:
        """
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: ValueTuple[T1, T2, T3]) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def ToStringEnd(self) -> str:
        """:return:"""
    def __getitem__(self, index: int) -> object:
        """:param index:
        :return:
        """

class ValueTuple(
    Generic[T1, T2],
    ValueType,
    IStructuralComparable,
    IStructuralEquatable,
    ITuple,
    IComparable,
    IComparable[ValueTuple, T2],
    IEquatable[ValueTuple, T2],
    IValueTupleInternal,
):
    """"""

    Item1: Final[T1] = ...
    """
    
    :return: 
    """
    Item2: Final[T2] = ...
    """"""
    def __init__(self, item1: T1, item2: T2):
        """:param item1:"""
    @property
    def Item(self) -> object:
        """:return:"""
    @property
    def Length(self) -> int:
        """:return:"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: ValueTuple[T1, T2]) -> int:
        """:param other:
        :return:
        """
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: ValueTuple[T1, T2]) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def ToStringEnd(self) -> str:
        """:return:"""
    def __getitem__(self, index: int) -> object:
        """:param index:
        :return:
        """

class ValueTuple(
    Generic[T1],
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

    Item1: Final[T1] = ...
    """
    
    :return: 
    """
    def __init__(self, item1: T1):
        """:param item1:"""
    @property
    def Item(self) -> object:
        """:return:"""
    @property
    def Length(self) -> int:
        """:return:"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: ValueTuple[T1]) -> int:
        """:param other:
        :return:
        """
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: ValueTuple[T1]) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """:param other:
        :param comparer:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """:param comparer:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def ToStringEnd(self) -> str:
        """:return:"""
    def __getitem__(self, index: int) -> object:
        """:param index:
        :return:
        """

class ValueType(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class Variant(ValueType):
    """"""

    @overload
    def __init__(self, val: bool):
        """:param val:"""
    @overload
    def __init__(self, val: int):
        """:param val:"""
    @overload
    def __init__(self, val: Char):
        """:param val:"""
    @overload
    def __init__(self, val: DateTime):
        """:param val:"""
    @overload
    def __init__(self, val: Decimal):
        """:param val:"""
    @overload
    def __init__(self, val: float):
        """:param val:"""
    @overload
    def __init__(self, val: int):
        """:param val:"""
    @overload
    def __init__(self, val: int):
        """:param val:"""
    @overload
    def __init__(self, val: int):
        """:param val:"""
    @overload
    def __init__(self, obj: object):
        """:param obj:"""
    @overload
    def __init__(self, val: int):
        """:param val:"""
    @overload
    def __init__(self, val: float):
        """:param val:"""
    @overload
    def __init__(self, val: int):
        """:param val:"""
    @overload
    def __init__(self, val: int):
        """:param val:"""
    @overload
    def __init__(self, val: int):
        """:param val:"""
    @overload
    def __init__(self, voidPointer: None, pointerType: Type):
        """:param voidPointer:
        :param pointerType:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToObject(self) -> object:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class Version(Object, ICloneable, IComparable, IComparable[Version], IEquatable[Version]):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, version: str):
        """:param version:"""
    @overload
    def __init__(self, major: int, minor: int):
        """:param major:
        :param minor:
        """
    @overload
    def __init__(self, major: int, minor: int, build: int):
        """:param major:
        :param minor:
        :param build:
        """
    @overload
    def __init__(self, major: int, minor: int, build: int, revision: int):
        """:param major:
        :param minor:
        :param build:
        :param revision:
        """
    @property
    def Build(self) -> int:
        """:return:"""
    @property
    def Major(self) -> int:
        """:return:"""
    @property
    def MajorRevision(self) -> int:
        """:return:"""
    @property
    def Minor(self) -> int:
        """:return:"""
    @property
    def MinorRevision(self) -> int:
        """:return:"""
    @property
    def Revision(self) -> int:
        """:return:"""
    def Clone(self) -> object:
        """:return:"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    @overload
    def CompareTo(self, other: Version) -> int:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, other: Version) -> bool:
        """:param other:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def Parse(cls, input: str) -> Version:
        """:param input:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self, fieldCount: int) -> str:
        """:param fieldCount:
        :return:
        """
    @classmethod
    def TryParse(cls, input: str, result: Version) -> Tuple[bool, Version]:
        """:param input:
        :param result:
        :return:
        """
    def __eq__(self, other: Version) -> bool:
        """:param other:
        :return:
        """
    def __ge__(self, other: Version) -> bool:
        """:param other:
        :return:
        """
    def __gt__(self, other: Version) -> bool:
        """:param other:
        :return:
        """
    def __le__(self, other: Version) -> bool:
        """:param other:
        :return:
        """
    def __lt__(self, other: Version) -> bool:
        """:param other:
        :return:
        """
    def __ne__(self, other: Version) -> bool:
        """:param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, v1: Version, v2: Version) -> bool:
        """:param v1:
        :param v2:
        :return:
        """
    @classmethod
    def op_GreaterThan(cls, v1: Version, v2: Version) -> bool:
        """:param v1:
        :param v2:
        :return:
        """
    @classmethod
    def op_GreaterThanOrEqual(cls, v1: Version, v2: Version) -> bool:
        """:param v1:
        :param v2:
        :return:
        """
    @classmethod
    def op_Inequality(cls, v1: Version, v2: Version) -> bool:
        """:param v1:
        :param v2:
        :return:
        """
    @classmethod
    def op_LessThan(cls, v1: Version, v2: Version) -> bool:
        """:param v1:
        :param v2:
        :return:
        """
    @classmethod
    def op_LessThanOrEqual(cls, v1: Version, v2: Version) -> bool:
        """:param v1:
        :param v2:
        :return:
        """

class Void(ValueType):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class WeakReference(Object, ISerializable):
    """"""

    @overload
    def __init__(self, target: object):
        """:param target:"""
    @overload
    def __init__(self, target: object, trackResurrection: bool):
        """:param target:
        :param trackResurrection:
        """
    @property
    def IsAlive(self) -> bool:
        """:return:"""
    @property
    def Target(self) -> object:
        """:return:"""
    @Target.setter
    def Target(self, value: object) -> None: ...
    @property
    def TrackResurrection(self) -> bool:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class WeakReference(Generic[T], Object, ISerializable):
    """"""

    @overload
    def __init__(self, target: T):
        """:param target:"""
    @overload
    def __init__(self, target: T, trackResurrection: bool):
        """:param target:
        :param trackResurrection:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    def GetType(self) -> Type:
        """:return:"""
    def SetTarget(self, target: T) -> None:
        """:param target:"""
    def ToString(self) -> str:
        """:return:"""
    def TryGetTarget(self, target: T) -> Tuple[bool, T]:
        """:param target:
        :return:
        """

class XmlIgnoreMemberAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
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
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class _AppDomain:
    """"""

    @property
    def BaseDirectory(self) -> str:
        """:return:"""
    @property
    def DynamicDirectory(self) -> str:
        """:return:"""
    @property
    def Evidence(self) -> Evidence:
        """:return:"""
    @property
    def FriendlyName(self) -> str:
        """:return:"""
    @property
    def RelativeSearchPath(self) -> str:
        """:return:"""
    @property
    def ShadowCopyFiles(self) -> bool:
        """:return:"""
    def AppendPrivatePath(self, path: str) -> None:
        """:param path:"""
    def ClearPrivatePath(self) -> None:
        """"""
    def ClearShadowCopyPath(self) -> None:
        """"""
    @overload
    def CreateInstance(self, assemblyName: str, typeName: str) -> ObjectHandle:
        """:param assemblyName:
        :param typeName:
        :return:
        """
    @overload
    def CreateInstance(
        self, assemblyName: str, typeName: str, activationAttributes: Array[object]
    ) -> ObjectHandle:
        """:param assemblyName:
        :param typeName:
        :param activationAttributes:
        :return:
        """
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
        """:param assemblyName:
        :param typeName:
        :param ignoreCase:
        :param bindingAttr:
        :param binder:
        :param args:
        :param culture:
        :param activationAttributes:
        :param securityAttributes:
        :return:
        """
    @overload
    def CreateInstanceFrom(self, assemblyFile: str, typeName: str) -> ObjectHandle:
        """:param assemblyFile:
        :param typeName:
        :return:
        """
    @overload
    def CreateInstanceFrom(
        self, assemblyFile: str, typeName: str, activationAttributes: Array[object]
    ) -> ObjectHandle:
        """:param assemblyFile:
        :param typeName:
        :param activationAttributes:
        :return:
        """
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
        """:param assemblyFile:
        :param typeName:
        :param ignoreCase:
        :param bindingAttr:
        :param binder:
        :param args:
        :param culture:
        :param activationAttributes:
        :param securityAttributes:
        :return:
        """
    @overload
    def DefineDynamicAssembly(
        self, name: AssemblyName, access: AssemblyBuilderAccess
    ) -> AssemblyBuilder:
        """:param name:
        :param access:
        :return:
        """
    @overload
    def DefineDynamicAssembly(
        self, name: AssemblyName, access: AssemblyBuilderAccess, evidence: Evidence
    ) -> AssemblyBuilder:
        """:param name:
        :param access:
        :param evidence:
        :return:
        """
    @overload
    def DefineDynamicAssembly(
        self, name: AssemblyName, access: AssemblyBuilderAccess, dir: str
    ) -> AssemblyBuilder:
        """:param name:
        :param access:
        :param dir:
        :return:
        """
    @overload
    def DefineDynamicAssembly(
        self,
        name: AssemblyName,
        access: AssemblyBuilderAccess,
        dir: str,
        evidence: Evidence,
    ) -> AssemblyBuilder:
        """:param name:
        :param access:
        :param dir:
        :param evidence:
        :return:
        """
    @overload
    def DefineDynamicAssembly(
        self,
        name: AssemblyName,
        access: AssemblyBuilderAccess,
        requiredPermissions: PermissionSet,
        optionalPermissions: PermissionSet,
        refusedPermissions: PermissionSet,
    ) -> AssemblyBuilder:
        """:param name:
        :param access:
        :param requiredPermissions:
        :param optionalPermissions:
        :param refusedPermissions:
        :return:
        """
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
        """:param name:
        :param access:
        :param evidence:
        :param requiredPermissions:
        :param optionalPermissions:
        :param refusedPermissions:
        :return:
        """
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
        """:param name:
        :param access:
        :param dir:
        :param requiredPermissions:
        :param optionalPermissions:
        :param refusedPermissions:
        :return:
        """
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
        """:param name:
        :param access:
        :param dir:
        :param evidence:
        :param requiredPermissions:
        :param optionalPermissions:
        :param refusedPermissions:
        :return:
        """
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
        """:param name:
        :param access:
        :param dir:
        :param evidence:
        :param requiredPermissions:
        :param optionalPermissions:
        :param refusedPermissions:
        :param isSynchronized:
        :return:
        """
    def DoCallBack(self, theDelegate: CrossAppDomainDelegate) -> None:
        """:param theDelegate:"""
    def Equals(self, other: object) -> bool:
        """:param other:
        :return:
        """
    @overload
    def ExecuteAssembly(self, assemblyFile: str) -> int:
        """:param assemblyFile:
        :return:
        """
    @overload
    def ExecuteAssembly(self, assemblyFile: str, assemblySecurity: Evidence) -> int:
        """:param assemblyFile:
        :param assemblySecurity:
        :return:
        """
    @overload
    def ExecuteAssembly(
        self, assemblyFile: str, assemblySecurity: Evidence, args: Array[str]
    ) -> int:
        """:param assemblyFile:
        :param assemblySecurity:
        :param args:
        :return:
        """
    def GetAssemblies(self) -> Array[Assembly]:
        """:return:"""
    def GetData(self, name: str) -> object:
        """:param name:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetLifetimeService(self) -> object:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """:param pcTInfo:"""
    def InitializeLifetimeService(self) -> object:
        """:return:"""
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
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    @overload
    def Load(self, assemblyRef: AssemblyName) -> Assembly:
        """:param assemblyRef:
        :return:
        """
    @overload
    def Load(self, rawAssembly: Array[int]) -> Assembly:
        """:param rawAssembly:
        :return:
        """
    @overload
    def Load(self, assemblyString: str) -> Assembly:
        """:param assemblyString:
        :return:
        """
    @overload
    def Load(self, assemblyRef: AssemblyName, assemblySecurity: Evidence) -> Assembly:
        """:param assemblyRef:
        :param assemblySecurity:
        :return:
        """
    @overload
    def Load(self, rawAssembly: Array[int], rawSymbolStore: Array[int]) -> Assembly:
        """:param rawAssembly:
        :param rawSymbolStore:
        :return:
        """
    @overload
    def Load(self, assemblyString: str, assemblySecurity: Evidence) -> Assembly:
        """:param assemblyString:
        :param assemblySecurity:
        :return:
        """
    @overload
    def Load(
        self,
        rawAssembly: Array[int],
        rawSymbolStore: Array[int],
        securityEvidence: Evidence,
    ) -> Assembly:
        """:param rawAssembly:
        :param rawSymbolStore:
        :param securityEvidence:
        :return:
        """
    def SetAppDomainPolicy(self, domainPolicy: PolicyLevel) -> None:
        """:param domainPolicy:"""
    def SetCachePath(self, s: str) -> None:
        """:param s:"""
    def SetData(self, name: str, data: object) -> None:
        """:param name:
        :param data:
        """
    def SetPrincipalPolicy(self, policy: PrincipalPolicy) -> None:
        """:param policy:"""
    def SetShadowCopyPath(self, s: str) -> None:
        """:param s:"""
    def SetThreadPrincipal(self, principal: IPrincipal) -> None:
        """:param principal:"""
    def ToString(self) -> str:
        """:return:"""
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

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class __ComObject(MarshalByRefObject):
    """"""

    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """:param requestedType:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetLifetimeService(self) -> object:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def InitializeLifetimeService(self) -> object:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class __DTString(ValueType):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class __Filters(Object):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class __HResults(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
