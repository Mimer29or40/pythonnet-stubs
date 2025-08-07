"""Automatically generated stubs for C# namespace: System.Runtime.InteropServices."""

from abc import ABC
from collections.abc import Callable
from collections.abc import Iterator
from typing import ClassVar
from typing import Final
from typing import Self
from typing import overload

from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from System import Array
from System import Attribute
from System import Boolean
from System import Byte
from System import Char
from System import DateTime
from System import Decimal
from System import Delegate
from System import Enum
from System import Exception
from System import Guid
from System import IDisposable
from System import IEquatable
from System import Int16
from System import Int32
from System import Int64
from System import IntPtr
from System import MarshalByRefObject
from System import Object
from System import RuntimeFieldHandle
from System import RuntimeMethodHandle
from System import RuntimeTypeHandle
from System import String
from System import SystemException
from System import Type
from System import TypedReference
from System import UInt32
from System import ValueType
from System import Version
from System.Collections import IDictionary
from System.Collections import IEnumerator
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IList
from System.Globalization import CultureInfo
from System.IO import FileStream
from System.IO import Stream
from System.Reflection import Assembly
from System.Reflection import AssemblyName
from System.Reflection import Binder
from System.Reflection import BindingFlags
from System.Reflection import CallingConventions
from System.Reflection import ConstructorInfo
from System.Reflection import CustomAttributeData
from System.Reflection import EventAttributes
from System.Reflection import EventInfo
from System.Reflection import FieldAttributes
from System.Reflection import FieldInfo
from System.Reflection import ICustomAttributeProvider
from System.Reflection import InterfaceMapping
from System.Reflection import ManifestResourceInfo
from System.Reflection import MemberFilter
from System.Reflection import MemberInfo
from System.Reflection import MemberTypes
from System.Reflection import MethodAttributes
from System.Reflection import MethodBase
from System.Reflection import MethodImplAttributes
from System.Reflection import MethodInfo
from System.Reflection import Module
from System.Reflection import ModuleResolveEventHandler
from System.Reflection import ParameterInfo
from System.Reflection import ParameterModifier
from System.Reflection import PropertyAttributes
from System.Reflection import PropertyInfo
from System.Reflection import StrongNameKeyPair
from System.Reflection import TypeAttributes
from System.Reflection import TypeFilter
from System.Reflection.Emit import AssemblyBuilder
from System.Runtime.ConstrainedExecution import CriticalFinalizerObject
from System.Runtime.InteropServices.ComTypes import DISPPARAMS
from System.Runtime.InteropServices.ComTypes import INVOKEKIND
from System.Runtime.InteropServices.ComTypes import ITypeInfo
from System.Runtime.InteropServices.ComTypes import ITypeLib
from System.Runtime.Remoting import ObjRef
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Security import SecureString
from System.Security.Policy import Evidence
from System.Threading import Thread

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

class AllowReversePInvokeCallsAttribute(Attribute, _Attribute):
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

class Architecture(Enum):
    """"""

    X86: Architecture = ...
    """"""
    X64: Architecture = ...
    """"""
    Arm: Architecture = ...
    """"""
    Arm64: Architecture = ...
    """"""

class ArrayWithOffset(ValueType):
    """"""
    def __init__(self, array: object, offset: int) -> None:
        """"""
    @overload
    def Equals(self, obj: ArrayWithOffset) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArray(self) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOffset(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, a: ArrayWithOffset, b: ArrayWithOffset) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, a: ArrayWithOffset, b: ArrayWithOffset) -> bool:
        """"""
    def __eq__(self, other: ArrayWithOffset) -> bool:
        """"""
    def __ne__(self, other: ArrayWithOffset) -> bool:
        """"""

class AssemblyRegistrationFlags(Enum):
    """"""

    _None: AssemblyRegistrationFlags = ...
    """"""
    SetCodeBase: AssemblyRegistrationFlags = ...
    """"""

class AutomationProxyAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, val: bool) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Value(self) -> bool:
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

class BINDPTR(ValueType):
    """"""

    lpfuncdesc: Final[IntPtr]
    """"""
    lptcomp: Final[IntPtr]
    """"""
    lpvardesc: Final[IntPtr]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class BIND_OPTS(ValueType):
    """"""

    cbStruct: Final[int]
    """"""
    dwTickCountDeadline: Final[int]
    """"""
    grfFlags: Final[int]
    """"""
    grfMode: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class BStrWrapper(Object):
    """"""
    @overload
    def __init__(self, value: str) -> None:
        """"""
    @overload
    def __init__(self, value: object) -> None:
        """"""
    @property
    def WrappedObject(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class BestFitMappingAttribute(Attribute, _Attribute):
    """"""

    ThrowOnUnmappableChar: Final[bool]
    """"""
    def __init__(self, BestFitMapping: bool) -> None:
        """"""
    @property
    def BestFitMapping(self) -> bool:
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

class CALLCONV(Enum):
    """"""

    CC_CDECL: CALLCONV = ...
    """"""
    CC_MSCPASCAL: CALLCONV = ...
    """"""
    CC_PASCAL: CALLCONV = ...
    """"""
    CC_MACPASCAL: CALLCONV = ...
    """"""
    CC_STDCALL: CALLCONV = ...
    """"""
    CC_RESERVED: CALLCONV = ...
    """"""
    CC_SYSCALL: CALLCONV = ...
    """"""
    CC_MPWCDECL: CALLCONV = ...
    """"""
    CC_MPWPASCAL: CALLCONV = ...
    """"""
    CC_MAX: CALLCONV = ...
    """"""

class COMException(ExternalException, _Exception, ISerializable):
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
    def __init__(self, message: str, errorCode: int) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def ErrorCode(self) -> int:
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

class CONNECTDATA(ValueType):
    """"""

    dwCookie: Final[int]
    """"""
    pUnk: Final[object]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CallingConvention(Enum):
    """"""

    Winapi: CallingConvention = ...
    """"""
    Cdecl: CallingConvention = ...
    """"""
    StdCall: CallingConvention = ...
    """"""
    ThisCall: CallingConvention = ...
    """"""
    FastCall: CallingConvention = ...
    """"""

class CharSet(Enum):
    """"""

    _None: CharSet = ...
    """"""
    Ansi: CharSet = ...
    """"""
    Unicode: CharSet = ...
    """"""
    Auto: CharSet = ...
    """"""

class ClassInterfaceAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, classInterfaceType: ClassInterfaceType) -> None:
        """"""
    @overload
    def __init__(self, classInterfaceType: int) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Value(self) -> ClassInterfaceType:
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

class ClassInterfaceType(Enum):
    """"""

    _None: ClassInterfaceType = ...
    """"""
    AutoDispatch: ClassInterfaceType = ...
    """"""
    AutoDual: ClassInterfaceType = ...
    """"""

class CoClassAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, coClass: Type) -> None:
        """"""
    @property
    def CoClass(self) -> Type:
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

class ComAliasNameAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, alias: str) -> None:
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

class ComAwareEventInfo(EventInfo, ICustomAttributeProvider, _EventInfo, _MemberInfo):
    """"""
    def __init__(self, type: Type, eventName: str) -> None:
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

class ComCompatibleVersionAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, major: int, minor: int, build: int, revision: int) -> None:
        """"""
    @property
    def BuildNumber(self) -> int:
        """"""
    @property
    def MajorVersion(self) -> int:
        """"""
    @property
    def MinorVersion(self) -> int:
        """"""
    @property
    def RevisionNumber(self) -> int:
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

class ComConversionLossAttribute(Attribute, _Attribute):
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

class ComDefaultInterfaceAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, defaultInterface: Type) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Value(self) -> Type:
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

class ComEventInterfaceAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, SourceInterface: Type, EventProvider: Type) -> None:
        """"""
    @property
    def EventProvider(self) -> Type:
        """"""
    @property
    def SourceInterface(self) -> Type:
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

class ComEventsHelper(ABC, Object):
    """"""
    @classmethod
    def Combine(cls, rcw: object, iid: Guid, dispid: int, d: Delegate) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Remove(cls, rcw: object, iid: Guid, dispid: int, d: Delegate) -> Delegate:
        """"""
    def ToString(self) -> str:
        """"""
    def __delitem__(self, rcw: object, iid: Guid, dispid: int, d: Delegate) -> Delegate:
        """"""

class ComEventsInfo(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ComEventsMethod(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ComEventsSink(Object, ICustomQueryInterface, NativeMethods.IDispatch):
    """"""
    def AddMethod(self, dispid: int) -> ComEventsMethod:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FindMethod(self, dispid: int) -> ComEventsMethod:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, iid: Guid, names: Array[str], cNames: int, lcid: int, rgDispId: Array[int]
    ) -> tuple[None, Array[int]]:
        """"""
    def GetInterface(self, iid: Guid, ppv: IntPtr) -> tuple[CustomQueryInterfaceResult, IntPtr]:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, info: IntPtr) -> tuple[None, IntPtr]:
        """"""
    def GetTypeInfoCount(self, pctinfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: INVOKEKIND,
        pDispParams: DISPPARAMS,
        pvarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def RemoveMethod(self, method: ComEventsMethod) -> ComEventsMethod:
        """"""
    def ToString(self) -> str:
        """"""

class ComImportAttribute(Attribute, _Attribute):
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

class ComInterfaceType(Enum):
    """"""

    InterfaceIsDual: ComInterfaceType = ...
    """"""
    InterfaceIsIUnknown: ComInterfaceType = ...
    """"""
    InterfaceIsIDispatch: ComInterfaceType = ...
    """"""
    InterfaceIsIInspectable: ComInterfaceType = ...
    """"""

class ComMemberType(Enum):
    """"""

    Method: ComMemberType = ...
    """"""
    PropGet: ComMemberType = ...
    """"""
    PropSet: ComMemberType = ...
    """"""

class ComRegisterFunctionAttribute(Attribute, _Attribute):
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

class ComSourceInterfacesAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, sourceInterfaces: str) -> None:
        """"""
    @overload
    def __init__(self, sourceInterface: Type) -> None:
        """"""
    @overload
    def __init__(self, sourceInterface1: Type, sourceInterface2: Type) -> None:
        """"""
    @overload
    def __init__(
        self, sourceInterface1: Type, sourceInterface2: Type, sourceInterface3: Type
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        sourceInterface1: Type,
        sourceInterface2: Type,
        sourceInterface3: Type,
        sourceInterface4: Type,
    ) -> None:
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

class ComUnregisterFunctionAttribute(Attribute, _Attribute):
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

class ComVisibleAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, visibility: bool) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Value(self) -> bool:
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

class CriticalHandle(ABC, CriticalFinalizerObject, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
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

class CurrencyWrapper(Object):
    """"""
    @overload
    def __init__(self, obj: Decimal) -> None:
        """"""
    @overload
    def __init__(self, obj: object) -> None:
        """"""
    @property
    def WrappedObject(self) -> Decimal:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CustomQueryInterfaceMode(Enum):
    """"""

    Ignore: CustomQueryInterfaceMode = ...
    """"""
    Allow: CustomQueryInterfaceMode = ...
    """"""

class CustomQueryInterfaceResult(Enum):
    """"""

    Handled: CustomQueryInterfaceResult = ...
    """"""
    NotHandled: CustomQueryInterfaceResult = ...
    """"""
    Failed: CustomQueryInterfaceResult = ...
    """"""

class DESCKIND(Enum):
    """"""

    DESCKIND_NONE: DESCKIND = ...
    """"""
    DESCKIND_FUNCDESC: DESCKIND = ...
    """"""
    DESCKIND_VARDESC: DESCKIND = ...
    """"""
    DESCKIND_TYPECOMP: DESCKIND = ...
    """"""
    DESCKIND_IMPLICITAPPOBJ: DESCKIND = ...
    """"""
    DESCKIND_MAX: DESCKIND = ...
    """"""

class DISPPARAMS(ValueType):
    """"""

    cArgs: Final[int]
    """"""
    cNamedArgs: Final[int]
    """"""
    rgdispidNamedArgs: Final[IntPtr]
    """"""
    rgvarg: Final[IntPtr]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DefaultCharSetAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, charSet: CharSet) -> None:
        """"""
    @property
    def CharSet(self) -> CharSet:
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

class DefaultDllImportSearchPathsAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, paths: DllImportSearchPath) -> None:
        """"""
    @property
    def Paths(self) -> DllImportSearchPath:
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

class DefaultParameterValueAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, value: object) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Value(self) -> object:
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

class DispIdAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, dispId: int) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Value(self) -> int:
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

