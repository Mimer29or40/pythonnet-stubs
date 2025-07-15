from abc import ABC
from collections.abc import Callable
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import TypeVar
from typing import overload

from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from System import Array
from System import Attribute
from System import Char
from System import DateTime
from System import Decimal
from System import Delegate
from System import Enum
from System import Exception
from System import Guid
from System import IDisposable
from System import IEquatable
from System import IntPtr
from System import MarshalByRefObject
from System import Object
from System import RuntimeFieldHandle
from System import RuntimeMethodHandle
from System import RuntimeTypeHandle
from System import SystemException
from System import Type
from System import TypedReference
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

T = TypeVar("T")
TDelegate = TypeVar("TDelegate")
TWrapper = TypeVar("TWrapper")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class AllowReversePInvokeCallsAttribute(Attribute, _Attribute):
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

    def __init__(self, array: object, offset: int):
        """:param array:
        :param offset:
        """
    @overload
    def Equals(self, obj: ArrayWithOffset) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetArray(self) -> object:
        """:return:"""
    def GetHashCode(self) -> int:
        """:return:"""
    def GetOffset(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def __eq__(self, other: ArrayWithOffset) -> bool:
        """:param other:
        :return:
        """
    def __ne__(self, other: ArrayWithOffset) -> bool:
        """:param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, a: ArrayWithOffset, b: ArrayWithOffset) -> bool:
        """:param a:
        :param b:
        :return:
        """
    @classmethod
    def op_Inequality(cls, a: ArrayWithOffset, b: ArrayWithOffset) -> bool:
        """:param a:
        :param b:
        :return:
        """

class AssemblyRegistrationFlags(Enum):
    """"""

    _None: AssemblyRegistrationFlags = ...
    """"""
    SetCodeBase: AssemblyRegistrationFlags = ...
    """"""

class AutomationProxyAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, val: bool):
        """:param val:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    @property
    def Value(self) -> bool:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class BINDPTR(ValueType):
    """"""

    lpfuncdesc: Final[IntPtr] = ...
    """
    
    :return: 
    """
    lptcomp: Final[IntPtr] = ...
    """
    
    :return: 
    """
    lpvardesc: Final[IntPtr] = ...
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

class BIND_OPTS(ValueType):
    """"""

    cbStruct: Final[int] = ...
    """
    
    :return: 
    """
    dwTickCountDeadline: Final[int] = ...
    """
    
    :return: 
    """
    grfFlags: Final[int] = ...
    """
    
    :return: 
    """
    grfMode: Final[int] = ...
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

class BStrWrapper(Object):
    """"""

    @overload
    def __init__(self, value: object):
        """:param value:"""
    @overload
    def __init__(self, value: str):
        """:param value:"""
    @property
    def WrappedObject(self) -> str:
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

class BestFitMappingAttribute(Attribute, _Attribute):
    """"""

    ThrowOnUnmappableChar: Final[bool] = ...
    """
    
    :return: 
    """
    def __init__(self, BestFitMapping: bool):
        """:param BestFitMapping:"""
    @property
    def BestFitMapping(self) -> bool:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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
    def __init__(self, message: str, errorCode: int):
        """:param message:
        :param errorCode:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def ErrorCode(self) -> int:
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

class CONNECTDATA(ValueType):
    """"""

    dwCookie: Final[int] = ...
    """
    
    :return: 
    """
    pUnk: Final[object] = ...
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
    def __init__(self, classInterfaceType: ClassInterfaceType):
        """:param classInterfaceType:"""
    @overload
    def __init__(self, classInterfaceType: int):
        """:param classInterfaceType:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    @property
    def Value(self) -> ClassInterfaceType:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

    def __init__(self, coClass: Type):
        """:param coClass:"""
    @property
    def CoClass(self) -> Type:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class ComAliasNameAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, alias: str):
        """:param alias:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    @property
    def Value(self) -> str:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class ComAwareEventInfo(EventInfo, ICustomAttributeProvider, _EventInfo, _MemberInfo):
    """"""

    def __init__(self, type: Type, eventName: str):
        """:param type:
        :param eventName:
        """
    @property
    def AddMethod(self) -> MethodInfo:
        """:return:"""
    @property
    def Attributes(self) -> EventAttributes:
        """:return:"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """:return:"""
    @property
    def DeclaringType(self) -> Type:
        """:return:"""
    @property
    def DeclaringType(self) -> Type:
        """:return:"""
    @property
    def EventHandlerType(self) -> Type:
        """:return:"""
    @property
    def IsMulticast(self) -> bool:
        """:return:"""
    @property
    def IsSpecialName(self) -> bool:
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
    def Name(self) -> str:
        """:return:"""
    @property
    def Name(self) -> str:
        """:return:"""
    @property
    def RaiseMethod(self) -> MethodInfo:
        """:return:"""
    @property
    def ReflectedType(self) -> Type:
        """:return:"""
    @property
    def ReflectedType(self) -> Type:
        """:return:"""
    @property
    def RemoveMethod(self) -> MethodInfo:
        """:return:"""
    def AddEventHandler(self, target: object, handler: Delegate) -> None:
        """:param target:
        :param handler:
        """
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
    def GetAddMethod(self) -> MethodInfo:
        """:return:"""
    @overload
    def GetAddMethod(self, nonPublic: bool) -> MethodInfo:
        """:param nonPublic:
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
    def GetOtherMethods(self) -> Array[MethodInfo]:
        """:return:"""
    @overload
    def GetOtherMethods(self, nonPublic: bool) -> Array[MethodInfo]:
        """:param nonPublic:
        :return:
        """
    @overload
    def GetRaiseMethod(self) -> MethodInfo:
        """:return:"""
    @overload
    def GetRaiseMethod(self, nonPublic: bool) -> MethodInfo:
        """:param nonPublic:
        :return:
        """
    @overload
    def GetRemoveMethod(self) -> MethodInfo:
        """:return:"""
    @overload
    def GetRemoveMethod(self, nonPublic: bool) -> MethodInfo:
        """:param nonPublic:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
        """:param pcTInfo:"""
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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
    def RemoveEventHandler(self, target: object, handler: Delegate) -> None:
        """:param target:
        :param handler:
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

class ComCompatibleVersionAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, major: int, minor: int, build: int, revision: int):
        """:param major:
        :param minor:
        :param build:
        :param revision:
        """
    @property
    def BuildNumber(self) -> int:
        """:return:"""
    @property
    def MajorVersion(self) -> int:
        """:return:"""
    @property
    def MinorVersion(self) -> int:
        """:return:"""
    @property
    def RevisionNumber(self) -> int:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class ComConversionLossAttribute(Attribute, _Attribute):
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class ComDefaultInterfaceAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, defaultInterface: Type):
        """:param defaultInterface:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    @property
    def Value(self) -> Type:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class ComEventInterfaceAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, SourceInterface: Type, EventProvider: Type):
        """:param SourceInterface:
        :param EventProvider:
        """
    @property
    def EventProvider(self) -> Type:
        """:return:"""
    @property
    def SourceInterface(self) -> Type:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class ComEventsHelper(ABC, Object):
    """"""

    @classmethod
    def Combine(cls, rcw: object, iid: Guid, dispid: int, d: Delegate) -> None:
        """:param rcw:
        :param iid:
        :param dispid:
        :param d:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def Remove(cls, rcw: object, iid: Guid, dispid: int, d: Delegate) -> Delegate:
        """:param rcw:
        :param iid:
        :param dispid:
        :param d:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class ComEventsInfo(Object):
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

class ComEventsMethod(Object):
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

class ComEventsSink(Object, ICustomQueryInterface, NativeMethods.IDispatch):
    """"""

    def AddMethod(self, dispid: int) -> ComEventsMethod:
        """:param dispid:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def FindMethod(self, dispid: int) -> ComEventsMethod:
        """:param dispid:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, iid: Guid, names: Array[str], cNames: int, lcid: int, rgDispId: Array[int]
    ) -> tuple[None, Array[int]]:
        """"""
    def GetInterface(self, iid: Guid, ppv: IntPtr) -> tuple[CustomQueryInterfaceResult, IntPtr]:
        """:param iid:
        :param ppv:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, info: IntPtr) -> tuple[None, IntPtr]:
        """"""
    def GetTypeInfoCount(self, pctinfo: int) -> tuple[None, int]:
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
        """:param method:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class ComImportAttribute(Attribute, _Attribute):
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class ComSourceInterfacesAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, sourceInterfaces: str):
        """:param sourceInterfaces:"""
    @overload
    def __init__(self, sourceInterface: Type):
        """:param sourceInterface:"""
    @overload
    def __init__(self, sourceInterface1: Type, sourceInterface2: Type):
        """:param sourceInterface1:
        :param sourceInterface2:
        """
    @overload
    def __init__(self, sourceInterface1: Type, sourceInterface2: Type, sourceInterface3: Type):
        """:param sourceInterface1:
        :param sourceInterface2:
        :param sourceInterface3:
        """
    @overload
    def __init__(
        self,
        sourceInterface1: Type,
        sourceInterface2: Type,
        sourceInterface3: Type,
        sourceInterface4: Type,
    ):
        """:param sourceInterface1:
        :param sourceInterface2:
        :param sourceInterface3:
        :param sourceInterface4:
        """
    @property
    def TypeId(self) -> object:
        """:return:"""
    @property
    def Value(self) -> str:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class ComUnregisterFunctionAttribute(Attribute, _Attribute):
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class ComVisibleAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, visibility: bool):
        """:param visibility:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    @property
    def Value(self) -> bool:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class CriticalHandle(ABC, CriticalFinalizerObject, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """:return:"""
    @property
    def IsInvalid(self) -> bool:
        """:return:"""
    def Close(self) -> None:
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

class CurrencyWrapper(Object):
    """"""

    @overload
    def __init__(self, obj: Decimal):
        """:param obj:"""
    @overload
    def __init__(self, obj: object):
        """:param obj:"""
    @property
    def WrappedObject(self) -> Decimal:
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

    cArgs: Final[int] = ...
    """
    
    :return: 
    """
    cNamedArgs: Final[int] = ...
    """
    
    :return: 
    """
    rgdispidNamedArgs: Final[IntPtr] = ...
    """
    
    :return: 
    """
    rgvarg: Final[IntPtr] = ...
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

class DefaultCharSetAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, charSet: CharSet):
        """:param charSet:"""
    @property
    def CharSet(self) -> CharSet:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class DefaultDllImportSearchPathsAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, paths: DllImportSearchPath):
        """:param paths:"""
    @property
    def Paths(self) -> DllImportSearchPath:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class DefaultParameterValueAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, value: object):
        """:param value:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    @property
    def Value(self) -> object:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class DispIdAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, dispId: int):
        """:param dispId:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    @property
    def Value(self) -> int:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class DispatchWrapper(Object):
    """"""

    def __init__(self, obj: object):
        """:param obj:"""
    @property
    def WrappedObject(self) -> object:
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

class DllImportAttribute(Attribute, _Attribute):
    """"""

    BestFitMapping: Final[bool] = ...
    """
    
    :return: 
    """
    CallingConvention: Final[CallingConvention] = ...
    """
    
    :return: 
    """
    CharSet: Final[CharSet] = ...
    """
    
    :return: 
    """
    EntryPoint: Final[str] = ...
    """
    
    :return: 
    """
    ExactSpelling: Final[bool] = ...
    """
    
    :return: 
    """
    PreserveSig: Final[bool] = ...
    """
    
    :return: 
    """
    SetLastError: Final[bool] = ...
    """
    
    :return: 
    """
    ThrowOnUnmappableChar: Final[bool] = ...
    """
    
    :return: 
    """
    def __init__(self, dllName: str):
        """:param dllName:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    @property
    def Value(self) -> str:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

    desc: Final[ELEMDESC.DESCUNION] = ...
    """
    
    :return: 
    """
    tdesc: Final[TYPEDESC] = ...
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

    class DESCUNION(ValueType):
        """"""

        idldesc: Final[IDLDESC] = ...
        """"""
        paramdesc: Final[PARAMDESC] = ...
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

class EXCEPINFO(ValueType):
    """"""

    bstrDescription: Final[str] = ...
    """
    
    :return: 
    """
    bstrHelpFile: Final[str] = ...
    """
    
    :return: 
    """
    bstrSource: Final[str] = ...
    """
    
    :return: 
    """
    dwHelpContext: Final[int] = ...
    """
    
    :return: 
    """
    pfnDeferredFillIn: Final[IntPtr] = ...
    """
    
    :return: 
    """
    pvReserved: Final[IntPtr] = ...
    """
    
    :return: 
    """
    wCode: Final[int] = ...
    """
    
    :return: 
    """
    wReserved: Final[int] = ...
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

class ErrorWrapper(Object):
    """"""

    @overload
    def __init__(self, e: Exception):
        """:param e:"""
    @overload
    def __init__(self, errorCode: int):
        """:param errorCode:"""
    @overload
    def __init__(self, errorCode: object):
        """:param errorCode:"""
    @property
    def ErrorCode(self) -> int:
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
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def RegisterObjectCreationCallback(cls, callback: ObjectCreationDelegate) -> None:
        """:param callback:"""
    def ToString(self) -> str:
        """:return:"""

class ExternalException(SystemException, _Exception, ISerializable):
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
    def __init__(self, message: str, errorCode: int):
        """:param message:
        :param errorCode:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def ErrorCode(self) -> int:
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

class FILETIME(ValueType):
    """"""

    dwHighDateTime: Final[int] = ...
    """
    
    :return: 
    """
    dwLowDateTime: Final[int] = ...
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

