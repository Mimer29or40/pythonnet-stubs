from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Iterator
from typing import Tuple
from typing import TypeVar
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
from System import ValueType
from System.Collections import ICollection
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IList
from System.Collections.Generic import ICollection
from System.Collections.Generic import IEnumerable
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
from System.Runtime.CompilerServices.ConditionalWeakTable import CreateValueCallback
from System.Runtime.CompilerServices.ConfiguredTaskAwaitable import ConfiguredTaskAwaiter
from System.Runtime.CompilerServices.RuntimeHelpers import CleanupCode
from System.Runtime.CompilerServices.RuntimeHelpers import TryCode
from System.Runtime.CompilerServices.YieldAwaitable import YieldAwaiter
from System.Runtime.InteropServices import _Attribute
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Threading.Tasks import Task

T = TypeVar("T")
TKey = TypeVar("TKey")
TResult = TypeVar("TResult")
TValue = TypeVar("TValue")

class AccessedThroughPropertyAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, propertyName: str):
        """

        :param propertyName:
        """
    @property
    def PropertyName(self) -> str:
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

class AssemblyAttributesGoHere(Object):
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

class AssemblyAttributesGoHereM(Object):
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

class AssemblyAttributesGoHereS(Object):
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

class AssemblyAttributesGoHereSM(Object):
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

class AsyncMethodBuilderCore(ValueType):
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
    def SetStateMachine(self, stateMachine: IAsyncStateMachine) -> None:
        """

        :param stateMachine:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class AsyncStateMachineAttribute(StateMachineAttribute, _Attribute):
    """"""

    def __init__(self, stateMachineType: Type):
        """

        :param stateMachineType:
        """
    @property
    def StateMachineType(self) -> Type:
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

class AsyncTaskCache(ABC, Object):
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

class AsyncTaskMethodBuilder(ValueType):
    """"""

    @property
    def Task(self) -> Task:
        """

        :return:
        """
    def AwaitOnCompleted(self, awaiter: TAwaiter, stateMachine: TStateMachine) -> None:
        """

        :param awaiter:
        :param stateMachine:
        """
    def AwaitUnsafeOnCompleted(self, awaiter: TAwaiter, stateMachine: TStateMachine) -> None:
        """

        :param awaiter:
        :param stateMachine:
        """
    @classmethod
    def Create(cls) -> AsyncTaskMethodBuilder:
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
    def SetException(self, exception: Exception) -> None:
        """

        :param exception:
        """
    def SetResult(self) -> None:
        """"""
    def SetStateMachine(self, stateMachine: IAsyncStateMachine) -> None:
        """

        :param stateMachine:
        """
    def Start(self, stateMachine: TStateMachine) -> None:
        """

        :param stateMachine:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class AsyncTaskMethodBuilder(Generic[TResult], ValueType):
    """"""

    @property
    def Task(self) -> Task[TResult]:
        """

        :return:
        """
    def AwaitOnCompleted(self, awaiter: TAwaiter, stateMachine: TStateMachine) -> None:
        """

        :param awaiter:
        :param stateMachine:
        """
    def AwaitUnsafeOnCompleted(self, awaiter: TAwaiter, stateMachine: TStateMachine) -> None:
        """

        :param awaiter:
        :param stateMachine:
        """
    @classmethod
    def Create(cls) -> AsyncTaskMethodBuilder[TResult]:
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
    def SetException(self, exception: Exception) -> None:
        """

        :param exception:
        """
    def SetResult(self, result: TResult) -> None:
        """

        :param result:
        """
    def SetStateMachine(self, stateMachine: IAsyncStateMachine) -> None:
        """

        :param stateMachine:
        """
    def Start(self, stateMachine: TStateMachine) -> None:
        """

        :param stateMachine:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class AsyncVoidMethodBuilder(ValueType):
    """"""

    def AwaitOnCompleted(self, awaiter: TAwaiter, stateMachine: TStateMachine) -> None:
        """

        :param awaiter:
        :param stateMachine:
        """
    def AwaitUnsafeOnCompleted(self, awaiter: TAwaiter, stateMachine: TStateMachine) -> None:
        """

        :param awaiter:
        :param stateMachine:
        """
    @classmethod
    def Create(cls) -> AsyncVoidMethodBuilder:
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
    def SetException(self, exception: Exception) -> None:
        """

        :param exception:
        """
    def SetResult(self) -> None:
        """"""
    def SetStateMachine(self, stateMachine: IAsyncStateMachine) -> None:
        """

        :param stateMachine:
        """
    def Start(self, stateMachine: TStateMachine) -> None:
        """

        :param stateMachine:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CallConvCdecl(Object):
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