class DispatchWrapper(Object):
    """"""
    def __init__(self, obj: object) -> None:
        """"""
    @property
    def WrappedObject(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DllImportAttribute(Attribute, _Attribute):
    """"""

    BestFitMapping: Final[bool]
    """"""
    CallingConvention: Final[CallingConvention]
    """"""
    CharSet: Final[CharSet]
    """"""
    EntryPoint: Final[str]
    """"""
    ExactSpelling: Final[bool]
    """"""
    PreserveSig: Final[bool]
    """"""
    SetLastError: Final[bool]
    """"""
    ThrowOnUnmappableChar: Final[bool]
    """"""
    def __init__(self, dllName: str) -> None:
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

class DllImportSearchPath(Enum):
    """"""

    LegacyBehavior: DllImportSearchPath = ...
    """"""
    AssemblyDirectory: DllImportSearchPath = ...
    """"""
    UseDllDirectoryForDependencies: DllImportSearchPath = ...
    """"""
    ApplicationDirectory: DllImportSearchPath = ...
    """"""
    UserDirectories: DllImportSearchPath = ...
    """"""
    System32: DllImportSearchPath = ...
    """"""
    SafeDirectories: DllImportSearchPath = ...
    """"""

class ELEMDESC(ValueType):
    """"""

    desc: Final[ELEMDESC.DESCUNION]
    """"""
    tdesc: Final[TYPEDESC]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    class DESCUNION(ValueType):
        """"""

        idldesc: Final[IDLDESC]
        """"""
        paramdesc: Final[PARAMDESC]
        """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""

class EXCEPINFO(ValueType):
    """"""

    bstrDescription: Final[str]
    """"""
    bstrHelpFile: Final[str]
    """"""
    bstrSource: Final[str]
    """"""
    dwHelpContext: Final[int]
    """"""
    pfnDeferredFillIn: Final[IntPtr]
    """"""
    pvReserved: Final[IntPtr]
    """"""
    wCode: Final[int]
    """"""
    wReserved: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ErrorWrapper(Object):
    """"""
    @overload
    def __init__(self, errorCode: int) -> None:
        """"""
    @overload
    def __init__(self, errorCode: object) -> None:
        """"""
    @overload
    def __init__(self, e: Exception) -> None:
        """"""
    @property
    def ErrorCode(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ExporterEventKind(Enum):
    """"""

    NOTIF_TYPECONVERTED: ExporterEventKind = ...
    """"""
    NOTIF_CONVERTWARNING: ExporterEventKind = ...
    """"""
    ERROR_REFTOINVALIDASSEMBLY: ExporterEventKind = ...
    """"""

class ExtensibleClassFactory(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def RegisterObjectCreationCallback(cls, callback: ObjectCreationDelegate) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class ExternalException(SystemException, _Exception, ISerializable):
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
    def __init__(self, message: str, errorCode: int) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def ErrorCode(self) -> int:
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

class FILETIME(ValueType):
    """"""

    dwHighDateTime: Final[int]
    """"""
    dwLowDateTime: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class FUNCDESC(ValueType):
    """"""

    cParams: Final[int]
    """"""
    cParamsOpt: Final[int]
    """"""
    cScodes: Final[int]
    """"""
    callconv: Final[CALLCONV]
    """"""
    elemdescFunc: Final[ELEMDESC]
    """"""
    funckind: Final[FUNCKIND]
    """"""
    invkind: Final[INVOKEKIND]
    """"""
    lprgelemdescParam: Final[IntPtr]
    """"""
    lprgscode: Final[IntPtr]
    """"""
    memid: Final[int]
    """"""
    oVft: Final[int]
    """"""
    wFuncFlags: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class FUNCFLAGS(Enum):
    """"""

    FUNCFLAG_FRESTRICTED: FUNCFLAGS = ...
    """"""
    FUNCFLAG_FSOURCE: FUNCFLAGS = ...
    """"""
    FUNCFLAG_FBINDABLE: FUNCFLAGS = ...
    """"""
    FUNCFLAG_FREQUESTEDIT: FUNCFLAGS = ...
    """"""
    FUNCFLAG_FDISPLAYBIND: FUNCFLAGS = ...
    """"""
    FUNCFLAG_FDEFAULTBIND: FUNCFLAGS = ...
    """"""
    FUNCFLAG_FHIDDEN: FUNCFLAGS = ...
    """"""
    FUNCFLAG_FUSESGETLASTERROR: FUNCFLAGS = ...
    """"""
    FUNCFLAG_FDEFAULTCOLLELEM: FUNCFLAGS = ...
    """"""
    FUNCFLAG_FUIDEFAULT: FUNCFLAGS = ...
    """"""
    FUNCFLAG_FNONBROWSABLE: FUNCFLAGS = ...
    """"""
    FUNCFLAG_FREPLACEABLE: FUNCFLAGS = ...
    """"""
    FUNCFLAG_FIMMEDIATEBIND: FUNCFLAGS = ...
    """"""

class FUNCKIND(Enum):
    """"""

    FUNC_VIRTUAL: FUNCKIND = ...
    """"""
    FUNC_PUREVIRTUAL: FUNCKIND = ...
    """"""
    FUNC_NONVIRTUAL: FUNCKIND = ...
    """"""
    FUNC_STATIC: FUNCKIND = ...
    """"""
    FUNC_DISPATCH: FUNCKIND = ...
    """"""

class FieldOffsetAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, offset: int) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Value(self) -> int:
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

class GCHandle(ValueType):
    """"""
    @property
    def IsAllocated(self) -> bool:
        """"""
    @property
    def Target(self) -> object:
        """"""
    @Target.setter
    def Target(self, value: object) -> None: ...
    def AddrOfPinnedObject(self) -> IntPtr:
        """"""
    @classmethod
    @overload
    def Alloc(cls, value: object) -> GCHandle:
        """"""
    @classmethod
    @overload
    def Alloc(cls, value: object, type: GCHandleType) -> GCHandle:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def Free(self) -> None:
        """"""
    @classmethod
    def FromIntPtr(cls, value: IntPtr) -> GCHandle:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ToIntPtr(cls, value: GCHandle) -> IntPtr:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, a: GCHandle, b: GCHandle) -> bool:
        """"""
    @classmethod
    @overload
    def op_Explicit(cls, value: GCHandle) -> IntPtr:
        """"""
    @classmethod
    @overload
    def op_Explicit(cls, value: IntPtr) -> GCHandle:
        """"""
    @classmethod
    def op_Inequality(cls, a: GCHandle, b: GCHandle) -> bool:
        """"""
    def __eq__(self, other: GCHandle) -> bool:
        """"""
    def __ne__(self, other: GCHandle) -> bool:
        """"""

class GCHandleCookieTable(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class GCHandleType(Enum):
    """"""

    Weak: GCHandleType = ...
    """"""
    WeakTrackResurrection: GCHandleType = ...
    """"""
    Normal: GCHandleType = ...
    """"""
    Pinned: GCHandleType = ...
    """"""

class GuidAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, guid: str) -> None:
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

class HandleCollector(Object):
    """"""
    @overload
    def __init__(self, name: str, initialThreshold: int) -> None:
        """"""
    @overload
    def __init__(self, name: str, initialThreshold: int, maximumThreshold: int) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def InitialThreshold(self) -> int:
        """"""
    @property
    def MaximumThreshold(self) -> int:
        """"""
    @property
    def Name(self) -> str:
        """"""
    def Add(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __delitem__(self) -> None:
        """"""
    def __len__(self) -> int:
        """"""

class HandleRef(ValueType):
    """"""
    def __init__(self, wrapper: object, handle: IntPtr) -> None:
        """"""
    @property
    def Handle(self) -> IntPtr:
        """"""
    @property
    def Wrapper(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ToIntPtr(cls, value: HandleRef) -> IntPtr:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Explicit(cls, value: HandleRef) -> IntPtr:
        """"""

class ICustomAdapter:
    """"""
    def GetUnderlyingObject(self) -> object:
        """"""

class ICustomFactory:
    """"""
    def CreateInstance(self, serverType: Type) -> MarshalByRefObject:
        """"""

class ICustomMarshaler:
    """"""
    def CleanUpManagedData(self, ManagedObj: object) -> None:
        """"""
    def CleanUpNativeData(self, pNativeData: IntPtr) -> None:
        """"""
    def GetNativeDataSize(self) -> int:
        """"""
    def MarshalManagedToNative(self, ManagedObj: object) -> IntPtr:
        """"""
    def MarshalNativeToManaged(self, pNativeData: IntPtr) -> object:
        """"""

class ICustomQueryInterface:
    """"""
    def GetInterface(self, iid: Guid, ppv: IntPtr) -> tuple[CustomQueryInterfaceResult, IntPtr]:
        """"""

class IDLDESC(ValueType):
    """"""

    dwReserved: Final[int]
    """"""
    wIDLFlags: Final[IDLFLAG]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IDLFLAG(Enum):
    """"""

    IDLFLAG_NONE: IDLFLAG = ...
    """"""
    IDLFLAG_FIN: IDLFLAG = ...
    """"""
    IDLFLAG_FOUT: IDLFLAG = ...
    """"""
    IDLFLAG_FLCID: IDLFLAG = ...
    """"""
    IDLFLAG_FRETVAL: IDLFLAG = ...
    """"""

class IDispatchImplAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, implType: IDispatchImplType) -> None:
        """"""
    @overload
    def __init__(self, implType: int) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Value(self) -> IDispatchImplType:
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

class IDispatchImplType(Enum):
    """"""

    SystemDefinedImpl: IDispatchImplType = ...
    """"""
    InternalImpl: IDispatchImplType = ...
    """"""
    CompatibleImpl: IDispatchImplType = ...
    """"""

class IMPLTYPEFLAGS(Enum):
    """"""

    IMPLTYPEFLAG_FDEFAULT: IMPLTYPEFLAGS = ...
    """"""
    IMPLTYPEFLAG_FSOURCE: IMPLTYPEFLAGS = ...
    """"""
    IMPLTYPEFLAG_FRESTRICTED: IMPLTYPEFLAGS = ...
    """"""
    IMPLTYPEFLAG_FDEFAULTVTABLE: IMPLTYPEFLAGS = ...
    """"""

class INVOKEKIND(Enum):
    """"""

    INVOKE_FUNC: INVOKEKIND = ...
    """"""
    INVOKE_PROPERTYGET: INVOKEKIND = ...
    """"""
    INVOKE_PROPERTYPUT: INVOKEKIND = ...
    """"""
    INVOKE_PROPERTYPUTREF: INVOKEKIND = ...
    """"""

class IRegistrationServices:
    """"""
    def GetManagedCategoryGuid(self) -> Guid:
        """"""
    def GetProgIdForType(self, type: Type) -> str:
        """"""
    def GetRegistrableTypesInAssembly(self, assembly: Assembly) -> Array[Type]:
        """"""
    def RegisterAssembly(self, assembly: Assembly, flags: AssemblyRegistrationFlags) -> bool:
        """"""
    def RegisterTypeForComClients(self, type: Type, g: Guid) -> None:
        """"""
    def TypeRepresentsComType(self, type: Type) -> bool:
        """"""
    def TypeRequiresRegistration(self, type: Type) -> bool:
        """"""
    def UnregisterAssembly(self, assembly: Assembly) -> bool:
        """"""

class ITypeLibConverter:
    """"""
    def ConvertAssemblyToTypeLib(
        self,
        assembly: Assembly,
        typeLibName: str,
        flags: TypeLibExporterFlags,
        notifySink: ITypeLibExporterNotifySink,
    ) -> object:
        """"""
    @overload
    def ConvertTypeLibToAssembly(
        self,
        typeLib: object,
        asmFileName: str,
        flags: TypeLibImporterFlags,
        notifySink: ITypeLibImporterNotifySink,
        publicKey: Array[int],
        keyPair: StrongNameKeyPair,
        asmNamespace: str,
        asmVersion: Version,
    ) -> AssemblyBuilder:
        """"""
    @overload
    def ConvertTypeLibToAssembly(
        self,
        typeLib: object,
        asmFileName: str,
        flags: int,
        notifySink: ITypeLibImporterNotifySink,
        publicKey: Array[int],
        keyPair: StrongNameKeyPair,
        unsafeInterfaces: bool,
    ) -> AssemblyBuilder:
        """"""
    def GetPrimaryInteropAssembly(
        self, g: Guid, major: int, minor: int, lcid: int, asmName: String, asmCodeBase: String
    ) -> tuple[bool, String, String]:
        """"""

class ITypeLibExporterNameProvider:
    """"""
    def GetNames(self) -> Array[str]:
        """"""

class ITypeLibExporterNotifySink:
    """"""
    def ReportEvent(self, eventKind: ExporterEventKind, eventCode: int, eventMsg: str) -> None:
        """"""
    def ResolveRef(self, assembly: Assembly) -> object:
        """"""

class ITypeLibImporterNotifySink:
    """"""
    def ReportEvent(self, eventKind: ImporterEventKind, eventCode: int, eventMsg: str) -> None:
        """"""
    def ResolveRef(self, typeLib: object) -> Assembly:
        """"""

class ImportedFromTypeLibAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, tlbFile: str) -> None:
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

class ImporterCallback(Object, ITypeLibImporterNotifySink):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ReportEvent(self, EventKind: ImporterEventKind, EventCode: int, EventMsg: str) -> None:
        """"""
    def ResolveRef(self, TypeLib: object) -> Assembly:
        """"""
    def ToString(self) -> str:
        """"""

class ImporterEventKind(Enum):
    """"""

    NOTIF_TYPECONVERTED: ImporterEventKind = ...
    """"""
    NOTIF_CONVERTWARNING: ImporterEventKind = ...
    """"""
    ERROR_REFTOINVALIDTYPELIB: ImporterEventKind = ...
    """"""

class InAttribute(Attribute, _Attribute):
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

class InterfaceTypeAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, interfaceType: ComInterfaceType) -> None:
        """"""
    @overload
    def __init__(self, interfaceType: int) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Value(self) -> ComInterfaceType:
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

class InvalidComObjectException(SystemException, _Exception, ISerializable):
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

class InvalidOleVariantTypeException(SystemException, _Exception, ISerializable):
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

class LCIDConversionAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, lcid: int) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Value(self) -> int:
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

class LIBFLAGS(Enum):
    """"""

    LIBFLAG_FRESTRICTED: LIBFLAGS = ...
    """"""
    LIBFLAG_FCONTROL: LIBFLAGS = ...
    """"""
    LIBFLAG_FHIDDEN: LIBFLAGS = ...
    """"""
    LIBFLAG_FHASDISKIMAGE: LIBFLAGS = ...
    """"""

class LayoutKind(Enum):
    """"""

    Sequential: LayoutKind = ...
    """"""
    Explicit: LayoutKind = ...
    """"""
    Auto: LayoutKind = ...
    """"""

class ManagedToNativeComInteropStubAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, classType: Type, methodName: str) -> None:
        """"""
    @property
    def ClassType(self) -> Type:
        """"""
    @property
    def MethodName(self) -> str:
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

class Marshal(ABC, Object):
    """"""

    SystemDefaultCharSize: ClassVar[int]
    """"""
    SystemMaxDBCSCharSize: ClassVar[int]
    """"""
    @classmethod
    def AddRef(cls, pUnk: IntPtr) -> int:
        """"""
    @classmethod
    def AllocCoTaskMem(cls, cb: int) -> IntPtr:
        """"""
    @classmethod
    @overload
    def AllocHGlobal(cls, cb: int) -> IntPtr:
        """"""
    @classmethod
    @overload
    def AllocHGlobal(cls, cb: IntPtr) -> IntPtr:
        """"""
    @classmethod
    def AreComObjectsAvailableForCleanup(cls) -> bool:
        """"""
    @classmethod
    def BindToMoniker(cls, monikerName: str) -> object:
        """"""
    @classmethod
    def ChangeWrapperHandleStrength(cls, otp: object, fIsWeak: bool) -> None:
        """"""
    @classmethod
    def CleanupUnusedObjectsInCurrentContext(cls) -> None:
        """"""
    @classmethod
    @overload
    def Copy(cls, source: Array[int], startIndex: int, destination: IntPtr, length: int) -> None:
        """"""
    @classmethod
    @overload
    def Copy(cls, source: Array[Char], startIndex: int, destination: IntPtr, length: int) -> None:
        """"""
    @classmethod
    @overload
    def Copy(cls, source: Array[float], startIndex: int, destination: IntPtr, length: int) -> None:
        """"""
    @classmethod
    @overload
    def Copy(cls, source: Array[int], startIndex: int, destination: IntPtr, length: int) -> None:
        """"""
    @classmethod
    @overload
    def Copy(cls, source: Array[int], startIndex: int, destination: IntPtr, length: int) -> None:
        """"""
    @classmethod
    @overload
    def Copy(cls, source: Array[int], startIndex: int, destination: IntPtr, length: int) -> None:
        """"""
    @classmethod
    @overload
    def Copy(cls, source: Array[IntPtr], startIndex: int, destination: IntPtr, length: int) -> None:
        """"""
    @classmethod
    @overload
    def Copy(cls, source: Array[float], startIndex: int, destination: IntPtr, length: int) -> None:
        """"""
    @classmethod
    @overload
    def Copy(cls, source: IntPtr, destination: Array[int], startIndex: int, length: int) -> None:
        """"""
    @classmethod
    @overload
    def Copy(cls, source: IntPtr, destination: Array[Char], startIndex: int, length: int) -> None:
        """"""
    @classmethod
    @overload
    def Copy(cls, source: IntPtr, destination: Array[float], startIndex: int, length: int) -> None:
        """"""
    @classmethod
    @overload
    def Copy(cls, source: IntPtr, destination: Array[int], startIndex: int, length: int) -> None:
        """"""
    @classmethod
    @overload
    def Copy(cls, source: IntPtr, destination: Array[int], startIndex: int, length: int) -> None:
        """"""
    @classmethod
    @overload
    def Copy(cls, source: IntPtr, destination: Array[int], startIndex: int, length: int) -> None:
        """"""
    @classmethod
    @overload
    def Copy(cls, source: IntPtr, destination: Array[IntPtr], startIndex: int, length: int) -> None:
        """"""
    @classmethod
    @overload
    def Copy(cls, source: IntPtr, destination: Array[float], startIndex: int, length: int) -> None:
        """"""
    @classmethod
    @overload
    def CreateAggregatedObject[T](cls, pOuter: IntPtr, o: T) -> IntPtr:
        """"""
    @classmethod
    @overload
    def CreateAggregatedObject(cls, pOuter: IntPtr, o: object) -> IntPtr:
        """"""
    @classmethod
    @overload
    def CreateWrapperOfType[T, TWrapper](cls, o: T) -> TWrapper:
        """"""
    @classmethod
    @overload
    def CreateWrapperOfType(cls, o: object, t: Type) -> object:
        """"""
    @classmethod
    @overload
    def DestroyStructure(cls, ptr: IntPtr) -> None:
        """"""
    @classmethod
    @overload
    def DestroyStructure(cls, ptr: IntPtr, structuretype: Type) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FinalReleaseComObject(cls, o: object) -> int:
        """"""
    @classmethod
    def FreeBSTR(cls, ptr: IntPtr) -> None:
        """"""
    @classmethod
    def FreeCoTaskMem(cls, ptr: IntPtr) -> None:
        """"""
    @classmethod
    def FreeHGlobal(cls, hglobal: IntPtr) -> None:
        """"""
    @classmethod
    def GenerateGuidForType(cls, type: Type) -> Guid:
        """"""
    @classmethod
    def GenerateProgIdForType(cls, type: Type) -> str:
        """"""
    @classmethod
    def GetActiveObject(cls, progID: str) -> object:
        """"""
    @classmethod
    @overload
    def GetComInterfaceForObject[T](cls, o: T) -> IntPtr:
        """"""
    @classmethod
    @overload
    def GetComInterfaceForObject(cls, o: object, T: Type) -> IntPtr:
        """"""
    @classmethod
    @overload
    def GetComInterfaceForObject(cls, o: object, T: Type, mode: CustomQueryInterfaceMode) -> IntPtr:
        """"""
    @classmethod
    def GetComInterfaceForObjectInContext(cls, o: object, t: Type) -> IntPtr:
        """"""
    @classmethod
    def GetComObjectData(cls, obj: object, key: object) -> object:
        """"""
    @classmethod
    def GetComSlotForMethodInfo(cls, m: MemberInfo) -> int:
        """"""
    @classmethod
    @overload
    def GetDelegateForFunctionPointer[TDelegate](cls, ptr: IntPtr) -> TDelegate:
        """"""
    @classmethod
    @overload
    def GetDelegateForFunctionPointer(cls, ptr: IntPtr, t: Type) -> Delegate:
        """"""
    @classmethod
    def GetEndComSlot(cls, t: Type) -> int:
        """"""
    @classmethod
    def GetExceptionCode(cls) -> int:
        """"""
    @classmethod
    @overload
    def GetExceptionForHR(cls, errorCode: int) -> Exception:
        """"""
    @classmethod
    @overload
    def GetExceptionForHR(cls, errorCode: int, errorInfo: IntPtr) -> Exception:
        """"""
    @classmethod
    def GetExceptionPointers(cls) -> IntPtr:
        """"""
    @classmethod
    @overload
    def GetFunctionPointerForDelegate[TDelegate](cls, d: TDelegate) -> IntPtr:
        """"""
    @classmethod
    @overload
    def GetFunctionPointerForDelegate(cls, d: Delegate) -> IntPtr:
        """"""
    @classmethod
    def GetHINSTANCE(cls, m: Module) -> IntPtr:
        """"""
    @classmethod
    def GetHRForException(cls, e: Exception) -> int:
        """"""
    @classmethod
    def GetHRForLastWin32Error(cls) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetIDispatchForObject(cls, o: object) -> IntPtr:
        """"""
    @classmethod
    def GetIDispatchForObjectInContext(cls, o: object) -> IntPtr:
        """"""
    @classmethod
    def GetITypeInfoForType(cls, t: Type) -> IntPtr:
        """"""
    @classmethod
    def GetIUnknownForObject(cls, o: object) -> IntPtr:
        """"""
    @classmethod
    def GetIUnknownForObjectInContext(cls, o: object) -> IntPtr:
        """"""
    @classmethod
    def GetLastWin32Error(cls) -> int:
        """"""
    @classmethod
    def GetManagedThunkForUnmanagedMethodPtr(
        cls, pfnMethodToWrap: IntPtr, pbSignature: IntPtr, cbSignature: int
    ) -> IntPtr:
        """"""
    @classmethod
    def GetMethodInfoForComSlot(cls, t: Type, slot: int, memberType: ComMemberType) -> MemberInfo:
        """"""
    @classmethod
    @overload
    def GetNativeVariantForObject[T](cls, obj: T, pDstNativeVariant: IntPtr) -> None:
        """"""
    @classmethod
    @overload
    def GetNativeVariantForObject(cls, obj: object, pDstNativeVariant: IntPtr) -> None:
        """"""
    @classmethod
    def GetObjectForIUnknown(cls, pUnk: IntPtr) -> object:
        """"""
    @classmethod
    def GetObjectForNativeVariant[T](cls, pSrcNativeVariant: IntPtr) -> T:
        """"""
    @classmethod
    def GetObjectsForNativeVariants(cls, aSrcNativeVariant: IntPtr, cVars: int) -> Array[T]:
        """"""
    @classmethod
    def GetStartComSlot(cls, t: Type) -> int:
        """"""
    @classmethod
    def GetThreadFromFiberCookie(cls, cookie: int) -> Thread:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetTypeForITypeInfo(cls, piTypeInfo: IntPtr) -> Type:
        """"""
    @classmethod
    def GetTypeFromCLSID(cls, clsid: Guid) -> Type:
        """"""
    @classmethod
    @overload
    def GetTypeInfoName(cls, typeInfo: ITypeInfo) -> str:
        """"""
    @classmethod
    @overload
    def GetTypeInfoName(cls, pTI: UCOMITypeInfo) -> str:
        """"""
    @classmethod
    @overload
    def GetTypeLibGuid(cls, typelib: ITypeLib) -> Guid:
        """"""
    @classmethod
    @overload
    def GetTypeLibGuid(cls, pTLB: UCOMITypeLib) -> Guid:
        """"""
    @classmethod
    def GetTypeLibGuidForAssembly(cls, asm: Assembly) -> Guid:
        """"""
    @classmethod
    @overload
    def GetTypeLibLcid(cls, typelib: ITypeLib) -> int:
        """"""
    @classmethod
    @overload
    def GetTypeLibLcid(cls, pTLB: UCOMITypeLib) -> int:
        """"""
    @classmethod
    @overload
    def GetTypeLibName(cls, typelib: ITypeLib) -> str:
        """"""
    @classmethod
    @overload
    def GetTypeLibName(cls, pTLB: UCOMITypeLib) -> str:
        """"""
    @classmethod
    def GetTypeLibVersionForAssembly(
        cls, inputAssembly: Assembly, majorVersion: Int32, minorVersion: Int32
    ) -> tuple[None, Int32, Int32]:
        """"""
    @classmethod
    def GetTypedObjectForIUnknown(cls, pUnk: IntPtr, t: Type) -> object:
        """"""
    @classmethod
    def GetUniqueObjectForIUnknown(cls, unknown: IntPtr) -> object:
        """"""
    @classmethod
    def GetUnmanagedThunkForManagedMethodPtr(
        cls, pfnMethodToWrap: IntPtr, pbSignature: IntPtr, cbSignature: int
    ) -> IntPtr:
        """"""
    @classmethod
    def IsComObject(cls, o: object) -> bool:
        """"""
    @classmethod
    def IsTypeVisibleFromCom(cls, t: Type) -> bool:
        """"""
    @classmethod
    def NumParamBytes(cls, m: MethodInfo) -> int:
        """"""
    @classmethod
    @overload
    def OffsetOf(cls, fieldName: str) -> IntPtr:
        """"""
    @classmethod
    @overload
    def OffsetOf(cls, t: Type, fieldName: str) -> IntPtr:
        """"""
    @classmethod
    def Prelink(cls, m: MethodInfo) -> None:
        """"""
    @classmethod
    def PrelinkAll(cls, c: Type) -> None:
        """"""
    @classmethod
    @overload
    def PtrToStringAnsi(cls, ptr: IntPtr) -> str:
        """"""
    @classmethod
    @overload
    def PtrToStringAnsi(cls, ptr: IntPtr, len: int) -> str:
        """"""
    @classmethod
    @overload
    def PtrToStringAuto(cls, ptr: IntPtr) -> str:
        """"""
    @classmethod
    @overload
    def PtrToStringAuto(cls, ptr: IntPtr, len: int) -> str:
        """"""
    @classmethod
    def PtrToStringBSTR(cls, ptr: IntPtr) -> str:
        """"""
    @classmethod
    @overload
    def PtrToStringUni(cls, ptr: IntPtr) -> str:
        """"""
    @classmethod
    @overload
    def PtrToStringUni(cls, ptr: IntPtr, len: int) -> str:
        """"""
    @classmethod
    @overload
    def PtrToStructure[T](cls, ptr: IntPtr) -> T:
        """"""
    @classmethod
    @overload
    def PtrToStructure[T](cls, ptr: IntPtr, structure: T) -> None:
        """"""
    @classmethod
    @overload
    def PtrToStructure(cls, ptr: IntPtr, structure: object) -> None:
        """"""
    @classmethod
    @overload
    def PtrToStructure(cls, ptr: IntPtr, structureType: Type) -> object:
        """"""
    @classmethod
    def QueryInterface(cls, pUnk: IntPtr, iid: Guid, ppv: IntPtr) -> tuple[int, IntPtr]:
        """"""
    @classmethod
    def ReAllocCoTaskMem(cls, pv: IntPtr, cb: int) -> IntPtr:
        """"""
    @classmethod
    def ReAllocHGlobal(cls, pv: IntPtr, cb: IntPtr) -> IntPtr:
        """"""
    @classmethod
    @overload
    def ReadByte(cls, ptr: IntPtr) -> int:
        """"""
    @classmethod
    @overload
    def ReadByte(cls, ptr: IntPtr, ofs: int) -> int:
        """"""
    @classmethod
    @overload
    def ReadByte(cls, ptr: object, ofs: int) -> int:
        """"""
    @classmethod
    @overload
    def ReadInt16(cls, ptr: IntPtr) -> int:
        """"""
    @classmethod
    @overload
    def ReadInt16(cls, ptr: IntPtr, ofs: int) -> int:
        """"""
    @classmethod
    @overload
    def ReadInt16(cls, ptr: object, ofs: int) -> int:
        """"""
    @classmethod
    @overload
    def ReadInt32(cls, ptr: IntPtr) -> int:
        """"""
    @classmethod
    @overload
    def ReadInt32(cls, ptr: IntPtr, ofs: int) -> int:
        """"""
    @classmethod
    @overload
    def ReadInt32(cls, ptr: object, ofs: int) -> int:
        """"""
    @classmethod
    @overload
    def ReadInt64(cls, ptr: IntPtr) -> int:
        """"""
    @classmethod
    @overload
    def ReadInt64(cls, ptr: IntPtr, ofs: int) -> int:
        """"""
    @classmethod
    @overload
    def ReadInt64(cls, ptr: object, ofs: int) -> int:
        """"""
    @classmethod
    @overload
    def ReadIntPtr(cls, ptr: IntPtr) -> IntPtr:
        """"""
    @classmethod
    @overload
    def ReadIntPtr(cls, ptr: IntPtr, ofs: int) -> IntPtr:
        """"""
    @classmethod
    @overload
    def ReadIntPtr(cls, ptr: object, ofs: int) -> IntPtr:
        """"""
    @classmethod
    def Release(cls, pUnk: IntPtr) -> int:
        """"""
    @classmethod
    def ReleaseComObject(cls, o: object) -> int:
        """"""
    @classmethod
    def ReleaseThreadCache(cls) -> None:
        """"""
    @classmethod
    def SecureStringToBSTR(cls, s: SecureString) -> IntPtr:
        """"""
    @classmethod
    def SecureStringToCoTaskMemAnsi(cls, s: SecureString) -> IntPtr:
        """"""
    @classmethod
    def SecureStringToCoTaskMemUnicode(cls, s: SecureString) -> IntPtr:
        """"""
    @classmethod
    def SecureStringToGlobalAllocAnsi(cls, s: SecureString) -> IntPtr:
        """"""
    @classmethod
    def SecureStringToGlobalAllocUnicode(cls, s: SecureString) -> IntPtr:
        """"""
    @classmethod
    def SetComObjectData(cls, obj: object, key: object, data: object) -> bool:
        """"""
    @classmethod
    @overload
    def SizeOf[T](cls, structure: T) -> int:
        """"""
    @classmethod
    @overload
    def SizeOf(cls) -> int:
        """"""
    @classmethod
    @overload
    def SizeOf(cls, structure: object) -> int:
        """"""
    @classmethod
    @overload
    def SizeOf(cls, t: Type) -> int:
        """"""
    @classmethod
    def StringToBSTR(cls, s: str) -> IntPtr:
        """"""
    @classmethod
    def StringToCoTaskMemAnsi(cls, s: str) -> IntPtr:
        """"""
    @classmethod
    def StringToCoTaskMemAuto(cls, s: str) -> IntPtr:
        """"""
    @classmethod
    def StringToCoTaskMemUni(cls, s: str) -> IntPtr:
        """"""
    @classmethod
    def StringToHGlobalAnsi(cls, s: str) -> IntPtr:
        """"""
    @classmethod
    def StringToHGlobalAuto(cls, s: str) -> IntPtr:
        """"""
    @classmethod
    def StringToHGlobalUni(cls, s: str) -> IntPtr:
        """"""
    @classmethod
    @overload
    def StructureToPtr[T](cls, structure: T, ptr: IntPtr, fDeleteOld: bool) -> None:
        """"""
    @classmethod
    @overload
    def StructureToPtr(cls, structure: object, ptr: IntPtr, fDeleteOld: bool) -> None:
        """"""
    @classmethod
    @overload
    def ThrowExceptionForHR(cls, errorCode: int) -> None:
        """"""
    @classmethod
    @overload
    def ThrowExceptionForHR(cls, errorCode: int, errorInfo: IntPtr) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def UnsafeAddrOfPinnedArrayElement(cls, arr: Array, index: int) -> IntPtr:
        """"""
    @classmethod
    @overload
    def UnsafeAddrOfPinnedArrayElement(cls, arr: Array[T], index: int) -> IntPtr:
        """"""
    @classmethod
    @overload
    def WriteByte(cls, ptr: IntPtr, val: int) -> None:
        """"""
    @classmethod
    @overload
    def WriteByte(cls, ptr: IntPtr, ofs: int, val: int) -> None:
        """"""
    @classmethod
    @overload
    def WriteByte(cls, ptr: object, ofs: int, val: int) -> tuple[None, object]:
        """"""
    @classmethod
    @overload
    def WriteInt16(cls, ptr: IntPtr, val: Char) -> None:
        """"""
    @classmethod
    @overload
    def WriteInt16(cls, ptr: IntPtr, val: int) -> None:
        """"""
    @classmethod
    @overload
    def WriteInt16(cls, ptr: IntPtr, ofs: int, val: Char) -> None:
        """"""
    @classmethod
    @overload
    def WriteInt16(cls, ptr: IntPtr, ofs: int, val: int) -> None:
        """"""
    @classmethod
    @overload
    def WriteInt16(cls, ptr: object, ofs: int, val: Char) -> tuple[None, object]:
        """"""
    @classmethod
    @overload
    def WriteInt16(cls, ptr: object, ofs: int, val: int) -> tuple[None, object]:
        """"""
    @classmethod
    @overload
    def WriteInt32(cls, ptr: IntPtr, val: int) -> None:
        """"""
    @classmethod
    @overload
    def WriteInt32(cls, ptr: IntPtr, ofs: int, val: int) -> None:
        """"""
    @classmethod
    @overload
    def WriteInt32(cls, ptr: object, ofs: int, val: int) -> tuple[None, object]:
        """"""
    @classmethod
    @overload
    def WriteInt64(cls, ptr: IntPtr, ofs: int, val: int) -> None:
        """"""
    @classmethod
    @overload
    def WriteInt64(cls, ptr: IntPtr, val: int) -> None:
        """"""
    @classmethod
    @overload
    def WriteInt64(cls, ptr: object, ofs: int, val: int) -> tuple[None, object]:
        """"""
    @classmethod
    @overload
    def WriteIntPtr(cls, ptr: IntPtr, ofs: int, val: IntPtr) -> None:
        """"""
    @classmethod
    @overload
    def WriteIntPtr(cls, ptr: IntPtr, val: IntPtr) -> None:
        """"""
    @classmethod
    @overload
    def WriteIntPtr(cls, ptr: object, ofs: int, val: IntPtr) -> tuple[None, object]:
        """"""
    @classmethod
    def ZeroFreeBSTR(cls, s: IntPtr) -> None:
        """"""
    @classmethod
    def ZeroFreeCoTaskMemAnsi(cls, s: IntPtr) -> None:
        """"""
    @classmethod
    def ZeroFreeCoTaskMemUnicode(cls, s: IntPtr) -> None:
        """"""
    @classmethod
    def ZeroFreeGlobalAllocAnsi(cls, s: IntPtr) -> None:
        """"""
    @classmethod
    def ZeroFreeGlobalAllocUnicode(cls, s: IntPtr) -> None:
        """"""

class MarshalAsAttribute(Attribute, _Attribute):
    """"""

    ArraySubType: Final[UnmanagedType]
    """"""
    IidParameterIndex: Final[int]
    """"""
    MarshalCookie: Final[str]
    """"""
    MarshalType: Final[str]
    """"""
    MarshalTypeRef: Final[Type]
    """"""
    SafeArraySubType: Final[VarEnum]
    """"""
    SafeArrayUserDefinedSubType: Final[Type]
    """"""
    SizeConst: Final[int]
    """"""
    SizeParamIndex: Final[int]
    """"""
    @overload
    def __init__(self, unmanagedType: UnmanagedType) -> None:
        """"""
    @overload
    def __init__(self, unmanagedType: int) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Value(self) -> UnmanagedType:
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

class MarshalDirectiveException(SystemException, _Exception, ISerializable):
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

class NativeBuffer(Object, IDisposable):
    """"""
    def __init__(self, initialMinCapacity: int = ...) -> None:
        """"""
    @property
    def ByteCapacity(self) -> int:
        """"""
    @property
    def Item(self) -> int:
        """"""
    @Item.setter
    def Item(self, value: int) -> None: ...
    def Dispose(self) -> None:
        """"""
    def EnsureByteCapacity(self, minCapacity: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Free(self) -> None:
        """"""
    def GetHandle(self) -> SafeHandle:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __getitem__(self, index: int) -> int:
        """"""
    def __setitem__(self, index: int, value: int) -> None:
        """"""

class NativeMethods(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class OSPlatform(ValueType, IEquatable[OSPlatform]):
    """"""
    @classmethod
    @property
    def Linux(cls) -> OSPlatform:
        """"""
    @classmethod
    @property
    def OSX(cls) -> OSPlatform:
        """"""
    @classmethod
    @property
    def Windows(cls) -> OSPlatform:
        """"""
    @classmethod
    def Create(cls, osPlatform: str) -> OSPlatform:
        """"""
    @overload
    def Equals(self, other: OSPlatform) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: OSPlatform, right: OSPlatform) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: OSPlatform, right: OSPlatform) -> bool:
        """"""
    def __eq__(self, other: OSPlatform) -> bool:
        """"""
    def __ne__(self, other: OSPlatform) -> bool:
        """"""

ObjectCreationDelegate: Callable[[IntPtr], IntPtr] = ...
""""""

class OptionalAttribute(Attribute, _Attribute):
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

class OutAttribute(Attribute, _Attribute):
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

class PARAMDESC(ValueType):
    """"""

    lpVarValue: Final[IntPtr]
    """"""
    wParamFlags: Final[PARAMFLAG]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PARAMFLAG(Enum):
    """"""

    PARAMFLAG_NONE: PARAMFLAG = ...
    """"""
    PARAMFLAG_FIN: PARAMFLAG = ...
    """"""
    PARAMFLAG_FOUT: PARAMFLAG = ...
    """"""
    PARAMFLAG_FLCID: PARAMFLAG = ...
    """"""
    PARAMFLAG_FRETVAL: PARAMFLAG = ...
    """"""
    PARAMFLAG_FOPT: PARAMFLAG = ...
    """"""
    PARAMFLAG_FHASDEFAULT: PARAMFLAG = ...
    """"""
    PARAMFLAG_FHASCUSTDATA: PARAMFLAG = ...
    """"""

class PInvokeMap(Enum):
    """"""

    CharSetNotSpec: PInvokeMap = ...
    """"""
    NoMangle: PInvokeMap = ...
    """"""
    CharSetAnsi: PInvokeMap = ...
    """"""
    CharSetUnicode: PInvokeMap = ...
    """"""
    CharSetAuto: PInvokeMap = ...
    """"""
    CharSetMask: PInvokeMap = ...
    """"""
    BestFitEnabled: PInvokeMap = ...
    """"""
    BestFitDisabled: PInvokeMap = ...
    """"""
    PinvokeOLE: PInvokeMap = ...
    """"""
    BestFitMask: PInvokeMap = ...
    """"""
    BestFitUseAsm: PInvokeMap = ...
    """"""
    SupportsLastError: PInvokeMap = ...
    """"""
    CallConvWinapi: PInvokeMap = ...
    """"""
    CallConvCdecl: PInvokeMap = ...
    """"""
    CallConvStdcall: PInvokeMap = ...
    """"""
    CallConvThiscall: PInvokeMap = ...
    """"""
    CallConvFastcall: PInvokeMap = ...
    """"""
    CallConvMask: PInvokeMap = ...
    """"""
    ThrowOnUnmappableCharEnabled: PInvokeMap = ...
    """"""
    ThrowOnUnmappableCharDisabled: PInvokeMap = ...
    """"""
    ThrowOnUnmappableCharMask: PInvokeMap = ...
    """"""
    ThrowOnUnmappableCharUseAsm: PInvokeMap = ...
    """"""

class PreserveSigAttribute(Attribute, _Attribute):
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

class PrimaryInteropAssemblyAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, major: int, minor: int) -> None:
        """"""
    @property
    def MajorVersion(self) -> int:
        """"""
    @property
    def MinorVersion(self) -> int:
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

class ProgIdAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, progId: str) -> None:
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

class RegistrationClassContext(Enum):
    """"""

    InProcessServer: RegistrationClassContext = ...
    """"""
    InProcessHandler: RegistrationClassContext = ...
    """"""
    LocalServer: RegistrationClassContext = ...
    """"""
    InProcessServer16: RegistrationClassContext = ...
    """"""
    RemoteServer: RegistrationClassContext = ...
    """"""
    InProcessHandler16: RegistrationClassContext = ...
    """"""
    Reserved1: RegistrationClassContext = ...
    """"""
    Reserved2: RegistrationClassContext = ...
    """"""
    Reserved3: RegistrationClassContext = ...
    """"""
    Reserved4: RegistrationClassContext = ...
    """"""
    NoCodeDownload: RegistrationClassContext = ...
    """"""
    Reserved5: RegistrationClassContext = ...
    """"""
    NoCustomMarshal: RegistrationClassContext = ...
    """"""
    EnableCodeDownload: RegistrationClassContext = ...
    """"""
    NoFailureLog: RegistrationClassContext = ...
    """"""
    DisableActivateAsActivator: RegistrationClassContext = ...
    """"""
    EnableActivateAsActivator: RegistrationClassContext = ...
    """"""
    FromDefaultContext: RegistrationClassContext = ...
    """"""

class RegistrationConnectionType(Enum):
    """"""

    SingleUse: RegistrationConnectionType = ...
    """"""
    MultipleUse: RegistrationConnectionType = ...
    """"""
    MultiSeparate: RegistrationConnectionType = ...
    """"""
    Suspended: RegistrationConnectionType = ...
    """"""
    Surrogate: RegistrationConnectionType = ...
    """"""

class RegistrationServices(Object, IRegistrationServices):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetManagedCategoryGuid(self) -> Guid:
        """"""
    def GetProgIdForType(self, type: Type) -> str:
        """"""
    def GetRegistrableTypesInAssembly(self, assembly: Assembly) -> Array[Type]:
        """"""
    def GetType(self) -> Type:
        """"""
    def RegisterAssembly(self, assembly: Assembly, flags: AssemblyRegistrationFlags) -> bool:
        """"""
    @overload
    def RegisterTypeForComClients(
        self, type: Type, classContext: RegistrationClassContext, flags: RegistrationConnectionType
    ) -> int:
        """"""
    @overload
    def RegisterTypeForComClients(self, type: Type, g: Guid) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TypeRepresentsComType(self, type: Type) -> bool:
        """"""
    def TypeRequiresRegistration(self, type: Type) -> bool:
        """"""
    def UnregisterAssembly(self, assembly: Assembly) -> bool:
        """"""
    def UnregisterTypeForComClients(self, cookie: int) -> None:
        """"""

class RuntimeEnvironment(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @classmethod
    @property
    def SystemConfigurationFile(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FromGlobalAccessCache(cls, a: Assembly) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetRuntimeDirectory(cls) -> str:
        """"""
    @classmethod
    def GetRuntimeInterfaceAsIntPtr(cls, clsid: Guid, riid: Guid) -> IntPtr:
        """"""
    @classmethod
    def GetRuntimeInterfaceAsObject(cls, clsid: Guid, riid: Guid) -> object:
        """"""
    @classmethod
    def GetSystemVersion(cls) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RuntimeInformation(ABC, Object):
    """"""
    @classmethod
    @property
    def FrameworkDescription(cls) -> str:
        """"""
    @classmethod
    @property
    def OSArchitecture(cls) -> Architecture:
        """"""
    @classmethod
    @property
    def OSDescription(cls) -> str:
        """"""
    @classmethod
    @property
    def ProcessArchitecture(cls) -> Architecture:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsOSPlatform(cls, osPlatform: OSPlatform) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SEHException(ExternalException, _Exception, ISerializable):
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
    def ErrorCode(self) -> int:
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
    def CanResume(self) -> bool:
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

class STATSTG(ValueType):
    """"""

    atime: Final[FILETIME]
    """"""
    cbSize: Final[int]
    """"""
    clsid: Final[Guid]
    """"""
    ctime: Final[FILETIME]
    """"""
    grfLocksSupported: Final[int]
    """"""
    grfMode: Final[int]
    """"""
    grfStateBits: Final[int]
    """"""
    mtime: Final[FILETIME]
    """"""
    pwcsName: Final[str]
    """"""
    reserved: Final[int]
    """"""
    type: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SYSKIND(Enum):
    """"""

    SYS_WIN16: SYSKIND = ...
    """"""
    SYS_WIN32: SYSKIND = ...
    """"""
    SYS_MAC: SYSKIND = ...
    """"""

class SafeArrayRankMismatchException(SystemException, _Exception, ISerializable):
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

class SafeArrayTypeMismatchException(SystemException, _Exception, ISerializable):
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

class SafeBuffer(ABC, SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    @property
    def ByteLength(self) -> int:
        """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def AcquirePointer(self, pointer: Byte) -> None:
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
    @overload
    def Initialize(self, numElements: int) -> None:
        """"""
    @overload
    def Initialize(self, numElements: int, sizeOfEachElement: int) -> None:
        """"""
    @overload
    def Initialize(self, numBytes: int) -> None:
        """"""
    def Read[T](self, byteOffset: int) -> T:
        """"""
    def ReadArray(self, byteOffset: int, array: Array[T], index: int, count: int) -> None:
        """"""
    def ReleasePointer(self) -> None:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write[T](self, byteOffset: int, value: T) -> None:
        """"""
    def WriteArray(self, byteOffset: int, array: Array[T], index: int, count: int) -> None:
        """"""

class SafeHandle(ABC, CriticalFinalizerObject, IDisposable):
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

class SafeHeapHandle(SafeBuffer, IDisposable):
    """"""
    def __init__(self, byteLength: int) -> None:
        """"""
    @property
    def ByteLength(self) -> int:
        """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def AcquirePointer(self, pointer: Byte) -> None:
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
    @overload
    def Initialize(self, numElements: int) -> None:
        """"""
    @overload
    def Initialize(self, numElements: int, sizeOfEachElement: int) -> None:
        """"""
    @overload
    def Initialize(self, numBytes: int) -> None:
        """"""
    def Read[T](self, byteOffset: int) -> T:
        """"""
    def ReadArray(self, byteOffset: int, array: Array[T], index: int, count: int) -> None:
        """"""
    def ReleasePointer(self) -> None:
        """"""
    def Resize(self, byteLength: int) -> None:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write[T](self, byteOffset: int, value: T) -> None:
        """"""
    def WriteArray(self, byteOffset: int, array: Array[T], index: int, count: int) -> None:
        """"""

class SafeHeapHandleCache(Object, IDisposable):
    """"""
    def __init__(self, minSize: int = ..., maxSize: int = ..., maxHandles: int = ...) -> None:
        """"""
    def Acquire(self, minSize: int = ...) -> SafeHeapHandle:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Release(self, handle: SafeHeapHandle) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SetWin32ContextInIDispatchAttribute(Attribute, _Attribute):
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

class StandardOleMarshalObject(MarshalByRefObject, UnsafeNativeMethods.IMarshal):
    """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def DisconnectObject(self, dwReserved: int) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetMarshalSizeMax(
        self,
        riid: Guid,
        pv: IntPtr,
        dwDestContext: int,
        pvDestContext: IntPtr,
        mshlflags: int,
        pSize: Int32,
    ) -> tuple[int, Int32]:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUnmarshalClass(
        self,
        riid: Guid,
        pv: IntPtr,
        dwDestContext: int,
        pvDestContext: IntPtr,
        mshlflags: int,
        pCid: Guid,
    ) -> tuple[int, Guid]:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def MarshalInterface(
        self,
        pStm: IntPtr,
        riid: Guid,
        pv: IntPtr,
        dwDestContext: int,
        pvDestContext: IntPtr,
        mshlflags: int,
    ) -> int:
        """"""
    def ReleaseMarshalData(self, pStm: IntPtr) -> int:
        """"""
    def ToString(self) -> str:
        """"""
    def UnmarshalInterface(self, pStm: IntPtr, riid: Guid, ppv: IntPtr) -> tuple[int, IntPtr]:
        """"""

class StringBuffer(NativeBuffer, IDisposable):
    """"""
    @overload
    def __init__(self, initialCapacity: int = ...) -> None:
        """"""
    @overload
    def __init__(self, initialContents: str) -> None:
        """"""
    @overload
    def __init__(self, initialContents: StringBuffer) -> None:
        """"""
    @property
    def ByteCapacity(self) -> int:
        """"""
    @property
    def CharCapacity(self) -> int:
        """"""
    @property
    def Item(self) -> int:
        """"""
    @Item.setter
    def Item(self, value: int) -> None: ...
    @property
    def Length(self) -> int:
        """"""
    @Length.setter
    def Length(self, value: int) -> None: ...
    @overload
    def Append(self, value: StringBuffer, startIndex: int = ...) -> None:
        """"""
    @overload
    def Append(self, value: StringBuffer, startIndex: int, count: int) -> None:
        """"""
    @overload
    def Append(self, value: str, startIndex: int = ..., count: int = ...) -> None:
        """"""
    def Contains(self, value: Char) -> bool:
        """"""
    def CopyFrom(
        self, bufferIndex: int, source: str, sourceIndex: int = ..., count: int = ...
    ) -> None:
        """"""
    def CopyTo(
        self, bufferIndex: int, destination: StringBuffer, destinationIndex: int, count: int
    ) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def EnsureByteCapacity(self, minCapacity: int) -> None:
        """"""
    def EnsureCharCapacity(self, minCapacity: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Free(self) -> None:
        """"""
    def GetHandle(self) -> SafeHandle:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetLengthToFirstNull(self) -> None:
        """"""
    def StartsWith(self, value: str) -> bool:
        """"""
    def Substring(self, startIndex: int, count: int = ...) -> str:
        """"""
    def SubstringEquals(self, value: str, startIndex: int = ..., count: int = ...) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def TrimEnd(self, values: Array[Char]) -> None:
        """"""
    def __contains__(self, value: Char) -> bool:
        """"""
    @overload
    def __getitem__(self, index: int) -> Char:
        """"""
    @overload
    def __getitem__(self, index: int) -> int:
        """"""
    @overload
    def __setitem__(self, index: int, value: Char) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: int) -> None:
        """"""

class StructLayoutAttribute(Attribute, _Attribute):
    """"""

    CharSet: Final[CharSet]
    """"""
    Pack: Final[int]
    """"""
    Size: Final[int]
    """"""
    @overload
    def __init__(self, layoutKind: LayoutKind) -> None:
        """"""
    @overload
    def __init__(self, layoutKind: int) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Value(self) -> LayoutKind:
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

class TYPEATTR(ValueType):
    """"""

    MEMBER_ID_NIL: ClassVar[int]
    """"""
    cFuncs: Final[int]
    """"""
    cImplTypes: Final[int]
    """"""
    cVars: Final[int]
    """"""
    cbAlignment: Final[int]
    """"""
    cbSizeInstance: Final[int]
    """"""
    cbSizeVft: Final[int]
    """"""
    dwReserved: Final[int]
    """"""
    guid: Final[Guid]
    """"""
    idldescType: Final[IDLDESC]
    """"""
    lcid: Final[int]
    """"""
    lpstrSchema: Final[IntPtr]
    """"""
    memidConstructor: Final[int]
    """"""
    memidDestructor: Final[int]
    """"""
    tdescAlias: Final[TYPEDESC]
    """"""
    typekind: Final[TYPEKIND]
    """"""
    wMajorVerNum: Final[int]
    """"""
    wMinorVerNum: Final[int]
    """"""
    wTypeFlags: Final[TYPEFLAGS]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TYPEDESC(ValueType):
    """"""

    lpValue: Final[IntPtr]
    """"""
    vt: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TYPEFLAGS(Enum):
    """"""

    TYPEFLAG_FAPPOBJECT: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FCANCREATE: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FLICENSED: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FPREDECLID: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FHIDDEN: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FCONTROL: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FDUAL: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FNONEXTENSIBLE: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FOLEAUTOMATION: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FRESTRICTED: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FAGGREGATABLE: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FREPLACEABLE: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FDISPATCHABLE: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FREVERSEBIND: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FPROXY: TYPEFLAGS = ...
    """"""

class TYPEKIND(Enum):
    """"""

    TKIND_ENUM: TYPEKIND = ...
    """"""
    TKIND_RECORD: TYPEKIND = ...
    """"""
    TKIND_MODULE: TYPEKIND = ...
    """"""
    TKIND_INTERFACE: TYPEKIND = ...
    """"""
    TKIND_DISPATCH: TYPEKIND = ...
    """"""
    TKIND_COCLASS: TYPEKIND = ...
    """"""
    TKIND_ALIAS: TYPEKIND = ...
    """"""
    TKIND_UNION: TYPEKIND = ...
    """"""
    TKIND_MAX: TYPEKIND = ...
    """"""

class TYPELIBATTR(ValueType):
    """"""

    guid: Final[Guid]
    """"""
    lcid: Final[int]
    """"""
    syskind: Final[SYSKIND]
    """"""
    wLibFlags: Final[LIBFLAGS]
    """"""
    wMajorVerNum: Final[int]
    """"""
    wMinorVerNum: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TypeIdentifierAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, scope: str, identifier: str) -> None:
        """"""
    @property
    def Identifier(self) -> str:
        """"""
    @property
    def Scope(self) -> str:
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