class FUNCDESC(ValueType):
    """"""

    cParams: Final[int] = ...
    """
    
    :return: 
    """
    cParamsOpt: Final[int] = ...
    """
    
    :return: 
    """
    cScodes: Final[int] = ...
    """
    
    :return: 
    """
    callconv: Final[CALLCONV] = ...
    """
    
    :return: 
    """
    elemdescFunc: Final[ELEMDESC] = ...
    """
    
    :return: 
    """
    funckind: Final[FUNCKIND] = ...
    """
    
    :return: 
    """
    invkind: Final[INVOKEKIND] = ...
    """
    
    :return: 
    """
    lprgelemdescParam: Final[IntPtr] = ...
    """
    
    :return: 
    """
    lprgscode: Final[IntPtr] = ...
    """
    
    :return: 
    """
    memid: Final[int] = ...
    """
    
    :return: 
    """
    oVft: Final[int] = ...
    """
    
    :return: 
    """
    wFuncFlags: Final[int] = ...
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

    def __init__(self, offset: int):
        """:param offset:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    @property
    def Value(self) -> int:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class GCHandle(ValueType):
    """"""

    @property
    def IsAllocated(self) -> bool:
        """:return:"""
    @property
    def Target(self) -> object:
        """:return:"""
    @Target.setter
    def Target(self, value: object) -> None: ...
    def AddrOfPinnedObject(self) -> IntPtr:
        """:return:"""
    @classmethod
    @overload
    def Alloc(cls, value: object) -> GCHandle:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def Alloc(cls, value: object, type: GCHandleType) -> GCHandle:
        """:param value:
        :param type:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def Free(self) -> None:
        """"""
    @classmethod
    def FromIntPtr(cls, value: IntPtr) -> GCHandle:
        """:param value:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def ToIntPtr(cls, value: GCHandle) -> IntPtr:
        """:param value:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""
    def __eq__(self, other: GCHandle) -> bool:
        """:param other:
        :return:
        """
    def __ne__(self, other: GCHandle) -> bool:
        """:param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, a: GCHandle, b: GCHandle) -> bool:
        """:param a:
        :param b:
        :return:
        """
    @classmethod
    @overload
    def op_Explicit(cls, value: GCHandle) -> IntPtr:
        """:param value:
        :return:
        """
    @classmethod
    @overload
    def op_Explicit(cls, value: IntPtr) -> GCHandle:
        """:param value:
        :return:
        """
    @classmethod
    def op_Inequality(cls, a: GCHandle, b: GCHandle) -> bool:
        """:param a:
        :param b:
        :return:
        """

class GCHandleCookieTable(Object):
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

    def __init__(self, guid: str):
        """:param guid:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    @property
    def Value(self) -> str:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class HandleCollector(Object):
    """"""

    @overload
    def __init__(self, name: str, initialThreshold: int):
        """:param name:
        :param initialThreshold:
        """
    @overload
    def __init__(self, name: str, initialThreshold: int, maximumThreshold: int):
        """:param name:
        :param initialThreshold:
        :param maximumThreshold:
        """
    @property
    def Count(self) -> int:
        """:return:"""
    @property
    def InitialThreshold(self) -> int:
        """:return:"""
    @property
    def MaximumThreshold(self) -> int:
        """:return:"""
    @property
    def Name(self) -> str:
        """:return:"""
    def Add(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def Remove(self) -> None:
        """"""
    def ToString(self) -> str:
        """:return:"""

class HandleRef(ValueType):
    """"""

    def __init__(self, wrapper: object, handle: IntPtr):
        """:param wrapper:
        :param handle:
        """
    @property
    def Handle(self) -> IntPtr:
        """:return:"""
    @property
    def Wrapper(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def ToIntPtr(cls, value: HandleRef) -> IntPtr:
        """:param value:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""
    @classmethod
    def op_Explicit(cls, value: HandleRef) -> IntPtr:
        """:param value:
        :return:
        """

class ICustomAdapter:
    """"""

    def GetUnderlyingObject(self) -> object:
        """:return:"""

class ICustomFactory:
    """"""

    def CreateInstance(self, serverType: Type) -> MarshalByRefObject:
        """:param serverType:
        :return:
        """

class ICustomMarshaler:
    """"""

    def CleanUpManagedData(self, ManagedObj: object) -> None:
        """:param ManagedObj:"""
    def CleanUpNativeData(self, pNativeData: IntPtr) -> None:
        """:param pNativeData:"""
    def GetNativeDataSize(self) -> int:
        """:return:"""
    def MarshalManagedToNative(self, ManagedObj: object) -> IntPtr:
        """:param ManagedObj:
        :return:
        """
    def MarshalNativeToManaged(self, pNativeData: IntPtr) -> object:
        """:param pNativeData:
        :return:
        """

class ICustomQueryInterface:
    """"""

    def GetInterface(self, iid: Guid, ppv: IntPtr) -> tuple[CustomQueryInterfaceResult, IntPtr]:
        """:param iid:
        :param ppv:
        :return:
        """

class IDLDESC(ValueType):
    """"""

    dwReserved: Final[int] = ...
    """
    
    :return: 
    """
    wIDLFlags: Final[IDLFLAG] = ...
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
    def __init__(self, implType: IDispatchImplType):
        """:param implType:"""
    @overload
    def __init__(self, implType: int):
        """:param implType:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    @property
    def Value(self) -> IDispatchImplType:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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
        """:return:"""
    def GetProgIdForType(self, type: Type) -> str:
        """:param type:
        :return:
        """
    def GetRegistrableTypesInAssembly(self, assembly: Assembly) -> Array[Type]:
        """:param assembly:
        :return:
        """
    def RegisterAssembly(self, assembly: Assembly, flags: AssemblyRegistrationFlags) -> bool:
        """:param assembly:
        :param flags:
        :return:
        """
    def RegisterTypeForComClients(self, type: Type, g: Guid) -> None:
        """:param type:
        :param g:
        """
    def TypeRepresentsComType(self, type: Type) -> bool:
        """:param type:
        :return:
        """
    def TypeRequiresRegistration(self, type: Type) -> bool:
        """:param type:
        :return:
        """
    def UnregisterAssembly(self, assembly: Assembly) -> bool:
        """:param assembly:
        :return:
        """

class ITypeLibConverter:
    """"""

    def ConvertAssemblyToTypeLib(
        self,
        assembly: Assembly,
        typeLibName: str,
        flags: TypeLibExporterFlags,
        notifySink: ITypeLibExporterNotifySink,
    ) -> object:
        """:param assembly:
        :param typeLibName:
        :param flags:
        :param notifySink:
        :return:
        """
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
        """:param typeLib:
        :param asmFileName:
        :param flags:
        :param notifySink:
        :param publicKey:
        :param keyPair:
        :param unsafeInterfaces:
        :return:
        """
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
        """:param typeLib:
        :param asmFileName:
        :param flags:
        :param notifySink:
        :param publicKey:
        :param keyPair:
        :param asmNamespace:
        :param asmVersion:
        :return:
        """
    def GetPrimaryInteropAssembly(
        self, g: Guid, major: int, minor: int, lcid: int, asmName: str, asmCodeBase: str
    ) -> tuple[bool, str, str]:
        """:param g:
        :param major:
        :param minor:
        :param lcid:
        :param asmName:
        :param asmCodeBase:
        :return:
        """

class ITypeLibExporterNameProvider:
    """"""

    def GetNames(self) -> Array[str]:
        """:return:"""

class ITypeLibExporterNotifySink:
    """"""

    def ReportEvent(self, eventKind: ExporterEventKind, eventCode: int, eventMsg: str) -> None:
        """:param eventKind:
        :param eventCode:
        :param eventMsg:
        """
    def ResolveRef(self, assembly: Assembly) -> object:
        """:param assembly:
        :return:
        """

class ITypeLibImporterNotifySink:
    """"""

    def ReportEvent(self, eventKind: ImporterEventKind, eventCode: int, eventMsg: str) -> None:
        """:param eventKind:
        :param eventCode:
        :param eventMsg:
        """
    def ResolveRef(self, typeLib: object) -> Assembly:
        """:param typeLib:
        :return:
        """

class ImportedFromTypeLibAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, tlbFile: str):
        """:param tlbFile:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    @property
    def Value(self) -> str:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class ImporterCallback(Object, ITypeLibImporterNotifySink):
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
    def ReportEvent(self, eventKind: ImporterEventKind, eventCode: int, eventMsg: str) -> None:
        """:param eventKind:
        :param eventCode:
        :param eventMsg:
        """
    def ResolveRef(self, typeLib: object) -> Assembly:
        """:param typeLib:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class InterfaceTypeAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, interfaceType: ComInterfaceType):
        """:param interfaceType:"""
    @overload
    def __init__(self, interfaceType: int):
        """:param interfaceType:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    @property
    def Value(self) -> ComInterfaceType:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class InvalidComObjectException(SystemException, _Exception, ISerializable):
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

class InvalidOleVariantTypeException(SystemException, _Exception, ISerializable):
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

class LCIDConversionAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, lcid: int):
        """:param lcid:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    @property
    def Value(self) -> int:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

    def __init__(self, classType: Type, methodName: str):
        """:param classType:
        :param methodName:
        """
    @property
    def ClassType(self) -> Type:
        """:return:"""
    @property
    def MethodName(self) -> str:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class Marshal(ABC, Object):
    """"""

    SystemDefaultCharSize: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SystemMaxDBCSCharSize: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @classmethod
    def AddRef(cls, pUnk: IntPtr) -> int:
        """:param pUnk:
        :return:
        """
    @classmethod
    def AllocCoTaskMem(cls, cb: int) -> IntPtr:
        """:param cb:
        :return:
        """
    @classmethod
    @overload
    def AllocHGlobal(cls, cb: int) -> IntPtr:
        """:param cb:
        :return:
        """
    @classmethod
    @overload
    def AllocHGlobal(cls, cb: IntPtr) -> IntPtr:
        """:param cb:
        :return:
        """
    @classmethod
    def AreComObjectsAvailableForCleanup(cls) -> bool:
        """:return:"""
    @classmethod
    def BindToMoniker(cls, monikerName: str) -> object:
        """:param monikerName:
        :return:
        """
    @classmethod
    def ChangeWrapperHandleStrength(cls, otp: object, fIsWeak: bool) -> None:
        """:param otp:
        :param fIsWeak:
        """
    @classmethod
    def CleanupUnusedObjectsInCurrentContext(cls) -> None:
        """"""
    @classmethod
    @overload
    def Copy(cls, source: Array[int], startIndex: int, destination: IntPtr, length: int) -> None:
        """:param source:
        :param startIndex:
        :param destination:
        :param length:
        """
    @classmethod
    @overload
    def Copy(cls, source: Array[Char], startIndex: int, destination: IntPtr, length: int) -> None:
        """:param source:
        :param startIndex:
        :param destination:
        :param length:
        """
    @classmethod
    @overload
    def Copy(cls, source: Array[float], startIndex: int, destination: IntPtr, length: int) -> None:
        """:param source:
        :param startIndex:
        :param destination:
        :param length:
        """
    @classmethod
    @overload
    def Copy(cls, source: Array[int], startIndex: int, destination: IntPtr, length: int) -> None:
        """:param source:
        :param startIndex:
        :param destination:
        :param length:
        """
    @classmethod
    @overload
    def Copy(cls, source: Array[int], startIndex: int, destination: IntPtr, length: int) -> None:
        """:param source:
        :param startIndex:
        :param destination:
        :param length:
        """
    @classmethod
    @overload
    def Copy(cls, source: Array[int], startIndex: int, destination: IntPtr, length: int) -> None:
        """:param source:
        :param startIndex:
        :param destination:
        :param length:
        """
    @classmethod
    @overload
    def Copy(cls, source: Array[IntPtr], startIndex: int, destination: IntPtr, length: int) -> None:
        """:param source:
        :param startIndex:
        :param destination:
        :param length:
        """
    @classmethod
    @overload
    def Copy(cls, source: Array[float], startIndex: int, destination: IntPtr, length: int) -> None:
        """:param source:
        :param startIndex:
        :param destination:
        :param length:
        """
    @classmethod
    @overload
    def Copy(cls, source: IntPtr, destination: Array[int], startIndex: int, length: int) -> None:
        """:param source:
        :param destination:
        :param startIndex:
        :param length:
        """
    @classmethod
    @overload
    def Copy(cls, source: IntPtr, destination: Array[Char], startIndex: int, length: int) -> None:
        """:param source:
        :param destination:
        :param startIndex:
        :param length:
        """
    @classmethod
    @overload
    def Copy(cls, source: IntPtr, destination: Array[float], startIndex: int, length: int) -> None:
        """:param source:
        :param destination:
        :param startIndex:
        :param length:
        """
    @classmethod
    @overload
    def Copy(cls, source: IntPtr, destination: Array[int], startIndex: int, length: int) -> None:
        """:param source:
        :param destination:
        :param startIndex:
        :param length:
        """
    @classmethod
    @overload
    def Copy(cls, source: IntPtr, destination: Array[int], startIndex: int, length: int) -> None:
        """:param source:
        :param destination:
        :param startIndex:
        :param length:
        """
    @classmethod
    @overload
    def Copy(cls, source: IntPtr, destination: Array[int], startIndex: int, length: int) -> None:
        """:param source:
        :param destination:
        :param startIndex:
        :param length:
        """
    @classmethod
    @overload
    def Copy(cls, source: IntPtr, destination: Array[IntPtr], startIndex: int, length: int) -> None:
        """:param source:
        :param destination:
        :param startIndex:
        :param length:
        """
    @classmethod
    @overload
    def Copy(cls, source: IntPtr, destination: Array[float], startIndex: int, length: int) -> None:
        """:param source:
        :param destination:
        :param startIndex:
        :param length:
        """
    @classmethod
    @overload
    def CreateAggregatedObject(cls, pOuter: IntPtr, o: T) -> IntPtr:
        """:param pOuter:
        :param o:
        :return:
        """
    @classmethod
    @overload
    def CreateAggregatedObject(cls, pOuter: IntPtr, o: object) -> IntPtr:
        """:param pOuter:
        :param o:
        :return:
        """
    @classmethod
    @overload
    def CreateWrapperOfType(cls, o: T) -> TWrapper:
        """:param o:
        :return:
        """
    @classmethod
    @overload
    def CreateWrapperOfType(cls, o: object, t: Type) -> object:
        """:param o:
        :param t:
        :return:
        """
    @classmethod
    @overload
    def DestroyStructure(cls, ptr: IntPtr) -> None:
        """:param ptr:"""
    @classmethod
    @overload
    def DestroyStructure(cls, ptr: IntPtr, structuretype: Type) -> None:
        """:param ptr:
        :param structuretype:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    def FinalReleaseComObject(cls, o: object) -> int:
        """:param o:
        :return:
        """
    @classmethod
    def FreeBSTR(cls, ptr: IntPtr) -> None:
        """:param ptr:"""
    @classmethod
    def FreeCoTaskMem(cls, ptr: IntPtr) -> None:
        """:param ptr:"""
    @classmethod
    def FreeHGlobal(cls, hglobal: IntPtr) -> None:
        """:param hglobal:"""
    @classmethod
    def GenerateGuidForType(cls, type: Type) -> Guid:
        """:param type:
        :return:
        """
    @classmethod
    def GenerateProgIdForType(cls, type: Type) -> str:
        """:param type:
        :return:
        """
    @classmethod
    def GetActiveObject(cls, progID: str) -> object:
        """:param progID:
        :return:
        """
    @classmethod
    @overload
    def GetComInterfaceForObject(cls, o: T) -> IntPtr:
        """:param o:
        :return:
        """
    @classmethod
    @overload
    def GetComInterfaceForObject(cls, o: object, T: Type) -> IntPtr:
        """:param o:
        :param T:
        :return:
        """
    @classmethod
    @overload
    def GetComInterfaceForObject(cls, o: object, T: Type, mode: CustomQueryInterfaceMode) -> IntPtr:
        """:param o:
        :param T:
        :param mode:
        :return:
        """
    @classmethod
    def GetComInterfaceForObjectInContext(cls, o: object, t: Type) -> IntPtr:
        """:param o:
        :param t:
        :return:
        """
    @classmethod
    def GetComObjectData(cls, obj: object, key: object) -> object:
        """:param obj:
        :param key:
        :return:
        """
    @classmethod
    def GetComSlotForMethodInfo(cls, m: MemberInfo) -> int:
        """:param m:
        :return:
        """
    @classmethod
    @overload
    def GetDelegateForFunctionPointer(cls, ptr: IntPtr) -> TDelegate:
        """:param ptr:
        :return:
        """
    @classmethod
    @overload
    def GetDelegateForFunctionPointer(cls, ptr: IntPtr, t: Type) -> Delegate:
        """:param ptr:
        :param t:
        :return:
        """
    @classmethod
    def GetEndComSlot(cls, t: Type) -> int:
        """:param t:
        :return:
        """
    @classmethod
    def GetExceptionCode(cls) -> int:
        """:return:"""
    @classmethod
    @overload
    def GetExceptionForHR(cls, errorCode: int) -> Exception:
        """:param errorCode:
        :return:
        """
    @classmethod
    @overload
    def GetExceptionForHR(cls, errorCode: int, errorInfo: IntPtr) -> Exception:
        """:param errorCode:
        :param errorInfo:
        :return:
        """
    @classmethod
    def GetExceptionPointers(cls) -> IntPtr:
        """:return:"""
    @classmethod
    @overload
    def GetFunctionPointerForDelegate(cls, d: TDelegate) -> IntPtr:
        """:param d:
        :return:
        """
    @classmethod
    @overload
    def GetFunctionPointerForDelegate(cls, d: Delegate) -> IntPtr:
        """:param d:
        :return:
        """
    @classmethod
    def GetHINSTANCE(cls, m: Module) -> IntPtr:
        """:param m:
        :return:
        """
    @classmethod
    def GetHRForException(cls, e: Exception) -> int:
        """:param e:
        :return:
        """
    @classmethod
    def GetHRForLastWin32Error(cls) -> int:
        """:return:"""
    def GetHashCode(self) -> int:
        """:return:"""
    @classmethod
    def GetIDispatchForObject(cls, o: object) -> IntPtr:
        """:param o:
        :return:
        """
    @classmethod
    def GetIDispatchForObjectInContext(cls, o: object) -> IntPtr:
        """:param o:
        :return:
        """
    @classmethod
    def GetITypeInfoForType(cls, t: Type) -> IntPtr:
        """:param t:
        :return:
        """
    @classmethod
    def GetIUnknownForObject(cls, o: object) -> IntPtr:
        """:param o:
        :return:
        """
    @classmethod
    def GetIUnknownForObjectInContext(cls, o: object) -> IntPtr:
        """:param o:
        :return:
        """
    @classmethod
    def GetLastWin32Error(cls) -> int:
        """:return:"""
    @classmethod
    def GetManagedThunkForUnmanagedMethodPtr(
        cls, pfnMethodToWrap: IntPtr, pbSignature: IntPtr, cbSignature: int
    ) -> IntPtr:
        """:param pfnMethodToWrap:
        :param pbSignature:
        :param cbSignature:
        :return:
        """
    @classmethod
    def GetMethodInfoForComSlot(cls, t: Type, slot: int, memberType: ComMemberType) -> MemberInfo:
        """:param t:
        :param slot:
        :param memberType:
        :return:
        """
    @classmethod
    @overload
    def GetNativeVariantForObject(cls, obj: T, pDstNativeVariant: IntPtr) -> None:
        """:param obj:
        :param pDstNativeVariant:
        """
    @classmethod
    @overload
    def GetNativeVariantForObject(cls, obj: object, pDstNativeVariant: IntPtr) -> None:
        """:param obj:
        :param pDstNativeVariant:
        """
    @classmethod
    def GetObjectForIUnknown(cls, pUnk: IntPtr) -> object:
        """:param pUnk:
        :return:
        """
    @classmethod
    def GetObjectForNativeVariant(cls, pSrcNativeVariant: IntPtr) -> T:
        """:param pSrcNativeVariant:
        :return:
        """
    @classmethod
    def GetObjectsForNativeVariants(cls, aSrcNativeVariant: IntPtr, cVars: int) -> Array[T]:
        """:param aSrcNativeVariant:
        :param cVars:
        :return:
        """
    @classmethod
    def GetStartComSlot(cls, t: Type) -> int:
        """:param t:
        :return:
        """
    @classmethod
    def GetThreadFromFiberCookie(cls, cookie: int) -> Thread:
        """:param cookie:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def GetTypeForITypeInfo(cls, piTypeInfo: IntPtr) -> Type:
        """:param piTypeInfo:
        :return:
        """
    @classmethod
    def GetTypeFromCLSID(cls, clsid: Guid) -> Type:
        """:param clsid:
        :return:
        """
    @classmethod
    @overload
    def GetTypeInfoName(cls, typeInfo: ITypeInfo) -> str:
        """:param typeInfo:
        :return:
        """
    @classmethod
    @overload
    def GetTypeInfoName(cls, pTI: UCOMITypeInfo) -> str:
        """:param pTI:
        :return:
        """
    @classmethod
    @overload
    def GetTypeLibGuid(cls, typelib: ITypeLib) -> Guid:
        """:param typelib:
        :return:
        """
    @classmethod
    @overload
    def GetTypeLibGuid(cls, pTLB: UCOMITypeLib) -> Guid:
        """:param pTLB:
        :return:
        """
    @classmethod
    def GetTypeLibGuidForAssembly(cls, asm: Assembly) -> Guid:
        """:param asm:
        :return:
        """
    @classmethod
    @overload
    def GetTypeLibLcid(cls, typelib: ITypeLib) -> int:
        """:param typelib:
        :return:
        """
    @classmethod
    @overload
    def GetTypeLibLcid(cls, pTLB: UCOMITypeLib) -> int:
        """:param pTLB:
        :return:
        """
    @classmethod
    @overload
    def GetTypeLibName(cls, typelib: ITypeLib) -> str:
        """:param typelib:
        :return:
        """
    @classmethod
    @overload
    def GetTypeLibName(cls, pTLB: UCOMITypeLib) -> str:
        """:param pTLB:
        :return:
        """
    @classmethod
    def GetTypeLibVersionForAssembly(
        cls, inputAssembly: Assembly, majorVersion: int, minorVersion: int
    ) -> tuple[None, int, int]:
        """:param inputAssembly:
        :param majorVersion:
        :param minorVersion:
        """
    @classmethod
    def GetTypedObjectForIUnknown(cls, pUnk: IntPtr, t: Type) -> object:
        """:param pUnk:
        :param t:
        :return:
        """
    @classmethod
    def GetUniqueObjectForIUnknown(cls, unknown: IntPtr) -> object:
        """:param unknown:
        :return:
        """
    @classmethod
    def GetUnmanagedThunkForManagedMethodPtr(
        cls, pfnMethodToWrap: IntPtr, pbSignature: IntPtr, cbSignature: int
    ) -> IntPtr:
        """:param pfnMethodToWrap:
        :param pbSignature:
        :param cbSignature:
        :return:
        """
    @classmethod
    def IsComObject(cls, o: object) -> bool:
        """:param o:
        :return:
        """
    @classmethod
    def IsTypeVisibleFromCom(cls, t: Type) -> bool:
        """:param t:
        :return:
        """
    @classmethod
    def NumParamBytes(cls, m: MethodInfo) -> int:
        """:param m:
        :return:
        """
    @classmethod
    @overload
    def OffsetOf(cls, fieldName: str) -> IntPtr:
        """:param fieldName:
        :return:
        """
    @classmethod
    @overload
    def OffsetOf(cls, t: Type, fieldName: str) -> IntPtr:
        """:param t:
        :param fieldName:
        :return:
        """
    @classmethod
    def Prelink(cls, m: MethodInfo) -> None:
        """:param m:"""
    @classmethod
    def PrelinkAll(cls, c: Type) -> None:
        """:param c:"""
    @classmethod
    @overload
    def PtrToStringAnsi(cls, ptr: IntPtr) -> str:
        """:param ptr:
        :return:
        """
    @classmethod
    @overload
    def PtrToStringAnsi(cls, ptr: IntPtr, len: int) -> str:
        """:param ptr:
        :param len:
        :return:
        """
    @classmethod
    @overload
    def PtrToStringAuto(cls, ptr: IntPtr) -> str:
        """:param ptr:
        :return:
        """
    @classmethod
    @overload
    def PtrToStringAuto(cls, ptr: IntPtr, len: int) -> str:
        """:param ptr:
        :param len:
        :return:
        """
    @classmethod
    def PtrToStringBSTR(cls, ptr: IntPtr) -> str:
        """:param ptr:
        :return:
        """
    @classmethod
    @overload
    def PtrToStringUni(cls, ptr: IntPtr) -> str:
        """:param ptr:
        :return:
        """
    @classmethod
    @overload
    def PtrToStringUni(cls, ptr: IntPtr, len: int) -> str:
        """:param ptr:
        :param len:
        :return:
        """
    @classmethod
    @overload
    def PtrToStructure(cls, ptr: IntPtr) -> T:
        """:param ptr:
        :return:
        """
    @classmethod
    @overload
    def PtrToStructure(cls, ptr: IntPtr, structure: T) -> None:
        """:param ptr:
        :param structure:
        """
    @classmethod
    @overload
    def PtrToStructure(cls, ptr: IntPtr, structure: object) -> None:
        """:param ptr:
        :param structure:
        """
    @classmethod
    @overload
    def PtrToStructure(cls, ptr: IntPtr, structureType: Type) -> object:
        """:param ptr:
        :param structureType:
        :return:
        """
    @classmethod
    def QueryInterface(cls, pUnk: IntPtr, iid: Guid, ppv: IntPtr) -> tuple[int, IntPtr]:
        """:param pUnk:
        :param iid:
        :param ppv:
        :return:
        """
    @classmethod
    def ReAllocCoTaskMem(cls, pv: IntPtr, cb: int) -> IntPtr:
        """:param pv:
        :param cb:
        :return:
        """
    @classmethod
    def ReAllocHGlobal(cls, pv: IntPtr, cb: IntPtr) -> IntPtr:
        """:param pv:
        :param cb:
        :return:
        """
    @classmethod
    @overload
    def ReadByte(cls, ptr: IntPtr) -> int:
        """:param ptr:
        :return:
        """
    @classmethod
    @overload
    def ReadByte(cls, ptr: IntPtr, ofs: int) -> int:
        """:param ptr:
        :param ofs:
        :return:
        """
    @classmethod
    @overload
    def ReadByte(cls, ptr: object, ofs: int) -> int:
        """:param ptr:
        :param ofs:
        :return:
        """
    @classmethod
    @overload
    def ReadInt16(cls, ptr: IntPtr) -> int:
        """:param ptr:
        :return:
        """
    @classmethod
    @overload
    def ReadInt16(cls, ptr: IntPtr, ofs: int) -> int:
        """:param ptr:
        :param ofs:
        :return:
        """
    @classmethod
    @overload
    def ReadInt16(cls, ptr: object, ofs: int) -> int:
        """:param ptr:
        :param ofs:
        :return:
        """
    @classmethod
    @overload
    def ReadInt32(cls, ptr: IntPtr) -> int:
        """:param ptr:
        :return:
        """
    @classmethod
    @overload
    def ReadInt32(cls, ptr: IntPtr, ofs: int) -> int:
        """:param ptr:
        :param ofs:
        :return:
        """
    @classmethod
    @overload
    def ReadInt32(cls, ptr: object, ofs: int) -> int:
        """:param ptr:
        :param ofs:
        :return:
        """
    @classmethod
    @overload
    def ReadInt64(cls, ptr: IntPtr) -> int:
        """:param ptr:
        :return:
        """
    @classmethod
    @overload
    def ReadInt64(cls, ptr: IntPtr, ofs: int) -> int:
        """:param ptr:
        :param ofs:
        :return:
        """
    @classmethod
    @overload
    def ReadInt64(cls, ptr: object, ofs: int) -> int:
        """:param ptr:
        :param ofs:
        :return:
        """
    @classmethod
    @overload
    def ReadIntPtr(cls, ptr: IntPtr) -> IntPtr:
        """:param ptr:
        :return:
        """
    @classmethod
    @overload
    def ReadIntPtr(cls, ptr: IntPtr, ofs: int) -> IntPtr:
        """:param ptr:
        :param ofs:
        :return:
        """
    @classmethod
    @overload
    def ReadIntPtr(cls, ptr: object, ofs: int) -> IntPtr:
        """:param ptr:
        :param ofs:
        :return:
        """
    @classmethod
    def Release(cls, pUnk: IntPtr) -> int:
        """:param pUnk:
        :return:
        """
    @classmethod
    def ReleaseComObject(cls, o: object) -> int:
        """:param o:
        :return:
        """
    @classmethod
    def ReleaseThreadCache(cls) -> None:
        """"""
    @classmethod
    def SecureStringToBSTR(cls, s: SecureString) -> IntPtr:
        """:param s:
        :return:
        """
    @classmethod
    def SecureStringToCoTaskMemAnsi(cls, s: SecureString) -> IntPtr:
        """:param s:
        :return:
        """
    @classmethod
    def SecureStringToCoTaskMemUnicode(cls, s: SecureString) -> IntPtr:
        """:param s:
        :return:
        """
    @classmethod
    def SecureStringToGlobalAllocAnsi(cls, s: SecureString) -> IntPtr:
        """:param s:
        :return:
        """
    @classmethod
    def SecureStringToGlobalAllocUnicode(cls, s: SecureString) -> IntPtr:
        """:param s:
        :return:
        """
    @classmethod
    def SetComObjectData(cls, obj: object, key: object, data: object) -> bool:
        """:param obj:
        :param key:
        :param data:
        :return:
        """
    @classmethod
    @overload
    def SizeOf(cls) -> int:
        """:return:"""
    @classmethod
    @overload
    def SizeOf(cls, structure: T) -> int:
        """:param structure:
        :return:
        """
    @classmethod
    @overload
    def SizeOf(cls, structure: object) -> int:
        """:param structure:
        :return:
        """
    @classmethod
    @overload
    def SizeOf(cls, t: Type) -> int:
        """:param t:
        :return:
        """
    @classmethod
    def StringToBSTR(cls, s: str) -> IntPtr:
        """:param s:
        :return:
        """
    @classmethod
    def StringToCoTaskMemAnsi(cls, s: str) -> IntPtr:
        """:param s:
        :return:
        """
    @classmethod
    def StringToCoTaskMemAuto(cls, s: str) -> IntPtr:
        """:param s:
        :return:
        """
    @classmethod
    def StringToCoTaskMemUni(cls, s: str) -> IntPtr:
        """:param s:
        :return:
        """
    @classmethod
    def StringToHGlobalAnsi(cls, s: str) -> IntPtr:
        """:param s:
        :return:
        """
    @classmethod
    def StringToHGlobalAuto(cls, s: str) -> IntPtr:
        """:param s:
        :return:
        """
    @classmethod
    def StringToHGlobalUni(cls, s: str) -> IntPtr:
        """:param s:
        :return:
        """
    @classmethod
    @overload
    def StructureToPtr(cls, structure: T, ptr: IntPtr, fDeleteOld: bool) -> None:
        """:param structure:
        :param ptr:
        :param fDeleteOld:
        """
    @classmethod
    @overload
    def StructureToPtr(cls, structure: object, ptr: IntPtr, fDeleteOld: bool) -> None:
        """:param structure:
        :param ptr:
        :param fDeleteOld:
        """
    @classmethod
    @overload
    def ThrowExceptionForHR(cls, errorCode: int) -> None:
        """:param errorCode:"""
    @classmethod
    @overload
    def ThrowExceptionForHR(cls, errorCode: int, errorInfo: IntPtr) -> None:
        """:param errorCode:
        :param errorInfo:
        """
    def ToString(self) -> str:
        """:return:"""
    @classmethod
    @overload
    def UnsafeAddrOfPinnedArrayElement(cls, arr: Array, index: int) -> IntPtr:
        """:param arr:
        :param index:
        :return:
        """
    @classmethod
    @overload
    def UnsafeAddrOfPinnedArrayElement(cls, arr: Array[T], index: int) -> IntPtr:
        """:param arr:
        :param index:
        :return:
        """
    @classmethod
    @overload
    def WriteByte(cls, ptr: IntPtr, val: int) -> None:
        """:param ptr:
        :param val:
        """
    @classmethod
    @overload
    def WriteByte(cls, ptr: IntPtr, ofs: int, val: int) -> None:
        """:param ptr:
        :param ofs:
        :param val:
        """
    @classmethod
    @overload
    def WriteByte(cls, ptr: object, ofs: int, val: int) -> tuple[None, object]:
        """:param ptr:
        :param ofs:
        :param val:
        """
    @classmethod
    @overload
    def WriteInt16(cls, ptr: IntPtr, val: Char) -> None:
        """:param ptr:
        :param val:
        """
    @classmethod
    @overload
    def WriteInt16(cls, ptr: IntPtr, val: int) -> None:
        """:param ptr:
        :param val:
        """
    @classmethod
    @overload
    def WriteInt16(cls, ptr: IntPtr, ofs: int, val: Char) -> None:
        """:param ptr:
        :param ofs:
        :param val:
        """
    @classmethod
    @overload
    def WriteInt16(cls, ptr: IntPtr, ofs: int, val: int) -> None:
        """:param ptr:
        :param ofs:
        :param val:
        """
    @classmethod
    @overload
    def WriteInt16(cls, ptr: object, ofs: int, val: Char) -> tuple[None, object]:
        """:param ptr:
        :param ofs:
        :param val:
        """
    @classmethod
    @overload
    def WriteInt16(cls, ptr: object, ofs: int, val: int) -> tuple[None, object]:
        """:param ptr:
        :param ofs:
        :param val:
        """
    @classmethod
    @overload
    def WriteInt32(cls, ptr: IntPtr, val: int) -> None:
        """:param ptr:
        :param val:
        """
    @classmethod
    @overload
    def WriteInt32(cls, ptr: IntPtr, ofs: int, val: int) -> None:
        """:param ptr:
        :param ofs:
        :param val:
        """
    @classmethod
    @overload
    def WriteInt32(cls, ptr: object, ofs: int, val: int) -> tuple[None, object]:
        """:param ptr:
        :param ofs:
        :param val:
        """
    @classmethod
    @overload
    def WriteInt64(cls, ptr: IntPtr, val: int) -> None:
        """:param ptr:
        :param val:
        """
    @classmethod
    @overload
    def WriteInt64(cls, ptr: IntPtr, ofs: int, val: int) -> None:
        """:param ptr:
        :param ofs:
        :param val:
        """
    @classmethod
    @overload
    def WriteInt64(cls, ptr: object, ofs: int, val: int) -> tuple[None, object]:
        """:param ptr:
        :param ofs:
        :param val:
        """
    @classmethod
    @overload
    def WriteIntPtr(cls, ptr: IntPtr, val: IntPtr) -> None:
        """:param ptr:
        :param val:
        """
    @classmethod
    @overload
    def WriteIntPtr(cls, ptr: IntPtr, ofs: int, val: IntPtr) -> None:
        """:param ptr:
        :param ofs:
        :param val:
        """
    @classmethod
    @overload
    def WriteIntPtr(cls, ptr: object, ofs: int, val: IntPtr) -> tuple[None, object]:
        """:param ptr:
        :param ofs:
        :param val:
        """
    @classmethod
    def ZeroFreeBSTR(cls, s: IntPtr) -> None:
        """:param s:"""
    @classmethod
    def ZeroFreeCoTaskMemAnsi(cls, s: IntPtr) -> None:
        """:param s:"""
    @classmethod
    def ZeroFreeCoTaskMemUnicode(cls, s: IntPtr) -> None:
        """:param s:"""
    @classmethod
    def ZeroFreeGlobalAllocAnsi(cls, s: IntPtr) -> None:
        """:param s:"""
    @classmethod
    def ZeroFreeGlobalAllocUnicode(cls, s: IntPtr) -> None:
        """:param s:"""