class CallConvFastcall(Object):
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

class CallConvStdcall(Object):
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

class CallConvThiscall(Object):
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

class CallSite(Object):
    """"""

    @property
    def Binder(self) -> CallSiteBinder:
        """

        :return:
        """
    @classmethod
    def Create(cls, delegateType: Type, binder: CallSiteBinder) -> CallSite:
        """

        :param delegateType:
        :param binder:
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

class CallSiteBinder(ABC, Object):
    """"""

    @classmethod
    @property
    def UpdateLabel(cls) -> LabelTarget:
        """

        :return:
        """
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """

        :param args:
        :param parameters:
        :param returnLabel:
        :return:
        """
    def BindDelegate(self, site: CallSite[T], args: Array[object]) -> T:
        """

        :param site:
        :param args:
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

class CallSiteHelpers(ABC, Object):
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
    def IsInternalFrame(cls, mb: MethodBase) -> bool:
        """

        :param mb:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CallSiteOps(ABC, Object):
    """"""

    @classmethod
    def AddRule(cls, site: CallSite[T], rule: T) -> None:
        """

        :param site:
        :param rule:
        """
    @classmethod
    def Bind(cls, binder: CallSiteBinder, site: CallSite[T], args: Array[object]) -> T:
        """

        :param binder:
        :param site:
        :param args:
        :return:
        """
    @classmethod
    def ClearMatch(cls, site: CallSite) -> None:
        """

        :param site:
        """
    @classmethod
    def CreateMatchmaker(cls, site: CallSite[T]) -> CallSite[T]:
        """

        :param site:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetCachedRules(cls, cache: RuleCache[T]) -> Array[T]:
        """

        :param cache:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    def GetMatch(cls, site: CallSite) -> bool:
        """

        :param site:
        :return:
        """
    @classmethod
    def GetRuleCache(cls, site: CallSite[T]) -> RuleCache[T]:
        """

        :param site:
        :return:
        """
    @classmethod
    def GetRules(cls, site: CallSite[T]) -> Array[T]:
        """

        :param site:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def MoveRule(cls, cache: RuleCache[T], rule: T, i: int) -> None:
        """

        :param cache:
        :param rule:
        :param i:
        """
    @classmethod
    def SetNotMatched(cls, site: CallSite) -> bool:
        """

        :param site:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def UpdateRules(cls, this: CallSite[T], matched: int) -> None:
        """

        :param this:
        :param matched:
        """

class CallSite(Generic[T], CallSite):
    """"""

    Target: Final[T] = ...
    """
    
    :return: 
    """
    @property
    def Binder(self) -> CallSiteBinder:
        """

        :return:
        """
    @property
    def Update(self) -> T:
        """

        :return:
        """
    @classmethod
    def Create(cls, binder: CallSiteBinder) -> CallSite[T]:
        """

        :param binder:
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

class CallerFilePathAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
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

class CallerLineNumberAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
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

class CallerMemberNameAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
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