class TypeLibConverter(Object, ITypeLibConverter):
    """"""
    def __init__(self) -> None:
        """"""
    def ConvertAssemblyToTypeLib(
        self,
        assembly: Assembly,
        strTypeLibName: str,
        flags: TypeLibExporterFlags,
        notifySink: ITypeLibExporterNotifySink,
    ) -> object:
        """"""
    @overload
    def ConvertTypeLibToAssembly(
        self,
        typeLib: object,
        asmFileName: str,
        flags: TypeLibImporterFlags,
        notifySink: ITypeLibImporterNotifySink,
        publicKey: Array[int],
        keyPair: StrongNameKeyPair,
        asmNamespace: str,
        asmVersion: Version,
    ) -> AssemblyBuilder:
        """"""
    @overload
    def ConvertTypeLibToAssembly(
        self,
        typeLib: object,
        asmFileName: str,
        flags: int,
        notifySink: ITypeLibImporterNotifySink,
        publicKey: Array[int],
        keyPair: StrongNameKeyPair,
        unsafeInterfaces: bool,
    ) -> AssemblyBuilder:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetPrimaryInteropAssembly(
        self, g: Guid, major: int, minor: int, lcid: int, asmName: String, asmCodeBase: String
    ) -> tuple[bool, String, String]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TypeLibExporterFlags(Enum):
    """"""

    _None: TypeLibExporterFlags = ...
    """"""
    OnlyReferenceRegistered: TypeLibExporterFlags = ...
    """"""
    CallerResolvedReferences: TypeLibExporterFlags = ...
    """"""
    OldNames: TypeLibExporterFlags = ...
    """"""
    ExportAs32Bit: TypeLibExporterFlags = ...
    """"""
    ExportAs64Bit: TypeLibExporterFlags = ...
    """"""

class TypeLibFuncAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, flags: TypeLibFuncFlags) -> None:
        """"""
    @overload
    def __init__(self, flags: int) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Value(self) -> TypeLibFuncFlags:
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

class TypeLibFuncFlags(Enum):
    """"""

    FRestricted: TypeLibFuncFlags = ...
    """"""
    FSource: TypeLibFuncFlags = ...
    """"""
    FBindable: TypeLibFuncFlags = ...
    """"""
    FRequestEdit: TypeLibFuncFlags = ...
    """"""
    FDisplayBind: TypeLibFuncFlags = ...
    """"""
    FDefaultBind: TypeLibFuncFlags = ...
    """"""
    FHidden: TypeLibFuncFlags = ...
    """"""
    FUsesGetLastError: TypeLibFuncFlags = ...
    """"""
    FDefaultCollelem: TypeLibFuncFlags = ...
    """"""
    FUiDefault: TypeLibFuncFlags = ...
    """"""
    FNonBrowsable: TypeLibFuncFlags = ...
    """"""
    FReplaceable: TypeLibFuncFlags = ...
    """"""
    FImmediateBind: TypeLibFuncFlags = ...
    """"""

class TypeLibImportClassAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, importClass: Type) -> None:
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

class TypeLibImporterFlags(Enum):
    """"""

    _None: TypeLibImporterFlags = ...
    """"""
    PrimaryInteropAssembly: TypeLibImporterFlags = ...
    """"""
    UnsafeInterfaces: TypeLibImporterFlags = ...
    """"""
    SafeArrayAsSystemArray: TypeLibImporterFlags = ...
    """"""
    TransformDispRetVals: TypeLibImporterFlags = ...
    """"""
    PreventClassMembers: TypeLibImporterFlags = ...
    """"""
    SerializableValueClasses: TypeLibImporterFlags = ...
    """"""
    ImportAsX86: TypeLibImporterFlags = ...
    """"""
    ImportAsX64: TypeLibImporterFlags = ...
    """"""
    ImportAsItanium: TypeLibImporterFlags = ...
    """"""
    ImportAsAgnostic: TypeLibImporterFlags = ...
    """"""
    ReflectionOnlyLoading: TypeLibImporterFlags = ...
    """"""
    NoDefineVersionResource: TypeLibImporterFlags = ...
    """"""
    ImportAsArm: TypeLibImporterFlags = ...
    """"""

class TypeLibTypeAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, flags: TypeLibTypeFlags) -> None:
        """"""
    @overload
    def __init__(self, flags: int) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Value(self) -> TypeLibTypeFlags:
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

class TypeLibTypeFlags(Enum):
    """"""

    FAppObject: TypeLibTypeFlags = ...
    """"""
    FCanCreate: TypeLibTypeFlags = ...
    """"""
    FLicensed: TypeLibTypeFlags = ...
    """"""
    FPreDeclId: TypeLibTypeFlags = ...
    """"""
    FHidden: TypeLibTypeFlags = ...
    """"""
    FControl: TypeLibTypeFlags = ...
    """"""
    FDual: TypeLibTypeFlags = ...
    """"""
    FNonExtensible: TypeLibTypeFlags = ...
    """"""
    FOleAutomation: TypeLibTypeFlags = ...
    """"""
    FRestricted: TypeLibTypeFlags = ...
    """"""
    FAggregatable: TypeLibTypeFlags = ...
    """"""
    FReplaceable: TypeLibTypeFlags = ...
    """"""
    FDispatchable: TypeLibTypeFlags = ...
    """"""
    FReverseBind: TypeLibTypeFlags = ...
    """"""

class TypeLibVarAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, flags: TypeLibVarFlags) -> None:
        """"""
    @overload
    def __init__(self, flags: int) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Value(self) -> TypeLibVarFlags:
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