class MarshalAsAttribute(Attribute, _Attribute):
    """"""

    ArraySubType: Final[UnmanagedType] = ...
    """
    
    :return: 
    """
    IidParameterIndex: Final[int] = ...
    """
    
    :return: 
    """
    MarshalCookie: Final[str] = ...
    """
    
    :return: 
    """
    MarshalType: Final[str] = ...
    """
    
    :return: 
    """
    MarshalTypeRef: Final[Type] = ...
    """
    
    :return: 
    """
    SafeArraySubType: Final[VarEnum] = ...
    """
    
    :return: 
    """
    SafeArrayUserDefinedSubType: Final[Type] = ...
    """
    
    :return: 
    """
    SizeConst: Final[int] = ...
    """
    
    :return: 
    """
    SizeParamIndex: Final[int] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, unmanagedType: UnmanagedType):
        """:param unmanagedType:"""
    @overload
    def __init__(self, unmanagedType: int):
        """:param unmanagedType:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    @property
    def Value(self) -> UnmanagedType:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class MarshalDirectiveException(SystemException, _Exception, ISerializable):
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

class NativeBuffer(Object, IDisposable):
    """"""

    def __init__(self, initialMinCapacity: int = ...):
        """:param initialMinCapacity:"""
    @property
    def ByteCapacity(self) -> int:
        """:return:"""
    @property
    def Item(self) -> int:
        """:return:"""
    @Item.setter
    def Item(self, value: int) -> None: ...
    def Dispose(self) -> None:
        """"""
    def EnsureByteCapacity(self, minCapacity: int) -> None:
        """:param minCapacity:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def Free(self) -> None:
        """"""
    def GetHandle(self) -> SafeHandle:
        """:return:"""
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def __getitem__(self, index: int) -> int:
        """:param index:
        :return:
        """
    def __setitem__(self, index: int, value: int) -> None:
        """:param index:
        :param value:
        """

