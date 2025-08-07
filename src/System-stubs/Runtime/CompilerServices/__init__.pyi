"""Automatically generated stubs for C# namespace: System.Runtime.CompilerServices."""

from abc import ABC
from collections.abc import Callable
from collections.abc import Iterator
from typing import ClassVar
from typing import Final
from typing import overload

from System import Action
from System import Array
from System import Attribute
from System import Decimal
from System import Delegate
from System import Enum
from System import Exception
from System import FormattableString
from System import Guid
from System import IntPtr
from System import ModuleHandle
from System import Object
from System import RuntimeFieldHandle
from System import RuntimeMethodHandle
from System import RuntimeTypeHandle
from System import Type
from System import UInt32
from System import ValueType
from System.Collections import ICollection
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IList
from System.Collections.Generic import ICollection
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEnumerator
from System.Collections.Generic import IList
from System.Collections.Generic import IReadOnlyCollection
from System.Collections.Generic import IReadOnlyList
from System.Collections.ObjectModel import ReadOnlyCollection
from System.Diagnostics.Contracts import ContractFailureKind
from System.Dynamic import ExpandoObject
from System.Linq.Expressions import DebugInfoExpression
from System.Linq.Expressions import Expression
from System.Linq.Expressions import LabelTarget
from System.Linq.Expressions import LambdaExpression
from System.Linq.Expressions import ParameterExpression
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Attribute
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Threading.Tasks import Task

class AccessedThroughPropertyAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, propertyName: str) -> None:
        """"""
    @property
    def PropertyName(self) -> str:
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