class Closure(Object):
    """"""

    Constants: Final[Array[object]] = ...
    """
    
    :return: 
    """
    Locals: Final[Array[object]] = ...
    """
    
    :return: 
    """
    def __init__(self, constants: Array[object], locals: Array[object]):
        """

        :param constants:
        :param locals:
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

class CompilationRelaxations(Enum):
    """"""

    NoStringInterning: CompilationRelaxations = ...
    """"""

class CompilationRelaxationsAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, relaxations: CompilationRelaxations):
        """

        :param relaxations:
        """
    @overload
    def __init__(self, relaxations: int):
        """

        :param relaxations:
        """
    @property
    def CompilationRelaxations(self) -> int:
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

class CompilerGeneratedAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
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

class CompilerGlobalScopeAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
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

class CompilerMarshalOverride(ABC, Object):
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

class ConditionalWeakTable(Generic[TKey, TValue], Object):
    """"""

    def __init__(self):
        """"""
    def Add(self, key: TKey, value: TValue) -> None:
        """

        :param key:
        :param value:
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
    def GetOrCreateValue(self, key: TKey) -> TValue:
        """

        :param key:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetValue(
        self, key: TKey, createValueCallback: ConditionalWeakTable.CreateValueCallback[TKey, TValue]
    ) -> TValue:
        """

        :param key:
        :param createValueCallback:
        :return:
        """
    def Remove(self, key: TKey) -> bool:
        """

        :param key:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TryGetValue(self, key: TKey, value: TValue) -> Tuple[bool, TValue]:
        """

        :param key:
        :param value:
        :return:
        """
    CreateValueCallback: Callable[[TKey], TValue] = ...
    """
    
    :param key: 
    :return: 
    """

class ConfiguredTaskAwaitable(ValueType):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAwaiter(self) -> ConfiguredTaskAwaitable.ConfiguredTaskAwaiter:
        """

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

    class ConfiguredTaskAwaiter(ValueType, ICriticalNotifyCompletion, INotifyCompletion):
        """"""

        @property
        def IsCompleted(self) -> bool:
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
        def GetResult(self) -> None:
            """"""
        def GetType(self) -> Type:
            """

            :return:
            """
        def OnCompleted(self, continuation: Action) -> None:
            """

            :param continuation:
            """
        def ToString(self) -> str:
            """

            :return:
            """
        def UnsafeOnCompleted(self, continuation: Action) -> None:
            """

            :param continuation:
            """

class ConfiguredTaskAwaitable(Generic[TResult], ValueType):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAwaiter(self) -> ConfiguredTaskAwaitable.ConfiguredTaskAwaiter[TResult]:
        """

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

    class ConfiguredTaskAwaiter(
        Generic[TResult], ValueType, ICriticalNotifyCompletion, INotifyCompletion
    ):
        """"""

        @property
        def IsCompleted(self) -> bool:
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
        def GetResult(self) -> TResult:
            """"""
        def GetType(self) -> Type:
            """

            :return:
            """
        def OnCompleted(self, continuation: Action) -> None:
            """

            :param continuation:
            """
        def ToString(self) -> str:
            """

            :return:
            """
        def UnsafeOnCompleted(self, continuation: Action) -> None:
            """

            :param continuation:
            """

class ContractHelper(ABC, Object):
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
    def RaiseContractFailedEvent(
        cls,
        failureKind: ContractFailureKind,
        userMessage: str,
        conditionText: str,
        innerException: Exception,
    ) -> str:
        """

        :param failureKind:
        :param userMessage:
        :param conditionText:
        :param innerException:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def TriggerFailure(
        cls,
        kind: ContractFailureKind,
        displayMessage: str,
        userMessage: str,
        conditionText: str,
        innerException: Exception,
    ) -> None:
        """

        :param kind:
        :param displayMessage:
        :param userMessage:
        :param conditionText:
        :param innerException:
        """

class CustomConstantAttribute(ABC, Attribute, _Attribute):
    """"""

    @property
    def TypeId(self) -> object:
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

class DateTimeConstantAttribute(CustomConstantAttribute, _Attribute):
    """"""

    def __init__(self, ticks: int):
        """

        :param ticks:
        """
    @property
    def TypeId(self) -> object:
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

class DebugInfoGenerator(ABC, Object):
    """"""

    @classmethod
    def CreatePdbGenerator(cls) -> DebugInfoGenerator:
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
    def MarkSequencePoint(
        self, method: LambdaExpression, ilOffset: int, sequencePoint: DebugInfoExpression
    ) -> None:
        """

        :param method:
        :param ilOffset:
        :param sequencePoint:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DecimalConstantAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, scale: int, sign: int, hi: int, mid: int, low: int):
        """

        :param scale:
        :param sign:
        :param hi:
        :param mid:
        :param low:
        """
    @overload
    def __init__(self, scale: int, sign: int, hi: int, mid: int, low: int):
        """

        :param scale:
        :param sign:
        :param hi:
        :param mid:
        :param low:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Value(self) -> Decimal:
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

class DecoratedNameAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, decoratedName: str):
        """

        :param decoratedName:
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

class DefaultDependencyAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, loadHintArgument: LoadHint):
        """

        :param loadHintArgument:
        """
    @property
    def LoadHint(self) -> LoadHint:
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

class DependencyAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, dependentAssemblyArgument: str, loadHintArgument: LoadHint):
        """

        :param dependentAssemblyArgument:
        :param loadHintArgument:
        """
    @property
    def DependentAssembly(self) -> str:
        """

        :return:
        """
    @property
    def LoadHint(self) -> LoadHint:
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

class DependentHandle(ValueType):
    """"""

    def __init__(self, primary: object, secondary: object):
        """

        :param primary:
        :param secondary:
        """
    @property
    def IsAllocated(self) -> bool:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Free(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetPrimary(self) -> object:
        """

        :return:
        """
    def GetPrimaryAndSecondary(
        self, primary: object, secondary: object
    ) -> Tuple[None, object, object]:
        """

        :param primary:
        :param secondary:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DisablePrivateReflectionAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
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

class DiscardableAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
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

class DynamicAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, transformFlags: Array[bool]):
        """

        :param transformFlags:
        """
    @property
    def TransformFlags(self) -> IList[bool]:
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

class ExecutionScope(Object):
    """"""

    Globals: Final[Array[object]] = ...
    """
    
    :return: 
    """
    Locals: Final[Array[object]] = ...
    """
    
    :return: 
    """
    Parent: Final[ExecutionScope] = ...
    """
    
    :return: 
    """
    def CreateDelegate(self, indexLambda: int, locals: Array[object]) -> Delegate:
        """

        :param indexLambda:
        :param locals:
        :return:
        """
    def CreateHoistedLocals(self) -> Array[object]:
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
    def IsolateExpression(self, expression: Expression, locals: Array[object]) -> Expression:
        """

        :param expression:
        :param locals:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ExtensionAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
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

class FixedAddressValueTypeAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
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

class FixedBufferAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, elementType: Type, length: int):
        """

        :param elementType:
        :param length:
        """
    @property
    def ElementType(self) -> Type:
        """

        :return:
        """
    @property
    def Length(self) -> int:
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

class FormattableStringFactory(ABC, Object):
    """"""

    @classmethod
    def Create(cls, format: str, arguments: Array[object]) -> FormattableString:
        """

        :param format:
        :param arguments:
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

class FriendAccessAllowedAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
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

class HasCopySemanticsAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
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

class IAsyncStateMachine:
    """"""

    def MoveNext(self) -> None:
        """"""
    def SetStateMachine(self, stateMachine: IAsyncStateMachine) -> None:
        """

        :param stateMachine:
        """

class ICriticalNotifyCompletion(INotifyCompletion):
    """"""

    def OnCompleted(self, continuation: Action) -> None:
        """

        :param continuation:
        """
    def UnsafeOnCompleted(self, continuation: Action) -> None:
        """

        :param continuation:
        """

class IDispatchConstantAttribute(CustomConstantAttribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
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

class INotifyCompletion:
    """"""

    def OnCompleted(self, continuation: Action) -> None:
        """

        :param continuation:
        """

class IRuntimeVariables:
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class IStrongBox:
    """"""

    @property
    def Value(self) -> object:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: object) -> None: ...

class ITuple:
    """"""

    @property
    def Item(self) -> object:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """

class IUnknownConstantAttribute(CustomConstantAttribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
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

class IndexerNameAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, indexerName: str):
        """

        :param indexerName:
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

class InternalsVisibleToAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, assemblyName: str):
        """

        :param assemblyName:
        """
    @property
    def AllInternalsVisible(self) -> bool:
        """

        :return:
        """
    @AllInternalsVisible.setter
    def AllInternalsVisible(self, value: bool) -> None: ...
    @property
    def AssemblyName(self) -> str:
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

class IsBoxed(ABC, Object):
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

class IsByRefLikeAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
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

class IsByValue(ABC, Object):
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

class IsConst(ABC, Object):
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

class IsCopyConstructed(ABC, Object):
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

class IsExplicitlyDereferenced(ABC, Object):
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

class IsImplicitlyDereferenced(ABC, Object):
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

class IsJitIntrinsic(ABC, Object):
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

class IsLong(ABC, Object):
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

class IsPinned(ABC, Object):
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

class IsReadOnlyAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
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

class IsSignUnspecifiedByte(ABC, Object):
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

class IsUdtReturn(ABC, Object):
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

class IsVolatile(ABC, Object):
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

class IteratorStateMachineAttribute(StateMachineAttribute, _Attribute):
    """"""

    def __init__(self, stateMachineType: Type):
        """

        :param stateMachineType:
        """
    @property
    def StateMachineType(self) -> Type:
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

class JitHelpers(ABC, Object):
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

    MethodCodeType: Final[MethodCodeType] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, methodImplOptions: MethodImplOptions):
        """

        :param methodImplOptions:
        """
    @overload
    def __init__(self, value: int):
        """

        :param value:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Value(self) -> MethodImplOptions:
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

    def __init__(self):
        """"""
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

class ObjectHandleOnStack(ValueType):
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

class PinningHelper(Object):
    """"""

    m_data: Final[int] = ...
    """
    
    :return: 
    """
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

class ReadOnlyCollectionBuilder(
    Generic[T], Object, ICollection[T], IEnumerable[T], IList[T], ICollection, IEnumerable, IList
):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, collection: IEnumerable[T]):
        """

        :param collection:
        """
    @overload
    def __init__(self, capacity: int):
        """

        :param capacity:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> T:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: T) -> None: ...
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, item: T) -> None:
        """

        :param item:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    @overload
    def IndexOf(self, item: T) -> int:
        """

        :param item:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, item: T) -> None:
        """

        :param index:
        :param item:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    @overload
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    @overload
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    @overload
    def Reverse(self) -> None:
        """"""
    @overload
    def Reverse(self, index: int, count: int) -> None:
        """

        :param index:
        :param count:
        """
    def ToArray(self) -> Array[T]:
        """

        :return:
        """
    def ToReadOnlyCollection(self) -> ReadOnlyCollection[T]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def __contains__(self, value: T) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> T:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[T]:
        """

        :return:
        """
    @overload
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: T) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class ReferenceAssemblyAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
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

class RequiredAttributeAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, requiredContract: Type):
        """

        :param requiredContract:
        """
    @property
    def RequiredContract(self) -> Type:
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

class RuleCache(Generic[T], Object):
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

class RuntimeCompatibilityAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def WrapNonExceptionThrows(self) -> bool:
        """

        :return:
        """
    @WrapNonExceptionThrows.setter
    def WrapNonExceptionThrows(self, value: bool) -> None: ...
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