class NativeMethods(ABC, Object):
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

class OSPlatform(ValueType, IEquatable[OSPlatform]):
    """"""

    @classmethod
    @property
    def Linux(cls) -> OSPlatform:
        """:return:"""
    @classmethod
    @property
    def OSX(cls) -> OSPlatform:
        """:return:"""
    @classmethod
    @property
    def Windows(cls) -> OSPlatform:
        """:return:"""
    @classmethod
    def Create(cls, osPlatform: str) -> OSPlatform:
        """:param osPlatform:
        :return:
        """
    @overload
    def Equals(self, other: OSPlatform) -> bool:
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
    def ToString(self) -> str:
        """:return:"""
    def __eq__(self, other: OSPlatform) -> bool:
        """:param other:
        :return:
        """
    def __ne__(self, other: OSPlatform) -> bool:
        """:param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: OSPlatform, right: OSPlatform) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: OSPlatform, right: OSPlatform) -> bool:
        """:param left:
        :param right:
        :return:
        """

ObjectCreationDelegate: Callable[[IntPtr], IntPtr] = ...
"""

:param aggregator: 
:return: 
"""

class OptionalAttribute(Attribute, _Attribute):
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class OutAttribute(Attribute, _Attribute):
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class PARAMDESC(ValueType):
    """"""

    lpVarValue: Final[IntPtr] = ...
    """
    
    :return: 
    """
    wParamFlags: Final[PARAMFLAG] = ...
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class PrimaryInteropAssemblyAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, major: int, minor: int):
        """:param major:
        :param minor:
        """
    @property
    def MajorVersion(self) -> int:
        """:return:"""
    @property
    def MinorVersion(self) -> int:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class ProgIdAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, progId: str):
        """:param progId:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    @property
    def Value(self) -> str:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetManagedCategoryGuid(self) -> Guid:
        """:return:"""
    def GetProgIdForType(self, type: Type) -> str:
        """:param type:
        :return:
        """
    def GetRegistrableTypesInAssembly(self, assembly: Assembly) -> Array[Type]:
        """:param assembly:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def RegisterAssembly(self, assembly: Assembly, flags: AssemblyRegistrationFlags) -> bool:
        """:param assembly:
        :param flags:
        :return:
        """
    @overload
    def RegisterTypeForComClients(self, type: Type, g: Guid) -> None:
        """:param type:
        :param g:
        """
    @overload
    def RegisterTypeForComClients(
        self,
        type: Type,
        classContext: RegistrationClassContext,
        flags: RegistrationConnectionType,
    ) -> int:
        """:param type:
        :param classContext:
        :param flags:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""
    def TypeRepresentsComType(self, type: Type) -> bool:
        """:param type:
        :return:
        """
    def TypeRequiresRegistration(self, type: Type) -> bool:
        """:param type:
        :return:
        """
    def UnregisterAssembly(self, assembly: Assembly) -> bool:
        """:param assembly:
        :return:
        """
    def UnregisterTypeForComClients(self, cookie: int) -> None:
        """:param cookie:"""

class RuntimeEnvironment(Object):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def SystemConfigurationFile(cls) -> str:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    def FromGlobalAccessCache(cls, a: Assembly) -> bool:
        """:param a:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    @classmethod
    def GetRuntimeDirectory(cls) -> str:
        """:return:"""
    @classmethod
    def GetRuntimeInterfaceAsIntPtr(cls, clsid: Guid, riid: Guid) -> IntPtr:
        """:param clsid:
        :param riid:
        :return:
        """
    @classmethod
    def GetRuntimeInterfaceAsObject(cls, clsid: Guid, riid: Guid) -> object:
        """:param clsid:
        :param riid:
        :return:
        """
    @classmethod
    def GetSystemVersion(cls) -> str:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class RuntimeInformation(ABC, Object):
    """"""

    @classmethod
    @property
    def FrameworkDescription(cls) -> str:
        """:return:"""
    @classmethod
    @property
    def OSArchitecture(cls) -> Architecture:
        """:return:"""
    @classmethod
    @property
    def OSDescription(cls) -> str:
        """:return:"""
    @classmethod
    @property
    def ProcessArchitecture(cls) -> Architecture:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def IsOSPlatform(cls, osPlatform: OSPlatform) -> bool:
        """:param osPlatform:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class SEHException(ExternalException, _Exception, ISerializable):
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
    def ErrorCode(self) -> int:
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
    def CanResume(self) -> bool:
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