class AssemblyAttributesGoHere(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class AssemblyAttributesGoHereM(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class AssemblyAttributesGoHereS(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class AssemblyAttributesGoHereSM(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class AsyncMethodBuilderCore(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetStateMachine(self, stateMachine: IAsyncStateMachine) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class AsyncStateMachineAttribute(StateMachineAttribute, _Attribute):
    """"""
    def __init__(self, stateMachineType: Type) -> None:
        """"""
    @property
    def StateMachineType(self) -> Type:
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

class AsyncTaskCache(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class AsyncTaskMethodBuilder(ValueType):
    """"""
    @property
    def Task(self) -> Task:
        """"""
    def AwaitOnCompleted(self, awaiter: TAwaiter, stateMachine: TStateMachine) -> None:
        """"""
    def AwaitUnsafeOnCompleted(self, awaiter: TAwaiter, stateMachine: TStateMachine) -> None:
        """"""
    @classmethod
    def Create(cls) -> AsyncTaskMethodBuilder:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetException(self, exception: Exception) -> None:
        """"""
    def SetResult(self) -> None:
        """"""
    def SetStateMachine(self, stateMachine: IAsyncStateMachine) -> None:
        """"""
    def Start(self, stateMachine: TStateMachine) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class AsyncTaskMethodBuilder[TResult](ValueType):
    """"""
    @property
    def Task(self) -> Task[TResult]:
        """"""
    def AwaitOnCompleted(self, awaiter: TAwaiter, stateMachine: TStateMachine) -> None:
        """"""
    def AwaitUnsafeOnCompleted(self, awaiter: TAwaiter, stateMachine: TStateMachine) -> None:
        """"""
    @classmethod
    def Create(cls) -> AsyncTaskMethodBuilder[TResult]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetException(self, exception: Exception) -> None:
        """"""
    def SetResult[TResult](self, result: TResult) -> None:
        """"""
    def SetStateMachine(self, stateMachine: IAsyncStateMachine) -> None:
        """"""
    def Start(self, stateMachine: TStateMachine) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class AsyncVoidMethodBuilder(ValueType):
    """"""
    def AwaitOnCompleted(self, awaiter: TAwaiter, stateMachine: TStateMachine) -> None:
        """"""
    def AwaitUnsafeOnCompleted(self, awaiter: TAwaiter, stateMachine: TStateMachine) -> None:
        """"""
    @classmethod
    def Create(cls) -> AsyncVoidMethodBuilder:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetException(self, exception: Exception) -> None:
        """"""
    def SetResult(self) -> None:
        """"""
    def SetStateMachine(self, stateMachine: IAsyncStateMachine) -> None:
        """"""
    def Start(self, stateMachine: TStateMachine) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class CallConvCdecl(Object):
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

class CallConvFastcall(Object):
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

class CallConvStdcall(Object):
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

class CallConvThiscall(Object):
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

class CallSite(Object):
    """"""
    @property
    def Binder(self) -> CallSiteBinder:
        """"""
    @classmethod
    def Create(cls, delegateType: Type, binder: CallSiteBinder) -> CallSite:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CallSiteBinder(ABC, Object):
    """"""
    @classmethod
    @property
    def UpdateLabel(cls) -> LabelTarget:
        """"""
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """"""
    def BindDelegate[T](self, site: CallSite[T], args: Array[object]) -> T:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CallSiteHelpers(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsInternalFrame(cls, mb: MethodBase) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class CallSiteOps(ABC, Object):
    """"""
    @classmethod
    def AddRule[T](cls, site: CallSite[T], rule: T) -> None:
        """"""
    @classmethod
    def Bind[T](cls, binder: CallSiteBinder, site: CallSite[T], args: Array[object]) -> T:
        """"""
    @classmethod
    def ClearMatch(cls, site: CallSite) -> None:
        """"""
    @classmethod
    def CreateMatchmaker(cls, site: CallSite[T]) -> CallSite[T]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetCachedRules(cls, cache: RuleCache[T]) -> Array[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetMatch(cls, site: CallSite) -> bool:
        """"""
    @classmethod
    def GetRuleCache(cls, site: CallSite[T]) -> RuleCache[T]:
        """"""
    @classmethod
    def GetRules(cls, site: CallSite[T]) -> Array[T]:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def MoveRule[T](cls, cache: RuleCache[T], rule: T, i: int) -> None:
        """"""
    @classmethod
    def SetNotMatched(cls, site: CallSite) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def UpdateRules(cls, this: CallSite[T], matched: int) -> None:
        """"""

class CallSite[T](CallSite):
    """"""

    Target: Final[T]
    """"""
    @property
    def Binder(self) -> CallSiteBinder:
        """"""
    @property
    def Update(self) -> T:
        """"""
    @classmethod
    def Create(cls, binder: CallSiteBinder) -> CallSite[T]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CallerFilePathAttribute(Attribute, _Attribute):
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

class CallerLineNumberAttribute(Attribute, _Attribute):
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

class CallerMemberNameAttribute(Attribute, _Attribute):
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

class Closure(Object):
    """"""

    Constants: Final[Array[object]]
    """"""
    Locals: Final[Array[object]]
    """"""
    def __init__(self, constants: Array[object], locals: Array[object]) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CompilationRelaxations(Enum):
    """"""

    NoStringInterning: CompilationRelaxations = ...
    """"""

class CompilationRelaxationsAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, relaxations: int) -> None:
        """"""
    @overload
    def __init__(self, relaxations: CompilationRelaxations) -> None:
        """"""
    @property
    def CompilationRelaxations(self) -> int:
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

class CompilerGeneratedAttribute(Attribute, _Attribute):
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

class CompilerGlobalScopeAttribute(Attribute, _Attribute):
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

class CompilerMarshalOverride(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ConditionalWeakTable[TKey, TValue](Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Add[TKey, TValue](self, key: TKey, value: TValue) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOrCreateValue[TKey, TValue](self, key: TKey) -> TValue:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetValue[TKey, TValue](
        self, key: TKey, createValueCallback: ConditionalWeakTable.CreateValueCallback[TKey, TValue]
    ) -> TValue:
        """"""
    def Remove[TKey](self, key: TKey) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def TryGetValue[TKey](self, key: TKey, value: TValue) -> tuple[bool, TValue]:
        """"""
    def __delitem__[TKey](self, key: TKey) -> bool:
        """"""
    CreateValueCallback: Callable[[TKey], TValue] = ...
    """"""

class ConfiguredTaskAwaitable(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAwaiter(self) -> ConfiguredTaskAwaitable.ConfiguredTaskAwaiter:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    class ConfiguredTaskAwaiter(ValueType, ICriticalNotifyCompletion, INotifyCompletion):
        """"""
        @property
        def IsCompleted(self) -> bool:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetResult(self) -> None:
            """"""
        def GetType(self) -> Type:
            """"""
        def OnCompleted(self, continuation: Action) -> None:
            """"""
        def ToString(self) -> str:
            """"""
        def UnsafeOnCompleted(self, continuation: Action) -> None:
            """"""

class ConfiguredTaskAwaitable[TResult](ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAwaiter(self) -> ConfiguredTaskAwaitable.ConfiguredTaskAwaiter[TResult]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    class ConfiguredTaskAwaiter[TResult](ValueType, ICriticalNotifyCompletion, INotifyCompletion):
        """"""
        @property
        def IsCompleted(self) -> bool:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetResult[TResult](self) -> TResult:
            """"""
        def GetType(self) -> Type:
            """"""
        def OnCompleted(self, continuation: Action) -> None:
            """"""
        def ToString(self) -> str:
            """"""
        def UnsafeOnCompleted(self, continuation: Action) -> None:
            """"""

class ContractHelper(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def RaiseContractFailedEvent(
        cls,
        failureKind: ContractFailureKind,
        userMessage: str,
        conditionText: str,
        innerException: Exception,
    ) -> str:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def TriggerFailure(
        cls,
        kind: ContractFailureKind,
        displayMessage: str,
        userMessage: str,
        conditionText: str,
        innerException: Exception,
    ) -> None:
        """"""

class CustomConstantAttribute(ABC, Attribute, _Attribute):
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

class DateTimeConstantAttribute(CustomConstantAttribute, _Attribute):
    """"""
    def __init__(self, ticks: int) -> None:
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

class DebugInfoGenerator(ABC, Object):
    """"""
    @classmethod
    def CreatePdbGenerator(cls) -> DebugInfoGenerator:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MarkSequencePoint(
        self, method: LambdaExpression, ilOffset: int, sequencePoint: DebugInfoExpression
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class DecimalConstantAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, scale: int, sign: int, hi: int, mid: int, low: int) -> None:
        """"""
    @overload
    def __init__(self, scale: int, sign: int, hi: int, mid: int, low: int) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Value(self) -> Decimal:
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

class DecoratedNameAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, decoratedName: str) -> None:
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

class DefaultDependencyAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, loadHintArgument: LoadHint) -> None:
        """"""
    @property
    def LoadHint(self) -> LoadHint:
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

class DependencyAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, dependentAssemblyArgument: str, loadHintArgument: LoadHint) -> None:
        """"""
    @property
    def DependentAssembly(self) -> str:
        """"""
    @property
    def LoadHint(self) -> LoadHint:
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

class DependentHandle(ValueType):
    """"""
    def __init__(self, primary: object, secondary: object) -> None:
        """"""
    @property
    def IsAllocated(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Free(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetPrimary(self) -> object:
        """"""
    def GetPrimaryAndSecondary(
        self, primary: Object, secondary: Object
    ) -> tuple[None, Object, Object]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DisablePrivateReflectionAttribute(Attribute, _Attribute):
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

class DiscardableAttribute(Attribute, _Attribute):
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

class DynamicAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, transformFlags: Array[bool]) -> None:
        """"""
    @property
    def TransformFlags(self) -> IList[bool]:
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

class ExecutionScope(Object):
    """"""

    Globals: Final[Array[object]]
    """"""
    Locals: Final[Array[object]]
    """"""
    Parent: Final[ExecutionScope]
    """"""
    def CreateDelegate(self, indexLambda: int, locals: Array[object]) -> Delegate:
        """"""
    def CreateHoistedLocals(self) -> Array[object]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsolateExpression(self, expression: Expression, locals: Array[object]) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""

class ExtensionAttribute(Attribute, _Attribute):
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

class FixedAddressValueTypeAttribute(Attribute, _Attribute):
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

class FixedBufferAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, elementType: Type, length: int) -> None:
        """"""
    @property
    def ElementType(self) -> Type:
        """"""
    @property
    def Length(self) -> int:
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

class FormattableStringFactory(ABC, Object):
    """"""
    @classmethod
    def Create(cls, format: str, arguments: Array[object]) -> FormattableString:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class FriendAccessAllowedAttribute(Attribute, _Attribute):
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

class HasCopySemanticsAttribute(Attribute, _Attribute):
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

class IAsyncStateMachine:
    """"""
    def MoveNext(self) -> None:
        """"""
    def SetStateMachine(self, stateMachine: IAsyncStateMachine) -> None:
        """"""

class ICriticalNotifyCompletion(INotifyCompletion):
    """"""
    def OnCompleted(self, continuation: Action) -> None:
        """"""
    def UnsafeOnCompleted(self, continuation: Action) -> None:
        """"""

class IDispatchConstantAttribute(CustomConstantAttribute, _Attribute):
    """"""
    def __init__(self) -> None:
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

class INotifyCompletion:
    """"""
    def OnCompleted(self, continuation: Action) -> None:
        """"""

class IRuntimeVariables:
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""
    def __setitem__(self, index: int, value: object) -> None:
        """"""

class IStrongBox:
    """"""
    @property
    def Value(self) -> object:
        """"""
    @Value.setter
    def Value(self, value: object) -> None: ...

class ITuple:
    """"""
    @property
    def Item(self) -> object:
        """"""
    @property
    def Length(self) -> int:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""

class IUnknownConstantAttribute(CustomConstantAttribute, _Attribute):
    """"""
    def __init__(self) -> None:
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

class IndexerNameAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, indexerName: str) -> None:
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

class InternalsVisibleToAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, assemblyName: str) -> None:
        """"""
    @property
    def AllInternalsVisible(self) -> bool:
        """"""
    @AllInternalsVisible.setter
    def AllInternalsVisible(self, value: bool) -> None: ...
    @property
    def AssemblyName(self) -> str:
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

class IsBoxed(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IsByRefLikeAttribute(Attribute, _Attribute):
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

class IsByValue(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IsConst(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IsCopyConstructed(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IsExplicitlyDereferenced(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IsImplicitlyDereferenced(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IsJitIntrinsic(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IsLong(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IsPinned(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IsReadOnlyAttribute(Attribute, _Attribute):
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

class IsSignUnspecifiedByte(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IsUdtReturn(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IsVolatile(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IteratorStateMachineAttribute(StateMachineAttribute, _Attribute):
    """"""
    def __init__(self, stateMachineType: Type) -> None:
        """"""
    @property
    def StateMachineType(self) -> Type:
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

class JitHelpers(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class LoadHint(Enum):
    """"""

    Default: LoadHint = ...
    """"""
    Always: LoadHint = ...
    """"""
    Sometimes: LoadHint = ...
    """"""

class MethodCodeType(Enum):
    """"""

    IL: MethodCodeType = ...
    """"""
    Native: MethodCodeType = ...
    """"""
    OPTIL: MethodCodeType = ...
    """"""
    Runtime: MethodCodeType = ...
    """"""

class MethodImplAttribute(Attribute, _Attribute):
    """"""

    MethodCodeType: Final[MethodCodeType]
    """"""
    @overload
    def __init__(self, methodImplOptions: MethodImplOptions) -> None:
        """"""
    @overload
    def __init__(self, value: int) -> None:
        """"""
    @overload
    def __init__(self) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Value(self) -> MethodImplOptions:
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

class MethodImplOptions(Enum):
    """"""

    Unmanaged: MethodImplOptions = ...
    """"""
    NoInlining: MethodImplOptions = ...
    """"""
    ForwardRef: MethodImplOptions = ...
    """"""
    Synchronized: MethodImplOptions = ...
    """"""
    NoOptimization: MethodImplOptions = ...
    """"""
    PreserveSig: MethodImplOptions = ...
    """"""
    AggressiveInlining: MethodImplOptions = ...
    """"""
    SecurityMitigations: MethodImplOptions = ...
    """"""
    InternalCall: MethodImplOptions = ...
    """"""

class NativeCppClassAttribute(Attribute, _Attribute):
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

class ObjectHandleOnStack(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PinningHelper(Object):
    """"""

    m_data: Final[int]
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

class ReadOnlyCollectionBuilder[T](
    Object, ICollection[T], IEnumerable[T], IList[T], ICollection, IEnumerable, IList
):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, capacity: int) -> None:
        """"""
    @overload
    def __init__(self, collection: IEnumerable[T]) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
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
    def Item(self) -> T:
        """"""
    @Item.setter
    def Item(self, value: T) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add[T](self, item: T) -> None:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains[T](self, item: T) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf[T](self, item: T) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert[T](self, index: int, item: T) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove[T](self, item: T) -> bool:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    @overload
    def Reverse(self) -> None:
        """"""
    @overload
    def Reverse(self, index: int, count: int) -> None:
        """"""
    def ToArray(self) -> Array[T]:
        """"""
    def ToReadOnlyCollection(self) -> ReadOnlyCollection[T]:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__[T](self, item: T) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator[T]:
        """"""
    @overload
    def __delitem__[T](self, item: T) -> bool:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__[T](self, index: int) -> T:
        """"""
    @overload
    def __setitem__[T](self, index: int, value: T) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

class ReferenceAssemblyAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
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

class RequiredAttributeAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, requiredContract: Type) -> None:
        """"""
    @property
    def RequiredContract(self) -> Type:
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

class RuleCache[T](Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RuntimeCompatibilityAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def WrapNonExceptionThrows(self) -> bool:
        """"""
    @WrapNonExceptionThrows.setter
    def WrapNonExceptionThrows(self, value: bool) -> None: ...
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

class RuntimeFeature(ABC, Object):
    """"""

    PortablePdb: ClassVar[str]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsSupported(cls, feature: str) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class RuntimeHelpers(ABC, Object):
    """"""
    @classmethod
    @property
    def OffsetToStringData(cls) -> int:
        """"""
    @classmethod
    def EnsureSufficientExecutionStack(cls) -> None:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def Equals(cls, o1: object, o2: object) -> bool:
        """"""
    @classmethod
    def ExecuteCodeWithGuaranteedCleanup(
        cls, code: RuntimeHelpers.TryCode, backoutCode: RuntimeHelpers.CleanupCode, userData: object
    ) -> None:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    @overload
    def GetHashCode(cls, o: object) -> int:
        """"""
    @classmethod
    def GetObjectValue(cls, obj: object) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def InitializeArray(cls, array: Array, fldHandle: RuntimeFieldHandle) -> None:
        """"""
    @classmethod
    def PrepareConstrainedRegions(cls) -> None:
        """"""
    @classmethod
    def PrepareConstrainedRegionsNoOP(cls) -> None:
        """"""
    @classmethod
    def PrepareContractedDelegate(cls, d: Delegate) -> None:
        """"""
    @classmethod
    def PrepareDelegate(cls, d: Delegate) -> None:
        """"""
    @classmethod
    @overload
    def PrepareMethod(cls, method: RuntimeMethodHandle) -> None:
        """"""
    @classmethod
    @overload
    def PrepareMethod(
        cls, method: RuntimeMethodHandle, instantiation: Array[RuntimeTypeHandle]
    ) -> None:
        """"""
    @classmethod
    def ProbeForSufficientStack(cls) -> None:
        """"""
    @classmethod
    def RunClassConstructor(cls, type: RuntimeTypeHandle) -> None:
        """"""
    @classmethod
    def RunModuleConstructor(cls, module: ModuleHandle) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    CleanupCode: Callable[[object, bool], None] = ...
    """"""
    TryCode: Callable[[object], None] = ...
    """"""

class RuntimeOps(ABC, Object):
    """"""
    @classmethod
    @overload
    def CreateRuntimeVariables(cls) -> IRuntimeVariables:
        """"""
    @classmethod
    @overload
    def CreateRuntimeVariables(cls, data: Array[object], indexes: Array[int]) -> IRuntimeVariables:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def ExpandoCheckVersion(cls, expando: ExpandoObject, version: object) -> bool:
        """"""
    @classmethod
    def ExpandoPromoteClass(
        cls, expando: ExpandoObject, oldClass: object, newClass: object
    ) -> None:
        """"""
    @classmethod
    def ExpandoTryDeleteValue(
        cls, expando: ExpandoObject, indexClass: object, index: int, name: str, ignoreCase: bool
    ) -> bool:
        """"""
    @classmethod
    def ExpandoTryGetValue(
        cls,
        expando: ExpandoObject,
        indexClass: object,
        index: int,
        name: str,
        ignoreCase: bool,
        value: Object,
    ) -> tuple[bool, Object]:
        """"""
    @classmethod
    def ExpandoTrySetValue(
        cls,
        expando: ExpandoObject,
        indexClass: object,
        index: int,
        value: object,
        name: str,
        ignoreCase: bool,
    ) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def MergeRuntimeVariables(
        cls, first: IRuntimeVariables, second: IRuntimeVariables, indexes: Array[int]
    ) -> IRuntimeVariables:
        """"""
    @classmethod
    def Quote(
        cls, expression: Expression, hoistedLocals: object, locals: Array[object]
    ) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""

class RuntimeWrappedException(Exception, _Exception, ISerializable):
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
    def WrappedException(self) -> object:
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

class ScopelessEnumAttribute(Attribute, _Attribute):
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

class SpecialNameAttribute(Attribute, _Attribute):
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

class StackCrawlMarkHandle(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class StateMachineAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, stateMachineType: Type) -> None:
        """"""
    @property
    def StateMachineType(self) -> Type:
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

class StringFreezingAttribute(Attribute, _Attribute):
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

class StringHandleOnStack(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class StrongBox[T](Object, IStrongBox):
    """"""

    Value: Final[T]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: T) -> None:
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

class SuppressIldasmAttribute(Attribute, _Attribute):
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

class SuppressMergeCheckAttribute(Attribute, _Attribute):
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

class SymbolDocumentGenerator(DebugInfoGenerator):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MarkSequencePoint(
        self, method: LambdaExpression, ilOffset: int, sequencePoint: DebugInfoExpression
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class TaskAwaiter(ValueType, ICriticalNotifyCompletion, INotifyCompletion):
    """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetResult(self) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def OnCompleted(self, continuation: Action) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def UnsafeOnCompleted(self, continuation: Action) -> None:
        """"""

class TaskAwaiter[TResult](ValueType, ICriticalNotifyCompletion, INotifyCompletion):
    """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetResult[TResult](self) -> TResult:
        """"""
    def GetType(self) -> Type:
        """"""
    def OnCompleted(self, continuation: Action) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def UnsafeOnCompleted(self, continuation: Action) -> None:
        """"""

class TrueReadOnlyCollection[T](
    ReadOnlyCollection[T],
    ICollection[T],
    IEnumerable[T],
    IList[T],
    IReadOnlyCollection[T],
    IReadOnlyList[T],
    ICollection,
    IEnumerable,
    IList,
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
    def Item(self) -> T:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add[T](self, item: T) -> None:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains[T](self, value: T) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[T], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf[T](self, value: T) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert[T](self, index: int, item: T) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove[T](self, item: T) -> bool:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__[T](self, value: T) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator[T]:
        """"""
    @overload
    def __delitem__[T](self, item: T) -> bool:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__[T](self, index: int) -> T:
        """"""
    @overload
    def __setitem__[T](self, index: int, value: T) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

class TupleElementNamesAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, transformNames: Array[str]) -> None:
        """"""
    @property
    def TransformNames(self) -> IList[str]:
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

class TypeDependencyAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, typeName: str) -> None:
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

class TypeForwardedFromAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, assemblyFullName: str) -> None:
        """"""
    @property
    def AssemblyFullName(self) -> str:
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

class TypeForwardedToAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, destination: Type) -> None:
        """"""
    @property
    def Destination(self) -> Type:
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

class UnsafeValueTypeAttribute(Attribute, _Attribute):
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

class YieldAwaitable(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAwaiter(self) -> YieldAwaitable.YieldAwaiter:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    class YieldAwaiter(ValueType, ICriticalNotifyCompletion, INotifyCompletion):
        """"""
        @property
        def IsCompleted(self) -> bool:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetResult(self) -> None:
            """"""
        def GetType(self) -> Type:
            """"""
        def OnCompleted(self, continuation: Action) -> None:
            """"""
        def ToString(self) -> str:
            """"""
        def UnsafeOnCompleted(self, continuation: Action) -> None:
            """"""
