from __future__ import annotations

from abc import ABC
from typing import Callable, Generic, List, Optional, Protocol, Tuple, TypeVar, Union, overload

from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from System.Collections import ICollection, IComparer, IDictionary, IEnumerable, IEnumerator, IEqualityComparer, IList, IStructuralComparable, IStructuralEquatable
from System.Collections.Generic import ICollection, IComparer, IEnumerable, IEnumerator, IEqualityComparer, IList, IReadOnlyCollection, IReadOnlyList
from System.Collections.ObjectModel import ReadOnlyCollection
from System.ComponentModel import CategoryAttribute, DescriptionAttribute, ITypeDescriptorContext, TypeConverter
from System.Configuration.Assemblies import AssemblyHashAlgorithm
from System.Diagnostics.Tracing import EventSource
from System.Globalization import Calendar, CompareOptions, CultureInfo, DateTimeStyles, DaylightTime, NumberFormatInfo, NumberStyles, TimeSpanStyles, UnicodeCategory
from System.IO import Stream, TextReader, TextWriter
from System.Reflection import Assembly, AssemblyName, Binder, BindingFlags, CallingConventions, ConstructorInfo, CustomAttributeData, EventInfo, FieldInfo, GenericParameterAttributes, ICustomAttributeProvider, IReflect, IReflectableType, InterfaceMapping, MemberFilter, MemberInfo, MemberTypes, MethodBase, MethodInfo, Module, ParameterInfo, ParameterModifier, PropertyInfo, TypeAttributes, TypeFilter, TypeInfo
from System.Reflection.Emit import AssemblyBuilder, AssemblyBuilderAccess, CustomAttributeBuilder
from System.Resources import ResourceManager
from System.Runtime.CompilerServices import ITuple
from System.Runtime.ConstrainedExecution import CriticalFinalizerObject
from System.Runtime.ExceptionServices import FirstChanceExceptionEventArgs
from System.Runtime.Hosting import ActivationArguments, ApplicationActivator
from System.Runtime.InteropServices import StructLayoutAttribute, _Activator, _Attribute, _Exception, _MemberInfo, _Type
from System.Runtime.Remoting import ObjRef, ObjectHandle
from System.Runtime.Serialization import IDeserializationCallback, IObjectReference, ISerializable, SerializationInfo, StreamingContext
from System.Security import HostSecurityManager, IEvidenceFactory, IPermission, PermissionSet, SecurityContextSource, SecurityState
from System.Security.Policy import ApplicationTrust, Evidence, PolicyLevel, StrongName
from System.Security.Principal import IPrincipal, PrincipalPolicy
from System.Security.Util import Tokenizer
from System.Text import Encoding, NormalizationForm, StringBuilder
from System.Threading import CancellationToken, HostExecutionContextManager, LazyThreadSafetyMode, WaitHandle

# ---------- Types ---------- #

T = TypeVar('T')
T1 = TypeVar('T1')
T10 = TypeVar('T10')
T11 = TypeVar('T11')
T12 = TypeVar('T12')
T13 = TypeVar('T13')
T14 = TypeVar('T14')
T15 = TypeVar('T15')
T16 = TypeVar('T16')
T17 = TypeVar('T17')
T18 = TypeVar('T18')
T19 = TypeVar('T19')
T2 = TypeVar('T2')
T20 = TypeVar('T20')
T21 = TypeVar('T21')
T3 = TypeVar('T3')
T4 = TypeVar('T4')
T5 = TypeVar('T5')
T6 = TypeVar('T6')
T7 = TypeVar('T7')
T8 = TypeVar('T8')
T9 = TypeVar('T9')
TEventArgs = TypeVar('TEventArgs')
TInput = TypeVar('TInput')
TKey = TypeVar('TKey')
TOutput = TypeVar('TOutput')
TRest = TypeVar('TRest')
TResult = TypeVar('TResult')

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
NUIntType = Union[int, UIntPtr]
NullableType = Union[Optional, Nullable]
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

class AccessViolationException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Action(Generic[T], MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, obj: T, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, obj: T) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Action(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Action(Generic[T1, T2], MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, arg1: T1, arg2: T2, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, arg1: T1, arg2: T2) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Action(Generic[T1, T2, T3], MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Action(Generic[T1, T2, T3, T4], MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Action(Generic[T1, T2, T3, T4, T5], MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Action(Generic[T1, T2, T3, T4, T5, T6], MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Action(Generic[T1, T2, T3, T4, T5, T6, T7], MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Action(Generic[T1, T2, T3, T4, T5, T6, T7, T8], MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ActivationContext(ObjectType, IDisposable, ISerializable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ApplicationManifestBytes(self) -> ArrayType[ByteType]: ...
    
    @property
    def DeploymentManifestBytes(self) -> ArrayType[ByteType]: ...
    
    @property
    def Form(self) -> ContextForm: ...
    
    @property
    def Identity(self) -> ApplicationIdentity: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def CreatePartialActivationContext(identity: ApplicationIdentity) -> ActivationContext: ...
    
    @staticmethod
    @overload
    def CreatePartialActivationContext(identity: ApplicationIdentity, manifestPaths: ArrayType[StringType]) -> ActivationContext: ...
    
    def Dispose(self) -> VoidType: ...
    
    def get_ApplicationManifestBytes(self) -> ArrayType[ByteType]: ...
    
    def get_DeploymentManifestBytes(self) -> ArrayType[ByteType]: ...
    
    def get_Form(self) -> ContextForm: ...
    
    def get_Identity(self) -> ApplicationIdentity: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class ContextForm(Enum):
        Loose: IntType = 0
        StoreBounded: IntType = 1
    


class Activator(ObjectType, _Activator):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def CreateComInstanceFrom(assemblyName: StringType, typeName: StringType) -> ObjectHandle: ...
    
    @staticmethod
    @overload
    def CreateComInstanceFrom(assemblyName: StringType, typeName: StringType, hashValue: ArrayType[ByteType], hashAlgorithm: AssemblyHashAlgorithm) -> ObjectHandle: ...
    
    @staticmethod
    @overload
    def CreateInstance(type: TypeType, bindingAttr: BindingFlags, binder: Binder, args: ArrayType[ObjectType], culture: CultureInfo) -> ObjectType: ...
    
    @staticmethod
    @overload
    def CreateInstance(type: TypeType, bindingAttr: BindingFlags, binder: Binder, args: ArrayType[ObjectType], culture: CultureInfo, activationAttributes: ArrayType[ObjectType]) -> ObjectType: ...
    
    @staticmethod
    @overload
    def CreateInstance(type: TypeType, args: ArrayType[ObjectType]) -> ObjectType: ...
    
    @staticmethod
    @overload
    def CreateInstance(type: TypeType, args: ArrayType[ObjectType], activationAttributes: ArrayType[ObjectType]) -> ObjectType: ...
    
    @staticmethod
    @overload
    def CreateInstance(type: TypeType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def CreateInstance(assemblyName: StringType, typeName: StringType) -> ObjectHandle: ...
    
    @staticmethod
    @overload
    def CreateInstance(assemblyName: StringType, typeName: StringType, activationAttributes: ArrayType[ObjectType]) -> ObjectHandle: ...
    
    @staticmethod
    @overload
    def CreateInstance(type: TypeType, nonPublic: BooleanType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def CreateInstance(assemblyName: StringType, typeName: StringType, ignoreCase: BooleanType, bindingAttr: BindingFlags, binder: Binder, args: ArrayType[ObjectType], culture: CultureInfo, activationAttributes: ArrayType[ObjectType], securityInfo: Evidence) -> ObjectHandle: ...
    
    @staticmethod
    @overload
    def CreateInstance(assemblyName: StringType, typeName: StringType, ignoreCase: BooleanType, bindingAttr: BindingFlags, binder: Binder, args: ArrayType[ObjectType], culture: CultureInfo, activationAttributes: ArrayType[ObjectType]) -> ObjectHandle: ...
    
    @staticmethod
    @overload
    def CreateInstance(domain: AppDomain, assemblyName: StringType, typeName: StringType) -> ObjectHandle: ...
    
    @staticmethod
    @overload
    def CreateInstance(domain: AppDomain, assemblyName: StringType, typeName: StringType, ignoreCase: BooleanType, bindingAttr: BindingFlags, binder: Binder, args: ArrayType[ObjectType], culture: CultureInfo, activationAttributes: ArrayType[ObjectType], securityAttributes: Evidence) -> ObjectHandle: ...
    
    @staticmethod
    @overload
    def CreateInstance(domain: AppDomain, assemblyName: StringType, typeName: StringType, ignoreCase: BooleanType, bindingAttr: BindingFlags, binder: Binder, args: ArrayType[ObjectType], culture: CultureInfo, activationAttributes: ArrayType[ObjectType]) -> ObjectHandle: ...
    
    @staticmethod
    @overload
    def CreateInstance(activationContext: ActivationContext) -> ObjectHandle: ...
    
    @staticmethod
    @overload
    def CreateInstance(activationContext: ActivationContext, activationCustomData: ArrayType[StringType]) -> ObjectHandle: ...
    
    @staticmethod
    @overload
    def CreateInstance() -> T: ...
    
    @staticmethod
    @overload
    def CreateInstanceFrom(assemblyFile: StringType, typeName: StringType) -> ObjectHandle: ...
    
    @staticmethod
    @overload
    def CreateInstanceFrom(assemblyFile: StringType, typeName: StringType, activationAttributes: ArrayType[ObjectType]) -> ObjectHandle: ...
    
    @staticmethod
    @overload
    def CreateInstanceFrom(assemblyFile: StringType, typeName: StringType, ignoreCase: BooleanType, bindingAttr: BindingFlags, binder: Binder, args: ArrayType[ObjectType], culture: CultureInfo, activationAttributes: ArrayType[ObjectType], securityInfo: Evidence) -> ObjectHandle: ...
    
    @staticmethod
    @overload
    def CreateInstanceFrom(assemblyFile: StringType, typeName: StringType, ignoreCase: BooleanType, bindingAttr: BindingFlags, binder: Binder, args: ArrayType[ObjectType], culture: CultureInfo, activationAttributes: ArrayType[ObjectType]) -> ObjectHandle: ...
    
    @staticmethod
    @overload
    def CreateInstanceFrom(domain: AppDomain, assemblyFile: StringType, typeName: StringType) -> ObjectHandle: ...
    
    @staticmethod
    @overload
    def CreateInstanceFrom(domain: AppDomain, assemblyFile: StringType, typeName: StringType, ignoreCase: BooleanType, bindingAttr: BindingFlags, binder: Binder, args: ArrayType[ObjectType], culture: CultureInfo, activationAttributes: ArrayType[ObjectType], securityAttributes: Evidence) -> ObjectHandle: ...
    
    @staticmethod
    @overload
    def CreateInstanceFrom(domain: AppDomain, assemblyFile: StringType, typeName: StringType, ignoreCase: BooleanType, bindingAttr: BindingFlags, binder: Binder, args: ArrayType[ObjectType], culture: CultureInfo, activationAttributes: ArrayType[ObjectType]) -> ObjectHandle: ...
    
    @staticmethod
    @overload
    def GetObject(type: TypeType, url: StringType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def GetObject(type: TypeType, url: StringType, state: ObjectType) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AggregateException(Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, innerExceptions: IEnumerable[Exception]): ...
    
    @overload
    def __init__(self, innerExceptions: ArrayType[Exception]): ...
    
    @overload
    def __init__(self, message: StringType, innerExceptions: IEnumerable[Exception]): ...
    
    @overload
    def __init__(self, message: StringType, innerExceptions: ArrayType[Exception]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def InnerExceptions(self) -> ReadOnlyCollection[Exception]: ...
    
    # ---------- Methods ---------- #
    
    def Flatten(self) -> AggregateException: ...
    
    def GetBaseException(self) -> Exception: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def Handle(self, predicate: Func[Exception, BooleanType]) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_InnerExceptions(self) -> ReadOnlyCollection[Exception]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AppContext(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def BaseDirectory() -> StringType: ...
    
    @staticmethod
    @property
    def TargetFrameworkName() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetData(name: StringType) -> ObjectType: ...
    
    @staticmethod
    def SetSwitch(switchName: StringType, isEnabled: BooleanType) -> VoidType: ...
    
    @staticmethod
    def TryGetSwitch(switchName: StringType, isEnabled: BooleanType) -> Tuple[BooleanType, BooleanType]: ...
    
    @staticmethod
    def get_BaseDirectory() -> StringType: ...
    
    @staticmethod
    def get_TargetFrameworkName() -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AppContextDefaultValues(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def PopulateDefaultValues() -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AppContextDefaultValues(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def PopulateDefaultValues() -> VoidType: ...
    
    @staticmethod
    def TryGetSwitchOverride(switchName: StringType, overrideValue: BooleanType) -> Tuple[BooleanType, BooleanType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AppContextDefaultValues(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def PopulateDefaultValues() -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AppContextDefaultValues(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def PopulateDefaultValues() -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AppContextSwitches(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def BlockLongPaths() -> BooleanType: ...
    
    @staticmethod
    @property
    def DoNotAddrOfCspParentWindowHandle() -> BooleanType: ...
    
    @staticmethod
    @property
    def DoNotMarshalOutByrefSafeArrayOnInvoke() -> BooleanType: ...
    
    @staticmethod
    @property
    def EnforceJapaneseEraYearRanges() -> BooleanType: ...
    
    @staticmethod
    @property
    def EnforceLegacyJapaneseDateParsing() -> BooleanType: ...
    
    @staticmethod
    @property
    def FormatJapaneseFirstYearAsANumber() -> BooleanType: ...
    
    @staticmethod
    @property
    def IgnorePortablePDBsInStackTraces() -> BooleanType: ...
    
    @staticmethod
    @property
    def NoAsyncCurrentCulture() -> BooleanType: ...
    
    @staticmethod
    @property
    def PreserveEventListnerObjectIdentity() -> BooleanType: ...
    
    @staticmethod
    @property
    def SetActorAsReferenceWhenCopyingClaimsIdentity() -> BooleanType: ...
    
    @staticmethod
    @property
    def ThrowExceptionIfDisposedCancellationTokenSource() -> BooleanType: ...
    
    @staticmethod
    @property
    def UseConcurrentFormatterTypeCache() -> BooleanType: ...
    
    @staticmethod
    @property
    def UseLegacyExecutionContextBehaviorUponUndoFailure() -> BooleanType: ...
    
    @staticmethod
    @property
    def UseLegacyFipsThrow() -> BooleanType: ...
    
    @staticmethod
    @property
    def UseLegacyPathHandling() -> BooleanType: ...
    
    @staticmethod
    @property
    def UseNetCoreTimer() -> BooleanType: ...
    
    @staticmethod
    @property
    def UseNewMaxArraySize() -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_BlockLongPaths() -> BooleanType: ...
    
    @staticmethod
    def get_DoNotAddrOfCspParentWindowHandle() -> BooleanType: ...
    
    @staticmethod
    def get_DoNotMarshalOutByrefSafeArrayOnInvoke() -> BooleanType: ...
    
    @staticmethod
    def get_EnforceJapaneseEraYearRanges() -> BooleanType: ...
    
    @staticmethod
    def get_EnforceLegacyJapaneseDateParsing() -> BooleanType: ...
    
    @staticmethod
    def get_FormatJapaneseFirstYearAsANumber() -> BooleanType: ...
    
    @staticmethod
    def get_IgnorePortablePDBsInStackTraces() -> BooleanType: ...
    
    @staticmethod
    def get_NoAsyncCurrentCulture() -> BooleanType: ...
    
    @staticmethod
    def get_PreserveEventListnerObjectIdentity() -> BooleanType: ...
    
    @staticmethod
    def get_SetActorAsReferenceWhenCopyingClaimsIdentity() -> BooleanType: ...
    
    @staticmethod
    def get_ThrowExceptionIfDisposedCancellationTokenSource() -> BooleanType: ...
    
    @staticmethod
    def get_UseConcurrentFormatterTypeCache() -> BooleanType: ...
    
    @staticmethod
    def get_UseLegacyExecutionContextBehaviorUponUndoFailure() -> BooleanType: ...
    
    @staticmethod
    def get_UseLegacyFipsThrow() -> BooleanType: ...
    
    @staticmethod
    def get_UseLegacyPathHandling() -> BooleanType: ...
    
    @staticmethod
    def get_UseNetCoreTimer() -> BooleanType: ...
    
    @staticmethod
    def get_UseNewMaxArraySize() -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AppDomain(MarshalByRefObject, _AppDomain, IEvidenceFactory):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ActivationContext(self) -> ActivationContext: ...
    
    @property
    def ApplicationIdentity(self) -> ApplicationIdentity: ...
    
    @property
    def ApplicationTrust(self) -> ApplicationTrust: ...
    
    @property
    def BaseDirectory(self) -> StringType: ...
    
    @staticmethod
    @property
    def CurrentDomain() -> AppDomain: ...
    
    @property
    def DomainManager(self) -> AppDomainManager: ...
    
    @property
    def DynamicDirectory(self) -> StringType: ...
    
    @property
    def Evidence(self) -> Evidence: ...
    
    @property
    def FriendlyName(self) -> StringType: ...
    
    @property
    def Id(self) -> IntType: ...
    
    @property
    def IsFullyTrusted(self) -> BooleanType: ...
    
    @property
    def IsHomogenous(self) -> BooleanType: ...
    
    @staticmethod
    @property
    def MonitoringIsEnabled() -> BooleanType: ...
    
    @staticmethod
    @MonitoringIsEnabled.setter
    def MonitoringIsEnabled(value: BooleanType) -> None: ...
    
    @property
    def MonitoringSurvivedMemorySize(self) -> LongType: ...
    
    @staticmethod
    @property
    def MonitoringSurvivedProcessMemorySize() -> LongType: ...
    
    @property
    def MonitoringTotalAllocatedMemorySize(self) -> LongType: ...
    
    @property
    def MonitoringTotalProcessorTime(self) -> TimeSpan: ...
    
    @property
    def PermissionSet(self) -> PermissionSet: ...
    
    @property
    def RelativeSearchPath(self) -> StringType: ...
    
    @property
    def SetupInformation(self) -> AppDomainSetup: ...
    
    @property
    def ShadowCopyFiles(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def AppendPrivatePath(self, path: StringType) -> VoidType: ...
    
    def ApplyPolicy(self, assemblyName: StringType) -> StringType: ...
    
    def ClearPrivatePath(self) -> VoidType: ...
    
    def ClearShadowCopyPath(self) -> VoidType: ...
    
    @overload
    def CreateComInstanceFrom(self, assemblyName: StringType, typeName: StringType) -> ObjectHandle: ...
    
    @overload
    def CreateComInstanceFrom(self, assemblyFile: StringType, typeName: StringType, hashValue: ArrayType[ByteType], hashAlgorithm: AssemblyHashAlgorithm) -> ObjectHandle: ...
    
    @staticmethod
    @overload
    def CreateDomain(friendlyName: StringType, securityInfo: Evidence) -> AppDomain: ...
    
    @staticmethod
    @overload
    def CreateDomain(friendlyName: StringType) -> AppDomain: ...
    
    @staticmethod
    @overload
    def CreateDomain(friendlyName: StringType, securityInfo: Evidence, info: AppDomainSetup) -> AppDomain: ...
    
    @staticmethod
    @overload
    def CreateDomain(friendlyName: StringType, securityInfo: Evidence, info: AppDomainSetup, grantSet: PermissionSet, fullTrustAssemblies: ArrayType[StrongName]) -> AppDomain: ...
    
    @staticmethod
    @overload
    def CreateDomain(friendlyName: StringType, securityInfo: Evidence, appBasePath: StringType, appRelativeSearchPath: StringType, shadowCopyFiles: BooleanType) -> AppDomain: ...
    
    @staticmethod
    @overload
    def CreateDomain(friendlyName: StringType, securityInfo: Evidence, appBasePath: StringType, appRelativeSearchPath: StringType, shadowCopyFiles: BooleanType, adInit: AppDomainInitializer, adInitArgs: ArrayType[StringType]) -> AppDomain: ...
    
    @overload
    def CreateInstance(self, assemblyName: StringType, typeName: StringType) -> ObjectHandle: ...
    
    @overload
    def CreateInstance(self, assemblyName: StringType, typeName: StringType, activationAttributes: ArrayType[ObjectType]) -> ObjectHandle: ...
    
    @overload
    def CreateInstance(self, assemblyName: StringType, typeName: StringType, ignoreCase: BooleanType, bindingAttr: BindingFlags, binder: Binder, args: ArrayType[ObjectType], culture: CultureInfo, activationAttributes: ArrayType[ObjectType], securityAttributes: Evidence) -> ObjectHandle: ...
    
    @overload
    def CreateInstance(self, assemblyName: StringType, typeName: StringType, ignoreCase: BooleanType, bindingAttr: BindingFlags, binder: Binder, args: ArrayType[ObjectType], culture: CultureInfo, activationAttributes: ArrayType[ObjectType]) -> ObjectHandle: ...
    
    @overload
    def CreateInstanceAndUnwrap(self, assemblyName: StringType, typeName: StringType) -> ObjectType: ...
    
    @overload
    def CreateInstanceAndUnwrap(self, assemblyName: StringType, typeName: StringType, activationAttributes: ArrayType[ObjectType]) -> ObjectType: ...
    
    @overload
    def CreateInstanceAndUnwrap(self, assemblyName: StringType, typeName: StringType, ignoreCase: BooleanType, bindingAttr: BindingFlags, binder: Binder, args: ArrayType[ObjectType], culture: CultureInfo, activationAttributes: ArrayType[ObjectType], securityAttributes: Evidence) -> ObjectType: ...
    
    @overload
    def CreateInstanceAndUnwrap(self, assemblyName: StringType, typeName: StringType, ignoreCase: BooleanType, bindingAttr: BindingFlags, binder: Binder, args: ArrayType[ObjectType], culture: CultureInfo, activationAttributes: ArrayType[ObjectType]) -> ObjectType: ...
    
    @overload
    def CreateInstanceFrom(self, assemblyFile: StringType, typeName: StringType) -> ObjectHandle: ...
    
    @overload
    def CreateInstanceFrom(self, assemblyFile: StringType, typeName: StringType, activationAttributes: ArrayType[ObjectType]) -> ObjectHandle: ...
    
    @overload
    def CreateInstanceFrom(self, assemblyFile: StringType, typeName: StringType, ignoreCase: BooleanType, bindingAttr: BindingFlags, binder: Binder, args: ArrayType[ObjectType], culture: CultureInfo, activationAttributes: ArrayType[ObjectType], securityAttributes: Evidence) -> ObjectHandle: ...
    
    @overload
    def CreateInstanceFrom(self, assemblyFile: StringType, typeName: StringType, ignoreCase: BooleanType, bindingAttr: BindingFlags, binder: Binder, args: ArrayType[ObjectType], culture: CultureInfo, activationAttributes: ArrayType[ObjectType]) -> ObjectHandle: ...
    
    @overload
    def CreateInstanceFromAndUnwrap(self, assemblyName: StringType, typeName: StringType) -> ObjectType: ...
    
    @overload
    def CreateInstanceFromAndUnwrap(self, assemblyName: StringType, typeName: StringType, activationAttributes: ArrayType[ObjectType]) -> ObjectType: ...
    
    @overload
    def CreateInstanceFromAndUnwrap(self, assemblyName: StringType, typeName: StringType, ignoreCase: BooleanType, bindingAttr: BindingFlags, binder: Binder, args: ArrayType[ObjectType], culture: CultureInfo, activationAttributes: ArrayType[ObjectType], securityAttributes: Evidence) -> ObjectType: ...
    
    @overload
    def CreateInstanceFromAndUnwrap(self, assemblyFile: StringType, typeName: StringType, ignoreCase: BooleanType, bindingAttr: BindingFlags, binder: Binder, args: ArrayType[ObjectType], culture: CultureInfo, activationAttributes: ArrayType[ObjectType]) -> ObjectType: ...
    
    @overload
    def DefineDynamicAssembly(self, name: AssemblyName, access: AssemblyBuilderAccess) -> AssemblyBuilder: ...
    
    @overload
    def DefineDynamicAssembly(self, name: AssemblyName, access: AssemblyBuilderAccess, dir: StringType) -> AssemblyBuilder: ...
    
    @overload
    def DefineDynamicAssembly(self, name: AssemblyName, access: AssemblyBuilderAccess, evidence: Evidence) -> AssemblyBuilder: ...
    
    @overload
    def DefineDynamicAssembly(self, name: AssemblyName, access: AssemblyBuilderAccess, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet) -> AssemblyBuilder: ...
    
    @overload
    def DefineDynamicAssembly(self, name: AssemblyName, access: AssemblyBuilderAccess, dir: StringType, evidence: Evidence) -> AssemblyBuilder: ...
    
    @overload
    def DefineDynamicAssembly(self, name: AssemblyName, access: AssemblyBuilderAccess, dir: StringType, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet) -> AssemblyBuilder: ...
    
    @overload
    def DefineDynamicAssembly(self, name: AssemblyName, access: AssemblyBuilderAccess, evidence: Evidence, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet) -> AssemblyBuilder: ...
    
    @overload
    def DefineDynamicAssembly(self, name: AssemblyName, access: AssemblyBuilderAccess, dir: StringType, evidence: Evidence, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet) -> AssemblyBuilder: ...
    
    @overload
    def DefineDynamicAssembly(self, name: AssemblyName, access: AssemblyBuilderAccess, dir: StringType, evidence: Evidence, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet, isSynchronized: BooleanType) -> AssemblyBuilder: ...
    
    @overload
    def DefineDynamicAssembly(self, name: AssemblyName, access: AssemblyBuilderAccess, assemblyAttributes: IEnumerable[CustomAttributeBuilder]) -> AssemblyBuilder: ...
    
    @overload
    def DefineDynamicAssembly(self, name: AssemblyName, access: AssemblyBuilderAccess, assemblyAttributes: IEnumerable[CustomAttributeBuilder], securityContextSource: SecurityContextSource) -> AssemblyBuilder: ...
    
    @overload
    def DefineDynamicAssembly(self, name: AssemblyName, access: AssemblyBuilderAccess, dir: StringType, evidence: Evidence, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet, isSynchronized: BooleanType, assemblyAttributes: IEnumerable[CustomAttributeBuilder]) -> AssemblyBuilder: ...
    
    @overload
    def DefineDynamicAssembly(self, name: AssemblyName, access: AssemblyBuilderAccess, dir: StringType, isSynchronized: BooleanType, assemblyAttributes: IEnumerable[CustomAttributeBuilder]) -> AssemblyBuilder: ...
    
    def DoCallBack(self, callBackDelegate: CrossAppDomainDelegate) -> VoidType: ...
    
    @overload
    def ExecuteAssembly(self, assemblyFile: StringType) -> IntType: ...
    
    @overload
    def ExecuteAssembly(self, assemblyFile: StringType, assemblySecurity: Evidence) -> IntType: ...
    
    @overload
    def ExecuteAssembly(self, assemblyFile: StringType, assemblySecurity: Evidence, args: ArrayType[StringType]) -> IntType: ...
    
    @overload
    def ExecuteAssembly(self, assemblyFile: StringType, args: ArrayType[StringType]) -> IntType: ...
    
    @overload
    def ExecuteAssembly(self, assemblyFile: StringType, assemblySecurity: Evidence, args: ArrayType[StringType], hashValue: ArrayType[ByteType], hashAlgorithm: AssemblyHashAlgorithm) -> IntType: ...
    
    @overload
    def ExecuteAssembly(self, assemblyFile: StringType, args: ArrayType[StringType], hashValue: ArrayType[ByteType], hashAlgorithm: AssemblyHashAlgorithm) -> IntType: ...
    
    @overload
    def ExecuteAssemblyByName(self, assemblyName: StringType) -> IntType: ...
    
    @overload
    def ExecuteAssemblyByName(self, assemblyName: StringType, assemblySecurity: Evidence) -> IntType: ...
    
    @overload
    def ExecuteAssemblyByName(self, assemblyName: StringType, assemblySecurity: Evidence, args: ArrayType[StringType]) -> IntType: ...
    
    @overload
    def ExecuteAssemblyByName(self, assemblyName: StringType, args: ArrayType[StringType]) -> IntType: ...
    
    @overload
    def ExecuteAssemblyByName(self, assemblyName: AssemblyName, assemblySecurity: Evidence, args: ArrayType[StringType]) -> IntType: ...
    
    @overload
    def ExecuteAssemblyByName(self, assemblyName: AssemblyName, args: ArrayType[StringType]) -> IntType: ...
    
    def GetAssemblies(self) -> ArrayType[Assembly]: ...
    
    @staticmethod
    def GetCurrentThreadId() -> IntType: ...
    
    def GetData(self, name: StringType) -> ObjectType: ...
    
    @overload
    def GetType(self) -> TypeType: ...
    
    def InitializeLifetimeService(self) -> ObjectType: ...
    
    def IsCompatibilitySwitchSet(self, value: StringType) -> NullableType[Nullable[BooleanType]]: ...
    
    def IsDefaultAppDomain(self) -> BooleanType: ...
    
    def IsFinalizingForUnload(self) -> BooleanType: ...
    
    @overload
    def Load(self, assemblyRef: AssemblyName) -> Assembly: ...
    
    @overload
    def Load(self, assemblyString: StringType) -> Assembly: ...
    
    @overload
    def Load(self, rawAssembly: ArrayType[ByteType]) -> Assembly: ...
    
    @overload
    def Load(self, rawAssembly: ArrayType[ByteType], rawSymbolStore: ArrayType[ByteType]) -> Assembly: ...
    
    @overload
    def Load(self, rawAssembly: ArrayType[ByteType], rawSymbolStore: ArrayType[ByteType], securityEvidence: Evidence) -> Assembly: ...
    
    @overload
    def Load(self, assemblyRef: AssemblyName, assemblySecurity: Evidence) -> Assembly: ...
    
    @overload
    def Load(self, assemblyString: StringType, assemblySecurity: Evidence) -> Assembly: ...
    
    def ReflectionOnlyGetAssemblies(self) -> ArrayType[Assembly]: ...
    
    def SetAppDomainPolicy(self, domainPolicy: PolicyLevel) -> VoidType: ...
    
    def SetCachePath(self, path: StringType) -> VoidType: ...
    
    @overload
    def SetData(self, name: StringType, data: ObjectType) -> VoidType: ...
    
    @overload
    def SetData(self, name: StringType, data: ObjectType, permission: IPermission) -> VoidType: ...
    
    def SetDynamicBase(self, path: StringType) -> VoidType: ...
    
    def SetPrincipalPolicy(self, policy: PrincipalPolicy) -> VoidType: ...
    
    def SetShadowCopyFiles(self) -> VoidType: ...
    
    def SetShadowCopyPath(self, path: StringType) -> VoidType: ...
    
    def SetThreadPrincipal(self, principal: IPrincipal) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    @staticmethod
    def Unload(domain: AppDomain) -> VoidType: ...
    
    def add_AssemblyLoad(self, value: AssemblyLoadEventHandler) -> VoidType: ...
    
    def add_AssemblyResolve(self, value: ResolveEventHandler) -> VoidType: ...
    
    def add_DomainUnload(self, value: EventHandler) -> VoidType: ...
    
    def add_FirstChanceException(self, value: EventHandler[FirstChanceExceptionEventArgs]) -> VoidType: ...
    
    def add_ProcessExit(self, value: EventHandler) -> VoidType: ...
    
    def add_ReflectionOnlyAssemblyResolve(self, value: ResolveEventHandler) -> VoidType: ...
    
    def add_ResourceResolve(self, value: ResolveEventHandler) -> VoidType: ...
    
    def add_TypeResolve(self, value: ResolveEventHandler) -> VoidType: ...
    
    def add_UnhandledException(self, value: UnhandledExceptionEventHandler) -> VoidType: ...
    
    def get_ActivationContext(self) -> ActivationContext: ...
    
    def get_ApplicationIdentity(self) -> ApplicationIdentity: ...
    
    def get_ApplicationTrust(self) -> ApplicationTrust: ...
    
    def get_BaseDirectory(self) -> StringType: ...
    
    @staticmethod
    def get_CurrentDomain() -> AppDomain: ...
    
    def get_DomainManager(self) -> AppDomainManager: ...
    
    def get_DynamicDirectory(self) -> StringType: ...
    
    def get_Evidence(self) -> Evidence: ...
    
    def get_FriendlyName(self) -> StringType: ...
    
    def get_Id(self) -> IntType: ...
    
    def get_IsFullyTrusted(self) -> BooleanType: ...
    
    def get_IsHomogenous(self) -> BooleanType: ...
    
    @staticmethod
    def get_MonitoringIsEnabled() -> BooleanType: ...
    
    def get_MonitoringSurvivedMemorySize(self) -> LongType: ...
    
    @staticmethod
    def get_MonitoringSurvivedProcessMemorySize() -> LongType: ...
    
    def get_MonitoringTotalAllocatedMemorySize(self) -> LongType: ...
    
    def get_MonitoringTotalProcessorTime(self) -> TimeSpan: ...
    
    def get_PermissionSet(self) -> PermissionSet: ...
    
    def get_RelativeSearchPath(self) -> StringType: ...
    
    def get_SetupInformation(self) -> AppDomainSetup: ...
    
    def get_ShadowCopyFiles(self) -> BooleanType: ...
    
    def remove_AssemblyLoad(self, value: AssemblyLoadEventHandler) -> VoidType: ...
    
    def remove_AssemblyResolve(self, value: ResolveEventHandler) -> VoidType: ...
    
    def remove_DomainUnload(self, value: EventHandler) -> VoidType: ...
    
    def remove_FirstChanceException(self, value: EventHandler[FirstChanceExceptionEventArgs]) -> VoidType: ...
    
    def remove_ProcessExit(self, value: EventHandler) -> VoidType: ...
    
    def remove_ReflectionOnlyAssemblyResolve(self, value: ResolveEventHandler) -> VoidType: ...
    
    def remove_ResourceResolve(self, value: ResolveEventHandler) -> VoidType: ...
    
    def remove_TypeResolve(self, value: ResolveEventHandler) -> VoidType: ...
    
    def remove_UnhandledException(self, value: UnhandledExceptionEventHandler) -> VoidType: ...
    
    @staticmethod
    def set_MonitoringIsEnabled(value: BooleanType) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    AssemblyLoad: EventType[AssemblyLoadEventHandler] = ...
    
    AssemblyResolve: EventType[ResolveEventHandler] = ...
    
    DomainUnload: EventType[EventHandler] = ...
    
    FirstChanceException: EventType[EventHandler[FirstChanceExceptionEventArgs]] = ...
    
    ProcessExit: EventType[EventHandler] = ...
    
    ReflectionOnlyAssemblyResolve: EventType[ResolveEventHandler] = ...
    
    ResourceResolve: EventType[ResolveEventHandler] = ...
    
    TypeResolve: EventType[ResolveEventHandler] = ...
    
    UnhandledException: EventType[UnhandledExceptionEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AppDomainInitializer(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, args: ArrayType[StringType], callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, args: ArrayType[StringType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AppDomainInitializerInfo(ObjectType):
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


class AppDomainManager(MarshalByRefObject):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ApplicationActivator(self) -> ApplicationActivator: ...
    
    @property
    def EntryAssembly(self) -> Assembly: ...
    
    @property
    def HostExecutionContextManager(self) -> HostExecutionContextManager: ...
    
    @property
    def HostSecurityManager(self) -> HostSecurityManager: ...
    
    @property
    def InitializationFlags(self) -> AppDomainManagerInitializationOptions: ...
    
    @InitializationFlags.setter
    def InitializationFlags(self, value: AppDomainManagerInitializationOptions) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CheckSecuritySettings(self, state: SecurityState) -> BooleanType: ...
    
    def CreateDomain(self, friendlyName: StringType, securityInfo: Evidence, appDomainInfo: AppDomainSetup) -> AppDomain: ...
    
    def InitializeNewDomain(self, appDomainInfo: AppDomainSetup) -> VoidType: ...
    
    def get_ApplicationActivator(self) -> ApplicationActivator: ...
    
    def get_EntryAssembly(self) -> Assembly: ...
    
    def get_HostExecutionContextManager(self) -> HostExecutionContextManager: ...
    
    def get_HostSecurityManager(self) -> HostSecurityManager: ...
    
    def get_InitializationFlags(self) -> AppDomainManagerInitializationOptions: ...
    
    def set_InitializationFlags(self, value: AppDomainManagerInitializationOptions) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AppDomainPauseManager(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Paused(self) -> VoidType: ...
    
    def Pausing(self) -> VoidType: ...
    
    def Resumed(self) -> VoidType: ...
    
    def Resuming(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AppDomainSetup(ObjectType, IAppDomainSetup):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, activationContext: ActivationContext): ...
    
    @overload
    def __init__(self, activationArguments: ActivationArguments): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ActivationArguments(self) -> ActivationArguments: ...
    
    @ActivationArguments.setter
    def ActivationArguments(self, value: ActivationArguments) -> None: ...
    
    @property
    def AppDomainInitializer(self) -> AppDomainInitializer: ...
    
    @AppDomainInitializer.setter
    def AppDomainInitializer(self, value: AppDomainInitializer) -> None: ...
    
    @property
    def AppDomainInitializerArguments(self) -> ArrayType[StringType]: ...
    
    @AppDomainInitializerArguments.setter
    def AppDomainInitializerArguments(self, value: ArrayType[StringType]) -> None: ...
    
    @property
    def AppDomainManagerAssembly(self) -> StringType: ...
    
    @AppDomainManagerAssembly.setter
    def AppDomainManagerAssembly(self, value: StringType) -> None: ...
    
    @property
    def AppDomainManagerType(self) -> StringType: ...
    
    @AppDomainManagerType.setter
    def AppDomainManagerType(self, value: StringType) -> None: ...
    
    @property
    def ApplicationBase(self) -> StringType: ...
    
    @ApplicationBase.setter
    def ApplicationBase(self, value: StringType) -> None: ...
    
    @property
    def ApplicationName(self) -> StringType: ...
    
    @ApplicationName.setter
    def ApplicationName(self, value: StringType) -> None: ...
    
    @property
    def ApplicationTrust(self) -> ApplicationTrust: ...
    
    @ApplicationTrust.setter
    def ApplicationTrust(self, value: ApplicationTrust) -> None: ...
    
    @property
    def CachePath(self) -> StringType: ...
    
    @CachePath.setter
    def CachePath(self, value: StringType) -> None: ...
    
    @property
    def ConfigurationFile(self) -> StringType: ...
    
    @ConfigurationFile.setter
    def ConfigurationFile(self, value: StringType) -> None: ...
    
    @property
    def DisallowApplicationBaseProbing(self) -> BooleanType: ...
    
    @DisallowApplicationBaseProbing.setter
    def DisallowApplicationBaseProbing(self, value: BooleanType) -> None: ...
    
    @property
    def DisallowBindingRedirects(self) -> BooleanType: ...
    
    @DisallowBindingRedirects.setter
    def DisallowBindingRedirects(self, value: BooleanType) -> None: ...
    
    @property
    def DisallowCodeDownload(self) -> BooleanType: ...
    
    @DisallowCodeDownload.setter
    def DisallowCodeDownload(self, value: BooleanType) -> None: ...
    
    @property
    def DisallowPublisherPolicy(self) -> BooleanType: ...
    
    @DisallowPublisherPolicy.setter
    def DisallowPublisherPolicy(self, value: BooleanType) -> None: ...
    
    @property
    def DynamicBase(self) -> StringType: ...
    
    @DynamicBase.setter
    def DynamicBase(self, value: StringType) -> None: ...
    
    @property
    def LicenseFile(self) -> StringType: ...
    
    @LicenseFile.setter
    def LicenseFile(self, value: StringType) -> None: ...
    
    @property
    def LoaderOptimization(self) -> LoaderOptimization: ...
    
    @LoaderOptimization.setter
    def LoaderOptimization(self, value: LoaderOptimization) -> None: ...
    
    @property
    def PartialTrustVisibleAssemblies(self) -> ArrayType[StringType]: ...
    
    @PartialTrustVisibleAssemblies.setter
    def PartialTrustVisibleAssemblies(self, value: ArrayType[StringType]) -> None: ...
    
    @property
    def PrivateBinPath(self) -> StringType: ...
    
    @PrivateBinPath.setter
    def PrivateBinPath(self, value: StringType) -> None: ...
    
    @property
    def PrivateBinPathProbe(self) -> StringType: ...
    
    @PrivateBinPathProbe.setter
    def PrivateBinPathProbe(self, value: StringType) -> None: ...
    
    @property
    def SandboxInterop(self) -> BooleanType: ...
    
    @SandboxInterop.setter
    def SandboxInterop(self, value: BooleanType) -> None: ...
    
    @property
    def ShadowCopyDirectories(self) -> StringType: ...
    
    @ShadowCopyDirectories.setter
    def ShadowCopyDirectories(self, value: StringType) -> None: ...
    
    @property
    def ShadowCopyFiles(self) -> StringType: ...
    
    @ShadowCopyFiles.setter
    def ShadowCopyFiles(self, value: StringType) -> None: ...
    
    @property
    def TargetFrameworkName(self) -> StringType: ...
    
    @TargetFrameworkName.setter
    def TargetFrameworkName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetConfigurationBytes(self) -> ArrayType[ByteType]: ...
    
    def SetCompatibilitySwitches(self, switches: IEnumerable[StringType]) -> VoidType: ...
    
    def SetConfigurationBytes(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    def SetNativeFunction(self, functionName: StringType, functionVersion: IntType, functionPointer: NIntType) -> VoidType: ...
    
    def get_ActivationArguments(self) -> ActivationArguments: ...
    
    def get_AppDomainInitializer(self) -> AppDomainInitializer: ...
    
    def get_AppDomainInitializerArguments(self) -> ArrayType[StringType]: ...
    
    def get_AppDomainManagerAssembly(self) -> StringType: ...
    
    def get_AppDomainManagerType(self) -> StringType: ...
    
    def get_ApplicationBase(self) -> StringType: ...
    
    def get_ApplicationName(self) -> StringType: ...
    
    def get_ApplicationTrust(self) -> ApplicationTrust: ...
    
    def get_CachePath(self) -> StringType: ...
    
    def get_ConfigurationFile(self) -> StringType: ...
    
    def get_DisallowApplicationBaseProbing(self) -> BooleanType: ...
    
    def get_DisallowBindingRedirects(self) -> BooleanType: ...
    
    def get_DisallowCodeDownload(self) -> BooleanType: ...
    
    def get_DisallowPublisherPolicy(self) -> BooleanType: ...
    
    def get_DynamicBase(self) -> StringType: ...
    
    def get_LicenseFile(self) -> StringType: ...
    
    def get_LoaderOptimization(self) -> LoaderOptimization: ...
    
    def get_PartialTrustVisibleAssemblies(self) -> ArrayType[StringType]: ...
    
    def get_PrivateBinPath(self) -> StringType: ...
    
    def get_PrivateBinPathProbe(self) -> StringType: ...
    
    def get_SandboxInterop(self) -> BooleanType: ...
    
    def get_ShadowCopyDirectories(self) -> StringType: ...
    
    def get_ShadowCopyFiles(self) -> StringType: ...
    
    def get_TargetFrameworkName(self) -> StringType: ...
    
    def set_ActivationArguments(self, value: ActivationArguments) -> VoidType: ...
    
    def set_AppDomainInitializer(self, value: AppDomainInitializer) -> VoidType: ...
    
    def set_AppDomainInitializerArguments(self, value: ArrayType[StringType]) -> VoidType: ...
    
    def set_AppDomainManagerAssembly(self, value: StringType) -> VoidType: ...
    
    def set_AppDomainManagerType(self, value: StringType) -> VoidType: ...
    
    def set_ApplicationBase(self, value: StringType) -> VoidType: ...
    
    def set_ApplicationName(self, value: StringType) -> VoidType: ...
    
    def set_ApplicationTrust(self, value: ApplicationTrust) -> VoidType: ...
    
    def set_CachePath(self, value: StringType) -> VoidType: ...
    
    def set_ConfigurationFile(self, value: StringType) -> VoidType: ...
    
    def set_DisallowApplicationBaseProbing(self, value: BooleanType) -> VoidType: ...
    
    def set_DisallowBindingRedirects(self, value: BooleanType) -> VoidType: ...
    
    def set_DisallowCodeDownload(self, value: BooleanType) -> VoidType: ...
    
    def set_DisallowPublisherPolicy(self, value: BooleanType) -> VoidType: ...
    
    def set_DynamicBase(self, value: StringType) -> VoidType: ...
    
    def set_LicenseFile(self, value: StringType) -> VoidType: ...
    
    def set_LoaderOptimization(self, value: LoaderOptimization) -> VoidType: ...
    
    def set_PartialTrustVisibleAssemblies(self, value: ArrayType[StringType]) -> VoidType: ...
    
    def set_PrivateBinPath(self, value: StringType) -> VoidType: ...
    
    def set_PrivateBinPathProbe(self, value: StringType) -> VoidType: ...
    
    def set_SandboxInterop(self, value: BooleanType) -> VoidType: ...
    
    def set_ShadowCopyDirectories(self, value: StringType) -> VoidType: ...
    
    def set_ShadowCopyFiles(self, value: StringType) -> VoidType: ...
    
    def set_TargetFrameworkName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AppDomainUnloadedException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationException(Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationId(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, publicKeyToken: ArrayType[ByteType], name: StringType, version: Version, processorArchitecture: StringType, culture: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Culture(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ProcessorArchitecture(self) -> StringType: ...
    
    @property
    def PublicKeyToken(self) -> ArrayType[ByteType]: ...
    
    @property
    def Version(self) -> Version: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> ApplicationId: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Culture(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ProcessorArchitecture(self) -> StringType: ...
    
    def get_PublicKeyToken(self) -> ArrayType[ByteType]: ...
    
    def get_Version(self) -> Version: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationIdentity(ObjectType, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, applicationIdentityFullName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CodeBase(self) -> StringType: ...
    
    @property
    def FullName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    def get_CodeBase(self) -> StringType: ...
    
    def get_FullName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ArgumentException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, message: StringType, paramName: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, message: StringType, paramName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Message(self) -> StringType: ...
    
    @property
    def ParamName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_Message(self) -> StringType: ...
    
    def get_ParamName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ArgumentNullException(ArgumentException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, paramName: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, paramName: StringType, message: StringType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ArgumentOutOfRangeException(ArgumentException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, paramName: StringType): ...
    
    @overload
    def __init__(self, paramName: StringType, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, paramName: StringType, actualValue: ObjectType, message: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ActualValue(self) -> ObjectType: ...
    
    @property
    def Message(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_ActualValue(self) -> ObjectType: ...
    
    def get_Message(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ArithmeticException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Array(ABC, ObjectType, ICloneable, IList, ICollection, IEnumerable, IStructuralComparable, IStructuralEquatable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsFixedSize(self) -> BooleanType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def Length(self) -> IntType: ...
    
    @property
    def LongLength(self) -> LongType: ...
    
    @property
    def Rank(self) -> IntType: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def AsReadOnly(array: ArrayType[T]) -> ReadOnlyCollection[T]: ...
    
    @staticmethod
    @overload
    def BinarySearch(array: Array, value: ObjectType) -> IntType: ...
    
    @staticmethod
    @overload
    def BinarySearch(array: Array, index: IntType, length: IntType, value: ObjectType) -> IntType: ...
    
    @staticmethod
    @overload
    def BinarySearch(array: Array, value: ObjectType, comparer: IComparer) -> IntType: ...
    
    @staticmethod
    @overload
    def BinarySearch(array: ArrayType[T], value: T) -> IntType: ...
    
    @staticmethod
    @overload
    def BinarySearch(array: ArrayType[T], value: T, comparer: IComparer[T]) -> IntType: ...
    
    @staticmethod
    @overload
    def BinarySearch(array: ArrayType[T], index: IntType, length: IntType, value: T) -> IntType: ...
    
    @staticmethod
    @overload
    def BinarySearch(array: ArrayType[T], index: IntType, length: IntType, value: T, comparer: IComparer[T]) -> IntType: ...
    
    @staticmethod
    @overload
    def BinarySearch(array: Array, index: IntType, length: IntType, value: ObjectType, comparer: IComparer) -> IntType: ...
    
    @staticmethod
    def Clear(array: Array, index: IntType, length: IntType) -> VoidType: ...
    
    def Clone(self) -> ObjectType: ...
    
    @staticmethod
    def ConstrainedCopy(sourceArray: Array, sourceIndex: IntType, destinationArray: Array, destinationIndex: IntType, length: IntType) -> VoidType: ...
    
    @staticmethod
    def ConvertAll(array: ArrayType[TInput], converter: Converter[TInput, TOutput]) -> ArrayType[TOutput]: ...
    
    @staticmethod
    @overload
    def Copy(sourceArray: Array, destinationArray: Array, length: IntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Copy(sourceArray: Array, sourceIndex: IntType, destinationArray: Array, destinationIndex: IntType, length: IntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Copy(sourceArray: Array, destinationArray: Array, length: LongType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Copy(sourceArray: Array, sourceIndex: LongType, destinationArray: Array, destinationIndex: LongType, length: LongType) -> VoidType: ...
    
    @overload
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    @overload
    def CopyTo(self, array: Array, index: LongType) -> VoidType: ...
    
    @staticmethod
    @overload
    def CreateInstance(elementType: TypeType, length: IntType) -> Array: ...
    
    @staticmethod
    @overload
    def CreateInstance(elementType: TypeType, length1: IntType, length2: IntType, length3: IntType) -> Array: ...
    
    @staticmethod
    @overload
    def CreateInstance(elementType: TypeType, lengths: ArrayType[IntType]) -> Array: ...
    
    @staticmethod
    @overload
    def CreateInstance(elementType: TypeType, lengths: ArrayType[LongType]) -> Array: ...
    
    @staticmethod
    @overload
    def CreateInstance(elementType: TypeType, lengths: ArrayType[IntType], lowerBounds: ArrayType[IntType]) -> Array: ...
    
    @staticmethod
    @overload
    def CreateInstance(elementType: TypeType, length1: IntType, length2: IntType) -> Array: ...
    
    @staticmethod
    def Empty() -> ArrayType[T]: ...
    
    @staticmethod
    def Exists(array: ArrayType[T], match: Predicate[T]) -> BooleanType: ...
    
    @staticmethod
    def Find(array: ArrayType[T], match: Predicate[T]) -> T: ...
    
    @staticmethod
    def FindAll(array: ArrayType[T], match: Predicate[T]) -> ArrayType[T]: ...
    
    @staticmethod
    @overload
    def FindIndex(array: ArrayType[T], match: Predicate[T]) -> IntType: ...
    
    @staticmethod
    @overload
    def FindIndex(array: ArrayType[T], startIndex: IntType, match: Predicate[T]) -> IntType: ...
    
    @staticmethod
    @overload
    def FindIndex(array: ArrayType[T], startIndex: IntType, count: IntType, match: Predicate[T]) -> IntType: ...
    
    @staticmethod
    def FindLast(array: ArrayType[T], match: Predicate[T]) -> T: ...
    
    @staticmethod
    @overload
    def FindLastIndex(array: ArrayType[T], match: Predicate[T]) -> IntType: ...
    
    @staticmethod
    @overload
    def FindLastIndex(array: ArrayType[T], startIndex: IntType, match: Predicate[T]) -> IntType: ...
    
    @staticmethod
    @overload
    def FindLastIndex(array: ArrayType[T], startIndex: IntType, count: IntType, match: Predicate[T]) -> IntType: ...
    
    @staticmethod
    def ForEach(array: ArrayType[T], action: Action[T]) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def GetLength(self, dimension: IntType) -> IntType: ...
    
    def GetLongLength(self, dimension: IntType) -> LongType: ...
    
    def GetLowerBound(self, dimension: IntType) -> IntType: ...
    
    def GetUpperBound(self, dimension: IntType) -> IntType: ...
    
    @overload
    def GetValue(self, indices: ArrayType[IntType]) -> ObjectType: ...
    
    @overload
    def GetValue(self, index: IntType) -> ObjectType: ...
    
    @overload
    def GetValue(self, index1: IntType, index2: IntType) -> ObjectType: ...
    
    @overload
    def GetValue(self, index1: IntType, index2: IntType, index3: IntType) -> ObjectType: ...
    
    @overload
    def GetValue(self, index: LongType) -> ObjectType: ...
    
    @overload
    def GetValue(self, index1: LongType, index2: LongType) -> ObjectType: ...
    
    @overload
    def GetValue(self, index1: LongType, index2: LongType, index3: LongType) -> ObjectType: ...
    
    @overload
    def GetValue(self, indices: ArrayType[LongType]) -> ObjectType: ...
    
    @staticmethod
    @overload
    def IndexOf(array: Array, value: ObjectType) -> IntType: ...
    
    @staticmethod
    @overload
    def IndexOf(array: Array, value: ObjectType, startIndex: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def IndexOf(array: Array, value: ObjectType, startIndex: IntType, count: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def IndexOf(array: ArrayType[T], value: T) -> IntType: ...
    
    @staticmethod
    @overload
    def IndexOf(array: ArrayType[T], value: T, startIndex: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def IndexOf(array: ArrayType[T], value: T, startIndex: IntType, count: IntType) -> IntType: ...
    
    def Initialize(self) -> VoidType: ...
    
    @staticmethod
    @overload
    def LastIndexOf(array: Array, value: ObjectType) -> IntType: ...
    
    @staticmethod
    @overload
    def LastIndexOf(array: Array, value: ObjectType, startIndex: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def LastIndexOf(array: Array, value: ObjectType, startIndex: IntType, count: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def LastIndexOf(array: ArrayType[T], value: T) -> IntType: ...
    
    @staticmethod
    @overload
    def LastIndexOf(array: ArrayType[T], value: T, startIndex: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def LastIndexOf(array: ArrayType[T], value: T, startIndex: IntType, count: IntType) -> IntType: ...
    
    @staticmethod
    def Resize(array: T, newSize: IntType) -> Tuple[VoidType, T]: ...
    
    @staticmethod
    @overload
    def Reverse(array: Array) -> VoidType: ...
    
    @staticmethod
    @overload
    def Reverse(array: Array, index: IntType, length: IntType) -> VoidType: ...
    
    @overload
    def SetValue(self, value: ObjectType, index: IntType) -> VoidType: ...
    
    @overload
    def SetValue(self, value: ObjectType, index1: IntType, index2: IntType) -> VoidType: ...
    
    @overload
    def SetValue(self, value: ObjectType, index1: IntType, index2: IntType, index3: IntType) -> VoidType: ...
    
    @overload
    def SetValue(self, value: ObjectType, indices: ArrayType[IntType]) -> VoidType: ...
    
    @overload
    def SetValue(self, value: ObjectType, index: LongType) -> VoidType: ...
    
    @overload
    def SetValue(self, value: ObjectType, index1: LongType, index2: LongType) -> VoidType: ...
    
    @overload
    def SetValue(self, value: ObjectType, index1: LongType, index2: LongType, index3: LongType) -> VoidType: ...
    
    @overload
    def SetValue(self, value: ObjectType, indices: ArrayType[LongType]) -> VoidType: ...
    
    @staticmethod
    @overload
    def Sort(array: Array) -> VoidType: ...
    
    @staticmethod
    @overload
    def Sort(keys: Array, items: Array) -> VoidType: ...
    
    @staticmethod
    @overload
    def Sort(array: Array, index: IntType, length: IntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Sort(keys: Array, items: Array, index: IntType, length: IntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Sort(array: Array, comparer: IComparer) -> VoidType: ...
    
    @staticmethod
    @overload
    def Sort(keys: Array, items: Array, comparer: IComparer) -> VoidType: ...
    
    @staticmethod
    @overload
    def Sort(array: Array, index: IntType, length: IntType, comparer: IComparer) -> VoidType: ...
    
    @staticmethod
    @overload
    def Sort(array: ArrayType[T]) -> VoidType: ...
    
    @staticmethod
    @overload
    def Sort(keys: ArrayType[TKey], items: ArrayType[TValue]) -> VoidType: ...
    
    @staticmethod
    @overload
    def Sort(array: ArrayType[T], index: IntType, length: IntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Sort(keys: ArrayType[TKey], items: ArrayType[TValue], index: IntType, length: IntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Sort(array: ArrayType[T], comparer: IComparer[T]) -> VoidType: ...
    
    @staticmethod
    @overload
    def Sort(keys: ArrayType[TKey], items: ArrayType[TValue], comparer: IComparer[TKey]) -> VoidType: ...
    
    @staticmethod
    @overload
    def Sort(array: ArrayType[T], index: IntType, length: IntType, comparer: IComparer[T]) -> VoidType: ...
    
    @staticmethod
    @overload
    def Sort(keys: ArrayType[TKey], items: ArrayType[TValue], index: IntType, length: IntType, comparer: IComparer[TKey]) -> VoidType: ...
    
    @staticmethod
    @overload
    def Sort(array: ArrayType[T], comparison: Comparison[T]) -> VoidType: ...
    
    @staticmethod
    @overload
    def Sort(keys: Array, items: Array, index: IntType, length: IntType, comparer: IComparer) -> VoidType: ...
    
    @staticmethod
    def TrueForAll(array: ArrayType[T], match: Predicate[T]) -> BooleanType: ...
    
    def get_IsFixedSize(self) -> BooleanType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Length(self) -> IntType: ...
    
    def get_LongLength(self) -> LongType: ...
    
    def get_Rank(self) -> IntType: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ArrayTypeMismatchException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyLoadEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, loadedAssembly: Assembly): ...
    
    # ---------- Properties ---------- #
    
    @property
    def LoadedAssembly(self) -> Assembly: ...
    
    # ---------- Methods ---------- #
    
    def get_LoadedAssembly(self) -> Assembly: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyLoadEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, args: AssemblyLoadEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, args: AssemblyLoadEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsyncCallback(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, ar: IAsyncResult, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, ar: IAsyncResult) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Attribute(ABC, ObjectType, _Attribute):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def TypeId(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def GetCustomAttribute(element: MemberInfo, attributeType: TypeType) -> Attribute: ...
    
    @staticmethod
    @overload
    def GetCustomAttribute(element: MemberInfo, attributeType: TypeType, inherit: BooleanType) -> Attribute: ...
    
    @staticmethod
    @overload
    def GetCustomAttribute(element: ParameterInfo, attributeType: TypeType) -> Attribute: ...
    
    @staticmethod
    @overload
    def GetCustomAttribute(element: ParameterInfo, attributeType: TypeType, inherit: BooleanType) -> Attribute: ...
    
    @staticmethod
    @overload
    def GetCustomAttribute(element: Module, attributeType: TypeType) -> Attribute: ...
    
    @staticmethod
    @overload
    def GetCustomAttribute(element: Module, attributeType: TypeType, inherit: BooleanType) -> Attribute: ...
    
    @staticmethod
    @overload
    def GetCustomAttribute(element: Assembly, attributeType: TypeType) -> Attribute: ...
    
    @staticmethod
    @overload
    def GetCustomAttribute(element: Assembly, attributeType: TypeType, inherit: BooleanType) -> Attribute: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: MemberInfo, type: TypeType) -> ArrayType[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: MemberInfo, type: TypeType, inherit: BooleanType) -> ArrayType[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: MemberInfo) -> ArrayType[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: MemberInfo, inherit: BooleanType) -> ArrayType[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: ParameterInfo) -> ArrayType[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: ParameterInfo, attributeType: TypeType) -> ArrayType[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: ParameterInfo, attributeType: TypeType, inherit: BooleanType) -> ArrayType[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: ParameterInfo, inherit: BooleanType) -> ArrayType[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: Module, attributeType: TypeType) -> ArrayType[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: Module) -> ArrayType[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: Module, inherit: BooleanType) -> ArrayType[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: Module, attributeType: TypeType, inherit: BooleanType) -> ArrayType[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: Assembly, attributeType: TypeType) -> ArrayType[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: Assembly, attributeType: TypeType, inherit: BooleanType) -> ArrayType[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: Assembly) -> ArrayType[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: Assembly, inherit: BooleanType) -> ArrayType[Attribute]: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsDefined(element: MemberInfo, attributeType: TypeType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsDefined(element: MemberInfo, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsDefined(element: ParameterInfo, attributeType: TypeType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsDefined(element: ParameterInfo, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsDefined(element: Module, attributeType: TypeType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsDefined(element: Module, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsDefined(element: Assembly, attributeType: TypeType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsDefined(element: Assembly, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def Match(self, obj: ObjectType) -> BooleanType: ...
    
    def get_TypeId(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AttributeUsageAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, validOn: AttributeTargets): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AllowMultiple(self) -> BooleanType: ...
    
    @AllowMultiple.setter
    def AllowMultiple(self, value: BooleanType) -> None: ...
    
    @property
    def Inherited(self) -> BooleanType: ...
    
    @Inherited.setter
    def Inherited(self, value: BooleanType) -> None: ...
    
    @property
    def ValidOn(self) -> AttributeTargets: ...
    
    # ---------- Methods ---------- #
    
    def get_AllowMultiple(self) -> BooleanType: ...
    
    def get_Inherited(self) -> BooleanType: ...
    
    def get_ValidOn(self) -> AttributeTargets: ...
    
    def set_AllowMultiple(self, value: BooleanType) -> VoidType: ...
    
    def set_Inherited(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BCLDebug(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Assert(condition: BooleanType, message: StringType) -> VoidType: ...
    
    @staticmethod
    def DumpStack(switchName: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Log(message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Log(switchName: StringType, message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Log(switchName: StringType, level: LogLevel, messages: ArrayType[ObjectType]) -> VoidType: ...
    
    @staticmethod
    @overload
    def Trace(switchName: StringType, messages: ArrayType[ObjectType]) -> VoidType: ...
    
    @staticmethod
    @overload
    def Trace(switchName: StringType, format: StringType, messages: ArrayType[ObjectType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BadImageFormatException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    @overload
    def __init__(self, message: StringType, fileName: StringType): ...
    
    @overload
    def __init__(self, message: StringType, fileName: StringType, inner: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def FileName(self) -> StringType: ...
    
    @property
    def FusionLog(self) -> StringType: ...
    
    @property
    def Message(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_FileName(self) -> StringType: ...
    
    def get_FusionLog(self) -> StringType: ...
    
    def get_Message(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BaseConfigHandler(ABC, ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginChildren(self, size: IntType, subType: ConfigNodeSubType, nType: ConfigNodeType, terminal: IntType, text: StringType, textLength: IntType, prefixLength: IntType) -> VoidType: ...
    
    def CreateAttribute(self, size: IntType, subType: ConfigNodeSubType, nType: ConfigNodeType, terminal: IntType, text: StringType, textLength: IntType, prefixLength: IntType) -> VoidType: ...
    
    def CreateNode(self, size: IntType, subType: ConfigNodeSubType, nType: ConfigNodeType, terminal: IntType, text: StringType, textLength: IntType, prefixLength: IntType) -> VoidType: ...
    
    def EndChildren(self, fEmpty: IntType, size: IntType, subType: ConfigNodeSubType, nType: ConfigNodeType, terminal: IntType, text: StringType, textLength: IntType, prefixLength: IntType) -> VoidType: ...
    
    def Error(self, size: IntType, subType: ConfigNodeSubType, nType: ConfigNodeType, terminal: IntType, text: StringType, textLength: IntType, prefixLength: IntType) -> VoidType: ...
    
    def NotifyEvent(self, nEvent: ConfigEvents) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BitConverter(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def IsLittleEndian() -> BooleanType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def DoubleToInt64Bits(value: DoubleType) -> LongType: ...
    
    @staticmethod
    @overload
    def GetBytes(value: BooleanType) -> ArrayType[ByteType]: ...
    
    @staticmethod
    @overload
    def GetBytes(value: CharType) -> ArrayType[ByteType]: ...
    
    @staticmethod
    @overload
    def GetBytes(value: ShortType) -> ArrayType[ByteType]: ...
    
    @staticmethod
    @overload
    def GetBytes(value: IntType) -> ArrayType[ByteType]: ...
    
    @staticmethod
    @overload
    def GetBytes(value: LongType) -> ArrayType[ByteType]: ...
    
    @staticmethod
    @overload
    def GetBytes(value: UShortType) -> ArrayType[ByteType]: ...
    
    @staticmethod
    @overload
    def GetBytes(value: UIntType) -> ArrayType[ByteType]: ...
    
    @staticmethod
    @overload
    def GetBytes(value: ULongType) -> ArrayType[ByteType]: ...
    
    @staticmethod
    @overload
    def GetBytes(value: FloatType) -> ArrayType[ByteType]: ...
    
    @staticmethod
    @overload
    def GetBytes(value: DoubleType) -> ArrayType[ByteType]: ...
    
    @staticmethod
    def Int64BitsToDouble(value: LongType) -> DoubleType: ...
    
    @staticmethod
    def ToBoolean(value: ArrayType[ByteType], startIndex: IntType) -> BooleanType: ...
    
    @staticmethod
    def ToChar(value: ArrayType[ByteType], startIndex: IntType) -> CharType: ...
    
    @staticmethod
    def ToDouble(value: ArrayType[ByteType], startIndex: IntType) -> DoubleType: ...
    
    @staticmethod
    def ToInt16(value: ArrayType[ByteType], startIndex: IntType) -> ShortType: ...
    
    @staticmethod
    def ToInt32(value: ArrayType[ByteType], startIndex: IntType) -> IntType: ...
    
    @staticmethod
    def ToInt64(value: ArrayType[ByteType], startIndex: IntType) -> LongType: ...
    
    @staticmethod
    def ToSingle(value: ArrayType[ByteType], startIndex: IntType) -> FloatType: ...
    
    @staticmethod
    @overload
    def ToString(value: ArrayType[ByteType], startIndex: IntType, length: IntType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: ArrayType[ByteType]) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: ArrayType[ByteType], startIndex: IntType) -> StringType: ...
    
    @staticmethod
    def ToUInt16(value: ArrayType[ByteType], startIndex: IntType) -> UShortType: ...
    
    @staticmethod
    def ToUInt32(value: ArrayType[ByteType], startIndex: IntType) -> UIntType: ...
    
    @staticmethod
    def ToUInt64(value: ArrayType[ByteType], startIndex: IntType) -> ULongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Buffer(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def BlockCopy(src: Array, srcOffset: IntType, dst: Array, dstOffset: IntType, count: IntType) -> VoidType: ...
    
    @staticmethod
    def ByteLength(array: Array) -> IntType: ...
    
    @staticmethod
    def GetByte(array: Array, index: IntType) -> ByteType: ...
    
    @staticmethod
    @overload
    def MemoryCopy(source: VoidType, destination: VoidType, destinationSizeInBytes: LongType, sourceBytesToCopy: LongType) -> VoidType: ...
    
    @staticmethod
    @overload
    def MemoryCopy(source: VoidType, destination: VoidType, destinationSizeInBytes: ULongType, sourceBytesToCopy: ULongType) -> VoidType: ...
    
    @staticmethod
    def SetByte(array: Array, index: IntType, value: ByteType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CLRConfig(ObjectType):
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


class CLSCompliantAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, isCompliant: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsCompliant(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_IsCompliant(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CannotUnloadAppDomainException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CharEnumerator(ObjectType, IEnumerator, ICloneable, IEnumerator[CharType], IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> CharType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ObjectType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> CharType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ClientUtils(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetBitCount(x: UIntType) -> IntType: ...
    
    @staticmethod
    def IsCriticalException(ex: Exception) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsEnumValid(enumValue: Enum, value: IntType, minValue: IntType, maxValue: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsEnumValid(enumValue: Enum, value: IntType, minValue: IntType, maxValue: IntType, maxNumberOfBitsOn: IntType) -> BooleanType: ...
    
    @staticmethod
    def IsEnumValid_Masked(enumValue: Enum, value: IntType, mask: UIntType) -> BooleanType: ...
    
    @staticmethod
    def IsEnumValid_NotSequential(enumValue: Enum, value: IntType, enumValues: ArrayType[IntType]) -> BooleanType: ...
    
    @staticmethod
    def IsSecurityOrCriticalException(ex: Exception) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Comparison(Generic[T], MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, x: T, y: T, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> IntType: ...
    
    def Invoke(self, x: T, y: T) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CompatibilitySwitches(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def IsAppEarlierThanSilverlight4() -> BooleanType: ...
    
    @staticmethod
    @property
    def IsAppEarlierThanWindowsPhone8() -> BooleanType: ...
    
    @staticmethod
    @property
    def IsAppEarlierThanWindowsPhoneMango() -> BooleanType: ...
    
    @staticmethod
    @property
    def IsCompatibilityBehaviorDefined() -> BooleanType: ...
    
    @staticmethod
    @property
    def IsNetFx40LegacySecurityPolicy() -> BooleanType: ...
    
    @staticmethod
    @property
    def IsNetFx40TimeSpanLegacyFormatMode() -> BooleanType: ...
    
    @staticmethod
    @property
    def IsNetFx45LegacyManagedDeflateStream() -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_IsAppEarlierThanSilverlight4() -> BooleanType: ...
    
    @staticmethod
    def get_IsAppEarlierThanWindowsPhone8() -> BooleanType: ...
    
    @staticmethod
    def get_IsAppEarlierThanWindowsPhoneMango() -> BooleanType: ...
    
    @staticmethod
    def get_IsCompatibilityBehaviorDefined() -> BooleanType: ...
    
    @staticmethod
    def get_IsNetFx40LegacySecurityPolicy() -> BooleanType: ...
    
    @staticmethod
    def get_IsNetFx40TimeSpanLegacyFormatMode() -> BooleanType: ...
    
    @staticmethod
    def get_IsNetFx45LegacyManagedDeflateStream() -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConfigNode(ObjectType):
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


class ConfigTreeParser(BaseConfigHandler):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginChildren(self, size: IntType, subType: ConfigNodeSubType, nType: ConfigNodeType, terminal: IntType, text: StringType, textLength: IntType, prefixLength: IntType) -> VoidType: ...
    
    def CreateAttribute(self, size: IntType, subType: ConfigNodeSubType, nType: ConfigNodeType, terminal: IntType, text: StringType, textLength: IntType, prefixLength: IntType) -> VoidType: ...
    
    def CreateNode(self, size: IntType, subType: ConfigNodeSubType, nType: ConfigNodeType, terminal: IntType, text: StringType, textLength: IntType, prefixLength: IntType) -> VoidType: ...
    
    def EndChildren(self, fEmpty: IntType, size: IntType, subType: ConfigNodeSubType, nType: ConfigNodeType, terminal: IntType, text: StringType, textLength: IntType, prefixLength: IntType) -> VoidType: ...
    
    def Error(self, size: IntType, subType: ConfigNodeSubType, nType: ConfigNodeType, terminal: IntType, text: StringType, textLength: IntType, prefixLength: IntType) -> VoidType: ...
    
    def NotifyEvent(self, nEvent: ConfigEvents) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Console(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def BackgroundColor() -> ConsoleColor: ...
    
    @staticmethod
    @BackgroundColor.setter
    def BackgroundColor(value: ConsoleColor) -> None: ...
    
    @staticmethod
    @property
    def BufferHeight() -> IntType: ...
    
    @staticmethod
    @BufferHeight.setter
    def BufferHeight(value: IntType) -> None: ...
    
    @staticmethod
    @property
    def BufferWidth() -> IntType: ...
    
    @staticmethod
    @BufferWidth.setter
    def BufferWidth(value: IntType) -> None: ...
    
    @staticmethod
    @property
    def CapsLock() -> BooleanType: ...
    
    @staticmethod
    @property
    def CursorLeft() -> IntType: ...
    
    @staticmethod
    @CursorLeft.setter
    def CursorLeft(value: IntType) -> None: ...
    
    @staticmethod
    @property
    def CursorSize() -> IntType: ...
    
    @staticmethod
    @CursorSize.setter
    def CursorSize(value: IntType) -> None: ...
    
    @staticmethod
    @property
    def CursorTop() -> IntType: ...
    
    @staticmethod
    @CursorTop.setter
    def CursorTop(value: IntType) -> None: ...
    
    @staticmethod
    @property
    def CursorVisible() -> BooleanType: ...
    
    @staticmethod
    @CursorVisible.setter
    def CursorVisible(value: BooleanType) -> None: ...
    
    @staticmethod
    @property
    def Error() -> TextWriter: ...
    
    @staticmethod
    @property
    def ForegroundColor() -> ConsoleColor: ...
    
    @staticmethod
    @ForegroundColor.setter
    def ForegroundColor(value: ConsoleColor) -> None: ...
    
    @staticmethod
    @property
    def In() -> TextReader: ...
    
    @staticmethod
    @property
    def InputEncoding() -> Encoding: ...
    
    @staticmethod
    @InputEncoding.setter
    def InputEncoding(value: Encoding) -> None: ...
    
    @staticmethod
    @property
    def IsErrorRedirected() -> BooleanType: ...
    
    @staticmethod
    @property
    def IsInputRedirected() -> BooleanType: ...
    
    @staticmethod
    @property
    def IsOutputRedirected() -> BooleanType: ...
    
    @staticmethod
    @property
    def KeyAvailable() -> BooleanType: ...
    
    @staticmethod
    @property
    def LargestWindowHeight() -> IntType: ...
    
    @staticmethod
    @property
    def LargestWindowWidth() -> IntType: ...
    
    @staticmethod
    @property
    def NumberLock() -> BooleanType: ...
    
    @staticmethod
    @property
    def Out() -> TextWriter: ...
    
    @staticmethod
    @property
    def OutputEncoding() -> Encoding: ...
    
    @staticmethod
    @OutputEncoding.setter
    def OutputEncoding(value: Encoding) -> None: ...
    
    @staticmethod
    @property
    def Title() -> StringType: ...
    
    @staticmethod
    @Title.setter
    def Title(value: StringType) -> None: ...
    
    @staticmethod
    @property
    def TreatControlCAsInput() -> BooleanType: ...
    
    @staticmethod
    @TreatControlCAsInput.setter
    def TreatControlCAsInput(value: BooleanType) -> None: ...
    
    @staticmethod
    @property
    def WindowHeight() -> IntType: ...
    
    @staticmethod
    @WindowHeight.setter
    def WindowHeight(value: IntType) -> None: ...
    
    @staticmethod
    @property
    def WindowLeft() -> IntType: ...
    
    @staticmethod
    @WindowLeft.setter
    def WindowLeft(value: IntType) -> None: ...
    
    @staticmethod
    @property
    def WindowTop() -> IntType: ...
    
    @staticmethod
    @WindowTop.setter
    def WindowTop(value: IntType) -> None: ...
    
    @staticmethod
    @property
    def WindowWidth() -> IntType: ...
    
    @staticmethod
    @WindowWidth.setter
    def WindowWidth(value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Beep() -> VoidType: ...
    
    @staticmethod
    @overload
    def Beep(frequency: IntType, duration: IntType) -> VoidType: ...
    
    @staticmethod
    def Clear() -> VoidType: ...
    
    @staticmethod
    @overload
    def MoveBufferArea(sourceLeft: IntType, sourceTop: IntType, sourceWidth: IntType, sourceHeight: IntType, targetLeft: IntType, targetTop: IntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def MoveBufferArea(sourceLeft: IntType, sourceTop: IntType, sourceWidth: IntType, sourceHeight: IntType, targetLeft: IntType, targetTop: IntType, sourceChar: CharType, sourceForeColor: ConsoleColor, sourceBackColor: ConsoleColor) -> VoidType: ...
    
    @staticmethod
    @overload
    def OpenStandardError() -> Stream: ...
    
    @staticmethod
    @overload
    def OpenStandardError(bufferSize: IntType) -> Stream: ...
    
    @staticmethod
    @overload
    def OpenStandardInput() -> Stream: ...
    
    @staticmethod
    @overload
    def OpenStandardInput(bufferSize: IntType) -> Stream: ...
    
    @staticmethod
    @overload
    def OpenStandardOutput() -> Stream: ...
    
    @staticmethod
    @overload
    def OpenStandardOutput(bufferSize: IntType) -> Stream: ...
    
    @staticmethod
    def Read() -> IntType: ...
    
    @staticmethod
    @overload
    def ReadKey() -> ConsoleKeyInfo: ...
    
    @staticmethod
    @overload
    def ReadKey(intercept: BooleanType) -> ConsoleKeyInfo: ...
    
    @staticmethod
    def ReadLine() -> StringType: ...
    
    @staticmethod
    def ResetColor() -> VoidType: ...
    
    @staticmethod
    def SetBufferSize(width: IntType, height: IntType) -> VoidType: ...
    
    @staticmethod
    def SetCursorPosition(left: IntType, top: IntType) -> VoidType: ...
    
    @staticmethod
    def SetError(newError: TextWriter) -> VoidType: ...
    
    @staticmethod
    def SetIn(newIn: TextReader) -> VoidType: ...
    
    @staticmethod
    def SetOut(newOut: TextWriter) -> VoidType: ...
    
    @staticmethod
    def SetWindowPosition(left: IntType, top: IntType) -> VoidType: ...
    
    @staticmethod
    def SetWindowSize(width: IntType, height: IntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(format: StringType, arg0: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(format: StringType, arg0: ObjectType, arg1: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(format: StringType, arg0: ObjectType, arg1: ObjectType, arg2: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(format: StringType, arg0: ObjectType, arg1: ObjectType, arg2: ObjectType, arg3: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(format: StringType, arg: ArrayType[ObjectType]) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(value: BooleanType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(value: CharType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(buffer: ArrayType[CharType]) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(value: DoubleType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(value: DecimalType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(value: FloatType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(value: IntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(value: UIntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(value: LongType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(value: ULongType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(value: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(value: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine() -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(value: BooleanType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(value: CharType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(buffer: ArrayType[CharType]) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(value: DecimalType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(value: DoubleType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(value: FloatType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(value: IntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(value: UIntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(value: LongType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(value: ULongType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(value: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(value: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(format: StringType, arg0: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(format: StringType, arg0: ObjectType, arg1: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(format: StringType, arg0: ObjectType, arg1: ObjectType, arg2: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(format: StringType, arg0: ObjectType, arg1: ObjectType, arg2: ObjectType, arg3: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(format: StringType, arg: ArrayType[ObjectType]) -> VoidType: ...
    
    @staticmethod
    def add_CancelKeyPress(value: ConsoleCancelEventHandler) -> VoidType: ...
    
    @staticmethod
    def get_BackgroundColor() -> ConsoleColor: ...
    
    @staticmethod
    def get_BufferHeight() -> IntType: ...
    
    @staticmethod
    def get_BufferWidth() -> IntType: ...
    
    @staticmethod
    def get_CapsLock() -> BooleanType: ...
    
    @staticmethod
    def get_CursorLeft() -> IntType: ...
    
    @staticmethod
    def get_CursorSize() -> IntType: ...
    
    @staticmethod
    def get_CursorTop() -> IntType: ...
    
    @staticmethod
    def get_CursorVisible() -> BooleanType: ...
    
    @staticmethod
    def get_Error() -> TextWriter: ...
    
    @staticmethod
    def get_ForegroundColor() -> ConsoleColor: ...
    
    @staticmethod
    def get_In() -> TextReader: ...
    
    @staticmethod
    def get_InputEncoding() -> Encoding: ...
    
    @staticmethod
    def get_IsErrorRedirected() -> BooleanType: ...
    
    @staticmethod
    def get_IsInputRedirected() -> BooleanType: ...
    
    @staticmethod
    def get_IsOutputRedirected() -> BooleanType: ...
    
    @staticmethod
    def get_KeyAvailable() -> BooleanType: ...
    
    @staticmethod
    def get_LargestWindowHeight() -> IntType: ...
    
    @staticmethod
    def get_LargestWindowWidth() -> IntType: ...
    
    @staticmethod
    def get_NumberLock() -> BooleanType: ...
    
    @staticmethod
    def get_Out() -> TextWriter: ...
    
    @staticmethod
    def get_OutputEncoding() -> Encoding: ...
    
    @staticmethod
    def get_Title() -> StringType: ...
    
    @staticmethod
    def get_TreatControlCAsInput() -> BooleanType: ...
    
    @staticmethod
    def get_WindowHeight() -> IntType: ...
    
    @staticmethod
    def get_WindowLeft() -> IntType: ...
    
    @staticmethod
    def get_WindowTop() -> IntType: ...
    
    @staticmethod
    def get_WindowWidth() -> IntType: ...
    
    @staticmethod
    def remove_CancelKeyPress(value: ConsoleCancelEventHandler) -> VoidType: ...
    
    @staticmethod
    def set_BackgroundColor(value: ConsoleColor) -> VoidType: ...
    
    @staticmethod
    def set_BufferHeight(value: IntType) -> VoidType: ...
    
    @staticmethod
    def set_BufferWidth(value: IntType) -> VoidType: ...
    
    @staticmethod
    def set_CursorLeft(value: IntType) -> VoidType: ...
    
    @staticmethod
    def set_CursorSize(value: IntType) -> VoidType: ...
    
    @staticmethod
    def set_CursorTop(value: IntType) -> VoidType: ...
    
    @staticmethod
    def set_CursorVisible(value: BooleanType) -> VoidType: ...
    
    @staticmethod
    def set_ForegroundColor(value: ConsoleColor) -> VoidType: ...
    
    @staticmethod
    def set_InputEncoding(value: Encoding) -> VoidType: ...
    
    @staticmethod
    def set_OutputEncoding(value: Encoding) -> VoidType: ...
    
    @staticmethod
    def set_Title(value: StringType) -> VoidType: ...
    
    @staticmethod
    def set_TreatControlCAsInput(value: BooleanType) -> VoidType: ...
    
    @staticmethod
    def set_WindowHeight(value: IntType) -> VoidType: ...
    
    @staticmethod
    def set_WindowLeft(value: IntType) -> VoidType: ...
    
    @staticmethod
    def set_WindowTop(value: IntType) -> VoidType: ...
    
    @staticmethod
    def set_WindowWidth(value: IntType) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    CancelKeyPress: EventType[ConsoleCancelEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConsoleCancelEventArgs(EventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Cancel(self) -> BooleanType: ...
    
    @Cancel.setter
    def Cancel(self, value: BooleanType) -> None: ...
    
    @property
    def SpecialKey(self) -> ConsoleSpecialKey: ...
    
    # ---------- Methods ---------- #
    
    def get_Cancel(self) -> BooleanType: ...
    
    def get_SpecialKey(self) -> ConsoleSpecialKey: ...
    
    def set_Cancel(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConsoleCancelEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: ConsoleCancelEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: ConsoleCancelEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContextBoundObject(ABC, MarshalByRefObject):
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


class ContextMarshalException(SystemException, ISerializable, _Exception):
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


class ContextStaticAttribute(Attribute, _Attribute):
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


class Convert(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def DBNull() -> ObjectType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def ChangeType(value: ObjectType, typeCode: TypeCode) -> ObjectType: ...
    
    @staticmethod
    @overload
    def ChangeType(value: ObjectType, typeCode: TypeCode, provider: IFormatProvider) -> ObjectType: ...
    
    @staticmethod
    @overload
    def ChangeType(value: ObjectType, conversionType: TypeType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def ChangeType(value: ObjectType, conversionType: TypeType, provider: IFormatProvider) -> ObjectType: ...
    
    @staticmethod
    def FromBase64CharArray(inArray: ArrayType[CharType], offset: IntType, length: IntType) -> ArrayType[ByteType]: ...
    
    @staticmethod
    def FromBase64String(s: StringType) -> ArrayType[ByteType]: ...
    
    @staticmethod
    def GetTypeCode(value: ObjectType) -> TypeCode: ...
    
    @staticmethod
    def IsDBNull(value: ObjectType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def ToBase64CharArray(inArray: ArrayType[ByteType], offsetIn: IntType, length: IntType, outArray: ArrayType[CharType], offsetOut: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def ToBase64CharArray(inArray: ArrayType[ByteType], offsetIn: IntType, length: IntType, outArray: ArrayType[CharType], offsetOut: IntType, options: Base64FormattingOptions) -> IntType: ...
    
    @staticmethod
    @overload
    def ToBase64String(inArray: ArrayType[ByteType]) -> StringType: ...
    
    @staticmethod
    @overload
    def ToBase64String(inArray: ArrayType[ByteType], options: Base64FormattingOptions) -> StringType: ...
    
    @staticmethod
    @overload
    def ToBase64String(inArray: ArrayType[ByteType], offset: IntType, length: IntType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToBase64String(inArray: ArrayType[ByteType], offset: IntType, length: IntType, options: Base64FormattingOptions) -> StringType: ...
    
    @staticmethod
    @overload
    def ToBoolean(value: ObjectType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def ToBoolean(value: ObjectType, provider: IFormatProvider) -> BooleanType: ...
    
    @staticmethod
    @overload
    def ToBoolean(value: BooleanType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def ToBoolean(value: SByteType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def ToBoolean(value: CharType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def ToBoolean(value: ByteType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def ToBoolean(value: ShortType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def ToBoolean(value: UShortType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def ToBoolean(value: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def ToBoolean(value: UIntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def ToBoolean(value: LongType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def ToBoolean(value: ULongType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def ToBoolean(value: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def ToBoolean(value: StringType, provider: IFormatProvider) -> BooleanType: ...
    
    @staticmethod
    @overload
    def ToBoolean(value: FloatType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def ToBoolean(value: DoubleType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def ToBoolean(value: DecimalType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def ToBoolean(value: DateTime) -> BooleanType: ...
    
    @staticmethod
    @overload
    def ToByte(value: ObjectType) -> ByteType: ...
    
    @staticmethod
    @overload
    def ToByte(value: ObjectType, provider: IFormatProvider) -> ByteType: ...
    
    @staticmethod
    @overload
    def ToByte(value: BooleanType) -> ByteType: ...
    
    @staticmethod
    @overload
    def ToByte(value: ByteType) -> ByteType: ...
    
    @staticmethod
    @overload
    def ToByte(value: CharType) -> ByteType: ...
    
    @staticmethod
    @overload
    def ToByte(value: SByteType) -> ByteType: ...
    
    @staticmethod
    @overload
    def ToByte(value: ShortType) -> ByteType: ...
    
    @staticmethod
    @overload
    def ToByte(value: UShortType) -> ByteType: ...
    
    @staticmethod
    @overload
    def ToByte(value: IntType) -> ByteType: ...
    
    @staticmethod
    @overload
    def ToByte(value: UIntType) -> ByteType: ...
    
    @staticmethod
    @overload
    def ToByte(value: LongType) -> ByteType: ...
    
    @staticmethod
    @overload
    def ToByte(value: ULongType) -> ByteType: ...
    
    @staticmethod
    @overload
    def ToByte(value: FloatType) -> ByteType: ...
    
    @staticmethod
    @overload
    def ToByte(value: DoubleType) -> ByteType: ...
    
    @staticmethod
    @overload
    def ToByte(value: DecimalType) -> ByteType: ...
    
    @staticmethod
    @overload
    def ToByte(value: StringType) -> ByteType: ...
    
    @staticmethod
    @overload
    def ToByte(value: StringType, provider: IFormatProvider) -> ByteType: ...
    
    @staticmethod
    @overload
    def ToByte(value: DateTime) -> ByteType: ...
    
    @staticmethod
    @overload
    def ToByte(value: StringType, fromBase: IntType) -> ByteType: ...
    
    @staticmethod
    @overload
    def ToChar(value: ObjectType) -> CharType: ...
    
    @staticmethod
    @overload
    def ToChar(value: ObjectType, provider: IFormatProvider) -> CharType: ...
    
    @staticmethod
    @overload
    def ToChar(value: BooleanType) -> CharType: ...
    
    @staticmethod
    @overload
    def ToChar(value: CharType) -> CharType: ...
    
    @staticmethod
    @overload
    def ToChar(value: SByteType) -> CharType: ...
    
    @staticmethod
    @overload
    def ToChar(value: ByteType) -> CharType: ...
    
    @staticmethod
    @overload
    def ToChar(value: ShortType) -> CharType: ...
    
    @staticmethod
    @overload
    def ToChar(value: UShortType) -> CharType: ...
    
    @staticmethod
    @overload
    def ToChar(value: IntType) -> CharType: ...
    
    @staticmethod
    @overload
    def ToChar(value: UIntType) -> CharType: ...
    
    @staticmethod
    @overload
    def ToChar(value: LongType) -> CharType: ...
    
    @staticmethod
    @overload
    def ToChar(value: ULongType) -> CharType: ...
    
    @staticmethod
    @overload
    def ToChar(value: StringType) -> CharType: ...
    
    @staticmethod
    @overload
    def ToChar(value: StringType, provider: IFormatProvider) -> CharType: ...
    
    @staticmethod
    @overload
    def ToChar(value: FloatType) -> CharType: ...
    
    @staticmethod
    @overload
    def ToChar(value: DoubleType) -> CharType: ...
    
    @staticmethod
    @overload
    def ToChar(value: DecimalType) -> CharType: ...
    
    @staticmethod
    @overload
    def ToChar(value: DateTime) -> CharType: ...
    
    @staticmethod
    @overload
    def ToDateTime(value: DateTime) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTime(value: ObjectType) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTime(value: ObjectType, provider: IFormatProvider) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTime(value: StringType) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTime(value: StringType, provider: IFormatProvider) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTime(value: SByteType) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTime(value: ByteType) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTime(value: ShortType) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTime(value: UShortType) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTime(value: IntType) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTime(value: UIntType) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTime(value: LongType) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTime(value: ULongType) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTime(value: BooleanType) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTime(value: CharType) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTime(value: FloatType) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTime(value: DoubleType) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTime(value: DecimalType) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDecimal(value: ObjectType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def ToDecimal(value: ObjectType, provider: IFormatProvider) -> DecimalType: ...
    
    @staticmethod
    @overload
    def ToDecimal(value: SByteType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def ToDecimal(value: ByteType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def ToDecimal(value: CharType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def ToDecimal(value: ShortType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def ToDecimal(value: UShortType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def ToDecimal(value: IntType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def ToDecimal(value: UIntType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def ToDecimal(value: LongType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def ToDecimal(value: ULongType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def ToDecimal(value: FloatType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def ToDecimal(value: DoubleType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def ToDecimal(value: StringType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def ToDecimal(value: StringType, provider: IFormatProvider) -> DecimalType: ...
    
    @staticmethod
    @overload
    def ToDecimal(value: DecimalType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def ToDecimal(value: BooleanType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def ToDecimal(value: DateTime) -> DecimalType: ...
    
    @staticmethod
    @overload
    def ToDouble(value: ObjectType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def ToDouble(value: ObjectType, provider: IFormatProvider) -> DoubleType: ...
    
    @staticmethod
    @overload
    def ToDouble(value: SByteType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def ToDouble(value: ByteType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def ToDouble(value: ShortType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def ToDouble(value: CharType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def ToDouble(value: UShortType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def ToDouble(value: IntType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def ToDouble(value: UIntType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def ToDouble(value: LongType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def ToDouble(value: ULongType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def ToDouble(value: FloatType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def ToDouble(value: DoubleType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def ToDouble(value: DecimalType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def ToDouble(value: StringType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def ToDouble(value: StringType, provider: IFormatProvider) -> DoubleType: ...
    
    @staticmethod
    @overload
    def ToDouble(value: BooleanType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def ToDouble(value: DateTime) -> DoubleType: ...
    
    @staticmethod
    @overload
    def ToInt16(value: ObjectType) -> ShortType: ...
    
    @staticmethod
    @overload
    def ToInt16(value: ObjectType, provider: IFormatProvider) -> ShortType: ...
    
    @staticmethod
    @overload
    def ToInt16(value: BooleanType) -> ShortType: ...
    
    @staticmethod
    @overload
    def ToInt16(value: CharType) -> ShortType: ...
    
    @staticmethod
    @overload
    def ToInt16(value: SByteType) -> ShortType: ...
    
    @staticmethod
    @overload
    def ToInt16(value: ByteType) -> ShortType: ...
    
    @staticmethod
    @overload
    def ToInt16(value: UShortType) -> ShortType: ...
    
    @staticmethod
    @overload
    def ToInt16(value: IntType) -> ShortType: ...
    
    @staticmethod
    @overload
    def ToInt16(value: UIntType) -> ShortType: ...
    
    @staticmethod
    @overload
    def ToInt16(value: ShortType) -> ShortType: ...
    
    @staticmethod
    @overload
    def ToInt16(value: LongType) -> ShortType: ...
    
    @staticmethod
    @overload
    def ToInt16(value: ULongType) -> ShortType: ...
    
    @staticmethod
    @overload
    def ToInt16(value: FloatType) -> ShortType: ...
    
    @staticmethod
    @overload
    def ToInt16(value: DoubleType) -> ShortType: ...
    
    @staticmethod
    @overload
    def ToInt16(value: DecimalType) -> ShortType: ...
    
    @staticmethod
    @overload
    def ToInt16(value: StringType) -> ShortType: ...
    
    @staticmethod
    @overload
    def ToInt16(value: StringType, provider: IFormatProvider) -> ShortType: ...
    
    @staticmethod
    @overload
    def ToInt16(value: DateTime) -> ShortType: ...
    
    @staticmethod
    @overload
    def ToInt16(value: StringType, fromBase: IntType) -> ShortType: ...
    
    @staticmethod
    @overload
    def ToInt32(value: ObjectType) -> IntType: ...
    
    @staticmethod
    @overload
    def ToInt32(value: ObjectType, provider: IFormatProvider) -> IntType: ...
    
    @staticmethod
    @overload
    def ToInt32(value: BooleanType) -> IntType: ...
    
    @staticmethod
    @overload
    def ToInt32(value: CharType) -> IntType: ...
    
    @staticmethod
    @overload
    def ToInt32(value: SByteType) -> IntType: ...
    
    @staticmethod
    @overload
    def ToInt32(value: ByteType) -> IntType: ...
    
    @staticmethod
    @overload
    def ToInt32(value: ShortType) -> IntType: ...
    
    @staticmethod
    @overload
    def ToInt32(value: UShortType) -> IntType: ...
    
    @staticmethod
    @overload
    def ToInt32(value: UIntType) -> IntType: ...
    
    @staticmethod
    @overload
    def ToInt32(value: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def ToInt32(value: LongType) -> IntType: ...
    
    @staticmethod
    @overload
    def ToInt32(value: ULongType) -> IntType: ...
    
    @staticmethod
    @overload
    def ToInt32(value: FloatType) -> IntType: ...
    
    @staticmethod
    @overload
    def ToInt32(value: DoubleType) -> IntType: ...
    
    @staticmethod
    @overload
    def ToInt32(value: DecimalType) -> IntType: ...
    
    @staticmethod
    @overload
    def ToInt32(value: StringType) -> IntType: ...
    
    @staticmethod
    @overload
    def ToInt32(value: StringType, provider: IFormatProvider) -> IntType: ...
    
    @staticmethod
    @overload
    def ToInt32(value: DateTime) -> IntType: ...
    
    @staticmethod
    @overload
    def ToInt32(value: StringType, fromBase: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def ToInt64(value: ObjectType) -> LongType: ...
    
    @staticmethod
    @overload
    def ToInt64(value: ObjectType, provider: IFormatProvider) -> LongType: ...
    
    @staticmethod
    @overload
    def ToInt64(value: BooleanType) -> LongType: ...
    
    @staticmethod
    @overload
    def ToInt64(value: CharType) -> LongType: ...
    
    @staticmethod
    @overload
    def ToInt64(value: SByteType) -> LongType: ...
    
    @staticmethod
    @overload
    def ToInt64(value: ByteType) -> LongType: ...
    
    @staticmethod
    @overload
    def ToInt64(value: ShortType) -> LongType: ...
    
    @staticmethod
    @overload
    def ToInt64(value: UShortType) -> LongType: ...
    
    @staticmethod
    @overload
    def ToInt64(value: IntType) -> LongType: ...
    
    @staticmethod
    @overload
    def ToInt64(value: UIntType) -> LongType: ...
    
    @staticmethod
    @overload
    def ToInt64(value: ULongType) -> LongType: ...
    
    @staticmethod
    @overload
    def ToInt64(value: LongType) -> LongType: ...
    
    @staticmethod
    @overload
    def ToInt64(value: FloatType) -> LongType: ...
    
    @staticmethod
    @overload
    def ToInt64(value: DoubleType) -> LongType: ...
    
    @staticmethod
    @overload
    def ToInt64(value: DecimalType) -> LongType: ...
    
    @staticmethod
    @overload
    def ToInt64(value: StringType) -> LongType: ...
    
    @staticmethod
    @overload
    def ToInt64(value: StringType, provider: IFormatProvider) -> LongType: ...
    
    @staticmethod
    @overload
    def ToInt64(value: DateTime) -> LongType: ...
    
    @staticmethod
    @overload
    def ToInt64(value: StringType, fromBase: IntType) -> LongType: ...
    
    @staticmethod
    @overload
    def ToSByte(value: ObjectType) -> SByteType: ...
    
    @staticmethod
    @overload
    def ToSByte(value: ObjectType, provider: IFormatProvider) -> SByteType: ...
    
    @staticmethod
    @overload
    def ToSByte(value: BooleanType) -> SByteType: ...
    
    @staticmethod
    @overload
    def ToSByte(value: SByteType) -> SByteType: ...
    
    @staticmethod
    @overload
    def ToSByte(value: CharType) -> SByteType: ...
    
    @staticmethod
    @overload
    def ToSByte(value: ByteType) -> SByteType: ...
    
    @staticmethod
    @overload
    def ToSByte(value: ShortType) -> SByteType: ...
    
    @staticmethod
    @overload
    def ToSByte(value: UShortType) -> SByteType: ...
    
    @staticmethod
    @overload
    def ToSByte(value: IntType) -> SByteType: ...
    
    @staticmethod
    @overload
    def ToSByte(value: UIntType) -> SByteType: ...
    
    @staticmethod
    @overload
    def ToSByte(value: LongType) -> SByteType: ...
    
    @staticmethod
    @overload
    def ToSByte(value: ULongType) -> SByteType: ...
    
    @staticmethod
    @overload
    def ToSByte(value: FloatType) -> SByteType: ...
    
    @staticmethod
    @overload
    def ToSByte(value: DoubleType) -> SByteType: ...
    
    @staticmethod
    @overload
    def ToSByte(value: DecimalType) -> SByteType: ...
    
    @staticmethod
    @overload
    def ToSByte(value: StringType) -> SByteType: ...
    
    @staticmethod
    @overload
    def ToSByte(value: StringType, provider: IFormatProvider) -> SByteType: ...
    
    @staticmethod
    @overload
    def ToSByte(value: DateTime) -> SByteType: ...
    
    @staticmethod
    @overload
    def ToSByte(value: StringType, fromBase: IntType) -> SByteType: ...
    
    @staticmethod
    @overload
    def ToSingle(value: ObjectType) -> FloatType: ...
    
    @staticmethod
    @overload
    def ToSingle(value: ObjectType, provider: IFormatProvider) -> FloatType: ...
    
    @staticmethod
    @overload
    def ToSingle(value: SByteType) -> FloatType: ...
    
    @staticmethod
    @overload
    def ToSingle(value: ByteType) -> FloatType: ...
    
    @staticmethod
    @overload
    def ToSingle(value: CharType) -> FloatType: ...
    
    @staticmethod
    @overload
    def ToSingle(value: ShortType) -> FloatType: ...
    
    @staticmethod
    @overload
    def ToSingle(value: UShortType) -> FloatType: ...
    
    @staticmethod
    @overload
    def ToSingle(value: IntType) -> FloatType: ...
    
    @staticmethod
    @overload
    def ToSingle(value: UIntType) -> FloatType: ...
    
    @staticmethod
    @overload
    def ToSingle(value: LongType) -> FloatType: ...
    
    @staticmethod
    @overload
    def ToSingle(value: ULongType) -> FloatType: ...
    
    @staticmethod
    @overload
    def ToSingle(value: FloatType) -> FloatType: ...
    
    @staticmethod
    @overload
    def ToSingle(value: DoubleType) -> FloatType: ...
    
    @staticmethod
    @overload
    def ToSingle(value: DecimalType) -> FloatType: ...
    
    @staticmethod
    @overload
    def ToSingle(value: StringType) -> FloatType: ...
    
    @staticmethod
    @overload
    def ToSingle(value: StringType, provider: IFormatProvider) -> FloatType: ...
    
    @staticmethod
    @overload
    def ToSingle(value: BooleanType) -> FloatType: ...
    
    @staticmethod
    @overload
    def ToSingle(value: DateTime) -> FloatType: ...
    
    @staticmethod
    @overload
    def ToString(value: ObjectType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: ObjectType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: CharType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: CharType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: SByteType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: SByteType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: ByteType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: ByteType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: ShortType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: ShortType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: UShortType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: UShortType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: IntType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: IntType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: UIntType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: UIntType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: LongType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: LongType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: ULongType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: ULongType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: FloatType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: FloatType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: DoubleType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: DoubleType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: DecimalType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: DecimalType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: DateTime) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: DateTime, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: StringType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: ByteType, toBase: IntType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: ShortType, toBase: IntType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: IntType, toBase: IntType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: LongType, toBase: IntType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: BooleanType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: BooleanType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def ToUInt16(value: ObjectType) -> UShortType: ...
    
    @staticmethod
    @overload
    def ToUInt16(value: ObjectType, provider: IFormatProvider) -> UShortType: ...
    
    @staticmethod
    @overload
    def ToUInt16(value: BooleanType) -> UShortType: ...
    
    @staticmethod
    @overload
    def ToUInt16(value: CharType) -> UShortType: ...
    
    @staticmethod
    @overload
    def ToUInt16(value: SByteType) -> UShortType: ...
    
    @staticmethod
    @overload
    def ToUInt16(value: ByteType) -> UShortType: ...
    
    @staticmethod
    @overload
    def ToUInt16(value: ShortType) -> UShortType: ...
    
    @staticmethod
    @overload
    def ToUInt16(value: IntType) -> UShortType: ...
    
    @staticmethod
    @overload
    def ToUInt16(value: UShortType) -> UShortType: ...
    
    @staticmethod
    @overload
    def ToUInt16(value: UIntType) -> UShortType: ...
    
    @staticmethod
    @overload
    def ToUInt16(value: LongType) -> UShortType: ...
    
    @staticmethod
    @overload
    def ToUInt16(value: ULongType) -> UShortType: ...
    
    @staticmethod
    @overload
    def ToUInt16(value: FloatType) -> UShortType: ...
    
    @staticmethod
    @overload
    def ToUInt16(value: DoubleType) -> UShortType: ...
    
    @staticmethod
    @overload
    def ToUInt16(value: DecimalType) -> UShortType: ...
    
    @staticmethod
    @overload
    def ToUInt16(value: StringType) -> UShortType: ...
    
    @staticmethod
    @overload
    def ToUInt16(value: StringType, provider: IFormatProvider) -> UShortType: ...
    
    @staticmethod
    @overload
    def ToUInt16(value: DateTime) -> UShortType: ...
    
    @staticmethod
    @overload
    def ToUInt16(value: StringType, fromBase: IntType) -> UShortType: ...
    
    @staticmethod
    @overload
    def ToUInt32(value: ObjectType) -> UIntType: ...
    
    @staticmethod
    @overload
    def ToUInt32(value: ObjectType, provider: IFormatProvider) -> UIntType: ...
    
    @staticmethod
    @overload
    def ToUInt32(value: BooleanType) -> UIntType: ...
    
    @staticmethod
    @overload
    def ToUInt32(value: CharType) -> UIntType: ...
    
    @staticmethod
    @overload
    def ToUInt32(value: SByteType) -> UIntType: ...
    
    @staticmethod
    @overload
    def ToUInt32(value: ByteType) -> UIntType: ...
    
    @staticmethod
    @overload
    def ToUInt32(value: ShortType) -> UIntType: ...
    
    @staticmethod
    @overload
    def ToUInt32(value: UShortType) -> UIntType: ...
    
    @staticmethod
    @overload
    def ToUInt32(value: IntType) -> UIntType: ...
    
    @staticmethod
    @overload
    def ToUInt32(value: UIntType) -> UIntType: ...
    
    @staticmethod
    @overload
    def ToUInt32(value: LongType) -> UIntType: ...
    
    @staticmethod
    @overload
    def ToUInt32(value: ULongType) -> UIntType: ...
    
    @staticmethod
    @overload
    def ToUInt32(value: FloatType) -> UIntType: ...
    
    @staticmethod
    @overload
    def ToUInt32(value: DoubleType) -> UIntType: ...
    
    @staticmethod
    @overload
    def ToUInt32(value: DecimalType) -> UIntType: ...
    
    @staticmethod
    @overload
    def ToUInt32(value: StringType) -> UIntType: ...
    
    @staticmethod
    @overload
    def ToUInt32(value: StringType, provider: IFormatProvider) -> UIntType: ...
    
    @staticmethod
    @overload
    def ToUInt32(value: DateTime) -> UIntType: ...
    
    @staticmethod
    @overload
    def ToUInt32(value: StringType, fromBase: IntType) -> UIntType: ...
    
    @staticmethod
    @overload
    def ToUInt64(value: ObjectType) -> ULongType: ...
    
    @staticmethod
    @overload
    def ToUInt64(value: ObjectType, provider: IFormatProvider) -> ULongType: ...
    
    @staticmethod
    @overload
    def ToUInt64(value: BooleanType) -> ULongType: ...
    
    @staticmethod
    @overload
    def ToUInt64(value: CharType) -> ULongType: ...
    
    @staticmethod
    @overload
    def ToUInt64(value: SByteType) -> ULongType: ...
    
    @staticmethod
    @overload
    def ToUInt64(value: ByteType) -> ULongType: ...
    
    @staticmethod
    @overload
    def ToUInt64(value: ShortType) -> ULongType: ...
    
    @staticmethod
    @overload
    def ToUInt64(value: UShortType) -> ULongType: ...
    
    @staticmethod
    @overload
    def ToUInt64(value: IntType) -> ULongType: ...
    
    @staticmethod
    @overload
    def ToUInt64(value: UIntType) -> ULongType: ...
    
    @staticmethod
    @overload
    def ToUInt64(value: LongType) -> ULongType: ...
    
    @staticmethod
    @overload
    def ToUInt64(value: ULongType) -> ULongType: ...
    
    @staticmethod
    @overload
    def ToUInt64(value: FloatType) -> ULongType: ...
    
    @staticmethod
    @overload
    def ToUInt64(value: DoubleType) -> ULongType: ...
    
    @staticmethod
    @overload
    def ToUInt64(value: DecimalType) -> ULongType: ...
    
    @staticmethod
    @overload
    def ToUInt64(value: StringType) -> ULongType: ...
    
    @staticmethod
    @overload
    def ToUInt64(value: StringType, provider: IFormatProvider) -> ULongType: ...
    
    @staticmethod
    @overload
    def ToUInt64(value: DateTime) -> ULongType: ...
    
    @staticmethod
    @overload
    def ToUInt64(value: StringType, fromBase: IntType) -> ULongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Converter(Generic[TInput, TOutput], MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, input: TInput, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> TOutput: ...
    
    def Invoke(self, input: TInput) -> TOutput: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CrossAppDomainDelegate(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CtorDelegate(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, instance: ObjectType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, instance: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CultureAwareComparer(StringComparer, IComparer, IEqualityComparer, IComparer[StringType], IEqualityComparer[StringType], IWellKnownStringEqualityComparer):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Compare(self, x: StringType, y: StringType) -> IntType: ...
    
    @overload
    def Equals(self, x: StringType, y: StringType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def GetHashCode(self, obj: StringType) -> IntType: ...
    
    @overload
    def GetHashCode(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CultureAwareRandomizedComparer(StringComparer, IComparer, IEqualityComparer, IComparer[StringType], IEqualityComparer[StringType], IWellKnownStringEqualityComparer):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Compare(self, x: StringType, y: StringType) -> IntType: ...
    
    @overload
    def Equals(self, x: StringType, y: StringType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def GetHashCode(self, obj: StringType) -> IntType: ...
    
    @overload
    def GetHashCode(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CurrentSystemTimeZone(TimeZone):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def DaylightName(self) -> StringType: ...
    
    @property
    def StandardName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetDaylightChanges(self, year: IntType) -> DaylightTime: ...
    
    def GetUtcOffset(self, time: DateTime) -> TimeSpan: ...
    
    def ToLocalTime(self, time: DateTime) -> DateTime: ...
    
    def get_DaylightName(self) -> StringType: ...
    
    def get_StandardName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DBNull(ObjectType, ISerializable, IConvertible):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Value() -> DBNull: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def GetTypeCode(self) -> TypeCode: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, provider: IFormatProvider) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DataMisalignedException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DateTimeFormat(ABC, ObjectType):
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


class DateTimeParse(ABC, ObjectType):
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


class DefaultBinder(Binder):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BindToField(self, bindingAttr: BindingFlags, match: ArrayType[FieldInfo], value: ObjectType, cultureInfo: CultureInfo) -> FieldInfo: ...
    
    def BindToMethod(self, bindingAttr: BindingFlags, match: ArrayType[MethodBase], args: ObjectType, modifiers: ArrayType[ParameterModifier], cultureInfo: CultureInfo, names: ArrayType[StringType], state: ObjectType) -> Tuple[MethodBase, ObjectType, ObjectType]: ...
    
    def ChangeType(self, value: ObjectType, type: TypeType, cultureInfo: CultureInfo) -> ObjectType: ...
    
    @staticmethod
    def ExactBinding(match: ArrayType[MethodBase], types: ArrayType[TypeType], modifiers: ArrayType[ParameterModifier]) -> MethodBase: ...
    
    @staticmethod
    def ExactPropertyBinding(match: ArrayType[PropertyInfo], returnType: TypeType, types: ArrayType[TypeType], modifiers: ArrayType[ParameterModifier]) -> PropertyInfo: ...
    
    def ReorderArgumentArray(self, args: ObjectType, state: ObjectType) -> Tuple[VoidType, ObjectType]: ...
    
    def SelectMethod(self, bindingAttr: BindingFlags, match: ArrayType[MethodBase], types: ArrayType[TypeType], modifiers: ArrayType[ParameterModifier]) -> MethodBase: ...
    
    def SelectProperty(self, bindingAttr: BindingFlags, match: ArrayType[PropertyInfo], returnType: TypeType, indexes: ArrayType[TypeType], modifiers: ArrayType[ParameterModifier]) -> PropertyInfo: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Delegate(ABC, ObjectType, ICloneable, ISerializable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Method(self) -> MethodInfo: ...
    
    @property
    def Target(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ObjectType: ...
    
    @staticmethod
    @overload
    def Combine(a: Delegate, b: Delegate) -> Delegate: ...
    
    @staticmethod
    @overload
    def Combine(delegates: ArrayType[Delegate]) -> Delegate: ...
    
    @staticmethod
    @overload
    def CreateDelegate(type: TypeType, target: ObjectType, method: StringType) -> Delegate: ...
    
    @staticmethod
    @overload
    def CreateDelegate(type: TypeType, target: ObjectType, method: StringType, ignoreCase: BooleanType) -> Delegate: ...
    
    @staticmethod
    @overload
    def CreateDelegate(type: TypeType, target: ObjectType, method: StringType, ignoreCase: BooleanType, throwOnBindFailure: BooleanType) -> Delegate: ...
    
    @staticmethod
    @overload
    def CreateDelegate(type: TypeType, target: TypeType, method: StringType) -> Delegate: ...
    
    @staticmethod
    @overload
    def CreateDelegate(type: TypeType, target: TypeType, method: StringType, ignoreCase: BooleanType) -> Delegate: ...
    
    @staticmethod
    @overload
    def CreateDelegate(type: TypeType, target: TypeType, method: StringType, ignoreCase: BooleanType, throwOnBindFailure: BooleanType) -> Delegate: ...
    
    @staticmethod
    @overload
    def CreateDelegate(type: TypeType, method: MethodInfo, throwOnBindFailure: BooleanType) -> Delegate: ...
    
    @staticmethod
    @overload
    def CreateDelegate(type: TypeType, firstArgument: ObjectType, method: MethodInfo, throwOnBindFailure: BooleanType) -> Delegate: ...
    
    @staticmethod
    @overload
    def CreateDelegate(type: TypeType, method: MethodInfo) -> Delegate: ...
    
    @staticmethod
    @overload
    def CreateDelegate(type: TypeType, firstArgument: ObjectType, method: MethodInfo) -> Delegate: ...
    
    def DynamicInvoke(self, args: ArrayType[ObjectType]) -> ObjectType: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetInvocationList(self) -> ArrayType[Delegate]: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    @staticmethod
    def Remove(source: Delegate, value: Delegate) -> Delegate: ...
    
    @staticmethod
    def RemoveAll(source: Delegate, value: Delegate) -> Delegate: ...
    
    def get_Method(self) -> MethodInfo: ...
    
    def get_Target(self) -> ObjectType: ...
    
    @staticmethod
    def op_Equality(d1: Delegate, d2: Delegate) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(d1: Delegate, d2: Delegate) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DelegateSerializationHolder(ObjectType, IObjectReference, ISerializable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def GetRealObject(self, context: StreamingContext) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DivideByZeroException(ArithmeticException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DllNotFoundException(TypeLoadException, ISerializable, _Exception):
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


class DomainNameHelper(ObjectType):
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


class DuplicateWaitObjectException(ArgumentException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, parameterName: StringType): ...
    
    @overload
    def __init__(self, parameterName: StringType, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Empty(ObjectType, ISerializable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Value() -> Empty: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EntryPointNotFoundException(TypeLoadException, ISerializable, _Exception):
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


class Enum(ABC, ValueType, IComparable, IFormattable, IConvertible):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CompareTo(self, target: ObjectType) -> IntType: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @staticmethod
    def Format(enumType: TypeType, value: ObjectType, format: StringType) -> StringType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    def GetName(enumType: TypeType, value: ObjectType) -> StringType: ...
    
    @staticmethod
    def GetNames(enumType: TypeType) -> ArrayType[StringType]: ...
    
    def GetTypeCode(self) -> TypeCode: ...
    
    @staticmethod
    def GetUnderlyingType(enumType: TypeType) -> TypeType: ...
    
    @staticmethod
    def GetValues(enumType: TypeType) -> Array: ...
    
    def HasFlag(self, flag: Enum) -> BooleanType: ...
    
    @staticmethod
    def IsDefined(enumType: TypeType, value: ObjectType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Parse(enumType: TypeType, value: StringType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def Parse(enumType: TypeType, value: StringType, ignoreCase: BooleanType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def ToObject(enumType: TypeType, value: ObjectType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def ToObject(enumType: TypeType, value: SByteType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def ToObject(enumType: TypeType, value: ShortType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def ToObject(enumType: TypeType, value: IntType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def ToObject(enumType: TypeType, value: ByteType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def ToObject(enumType: TypeType, value: UShortType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def ToObject(enumType: TypeType, value: UIntType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def ToObject(enumType: TypeType, value: LongType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def ToObject(enumType: TypeType, value: ULongType) -> ObjectType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType, provider: IFormatProvider) -> StringType: ...
    
    @overload
    def ToString(self, provider: IFormatProvider) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def TryParse(value: StringType, result: TEnum) -> Tuple[BooleanType, TEnum]: ...
    
    @staticmethod
    @overload
    def TryParse(value: StringType, ignoreCase: BooleanType, result: TEnum) -> Tuple[BooleanType, TEnum]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Environment(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def CommandLine() -> StringType: ...
    
    @staticmethod
    @property
    def CurrentDirectory() -> StringType: ...
    
    @staticmethod
    @CurrentDirectory.setter
    def CurrentDirectory(value: StringType) -> None: ...
    
    @staticmethod
    @property
    def CurrentManagedThreadId() -> IntType: ...
    
    @staticmethod
    @property
    def ExitCode() -> IntType: ...
    
    @staticmethod
    @ExitCode.setter
    def ExitCode(value: IntType) -> None: ...
    
    @staticmethod
    @property
    def HasShutdownStarted() -> BooleanType: ...
    
    @staticmethod
    @property
    def Is64BitOperatingSystem() -> BooleanType: ...
    
    @staticmethod
    @property
    def Is64BitProcess() -> BooleanType: ...
    
    @staticmethod
    @property
    def MachineName() -> StringType: ...
    
    @staticmethod
    @property
    def NewLine() -> StringType: ...
    
    @staticmethod
    @property
    def OSVersion() -> OperatingSystem: ...
    
    @staticmethod
    @property
    def ProcessorCount() -> IntType: ...
    
    @staticmethod
    @property
    def StackTrace() -> StringType: ...
    
    @staticmethod
    @property
    def SystemDirectory() -> StringType: ...
    
    @staticmethod
    @property
    def SystemPageSize() -> IntType: ...
    
    @staticmethod
    @property
    def TickCount() -> IntType: ...
    
    @staticmethod
    @property
    def UserDomainName() -> StringType: ...
    
    @staticmethod
    @property
    def UserInteractive() -> BooleanType: ...
    
    @staticmethod
    @property
    def UserName() -> StringType: ...
    
    @staticmethod
    @property
    def Version() -> Version: ...
    
    @staticmethod
    @property
    def WorkingSet() -> LongType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Exit(exitCode: IntType) -> VoidType: ...
    
    @staticmethod
    def ExpandEnvironmentVariables(name: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def FailFast(message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def FailFast(message: StringType, exception: Exception) -> VoidType: ...
    
    @staticmethod
    def GetCommandLineArgs() -> ArrayType[StringType]: ...
    
    @staticmethod
    @overload
    def GetEnvironmentVariable(variable: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def GetEnvironmentVariable(variable: StringType, target: EnvironmentVariableTarget) -> StringType: ...
    
    @staticmethod
    @overload
    def GetEnvironmentVariables() -> IDictionary: ...
    
    @staticmethod
    @overload
    def GetEnvironmentVariables(target: EnvironmentVariableTarget) -> IDictionary: ...
    
    @staticmethod
    @overload
    def GetFolderPath(folder: SpecialFolder) -> StringType: ...
    
    @staticmethod
    @overload
    def GetFolderPath(folder: SpecialFolder, option: SpecialFolderOption) -> StringType: ...
    
    @staticmethod
    def GetLogicalDrives() -> ArrayType[StringType]: ...
    
    @staticmethod
    @overload
    def SetEnvironmentVariable(variable: StringType, value: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def SetEnvironmentVariable(variable: StringType, value: StringType, target: EnvironmentVariableTarget) -> VoidType: ...
    
    @staticmethod
    def get_CommandLine() -> StringType: ...
    
    @staticmethod
    def get_CurrentDirectory() -> StringType: ...
    
    @staticmethod
    def get_CurrentManagedThreadId() -> IntType: ...
    
    @staticmethod
    def get_ExitCode() -> IntType: ...
    
    @staticmethod
    def get_HasShutdownStarted() -> BooleanType: ...
    
    @staticmethod
    def get_Is64BitOperatingSystem() -> BooleanType: ...
    
    @staticmethod
    def get_Is64BitProcess() -> BooleanType: ...
    
    @staticmethod
    def get_MachineName() -> StringType: ...
    
    @staticmethod
    def get_NewLine() -> StringType: ...
    
    @staticmethod
    def get_OSVersion() -> OperatingSystem: ...
    
    @staticmethod
    def get_ProcessorCount() -> IntType: ...
    
    @staticmethod
    def get_StackTrace() -> StringType: ...
    
    @staticmethod
    def get_SystemDirectory() -> StringType: ...
    
    @staticmethod
    def get_SystemPageSize() -> IntType: ...
    
    @staticmethod
    def get_TickCount() -> IntType: ...
    
    @staticmethod
    def get_UserDomainName() -> StringType: ...
    
    @staticmethod
    def get_UserInteractive() -> BooleanType: ...
    
    @staticmethod
    def get_UserName() -> StringType: ...
    
    @staticmethod
    def get_Version() -> Version: ...
    
    @staticmethod
    def get_WorkingSet() -> LongType: ...
    
    @staticmethod
    def set_CurrentDirectory(value: StringType) -> VoidType: ...
    
    @staticmethod
    def set_ExitCode(value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class SpecialFolderOption(Enum):
        #None: IntType = 0
        DoNotVerify: IntType = 16384
        Create: IntType = 32768
    
    
    class SpecialFolder(Enum):
        Desktop: IntType = 0
        Programs: IntType = 2
        MyDocuments: IntType = 5
        Personal: IntType = 5
        Favorites: IntType = 6
        Startup: IntType = 7
        Recent: IntType = 8
        SendTo: IntType = 9
        StartMenu: IntType = 11
        MyMusic: IntType = 13
        MyVideos: IntType = 14
        DesktopDirectory: IntType = 16
        MyComputer: IntType = 17
        NetworkShortcuts: IntType = 19
        Fonts: IntType = 20
        Templates: IntType = 21
        CommonStartMenu: IntType = 22
        CommonPrograms: IntType = 23
        CommonStartup: IntType = 24
        CommonDesktopDirectory: IntType = 25
        ApplicationData: IntType = 26
        PrinterShortcuts: IntType = 27
        LocalApplicationData: IntType = 28
        InternetCache: IntType = 32
        Cookies: IntType = 33
        History: IntType = 34
        CommonApplicationData: IntType = 35
        Windows: IntType = 36
        System: IntType = 37
        ProgramFiles: IntType = 38
        MyPictures: IntType = 39
        UserProfile: IntType = 40
        SystemX86: IntType = 41
        ProgramFilesX86: IntType = 42
        CommonProgramFiles: IntType = 43
        CommonProgramFilesX86: IntType = 44
        CommonTemplates: IntType = 45
        CommonDocuments: IntType = 46
        CommonAdminTools: IntType = 47
        AdminTools: IntType = 48
        CommonMusic: IntType = 53
        CommonPictures: IntType = 54
        CommonVideos: IntType = 55
        Resources: IntType = 56
        LocalizedResources: IntType = 57
        CommonOemLinks: IntType = 58
        CDBurning: IntType = 59
    


class EnvironmentHelpers(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def IsAppContainerProcess() -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_IsAppContainerProcess() -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventArgs(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Empty() -> EventArgs: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: EventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: EventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventHandler(Generic[TEventArgs], MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: TEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: TEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Exception(ObjectType, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Data(self) -> IDictionary: ...
    
    @property
    def HResult(self) -> IntType: ...
    
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
    
    def GetBaseException(self) -> Exception: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    @overload
    def GetType(self) -> TypeType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Data(self) -> IDictionary: ...
    
    def get_HResult(self) -> IntType: ...
    
    def get_HelpLink(self) -> StringType: ...
    
    def get_InnerException(self) -> Exception: ...
    
    def get_Message(self) -> StringType: ...
    
    def get_Source(self) -> StringType: ...
    
    def get_StackTrace(self) -> StringType: ...
    
    def get_TargetSite(self) -> MethodBase: ...
    
    def set_HelpLink(self, value: StringType) -> VoidType: ...
    
    def set_Source(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExecutionEngineException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExternDll(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Activeds() -> StringType: ...
    
    @staticmethod
    @property
    def Advapi32() -> StringType: ...
    
    @staticmethod
    @property
    def Clr() -> StringType: ...
    
    @staticmethod
    @property
    def Comctl32() -> StringType: ...
    
    @staticmethod
    @property
    def Comdlg32() -> StringType: ...
    
    @staticmethod
    @property
    def Crypt32() -> StringType: ...
    
    @staticmethod
    @property
    def Fxassert() -> StringType: ...
    
    @staticmethod
    @property
    def Gdi32() -> StringType: ...
    
    @staticmethod
    @property
    def Gdiplus() -> StringType: ...
    
    @staticmethod
    @property
    def Hhctrl() -> StringType: ...
    
    @staticmethod
    @property
    def Imm32() -> StringType: ...
    
    @staticmethod
    @property
    def Kernel32() -> StringType: ...
    
    @staticmethod
    @property
    def Loadperf() -> StringType: ...
    
    @staticmethod
    @property
    def Mqrt() -> StringType: ...
    
    @staticmethod
    @property
    def Mscoree() -> StringType: ...
    
    @staticmethod
    @property
    def Msi() -> StringType: ...
    
    @staticmethod
    @property
    def Ntdll() -> StringType: ...
    
    @staticmethod
    @property
    def Ole32() -> StringType: ...
    
    @staticmethod
    @property
    def Oleacc() -> StringType: ...
    
    @staticmethod
    @property
    def Oleaut32() -> StringType: ...
    
    @staticmethod
    @property
    def Olepro32() -> StringType: ...
    
    @staticmethod
    @property
    def PerfCounter() -> StringType: ...
    
    @staticmethod
    @property
    def Powrprof() -> StringType: ...
    
    @staticmethod
    @property
    def Psapi() -> StringType: ...
    
    @staticmethod
    @property
    def ShCore() -> StringType: ...
    
    @staticmethod
    @property
    def Shell32() -> StringType: ...
    
    @staticmethod
    @property
    def Shlwapi() -> StringType: ...
    
    @staticmethod
    @property
    def User32() -> StringType: ...
    
    @staticmethod
    @property
    def Uxtheme() -> StringType: ...
    
    @staticmethod
    @property
    def Version() -> StringType: ...
    
    @staticmethod
    @property
    def Vsassert() -> StringType: ...
    
    @staticmethod
    @property
    def WinMM() -> StringType: ...
    
    @staticmethod
    @property
    def Winspool() -> StringType: ...
    
    @staticmethod
    @property
    def Wldp() -> StringType: ...
    
    @staticmethod
    @property
    def Wtsapi32() -> StringType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExternDll(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Activeds() -> StringType: ...
    
    @staticmethod
    @property
    def Advapi32() -> StringType: ...
    
    @staticmethod
    @property
    def Clr() -> StringType: ...
    
    @staticmethod
    @property
    def Comctl32() -> StringType: ...
    
    @staticmethod
    @property
    def Comdlg32() -> StringType: ...
    
    @staticmethod
    @property
    def Crypt32() -> StringType: ...
    
    @staticmethod
    @property
    def Fxassert() -> StringType: ...
    
    @staticmethod
    @property
    def Gdi32() -> StringType: ...
    
    @staticmethod
    @property
    def Gdiplus() -> StringType: ...
    
    @staticmethod
    @property
    def Hhctrl() -> StringType: ...
    
    @staticmethod
    @property
    def Imm32() -> StringType: ...
    
    @staticmethod
    @property
    def Kernel32() -> StringType: ...
    
    @staticmethod
    @property
    def Loadperf() -> StringType: ...
    
    @staticmethod
    @property
    def Mqrt() -> StringType: ...
    
    @staticmethod
    @property
    def Mscoree() -> StringType: ...
    
    @staticmethod
    @property
    def Msi() -> StringType: ...
    
    @staticmethod
    @property
    def Ntdll() -> StringType: ...
    
    @staticmethod
    @property
    def Ole32() -> StringType: ...
    
    @staticmethod
    @property
    def Oleacc() -> StringType: ...
    
    @staticmethod
    @property
    def Oleaut32() -> StringType: ...
    
    @staticmethod
    @property
    def Olepro32() -> StringType: ...
    
    @staticmethod
    @property
    def PerfCounter() -> StringType: ...
    
    @staticmethod
    @property
    def Powrprof() -> StringType: ...
    
    @staticmethod
    @property
    def Psapi() -> StringType: ...
    
    @staticmethod
    @property
    def ShCore() -> StringType: ...
    
    @staticmethod
    @property
    def Shell32() -> StringType: ...
    
    @staticmethod
    @property
    def Shlwapi() -> StringType: ...
    
    @staticmethod
    @property
    def User32() -> StringType: ...
    
    @staticmethod
    @property
    def Uxtheme() -> StringType: ...
    
    @staticmethod
    @property
    def Version() -> StringType: ...
    
    @staticmethod
    @property
    def Vsassert() -> StringType: ...
    
    @staticmethod
    @property
    def WinMM() -> StringType: ...
    
    @staticmethod
    @property
    def Winspool() -> StringType: ...
    
    @staticmethod
    @property
    def Wldp() -> StringType: ...
    
    @staticmethod
    @property
    def Wtsapi32() -> StringType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FieldAccessException(MemberAccessException, ISerializable, _Exception):
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


class FileStyleUriParser(UriParser):
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


class FlagsAttribute(Attribute, _Attribute):
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


class FormatException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FormattableString(ABC, ObjectType, IFormattable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ArgumentCount(self) -> IntType: ...
    
    @property
    def Format(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetArgument(self, index: IntType) -> ObjectType: ...
    
    def GetArguments(self) -> ArrayType[ObjectType]: ...
    
    @staticmethod
    def Invariant(formattable: FormattableString) -> StringType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, formatProvider: IFormatProvider) -> StringType: ...
    
    def get_ArgumentCount(self) -> IntType: ...
    
    def get_Format(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FtpStyleUriParser(UriParser):
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


class Func(Generic[TResult], MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> TResult: ...
    
    def Invoke(self) -> TResult: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Func(Generic[T, TResult], MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, arg: T, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> TResult: ...
    
    def Invoke(self, arg: T) -> TResult: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Func(Generic[T1, T2, TResult], MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, arg1: T1, arg2: T2, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> TResult: ...
    
    def Invoke(self, arg1: T1, arg2: T2) -> TResult: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Func(Generic[T1, T2, T3, TResult], MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> TResult: ...
    
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3) -> TResult: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Func(Generic[T1, T2, T3, T4, TResult], MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> TResult: ...
    
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4) -> TResult: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Func(Generic[T1, T2, T3, T4, T5, TResult], MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> TResult: ...
    
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5) -> TResult: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Func(Generic[T1, T2, T3, T4, T5, T6, TResult], MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> TResult: ...
    
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6) -> TResult: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Func(Generic[T1, T2, T3, T4, T5, T6, T7, TResult], MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> TResult: ...
    
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7) -> TResult: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Func(Generic[T1, T2, T3, T4, T5, T6, T7, T8, TResult], MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> TResult: ...
    
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8) -> TResult: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GC(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def MaxGeneration() -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def AddMemoryPressure(bytesAllocated: LongType) -> VoidType: ...
    
    @staticmethod
    def CancelFullGCNotification() -> VoidType: ...
    
    @staticmethod
    @overload
    def Collect(generation: IntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Collect() -> VoidType: ...
    
    @staticmethod
    @overload
    def Collect(generation: IntType, mode: GCCollectionMode) -> VoidType: ...
    
    @staticmethod
    @overload
    def Collect(generation: IntType, mode: GCCollectionMode, blocking: BooleanType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Collect(generation: IntType, mode: GCCollectionMode, blocking: BooleanType, compacting: BooleanType) -> VoidType: ...
    
    @staticmethod
    def CollectionCount(generation: IntType) -> IntType: ...
    
    @staticmethod
    def EndNoGCRegion() -> VoidType: ...
    
    @staticmethod
    def GetAllocatedBytesForCurrentThread() -> LongType: ...
    
    @staticmethod
    @overload
    def GetGeneration(wo: WeakReference) -> IntType: ...
    
    @staticmethod
    @overload
    def GetGeneration(obj: ObjectType) -> IntType: ...
    
    @staticmethod
    def GetTotalMemory(forceFullCollection: BooleanType) -> LongType: ...
    
    @staticmethod
    def KeepAlive(obj: ObjectType) -> VoidType: ...
    
    @staticmethod
    def ReRegisterForFinalize(obj: ObjectType) -> VoidType: ...
    
    @staticmethod
    def RegisterForFullGCNotification(maxGenerationThreshold: IntType, largeObjectHeapThreshold: IntType) -> VoidType: ...
    
    @staticmethod
    def RemoveMemoryPressure(bytesAllocated: LongType) -> VoidType: ...
    
    @staticmethod
    def SuppressFinalize(obj: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def TryStartNoGCRegion(totalSize: LongType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def TryStartNoGCRegion(totalSize: LongType, lohSize: LongType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def TryStartNoGCRegion(totalSize: LongType, disallowFullBlockingGC: BooleanType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def TryStartNoGCRegion(totalSize: LongType, lohSize: LongType, disallowFullBlockingGC: BooleanType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def WaitForFullGCApproach() -> GCNotificationStatus: ...
    
    @staticmethod
    @overload
    def WaitForFullGCApproach(millisecondsTimeout: IntType) -> GCNotificationStatus: ...
    
    @staticmethod
    @overload
    def WaitForFullGCComplete() -> GCNotificationStatus: ...
    
    @staticmethod
    @overload
    def WaitForFullGCComplete(millisecondsTimeout: IntType) -> GCNotificationStatus: ...
    
    @staticmethod
    def WaitForPendingFinalizers() -> VoidType: ...
    
    @staticmethod
    def get_MaxGeneration() -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Gen2GcCallback(CriticalFinalizerObject):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Register(callback: Func[ObjectType, BooleanType], targetObj: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GenericUriParser(UriParser):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, options: GenericUriParserOptions): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GopherStyleUriParser(UriParser):
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


class HResults(ABC, ObjectType):
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


class HResults(ABC, ObjectType):
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


class HResults(ABC, ObjectType):
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


class HttpStyleUriParser(UriParser):
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


class IPv4AddressHelper(ABC, ObjectType):
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


class IPv6AddressHelper(ABC, ObjectType):
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


class IndexOutOfRangeException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InsufficientExecutionStackException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InsufficientMemoryException(OutOfMemoryException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Internal(ABC, ObjectType):
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


class InvalidCastException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, message: StringType, errorCode: IntType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InvalidOperationException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InvalidProgramException(SystemException, ISerializable, _Exception):
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


class InvalidTimeZoneException(Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InvariantComparer(ObjectType, IComparer):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Compare(self, a: ObjectType, b: ObjectType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InvariantComparer(ObjectType, IComparer):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Compare(self, a: ObjectType, b: ObjectType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IriHelper(ABC, ObjectType):
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


class Lazy(Generic[T], ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, valueFactory: Func[T]): ...
    
    @overload
    def __init__(self, isThreadSafe: BooleanType): ...
    
    @overload
    def __init__(self, mode: LazyThreadSafetyMode): ...
    
    @overload
    def __init__(self, valueFactory: Func[T], isThreadSafe: BooleanType): ...
    
    @overload
    def __init__(self, valueFactory: Func[T], mode: LazyThreadSafetyMode): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsValueCreated(self) -> BooleanType: ...
    
    @property
    def Value(self) -> T: ...
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    def get_IsValueCreated(self) -> BooleanType: ...
    
    def get_Value(self) -> T: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LazyHelpers(ABC, ObjectType):
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


class LdapStyleUriParser(UriParser):
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


class LoaderOptimizationAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, value: ByteType): ...
    
    @overload
    def __init__(self, value: LoaderOptimization): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> LoaderOptimization: ...
    
    # ---------- Methods ---------- #
    
    def get_Value(self) -> LoaderOptimization: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LocalAppContext(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def IsSwitchEnabled(switchName: StringType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LocalAppContext(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def IsSwitchEnabled(switchName: StringType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LocalAppContext(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def IsSwitchEnabled(switchName: StringType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LocalAppContextSwitches(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def AllocateOverlappedOnDemand() -> BooleanType: ...
    
    @staticmethod
    @property
    def DisableEventLogRegistryKeysFiltering() -> BooleanType: ...
    
    @staticmethod
    @property
    def DisableTempFileCollectionDirectoryFeature() -> BooleanType: ...
    
    @staticmethod
    @property
    def DoNotCatchSerialStreamThreadExceptions() -> BooleanType: ...
    
    @staticmethod
    @property
    def DoNotUseNativeZipLibraryForDecompression() -> BooleanType: ...
    
    @staticmethod
    @property
    def DoNotValidateX509KeyStorageFlags() -> BooleanType: ...
    
    @staticmethod
    @property
    def DontCheckCertificateEKUs() -> BooleanType: ...
    
    @staticmethod
    @property
    def DontCheckCertificateRevocation() -> BooleanType: ...
    
    @staticmethod
    @property
    def DontEnableSchSendAuxRecord() -> BooleanType: ...
    
    @staticmethod
    @property
    def DontEnableSchUseStrongCrypto() -> BooleanType: ...
    
    @staticmethod
    @property
    def DontEnableStrictRFC3986ReservedCharacterSets() -> BooleanType: ...
    
    @staticmethod
    @property
    def DontEnableSystemDefaultTlsVersions() -> BooleanType: ...
    
    @staticmethod
    @property
    def DontEnableTls13() -> BooleanType: ...
    
    @staticmethod
    @property
    def DontEnableTlsAlerts() -> BooleanType: ...
    
    @staticmethod
    @property
    def DontKeepUnicodeBidiFormattingCharacters() -> BooleanType: ...
    
    @staticmethod
    @property
    def MemberDescriptorEqualsReturnsFalseIfEquivalent() -> BooleanType: ...
    
    @staticmethod
    @property
    def UseLegacyTimeoutCheck() -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_AllocateOverlappedOnDemand() -> BooleanType: ...
    
    @staticmethod
    def get_DisableEventLogRegistryKeysFiltering() -> BooleanType: ...
    
    @staticmethod
    def get_DisableTempFileCollectionDirectoryFeature() -> BooleanType: ...
    
    @staticmethod
    def get_DoNotCatchSerialStreamThreadExceptions() -> BooleanType: ...
    
    @staticmethod
    def get_DoNotUseNativeZipLibraryForDecompression() -> BooleanType: ...
    
    @staticmethod
    def get_DoNotValidateX509KeyStorageFlags() -> BooleanType: ...
    
    @staticmethod
    def get_DontCheckCertificateEKUs() -> BooleanType: ...
    
    @staticmethod
    def get_DontCheckCertificateRevocation() -> BooleanType: ...
    
    @staticmethod
    def get_DontEnableSchSendAuxRecord() -> BooleanType: ...
    
    @staticmethod
    def get_DontEnableSchUseStrongCrypto() -> BooleanType: ...
    
    @staticmethod
    def get_DontEnableStrictRFC3986ReservedCharacterSets() -> BooleanType: ...
    
    @staticmethod
    def get_DontEnableSystemDefaultTlsVersions() -> BooleanType: ...
    
    @staticmethod
    def get_DontEnableTls13() -> BooleanType: ...
    
    @staticmethod
    def get_DontEnableTlsAlerts() -> BooleanType: ...
    
    @staticmethod
    def get_DontKeepUnicodeBidiFormattingCharacters() -> BooleanType: ...
    
    @staticmethod
    def get_MemberDescriptorEqualsReturnsFalseIfEquivalent() -> BooleanType: ...
    
    @staticmethod
    def get_UseLegacyTimeoutCheck() -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LocalAppContextSwitches(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def AllowUserConfigFilesToLoadWhenSearchingForDatasetSerializationAllowedTypes() -> BooleanType: ...
    
    @staticmethod
    @property
    def AllowUserConfigFilesToLoadWhenSearchingForWellKnownSqlClientFactories() -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_AllowUserConfigFilesToLoadWhenSearchingForDatasetSerializationAllowedTypes() -> BooleanType: ...
    
    @staticmethod
    def get_AllowUserConfigFilesToLoadWhenSearchingForWellKnownSqlClientFactories() -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LocalAppContextSwitches(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def DontThrowOnInvalidSurrogatePairs() -> BooleanType: ...
    
    @staticmethod
    @property
    def EnableTimeSpanSerialization() -> BooleanType: ...
    
    @staticmethod
    @property
    def IgnoreEmptyKeySequences() -> BooleanType: ...
    
    @staticmethod
    @property
    def IgnoreKindInUtcTimeSerialization() -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_DontThrowOnInvalidSurrogatePairs() -> BooleanType: ...
    
    @staticmethod
    def get_EnableTimeSpanSerialization() -> BooleanType: ...
    
    @staticmethod
    def get_IgnoreEmptyKeySequences() -> BooleanType: ...
    
    @staticmethod
    def get_IgnoreKindInUtcTimeSerialization() -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LocalDataStore(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, mgr: LocalDataStoreMgr, InitialCapacity: IntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetData(self, slot: LocalDataStoreSlot) -> ObjectType: ...
    
    def SetData(self, slot: LocalDataStoreSlot, data: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LocalDataStoreElement(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, cookie: LongType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Cookie(self) -> LongType: ...
    
    @property
    def Value(self) -> ObjectType: ...
    
    @Value.setter
    def Value(self, value: ObjectType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Cookie(self) -> LongType: ...
    
    def get_Value(self) -> ObjectType: ...
    
    def set_Value(self, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LocalDataStoreHolder(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, store: LocalDataStore): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Store(self) -> LocalDataStore: ...
    
    # ---------- Methods ---------- #
    
    def get_Store(self) -> LocalDataStore: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LocalDataStoreMgr(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AllocateDataSlot(self) -> LocalDataStoreSlot: ...
    
    def AllocateNamedDataSlot(self, name: StringType) -> LocalDataStoreSlot: ...
    
    def CreateLocalDataStore(self) -> LocalDataStoreHolder: ...
    
    def DeleteLocalDataStore(self, store: LocalDataStore) -> VoidType: ...
    
    def FreeNamedDataSlot(self, name: StringType) -> VoidType: ...
    
    def GetNamedDataSlot(self, name: StringType) -> LocalDataStoreSlot: ...
    
    def ValidateSlot(self, slot: LocalDataStoreSlot) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LocalDataStoreSlot(ObjectType):
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


class MTAThreadAttribute(Attribute, _Attribute):
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


class MarshalByRefObject(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CreateObjRef(self, requestedType: TypeType) -> ObjRef: ...
    
    def GetLifetimeService(self) -> ObjectType: ...
    
    def InitializeLifetimeService(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MarvinHash(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def DefaultSeed() -> ULongType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def ComputeHash32(key: StringType, seed: ULongType) -> IntType: ...
    
    @staticmethod
    @overload
    def ComputeHash32(key: ArrayType[CharType], start: IntType, len: IntType, seed: ULongType) -> IntType: ...
    
    @staticmethod
    def GenerateSeed() -> ULongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Math(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def E() -> DoubleType: ...
    
    @staticmethod
    @property
    def PI() -> DoubleType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Abs(value: SByteType) -> SByteType: ...
    
    @staticmethod
    @overload
    def Abs(value: ShortType) -> ShortType: ...
    
    @staticmethod
    @overload
    def Abs(value: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def Abs(value: LongType) -> LongType: ...
    
    @staticmethod
    @overload
    def Abs(value: DecimalType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def Abs(value: FloatType) -> FloatType: ...
    
    @staticmethod
    @overload
    def Abs(value: DoubleType) -> DoubleType: ...
    
    @staticmethod
    def Acos(d: DoubleType) -> DoubleType: ...
    
    @staticmethod
    def Asin(d: DoubleType) -> DoubleType: ...
    
    @staticmethod
    def Atan(d: DoubleType) -> DoubleType: ...
    
    @staticmethod
    def Atan2(y: DoubleType, x: DoubleType) -> DoubleType: ...
    
    @staticmethod
    def BigMul(a: IntType, b: IntType) -> LongType: ...
    
    @staticmethod
    @overload
    def Ceiling(d: DecimalType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def Ceiling(a: DoubleType) -> DoubleType: ...
    
    @staticmethod
    def Cos(d: DoubleType) -> DoubleType: ...
    
    @staticmethod
    def Cosh(value: DoubleType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def DivRem(a: IntType, b: IntType, result: IntType) -> Tuple[IntType, IntType]: ...
    
    @staticmethod
    @overload
    def DivRem(a: LongType, b: LongType, result: LongType) -> Tuple[LongType, LongType]: ...
    
    @staticmethod
    def Exp(d: DoubleType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def Floor(d: DecimalType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def Floor(d: DoubleType) -> DoubleType: ...
    
    @staticmethod
    def IEEERemainder(x: DoubleType, y: DoubleType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def Log(a: DoubleType, newBase: DoubleType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def Log(d: DoubleType) -> DoubleType: ...
    
    @staticmethod
    def Log10(d: DoubleType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def Max(val1: SByteType, val2: SByteType) -> SByteType: ...
    
    @staticmethod
    @overload
    def Max(val1: ByteType, val2: ByteType) -> ByteType: ...
    
    @staticmethod
    @overload
    def Max(val1: ShortType, val2: ShortType) -> ShortType: ...
    
    @staticmethod
    @overload
    def Max(val1: UShortType, val2: UShortType) -> UShortType: ...
    
    @staticmethod
    @overload
    def Max(val1: IntType, val2: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def Max(val1: UIntType, val2: UIntType) -> UIntType: ...
    
    @staticmethod
    @overload
    def Max(val1: LongType, val2: LongType) -> LongType: ...
    
    @staticmethod
    @overload
    def Max(val1: ULongType, val2: ULongType) -> ULongType: ...
    
    @staticmethod
    @overload
    def Max(val1: FloatType, val2: FloatType) -> FloatType: ...
    
    @staticmethod
    @overload
    def Max(val1: DoubleType, val2: DoubleType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def Max(val1: DecimalType, val2: DecimalType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def Min(val1: SByteType, val2: SByteType) -> SByteType: ...
    
    @staticmethod
    @overload
    def Min(val1: ByteType, val2: ByteType) -> ByteType: ...
    
    @staticmethod
    @overload
    def Min(val1: ShortType, val2: ShortType) -> ShortType: ...
    
    @staticmethod
    @overload
    def Min(val1: UShortType, val2: UShortType) -> UShortType: ...
    
    @staticmethod
    @overload
    def Min(val1: IntType, val2: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def Min(val1: UIntType, val2: UIntType) -> UIntType: ...
    
    @staticmethod
    @overload
    def Min(val1: LongType, val2: LongType) -> LongType: ...
    
    @staticmethod
    @overload
    def Min(val1: ULongType, val2: ULongType) -> ULongType: ...
    
    @staticmethod
    @overload
    def Min(val1: FloatType, val2: FloatType) -> FloatType: ...
    
    @staticmethod
    @overload
    def Min(val1: DoubleType, val2: DoubleType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def Min(val1: DecimalType, val2: DecimalType) -> DecimalType: ...
    
    @staticmethod
    def Pow(x: DoubleType, y: DoubleType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def Round(value: DoubleType, digits: IntType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def Round(value: DoubleType, mode: MidpointRounding) -> DoubleType: ...
    
    @staticmethod
    @overload
    def Round(value: DoubleType, digits: IntType, mode: MidpointRounding) -> DoubleType: ...
    
    @staticmethod
    @overload
    def Round(d: DecimalType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def Round(d: DecimalType, decimals: IntType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def Round(d: DecimalType, mode: MidpointRounding) -> DecimalType: ...
    
    @staticmethod
    @overload
    def Round(d: DecimalType, decimals: IntType, mode: MidpointRounding) -> DecimalType: ...
    
    @staticmethod
    @overload
    def Round(a: DoubleType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def Sign(value: SByteType) -> IntType: ...
    
    @staticmethod
    @overload
    def Sign(value: ShortType) -> IntType: ...
    
    @staticmethod
    @overload
    def Sign(value: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def Sign(value: LongType) -> IntType: ...
    
    @staticmethod
    @overload
    def Sign(value: FloatType) -> IntType: ...
    
    @staticmethod
    @overload
    def Sign(value: DoubleType) -> IntType: ...
    
    @staticmethod
    @overload
    def Sign(value: DecimalType) -> IntType: ...
    
    @staticmethod
    def Sin(a: DoubleType) -> DoubleType: ...
    
    @staticmethod
    def Sinh(value: DoubleType) -> DoubleType: ...
    
    @staticmethod
    def Sqrt(d: DoubleType) -> DoubleType: ...
    
    @staticmethod
    def Tan(a: DoubleType) -> DoubleType: ...
    
    @staticmethod
    def Tanh(value: DoubleType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def Truncate(d: DecimalType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def Truncate(d: DoubleType) -> DoubleType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Mda(ABC, ObjectType):
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


class MemberAccessException(SystemException, ISerializable, _Exception):
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


class MethodAccessException(MemberAccessException, ISerializable, _Exception):
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


class MissingFieldException(MissingMemberException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    @overload
    def __init__(self, className: StringType, fieldName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Message(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Message(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MissingMemberException(MemberAccessException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    @overload
    def __init__(self, className: StringType, memberName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Message(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_Message(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MissingMethodException(MissingMemberException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    @overload
    def __init__(self, className: StringType, methodName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Message(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Message(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MulticastDelegate(ABC, Delegate, ICloneable, ISerializable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetInvocationList(self) -> ArrayType[Delegate]: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    @staticmethod
    def op_Equality(d1: MulticastDelegate, d2: MulticastDelegate) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(d1: MulticastDelegate, d2: MulticastDelegate) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MulticastNotSupportedException(SystemException, ISerializable, _Exception):
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


class NetPipeStyleUriParser(UriParser):
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


class NetTcpStyleUriParser(UriParser):
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


class NewsStyleUriParser(UriParser):
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


class NonSerializedAttribute(Attribute, _Attribute):
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


class NotFiniteNumberException(ArithmeticException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, offendingNumber: DoubleType): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, offendingNumber: DoubleType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, message: StringType, offendingNumber: DoubleType, innerException: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def OffendingNumber(self) -> DoubleType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_OffendingNumber(self) -> DoubleType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NotImplementedException(SystemException, ISerializable, _Exception):
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


class NotSupportedException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NullReferenceException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Nullable(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Compare(n1: NullableType[Nullable[T]], n2: NullableType[Nullable[T]]) -> IntType: ...
    
    @staticmethod
    @overload
    def Equals(n1: NullableType[Nullable[T]], n2: NullableType[Nullable[T]]) -> BooleanType: ...
    
    @staticmethod
    def GetUnderlyingType(nullableType: TypeType) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Number(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def FormatDecimal(value: DecimalType, format: StringType, info: NumberFormatInfo) -> StringType: ...
    
    @staticmethod
    def FormatDouble(value: DoubleType, format: StringType, info: NumberFormatInfo) -> StringType: ...
    
    @staticmethod
    def FormatInt32(value: IntType, format: StringType, info: NumberFormatInfo) -> StringType: ...
    
    @staticmethod
    def FormatInt64(value: LongType, format: StringType, info: NumberFormatInfo) -> StringType: ...
    
    @staticmethod
    def FormatSingle(value: FloatType, format: StringType, info: NumberFormatInfo) -> StringType: ...
    
    @staticmethod
    def FormatUInt32(value: UIntType, format: StringType, info: NumberFormatInfo) -> StringType: ...
    
    @staticmethod
    def FormatUInt64(value: ULongType, format: StringType, info: NumberFormatInfo) -> StringType: ...
    
    @staticmethod
    def NumberBufferToDecimal(number: ByteType, value: DecimalType) -> Tuple[BooleanType, DecimalType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Object:
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Equals(objA: ObjectType, objB: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetType(self) -> TypeType: ...
    
    @staticmethod
    def ReferenceEquals(objA: ObjectType, objB: ObjectType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ObjectDisposedException(InvalidOperationException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, objectName: StringType): ...
    
    @overload
    def __init__(self, objectName: StringType, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Message(self) -> StringType: ...
    
    @property
    def ObjectName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_Message(self) -> StringType: ...
    
    def get_ObjectName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ObsoleteAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, error: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsError(self) -> BooleanType: ...
    
    @property
    def Message(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_IsError(self) -> BooleanType: ...
    
    def get_Message(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OleAutBinder(DefaultBinder):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ChangeType(self, value: ObjectType, type: TypeType, cultureInfo: CultureInfo) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OperatingSystem(ObjectType, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, platform: PlatformID, version: Version): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Platform(self) -> PlatformID: ...
    
    @property
    def ServicePack(self) -> StringType: ...
    
    @property
    def Version(self) -> Version: ...
    
    @property
    def VersionString(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ObjectType: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Platform(self) -> PlatformID: ...
    
    def get_ServicePack(self) -> StringType: ...
    
    def get_Version(self) -> Version: ...
    
    def get_VersionString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OperationCanceledException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, token: CancellationToken): ...
    
    @overload
    def __init__(self, message: StringType, token: CancellationToken): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception, token: CancellationToken): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CancellationToken(self) -> CancellationToken: ...
    
    # ---------- Methods ---------- #
    
    def get_CancellationToken(self) -> CancellationToken: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OrdinalComparer(StringComparer, IComparer, IEqualityComparer, IComparer[StringType], IEqualityComparer[StringType], IWellKnownStringEqualityComparer):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Compare(self, x: StringType, y: StringType) -> IntType: ...
    
    @overload
    def Equals(self, x: StringType, y: StringType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def GetHashCode(self, obj: StringType) -> IntType: ...
    
    @overload
    def GetHashCode(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OrdinalRandomizedComparer(StringComparer, IComparer, IEqualityComparer, IComparer[StringType], IEqualityComparer[StringType], IWellKnownStringEqualityComparer):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Compare(self, x: StringType, y: StringType) -> IntType: ...
    
    @overload
    def Equals(self, x: StringType, y: StringType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def GetHashCode(self, obj: StringType) -> IntType: ...
    
    @overload
    def GetHashCode(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OutOfMemoryException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OverflowException(ArithmeticException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ParamArrayAttribute(Attribute, _Attribute):
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


class ParseNumbers(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def IntToString(l: IntType, radix: IntType, width: IntType, paddingChar: CharType, flags: IntType) -> StringType: ...
    
    @staticmethod
    def LongToString(l: LongType, radix: IntType, width: IntType, paddingChar: CharType, flags: IntType) -> StringType: ...
    
    @staticmethod
    @overload
    def StringToInt(s: StringType, radix: IntType, flags: IntType, currPos: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def StringToInt(s: StringType, radix: IntType, flags: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def StringToInt(s: StringType, radix: IntType, flags: IntType, currPos: IntType) -> Tuple[IntType, IntType]: ...
    
    @staticmethod
    @overload
    def StringToLong(s: StringType, radix: IntType, flags: IntType, currPos: IntType) -> LongType: ...
    
    @staticmethod
    @overload
    def StringToLong(s: StringType, radix: IntType, flags: IntType) -> LongType: ...
    
    @staticmethod
    @overload
    def StringToLong(s: StringType, radix: IntType, flags: IntType, currPos: IntType) -> Tuple[LongType, IntType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PinnableBufferCache(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, cacheName: StringType, numberOfElements: IntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AllocateBuffer(self) -> ArrayType[ByteType]: ...
    
    def FreeBuffer(self, buffer: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PinnableBufferCacheEventSource(EventSource, IDisposable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Log() -> PinnableBufferCacheEventSource: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AgePendingBuffersResults(self, cacheName: StringType, promotedToFreeListCount: IntType, heldBackCount: IntType) -> VoidType: ...
    
    def AllocateBuffer(self, cacheName: StringType, objectId: ULongType, objectHash: IntType, objectGen: IntType, freeCountAfter: IntType) -> VoidType: ...
    
    def AllocateBufferAged(self, cacheName: StringType, agedCount: IntType) -> VoidType: ...
    
    def AllocateBufferCreatingNewBuffers(self, cacheName: StringType, totalBuffsBefore: IntType, objectCount: IntType) -> VoidType: ...
    
    def AllocateBufferFreeListEmpty(self, cacheName: StringType, notGen2CountBefore: IntType) -> VoidType: ...
    
    def AllocateBufferFromNotGen2(self, cacheName: StringType, notGen2CountAfter: IntType) -> VoidType: ...
    
    def Create(self, cacheName: StringType) -> VoidType: ...
    
    def DebugMessage(self, message: StringType) -> VoidType: ...
    
    def DebugMessage1(self, message: StringType, value: LongType) -> VoidType: ...
    
    def DebugMessage2(self, message: StringType, value1: LongType, value2: LongType) -> VoidType: ...
    
    def DebugMessage3(self, message: StringType, value1: LongType, value2: LongType, value3: LongType) -> VoidType: ...
    
    def FreeBuffer(self, cacheName: StringType, objectId: ULongType, objectHash: IntType, freeCountBefore: IntType) -> VoidType: ...
    
    def FreeBufferNull(self, cacheName: StringType, freeCountBefore: IntType) -> VoidType: ...
    
    def FreeBufferStillTooYoung(self, cacheName: StringType, notGen2CountBefore: IntType) -> VoidType: ...
    
    def TrimCheck(self, cacheName: StringType, totalBuffs: IntType, neededMoreThanFreeList: BooleanType, deltaMSec: IntType) -> VoidType: ...
    
    def TrimExperiment(self, cacheName: StringType, totalBuffs: IntType, freeListCount: IntType, numTrimTrial: IntType) -> VoidType: ...
    
    def TrimFlush(self, cacheName: StringType, totalBuffs: IntType, freeListCount: IntType, notGen2CountBefore: IntType) -> VoidType: ...
    
    def TrimFree(self, cacheName: StringType, totalBuffs: IntType, freeListCount: IntType, toBeFreed: IntType) -> VoidType: ...
    
    def TrimFreeSizeOK(self, cacheName: StringType, totalBuffs: IntType, freeListCount: IntType) -> VoidType: ...
    
    def WalkFreeListResult(self, cacheName: StringType, freeListCount: IntType, gen0BuffersInFreeList: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PlatformNotSupportedException(NotSupportedException, ISerializable, _Exception):
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


class Predicate(Generic[T], MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, obj: T, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> BooleanType: ...
    
    def Invoke(self, obj: T) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Progress(Generic[T], ObjectType, IProgress[T]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, handler: Action[T]): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def add_ProgressChanged(self, value: EventHandler[T]) -> VoidType: ...
    
    def remove_ProgressChanged(self, value: EventHandler[T]) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    ProgressChanged: EventType[EventHandler[T]] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ProgressStatics(ABC, ObjectType):
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


class Random(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, Seed: IntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Next(self) -> IntType: ...
    
    @overload
    def Next(self, minValue: IntType, maxValue: IntType) -> IntType: ...
    
    @overload
    def Next(self, maxValue: IntType) -> IntType: ...
    
    def NextBytes(self, buffer: ArrayType[ByteType]) -> VoidType: ...
    
    def NextDouble(self) -> DoubleType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RankException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReflectionOnlyType(RuntimeType, ICustomAttributeProvider, _MemberInfo, _Type, IReflect, IReflectableType, ISerializable, ICloneable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def TypeHandle(self) -> RuntimeTypeHandle: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeHandle(self) -> RuntimeTypeHandle: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResId(ABC, ObjectType):
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


class ResolveEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, name: StringType): ...
    
    @overload
    def __init__(self, name: StringType, requestingAssembly: Assembly): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def RequestingAssembly(self) -> Assembly: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    def get_RequestingAssembly(self) -> Assembly: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResolveEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, args: ResolveEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> Assembly: ...
    
    def Invoke(self, sender: ObjectType, args: ResolveEventArgs) -> Assembly: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Resolver(ABC, ObjectType):
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


class RuntimeFieldInfoStub(ObjectType, IRuntimeFieldInfo):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, methodHandleValue: NIntType, keepalive: ObjectType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RuntimeMethodInfoStub(ObjectType, IRuntimeMethodInfo):
    # ---------- Fields ---------- #
    
    @property
    def m_value(self) -> RuntimeMethodHandleInternal: ...
    
    @m_value.setter
    def m_value(self, value: RuntimeMethodHandleInternal) -> None: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, methodHandleValue: RuntimeMethodHandleInternal, keepalive: ObjectType): ...
    
    @overload
    def __init__(self, methodHandleValue: NIntType, keepalive: ObjectType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RuntimeType(TypeInfo, ICustomAttributeProvider, _MemberInfo, _Type, IReflect, IReflectableType, ISerializable, ICloneable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Assembly(self) -> Assembly: ...
    
    @property
    def AssemblyQualifiedName(self) -> StringType: ...
    
    @property
    def BaseType(self) -> TypeType: ...
    
    @property
    def ContainsGenericParameters(self) -> BooleanType: ...
    
    @property
    def DeclaringMethod(self) -> MethodBase: ...
    
    @property
    def DeclaringType(self) -> TypeType: ...
    
    @property
    def FullName(self) -> StringType: ...
    
    @property
    def GUID(self) -> Guid: ...
    
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes: ...
    
    @property
    def GenericParameterPosition(self) -> IntType: ...
    
    @property
    def IsConstructedGenericType(self) -> BooleanType: ...
    
    @property
    def IsEnum(self) -> BooleanType: ...
    
    @property
    def IsGenericParameter(self) -> BooleanType: ...
    
    @property
    def IsGenericType(self) -> BooleanType: ...
    
    @property
    def IsGenericTypeDefinition(self) -> BooleanType: ...
    
    @property
    def IsSecurityCritical(self) -> BooleanType: ...
    
    @property
    def IsSecuritySafeCritical(self) -> BooleanType: ...
    
    @property
    def IsSecurityTransparent(self) -> BooleanType: ...
    
    @property
    def MemberType(self) -> MemberTypes: ...
    
    @property
    def MetadataToken(self) -> IntType: ...
    
    @property
    def Module(self) -> Module: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @property
    def ReflectedType(self) -> TypeType: ...
    
    @property
    def StructLayoutAttribute(self) -> StructLayoutAttribute: ...
    
    @property
    def TypeHandle(self) -> RuntimeTypeHandle: ...
    
    @property
    def UnderlyingSystemType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ObjectType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetArrayRank(self) -> IntType: ...
    
    @overload
    def GetConstructors(self, bindingAttr: BindingFlags) -> ArrayType[ConstructorInfo]: ...
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]: ...
    
    def GetDefaultMembers(self) -> ArrayType[MemberInfo]: ...
    
    def GetElementType(self) -> TypeType: ...
    
    def GetEnumName(self, value: ObjectType) -> StringType: ...
    
    def GetEnumNames(self) -> ArrayType[StringType]: ...
    
    def GetEnumUnderlyingType(self) -> TypeType: ...
    
    def GetEnumValues(self) -> Array: ...
    
    @overload
    def GetEvent(self, name: StringType, bindingAttr: BindingFlags) -> EventInfo: ...
    
    @overload
    def GetEvents(self, bindingAttr: BindingFlags) -> ArrayType[EventInfo]: ...
    
    @overload
    def GetField(self, name: StringType, bindingAttr: BindingFlags) -> FieldInfo: ...
    
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> ArrayType[FieldInfo]: ...
    
    def GetGenericArguments(self) -> ArrayType[TypeType]: ...
    
    def GetGenericParameterConstraints(self) -> ArrayType[TypeType]: ...
    
    def GetGenericTypeDefinition(self) -> TypeType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @overload
    def GetInterface(self, fullname: StringType, ignoreCase: BooleanType) -> TypeType: ...
    
    def GetInterfaceMap(self, ifaceType: TypeType) -> InterfaceMapping: ...
    
    def GetInterfaces(self) -> ArrayType[TypeType]: ...
    
    @overload
    def GetMember(self, name: StringType, type: MemberTypes, bindingAttr: BindingFlags) -> ArrayType[MemberInfo]: ...
    
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> ArrayType[MemberInfo]: ...
    
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> ArrayType[MethodInfo]: ...
    
    @overload
    def GetNestedType(self, fullname: StringType, bindingAttr: BindingFlags) -> TypeType: ...
    
    @overload
    def GetNestedTypes(self, bindingAttr: BindingFlags) -> ArrayType[TypeType]: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> ArrayType[PropertyInfo]: ...
    
    @overload
    def InvokeMember(self, name: StringType, bindingFlags: BindingFlags, binder: Binder, target: ObjectType, providedArgs: ArrayType[ObjectType], modifiers: ArrayType[ParameterModifier], culture: CultureInfo, namedParams: ArrayType[StringType]) -> ObjectType: ...
    
    @overload
    def IsAssignableFrom(self, typeInfo: TypeInfo) -> BooleanType: ...
    
    @overload
    def IsAssignableFrom(self, c: TypeType) -> BooleanType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def IsEnumDefined(self, value: ObjectType) -> BooleanType: ...
    
    def IsEquivalentTo(self, other: TypeType) -> BooleanType: ...
    
    def IsInstanceOfType(self, o: ObjectType) -> BooleanType: ...
    
    def IsSubclassOf(self, type: TypeType) -> BooleanType: ...
    
    @overload
    def MakeArrayType(self) -> TypeType: ...
    
    @overload
    def MakeArrayType(self, rank: IntType) -> TypeType: ...
    
    def MakeByRefType(self) -> TypeType: ...
    
    def MakeGenericType(self, instantiation: ArrayType[TypeType]) -> TypeType: ...
    
    def MakePointerType(self) -> TypeType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Assembly(self) -> Assembly: ...
    
    def get_AssemblyQualifiedName(self) -> StringType: ...
    
    def get_BaseType(self) -> TypeType: ...
    
    def get_ContainsGenericParameters(self) -> BooleanType: ...
    
    def get_DeclaringMethod(self) -> MethodBase: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_FullName(self) -> StringType: ...
    
    def get_GUID(self) -> Guid: ...
    
    def get_GenericParameterAttributes(self) -> GenericParameterAttributes: ...
    
    def get_GenericParameterPosition(self) -> IntType: ...
    
    def get_IsConstructedGenericType(self) -> BooleanType: ...
    
    def get_IsEnum(self) -> BooleanType: ...
    
    def get_IsGenericParameter(self) -> BooleanType: ...
    
    def get_IsGenericType(self) -> BooleanType: ...
    
    def get_IsGenericTypeDefinition(self) -> BooleanType: ...
    
    def get_IsSecurityCritical(self) -> BooleanType: ...
    
    def get_IsSecuritySafeCritical(self) -> BooleanType: ...
    
    def get_IsSecurityTransparent(self) -> BooleanType: ...
    
    def get_MemberType(self) -> MemberTypes: ...
    
    def get_MetadataToken(self) -> IntType: ...
    
    @overload
    def get_Module(self) -> Module: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Namespace(self) -> StringType: ...
    
    def get_ReflectedType(self) -> TypeType: ...
    
    def get_StructLayoutAttribute(self) -> StructLayoutAttribute: ...
    
    def get_TypeHandle(self) -> RuntimeTypeHandle: ...
    
    def get_UnderlyingSystemType(self) -> TypeType: ...
    
    @staticmethod
    def op_Equality(left: RuntimeType, right: RuntimeType) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: RuntimeType, right: RuntimeType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SR(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Resources() -> ResourceManager: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetObject(name: StringType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def GetString(name: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def GetString(name: StringType, args: ArrayType[ObjectType]) -> StringType: ...
    
    @staticmethod
    @overload
    def GetString(name: StringType, usedFallback: BooleanType) -> Tuple[StringType, BooleanType]: ...
    
    @staticmethod
    def get_Resources() -> ResourceManager: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SRCategoryAttribute(CategoryAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, category: StringType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SRDescriptionAttribute(DescriptionAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, description: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Description(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Description(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class STAThreadAttribute(Attribute, _Attribute):
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


class SZArrayHelper(ObjectType):
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


class SafeTypeNameParserHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SecurityUtils(ABC, ObjectType):
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


class SerializableAttribute(Attribute, _Attribute):
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


class SharedStatics(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Remoting_Identity_IDGuid() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetSharedStringMaker() -> StringMaker: ...
    
    @staticmethod
    def ReleaseSharedStringMaker(maker: StringMaker) -> Tuple[VoidType, StringMaker]: ...
    
    @staticmethod
    def get_Remoting_Identity_IDGuid() -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Signature(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, method: IRuntimeMethodInfo, arguments: ArrayType[RuntimeType], returnType: RuntimeType, callingConvention: CallingConventions): ...
    
    @overload
    def __init__(self, methodHandle: IRuntimeMethodInfo, declaringType: RuntimeType): ...
    
    @overload
    def __init__(self, fieldHandle: IRuntimeFieldInfo, declaringType: RuntimeType): ...
    
    @overload
    def __init__(self, pCorSig: VoidType, cCorSig: IntType, declaringType: RuntimeType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SizedReference(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, target: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ApproximateSize(self) -> LongType: ...
    
    @property
    def Target(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def get_ApproximateSize(self) -> LongType: ...
    
    def get_Target(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StackOverflowException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class String(ObjectType, IComparable, ICloneable, IConvertible, IEnumerable, IComparable[StringType], IEnumerable[CharType], IEquatable[StringType]):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Empty() -> StringType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, value: CharType): ...
    
    @overload
    def __init__(self, value: CharType, startIndex: IntType, length: IntType): ...
    
    @overload
    def __init__(self, value: SByteType): ...
    
    @overload
    def __init__(self, value: SByteType, startIndex: IntType, length: IntType): ...
    
    @overload
    def __init__(self, value: SByteType, startIndex: IntType, length: IntType, enc: Encoding): ...
    
    @overload
    def __init__(self, value: ArrayType[CharType], startIndex: IntType, length: IntType): ...
    
    @overload
    def __init__(self, value: ArrayType[CharType]): ...
    
    @overload
    def __init__(self, c: CharType, count: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Chars(self) -> CharType: ...
    
    @property
    def Length(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ObjectType: ...
    
    @staticmethod
    @overload
    def Compare(strA: StringType, strB: StringType) -> IntType: ...
    
    @staticmethod
    @overload
    def Compare(strA: StringType, strB: StringType, ignoreCase: BooleanType) -> IntType: ...
    
    @staticmethod
    @overload
    def Compare(strA: StringType, strB: StringType, comparisonType: StringComparison) -> IntType: ...
    
    @staticmethod
    @overload
    def Compare(strA: StringType, strB: StringType, culture: CultureInfo, options: CompareOptions) -> IntType: ...
    
    @staticmethod
    @overload
    def Compare(strA: StringType, strB: StringType, ignoreCase: BooleanType, culture: CultureInfo) -> IntType: ...
    
    @staticmethod
    @overload
    def Compare(strA: StringType, indexA: IntType, strB: StringType, indexB: IntType, length: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def Compare(strA: StringType, indexA: IntType, strB: StringType, indexB: IntType, length: IntType, ignoreCase: BooleanType) -> IntType: ...
    
    @staticmethod
    @overload
    def Compare(strA: StringType, indexA: IntType, strB: StringType, indexB: IntType, length: IntType, ignoreCase: BooleanType, culture: CultureInfo) -> IntType: ...
    
    @staticmethod
    @overload
    def Compare(strA: StringType, indexA: IntType, strB: StringType, indexB: IntType, length: IntType, culture: CultureInfo, options: CompareOptions) -> IntType: ...
    
    @staticmethod
    @overload
    def Compare(strA: StringType, indexA: IntType, strB: StringType, indexB: IntType, length: IntType, comparisonType: StringComparison) -> IntType: ...
    
    @staticmethod
    @overload
    def CompareOrdinal(strA: StringType, strB: StringType) -> IntType: ...
    
    @staticmethod
    @overload
    def CompareOrdinal(strA: StringType, indexA: IntType, strB: StringType, indexB: IntType, length: IntType) -> IntType: ...
    
    @overload
    def CompareTo(self, value: ObjectType) -> IntType: ...
    
    @overload
    def CompareTo(self, strB: StringType) -> IntType: ...
    
    @staticmethod
    @overload
    def Concat(arg0: ObjectType) -> StringType: ...
    
    @staticmethod
    @overload
    def Concat(arg0: ObjectType, arg1: ObjectType) -> StringType: ...
    
    @staticmethod
    @overload
    def Concat(arg0: ObjectType, arg1: ObjectType, arg2: ObjectType) -> StringType: ...
    
    @staticmethod
    @overload
    def Concat(arg0: ObjectType, arg1: ObjectType, arg2: ObjectType, arg3: ObjectType) -> StringType: ...
    
    @staticmethod
    @overload
    def Concat(args: ArrayType[ObjectType]) -> StringType: ...
    
    @staticmethod
    @overload
    def Concat(values: IEnumerable[StringType]) -> StringType: ...
    
    @staticmethod
    @overload
    def Concat(str0: StringType, str1: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def Concat(str0: StringType, str1: StringType, str2: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def Concat(str0: StringType, str1: StringType, str2: StringType, str3: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def Concat(values: ArrayType[StringType]) -> StringType: ...
    
    @staticmethod
    @overload
    def Concat(values: IEnumerable[T]) -> StringType: ...
    
    def Contains(self, value: StringType) -> BooleanType: ...
    
    @staticmethod
    def Copy(str: StringType) -> StringType: ...
    
    def CopyTo(self, sourceIndex: IntType, destination: ArrayType[CharType], destinationIndex: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def EndsWith(self, value: StringType) -> BooleanType: ...
    
    @overload
    def EndsWith(self, value: StringType, comparisonType: StringComparison) -> BooleanType: ...
    
    @overload
    def EndsWith(self, value: StringType, ignoreCase: BooleanType, culture: CultureInfo) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, value: StringType) -> BooleanType: ...
    
    @overload
    def Equals(self, value: StringType, comparisonType: StringComparison) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Equals(a: StringType, b: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Equals(a: StringType, b: StringType, comparisonType: StringComparison) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Format(format: StringType, arg0: ObjectType) -> StringType: ...
    
    @staticmethod
    @overload
    def Format(format: StringType, arg0: ObjectType, arg1: ObjectType) -> StringType: ...
    
    @staticmethod
    @overload
    def Format(format: StringType, arg0: ObjectType, arg1: ObjectType, arg2: ObjectType) -> StringType: ...
    
    @staticmethod
    @overload
    def Format(provider: IFormatProvider, format: StringType, arg0: ObjectType) -> StringType: ...
    
    @staticmethod
    @overload
    def Format(provider: IFormatProvider, format: StringType, arg0: ObjectType, arg1: ObjectType) -> StringType: ...
    
    @staticmethod
    @overload
    def Format(provider: IFormatProvider, format: StringType, arg0: ObjectType, arg1: ObjectType, arg2: ObjectType) -> StringType: ...
    
    @staticmethod
    @overload
    def Format(format: StringType, args: ArrayType[ObjectType]) -> StringType: ...
    
    @staticmethod
    @overload
    def Format(provider: IFormatProvider, format: StringType, args: ArrayType[ObjectType]) -> StringType: ...
    
    def GetEnumerator(self) -> CharEnumerator: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetTypeCode(self) -> TypeCode: ...
    
    @overload
    def IndexOf(self, value: CharType) -> IntType: ...
    
    @overload
    def IndexOf(self, value: CharType, startIndex: IntType) -> IntType: ...
    
    @overload
    def IndexOf(self, value: StringType) -> IntType: ...
    
    @overload
    def IndexOf(self, value: StringType, startIndex: IntType) -> IntType: ...
    
    @overload
    def IndexOf(self, value: StringType, startIndex: IntType, count: IntType) -> IntType: ...
    
    @overload
    def IndexOf(self, value: StringType, comparisonType: StringComparison) -> IntType: ...
    
    @overload
    def IndexOf(self, value: StringType, startIndex: IntType, comparisonType: StringComparison) -> IntType: ...
    
    @overload
    def IndexOf(self, value: StringType, startIndex: IntType, count: IntType, comparisonType: StringComparison) -> IntType: ...
    
    @overload
    def IndexOf(self, value: CharType, startIndex: IntType, count: IntType) -> IntType: ...
    
    @overload
    def IndexOfAny(self, anyOf: ArrayType[CharType]) -> IntType: ...
    
    @overload
    def IndexOfAny(self, anyOf: ArrayType[CharType], startIndex: IntType) -> IntType: ...
    
    @overload
    def IndexOfAny(self, anyOf: ArrayType[CharType], startIndex: IntType, count: IntType) -> IntType: ...
    
    def Insert(self, startIndex: IntType, value: StringType) -> StringType: ...
    
    @staticmethod
    def Intern(str: StringType) -> StringType: ...
    
    @staticmethod
    def IsInterned(str: StringType) -> StringType: ...
    
    @overload
    def IsNormalized(self) -> BooleanType: ...
    
    @overload
    def IsNormalized(self, normalizationForm: NormalizationForm) -> BooleanType: ...
    
    @staticmethod
    def IsNullOrEmpty(value: StringType) -> BooleanType: ...
    
    @staticmethod
    def IsNullOrWhiteSpace(value: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Join(separator: StringType, value: ArrayType[StringType]) -> StringType: ...
    
    @staticmethod
    @overload
    def Join(separator: StringType, values: ArrayType[ObjectType]) -> StringType: ...
    
    @staticmethod
    @overload
    def Join(separator: StringType, values: IEnumerable[StringType]) -> StringType: ...
    
    @staticmethod
    @overload
    def Join(separator: StringType, value: ArrayType[StringType], startIndex: IntType, count: IntType) -> StringType: ...
    
    @staticmethod
    @overload
    def Join(separator: StringType, values: IEnumerable[T]) -> StringType: ...
    
    @overload
    def LastIndexOf(self, value: CharType) -> IntType: ...
    
    @overload
    def LastIndexOf(self, value: CharType, startIndex: IntType) -> IntType: ...
    
    @overload
    def LastIndexOf(self, value: StringType) -> IntType: ...
    
    @overload
    def LastIndexOf(self, value: StringType, startIndex: IntType) -> IntType: ...
    
    @overload
    def LastIndexOf(self, value: StringType, startIndex: IntType, count: IntType) -> IntType: ...
    
    @overload
    def LastIndexOf(self, value: StringType, comparisonType: StringComparison) -> IntType: ...
    
    @overload
    def LastIndexOf(self, value: StringType, startIndex: IntType, comparisonType: StringComparison) -> IntType: ...
    
    @overload
    def LastIndexOf(self, value: StringType, startIndex: IntType, count: IntType, comparisonType: StringComparison) -> IntType: ...
    
    @overload
    def LastIndexOf(self, value: CharType, startIndex: IntType, count: IntType) -> IntType: ...
    
    @overload
    def LastIndexOfAny(self, anyOf: ArrayType[CharType]) -> IntType: ...
    
    @overload
    def LastIndexOfAny(self, anyOf: ArrayType[CharType], startIndex: IntType) -> IntType: ...
    
    @overload
    def LastIndexOfAny(self, anyOf: ArrayType[CharType], startIndex: IntType, count: IntType) -> IntType: ...
    
    @overload
    def Normalize(self) -> StringType: ...
    
    @overload
    def Normalize(self, normalizationForm: NormalizationForm) -> StringType: ...
    
    @overload
    def PadLeft(self, totalWidth: IntType) -> StringType: ...
    
    @overload
    def PadLeft(self, totalWidth: IntType, paddingChar: CharType) -> StringType: ...
    
    @overload
    def PadRight(self, totalWidth: IntType) -> StringType: ...
    
    @overload
    def PadRight(self, totalWidth: IntType, paddingChar: CharType) -> StringType: ...
    
    @overload
    def Remove(self, startIndex: IntType, count: IntType) -> StringType: ...
    
    @overload
    def Remove(self, startIndex: IntType) -> StringType: ...
    
    @overload
    def Replace(self, oldChar: CharType, newChar: CharType) -> StringType: ...
    
    @overload
    def Replace(self, oldValue: StringType, newValue: StringType) -> StringType: ...
    
    @overload
    def Split(self, separator: ArrayType[CharType]) -> ArrayType[StringType]: ...
    
    @overload
    def Split(self, separator: ArrayType[CharType], count: IntType) -> ArrayType[StringType]: ...
    
    @overload
    def Split(self, separator: ArrayType[CharType], options: StringSplitOptions) -> ArrayType[StringType]: ...
    
    @overload
    def Split(self, separator: ArrayType[CharType], count: IntType, options: StringSplitOptions) -> ArrayType[StringType]: ...
    
    @overload
    def Split(self, separator: ArrayType[StringType], options: StringSplitOptions) -> ArrayType[StringType]: ...
    
    @overload
    def Split(self, separator: ArrayType[StringType], count: IntType, options: StringSplitOptions) -> ArrayType[StringType]: ...
    
    @overload
    def StartsWith(self, value: StringType) -> BooleanType: ...
    
    @overload
    def StartsWith(self, value: StringType, comparisonType: StringComparison) -> BooleanType: ...
    
    @overload
    def StartsWith(self, value: StringType, ignoreCase: BooleanType, culture: CultureInfo) -> BooleanType: ...
    
    @overload
    def Substring(self, startIndex: IntType) -> StringType: ...
    
    @overload
    def Substring(self, startIndex: IntType, length: IntType) -> StringType: ...
    
    @overload
    def ToCharArray(self) -> ArrayType[CharType]: ...
    
    @overload
    def ToCharArray(self, startIndex: IntType, length: IntType) -> ArrayType[CharType]: ...
    
    @overload
    def ToLower(self) -> StringType: ...
    
    @overload
    def ToLower(self, culture: CultureInfo) -> StringType: ...
    
    def ToLowerInvariant(self) -> StringType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, provider: IFormatProvider) -> StringType: ...
    
    @overload
    def ToUpper(self) -> StringType: ...
    
    @overload
    def ToUpper(self, culture: CultureInfo) -> StringType: ...
    
    def ToUpperInvariant(self) -> StringType: ...
    
    @overload
    def Trim(self, trimChars: ArrayType[CharType]) -> StringType: ...
    
    @overload
    def Trim(self) -> StringType: ...
    
    def TrimEnd(self, trimChars: ArrayType[CharType]) -> StringType: ...
    
    def TrimStart(self, trimChars: ArrayType[CharType]) -> StringType: ...
    
    def get_Chars(self, index: IntType) -> CharType: ...
    
    def get_Length(self) -> IntType: ...
    
    @staticmethod
    def op_Equality(a: StringType, b: StringType) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(a: StringType, b: StringType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringComparer(ABC, ObjectType, IComparer, IEqualityComparer, IComparer[StringType], IEqualityComparer[StringType]):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def CurrentCulture() -> StringComparer: ...
    
    @staticmethod
    @property
    def CurrentCultureIgnoreCase() -> StringComparer: ...
    
    @staticmethod
    @property
    def InvariantCulture() -> StringComparer: ...
    
    @staticmethod
    @property
    def InvariantCultureIgnoreCase() -> StringComparer: ...
    
    @staticmethod
    @property
    def Ordinal() -> StringComparer: ...
    
    @staticmethod
    @property
    def OrdinalIgnoreCase() -> StringComparer: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Compare(self, x: ObjectType, y: ObjectType) -> IntType: ...
    
    @overload
    def Compare(self, x: StringType, y: StringType) -> IntType: ...
    
    @staticmethod
    def Create(culture: CultureInfo, ignoreCase: BooleanType) -> StringComparer: ...
    
    @overload
    def Equals(self, x: ObjectType, y: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, x: StringType, y: StringType) -> BooleanType: ...
    
    @overload
    def GetHashCode(self, obj: ObjectType) -> IntType: ...
    
    @overload
    def GetHashCode(self, obj: StringType) -> IntType: ...
    
    @staticmethod
    def get_CurrentCulture() -> StringComparer: ...
    
    @staticmethod
    def get_CurrentCultureIgnoreCase() -> StringComparer: ...
    
    @staticmethod
    def get_InvariantCulture() -> StringComparer: ...
    
    @staticmethod
    def get_InvariantCultureIgnoreCase() -> StringComparer: ...
    
    @staticmethod
    def get_Ordinal() -> StringComparer: ...
    
    @staticmethod
    def get_OrdinalIgnoreCase() -> StringComparer: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringNormalizationExtensions(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def IsNormalized(value: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsNormalized(value: StringType, normalizationForm: NormalizationForm) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Normalize(value: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def Normalize(value: StringType, normalizationForm: NormalizationForm) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemException(Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class System_LazyDebugView(Generic[T], ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, lazy: Lazy[T]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsValueCreated(self) -> BooleanType: ...
    
    @property
    def IsValueFaulted(self) -> BooleanType: ...
    
    @property
    def Mode(self) -> LazyThreadSafetyMode: ...
    
    @property
    def Value(self) -> T: ...
    
    # ---------- Methods ---------- #
    
    def get_IsValueCreated(self) -> BooleanType: ...
    
    def get_IsValueFaulted(self) -> BooleanType: ...
    
    def get_Mode(self) -> LazyThreadSafetyMode: ...
    
    def get_Value(self) -> T: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ThreadStaticAttribute(Attribute, _Attribute):
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


class ThrowHelper(ABC, ObjectType):
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


class ThrowHelper(ABC, ObjectType):
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


class TimeZone(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def CurrentTimeZone() -> TimeZone: ...
    
    @property
    def DaylightName(self) -> StringType: ...
    
    @property
    def StandardName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetDaylightChanges(self, year: IntType) -> DaylightTime: ...
    
    def GetUtcOffset(self, time: DateTime) -> TimeSpan: ...
    
    @overload
    def IsDaylightSavingTime(self, time: DateTime) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsDaylightSavingTime(time: DateTime, daylightTimes: DaylightTime) -> BooleanType: ...
    
    def ToLocalTime(self, time: DateTime) -> DateTime: ...
    
    def ToUniversalTime(self, time: DateTime) -> DateTime: ...
    
    @staticmethod
    def get_CurrentTimeZone() -> TimeZone: ...
    
    def get_DaylightName(self) -> StringType: ...
    
    def get_StandardName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TimeZoneInfo(ObjectType, IEquatable[TimeZoneInfo], ISerializable, IDeserializationCallback):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BaseUtcOffset(self) -> TimeSpan: ...
    
    @property
    def DaylightName(self) -> StringType: ...
    
    @property
    def DisplayName(self) -> StringType: ...
    
    @property
    def Id(self) -> StringType: ...
    
    @staticmethod
    @property
    def Local() -> TimeZoneInfo: ...
    
    @property
    def StandardName(self) -> StringType: ...
    
    @property
    def SupportsDaylightSavingTime(self) -> BooleanType: ...
    
    @staticmethod
    @property
    def Utc() -> TimeZoneInfo: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def ClearCachedData() -> VoidType: ...
    
    @staticmethod
    @overload
    def ConvertTime(dateTimeOffset: DateTimeOffset, destinationTimeZone: TimeZoneInfo) -> DateTimeOffset: ...
    
    @staticmethod
    @overload
    def ConvertTime(dateTime: DateTime, destinationTimeZone: TimeZoneInfo) -> DateTime: ...
    
    @staticmethod
    @overload
    def ConvertTime(dateTime: DateTime, sourceTimeZone: TimeZoneInfo, destinationTimeZone: TimeZoneInfo) -> DateTime: ...
    
    @staticmethod
    @overload
    def ConvertTimeBySystemTimeZoneId(dateTimeOffset: DateTimeOffset, destinationTimeZoneId: StringType) -> DateTimeOffset: ...
    
    @staticmethod
    @overload
    def ConvertTimeBySystemTimeZoneId(dateTime: DateTime, destinationTimeZoneId: StringType) -> DateTime: ...
    
    @staticmethod
    @overload
    def ConvertTimeBySystemTimeZoneId(dateTime: DateTime, sourceTimeZoneId: StringType, destinationTimeZoneId: StringType) -> DateTime: ...
    
    @staticmethod
    def ConvertTimeFromUtc(dateTime: DateTime, destinationTimeZone: TimeZoneInfo) -> DateTime: ...
    
    @staticmethod
    @overload
    def ConvertTimeToUtc(dateTime: DateTime) -> DateTime: ...
    
    @staticmethod
    @overload
    def ConvertTimeToUtc(dateTime: DateTime, sourceTimeZone: TimeZoneInfo) -> DateTime: ...
    
    @staticmethod
    @overload
    def CreateCustomTimeZone(id: StringType, baseUtcOffset: TimeSpan, displayName: StringType, standardDisplayName: StringType) -> TimeZoneInfo: ...
    
    @staticmethod
    @overload
    def CreateCustomTimeZone(id: StringType, baseUtcOffset: TimeSpan, displayName: StringType, standardDisplayName: StringType, daylightDisplayName: StringType, adjustmentRules: ArrayType[AdjustmentRule]) -> TimeZoneInfo: ...
    
    @staticmethod
    @overload
    def CreateCustomTimeZone(id: StringType, baseUtcOffset: TimeSpan, displayName: StringType, standardDisplayName: StringType, daylightDisplayName: StringType, adjustmentRules: ArrayType[AdjustmentRule], disableDaylightSavingTime: BooleanType) -> TimeZoneInfo: ...
    
    @overload
    def Equals(self, other: TimeZoneInfo) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @staticmethod
    def FindSystemTimeZoneById(id: StringType) -> TimeZoneInfo: ...
    
    @staticmethod
    def FromSerializedString(source: StringType) -> TimeZoneInfo: ...
    
    def GetAdjustmentRules(self) -> ArrayType[AdjustmentRule]: ...
    
    @overload
    def GetAmbiguousTimeOffsets(self, dateTimeOffset: DateTimeOffset) -> ArrayType[TimeSpan]: ...
    
    @overload
    def GetAmbiguousTimeOffsets(self, dateTime: DateTime) -> ArrayType[TimeSpan]: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    def GetSystemTimeZones() -> ReadOnlyCollection[TimeZoneInfo]: ...
    
    @overload
    def GetUtcOffset(self, dateTimeOffset: DateTimeOffset) -> TimeSpan: ...
    
    @overload
    def GetUtcOffset(self, dateTime: DateTime) -> TimeSpan: ...
    
    def HasSameRules(self, other: TimeZoneInfo) -> BooleanType: ...
    
    @overload
    def IsAmbiguousTime(self, dateTimeOffset: DateTimeOffset) -> BooleanType: ...
    
    @overload
    def IsAmbiguousTime(self, dateTime: DateTime) -> BooleanType: ...
    
    @overload
    def IsDaylightSavingTime(self, dateTimeOffset: DateTimeOffset) -> BooleanType: ...
    
    @overload
    def IsDaylightSavingTime(self, dateTime: DateTime) -> BooleanType: ...
    
    def IsInvalidTime(self, dateTime: DateTime) -> BooleanType: ...
    
    def ToSerializedString(self) -> StringType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_BaseUtcOffset(self) -> TimeSpan: ...
    
    def get_DaylightName(self) -> StringType: ...
    
    def get_DisplayName(self) -> StringType: ...
    
    def get_Id(self) -> StringType: ...
    
    @staticmethod
    def get_Local() -> TimeZoneInfo: ...
    
    def get_StandardName(self) -> StringType: ...
    
    def get_SupportsDaylightSavingTime(self) -> BooleanType: ...
    
    @staticmethod
    def get_Utc() -> TimeZoneInfo: ...
    
    # No Events
    
    
    # ---------- Sub Classes ---------- #
    
    class AdjustmentRule(ObjectType, IEquatable[AdjustmentRule], ISerializable, IDeserializationCallback):
        # No Fields
        
        # No Constructors
        
        # ---------- Properties ---------- #
        
        @property
        def DateEnd(self) -> DateTime: ...
        
        @property
        def DateStart(self) -> DateTime: ...
        
        @property
        def DaylightDelta(self) -> TimeSpan: ...
        
        @property
        def DaylightTransitionEnd(self) -> TransitionTime: ...
        
        @property
        def DaylightTransitionStart(self) -> TransitionTime: ...
        
        # ---------- Methods ---------- #
        
        @staticmethod
        def CreateAdjustmentRule(dateStart: DateTime, dateEnd: DateTime, daylightDelta: TimeSpan, daylightTransitionStart: TransitionTime, daylightTransitionEnd: TransitionTime) -> AdjustmentRule: ...
        
        @overload
        def Equals(self, other: AdjustmentRule) -> BooleanType: ...
        
        def GetHashCode(self) -> IntType: ...
        
        def get_DateEnd(self) -> DateTime: ...
        
        def get_DateStart(self) -> DateTime: ...
        
        def get_DaylightDelta(self) -> TimeSpan: ...
        
        def get_DaylightTransitionEnd(self) -> TransitionTime: ...
        
        def get_DaylightTransitionStart(self) -> TransitionTime: ...
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # ---------- Sub Structs ---------- #
    
    class TransitionTime(ValueType, IEquatable[TransitionTime], ISerializable, IDeserializationCallback):
        # No Fields
        
        # No Constructors
        
        # ---------- Properties ---------- #
        
        @property
        def Day(self) -> IntType: ...
        
        @property
        def DayOfWeek(self) -> DayOfWeek: ...
        
        @property
        def IsFixedDateRule(self) -> BooleanType: ...
        
        @property
        def Month(self) -> IntType: ...
        
        @property
        def TimeOfDay(self) -> DateTime: ...
        
        @property
        def Week(self) -> IntType: ...
        
        # ---------- Methods ---------- #
        
        @staticmethod
        def CreateFixedDateRule(timeOfDay: DateTime, month: IntType, day: IntType) -> TransitionTime: ...
        
        @staticmethod
        def CreateFloatingDateRule(timeOfDay: DateTime, month: IntType, week: IntType, dayOfWeek: DayOfWeek) -> TransitionTime: ...
        
        @overload
        def Equals(self, obj: ObjectType) -> BooleanType: ...
        
        @overload
        def Equals(self, other: TransitionTime) -> BooleanType: ...
        
        def GetHashCode(self) -> IntType: ...
        
        def get_Day(self) -> IntType: ...
        
        def get_DayOfWeek(self) -> DayOfWeek: ...
        
        def get_IsFixedDateRule(self) -> BooleanType: ...
        
        def get_Month(self) -> IntType: ...
        
        def get_TimeOfDay(self) -> DateTime: ...
        
        def get_Week(self) -> IntType: ...
        
        @staticmethod
        def op_Equality(t1: TransitionTime, t2: TransitionTime) -> BooleanType: ...
        
        @staticmethod
        def op_Inequality(t1: TransitionTime, t2: TransitionTime) -> BooleanType: ...
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Interfaces
    
    # No Sub Enums


class TimeZoneNotFoundException(Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TimeoutException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Tuple(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Create(item1: T1, item2: T2) -> Tuple[T1, T2]: ...
    
    @staticmethod
    @overload
    def Create(item1: T1, item2: T2, item3: T3) -> Tuple[T1, T2, T3]: ...
    
    @staticmethod
    @overload
    def Create(item1: T1) -> Tuple[T1]: ...
    
    @staticmethod
    @overload
    def Create(item1: T1, item2: T2, item3: T3, item4: T4) -> Tuple[T1, T2, T3, T4]: ...
    
    @staticmethod
    @overload
    def Create(item1: T1, item2: T2, item3: T3, item4: T4, item5: T5) -> Tuple[T1, T2, T3, T4, T5]: ...
    
    @staticmethod
    @overload
    def Create(item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6) -> Tuple[T1, T2, T3, T4, T5, T6]: ...
    
    @staticmethod
    @overload
    def Create(item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7) -> Tuple[T1, T2, T3, T4, T5, T6, T7]: ...
    
    @staticmethod
    @overload
    def Create(item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7, item8: T8) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8]]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Tuple(Generic[T1], ObjectType, IStructuralEquatable, IStructuralComparable, IComparable, ITupleInternal, ITuple):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, item1: T1): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item1(self) -> T1: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Item1(self) -> T1: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Tuple(Generic[T1, T2], ObjectType, IStructuralEquatable, IStructuralComparable, IComparable, ITupleInternal, ITuple):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, item1: T1, item2: T2): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item1(self) -> T1: ...
    
    @property
    def Item2(self) -> T2: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Item1(self) -> T1: ...
    
    def get_Item2(self) -> T2: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Tuple(Generic[T1, T2, T3], ObjectType, IStructuralEquatable, IStructuralComparable, IComparable, ITupleInternal, ITuple):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, item1: T1, item2: T2, item3: T3): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item1(self) -> T1: ...
    
    @property
    def Item2(self) -> T2: ...
    
    @property
    def Item3(self) -> T3: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Item1(self) -> T1: ...
    
    def get_Item2(self) -> T2: ...
    
    def get_Item3(self) -> T3: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Tuple(Generic[T1, T2, T3, T4], ObjectType, IStructuralEquatable, IStructuralComparable, IComparable, ITupleInternal, ITuple):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, item1: T1, item2: T2, item3: T3, item4: T4): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item1(self) -> T1: ...
    
    @property
    def Item2(self) -> T2: ...
    
    @property
    def Item3(self) -> T3: ...
    
    @property
    def Item4(self) -> T4: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Item1(self) -> T1: ...
    
    def get_Item2(self) -> T2: ...
    
    def get_Item3(self) -> T3: ...
    
    def get_Item4(self) -> T4: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Tuple(Generic[T1, T2, T3, T4, T5], ObjectType, IStructuralEquatable, IStructuralComparable, IComparable, ITupleInternal, ITuple):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item1(self) -> T1: ...
    
    @property
    def Item2(self) -> T2: ...
    
    @property
    def Item3(self) -> T3: ...
    
    @property
    def Item4(self) -> T4: ...
    
    @property
    def Item5(self) -> T5: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Item1(self) -> T1: ...
    
    def get_Item2(self) -> T2: ...
    
    def get_Item3(self) -> T3: ...
    
    def get_Item4(self) -> T4: ...
    
    def get_Item5(self) -> T5: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Tuple(Generic[T1, T2, T3, T4, T5, T6], ObjectType, IStructuralEquatable, IStructuralComparable, IComparable, ITupleInternal, ITuple):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item1(self) -> T1: ...
    
    @property
    def Item2(self) -> T2: ...
    
    @property
    def Item3(self) -> T3: ...
    
    @property
    def Item4(self) -> T4: ...
    
    @property
    def Item5(self) -> T5: ...
    
    @property
    def Item6(self) -> T6: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Item1(self) -> T1: ...
    
    def get_Item2(self) -> T2: ...
    
    def get_Item3(self) -> T3: ...
    
    def get_Item4(self) -> T4: ...
    
    def get_Item5(self) -> T5: ...
    
    def get_Item6(self) -> T6: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Tuple(Generic[T1, T2, T3, T4, T5, T6, T7], ObjectType, IStructuralEquatable, IStructuralComparable, IComparable, ITupleInternal, ITuple):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item1(self) -> T1: ...
    
    @property
    def Item2(self) -> T2: ...
    
    @property
    def Item3(self) -> T3: ...
    
    @property
    def Item4(self) -> T4: ...
    
    @property
    def Item5(self) -> T5: ...
    
    @property
    def Item6(self) -> T6: ...
    
    @property
    def Item7(self) -> T7: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Item1(self) -> T1: ...
    
    def get_Item2(self) -> T2: ...
    
    def get_Item3(self) -> T3: ...
    
    def get_Item4(self) -> T4: ...
    
    def get_Item5(self) -> T5: ...
    
    def get_Item6(self) -> T6: ...
    
    def get_Item7(self) -> T7: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Tuple(Generic[T1, T2, T3, T4, T5, T6, T7, TRest], ObjectType, IStructuralEquatable, IStructuralComparable, IComparable, ITupleInternal, ITuple):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7, rest: TRest): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item1(self) -> T1: ...
    
    @property
    def Item2(self) -> T2: ...
    
    @property
    def Item3(self) -> T3: ...
    
    @property
    def Item4(self) -> T4: ...
    
    @property
    def Item5(self) -> T5: ...
    
    @property
    def Item6(self) -> T6: ...
    
    @property
    def Item7(self) -> T7: ...
    
    @property
    def Rest(self) -> TRest: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Item1(self) -> T1: ...
    
    def get_Item2(self) -> T2: ...
    
    def get_Item3(self) -> T3: ...
    
    def get_Item4(self) -> T4: ...
    
    def get_Item5(self) -> T5: ...
    
    def get_Item6(self) -> T6: ...
    
    def get_Item7(self) -> T7: ...
    
    def get_Rest(self) -> TRest: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TupleExtensions(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Deconstruct(value: Tuple[T1], item1: T1) -> Tuple[VoidType, T1]: ...
    
    @staticmethod
    @overload
    def Deconstruct(value: Tuple[T1, T2], item1: T1, item2: T2) -> Tuple[VoidType, T1, T2]: ...
    
    @staticmethod
    @overload
    def Deconstruct(value: Tuple[T1, T2, T3], item1: T1, item2: T2, item3: T3) -> Tuple[VoidType, T1, T2, T3]: ...
    
    @staticmethod
    @overload
    def Deconstruct(value: Tuple[T1, T2, T3, T4], item1: T1, item2: T2, item3: T3, item4: T4) -> Tuple[VoidType, T1, T2, T3, T4]: ...
    
    @staticmethod
    @overload
    def Deconstruct(value: Tuple[T1, T2, T3, T4, T5], item1: T1, item2: T2, item3: T3, item4: T4, item5: T5) -> Tuple[VoidType, T1, T2, T3, T4, T5]: ...
    
    @staticmethod
    @overload
    def Deconstruct(value: Tuple[T1, T2, T3, T4, T5, T6], item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6) -> Tuple[VoidType, T1, T2, T3, T4, T5, T6]: ...
    
    @staticmethod
    @overload
    def Deconstruct(value: Tuple[T1, T2, T3, T4, T5, T6, T7], item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7) -> Tuple[VoidType, T1, T2, T3, T4, T5, T6, T7]: ...
    
    @staticmethod
    @overload
    def Deconstruct(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8]], item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7, item8: T8) -> Tuple[VoidType, T1, T2, T3, T4, T5, T6, T7, T8]: ...
    
    @staticmethod
    @overload
    def Deconstruct(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9]], item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7, item8: T8, item9: T9) -> Tuple[VoidType, T1, T2, T3, T4, T5, T6, T7, T8, T9]: ...
    
    @staticmethod
    @overload
    def Deconstruct(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10]], item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7, item8: T8, item9: T9, item10: T10) -> Tuple[VoidType, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10]: ...
    
    @staticmethod
    @overload
    def Deconstruct(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11]], item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7, item8: T8, item9: T9, item10: T10, item11: T11) -> Tuple[VoidType, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11]: ...
    
    @staticmethod
    @overload
    def Deconstruct(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12]], item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7, item8: T8, item9: T9, item10: T10, item11: T11, item12: T12) -> Tuple[VoidType, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12]: ...
    
    @staticmethod
    @overload
    def Deconstruct(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13]], item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7, item8: T8, item9: T9, item10: T10, item11: T11, item12: T12, item13: T13) -> Tuple[VoidType, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13]: ...
    
    @staticmethod
    @overload
    def Deconstruct(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14]], item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7, item8: T8, item9: T9, item10: T10, item11: T11, item12: T12, item13: T13, item14: T14) -> Tuple[VoidType, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14]: ...
    
    @staticmethod
    @overload
    def Deconstruct(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15]]], item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7, item8: T8, item9: T9, item10: T10, item11: T11, item12: T12, item13: T13, item14: T14, item15: T15) -> Tuple[VoidType, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15]: ...
    
    @staticmethod
    @overload
    def Deconstruct(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16]]], item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7, item8: T8, item9: T9, item10: T10, item11: T11, item12: T12, item13: T13, item14: T14, item15: T15, item16: T16) -> Tuple[VoidType, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16]: ...
    
    @staticmethod
    @overload
    def Deconstruct(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17]]], item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7, item8: T8, item9: T9, item10: T10, item11: T11, item12: T12, item13: T13, item14: T14, item15: T15, item16: T16, item17: T17) -> Tuple[VoidType, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17]: ...
    
    @staticmethod
    @overload
    def Deconstruct(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18]]], item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7, item8: T8, item9: T9, item10: T10, item11: T11, item12: T12, item13: T13, item14: T14, item15: T15, item16: T16, item17: T17, item18: T18) -> Tuple[VoidType, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18]: ...
    
    @staticmethod
    @overload
    def Deconstruct(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19]]], item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7, item8: T8, item9: T9, item10: T10, item11: T11, item12: T12, item13: T13, item14: T14, item15: T15, item16: T16, item17: T17, item18: T18, item19: T19) -> Tuple[VoidType, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19]: ...
    
    @staticmethod
    @overload
    def Deconstruct(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19, T20]]], item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7, item8: T8, item9: T9, item10: T10, item11: T11, item12: T12, item13: T13, item14: T14, item15: T15, item16: T16, item17: T17, item18: T18, item19: T19, item20: T20) -> Tuple[VoidType, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20]: ...
    
    @staticmethod
    @overload
    def Deconstruct(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19, T20, T21]]], item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7, item8: T8, item9: T9, item10: T10, item11: T11, item12: T12, item13: T13, item14: T14, item15: T15, item16: T16, item17: T17, item18: T18, item19: T19, item20: T20, item21: T21) -> Tuple[VoidType, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, T21]: ...
    
    @staticmethod
    @overload
    def ToTuple(value: ValueTuple[T1]) -> Tuple[T1]: ...
    
    @staticmethod
    @overload
    def ToTuple(value: ValueTuple[T1, T2]) -> Tuple[T1, T2]: ...
    
    @staticmethod
    @overload
    def ToTuple(value: ValueTuple[T1, T2, T3]) -> Tuple[T1, T2, T3]: ...
    
    @staticmethod
    @overload
    def ToTuple(value: ValueTuple[T1, T2, T3, T4]) -> Tuple[T1, T2, T3, T4]: ...
    
    @staticmethod
    @overload
    def ToTuple(value: ValueTuple[T1, T2, T3, T4, T5]) -> Tuple[T1, T2, T3, T4, T5]: ...
    
    @staticmethod
    @overload
    def ToTuple(value: ValueTuple[T1, T2, T3, T4, T5, T6]) -> Tuple[T1, T2, T3, T4, T5, T6]: ...
    
    @staticmethod
    @overload
    def ToTuple(value: ValueTuple[T1, T2, T3, T4, T5, T6, T7]) -> Tuple[T1, T2, T3, T4, T5, T6, T7]: ...
    
    @staticmethod
    @overload
    def ToTuple(value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8]]: ...
    
    @staticmethod
    @overload
    def ToTuple(value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9]]: ...
    
    @staticmethod
    @overload
    def ToTuple(value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10]]: ...
    
    @staticmethod
    @overload
    def ToTuple(value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11]]: ...
    
    @staticmethod
    @overload
    def ToTuple(value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12]]: ...
    
    @staticmethod
    @overload
    def ToTuple(value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13]]: ...
    
    @staticmethod
    @overload
    def ToTuple(value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14]]: ...
    
    @staticmethod
    @overload
    def ToTuple(value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15]]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15]]]: ...
    
    @staticmethod
    @overload
    def ToTuple(value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16]]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16]]]: ...
    
    @staticmethod
    @overload
    def ToTuple(value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17]]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17]]]: ...
    
    @staticmethod
    @overload
    def ToTuple(value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17, T18]]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18]]]: ...
    
    @staticmethod
    @overload
    def ToTuple(value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17, T18, T19]]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19]]]: ...
    
    @staticmethod
    @overload
    def ToTuple(value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17, T18, T19, T20]]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19, T20]]]: ...
    
    @staticmethod
    @overload
    def ToTuple(value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17, T18, T19, T20, T21]]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19, T20, T21]]]: ...
    
    @staticmethod
    @overload
    def ToValueTuple(value: Tuple[T1]) -> ValueTuple[T1]: ...
    
    @staticmethod
    @overload
    def ToValueTuple(value: Tuple[T1, T2]) -> ValueTuple[T1, T2]: ...
    
    @staticmethod
    @overload
    def ToValueTuple(value: Tuple[T1, T2, T3]) -> ValueTuple[T1, T2, T3]: ...
    
    @staticmethod
    @overload
    def ToValueTuple(value: Tuple[T1, T2, T3, T4]) -> ValueTuple[T1, T2, T3, T4]: ...
    
    @staticmethod
    @overload
    def ToValueTuple(value: Tuple[T1, T2, T3, T4, T5]) -> ValueTuple[T1, T2, T3, T4, T5]: ...
    
    @staticmethod
    @overload
    def ToValueTuple(value: Tuple[T1, T2, T3, T4, T5, T6]) -> ValueTuple[T1, T2, T3, T4, T5, T6]: ...
    
    @staticmethod
    @overload
    def ToValueTuple(value: Tuple[T1, T2, T3, T4, T5, T6, T7]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7]: ...
    
    @staticmethod
    @overload
    def ToValueTuple(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8]]: ...
    
    @staticmethod
    @overload
    def ToValueTuple(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9]]: ...
    
    @staticmethod
    @overload
    def ToValueTuple(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10]]: ...
    
    @staticmethod
    @overload
    def ToValueTuple(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11]]: ...
    
    @staticmethod
    @overload
    def ToValueTuple(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12]]: ...
    
    @staticmethod
    @overload
    def ToValueTuple(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13]]: ...
    
    @staticmethod
    @overload
    def ToValueTuple(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14]]: ...
    
    @staticmethod
    @overload
    def ToValueTuple(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15]]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15]]]: ...
    
    @staticmethod
    @overload
    def ToValueTuple(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16]]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16]]]: ...
    
    @staticmethod
    @overload
    def ToValueTuple(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17]]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17]]]: ...
    
    @staticmethod
    @overload
    def ToValueTuple(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18]]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17, T18]]]: ...
    
    @staticmethod
    @overload
    def ToValueTuple(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19]]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17, T18, T19]]]: ...
    
    @staticmethod
    @overload
    def ToValueTuple(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19, T20]]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17, T18, T19, T20]]]: ...
    
    @staticmethod
    @overload
    def ToValueTuple(value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19, T20, T21]]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17, T18, T19, T20, T21]]]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Type(ABC, MemberInfo, ICustomAttributeProvider, _MemberInfo, _Type, IReflect):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Delimiter() -> CharType: ...
    
    @staticmethod
    @property
    def EmptyTypes() -> ArrayType[TypeType]: ...
    
    @staticmethod
    @property
    def FilterAttribute() -> MemberFilter: ...
    
    @staticmethod
    @property
    def FilterName() -> MemberFilter: ...
    
    @staticmethod
    @property
    def FilterNameIgnoreCase() -> MemberFilter: ...
    
    @staticmethod
    @property
    def Missing() -> ObjectType: ...
    
    # No Constructors
    
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
    def ContainsGenericParameters(self) -> BooleanType: ...
    
    @property
    def DeclaringMethod(self) -> MethodBase: ...
    
    @property
    def DeclaringType(self) -> TypeType: ...
    
    @staticmethod
    @property
    def DefaultBinder() -> Binder: ...
    
    @property
    def FullName(self) -> StringType: ...
    
    @property
    def GUID(self) -> Guid: ...
    
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes: ...
    
    @property
    def GenericParameterPosition(self) -> IntType: ...
    
    @property
    def GenericTypeArguments(self) -> ArrayType[TypeType]: ...
    
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
    def IsConstructedGenericType(self) -> BooleanType: ...
    
    @property
    def IsContextful(self) -> BooleanType: ...
    
    @property
    def IsEnum(self) -> BooleanType: ...
    
    @property
    def IsExplicitLayout(self) -> BooleanType: ...
    
    @property
    def IsGenericParameter(self) -> BooleanType: ...
    
    @property
    def IsGenericType(self) -> BooleanType: ...
    
    @property
    def IsGenericTypeDefinition(self) -> BooleanType: ...
    
    @property
    def IsImport(self) -> BooleanType: ...
    
    @property
    def IsInterface(self) -> BooleanType: ...
    
    @property
    def IsLayoutSequential(self) -> BooleanType: ...
    
    @property
    def IsMarshalByRef(self) -> BooleanType: ...
    
    @property
    def IsNested(self) -> BooleanType: ...
    
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
    def IsSecurityCritical(self) -> BooleanType: ...
    
    @property
    def IsSecuritySafeCritical(self) -> BooleanType: ...
    
    @property
    def IsSecurityTransparent(self) -> BooleanType: ...
    
    @property
    def IsSerializable(self) -> BooleanType: ...
    
    @property
    def IsSpecialName(self) -> BooleanType: ...
    
    @property
    def IsUnicodeClass(self) -> BooleanType: ...
    
    @property
    def IsValueType(self) -> BooleanType: ...
    
    @property
    def IsVisible(self) -> BooleanType: ...
    
    @property
    def MemberType(self) -> MemberTypes: ...
    
    @property
    def Module(self) -> Module: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @property
    def ReflectedType(self) -> TypeType: ...
    
    @property
    def StructLayoutAttribute(self) -> StructLayoutAttribute: ...
    
    @property
    def TypeHandle(self) -> RuntimeTypeHandle: ...
    
    @property
    def TypeInitializer(self) -> ConstructorInfo: ...
    
    @property
    def UnderlyingSystemType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, o: TypeType) -> BooleanType: ...
    
    def FindInterfaces(self, filter: TypeFilter, filterCriteria: ObjectType) -> ArrayType[TypeType]: ...
    
    def FindMembers(self, memberType: MemberTypes, bindingAttr: BindingFlags, filter: MemberFilter, filterCriteria: ObjectType) -> ArrayType[MemberInfo]: ...
    
    def GetArrayRank(self) -> IntType: ...
    
    @overload
    def GetConstructor(self, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: ArrayType[TypeType], modifiers: ArrayType[ParameterModifier]) -> ConstructorInfo: ...
    
    @overload
    def GetConstructor(self, bindingAttr: BindingFlags, binder: Binder, types: ArrayType[TypeType], modifiers: ArrayType[ParameterModifier]) -> ConstructorInfo: ...
    
    @overload
    def GetConstructor(self, types: ArrayType[TypeType]) -> ConstructorInfo: ...
    
    @overload
    def GetConstructors(self) -> ArrayType[ConstructorInfo]: ...
    
    @overload
    def GetConstructors(self, bindingAttr: BindingFlags) -> ArrayType[ConstructorInfo]: ...
    
    def GetDefaultMembers(self) -> ArrayType[MemberInfo]: ...
    
    def GetElementType(self) -> TypeType: ...
    
    def GetEnumName(self, value: ObjectType) -> StringType: ...
    
    def GetEnumNames(self) -> ArrayType[StringType]: ...
    
    def GetEnumUnderlyingType(self) -> TypeType: ...
    
    def GetEnumValues(self) -> Array: ...
    
    @overload
    def GetEvent(self, name: StringType) -> EventInfo: ...
    
    @overload
    def GetEvent(self, name: StringType, bindingAttr: BindingFlags) -> EventInfo: ...
    
    @overload
    def GetEvents(self) -> ArrayType[EventInfo]: ...
    
    @overload
    def GetEvents(self, bindingAttr: BindingFlags) -> ArrayType[EventInfo]: ...
    
    @overload
    def GetField(self, name: StringType) -> FieldInfo: ...
    
    @overload
    def GetField(self, name: StringType, bindingAttr: BindingFlags) -> FieldInfo: ...
    
    @overload
    def GetFields(self) -> ArrayType[FieldInfo]: ...
    
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> ArrayType[FieldInfo]: ...
    
    def GetGenericArguments(self) -> ArrayType[TypeType]: ...
    
    def GetGenericParameterConstraints(self) -> ArrayType[TypeType]: ...
    
    def GetGenericTypeDefinition(self) -> TypeType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @overload
    def GetInterface(self, name: StringType) -> TypeType: ...
    
    @overload
    def GetInterface(self, name: StringType, ignoreCase: BooleanType) -> TypeType: ...
    
    def GetInterfaceMap(self, interfaceType: TypeType) -> InterfaceMapping: ...
    
    def GetInterfaces(self) -> ArrayType[TypeType]: ...
    
    @overload
    def GetMember(self, name: StringType) -> ArrayType[MemberInfo]: ...
    
    @overload
    def GetMember(self, name: StringType, bindingAttr: BindingFlags) -> ArrayType[MemberInfo]: ...
    
    @overload
    def GetMember(self, name: StringType, type: MemberTypes, bindingAttr: BindingFlags) -> ArrayType[MemberInfo]: ...
    
    @overload
    def GetMembers(self) -> ArrayType[MemberInfo]: ...
    
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> ArrayType[MemberInfo]: ...
    
    @overload
    def GetMethod(self, name: StringType, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: ArrayType[TypeType], modifiers: ArrayType[ParameterModifier]) -> MethodInfo: ...
    
    @overload
    def GetMethod(self, name: StringType, bindingAttr: BindingFlags, binder: Binder, types: ArrayType[TypeType], modifiers: ArrayType[ParameterModifier]) -> MethodInfo: ...
    
    @overload
    def GetMethod(self, name: StringType, types: ArrayType[TypeType], modifiers: ArrayType[ParameterModifier]) -> MethodInfo: ...
    
    @overload
    def GetMethod(self, name: StringType, types: ArrayType[TypeType]) -> MethodInfo: ...
    
    @overload
    def GetMethod(self, name: StringType, bindingAttr: BindingFlags) -> MethodInfo: ...
    
    @overload
    def GetMethod(self, name: StringType) -> MethodInfo: ...
    
    @overload
    def GetMethods(self) -> ArrayType[MethodInfo]: ...
    
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> ArrayType[MethodInfo]: ...
    
    @overload
    def GetNestedType(self, name: StringType) -> TypeType: ...
    
    @overload
    def GetNestedType(self, name: StringType, bindingAttr: BindingFlags) -> TypeType: ...
    
    @overload
    def GetNestedTypes(self) -> ArrayType[TypeType]: ...
    
    @overload
    def GetNestedTypes(self, bindingAttr: BindingFlags) -> ArrayType[TypeType]: ...
    
    @overload
    def GetProperties(self) -> ArrayType[PropertyInfo]: ...
    
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> ArrayType[PropertyInfo]: ...
    
    @overload
    def GetProperty(self, name: StringType, bindingAttr: BindingFlags, binder: Binder, returnType: TypeType, types: ArrayType[TypeType], modifiers: ArrayType[ParameterModifier]) -> PropertyInfo: ...
    
    @overload
    def GetProperty(self, name: StringType, returnType: TypeType, types: ArrayType[TypeType], modifiers: ArrayType[ParameterModifier]) -> PropertyInfo: ...
    
    @overload
    def GetProperty(self, name: StringType, bindingAttr: BindingFlags) -> PropertyInfo: ...
    
    @overload
    def GetProperty(self, name: StringType, returnType: TypeType, types: ArrayType[TypeType]) -> PropertyInfo: ...
    
    @overload
    def GetProperty(self, name: StringType, types: ArrayType[TypeType]) -> PropertyInfo: ...
    
    @overload
    def GetProperty(self, name: StringType, returnType: TypeType) -> PropertyInfo: ...
    
    @overload
    def GetProperty(self, name: StringType) -> PropertyInfo: ...
    
    @staticmethod
    @overload
    def GetType(typeName: StringType, throwOnError: BooleanType, ignoreCase: BooleanType) -> TypeType: ...
    
    @staticmethod
    @overload
    def GetType(typeName: StringType, throwOnError: BooleanType) -> TypeType: ...
    
    @staticmethod
    @overload
    def GetType(typeName: StringType) -> TypeType: ...
    
    @staticmethod
    @overload
    def GetType(typeName: StringType, assemblyResolver: Func[AssemblyName, Assembly], typeResolver: Func[Assembly, StringType, BooleanType, TypeType]) -> TypeType: ...
    
    @staticmethod
    @overload
    def GetType(typeName: StringType, assemblyResolver: Func[AssemblyName, Assembly], typeResolver: Func[Assembly, StringType, BooleanType, TypeType], throwOnError: BooleanType) -> TypeType: ...
    
    @staticmethod
    @overload
    def GetType(typeName: StringType, assemblyResolver: Func[AssemblyName, Assembly], typeResolver: Func[Assembly, StringType, BooleanType, TypeType], throwOnError: BooleanType, ignoreCase: BooleanType) -> TypeType: ...
    
    @overload
    def GetType(self) -> TypeType: ...
    
    @staticmethod
    def GetTypeArray(args: ArrayType[ObjectType]) -> ArrayType[TypeType]: ...
    
    @staticmethod
    def GetTypeCode(type: TypeType) -> TypeCode: ...
    
    @staticmethod
    @overload
    def GetTypeFromCLSID(clsid: Guid) -> TypeType: ...
    
    @staticmethod
    @overload
    def GetTypeFromCLSID(clsid: Guid, throwOnError: BooleanType) -> TypeType: ...
    
    @staticmethod
    @overload
    def GetTypeFromCLSID(clsid: Guid, server: StringType) -> TypeType: ...
    
    @staticmethod
    @overload
    def GetTypeFromCLSID(clsid: Guid, server: StringType, throwOnError: BooleanType) -> TypeType: ...
    
    @staticmethod
    def GetTypeFromHandle(handle: RuntimeTypeHandle) -> TypeType: ...
    
    @staticmethod
    @overload
    def GetTypeFromProgID(progID: StringType) -> TypeType: ...
    
    @staticmethod
    @overload
    def GetTypeFromProgID(progID: StringType, throwOnError: BooleanType) -> TypeType: ...
    
    @staticmethod
    @overload
    def GetTypeFromProgID(progID: StringType, server: StringType) -> TypeType: ...
    
    @staticmethod
    @overload
    def GetTypeFromProgID(progID: StringType, server: StringType, throwOnError: BooleanType) -> TypeType: ...
    
    @staticmethod
    def GetTypeHandle(o: ObjectType) -> RuntimeTypeHandle: ...
    
    @overload
    def InvokeMember(self, name: StringType, invokeAttr: BindingFlags, binder: Binder, target: ObjectType, args: ArrayType[ObjectType], culture: CultureInfo) -> ObjectType: ...
    
    @overload
    def InvokeMember(self, name: StringType, invokeAttr: BindingFlags, binder: Binder, target: ObjectType, args: ArrayType[ObjectType]) -> ObjectType: ...
    
    @overload
    def InvokeMember(self, name: StringType, invokeAttr: BindingFlags, binder: Binder, target: ObjectType, args: ArrayType[ObjectType], modifiers: ArrayType[ParameterModifier], culture: CultureInfo, namedParameters: ArrayType[StringType]) -> ObjectType: ...
    
    def IsAssignableFrom(self, c: TypeType) -> BooleanType: ...
    
    def IsEnumDefined(self, value: ObjectType) -> BooleanType: ...
    
    def IsEquivalentTo(self, other: TypeType) -> BooleanType: ...
    
    def IsInstanceOfType(self, o: ObjectType) -> BooleanType: ...
    
    def IsSubclassOf(self, c: TypeType) -> BooleanType: ...
    
    @overload
    def MakeArrayType(self) -> TypeType: ...
    
    @overload
    def MakeArrayType(self, rank: IntType) -> TypeType: ...
    
    def MakeByRefType(self) -> TypeType: ...
    
    def MakeGenericType(self, typeArguments: ArrayType[TypeType]) -> TypeType: ...
    
    def MakePointerType(self) -> TypeType: ...
    
    @staticmethod
    def ReflectionOnlyGetType(typeName: StringType, throwIfNotFound: BooleanType, ignoreCase: BooleanType) -> TypeType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Assembly(self) -> Assembly: ...
    
    def get_AssemblyQualifiedName(self) -> StringType: ...
    
    def get_Attributes(self) -> TypeAttributes: ...
    
    def get_BaseType(self) -> TypeType: ...
    
    def get_ContainsGenericParameters(self) -> BooleanType: ...
    
    def get_DeclaringMethod(self) -> MethodBase: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    @staticmethod
    def get_DefaultBinder() -> Binder: ...
    
    def get_FullName(self) -> StringType: ...
    
    def get_GUID(self) -> Guid: ...
    
    def get_GenericParameterAttributes(self) -> GenericParameterAttributes: ...
    
    def get_GenericParameterPosition(self) -> IntType: ...
    
    def get_GenericTypeArguments(self) -> ArrayType[TypeType]: ...
    
    def get_HasElementType(self) -> BooleanType: ...
    
    def get_IsAbstract(self) -> BooleanType: ...
    
    def get_IsAnsiClass(self) -> BooleanType: ...
    
    def get_IsArray(self) -> BooleanType: ...
    
    def get_IsAutoClass(self) -> BooleanType: ...
    
    def get_IsAutoLayout(self) -> BooleanType: ...
    
    def get_IsByRef(self) -> BooleanType: ...
    
    def get_IsCOMObject(self) -> BooleanType: ...
    
    def get_IsClass(self) -> BooleanType: ...
    
    def get_IsConstructedGenericType(self) -> BooleanType: ...
    
    def get_IsContextful(self) -> BooleanType: ...
    
    def get_IsEnum(self) -> BooleanType: ...
    
    def get_IsExplicitLayout(self) -> BooleanType: ...
    
    def get_IsGenericParameter(self) -> BooleanType: ...
    
    def get_IsGenericType(self) -> BooleanType: ...
    
    def get_IsGenericTypeDefinition(self) -> BooleanType: ...
    
    def get_IsImport(self) -> BooleanType: ...
    
    def get_IsInterface(self) -> BooleanType: ...
    
    def get_IsLayoutSequential(self) -> BooleanType: ...
    
    def get_IsMarshalByRef(self) -> BooleanType: ...
    
    def get_IsNested(self) -> BooleanType: ...
    
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
    
    def get_IsSecurityCritical(self) -> BooleanType: ...
    
    def get_IsSecuritySafeCritical(self) -> BooleanType: ...
    
    def get_IsSecurityTransparent(self) -> BooleanType: ...
    
    def get_IsSerializable(self) -> BooleanType: ...
    
    def get_IsSpecialName(self) -> BooleanType: ...
    
    def get_IsUnicodeClass(self) -> BooleanType: ...
    
    def get_IsValueType(self) -> BooleanType: ...
    
    def get_IsVisible(self) -> BooleanType: ...
    
    def get_MemberType(self) -> MemberTypes: ...
    
    @overload
    def get_Module(self) -> Module: ...
    
    def get_Namespace(self) -> StringType: ...
    
    def get_ReflectedType(self) -> TypeType: ...
    
    def get_StructLayoutAttribute(self) -> StructLayoutAttribute: ...
    
    def get_TypeHandle(self) -> RuntimeTypeHandle: ...
    
    def get_TypeInitializer(self) -> ConstructorInfo: ...
    
    def get_UnderlyingSystemType(self) -> TypeType: ...
    
    @staticmethod
    def op_Equality(left: TypeType, right: TypeType) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: TypeType, right: TypeType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeAccessException(TypeLoadException, ISerializable, _Exception):
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


class TypeInitializationException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, fullTypeName: StringType, innerException: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_TypeName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeLoadException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Message(self) -> StringType: ...
    
    @property
    def TypeName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_Message(self) -> StringType: ...
    
    def get_TypeName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeNameParser(ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeUnloadedException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnauthorizedAccessException(SystemException, ISerializable, _Exception):
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


class UncNameHelper(ObjectType):
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


class UnhandledExceptionEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, exception: ObjectType, isTerminating: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ExceptionObject(self) -> ObjectType: ...
    
    @property
    def IsTerminating(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_ExceptionObject(self) -> ObjectType: ...
    
    def get_IsTerminating(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnhandledExceptionEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: UnhandledExceptionEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: UnhandledExceptionEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnitySerializationHolder(ObjectType, ISerializable, IObjectReference):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def GetRealObject(self, context: StreamingContext) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Uri(ObjectType, ISerializable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def SchemeDelimiter() -> StringType: ...
    
    @staticmethod
    @property
    def UriSchemeFile() -> StringType: ...
    
    @staticmethod
    @property
    def UriSchemeFtp() -> StringType: ...
    
    @staticmethod
    @property
    def UriSchemeGopher() -> StringType: ...
    
    @staticmethod
    @property
    def UriSchemeHttp() -> StringType: ...
    
    @staticmethod
    @property
    def UriSchemeHttps() -> StringType: ...
    
    @staticmethod
    @property
    def UriSchemeMailto() -> StringType: ...
    
    @staticmethod
    @property
    def UriSchemeNetPipe() -> StringType: ...
    
    @staticmethod
    @property
    def UriSchemeNetTcp() -> StringType: ...
    
    @staticmethod
    @property
    def UriSchemeNews() -> StringType: ...
    
    @staticmethod
    @property
    def UriSchemeNntp() -> StringType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, uriString: StringType): ...
    
    @overload
    def __init__(self, uriString: StringType, dontEscape: BooleanType): ...
    
    @overload
    def __init__(self, baseUri: Uri, relativeUri: StringType, dontEscape: BooleanType): ...
    
    @overload
    def __init__(self, uriString: StringType, uriKind: UriKind): ...
    
    @overload
    def __init__(self, baseUri: Uri, relativeUri: StringType): ...
    
    @overload
    def __init__(self, baseUri: Uri, relativeUri: Uri): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AbsolutePath(self) -> StringType: ...
    
    @property
    def AbsoluteUri(self) -> StringType: ...
    
    @property
    def Authority(self) -> StringType: ...
    
    @property
    def DnsSafeHost(self) -> StringType: ...
    
    @property
    def Fragment(self) -> StringType: ...
    
    @property
    def Host(self) -> StringType: ...
    
    @property
    def HostNameType(self) -> UriHostNameType: ...
    
    @property
    def IdnHost(self) -> StringType: ...
    
    @property
    def IsAbsoluteUri(self) -> BooleanType: ...
    
    @property
    def IsDefaultPort(self) -> BooleanType: ...
    
    @property
    def IsFile(self) -> BooleanType: ...
    
    @property
    def IsLoopback(self) -> BooleanType: ...
    
    @property
    def IsUnc(self) -> BooleanType: ...
    
    @property
    def LocalPath(self) -> StringType: ...
    
    @property
    def OriginalString(self) -> StringType: ...
    
    @property
    def PathAndQuery(self) -> StringType: ...
    
    @property
    def Port(self) -> IntType: ...
    
    @property
    def Query(self) -> StringType: ...
    
    @property
    def Scheme(self) -> StringType: ...
    
    @property
    def Segments(self) -> ArrayType[StringType]: ...
    
    @property
    def UserEscaped(self) -> BooleanType: ...
    
    @property
    def UserInfo(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CheckHostName(name: StringType) -> UriHostNameType: ...
    
    @staticmethod
    def CheckSchemeName(schemeName: StringType) -> BooleanType: ...
    
    @staticmethod
    def Compare(uri1: Uri, uri2: Uri, partsToCompare: UriComponents, compareFormat: UriFormat, comparisonType: StringComparison) -> IntType: ...
    
    def Equals(self, comparand: ObjectType) -> BooleanType: ...
    
    @staticmethod
    def EscapeDataString(stringToEscape: StringType) -> StringType: ...
    
    @staticmethod
    def EscapeUriString(stringToEscape: StringType) -> StringType: ...
    
    @staticmethod
    def FromHex(digit: CharType) -> IntType: ...
    
    def GetComponents(self, components: UriComponents, format: UriFormat) -> StringType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetLeftPart(self, part: UriPartial) -> StringType: ...
    
    @staticmethod
    def HexEscape(character: CharType) -> StringType: ...
    
    @staticmethod
    def HexUnescape(pattern: StringType, index: IntType) -> Tuple[CharType, IntType]: ...
    
    def IsBaseOf(self, uri: Uri) -> BooleanType: ...
    
    @staticmethod
    def IsHexDigit(character: CharType) -> BooleanType: ...
    
    @staticmethod
    def IsHexEncoding(pattern: StringType, index: IntType) -> BooleanType: ...
    
    def IsWellFormedOriginalString(self) -> BooleanType: ...
    
    @staticmethod
    def IsWellFormedUriString(uriString: StringType, uriKind: UriKind) -> BooleanType: ...
    
    def MakeRelative(self, toUri: Uri) -> StringType: ...
    
    def MakeRelativeUri(self, uri: Uri) -> Uri: ...
    
    def ToString(self) -> StringType: ...
    
    @staticmethod
    @overload
    def TryCreate(uriString: StringType, uriKind: UriKind, result: Uri) -> Tuple[BooleanType, Uri]: ...
    
    @staticmethod
    @overload
    def TryCreate(baseUri: Uri, relativeUri: StringType, result: Uri) -> Tuple[BooleanType, Uri]: ...
    
    @staticmethod
    @overload
    def TryCreate(baseUri: Uri, relativeUri: Uri, result: Uri) -> Tuple[BooleanType, Uri]: ...
    
    @staticmethod
    def UnescapeDataString(stringToUnescape: StringType) -> StringType: ...
    
    def get_AbsolutePath(self) -> StringType: ...
    
    def get_AbsoluteUri(self) -> StringType: ...
    
    def get_Authority(self) -> StringType: ...
    
    def get_DnsSafeHost(self) -> StringType: ...
    
    def get_Fragment(self) -> StringType: ...
    
    def get_Host(self) -> StringType: ...
    
    def get_HostNameType(self) -> UriHostNameType: ...
    
    def get_IdnHost(self) -> StringType: ...
    
    def get_IsAbsoluteUri(self) -> BooleanType: ...
    
    def get_IsDefaultPort(self) -> BooleanType: ...
    
    def get_IsFile(self) -> BooleanType: ...
    
    def get_IsLoopback(self) -> BooleanType: ...
    
    def get_IsUnc(self) -> BooleanType: ...
    
    def get_LocalPath(self) -> StringType: ...
    
    def get_OriginalString(self) -> StringType: ...
    
    def get_PathAndQuery(self) -> StringType: ...
    
    def get_Port(self) -> IntType: ...
    
    def get_Query(self) -> StringType: ...
    
    def get_Scheme(self) -> StringType: ...
    
    def get_Segments(self) -> ArrayType[StringType]: ...
    
    def get_UserEscaped(self) -> BooleanType: ...
    
    def get_UserInfo(self) -> StringType: ...
    
    @staticmethod
    def op_Equality(uri1: Uri, uri2: Uri) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(uri1: Uri, uri2: Uri) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UriBuilder(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, uri: StringType): ...
    
    @overload
    def __init__(self, uri: Uri): ...
    
    @overload
    def __init__(self, schemeName: StringType, hostName: StringType): ...
    
    @overload
    def __init__(self, scheme: StringType, host: StringType, portNumber: IntType): ...
    
    @overload
    def __init__(self, scheme: StringType, host: StringType, port: IntType, pathValue: StringType): ...
    
    @overload
    def __init__(self, scheme: StringType, host: StringType, port: IntType, path: StringType, extraValue: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Fragment(self) -> StringType: ...
    
    @Fragment.setter
    def Fragment(self, value: StringType) -> None: ...
    
    @property
    def Host(self) -> StringType: ...
    
    @Host.setter
    def Host(self, value: StringType) -> None: ...
    
    @property
    def Password(self) -> StringType: ...
    
    @Password.setter
    def Password(self, value: StringType) -> None: ...
    
    @property
    def Path(self) -> StringType: ...
    
    @Path.setter
    def Path(self, value: StringType) -> None: ...
    
    @property
    def Port(self) -> IntType: ...
    
    @Port.setter
    def Port(self, value: IntType) -> None: ...
    
    @property
    def Query(self) -> StringType: ...
    
    @Query.setter
    def Query(self, value: StringType) -> None: ...
    
    @property
    def Scheme(self) -> StringType: ...
    
    @Scheme.setter
    def Scheme(self, value: StringType) -> None: ...
    
    @property
    def Uri(self) -> Uri: ...
    
    @property
    def UserName(self) -> StringType: ...
    
    @UserName.setter
    def UserName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, rparam: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Fragment(self) -> StringType: ...
    
    def get_Host(self) -> StringType: ...
    
    def get_Password(self) -> StringType: ...
    
    def get_Path(self) -> StringType: ...
    
    def get_Port(self) -> IntType: ...
    
    def get_Query(self) -> StringType: ...
    
    def get_Scheme(self) -> StringType: ...
    
    def get_Uri(self) -> Uri: ...
    
    def get_UserName(self) -> StringType: ...
    
    def set_Fragment(self, value: StringType) -> VoidType: ...
    
    def set_Host(self, value: StringType) -> VoidType: ...
    
    def set_Password(self, value: StringType) -> VoidType: ...
    
    def set_Path(self, value: StringType) -> VoidType: ...
    
    def set_Port(self, value: IntType) -> VoidType: ...
    
    def set_Query(self, value: StringType) -> VoidType: ...
    
    def set_Scheme(self, value: StringType) -> VoidType: ...
    
    def set_UserName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UriFormatException(FormatException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, textString: StringType): ...
    
    @overload
    def __init__(self, textString: StringType, e: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UriHelper(ABC, ObjectType):
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


class UriParser(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def IsKnownScheme(schemeName: StringType) -> BooleanType: ...
    
    @staticmethod
    def Register(uriParser: UriParser, schemeName: StringType, defaultPort: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UriTypeConverter(TypeConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: TypeType) -> BooleanType: ...
    
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: TypeType) -> BooleanType: ...
    
    @overload
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType) -> ObjectType: ...
    
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: ObjectType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ValueType(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Version(ObjectType, ICloneable, IComparable, IComparable[Version], IEquatable[Version]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, major: IntType, minor: IntType, build: IntType, revision: IntType): ...
    
    @overload
    def __init__(self, major: IntType, minor: IntType, build: IntType): ...
    
    @overload
    def __init__(self, major: IntType, minor: IntType): ...
    
    @overload
    def __init__(self, version: StringType): ...
    
    @overload
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Build(self) -> IntType: ...
    
    @property
    def Major(self) -> IntType: ...
    
    @property
    def MajorRevision(self) -> ShortType: ...
    
    @property
    def Minor(self) -> IntType: ...
    
    @property
    def MinorRevision(self) -> ShortType: ...
    
    @property
    def Revision(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ObjectType: ...
    
    @overload
    def CompareTo(self, version: ObjectType) -> IntType: ...
    
    @overload
    def CompareTo(self, value: Version) -> IntType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: Version) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    def Parse(input: StringType) -> Version: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, fieldCount: IntType) -> StringType: ...
    
    @staticmethod
    def TryParse(input: StringType, result: Version) -> Tuple[BooleanType, Version]: ...
    
    def get_Build(self) -> IntType: ...
    
    def get_Major(self) -> IntType: ...
    
    def get_MajorRevision(self) -> ShortType: ...
    
    def get_Minor(self) -> IntType: ...
    
    def get_MinorRevision(self) -> ShortType: ...
    
    def get_Revision(self) -> IntType: ...
    
    @staticmethod
    def op_Equality(v1: Version, v2: Version) -> BooleanType: ...
    
    @staticmethod
    def op_GreaterThan(v1: Version, v2: Version) -> BooleanType: ...
    
    @staticmethod
    def op_GreaterThanOrEqual(v1: Version, v2: Version) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(v1: Version, v2: Version) -> BooleanType: ...
    
    @staticmethod
    def op_LessThan(v1: Version, v2: Version) -> BooleanType: ...
    
    @staticmethod
    def op_LessThanOrEqual(v1: Version, v2: Version) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WeakReference(ObjectType, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, target: ObjectType): ...
    
    @overload
    def __init__(self, target: ObjectType, trackResurrection: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsAlive(self) -> BooleanType: ...
    
    @property
    def Target(self) -> ObjectType: ...
    
    @Target.setter
    def Target(self, value: ObjectType) -> None: ...
    
    @property
    def TrackResurrection(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_IsAlive(self) -> BooleanType: ...
    
    def get_Target(self) -> ObjectType: ...
    
    def get_TrackResurrection(self) -> BooleanType: ...
    
    def set_Target(self, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WeakReference(Generic[T], ObjectType, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, target: T): ...
    
    @overload
    def __init__(self, target: T, trackResurrection: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def SetTarget(self, target: T) -> VoidType: ...
    
    def TryGetTarget(self, target: T) -> Tuple[BooleanType, T]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlIgnoreMemberAttribute(Attribute, _Attribute):
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


class __Canon(ObjectType):
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


class __ComObject(MarshalByRefObject):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class __Filters(ObjectType):
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


class __HResults(ABC, ObjectType):
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


# ---------- Structs ---------- #

class AppDomainHandle(ValueType):
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


class ArgIterator(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, arglist: RuntimeArgumentHandle): ...
    
    @overload
    def __init__(self, arglist: RuntimeArgumentHandle, ptr: VoidType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def End(self) -> VoidType: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @overload
    def GetNextArg(self) -> TypedReference: ...
    
    @overload
    def GetNextArg(self, rth: RuntimeTypeHandle) -> TypedReference: ...
    
    def GetNextArgType(self) -> RuntimeTypeHandle: ...
    
    def GetRemainingCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ArraySegment(Generic[T], ValueType, IList[T], ICollection[T], IEnumerable[T], IEnumerable, IReadOnlyList[T], IReadOnlyCollection[T]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, array: ArrayType[T]): ...
    
    @overload
    def __init__(self, array: ArrayType[T], offset: IntType, count: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Array(self) -> ArrayType[T]: ...
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Offset(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: ArraySegment[T]) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Array(self) -> ArrayType[T]: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Offset(self) -> IntType: ...
    
    @staticmethod
    def op_Equality(a: ArraySegment[T], b: ArraySegment[T]) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(a: ArraySegment[T], b: ArraySegment[T]) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Boolean(ValueType, IComparable, IConvertible, IComparable[BooleanType], IEquatable[BooleanType]):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def FalseString() -> StringType: ...
    
    @staticmethod
    @property
    def TrueString() -> StringType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CompareTo(self, obj: ObjectType) -> IntType: ...
    
    @overload
    def CompareTo(self, value: BooleanType) -> IntType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: BooleanType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetTypeCode(self) -> TypeCode: ...
    
    @staticmethod
    def Parse(value: StringType) -> BooleanType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    def TryParse(value: StringType, result: BooleanType) -> Tuple[BooleanType, BooleanType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Byte(ValueType, IComparable, IFormattable, IConvertible, IComparable[ByteType], IEquatable[ByteType]):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def MaxValue() -> ByteType: ...
    
    @staticmethod
    @property
    def MinValue() -> ByteType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CompareTo(self, value: ObjectType) -> IntType: ...
    
    @overload
    def CompareTo(self, value: ByteType) -> IntType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: ByteType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetTypeCode(self) -> TypeCode: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType) -> ByteType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, style: NumberStyles) -> ByteType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, provider: IFormatProvider) -> ByteType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, style: NumberStyles, provider: IFormatProvider) -> ByteType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType) -> StringType: ...
    
    @overload
    def ToString(self, provider: IFormatProvider) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, result: ByteType) -> Tuple[BooleanType, ByteType]: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, style: NumberStyles, provider: IFormatProvider, result: ByteType) -> Tuple[BooleanType, ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Char(ValueType, IComparable, IConvertible, IComparable[CharType], IEquatable[CharType]):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def MaxValue() -> CharType: ...
    
    @staticmethod
    @property
    def MinValue() -> CharType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CompareTo(self, value: ObjectType) -> IntType: ...
    
    @overload
    def CompareTo(self, value: CharType) -> IntType: ...
    
    @staticmethod
    def ConvertFromUtf32(utf32: IntType) -> StringType: ...
    
    @staticmethod
    @overload
    def ConvertToUtf32(highSurrogate: CharType, lowSurrogate: CharType) -> IntType: ...
    
    @staticmethod
    @overload
    def ConvertToUtf32(s: StringType, index: IntType) -> IntType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: CharType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    @overload
    def GetNumericValue(c: CharType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def GetNumericValue(s: StringType, index: IntType) -> DoubleType: ...
    
    def GetTypeCode(self) -> TypeCode: ...
    
    @staticmethod
    @overload
    def GetUnicodeCategory(c: CharType) -> UnicodeCategory: ...
    
    @staticmethod
    @overload
    def GetUnicodeCategory(s: StringType, index: IntType) -> UnicodeCategory: ...
    
    @staticmethod
    @overload
    def IsControl(c: CharType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsControl(s: StringType, index: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsDigit(c: CharType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsDigit(s: StringType, index: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsHighSurrogate(c: CharType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsHighSurrogate(s: StringType, index: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsLetter(c: CharType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsLetter(s: StringType, index: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsLetterOrDigit(c: CharType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsLetterOrDigit(s: StringType, index: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsLowSurrogate(c: CharType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsLowSurrogate(s: StringType, index: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsLower(c: CharType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsLower(s: StringType, index: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsNumber(c: CharType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsNumber(s: StringType, index: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsPunctuation(c: CharType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsPunctuation(s: StringType, index: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsSeparator(c: CharType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsSeparator(s: StringType, index: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsSurrogate(c: CharType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsSurrogate(s: StringType, index: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsSurrogatePair(s: StringType, index: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsSurrogatePair(highSurrogate: CharType, lowSurrogate: CharType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsSymbol(c: CharType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsSymbol(s: StringType, index: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsUpper(c: CharType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsUpper(s: StringType, index: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsWhiteSpace(c: CharType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsWhiteSpace(s: StringType, index: IntType) -> BooleanType: ...
    
    @staticmethod
    def Parse(s: StringType) -> CharType: ...
    
    @staticmethod
    @overload
    def ToLower(c: CharType, culture: CultureInfo) -> CharType: ...
    
    @staticmethod
    @overload
    def ToLower(c: CharType) -> CharType: ...
    
    @staticmethod
    def ToLowerInvariant(c: CharType) -> CharType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(c: CharType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToUpper(c: CharType, culture: CultureInfo) -> CharType: ...
    
    @staticmethod
    @overload
    def ToUpper(c: CharType) -> CharType: ...
    
    @staticmethod
    def ToUpperInvariant(c: CharType) -> CharType: ...
    
    @staticmethod
    def TryParse(s: StringType, result: CharType) -> Tuple[BooleanType, CharType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConsoleKeyInfo(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, keyChar: CharType, key: ConsoleKey, shift: BooleanType, alt: BooleanType, control: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Key(self) -> ConsoleKey: ...
    
    @property
    def KeyChar(self) -> CharType: ...
    
    @property
    def Modifiers(self) -> ConsoleModifiers: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: ConsoleKeyInfo) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Key(self) -> ConsoleKey: ...
    
    def get_KeyChar(self) -> CharType: ...
    
    def get_Modifiers(self) -> ConsoleModifiers: ...
    
    @staticmethod
    def op_Equality(a: ConsoleKeyInfo, b: ConsoleKeyInfo) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(a: ConsoleKeyInfo, b: ConsoleKeyInfo) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Currency(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, value: DecimalType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def FromOACurrency(cy: LongType) -> Currency: ...
    
    @staticmethod
    def ToDecimal(c: Currency) -> DecimalType: ...
    
    def ToOACurrency(self) -> LongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DTSubString(ValueType):
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


class DateTime(ValueType, IComparable, IFormattable, IConvertible, ISerializable, IComparable[DateTime], IEquatable[DateTime]):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def MaxValue() -> DateTime: ...
    
    @staticmethod
    @property
    def MinValue() -> DateTime: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, ticks: LongType): ...
    
    @overload
    def __init__(self, ticks: LongType, kind: DateTimeKind): ...
    
    @overload
    def __init__(self, year: IntType, month: IntType, day: IntType): ...
    
    @overload
    def __init__(self, year: IntType, month: IntType, day: IntType, calendar: Calendar): ...
    
    @overload
    def __init__(self, year: IntType, month: IntType, day: IntType, hour: IntType, minute: IntType, second: IntType): ...
    
    @overload
    def __init__(self, year: IntType, month: IntType, day: IntType, hour: IntType, minute: IntType, second: IntType, kind: DateTimeKind): ...
    
    @overload
    def __init__(self, year: IntType, month: IntType, day: IntType, hour: IntType, minute: IntType, second: IntType, calendar: Calendar): ...
    
    @overload
    def __init__(self, year: IntType, month: IntType, day: IntType, hour: IntType, minute: IntType, second: IntType, millisecond: IntType): ...
    
    @overload
    def __init__(self, year: IntType, month: IntType, day: IntType, hour: IntType, minute: IntType, second: IntType, millisecond: IntType, kind: DateTimeKind): ...
    
    @overload
    def __init__(self, year: IntType, month: IntType, day: IntType, hour: IntType, minute: IntType, second: IntType, millisecond: IntType, calendar: Calendar): ...
    
    @overload
    def __init__(self, year: IntType, month: IntType, day: IntType, hour: IntType, minute: IntType, second: IntType, millisecond: IntType, calendar: Calendar, kind: DateTimeKind): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Date(self) -> DateTime: ...
    
    @property
    def Day(self) -> IntType: ...
    
    @property
    def DayOfWeek(self) -> DayOfWeek: ...
    
    @property
    def DayOfYear(self) -> IntType: ...
    
    @property
    def Hour(self) -> IntType: ...
    
    @property
    def Kind(self) -> DateTimeKind: ...
    
    @property
    def Millisecond(self) -> IntType: ...
    
    @property
    def Minute(self) -> IntType: ...
    
    @property
    def Month(self) -> IntType: ...
    
    @staticmethod
    @property
    def Now() -> DateTime: ...
    
    @property
    def Second(self) -> IntType: ...
    
    @property
    def Ticks(self) -> LongType: ...
    
    @property
    def TimeOfDay(self) -> TimeSpan: ...
    
    @staticmethod
    @property
    def Today() -> DateTime: ...
    
    @staticmethod
    @property
    def UtcNow() -> DateTime: ...
    
    @property
    def Year(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, value: TimeSpan) -> DateTime: ...
    
    def AddDays(self, value: DoubleType) -> DateTime: ...
    
    def AddHours(self, value: DoubleType) -> DateTime: ...
    
    def AddMilliseconds(self, value: DoubleType) -> DateTime: ...
    
    def AddMinutes(self, value: DoubleType) -> DateTime: ...
    
    def AddMonths(self, months: IntType) -> DateTime: ...
    
    def AddSeconds(self, value: DoubleType) -> DateTime: ...
    
    def AddTicks(self, value: LongType) -> DateTime: ...
    
    def AddYears(self, value: IntType) -> DateTime: ...
    
    @staticmethod
    def Compare(t1: DateTime, t2: DateTime) -> IntType: ...
    
    @overload
    def CompareTo(self, value: ObjectType) -> IntType: ...
    
    @overload
    def CompareTo(self, value: DateTime) -> IntType: ...
    
    @staticmethod
    def DaysInMonth(year: IntType, month: IntType) -> IntType: ...
    
    @overload
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, value: DateTime) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Equals(t1: DateTime, t2: DateTime) -> BooleanType: ...
    
    @staticmethod
    def FromBinary(dateData: LongType) -> DateTime: ...
    
    @staticmethod
    def FromFileTime(fileTime: LongType) -> DateTime: ...
    
    @staticmethod
    def FromFileTimeUtc(fileTime: LongType) -> DateTime: ...
    
    @staticmethod
    def FromOADate(d: DoubleType) -> DateTime: ...
    
    @overload
    def GetDateTimeFormats(self) -> ArrayType[StringType]: ...
    
    @overload
    def GetDateTimeFormats(self, provider: IFormatProvider) -> ArrayType[StringType]: ...
    
    @overload
    def GetDateTimeFormats(self, format: CharType) -> ArrayType[StringType]: ...
    
    @overload
    def GetDateTimeFormats(self, format: CharType, provider: IFormatProvider) -> ArrayType[StringType]: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetTypeCode(self) -> TypeCode: ...
    
    def IsDaylightSavingTime(self) -> BooleanType: ...
    
    @staticmethod
    def IsLeapYear(year: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType) -> DateTime: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, provider: IFormatProvider) -> DateTime: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, provider: IFormatProvider, styles: DateTimeStyles) -> DateTime: ...
    
    @staticmethod
    @overload
    def ParseExact(s: StringType, format: StringType, provider: IFormatProvider) -> DateTime: ...
    
    @staticmethod
    @overload
    def ParseExact(s: StringType, format: StringType, provider: IFormatProvider, style: DateTimeStyles) -> DateTime: ...
    
    @staticmethod
    @overload
    def ParseExact(s: StringType, formats: ArrayType[StringType], provider: IFormatProvider, style: DateTimeStyles) -> DateTime: ...
    
    @staticmethod
    def SpecifyKind(value: DateTime, kind: DateTimeKind) -> DateTime: ...
    
    @overload
    def Subtract(self, value: DateTime) -> TimeSpan: ...
    
    @overload
    def Subtract(self, value: TimeSpan) -> DateTime: ...
    
    def ToBinary(self) -> LongType: ...
    
    def ToFileTime(self) -> LongType: ...
    
    def ToFileTimeUtc(self) -> LongType: ...
    
    def ToLocalTime(self) -> DateTime: ...
    
    def ToLongDateString(self) -> StringType: ...
    
    def ToLongTimeString(self) -> StringType: ...
    
    def ToOADate(self) -> DoubleType: ...
    
    def ToShortDateString(self) -> StringType: ...
    
    def ToShortTimeString(self) -> StringType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType) -> StringType: ...
    
    @overload
    def ToString(self, provider: IFormatProvider) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType, provider: IFormatProvider) -> StringType: ...
    
    def ToUniversalTime(self) -> DateTime: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, result: DateTime) -> Tuple[BooleanType, DateTime]: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, provider: IFormatProvider, styles: DateTimeStyles, result: DateTime) -> Tuple[BooleanType, DateTime]: ...
    
    @staticmethod
    @overload
    def TryParseExact(s: StringType, format: StringType, provider: IFormatProvider, style: DateTimeStyles, result: DateTime) -> Tuple[BooleanType, DateTime]: ...
    
    @staticmethod
    @overload
    def TryParseExact(s: StringType, formats: ArrayType[StringType], provider: IFormatProvider, style: DateTimeStyles, result: DateTime) -> Tuple[BooleanType, DateTime]: ...
    
    def get_Date(self) -> DateTime: ...
    
    def get_Day(self) -> IntType: ...
    
    def get_DayOfWeek(self) -> DayOfWeek: ...
    
    def get_DayOfYear(self) -> IntType: ...
    
    def get_Hour(self) -> IntType: ...
    
    def get_Kind(self) -> DateTimeKind: ...
    
    def get_Millisecond(self) -> IntType: ...
    
    def get_Minute(self) -> IntType: ...
    
    def get_Month(self) -> IntType: ...
    
    @staticmethod
    def get_Now() -> DateTime: ...
    
    def get_Second(self) -> IntType: ...
    
    def get_Ticks(self) -> LongType: ...
    
    def get_TimeOfDay(self) -> TimeSpan: ...
    
    @staticmethod
    def get_Today() -> DateTime: ...
    
    @staticmethod
    def get_UtcNow() -> DateTime: ...
    
    def get_Year(self) -> IntType: ...
    
    @staticmethod
    def op_Addition(d: DateTime, t: TimeSpan) -> DateTime: ...
    
    @staticmethod
    def op_Equality(d1: DateTime, d2: DateTime) -> BooleanType: ...
    
    @staticmethod
    def op_GreaterThan(t1: DateTime, t2: DateTime) -> BooleanType: ...
    
    @staticmethod
    def op_GreaterThanOrEqual(t1: DateTime, t2: DateTime) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(d1: DateTime, d2: DateTime) -> BooleanType: ...
    
    @staticmethod
    def op_LessThan(t1: DateTime, t2: DateTime) -> BooleanType: ...
    
    @staticmethod
    def op_LessThanOrEqual(t1: DateTime, t2: DateTime) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Subtraction(d: DateTime, t: TimeSpan) -> DateTime: ...
    
    @staticmethod
    @overload
    def op_Subtraction(d1: DateTime, d2: DateTime) -> TimeSpan: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DateTimeOffset(ValueType, IComparable, IFormattable, ISerializable, IDeserializationCallback, IComparable[DateTimeOffset], IEquatable[DateTimeOffset]):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def MaxValue() -> DateTimeOffset: ...
    
    @staticmethod
    @property
    def MinValue() -> DateTimeOffset: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, ticks: LongType, offset: TimeSpan): ...
    
    @overload
    def __init__(self, dateTime: DateTime): ...
    
    @overload
    def __init__(self, dateTime: DateTime, offset: TimeSpan): ...
    
    @overload
    def __init__(self, year: IntType, month: IntType, day: IntType, hour: IntType, minute: IntType, second: IntType, offset: TimeSpan): ...
    
    @overload
    def __init__(self, year: IntType, month: IntType, day: IntType, hour: IntType, minute: IntType, second: IntType, millisecond: IntType, offset: TimeSpan): ...
    
    @overload
    def __init__(self, year: IntType, month: IntType, day: IntType, hour: IntType, minute: IntType, second: IntType, millisecond: IntType, calendar: Calendar, offset: TimeSpan): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Date(self) -> DateTime: ...
    
    @property
    def DateTime(self) -> DateTime: ...
    
    @property
    def Day(self) -> IntType: ...
    
    @property
    def DayOfWeek(self) -> DayOfWeek: ...
    
    @property
    def DayOfYear(self) -> IntType: ...
    
    @property
    def Hour(self) -> IntType: ...
    
    @property
    def LocalDateTime(self) -> DateTime: ...
    
    @property
    def Millisecond(self) -> IntType: ...
    
    @property
    def Minute(self) -> IntType: ...
    
    @property
    def Month(self) -> IntType: ...
    
    @staticmethod
    @property
    def Now() -> DateTimeOffset: ...
    
    @property
    def Offset(self) -> TimeSpan: ...
    
    @property
    def Second(self) -> IntType: ...
    
    @property
    def Ticks(self) -> LongType: ...
    
    @property
    def TimeOfDay(self) -> TimeSpan: ...
    
    @property
    def UtcDateTime(self) -> DateTime: ...
    
    @staticmethod
    @property
    def UtcNow() -> DateTimeOffset: ...
    
    @property
    def UtcTicks(self) -> LongType: ...
    
    @property
    def Year(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, timeSpan: TimeSpan) -> DateTimeOffset: ...
    
    def AddDays(self, days: DoubleType) -> DateTimeOffset: ...
    
    def AddHours(self, hours: DoubleType) -> DateTimeOffset: ...
    
    def AddMilliseconds(self, milliseconds: DoubleType) -> DateTimeOffset: ...
    
    def AddMinutes(self, minutes: DoubleType) -> DateTimeOffset: ...
    
    def AddMonths(self, months: IntType) -> DateTimeOffset: ...
    
    def AddSeconds(self, seconds: DoubleType) -> DateTimeOffset: ...
    
    def AddTicks(self, ticks: LongType) -> DateTimeOffset: ...
    
    def AddYears(self, years: IntType) -> DateTimeOffset: ...
    
    @staticmethod
    def Compare(first: DateTimeOffset, second: DateTimeOffset) -> IntType: ...
    
    def CompareTo(self, other: DateTimeOffset) -> IntType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: DateTimeOffset) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Equals(first: DateTimeOffset, second: DateTimeOffset) -> BooleanType: ...
    
    def EqualsExact(self, other: DateTimeOffset) -> BooleanType: ...
    
    @staticmethod
    def FromFileTime(fileTime: LongType) -> DateTimeOffset: ...
    
    @staticmethod
    def FromUnixTimeMilliseconds(milliseconds: LongType) -> DateTimeOffset: ...
    
    @staticmethod
    def FromUnixTimeSeconds(seconds: LongType) -> DateTimeOffset: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    @overload
    def Parse(input: StringType) -> DateTimeOffset: ...
    
    @staticmethod
    @overload
    def Parse(input: StringType, formatProvider: IFormatProvider) -> DateTimeOffset: ...
    
    @staticmethod
    @overload
    def Parse(input: StringType, formatProvider: IFormatProvider, styles: DateTimeStyles) -> DateTimeOffset: ...
    
    @staticmethod
    @overload
    def ParseExact(input: StringType, format: StringType, formatProvider: IFormatProvider) -> DateTimeOffset: ...
    
    @staticmethod
    @overload
    def ParseExact(input: StringType, format: StringType, formatProvider: IFormatProvider, styles: DateTimeStyles) -> DateTimeOffset: ...
    
    @staticmethod
    @overload
    def ParseExact(input: StringType, formats: ArrayType[StringType], formatProvider: IFormatProvider, styles: DateTimeStyles) -> DateTimeOffset: ...
    
    @overload
    def Subtract(self, value: DateTimeOffset) -> TimeSpan: ...
    
    @overload
    def Subtract(self, value: TimeSpan) -> DateTimeOffset: ...
    
    def ToFileTime(self) -> LongType: ...
    
    def ToLocalTime(self) -> DateTimeOffset: ...
    
    def ToOffset(self, offset: TimeSpan) -> DateTimeOffset: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType) -> StringType: ...
    
    @overload
    def ToString(self, formatProvider: IFormatProvider) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType, formatProvider: IFormatProvider) -> StringType: ...
    
    def ToUniversalTime(self) -> DateTimeOffset: ...
    
    def ToUnixTimeMilliseconds(self) -> LongType: ...
    
    def ToUnixTimeSeconds(self) -> LongType: ...
    
    @staticmethod
    @overload
    def TryParse(input: StringType, result: DateTimeOffset) -> Tuple[BooleanType, DateTimeOffset]: ...
    
    @staticmethod
    @overload
    def TryParse(input: StringType, formatProvider: IFormatProvider, styles: DateTimeStyles, result: DateTimeOffset) -> Tuple[BooleanType, DateTimeOffset]: ...
    
    @staticmethod
    @overload
    def TryParseExact(input: StringType, format: StringType, formatProvider: IFormatProvider, styles: DateTimeStyles, result: DateTimeOffset) -> Tuple[BooleanType, DateTimeOffset]: ...
    
    @staticmethod
    @overload
    def TryParseExact(input: StringType, formats: ArrayType[StringType], formatProvider: IFormatProvider, styles: DateTimeStyles, result: DateTimeOffset) -> Tuple[BooleanType, DateTimeOffset]: ...
    
    def get_Date(self) -> DateTime: ...
    
    def get_DateTime(self) -> DateTime: ...
    
    def get_Day(self) -> IntType: ...
    
    def get_DayOfWeek(self) -> DayOfWeek: ...
    
    def get_DayOfYear(self) -> IntType: ...
    
    def get_Hour(self) -> IntType: ...
    
    def get_LocalDateTime(self) -> DateTime: ...
    
    def get_Millisecond(self) -> IntType: ...
    
    def get_Minute(self) -> IntType: ...
    
    def get_Month(self) -> IntType: ...
    
    @staticmethod
    def get_Now() -> DateTimeOffset: ...
    
    def get_Offset(self) -> TimeSpan: ...
    
    def get_Second(self) -> IntType: ...
    
    def get_Ticks(self) -> LongType: ...
    
    def get_TimeOfDay(self) -> TimeSpan: ...
    
    def get_UtcDateTime(self) -> DateTime: ...
    
    @staticmethod
    def get_UtcNow() -> DateTimeOffset: ...
    
    def get_UtcTicks(self) -> LongType: ...
    
    def get_Year(self) -> IntType: ...
    
    @staticmethod
    def op_Addition(dateTimeOffset: DateTimeOffset, timeSpan: TimeSpan) -> DateTimeOffset: ...
    
    @staticmethod
    def op_Equality(left: DateTimeOffset, right: DateTimeOffset) -> BooleanType: ...
    
    @staticmethod
    def op_GreaterThan(left: DateTimeOffset, right: DateTimeOffset) -> BooleanType: ...
    
    @staticmethod
    def op_GreaterThanOrEqual(left: DateTimeOffset, right: DateTimeOffset) -> BooleanType: ...
    
    @staticmethod
    def op_Implicit(dateTime: DateTime) -> DateTimeOffset: ...
    
    @staticmethod
    def op_Inequality(left: DateTimeOffset, right: DateTimeOffset) -> BooleanType: ...
    
    @staticmethod
    def op_LessThan(left: DateTimeOffset, right: DateTimeOffset) -> BooleanType: ...
    
    @staticmethod
    def op_LessThanOrEqual(left: DateTimeOffset, right: DateTimeOffset) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Subtraction(dateTimeOffset: DateTimeOffset, timeSpan: TimeSpan) -> DateTimeOffset: ...
    
    @staticmethod
    @overload
    def op_Subtraction(left: DateTimeOffset, right: DateTimeOffset) -> TimeSpan: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DateTimeRawInfo(ValueType):
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


class DateTimeResult(ValueType):
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


class DateTimeToken(ValueType):
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


class Decimal(ValueType, IFormattable, IComparable, IConvertible, IDeserializationCallback, IComparable[DecimalType], IEquatable[DecimalType]):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def MaxValue() -> DecimalType: ...
    
    @staticmethod
    @property
    def MinValue() -> DecimalType: ...
    
    @staticmethod
    @property
    def MinusOne() -> DecimalType: ...
    
    @staticmethod
    @property
    def One() -> DecimalType: ...
    
    @staticmethod
    @property
    def Zero() -> DecimalType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, value: IntType): ...
    
    @overload
    def __init__(self, value: UIntType): ...
    
    @overload
    def __init__(self, value: LongType): ...
    
    @overload
    def __init__(self, value: ULongType): ...
    
    @overload
    def __init__(self, value: FloatType): ...
    
    @overload
    def __init__(self, value: DoubleType): ...
    
    @overload
    def __init__(self, bits: ArrayType[IntType]): ...
    
    @overload
    def __init__(self, lo: IntType, mid: IntType, hi: IntType, isNegative: BooleanType, scale: ByteType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Add(d1: DecimalType, d2: DecimalType) -> DecimalType: ...
    
    @staticmethod
    def Ceiling(d: DecimalType) -> DecimalType: ...
    
    @staticmethod
    def Compare(d1: DecimalType, d2: DecimalType) -> IntType: ...
    
    @overload
    def CompareTo(self, value: ObjectType) -> IntType: ...
    
    @overload
    def CompareTo(self, value: DecimalType) -> IntType: ...
    
    @staticmethod
    def Divide(d1: DecimalType, d2: DecimalType) -> DecimalType: ...
    
    @overload
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, value: DecimalType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Equals(d1: DecimalType, d2: DecimalType) -> BooleanType: ...
    
    @staticmethod
    def Floor(d: DecimalType) -> DecimalType: ...
    
    @staticmethod
    def FromOACurrency(cy: LongType) -> DecimalType: ...
    
    @staticmethod
    def GetBits(d: DecimalType) -> ArrayType[IntType]: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetTypeCode(self) -> TypeCode: ...
    
    @staticmethod
    def Multiply(d1: DecimalType, d2: DecimalType) -> DecimalType: ...
    
    @staticmethod
    def Negate(d: DecimalType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, style: NumberStyles) -> DecimalType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, provider: IFormatProvider) -> DecimalType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, style: NumberStyles, provider: IFormatProvider) -> DecimalType: ...
    
    @staticmethod
    def Remainder(d1: DecimalType, d2: DecimalType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def Round(d: DecimalType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def Round(d: DecimalType, decimals: IntType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def Round(d: DecimalType, mode: MidpointRounding) -> DecimalType: ...
    
    @staticmethod
    @overload
    def Round(d: DecimalType, decimals: IntType, mode: MidpointRounding) -> DecimalType: ...
    
    @staticmethod
    def Subtract(d1: DecimalType, d2: DecimalType) -> DecimalType: ...
    
    @staticmethod
    def ToByte(value: DecimalType) -> ByteType: ...
    
    @staticmethod
    def ToDouble(d: DecimalType) -> DoubleType: ...
    
    @staticmethod
    def ToInt16(value: DecimalType) -> ShortType: ...
    
    @staticmethod
    def ToInt32(d: DecimalType) -> IntType: ...
    
    @staticmethod
    def ToInt64(d: DecimalType) -> LongType: ...
    
    @staticmethod
    def ToOACurrency(value: DecimalType) -> LongType: ...
    
    @staticmethod
    def ToSByte(value: DecimalType) -> SByteType: ...
    
    @staticmethod
    def ToSingle(d: DecimalType) -> FloatType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType) -> StringType: ...
    
    @overload
    def ToString(self, provider: IFormatProvider) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    def ToUInt16(value: DecimalType) -> UShortType: ...
    
    @staticmethod
    def ToUInt32(d: DecimalType) -> UIntType: ...
    
    @staticmethod
    def ToUInt64(d: DecimalType) -> ULongType: ...
    
    @staticmethod
    def Truncate(d: DecimalType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, result: DecimalType) -> Tuple[BooleanType, DecimalType]: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, style: NumberStyles, provider: IFormatProvider, result: DecimalType) -> Tuple[BooleanType, DecimalType]: ...
    
    @staticmethod
    def op_Addition(d1: DecimalType, d2: DecimalType) -> DecimalType: ...
    
    @staticmethod
    def op_Decrement(d: DecimalType) -> DecimalType: ...
    
    @staticmethod
    def op_Division(d1: DecimalType, d2: DecimalType) -> DecimalType: ...
    
    @staticmethod
    def op_Equality(d1: DecimalType, d2: DecimalType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: FloatType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: DoubleType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: DecimalType) -> ByteType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: DecimalType) -> SByteType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: DecimalType) -> CharType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: DecimalType) -> ShortType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: DecimalType) -> UShortType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: DecimalType) -> IntType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: DecimalType) -> UIntType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: DecimalType) -> LongType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: DecimalType) -> ULongType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: DecimalType) -> FloatType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: DecimalType) -> DoubleType: ...
    
    @staticmethod
    def op_GreaterThan(d1: DecimalType, d2: DecimalType) -> BooleanType: ...
    
    @staticmethod
    def op_GreaterThanOrEqual(d1: DecimalType, d2: DecimalType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: ByteType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: SByteType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: ShortType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: UShortType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: CharType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: IntType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: UIntType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: LongType) -> DecimalType: ...
    
    @staticmethod
    @overload
    def op_Implicit(value: ULongType) -> DecimalType: ...
    
    @staticmethod
    def op_Increment(d: DecimalType) -> DecimalType: ...
    
    @staticmethod
    def op_Inequality(d1: DecimalType, d2: DecimalType) -> BooleanType: ...
    
    @staticmethod
    def op_LessThan(d1: DecimalType, d2: DecimalType) -> BooleanType: ...
    
    @staticmethod
    def op_LessThanOrEqual(d1: DecimalType, d2: DecimalType) -> BooleanType: ...
    
    @staticmethod
    def op_Modulus(d1: DecimalType, d2: DecimalType) -> DecimalType: ...
    
    @staticmethod
    def op_Multiply(d1: DecimalType, d2: DecimalType) -> DecimalType: ...
    
    @staticmethod
    def op_Subtraction(d1: DecimalType, d2: DecimalType) -> DecimalType: ...
    
    @staticmethod
    def op_UnaryNegation(d: DecimalType) -> DecimalType: ...
    
    @staticmethod
    def op_UnaryPlus(d: DecimalType) -> DecimalType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Double(ValueType, IComparable, IFormattable, IConvertible, IComparable[DoubleType], IEquatable[DoubleType]):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Epsilon() -> DoubleType: ...
    
    @staticmethod
    @property
    def MaxValue() -> DoubleType: ...
    
    @staticmethod
    @property
    def MinValue() -> DoubleType: ...
    
    @staticmethod
    @property
    def NaN() -> DoubleType: ...
    
    @staticmethod
    @property
    def NegativeInfinity() -> DoubleType: ...
    
    @staticmethod
    @property
    def PositiveInfinity() -> DoubleType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CompareTo(self, value: ObjectType) -> IntType: ...
    
    @overload
    def CompareTo(self, value: DoubleType) -> IntType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: DoubleType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetTypeCode(self) -> TypeCode: ...
    
    @staticmethod
    def IsInfinity(d: DoubleType) -> BooleanType: ...
    
    @staticmethod
    def IsNaN(d: DoubleType) -> BooleanType: ...
    
    @staticmethod
    def IsNegativeInfinity(d: DoubleType) -> BooleanType: ...
    
    @staticmethod
    def IsPositiveInfinity(d: DoubleType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, style: NumberStyles) -> DoubleType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, provider: IFormatProvider) -> DoubleType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, style: NumberStyles, provider: IFormatProvider) -> DoubleType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType) -> StringType: ...
    
    @overload
    def ToString(self, provider: IFormatProvider) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, result: DoubleType) -> Tuple[BooleanType, DoubleType]: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, style: NumberStyles, provider: IFormatProvider, result: DoubleType) -> Tuple[BooleanType, DoubleType]: ...
    
    @staticmethod
    def op_Equality(left: DoubleType, right: DoubleType) -> BooleanType: ...
    
    @staticmethod
    def op_GreaterThan(left: DoubleType, right: DoubleType) -> BooleanType: ...
    
    @staticmethod
    def op_GreaterThanOrEqual(left: DoubleType, right: DoubleType) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: DoubleType, right: DoubleType) -> BooleanType: ...
    
    @staticmethod
    def op_LessThan(left: DoubleType, right: DoubleType) -> BooleanType: ...
    
    @staticmethod
    def op_LessThanOrEqual(left: DoubleType, right: DoubleType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Guid(ValueType, IFormattable, IComparable, IComparable[Guid], IEquatable[Guid]):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Empty() -> Guid: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, b: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, a: UIntType, b: UShortType, c: UShortType, d: ByteType, e: ByteType, f: ByteType, g: ByteType, h: ByteType, i: ByteType, j: ByteType, k: ByteType): ...
    
    @overload
    def __init__(self, a: IntType, b: ShortType, c: ShortType, d: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, a: IntType, b: ShortType, c: ShortType, d: ByteType, e: ByteType, f: ByteType, g: ByteType, h: ByteType, i: ByteType, j: ByteType, k: ByteType): ...
    
    @overload
    def __init__(self, g: StringType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CompareTo(self, value: ObjectType) -> IntType: ...
    
    @overload
    def CompareTo(self, value: Guid) -> IntType: ...
    
    @overload
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, g: Guid) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    def NewGuid() -> Guid: ...
    
    @staticmethod
    def Parse(input: StringType) -> Guid: ...
    
    @staticmethod
    def ParseExact(input: StringType, format: StringType) -> Guid: ...
    
    def ToByteArray(self) -> ArrayType[ByteType]: ...
    
    @overload
    def ToString(self, format: StringType) -> StringType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    def TryParse(input: StringType, result: Guid) -> Tuple[BooleanType, Guid]: ...
    
    @staticmethod
    def TryParseExact(input: StringType, format: StringType, result: Guid) -> Tuple[BooleanType, Guid]: ...
    
    @staticmethod
    def op_Equality(a: Guid, b: Guid) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(a: Guid, b: Guid) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Int16(ValueType, IComparable, IFormattable, IConvertible, IComparable[ShortType], IEquatable[ShortType]):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def MaxValue() -> ShortType: ...
    
    @staticmethod
    @property
    def MinValue() -> ShortType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CompareTo(self, value: ObjectType) -> IntType: ...
    
    @overload
    def CompareTo(self, value: ShortType) -> IntType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: ShortType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetTypeCode(self) -> TypeCode: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType) -> ShortType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, style: NumberStyles) -> ShortType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, provider: IFormatProvider) -> ShortType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, style: NumberStyles, provider: IFormatProvider) -> ShortType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, provider: IFormatProvider) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, result: ShortType) -> Tuple[BooleanType, ShortType]: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, style: NumberStyles, provider: IFormatProvider, result: ShortType) -> Tuple[BooleanType, ShortType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Int32(ValueType, IComparable, IFormattable, IConvertible, IComparable[IntType], IEquatable[IntType]):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def MaxValue() -> IntType: ...
    
    @staticmethod
    @property
    def MinValue() -> IntType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CompareTo(self, value: ObjectType) -> IntType: ...
    
    @overload
    def CompareTo(self, value: IntType) -> IntType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: IntType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetTypeCode(self) -> TypeCode: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType) -> IntType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, style: NumberStyles) -> IntType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, provider: IFormatProvider) -> IntType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, style: NumberStyles, provider: IFormatProvider) -> IntType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType) -> StringType: ...
    
    @overload
    def ToString(self, provider: IFormatProvider) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, result: IntType) -> Tuple[BooleanType, IntType]: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, style: NumberStyles, provider: IFormatProvider, result: IntType) -> Tuple[BooleanType, IntType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Int64(ValueType, IComparable, IFormattable, IConvertible, IComparable[LongType], IEquatable[LongType]):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def MaxValue() -> LongType: ...
    
    @staticmethod
    @property
    def MinValue() -> LongType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CompareTo(self, value: ObjectType) -> IntType: ...
    
    @overload
    def CompareTo(self, value: LongType) -> IntType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: LongType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetTypeCode(self) -> TypeCode: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType) -> LongType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, style: NumberStyles) -> LongType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, provider: IFormatProvider) -> LongType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, style: NumberStyles, provider: IFormatProvider) -> LongType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, provider: IFormatProvider) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, result: LongType) -> Tuple[BooleanType, LongType]: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, style: NumberStyles, provider: IFormatProvider, result: LongType) -> Tuple[BooleanType, LongType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IntPtr(ValueType, ISerializable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Zero() -> NIntType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, value: IntType): ...
    
    @overload
    def __init__(self, value: LongType): ...
    
    @overload
    def __init__(self, value: VoidType): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Size() -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Add(pointer: NIntType, offset: IntType) -> NIntType: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    def Subtract(pointer: NIntType, offset: IntType) -> NIntType: ...
    
    def ToInt32(self) -> IntType: ...
    
    def ToInt64(self) -> LongType: ...
    
    def ToPointer(self) -> VoidType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType) -> StringType: ...
    
    @staticmethod
    def get_Size() -> IntType: ...
    
    @staticmethod
    def op_Addition(pointer: NIntType, offset: IntType) -> NIntType: ...
    
    @staticmethod
    def op_Equality(value1: NIntType, value2: NIntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: IntType) -> NIntType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: LongType) -> NIntType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: VoidType) -> NIntType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: NIntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: NIntType) -> IntType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: NIntType) -> LongType: ...
    
    @staticmethod
    def op_Inequality(value1: NIntType, value2: NIntType) -> BooleanType: ...
    
    @staticmethod
    def op_Subtraction(pointer: NIntType, offset: IntType) -> NIntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ModuleHandle(ValueType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def EmptyHandle() -> ModuleHandle: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def MDStreamVersion(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, handle: ModuleHandle) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetRuntimeFieldHandleFromMetadataToken(self, fieldToken: IntType) -> RuntimeFieldHandle: ...
    
    def GetRuntimeMethodHandleFromMetadataToken(self, methodToken: IntType) -> RuntimeMethodHandle: ...
    
    def GetRuntimeTypeHandleFromMetadataToken(self, typeToken: IntType) -> RuntimeTypeHandle: ...
    
    @overload
    def ResolveFieldHandle(self, fieldToken: IntType) -> RuntimeFieldHandle: ...
    
    @overload
    def ResolveFieldHandle(self, fieldToken: IntType, typeInstantiationContext: ArrayType[RuntimeTypeHandle], methodInstantiationContext: ArrayType[RuntimeTypeHandle]) -> RuntimeFieldHandle: ...
    
    @overload
    def ResolveMethodHandle(self, methodToken: IntType) -> RuntimeMethodHandle: ...
    
    @overload
    def ResolveMethodHandle(self, methodToken: IntType, typeInstantiationContext: ArrayType[RuntimeTypeHandle], methodInstantiationContext: ArrayType[RuntimeTypeHandle]) -> RuntimeMethodHandle: ...
    
    @overload
    def ResolveTypeHandle(self, typeToken: IntType) -> RuntimeTypeHandle: ...
    
    @overload
    def ResolveTypeHandle(self, typeToken: IntType, typeInstantiationContext: ArrayType[RuntimeTypeHandle], methodInstantiationContext: ArrayType[RuntimeTypeHandle]) -> RuntimeTypeHandle: ...
    
    def get_MDStreamVersion(self) -> IntType: ...
    
    @staticmethod
    def op_Equality(left: ModuleHandle, right: ModuleHandle) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: ModuleHandle, right: ModuleHandle) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Nullable(Generic[T], ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, value: T): ...
    
    # ---------- Properties ---------- #
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def Value(self) -> T: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, other: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @overload
    def GetValueOrDefault(self) -> T: ...
    
    @overload
    def GetValueOrDefault(self, defaultValue: T) -> T: ...
    
    def ToString(self) -> StringType: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_Value(self) -> T: ...
    
    @staticmethod
    def op_Explicit(value: Nullable[T]) -> T: ...
    
    @staticmethod
    def op_Implicit(value: T) -> Nullable[T]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ParamsArray(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, arg0: ObjectType): ...
    
    @overload
    def __init__(self, arg0: ObjectType, arg1: ObjectType): ...
    
    @overload
    def __init__(self, arg0: ObjectType, arg1: ObjectType, arg2: ObjectType): ...
    
    @overload
    def __init__(self, args: ArrayType[ObjectType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> ObjectType: ...
    
    @property
    def Length(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_Item(self, index: IntType) -> ObjectType: ...
    
    def get_Length(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ParsingInfo(ValueType):
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


class RuntimeArgumentHandle(ValueType):
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


class RuntimeFieldHandle(ValueType, ISerializable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> NIntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, handle: RuntimeFieldHandle) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_Value(self) -> NIntType: ...
    
    @staticmethod
    def op_Equality(left: RuntimeFieldHandle, right: RuntimeFieldHandle) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: RuntimeFieldHandle, right: RuntimeFieldHandle) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RuntimeFieldHandleInternal(ValueType):
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


class RuntimeMethodHandle(ValueType, ISerializable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> NIntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, handle: RuntimeMethodHandle) -> BooleanType: ...
    
    def GetFunctionPointer(self) -> NIntType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_Value(self) -> NIntType: ...
    
    @staticmethod
    def op_Equality(left: RuntimeMethodHandle, right: RuntimeMethodHandle) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: RuntimeMethodHandle, right: RuntimeMethodHandle) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RuntimeMethodHandleInternal(ValueType):
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


class RuntimeTypeHandle(ValueType, ISerializable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> NIntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, handle: RuntimeTypeHandle) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetModuleHandle(self) -> ModuleHandle: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_Value(self) -> NIntType: ...
    
    @staticmethod
    @overload
    def op_Equality(left: RuntimeTypeHandle, right: ObjectType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Equality(left: ObjectType, right: RuntimeTypeHandle) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Inequality(left: RuntimeTypeHandle, right: ObjectType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Inequality(left: ObjectType, right: RuntimeTypeHandle) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SByte(ValueType, IComparable, IFormattable, IConvertible, IComparable[SByteType], IEquatable[SByteType]):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def MaxValue() -> SByteType: ...
    
    @staticmethod
    @property
    def MinValue() -> SByteType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CompareTo(self, obj: ObjectType) -> IntType: ...
    
    @overload
    def CompareTo(self, value: SByteType) -> IntType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: SByteType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetTypeCode(self) -> TypeCode: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType) -> SByteType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, style: NumberStyles) -> SByteType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, provider: IFormatProvider) -> SByteType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, style: NumberStyles, provider: IFormatProvider) -> SByteType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, provider: IFormatProvider) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, result: SByteType) -> Tuple[BooleanType, SByteType]: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, style: NumberStyles, provider: IFormatProvider, result: SByteType) -> Tuple[BooleanType, SByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Single(ValueType, IComparable, IFormattable, IConvertible, IComparable[FloatType], IEquatable[FloatType]):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Epsilon() -> FloatType: ...
    
    @staticmethod
    @property
    def MaxValue() -> FloatType: ...
    
    @staticmethod
    @property
    def MinValue() -> FloatType: ...
    
    @staticmethod
    @property
    def NaN() -> FloatType: ...
    
    @staticmethod
    @property
    def NegativeInfinity() -> FloatType: ...
    
    @staticmethod
    @property
    def PositiveInfinity() -> FloatType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CompareTo(self, value: ObjectType) -> IntType: ...
    
    @overload
    def CompareTo(self, value: FloatType) -> IntType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: FloatType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetTypeCode(self) -> TypeCode: ...
    
    @staticmethod
    def IsInfinity(f: FloatType) -> BooleanType: ...
    
    @staticmethod
    def IsNaN(f: FloatType) -> BooleanType: ...
    
    @staticmethod
    def IsNegativeInfinity(f: FloatType) -> BooleanType: ...
    
    @staticmethod
    def IsPositiveInfinity(f: FloatType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType) -> FloatType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, style: NumberStyles) -> FloatType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, provider: IFormatProvider) -> FloatType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, style: NumberStyles, provider: IFormatProvider) -> FloatType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, provider: IFormatProvider) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, result: FloatType) -> Tuple[BooleanType, FloatType]: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, style: NumberStyles, provider: IFormatProvider, result: FloatType) -> Tuple[BooleanType, FloatType]: ...
    
    @staticmethod
    def op_Equality(left: FloatType, right: FloatType) -> BooleanType: ...
    
    @staticmethod
    def op_GreaterThan(left: FloatType, right: FloatType) -> BooleanType: ...
    
    @staticmethod
    def op_GreaterThanOrEqual(left: FloatType, right: FloatType) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: FloatType, right: FloatType) -> BooleanType: ...
    
    @staticmethod
    def op_LessThan(left: FloatType, right: FloatType) -> BooleanType: ...
    
    @staticmethod
    def op_LessThanOrEqual(left: FloatType, right: FloatType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SwitchStructure(ValueType):
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


class TimeSpan(ValueType, IComparable, IComparable[TimeSpan], IEquatable[TimeSpan], IFormattable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def MaxValue() -> TimeSpan: ...
    
    @staticmethod
    @property
    def MinValue() -> TimeSpan: ...
    
    @staticmethod
    @property
    def TicksPerDay() -> LongType: ...
    
    @staticmethod
    @property
    def TicksPerHour() -> LongType: ...
    
    @staticmethod
    @property
    def TicksPerMillisecond() -> LongType: ...
    
    @staticmethod
    @property
    def TicksPerMinute() -> LongType: ...
    
    @staticmethod
    @property
    def TicksPerSecond() -> LongType: ...
    
    @staticmethod
    @property
    def Zero() -> TimeSpan: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, ticks: LongType): ...
    
    @overload
    def __init__(self, hours: IntType, minutes: IntType, seconds: IntType): ...
    
    @overload
    def __init__(self, days: IntType, hours: IntType, minutes: IntType, seconds: IntType): ...
    
    @overload
    def __init__(self, days: IntType, hours: IntType, minutes: IntType, seconds: IntType, milliseconds: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Days(self) -> IntType: ...
    
    @property
    def Hours(self) -> IntType: ...
    
    @property
    def Milliseconds(self) -> IntType: ...
    
    @property
    def Minutes(self) -> IntType: ...
    
    @property
    def Seconds(self) -> IntType: ...
    
    @property
    def Ticks(self) -> LongType: ...
    
    @property
    def TotalDays(self) -> DoubleType: ...
    
    @property
    def TotalHours(self) -> DoubleType: ...
    
    @property
    def TotalMilliseconds(self) -> DoubleType: ...
    
    @property
    def TotalMinutes(self) -> DoubleType: ...
    
    @property
    def TotalSeconds(self) -> DoubleType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, ts: TimeSpan) -> TimeSpan: ...
    
    @staticmethod
    def Compare(t1: TimeSpan, t2: TimeSpan) -> IntType: ...
    
    @overload
    def CompareTo(self, value: ObjectType) -> IntType: ...
    
    @overload
    def CompareTo(self, value: TimeSpan) -> IntType: ...
    
    def Duration(self) -> TimeSpan: ...
    
    @overload
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: TimeSpan) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Equals(t1: TimeSpan, t2: TimeSpan) -> BooleanType: ...
    
    @staticmethod
    def FromDays(value: DoubleType) -> TimeSpan: ...
    
    @staticmethod
    def FromHours(value: DoubleType) -> TimeSpan: ...
    
    @staticmethod
    def FromMilliseconds(value: DoubleType) -> TimeSpan: ...
    
    @staticmethod
    def FromMinutes(value: DoubleType) -> TimeSpan: ...
    
    @staticmethod
    def FromSeconds(value: DoubleType) -> TimeSpan: ...
    
    @staticmethod
    def FromTicks(value: LongType) -> TimeSpan: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def Negate(self) -> TimeSpan: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType) -> TimeSpan: ...
    
    @staticmethod
    @overload
    def Parse(input: StringType, formatProvider: IFormatProvider) -> TimeSpan: ...
    
    @staticmethod
    @overload
    def ParseExact(input: StringType, format: StringType, formatProvider: IFormatProvider) -> TimeSpan: ...
    
    @staticmethod
    @overload
    def ParseExact(input: StringType, formats: ArrayType[StringType], formatProvider: IFormatProvider) -> TimeSpan: ...
    
    @staticmethod
    @overload
    def ParseExact(input: StringType, format: StringType, formatProvider: IFormatProvider, styles: TimeSpanStyles) -> TimeSpan: ...
    
    @staticmethod
    @overload
    def ParseExact(input: StringType, formats: ArrayType[StringType], formatProvider: IFormatProvider, styles: TimeSpanStyles) -> TimeSpan: ...
    
    def Subtract(self, ts: TimeSpan) -> TimeSpan: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType, formatProvider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, result: TimeSpan) -> Tuple[BooleanType, TimeSpan]: ...
    
    @staticmethod
    @overload
    def TryParse(input: StringType, formatProvider: IFormatProvider, result: TimeSpan) -> Tuple[BooleanType, TimeSpan]: ...
    
    @staticmethod
    @overload
    def TryParseExact(input: StringType, format: StringType, formatProvider: IFormatProvider, result: TimeSpan) -> Tuple[BooleanType, TimeSpan]: ...
    
    @staticmethod
    @overload
    def TryParseExact(input: StringType, formats: ArrayType[StringType], formatProvider: IFormatProvider, result: TimeSpan) -> Tuple[BooleanType, TimeSpan]: ...
    
    @staticmethod
    @overload
    def TryParseExact(input: StringType, format: StringType, formatProvider: IFormatProvider, styles: TimeSpanStyles, result: TimeSpan) -> Tuple[BooleanType, TimeSpan]: ...
    
    @staticmethod
    @overload
    def TryParseExact(input: StringType, formats: ArrayType[StringType], formatProvider: IFormatProvider, styles: TimeSpanStyles, result: TimeSpan) -> Tuple[BooleanType, TimeSpan]: ...
    
    def get_Days(self) -> IntType: ...
    
    def get_Hours(self) -> IntType: ...
    
    def get_Milliseconds(self) -> IntType: ...
    
    def get_Minutes(self) -> IntType: ...
    
    def get_Seconds(self) -> IntType: ...
    
    def get_Ticks(self) -> LongType: ...
    
    def get_TotalDays(self) -> DoubleType: ...
    
    def get_TotalHours(self) -> DoubleType: ...
    
    def get_TotalMilliseconds(self) -> DoubleType: ...
    
    def get_TotalMinutes(self) -> DoubleType: ...
    
    def get_TotalSeconds(self) -> DoubleType: ...
    
    @staticmethod
    def op_Addition(t1: TimeSpan, t2: TimeSpan) -> TimeSpan: ...
    
    @staticmethod
    def op_Equality(t1: TimeSpan, t2: TimeSpan) -> BooleanType: ...
    
    @staticmethod
    def op_GreaterThan(t1: TimeSpan, t2: TimeSpan) -> BooleanType: ...
    
    @staticmethod
    def op_GreaterThanOrEqual(t1: TimeSpan, t2: TimeSpan) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(t1: TimeSpan, t2: TimeSpan) -> BooleanType: ...
    
    @staticmethod
    def op_LessThan(t1: TimeSpan, t2: TimeSpan) -> BooleanType: ...
    
    @staticmethod
    def op_LessThanOrEqual(t1: TimeSpan, t2: TimeSpan) -> BooleanType: ...
    
    @staticmethod
    def op_Subtraction(t1: TimeSpan, t2: TimeSpan) -> TimeSpan: ...
    
    @staticmethod
    def op_UnaryNegation(t: TimeSpan) -> TimeSpan: ...
    
    @staticmethod
    def op_UnaryPlus(t: TimeSpan) -> TimeSpan: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypedReference(ValueType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    def GetTargetType(value: TypedReference) -> TypeType: ...
    
    @staticmethod
    def MakeTypedReference(target: ObjectType, flds: ArrayType[FieldInfo]) -> TypedReference: ...
    
    @staticmethod
    def SetTypedReference(target: TypedReference, value: ObjectType) -> VoidType: ...
    
    @staticmethod
    def TargetTypeToken(value: TypedReference) -> RuntimeTypeHandle: ...
    
    @staticmethod
    def ToObject(value: TypedReference) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UInt16(ValueType, IComparable, IFormattable, IConvertible, IComparable[UShortType], IEquatable[UShortType]):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def MaxValue() -> UShortType: ...
    
    @staticmethod
    @property
    def MinValue() -> UShortType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CompareTo(self, value: ObjectType) -> IntType: ...
    
    @overload
    def CompareTo(self, value: UShortType) -> IntType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: UShortType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetTypeCode(self) -> TypeCode: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType) -> UShortType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, style: NumberStyles) -> UShortType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, provider: IFormatProvider) -> UShortType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, style: NumberStyles, provider: IFormatProvider) -> UShortType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, provider: IFormatProvider) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, result: UShortType) -> Tuple[BooleanType, UShortType]: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, style: NumberStyles, provider: IFormatProvider, result: UShortType) -> Tuple[BooleanType, UShortType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UInt32(ValueType, IComparable, IFormattable, IConvertible, IComparable[UIntType], IEquatable[UIntType]):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def MaxValue() -> UIntType: ...
    
    @staticmethod
    @property
    def MinValue() -> UIntType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CompareTo(self, value: ObjectType) -> IntType: ...
    
    @overload
    def CompareTo(self, value: UIntType) -> IntType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: UIntType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetTypeCode(self) -> TypeCode: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType) -> UIntType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, style: NumberStyles) -> UIntType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, provider: IFormatProvider) -> UIntType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, style: NumberStyles, provider: IFormatProvider) -> UIntType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, provider: IFormatProvider) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, result: UIntType) -> Tuple[BooleanType, UIntType]: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, style: NumberStyles, provider: IFormatProvider, result: UIntType) -> Tuple[BooleanType, UIntType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UInt64(ValueType, IComparable, IFormattable, IConvertible, IComparable[ULongType], IEquatable[ULongType]):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def MaxValue() -> ULongType: ...
    
    @staticmethod
    @property
    def MinValue() -> ULongType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CompareTo(self, value: ObjectType) -> IntType: ...
    
    @overload
    def CompareTo(self, value: ULongType) -> IntType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: ULongType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetTypeCode(self) -> TypeCode: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType) -> ULongType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, style: NumberStyles) -> ULongType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, provider: IFormatProvider) -> ULongType: ...
    
    @staticmethod
    @overload
    def Parse(s: StringType, style: NumberStyles, provider: IFormatProvider) -> ULongType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, provider: IFormatProvider) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType) -> StringType: ...
    
    @overload
    def ToString(self, format: StringType, provider: IFormatProvider) -> StringType: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, result: ULongType) -> Tuple[BooleanType, ULongType]: ...
    
    @staticmethod
    @overload
    def TryParse(s: StringType, style: NumberStyles, provider: IFormatProvider, result: ULongType) -> Tuple[BooleanType, ULongType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UIntPtr(ValueType, ISerializable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Zero() -> NUIntType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, value: UIntType): ...
    
    @overload
    def __init__(self, value: ULongType): ...
    
    @overload
    def __init__(self, value: VoidType): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Size() -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Add(pointer: NUIntType, offset: IntType) -> NUIntType: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    def Subtract(pointer: NUIntType, offset: IntType) -> NUIntType: ...
    
    def ToPointer(self) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def ToUInt32(self) -> UIntType: ...
    
    def ToUInt64(self) -> ULongType: ...
    
    @staticmethod
    def get_Size() -> IntType: ...
    
    @staticmethod
    def op_Addition(pointer: NUIntType, offset: IntType) -> NUIntType: ...
    
    @staticmethod
    def op_Equality(value1: NUIntType, value2: NUIntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: ULongType) -> NUIntType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: NUIntType) -> UIntType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: UIntType) -> NUIntType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: NUIntType) -> ULongType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: VoidType) -> NUIntType: ...
    
    @staticmethod
    @overload
    def op_Explicit(value: NUIntType) -> VoidType: ...
    
    @staticmethod
    def op_Inequality(value1: NUIntType, value2: NUIntType) -> BooleanType: ...
    
    @staticmethod
    def op_Subtraction(pointer: NUIntType, offset: IntType) -> NUIntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnSafeCharBuffer(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, buffer: CharType, bufferSize: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Length(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def AppendString(self, stringToAppend: StringType) -> VoidType: ...
    
    def get_Length(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Utf8String(ValueType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ValueTuple(ValueType, IEquatable[ValueTuple], IStructuralEquatable, IStructuralComparable, IComparable, IComparable[ValueTuple], IValueTupleInternal, ITuple):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CompareTo(self, other: ValueTuple) -> IntType: ...
    
    @staticmethod
    @overload
    def Create() -> ValueTuple: ...
    
    @staticmethod
    @overload
    def Create(item1: T1) -> ValueTuple[T1]: ...
    
    @staticmethod
    @overload
    def Create(item1: T1, item2: T2) -> ValueTuple[T1, T2]: ...
    
    @staticmethod
    @overload
    def Create(item1: T1, item2: T2, item3: T3) -> ValueTuple[T1, T2, T3]: ...
    
    @staticmethod
    @overload
    def Create(item1: T1, item2: T2, item3: T3, item4: T4) -> ValueTuple[T1, T2, T3, T4]: ...
    
    @staticmethod
    @overload
    def Create(item1: T1, item2: T2, item3: T3, item4: T4, item5: T5) -> ValueTuple[T1, T2, T3, T4, T5]: ...
    
    @staticmethod
    @overload
    def Create(item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6) -> ValueTuple[T1, T2, T3, T4, T5, T6]: ...
    
    @staticmethod
    @overload
    def Create(item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7]: ...
    
    @staticmethod
    @overload
    def Create(item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7, item8: T8) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8]]: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: ValueTuple) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ValueTuple(Generic[T1], ValueType, IEquatable[ValueTuple[T1]], IStructuralEquatable, IStructuralComparable, IComparable, IComparable[ValueTuple[T1]], IValueTupleInternal, ITuple):
    # ---------- Fields ---------- #
    
    @property
    def Item1(self) -> T1: ...
    
    @Item1.setter
    def Item1(self, value: T1) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, item1: T1): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CompareTo(self, other: ValueTuple[T1]) -> IntType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: ValueTuple[T1]) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ValueTuple(Generic[T1, T2], ValueType, IEquatable[ValueTuple[T1, T2]], IStructuralEquatable, IStructuralComparable, IComparable, IComparable[ValueTuple[T1, T2]], IValueTupleInternal, ITuple):
    # ---------- Fields ---------- #
    
    @property
    def Item1(self) -> T1: ...
    
    @Item1.setter
    def Item1(self, value: T1) -> None: ...
    
    @property
    def Item2(self) -> T2: ...
    
    @Item2.setter
    def Item2(self, value: T2) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, item1: T1, item2: T2): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CompareTo(self, other: ValueTuple[T1, T2]) -> IntType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: ValueTuple[T1, T2]) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ValueTuple(Generic[T1, T2, T3], ValueType, IEquatable[ValueTuple[T1, T2, T3]], IStructuralEquatable, IStructuralComparable, IComparable, IComparable[ValueTuple[T1, T2, T3]], IValueTupleInternal, ITuple):
    # ---------- Fields ---------- #
    
    @property
    def Item1(self) -> T1: ...
    
    @Item1.setter
    def Item1(self, value: T1) -> None: ...
    
    @property
    def Item2(self) -> T2: ...
    
    @Item2.setter
    def Item2(self, value: T2) -> None: ...
    
    @property
    def Item3(self) -> T3: ...
    
    @Item3.setter
    def Item3(self, value: T3) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, item1: T1, item2: T2, item3: T3): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CompareTo(self, other: ValueTuple[T1, T2, T3]) -> IntType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: ValueTuple[T1, T2, T3]) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ValueTuple(Generic[T1, T2, T3, T4], ValueType, IEquatable[ValueTuple[T1, T2, T3, T4]], IStructuralEquatable, IStructuralComparable, IComparable, IComparable[ValueTuple[T1, T2, T3, T4]], IValueTupleInternal, ITuple):
    # ---------- Fields ---------- #
    
    @property
    def Item1(self) -> T1: ...
    
    @Item1.setter
    def Item1(self, value: T1) -> None: ...
    
    @property
    def Item2(self) -> T2: ...
    
    @Item2.setter
    def Item2(self, value: T2) -> None: ...
    
    @property
    def Item3(self) -> T3: ...
    
    @Item3.setter
    def Item3(self, value: T3) -> None: ...
    
    @property
    def Item4(self) -> T4: ...
    
    @Item4.setter
    def Item4(self, value: T4) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, item1: T1, item2: T2, item3: T3, item4: T4): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CompareTo(self, other: ValueTuple[T1, T2, T3, T4]) -> IntType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: ValueTuple[T1, T2, T3, T4]) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ValueTuple(Generic[T1, T2, T3, T4, T5], ValueType, IEquatable[ValueTuple[T1, T2, T3, T4, T5]], IStructuralEquatable, IStructuralComparable, IComparable, IComparable[ValueTuple[T1, T2, T3, T4, T5]], IValueTupleInternal, ITuple):
    # ---------- Fields ---------- #
    
    @property
    def Item1(self) -> T1: ...
    
    @Item1.setter
    def Item1(self, value: T1) -> None: ...
    
    @property
    def Item2(self) -> T2: ...
    
    @Item2.setter
    def Item2(self, value: T2) -> None: ...
    
    @property
    def Item3(self) -> T3: ...
    
    @Item3.setter
    def Item3(self, value: T3) -> None: ...
    
    @property
    def Item4(self) -> T4: ...
    
    @Item4.setter
    def Item4(self, value: T4) -> None: ...
    
    @property
    def Item5(self) -> T5: ...
    
    @Item5.setter
    def Item5(self, value: T5) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CompareTo(self, other: ValueTuple[T1, T2, T3, T4, T5]) -> IntType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: ValueTuple[T1, T2, T3, T4, T5]) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ValueTuple(Generic[T1, T2, T3, T4, T5, T6], ValueType, IEquatable[ValueTuple[T1, T2, T3, T4, T5, T6]], IStructuralEquatable, IStructuralComparable, IComparable, IComparable[ValueTuple[T1, T2, T3, T4, T5, T6]], IValueTupleInternal, ITuple):
    # ---------- Fields ---------- #
    
    @property
    def Item1(self) -> T1: ...
    
    @Item1.setter
    def Item1(self, value: T1) -> None: ...
    
    @property
    def Item2(self) -> T2: ...
    
    @Item2.setter
    def Item2(self, value: T2) -> None: ...
    
    @property
    def Item3(self) -> T3: ...
    
    @Item3.setter
    def Item3(self, value: T3) -> None: ...
    
    @property
    def Item4(self) -> T4: ...
    
    @Item4.setter
    def Item4(self, value: T4) -> None: ...
    
    @property
    def Item5(self) -> T5: ...
    
    @Item5.setter
    def Item5(self, value: T5) -> None: ...
    
    @property
    def Item6(self) -> T6: ...
    
    @Item6.setter
    def Item6(self, value: T6) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CompareTo(self, other: ValueTuple[T1, T2, T3, T4, T5, T6]) -> IntType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: ValueTuple[T1, T2, T3, T4, T5, T6]) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ValueTuple(Generic[T1, T2, T3, T4, T5, T6, T7], ValueType, IEquatable[ValueTuple[T1, T2, T3, T4, T5, T6, T7]], IStructuralEquatable, IStructuralComparable, IComparable, IComparable[ValueTuple[T1, T2, T3, T4, T5, T6, T7]], IValueTupleInternal, ITuple):
    # ---------- Fields ---------- #
    
    @property
    def Item1(self) -> T1: ...
    
    @Item1.setter
    def Item1(self, value: T1) -> None: ...
    
    @property
    def Item2(self) -> T2: ...
    
    @Item2.setter
    def Item2(self, value: T2) -> None: ...
    
    @property
    def Item3(self) -> T3: ...
    
    @Item3.setter
    def Item3(self, value: T3) -> None: ...
    
    @property
    def Item4(self) -> T4: ...
    
    @Item4.setter
    def Item4(self, value: T4) -> None: ...
    
    @property
    def Item5(self) -> T5: ...
    
    @Item5.setter
    def Item5(self, value: T5) -> None: ...
    
    @property
    def Item6(self) -> T6: ...
    
    @Item6.setter
    def Item6(self, value: T6) -> None: ...
    
    @property
    def Item7(self) -> T7: ...
    
    @Item7.setter
    def Item7(self, value: T7) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CompareTo(self, other: ValueTuple[T1, T2, T3, T4, T5, T6, T7]) -> IntType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: ValueTuple[T1, T2, T3, T4, T5, T6, T7]) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ValueTuple(Generic[T1, T2, T3, T4, T5, T6, T7, TRest], ValueType, IEquatable[ValueTuple[T1, T2, T3, T4, T5, T6, T7, TRest]], IStructuralEquatable, IStructuralComparable, IComparable, IComparable[ValueTuple[T1, T2, T3, T4, T5, T6, T7, TRest]], IValueTupleInternal, ITuple):
    # ---------- Fields ---------- #
    
    @property
    def Item1(self) -> T1: ...
    
    @Item1.setter
    def Item1(self, value: T1) -> None: ...
    
    @property
    def Item2(self) -> T2: ...
    
    @Item2.setter
    def Item2(self, value: T2) -> None: ...
    
    @property
    def Item3(self) -> T3: ...
    
    @Item3.setter
    def Item3(self, value: T3) -> None: ...
    
    @property
    def Item4(self) -> T4: ...
    
    @Item4.setter
    def Item4(self, value: T4) -> None: ...
    
    @property
    def Item5(self) -> T5: ...
    
    @Item5.setter
    def Item5(self, value: T5) -> None: ...
    
    @property
    def Item6(self) -> T6: ...
    
    @Item6.setter
    def Item6(self, value: T6) -> None: ...
    
    @property
    def Item7(self) -> T7: ...
    
    @Item7.setter
    def Item7(self, value: T7) -> None: ...
    
    @property
    def Rest(self) -> TRest: ...
    
    @Rest.setter
    def Rest(self, value: TRest) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7, rest: TRest): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CompareTo(self, other: ValueTuple[T1, T2, T3, T4, T5, T6, T7, TRest]) -> IntType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: ValueTuple[T1, T2, T3, T4, T5, T6, T7, TRest]) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Variant(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, val: BooleanType): ...
    
    @overload
    def __init__(self, val: SByteType): ...
    
    @overload
    def __init__(self, val: ByteType): ...
    
    @overload
    def __init__(self, val: ShortType): ...
    
    @overload
    def __init__(self, val: UShortType): ...
    
    @overload
    def __init__(self, val: CharType): ...
    
    @overload
    def __init__(self, val: IntType): ...
    
    @overload
    def __init__(self, val: UIntType): ...
    
    @overload
    def __init__(self, val: LongType): ...
    
    @overload
    def __init__(self, val: ULongType): ...
    
    @overload
    def __init__(self, val: FloatType): ...
    
    @overload
    def __init__(self, val: DoubleType): ...
    
    @overload
    def __init__(self, val: DateTime): ...
    
    @overload
    def __init__(self, val: DecimalType): ...
    
    @overload
    def __init__(self, obj: ObjectType): ...
    
    @overload
    def __init__(self, voidPointer: VoidType, pointerType: TypeType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ToObject(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Void(ValueType):
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


class __DTString(ValueType):
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

class IAppDomainSetup(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def ApplicationBase(self) -> StringType: ...
    
    @ApplicationBase.setter
    def ApplicationBase(self, value: StringType) -> None: ...
    
    @property
    def ApplicationName(self) -> StringType: ...
    
    @ApplicationName.setter
    def ApplicationName(self, value: StringType) -> None: ...
    
    @property
    def CachePath(self) -> StringType: ...
    
    @CachePath.setter
    def CachePath(self, value: StringType) -> None: ...
    
    @property
    def ConfigurationFile(self) -> StringType: ...
    
    @ConfigurationFile.setter
    def ConfigurationFile(self, value: StringType) -> None: ...
    
    @property
    def DynamicBase(self) -> StringType: ...
    
    @DynamicBase.setter
    def DynamicBase(self, value: StringType) -> None: ...
    
    @property
    def LicenseFile(self) -> StringType: ...
    
    @LicenseFile.setter
    def LicenseFile(self, value: StringType) -> None: ...
    
    @property
    def PrivateBinPath(self) -> StringType: ...
    
    @PrivateBinPath.setter
    def PrivateBinPath(self, value: StringType) -> None: ...
    
    @property
    def PrivateBinPathProbe(self) -> StringType: ...
    
    @PrivateBinPathProbe.setter
    def PrivateBinPathProbe(self, value: StringType) -> None: ...
    
    @property
    def ShadowCopyDirectories(self) -> StringType: ...
    
    @ShadowCopyDirectories.setter
    def ShadowCopyDirectories(self, value: StringType) -> None: ...
    
    @property
    def ShadowCopyFiles(self) -> StringType: ...
    
    @ShadowCopyFiles.setter
    def ShadowCopyFiles(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ApplicationBase(self) -> StringType: ...
    
    def get_ApplicationName(self) -> StringType: ...
    
    def get_CachePath(self) -> StringType: ...
    
    def get_ConfigurationFile(self) -> StringType: ...
    
    def get_DynamicBase(self) -> StringType: ...
    
    def get_LicenseFile(self) -> StringType: ...
    
    def get_PrivateBinPath(self) -> StringType: ...
    
    def get_PrivateBinPathProbe(self) -> StringType: ...
    
    def get_ShadowCopyDirectories(self) -> StringType: ...
    
    def get_ShadowCopyFiles(self) -> StringType: ...
    
    def set_ApplicationBase(self, value: StringType) -> VoidType: ...
    
    def set_ApplicationName(self, value: StringType) -> VoidType: ...
    
    def set_CachePath(self, value: StringType) -> VoidType: ...
    
    def set_ConfigurationFile(self, value: StringType) -> VoidType: ...
    
    def set_DynamicBase(self, value: StringType) -> VoidType: ...
    
    def set_LicenseFile(self, value: StringType) -> VoidType: ...
    
    def set_PrivateBinPath(self, value: StringType) -> VoidType: ...
    
    def set_PrivateBinPathProbe(self, value: StringType) -> VoidType: ...
    
    def set_ShadowCopyDirectories(self, value: StringType) -> VoidType: ...
    
    def set_ShadowCopyFiles(self, value: StringType) -> VoidType: ...
    
    # No Events


class IAsyncResult(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AsyncState(self) -> ObjectType: ...
    
    @property
    def AsyncWaitHandle(self) -> WaitHandle: ...
    
    @property
    def CompletedSynchronously(self) -> BooleanType: ...
    
    @property
    def IsCompleted(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_AsyncState(self) -> ObjectType: ...
    
    def get_AsyncWaitHandle(self) -> WaitHandle: ...
    
    def get_CompletedSynchronously(self) -> BooleanType: ...
    
    def get_IsCompleted(self) -> BooleanType: ...
    
    # No Events


class ICloneable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ObjectType: ...
    
    # No Events


class IComparable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CompareTo(self, obj: ObjectType) -> IntType: ...
    
    # No Events


class IComparable(Protocol[T]):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CompareTo(self, other: T) -> IntType: ...
    
    # No Events


class IConvertible(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetTypeCode(self) -> TypeCode: ...
    
    def ToBoolean(self, provider: IFormatProvider) -> BooleanType: ...
    
    def ToByte(self, provider: IFormatProvider) -> ByteType: ...
    
    def ToChar(self, provider: IFormatProvider) -> CharType: ...
    
    def ToDateTime(self, provider: IFormatProvider) -> DateTime: ...
    
    def ToDecimal(self, provider: IFormatProvider) -> DecimalType: ...
    
    def ToDouble(self, provider: IFormatProvider) -> DoubleType: ...
    
    def ToInt16(self, provider: IFormatProvider) -> ShortType: ...
    
    def ToInt32(self, provider: IFormatProvider) -> IntType: ...
    
    def ToInt64(self, provider: IFormatProvider) -> LongType: ...
    
    def ToSByte(self, provider: IFormatProvider) -> SByteType: ...
    
    def ToSingle(self, provider: IFormatProvider) -> FloatType: ...
    
    def ToString(self, provider: IFormatProvider) -> StringType: ...
    
    def ToType(self, conversionType: TypeType, provider: IFormatProvider) -> ObjectType: ...
    
    def ToUInt16(self, provider: IFormatProvider) -> UShortType: ...
    
    def ToUInt32(self, provider: IFormatProvider) -> UIntType: ...
    
    def ToUInt64(self, provider: IFormatProvider) -> ULongType: ...
    
    # No Events


class ICustomFormatter(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Format(self, format: StringType, arg: ObjectType, formatProvider: IFormatProvider) -> StringType: ...
    
    # No Events


class IDisposable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    # No Events


class IEquatable(Protocol[T]):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, other: T) -> BooleanType: ...
    
    # No Events


class IFormatProvider(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetFormat(self, formatType: TypeType) -> ObjectType: ...
    
    # No Events


class IFormattable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ToString(self, format: StringType, formatProvider: IFormatProvider) -> StringType: ...
    
    # No Events


class IObservable(Protocol[T]):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Subscribe(self, observer: IObserver[T]) -> IDisposable: ...
    
    # No Events


class IObserver(Protocol[T]):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def OnCompleted(self) -> VoidType: ...
    
    def OnError(self, error: Exception) -> VoidType: ...
    
    def OnNext(self, value: T) -> VoidType: ...
    
    # No Events


class IProgress(Protocol[T]):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Report(self, value: T) -> VoidType: ...
    
    # No Events


class IRuntimeFieldInfo(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> RuntimeFieldHandleInternal: ...
    
    # ---------- Methods ---------- #
    
    def get_Value(self) -> RuntimeFieldHandleInternal: ...
    
    # No Events


class IRuntimeMethodInfo(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> RuntimeMethodHandleInternal: ...
    
    # ---------- Methods ---------- #
    
    def get_Value(self) -> RuntimeMethodHandleInternal: ...
    
    # No Events


class IServiceProvider(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetService(self, serviceType: TypeType) -> ObjectType: ...
    
    # No Events


class ITupleInternal(Protocol, ITuple):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetHashCode(self, comparer: IEqualityComparer) -> IntType: ...
    
    def ToString(self, sb: StringBuilder) -> StringType: ...
    
    # No Events


class IValueTupleInternal(Protocol, ITuple):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetHashCode(self, comparer: IEqualityComparer) -> IntType: ...
    
    def ToStringEnd(self) -> StringType: ...
    
    # No Events


class IWellKnownStringEqualityComparer(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetEqualityComparerForSerialization(self) -> IEqualityComparer: ...
    
    def GetRandomizedEqualityComparer(self) -> IEqualityComparer: ...
    
    # No Events


class _AppDomain(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def BaseDirectory(self) -> StringType: ...
    
    @property
    def DynamicDirectory(self) -> StringType: ...
    
    @property
    def Evidence(self) -> Evidence: ...
    
    @property
    def FriendlyName(self) -> StringType: ...
    
    @property
    def RelativeSearchPath(self) -> StringType: ...
    
    @property
    def ShadowCopyFiles(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def AppendPrivatePath(self, path: StringType) -> VoidType: ...
    
    def ClearPrivatePath(self) -> VoidType: ...
    
    def ClearShadowCopyPath(self) -> VoidType: ...
    
    @overload
    def CreateInstance(self, assemblyName: StringType, typeName: StringType) -> ObjectHandle: ...
    
    @overload
    def CreateInstance(self, assemblyName: StringType, typeName: StringType, activationAttributes: ArrayType[ObjectType]) -> ObjectHandle: ...
    
    @overload
    def CreateInstance(self, assemblyName: StringType, typeName: StringType, ignoreCase: BooleanType, bindingAttr: BindingFlags, binder: Binder, args: ArrayType[ObjectType], culture: CultureInfo, activationAttributes: ArrayType[ObjectType], securityAttributes: Evidence) -> ObjectHandle: ...
    
    @overload
    def CreateInstanceFrom(self, assemblyFile: StringType, typeName: StringType) -> ObjectHandle: ...
    
    @overload
    def CreateInstanceFrom(self, assemblyFile: StringType, typeName: StringType, activationAttributes: ArrayType[ObjectType]) -> ObjectHandle: ...
    
    @overload
    def CreateInstanceFrom(self, assemblyFile: StringType, typeName: StringType, ignoreCase: BooleanType, bindingAttr: BindingFlags, binder: Binder, args: ArrayType[ObjectType], culture: CultureInfo, activationAttributes: ArrayType[ObjectType], securityAttributes: Evidence) -> ObjectHandle: ...
    
    @overload
    def DefineDynamicAssembly(self, name: AssemblyName, access: AssemblyBuilderAccess) -> AssemblyBuilder: ...
    
    @overload
    def DefineDynamicAssembly(self, name: AssemblyName, access: AssemblyBuilderAccess, dir: StringType) -> AssemblyBuilder: ...
    
    @overload
    def DefineDynamicAssembly(self, name: AssemblyName, access: AssemblyBuilderAccess, evidence: Evidence) -> AssemblyBuilder: ...
    
    @overload
    def DefineDynamicAssembly(self, name: AssemblyName, access: AssemblyBuilderAccess, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet) -> AssemblyBuilder: ...
    
    @overload
    def DefineDynamicAssembly(self, name: AssemblyName, access: AssemblyBuilderAccess, dir: StringType, evidence: Evidence) -> AssemblyBuilder: ...
    
    @overload
    def DefineDynamicAssembly(self, name: AssemblyName, access: AssemblyBuilderAccess, dir: StringType, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet) -> AssemblyBuilder: ...
    
    @overload
    def DefineDynamicAssembly(self, name: AssemblyName, access: AssemblyBuilderAccess, evidence: Evidence, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet) -> AssemblyBuilder: ...
    
    @overload
    def DefineDynamicAssembly(self, name: AssemblyName, access: AssemblyBuilderAccess, dir: StringType, evidence: Evidence, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet) -> AssemblyBuilder: ...
    
    @overload
    def DefineDynamicAssembly(self, name: AssemblyName, access: AssemblyBuilderAccess, dir: StringType, evidence: Evidence, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet, isSynchronized: BooleanType) -> AssemblyBuilder: ...
    
    def DoCallBack(self, theDelegate: CrossAppDomainDelegate) -> VoidType: ...
    
    def Equals(self, other: ObjectType) -> BooleanType: ...
    
    @overload
    def ExecuteAssembly(self, assemblyFile: StringType, assemblySecurity: Evidence) -> IntType: ...
    
    @overload
    def ExecuteAssembly(self, assemblyFile: StringType) -> IntType: ...
    
    @overload
    def ExecuteAssembly(self, assemblyFile: StringType, assemblySecurity: Evidence, args: ArrayType[StringType]) -> IntType: ...
    
    def GetAssemblies(self) -> ArrayType[Assembly]: ...
    
    def GetData(self, name: StringType) -> ObjectType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetIDsOfNames(self, riid: Guid, rgszNames: NIntType, cNames: UIntType, lcid: UIntType, rgDispId: NIntType) -> Tuple[VoidType, Guid]: ...
    
    def GetLifetimeService(self) -> ObjectType: ...
    
    def GetType(self) -> TypeType: ...
    
    def GetTypeInfo(self, iTInfo: UIntType, lcid: UIntType, ppTInfo: NIntType) -> VoidType: ...
    
    def GetTypeInfoCount(self, pcTInfo: UIntType) -> Tuple[VoidType, UIntType]: ...
    
    def InitializeLifetimeService(self) -> ObjectType: ...
    
    def Invoke(self, dispIdMember: UIntType, riid: Guid, lcid: UIntType, wFlags: ShortType, pDispParams: NIntType, pVarResult: NIntType, pExcepInfo: NIntType, puArgErr: NIntType) -> Tuple[VoidType, Guid]: ...
    
    @overload
    def Load(self, assemblyRef: AssemblyName) -> Assembly: ...
    
    @overload
    def Load(self, assemblyString: StringType) -> Assembly: ...
    
    @overload
    def Load(self, rawAssembly: ArrayType[ByteType]) -> Assembly: ...
    
    @overload
    def Load(self, rawAssembly: ArrayType[ByteType], rawSymbolStore: ArrayType[ByteType]) -> Assembly: ...
    
    @overload
    def Load(self, rawAssembly: ArrayType[ByteType], rawSymbolStore: ArrayType[ByteType], securityEvidence: Evidence) -> Assembly: ...
    
    @overload
    def Load(self, assemblyRef: AssemblyName, assemblySecurity: Evidence) -> Assembly: ...
    
    @overload
    def Load(self, assemblyString: StringType, assemblySecurity: Evidence) -> Assembly: ...
    
    def SetAppDomainPolicy(self, domainPolicy: PolicyLevel) -> VoidType: ...
    
    def SetCachePath(self, s: StringType) -> VoidType: ...
    
    def SetData(self, name: StringType, data: ObjectType) -> VoidType: ...
    
    def SetPrincipalPolicy(self, policy: PrincipalPolicy) -> VoidType: ...
    
    def SetShadowCopyPath(self, s: StringType) -> VoidType: ...
    
    def SetThreadPrincipal(self, principal: IPrincipal) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def add_AssemblyLoad(self, value: AssemblyLoadEventHandler) -> VoidType: ...
    
    def add_AssemblyResolve(self, value: ResolveEventHandler) -> VoidType: ...
    
    def add_DomainUnload(self, value: EventHandler) -> VoidType: ...
    
    def add_ProcessExit(self, value: EventHandler) -> VoidType: ...
    
    def add_ResourceResolve(self, value: ResolveEventHandler) -> VoidType: ...
    
    def add_TypeResolve(self, value: ResolveEventHandler) -> VoidType: ...
    
    def add_UnhandledException(self, value: UnhandledExceptionEventHandler) -> VoidType: ...
    
    def get_BaseDirectory(self) -> StringType: ...
    
    def get_DynamicDirectory(self) -> StringType: ...
    
    def get_Evidence(self) -> Evidence: ...
    
    def get_FriendlyName(self) -> StringType: ...
    
    def get_RelativeSearchPath(self) -> StringType: ...
    
    def get_ShadowCopyFiles(self) -> BooleanType: ...
    
    def remove_AssemblyLoad(self, value: AssemblyLoadEventHandler) -> VoidType: ...
    
    def remove_AssemblyResolve(self, value: ResolveEventHandler) -> VoidType: ...
    
    def remove_DomainUnload(self, value: EventHandler) -> VoidType: ...
    
    def remove_ProcessExit(self, value: EventHandler) -> VoidType: ...
    
    def remove_ResourceResolve(self, value: ResolveEventHandler) -> VoidType: ...
    
    def remove_TypeResolve(self, value: ResolveEventHandler) -> VoidType: ...
    
    def remove_UnhandledException(self, value: UnhandledExceptionEventHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    AssemblyLoad: EventType[AssemblyLoadEventHandler] = ...
    
    AssemblyResolve: EventType[ResolveEventHandler] = ...
    
    DomainUnload: EventType[EventHandler] = ...
    
    ProcessExit: EventType[EventHandler] = ...
    
    ResourceResolve: EventType[ResolveEventHandler] = ...
    
    TypeResolve: EventType[ResolveEventHandler] = ...
    
    UnhandledException: EventType[UnhandledExceptionEventHandler] = ...


# ---------- Enums ---------- #

class AppDomainManagerInitializationOptions(Enum):
    #None: IntType = 0
    RegisterWithHost: IntType = 1


class AttributeTargets(Enum):
    Assembly: IntType = 1
    Module: IntType = 2
    Class: IntType = 4
    Struct: IntType = 8
    Enum: IntType = 16
    Constructor: IntType = 32
    Method: IntType = 64
    Property: IntType = 128
    Field: IntType = 256
    Event: IntType = 512
    Interface: IntType = 1024
    Parameter: IntType = 2048
    Delegate: IntType = 4096
    ReturnValue: IntType = 8192
    GenericParameter: IntType = 16384
    All: IntType = 32767


class Base64FormattingOptions(Enum):
    #None: IntType = 0
    InsertLineBreaks: IntType = 1


class CompatibilityFlag(Enum):
    SwallowUnhandledExceptions: IntType = 0
    NullReferenceExceptionOnAV: IntType = 1
    EagerlyGenerateRandomAsymmKeys: IntType = 2
    FullTrustListAssembliesInGac: IntType = 3
    DateTimeParseIgnorePunctuation: IntType = 4
    OnlyGACDomainNeutral: IntType = 5
    DisableReplacementCustomCulture: IntType = 6


class ConfigEvents(Enum):
    StartDocument: IntType = 0
    StartDTD: IntType = 1
    EndDTD: IntType = 2
    StartDTDSubset: IntType = 3
    EndDTDSubset: IntType = 4
    EndProlog: IntType = 5
    StartEntity: IntType = 6
    EndEntity: IntType = 7
    EndDocument: IntType = 8
    DataAvailable: IntType = 9
    LastEvent: IntType = 9


class ConfigNodeSubType(Enum):
    Version: IntType = 28
    Encoding: IntType = 29
    Standalone: IntType = 30
    NS: IntType = 31
    XMLSpace: IntType = 32
    XMLLang: IntType = 33
    System: IntType = 34
    Public: IntType = 35
    NData: IntType = 36
    AtCData: IntType = 37
    AtId: IntType = 38
    AtIdref: IntType = 39
    AtIdrefs: IntType = 40
    AtEntity: IntType = 41
    AtEntities: IntType = 42
    AtNmToken: IntType = 43
    AtNmTokens: IntType = 44
    AtNotation: IntType = 45
    AtRequired: IntType = 46
    AtImplied: IntType = 47
    AtFixed: IntType = 48
    PentityDecl: IntType = 49
    Empty: IntType = 50
    Any: IntType = 51
    Mixed: IntType = 52
    Sequence: IntType = 53
    Choice: IntType = 54
    Star: IntType = 55
    Plus: IntType = 56
    Questionmark: IntType = 57
    LastSubNodeType: IntType = 58


class ConfigNodeType(Enum):
    Element: IntType = 1
    Attribute: IntType = 2
    Pi: IntType = 3
    XmlDecl: IntType = 4
    DocType: IntType = 5
    DTDAttribute: IntType = 6
    EntityDecl: IntType = 7
    ElementDecl: IntType = 8
    AttlistDecl: IntType = 9
    Notation: IntType = 10
    Group: IntType = 11
    IncludeSect: IntType = 12
    PCData: IntType = 13
    CData: IntType = 14
    IgnoreSect: IntType = 15
    Comment: IntType = 16
    EntityRef: IntType = 17
    Whitespace: IntType = 18
    Name: IntType = 19
    NMToken: IntType = 20
    String: IntType = 21
    Peref: IntType = 22
    Model: IntType = 23
    ATTDef: IntType = 24
    ATTType: IntType = 25
    ATTPresence: IntType = 26
    DTDSubset: IntType = 27
    LastNodeType: IntType = 28


class ConsoleColor(Enum):
    Black: IntType = 0
    DarkBlue: IntType = 1
    DarkGreen: IntType = 2
    DarkCyan: IntType = 3
    DarkRed: IntType = 4
    DarkMagenta: IntType = 5
    DarkYellow: IntType = 6
    Gray: IntType = 7
    DarkGray: IntType = 8
    Blue: IntType = 9
    Green: IntType = 10
    Cyan: IntType = 11
    Red: IntType = 12
    Magenta: IntType = 13
    Yellow: IntType = 14
    White: IntType = 15


class ConsoleKey(Enum):
    Backspace: IntType = 8
    Tab: IntType = 9
    Clear: IntType = 12
    Enter: IntType = 13
    Pause: IntType = 19
    Escape: IntType = 27
    Spacebar: IntType = 32
    PageUp: IntType = 33
    PageDown: IntType = 34
    End: IntType = 35
    Home: IntType = 36
    LeftArrow: IntType = 37
    UpArrow: IntType = 38
    RightArrow: IntType = 39
    DownArrow: IntType = 40
    Select: IntType = 41
    Print: IntType = 42
    Execute: IntType = 43
    PrintScreen: IntType = 44
    Insert: IntType = 45
    Delete: IntType = 46
    Help: IntType = 47
    D0: IntType = 48
    D1: IntType = 49
    D2: IntType = 50
    D3: IntType = 51
    D4: IntType = 52
    D5: IntType = 53
    D6: IntType = 54
    D7: IntType = 55
    D8: IntType = 56
    D9: IntType = 57
    A: IntType = 65
    B: IntType = 66
    C: IntType = 67
    D: IntType = 68
    E: IntType = 69
    F: IntType = 70
    G: IntType = 71
    H: IntType = 72
    I: IntType = 73
    J: IntType = 74
    K: IntType = 75
    L: IntType = 76
    M: IntType = 77
    N: IntType = 78
    O: IntType = 79
    P: IntType = 80
    Q: IntType = 81
    R: IntType = 82
    S: IntType = 83
    T: IntType = 84
    U: IntType = 85
    V: IntType = 86
    W: IntType = 87
    X: IntType = 88
    Y: IntType = 89
    Z: IntType = 90
    LeftWindows: IntType = 91
    RightWindows: IntType = 92
    Applications: IntType = 93
    Sleep: IntType = 95
    NumPad0: IntType = 96
    NumPad1: IntType = 97
    NumPad2: IntType = 98
    NumPad3: IntType = 99
    NumPad4: IntType = 100
    NumPad5: IntType = 101
    NumPad6: IntType = 102
    NumPad7: IntType = 103
    NumPad8: IntType = 104
    NumPad9: IntType = 105
    Multiply: IntType = 106
    Add: IntType = 107
    Separator: IntType = 108
    Subtract: IntType = 109
    Decimal: IntType = 110
    Divide: IntType = 111
    F1: IntType = 112
    F2: IntType = 113
    F3: IntType = 114
    F4: IntType = 115
    F5: IntType = 116
    F6: IntType = 117
    F7: IntType = 118
    F8: IntType = 119
    F9: IntType = 120
    F10: IntType = 121
    F11: IntType = 122
    F12: IntType = 123
    F13: IntType = 124
    F14: IntType = 125
    F15: IntType = 126
    F16: IntType = 127
    F17: IntType = 128
    F18: IntType = 129
    F19: IntType = 130
    F20: IntType = 131
    F21: IntType = 132
    F22: IntType = 133
    F23: IntType = 134
    F24: IntType = 135
    BrowserBack: IntType = 166
    BrowserForward: IntType = 167
    BrowserRefresh: IntType = 168
    BrowserStop: IntType = 169
    BrowserSearch: IntType = 170
    BrowserFavorites: IntType = 171
    BrowserHome: IntType = 172
    VolumeMute: IntType = 173
    VolumeDown: IntType = 174
    VolumeUp: IntType = 175
    MediaNext: IntType = 176
    MediaPrevious: IntType = 177
    MediaStop: IntType = 178
    MediaPlay: IntType = 179
    LaunchMail: IntType = 180
    LaunchMediaSelect: IntType = 181
    LaunchApp1: IntType = 182
    LaunchApp2: IntType = 183
    Oem1: IntType = 186
    OemPlus: IntType = 187
    OemComma: IntType = 188
    OemMinus: IntType = 189
    OemPeriod: IntType = 190
    Oem2: IntType = 191
    Oem3: IntType = 192
    Oem4: IntType = 219
    Oem5: IntType = 220
    Oem6: IntType = 221
    Oem7: IntType = 222
    Oem8: IntType = 223
    Oem102: IntType = 226
    Process: IntType = 229
    Packet: IntType = 231
    Attention: IntType = 246
    CrSel: IntType = 247
    ExSel: IntType = 248
    EraseEndOfFile: IntType = 249
    Play: IntType = 250
    Zoom: IntType = 251
    NoName: IntType = 252
    Pa1: IntType = 253
    OemClear: IntType = 254


class ConsoleModifiers(Enum):
    Alt: IntType = 1
    Shift: IntType = 2
    Control: IntType = 4


class ConsoleSpecialKey(Enum):
    ControlC: IntType = 0
    ControlBreak: IntType = 1


class DTSubStringType(Enum):
    Unknown: IntType = 0
    Invalid: IntType = 1
    Number: IntType = 2
    End: IntType = 3
    Other: IntType = 4


class DateTimeKind(Enum):
    Unspecified: IntType = 0
    Utc: IntType = 1
    Local: IntType = 2


class DayOfWeek(Enum):
    Sunday: IntType = 0
    Monday: IntType = 1
    Tuesday: IntType = 2
    Wednesday: IntType = 3
    Thursday: IntType = 4
    Friday: IntType = 5
    Saturday: IntType = 6


class DelegateBindingFlags(Enum):
    StaticMethodOnly: IntType = 1
    InstanceMethodOnly: IntType = 2
    OpenDelegateOnly: IntType = 4
    ClosedDelegateOnly: IntType = 8
    NeverCloseOverNull: IntType = 16
    CaselessMatching: IntType = 32
    SkipSecurityChecks: IntType = 64
    RelaxedSignature: IntType = 128


class EnvironmentVariableTarget(Enum):
    Process: IntType = 0
    User: IntType = 1
    Machine: IntType = 2


class ExceptionArgument(Enum):
    obj: IntType = 0
    dictionary: IntType = 1
    array: IntType = 2
    info: IntType = 3
    key: IntType = 4
    collection: IntType = 5
    match: IntType = 6
    converter: IntType = 7
    queue: IntType = 8
    stack: IntType = 9
    capacity: IntType = 10
    index: IntType = 11
    startIndex: IntType = 12
    value: IntType = 13
    count: IntType = 14
    arrayIndex: IntType = 15
    item: IntType = 16


class ExceptionArgument(Enum):
    obj: IntType = 0
    dictionary: IntType = 1
    dictionaryCreationThreshold: IntType = 2
    array: IntType = 3
    info: IntType = 4
    key: IntType = 5
    collection: IntType = 6
    list: IntType = 7
    match: IntType = 8
    converter: IntType = 9
    queue: IntType = 10
    stack: IntType = 11
    capacity: IntType = 12
    index: IntType = 13
    startIndex: IntType = 14
    value: IntType = 15
    count: IntType = 16
    arrayIndex: IntType = 17
    name: IntType = 18
    mode: IntType = 19
    item: IntType = 20
    options: IntType = 21
    view: IntType = 22
    sourceBytesToCopy: IntType = 23


class ExceptionResource(Enum):
    Argument_ImplementIComparable: IntType = 0
    ArgumentOutOfRange_NeedNonNegNum: IntType = 1
    ArgumentOutOfRange_NeedNonNegNumRequired: IntType = 2
    Arg_ArrayPlusOffTooSmall: IntType = 3
    Argument_AddingDuplicate: IntType = 4
    Serialization_InvalidOnDeser: IntType = 5
    Serialization_MismatchedCount: IntType = 6
    Serialization_MissingValues: IntType = 7
    Arg_RankMultiDimNotSupported: IntType = 8
    Arg_NonZeroLowerBound: IntType = 9
    Argument_InvalidArrayType: IntType = 10
    NotSupported_KeyCollectionSet: IntType = 11
    ArgumentOutOfRange_SmallCapacity: IntType = 12
    ArgumentOutOfRange_Index: IntType = 13
    Argument_InvalidOffLen: IntType = 14
    NotSupported_ReadOnlyCollection: IntType = 15
    InvalidOperation_CannotRemoveFromStackOrQueue: IntType = 16
    InvalidOperation_EmptyCollection: IntType = 17
    InvalidOperation_EmptyQueue: IntType = 18
    InvalidOperation_EnumOpCantHappen: IntType = 19
    InvalidOperation_EnumFailedVersion: IntType = 20
    InvalidOperation_EmptyStack: IntType = 21
    InvalidOperation_EnumNotStarted: IntType = 22
    InvalidOperation_EnumEnded: IntType = 23
    NotSupported_SortedListNestedWrite: IntType = 24
    NotSupported_ValueCollectionSet: IntType = 25


class ExceptionResource(Enum):
    Argument_ImplementIComparable: IntType = 0
    Argument_InvalidType: IntType = 1
    Argument_InvalidArgumentForComparison: IntType = 2
    Argument_InvalidRegistryKeyPermissionCheck: IntType = 3
    ArgumentOutOfRange_NeedNonNegNum: IntType = 4
    Arg_ArrayPlusOffTooSmall: IntType = 5
    Arg_NonZeroLowerBound: IntType = 6
    Arg_RankMultiDimNotSupported: IntType = 7
    Arg_RegKeyDelHive: IntType = 8
    Arg_RegKeyStrLenBug: IntType = 9
    Arg_RegSetStrArrNull: IntType = 10
    Arg_RegSetMismatchedKind: IntType = 11
    Arg_RegSubKeyAbsent: IntType = 12
    Arg_RegSubKeyValueAbsent: IntType = 13
    Argument_AddingDuplicate: IntType = 14
    Serialization_InvalidOnDeser: IntType = 15
    Serialization_MissingKeys: IntType = 16
    Serialization_NullKey: IntType = 17
    Argument_InvalidArrayType: IntType = 18
    NotSupported_KeyCollectionSet: IntType = 19
    NotSupported_ValueCollectionSet: IntType = 20
    ArgumentOutOfRange_SmallCapacity: IntType = 21
    ArgumentOutOfRange_Index: IntType = 22
    Argument_InvalidOffLen: IntType = 23
    Argument_ItemNotExist: IntType = 24
    ArgumentOutOfRange_Count: IntType = 25
    ArgumentOutOfRange_InvalidThreshold: IntType = 26
    ArgumentOutOfRange_ListInsert: IntType = 27
    NotSupported_ReadOnlyCollection: IntType = 28
    InvalidOperation_CannotRemoveFromStackOrQueue: IntType = 29
    InvalidOperation_EmptyQueue: IntType = 30
    InvalidOperation_EnumOpCantHappen: IntType = 31
    InvalidOperation_EnumFailedVersion: IntType = 32
    InvalidOperation_EmptyStack: IntType = 33
    ArgumentOutOfRange_BiggerThanCollection: IntType = 34
    InvalidOperation_EnumNotStarted: IntType = 35
    InvalidOperation_EnumEnded: IntType = 36
    NotSupported_SortedListNestedWrite: IntType = 37
    InvalidOperation_NoValue: IntType = 38
    InvalidOperation_RegRemoveSubKey: IntType = 39
    Security_RegistryPermission: IntType = 40
    UnauthorizedAccess_RegistryNoWrite: IntType = 41
    ObjectDisposed_RegKeyClosed: IntType = 42
    NotSupported_InComparableType: IntType = 43
    Argument_InvalidRegistryOptionsCheck: IntType = 44
    Argument_InvalidRegistryViewCheck: IntType = 45


class GCCollectionMode(Enum):
    Default: IntType = 0
    Forced: IntType = 1
    Optimized: IntType = 2


class GCNotificationStatus(Enum):
    Succeeded: IntType = 0
    Failed: IntType = 1
    Canceled: IntType = 2
    Timeout: IntType = 3
    NotApplicable: IntType = 4


class GenericUriParserOptions(Enum):
    Default: IntType = 0
    GenericAuthority: IntType = 1
    AllowEmptyAuthority: IntType = 2
    NoUserInfo: IntType = 4
    NoPort: IntType = 8
    NoQuery: IntType = 16
    NoFragment: IntType = 32
    DontConvertPathBackslashes: IntType = 64
    DontCompressPath: IntType = 128
    DontUnescapePathDotsAndSlashes: IntType = 256
    Idn: IntType = 512
    IriParsing: IntType = 1024


class InternalGCCollectionMode(Enum):
    NonBlocking: IntType = 1
    Blocking: IntType = 2
    Optimized: IntType = 4
    Compacting: IntType = 8


class LoaderOptimization(Enum):
    NotSpecified: IntType = 0
    SingleDomain: IntType = 1
    MultiDomain: IntType = 2
    MultiDomainHost: IntType = 3
    DomainMask: IntType = 3
    DisallowBindings: IntType = 4


class LogLevel(Enum):
    Trace: IntType = 0
    Status: IntType = 20
    Warning: IntType = 40
    Error: IntType = 50
    Panic: IntType = 100


class MidpointRounding(Enum):
    ToEven: IntType = 0
    AwayFromZero: IntType = 1


class ParseFailureKind(Enum):
    #None: IntType = 0
    ArgumentNull: IntType = 1
    Format: IntType = 2
    FormatWithParameter: IntType = 3
    FormatBadDateTimeCalendar: IntType = 4


class ParseFlags(Enum):
    HaveYear: IntType = 1
    HaveMonth: IntType = 2
    HaveDay: IntType = 4
    HaveHour: IntType = 8
    HaveMinute: IntType = 16
    HaveSecond: IntType = 32
    HaveTime: IntType = 64
    HaveDate: IntType = 128
    TimeZoneUsed: IntType = 256
    TimeZoneUtc: IntType = 512
    ParsedMonthName: IntType = 1024
    CaptureOffset: IntType = 2048
    YearDefault: IntType = 4096
    Rfc1123Pattern: IntType = 8192
    UtcSortPattern: IntType = 16384


class ParsingError(Enum):
    #None: IntType = 0
    BadFormat: IntType = 1
    BadScheme: IntType = 2
    BadAuthority: IntType = 3
    EmptyUriString: IntType = 4
    LastRelativeUriOkErrIndex: IntType = 4
    SchemeLimit: IntType = 5
    SizeLimit: IntType = 6
    MustRootedPath: IntType = 7
    BadHostName: IntType = 8
    NonEmptyHost: IntType = 9
    BadPort: IntType = 10
    BadAuthorityTerminator: IntType = 11
    CannotCreateRelative: IntType = 12


class PlatformID(Enum):
    Win32S: IntType = 0
    Win32Windows: IntType = 1
    Win32NT: IntType = 2
    WinCE: IntType = 3
    Unix: IntType = 4
    Xbox: IntType = 5
    MacOSX: IntType = 6


class StringComparison(Enum):
    CurrentCulture: IntType = 0
    CurrentCultureIgnoreCase: IntType = 1
    InvariantCulture: IntType = 2
    InvariantCultureIgnoreCase: IntType = 3
    Ordinal: IntType = 4
    OrdinalIgnoreCase: IntType = 5


class StringSplitOptions(Enum):
    #None: IntType = 0
    RemoveEmptyEntries: IntType = 1


class TimeZoneInfoOptions(Enum):
    #None: IntType = 1
    NoThrowOnInvalidTime: IntType = 2


class TokenType(Enum):
    NumberToken: IntType = 1
    YearNumberToken: IntType = 2
    Am: IntType = 3
    Pm: IntType = 4
    MonthToken: IntType = 5
    EndOfString: IntType = 6
    DayOfWeekToken: IntType = 7
    TimeZoneToken: IntType = 8
    EraToken: IntType = 9
    DateWordToken: IntType = 10
    UnknownToken: IntType = 11
    HebrewNumber: IntType = 12
    JapaneseEraToken: IntType = 13
    TEraToken: IntType = 14
    IgnorableSymbol: IntType = 15
    RegularTokenMask: IntType = 255
    SEP_Unk: IntType = 256
    SEP_End: IntType = 512
    SEP_Space: IntType = 768
    SEP_Am: IntType = 1024
    SEP_Pm: IntType = 1280
    SEP_Date: IntType = 1536
    SEP_Time: IntType = 1792
    SEP_YearSuff: IntType = 2048
    SEP_MonthSuff: IntType = 2304
    SEP_DaySuff: IntType = 2560
    SEP_HourSuff: IntType = 2816
    SEP_MinuteSuff: IntType = 3072
    SEP_SecondSuff: IntType = 3328
    SEP_LocalTimeMark: IntType = 3584
    SEP_DateOrOffset: IntType = 3840
    SeparatorTokenMask: IntType = 65280


class TypeCode(Enum):
    Empty: IntType = 0
    Object: IntType = 1
    DBNull: IntType = 2
    Boolean: IntType = 3
    Char: IntType = 4
    SByte: IntType = 5
    Byte: IntType = 6
    Int16: IntType = 7
    UInt16: IntType = 8
    Int32: IntType = 9
    UInt32: IntType = 10
    Int64: IntType = 11
    UInt64: IntType = 12
    Single: IntType = 13
    Double: IntType = 14
    Decimal: IntType = 15
    DateTime: IntType = 16
    String: IntType = 18


class TypeNameFormatFlags(Enum):
    FormatBasic: IntType = 0
    FormatNamespace: IntType = 1
    FormatFullInst: IntType = 2
    FormatAssembly: IntType = 4
    FormatSignature: IntType = 8
    FormatNoVersion: IntType = 16
    FormatAngleBrackets: IntType = 64
    FormatStubInfo: IntType = 128
    FormatGenericParam: IntType = 256
    FormatSerialization: IntType = 259


class TypeNameKind(Enum):
    Name: IntType = 0
    ToString: IntType = 1
    SerializationName: IntType = 2
    FullName: IntType = 3


class UnescapeMode(Enum):
    CopyOnly: IntType = 0
    Escape: IntType = 1
    Unescape: IntType = 2
    EscapeUnescape: IntType = 3
    V1ToStringFlag: IntType = 4
    UnescapeAll: IntType = 8
    UnescapeAllOrThrow: IntType = 24


class UriComponents(Enum):
    SerializationInfoString: IntType = -2147483648
    Scheme: IntType = 1
    UserInfo: IntType = 2
    Host: IntType = 4
    Port: IntType = 8
    SchemeAndServer: IntType = 13
    Path: IntType = 16
    Query: IntType = 32
    PathAndQuery: IntType = 48
    HttpRequestUrl: IntType = 61
    Fragment: IntType = 64
    AbsoluteUri: IntType = 127
    StrongPort: IntType = 128
    HostAndPort: IntType = 132
    StrongAuthority: IntType = 134
    NormalizedHost: IntType = 256
    KeepDelimiter: IntType = 1073741824


class UriFormat(Enum):
    UriEscaped: IntType = 1
    Unescaped: IntType = 2
    SafeUnescaped: IntType = 3


class UriHostNameType(Enum):
    Unknown: IntType = 0
    Basic: IntType = 1
    Dns: IntType = 2
    IPv4: IntType = 3
    IPv6: IntType = 4


class UriIdnScope(Enum):
    #None: IntType = 0
    AllExceptIntranet: IntType = 1
    All: IntType = 2


class UriKind(Enum):
    RelativeOrAbsolute: IntType = 0
    Absolute: IntType = 1
    Relative: IntType = 2


class UriPartial(Enum):
    Scheme: IntType = 0
    Authority: IntType = 1
    Path: IntType = 2
    Query: IntType = 3


class UriSyntaxFlags(Enum):
    #None: IntType = 0
    MustHaveAuthority: IntType = 1
    OptionalAuthority: IntType = 2
    MayHaveUserInfo: IntType = 4
    MayHavePort: IntType = 8
    MayHavePath: IntType = 16
    MayHaveQuery: IntType = 32
    MayHaveFragment: IntType = 64
    AllowEmptyHost: IntType = 128
    AllowUncHost: IntType = 256
    AllowDnsHost: IntType = 512
    AllowIPv4Host: IntType = 1024
    AllowIPv6Host: IntType = 2048
    AllowAnInternetHost: IntType = 3584
    AllowAnyOtherHost: IntType = 4096
    FileLikeUri: IntType = 8192
    MailToLikeUri: IntType = 16384
    V1_UnknownUri: IntType = 65536
    SimpleUserSyntax: IntType = 131072
    BuiltInSyntax: IntType = 262144
    ParserSchemeOnly: IntType = 524288
    AllowDOSPath: IntType = 1048576
    PathIsRooted: IntType = 2097152
    ConvertPathSlashes: IntType = 4194304
    CompressPath: IntType = 8388608
    CanonicalizeAsFilePath: IntType = 16777216
    UnEscapeDotsAndSlashes: IntType = 33554432
    AllowIdn: IntType = 67108864
    AllowIriParsing: IntType = 268435456


# ---------- Delegates ---------- #

Action = Callable[[T], VoidType]

Action = Callable[[], VoidType]

Action = Callable[[T1, T2], VoidType]

Action = Callable[[T1, T2, T3], VoidType]

Action = Callable[[T1, T2, T3, T4], VoidType]

Action = Callable[[T1, T2, T3, T4, T5], VoidType]

Action = Callable[[T1, T2, T3, T4, T5, T6], VoidType]

Action = Callable[[T1, T2, T3, T4, T5, T6, T7], VoidType]

Action = Callable[[T1, T2, T3, T4, T5, T6, T7, T8], VoidType]

AppDomainInitializer = Callable[[ArrayType[StringType]], VoidType]

AssemblyLoadEventHandler = Callable[[ObjectType, AssemblyLoadEventArgs], VoidType]

AsyncCallback = Callable[[IAsyncResult], VoidType]

Comparison = Callable[[T, T], IntType]

ConsoleCancelEventHandler = Callable[[ObjectType, ConsoleCancelEventArgs], VoidType]

Converter = Callable[[TInput], TOutput]

CrossAppDomainDelegate = Callable[[], VoidType]

CtorDelegate = Callable[[ObjectType], VoidType]

EventHandler = Callable[[ObjectType, EventArgs], VoidType]

EventHandler = Callable[[ObjectType, TEventArgs], VoidType]

Func = Callable[[], TResult]

Func = Callable[[T], TResult]

Func = Callable[[T1, T2], TResult]

Func = Callable[[T1, T2, T3], TResult]

Func = Callable[[T1, T2, T3, T4], TResult]

Func = Callable[[T1, T2, T3, T4, T5], TResult]

Func = Callable[[T1, T2, T3, T4, T5, T6], TResult]

Func = Callable[[T1, T2, T3, T4, T5, T6, T7], TResult]

Func = Callable[[T1, T2, T3, T4, T5, T6, T7, T8], TResult]

Predicate = Callable[[T], BooleanType]

ResolveEventHandler = Callable[[ObjectType, ResolveEventArgs], Assembly]

UnhandledExceptionEventHandler = Callable[[ObjectType, UnhandledExceptionEventArgs], VoidType]

__all__ = [
    AccessViolationException,
    Action,
    ActivationContext,
    Activator,
    AggregateException,
    AppContext,
    AppContextDefaultValues,
    AppContextSwitches,
    AppDomain,
    AppDomainInitializer,
    AppDomainInitializerInfo,
    AppDomainManager,
    AppDomainPauseManager,
    AppDomainSetup,
    AppDomainUnloadedException,
    ApplicationException,
    ApplicationId,
    ApplicationIdentity,
    ArgumentException,
    ArgumentNullException,
    ArgumentOutOfRangeException,
    ArithmeticException,
    Array,
    ArrayTypeMismatchException,
    AssemblyLoadEventArgs,
    AssemblyLoadEventHandler,
    AsyncCallback,
    Attribute,
    AttributeUsageAttribute,
    BCLDebug,
    BadImageFormatException,
    BaseConfigHandler,
    BitConverter,
    Buffer,
    CLRConfig,
    CLSCompliantAttribute,
    CannotUnloadAppDomainException,
    CharEnumerator,
    ClientUtils,
    Comparison,
    CompatibilitySwitches,
    ConfigNode,
    ConfigTreeParser,
    Console,
    ConsoleCancelEventArgs,
    ConsoleCancelEventHandler,
    ContextBoundObject,
    ContextMarshalException,
    ContextStaticAttribute,
    Convert,
    Converter,
    CrossAppDomainDelegate,
    CtorDelegate,
    CultureAwareComparer,
    CultureAwareRandomizedComparer,
    CurrentSystemTimeZone,
    DBNull,
    DataMisalignedException,
    DateTimeFormat,
    DateTimeParse,
    DefaultBinder,
    Delegate,
    DelegateSerializationHolder,
    DivideByZeroException,
    DllNotFoundException,
    DomainNameHelper,
    DuplicateWaitObjectException,
    Empty,
    EntryPointNotFoundException,
    Enum,
    Environment,
    EnvironmentHelpers,
    EventArgs,
    EventHandler,
    Exception,
    ExecutionEngineException,
    ExternDll,
    FieldAccessException,
    FileStyleUriParser,
    FlagsAttribute,
    FormatException,
    FormattableString,
    FtpStyleUriParser,
    Func,
    GC,
    Gen2GcCallback,
    GenericUriParser,
    GopherStyleUriParser,
    HResults,
    HttpStyleUriParser,
    IPv4AddressHelper,
    IPv6AddressHelper,
    IndexOutOfRangeException,
    InsufficientExecutionStackException,
    InsufficientMemoryException,
    Internal,
    InvalidCastException,
    InvalidOperationException,
    InvalidProgramException,
    InvalidTimeZoneException,
    InvariantComparer,
    IriHelper,
    Lazy,
    LazyHelpers,
    LdapStyleUriParser,
    LoaderOptimizationAttribute,
    LocalAppContext,
    LocalAppContextSwitches,
    LocalDataStore,
    LocalDataStoreElement,
    LocalDataStoreHolder,
    LocalDataStoreMgr,
    LocalDataStoreSlot,
    MTAThreadAttribute,
    MarshalByRefObject,
    MarvinHash,
    Math,
    Mda,
    MemberAccessException,
    MethodAccessException,
    MissingFieldException,
    MissingMemberException,
    MissingMethodException,
    MulticastDelegate,
    MulticastNotSupportedException,
    NetPipeStyleUriParser,
    NetTcpStyleUriParser,
    NewsStyleUriParser,
    NonSerializedAttribute,
    NotFiniteNumberException,
    NotImplementedException,
    NotSupportedException,
    NullReferenceException,
    Nullable,
    Number,
    Object,
    ObjectDisposedException,
    ObsoleteAttribute,
    OleAutBinder,
    OperatingSystem,
    OperationCanceledException,
    OrdinalComparer,
    OrdinalRandomizedComparer,
    OutOfMemoryException,
    OverflowException,
    ParamArrayAttribute,
    ParseNumbers,
    PinnableBufferCache,
    PinnableBufferCacheEventSource,
    PlatformNotSupportedException,
    Predicate,
    Progress,
    ProgressStatics,
    Random,
    RankException,
    ReflectionOnlyType,
    ResId,
    ResolveEventArgs,
    ResolveEventHandler,
    Resolver,
    RuntimeFieldInfoStub,
    RuntimeMethodInfoStub,
    RuntimeType,
    SR,
    SRCategoryAttribute,
    SRDescriptionAttribute,
    STAThreadAttribute,
    SZArrayHelper,
    SafeTypeNameParserHandle,
    SecurityUtils,
    SerializableAttribute,
    SharedStatics,
    Signature,
    SizedReference,
    StackOverflowException,
    String,
    StringComparer,
    StringNormalizationExtensions,
    SystemException,
    System_LazyDebugView,
    ThreadStaticAttribute,
    ThrowHelper,
    TimeZone,
    TimeZoneInfo,
    TimeZoneNotFoundException,
    TimeoutException,
    Tuple,
    TupleExtensions,
    Type,
    TypeAccessException,
    TypeInitializationException,
    TypeLoadException,
    TypeNameParser,
    TypeUnloadedException,
    UnauthorizedAccessException,
    UncNameHelper,
    UnhandledExceptionEventArgs,
    UnhandledExceptionEventHandler,
    UnitySerializationHolder,
    Uri,
    UriBuilder,
    UriFormatException,
    UriHelper,
    UriParser,
    UriTypeConverter,
    ValueType,
    Version,
    WeakReference,
    XmlIgnoreMemberAttribute,
    __Canon,
    __ComObject,
    __Filters,
    __HResults,
    AppDomainHandle,
    ArgIterator,
    ArraySegment,
    Boolean,
    Byte,
    Char,
    ConsoleKeyInfo,
    Currency,
    DTSubString,
    DateTime,
    DateTimeOffset,
    DateTimeRawInfo,
    DateTimeResult,
    DateTimeToken,
    Decimal,
    Double,
    Guid,
    Int16,
    Int32,
    Int64,
    IntPtr,
    ModuleHandle,
    Nullable,
    ParamsArray,
    ParsingInfo,
    RuntimeArgumentHandle,
    RuntimeFieldHandle,
    RuntimeFieldHandleInternal,
    RuntimeMethodHandle,
    RuntimeMethodHandleInternal,
    RuntimeTypeHandle,
    SByte,
    Single,
    SwitchStructure,
    TimeSpan,
    TypedReference,
    UInt16,
    UInt32,
    UInt64,
    UIntPtr,
    UnSafeCharBuffer,
    Utf8String,
    ValueTuple,
    Variant,
    Void,
    __DTString,
    IAppDomainSetup,
    IAsyncResult,
    ICloneable,
    IComparable,
    IConvertible,
    ICustomFormatter,
    IDisposable,
    IEquatable,
    IFormatProvider,
    IFormattable,
    IObservable,
    IObserver,
    IProgress,
    IRuntimeFieldInfo,
    IRuntimeMethodInfo,
    IServiceProvider,
    ITupleInternal,
    IValueTupleInternal,
    IWellKnownStringEqualityComparer,
    _AppDomain,
    AppDomainManagerInitializationOptions,
    AttributeTargets,
    Base64FormattingOptions,
    CompatibilityFlag,
    ConfigEvents,
    ConfigNodeSubType,
    ConfigNodeType,
    ConsoleColor,
    ConsoleKey,
    ConsoleModifiers,
    ConsoleSpecialKey,
    DTSubStringType,
    DateTimeKind,
    DayOfWeek,
    DelegateBindingFlags,
    EnvironmentVariableTarget,
    ExceptionArgument,
    ExceptionResource,
    GCCollectionMode,
    GCNotificationStatus,
    GenericUriParserOptions,
    InternalGCCollectionMode,
    LoaderOptimization,
    LogLevel,
    MidpointRounding,
    ParseFailureKind,
    ParseFlags,
    ParsingError,
    PlatformID,
    StringComparison,
    StringSplitOptions,
    TimeZoneInfoOptions,
    TokenType,
    TypeCode,
    TypeNameFormatFlags,
    TypeNameKind,
    UnescapeMode,
    UriComponents,
    UriFormat,
    UriHostNameType,
    UriIdnScope,
    UriKind,
    UriPartial,
    UriSyntaxFlags,
    Action,
    AppDomainInitializer,
    AssemblyLoadEventHandler,
    AsyncCallback,
    Comparison,
    ConsoleCancelEventHandler,
    Converter,
    CrossAppDomainDelegate,
    CtorDelegate,
    EventHandler,
    Func,
    Predicate,
    ResolveEventHandler,
    UnhandledExceptionEventHandler,
]