class STATSTG(ValueType):
    """"""

    atime: Final[FILETIME] = ...
    """
    
    :return: 
    """
    cbSize: Final[int] = ...
    """
    
    :return: 
    """
    clsid: Final[Guid] = ...
    """
    
    :return: 
    """
    ctime: Final[FILETIME] = ...
    """
    
    :return: 
    """
    grfLocksSupported: Final[int] = ...
    """
    
    :return: 
    """
    grfMode: Final[int] = ...
    """
    
    :return: 
    """
    grfStateBits: Final[int] = ...
    """
    
    :return: 
    """
    mtime: Final[FILETIME] = ...
    """
    
    :return: 
    """
    pwcsName: Final[str] = ...
    """
    
    :return: 
    """
    reserved: Final[int] = ...
    """
    
    :return: 
    """
    type: Final[int] = ...
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

class SafeArrayTypeMismatchException(SystemException, _Exception, ISerializable):
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

class SafeBuffer(ABC, SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    @property
    def ByteLength(self) -> int:
        """:return:"""
    @property
    def IsClosed(self) -> bool:
        """:return:"""
    @property
    def IsInvalid(self) -> bool:
        """:return:"""
    def AcquirePointer(self, pointer: int) -> None:
        """:param pointer:"""
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
    @overload
    def Initialize(self, numElements: int) -> None:
        """:param numElements:"""
    @overload
    def Initialize(self, numBytes: int) -> None:
        """:param numBytes:"""
    @overload
    def Initialize(self, numElements: int, sizeOfEachElement: int) -> None:
        """:param numElements:
        :param sizeOfEachElement:
        """
    def Read(self, byteOffset: int) -> T:
        """:param byteOffset:
        :return:
        """
    def ReadArray(self, byteOffset: int, array: Array[T], index: int, count: int) -> None:
        """:param byteOffset:
        :param array:
        :param index:
        :param count:
        """
    def ReleasePointer(self) -> None:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """:return:"""
    def Write(self, byteOffset: int, value: T) -> None:
        """:param byteOffset:
        :param value:
        """
    def WriteArray(self, byteOffset: int, array: Array[T], index: int, count: int) -> None:
        """:param byteOffset:
        :param array:
        :param index:
        :param count:
        """

class SafeHandle(ABC, CriticalFinalizerObject, IDisposable):
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

class SafeHeapHandle(SafeBuffer, IDisposable):
    """"""

    def __init__(self, byteLength: int):
        """:param byteLength:"""
    @property
    def ByteLength(self) -> int:
        """:return:"""
    @property
    def IsClosed(self) -> bool:
        """:return:"""
    @property
    def IsInvalid(self) -> bool:
        """:return:"""
    def AcquirePointer(self, pointer: int) -> None:
        """:param pointer:"""
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
    @overload
    def Initialize(self, numElements: int) -> None:
        """:param numElements:"""
    @overload
    def Initialize(self, numBytes: int) -> None:
        """:param numBytes:"""
    @overload
    def Initialize(self, numElements: int, sizeOfEachElement: int) -> None:
        """:param numElements:
        :param sizeOfEachElement:
        """
    def Read(self, byteOffset: int) -> T:
        """:param byteOffset:
        :return:
        """
    def ReadArray(self, byteOffset: int, array: Array[T], index: int, count: int) -> None:
        """:param byteOffset:
        :param array:
        :param index:
        :param count:
        """
    def ReleasePointer(self) -> None:
        """"""
    def Resize(self, byteLength: int) -> None:
        """:param byteLength:"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """:return:"""
    def Write(self, byteOffset: int, value: T) -> None:
        """:param byteOffset:
        :param value:
        """
    def WriteArray(self, byteOffset: int, array: Array[T], index: int, count: int) -> None:
        """:param byteOffset:
        :param array:
        :param index:
        :param count:
        """

class SafeHeapHandleCache(Object, IDisposable):
    """"""

    def __init__(self, minSize: int = ..., maxSize: int = ..., maxHandles: int = ...):
        """:param minSize:
        :param maxSize:
        :param maxHandles:
        """
    def Acquire(self, minSize: int = ...) -> SafeHeapHandle:
        """:param minSize:
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
    def GetType(self) -> Type:
        """:return:"""
    def Release(self, handle: SafeHeapHandle) -> None:
        """:param handle:"""
    def ToString(self) -> str:
        """:return:"""

class SetWin32ContextInIDispatchAttribute(Attribute, _Attribute):
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class StandardOleMarshalObject(MarshalByRefObject, UnsafeNativeMethods.IMarshal):
    """"""

    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """:param requestedType:
        :return:
        """
    def DisconnectObject(self, dwReserved: int) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetLifetimeService(self) -> object:
        """:return:"""
    def GetMarshalSizeMax(
        self,
        riid: Guid,
        pv: IntPtr,
        dwDestContext: int,
        pvDestContext: IntPtr,
        mshlflags: int,
        pSize: int,
    ) -> tuple[int, int]:
        """"""
    def GetType(self) -> Type:
        """:return:"""
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
        """:return:"""
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
        """:return:"""
    def UnmarshalInterface(self, pStm: IntPtr, riid: Guid, ppv: IntPtr) -> tuple[int, IntPtr]:
        """"""

class StringBuffer(NativeBuffer, IDisposable):
    """"""

    @overload
    def __init__(self, initialContents: StringBuffer):
        """:param initialContents:"""
    @overload
    def __init__(self, initialContents: str):
        """:param initialContents:"""
    @overload
    def __init__(self, initialCapacity: int = ...):
        """:param initialCapacity:"""
    @property
    def ByteCapacity(self) -> int:
        """:return:"""
    @property
    def CharCapacity(self) -> int:
        """:return:"""
    @property
    def Item(self) -> int:
        """:return:"""
    @Item.setter
    def Item(self, value: int) -> None: ...
    @property
    def Length(self) -> int:
        """:return:"""
    @Length.setter
    def Length(self, value: int) -> None: ...
    @overload
    def Append(self, value: StringBuffer, startIndex: int = ...) -> None:
        """:param value:
        :param startIndex:
        """
    @overload
    def Append(self, value: StringBuffer, startIndex: int, count: int) -> None:
        """:param value:
        :param startIndex:
        :param count:
        """
    @overload
    def Append(self, value: str, startIndex: int = ..., count: int = ...) -> None:
        """:param value:
        :param startIndex:
        :param count:
        """
    def Contains(self, value: Char) -> bool:
        """:param value:
        :return:
        """
    def CopyFrom(
        self, bufferIndex: int, source: str, sourceIndex: int = ..., count: int = ...
    ) -> None:
        """:param bufferIndex:
        :param source:
        :param sourceIndex:
        :param count:
        """
    def CopyTo(
        self,
        bufferIndex: int,
        destination: StringBuffer,
        destinationIndex: int,
        count: int,
    ) -> None:
        """:param bufferIndex:
        :param destination:
        :param destinationIndex:
        :param count:
        """
    def Dispose(self) -> None:
        """"""
    def EnsureByteCapacity(self, minCapacity: int) -> None:
        """:param minCapacity:"""
    def EnsureCharCapacity(self, minCapacity: int) -> None:
        """:param minCapacity:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def Free(self) -> None:
        """"""
    def GetHandle(self) -> SafeHandle:
        """:return:"""
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def SetLengthToFirstNull(self) -> None:
        """"""
    def StartsWith(self, value: str) -> bool:
        """:param value:
        :return:
        """
    def Substring(self, startIndex: int, count: int = ...) -> str:
        """:param startIndex:
        :param count:
        :return:
        """
    def SubstringEquals(self, value: str, startIndex: int = ..., count: int = ...) -> bool:
        """:param value:
        :param startIndex:
        :param count:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""
    def TrimEnd(self, values: Array[Char]) -> None:
        """:param values:"""
    @overload
    def __getitem__(self, index: int) -> Char:
        """:param index:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> int:
        """:param index:
        :return:
        """
    @overload
    def __setitem__(self, index: int, value: Char) -> None:
        """:param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: int) -> None:
        """:param index:
        :param value:
        """