class TypeLibVarFlags(Enum):
    """"""

    FReadOnly: TypeLibVarFlags = ...
    """"""
    FSource: TypeLibVarFlags = ...
    """"""
    FBindable: TypeLibVarFlags = ...
    """"""
    FRequestEdit: TypeLibVarFlags = ...
    """"""
    FDisplayBind: TypeLibVarFlags = ...
    """"""
    FDefaultBind: TypeLibVarFlags = ...
    """"""
    FHidden: TypeLibVarFlags = ...
    """"""
    FRestricted: TypeLibVarFlags = ...
    """"""
    FDefaultCollelem: TypeLibVarFlags = ...
    """"""
    FUiDefault: TypeLibVarFlags = ...
    """"""
    FNonBrowsable: TypeLibVarFlags = ...
    """"""
    FReplaceable: TypeLibVarFlags = ...
    """"""
    FImmediateBind: TypeLibVarFlags = ...
    """"""

class TypeLibVersionAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, major: int, minor: int) -> None:
        """"""
    @property
    def MajorVersion(self) -> int:
        """"""
    @property
    def MinorVersion(self) -> int:
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

class UCOMIBindCtx:
    """"""
    def EnumObjectParam(self, ppenum: UCOMIEnumString) -> tuple[None, UCOMIEnumString]:
        """"""
    def GetBindOptions(self, pbindopts: BIND_OPTS) -> None:
        """"""
    def GetObjectParam(self, pszKey: str, ppunk: Object) -> tuple[None, Object]:
        """"""
    def GetRunningObjectTable(
        self, pprot: UCOMIRunningObjectTable
    ) -> tuple[None, UCOMIRunningObjectTable]:
        """"""
    def RegisterObjectBound(self, punk: object) -> None:
        """"""
    def RegisterObjectParam(self, pszKey: str, punk: object) -> None:
        """"""
    def ReleaseBoundObjects(self) -> None:
        """"""
    def RevokeObjectBound(self, punk: object) -> None:
        """"""
    def RevokeObjectParam(self, pszKey: str) -> None:
        """"""
    def SetBindOptions(self, pbindopts: BIND_OPTS) -> None:
        """"""

class UCOMIConnectionPoint:
    """"""
    def Advise(self, pUnkSink: object, pdwCookie: Int32) -> tuple[None, Int32]:
        """"""
    def EnumConnections(self, ppEnum: UCOMIEnumConnections) -> tuple[None, UCOMIEnumConnections]:
        """"""
    def GetConnectionInterface(self, pIID: Guid) -> tuple[None, Guid]:
        """"""
    def GetConnectionPointContainer(
        self, ppCPC: UCOMIConnectionPointContainer
    ) -> tuple[None, UCOMIConnectionPointContainer]:
        """"""
    def Unadvise(self, dwCookie: int) -> None:
        """"""

class UCOMIConnectionPointContainer:
    """"""
    def EnumConnectionPoints(
        self, ppEnum: UCOMIEnumConnectionPoints
    ) -> tuple[None, UCOMIEnumConnectionPoints]:
        """"""
    def FindConnectionPoint(
        self, riid: Guid, ppCP: UCOMIConnectionPoint
    ) -> tuple[None, UCOMIConnectionPoint]:
        """"""

class UCOMIEnumConnectionPoints:
    """"""
    def Clone(self, ppenum: UCOMIEnumConnectionPoints) -> tuple[None, UCOMIEnumConnectionPoints]:
        """"""
    def Next(
        self, celt: int, rgelt: Array[UCOMIConnectionPoint], pceltFetched: Int32
    ) -> tuple[int, Array[UCOMIConnectionPoint], Int32]:
        """"""
    def Reset(self) -> int:
        """"""
    def Skip(self, celt: int) -> int:
        """"""

class UCOMIEnumConnections:
    """"""
    def Clone(self, ppenum: UCOMIEnumConnections) -> tuple[None, UCOMIEnumConnections]:
        """"""
    def Next(
        self, celt: int, rgelt: Array[CONNECTDATA], pceltFetched: Int32
    ) -> tuple[int, Array[CONNECTDATA], Int32]:
        """"""
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> int:
        """"""

class UCOMIEnumMoniker:
    """"""
    def Clone(self, ppenum: UCOMIEnumMoniker) -> tuple[None, UCOMIEnumMoniker]:
        """"""
    def Next(
        self, celt: int, rgelt: Array[UCOMIMoniker], pceltFetched: Int32
    ) -> tuple[int, Array[UCOMIMoniker], Int32]:
        """"""
    def Reset(self) -> int:
        """"""
    def Skip(self, celt: int) -> int:
        """"""

class UCOMIEnumString:
    """"""
    def Clone(self, ppenum: UCOMIEnumString) -> tuple[None, UCOMIEnumString]:
        """"""
    def Next(
        self, celt: int, rgelt: Array[str], pceltFetched: Int32
    ) -> tuple[int, Array[str], Int32]:
        """"""
    def Reset(self) -> int:
        """"""
    def Skip(self, celt: int) -> int:
        """"""

