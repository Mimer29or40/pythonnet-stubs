from __future__ import annotations

from abc import ABC
from typing import Generic, List, Protocol, Tuple, TypeVar, Union, overload

from System import Action, Array, AsyncCallback, Attribute, Boolean, Byte, Decimal, Delegate, Enum, Exception, FormattableString, IAsyncResult, ICloneable, Int16, Int32, Int64, IntPtr, ModuleHandle, MulticastDelegate, Object, RuntimeFieldHandle, RuntimeMethodHandle, RuntimeTypeHandle, String, Type, UInt32, ValueType, Void
from System.Collections.Generic import IList
from System.Diagnostics.Contracts import ContractFailureKind
from System.Runtime.InteropServices import _Attribute, _Exception
from System.Runtime.Serialization import ISerializable, SerializationInfo, StreamingContext
from System.Threading.Tasks import Task

# ---------- Types ---------- #

TKey = TypeVar('TKey')
TResult = TypeVar('TResult')
TValue = TypeVar('TValue')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
DecimalType = Union[float, Decimal]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
ShortType = Union[int, Int16]
StringType = Union[str, String]
TypeType = Union[type, Type]
UIntType = Union[int, UInt32]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class AccessedThroughPropertyAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, propertyName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def PropertyName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_PropertyName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyAttributesGoHere(ObjectType):
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


class AssemblyAttributesGoHereM(ObjectType):
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


class AssemblyAttributesGoHereS(ObjectType):
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


class AssemblyAttributesGoHereSM(ObjectType):
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