class StructLayoutAttribute(Attribute, _Attribute):
    """"""

    CharSet: Final[CharSet] = ...
    """
    
    :return: 
    """
    Pack: Final[int] = ...
    """
    
    :return: 
    """
    Size: Final[int] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, layoutKind: LayoutKind):
        """:param layoutKind:"""
    @overload
    def __init__(self, layoutKind: int):
        """:param layoutKind:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    @property
    def Value(self) -> LayoutKind:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class TYPEATTR(ValueType):
    """"""

    MEMBER_ID_NIL: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    cFuncs: Final[int] = ...
    """
    
    :return: 
    """
    cImplTypes: Final[int] = ...
    """
    
    :return: 
    """
    cVars: Final[int] = ...
    """
    
    :return: 
    """
    cbAlignment: Final[int] = ...
    """
    
    :return: 
    """
    cbSizeInstance: Final[int] = ...
    """
    
    :return: 
    """
    cbSizeVft: Final[int] = ...
    """
    
    :return: 
    """
    dwReserved: Final[int] = ...
    """
    
    :return: 
    """
    guid: Final[Guid] = ...
    """
    
    :return: 
    """
    idldescType: Final[IDLDESC] = ...
    """
    
    :return: 
    """
    lcid: Final[int] = ...
    """
    
    :return: 
    """
    lpstrSchema: Final[IntPtr] = ...
    """
    
    :return: 
    """
    memidConstructor: Final[int] = ...
    """
    
    :return: 
    """
    memidDestructor: Final[int] = ...
    """
    
    :return: 
    """
    tdescAlias: Final[TYPEDESC] = ...
    """
    
    :return: 
    """
    typekind: Final[TYPEKIND] = ...
    """
    
    :return: 
    """
    wMajorVerNum: Final[int] = ...
    """
    
    :return: 
    """
    wMinorVerNum: Final[int] = ...
    """
    
    :return: 
    """
    wTypeFlags: Final[TYPEFLAGS] = ...
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

class TYPEDESC(ValueType):
    """"""

    lpValue: Final[IntPtr] = ...
    """
    
    :return: 
    """
    vt: Final[int] = ...
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

    guid: Final[Guid] = ...
    """
    
    :return: 
    """
    lcid: Final[int] = ...
    """
    
    :return: 
    """
    syskind: Final[SYSKIND] = ...
    """
    
    :return: 
    """
    wLibFlags: Final[LIBFLAGS] = ...
    """
    
    :return: 
    """
    wMajorVerNum: Final[int] = ...
    """
    
    :return: 
    """
    wMinorVerNum: Final[int] = ...
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

class TypeIdentifierAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, scope: str, identifier: str):
        """:param scope:
        :param identifier:
        """
    @property
    def Identifier(self) -> str:
        """:return:"""
    @property
    def Scope(self) -> str:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class TypeLibConverter(Object, ITypeLibConverter):
    """"""

    def __init__(self):
        """"""
    def ConvertAssemblyToTypeLib(
        self,
        assembly: Assembly,
        typeLibName: str,
        flags: TypeLibExporterFlags,
        notifySink: ITypeLibExporterNotifySink,
    ) -> object:
        """:param assembly:
        :param typeLibName:
        :param flags:
        :param notifySink:
        :return:
        """
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
        """:param typeLib:
        :param asmFileName:
        :param flags:
        :param notifySink:
        :param publicKey:
        :param keyPair:
        :param unsafeInterfaces:
        :return:
        """
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
        """:param typeLib:
        :param asmFileName:
        :param flags:
        :param notifySink:
        :param publicKey:
        :param keyPair:
        :param asmNamespace:
        :param asmVersion:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetPrimaryInteropAssembly(
        self, g: Guid, major: int, minor: int, lcid: int, asmName: str, asmCodeBase: str
    ) -> tuple[bool, str, str]:
        """:param g:
        :param major:
        :param minor:
        :param lcid:
        :param asmName:
        :param asmCodeBase:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

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
    def __init__(self, flags: TypeLibFuncFlags):
        """:param flags:"""
    @overload
    def __init__(self, flags: int):
        """:param flags:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    @property
    def Value(self) -> TypeLibFuncFlags:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

    def __init__(self, importClass: Type):
        """:param importClass:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    @property
    def Value(self) -> str:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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
    def __init__(self, flags: TypeLibTypeFlags):
        """:param flags:"""
    @overload
    def __init__(self, flags: int):
        """:param flags:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    @property
    def Value(self) -> TypeLibTypeFlags:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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
    def __init__(self, flags: TypeLibVarFlags):
        """:param flags:"""
    @overload
    def __init__(self, flags: int):
        """:param flags:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    @property
    def Value(self) -> TypeLibVarFlags:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

    def __init__(self, major: int, minor: int):
        """:param major:
        :param minor:
        """
    @property
    def MajorVersion(self) -> int:
        """:return:"""
    @property
    def MinorVersion(self) -> int:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class UCOMIBindCtx:
    """"""

    def EnumObjectParam(self, ppenum: UCOMIEnumString) -> tuple[None, UCOMIEnumString]:
        """:param ppenum:"""
    def GetBindOptions(self, pbindopts: BIND_OPTS) -> None:
        """:param pbindopts:"""
    def GetObjectParam(self, pszKey: str, ppunk: object) -> tuple[None, object]:
        """:param pszKey:
        :param ppunk:
        """
    def GetRunningObjectTable(
        self, pprot: UCOMIRunningObjectTable
    ) -> tuple[None, UCOMIRunningObjectTable]:
        """:param pprot:"""
    def RegisterObjectBound(self, punk: object) -> None:
        """:param punk:"""
    def RegisterObjectParam(self, pszKey: str, punk: object) -> None:
        """:param pszKey:
        :param punk:
        """
    def ReleaseBoundObjects(self) -> None:
        """"""
    def RevokeObjectBound(self, punk: object) -> None:
        """:param punk:"""
    def RevokeObjectParam(self, pszKey: str) -> None:
        """:param pszKey:"""
    def SetBindOptions(self, pbindopts: BIND_OPTS) -> None:
        """:param pbindopts:"""

class UCOMIConnectionPoint:
    """"""

    def Advise(self, pUnkSink: object, pdwCookie: int) -> tuple[None, int]:
        """:param pUnkSink:
        :param pdwCookie:
        """
    def EnumConnections(self, ppEnum: UCOMIEnumConnections) -> tuple[None, UCOMIEnumConnections]:
        """:param ppEnum:"""
    def GetConnectionInterface(self, pIID: Guid) -> tuple[None, Guid]:
        """:param pIID:"""
    def GetConnectionPointContainer(
        self, ppCPC: UCOMIConnectionPointContainer
    ) -> tuple[None, UCOMIConnectionPointContainer]:
        """:param ppCPC:"""
    def Unadvise(self, dwCookie: int) -> None:
        """:param dwCookie:"""

class UCOMIConnectionPointContainer:
    """"""

    def EnumConnectionPoints(
        self, ppEnum: UCOMIEnumConnectionPoints
    ) -> tuple[None, UCOMIEnumConnectionPoints]:
        """:param ppEnum:"""
    def FindConnectionPoint(
        self, riid: Guid, ppCP: UCOMIConnectionPoint
    ) -> tuple[None, UCOMIConnectionPoint]:
        """:param riid:
        :param ppCP:
        """

class UCOMIEnumConnectionPoints:
    """"""

    def Clone(self, ppenum: UCOMIEnumConnectionPoints) -> tuple[None, UCOMIEnumConnectionPoints]:
        """:param ppenum:"""
    def Next(
        self, celt: int, rgelt: Array[UCOMIConnectionPoint], pceltFetched: int
    ) -> tuple[int, Array[UCOMIConnectionPoint], int]:
        """:param celt:
        :param rgelt:
        :param pceltFetched:
        :return:
        """
    def Reset(self) -> int:
        """:return:"""
    def Skip(self, celt: int) -> int:
        """:param celt:
        :return:
        """

class UCOMIEnumConnections:
    """"""

    def Clone(self, ppenum: UCOMIEnumConnections) -> tuple[None, UCOMIEnumConnections]:
        """:param ppenum:"""
    def Next(
        self, celt: int, rgelt: Array[CONNECTDATA], pceltFetched: int
    ) -> tuple[int, Array[CONNECTDATA], int]:
        """:param celt:
        :param rgelt:
        :param pceltFetched:
        :return:
        """
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> int:
        """:param celt:
        :return:
        """

class UCOMIEnumMoniker:
    """"""

    def Clone(self, ppenum: UCOMIEnumMoniker) -> tuple[None, UCOMIEnumMoniker]:
        """:param ppenum:"""
    def Next(
        self, celt: int, rgelt: Array[UCOMIMoniker], pceltFetched: int
    ) -> tuple[int, Array[UCOMIMoniker], int]:
        """:param celt:
        :param rgelt:
        :param pceltFetched:
        :return:
        """
    def Reset(self) -> int:
        """:return:"""
    def Skip(self, celt: int) -> int:
        """:param celt:
        :return:
        """

class UCOMIEnumString:
    """"""

    def Clone(self, ppenum: UCOMIEnumString) -> tuple[None, UCOMIEnumString]:
        """:param ppenum:"""
    def Next(self, celt: int, rgelt: Array[str], pceltFetched: int) -> tuple[int, Array[str], int]:
        """:param celt:
        :param rgelt:
        :param pceltFetched:
        :return:
        """
    def Reset(self) -> int:
        """:return:"""
    def Skip(self, celt: int) -> int:
        """:param celt:
        :return:
        """

class UCOMIEnumVARIANT:
    """"""

    def Clone(self, ppenum: int) -> None:
        """:param ppenum:"""
    def Next(self, celt: int, rgvar: int, pceltFetched: int) -> int:
        """:param celt:
        :param rgvar:
        :param pceltFetched:
        :return:
        """
    def Reset(self) -> int:
        """:return:"""
    def Skip(self, celt: int) -> int:
        """:param celt:
        :return:
        """

class UCOMIEnumerable:
    """"""

    def GetEnumerator(self) -> IEnumerator:
        """:return:"""

class UCOMIEnumerator:
    """"""

    @property
    def Current(self) -> object:
        """:return:"""
    def MoveNext(self) -> bool:
        """:return:"""
    def Reset(self) -> None:
        """"""

class UCOMIExpando(UCOMIReflect):
    """"""

    @property
    def UnderlyingSystemType(self) -> Type:
        """:return:"""
    def AddField(self, name: str) -> FieldInfo:
        """:param name:
        :return:
        """
    def AddMethod(self, name: str, method: Delegate) -> MethodInfo:
        """:param name:
        :param method:
        :return:
        """
    def AddProperty(self, name: str) -> PropertyInfo:
        """:param name:
        :return:
        """
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """:param name:
        :param bindingAttr:
        :return:
        """
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """:param bindingAttr:
        :return:
        """
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """:param name:
        :param bindingAttr:
        :return:
        """
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """:param name:
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
        """:param name:
        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """:param bindingAttr:
        :return:
        """
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """:param name:
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
        """:param name:
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
    def RemoveMember(self, m: MemberInfo) -> None:
        """:param m:"""

class UCOMIMoniker:
    """"""

    def BindToObject(
        self,
        pbc: UCOMIBindCtx,
        pmkToLeft: UCOMIMoniker,
        riidResult: Guid,
        ppvResult: object,
    ) -> tuple[None, object]:
        """:param pbc:
        :param pmkToLeft:
        :param riidResult:
        :param ppvResult:
        """
    def BindToStorage(
        self, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, riid: Guid, ppvObj: object
    ) -> tuple[None, object]:
        """:param pbc:
        :param pmkToLeft:
        :param riid:
        :param ppvObj:
        """
    def CommonPrefixWith(
        self, pmkOther: UCOMIMoniker, ppmkPrefix: UCOMIMoniker
    ) -> tuple[None, UCOMIMoniker]:
        """:param pmkOther:
        :param ppmkPrefix:
        """
    def ComposeWith(
        self,
        pmkRight: UCOMIMoniker,
        fOnlyIfNotGeneric: bool,
        ppmkComposite: UCOMIMoniker,
    ) -> tuple[None, UCOMIMoniker]:
        """:param pmkRight:
        :param fOnlyIfNotGeneric:
        :param ppmkComposite:
        """
    def Enum(
        self, fForward: bool, ppenumMoniker: UCOMIEnumMoniker
    ) -> tuple[None, UCOMIEnumMoniker]:
        """:param fForward:
        :param ppenumMoniker:
        """
    def GetClassID(self, pClassID: Guid) -> tuple[None, Guid]:
        """:param pClassID:"""
    def GetDisplayName(
        self, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, ppszDisplayName: str
    ) -> tuple[None, str]:
        """:param pbc:
        :param pmkToLeft:
        :param ppszDisplayName:
        """
    def GetSizeMax(self, pcbSize: int) -> tuple[None, int]:
        """:param pcbSize:"""
    def GetTimeOfLastChange(
        self, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, pFileTime: FILETIME
    ) -> tuple[None, FILETIME]:
        """:param pbc:
        :param pmkToLeft:
        :param pFileTime:
        """
    def Hash(self, pdwHash: int) -> tuple[None, int]:
        """:param pdwHash:"""
    def Inverse(self, ppmk: UCOMIMoniker) -> tuple[None, UCOMIMoniker]:
        """:param ppmk:"""
    def IsDirty(self) -> int:
        """:return:"""
    def IsEqual(self, pmkOtherMoniker: UCOMIMoniker) -> None:
        """:param pmkOtherMoniker:"""
    def IsRunning(
        self, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, pmkNewlyRunning: UCOMIMoniker
    ) -> None:
        """:param pbc:
        :param pmkToLeft:
        :param pmkNewlyRunning:
        """
    def IsSystemMoniker(self, pdwMksys: int) -> tuple[None, int]:
        """:param pdwMksys:"""
    def Load(self, pStm: UCOMIStream) -> None:
        """:param pStm:"""
    def ParseDisplayName(
        self,
        pbc: UCOMIBindCtx,
        pmkToLeft: UCOMIMoniker,
        pszDisplayName: str,
        pchEaten: int,
        ppmkOut: UCOMIMoniker,
    ) -> tuple[None, int, UCOMIMoniker]:
        """:param pbc:
        :param pmkToLeft:
        :param pszDisplayName:
        :param pchEaten:
        :param ppmkOut:
        """
    def Reduce(
        self,
        pbc: UCOMIBindCtx,
        dwReduceHowFar: int,
        ppmkToLeft: UCOMIMoniker,
        ppmkReduced: UCOMIMoniker,
    ) -> tuple[None, UCOMIMoniker]:
        """:param pbc:
        :param dwReduceHowFar:
        :param ppmkToLeft:
        :param ppmkReduced:
        """
    def RelativePathTo(
        self, pmkOther: UCOMIMoniker, ppmkRelPath: UCOMIMoniker
    ) -> tuple[None, UCOMIMoniker]:
        """:param pmkOther:
        :param ppmkRelPath:
        """
    def Save(self, pStm: UCOMIStream, fClearDirty: bool) -> None:
        """:param pStm:
        :param fClearDirty:
        """

class UCOMIPersistFile:
    """"""

    def GetClassID(self, pClassID: Guid) -> tuple[None, Guid]:
        """:param pClassID:"""
    def GetCurFile(self, ppszFileName: str) -> tuple[None, str]:
        """:param ppszFileName:"""
    def IsDirty(self) -> int:
        """:return:"""
    def Load(self, pszFileName: str, dwMode: int) -> None:
        """:param pszFileName:
        :param dwMode:
        """
    def Save(self, pszFileName: str, fRemember: bool) -> None:
        """:param pszFileName:
        :param fRemember:
        """
    def SaveCompleted(self, pszFileName: str) -> None:
        """:param pszFileName:"""

class UCOMIReflect:
    """"""

    @property
    def UnderlyingSystemType(self) -> Type:
        """:return:"""
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """:param name:
        :param bindingAttr:
        :return:
        """
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """:param bindingAttr:
        :return:
        """
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """:param name:
        :param bindingAttr:
        :return:
        """
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """:param name:
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
        """:param name:
        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """:param bindingAttr:
        :return:
        """
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """:param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """:param name:
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
        """:param name:
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

class UCOMIRunningObjectTable:
    """"""

    def EnumRunning(self, ppenumMoniker: UCOMIEnumMoniker) -> tuple[None, UCOMIEnumMoniker]:
        """:param ppenumMoniker:"""
    def GetObject(self, pmkObjectName: UCOMIMoniker, ppunkObject: object) -> tuple[None, object]:
        """:param pmkObjectName:
        :param ppunkObject:
        """
    def GetTimeOfLastChange(
        self, pmkObjectName: UCOMIMoniker, pfiletime: FILETIME
    ) -> tuple[None, FILETIME]:
        """:param pmkObjectName:
        :param pfiletime:
        """
    def IsRunning(self, pmkObjectName: UCOMIMoniker) -> None:
        """:param pmkObjectName:"""
    def NoteChangeTime(self, dwRegister: int, pfiletime: FILETIME) -> None:
        """:param dwRegister:
        :param pfiletime:
        """
    def Register(
        self,
        grfFlags: int,
        punkObject: object,
        pmkObjectName: UCOMIMoniker,
        pdwRegister: int,
    ) -> tuple[None, int]:
        """:param grfFlags:
        :param punkObject:
        :param pmkObjectName:
        :param pdwRegister:
        """
    def Revoke(self, dwRegister: int) -> None:
        """:param dwRegister:"""

class UCOMIStream:
    """"""

    def Clone(self, ppstm: UCOMIStream) -> tuple[None, UCOMIStream]:
        """:param ppstm:"""
    def Commit(self, grfCommitFlags: int) -> None:
        """:param grfCommitFlags:"""
    def CopyTo(self, pstm: UCOMIStream, cb: int, pcbRead: IntPtr, pcbWritten: IntPtr) -> None:
        """:param pstm:
        :param cb:
        :param pcbRead:
        :param pcbWritten:
        """
    def LockRegion(self, libOffset: int, cb: int, dwLockType: int) -> None:
        """:param libOffset:
        :param cb:
        :param dwLockType:
        """
    def Read(self, pv: Array[int], cb: int, pcbRead: IntPtr) -> tuple[None, Array[int]]:
        """:param pv:
        :param cb:
        :param pcbRead:
        """
    def Revert(self) -> None:
        """"""
    def Seek(self, dlibMove: int, dwOrigin: int, plibNewPosition: IntPtr) -> None:
        """:param dlibMove:
        :param dwOrigin:
        :param plibNewPosition:
        """
    def SetSize(self, libNewSize: int) -> None:
        """:param libNewSize:"""
    def Stat(self, pstatstg: STATSTG, grfStatFlag: int) -> tuple[None, STATSTG]:
        """:param pstatstg:
        :param grfStatFlag:
        """
    def UnlockRegion(self, libOffset: int, cb: int, dwLockType: int) -> None:
        """:param libOffset:
        :param cb:
        :param dwLockType:
        """
    def Write(self, pv: Array[int], cb: int, pcbWritten: IntPtr) -> None:
        """:param pv:
        :param cb:
        :param pcbWritten:
        """

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
        """:param szName:
        :param lHashVal:
        :param wFlags:
        :param ppTInfo:
        :param pDescKind:
        :param pBindPtr:
        """
    def BindType(
        self, szName: str, lHashVal: int, ppTInfo: UCOMITypeInfo, ppTComp: UCOMITypeComp
    ) -> tuple[None, UCOMITypeInfo, UCOMITypeComp]:
        """:param szName:
        :param lHashVal:
        :param ppTInfo:
        :param ppTComp:
        """