class UCOMIEnumVARIANT:
    """"""
    def Clone(self, ppenum: int) -> None:
        """"""
    def Next(self, celt: int, rgvar: int, pceltFetched: int) -> int:
        """"""
    def Reset(self) -> int:
        """"""
    def Skip(self, celt: int) -> int:
        """"""

class UCOMIEnumerable:
    """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def __iter__(self) -> Iterator:
        """"""

class UCOMIEnumerator:
    """"""
    @property
    def Current(self) -> object:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""

class UCOMIExpando(UCOMIReflect):
    """"""
    @property
    def UnderlyingSystemType(self) -> Type:
        """"""
    def AddField(self, name: str) -> FieldInfo:
        """"""
    def AddMethod(self, name: str, method: Delegate) -> MethodInfo:
        """"""
    def AddProperty(self, name: str) -> PropertyInfo:
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
    def RemoveMember(self, m: MemberInfo) -> None:
        """"""

class UCOMIMoniker:
    """"""
    def BindToObject(
        self, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, riidResult: Guid, ppvResult: Object
    ) -> tuple[None, Object]:
        """"""
    def BindToStorage(
        self, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, riid: Guid, ppvObj: Object
    ) -> tuple[None, Object]:
        """"""
    def CommonPrefixWith(
        self, pmkOther: UCOMIMoniker, ppmkPrefix: UCOMIMoniker
    ) -> tuple[None, UCOMIMoniker]:
        """"""
    def ComposeWith(
        self, pmkRight: UCOMIMoniker, fOnlyIfNotGeneric: bool, ppmkComposite: UCOMIMoniker
    ) -> tuple[None, UCOMIMoniker]:
        """"""
    def Enum(
        self, fForward: bool, ppenumMoniker: UCOMIEnumMoniker
    ) -> tuple[None, UCOMIEnumMoniker]:
        """"""
    def GetClassID(self, pClassID: Guid) -> tuple[None, Guid]:
        """"""
    def GetDisplayName(
        self, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, ppszDisplayName: String
    ) -> tuple[None, String]:
        """"""
    def GetSizeMax(self, pcbSize: Int64) -> tuple[None, Int64]:
        """"""
    def GetTimeOfLastChange(
        self, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, pFileTime: FILETIME
    ) -> tuple[None, FILETIME]:
        """"""
    def Hash(self, pdwHash: Int32) -> tuple[None, Int32]:
        """"""
    def Inverse(self, ppmk: UCOMIMoniker) -> tuple[None, UCOMIMoniker]:
        """"""
    def IsDirty(self) -> int:
        """"""
    def IsEqual(self, pmkOtherMoniker: UCOMIMoniker) -> None:
        """"""
    def IsRunning(
        self, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, pmkNewlyRunning: UCOMIMoniker
    ) -> None:
        """"""
    def IsSystemMoniker(self, pdwMksys: Int32) -> tuple[None, Int32]:
        """"""
    def Load(self, pStm: UCOMIStream) -> None:
        """"""
    def ParseDisplayName(
        self,
        pbc: UCOMIBindCtx,
        pmkToLeft: UCOMIMoniker,
        pszDisplayName: str,
        pchEaten: Int32,
        ppmkOut: UCOMIMoniker,
    ) -> tuple[None, Int32, UCOMIMoniker]:
        """"""
    def Reduce(
        self,
        pbc: UCOMIBindCtx,
        dwReduceHowFar: int,
        ppmkToLeft: UCOMIMoniker,
        ppmkReduced: UCOMIMoniker,
    ) -> tuple[None, UCOMIMoniker]:
        """"""
    def RelativePathTo(
        self, pmkOther: UCOMIMoniker, ppmkRelPath: UCOMIMoniker
    ) -> tuple[None, UCOMIMoniker]:
        """"""
    def Save(self, pStm: UCOMIStream, fClearDirty: bool) -> None:
        """"""

class UCOMIPersistFile:
    """"""
    def GetClassID(self, pClassID: Guid) -> tuple[None, Guid]:
        """"""
    def GetCurFile(self, ppszFileName: String) -> tuple[None, String]:
        """"""
    def IsDirty(self) -> int:
        """"""
    def Load(self, pszFileName: str, dwMode: int) -> None:
        """"""
    def Save(self, pszFileName: str, fRemember: bool) -> None:
        """"""
    def SaveCompleted(self, pszFileName: str) -> None:
        """"""

class UCOMIReflect:
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

class UCOMIRunningObjectTable:
    """"""
    def EnumRunning(self, ppenumMoniker: UCOMIEnumMoniker) -> tuple[None, UCOMIEnumMoniker]:
        """"""
    def GetObject(self, pmkObjectName: UCOMIMoniker, ppunkObject: Object) -> tuple[None, Object]:
        """"""
    def GetTimeOfLastChange(
        self, pmkObjectName: UCOMIMoniker, pfiletime: FILETIME
    ) -> tuple[None, FILETIME]:
        """"""
    def IsRunning(self, pmkObjectName: UCOMIMoniker) -> None:
        """"""
    def NoteChangeTime(self, dwRegister: int, pfiletime: FILETIME) -> None:
        """"""
    def Register(
        self, grfFlags: int, punkObject: object, pmkObjectName: UCOMIMoniker, pdwRegister: Int32
    ) -> tuple[None, Int32]:
        """"""
    def Revoke(self, dwRegister: int) -> None:
        """"""

class UCOMIStream:
    """"""
    def Clone(self, ppstm: UCOMIStream) -> tuple[None, UCOMIStream]:
        """"""
    def Commit(self, grfCommitFlags: int) -> None:
        """"""
    def CopyTo(self, pstm: UCOMIStream, cb: int, pcbRead: IntPtr, pcbWritten: IntPtr) -> None:
        """"""
    def LockRegion(self, libOffset: int, cb: int, dwLockType: int) -> None:
        """"""
    def Read(self, pv: Array[int], cb: int, pcbRead: IntPtr) -> tuple[None, Array[int]]:
        """"""
    def Revert(self) -> None:
        """"""
    def Seek(self, dlibMove: int, dwOrigin: int, plibNewPosition: IntPtr) -> None:
        """"""
    def SetSize(self, libNewSize: int) -> None:
        """"""
    def Stat(self, pstatstg: STATSTG, grfStatFlag: int) -> tuple[None, STATSTG]:
        """"""
    def UnlockRegion(self, libOffset: int, cb: int, dwLockType: int) -> None:
        """"""
    def Write(self, pv: Array[int], cb: int, pcbWritten: IntPtr) -> None:
        """"""

class UCOMITypeComp:
    """"""
    def Bind(
        self,
        szName: str,
        lHashVal: int,
        wFlags: int,
        ppTInfo: UCOMITypeInfo,
        pDescKind: DESCKIND,
        pBindPtr: BINDPTR,
    ) -> tuple[None, UCOMITypeInfo, DESCKIND, BINDPTR]:
        """"""
    def BindType(
        self, szName: str, lHashVal: int, ppTInfo: UCOMITypeInfo, ppTComp: UCOMITypeComp
    ) -> tuple[None, UCOMITypeInfo, UCOMITypeComp]:
        """"""

class UCOMITypeInfo:
    """"""
    def AddressOfMember(self, memid: int, invKind: INVOKEKIND, ppv: IntPtr) -> tuple[None, IntPtr]:
        """"""
    def CreateInstance(self, pUnkOuter: object, riid: Guid, ppvObj: Object) -> tuple[None, Object]:
        """"""
    def GetContainingTypeLib(
        self, ppTLB: UCOMITypeLib, pIndex: Int32
    ) -> tuple[None, UCOMITypeLib, Int32]:
        """"""
    def GetDllEntry(
        self,
        memid: int,
        invKind: INVOKEKIND,
        pBstrDllName: String,
        pBstrName: String,
        pwOrdinal: Int16,
    ) -> tuple[None, String, String, Int16]:
        """"""
    def GetDocumentation(
        self,
        index: int,
        strName: String,
        strDocString: String,
        dwHelpContext: Int32,
        strHelpFile: String,
    ) -> tuple[None, String, String, Int32, String]:
        """"""
    def GetFuncDesc(self, index: int, ppFuncDesc: IntPtr) -> tuple[None, IntPtr]:
        """"""
    def GetIDsOfNames(
        self, rgszNames: Array[str], cNames: int, pMemId: Array[int]
    ) -> tuple[None, Array[int]]:
        """"""
    def GetImplTypeFlags(self, index: int, pImplTypeFlags: Int32) -> tuple[None, Int32]:
        """"""
    def GetMops(self, memid: int, pBstrMops: String) -> tuple[None, String]:
        """"""
    def GetNames(
        self, memid: int, rgBstrNames: Array[str], cMaxNames: int, pcNames: Int32
    ) -> tuple[None, Array[str], Int32]:
        """"""
    def GetRefTypeInfo(self, hRef: int, ppTI: UCOMITypeInfo) -> tuple[None, UCOMITypeInfo]:
        """"""
    def GetRefTypeOfImplType(self, index: int, href: Int32) -> tuple[None, Int32]:
        """"""
    def GetTypeAttr(self, ppTypeAttr: IntPtr) -> tuple[None, IntPtr]:
        """"""
    def GetTypeComp(self, ppTComp: UCOMITypeComp) -> tuple[None, UCOMITypeComp]:
        """"""
    def GetVarDesc(self, index: int, ppVarDesc: IntPtr) -> tuple[None, IntPtr]:
        """"""
    def Invoke(
        self,
        pvInstance: object,
        memid: int,
        wFlags: int,
        pDispParams: DISPPARAMS,
        pVarResult: Object,
        pExcepInfo: EXCEPINFO,
        puArgErr: Int32,
    ) -> tuple[None, Object, EXCEPINFO, Int32]:
        """"""
    def ReleaseFuncDesc(self, pFuncDesc: IntPtr) -> None:
        """"""
    def ReleaseTypeAttr(self, pTypeAttr: IntPtr) -> None:
        """"""
    def ReleaseVarDesc(self, pVarDesc: IntPtr) -> None:
        """"""

class UCOMITypeLib:
    """"""
    def FindName(
        self,
        szNameBuf: str,
        lHashVal: int,
        ppTInfo: Array[UCOMITypeInfo],
        rgMemId: Array[int],
        pcFound: Int16,
    ) -> tuple[None, Array[UCOMITypeInfo], Array[int]]:
        """"""
    def GetDocumentation(
        self,
        index: int,
        strName: String,
        strDocString: String,
        dwHelpContext: Int32,
        strHelpFile: String,
    ) -> tuple[None, String, String, Int32, String]:
        """"""
    def GetLibAttr(self, ppTLibAttr: IntPtr) -> tuple[None, IntPtr]:
        """"""
    def GetTypeComp(self, ppTComp: UCOMITypeComp) -> tuple[None, UCOMITypeComp]:
        """"""
    def GetTypeInfo(self, index: int, ppTI: UCOMITypeInfo) -> tuple[None, UCOMITypeInfo]:
        """"""
    def GetTypeInfoCount(self) -> int:
        """"""
    def GetTypeInfoOfGuid(self, guid: Guid, ppTInfo: UCOMITypeInfo) -> tuple[None, UCOMITypeInfo]:
        """"""
    def GetTypeInfoType(self, index: int, pTKind: TYPEKIND) -> tuple[None, TYPEKIND]:
        """"""
    def IsName(self, szNameBuf: str, lHashVal: int) -> bool:
        """"""
    def ReleaseTLibAttr(self, pTLibAttr: IntPtr) -> None:
        """"""

class UnknownWrapper(Object):
    """"""
    def __init__(self, obj: object) -> None:
        """"""
    @property
    def WrappedObject(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class UnmanagedFunctionPointerAttribute(Attribute, _Attribute):
    """"""

    BestFitMapping: Final[bool]
    """"""
    CharSet: Final[CharSet]
    """"""
    SetLastError: Final[bool]
    """"""
    ThrowOnUnmappableChar: Final[bool]
    """"""
    def __init__(self, callingConvention: CallingConvention) -> None:
        """"""
    @property
    def CallingConvention(self) -> CallingConvention:
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

class UnmanagedType(Enum):
    """"""

    Bool: UnmanagedType = ...
    """"""
    I1: UnmanagedType = ...
    """"""
    U1: UnmanagedType = ...
    """"""
    I2: UnmanagedType = ...
    """"""
    U2: UnmanagedType = ...
    """"""
    I4: UnmanagedType = ...
    """"""
    U4: UnmanagedType = ...
    """"""
    I8: UnmanagedType = ...
    """"""
    U8: UnmanagedType = ...
    """"""
    R4: UnmanagedType = ...
    """"""
    R8: UnmanagedType = ...
    """"""
    Currency: UnmanagedType = ...
    """"""
    BStr: UnmanagedType = ...
    """"""
    LPStr: UnmanagedType = ...
    """"""
    LPWStr: UnmanagedType = ...
    """"""
    LPTStr: UnmanagedType = ...
    """"""
    ByValTStr: UnmanagedType = ...
    """"""
    IUnknown: UnmanagedType = ...
    """"""
    IDispatch: UnmanagedType = ...
    """"""
    Struct: UnmanagedType = ...
    """"""
    Interface: UnmanagedType = ...
    """"""
    SafeArray: UnmanagedType = ...
    """"""
    ByValArray: UnmanagedType = ...
    """"""
    SysInt: UnmanagedType = ...
    """"""
    SysUInt: UnmanagedType = ...
    """"""
    VBByRefStr: UnmanagedType = ...
    """"""
    AnsiBStr: UnmanagedType = ...
    """"""
    TBStr: UnmanagedType = ...
    """"""
    VariantBool: UnmanagedType = ...
    """"""
    FunctionPtr: UnmanagedType = ...
    """"""
    AsAny: UnmanagedType = ...
    """"""
    LPArray: UnmanagedType = ...
    """"""
    LPStruct: UnmanagedType = ...
    """"""
    CustomMarshaler: UnmanagedType = ...
    """"""
    Error: UnmanagedType = ...
    """"""
    IInspectable: UnmanagedType = ...
    """"""
    HString: UnmanagedType = ...
    """"""
    LPUTF8Str: UnmanagedType = ...
    """"""

class VARDESC(ValueType):
    """"""

    elemdescVar: Final[ELEMDESC]
    """"""
    lpstrSchema: Final[str]
    """"""
    memid: Final[int]
    """"""
    varkind: Final[VarEnum]
    """"""
    wVarFlags: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    class DESCUNION(ValueType):
        """"""

        lpvarValue: Final[IntPtr]
        """"""
        oInst: Final[int]
        """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""