class AsyncStateMachineAttribute(StateMachineAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, stateMachineType: TypeType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsyncTaskCache(ABC, ObjectType):
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


class CallConvCdecl(ObjectType):
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


class CallConvFastcall(ObjectType):
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


class CallConvStdcall(ObjectType):
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


class CallConvThiscall(ObjectType):
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


class CallerFilePathAttribute(Attribute, _Attribute):
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


class CallerLineNumberAttribute(Attribute, _Attribute):
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


class CallerMemberNameAttribute(Attribute, _Attribute):
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


class CompilationRelaxationsAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, relaxations: IntType): ...
    
    @overload
    def __init__(self, relaxations: CompilationRelaxations): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CompilationRelaxations(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_CompilationRelaxations(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CompilerGeneratedAttribute(Attribute, _Attribute):
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


class CompilerGlobalScopeAttribute(Attribute, _Attribute):
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


class CompilerMarshalOverride(ABC, ObjectType):
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


class ConditionalWeakTable(Generic[TKey, TValue], ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Add(self, key: TKey, value: TValue) -> VoidType: ...
    
    def GetOrCreateValue(self, key: TKey) -> TValue: ...
    
    def GetValue(self, key: TKey, createValueCallback: CreateValueCallback[TKey, TValue]) -> TValue: ...
    
    def Remove(self, key: TKey) -> BooleanType: ...
    
    def TryGetValue(self, key: TKey, value: TValue) -> Tuple[BooleanType, TValue]: ...
    
    # No Events
    
    
    # ---------- Sub Classes ---------- #
    
    class CreateValueCallback(Generic[TKey, TValue], MulticastDelegate, ICloneable, ISerializable):
        # No Fields
        
        # ---------- Constructors ---------- #
        
        def __init__(self, object: ObjectType, method: NIntType): ...
        
        # No Properties
        
        # ---------- Methods ---------- #
        
        def BeginInvoke(self, key: TKey, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
        
        def EndInvoke(self, result: IAsyncResult) -> TValue: ...
        
        def Invoke(self, key: TKey) -> TValue: ...
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContractHelper(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def RaiseContractFailedEvent(failureKind: ContractFailureKind, userMessage: StringType, conditionText: StringType, innerException: Exception) -> StringType: ...
    
    @staticmethod
    def TriggerFailure(kind: ContractFailureKind, displayMessage: StringType, userMessage: StringType, conditionText: StringType, innerException: Exception) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CustomConstantAttribute(ABC, Attribute, _Attribute):
    # No Fields
    
    # No Constructors
    
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


class DateTimeConstantAttribute(CustomConstantAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, ticks: LongType): ...
    
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


class DecimalConstantAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, scale: ByteType, sign: ByteType, hi: UIntType, mid: UIntType, low: UIntType): ...
    
    @overload
    def __init__(self, scale: ByteType, sign: ByteType, hi: IntType, mid: IntType, low: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DecimalType: ...
    
    # ---------- Methods ---------- #
    
    def get_Value(self) -> DecimalType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoratedNameAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, decoratedName: StringType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DefaultDependencyAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, loadHintArgument: LoadHint): ...
    
    # ---------- Properties ---------- #
    
    @property
    def LoadHint(self) -> LoadHint: ...
    
    # ---------- Methods ---------- #
    
    def get_LoadHint(self) -> LoadHint: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DependencyAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, dependentAssemblyArgument: StringType, loadHintArgument: LoadHint): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DependentAssembly(self) -> StringType: ...
    
    @property
    def LoadHint(self) -> LoadHint: ...
    
    # ---------- Methods ---------- #
    
    def get_DependentAssembly(self) -> StringType: ...
    
    def get_LoadHint(self) -> LoadHint: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DisablePrivateReflectionAttribute(Attribute, _Attribute):
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


class DiscardableAttribute(Attribute, _Attribute):
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


class ExtensionAttribute(Attribute, _Attribute):
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


class FixedAddressValueTypeAttribute(Attribute, _Attribute):
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


class FixedBufferAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, elementType: TypeType, length: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ElementType(self) -> TypeType: ...
    
    @property
    def Length(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_ElementType(self) -> TypeType: ...
    
    def get_Length(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FormattableStringFactory(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Create(format: StringType, arguments: ArrayType[ObjectType]) -> FormattableString: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FriendAccessAllowedAttribute(Attribute, _Attribute):
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


class HasCopySemanticsAttribute(Attribute, _Attribute):
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


class IDispatchConstantAttribute(CustomConstantAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
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


class IUnknownConstantAttribute(CustomConstantAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
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


class IndexerNameAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, indexerName: StringType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalsVisibleToAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, assemblyName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AllInternalsVisible(self) -> BooleanType: ...
    
    @AllInternalsVisible.setter
    def AllInternalsVisible(self, value: BooleanType) -> None: ...
    
    @property
    def AssemblyName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllInternalsVisible(self) -> BooleanType: ...
    
    def get_AssemblyName(self) -> StringType: ...
    
    def set_AllInternalsVisible(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IsBoxed(ABC, ObjectType):
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


class IsByRefLikeAttribute(Attribute, _Attribute):
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


class IsByValue(ABC, ObjectType):
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


class IsConst(ABC, ObjectType):
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


class IsCopyConstructed(ABC, ObjectType):
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


class IsExplicitlyDereferenced(ABC, ObjectType):
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


class IsImplicitlyDereferenced(ABC, ObjectType):
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


class IsJitIntrinsic(ABC, ObjectType):
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


class IsLong(ABC, ObjectType):
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


class IsPinned(ABC, ObjectType):
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


class IsReadOnlyAttribute(Attribute, _Attribute):
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


class IsSignUnspecifiedByte(ABC, ObjectType):
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


class IsUdtReturn(ABC, ObjectType):
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


class IsVolatile(ABC, ObjectType):
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


class IteratorStateMachineAttribute(StateMachineAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, stateMachineType: TypeType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class JitHelpers(ABC, ObjectType):
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


class MethodImplAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @property
    def MethodCodeType(self) -> MethodCodeType: ...
    
    @MethodCodeType.setter
    def MethodCodeType(self, value: MethodCodeType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, methodImplOptions: MethodImplOptions): ...
    
    @overload
    def __init__(self, value: ShortType): ...
    
    @overload
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> MethodImplOptions: ...
    
    # ---------- Methods ---------- #
    
    def get_Value(self) -> MethodImplOptions: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NativeCppClassAttribute(Attribute, _Attribute):
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


class PinningHelper(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def m_data(self) -> ByteType: ...
    
    @m_data.setter
    def m_data(self, value: ByteType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReferenceAssemblyAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
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


class RequiredAttributeAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, requiredContract: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def RequiredContract(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_RequiredContract(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RuntimeCompatibilityAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def WrapNonExceptionThrows(self) -> BooleanType: ...
    
    @WrapNonExceptionThrows.setter
    def WrapNonExceptionThrows(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_WrapNonExceptionThrows(self) -> BooleanType: ...
    
    def set_WrapNonExceptionThrows(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RuntimeFeature(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def PortablePdb() -> StringType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def IsSupported(feature: StringType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RuntimeHelpers(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def OffsetToStringData() -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def EnsureSufficientExecutionStack() -> VoidType: ...
    
    @staticmethod
    @overload
    def Equals(o1: ObjectType, o2: ObjectType) -> BooleanType: ...
    
    @staticmethod
    def ExecuteCodeWithGuaranteedCleanup(code: TryCode, backoutCode: CleanupCode, userData: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def GetHashCode(o: ObjectType) -> IntType: ...
    
    @staticmethod
    def GetObjectValue(obj: ObjectType) -> ObjectType: ...
    
    @staticmethod
    def InitializeArray(array: Array, fldHandle: RuntimeFieldHandle) -> VoidType: ...
    
    @staticmethod
    def PrepareConstrainedRegions() -> VoidType: ...
    
    @staticmethod
    def PrepareConstrainedRegionsNoOP() -> VoidType: ...
    
    @staticmethod
    def PrepareContractedDelegate(d: Delegate) -> VoidType: ...
    
    @staticmethod
    def PrepareDelegate(d: Delegate) -> VoidType: ...
    
    @staticmethod
    @overload
    def PrepareMethod(method: RuntimeMethodHandle) -> VoidType: ...
    
    @staticmethod
    @overload
    def PrepareMethod(method: RuntimeMethodHandle, instantiation: ArrayType[RuntimeTypeHandle]) -> VoidType: ...
    
    @staticmethod
    def ProbeForSufficientStack() -> VoidType: ...
    
    @staticmethod
    def RunClassConstructor(type: RuntimeTypeHandle) -> VoidType: ...
    
    @staticmethod
    def RunModuleConstructor(module: ModuleHandle) -> VoidType: ...
    
    @staticmethod
    def get_OffsetToStringData() -> IntType: ...
    
    # No Events
    
    
    # ---------- Sub Classes ---------- #
    
    class TryCode(MulticastDelegate, ICloneable, ISerializable):
        # No Fields
        
        # ---------- Constructors ---------- #
        
        def __init__(self, object: ObjectType, method: NIntType): ...
        
        # No Properties
        
        # ---------- Methods ---------- #
        
        def BeginInvoke(self, userData: ObjectType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
        
        def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
        
        def Invoke(self, userData: ObjectType) -> VoidType: ...
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    class CleanupCode(MulticastDelegate, ICloneable, ISerializable):
        # No Fields
        
        # ---------- Constructors ---------- #
        
        def __init__(self, object: ObjectType, method: NIntType): ...
        
        # No Properties
        
        # ---------- Methods ---------- #
        
        def BeginInvoke(self, userData: ObjectType, exceptionThrown: BooleanType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
        
        def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
        
        def Invoke(self, userData: ObjectType, exceptionThrown: BooleanType) -> VoidType: ...
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RuntimeWrappedException(Exception, ISerializable, _Exception):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def WrappedException(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_WrappedException(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ScopelessEnumAttribute(Attribute, _Attribute):
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


class SpecialNameAttribute(Attribute, _Attribute):
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


class StateMachineAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, stateMachineType: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def StateMachineType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_StateMachineType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringFreezingAttribute(Attribute, _Attribute):
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


class SuppressIldasmAttribute(Attribute, _Attribute):
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


class SuppressMergeCheckAttribute(Attribute, _Attribute):
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


class TupleElementNamesAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, transformNames: ArrayType[StringType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TransformNames(self) -> IList[StringType]: ...
    
    # ---------- Methods ---------- #
    
    def get_TransformNames(self) -> IList[StringType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeDependencyAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, typeName: StringType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeForwardedFromAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, assemblyFullName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AssemblyFullName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AssemblyFullName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeForwardedToAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, destination: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Destination(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_Destination(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnsafeValueTypeAttribute(Attribute, _Attribute):
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


# ---------- Structs ---------- #

class AsyncMethodBuilderCore(ValueType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def SetStateMachine(self, stateMachine: IAsyncStateMachine) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsyncTaskMethodBuilder(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Task(self) -> Task: ...
    
    # ---------- Methods ---------- #
    
    def AwaitOnCompleted(self, awaiter: TAwaiter, stateMachine: TStateMachine) -> Tuple[VoidType, TAwaiter, TStateMachine]: ...
    
    def AwaitUnsafeOnCompleted(self, awaiter: TAwaiter, stateMachine: TStateMachine) -> Tuple[VoidType, TAwaiter, TStateMachine]: ...
    
    @staticmethod
    def Create() -> AsyncTaskMethodBuilder: ...
    
    def SetException(self, exception: Exception) -> VoidType: ...
    
    def SetResult(self) -> VoidType: ...
    
    def SetStateMachine(self, stateMachine: IAsyncStateMachine) -> VoidType: ...
    
    def Start(self, stateMachine: TStateMachine) -> Tuple[VoidType, TStateMachine]: ...
    
    def get_Task(self) -> Task: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsyncTaskMethodBuilder(Generic[TResult], ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Task(self) -> Task[TResult]: ...
    
    # ---------- Methods ---------- #
    
    def AwaitOnCompleted(self, awaiter: TAwaiter, stateMachine: TStateMachine) -> Tuple[VoidType, TAwaiter, TStateMachine]: ...
    
    def AwaitUnsafeOnCompleted(self, awaiter: TAwaiter, stateMachine: TStateMachine) -> Tuple[VoidType, TAwaiter, TStateMachine]: ...
    
    @staticmethod
    def Create() -> AsyncTaskMethodBuilder[TResult]: ...
    
    def SetException(self, exception: Exception) -> VoidType: ...
    
    def SetResult(self, result: TResult) -> VoidType: ...
    
    def SetStateMachine(self, stateMachine: IAsyncStateMachine) -> VoidType: ...
    
    def Start(self, stateMachine: TStateMachine) -> Tuple[VoidType, TStateMachine]: ...
    
    def get_Task(self) -> Task[TResult]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsyncVoidMethodBuilder(ValueType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AwaitOnCompleted(self, awaiter: TAwaiter, stateMachine: TStateMachine) -> Tuple[VoidType, TAwaiter, TStateMachine]: ...
    
    def AwaitUnsafeOnCompleted(self, awaiter: TAwaiter, stateMachine: TStateMachine) -> Tuple[VoidType, TAwaiter, TStateMachine]: ...
    
    @staticmethod
    def Create() -> AsyncVoidMethodBuilder: ...
    
    def SetException(self, exception: Exception) -> VoidType: ...
    
    def SetResult(self) -> VoidType: ...
    
    def SetStateMachine(self, stateMachine: IAsyncStateMachine) -> VoidType: ...
    
    def Start(self, stateMachine: TStateMachine) -> Tuple[VoidType, TStateMachine]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConfiguredTaskAwaitable(ValueType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetAwaiter(self) -> ConfiguredTaskAwaiter: ...
    
    # No Events
    
    # No Sub Classes
    
    # ---------- Sub Structs ---------- #
    
    class ConfiguredTaskAwaiter(ValueType, ICriticalNotifyCompletion, INotifyCompletion):
        # No Fields
        
        # No Constructors
        
        # ---------- Properties ---------- #
        
        @property
        def IsCompleted(self) -> BooleanType: ...
        
        # ---------- Methods ---------- #
        
        def GetResult(self) -> VoidType: ...
        
        def OnCompleted(self, continuation: Action) -> VoidType: ...
        
        def UnsafeOnCompleted(self, continuation: Action) -> VoidType: ...
        
        def get_IsCompleted(self) -> BooleanType: ...
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConfiguredTaskAwaitable(Generic[TResult], ValueType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetAwaiter(self) -> ConfiguredTaskAwaiter[TResult]: ...
    
    # No Events
    
    # No Sub Classes
    
    # ---------- Sub Structs ---------- #
    
    class ConfiguredTaskAwaiter(Generic[TResult], ValueType, ICriticalNotifyCompletion, INotifyCompletion):
        # No Fields
        
        # No Constructors
        
        # ---------- Properties ---------- #
        
        @property
        def IsCompleted(self) -> BooleanType: ...
        
        # ---------- Methods ---------- #
        
        def GetResult(self) -> TResult: ...
        
        def OnCompleted(self, continuation: Action) -> VoidType: ...
        
        def UnsafeOnCompleted(self, continuation: Action) -> VoidType: ...
        
        def get_IsCompleted(self) -> BooleanType: ...
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Interfaces
    
    # No Sub Enums


class DependentHandle(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, primary: ObjectType, secondary: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsAllocated(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Free(self) -> VoidType: ...
    
    def GetPrimary(self) -> ObjectType: ...
    
    def GetPrimaryAndSecondary(self, primary: ObjectType, secondary: ObjectType) -> Tuple[VoidType, ObjectType, ObjectType]: ...
    
    def get_IsAllocated(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ObjectHandleOnStack(ValueType):
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


class StackCrawlMarkHandle(ValueType):
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


class StringHandleOnStack(ValueType):
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


class TaskAwaiter(ValueType, ICriticalNotifyCompletion, INotifyCompletion):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsCompleted(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def GetResult(self) -> VoidType: ...
    
    def OnCompleted(self, continuation: Action) -> VoidType: ...
    
    def UnsafeOnCompleted(self, continuation: Action) -> VoidType: ...
    
    def get_IsCompleted(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TaskAwaiter(Generic[TResult], ValueType, ICriticalNotifyCompletion, INotifyCompletion):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsCompleted(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def GetResult(self) -> TResult: ...
    
    def OnCompleted(self, continuation: Action) -> VoidType: ...
    
    def UnsafeOnCompleted(self, continuation: Action) -> VoidType: ...
    
    def get_IsCompleted(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class YieldAwaitable(ValueType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetAwaiter(self) -> YieldAwaiter: ...
    
    # No Events
    
    # No Sub Classes
    
    # ---------- Sub Structs ---------- #
    
    class YieldAwaiter(ValueType, ICriticalNotifyCompletion, INotifyCompletion):
        # No Fields
        
        # No Constructors
        
        # ---------- Properties ---------- #
        
        @property
        def IsCompleted(self) -> BooleanType: ...
        
        # ---------- Methods ---------- #
        
        def GetResult(self) -> VoidType: ...
        
        def OnCompleted(self, continuation: Action) -> VoidType: ...
        
        def UnsafeOnCompleted(self, continuation: Action) -> VoidType: ...
        
        def get_IsCompleted(self) -> BooleanType: ...
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Interfaces ---------- #

class IAsyncStateMachine(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> VoidType: ...
    
    def SetStateMachine(self, stateMachine: IAsyncStateMachine) -> VoidType: ...
    
    # No Events


class ICriticalNotifyCompletion(Protocol, INotifyCompletion):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def UnsafeOnCompleted(self, continuation: Action) -> VoidType: ...
    
    # No Events


class INotifyCompletion(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def OnCompleted(self, continuation: Action) -> VoidType: ...
    
    # No Events


class ITuple(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> ObjectType: ...
    
    @property
    def Length(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_Item(self, index: IntType) -> ObjectType: ...
    
    def get_Length(self) -> IntType: ...
    
    # No Events


# ---------- Enums ---------- #

class CompilationRelaxations(Enum):
    NoStringInterning: IntType = 8


class LoadHint(Enum):
    Default: IntType = 0
    Always: IntType = 1
    Sometimes: IntType = 2


class MethodCodeType(Enum):
    IL: IntType = 0
    Native: IntType = 1
    OPTIL: IntType = 2
    Runtime: IntType = 3


class MethodImplOptions(Enum):
    Unmanaged: IntType = 4
    NoInlining: IntType = 8
    ForwardRef: IntType = 16
    Synchronized: IntType = 32
    NoOptimization: IntType = 64
    PreserveSig: IntType = 128
    AggressiveInlining: IntType = 256
    SecurityMitigations: IntType = 1024
    InternalCall: IntType = 4096


# No Delegates

__all__ = [
    AccessedThroughPropertyAttribute,
    AssemblyAttributesGoHere,
    AssemblyAttributesGoHereM,
    AssemblyAttributesGoHereS,
    AssemblyAttributesGoHereSM,
    AsyncStateMachineAttribute,
    AsyncTaskCache,
    CallConvCdecl,
    CallConvFastcall,
    CallConvStdcall,
    CallConvThiscall,
    CallerFilePathAttribute,
    CallerLineNumberAttribute,
    CallerMemberNameAttribute,
    CompilationRelaxationsAttribute,
    CompilerGeneratedAttribute,
    CompilerGlobalScopeAttribute,
    CompilerMarshalOverride,
    ConditionalWeakTable,
    ContractHelper,
    CustomConstantAttribute,
    DateTimeConstantAttribute,
    DecimalConstantAttribute,
    DecoratedNameAttribute,
    DefaultDependencyAttribute,
    DependencyAttribute,
    DisablePrivateReflectionAttribute,
    DiscardableAttribute,
    ExtensionAttribute,
    FixedAddressValueTypeAttribute,
    FixedBufferAttribute,
    FormattableStringFactory,
    FriendAccessAllowedAttribute,
    HasCopySemanticsAttribute,
    IDispatchConstantAttribute,
    IUnknownConstantAttribute,
    IndexerNameAttribute,
    InternalsVisibleToAttribute,
    IsBoxed,
    IsByRefLikeAttribute,
    IsByValue,
    IsConst,
    IsCopyConstructed,
    IsExplicitlyDereferenced,
    IsImplicitlyDereferenced,
    IsJitIntrinsic,
    IsLong,
    IsPinned,
    IsReadOnlyAttribute,
    IsSignUnspecifiedByte,
    IsUdtReturn,
    IsVolatile,
    IteratorStateMachineAttribute,
    JitHelpers,
    MethodImplAttribute,
    NativeCppClassAttribute,
    PinningHelper,
    ReferenceAssemblyAttribute,
    RequiredAttributeAttribute,
    RuntimeCompatibilityAttribute,
    RuntimeFeature,
    RuntimeHelpers,
    RuntimeWrappedException,
    ScopelessEnumAttribute,
    SpecialNameAttribute,
    StateMachineAttribute,
    StringFreezingAttribute,
    SuppressIldasmAttribute,
    SuppressMergeCheckAttribute,
    TupleElementNamesAttribute,
    TypeDependencyAttribute,
    TypeForwardedFromAttribute,
    TypeForwardedToAttribute,
    UnsafeValueTypeAttribute,
    AsyncMethodBuilderCore,
    AsyncTaskMethodBuilder,
    AsyncVoidMethodBuilder,
    ConfiguredTaskAwaitable,
    DependentHandle,
    ObjectHandleOnStack,
    StackCrawlMarkHandle,
    StringHandleOnStack,
    TaskAwaiter,
    YieldAwaitable,
    IAsyncStateMachine,
    ICriticalNotifyCompletion,
    INotifyCompletion,
    ITuple,
    CompilationRelaxations,
    LoadHint,
    MethodCodeType,
    MethodImplOptions,
]