class UCOMITypeInfo:
    """"""

    def AddressOfMember(self, memid: int, invKind: INVOKEKIND, ppv: IntPtr) -> tuple[None, IntPtr]:
        """:param memid:
        :param invKind:
        :param ppv:
        """
    def CreateInstance(self, pUnkOuter: object, riid: Guid, ppvObj: object) -> tuple[None, object]:
        """:param pUnkOuter:
        :param riid:
        :param ppvObj:
        """
    def GetContainingTypeLib(
        self, ppTLB: UCOMITypeLib, pIndex: int
    ) -> tuple[None, UCOMITypeLib, int]:
        """:param ppTLB:
        :param pIndex:
        """
    def GetDllEntry(
        self,
        memid: int,
        invKind: INVOKEKIND,
        pBstrDllName: str,
        pBstrName: str,
        pwOrdinal: int,
    ) -> tuple[None, str, str, int]:
        """:param memid:
        :param invKind:
        :param pBstrDllName:
        :param pBstrName:
        :param pwOrdinal:
        """
    def GetDocumentation(
        self,
        index: int,
        strName: str,
        strDocString: str,
        dwHelpContext: int,
        strHelpFile: str,
    ) -> tuple[None, str, str, int, str]:
        """:param index:
        :param strName:
        :param strDocString:
        :param dwHelpContext:
        :param strHelpFile:
        """
    def GetFuncDesc(self, index: int, ppFuncDesc: IntPtr) -> tuple[None, IntPtr]:
        """:param index:
        :param ppFuncDesc:
        """
    def GetIDsOfNames(
        self, rgszNames: Array[str], cNames: int, pMemId: Array[int]
    ) -> tuple[None, Array[int]]:
        """:param rgszNames:
        :param cNames:
        :param pMemId:
        """
    def GetImplTypeFlags(self, index: int, pImplTypeFlags: int) -> tuple[None, int]:
        """:param index:
        :param pImplTypeFlags:
        """
    def GetMops(self, memid: int, pBstrMops: str) -> tuple[None, str]:
        """:param memid:
        :param pBstrMops:
        """
    def GetNames(
        self, memid: int, rgBstrNames: Array[str], cMaxNames: int, pcNames: int
    ) -> tuple[None, Array[str], int]:
        """:param memid:
        :param rgBstrNames:
        :param cMaxNames:
        :param pcNames:
        """
    def GetRefTypeInfo(self, hRef: int, ppTI: UCOMITypeInfo) -> tuple[None, UCOMITypeInfo]:
        """:param hRef:
        :param ppTI:
        """
    def GetRefTypeOfImplType(self, index: int, href: int) -> tuple[None, int]:
        """:param index:
        :param href:
        """
    def GetTypeAttr(self, ppTypeAttr: IntPtr) -> tuple[None, IntPtr]:
        """:param ppTypeAttr:"""
    def GetTypeComp(self, ppTComp: UCOMITypeComp) -> tuple[None, UCOMITypeComp]:
        """:param ppTComp:"""
    def GetVarDesc(self, index: int, ppVarDesc: IntPtr) -> tuple[None, IntPtr]:
        """:param index:
        :param ppVarDesc:
        """
    def Invoke(
        self,
        pvInstance: object,
        memid: int,
        wFlags: int,
        pDispParams: DISPPARAMS,
        pVarResult: object,
        pExcepInfo: EXCEPINFO,
        puArgErr: int,
    ) -> tuple[None, object, EXCEPINFO, int]:
        """:param pvInstance:
        :param memid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def ReleaseFuncDesc(self, pFuncDesc: IntPtr) -> None:
        """:param pFuncDesc:"""
    def ReleaseTypeAttr(self, pTypeAttr: IntPtr) -> None:
        """:param pTypeAttr:"""
    def ReleaseVarDesc(self, pVarDesc: IntPtr) -> None:
        """:param pVarDesc:"""

class UCOMITypeLib:
    """"""

    def FindName(
        self,
        szNameBuf: str,
        lHashVal: int,
        ppTInfo: Array[UCOMITypeInfo],
        rgMemId: Array[int],
        pcFound: int,
    ) -> tuple[None, Array[UCOMITypeInfo], Array[int]]:
        """:param szNameBuf:
        :param lHashVal:
        :param ppTInfo:
        :param rgMemId:
        :param pcFound:
        """
    def GetDocumentation(
        self,
        index: int,
        strName: str,
        strDocString: str,
        dwHelpContext: int,
        strHelpFile: str,
    ) -> tuple[None, str, str, int, str]:
        """:param index:
        :param strName:
        :param strDocString:
        :param dwHelpContext:
        :param strHelpFile:
        """
    def GetLibAttr(self, ppTLibAttr: IntPtr) -> tuple[None, IntPtr]:
        """:param ppTLibAttr:"""
    def GetTypeComp(self, ppTComp: UCOMITypeComp) -> tuple[None, UCOMITypeComp]:
        """:param ppTComp:"""
    def GetTypeInfo(self, index: int, ppTI: UCOMITypeInfo) -> tuple[None, UCOMITypeInfo]:
        """:param index:
        :param ppTI:
        """
    def GetTypeInfoCount(self) -> int:
        """:return:"""
    def GetTypeInfoOfGuid(self, guid: Guid, ppTInfo: UCOMITypeInfo) -> tuple[None, UCOMITypeInfo]:
        """:param guid:
        :param ppTInfo:
        """
    def GetTypeInfoType(self, index: int, pTKind: TYPEKIND) -> tuple[None, TYPEKIND]:
        """:param index:
        :param pTKind:
        """
    def IsName(self, szNameBuf: str, lHashVal: int) -> bool:
        """:param szNameBuf:
        :param lHashVal:
        :return:
        """
    def ReleaseTLibAttr(self, pTLibAttr: IntPtr) -> None:
        """:param pTLibAttr:"""

class UnknownWrapper(Object):
    """"""

    def __init__(self, obj: object):
        """:param obj:"""
    @property
    def WrappedObject(self) -> object:
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

class UnmanagedFunctionPointerAttribute(Attribute, _Attribute):
    """"""

    BestFitMapping: Final[bool] = ...
    """
    
    :return: 
    """
    CharSet: Final[CharSet] = ...
    """
    
    :return: 
    """
    SetLastError: Final[bool] = ...
    """
    
    :return: 
    """
    ThrowOnUnmappableChar: Final[bool] = ...
    """
    
    :return: 
    """
    def __init__(self, callingConvention: CallingConvention):
        """:param callingConvention:"""
    @property
    def CallingConvention(self) -> CallingConvention:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

    elemdescVar: Final[ELEMDESC] = ...
    """
    
    :return: 
    """
    lpstrSchema: Final[str] = ...
    """
    
    :return: 
    """
    memid: Final[int] = ...
    """
    
    :return: 
    """
    varkind: Final[VarEnum] = ...
    """
    
    :return: 
    """
    wVarFlags: Final[int] = ...
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

    class DESCUNION(ValueType):
        """"""

        lpvarValue: Final[IntPtr] = ...
        """"""
        oInst: Final[int] = ...
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
        """:return:"""
    @AsBool.setter
    def AsBool(self, value: bool) -> None: ...
    @property
    def AsBstr(self) -> str:
        """:return:"""
    @AsBstr.setter
    def AsBstr(self, value: str) -> None: ...
    @property
    def AsCy(self) -> Decimal:
        """:return:"""
    @AsCy.setter
    def AsCy(self, value: Decimal) -> None: ...
    @property
    def AsDate(self) -> DateTime:
        """:return:"""
    @AsDate.setter
    def AsDate(self, value: DateTime) -> None: ...
    @property
    def AsDecimal(self) -> Decimal:
        """:return:"""
    @AsDecimal.setter
    def AsDecimal(self, value: Decimal) -> None: ...
    @property
    def AsDispatch(self) -> object:
        """:return:"""
    @AsDispatch.setter
    def AsDispatch(self, value: object) -> None: ...
    @property
    def AsError(self) -> int:
        """:return:"""
    @AsError.setter
    def AsError(self, value: int) -> None: ...
    @property
    def AsI1(self) -> int:
        """:return:"""
    @AsI1.setter
    def AsI1(self, value: int) -> None: ...
    @property
    def AsI2(self) -> int:
        """:return:"""
    @AsI2.setter
    def AsI2(self, value: int) -> None: ...
    @property
    def AsI4(self) -> int:
        """:return:"""
    @AsI4.setter
    def AsI4(self, value: int) -> None: ...
    @property
    def AsI8(self) -> int:
        """:return:"""
    @AsI8.setter
    def AsI8(self, value: int) -> None: ...
    @property
    def AsInt(self) -> int:
        """:return:"""
    @AsInt.setter
    def AsInt(self, value: int) -> None: ...
    @property
    def AsR4(self) -> float:
        """:return:"""
    @AsR4.setter
    def AsR4(self, value: float) -> None: ...
    @property
    def AsR8(self) -> float:
        """:return:"""
    @AsR8.setter
    def AsR8(self, value: float) -> None: ...
    @property
    def AsUi1(self) -> int:
        """:return:"""
    @AsUi1.setter
    def AsUi1(self, value: int) -> None: ...
    @property
    def AsUi2(self) -> int:
        """:return:"""
    @AsUi2.setter
    def AsUi2(self, value: int) -> None: ...
    @property
    def AsUi4(self) -> int:
        """:return:"""
    @AsUi4.setter
    def AsUi4(self, value: int) -> None: ...
    @property
    def AsUi8(self) -> int:
        """:return:"""
    @AsUi8.setter
    def AsUi8(self, value: int) -> None: ...
    @property
    def AsUint(self) -> int:
        """:return:"""
    @AsUint.setter
    def AsUint(self, value: int) -> None: ...
    @property
    def AsUnknown(self) -> object:
        """:return:"""
    @AsUnknown.setter
    def AsUnknown(self, value: object) -> None: ...
    @property
    def VariantType(self) -> VarEnum:
        """:return:"""
    @VariantType.setter
    def VariantType(self, value: VarEnum) -> None: ...
    def Clear(self) -> None:
        """"""
    def CopyFromIndirect(self, value: object) -> None:
        """:param value:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def SetAsNULL(self) -> None:
        """"""
    def ToObject(self) -> object:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class VariantWrapper(Object):
    """"""

    def __init__(self, obj: object):
        """:param obj:"""
    @property
    def WrappedObject(self) -> object:
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