class RuntimeFeature(ABC, Object):
    """"""

    PortablePdb: Final[ClassVar[str]] = ...
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
    def IsSupported(cls, feature: str) -> bool:
        """

        :param feature:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class RuntimeHelpers(ABC, Object):
    """"""

    @classmethod
    @property
    def OffsetToStringData(cls) -> int:
        """

        :return:
        """
    @classmethod
    def EnsureSufficientExecutionStack(cls) -> None:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def Equals(cls, o1: object, o2: object) -> bool:
        """

        :param o1:
        :param o2:
        :return:
        """
    @classmethod
    def ExecuteCodeWithGuaranteedCleanup(
        cls, code: RuntimeHelpers.TryCode, backoutCode: RuntimeHelpers.CleanupCode, userData: object
    ) -> None:
        """

        :param code:
        :param backoutCode:
        :param userData:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    @overload
    def GetHashCode(cls, o: object) -> int:
        """

        :param o:
        :return:
        """
    @classmethod
    def GetObjectValue(cls, obj: object) -> object:
        """

        :param obj:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def InitializeArray(cls, array: Array, fldHandle: RuntimeFieldHandle) -> None:
        """

        :param array:
        :param fldHandle:
        """
    @classmethod
    def PrepareConstrainedRegions(cls) -> None:
        """"""
    @classmethod
    def PrepareConstrainedRegionsNoOP(cls) -> None:
        """"""
    @classmethod
    def PrepareContractedDelegate(cls, d: Delegate) -> None:
        """

        :param d:
        """
    @classmethod
    def PrepareDelegate(cls, d: Delegate) -> None:
        """

        :param d:
        """
    @classmethod
    @overload
    def PrepareMethod(cls, method: RuntimeMethodHandle) -> None:
        """

        :param method:
        """
    @classmethod
    @overload
    def PrepareMethod(
        cls, method: RuntimeMethodHandle, instantiation: Array[RuntimeTypeHandle]
    ) -> None:
        """

        :param method:
        :param instantiation:
        """
    @classmethod
    def ProbeForSufficientStack(cls) -> None:
        """"""
    @classmethod
    def RunClassConstructor(cls, type: RuntimeTypeHandle) -> None:
        """

        :param type:
        """
    @classmethod
    def RunModuleConstructor(cls, module: ModuleHandle) -> None:
        """

        :param module:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    CleanupCode: Callable[[object, bool], None] = ...
    """
    
    :param userData: 
    :param exceptionThrown: 
    """
    TryCode: Callable[[object], None] = ...
    """
    
    :param userData: 
    """