class VARFLAGS(Enum):
    """"""

    VARFLAG_FREADONLY: VARFLAGS = ...
    """"""
    VARFLAG_FSOURCE: VARFLAGS = ...
    """"""
    VARFLAG_FBINDABLE: VARFLAGS = ...
    """"""
    VARFLAG_FREQUESTEDIT: VARFLAGS = ...
    """"""
    VARFLAG_FDISPLAYBIND: VARFLAGS = ...
    """"""
    VARFLAG_FDEFAULTBIND: VARFLAGS = ...
    """"""
    VARFLAG_FHIDDEN: VARFLAGS = ...
    """"""
    VARFLAG_FRESTRICTED: VARFLAGS = ...
    """"""
    VARFLAG_FDEFAULTCOLLELEM: VARFLAGS = ...
    """"""
    VARFLAG_FUIDEFAULT: VARFLAGS = ...
    """"""
    VARFLAG_FNONBROWSABLE: VARFLAGS = ...
    """"""
    VARFLAG_FREPLACEABLE: VARFLAGS = ...
    """"""
    VARFLAG_FIMMEDIATEBIND: VARFLAGS = ...
    """"""

class VarEnum(Enum):
    """"""

    VT_EMPTY: VarEnum = ...
    """"""
    VT_NULL: VarEnum = ...
    """"""
    VT_I2: VarEnum = ...
    """"""
    VT_I4: VarEnum = ...
    """"""
    VT_R4: VarEnum = ...
    """"""
    VT_R8: VarEnum = ...
    """"""
    VT_CY: VarEnum = ...
    """"""
    VT_DATE: VarEnum = ...
    """"""
    VT_BSTR: VarEnum = ...
    """"""
    VT_DISPATCH: VarEnum = ...
    """"""
    VT_ERROR: VarEnum = ...
    """"""
    VT_BOOL: VarEnum = ...
    """"""
    VT_VARIANT: VarEnum = ...
    """"""
    VT_UNKNOWN: VarEnum = ...
    """"""
    VT_DECIMAL: VarEnum = ...
    """"""
    VT_I1: VarEnum = ...
    """"""
    VT_UI1: VarEnum = ...
    """"""
    VT_UI2: VarEnum = ...
    """"""
    VT_UI4: VarEnum = ...
    """"""
    VT_I8: VarEnum = ...
    """"""
    VT_UI8: VarEnum = ...
    """"""
    VT_INT: VarEnum = ...
    """"""
    VT_UINT: VarEnum = ...
    """"""
    VT_VOID: VarEnum = ...
    """"""
    VT_HRESULT: VarEnum = ...
    """"""
    VT_PTR: VarEnum = ...
    """"""
    VT_SAFEARRAY: VarEnum = ...
    """"""
    VT_CARRAY: VarEnum = ...
    """"""
    VT_USERDEFINED: VarEnum = ...
    """"""
    VT_LPSTR: VarEnum = ...
    """"""
    VT_LPWSTR: VarEnum = ...
    """"""
    VT_RECORD: VarEnum = ...
    """"""
    VT_FILETIME: VarEnum = ...
    """"""
    VT_BLOB: VarEnum = ...
    """"""
    VT_STREAM: VarEnum = ...
    """"""
    VT_STORAGE: VarEnum = ...
    """"""
    VT_STREAMED_OBJECT: VarEnum = ...
    """"""
    VT_STORED_OBJECT: VarEnum = ...
    """"""
    VT_BLOB_OBJECT: VarEnum = ...
    """"""
    VT_CF: VarEnum = ...
    """"""
    VT_CLSID: VarEnum = ...
    """"""
    VT_VECTOR: VarEnum = ...
    """"""
    VT_ARRAY: VarEnum = ...
    """"""
    VT_BYREF: VarEnum = ...
    """"""

class Variant(ValueType):
    """"""
    @property
    def AsBool(self) -> bool:
        """"""
    @AsBool.setter
    def AsBool(self, value: bool) -> None: ...
    @property
    def AsBstr(self) -> str:
        """"""
    @AsBstr.setter
    def AsBstr(self, value: str) -> None: ...
    @property
    def AsCy(self) -> Decimal:
        """"""
    @AsCy.setter
    def AsCy(self, value: Decimal) -> None: ...
    @property
    def AsDate(self) -> DateTime:
        """"""
    @AsDate.setter
    def AsDate(self, value: DateTime) -> None: ...
    @property
    def AsDecimal(self) -> Decimal:
        """"""
    @AsDecimal.setter
    def AsDecimal(self, value: Decimal) -> None: ...
    @property
    def AsDispatch(self) -> object:
        """"""
    @AsDispatch.setter
    def AsDispatch(self, value: object) -> None: ...
    @property
    def AsError(self) -> int:
        """"""
    @AsError.setter
    def AsError(self, value: int) -> None: ...
    @property
    def AsI1(self) -> int:
        """"""
    @AsI1.setter
    def AsI1(self, value: int) -> None: ...
    @property
    def AsI2(self) -> int:
        """"""
    @AsI2.setter
    def AsI2(self, value: int) -> None: ...
    @property
    def AsI4(self) -> int:
        """"""
    @AsI4.setter
    def AsI4(self, value: int) -> None: ...
    @property
    def AsI8(self) -> int:
        """"""
    @AsI8.setter
    def AsI8(self, value: int) -> None: ...
    @property
    def AsInt(self) -> int:
        """"""
    @AsInt.setter
    def AsInt(self, value: int) -> None: ...
    @property
    def AsR4(self) -> float:
        """"""
    @AsR4.setter
    def AsR4(self, value: float) -> None: ...
    @property
    def AsR8(self) -> float:
        """"""
    @AsR8.setter
    def AsR8(self, value: float) -> None: ...
    @property
    def AsUi1(self) -> int:
        """"""
    @AsUi1.setter
    def AsUi1(self, value: int) -> None: ...
    @property
    def AsUi2(self) -> int:
        """"""
    @AsUi2.setter
    def AsUi2(self, value: int) -> None: ...
    @property
    def AsUi4(self) -> int:
        """"""
    @AsUi4.setter
    def AsUi4(self, value: int) -> None: ...
    @property
    def AsUi8(self) -> int:
        """"""
    @AsUi8.setter
    def AsUi8(self, value: int) -> None: ...
    @property
    def AsUint(self) -> int:
        """"""
    @AsUint.setter
    def AsUint(self, value: int) -> None: ...
    @property
    def AsUnknown(self) -> object:
        """"""
    @AsUnknown.setter
    def AsUnknown(self, value: object) -> None: ...
    @property
    def VariantType(self) -> VarEnum:
        """"""
    @VariantType.setter
    def VariantType(self, value: VarEnum) -> None: ...
    def Clear(self) -> None:
        """"""
    def CopyFromIndirect(self, value: object) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetAsNULL(self) -> None:
        """"""
    def ToObject(self) -> object:
        """"""
    def ToString(self) -> str:
        """"""

class VariantWrapper(Object):
    """"""
    def __init__(self, obj: object) -> None:
        """"""
    @property
    def WrappedObject(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class _Activator:
    """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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

class _Assembly:
    """"""
    @property
    def CodeBase(self) -> str:
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
    def FullName(self) -> str:
        """"""
    @property
    def GlobalAssemblyCache(self) -> bool:
        """"""
    @property
    def Location(self) -> str:
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
    def Equals(self, other: object) -> bool:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
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

class _AssemblyBuilder:
    """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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

class _AssemblyName:
    """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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

class _Attribute:
    """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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

class _ConstructorBuilder:
    """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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

class _ConstructorInfo:
    """"""
    @property
    def Attributes(self) -> MethodAttributes:
        """"""
    @property
    def CallingConvention(self) -> CallingConventions:
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
    def IsHideBySig(self) -> bool:
        """"""
    @property
    def IsPrivate(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
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
    def MethodHandle(self) -> RuntimeMethodHandle:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    def Equals(self, other: object) -> bool:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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

class _CustomAttributeBuilder:
    """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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

class _EnumBuilder:
    """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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

class _EventBuilder:
    """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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

class _EventInfo:
    """"""
    @property
    def Attributes(self) -> EventAttributes:
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
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    def AddEventHandler(self, target: object, handler: Delegate) -> None:
        """"""
    def Equals(self, other: object) -> bool:
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
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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

class _Exception:
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

class _FieldBuilder:
    """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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

class _FieldInfo:
    """"""
    @property
    def Attributes(self) -> FieldAttributes:
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
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsStatic(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    def Equals(self, other: object) -> bool:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
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

class _ILGenerator:
    """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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

class _LocalBuilder:
    """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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

class _MemberInfo:
    """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    def Equals(self, other: object) -> bool:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
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

class _MethodBase:
    """"""
    @property
    def Attributes(self) -> MethodAttributes:
        """"""
    @property
    def CallingConvention(self) -> CallingConventions:
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
    def IsHideBySig(self) -> bool:
        """"""
    @property
    def IsPrivate(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
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
    def MethodHandle(self) -> RuntimeMethodHandle:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    def Equals(self, other: object) -> bool:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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

class _MethodBuilder:
    """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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

class _MethodInfo:
    """"""
    @property
    def Attributes(self) -> MethodAttributes:
        """"""
    @property
    def CallingConvention(self) -> CallingConventions:
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
    def IsHideBySig(self) -> bool:
        """"""
    @property
    def IsPrivate(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
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
    def MethodHandle(self) -> RuntimeMethodHandle:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    @property
    def ReturnType(self) -> Type:
        """"""
    @property
    def ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider:
        """"""
    def Equals(self, other: object) -> bool:
        """"""
    def GetBaseDefinition(self) -> MethodInfo:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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

class _MethodRental:
    """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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

class _Module:
    """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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

class _ModuleBuilder:
    """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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

class _ParameterBuilder:
    """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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

class _ParameterInfo:
    """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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

class _PropertyBuilder:
    """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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

class _PropertyInfo:
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
    def DeclaringType(self) -> Type:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
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
    def Equals(self, other: object) -> bool:
        """"""
    @overload
    def GetAccessors(self) -> Array[MethodInfo]:
        """"""
    @overload
    def GetAccessors(self, nonPublic: bool) -> Array[MethodInfo]:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
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

class _SignatureHelper:
    """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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

class _Thread:
    """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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

class _Type:
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
    def DeclaringType(self) -> Type:
        """"""
    @property
    def FullName(self) -> str:
        """"""
    @property
    def GUID(self) -> Guid:
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
    def IsContextful(self) -> bool:
        """"""
    @property
    def IsEnum(self) -> bool:
        """"""
    @property
    def IsExplicitLayout(self) -> bool:
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
    def MemberType(self) -> MemberTypes:
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
    def TypeHandle(self) -> RuntimeTypeHandle:
        """"""
    @property
    def TypeInitializer(self) -> ConstructorInfo:
        """"""
    @property
    def UnderlyingSystemType(self) -> Type:
        """"""
    @overload
    def Equals(self, other: object) -> bool:
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
    def GetDefaultMembers(self) -> Array[MemberInfo]:
        """"""
    def GetElementType(self) -> Type:
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
    def IsInstanceOfType(self, o: object) -> bool:
        """"""
    def IsSubclassOf(self, c: Type) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class _TypeBuilder:
    """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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