class _Activator:
    """"""

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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class _Assembly:
    """"""

    @property
    def CodeBase(self) -> str:
        """:return:"""
    @property
    def EntryPoint(self) -> MethodInfo:
        """:return:"""
    @property
    def EscapedCodeBase(self) -> str:
        """:return:"""
    @property
    def Evidence(self) -> Evidence:
        """:return:"""
    @property
    def FullName(self) -> str:
        """:return:"""
    @property
    def GlobalAssemblyCache(self) -> bool:
        """:return:"""
    @property
    def Location(self) -> str:
        """:return:"""
    @overload
    def CreateInstance(self, typeName: str) -> object:
        """:param typeName:
        :return:
        """
    @overload
    def CreateInstance(self, typeName: str, ignoreCase: bool) -> object:
        """:param typeName:
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
        """:param typeName:
        :param ignoreCase:
        :param bindingAttr:
        :param binder:
        :param args:
        :param culture:
        :param activationAttributes:
        :return:
        """
    def Equals(self, other: object) -> bool:
        """:param other:
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
    def GetExportedTypes(self) -> Array[Type]:
        """:return:"""
    def GetFile(self, name: str) -> FileStream:
        """:param name:
        :return:
        """
    @overload
    def GetFiles(self) -> Array[FileStream]:
        """:return:"""
    @overload
    def GetFiles(self, getResourceModules: bool) -> Array[FileStream]:
        """:param getResourceModules:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetLoadedModules(self) -> Array[Module]:
        """:return:"""
    @overload
    def GetLoadedModules(self, getResourceModules: bool) -> Array[Module]:
        """:param getResourceModules:
        :return:
        """
    def GetManifestResourceInfo(self, resourceName: str) -> ManifestResourceInfo:
        """:param resourceName:
        :return:
        """
    def GetManifestResourceNames(self) -> Array[str]:
        """:return:"""
    @overload
    def GetManifestResourceStream(self, name: str) -> Stream:
        """:param name:
        :return:
        """
    @overload
    def GetManifestResourceStream(self, type: Type, name: str) -> Stream:
        """:param type:
        :param name:
        :return:
        """
    def GetModule(self, name: str) -> Module:
        """:param name:
        :return:
        """
    @overload
    def GetModules(self) -> Array[Module]:
        """:return:"""
    @overload
    def GetModules(self, getResourceModules: bool) -> Array[Module]:
        """:param getResourceModules:
        :return:
        """
    @overload
    def GetName(self) -> AssemblyName:
        """:return:"""
    @overload
    def GetName(self, copiedName: bool) -> AssemblyName:
        """:param copiedName:
        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    def GetReferencedAssemblies(self) -> Array[AssemblyName]:
        """:return:"""
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo) -> Assembly:
        """:param culture:
        :return:
        """
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo, version: Version) -> Assembly:
        """:param culture:
        :param version:
        :return:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self, name: str) -> Type:
        """:param name:
        :return:
        """
    @overload
    def GetType(self, name: str, throwOnError: bool) -> Type:
        """:param name:
        :param throwOnError:
        :return:
        """
    @overload
    def GetType(self, name: str, throwOnError: bool, ignoreCase: bool) -> Type:
        """:param name:
        :param throwOnError:
        :param ignoreCase:
        :return:
        """
    def GetTypes(self) -> Array[Type]:
        """:return:"""
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """:param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def LoadModule(self, moduleName: str, rawModule: Array[int]) -> Module:
        """:param moduleName:
        :param rawModule:
        :return:
        """
    @overload
    def LoadModule(
        self, moduleName: str, rawModule: Array[int], rawSymbolStore: Array[int]
    ) -> Module:
        """:param moduleName:
        :param rawModule:
        :param rawSymbolStore:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""
    ModuleResolve: EventType[ModuleResolveEventHandler] = ...
    """"""

class _AssemblyBuilder:
    """"""

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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class _AssemblyName:
    """"""

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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class _Attribute:
    """"""

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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class _ConstructorBuilder:
    """"""

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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class _ConstructorInfo:
    """"""

    @property
    def Attributes(self) -> MethodAttributes:
        """:return:"""
    @property
    def CallingConvention(self) -> CallingConventions:
        """:return:"""
    @property
    def DeclaringType(self) -> Type:
        """:return:"""
    @property
    def IsAbstract(self) -> bool:
        """:return:"""
    @property
    def IsAssembly(self) -> bool:
        """:return:"""
    @property
    def IsConstructor(self) -> bool:
        """:return:"""
    @property
    def IsFamily(self) -> bool:
        """:return:"""
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """:return:"""
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """:return:"""
    @property
    def IsFinal(self) -> bool:
        """:return:"""
    @property
    def IsHideBySig(self) -> bool:
        """:return:"""
    @property
    def IsPrivate(self) -> bool:
        """:return:"""
    @property
    def IsPublic(self) -> bool:
        """:return:"""
    @property
    def IsSpecialName(self) -> bool:
        """:return:"""
    @property
    def IsStatic(self) -> bool:
        """:return:"""
    @property
    def IsVirtual(self) -> bool:
        """:return:"""
    @property
    def MemberType(self) -> MemberTypes:
        """:return:"""
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """:return:"""
    @property
    def Name(self) -> str:
        """:return:"""
    @property
    def ReflectedType(self) -> Type:
        """:return:"""
    def Equals(self, other: object) -> bool:
        """:param other:
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
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """:return:"""
    def GetParameters(self) -> Array[ParameterInfo]:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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
    def Invoke_2(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """:param obj:
        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    def Invoke_3(self, obj: object, parameters: Array[object]) -> object:
        """:param obj:
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
        """:param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    def Invoke_5(self, parameters: Array[object]) -> object:
        """:param parameters:
        :return:
        """
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """:param attributeType:
        :param inherit:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class _CustomAttributeBuilder:
    """"""

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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class _EnumBuilder:
    """"""

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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class _EventBuilder:
    """"""

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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class _EventInfo:
    """"""

    @property
    def Attributes(self) -> EventAttributes:
        """:return:"""
    @property
    def DeclaringType(self) -> Type:
        """:return:"""
    @property
    def EventHandlerType(self) -> Type:
        """:return:"""
    @property
    def IsMulticast(self) -> bool:
        """:return:"""
    @property
    def IsSpecialName(self) -> bool:
        """:return:"""
    @property
    def MemberType(self) -> MemberTypes:
        """:return:"""
    @property
    def Name(self) -> str:
        """:return:"""
    @property
    def ReflectedType(self) -> Type:
        """:return:"""
    def AddEventHandler(self, target: object, handler: Delegate) -> None:
        """:param target:
        :param handler:
        """
    def Equals(self, other: object) -> bool:
        """:param other:
        :return:
        """
    @overload
    def GetAddMethod(self) -> MethodInfo:
        """:return:"""
    @overload
    def GetAddMethod(self, nonPublic: bool) -> MethodInfo:
        """:param nonPublic:
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
    def GetRaiseMethod(self) -> MethodInfo:
        """:return:"""
    @overload
    def GetRaiseMethod(self, nonPublic: bool) -> MethodInfo:
        """:param nonPublic:
        :return:
        """
    @overload
    def GetRemoveMethod(self) -> MethodInfo:
        """:return:"""
    @overload
    def GetRemoveMethod(self, nonPublic: bool) -> MethodInfo:
        """:param nonPublic:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """:param attributeType:
        :param inherit:
        :return:
        """
    def RemoveEventHandler(self, target: object, handler: Delegate) -> None:
        """:param target:
        :param handler:
        """
    def ToString(self) -> str:
        """:return:"""

class _Exception:
    """"""

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
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
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

class _FieldBuilder:
    """"""

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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class _FieldInfo:
    """"""

    @property
    def Attributes(self) -> FieldAttributes:
        """:return:"""
    @property
    def DeclaringType(self) -> Type:
        """:return:"""
    @property
    def FieldHandle(self) -> RuntimeFieldHandle:
        """:return:"""
    @property
    def FieldType(self) -> Type:
        """:return:"""
    @property
    def IsAssembly(self) -> bool:
        """:return:"""
    @property
    def IsFamily(self) -> bool:
        """:return:"""
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """:return:"""
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """:return:"""
    @property
    def IsInitOnly(self) -> bool:
        """:return:"""
    @property
    def IsLiteral(self) -> bool:
        """:return:"""
    @property
    def IsNotSerialized(self) -> bool:
        """:return:"""
    @property
    def IsPinvokeImpl(self) -> bool:
        """:return:"""
    @property
    def IsPrivate(self) -> bool:
        """:return:"""
    @property
    def IsPublic(self) -> bool:
        """:return:"""
    @property
    def IsSpecialName(self) -> bool:
        """:return:"""
    @property
    def IsStatic(self) -> bool:
        """:return:"""
    @property
    def MemberType(self) -> MemberTypes:
        """:return:"""
    @property
    def Name(self) -> str:
        """:return:"""
    @property
    def ReflectedType(self) -> Type:
        """:return:"""
    def Equals(self, other: object) -> bool:
        """:param other:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
        """:param pcTInfo:"""
    def GetValue(self, obj: object) -> object:
        """:param obj:
        :return:
        """
    def GetValueDirect(self, obj: TypedReference) -> object:
        """:param obj:
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
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """:param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def SetValue(self, obj: object, value: object) -> None:
        """:param obj:
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
        """:param obj:
        :param value:
        :param invokeAttr:
        :param binder:
        :param culture:
        """
    def SetValueDirect(self, obj: TypedReference, value: object) -> None:
        """:param obj:
        :param value:
        """
    def ToString(self) -> str:
        """:return:"""

class _ILGenerator:
    """"""

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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class _LocalBuilder:
    """"""

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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class _MemberInfo:
    """"""

    @property
    def DeclaringType(self) -> Type:
        """:return:"""
    @property
    def MemberType(self) -> MemberTypes:
        """:return:"""
    @property
    def Name(self) -> str:
        """:return:"""
    @property
    def ReflectedType(self) -> Type:
        """:return:"""
    def Equals(self, other: object) -> bool:
        """:param other:
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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """:param attributeType:
        :param inherit:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class _MethodBase:
    """"""

    @property
    def Attributes(self) -> MethodAttributes:
        """:return:"""
    @property
    def CallingConvention(self) -> CallingConventions:
        """:return:"""
    @property
    def DeclaringType(self) -> Type:
        """:return:"""
    @property
    def IsAbstract(self) -> bool:
        """:return:"""
    @property
    def IsAssembly(self) -> bool:
        """:return:"""
    @property
    def IsConstructor(self) -> bool:
        """:return:"""
    @property
    def IsFamily(self) -> bool:
        """:return:"""
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """:return:"""
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """:return:"""
    @property
    def IsFinal(self) -> bool:
        """:return:"""
    @property
    def IsHideBySig(self) -> bool:
        """:return:"""
    @property
    def IsPrivate(self) -> bool:
        """:return:"""
    @property
    def IsPublic(self) -> bool:
        """:return:"""
    @property
    def IsSpecialName(self) -> bool:
        """:return:"""
    @property
    def IsStatic(self) -> bool:
        """:return:"""
    @property
    def IsVirtual(self) -> bool:
        """:return:"""
    @property
    def MemberType(self) -> MemberTypes:
        """:return:"""
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """:return:"""
    @property
    def Name(self) -> str:
        """:return:"""
    @property
    def ReflectedType(self) -> Type:
        """:return:"""
    def Equals(self, other: object) -> bool:
        """:param other:
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
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """:return:"""
    def GetParameters(self) -> Array[ParameterInfo]:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
        """:param pcTInfo:"""
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """:param obj:
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
        """:param obj:
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
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """:param attributeType:
        :param inherit:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class _MethodBuilder:
    """"""

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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class _MethodInfo:
    """"""

    @property
    def Attributes(self) -> MethodAttributes:
        """:return:"""
    @property
    def CallingConvention(self) -> CallingConventions:
        """:return:"""
    @property
    def DeclaringType(self) -> Type:
        """:return:"""
    @property
    def IsAbstract(self) -> bool:
        """:return:"""
    @property
    def IsAssembly(self) -> bool:
        """:return:"""
    @property
    def IsConstructor(self) -> bool:
        """:return:"""
    @property
    def IsFamily(self) -> bool:
        """:return:"""
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """:return:"""
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """:return:"""
    @property
    def IsFinal(self) -> bool:
        """:return:"""
    @property
    def IsHideBySig(self) -> bool:
        """:return:"""
    @property
    def IsPrivate(self) -> bool:
        """:return:"""
    @property
    def IsPublic(self) -> bool:
        """:return:"""
    @property
    def IsSpecialName(self) -> bool:
        """:return:"""
    @property
    def IsStatic(self) -> bool:
        """:return:"""
    @property
    def IsVirtual(self) -> bool:
        """:return:"""
    @property
    def MemberType(self) -> MemberTypes:
        """:return:"""
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """:return:"""
    @property
    def Name(self) -> str:
        """:return:"""
    @property
    def ReflectedType(self) -> Type:
        """:return:"""
    @property
    def ReturnType(self) -> Type:
        """:return:"""
    @property
    def ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider:
        """:return:"""
    def Equals(self, other: object) -> bool:
        """:param other:
        :return:
        """
    def GetBaseDefinition(self) -> MethodInfo:
        """:return:"""
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
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """:return:"""
    def GetParameters(self) -> Array[ParameterInfo]:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
        """:param pcTInfo:"""
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """:param obj:
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
        """:param obj:
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
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """:param attributeType:
        :param inherit:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class _MethodRental:
    """"""

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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class _Module:
    """"""

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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class _ModuleBuilder:
    """"""

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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class _ParameterBuilder:
    """"""

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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class _ParameterInfo:
    """"""

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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class _PropertyBuilder:
    """"""

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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class _PropertyInfo:
    """"""

    @property
    def Attributes(self) -> PropertyAttributes:
        """:return:"""
    @property
    def CanRead(self) -> bool:
        """:return:"""
    @property
    def CanWrite(self) -> bool:
        """:return:"""
    @property
    def DeclaringType(self) -> Type:
        """:return:"""
    @property
    def IsSpecialName(self) -> bool:
        """:return:"""
    @property
    def MemberType(self) -> MemberTypes:
        """:return:"""
    @property
    def Name(self) -> str:
        """:return:"""
    @property
    def PropertyType(self) -> Type:
        """:return:"""
    @property
    def ReflectedType(self) -> Type:
        """:return:"""
    def Equals(self, other: object) -> bool:
        """:param other:
        :return:
        """
    @overload
    def GetAccessors(self) -> Array[MethodInfo]:
        """:return:"""
    @overload
    def GetAccessors(self, nonPublic: bool) -> Array[MethodInfo]:
        """:param nonPublic:
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
    def GetGetMethod(self) -> MethodInfo:
        """:return:"""
    @overload
    def GetGetMethod(self, nonPublic: bool) -> MethodInfo:
        """:param nonPublic:
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
    def GetIndexParameters(self) -> Array[ParameterInfo]:
        """:return:"""
    @overload
    def GetSetMethod(self) -> MethodInfo:
        """:return:"""
    @overload
    def GetSetMethod(self, nonPublic: bool) -> MethodInfo:
        """:param nonPublic:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
        """:param pcTInfo:"""
    @overload
    def GetValue(self, obj: object, index: Array[object]) -> object:
        """:param obj:
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
        """:param obj:
        :param invokeAttr:
        :param binder:
        :param index:
        :param culture:
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
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """:param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def SetValue(self, obj: object, value: object, index: Array[object]) -> None:
        """:param obj:
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
        """:param obj:
        :param value:
        :param invokeAttr:
        :param binder:
        :param index:
        :param culture:
        """
    def ToString(self) -> str:
        """:return:"""

class _SignatureHelper:
    """"""

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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class _Thread:
    """"""

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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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

class _Type:
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
    def DeclaringType(self) -> Type:
        """:return:"""
    @property
    def FullName(self) -> str:
        """:return:"""
    @property
    def GUID(self) -> Guid:
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
    def IsContextful(self) -> bool:
        """:return:"""
    @property
    def IsEnum(self) -> bool:
        """:return:"""
    @property
    def IsExplicitLayout(self) -> bool:
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
    def MemberType(self) -> MemberTypes:
        """:return:"""
    @property
    def Module(self) -> Module:
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
    def TypeHandle(self) -> RuntimeTypeHandle:
        """:return:"""
    @property
    def TypeInitializer(self) -> ConstructorInfo:
        """:return:"""
    @property
    def UnderlyingSystemType(self) -> Type:
        """:return:"""
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
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """:param attributeType:
        :param inherit:
        :return:
        """
    def GetDefaultMembers(self) -> Array[MemberInfo]:
        """:return:"""
    def GetElementType(self) -> Type:
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
    def GetFields(self) -> Array[FieldInfo]:
        """:return:"""
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """:param bindingAttr:
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
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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
    def IsAssignableFrom(self, c: Type) -> bool:
        """:param c:
        :return:
        """
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """:param attributeType:
        :param inherit:
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
    def ToString(self) -> str:
        """:return:"""

class _TypeBuilder:
    """"""

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
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
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
