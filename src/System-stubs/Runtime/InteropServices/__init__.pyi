from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import Generic
from typing import List
from typing import Protocol
from typing import Tuple
from typing import TypeVar
from typing import Union
from typing import overload

from Microsoft.Win32 import UnsafeNativeMethods
from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from System import Array
from System import AsyncCallback
from System import Attribute
from System import Boolean
from System import Byte
from System import Char
from System import DateTime
from System import Decimal
from System import Delegate
from System import Double
from System import Enum
from System import Exception
from System import Guid
from System import IAsyncResult
from System import ICloneable
from System import IDisposable
from System import IEquatable
from System import Int16
from System import Int32
from System import Int64
from System import IntPtr
from System import MarshalByRefObject
from System import MulticastDelegate
from System import Object
from System import RuntimeFieldHandle
from System import RuntimeMethodHandle
from System import RuntimeTypeHandle
from System import SByte
from System import Single
from System import String
from System import SystemException
from System import Type
from System import TypedReference
from System import UInt16
from System import UInt32
from System import UInt64
from System import ValueType
from System import Version
from System import Void
from System.Collections import IEnumerator
from System.Globalization import CultureInfo
from System.IO import FileStream
from System.IO import Stream
from System.Reflection import Assembly
from System.Reflection import AssemblyName
from System.Reflection import Binder
from System.Reflection import BindingFlags
from System.Reflection import CallingConventions
from System.Reflection import ConstructorInfo
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
from System.Runtime.InteropServices.ComTypes import ITypeInfo
from System.Runtime.InteropServices.ComTypes import ITypeLib
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Security import SecureString
from System.Security.Policy import Evidence
from System.Threading import Thread

# ---------- Types ---------- #

T = TypeVar("T")
TDelegate = TypeVar("TDelegate")
TWrapper = TypeVar("TWrapper")

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
CharType = Union[str, Char]
DecimalType = Union[float, Decimal]
DoubleType = Union[float, Double]
FloatType = Union[float, Single]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
SByteType = Union[int, SByte]
ShortType = Union[int, Int16]
StringType = Union[str, String]
TypeType = Union[type, Type]
UIntType = Union[int, UInt32]
ULongType = Union[int, UInt64]
UShortType = Union[int, UInt16]
VoidType = Union[None, Void]

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

# ---------- Classes ---------- #

class AllowReversePInvokeCallsAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class AutomationProxyAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, val: BooleanType): ...

    # ---------- Properties ---------- #

    @property
    def Value(self) -> BooleanType: ...

    # ---------- Methods ---------- #

    def get_Value(self) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class BStrWrapper(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, value: StringType): ...
    @overload
    def __init__(self, value: ObjectType): ...

    # ---------- Properties ---------- #

    @property
    def WrappedObject(self) -> StringType: ...

    # ---------- Methods ---------- #

    def get_WrappedObject(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class BestFitMappingAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #

    @property
    def ThrowOnUnmappableChar(self) -> BooleanType: ...
    @ThrowOnUnmappableChar.setter
    def ThrowOnUnmappableChar(self, value: BooleanType) -> None: ...

    # ---------- Constructors ---------- #

    def __init__(self, BestFitMapping: BooleanType): ...

    # ---------- Properties ---------- #

    @property
    def BestFitMapping(self) -> BooleanType: ...

    # ---------- Methods ---------- #

    def get_BestFitMapping(self) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class COMException(ExternalException, ISerializable, _Exception):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: StringType): ...
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    @overload
    def __init__(self, message: StringType, errorCode: IntType): ...

    # No Properties

    # ---------- Methods ---------- #

    def ToString(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ClassInterfaceAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, classInterfaceType: ClassInterfaceType): ...
    @overload
    def __init__(self, classInterfaceType: ShortType): ...

    # ---------- Properties ---------- #

    @property
    def Value(self) -> ClassInterfaceType: ...

    # ---------- Methods ---------- #

    def get_Value(self) -> ClassInterfaceType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CoClassAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, coClass: TypeType): ...

    # ---------- Properties ---------- #

    @property
    def CoClass(self) -> TypeType: ...

    # ---------- Methods ---------- #

    def get_CoClass(self) -> TypeType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ComAliasNameAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, alias: StringType): ...

    # ---------- Properties ---------- #

    @property
    def Value(self) -> StringType: ...

    # ---------- Methods ---------- #

    def get_Value(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ComAwareEventInfo(EventInfo, ICustomAttributeProvider, _MemberInfo, _EventInfo):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, type: TypeType, eventName: StringType): ...

    # ---------- Properties ---------- #

    @property
    def Attributes(self) -> EventAttributes: ...
    @property
    def DeclaringType(self) -> TypeType: ...
    @property
    def Name(self) -> StringType: ...
    @property
    def ReflectedType(self) -> TypeType: ...

    # ---------- Methods ---------- #

    def AddEventHandler(self, target: ObjectType, handler: Delegate) -> VoidType: ...
    @overload
    def GetAddMethod(self, nonPublic: BooleanType) -> MethodInfo: ...
    @overload
    def GetCustomAttributes(
        self, attributeType: TypeType, inherit: BooleanType
    ) -> ArrayType[ObjectType]: ...
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    @overload
    def GetRaiseMethod(self, nonPublic: BooleanType) -> MethodInfo: ...
    @overload
    def GetRemoveMethod(self, nonPublic: BooleanType) -> MethodInfo: ...
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    def RemoveEventHandler(self, target: ObjectType, handler: Delegate) -> VoidType: ...
    def get_Attributes(self) -> EventAttributes: ...
    def get_DeclaringType(self) -> TypeType: ...
    def get_Name(self) -> StringType: ...
    def get_ReflectedType(self) -> TypeType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ComCompatibleVersionAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, major: IntType, minor: IntType, build: IntType, revision: IntType): ...

    # ---------- Properties ---------- #

    @property
    def BuildNumber(self) -> IntType: ...
    @property
    def MajorVersion(self) -> IntType: ...
    @property
    def MinorVersion(self) -> IntType: ...
    @property
    def RevisionNumber(self) -> IntType: ...

    # ---------- Methods ---------- #

    def get_BuildNumber(self) -> IntType: ...
    def get_MajorVersion(self) -> IntType: ...
    def get_MinorVersion(self) -> IntType: ...
    def get_RevisionNumber(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ComConversionLossAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ComDefaultInterfaceAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, defaultInterface: TypeType): ...

    # ---------- Properties ---------- #

    @property
    def Value(self) -> TypeType: ...

    # ---------- Methods ---------- #

    def get_Value(self) -> TypeType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ComEventInterfaceAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, SourceInterface: TypeType, EventProvider: TypeType): ...

    # ---------- Properties ---------- #

    @property
    def EventProvider(self) -> TypeType: ...
    @property
    def SourceInterface(self) -> TypeType: ...

    # ---------- Methods ---------- #

    def get_EventProvider(self) -> TypeType: ...
    def get_SourceInterface(self) -> TypeType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ComEventsHelper(ABC, ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    def Combine(rcw: ObjectType, iid: Guid, dispid: IntType, d: Delegate) -> VoidType: ...
    @staticmethod
    def Remove(rcw: ObjectType, iid: Guid, dispid: IntType, d: Delegate) -> Delegate: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ComEventsInfo(ObjectType):
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

class ComEventsMethod(ObjectType):
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

class ComEventsSink(ObjectType, IDispatch, ICustomQueryInterface):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def AddMethod(self, dispid: IntType) -> ComEventsMethod: ...
    def FindMethod(self, dispid: IntType) -> ComEventsMethod: ...
    def RemoveMethod(self, method: ComEventsMethod) -> ComEventsMethod: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ComImportAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ComRegisterFunctionAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ComSourceInterfacesAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, sourceInterfaces: StringType): ...
    @overload
    def __init__(self, sourceInterface: TypeType): ...
    @overload
    def __init__(self, sourceInterface1: TypeType, sourceInterface2: TypeType): ...
    @overload
    def __init__(
        self, sourceInterface1: TypeType, sourceInterface2: TypeType, sourceInterface3: TypeType
    ): ...
    @overload
    def __init__(
        self,
        sourceInterface1: TypeType,
        sourceInterface2: TypeType,
        sourceInterface3: TypeType,
        sourceInterface4: TypeType,
    ): ...

    # ---------- Properties ---------- #

    @property
    def Value(self) -> StringType: ...

    # ---------- Methods ---------- #

    def get_Value(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ComUnregisterFunctionAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ComVisibleAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, visibility: BooleanType): ...

    # ---------- Properties ---------- #

    @property
    def Value(self) -> BooleanType: ...

    # ---------- Methods ---------- #

    def get_Value(self) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CriticalHandle(ABC, CriticalFinalizerObject, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def IsClosed(self) -> BooleanType: ...
    @property
    def IsInvalid(self) -> BooleanType: ...

    # ---------- Methods ---------- #

    def Close(self) -> VoidType: ...
    def Dispose(self) -> VoidType: ...
    def SetHandleAsInvalid(self) -> VoidType: ...
    def get_IsClosed(self) -> BooleanType: ...
    def get_IsInvalid(self) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CurrencyWrapper(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, obj: DecimalType): ...
    @overload
    def __init__(self, obj: ObjectType): ...

    # ---------- Properties ---------- #

    @property
    def WrappedObject(self) -> DecimalType: ...

    # ---------- Methods ---------- #

    def get_WrappedObject(self) -> DecimalType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DefaultCharSetAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, charSet: CharSet): ...

    # ---------- Properties ---------- #

    @property
    def CharSet(self) -> CharSet: ...

    # ---------- Methods ---------- #

    def get_CharSet(self) -> CharSet: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DefaultDllImportSearchPathsAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, paths: DllImportSearchPath): ...

    # ---------- Properties ---------- #

    @property
    def Paths(self) -> DllImportSearchPath: ...

    # ---------- Methods ---------- #

    def get_Paths(self) -> DllImportSearchPath: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DefaultParameterValueAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, value: ObjectType): ...

    # ---------- Properties ---------- #

    @property
    def Value(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def get_Value(self) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DispIdAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, dispId: IntType): ...

    # ---------- Properties ---------- #

    @property
    def Value(self) -> IntType: ...

    # ---------- Methods ---------- #

    def get_Value(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DispatchWrapper(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, obj: ObjectType): ...

    # ---------- Properties ---------- #

    @property
    def WrappedObject(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def get_WrappedObject(self) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DllImportAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #

    @property
    def BestFitMapping(self) -> BooleanType: ...
    @BestFitMapping.setter
    def BestFitMapping(self, value: BooleanType) -> None: ...
    @property
    def CallingConvention(self) -> CallingConvention: ...
    @CallingConvention.setter
    def CallingConvention(self, value: CallingConvention) -> None: ...
    @property
    def CharSet(self) -> CharSet: ...
    @CharSet.setter
    def CharSet(self, value: CharSet) -> None: ...
    @property
    def EntryPoint(self) -> StringType: ...
    @EntryPoint.setter
    def EntryPoint(self, value: StringType) -> None: ...
    @property
    def ExactSpelling(self) -> BooleanType: ...
    @ExactSpelling.setter
    def ExactSpelling(self, value: BooleanType) -> None: ...
    @property
    def PreserveSig(self) -> BooleanType: ...
    @PreserveSig.setter
    def PreserveSig(self, value: BooleanType) -> None: ...
    @property
    def SetLastError(self) -> BooleanType: ...
    @SetLastError.setter
    def SetLastError(self, value: BooleanType) -> None: ...
    @property
    def ThrowOnUnmappableChar(self) -> BooleanType: ...
    @ThrowOnUnmappableChar.setter
    def ThrowOnUnmappableChar(self, value: BooleanType) -> None: ...

    # ---------- Constructors ---------- #

    def __init__(self, dllName: StringType): ...

    # ---------- Properties ---------- #

    @property
    def Value(self) -> StringType: ...

    # ---------- Methods ---------- #

    def get_Value(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ErrorWrapper(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, errorCode: IntType): ...
    @overload
    def __init__(self, errorCode: ObjectType): ...
    @overload
    def __init__(self, e: Exception): ...

    # ---------- Properties ---------- #

    @property
    def ErrorCode(self) -> IntType: ...

    # ---------- Methods ---------- #

    def get_ErrorCode(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ExtensibleClassFactory(ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    def RegisterObjectCreationCallback(callback: ObjectCreationDelegate) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ExternalException(SystemException, ISerializable, _Exception):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: StringType): ...
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    @overload
    def __init__(self, message: StringType, errorCode: IntType): ...

    # ---------- Properties ---------- #

    @property
    def ErrorCode(self) -> IntType: ...

    # ---------- Methods ---------- #

    def ToString(self) -> StringType: ...
    def get_ErrorCode(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class FieldOffsetAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, offset: IntType): ...

    # ---------- Properties ---------- #

    @property
    def Value(self) -> IntType: ...

    # ---------- Methods ---------- #

    def get_Value(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class GCHandleCookieTable(ObjectType):
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

class GuidAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, guid: StringType): ...

    # ---------- Properties ---------- #

    @property
    def Value(self) -> StringType: ...

    # ---------- Methods ---------- #

    def get_Value(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class HandleCollector(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, name: StringType, initialThreshold: IntType): ...
    @overload
    def __init__(self, name: StringType, initialThreshold: IntType, maximumThreshold: IntType): ...

    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...
    @property
    def InitialThreshold(self) -> IntType: ...
    @property
    def MaximumThreshold(self) -> IntType: ...
    @property
    def Name(self) -> StringType: ...

    # ---------- Methods ---------- #

    def Add(self) -> VoidType: ...
    def Remove(self) -> VoidType: ...
    def get_Count(self) -> IntType: ...
    def get_InitialThreshold(self) -> IntType: ...
    def get_MaximumThreshold(self) -> IntType: ...
    def get_Name(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class IDispatchImplAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, implType: IDispatchImplType): ...
    @overload
    def __init__(self, implType: ShortType): ...

    # ---------- Properties ---------- #

    @property
    def Value(self) -> IDispatchImplType: ...

    # ---------- Methods ---------- #

    def get_Value(self) -> IDispatchImplType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ImportedFromTypeLibAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, tlbFile: StringType): ...

    # ---------- Properties ---------- #

    @property
    def Value(self) -> StringType: ...

    # ---------- Methods ---------- #

    def get_Value(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ImporterCallback(ObjectType, ITypeLibImporterNotifySink):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def ReportEvent(
        self, EventKind: ImporterEventKind, EventCode: IntType, EventMsg: StringType
    ) -> VoidType: ...
    def ResolveRef(self, TypeLib: ObjectType) -> Assembly: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class InAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class InterfaceTypeAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, interfaceType: ComInterfaceType): ...
    @overload
    def __init__(self, interfaceType: ShortType): ...

    # ---------- Properties ---------- #

    @property
    def Value(self) -> ComInterfaceType: ...

    # ---------- Methods ---------- #

    def get_Value(self) -> ComInterfaceType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class InvalidComObjectException(SystemException, ISerializable, _Exception):
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

class InvalidOleVariantTypeException(SystemException, ISerializable, _Exception):
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

class LCIDConversionAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, lcid: IntType): ...

    # ---------- Properties ---------- #

    @property
    def Value(self) -> IntType: ...

    # ---------- Methods ---------- #

    def get_Value(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ManagedToNativeComInteropStubAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, classType: TypeType, methodName: StringType): ...

    # ---------- Properties ---------- #

    @property
    def ClassType(self) -> TypeType: ...
    @property
    def MethodName(self) -> StringType: ...

    # ---------- Methods ---------- #

    def get_ClassType(self) -> TypeType: ...
    def get_MethodName(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Marshal(ABC, ObjectType):
    # ---------- Fields ---------- #

    @staticmethod
    @property
    def SystemDefaultCharSize() -> IntType: ...
    @staticmethod
    @property
    def SystemMaxDBCSCharSize() -> IntType: ...

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    def AddRef(pUnk: NIntType) -> IntType: ...
    @staticmethod
    def AllocCoTaskMem(cb: IntType) -> NIntType: ...
    @staticmethod
    @overload
    def AllocHGlobal(cb: NIntType) -> NIntType: ...
    @staticmethod
    @overload
    def AllocHGlobal(cb: IntType) -> NIntType: ...
    @staticmethod
    def AreComObjectsAvailableForCleanup() -> BooleanType: ...
    @staticmethod
    def BindToMoniker(monikerName: StringType) -> ObjectType: ...
    @staticmethod
    def ChangeWrapperHandleStrength(otp: ObjectType, fIsWeak: BooleanType) -> VoidType: ...
    @staticmethod
    def CleanupUnusedObjectsInCurrentContext() -> VoidType: ...
    @staticmethod
    @overload
    def Copy(
        source: ArrayType[IntType], startIndex: IntType, destination: NIntType, length: IntType
    ) -> VoidType: ...
    @staticmethod
    @overload
    def Copy(
        source: ArrayType[CharType], startIndex: IntType, destination: NIntType, length: IntType
    ) -> VoidType: ...
    @staticmethod
    @overload
    def Copy(
        source: ArrayType[ShortType], startIndex: IntType, destination: NIntType, length: IntType
    ) -> VoidType: ...
    @staticmethod
    @overload
    def Copy(
        source: ArrayType[LongType], startIndex: IntType, destination: NIntType, length: IntType
    ) -> VoidType: ...
    @staticmethod
    @overload
    def Copy(
        source: ArrayType[FloatType], startIndex: IntType, destination: NIntType, length: IntType
    ) -> VoidType: ...
    @staticmethod
    @overload
    def Copy(
        source: ArrayType[DoubleType], startIndex: IntType, destination: NIntType, length: IntType
    ) -> VoidType: ...
    @staticmethod
    @overload
    def Copy(
        source: ArrayType[ByteType], startIndex: IntType, destination: NIntType, length: IntType
    ) -> VoidType: ...
    @staticmethod
    @overload
    def Copy(
        source: ArrayType[NIntType], startIndex: IntType, destination: NIntType, length: IntType
    ) -> VoidType: ...
    @staticmethod
    @overload
    def Copy(
        source: NIntType, destination: ArrayType[IntType], startIndex: IntType, length: IntType
    ) -> VoidType: ...
    @staticmethod
    @overload
    def Copy(
        source: NIntType, destination: ArrayType[CharType], startIndex: IntType, length: IntType
    ) -> VoidType: ...
    @staticmethod
    @overload
    def Copy(
        source: NIntType, destination: ArrayType[ShortType], startIndex: IntType, length: IntType
    ) -> VoidType: ...
    @staticmethod
    @overload
    def Copy(
        source: NIntType, destination: ArrayType[LongType], startIndex: IntType, length: IntType
    ) -> VoidType: ...
    @staticmethod
    @overload
    def Copy(
        source: NIntType, destination: ArrayType[FloatType], startIndex: IntType, length: IntType
    ) -> VoidType: ...
    @staticmethod
    @overload
    def Copy(
        source: NIntType, destination: ArrayType[DoubleType], startIndex: IntType, length: IntType
    ) -> VoidType: ...
    @staticmethod
    @overload
    def Copy(
        source: NIntType, destination: ArrayType[ByteType], startIndex: IntType, length: IntType
    ) -> VoidType: ...
    @staticmethod
    @overload
    def Copy(
        source: NIntType, destination: ArrayType[NIntType], startIndex: IntType, length: IntType
    ) -> VoidType: ...
    @staticmethod
    @overload
    def CreateAggregatedObject(pOuter: NIntType, o: ObjectType) -> NIntType: ...
    @staticmethod
    @overload
    def CreateAggregatedObject(pOuter: NIntType, o: T) -> NIntType: ...
    @staticmethod
    @overload
    def CreateWrapperOfType(o: ObjectType, t: TypeType) -> ObjectType: ...
    @staticmethod
    @overload
    def CreateWrapperOfType(o: T) -> TWrapper: ...
    @staticmethod
    @overload
    def DestroyStructure(ptr: NIntType) -> VoidType: ...
    @staticmethod
    @overload
    def DestroyStructure(ptr: NIntType, structuretype: TypeType) -> VoidType: ...
    @staticmethod
    def FinalReleaseComObject(o: ObjectType) -> IntType: ...
    @staticmethod
    def FreeBSTR(ptr: NIntType) -> VoidType: ...
    @staticmethod
    def FreeCoTaskMem(ptr: NIntType) -> VoidType: ...
    @staticmethod
    def FreeHGlobal(hglobal: NIntType) -> VoidType: ...
    @staticmethod
    def GenerateGuidForType(type: TypeType) -> Guid: ...
    @staticmethod
    def GenerateProgIdForType(type: TypeType) -> StringType: ...
    @staticmethod
    def GetActiveObject(progID: StringType) -> ObjectType: ...
    @staticmethod
    @overload
    def GetComInterfaceForObject(o: ObjectType, T: TypeType) -> NIntType: ...
    @staticmethod
    @overload
    def GetComInterfaceForObject(
        o: ObjectType, T: TypeType, mode: CustomQueryInterfaceMode
    ) -> NIntType: ...
    @staticmethod
    @overload
    def GetComInterfaceForObject(o: T) -> NIntType: ...
    @staticmethod
    def GetComInterfaceForObjectInContext(o: ObjectType, t: TypeType) -> NIntType: ...
    @staticmethod
    def GetComObjectData(obj: ObjectType, key: ObjectType) -> ObjectType: ...
    @staticmethod
    def GetComSlotForMethodInfo(m: MemberInfo) -> IntType: ...
    @staticmethod
    @overload
    def GetDelegateForFunctionPointer(ptr: NIntType, t: TypeType) -> Delegate: ...
    @staticmethod
    @overload
    def GetDelegateForFunctionPointer(ptr: NIntType) -> TDelegate: ...
    @staticmethod
    def GetEndComSlot(t: TypeType) -> IntType: ...
    @staticmethod
    def GetExceptionCode() -> IntType: ...
    @staticmethod
    @overload
    def GetExceptionForHR(errorCode: IntType) -> Exception: ...
    @staticmethod
    @overload
    def GetExceptionForHR(errorCode: IntType, errorInfo: NIntType) -> Exception: ...
    @staticmethod
    def GetExceptionPointers() -> NIntType: ...
    @staticmethod
    @overload
    def GetFunctionPointerForDelegate(d: Delegate) -> NIntType: ...
    @staticmethod
    @overload
    def GetFunctionPointerForDelegate(d: TDelegate) -> NIntType: ...
    @staticmethod
    def GetHINSTANCE(m: Module) -> NIntType: ...
    @staticmethod
    def GetHRForException(e: Exception) -> IntType: ...
    @staticmethod
    def GetHRForLastWin32Error() -> IntType: ...
    @staticmethod
    def GetIDispatchForObject(o: ObjectType) -> NIntType: ...
    @staticmethod
    def GetIDispatchForObjectInContext(o: ObjectType) -> NIntType: ...
    @staticmethod
    def GetITypeInfoForType(t: TypeType) -> NIntType: ...
    @staticmethod
    def GetIUnknownForObject(o: ObjectType) -> NIntType: ...
    @staticmethod
    def GetIUnknownForObjectInContext(o: ObjectType) -> NIntType: ...
    @staticmethod
    def GetLastWin32Error() -> IntType: ...
    @staticmethod
    def GetManagedThunkForUnmanagedMethodPtr(
        pfnMethodToWrap: NIntType, pbSignature: NIntType, cbSignature: IntType
    ) -> NIntType: ...
    @staticmethod
    def GetMethodInfoForComSlot(
        t: TypeType, slot: IntType, memberType: ComMemberType
    ) -> Tuple[MemberInfo, ComMemberType]: ...
    @staticmethod
    @overload
    def GetNativeVariantForObject(obj: ObjectType, pDstNativeVariant: NIntType) -> VoidType: ...
    @staticmethod
    @overload
    def GetNativeVariantForObject(obj: T, pDstNativeVariant: NIntType) -> VoidType: ...
    @staticmethod
    def GetObjectForIUnknown(pUnk: NIntType) -> ObjectType: ...
    @staticmethod
    @overload
    def GetObjectForNativeVariant(pSrcNativeVariant: NIntType) -> ObjectType: ...
    @staticmethod
    @overload
    def GetObjectForNativeVariant(pSrcNativeVariant: NIntType) -> T: ...
    @staticmethod
    @overload
    def GetObjectsForNativeVariants(
        aSrcNativeVariant: NIntType, cVars: IntType
    ) -> ArrayType[ObjectType]: ...
    @staticmethod
    @overload
    def GetObjectsForNativeVariants(
        aSrcNativeVariant: NIntType, cVars: IntType
    ) -> ArrayType[T]: ...
    @staticmethod
    def GetStartComSlot(t: TypeType) -> IntType: ...
    @staticmethod
    def GetThreadFromFiberCookie(cookie: IntType) -> Thread: ...
    @staticmethod
    def GetTypeForITypeInfo(piTypeInfo: NIntType) -> TypeType: ...
    @staticmethod
    def GetTypeFromCLSID(clsid: Guid) -> TypeType: ...
    @staticmethod
    @overload
    def GetTypeInfoName(pTI: UCOMITypeInfo) -> StringType: ...
    @staticmethod
    @overload
    def GetTypeInfoName(typeInfo: ITypeInfo) -> StringType: ...
    @staticmethod
    @overload
    def GetTypeLibGuid(pTLB: UCOMITypeLib) -> Guid: ...
    @staticmethod
    @overload
    def GetTypeLibGuid(typelib: ITypeLib) -> Guid: ...
    @staticmethod
    def GetTypeLibGuidForAssembly(asm: Assembly) -> Guid: ...
    @staticmethod
    @overload
    def GetTypeLibLcid(pTLB: UCOMITypeLib) -> IntType: ...
    @staticmethod
    @overload
    def GetTypeLibLcid(typelib: ITypeLib) -> IntType: ...
    @staticmethod
    @overload
    def GetTypeLibName(pTLB: UCOMITypeLib) -> StringType: ...
    @staticmethod
    @overload
    def GetTypeLibName(typelib: ITypeLib) -> StringType: ...
    @staticmethod
    def GetTypeLibVersionForAssembly(
        inputAssembly: Assembly, majorVersion: IntType, minorVersion: IntType
    ) -> Tuple[VoidType, IntType, IntType]: ...
    @staticmethod
    def GetTypedObjectForIUnknown(pUnk: NIntType, t: TypeType) -> ObjectType: ...
    @staticmethod
    def GetUniqueObjectForIUnknown(unknown: NIntType) -> ObjectType: ...
    @staticmethod
    def GetUnmanagedThunkForManagedMethodPtr(
        pfnMethodToWrap: NIntType, pbSignature: NIntType, cbSignature: IntType
    ) -> NIntType: ...
    @staticmethod
    def IsComObject(o: ObjectType) -> BooleanType: ...
    @staticmethod
    def IsTypeVisibleFromCom(t: TypeType) -> BooleanType: ...
    @staticmethod
    def NumParamBytes(m: MethodInfo) -> IntType: ...
    @staticmethod
    @overload
    def OffsetOf(t: TypeType, fieldName: StringType) -> NIntType: ...
    @staticmethod
    @overload
    def OffsetOf(fieldName: StringType) -> NIntType: ...
    @staticmethod
    def Prelink(m: MethodInfo) -> VoidType: ...
    @staticmethod
    def PrelinkAll(c: TypeType) -> VoidType: ...
    @staticmethod
    @overload
    def PtrToStringAnsi(ptr: NIntType) -> StringType: ...
    @staticmethod
    @overload
    def PtrToStringAnsi(ptr: NIntType, len: IntType) -> StringType: ...
    @staticmethod
    @overload
    def PtrToStringAuto(ptr: NIntType, len: IntType) -> StringType: ...
    @staticmethod
    @overload
    def PtrToStringAuto(ptr: NIntType) -> StringType: ...
    @staticmethod
    def PtrToStringBSTR(ptr: NIntType) -> StringType: ...
    @staticmethod
    @overload
    def PtrToStringUni(ptr: NIntType, len: IntType) -> StringType: ...
    @staticmethod
    @overload
    def PtrToStringUni(ptr: NIntType) -> StringType: ...
    @staticmethod
    @overload
    def PtrToStructure(ptr: NIntType, structure: ObjectType) -> VoidType: ...
    @staticmethod
    @overload
    def PtrToStructure(ptr: NIntType, structureType: TypeType) -> ObjectType: ...
    @staticmethod
    @overload
    def PtrToStructure(ptr: NIntType, structure: T) -> VoidType: ...
    @staticmethod
    @overload
    def PtrToStructure(ptr: NIntType) -> T: ...
    @staticmethod
    def QueryInterface(
        pUnk: NIntType, iid: Guid, ppv: NIntType
    ) -> Tuple[IntType, Guid, NIntType]: ...
    @staticmethod
    def ReAllocCoTaskMem(pv: NIntType, cb: IntType) -> NIntType: ...
    @staticmethod
    def ReAllocHGlobal(pv: NIntType, cb: NIntType) -> NIntType: ...
    @staticmethod
    @overload
    def ReadByte(ptr: NIntType, ofs: IntType) -> ByteType: ...
    @staticmethod
    @overload
    def ReadByte(ptr: NIntType) -> ByteType: ...
    @staticmethod
    @overload
    def ReadByte(ptr: ObjectType, ofs: IntType) -> ByteType: ...
    @staticmethod
    @overload
    def ReadInt16(ptr: NIntType, ofs: IntType) -> ShortType: ...
    @staticmethod
    @overload
    def ReadInt16(ptr: NIntType) -> ShortType: ...
    @staticmethod
    @overload
    def ReadInt16(ptr: ObjectType, ofs: IntType) -> ShortType: ...
    @staticmethod
    @overload
    def ReadInt32(ptr: NIntType, ofs: IntType) -> IntType: ...
    @staticmethod
    @overload
    def ReadInt32(ptr: NIntType) -> IntType: ...
    @staticmethod
    @overload
    def ReadInt32(ptr: ObjectType, ofs: IntType) -> IntType: ...
    @staticmethod
    @overload
    def ReadInt64(ptr: NIntType, ofs: IntType) -> LongType: ...
    @staticmethod
    @overload
    def ReadInt64(ptr: NIntType) -> LongType: ...
    @staticmethod
    @overload
    def ReadInt64(ptr: ObjectType, ofs: IntType) -> LongType: ...
    @staticmethod
    @overload
    def ReadIntPtr(ptr: ObjectType, ofs: IntType) -> NIntType: ...
    @staticmethod
    @overload
    def ReadIntPtr(ptr: NIntType, ofs: IntType) -> NIntType: ...
    @staticmethod
    @overload
    def ReadIntPtr(ptr: NIntType) -> NIntType: ...
    @staticmethod
    def Release(pUnk: NIntType) -> IntType: ...
    @staticmethod
    def ReleaseComObject(o: ObjectType) -> IntType: ...
    @staticmethod
    def ReleaseThreadCache() -> VoidType: ...
    @staticmethod
    def SecureStringToBSTR(s: SecureString) -> NIntType: ...
    @staticmethod
    def SecureStringToCoTaskMemAnsi(s: SecureString) -> NIntType: ...
    @staticmethod
    def SecureStringToCoTaskMemUnicode(s: SecureString) -> NIntType: ...
    @staticmethod
    def SecureStringToGlobalAllocAnsi(s: SecureString) -> NIntType: ...
    @staticmethod
    def SecureStringToGlobalAllocUnicode(s: SecureString) -> NIntType: ...
    @staticmethod
    def SetComObjectData(obj: ObjectType, key: ObjectType, data: ObjectType) -> BooleanType: ...
    @staticmethod
    @overload
    def SizeOf(structure: ObjectType) -> IntType: ...
    @staticmethod
    @overload
    def SizeOf(t: TypeType) -> IntType: ...
    @staticmethod
    @overload
    def SizeOf(structure: T) -> IntType: ...
    @staticmethod
    @overload
    def SizeOf() -> IntType: ...
    @staticmethod
    def StringToBSTR(s: StringType) -> NIntType: ...
    @staticmethod
    def StringToCoTaskMemAnsi(s: StringType) -> NIntType: ...
    @staticmethod
    def StringToCoTaskMemAuto(s: StringType) -> NIntType: ...
    @staticmethod
    def StringToCoTaskMemUni(s: StringType) -> NIntType: ...
    @staticmethod
    def StringToHGlobalAnsi(s: StringType) -> NIntType: ...
    @staticmethod
    def StringToHGlobalAuto(s: StringType) -> NIntType: ...
    @staticmethod
    def StringToHGlobalUni(s: StringType) -> NIntType: ...
    @staticmethod
    @overload
    def StructureToPtr(structure: T, ptr: NIntType, fDeleteOld: BooleanType) -> VoidType: ...
    @staticmethod
    @overload
    def StructureToPtr(
        structure: ObjectType, ptr: NIntType, fDeleteOld: BooleanType
    ) -> VoidType: ...
    @staticmethod
    @overload
    def ThrowExceptionForHR(errorCode: IntType) -> VoidType: ...
    @staticmethod
    @overload
    def ThrowExceptionForHR(errorCode: IntType, errorInfo: NIntType) -> VoidType: ...
    @staticmethod
    @overload
    def UnsafeAddrOfPinnedArrayElement(arr: ArrayType[T], index: IntType) -> NIntType: ...
    @staticmethod
    @overload
    def UnsafeAddrOfPinnedArrayElement(arr: Array, index: IntType) -> NIntType: ...
    @staticmethod
    @overload
    def WriteByte(ptr: NIntType, ofs: IntType, val: ByteType) -> VoidType: ...
    @staticmethod
    @overload
    def WriteByte(ptr: NIntType, val: ByteType) -> VoidType: ...
    @staticmethod
    @overload
    def WriteByte(ptr: ObjectType, ofs: IntType, val: ByteType) -> Tuple[VoidType, ObjectType]: ...
    @staticmethod
    @overload
    def WriteInt16(ptr: NIntType, ofs: IntType, val: ShortType) -> VoidType: ...
    @staticmethod
    @overload
    def WriteInt16(ptr: NIntType, val: ShortType) -> VoidType: ...
    @staticmethod
    @overload
    def WriteInt16(ptr: NIntType, ofs: IntType, val: CharType) -> VoidType: ...
    @staticmethod
    @overload
    def WriteInt16(ptr: ObjectType, ofs: IntType, val: CharType) -> Tuple[VoidType, ObjectType]: ...
    @staticmethod
    @overload
    def WriteInt16(ptr: NIntType, val: CharType) -> VoidType: ...
    @staticmethod
    @overload
    def WriteInt16(
        ptr: ObjectType, ofs: IntType, val: ShortType
    ) -> Tuple[VoidType, ObjectType]: ...
    @staticmethod
    @overload
    def WriteInt32(ptr: NIntType, ofs: IntType, val: IntType) -> VoidType: ...
    @staticmethod
    @overload
    def WriteInt32(ptr: NIntType, val: IntType) -> VoidType: ...
    @staticmethod
    @overload
    def WriteInt32(ptr: ObjectType, ofs: IntType, val: IntType) -> Tuple[VoidType, ObjectType]: ...
    @staticmethod
    @overload
    def WriteInt64(ptr: NIntType, ofs: IntType, val: LongType) -> VoidType: ...
    @staticmethod
    @overload
    def WriteInt64(ptr: NIntType, val: LongType) -> VoidType: ...
    @staticmethod
    @overload
    def WriteInt64(ptr: ObjectType, ofs: IntType, val: LongType) -> Tuple[VoidType, ObjectType]: ...
    @staticmethod
    @overload
    def WriteIntPtr(ptr: NIntType, ofs: IntType, val: NIntType) -> VoidType: ...
    @staticmethod
    @overload
    def WriteIntPtr(
        ptr: ObjectType, ofs: IntType, val: NIntType
    ) -> Tuple[VoidType, ObjectType]: ...
    @staticmethod
    @overload
    def WriteIntPtr(ptr: NIntType, val: NIntType) -> VoidType: ...
    @staticmethod
    def ZeroFreeBSTR(s: NIntType) -> VoidType: ...
    @staticmethod
    def ZeroFreeCoTaskMemAnsi(s: NIntType) -> VoidType: ...
    @staticmethod
    def ZeroFreeCoTaskMemUnicode(s: NIntType) -> VoidType: ...
    @staticmethod
    def ZeroFreeGlobalAllocAnsi(s: NIntType) -> VoidType: ...
    @staticmethod
    def ZeroFreeGlobalAllocUnicode(s: NIntType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class MarshalAsAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #

    @property
    def ArraySubType(self) -> UnmanagedType: ...
    @ArraySubType.setter
    def ArraySubType(self, value: UnmanagedType) -> None: ...
    @property
    def IidParameterIndex(self) -> IntType: ...
    @IidParameterIndex.setter
    def IidParameterIndex(self, value: IntType) -> None: ...
    @property
    def MarshalCookie(self) -> StringType: ...
    @MarshalCookie.setter
    def MarshalCookie(self, value: StringType) -> None: ...
    @property
    def MarshalType(self) -> StringType: ...
    @MarshalType.setter
    def MarshalType(self, value: StringType) -> None: ...
    @property
    def MarshalTypeRef(self) -> TypeType: ...
    @MarshalTypeRef.setter
    def MarshalTypeRef(self, value: TypeType) -> None: ...
    @property
    def SafeArraySubType(self) -> VarEnum: ...
    @SafeArraySubType.setter
    def SafeArraySubType(self, value: VarEnum) -> None: ...
    @property
    def SafeArrayUserDefinedSubType(self) -> TypeType: ...
    @SafeArrayUserDefinedSubType.setter
    def SafeArrayUserDefinedSubType(self, value: TypeType) -> None: ...
    @property
    def SizeConst(self) -> IntType: ...
    @SizeConst.setter
    def SizeConst(self, value: IntType) -> None: ...
    @property
    def SizeParamIndex(self) -> ShortType: ...
    @SizeParamIndex.setter
    def SizeParamIndex(self, value: ShortType) -> None: ...

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, unmanagedType: UnmanagedType): ...
    @overload
    def __init__(self, unmanagedType: ShortType): ...

    # ---------- Properties ---------- #

    @property
    def Value(self) -> UnmanagedType: ...

    # ---------- Methods ---------- #

    def get_Value(self) -> UnmanagedType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class MarshalDirectiveException(SystemException, ISerializable, _Exception):
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

class NativeBuffer(ObjectType, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, initialMinCapacity: ULongType): ...

    # ---------- Properties ---------- #

    @property
    def ByteCapacity(self) -> ULongType: ...
    def __getitem__(self, key: ULongType) -> ByteType: ...
    def __setitem__(self, key: ULongType, value: ByteType) -> None: ...

    # ---------- Methods ---------- #

    def Dispose(self) -> VoidType: ...
    def EnsureByteCapacity(self, minCapacity: ULongType) -> VoidType: ...
    def Free(self) -> VoidType: ...
    def GetHandle(self) -> SafeHandle: ...
    def get_ByteCapacity(self) -> ULongType: ...
    def get_Item(self, index: ULongType) -> ByteType: ...
    def set_Item(self, index: ULongType, value: ByteType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class NativeMethods(ABC, ObjectType):
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

class ObjectCreationDelegate(MulticastDelegate, ICloneable, ISerializable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, object: ObjectType, method: NIntType): ...

    # No Properties

    # ---------- Methods ---------- #

    def BeginInvoke(
        self, aggregator: NIntType, callback: AsyncCallback, object: ObjectType
    ) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> NIntType: ...
    def Invoke(self, aggregator: NIntType) -> NIntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class OptionalAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class OutAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class PreserveSigAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class PrimaryInteropAssemblyAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, major: IntType, minor: IntType): ...

    # ---------- Properties ---------- #

    @property
    def MajorVersion(self) -> IntType: ...
    @property
    def MinorVersion(self) -> IntType: ...

    # ---------- Methods ---------- #

    def get_MajorVersion(self) -> IntType: ...
    def get_MinorVersion(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ProgIdAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, progId: StringType): ...

    # ---------- Properties ---------- #

    @property
    def Value(self) -> StringType: ...

    # ---------- Methods ---------- #

    def get_Value(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RegistrationServices(ObjectType, IRegistrationServices):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def GetManagedCategoryGuid(self) -> Guid: ...
    def GetProgIdForType(self, type: TypeType) -> StringType: ...
    def GetRegistrableTypesInAssembly(self, assembly: Assembly) -> ArrayType[TypeType]: ...
    def RegisterAssembly(
        self, assembly: Assembly, flags: AssemblyRegistrationFlags
    ) -> BooleanType: ...
    @overload
    def RegisterTypeForComClients(self, type: TypeType, g: Guid) -> Tuple[VoidType, Guid]: ...
    @overload
    def RegisterTypeForComClients(
        self,
        type: TypeType,
        classContext: RegistrationClassContext,
        flags: RegistrationConnectionType,
    ) -> IntType: ...
    def TypeRepresentsComType(self, type: TypeType) -> BooleanType: ...
    def TypeRequiresRegistration(self, type: TypeType) -> BooleanType: ...
    def UnregisterAssembly(self, assembly: Assembly) -> BooleanType: ...
    def UnregisterTypeForComClients(self, cookie: IntType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RuntimeEnvironment(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @staticmethod
    @property
    def SystemConfigurationFile() -> StringType: ...

    # ---------- Methods ---------- #

    @staticmethod
    def FromGlobalAccessCache(a: Assembly) -> BooleanType: ...
    @staticmethod
    def GetRuntimeDirectory() -> StringType: ...
    @staticmethod
    def GetRuntimeInterfaceAsIntPtr(clsid: Guid, riid: Guid) -> NIntType: ...
    @staticmethod
    def GetRuntimeInterfaceAsObject(clsid: Guid, riid: Guid) -> ObjectType: ...
    @staticmethod
    def GetSystemVersion() -> StringType: ...
    @staticmethod
    def get_SystemConfigurationFile() -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RuntimeInformation(ABC, ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @staticmethod
    @property
    def FrameworkDescription() -> StringType: ...
    @staticmethod
    @property
    def OSArchitecture() -> Architecture: ...
    @staticmethod
    @property
    def OSDescription() -> StringType: ...
    @staticmethod
    @property
    def ProcessArchitecture() -> Architecture: ...

    # ---------- Methods ---------- #

    @staticmethod
    def IsOSPlatform(osPlatform: OSPlatform) -> BooleanType: ...
    @staticmethod
    def get_FrameworkDescription() -> StringType: ...
    @staticmethod
    def get_OSArchitecture() -> Architecture: ...
    @staticmethod
    def get_OSDescription() -> StringType: ...
    @staticmethod
    def get_ProcessArchitecture() -> Architecture: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SEHException(ExternalException, ISerializable, _Exception):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: StringType): ...
    @overload
    def __init__(self, message: StringType, inner: Exception): ...

    # No Properties

    # ---------- Methods ---------- #

    def CanResume(self) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SafeArrayRankMismatchException(SystemException, ISerializable, _Exception):
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

class SafeArrayTypeMismatchException(SystemException, ISerializable, _Exception):
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

class SafeBuffer(ABC, SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def ByteLength(self) -> ULongType: ...

    # ---------- Methods ---------- #

    def AcquirePointer(self, pointer: ByteType) -> Tuple[VoidType, ByteType]: ...
    @overload
    def Initialize(self, numBytes: ULongType) -> VoidType: ...
    @overload
    def Initialize(self, numElements: UIntType, sizeOfEachElement: UIntType) -> VoidType: ...
    @overload
    def Initialize(self, numElements: UIntType) -> VoidType: ...
    def Read(self, byteOffset: ULongType) -> T: ...
    def ReadArray(
        self, byteOffset: ULongType, array: ArrayType[T], index: IntType, count: IntType
    ) -> VoidType: ...
    def ReleasePointer(self) -> VoidType: ...
    def Write(self, byteOffset: ULongType, value: T) -> VoidType: ...
    def WriteArray(
        self, byteOffset: ULongType, array: ArrayType[T], index: IntType, count: IntType
    ) -> VoidType: ...
    def get_ByteLength(self) -> ULongType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SafeHandle(ABC, CriticalFinalizerObject, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def IsClosed(self) -> BooleanType: ...
    @property
    def IsInvalid(self) -> BooleanType: ...

    # ---------- Methods ---------- #

    def Close(self) -> VoidType: ...
    def DangerousAddRef(self, success: BooleanType) -> Tuple[VoidType, BooleanType]: ...
    def DangerousGetHandle(self) -> NIntType: ...
    def DangerousRelease(self) -> VoidType: ...
    def Dispose(self) -> VoidType: ...
    def SetHandleAsInvalid(self) -> VoidType: ...
    def get_IsClosed(self) -> BooleanType: ...
    def get_IsInvalid(self) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SafeHeapHandle(SafeBuffer, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, byteLength: ULongType): ...

    # ---------- Properties ---------- #

    @property
    def IsInvalid(self) -> BooleanType: ...

    # ---------- Methods ---------- #

    def Resize(self, byteLength: ULongType) -> VoidType: ...
    def get_IsInvalid(self) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SafeHeapHandleCache(ObjectType, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self, minSize: ULongType = 64, maxSize: ULongType = 2048, maxHandles: IntType = ...
    ): ...

    # No Properties

    # ---------- Methods ---------- #

    def Acquire(self, minSize: ULongType) -> SafeHeapHandle: ...
    def Dispose(self) -> VoidType: ...
    def Release(self, handle: SafeHeapHandle) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SetWin32ContextInIDispatchAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class StandardOleMarshalObject(MarshalByRefObject, IMarshal):
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

class StringBuffer(NativeBuffer, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, initialCapacity: UIntType): ...
    @overload
    def __init__(self, initialContents: StringType): ...
    @overload
    def __init__(self, initialContents: StringBuffer): ...

    # ---------- Properties ---------- #

    @property
    def CharCapacity(self) -> UIntType: ...
    def __getitem__(self, key: UIntType) -> CharType: ...
    def __setitem__(self, key: UIntType, value: CharType) -> None: ...
    @property
    def Length(self) -> UIntType: ...
    @Length.setter
    def Length(self, value: UIntType) -> None: ...

    # ---------- Methods ---------- #

    @overload
    def Append(self, value: StringType, startIndex: IntType, count: IntType = -1) -> VoidType: ...
    @overload
    def Append(self, value: StringBuffer, startIndex: UIntType) -> VoidType: ...
    @overload
    def Append(self, value: StringBuffer, startIndex: UIntType, count: UIntType) -> VoidType: ...
    def Contains(self, value: CharType) -> BooleanType: ...
    def CopyFrom(
        self, bufferIndex: UIntType, source: StringType, sourceIndex: IntType, count: IntType = -1
    ) -> VoidType: ...
    def CopyTo(
        self,
        bufferIndex: UIntType,
        destination: StringBuffer,
        destinationIndex: UIntType,
        count: UIntType,
    ) -> VoidType: ...
    def EnsureCharCapacity(self, minCapacity: UIntType) -> VoidType: ...
    def Free(self) -> VoidType: ...
    def SetLengthToFirstNull(self) -> VoidType: ...
    def StartsWith(self, value: StringType) -> BooleanType: ...
    def Substring(self, startIndex: UIntType, count: IntType = -1) -> StringType: ...
    def SubstringEquals(
        self, value: StringType, startIndex: UIntType, count: IntType = -1
    ) -> BooleanType: ...
    def ToString(self) -> StringType: ...
    def TrimEnd(self, values: ArrayType[CharType]) -> VoidType: ...
    def get_CharCapacity(self) -> UIntType: ...
    @overload
    def get_Item(self, index: UIntType) -> CharType: ...
    def get_Length(self) -> UIntType: ...
    @overload
    def set_Item(self, index: UIntType, value: CharType) -> VoidType: ...
    def set_Length(self, value: UIntType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class StructLayoutAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #

    @property
    def CharSet(self) -> CharSet: ...
    @CharSet.setter
    def CharSet(self, value: CharSet) -> None: ...
    @property
    def Pack(self) -> IntType: ...
    @Pack.setter
    def Pack(self, value: IntType) -> None: ...
    @property
    def Size(self) -> IntType: ...
    @Size.setter
    def Size(self, value: IntType) -> None: ...

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, layoutKind: LayoutKind): ...
    @overload
    def __init__(self, layoutKind: ShortType): ...

    # ---------- Properties ---------- #

    @property
    def Value(self) -> LayoutKind: ...

    # ---------- Methods ---------- #

    def get_Value(self) -> LayoutKind: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TypeIdentifierAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, scope: StringType, identifier: StringType): ...

    # ---------- Properties ---------- #

    @property
    def Identifier(self) -> StringType: ...
    @property
    def Scope(self) -> StringType: ...

    # ---------- Methods ---------- #

    def get_Identifier(self) -> StringType: ...
    def get_Scope(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TypeLibConverter(ObjectType, ITypeLibConverter):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def ConvertAssemblyToTypeLib(
        self,
        assembly: Assembly,
        strTypeLibName: StringType,
        flags: TypeLibExporterFlags,
        notifySink: ITypeLibExporterNotifySink,
    ) -> ObjectType: ...
    @overload
    def ConvertTypeLibToAssembly(
        self,
        typeLib: ObjectType,
        asmFileName: StringType,
        flags: IntType,
        notifySink: ITypeLibImporterNotifySink,
        publicKey: ArrayType[ByteType],
        keyPair: StrongNameKeyPair,
        unsafeInterfaces: BooleanType,
    ) -> AssemblyBuilder: ...
    @overload
    def ConvertTypeLibToAssembly(
        self,
        typeLib: ObjectType,
        asmFileName: StringType,
        flags: TypeLibImporterFlags,
        notifySink: ITypeLibImporterNotifySink,
        publicKey: ArrayType[ByteType],
        keyPair: StrongNameKeyPair,
        asmNamespace: StringType,
        asmVersion: Version,
    ) -> AssemblyBuilder: ...
    def GetPrimaryInteropAssembly(
        self,
        g: Guid,
        major: IntType,
        minor: IntType,
        lcid: IntType,
        asmName: StringType,
        asmCodeBase: StringType,
    ) -> Tuple[BooleanType, StringType, StringType]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TypeLibFuncAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, flags: TypeLibFuncFlags): ...
    @overload
    def __init__(self, flags: ShortType): ...

    # ---------- Properties ---------- #

    @property
    def Value(self) -> TypeLibFuncFlags: ...

    # ---------- Methods ---------- #

    def get_Value(self) -> TypeLibFuncFlags: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TypeLibImportClassAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, importClass: TypeType): ...

    # ---------- Properties ---------- #

    @property
    def Value(self) -> StringType: ...

    # ---------- Methods ---------- #

    def get_Value(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TypeLibTypeAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, flags: TypeLibTypeFlags): ...
    @overload
    def __init__(self, flags: ShortType): ...

    # ---------- Properties ---------- #

    @property
    def Value(self) -> TypeLibTypeFlags: ...

    # ---------- Methods ---------- #

    def get_Value(self) -> TypeLibTypeFlags: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TypeLibVarAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, flags: TypeLibVarFlags): ...
    @overload
    def __init__(self, flags: ShortType): ...

    # ---------- Properties ---------- #

    @property
    def Value(self) -> TypeLibVarFlags: ...

    # ---------- Methods ---------- #

    def get_Value(self) -> TypeLibVarFlags: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TypeLibVersionAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, major: IntType, minor: IntType): ...

    # ---------- Properties ---------- #

    @property
    def MajorVersion(self) -> IntType: ...
    @property
    def MinorVersion(self) -> IntType: ...

    # ---------- Methods ---------- #

    def get_MajorVersion(self) -> IntType: ...
    def get_MinorVersion(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class UnknownWrapper(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, obj: ObjectType): ...

    # ---------- Properties ---------- #

    @property
    def WrappedObject(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def get_WrappedObject(self) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class UnmanagedFunctionPointerAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #

    @property
    def BestFitMapping(self) -> BooleanType: ...
    @BestFitMapping.setter
    def BestFitMapping(self, value: BooleanType) -> None: ...
    @property
    def CharSet(self) -> CharSet: ...
    @CharSet.setter
    def CharSet(self, value: CharSet) -> None: ...
    @property
    def SetLastError(self) -> BooleanType: ...
    @SetLastError.setter
    def SetLastError(self, value: BooleanType) -> None: ...
    @property
    def ThrowOnUnmappableChar(self) -> BooleanType: ...
    @ThrowOnUnmappableChar.setter
    def ThrowOnUnmappableChar(self, value: BooleanType) -> None: ...

    # ---------- Constructors ---------- #

    def __init__(self, callingConvention: CallingConvention): ...

    # ---------- Properties ---------- #

    @property
    def CallingConvention(self) -> CallingConvention: ...

    # ---------- Methods ---------- #

    def get_CallingConvention(self) -> CallingConvention: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class VariantWrapper(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, obj: ObjectType): ...

    # ---------- Properties ---------- #

    @property
    def WrappedObject(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def get_WrappedObject(self) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# ---------- Structs ---------- #

class ArrayWithOffset(ValueType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, array: ObjectType, offset: IntType): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    @overload
    def Equals(self, obj: ArrayWithOffset) -> BooleanType: ...
    def GetArray(self) -> ObjectType: ...
    def GetHashCode(self) -> IntType: ...
    def GetOffset(self) -> IntType: ...
    @staticmethod
    def op_Equality(a: ArrayWithOffset, b: ArrayWithOffset) -> BooleanType: ...
    @staticmethod
    def op_Inequality(a: ArrayWithOffset, b: ArrayWithOffset) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class BINDPTR(ValueType):
    # ---------- Fields ---------- #

    @property
    def lpfuncdesc(self) -> NIntType: ...
    @lpfuncdesc.setter
    def lpfuncdesc(self, value: NIntType) -> None: ...
    @property
    def lptcomp(self) -> NIntType: ...
    @lptcomp.setter
    def lptcomp(self, value: NIntType) -> None: ...
    @property
    def lpvardesc(self) -> NIntType: ...
    @lpvardesc.setter
    def lpvardesc(self, value: NIntType) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class BIND_OPTS(ValueType):
    # ---------- Fields ---------- #

    @property
    def cbStruct(self) -> IntType: ...
    @cbStruct.setter
    def cbStruct(self, value: IntType) -> None: ...
    @property
    def dwTickCountDeadline(self) -> IntType: ...
    @dwTickCountDeadline.setter
    def dwTickCountDeadline(self, value: IntType) -> None: ...
    @property
    def grfFlags(self) -> IntType: ...
    @grfFlags.setter
    def grfFlags(self, value: IntType) -> None: ...
    @property
    def grfMode(self) -> IntType: ...
    @grfMode.setter
    def grfMode(self, value: IntType) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CONNECTDATA(ValueType):
    # ---------- Fields ---------- #

    @property
    def dwCookie(self) -> IntType: ...
    @dwCookie.setter
    def dwCookie(self, value: IntType) -> None: ...
    @property
    def pUnk(self) -> ObjectType: ...
    @pUnk.setter
    def pUnk(self, value: ObjectType) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DISPPARAMS(ValueType):
    # ---------- Fields ---------- #

    @property
    def cArgs(self) -> IntType: ...
    @cArgs.setter
    def cArgs(self, value: IntType) -> None: ...
    @property
    def cNamedArgs(self) -> IntType: ...
    @cNamedArgs.setter
    def cNamedArgs(self, value: IntType) -> None: ...
    @property
    def rgdispidNamedArgs(self) -> NIntType: ...
    @rgdispidNamedArgs.setter
    def rgdispidNamedArgs(self, value: NIntType) -> None: ...
    @property
    def rgvarg(self) -> NIntType: ...
    @rgvarg.setter
    def rgvarg(self, value: NIntType) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ELEMDESC(ValueType):
    # ---------- Fields ---------- #

    @property
    def desc(self) -> DESCUNION: ...
    @desc.setter
    def desc(self, value: DESCUNION) -> None: ...
    @property
    def tdesc(self) -> TYPEDESC: ...
    @tdesc.setter
    def tdesc(self, value: TYPEDESC) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # ---------- Sub Structs ---------- #

    class DESCUNION(ValueType):
        # ---------- Fields ---------- #

        @property
        def idldesc(self) -> IDLDESC: ...
        @idldesc.setter
        def idldesc(self, value: IDLDESC) -> None: ...
        @property
        def paramdesc(self) -> PARAMDESC: ...
        @paramdesc.setter
        def paramdesc(self, value: PARAMDESC) -> None: ...

        # No Constructors

        # No Properties

        # No Methods

        # No Events

        # No Sub Classes

        # No Sub Structs

        # No Sub Interfaces

        # No Sub Enums
    # No Sub Interfaces

    # No Sub Enums

class EXCEPINFO(ValueType):
    # ---------- Fields ---------- #

    @property
    def bstrDescription(self) -> StringType: ...
    @bstrDescription.setter
    def bstrDescription(self, value: StringType) -> None: ...
    @property
    def bstrHelpFile(self) -> StringType: ...
    @bstrHelpFile.setter
    def bstrHelpFile(self, value: StringType) -> None: ...
    @property
    def bstrSource(self) -> StringType: ...
    @bstrSource.setter
    def bstrSource(self, value: StringType) -> None: ...
    @property
    def dwHelpContext(self) -> IntType: ...
    @dwHelpContext.setter
    def dwHelpContext(self, value: IntType) -> None: ...
    @property
    def pfnDeferredFillIn(self) -> NIntType: ...
    @pfnDeferredFillIn.setter
    def pfnDeferredFillIn(self, value: NIntType) -> None: ...
    @property
    def pvReserved(self) -> NIntType: ...
    @pvReserved.setter
    def pvReserved(self, value: NIntType) -> None: ...
    @property
    def wCode(self) -> ShortType: ...
    @wCode.setter
    def wCode(self, value: ShortType) -> None: ...
    @property
    def wReserved(self) -> ShortType: ...
    @wReserved.setter
    def wReserved(self, value: ShortType) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class FILETIME(ValueType):
    # ---------- Fields ---------- #

    @property
    def dwHighDateTime(self) -> IntType: ...
    @dwHighDateTime.setter
    def dwHighDateTime(self, value: IntType) -> None: ...
    @property
    def dwLowDateTime(self) -> IntType: ...
    @dwLowDateTime.setter
    def dwLowDateTime(self, value: IntType) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class FUNCDESC(ValueType):
    # ---------- Fields ---------- #

    @property
    def cParams(self) -> ShortType: ...
    @cParams.setter
    def cParams(self, value: ShortType) -> None: ...
    @property
    def cParamsOpt(self) -> ShortType: ...
    @cParamsOpt.setter
    def cParamsOpt(self, value: ShortType) -> None: ...
    @property
    def cScodes(self) -> ShortType: ...
    @cScodes.setter
    def cScodes(self, value: ShortType) -> None: ...
    @property
    def callconv(self) -> CALLCONV: ...
    @callconv.setter
    def callconv(self, value: CALLCONV) -> None: ...
    @property
    def elemdescFunc(self) -> ELEMDESC: ...
    @elemdescFunc.setter
    def elemdescFunc(self, value: ELEMDESC) -> None: ...
    @property
    def funckind(self) -> FUNCKIND: ...
    @funckind.setter
    def funckind(self, value: FUNCKIND) -> None: ...
    @property
    def invkind(self) -> INVOKEKIND: ...
    @invkind.setter
    def invkind(self, value: INVOKEKIND) -> None: ...
    @property
    def lprgelemdescParam(self) -> NIntType: ...
    @lprgelemdescParam.setter
    def lprgelemdescParam(self, value: NIntType) -> None: ...
    @property
    def lprgscode(self) -> NIntType: ...
    @lprgscode.setter
    def lprgscode(self, value: NIntType) -> None: ...
    @property
    def memid(self) -> IntType: ...
    @memid.setter
    def memid(self, value: IntType) -> None: ...
    @property
    def oVft(self) -> ShortType: ...
    @oVft.setter
    def oVft(self, value: ShortType) -> None: ...
    @property
    def wFuncFlags(self) -> ShortType: ...
    @wFuncFlags.setter
    def wFuncFlags(self, value: ShortType) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class GCHandle(ValueType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def IsAllocated(self) -> BooleanType: ...
    @property
    def Target(self) -> ObjectType: ...
    @Target.setter
    def Target(self, value: ObjectType) -> None: ...

    # ---------- Methods ---------- #

    def AddrOfPinnedObject(self) -> NIntType: ...
    @staticmethod
    @overload
    def Alloc(value: ObjectType) -> GCHandle: ...
    @staticmethod
    @overload
    def Alloc(value: ObjectType, type: GCHandleType) -> GCHandle: ...
    def Equals(self, o: ObjectType) -> BooleanType: ...
    def Free(self) -> VoidType: ...
    @staticmethod
    def FromIntPtr(value: NIntType) -> GCHandle: ...
    def GetHashCode(self) -> IntType: ...
    @staticmethod
    def ToIntPtr(value: GCHandle) -> NIntType: ...
    def get_IsAllocated(self) -> BooleanType: ...
    def get_Target(self) -> ObjectType: ...
    @staticmethod
    def op_Equality(a: GCHandle, b: GCHandle) -> BooleanType: ...
    @staticmethod
    @overload
    def op_Explicit(value: NIntType) -> GCHandle: ...
    @staticmethod
    @overload
    def op_Explicit(value: GCHandle) -> NIntType: ...
    @staticmethod
    def op_Inequality(a: GCHandle, b: GCHandle) -> BooleanType: ...
    def set_Target(self, value: ObjectType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class HandleRef(ValueType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, wrapper: ObjectType, handle: NIntType): ...

    # ---------- Properties ---------- #

    @property
    def Handle(self) -> NIntType: ...
    @property
    def Wrapper(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    @staticmethod
    def ToIntPtr(value: HandleRef) -> NIntType: ...
    def get_Handle(self) -> NIntType: ...
    def get_Wrapper(self) -> ObjectType: ...
    @staticmethod
    def op_Explicit(value: HandleRef) -> NIntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class IDLDESC(ValueType):
    # ---------- Fields ---------- #

    @property
    def dwReserved(self) -> IntType: ...
    @dwReserved.setter
    def dwReserved(self, value: IntType) -> None: ...
    @property
    def wIDLFlags(self) -> IDLFLAG: ...
    @wIDLFlags.setter
    def wIDLFlags(self, value: IDLFLAG) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class OSPlatform(ValueType, IEquatable[OSPlatform]):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @staticmethod
    @property
    def Linux() -> OSPlatform: ...
    @staticmethod
    @property
    def OSX() -> OSPlatform: ...
    @staticmethod
    @property
    def Windows() -> OSPlatform: ...

    # ---------- Methods ---------- #

    @staticmethod
    def Create(osPlatform: StringType) -> OSPlatform: ...
    @overload
    def Equals(self, other: OSPlatform) -> BooleanType: ...
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    def GetHashCode(self) -> IntType: ...
    def ToString(self) -> StringType: ...
    @staticmethod
    def get_Linux() -> OSPlatform: ...
    @staticmethod
    def get_OSX() -> OSPlatform: ...
    @staticmethod
    def get_Windows() -> OSPlatform: ...
    @staticmethod
    def op_Equality(left: OSPlatform, right: OSPlatform) -> BooleanType: ...
    @staticmethod
    def op_Inequality(left: OSPlatform, right: OSPlatform) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class PARAMDESC(ValueType):
    # ---------- Fields ---------- #

    @property
    def lpVarValue(self) -> NIntType: ...
    @lpVarValue.setter
    def lpVarValue(self, value: NIntType) -> None: ...
    @property
    def wParamFlags(self) -> PARAMFLAG: ...
    @wParamFlags.setter
    def wParamFlags(self, value: PARAMFLAG) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class STATSTG(ValueType):
    # ---------- Fields ---------- #

    @property
    def atime(self) -> FILETIME: ...
    @atime.setter
    def atime(self, value: FILETIME) -> None: ...
    @property
    def cbSize(self) -> LongType: ...
    @cbSize.setter
    def cbSize(self, value: LongType) -> None: ...
    @property
    def clsid(self) -> Guid: ...
    @clsid.setter
    def clsid(self, value: Guid) -> None: ...
    @property
    def ctime(self) -> FILETIME: ...
    @ctime.setter
    def ctime(self, value: FILETIME) -> None: ...
    @property
    def grfLocksSupported(self) -> IntType: ...
    @grfLocksSupported.setter
    def grfLocksSupported(self, value: IntType) -> None: ...
    @property
    def grfMode(self) -> IntType: ...
    @grfMode.setter
    def grfMode(self, value: IntType) -> None: ...
    @property
    def grfStateBits(self) -> IntType: ...
    @grfStateBits.setter
    def grfStateBits(self, value: IntType) -> None: ...
    @property
    def mtime(self) -> FILETIME: ...
    @mtime.setter
    def mtime(self, value: FILETIME) -> None: ...
    @property
    def pwcsName(self) -> StringType: ...
    @pwcsName.setter
    def pwcsName(self, value: StringType) -> None: ...
    @property
    def reserved(self) -> IntType: ...
    @reserved.setter
    def reserved(self, value: IntType) -> None: ...
    @property
    def type(self) -> IntType: ...
    @type.setter
    def type(self, value: IntType) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TYPEATTR(ValueType):
    # ---------- Fields ---------- #

    @staticmethod
    @property
    def MEMBER_ID_NIL() -> IntType: ...
    @property
    def cFuncs(self) -> ShortType: ...
    @cFuncs.setter
    def cFuncs(self, value: ShortType) -> None: ...
    @property
    def cImplTypes(self) -> ShortType: ...
    @cImplTypes.setter
    def cImplTypes(self, value: ShortType) -> None: ...
    @property
    def cVars(self) -> ShortType: ...
    @cVars.setter
    def cVars(self, value: ShortType) -> None: ...
    @property
    def cbAlignment(self) -> ShortType: ...
    @cbAlignment.setter
    def cbAlignment(self, value: ShortType) -> None: ...
    @property
    def cbSizeInstance(self) -> IntType: ...
    @cbSizeInstance.setter
    def cbSizeInstance(self, value: IntType) -> None: ...
    @property
    def cbSizeVft(self) -> ShortType: ...
    @cbSizeVft.setter
    def cbSizeVft(self, value: ShortType) -> None: ...
    @property
    def dwReserved(self) -> IntType: ...
    @dwReserved.setter
    def dwReserved(self, value: IntType) -> None: ...
    @property
    def guid(self) -> Guid: ...
    @guid.setter
    def guid(self, value: Guid) -> None: ...
    @property
    def idldescType(self) -> IDLDESC: ...
    @idldescType.setter
    def idldescType(self, value: IDLDESC) -> None: ...
    @property
    def lcid(self) -> IntType: ...
    @lcid.setter
    def lcid(self, value: IntType) -> None: ...
    @property
    def lpstrSchema(self) -> NIntType: ...
    @lpstrSchema.setter
    def lpstrSchema(self, value: NIntType) -> None: ...
    @property
    def memidConstructor(self) -> IntType: ...
    @memidConstructor.setter
    def memidConstructor(self, value: IntType) -> None: ...
    @property
    def memidDestructor(self) -> IntType: ...
    @memidDestructor.setter
    def memidDestructor(self, value: IntType) -> None: ...
    @property
    def tdescAlias(self) -> TYPEDESC: ...
    @tdescAlias.setter
    def tdescAlias(self, value: TYPEDESC) -> None: ...
    @property
    def typekind(self) -> TYPEKIND: ...
    @typekind.setter
    def typekind(self, value: TYPEKIND) -> None: ...
    @property
    def wMajorVerNum(self) -> ShortType: ...
    @wMajorVerNum.setter
    def wMajorVerNum(self, value: ShortType) -> None: ...
    @property
    def wMinorVerNum(self) -> ShortType: ...
    @wMinorVerNum.setter
    def wMinorVerNum(self, value: ShortType) -> None: ...
    @property
    def wTypeFlags(self) -> TYPEFLAGS: ...
    @wTypeFlags.setter
    def wTypeFlags(self, value: TYPEFLAGS) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TYPEDESC(ValueType):
    # ---------- Fields ---------- #

    @property
    def lpValue(self) -> NIntType: ...
    @lpValue.setter
    def lpValue(self, value: NIntType) -> None: ...
    @property
    def vt(self) -> ShortType: ...
    @vt.setter
    def vt(self, value: ShortType) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TYPELIBATTR(ValueType):
    # ---------- Fields ---------- #

    @property
    def guid(self) -> Guid: ...
    @guid.setter
    def guid(self, value: Guid) -> None: ...
    @property
    def lcid(self) -> IntType: ...
    @lcid.setter
    def lcid(self, value: IntType) -> None: ...
    @property
    def syskind(self) -> SYSKIND: ...
    @syskind.setter
    def syskind(self, value: SYSKIND) -> None: ...
    @property
    def wLibFlags(self) -> LIBFLAGS: ...
    @wLibFlags.setter
    def wLibFlags(self, value: LIBFLAGS) -> None: ...
    @property
    def wMajorVerNum(self) -> ShortType: ...
    @wMajorVerNum.setter
    def wMajorVerNum(self, value: ShortType) -> None: ...
    @property
    def wMinorVerNum(self) -> ShortType: ...
    @wMinorVerNum.setter
    def wMinorVerNum(self, value: ShortType) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class VARDESC(ValueType):
    # ---------- Fields ---------- #

    @property
    def elemdescVar(self) -> ELEMDESC: ...
    @elemdescVar.setter
    def elemdescVar(self, value: ELEMDESC) -> None: ...
    @property
    def lpstrSchema(self) -> StringType: ...
    @lpstrSchema.setter
    def lpstrSchema(self, value: StringType) -> None: ...
    @property
    def memid(self) -> IntType: ...
    @memid.setter
    def memid(self, value: IntType) -> None: ...
    @property
    def varkind(self) -> VarEnum: ...
    @varkind.setter
    def varkind(self, value: VarEnum) -> None: ...
    @property
    def wVarFlags(self) -> ShortType: ...
    @wVarFlags.setter
    def wVarFlags(self, value: ShortType) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # ---------- Sub Structs ---------- #

    class DESCUNION(ValueType):
        # ---------- Fields ---------- #

        @property
        def lpvarValue(self) -> NIntType: ...
        @lpvarValue.setter
        def lpvarValue(self, value: NIntType) -> None: ...
        @property
        def oInst(self) -> IntType: ...
        @oInst.setter
        def oInst(self, value: IntType) -> None: ...

        # No Constructors

        # No Properties

        # No Methods

        # No Events

        # No Sub Classes

        # No Sub Structs

        # No Sub Interfaces

        # No Sub Enums
    # No Sub Interfaces

    # No Sub Enums

class Variant(ValueType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def AsBool(self) -> BooleanType: ...
    @AsBool.setter
    def AsBool(self, value: BooleanType) -> None: ...
    @property
    def AsBstr(self) -> StringType: ...
    @AsBstr.setter
    def AsBstr(self, value: StringType) -> None: ...
    @property
    def AsCy(self) -> DecimalType: ...
    @AsCy.setter
    def AsCy(self, value: DecimalType) -> None: ...
    @property
    def AsDate(self) -> DateTime: ...
    @AsDate.setter
    def AsDate(self, value: DateTime) -> None: ...
    @property
    def AsDecimal(self) -> DecimalType: ...
    @AsDecimal.setter
    def AsDecimal(self, value: DecimalType) -> None: ...
    @property
    def AsDispatch(self) -> ObjectType: ...
    @AsDispatch.setter
    def AsDispatch(self, value: ObjectType) -> None: ...
    @property
    def AsError(self) -> IntType: ...
    @AsError.setter
    def AsError(self, value: IntType) -> None: ...
    @property
    def AsI1(self) -> SByteType: ...
    @AsI1.setter
    def AsI1(self, value: SByteType) -> None: ...
    @property
    def AsI2(self) -> ShortType: ...
    @AsI2.setter
    def AsI2(self, value: ShortType) -> None: ...
    @property
    def AsI4(self) -> IntType: ...
    @AsI4.setter
    def AsI4(self, value: IntType) -> None: ...
    @property
    def AsI8(self) -> LongType: ...
    @AsI8.setter
    def AsI8(self, value: LongType) -> None: ...
    @property
    def AsInt(self) -> IntType: ...
    @AsInt.setter
    def AsInt(self, value: IntType) -> None: ...
    @property
    def AsR4(self) -> FloatType: ...
    @AsR4.setter
    def AsR4(self, value: FloatType) -> None: ...
    @property
    def AsR8(self) -> DoubleType: ...
    @AsR8.setter
    def AsR8(self, value: DoubleType) -> None: ...
    @property
    def AsUi1(self) -> ByteType: ...
    @AsUi1.setter
    def AsUi1(self, value: ByteType) -> None: ...
    @property
    def AsUi2(self) -> UShortType: ...
    @AsUi2.setter
    def AsUi2(self, value: UShortType) -> None: ...
    @property
    def AsUi4(self) -> UIntType: ...
    @AsUi4.setter
    def AsUi4(self, value: UIntType) -> None: ...
    @property
    def AsUi8(self) -> ULongType: ...
    @AsUi8.setter
    def AsUi8(self, value: ULongType) -> None: ...
    @property
    def AsUint(self) -> UIntType: ...
    @AsUint.setter
    def AsUint(self, value: UIntType) -> None: ...
    @property
    def AsUnknown(self) -> ObjectType: ...
    @AsUnknown.setter
    def AsUnknown(self, value: ObjectType) -> None: ...
    @property
    def VariantType(self) -> VarEnum: ...
    @VariantType.setter
    def VariantType(self, value: VarEnum) -> None: ...

    # ---------- Methods ---------- #

    def Clear(self) -> VoidType: ...
    def CopyFromIndirect(self, value: ObjectType) -> VoidType: ...
    def SetAsNULL(self) -> VoidType: ...
    def ToObject(self) -> ObjectType: ...
    def get_AsBool(self) -> BooleanType: ...
    def get_AsBstr(self) -> StringType: ...
    def get_AsCy(self) -> DecimalType: ...
    def get_AsDate(self) -> DateTime: ...
    def get_AsDecimal(self) -> DecimalType: ...
    def get_AsDispatch(self) -> ObjectType: ...
    def get_AsError(self) -> IntType: ...
    def get_AsI1(self) -> SByteType: ...
    def get_AsI2(self) -> ShortType: ...
    def get_AsI4(self) -> IntType: ...
    def get_AsI8(self) -> LongType: ...
    def get_AsInt(self) -> IntType: ...
    def get_AsR4(self) -> FloatType: ...
    def get_AsR8(self) -> DoubleType: ...
    def get_AsUi1(self) -> ByteType: ...
    def get_AsUi2(self) -> UShortType: ...
    def get_AsUi4(self) -> UIntType: ...
    def get_AsUi8(self) -> ULongType: ...
    def get_AsUint(self) -> UIntType: ...
    def get_AsUnknown(self) -> ObjectType: ...
    def get_VariantType(self) -> VarEnum: ...
    def set_AsBool(self, value: BooleanType) -> VoidType: ...
    def set_AsBstr(self, value: StringType) -> VoidType: ...
    def set_AsCy(self, value: DecimalType) -> VoidType: ...
    def set_AsDate(self, value: DateTime) -> VoidType: ...
    def set_AsDecimal(self, value: DecimalType) -> VoidType: ...
    def set_AsDispatch(self, value: ObjectType) -> VoidType: ...
    def set_AsError(self, value: IntType) -> VoidType: ...
    def set_AsI1(self, value: SByteType) -> VoidType: ...
    def set_AsI2(self, value: ShortType) -> VoidType: ...
    def set_AsI4(self, value: IntType) -> VoidType: ...
    def set_AsI8(self, value: LongType) -> VoidType: ...
    def set_AsInt(self, value: IntType) -> VoidType: ...
    def set_AsR4(self, value: FloatType) -> VoidType: ...
    def set_AsR8(self, value: DoubleType) -> VoidType: ...
    def set_AsUi1(self, value: ByteType) -> VoidType: ...
    def set_AsUi2(self, value: UShortType) -> VoidType: ...
    def set_AsUi4(self, value: UIntType) -> VoidType: ...
    def set_AsUi8(self, value: ULongType) -> VoidType: ...
    def set_AsUint(self, value: UIntType) -> VoidType: ...
    def set_AsUnknown(self, value: ObjectType) -> VoidType: ...
    def set_VariantType(self, value: VarEnum) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# ---------- Interfaces ---------- #

class ICustomAdapter(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetUnderlyingObject(self) -> ObjectType: ...

    # No Events

class ICustomFactory(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def CreateInstance(self, serverType: TypeType) -> MarshalByRefObject: ...

    # No Events

class ICustomMarshaler(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def CleanUpManagedData(self, ManagedObj: ObjectType) -> VoidType: ...
    def CleanUpNativeData(self, pNativeData: NIntType) -> VoidType: ...
    def GetNativeDataSize(self) -> IntType: ...
    def MarshalManagedToNative(self, ManagedObj: ObjectType) -> NIntType: ...
    def MarshalNativeToManaged(self, pNativeData: NIntType) -> ObjectType: ...

    # No Events

class ICustomQueryInterface(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetInterface(
        self, iid: Guid, ppv: NIntType
    ) -> Tuple[CustomQueryInterfaceResult, Guid, NIntType]: ...

    # No Events

class IRegistrationServices(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetManagedCategoryGuid(self) -> Guid: ...
    def GetProgIdForType(self, type: TypeType) -> StringType: ...
    def GetRegistrableTypesInAssembly(self, assembly: Assembly) -> ArrayType[TypeType]: ...
    def RegisterAssembly(
        self, assembly: Assembly, flags: AssemblyRegistrationFlags
    ) -> BooleanType: ...
    def RegisterTypeForComClients(self, type: TypeType, g: Guid) -> Tuple[VoidType, Guid]: ...
    def TypeRepresentsComType(self, type: TypeType) -> BooleanType: ...
    def TypeRequiresRegistration(self, type: TypeType) -> BooleanType: ...
    def UnregisterAssembly(self, assembly: Assembly) -> BooleanType: ...

    # No Events

class ITypeLibConverter(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def ConvertAssemblyToTypeLib(
        self,
        assembly: Assembly,
        typeLibName: StringType,
        flags: TypeLibExporterFlags,
        notifySink: ITypeLibExporterNotifySink,
    ) -> ObjectType: ...
    @overload
    def ConvertTypeLibToAssembly(
        self,
        typeLib: ObjectType,
        asmFileName: StringType,
        flags: TypeLibImporterFlags,
        notifySink: ITypeLibImporterNotifySink,
        publicKey: ArrayType[ByteType],
        keyPair: StrongNameKeyPair,
        asmNamespace: StringType,
        asmVersion: Version,
    ) -> AssemblyBuilder: ...
    @overload
    def ConvertTypeLibToAssembly(
        self,
        typeLib: ObjectType,
        asmFileName: StringType,
        flags: IntType,
        notifySink: ITypeLibImporterNotifySink,
        publicKey: ArrayType[ByteType],
        keyPair: StrongNameKeyPair,
        unsafeInterfaces: BooleanType,
    ) -> AssemblyBuilder: ...
    def GetPrimaryInteropAssembly(
        self,
        g: Guid,
        major: IntType,
        minor: IntType,
        lcid: IntType,
        asmName: StringType,
        asmCodeBase: StringType,
    ) -> Tuple[BooleanType, StringType, StringType]: ...

    # No Events

class ITypeLibExporterNameProvider(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetNames(self) -> ArrayType[StringType]: ...

    # No Events

class ITypeLibExporterNotifySink(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def ReportEvent(
        self, eventKind: ExporterEventKind, eventCode: IntType, eventMsg: StringType
    ) -> VoidType: ...
    def ResolveRef(self, assembly: Assembly) -> ObjectType: ...

    # No Events

class ITypeLibImporterNotifySink(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def ReportEvent(
        self, eventKind: ImporterEventKind, eventCode: IntType, eventMsg: StringType
    ) -> VoidType: ...
    def ResolveRef(self, typeLib: ObjectType) -> Assembly: ...

    # No Events

class UCOMIBindCtx(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def EnumObjectParam(self, ppenum: UCOMIEnumString) -> Tuple[VoidType, UCOMIEnumString]: ...
    def GetBindOptions(self, pbindopts: BIND_OPTS) -> Tuple[VoidType, BIND_OPTS]: ...
    def GetObjectParam(
        self, pszKey: StringType, ppunk: ObjectType
    ) -> Tuple[VoidType, ObjectType]: ...
    def GetRunningObjectTable(
        self, pprot: UCOMIRunningObjectTable
    ) -> Tuple[VoidType, UCOMIRunningObjectTable]: ...
    def RegisterObjectBound(self, punk: ObjectType) -> VoidType: ...
    def RegisterObjectParam(self, pszKey: StringType, punk: ObjectType) -> VoidType: ...
    def ReleaseBoundObjects(self) -> VoidType: ...
    def RevokeObjectBound(self, punk: ObjectType) -> VoidType: ...
    def RevokeObjectParam(self, pszKey: StringType) -> VoidType: ...
    def SetBindOptions(self, pbindopts: BIND_OPTS) -> Tuple[VoidType, BIND_OPTS]: ...

    # No Events

class UCOMIConnectionPoint(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Advise(self, pUnkSink: ObjectType, pdwCookie: IntType) -> Tuple[VoidType, IntType]: ...
    def EnumConnections(
        self, ppEnum: UCOMIEnumConnections
    ) -> Tuple[VoidType, UCOMIEnumConnections]: ...
    def GetConnectionInterface(self, pIID: Guid) -> Tuple[VoidType, Guid]: ...
    def GetConnectionPointContainer(
        self, ppCPC: UCOMIConnectionPointContainer
    ) -> Tuple[VoidType, UCOMIConnectionPointContainer]: ...
    def Unadvise(self, dwCookie: IntType) -> VoidType: ...

    # No Events

class UCOMIConnectionPointContainer(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def EnumConnectionPoints(
        self, ppEnum: UCOMIEnumConnectionPoints
    ) -> Tuple[VoidType, UCOMIEnumConnectionPoints]: ...
    def FindConnectionPoint(
        self, riid: Guid, ppCP: UCOMIConnectionPoint
    ) -> Tuple[VoidType, Guid, UCOMIConnectionPoint]: ...

    # No Events

class UCOMIEnumConnectionPoints(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Clone(
        self, ppenum: UCOMIEnumConnectionPoints
    ) -> Tuple[VoidType, UCOMIEnumConnectionPoints]: ...
    def Next(
        self, celt: IntType, rgelt: ArrayType[UCOMIConnectionPoint], pceltFetched: IntType
    ) -> Tuple[IntType, ArrayType[UCOMIConnectionPoint], IntType]: ...
    def Reset(self) -> IntType: ...
    def Skip(self, celt: IntType) -> IntType: ...

    # No Events

class UCOMIEnumConnections(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Clone(self, ppenum: UCOMIEnumConnections) -> Tuple[VoidType, UCOMIEnumConnections]: ...
    def Next(
        self, celt: IntType, rgelt: ArrayType[CONNECTDATA], pceltFetched: IntType
    ) -> Tuple[IntType, ArrayType[CONNECTDATA], IntType]: ...
    def Reset(self) -> VoidType: ...
    def Skip(self, celt: IntType) -> IntType: ...

    # No Events

class UCOMIEnumMoniker(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Clone(self, ppenum: UCOMIEnumMoniker) -> Tuple[VoidType, UCOMIEnumMoniker]: ...
    def Next(
        self, celt: IntType, rgelt: ArrayType[UCOMIMoniker], pceltFetched: IntType
    ) -> Tuple[IntType, ArrayType[UCOMIMoniker], IntType]: ...
    def Reset(self) -> IntType: ...
    def Skip(self, celt: IntType) -> IntType: ...

    # No Events

class UCOMIEnumString(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Clone(self, ppenum: UCOMIEnumString) -> Tuple[VoidType, UCOMIEnumString]: ...
    def Next(
        self, celt: IntType, rgelt: ArrayType[StringType], pceltFetched: IntType
    ) -> Tuple[IntType, ArrayType[StringType], IntType]: ...
    def Reset(self) -> IntType: ...
    def Skip(self, celt: IntType) -> IntType: ...

    # No Events

class UCOMIEnumVARIANT(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Clone(self, ppenum: IntType) -> VoidType: ...
    def Next(self, celt: IntType, rgvar: IntType, pceltFetched: IntType) -> IntType: ...
    def Reset(self) -> IntType: ...
    def Skip(self, celt: IntType) -> IntType: ...

    # No Events

class UCOMIEnumerable(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetEnumerator(self) -> IEnumerator: ...

    # No Events

class UCOMIEnumerator(Protocol):
    # ---------- Properties ---------- #

    @property
    def Current(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def MoveNext(self) -> BooleanType: ...
    def Reset(self) -> VoidType: ...
    def get_Current(self) -> ObjectType: ...

    # No Events

class UCOMIExpando(Protocol, UCOMIReflect):
    # No Properties

    # ---------- Methods ---------- #

    def AddField(self, name: StringType) -> FieldInfo: ...
    def AddMethod(self, name: StringType, method: Delegate) -> MethodInfo: ...
    def AddProperty(self, name: StringType) -> PropertyInfo: ...
    def RemoveMember(self, m: MemberInfo) -> VoidType: ...

    # No Events

class UCOMIMoniker(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def BindToObject(
        self, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, riidResult: Guid, ppvResult: ObjectType
    ) -> Tuple[VoidType, Guid, ObjectType]: ...
    def BindToStorage(
        self, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, riid: Guid, ppvObj: ObjectType
    ) -> Tuple[VoidType, Guid, ObjectType]: ...
    def CommonPrefixWith(
        self, pmkOther: UCOMIMoniker, ppmkPrefix: UCOMIMoniker
    ) -> Tuple[VoidType, UCOMIMoniker]: ...
    def ComposeWith(
        self, pmkRight: UCOMIMoniker, fOnlyIfNotGeneric: BooleanType, ppmkComposite: UCOMIMoniker
    ) -> Tuple[VoidType, UCOMIMoniker]: ...
    def Enum(
        self, fForward: BooleanType, ppenumMoniker: UCOMIEnumMoniker
    ) -> Tuple[VoidType, UCOMIEnumMoniker]: ...
    def GetClassID(self, pClassID: Guid) -> Tuple[VoidType, Guid]: ...
    def GetDisplayName(
        self, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, ppszDisplayName: StringType
    ) -> Tuple[VoidType, StringType]: ...
    def GetSizeMax(self, pcbSize: LongType) -> Tuple[VoidType, LongType]: ...
    def GetTimeOfLastChange(
        self, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, pFileTime: FILETIME
    ) -> Tuple[VoidType, FILETIME]: ...
    def Hash(self, pdwHash: IntType) -> Tuple[VoidType, IntType]: ...
    def Inverse(self, ppmk: UCOMIMoniker) -> Tuple[VoidType, UCOMIMoniker]: ...
    def IsDirty(self) -> IntType: ...
    def IsEqual(self, pmkOtherMoniker: UCOMIMoniker) -> VoidType: ...
    def IsRunning(
        self, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, pmkNewlyRunning: UCOMIMoniker
    ) -> VoidType: ...
    def IsSystemMoniker(self, pdwMksys: IntType) -> Tuple[VoidType, IntType]: ...
    def Load(self, pStm: UCOMIStream) -> VoidType: ...
    def ParseDisplayName(
        self,
        pbc: UCOMIBindCtx,
        pmkToLeft: UCOMIMoniker,
        pszDisplayName: StringType,
        pchEaten: IntType,
        ppmkOut: UCOMIMoniker,
    ) -> Tuple[VoidType, IntType, UCOMIMoniker]: ...
    def Reduce(
        self,
        pbc: UCOMIBindCtx,
        dwReduceHowFar: IntType,
        ppmkToLeft: UCOMIMoniker,
        ppmkReduced: UCOMIMoniker,
    ) -> Tuple[VoidType, UCOMIMoniker, UCOMIMoniker]: ...
    def RelativePathTo(
        self, pmkOther: UCOMIMoniker, ppmkRelPath: UCOMIMoniker
    ) -> Tuple[VoidType, UCOMIMoniker]: ...
    def Save(self, pStm: UCOMIStream, fClearDirty: BooleanType) -> VoidType: ...

    # No Events

class UCOMIPersistFile(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetClassID(self, pClassID: Guid) -> Tuple[VoidType, Guid]: ...
    def GetCurFile(self, ppszFileName: StringType) -> Tuple[VoidType, StringType]: ...
    def IsDirty(self) -> IntType: ...
    def Load(self, pszFileName: StringType, dwMode: IntType) -> VoidType: ...
    def Save(self, pszFileName: StringType, fRemember: BooleanType) -> VoidType: ...
    def SaveCompleted(self, pszFileName: StringType) -> VoidType: ...

    # No Events

class UCOMIReflect(Protocol):
    # ---------- Properties ---------- #

    @property
    def UnderlyingSystemType(self) -> TypeType: ...

    # ---------- Methods ---------- #

    def GetField(self, name: StringType, bindingAttr: BindingFlags) -> FieldInfo: ...
    def GetFields(self, bindingAttr: BindingFlags) -> ArrayType[FieldInfo]: ...
    def GetMember(self, name: StringType, bindingAttr: BindingFlags) -> ArrayType[MemberInfo]: ...
    def GetMembers(self, bindingAttr: BindingFlags) -> ArrayType[MemberInfo]: ...
    @overload
    def GetMethod(
        self,
        name: StringType,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: ArrayType[TypeType],
        modifiers: ArrayType[ParameterModifier],
    ) -> MethodInfo: ...
    @overload
    def GetMethod(self, name: StringType, bindingAttr: BindingFlags) -> MethodInfo: ...
    def GetMethods(self, bindingAttr: BindingFlags) -> ArrayType[MethodInfo]: ...
    def GetProperties(self, bindingAttr: BindingFlags) -> ArrayType[PropertyInfo]: ...
    @overload
    def GetProperty(self, name: StringType, bindingAttr: BindingFlags) -> PropertyInfo: ...
    @overload
    def GetProperty(
        self,
        name: StringType,
        bindingAttr: BindingFlags,
        binder: Binder,
        returnType: TypeType,
        types: ArrayType[TypeType],
        modifiers: ArrayType[ParameterModifier],
    ) -> PropertyInfo: ...
    def InvokeMember(
        self,
        name: StringType,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: ObjectType,
        args: ArrayType[ObjectType],
        modifiers: ArrayType[ParameterModifier],
        culture: CultureInfo,
        namedParameters: ArrayType[StringType],
    ) -> ObjectType: ...
    def get_UnderlyingSystemType(self) -> TypeType: ...

    # No Events

class UCOMIRunningObjectTable(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def EnumRunning(self, ppenumMoniker: UCOMIEnumMoniker) -> Tuple[VoidType, UCOMIEnumMoniker]: ...
    def GetObject(
        self, pmkObjectName: UCOMIMoniker, ppunkObject: ObjectType
    ) -> Tuple[VoidType, ObjectType]: ...
    def GetTimeOfLastChange(
        self, pmkObjectName: UCOMIMoniker, pfiletime: FILETIME
    ) -> Tuple[VoidType, FILETIME]: ...
    def IsRunning(self, pmkObjectName: UCOMIMoniker) -> VoidType: ...
    def NoteChangeTime(
        self, dwRegister: IntType, pfiletime: FILETIME
    ) -> Tuple[VoidType, FILETIME]: ...
    def Register(
        self,
        grfFlags: IntType,
        punkObject: ObjectType,
        pmkObjectName: UCOMIMoniker,
        pdwRegister: IntType,
    ) -> Tuple[VoidType, IntType]: ...
    def Revoke(self, dwRegister: IntType) -> VoidType: ...

    # No Events

class UCOMIStream(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Clone(self, ppstm: UCOMIStream) -> Tuple[VoidType, UCOMIStream]: ...
    def Commit(self, grfCommitFlags: IntType) -> VoidType: ...
    def CopyTo(
        self, pstm: UCOMIStream, cb: LongType, pcbRead: NIntType, pcbWritten: NIntType
    ) -> VoidType: ...
    def LockRegion(self, libOffset: LongType, cb: LongType, dwLockType: IntType) -> VoidType: ...
    def Read(
        self, pv: ArrayType[ByteType], cb: IntType, pcbRead: NIntType
    ) -> Tuple[VoidType, ArrayType[ByteType]]: ...
    def Revert(self) -> VoidType: ...
    def Seek(
        self, dlibMove: LongType, dwOrigin: IntType, plibNewPosition: NIntType
    ) -> VoidType: ...
    def SetSize(self, libNewSize: LongType) -> VoidType: ...
    def Stat(self, pstatstg: STATSTG, grfStatFlag: IntType) -> Tuple[VoidType, STATSTG]: ...
    def UnlockRegion(self, libOffset: LongType, cb: LongType, dwLockType: IntType) -> VoidType: ...
    def Write(self, pv: ArrayType[ByteType], cb: IntType, pcbWritten: NIntType) -> VoidType: ...

    # No Events

class UCOMITypeComp(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Bind(
        self,
        szName: StringType,
        lHashVal: IntType,
        wFlags: ShortType,
        ppTInfo: UCOMITypeInfo,
        pDescKind: DESCKIND,
        pBindPtr: BINDPTR,
    ) -> Tuple[VoidType, UCOMITypeInfo, DESCKIND, BINDPTR]: ...
    def BindType(
        self, szName: StringType, lHashVal: IntType, ppTInfo: UCOMITypeInfo, ppTComp: UCOMITypeComp
    ) -> Tuple[VoidType, UCOMITypeInfo, UCOMITypeComp]: ...

    # No Events

class UCOMITypeInfo(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def AddressOfMember(
        self, memid: IntType, invKind: INVOKEKIND, ppv: NIntType
    ) -> Tuple[VoidType, NIntType]: ...
    def CreateInstance(
        self, pUnkOuter: ObjectType, riid: Guid, ppvObj: ObjectType
    ) -> Tuple[VoidType, Guid, ObjectType]: ...
    def GetContainingTypeLib(
        self, ppTLB: UCOMITypeLib, pIndex: IntType
    ) -> Tuple[VoidType, UCOMITypeLib, IntType]: ...
    def GetDllEntry(
        self,
        memid: IntType,
        invKind: INVOKEKIND,
        pBstrDllName: StringType,
        pBstrName: StringType,
        pwOrdinal: ShortType,
    ) -> Tuple[VoidType, StringType, StringType, ShortType]: ...
    def GetDocumentation(
        self,
        index: IntType,
        strName: StringType,
        strDocString: StringType,
        dwHelpContext: IntType,
        strHelpFile: StringType,
    ) -> Tuple[VoidType, StringType, StringType, IntType, StringType]: ...
    def GetFuncDesc(self, index: IntType, ppFuncDesc: NIntType) -> Tuple[VoidType, NIntType]: ...
    def GetIDsOfNames(
        self, rgszNames: ArrayType[StringType], cNames: IntType, pMemId: ArrayType[IntType]
    ) -> Tuple[VoidType, ArrayType[IntType]]: ...
    def GetImplTypeFlags(
        self, index: IntType, pImplTypeFlags: IntType
    ) -> Tuple[VoidType, IntType]: ...
    def GetMops(self, memid: IntType, pBstrMops: StringType) -> Tuple[VoidType, StringType]: ...
    def GetNames(
        self,
        memid: IntType,
        rgBstrNames: ArrayType[StringType],
        cMaxNames: IntType,
        pcNames: IntType,
    ) -> Tuple[VoidType, ArrayType[StringType], IntType]: ...
    def GetRefTypeInfo(
        self, hRef: IntType, ppTI: UCOMITypeInfo
    ) -> Tuple[VoidType, UCOMITypeInfo]: ...
    def GetRefTypeOfImplType(self, index: IntType, href: IntType) -> Tuple[VoidType, IntType]: ...
    def GetTypeAttr(self, ppTypeAttr: NIntType) -> Tuple[VoidType, NIntType]: ...
    def GetTypeComp(self, ppTComp: UCOMITypeComp) -> Tuple[VoidType, UCOMITypeComp]: ...
    def GetVarDesc(self, index: IntType, ppVarDesc: NIntType) -> Tuple[VoidType, NIntType]: ...
    def Invoke(
        self,
        pvInstance: ObjectType,
        memid: IntType,
        wFlags: ShortType,
        pDispParams: DISPPARAMS,
        pVarResult: ObjectType,
        pExcepInfo: EXCEPINFO,
        puArgErr: IntType,
    ) -> Tuple[VoidType, DISPPARAMS, ObjectType, EXCEPINFO, IntType]: ...
    def ReleaseFuncDesc(self, pFuncDesc: NIntType) -> VoidType: ...
    def ReleaseTypeAttr(self, pTypeAttr: NIntType) -> VoidType: ...
    def ReleaseVarDesc(self, pVarDesc: NIntType) -> VoidType: ...

    # No Events

class UCOMITypeLib(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def FindName(
        self,
        szNameBuf: StringType,
        lHashVal: IntType,
        ppTInfo: ArrayType[UCOMITypeInfo],
        rgMemId: ArrayType[IntType],
        pcFound: ShortType,
    ) -> Tuple[VoidType, ArrayType[UCOMITypeInfo], ArrayType[IntType], ShortType]: ...
    def GetDocumentation(
        self,
        index: IntType,
        strName: StringType,
        strDocString: StringType,
        dwHelpContext: IntType,
        strHelpFile: StringType,
    ) -> Tuple[VoidType, StringType, StringType, IntType, StringType]: ...
    def GetLibAttr(self, ppTLibAttr: NIntType) -> Tuple[VoidType, NIntType]: ...
    def GetTypeComp(self, ppTComp: UCOMITypeComp) -> Tuple[VoidType, UCOMITypeComp]: ...
    def GetTypeInfo(
        self, index: IntType, ppTI: UCOMITypeInfo
    ) -> Tuple[VoidType, UCOMITypeInfo]: ...
    def GetTypeInfoCount(self) -> IntType: ...
    def GetTypeInfoOfGuid(
        self, guid: Guid, ppTInfo: UCOMITypeInfo
    ) -> Tuple[VoidType, Guid, UCOMITypeInfo]: ...
    def GetTypeInfoType(self, index: IntType, pTKind: TYPEKIND) -> Tuple[VoidType, TYPEKIND]: ...
    def IsName(self, szNameBuf: StringType, lHashVal: IntType) -> BooleanType: ...
    def ReleaseTLibAttr(self, pTLibAttr: NIntType) -> VoidType: ...

    # No Events

class _Activator(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...

    # No Events

class _Assembly(Protocol):
    # ---------- Properties ---------- #

    @property
    def CodeBase(self) -> StringType: ...
    @property
    def EntryPoint(self) -> MethodInfo: ...
    @property
    def EscapedCodeBase(self) -> StringType: ...
    @property
    def Evidence(self) -> Evidence: ...
    @property
    def FullName(self) -> StringType: ...
    @property
    def GlobalAssemblyCache(self) -> BooleanType: ...
    @property
    def Location(self) -> StringType: ...

    # ---------- Methods ---------- #

    @overload
    def CreateInstance(self, typeName: StringType) -> ObjectType: ...
    @overload
    def CreateInstance(self, typeName: StringType, ignoreCase: BooleanType) -> ObjectType: ...
    @overload
    def CreateInstance(
        self,
        typeName: StringType,
        ignoreCase: BooleanType,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: ArrayType[ObjectType],
        culture: CultureInfo,
        activationAttributes: ArrayType[ObjectType],
    ) -> ObjectType: ...
    def Equals(self, other: ObjectType) -> BooleanType: ...
    @overload
    def GetCustomAttributes(
        self, attributeType: TypeType, inherit: BooleanType
    ) -> ArrayType[ObjectType]: ...
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    def GetExportedTypes(self) -> ArrayType[TypeType]: ...
    def GetFile(self, name: StringType) -> FileStream: ...
    @overload
    def GetFiles(self) -> ArrayType[FileStream]: ...
    @overload
    def GetFiles(self, getResourceModules: BooleanType) -> ArrayType[FileStream]: ...
    def GetHashCode(self) -> IntType: ...
    @overload
    def GetLoadedModules(self) -> ArrayType[Module]: ...
    @overload
    def GetLoadedModules(self, getResourceModules: BooleanType) -> ArrayType[Module]: ...
    def GetManifestResourceInfo(self, resourceName: StringType) -> ManifestResourceInfo: ...
    def GetManifestResourceNames(self) -> ArrayType[StringType]: ...
    @overload
    def GetManifestResourceStream(self, type: TypeType, name: StringType) -> Stream: ...
    @overload
    def GetManifestResourceStream(self, name: StringType) -> Stream: ...
    def GetModule(self, name: StringType) -> Module: ...
    @overload
    def GetModules(self) -> ArrayType[Module]: ...
    @overload
    def GetModules(self, getResourceModules: BooleanType) -> ArrayType[Module]: ...
    @overload
    def GetName(self) -> AssemblyName: ...
    @overload
    def GetName(self, copiedName: BooleanType) -> AssemblyName: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    def GetReferencedAssemblies(self) -> ArrayType[AssemblyName]: ...
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo) -> Assembly: ...
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo, version: Version) -> Assembly: ...
    @overload
    def GetType(self) -> TypeType: ...
    @overload
    def GetType(self, name: StringType) -> TypeType: ...
    @overload
    def GetType(self, name: StringType, throwOnError: BooleanType) -> TypeType: ...
    @overload
    def GetType(
        self, name: StringType, throwOnError: BooleanType, ignoreCase: BooleanType
    ) -> TypeType: ...
    def GetTypes(self) -> ArrayType[TypeType]: ...
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    @overload
    def LoadModule(self, moduleName: StringType, rawModule: ArrayType[ByteType]) -> Module: ...
    @overload
    def LoadModule(
        self,
        moduleName: StringType,
        rawModule: ArrayType[ByteType],
        rawSymbolStore: ArrayType[ByteType],
    ) -> Module: ...
    def ToString(self) -> StringType: ...
    def add_ModuleResolve(self, value: ModuleResolveEventHandler) -> VoidType: ...
    def get_CodeBase(self) -> StringType: ...
    def get_EntryPoint(self) -> MethodInfo: ...
    def get_EscapedCodeBase(self) -> StringType: ...
    def get_Evidence(self) -> Evidence: ...
    def get_FullName(self) -> StringType: ...
    def get_GlobalAssemblyCache(self) -> BooleanType: ...
    def get_Location(self) -> StringType: ...
    def remove_ModuleResolve(self, value: ModuleResolveEventHandler) -> VoidType: ...

    # ---------- Events ---------- #

    ModuleResolve: EventType[ModuleResolveEventHandler] = ...

class _AssemblyBuilder(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...

    # No Events

class _AssemblyName(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...

    # No Events

class _Attribute(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...

    # No Events

class _ConstructorBuilder(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...

    # No Events

class _ConstructorInfo(Protocol):
    # ---------- Properties ---------- #

    @property
    def Attributes(self) -> MethodAttributes: ...
    @property
    def CallingConvention(self) -> CallingConventions: ...
    @property
    def DeclaringType(self) -> TypeType: ...
    @property
    def IsAbstract(self) -> BooleanType: ...
    @property
    def IsAssembly(self) -> BooleanType: ...
    @property
    def IsConstructor(self) -> BooleanType: ...
    @property
    def IsFamily(self) -> BooleanType: ...
    @property
    def IsFamilyAndAssembly(self) -> BooleanType: ...
    @property
    def IsFamilyOrAssembly(self) -> BooleanType: ...
    @property
    def IsFinal(self) -> BooleanType: ...
    @property
    def IsHideBySig(self) -> BooleanType: ...
    @property
    def IsPrivate(self) -> BooleanType: ...
    @property
    def IsPublic(self) -> BooleanType: ...
    @property
    def IsSpecialName(self) -> BooleanType: ...
    @property
    def IsStatic(self) -> BooleanType: ...
    @property
    def IsVirtual(self) -> BooleanType: ...
    @property
    def MemberType(self) -> MemberTypes: ...
    @property
    def MethodHandle(self) -> RuntimeMethodHandle: ...
    @property
    def Name(self) -> StringType: ...
    @property
    def ReflectedType(self) -> TypeType: ...

    # ---------- Methods ---------- #

    def Equals(self, other: ObjectType) -> BooleanType: ...
    @overload
    def GetCustomAttributes(
        self, attributeType: TypeType, inherit: BooleanType
    ) -> ArrayType[ObjectType]: ...
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    def GetHashCode(self) -> IntType: ...
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetMethodImplementationFlags(self) -> MethodImplAttributes: ...
    def GetParameters(self) -> ArrayType[ParameterInfo]: ...
    def GetType(self) -> TypeType: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...
    def Invoke_2(
        self,
        obj: ObjectType,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: ArrayType[ObjectType],
        culture: CultureInfo,
    ) -> ObjectType: ...
    def Invoke_3(self, obj: ObjectType, parameters: ArrayType[ObjectType]) -> ObjectType: ...
    def Invoke_4(
        self,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: ArrayType[ObjectType],
        culture: CultureInfo,
    ) -> ObjectType: ...
    def Invoke_5(self, parameters: ArrayType[ObjectType]) -> ObjectType: ...
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    def ToString(self) -> StringType: ...
    def get_Attributes(self) -> MethodAttributes: ...
    def get_CallingConvention(self) -> CallingConventions: ...
    def get_DeclaringType(self) -> TypeType: ...
    def get_IsAbstract(self) -> BooleanType: ...
    def get_IsAssembly(self) -> BooleanType: ...
    def get_IsConstructor(self) -> BooleanType: ...
    def get_IsFamily(self) -> BooleanType: ...
    def get_IsFamilyAndAssembly(self) -> BooleanType: ...
    def get_IsFamilyOrAssembly(self) -> BooleanType: ...
    def get_IsFinal(self) -> BooleanType: ...
    def get_IsHideBySig(self) -> BooleanType: ...
    def get_IsPrivate(self) -> BooleanType: ...
    def get_IsPublic(self) -> BooleanType: ...
    def get_IsSpecialName(self) -> BooleanType: ...
    def get_IsStatic(self) -> BooleanType: ...
    def get_IsVirtual(self) -> BooleanType: ...
    def get_MemberType(self) -> MemberTypes: ...
    def get_MethodHandle(self) -> RuntimeMethodHandle: ...
    def get_Name(self) -> StringType: ...
    def get_ReflectedType(self) -> TypeType: ...

    # No Events

class _CustomAttributeBuilder(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...

    # No Events

class _EnumBuilder(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...

    # No Events

class _EventBuilder(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...

    # No Events

class _EventInfo(Protocol):
    # ---------- Properties ---------- #

    @property
    def Attributes(self) -> EventAttributes: ...
    @property
    def DeclaringType(self) -> TypeType: ...
    @property
    def EventHandlerType(self) -> TypeType: ...
    @property
    def IsMulticast(self) -> BooleanType: ...
    @property
    def IsSpecialName(self) -> BooleanType: ...
    @property
    def MemberType(self) -> MemberTypes: ...
    @property
    def Name(self) -> StringType: ...
    @property
    def ReflectedType(self) -> TypeType: ...

    # ---------- Methods ---------- #

    def AddEventHandler(self, target: ObjectType, handler: Delegate) -> VoidType: ...
    def Equals(self, other: ObjectType) -> BooleanType: ...
    @overload
    def GetAddMethod(self, nonPublic: BooleanType) -> MethodInfo: ...
    @overload
    def GetAddMethod(self) -> MethodInfo: ...
    @overload
    def GetCustomAttributes(
        self, attributeType: TypeType, inherit: BooleanType
    ) -> ArrayType[ObjectType]: ...
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    def GetHashCode(self) -> IntType: ...
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    @overload
    def GetRaiseMethod(self, nonPublic: BooleanType) -> MethodInfo: ...
    @overload
    def GetRaiseMethod(self) -> MethodInfo: ...
    @overload
    def GetRemoveMethod(self, nonPublic: BooleanType) -> MethodInfo: ...
    @overload
    def GetRemoveMethod(self) -> MethodInfo: ...
    def GetType(self) -> TypeType: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    def RemoveEventHandler(self, target: ObjectType, handler: Delegate) -> VoidType: ...
    def ToString(self) -> StringType: ...
    def get_Attributes(self) -> EventAttributes: ...
    def get_DeclaringType(self) -> TypeType: ...
    def get_EventHandlerType(self) -> TypeType: ...
    def get_IsMulticast(self) -> BooleanType: ...
    def get_IsSpecialName(self) -> BooleanType: ...
    def get_MemberType(self) -> MemberTypes: ...
    def get_Name(self) -> StringType: ...
    def get_ReflectedType(self) -> TypeType: ...

    # No Events

class _Exception(Protocol):
    # ---------- Properties ---------- #

    @property
    def HelpLink(self) -> StringType: ...
    @HelpLink.setter
    def HelpLink(self, value: StringType) -> None: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> StringType: ...
    @property
    def Source(self) -> StringType: ...
    @Source.setter
    def Source(self, value: StringType) -> None: ...
    @property
    def StackTrace(self) -> StringType: ...
    @property
    def TargetSite(self) -> MethodBase: ...

    # ---------- Methods ---------- #

    def Equals(self, obj: ObjectType) -> BooleanType: ...
    def GetBaseException(self) -> Exception: ...
    def GetHashCode(self) -> IntType: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    def GetType(self) -> TypeType: ...
    def ToString(self) -> StringType: ...
    def get_HelpLink(self) -> StringType: ...
    def get_InnerException(self) -> Exception: ...
    def get_Message(self) -> StringType: ...
    def get_Source(self) -> StringType: ...
    def get_StackTrace(self) -> StringType: ...
    def get_TargetSite(self) -> MethodBase: ...
    def set_HelpLink(self, value: StringType) -> VoidType: ...
    def set_Source(self, value: StringType) -> VoidType: ...

    # No Events

class _FieldBuilder(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...

    # No Events

class _FieldInfo(Protocol):
    # ---------- Properties ---------- #

    @property
    def Attributes(self) -> FieldAttributes: ...
    @property
    def DeclaringType(self) -> TypeType: ...
    @property
    def FieldHandle(self) -> RuntimeFieldHandle: ...
    @property
    def FieldType(self) -> TypeType: ...
    @property
    def IsAssembly(self) -> BooleanType: ...
    @property
    def IsFamily(self) -> BooleanType: ...
    @property
    def IsFamilyAndAssembly(self) -> BooleanType: ...
    @property
    def IsFamilyOrAssembly(self) -> BooleanType: ...
    @property
    def IsInitOnly(self) -> BooleanType: ...
    @property
    def IsLiteral(self) -> BooleanType: ...
    @property
    def IsNotSerialized(self) -> BooleanType: ...
    @property
    def IsPinvokeImpl(self) -> BooleanType: ...
    @property
    def IsPrivate(self) -> BooleanType: ...
    @property
    def IsPublic(self) -> BooleanType: ...
    @property
    def IsSpecialName(self) -> BooleanType: ...
    @property
    def IsStatic(self) -> BooleanType: ...
    @property
    def MemberType(self) -> MemberTypes: ...
    @property
    def Name(self) -> StringType: ...
    @property
    def ReflectedType(self) -> TypeType: ...

    # ---------- Methods ---------- #

    def Equals(self, other: ObjectType) -> BooleanType: ...
    @overload
    def GetCustomAttributes(
        self, attributeType: TypeType, inherit: BooleanType
    ) -> ArrayType[ObjectType]: ...
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    def GetHashCode(self) -> IntType: ...
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetType(self) -> TypeType: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def GetValue(self, obj: ObjectType) -> ObjectType: ...
    def GetValueDirect(self, obj: TypedReference) -> ObjectType: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    @overload
    def SetValue(
        self,
        obj: ObjectType,
        value: ObjectType,
        invokeAttr: BindingFlags,
        binder: Binder,
        culture: CultureInfo,
    ) -> VoidType: ...
    @overload
    def SetValue(self, obj: ObjectType, value: ObjectType) -> VoidType: ...
    def SetValueDirect(self, obj: TypedReference, value: ObjectType) -> VoidType: ...
    def ToString(self) -> StringType: ...
    def get_Attributes(self) -> FieldAttributes: ...
    def get_DeclaringType(self) -> TypeType: ...
    def get_FieldHandle(self) -> RuntimeFieldHandle: ...
    def get_FieldType(self) -> TypeType: ...
    def get_IsAssembly(self) -> BooleanType: ...
    def get_IsFamily(self) -> BooleanType: ...
    def get_IsFamilyAndAssembly(self) -> BooleanType: ...
    def get_IsFamilyOrAssembly(self) -> BooleanType: ...
    def get_IsInitOnly(self) -> BooleanType: ...
    def get_IsLiteral(self) -> BooleanType: ...
    def get_IsNotSerialized(self) -> BooleanType: ...
    def get_IsPinvokeImpl(self) -> BooleanType: ...
    def get_IsPrivate(self) -> BooleanType: ...
    def get_IsPublic(self) -> BooleanType: ...
    def get_IsSpecialName(self) -> BooleanType: ...
    def get_IsStatic(self) -> BooleanType: ...
    def get_MemberType(self) -> MemberTypes: ...
    def get_Name(self) -> StringType: ...
    def get_ReflectedType(self) -> TypeType: ...

    # No Events

class _ILGenerator(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...

    # No Events

class _LocalBuilder(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...

    # No Events

class _MemberInfo(Protocol):
    # ---------- Properties ---------- #

    @property
    def DeclaringType(self) -> TypeType: ...
    @property
    def MemberType(self) -> MemberTypes: ...
    @property
    def Name(self) -> StringType: ...
    @property
    def ReflectedType(self) -> TypeType: ...

    # ---------- Methods ---------- #

    def Equals(self, other: ObjectType) -> BooleanType: ...
    @overload
    def GetCustomAttributes(
        self, attributeType: TypeType, inherit: BooleanType
    ) -> ArrayType[ObjectType]: ...
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    def GetHashCode(self) -> IntType: ...
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetType(self) -> TypeType: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    def ToString(self) -> StringType: ...
    def get_DeclaringType(self) -> TypeType: ...
    def get_MemberType(self) -> MemberTypes: ...
    def get_Name(self) -> StringType: ...
    def get_ReflectedType(self) -> TypeType: ...

    # No Events

class _MethodBase(Protocol):
    # ---------- Properties ---------- #

    @property
    def Attributes(self) -> MethodAttributes: ...
    @property
    def CallingConvention(self) -> CallingConventions: ...
    @property
    def DeclaringType(self) -> TypeType: ...
    @property
    def IsAbstract(self) -> BooleanType: ...
    @property
    def IsAssembly(self) -> BooleanType: ...
    @property
    def IsConstructor(self) -> BooleanType: ...
    @property
    def IsFamily(self) -> BooleanType: ...
    @property
    def IsFamilyAndAssembly(self) -> BooleanType: ...
    @property
    def IsFamilyOrAssembly(self) -> BooleanType: ...
    @property
    def IsFinal(self) -> BooleanType: ...
    @property
    def IsHideBySig(self) -> BooleanType: ...
    @property
    def IsPrivate(self) -> BooleanType: ...
    @property
    def IsPublic(self) -> BooleanType: ...
    @property
    def IsSpecialName(self) -> BooleanType: ...
    @property
    def IsStatic(self) -> BooleanType: ...
    @property
    def IsVirtual(self) -> BooleanType: ...
    @property
    def MemberType(self) -> MemberTypes: ...
    @property
    def MethodHandle(self) -> RuntimeMethodHandle: ...
    @property
    def Name(self) -> StringType: ...
    @property
    def ReflectedType(self) -> TypeType: ...

    # ---------- Methods ---------- #

    def Equals(self, other: ObjectType) -> BooleanType: ...
    @overload
    def GetCustomAttributes(
        self, attributeType: TypeType, inherit: BooleanType
    ) -> ArrayType[ObjectType]: ...
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    def GetHashCode(self) -> IntType: ...
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetMethodImplementationFlags(self) -> MethodImplAttributes: ...
    def GetParameters(self) -> ArrayType[ParameterInfo]: ...
    def GetType(self) -> TypeType: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    @overload
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...
    @overload
    def Invoke(
        self,
        obj: ObjectType,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: ArrayType[ObjectType],
        culture: CultureInfo,
    ) -> ObjectType: ...
    @overload
    def Invoke(self, obj: ObjectType, parameters: ArrayType[ObjectType]) -> ObjectType: ...
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    def ToString(self) -> StringType: ...
    def get_Attributes(self) -> MethodAttributes: ...
    def get_CallingConvention(self) -> CallingConventions: ...
    def get_DeclaringType(self) -> TypeType: ...
    def get_IsAbstract(self) -> BooleanType: ...
    def get_IsAssembly(self) -> BooleanType: ...
    def get_IsConstructor(self) -> BooleanType: ...
    def get_IsFamily(self) -> BooleanType: ...
    def get_IsFamilyAndAssembly(self) -> BooleanType: ...
    def get_IsFamilyOrAssembly(self) -> BooleanType: ...
    def get_IsFinal(self) -> BooleanType: ...
    def get_IsHideBySig(self) -> BooleanType: ...
    def get_IsPrivate(self) -> BooleanType: ...
    def get_IsPublic(self) -> BooleanType: ...
    def get_IsSpecialName(self) -> BooleanType: ...
    def get_IsStatic(self) -> BooleanType: ...
    def get_IsVirtual(self) -> BooleanType: ...
    def get_MemberType(self) -> MemberTypes: ...
    def get_MethodHandle(self) -> RuntimeMethodHandle: ...
    def get_Name(self) -> StringType: ...
    def get_ReflectedType(self) -> TypeType: ...

    # No Events

class _MethodBuilder(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...

    # No Events

class _MethodInfo(Protocol):
    # ---------- Properties ---------- #

    @property
    def Attributes(self) -> MethodAttributes: ...
    @property
    def CallingConvention(self) -> CallingConventions: ...
    @property
    def DeclaringType(self) -> TypeType: ...
    @property
    def IsAbstract(self) -> BooleanType: ...
    @property
    def IsAssembly(self) -> BooleanType: ...
    @property
    def IsConstructor(self) -> BooleanType: ...
    @property
    def IsFamily(self) -> BooleanType: ...
    @property
    def IsFamilyAndAssembly(self) -> BooleanType: ...
    @property
    def IsFamilyOrAssembly(self) -> BooleanType: ...
    @property
    def IsFinal(self) -> BooleanType: ...
    @property
    def IsHideBySig(self) -> BooleanType: ...
    @property
    def IsPrivate(self) -> BooleanType: ...
    @property
    def IsPublic(self) -> BooleanType: ...
    @property
    def IsSpecialName(self) -> BooleanType: ...
    @property
    def IsStatic(self) -> BooleanType: ...
    @property
    def IsVirtual(self) -> BooleanType: ...
    @property
    def MemberType(self) -> MemberTypes: ...
    @property
    def MethodHandle(self) -> RuntimeMethodHandle: ...
    @property
    def Name(self) -> StringType: ...
    @property
    def ReflectedType(self) -> TypeType: ...
    @property
    def ReturnType(self) -> TypeType: ...
    @property
    def ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider: ...

    # ---------- Methods ---------- #

    def Equals(self, other: ObjectType) -> BooleanType: ...
    def GetBaseDefinition(self) -> MethodInfo: ...
    @overload
    def GetCustomAttributes(
        self, attributeType: TypeType, inherit: BooleanType
    ) -> ArrayType[ObjectType]: ...
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    def GetHashCode(self) -> IntType: ...
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetMethodImplementationFlags(self) -> MethodImplAttributes: ...
    def GetParameters(self) -> ArrayType[ParameterInfo]: ...
    def GetType(self) -> TypeType: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    @overload
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...
    @overload
    def Invoke(
        self,
        obj: ObjectType,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: ArrayType[ObjectType],
        culture: CultureInfo,
    ) -> ObjectType: ...
    @overload
    def Invoke(self, obj: ObjectType, parameters: ArrayType[ObjectType]) -> ObjectType: ...
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    def ToString(self) -> StringType: ...
    def get_Attributes(self) -> MethodAttributes: ...
    def get_CallingConvention(self) -> CallingConventions: ...
    def get_DeclaringType(self) -> TypeType: ...
    def get_IsAbstract(self) -> BooleanType: ...
    def get_IsAssembly(self) -> BooleanType: ...
    def get_IsConstructor(self) -> BooleanType: ...
    def get_IsFamily(self) -> BooleanType: ...
    def get_IsFamilyAndAssembly(self) -> BooleanType: ...
    def get_IsFamilyOrAssembly(self) -> BooleanType: ...
    def get_IsFinal(self) -> BooleanType: ...
    def get_IsHideBySig(self) -> BooleanType: ...
    def get_IsPrivate(self) -> BooleanType: ...
    def get_IsPublic(self) -> BooleanType: ...
    def get_IsSpecialName(self) -> BooleanType: ...
    def get_IsStatic(self) -> BooleanType: ...
    def get_IsVirtual(self) -> BooleanType: ...
    def get_MemberType(self) -> MemberTypes: ...
    def get_MethodHandle(self) -> RuntimeMethodHandle: ...
    def get_Name(self) -> StringType: ...
    def get_ReflectedType(self) -> TypeType: ...
    def get_ReturnType(self) -> TypeType: ...
    def get_ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider: ...

    # No Events

class _MethodRental(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...

    # No Events

class _Module(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...

    # No Events

class _ModuleBuilder(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...

    # No Events

class _ParameterBuilder(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...

    # No Events

class _ParameterInfo(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...

    # No Events

class _PropertyBuilder(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...

    # No Events

class _PropertyInfo(Protocol):
    # ---------- Properties ---------- #

    @property
    def Attributes(self) -> PropertyAttributes: ...
    @property
    def CanRead(self) -> BooleanType: ...
    @property
    def CanWrite(self) -> BooleanType: ...
    @property
    def DeclaringType(self) -> TypeType: ...
    @property
    def IsSpecialName(self) -> BooleanType: ...
    @property
    def MemberType(self) -> MemberTypes: ...
    @property
    def Name(self) -> StringType: ...
    @property
    def PropertyType(self) -> TypeType: ...
    @property
    def ReflectedType(self) -> TypeType: ...

    # ---------- Methods ---------- #

    def Equals(self, other: ObjectType) -> BooleanType: ...
    @overload
    def GetAccessors(self, nonPublic: BooleanType) -> ArrayType[MethodInfo]: ...
    @overload
    def GetAccessors(self) -> ArrayType[MethodInfo]: ...
    @overload
    def GetCustomAttributes(
        self, attributeType: TypeType, inherit: BooleanType
    ) -> ArrayType[ObjectType]: ...
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    @overload
    def GetGetMethod(self, nonPublic: BooleanType) -> MethodInfo: ...
    @overload
    def GetGetMethod(self) -> MethodInfo: ...
    def GetHashCode(self) -> IntType: ...
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetIndexParameters(self) -> ArrayType[ParameterInfo]: ...
    @overload
    def GetSetMethod(self, nonPublic: BooleanType) -> MethodInfo: ...
    @overload
    def GetSetMethod(self) -> MethodInfo: ...
    def GetType(self) -> TypeType: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    @overload
    def GetValue(self, obj: ObjectType, index: ArrayType[ObjectType]) -> ObjectType: ...
    @overload
    def GetValue(
        self,
        obj: ObjectType,
        invokeAttr: BindingFlags,
        binder: Binder,
        index: ArrayType[ObjectType],
        culture: CultureInfo,
    ) -> ObjectType: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    @overload
    def SetValue(
        self, obj: ObjectType, value: ObjectType, index: ArrayType[ObjectType]
    ) -> VoidType: ...
    @overload
    def SetValue(
        self,
        obj: ObjectType,
        value: ObjectType,
        invokeAttr: BindingFlags,
        binder: Binder,
        index: ArrayType[ObjectType],
        culture: CultureInfo,
    ) -> VoidType: ...
    def ToString(self) -> StringType: ...
    def get_Attributes(self) -> PropertyAttributes: ...
    def get_CanRead(self) -> BooleanType: ...
    def get_CanWrite(self) -> BooleanType: ...
    def get_DeclaringType(self) -> TypeType: ...
    def get_IsSpecialName(self) -> BooleanType: ...
    def get_MemberType(self) -> MemberTypes: ...
    def get_Name(self) -> StringType: ...
    def get_PropertyType(self) -> TypeType: ...
    def get_ReflectedType(self) -> TypeType: ...

    # No Events

class _SignatureHelper(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...

    # No Events

class _Thread(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...

    # No Events

class _Type(Protocol):
    # ---------- Properties ---------- #

    @property
    def Assembly(self) -> Assembly: ...
    @property
    def AssemblyQualifiedName(self) -> StringType: ...
    @property
    def Attributes(self) -> TypeAttributes: ...
    @property
    def BaseType(self) -> TypeType: ...
    @property
    def DeclaringType(self) -> TypeType: ...
    @property
    def FullName(self) -> StringType: ...
    @property
    def GUID(self) -> Guid: ...
    @property
    def HasElementType(self) -> BooleanType: ...
    @property
    def IsAbstract(self) -> BooleanType: ...
    @property
    def IsAnsiClass(self) -> BooleanType: ...
    @property
    def IsArray(self) -> BooleanType: ...
    @property
    def IsAutoClass(self) -> BooleanType: ...
    @property
    def IsAutoLayout(self) -> BooleanType: ...
    @property
    def IsByRef(self) -> BooleanType: ...
    @property
    def IsCOMObject(self) -> BooleanType: ...
    @property
    def IsClass(self) -> BooleanType: ...
    @property
    def IsContextful(self) -> BooleanType: ...
    @property
    def IsEnum(self) -> BooleanType: ...
    @property
    def IsExplicitLayout(self) -> BooleanType: ...
    @property
    def IsImport(self) -> BooleanType: ...
    @property
    def IsInterface(self) -> BooleanType: ...
    @property
    def IsLayoutSequential(self) -> BooleanType: ...
    @property
    def IsMarshalByRef(self) -> BooleanType: ...
    @property
    def IsNestedAssembly(self) -> BooleanType: ...
    @property
    def IsNestedFamANDAssem(self) -> BooleanType: ...
    @property
    def IsNestedFamORAssem(self) -> BooleanType: ...
    @property
    def IsNestedFamily(self) -> BooleanType: ...
    @property
    def IsNestedPrivate(self) -> BooleanType: ...
    @property
    def IsNestedPublic(self) -> BooleanType: ...
    @property
    def IsNotPublic(self) -> BooleanType: ...
    @property
    def IsPointer(self) -> BooleanType: ...
    @property
    def IsPrimitive(self) -> BooleanType: ...
    @property
    def IsPublic(self) -> BooleanType: ...
    @property
    def IsSealed(self) -> BooleanType: ...
    @property
    def IsSerializable(self) -> BooleanType: ...
    @property
    def IsSpecialName(self) -> BooleanType: ...
    @property
    def IsUnicodeClass(self) -> BooleanType: ...
    @property
    def IsValueType(self) -> BooleanType: ...
    @property
    def MemberType(self) -> MemberTypes: ...
    @property
    def Module(self) -> Module: ...
    @property
    def Name(self) -> StringType: ...
    @property
    def Namespace(self) -> StringType: ...
    @property
    def ReflectedType(self) -> TypeType: ...
    @property
    def TypeHandle(self) -> RuntimeTypeHandle: ...
    @property
    def TypeInitializer(self) -> ConstructorInfo: ...
    @property
    def UnderlyingSystemType(self) -> TypeType: ...

    # ---------- Methods ---------- #

    @overload
    def Equals(self, other: ObjectType) -> BooleanType: ...
    @overload
    def Equals(self, o: TypeType) -> BooleanType: ...
    def FindInterfaces(
        self, filter: TypeFilter, filterCriteria: ObjectType
    ) -> ArrayType[TypeType]: ...
    def FindMembers(
        self,
        memberType: MemberTypes,
        bindingAttr: BindingFlags,
        filter: MemberFilter,
        filterCriteria: ObjectType,
    ) -> ArrayType[MemberInfo]: ...
    def GetArrayRank(self) -> IntType: ...
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: ArrayType[TypeType],
        modifiers: ArrayType[ParameterModifier],
    ) -> ConstructorInfo: ...
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: ArrayType[TypeType],
        modifiers: ArrayType[ParameterModifier],
    ) -> ConstructorInfo: ...
    @overload
    def GetConstructor(self, types: ArrayType[TypeType]) -> ConstructorInfo: ...
    @overload
    def GetConstructors(self, bindingAttr: BindingFlags) -> ArrayType[ConstructorInfo]: ...
    @overload
    def GetConstructors(self) -> ArrayType[ConstructorInfo]: ...
    @overload
    def GetCustomAttributes(
        self, attributeType: TypeType, inherit: BooleanType
    ) -> ArrayType[ObjectType]: ...
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    def GetDefaultMembers(self) -> ArrayType[MemberInfo]: ...
    def GetElementType(self) -> TypeType: ...
    @overload
    def GetEvent(self, name: StringType, bindingAttr: BindingFlags) -> EventInfo: ...
    @overload
    def GetEvent(self, name: StringType) -> EventInfo: ...
    @overload
    def GetEvents(self) -> ArrayType[EventInfo]: ...
    @overload
    def GetEvents(self, bindingAttr: BindingFlags) -> ArrayType[EventInfo]: ...
    @overload
    def GetField(self, name: StringType, bindingAttr: BindingFlags) -> FieldInfo: ...
    @overload
    def GetField(self, name: StringType) -> FieldInfo: ...
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> ArrayType[FieldInfo]: ...
    @overload
    def GetFields(self) -> ArrayType[FieldInfo]: ...
    def GetHashCode(self) -> IntType: ...
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    @overload
    def GetInterface(self, name: StringType, ignoreCase: BooleanType) -> TypeType: ...
    @overload
    def GetInterface(self, name: StringType) -> TypeType: ...
    def GetInterfaceMap(self, interfaceType: TypeType) -> InterfaceMapping: ...
    def GetInterfaces(self) -> ArrayType[TypeType]: ...
    @overload
    def GetMember(
        self, name: StringType, type: MemberTypes, bindingAttr: BindingFlags
    ) -> ArrayType[MemberInfo]: ...
    @overload
    def GetMember(self, name: StringType, bindingAttr: BindingFlags) -> ArrayType[MemberInfo]: ...
    @overload
    def GetMember(self, name: StringType) -> ArrayType[MemberInfo]: ...
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> ArrayType[MemberInfo]: ...
    @overload
    def GetMembers(self) -> ArrayType[MemberInfo]: ...
    @overload
    def GetMethod(
        self,
        name: StringType,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: ArrayType[TypeType],
        modifiers: ArrayType[ParameterModifier],
    ) -> MethodInfo: ...
    @overload
    def GetMethod(self, name: StringType, bindingAttr: BindingFlags) -> MethodInfo: ...
    @overload
    def GetMethod(
        self,
        name: StringType,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: ArrayType[TypeType],
        modifiers: ArrayType[ParameterModifier],
    ) -> MethodInfo: ...
    @overload
    def GetMethod(
        self, name: StringType, types: ArrayType[TypeType], modifiers: ArrayType[ParameterModifier]
    ) -> MethodInfo: ...
    @overload
    def GetMethod(self, name: StringType, types: ArrayType[TypeType]) -> MethodInfo: ...
    @overload
    def GetMethod(self, name: StringType) -> MethodInfo: ...
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> ArrayType[MethodInfo]: ...
    @overload
    def GetMethods(self) -> ArrayType[MethodInfo]: ...
    @overload
    def GetNestedType(self, name: StringType, bindingAttr: BindingFlags) -> TypeType: ...
    @overload
    def GetNestedType(self, name: StringType) -> TypeType: ...
    @overload
    def GetNestedTypes(self, bindingAttr: BindingFlags) -> ArrayType[TypeType]: ...
    @overload
    def GetNestedTypes(self) -> ArrayType[TypeType]: ...
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> ArrayType[PropertyInfo]: ...
    @overload
    def GetProperties(self) -> ArrayType[PropertyInfo]: ...
    @overload
    def GetProperty(self, name: StringType, bindingAttr: BindingFlags) -> PropertyInfo: ...
    @overload
    def GetProperty(
        self,
        name: StringType,
        bindingAttr: BindingFlags,
        binder: Binder,
        returnType: TypeType,
        types: ArrayType[TypeType],
        modifiers: ArrayType[ParameterModifier],
    ) -> PropertyInfo: ...
    @overload
    def GetProperty(
        self,
        name: StringType,
        returnType: TypeType,
        types: ArrayType[TypeType],
        modifiers: ArrayType[ParameterModifier],
    ) -> PropertyInfo: ...
    @overload
    def GetProperty(
        self, name: StringType, returnType: TypeType, types: ArrayType[TypeType]
    ) -> PropertyInfo: ...
    @overload
    def GetProperty(self, name: StringType, types: ArrayType[TypeType]) -> PropertyInfo: ...
    @overload
    def GetProperty(self, name: StringType, returnType: TypeType) -> PropertyInfo: ...
    @overload
    def GetProperty(self, name: StringType) -> PropertyInfo: ...
    def GetType(self) -> TypeType: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...
    @overload
    def InvokeMember(
        self,
        name: StringType,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: ObjectType,
        args: ArrayType[ObjectType],
        modifiers: ArrayType[ParameterModifier],
        culture: CultureInfo,
        namedParameters: ArrayType[StringType],
    ) -> ObjectType: ...
    @overload
    def InvokeMember(
        self,
        name: StringType,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: ObjectType,
        args: ArrayType[ObjectType],
        culture: CultureInfo,
    ) -> ObjectType: ...
    @overload
    def InvokeMember(
        self,
        name: StringType,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: ObjectType,
        args: ArrayType[ObjectType],
    ) -> ObjectType: ...
    def IsAssignableFrom(self, c: TypeType) -> BooleanType: ...
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    def IsInstanceOfType(self, o: ObjectType) -> BooleanType: ...
    def IsSubclassOf(self, c: TypeType) -> BooleanType: ...
    def ToString(self) -> StringType: ...
    def get_Assembly(self) -> Assembly: ...
    def get_AssemblyQualifiedName(self) -> StringType: ...
    def get_Attributes(self) -> TypeAttributes: ...
    def get_BaseType(self) -> TypeType: ...
    def get_DeclaringType(self) -> TypeType: ...
    def get_FullName(self) -> StringType: ...
    def get_GUID(self) -> Guid: ...
    def get_HasElementType(self) -> BooleanType: ...
    def get_IsAbstract(self) -> BooleanType: ...
    def get_IsAnsiClass(self) -> BooleanType: ...
    def get_IsArray(self) -> BooleanType: ...
    def get_IsAutoClass(self) -> BooleanType: ...
    def get_IsAutoLayout(self) -> BooleanType: ...
    def get_IsByRef(self) -> BooleanType: ...
    def get_IsCOMObject(self) -> BooleanType: ...
    def get_IsClass(self) -> BooleanType: ...
    def get_IsContextful(self) -> BooleanType: ...
    def get_IsEnum(self) -> BooleanType: ...
    def get_IsExplicitLayout(self) -> BooleanType: ...
    def get_IsImport(self) -> BooleanType: ...
    def get_IsInterface(self) -> BooleanType: ...
    def get_IsLayoutSequential(self) -> BooleanType: ...
    def get_IsMarshalByRef(self) -> BooleanType: ...
    def get_IsNestedAssembly(self) -> BooleanType: ...
    def get_IsNestedFamANDAssem(self) -> BooleanType: ...
    def get_IsNestedFamORAssem(self) -> BooleanType: ...
    def get_IsNestedFamily(self) -> BooleanType: ...
    def get_IsNestedPrivate(self) -> BooleanType: ...
    def get_IsNestedPublic(self) -> BooleanType: ...
    def get_IsNotPublic(self) -> BooleanType: ...
    def get_IsPointer(self) -> BooleanType: ...
    def get_IsPrimitive(self) -> BooleanType: ...
    def get_IsPublic(self) -> BooleanType: ...
    def get_IsSealed(self) -> BooleanType: ...
    def get_IsSerializable(self) -> BooleanType: ...
    def get_IsSpecialName(self) -> BooleanType: ...
    def get_IsUnicodeClass(self) -> BooleanType: ...
    def get_IsValueType(self) -> BooleanType: ...
    def get_MemberType(self) -> MemberTypes: ...
    def get_Module(self) -> Module: ...
    def get_Name(self) -> StringType: ...
    def get_Namespace(self) -> StringType: ...
    def get_ReflectedType(self) -> TypeType: ...
    def get_TypeHandle(self) -> RuntimeTypeHandle: ...
    def get_TypeInitializer(self) -> ConstructorInfo: ...
    def get_UnderlyingSystemType(self) -> TypeType: ...

    # No Events

class _TypeBuilder(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetIDsOfNames(
        self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType
    ) -> Tuple[VoidType, Guid]: ...
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    def Invoke(
        self,
        dispIdMember: UIntType,
        riid: Guid,
        lcid: UIntType,
        wFlags: ShortType,
        pDispParams: NIntType,
        pVarResult: NIntType,
        pExcepInfo: NIntType,
        puArgErr: NIntType,
    ) -> Tuple[VoidType, Guid]: ...

    # No Events

# ---------- Enums ---------- #

class Architecture(Enum):
    X86 = 0
    X64 = 1
    Arm = 2
    Arm64 = 3

class AssemblyRegistrationFlags(Enum):
    # None = 0
    SetCodeBase = 1

class CALLCONV(Enum):
    CC_CDECL = 1
    CC_MSCPASCAL = 2
    CC_PASCAL = 2
    CC_MACPASCAL = 3
    CC_STDCALL = 4
    CC_RESERVED = 5
    CC_SYSCALL = 6
    CC_MPWCDECL = 7
    CC_MPWPASCAL = 8
    CC_MAX = 9

class CallingConvention(Enum):
    Winapi = 1
    Cdecl = 2
    StdCall = 3
    ThisCall = 4
    FastCall = 5

class CharSet(Enum):
    # None = 1
    Ansi = 2
    Unicode = 3
    Auto = 4

class ClassInterfaceType(Enum):
    # None = 0
    AutoDispatch = 1
    AutoDual = 2

class ComInterfaceType(Enum):
    InterfaceIsDual = 0
    InterfaceIsIUnknown = 1
    InterfaceIsIDispatch = 2
    InterfaceIsIInspectable = 3

class ComMemberType(Enum):
    Method = 0
    PropGet = 1
    PropSet = 2

class CustomQueryInterfaceMode(Enum):
    Ignore = 0
    Allow = 1

class CustomQueryInterfaceResult(Enum):
    Handled = 0
    NotHandled = 1
    Failed = 2

class DESCKIND(Enum):
    DESCKIND_NONE = 0
    DESCKIND_FUNCDESC = 1
    DESCKIND_VARDESC = 2
    DESCKIND_TYPECOMP = 3
    DESCKIND_IMPLICITAPPOBJ = 4
    DESCKIND_MAX = 5

class DllImportSearchPath(Enum):
    LegacyBehavior = 0
    AssemblyDirectory = 2
    UseDllDirectoryForDependencies = 256
    ApplicationDirectory = 512
    UserDirectories = 1024
    System32 = 2048
    SafeDirectories = 4096

class ExporterEventKind(Enum):
    NOTIF_TYPECONVERTED = 0
    NOTIF_CONVERTWARNING = 1
    ERROR_REFTOINVALIDASSEMBLY = 2

class FUNCFLAGS(Enum):
    FUNCFLAG_FRESTRICTED = 1
    FUNCFLAG_FSOURCE = 2
    FUNCFLAG_FBINDABLE = 4
    FUNCFLAG_FREQUESTEDIT = 8
    FUNCFLAG_FDISPLAYBIND = 16
    FUNCFLAG_FDEFAULTBIND = 32
    FUNCFLAG_FHIDDEN = 64
    FUNCFLAG_FUSESGETLASTERROR = 128
    FUNCFLAG_FDEFAULTCOLLELEM = 256
    FUNCFLAG_FUIDEFAULT = 512
    FUNCFLAG_FNONBROWSABLE = 1024
    FUNCFLAG_FREPLACEABLE = 2048
    FUNCFLAG_FIMMEDIATEBIND = 4096

class FUNCKIND(Enum):
    FUNC_VIRTUAL = 0
    FUNC_PUREVIRTUAL = 1
    FUNC_NONVIRTUAL = 2
    FUNC_STATIC = 3
    FUNC_DISPATCH = 4

class GCHandleType(Enum):
    Weak = 0
    WeakTrackResurrection = 1
    Normal = 2
    Pinned = 3

class IDLFLAG(Enum):
    IDLFLAG_NONE = 0
    IDLFLAG_FIN = 1
    IDLFLAG_FOUT = 2
    IDLFLAG_FLCID = 4
    IDLFLAG_FRETVAL = 8

class IDispatchImplType(Enum):
    SystemDefinedImpl = 0
    InternalImpl = 1
    CompatibleImpl = 2

class IMPLTYPEFLAGS(Enum):
    IMPLTYPEFLAG_FDEFAULT = 1
    IMPLTYPEFLAG_FSOURCE = 2
    IMPLTYPEFLAG_FRESTRICTED = 4
    IMPLTYPEFLAG_FDEFAULTVTABLE = 8

class INVOKEKIND(Enum):
    INVOKE_FUNC = 1
    INVOKE_PROPERTYGET = 2
    INVOKE_PROPERTYPUT = 4
    INVOKE_PROPERTYPUTREF = 8

class ImporterEventKind(Enum):
    NOTIF_TYPECONVERTED = 0
    NOTIF_CONVERTWARNING = 1
    ERROR_REFTOINVALIDTYPELIB = 2

class LIBFLAGS(Enum):
    LIBFLAG_FRESTRICTED = 1
    LIBFLAG_FCONTROL = 2
    LIBFLAG_FHIDDEN = 4
    LIBFLAG_FHASDISKIMAGE = 8

class LayoutKind(Enum):
    Sequential = 0
    Explicit = 2
    Auto = 3

class PARAMFLAG(Enum):
    PARAMFLAG_NONE = 0
    PARAMFLAG_FIN = 1
    PARAMFLAG_FOUT = 2
    PARAMFLAG_FLCID = 4
    PARAMFLAG_FRETVAL = 8
    PARAMFLAG_FOPT = 16
    PARAMFLAG_FHASDEFAULT = 32
    PARAMFLAG_FHASCUSTDATA = 64

class PInvokeMap(Enum):
    CharSetNotSpec = 0
    NoMangle = 1
    CharSetAnsi = 2
    CharSetUnicode = 4
    CharSetAuto = 6
    CharSetMask = 6
    BestFitEnabled = 16
    BestFitDisabled = 32
    PinvokeOLE = 32
    BestFitMask = 48
    BestFitUseAsm = 48
    SupportsLastError = 64
    CallConvWinapi = 256
    CallConvCdecl = 512
    CallConvStdcall = 768
    CallConvThiscall = 1024
    CallConvFastcall = 1280
    CallConvMask = 1792
    ThrowOnUnmappableCharEnabled = 4096
    ThrowOnUnmappableCharDisabled = 8192
    ThrowOnUnmappableCharMask = 12288
    ThrowOnUnmappableCharUseAsm = 12288

class RegistrationClassContext(Enum):
    InProcessServer = 1
    InProcessHandler = 2
    LocalServer = 4
    InProcessServer16 = 8
    RemoteServer = 16
    InProcessHandler16 = 32
    Reserved1 = 64
    Reserved2 = 128
    Reserved3 = 256
    Reserved4 = 512
    NoCodeDownload = 1024
    Reserved5 = 2048
    NoCustomMarshal = 4096
    EnableCodeDownload = 8192
    NoFailureLog = 16384
    DisableActivateAsActivator = 32768
    EnableActivateAsActivator = 65536
    FromDefaultContext = 131072

class RegistrationConnectionType(Enum):
    SingleUse = 0
    MultipleUse = 1
    MultiSeparate = 2
    Suspended = 4
    Surrogate = 8

class SYSKIND(Enum):
    SYS_WIN16 = 0
    SYS_WIN32 = 1
    SYS_MAC = 2

class TYPEFLAGS(Enum):
    TYPEFLAG_FAPPOBJECT = 1
    TYPEFLAG_FCANCREATE = 2
    TYPEFLAG_FLICENSED = 4
    TYPEFLAG_FPREDECLID = 8
    TYPEFLAG_FHIDDEN = 16
    TYPEFLAG_FCONTROL = 32
    TYPEFLAG_FDUAL = 64
    TYPEFLAG_FNONEXTENSIBLE = 128
    TYPEFLAG_FOLEAUTOMATION = 256
    TYPEFLAG_FRESTRICTED = 512
    TYPEFLAG_FAGGREGATABLE = 1024
    TYPEFLAG_FREPLACEABLE = 2048
    TYPEFLAG_FDISPATCHABLE = 4096
    TYPEFLAG_FREVERSEBIND = 8192
    TYPEFLAG_FPROXY = 16384

class TYPEKIND(Enum):
    TKIND_ENUM = 0
    TKIND_RECORD = 1
    TKIND_MODULE = 2
    TKIND_INTERFACE = 3
    TKIND_DISPATCH = 4
    TKIND_COCLASS = 5
    TKIND_ALIAS = 6
    TKIND_UNION = 7
    TKIND_MAX = 8

class TypeLibExporterFlags(Enum):
    # None = 0
    OnlyReferenceRegistered = 1
    CallerResolvedReferences = 2
    OldNames = 4
    ExportAs32Bit = 16
    ExportAs64Bit = 32

class TypeLibFuncFlags(Enum):
    FRestricted = 1
    FSource = 2
    FBindable = 4
    FRequestEdit = 8
    FDisplayBind = 16
    FDefaultBind = 32
    FHidden = 64
    FUsesGetLastError = 128
    FDefaultCollelem = 256
    FUiDefault = 512
    FNonBrowsable = 1024
    FReplaceable = 2048
    FImmediateBind = 4096

class TypeLibImporterFlags(Enum):
    # None = 0
    PrimaryInteropAssembly = 1
    UnsafeInterfaces = 2
    SafeArrayAsSystemArray = 4
    TransformDispRetVals = 8
    PreventClassMembers = 16
    SerializableValueClasses = 32
    ImportAsX86 = 256
    ImportAsX64 = 512
    ImportAsItanium = 1024
    ImportAsAgnostic = 2048
    ReflectionOnlyLoading = 4096
    NoDefineVersionResource = 8192
    ImportAsArm = 16384

class TypeLibTypeFlags(Enum):
    FAppObject = 1
    FCanCreate = 2
    FLicensed = 4
    FPreDeclId = 8
    FHidden = 16
    FControl = 32
    FDual = 64
    FNonExtensible = 128
    FOleAutomation = 256
    FRestricted = 512
    FAggregatable = 1024
    FReplaceable = 2048
    FDispatchable = 4096
    FReverseBind = 8192

class TypeLibVarFlags(Enum):
    FReadOnly = 1
    FSource = 2
    FBindable = 4
    FRequestEdit = 8
    FDisplayBind = 16
    FDefaultBind = 32
    FHidden = 64
    FRestricted = 128
    FDefaultCollelem = 256
    FUiDefault = 512
    FNonBrowsable = 1024
    FReplaceable = 2048
    FImmediateBind = 4096

class UnmanagedType(Enum):
    Bool = 2
    I1 = 3
    U1 = 4
    I2 = 5
    U2 = 6
    I4 = 7
    U4 = 8
    I8 = 9
    U8 = 10
    R4 = 11
    R8 = 12
    Currency = 15
    BStr = 19
    LPStr = 20
    LPWStr = 21
    LPTStr = 22
    ByValTStr = 23
    IUnknown = 25
    IDispatch = 26
    Struct = 27
    Interface = 28
    SafeArray = 29
    ByValArray = 30
    SysInt = 31
    SysUInt = 32
    VBByRefStr = 34
    AnsiBStr = 35
    TBStr = 36
    VariantBool = 37
    FunctionPtr = 38
    AsAny = 40
    LPArray = 42
    LPStruct = 43
    CustomMarshaler = 44
    Error = 45
    IInspectable = 46
    HString = 47
    LPUTF8Str = 48

class VARFLAGS(Enum):
    VARFLAG_FREADONLY = 1
    VARFLAG_FSOURCE = 2
    VARFLAG_FBINDABLE = 4
    VARFLAG_FREQUESTEDIT = 8
    VARFLAG_FDISPLAYBIND = 16
    VARFLAG_FDEFAULTBIND = 32
    VARFLAG_FHIDDEN = 64
    VARFLAG_FRESTRICTED = 128
    VARFLAG_FDEFAULTCOLLELEM = 256
    VARFLAG_FUIDEFAULT = 512
    VARFLAG_FNONBROWSABLE = 1024
    VARFLAG_FREPLACEABLE = 2048
    VARFLAG_FIMMEDIATEBIND = 4096

class VarEnum(Enum):
    VT_EMPTY = 0
    VT_NULL = 1
    VT_I2 = 2
    VT_I4 = 3
    VT_R4 = 4
    VT_R8 = 5
    VT_CY = 6
    VT_DATE = 7
    VT_BSTR = 8
    VT_DISPATCH = 9
    VT_ERROR = 10
    VT_BOOL = 11
    VT_VARIANT = 12
    VT_UNKNOWN = 13
    VT_DECIMAL = 14
    VT_I1 = 16
    VT_UI1 = 17
    VT_UI2 = 18
    VT_UI4 = 19
    VT_I8 = 20
    VT_UI8 = 21
    VT_INT = 22
    VT_UINT = 23
    VT_VOID = 24
    VT_HRESULT = 25
    VT_PTR = 26
    VT_SAFEARRAY = 27
    VT_CARRAY = 28
    VT_USERDEFINED = 29
    VT_LPSTR = 30
    VT_LPWSTR = 31
    VT_RECORD = 36
    VT_FILETIME = 64
    VT_BLOB = 65
    VT_STREAM = 66
    VT_STORAGE = 67
    VT_STREAMED_OBJECT = 68
    VT_STORED_OBJECT = 69
    VT_BLOB_OBJECT = 70
    VT_CF = 71
    VT_CLSID = 72
    VT_VECTOR = 4096
    VT_ARRAY = 8192
    VT_BYREF = 16384

# ---------- Delegates ---------- #

ObjectCreationDelegate = Callable[[NIntType], NIntType]

__all__ = [
    AllowReversePInvokeCallsAttribute,
    AutomationProxyAttribute,
    BStrWrapper,
    BestFitMappingAttribute,
    COMException,
    ClassInterfaceAttribute,
    CoClassAttribute,
    ComAliasNameAttribute,
    ComAwareEventInfo,
    ComCompatibleVersionAttribute,
    ComConversionLossAttribute,
    ComDefaultInterfaceAttribute,
    ComEventInterfaceAttribute,
    ComEventsHelper,
    ComEventsInfo,
    ComEventsMethod,
    ComEventsSink,
    ComImportAttribute,
    ComRegisterFunctionAttribute,
    ComSourceInterfacesAttribute,
    ComUnregisterFunctionAttribute,
    ComVisibleAttribute,
    CriticalHandle,
    CurrencyWrapper,
    DefaultCharSetAttribute,
    DefaultDllImportSearchPathsAttribute,
    DefaultParameterValueAttribute,
    DispIdAttribute,
    DispatchWrapper,
    DllImportAttribute,
    ErrorWrapper,
    ExtensibleClassFactory,
    ExternalException,
    FieldOffsetAttribute,
    GCHandleCookieTable,
    GuidAttribute,
    HandleCollector,
    IDispatchImplAttribute,
    ImportedFromTypeLibAttribute,
    ImporterCallback,
    InAttribute,
    InterfaceTypeAttribute,
    InvalidComObjectException,
    InvalidOleVariantTypeException,
    LCIDConversionAttribute,
    ManagedToNativeComInteropStubAttribute,
    Marshal,
    MarshalAsAttribute,
    MarshalDirectiveException,
    NativeBuffer,
    NativeMethods,
    ObjectCreationDelegate,
    OptionalAttribute,
    OutAttribute,
    PreserveSigAttribute,
    PrimaryInteropAssemblyAttribute,
    ProgIdAttribute,
    RegistrationServices,
    RuntimeEnvironment,
    RuntimeInformation,
    SEHException,
    SafeArrayRankMismatchException,
    SafeArrayTypeMismatchException,
    SafeBuffer,
    SafeHandle,
    SafeHeapHandle,
    SafeHeapHandleCache,
    SetWin32ContextInIDispatchAttribute,
    StandardOleMarshalObject,
    StringBuffer,
    StructLayoutAttribute,
    TypeIdentifierAttribute,
    TypeLibConverter,
    TypeLibFuncAttribute,
    TypeLibImportClassAttribute,
    TypeLibTypeAttribute,
    TypeLibVarAttribute,
    TypeLibVersionAttribute,
    UnknownWrapper,
    UnmanagedFunctionPointerAttribute,
    VariantWrapper,
    ArrayWithOffset,
    BINDPTR,
    BIND_OPTS,
    CONNECTDATA,
    DISPPARAMS,
    ELEMDESC,
    EXCEPINFO,
    FILETIME,
    FUNCDESC,
    GCHandle,
    HandleRef,
    IDLDESC,
    OSPlatform,
    PARAMDESC,
    STATSTG,
    TYPEATTR,
    TYPEDESC,
    TYPELIBATTR,
    VARDESC,
    Variant,
    ICustomAdapter,
    ICustomFactory,
    ICustomMarshaler,
    ICustomQueryInterface,
    IRegistrationServices,
    ITypeLibConverter,
    ITypeLibExporterNameProvider,
    ITypeLibExporterNotifySink,
    ITypeLibImporterNotifySink,
    UCOMIBindCtx,
    UCOMIConnectionPoint,
    UCOMIConnectionPointContainer,
    UCOMIEnumConnectionPoints,
    UCOMIEnumConnections,
    UCOMIEnumMoniker,
    UCOMIEnumString,
    UCOMIEnumVARIANT,
    UCOMIEnumerable,
    UCOMIEnumerator,
    UCOMIExpando,
    UCOMIMoniker,
    UCOMIPersistFile,
    UCOMIReflect,
    UCOMIRunningObjectTable,
    UCOMIStream,
    UCOMITypeComp,
    UCOMITypeInfo,
    UCOMITypeLib,
    _Activator,
    _Assembly,
    _AssemblyBuilder,
    _AssemblyName,
    _Attribute,
    _ConstructorBuilder,
    _ConstructorInfo,
    _CustomAttributeBuilder,
    _EnumBuilder,
    _EventBuilder,
    _EventInfo,
    _Exception,
    _FieldBuilder,
    _FieldInfo,
    _ILGenerator,
    _LocalBuilder,
    _MemberInfo,
    _MethodBase,
    _MethodBuilder,
    _MethodInfo,
    _MethodRental,
    _Module,
    _ModuleBuilder,
    _ParameterBuilder,
    _ParameterInfo,
    _PropertyBuilder,
    _PropertyInfo,
    _SignatureHelper,
    _Thread,
    _Type,
    _TypeBuilder,
    Architecture,
    AssemblyRegistrationFlags,
    CALLCONV,
    CallingConvention,
    CharSet,
    ClassInterfaceType,
    ComInterfaceType,
    ComMemberType,
    CustomQueryInterfaceMode,
    CustomQueryInterfaceResult,
    DESCKIND,
    DllImportSearchPath,
    ExporterEventKind,
    FUNCFLAGS,
    FUNCKIND,
    GCHandleType,
    IDLFLAG,
    IDispatchImplType,
    IMPLTYPEFLAGS,
    INVOKEKIND,
    ImporterEventKind,
    LIBFLAGS,
    LayoutKind,
    PARAMFLAG,
    PInvokeMap,
    RegistrationClassContext,
    RegistrationConnectionType,
    SYSKIND,
    TYPEFLAGS,
    TYPEKIND,
    TypeLibExporterFlags,
    TypeLibFuncFlags,
    TypeLibImporterFlags,
    TypeLibTypeFlags,
    TypeLibVarFlags,
    UnmanagedType,
    VARFLAGS,
    VarEnum,
    ObjectCreationDelegate,
]