class RuntimeOps(ABC, Object):
    """"""

    @classmethod
    @overload
    def CreateRuntimeVariables(cls) -> IRuntimeVariables:
        """

        :return:
        """
    @classmethod
    @overload
    def CreateRuntimeVariables(cls, data: Array[object], indexes: Array[int]) -> IRuntimeVariables:
        """

        :param data:
        :param indexes:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def ExpandoCheckVersion(cls, expando: ExpandoObject, version: object) -> bool:
        """

        :param expando:
        :param version:
        :return:
        """
    @classmethod
    def ExpandoPromoteClass(
        cls, expando: ExpandoObject, oldClass: object, newClass: object
    ) -> None:
        """

        :param expando:
        :param oldClass:
        :param newClass:
        """
    @classmethod
    def ExpandoTryDeleteValue(
        cls, expando: ExpandoObject, indexClass: object, index: int, name: str, ignoreCase: bool
    ) -> bool:
        """

        :param expando:
        :param indexClass:
        :param index:
        :param name:
        :param ignoreCase:
        :return:
        """
    @classmethod
    def ExpandoTryGetValue(
        cls,
        expando: ExpandoObject,
        indexClass: object,
        index: int,
        name: str,
        ignoreCase: bool,
        value: object,
    ) -> Tuple[bool, object]:
        """

        :param expando:
        :param indexClass:
        :param index:
        :param name:
        :param ignoreCase:
        :param value:
        :return:
        """
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
        """

        :param expando:
        :param indexClass:
        :param index:
        :param value:
        :param name:
        :param ignoreCase:
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
    def MergeRuntimeVariables(
        cls, first: IRuntimeVariables, second: IRuntimeVariables, indexes: Array[int]
    ) -> IRuntimeVariables:
        """

        :param first:
        :param second:
        :param indexes:
        :return:
        """
    @classmethod
    def Quote(
        cls, expression: Expression, hoistedLocals: object, locals: Array[object]
    ) -> Expression:
        """

        :param expression:
        :param hoistedLocals:
        :param locals:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class RuntimeWrappedException(Exception, _Exception, ISerializable):
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
    @property
    def WrappedException(self) -> object:
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

class ScopelessEnumAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
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

class SpecialNameAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
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

class StackCrawlMarkHandle(ValueType):
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

class StateMachineAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, stateMachineType: Type):
        """

        :param stateMachineType:
        """
    @property
    def StateMachineType(self) -> Type:
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

class StringFreezingAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
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

class StringHandleOnStack(ValueType):
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

class StrongBox(Generic[T], Object, IStrongBox):
    """"""

    Value: Final[T] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: T):
        """

        :param value:
        """
    @property
    def Value(self) -> object:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: object) -> None: ...
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

class SuppressIldasmAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
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

class SuppressMergeCheckAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
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

class SymbolDocumentGenerator(DebugInfoGenerator):
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
    def MarkSequencePoint(
        self, method: LambdaExpression, ilOffset: int, sequencePoint: DebugInfoExpression
    ) -> None:
        """

        :param method:
        :param ilOffset:
        :param sequencePoint:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class TaskAwaiter(ValueType, ICriticalNotifyCompletion, INotifyCompletion):
    """"""

    @property
    def IsCompleted(self) -> bool:
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
    def GetResult(self) -> None:
        """"""
    def GetType(self) -> Type:
        """

        :return:
        """
    def OnCompleted(self, continuation: Action) -> None:
        """

        :param continuation:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def UnsafeOnCompleted(self, continuation: Action) -> None:
        """

        :param continuation:
        """

class TaskAwaiter(Generic[TResult], ValueType, ICriticalNotifyCompletion, INotifyCompletion):
    """"""

    @property
    def IsCompleted(self) -> bool:
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
    def GetResult(self) -> TResult:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def OnCompleted(self, continuation: Action) -> None:
        """

        :param continuation:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def UnsafeOnCompleted(self, continuation: Action) -> None:
        """

        :param continuation:
        """

class TrueReadOnlyCollection(
    Generic[T],
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
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> T:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Item(self) -> T:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: T) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, item: T) -> None:
        """

        :param item:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    @overload
    def IndexOf(self, item: T) -> int:
        """

        :param item:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, item: T) -> None:
        """

        :param index:
        :param item:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    @overload
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    @overload
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def __contains__(self, value: T) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> T:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> T:
        """

        :param index:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[T]:
        """

        :return:
        """
    @overload
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: T) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class TupleElementNamesAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, transformNames: Array[str]):
        """

        :param transformNames:
        """
    @property
    def TransformNames(self) -> IList[str]:
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

class TypeDependencyAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, typeName: str):
        """

        :param typeName:
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

class TypeForwardedFromAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, assemblyFullName: str):
        """

        :param assemblyFullName:
        """
    @property
    def AssemblyFullName(self) -> str:
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

class TypeForwardedToAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, destination: Type):
        """

        :param destination:
        """
    @property
    def Destination(self) -> Type:
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

class UnsafeValueTypeAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
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

class YieldAwaitable(ValueType):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAwaiter(self) -> YieldAwaitable.YieldAwaiter:
        """

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

    class YieldAwaiter(ValueType, ICriticalNotifyCompletion, INotifyCompletion):
        """"""

        @property
        def IsCompleted(self) -> bool:
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
        def GetResult(self) -> None:
            """"""
        def GetType(self) -> Type:
            """

            :return:
            """
        def OnCompleted(self, continuation: Action) -> None:
            """

            :param continuation:
            """
        def ToString(self) -> str:
            """

            :return:
            """
        def UnsafeOnCompleted(self, continuation: Action) -> None:
            """

            :param continuation:
            """
