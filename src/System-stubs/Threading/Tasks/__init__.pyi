from __future__ import annotations

from abc import ABC
from typing import Generic, List, Optional, Protocol, Tuple, TypeVar, Union, overload

from System import Action, AggregateException, Array, AsyncCallback, Boolean, Delegate, Enum, EventArgs, EventHandler, Exception, Func, Guid, IAsyncResult, IDisposable, Int32, Int64, Nullable, Object, OperationCanceledException, Predicate, String, TimeSpan, ValueType, Void
from System.Collections import ICollection, IEnumerable
from System.Collections.Concurrent import ConcurrentQueue, IProducerConsumerCollection, OrderablePartitioner, Partitioner
from System.Collections.Generic import IEnumerable, IEnumerator, IReadOnlyCollection
from System.Diagnostics.Tracing import EventKeywords, EventSource, EventTask
from System.Runtime.CompilerServices import ConfiguredTaskAwaitable, ICriticalNotifyCompletion, INotifyCompletion, TaskAwaiter, YieldAwaitable
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable
from System.Threading import CancellationToken, IThreadPoolWorkItem, StackCrawlMark, ThreadAbortException

# ---------- Types ---------- #

T = TypeVar('T')
TAntecedentResult = TypeVar('TAntecedentResult')
TArg1 = TypeVar('TArg1')
TArg2 = TypeVar('TArg2')
TArg3 = TypeVar('TArg3')
TLocal = TypeVar('TLocal')
TNewResult = TypeVar('TNewResult')
TResult = TypeVar('TResult')
TSource = TypeVar('TSource')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NullableType = Union[Optional, Nullable]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...



# ---------- Classes ---------- #

class AsyncCausalityTracer(ABC, ObjectType):
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


class AwaitTaskContinuation(TaskContinuation, IThreadPoolWorkItem):
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


class BeginEndAwaitableAdapter(ObjectType, ICriticalNotifyCompletion, INotifyCompletion):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Callback() -> AsyncCallback: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsCompleted(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def GetAwaiter(self) -> BeginEndAwaitableAdapter: ...
    
    def GetResult(self) -> IAsyncResult: ...
    
    def OnCompleted(self, continuation: Action) -> VoidType: ...
    
    def UnsafeOnCompleted(self, continuation: Action) -> VoidType: ...
    
    def get_IsCompleted(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CompletionActionInvoker(ObjectType, IThreadPoolWorkItem):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ExecuteWorkItem(self) -> VoidType: ...
    
    def MarkAborted(self, tae: ThreadAbortException) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConcurrentExclusiveSchedulerPair(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, taskScheduler: TaskScheduler): ...
    
    @overload
    def __init__(self, taskScheduler: TaskScheduler, maxConcurrencyLevel: IntType): ...
    
    @overload
    def __init__(self, taskScheduler: TaskScheduler, maxConcurrencyLevel: IntType, maxItemsPerTask: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Completion(self) -> Task: ...
    
    @property
    def ConcurrentScheduler(self) -> TaskScheduler: ...
    
    @property
    def ExclusiveScheduler(self) -> TaskScheduler: ...
    
    # ---------- Methods ---------- #
    
    def Complete(self) -> VoidType: ...
    
    def get_Completion(self) -> Task: ...
    
    def get_ConcurrentScheduler(self) -> TaskScheduler: ...
    
    def get_ExclusiveScheduler(self) -> TaskScheduler: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContinuationResultTaskFromResultTask(Generic[TAntecedentResult, TResult], Task[TResult], IThreadPoolWorkItem, IAsyncResult, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, antecedent: Task[TAntecedentResult], function: Delegate, state: ObjectType, creationOptions: TaskCreationOptions, internalOptions: InternalTaskOptions, stackMark: StackCrawlMark): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContinuationResultTaskFromTask(Generic[TResult], Task[TResult], IThreadPoolWorkItem, IAsyncResult, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, antecedent: Task, function: Delegate, state: ObjectType, creationOptions: TaskCreationOptions, internalOptions: InternalTaskOptions, stackMark: StackCrawlMark): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContinuationTaskFromResultTask(Generic[TAntecedentResult], Task, IThreadPoolWorkItem, IAsyncResult, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, antecedent: Task[TAntecedentResult], action: Delegate, state: ObjectType, creationOptions: TaskCreationOptions, internalOptions: InternalTaskOptions, stackMark: StackCrawlMark): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContinuationTaskFromTask(Task, IThreadPoolWorkItem, IAsyncResult, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, antecedent: Task, action: Delegate, state: ObjectType, creationOptions: TaskCreationOptions, internalOptions: InternalTaskOptions, stackMark: StackCrawlMark): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GenericDelegateCache(Protocol[TAntecedentResult, TResult], ObjectType):
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


class MultiProducerMultiConsumerQueue(Generic[T], ConcurrentQueue[T], IProducerConsumerCollection[T], IEnumerable[T], IEnumerable, ICollection, IReadOnlyCollection[T], IProducerConsumerQueue[T]):
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


class PaddingHelpers(ABC, ObjectType):
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


class Parallel(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def For(fromInclusive: IntType, toExclusive: IntType, body: Action[IntType]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def For(fromInclusive: LongType, toExclusive: LongType, body: Action[LongType]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def For(fromInclusive: IntType, toExclusive: IntType, parallelOptions: ParallelOptions, body: Action[IntType]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def For(fromInclusive: LongType, toExclusive: LongType, parallelOptions: ParallelOptions, body: Action[LongType]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def For(fromInclusive: IntType, toExclusive: IntType, body: Action[IntType, ParallelLoopState]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def For(fromInclusive: LongType, toExclusive: LongType, body: Action[LongType, ParallelLoopState]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def For(fromInclusive: IntType, toExclusive: IntType, parallelOptions: ParallelOptions, body: Action[IntType, ParallelLoopState]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def For(fromInclusive: LongType, toExclusive: LongType, parallelOptions: ParallelOptions, body: Action[LongType, ParallelLoopState]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def For(fromInclusive: IntType, toExclusive: IntType, localInit: Func[TLocal], body: Func[IntType, ParallelLoopState, TLocal, TLocal], localFinally: Action[TLocal]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def For(fromInclusive: LongType, toExclusive: LongType, localInit: Func[TLocal], body: Func[LongType, ParallelLoopState, TLocal, TLocal], localFinally: Action[TLocal]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def For(fromInclusive: IntType, toExclusive: IntType, parallelOptions: ParallelOptions, localInit: Func[TLocal], body: Func[IntType, ParallelLoopState, TLocal, TLocal], localFinally: Action[TLocal]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def For(fromInclusive: LongType, toExclusive: LongType, parallelOptions: ParallelOptions, localInit: Func[TLocal], body: Func[LongType, ParallelLoopState, TLocal, TLocal], localFinally: Action[TLocal]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def ForEach(source: IEnumerable[TSource], parallelOptions: ParallelOptions, body: Action[TSource]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def ForEach(source: IEnumerable[TSource], body: Action[TSource]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def ForEach(source: IEnumerable[TSource], body: Action[TSource, ParallelLoopState]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def ForEach(source: IEnumerable[TSource], parallelOptions: ParallelOptions, body: Action[TSource, ParallelLoopState]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def ForEach(source: IEnumerable[TSource], body: Action[TSource, ParallelLoopState, LongType]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def ForEach(source: IEnumerable[TSource], parallelOptions: ParallelOptions, body: Action[TSource, ParallelLoopState, LongType]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def ForEach(source: IEnumerable[TSource], localInit: Func[TLocal], body: Func[TSource, ParallelLoopState, TLocal, TLocal], localFinally: Action[TLocal]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def ForEach(source: IEnumerable[TSource], parallelOptions: ParallelOptions, localInit: Func[TLocal], body: Func[TSource, ParallelLoopState, TLocal, TLocal], localFinally: Action[TLocal]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def ForEach(source: IEnumerable[TSource], localInit: Func[TLocal], body: Func[TSource, ParallelLoopState, LongType, TLocal, TLocal], localFinally: Action[TLocal]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def ForEach(source: IEnumerable[TSource], parallelOptions: ParallelOptions, localInit: Func[TLocal], body: Func[TSource, ParallelLoopState, LongType, TLocal, TLocal], localFinally: Action[TLocal]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def ForEach(source: Partitioner[TSource], body: Action[TSource]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def ForEach(source: Partitioner[TSource], body: Action[TSource, ParallelLoopState]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def ForEach(source: OrderablePartitioner[TSource], body: Action[TSource, ParallelLoopState, LongType]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def ForEach(source: Partitioner[TSource], localInit: Func[TLocal], body: Func[TSource, ParallelLoopState, TLocal, TLocal], localFinally: Action[TLocal]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def ForEach(source: OrderablePartitioner[TSource], localInit: Func[TLocal], body: Func[TSource, ParallelLoopState, LongType, TLocal, TLocal], localFinally: Action[TLocal]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def ForEach(source: Partitioner[TSource], parallelOptions: ParallelOptions, body: Action[TSource]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def ForEach(source: Partitioner[TSource], parallelOptions: ParallelOptions, body: Action[TSource, ParallelLoopState]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def ForEach(source: OrderablePartitioner[TSource], parallelOptions: ParallelOptions, body: Action[TSource, ParallelLoopState, LongType]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def ForEach(source: Partitioner[TSource], parallelOptions: ParallelOptions, localInit: Func[TLocal], body: Func[TSource, ParallelLoopState, TLocal, TLocal], localFinally: Action[TLocal]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def ForEach(source: OrderablePartitioner[TSource], parallelOptions: ParallelOptions, localInit: Func[TLocal], body: Func[TSource, ParallelLoopState, LongType, TLocal, TLocal], localFinally: Action[TLocal]) -> ParallelLoopResult: ...
    
    @staticmethod
    @overload
    def Invoke(actions: ArrayType[Action]) -> VoidType: ...
    
    @staticmethod
    @overload
    def Invoke(parallelOptions: ParallelOptions, actions: ArrayType[Action]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ParallelForReplicaTask(Task, IThreadPoolWorkItem, IAsyncResult, IDisposable):
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


class ParallelForReplicatingTask(Task, IThreadPoolWorkItem, IAsyncResult, IDisposable):
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


class ParallelLoopState(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsExceptional(self) -> BooleanType: ...
    
    @property
    def IsStopped(self) -> BooleanType: ...
    
    @property
    def LowestBreakIteration(self) -> NullableType[Nullable[LongType]]: ...
    
    @property
    def ShouldExitCurrentIteration(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Break(self) -> VoidType: ...
    
    def Stop(self) -> VoidType: ...
    
    def get_IsExceptional(self) -> BooleanType: ...
    
    def get_IsStopped(self) -> BooleanType: ...
    
    def get_LowestBreakIteration(self) -> NullableType[Nullable[LongType]]: ...
    
    def get_ShouldExitCurrentIteration(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ParallelLoopState32(ParallelLoopState):
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


class ParallelLoopState64(ParallelLoopState):
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


class ParallelLoopStateFlags(ObjectType):
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


class ParallelLoopStateFlags32(ParallelLoopStateFlags):
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


class ParallelLoopStateFlags64(ParallelLoopStateFlags):
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


class ParallelOptions(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CancellationToken(self) -> CancellationToken: ...
    
    @CancellationToken.setter
    def CancellationToken(self, value: CancellationToken) -> None: ...
    
    @property
    def MaxDegreeOfParallelism(self) -> IntType: ...
    
    @MaxDegreeOfParallelism.setter
    def MaxDegreeOfParallelism(self, value: IntType) -> None: ...
    
    @property
    def TaskScheduler(self) -> TaskScheduler: ...
    
    @TaskScheduler.setter
    def TaskScheduler(self, value: TaskScheduler) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_CancellationToken(self) -> CancellationToken: ...
    
    def get_MaxDegreeOfParallelism(self) -> IntType: ...
    
    def get_TaskScheduler(self) -> TaskScheduler: ...
    
    def set_CancellationToken(self, value: CancellationToken) -> VoidType: ...
    
    def set_MaxDegreeOfParallelism(self, value: IntType) -> VoidType: ...
    
    def set_TaskScheduler(self, value: TaskScheduler) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RangeManager(ObjectType):
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


class Shared(Generic[T], ObjectType):
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


class SingleProducerSingleConsumerQueue(Generic[T], ObjectType, IProducerConsumerQueue[T], IEnumerable[T], IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsEmpty(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Clear(self) -> VoidType: ...
    
    def Enqueue(self, item: T) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[T]: ...
    
    def TryDequeue(self, result: T) -> Tuple[BooleanType, T]: ...
    
    def TryDequeueIf(self, predicate: Predicate[T], result: T) -> Tuple[BooleanType, T]: ...
    
    def TryPeek(self, result: T) -> Tuple[BooleanType, T]: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsEmpty(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StackGuard(ObjectType):
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


class StandardTaskContinuation(TaskContinuation):
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


class SynchronizationContextAwaitTaskContinuation(AwaitTaskContinuation, IThreadPoolWorkItem):
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


class SynchronizationContextTaskScheduler(TaskScheduler):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def MaximumConcurrencyLevel(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_MaximumConcurrencyLevel(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemThreadingTasks_FutureDebugView(Generic[TResult], ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, task: Task[TResult]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AsyncState(self) -> ObjectType: ...
    
    @property
    def CancellationPending(self) -> BooleanType: ...
    
    @property
    def CreationOptions(self) -> TaskCreationOptions: ...
    
    @property
    def Exception(self) -> Exception: ...
    
    @property
    def Id(self) -> IntType: ...
    
    @property
    def Result(self) -> TResult: ...
    
    @property
    def Status(self) -> TaskStatus: ...
    
    # ---------- Methods ---------- #
    
    def get_AsyncState(self) -> ObjectType: ...
    
    def get_CancellationPending(self) -> BooleanType: ...
    
    def get_CreationOptions(self) -> TaskCreationOptions: ...
    
    def get_Exception(self) -> Exception: ...
    
    def get_Id(self) -> IntType: ...
    
    def get_Result(self) -> TResult: ...
    
    def get_Status(self) -> TaskStatus: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemThreadingTasks_TaskDebugView(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, task: Task): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AsyncState(self) -> ObjectType: ...
    
    @property
    def CancellationPending(self) -> BooleanType: ...
    
    @property
    def CreationOptions(self) -> TaskCreationOptions: ...
    
    @property
    def Exception(self) -> Exception: ...
    
    @property
    def Id(self) -> IntType: ...
    
    @property
    def Status(self) -> TaskStatus: ...
    
    # ---------- Methods ---------- #
    
    def get_AsyncState(self) -> ObjectType: ...
    
    def get_CancellationPending(self) -> BooleanType: ...
    
    def get_CreationOptions(self) -> TaskCreationOptions: ...
    
    def get_Exception(self) -> Exception: ...
    
    def get_Id(self) -> IntType: ...
    
    def get_Status(self) -> TaskStatus: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Task(ObjectType, IThreadPoolWorkItem, IAsyncResult, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, action: Action): ...
    
    @overload
    def __init__(self, action: Action, cancellationToken: CancellationToken): ...
    
    @overload
    def __init__(self, action: Action, creationOptions: TaskCreationOptions): ...
    
    @overload
    def __init__(self, action: Action, cancellationToken: CancellationToken, creationOptions: TaskCreationOptions): ...
    
    @overload
    def __init__(self, action: Action[ObjectType], state: ObjectType): ...
    
    @overload
    def __init__(self, action: Action[ObjectType], state: ObjectType, cancellationToken: CancellationToken): ...
    
    @overload
    def __init__(self, action: Action[ObjectType], state: ObjectType, creationOptions: TaskCreationOptions): ...
    
    @overload
    def __init__(self, action: Action[ObjectType], state: ObjectType, cancellationToken: CancellationToken, creationOptions: TaskCreationOptions): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AsyncState(self) -> ObjectType: ...
    
    @staticmethod
    @property
    def CompletedTask() -> Task: ...
    
    @property
    def CreationOptions(self) -> TaskCreationOptions: ...
    
    @staticmethod
    @property
    def CurrentId() -> NullableType[Nullable[IntType]]: ...
    
    @property
    def Exception(self) -> AggregateException: ...
    
    @staticmethod
    @property
    def Factory() -> TaskFactory: ...
    
    @property
    def Id(self) -> IntType: ...
    
    @property
    def IsCanceled(self) -> BooleanType: ...
    
    @property
    def IsCompleted(self) -> BooleanType: ...
    
    @property
    def IsFaulted(self) -> BooleanType: ...
    
    @property
    def Status(self) -> TaskStatus: ...
    
    # ---------- Methods ---------- #
    
    def ConfigureAwait(self, continueOnCapturedContext: BooleanType) -> ConfiguredTaskAwaitable: ...
    
    @overload
    def ContinueWith(self, continuationAction: Action[Task]) -> Task: ...
    
    @overload
    def ContinueWith(self, continuationAction: Action[Task], cancellationToken: CancellationToken) -> Task: ...
    
    @overload
    def ContinueWith(self, continuationAction: Action[Task], scheduler: TaskScheduler) -> Task: ...
    
    @overload
    def ContinueWith(self, continuationAction: Action[Task], continuationOptions: TaskContinuationOptions) -> Task: ...
    
    @overload
    def ContinueWith(self, continuationAction: Action[Task], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task: ...
    
    @overload
    def ContinueWith(self, continuationAction: Action[Task, ObjectType], state: ObjectType) -> Task: ...
    
    @overload
    def ContinueWith(self, continuationAction: Action[Task, ObjectType], state: ObjectType, cancellationToken: CancellationToken) -> Task: ...
    
    @overload
    def ContinueWith(self, continuationAction: Action[Task, ObjectType], state: ObjectType, scheduler: TaskScheduler) -> Task: ...
    
    @overload
    def ContinueWith(self, continuationAction: Action[Task, ObjectType], state: ObjectType, continuationOptions: TaskContinuationOptions) -> Task: ...
    
    @overload
    def ContinueWith(self, continuationAction: Action[Task, ObjectType], state: ObjectType, cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task: ...
    
    @overload
    def ContinueWith(self, continuationFunction: Func[Task, TResult]) -> Task[TResult]: ...
    
    @overload
    def ContinueWith(self, continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken) -> Task[TResult]: ...
    
    @overload
    def ContinueWith(self, continuationFunction: Func[Task, TResult], scheduler: TaskScheduler) -> Task[TResult]: ...
    
    @overload
    def ContinueWith(self, continuationFunction: Func[Task, TResult], continuationOptions: TaskContinuationOptions) -> Task[TResult]: ...
    
    @overload
    def ContinueWith(self, continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task[TResult]: ...
    
    @overload
    def ContinueWith(self, continuationFunction: Func[Task, ObjectType, TResult], state: ObjectType) -> Task[TResult]: ...
    
    @overload
    def ContinueWith(self, continuationFunction: Func[Task, ObjectType, TResult], state: ObjectType, cancellationToken: CancellationToken) -> Task[TResult]: ...
    
    @overload
    def ContinueWith(self, continuationFunction: Func[Task, ObjectType, TResult], state: ObjectType, scheduler: TaskScheduler) -> Task[TResult]: ...
    
    @overload
    def ContinueWith(self, continuationFunction: Func[Task, ObjectType, TResult], state: ObjectType, continuationOptions: TaskContinuationOptions) -> Task[TResult]: ...
    
    @overload
    def ContinueWith(self, continuationFunction: Func[Task, ObjectType, TResult], state: ObjectType, cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task[TResult]: ...
    
    @staticmethod
    @overload
    def Delay(delay: TimeSpan) -> Task: ...
    
    @staticmethod
    @overload
    def Delay(delay: TimeSpan, cancellationToken: CancellationToken) -> Task: ...
    
    @staticmethod
    @overload
    def Delay(millisecondsDelay: IntType) -> Task: ...
    
    @staticmethod
    @overload
    def Delay(millisecondsDelay: IntType, cancellationToken: CancellationToken) -> Task: ...
    
    def Dispose(self) -> VoidType: ...
    
    @staticmethod
    @overload
    def FromCanceled(cancellationToken: CancellationToken) -> Task: ...
    
    @staticmethod
    @overload
    def FromCanceled(cancellationToken: CancellationToken) -> Task[TResult]: ...
    
    @staticmethod
    @overload
    def FromException(exception: Exception) -> Task: ...
    
    @staticmethod
    @overload
    def FromException(exception: Exception) -> Task[TResult]: ...
    
    @staticmethod
    def FromResult(result: TResult) -> Task[TResult]: ...
    
    def GetAwaiter(self) -> TaskAwaiter: ...
    
    @staticmethod
    @overload
    def Run(action: Action) -> Task: ...
    
    @staticmethod
    @overload
    def Run(action: Action, cancellationToken: CancellationToken) -> Task: ...
    
    @staticmethod
    @overload
    def Run(function: Func[Task]) -> Task: ...
    
    @staticmethod
    @overload
    def Run(function: Func[Task], cancellationToken: CancellationToken) -> Task: ...
    
    @staticmethod
    @overload
    def Run(function: Func[TResult]) -> Task[TResult]: ...
    
    @staticmethod
    @overload
    def Run(function: Func[TResult], cancellationToken: CancellationToken) -> Task[TResult]: ...
    
    @staticmethod
    @overload
    def Run(function: Func[Task[TResult]]) -> Task[TResult]: ...
    
    @staticmethod
    @overload
    def Run(function: Func[Task[TResult]], cancellationToken: CancellationToken) -> Task[TResult]: ...
    
    @overload
    def RunSynchronously(self) -> VoidType: ...
    
    @overload
    def RunSynchronously(self, scheduler: TaskScheduler) -> VoidType: ...
    
    @overload
    def Start(self) -> VoidType: ...
    
    @overload
    def Start(self, scheduler: TaskScheduler) -> VoidType: ...
    
    @overload
    def Wait(self) -> VoidType: ...
    
    @overload
    def Wait(self, timeout: TimeSpan) -> BooleanType: ...
    
    @overload
    def Wait(self, cancellationToken: CancellationToken) -> VoidType: ...
    
    @overload
    def Wait(self, millisecondsTimeout: IntType) -> BooleanType: ...
    
    @overload
    def Wait(self, millisecondsTimeout: IntType, cancellationToken: CancellationToken) -> BooleanType: ...
    
    @staticmethod
    @overload
    def WaitAll(tasks: ArrayType[Task]) -> VoidType: ...
    
    @staticmethod
    @overload
    def WaitAll(tasks: ArrayType[Task], timeout: TimeSpan) -> BooleanType: ...
    
    @staticmethod
    @overload
    def WaitAll(tasks: ArrayType[Task], millisecondsTimeout: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def WaitAll(tasks: ArrayType[Task], cancellationToken: CancellationToken) -> VoidType: ...
    
    @staticmethod
    @overload
    def WaitAll(tasks: ArrayType[Task], millisecondsTimeout: IntType, cancellationToken: CancellationToken) -> BooleanType: ...
    
    @staticmethod
    @overload
    def WaitAny(tasks: ArrayType[Task]) -> IntType: ...
    
    @staticmethod
    @overload
    def WaitAny(tasks: ArrayType[Task], timeout: TimeSpan) -> IntType: ...
    
    @staticmethod
    @overload
    def WaitAny(tasks: ArrayType[Task], cancellationToken: CancellationToken) -> IntType: ...
    
    @staticmethod
    @overload
    def WaitAny(tasks: ArrayType[Task], millisecondsTimeout: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def WaitAny(tasks: ArrayType[Task], millisecondsTimeout: IntType, cancellationToken: CancellationToken) -> IntType: ...
    
    @staticmethod
    @overload
    def WhenAll(tasks: IEnumerable[Task]) -> Task: ...
    
    @staticmethod
    @overload
    def WhenAll(tasks: ArrayType[Task]) -> Task: ...
    
    @staticmethod
    @overload
    def WhenAll(tasks: IEnumerable[Task[TResult]]) -> Task[ArrayType[TResult]]: ...
    
    @staticmethod
    @overload
    def WhenAll(tasks: ArrayType[Task[TResult]]) -> Task[ArrayType[TResult]]: ...
    
    @staticmethod
    @overload
    def WhenAny(tasks: ArrayType[Task]) -> Task[Task]: ...
    
    @staticmethod
    @overload
    def WhenAny(tasks: IEnumerable[Task]) -> Task[Task]: ...
    
    @staticmethod
    @overload
    def WhenAny(tasks: ArrayType[Task[TResult]]) -> Task[Task[TResult]]: ...
    
    @staticmethod
    @overload
    def WhenAny(tasks: IEnumerable[Task[TResult]]) -> Task[Task[TResult]]: ...
    
    @staticmethod
    def Yield() -> YieldAwaitable: ...
    
    def get_AsyncState(self) -> ObjectType: ...
    
    @staticmethod
    def get_CompletedTask() -> Task: ...
    
    def get_CreationOptions(self) -> TaskCreationOptions: ...
    
    @staticmethod
    def get_CurrentId() -> NullableType[Nullable[IntType]]: ...
    
    def get_Exception(self) -> AggregateException: ...
    
    @staticmethod
    def get_Factory() -> TaskFactory: ...
    
    def get_Id(self) -> IntType: ...
    
    def get_IsCanceled(self) -> BooleanType: ...
    
    def get_IsCompleted(self) -> BooleanType: ...
    
    def get_IsFaulted(self) -> BooleanType: ...
    
    def get_Status(self) -> TaskStatus: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Task(Generic[TResult], Task, IThreadPoolWorkItem, IAsyncResult, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, function: Func[TResult]): ...
    
    @overload
    def __init__(self, function: Func[TResult], cancellationToken: CancellationToken): ...
    
    @overload
    def __init__(self, function: Func[TResult], creationOptions: TaskCreationOptions): ...
    
    @overload
    def __init__(self, function: Func[TResult], cancellationToken: CancellationToken, creationOptions: TaskCreationOptions): ...
    
    @overload
    def __init__(self, function: Func[ObjectType, TResult], state: ObjectType): ...
    
    @overload
    def __init__(self, function: Func[ObjectType, TResult], state: ObjectType, cancellationToken: CancellationToken): ...
    
    @overload
    def __init__(self, function: Func[ObjectType, TResult], state: ObjectType, creationOptions: TaskCreationOptions): ...
    
    @overload
    def __init__(self, function: Func[ObjectType, TResult], state: ObjectType, cancellationToken: CancellationToken, creationOptions: TaskCreationOptions): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Factory() -> TaskFactory[TResult]: ...
    
    @property
    def Result(self) -> TResult: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def ConfigureAwait(self, continueOnCapturedContext: BooleanType) -> ConfiguredTaskAwaitable[TResult]: ...
    
    @overload
    def ContinueWith(self, continuationAction: Action[Task[TResult]], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task: ...
    
    @overload
    def ContinueWith(self, continuationFunction: Func[Task[TResult], TNewResult], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task[TNewResult]: ...
    
    @overload
    def ContinueWith(self, continuationAction: Action[Task[TResult]]) -> Task: ...
    
    @overload
    def ContinueWith(self, continuationAction: Action[Task[TResult]], cancellationToken: CancellationToken) -> Task: ...
    
    @overload
    def ContinueWith(self, continuationAction: Action[Task[TResult]], scheduler: TaskScheduler) -> Task: ...
    
    @overload
    def ContinueWith(self, continuationAction: Action[Task[TResult]], continuationOptions: TaskContinuationOptions) -> Task: ...
    
    @overload
    def ContinueWith(self, continuationAction: Action[Task[TResult], ObjectType], state: ObjectType) -> Task: ...
    
    @overload
    def ContinueWith(self, continuationAction: Action[Task[TResult], ObjectType], state: ObjectType, cancellationToken: CancellationToken) -> Task: ...
    
    @overload
    def ContinueWith(self, continuationAction: Action[Task[TResult], ObjectType], state: ObjectType, scheduler: TaskScheduler) -> Task: ...
    
    @overload
    def ContinueWith(self, continuationAction: Action[Task[TResult], ObjectType], state: ObjectType, continuationOptions: TaskContinuationOptions) -> Task: ...
    
    @overload
    def ContinueWith(self, continuationAction: Action[Task[TResult], ObjectType], state: ObjectType, cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task: ...
    
    @overload
    def ContinueWith(self, continuationFunction: Func[Task[TResult], TNewResult]) -> Task[TNewResult]: ...
    
    @overload
    def ContinueWith(self, continuationFunction: Func[Task[TResult], TNewResult], cancellationToken: CancellationToken) -> Task[TNewResult]: ...
    
    @overload
    def ContinueWith(self, continuationFunction: Func[Task[TResult], TNewResult], scheduler: TaskScheduler) -> Task[TNewResult]: ...
    
    @overload
    def ContinueWith(self, continuationFunction: Func[Task[TResult], TNewResult], continuationOptions: TaskContinuationOptions) -> Task[TNewResult]: ...
    
    @overload
    def ContinueWith(self, continuationFunction: Func[Task[TResult], ObjectType, TNewResult], state: ObjectType) -> Task[TNewResult]: ...
    
    @overload
    def ContinueWith(self, continuationFunction: Func[Task[TResult], ObjectType, TNewResult], state: ObjectType, cancellationToken: CancellationToken) -> Task[TNewResult]: ...
    
    @overload
    def ContinueWith(self, continuationFunction: Func[Task[TResult], ObjectType, TNewResult], state: ObjectType, scheduler: TaskScheduler) -> Task[TNewResult]: ...
    
    @overload
    def ContinueWith(self, continuationFunction: Func[Task[TResult], ObjectType, TNewResult], state: ObjectType, continuationOptions: TaskContinuationOptions) -> Task[TNewResult]: ...
    
    @overload
    def ContinueWith(self, continuationFunction: Func[Task[TResult], ObjectType, TNewResult], state: ObjectType, cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task[TNewResult]: ...
    
    @overload
    def GetAwaiter(self) -> TaskAwaiter[TResult]: ...
    
    @staticmethod
    def get_Factory() -> TaskFactory[TResult]: ...
    
    def get_Result(self) -> TResult: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TaskCanceledException(OperationCanceledException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, task: Task): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Task(self) -> Task: ...
    
    # ---------- Methods ---------- #
    
    def get_Task(self) -> Task: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TaskCompletionSource(Generic[TResult], ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, creationOptions: TaskCreationOptions): ...
    
    @overload
    def __init__(self, state: ObjectType): ...
    
    @overload
    def __init__(self, state: ObjectType, creationOptions: TaskCreationOptions): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Task(self) -> Task[TResult]: ...
    
    # ---------- Methods ---------- #
    
    def SetCanceled(self) -> VoidType: ...
    
    @overload
    def SetException(self, exception: Exception) -> VoidType: ...
    
    @overload
    def SetException(self, exceptions: IEnumerable[Exception]) -> VoidType: ...
    
    def SetResult(self, result: TResult) -> VoidType: ...
    
    @overload
    def TrySetCanceled(self) -> BooleanType: ...
    
    @overload
    def TrySetCanceled(self, cancellationToken: CancellationToken) -> BooleanType: ...
    
    @overload
    def TrySetException(self, exception: Exception) -> BooleanType: ...
    
    @overload
    def TrySetException(self, exceptions: IEnumerable[Exception]) -> BooleanType: ...
    
    def TrySetResult(self, result: TResult) -> BooleanType: ...
    
    def get_Task(self) -> Task[TResult]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TaskContinuation(ABC, ObjectType):
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


class TaskExceptionHolder(ObjectType):
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


class TaskExtensions(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Unwrap(task: Task[Task]) -> Task: ...
    
    @staticmethod
    @overload
    def Unwrap(task: Task[Task[TResult]]) -> Task[TResult]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TaskFactory(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, cancellationToken: CancellationToken): ...
    
    @overload
    def __init__(self, scheduler: TaskScheduler): ...
    
    @overload
    def __init__(self, creationOptions: TaskCreationOptions, continuationOptions: TaskContinuationOptions): ...
    
    @overload
    def __init__(self, cancellationToken: CancellationToken, creationOptions: TaskCreationOptions, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CancellationToken(self) -> CancellationToken: ...
    
    @property
    def ContinuationOptions(self) -> TaskContinuationOptions: ...
    
    @property
    def CreationOptions(self) -> TaskCreationOptions: ...
    
    @property
    def Scheduler(self) -> TaskScheduler: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def ContinueWhenAll(self, tasks: ArrayType[Task], continuationAction: Action[ArrayType[Task]]) -> Task: ...
    
    @overload
    def ContinueWhenAll(self, tasks: ArrayType[Task], continuationAction: Action[ArrayType[Task]], cancellationToken: CancellationToken) -> Task: ...
    
    @overload
    def ContinueWhenAll(self, tasks: ArrayType[Task], continuationAction: Action[ArrayType[Task]], continuationOptions: TaskContinuationOptions) -> Task: ...
    
    @overload
    def ContinueWhenAll(self, tasks: ArrayType[Task], continuationAction: Action[ArrayType[Task]], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task: ...
    
    @overload
    def ContinueWhenAll(self, tasks: ArrayType[Task[TAntecedentResult]], continuationAction: Action[ArrayType[Task[TAntecedentResult]]]) -> Task: ...
    
    @overload
    def ContinueWhenAll(self, tasks: ArrayType[Task[TAntecedentResult]], continuationAction: Action[ArrayType[Task[TAntecedentResult]]], cancellationToken: CancellationToken) -> Task: ...
    
    @overload
    def ContinueWhenAll(self, tasks: ArrayType[Task[TAntecedentResult]], continuationAction: Action[ArrayType[Task[TAntecedentResult]]], continuationOptions: TaskContinuationOptions) -> Task: ...
    
    @overload
    def ContinueWhenAll(self, tasks: ArrayType[Task[TAntecedentResult]], continuationAction: Action[ArrayType[Task[TAntecedentResult]]], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task: ...
    
    @overload
    def ContinueWhenAll(self, tasks: ArrayType[Task], continuationFunction: Func[ArrayType[Task], TResult]) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAll(self, tasks: ArrayType[Task], continuationFunction: Func[ArrayType[Task], TResult], cancellationToken: CancellationToken) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAll(self, tasks: ArrayType[Task], continuationFunction: Func[ArrayType[Task], TResult], continuationOptions: TaskContinuationOptions) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAll(self, tasks: ArrayType[Task], continuationFunction: Func[ArrayType[Task], TResult], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAll(self, tasks: ArrayType[Task[TAntecedentResult]], continuationFunction: Func[ArrayType[Task[TAntecedentResult]], TResult]) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAll(self, tasks: ArrayType[Task[TAntecedentResult]], continuationFunction: Func[ArrayType[Task[TAntecedentResult]], TResult], cancellationToken: CancellationToken) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAll(self, tasks: ArrayType[Task[TAntecedentResult]], continuationFunction: Func[ArrayType[Task[TAntecedentResult]], TResult], continuationOptions: TaskContinuationOptions) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAll(self, tasks: ArrayType[Task[TAntecedentResult]], continuationFunction: Func[ArrayType[Task[TAntecedentResult]], TResult], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAny(self, tasks: ArrayType[Task], continuationAction: Action[Task]) -> Task: ...
    
    @overload
    def ContinueWhenAny(self, tasks: ArrayType[Task], continuationAction: Action[Task], cancellationToken: CancellationToken) -> Task: ...
    
    @overload
    def ContinueWhenAny(self, tasks: ArrayType[Task], continuationAction: Action[Task], continuationOptions: TaskContinuationOptions) -> Task: ...
    
    @overload
    def ContinueWhenAny(self, tasks: ArrayType[Task], continuationAction: Action[Task], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task: ...
    
    @overload
    def ContinueWhenAny(self, tasks: ArrayType[Task], continuationFunction: Func[Task, TResult]) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAny(self, tasks: ArrayType[Task], continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAny(self, tasks: ArrayType[Task], continuationFunction: Func[Task, TResult], continuationOptions: TaskContinuationOptions) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAny(self, tasks: ArrayType[Task], continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAny(self, tasks: ArrayType[Task[TAntecedentResult]], continuationFunction: Func[Task[TAntecedentResult], TResult]) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAny(self, tasks: ArrayType[Task[TAntecedentResult]], continuationFunction: Func[Task[TAntecedentResult], TResult], cancellationToken: CancellationToken) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAny(self, tasks: ArrayType[Task[TAntecedentResult]], continuationFunction: Func[Task[TAntecedentResult], TResult], continuationOptions: TaskContinuationOptions) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAny(self, tasks: ArrayType[Task[TAntecedentResult]], continuationFunction: Func[Task[TAntecedentResult], TResult], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAny(self, tasks: ArrayType[Task[TAntecedentResult]], continuationAction: Action[Task[TAntecedentResult]]) -> Task: ...
    
    @overload
    def ContinueWhenAny(self, tasks: ArrayType[Task[TAntecedentResult]], continuationAction: Action[Task[TAntecedentResult]], cancellationToken: CancellationToken) -> Task: ...
    
    @overload
    def ContinueWhenAny(self, tasks: ArrayType[Task[TAntecedentResult]], continuationAction: Action[Task[TAntecedentResult]], continuationOptions: TaskContinuationOptions) -> Task: ...
    
    @overload
    def ContinueWhenAny(self, tasks: ArrayType[Task[TAntecedentResult]], continuationAction: Action[Task[TAntecedentResult]], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task: ...
    
    @overload
    def FromAsync(self, asyncResult: IAsyncResult, endMethod: Action[IAsyncResult]) -> Task: ...
    
    @overload
    def FromAsync(self, asyncResult: IAsyncResult, endMethod: Action[IAsyncResult], creationOptions: TaskCreationOptions) -> Task: ...
    
    @overload
    def FromAsync(self, asyncResult: IAsyncResult, endMethod: Action[IAsyncResult], creationOptions: TaskCreationOptions, scheduler: TaskScheduler) -> Task: ...
    
    @overload
    def FromAsync(self, beginMethod: Func[AsyncCallback, ObjectType, IAsyncResult], endMethod: Action[IAsyncResult], state: ObjectType) -> Task: ...
    
    @overload
    def FromAsync(self, beginMethod: Func[AsyncCallback, ObjectType, IAsyncResult], endMethod: Action[IAsyncResult], state: ObjectType, creationOptions: TaskCreationOptions) -> Task: ...
    
    @overload
    def FromAsync(self, beginMethod: Func[TArg1, AsyncCallback, ObjectType, IAsyncResult], endMethod: Action[IAsyncResult], arg1: TArg1, state: ObjectType) -> Task: ...
    
    @overload
    def FromAsync(self, beginMethod: Func[TArg1, AsyncCallback, ObjectType, IAsyncResult], endMethod: Action[IAsyncResult], arg1: TArg1, state: ObjectType, creationOptions: TaskCreationOptions) -> Task: ...
    
    @overload
    def FromAsync(self, beginMethod: Func[TArg1, TArg2, AsyncCallback, ObjectType, IAsyncResult], endMethod: Action[IAsyncResult], arg1: TArg1, arg2: TArg2, state: ObjectType) -> Task: ...
    
    @overload
    def FromAsync(self, beginMethod: Func[TArg1, TArg2, AsyncCallback, ObjectType, IAsyncResult], endMethod: Action[IAsyncResult], arg1: TArg1, arg2: TArg2, state: ObjectType, creationOptions: TaskCreationOptions) -> Task: ...
    
    @overload
    def FromAsync(self, beginMethod: Func[TArg1, TArg2, TArg3, AsyncCallback, ObjectType, IAsyncResult], endMethod: Action[IAsyncResult], arg1: TArg1, arg2: TArg2, arg3: TArg3, state: ObjectType) -> Task: ...
    
    @overload
    def FromAsync(self, beginMethod: Func[TArg1, TArg2, TArg3, AsyncCallback, ObjectType, IAsyncResult], endMethod: Action[IAsyncResult], arg1: TArg1, arg2: TArg2, arg3: TArg3, state: ObjectType, creationOptions: TaskCreationOptions) -> Task: ...
    
    @overload
    def FromAsync(self, asyncResult: IAsyncResult, endMethod: Func[IAsyncResult, TResult]) -> Task[TResult]: ...
    
    @overload
    def FromAsync(self, asyncResult: IAsyncResult, endMethod: Func[IAsyncResult, TResult], creationOptions: TaskCreationOptions) -> Task[TResult]: ...
    
    @overload
    def FromAsync(self, asyncResult: IAsyncResult, endMethod: Func[IAsyncResult, TResult], creationOptions: TaskCreationOptions, scheduler: TaskScheduler) -> Task[TResult]: ...
    
    @overload
    def FromAsync(self, beginMethod: Func[AsyncCallback, ObjectType, IAsyncResult], endMethod: Func[IAsyncResult, TResult], state: ObjectType) -> Task[TResult]: ...
    
    @overload
    def FromAsync(self, beginMethod: Func[AsyncCallback, ObjectType, IAsyncResult], endMethod: Func[IAsyncResult, TResult], state: ObjectType, creationOptions: TaskCreationOptions) -> Task[TResult]: ...
    
    @overload
    def FromAsync(self, beginMethod: Func[TArg1, AsyncCallback, ObjectType, IAsyncResult], endMethod: Func[IAsyncResult, TResult], arg1: TArg1, state: ObjectType) -> Task[TResult]: ...
    
    @overload
    def FromAsync(self, beginMethod: Func[TArg1, AsyncCallback, ObjectType, IAsyncResult], endMethod: Func[IAsyncResult, TResult], arg1: TArg1, state: ObjectType, creationOptions: TaskCreationOptions) -> Task[TResult]: ...
    
    @overload
    def FromAsync(self, beginMethod: Func[TArg1, TArg2, AsyncCallback, ObjectType, IAsyncResult], endMethod: Func[IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, state: ObjectType) -> Task[TResult]: ...
    
    @overload
    def FromAsync(self, beginMethod: Func[TArg1, TArg2, AsyncCallback, ObjectType, IAsyncResult], endMethod: Func[IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, state: ObjectType, creationOptions: TaskCreationOptions) -> Task[TResult]: ...
    
    @overload
    def FromAsync(self, beginMethod: Func[TArg1, TArg2, TArg3, AsyncCallback, ObjectType, IAsyncResult], endMethod: Func[IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, arg3: TArg3, state: ObjectType) -> Task[TResult]: ...
    
    @overload
    def FromAsync(self, beginMethod: Func[TArg1, TArg2, TArg3, AsyncCallback, ObjectType, IAsyncResult], endMethod: Func[IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, arg3: TArg3, state: ObjectType, creationOptions: TaskCreationOptions) -> Task[TResult]: ...
    
    @overload
    def StartNew(self, action: Action[ObjectType], state: ObjectType) -> Task: ...
    
    @overload
    def StartNew(self, action: Action) -> Task: ...
    
    @overload
    def StartNew(self, action: Action, cancellationToken: CancellationToken) -> Task: ...
    
    @overload
    def StartNew(self, action: Action, creationOptions: TaskCreationOptions) -> Task: ...
    
    @overload
    def StartNew(self, action: Action, cancellationToken: CancellationToken, creationOptions: TaskCreationOptions, scheduler: TaskScheduler) -> Task: ...
    
    @overload
    def StartNew(self, action: Action[ObjectType], state: ObjectType, cancellationToken: CancellationToken) -> Task: ...
    
    @overload
    def StartNew(self, action: Action[ObjectType], state: ObjectType, creationOptions: TaskCreationOptions) -> Task: ...
    
    @overload
    def StartNew(self, action: Action[ObjectType], state: ObjectType, cancellationToken: CancellationToken, creationOptions: TaskCreationOptions, scheduler: TaskScheduler) -> Task: ...
    
    @overload
    def StartNew(self, function: Func[TResult]) -> Task[TResult]: ...
    
    @overload
    def StartNew(self, function: Func[TResult], cancellationToken: CancellationToken) -> Task[TResult]: ...
    
    @overload
    def StartNew(self, function: Func[TResult], creationOptions: TaskCreationOptions) -> Task[TResult]: ...
    
    @overload
    def StartNew(self, function: Func[TResult], cancellationToken: CancellationToken, creationOptions: TaskCreationOptions, scheduler: TaskScheduler) -> Task[TResult]: ...
    
    @overload
    def StartNew(self, function: Func[ObjectType, TResult], state: ObjectType) -> Task[TResult]: ...
    
    @overload
    def StartNew(self, function: Func[ObjectType, TResult], state: ObjectType, cancellationToken: CancellationToken) -> Task[TResult]: ...
    
    @overload
    def StartNew(self, function: Func[ObjectType, TResult], state: ObjectType, creationOptions: TaskCreationOptions) -> Task[TResult]: ...
    
    @overload
    def StartNew(self, function: Func[ObjectType, TResult], state: ObjectType, cancellationToken: CancellationToken, creationOptions: TaskCreationOptions, scheduler: TaskScheduler) -> Task[TResult]: ...
    
    def get_CancellationToken(self) -> CancellationToken: ...
    
    def get_ContinuationOptions(self) -> TaskContinuationOptions: ...
    
    def get_CreationOptions(self) -> TaskCreationOptions: ...
    
    def get_Scheduler(self) -> TaskScheduler: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TaskFactory(Generic[TResult], ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, cancellationToken: CancellationToken): ...
    
    @overload
    def __init__(self, scheduler: TaskScheduler): ...
    
    @overload
    def __init__(self, creationOptions: TaskCreationOptions, continuationOptions: TaskContinuationOptions): ...
    
    @overload
    def __init__(self, cancellationToken: CancellationToken, creationOptions: TaskCreationOptions, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CancellationToken(self) -> CancellationToken: ...
    
    @property
    def ContinuationOptions(self) -> TaskContinuationOptions: ...
    
    @property
    def CreationOptions(self) -> TaskCreationOptions: ...
    
    @property
    def Scheduler(self) -> TaskScheduler: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def ContinueWhenAll(self, tasks: ArrayType[Task], continuationFunction: Func[ArrayType[Task], TResult]) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAll(self, tasks: ArrayType[Task], continuationFunction: Func[ArrayType[Task], TResult], cancellationToken: CancellationToken) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAll(self, tasks: ArrayType[Task], continuationFunction: Func[ArrayType[Task], TResult], continuationOptions: TaskContinuationOptions) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAll(self, tasks: ArrayType[Task], continuationFunction: Func[ArrayType[Task], TResult], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAll(self, tasks: ArrayType[Task[TAntecedentResult]], continuationFunction: Func[ArrayType[Task[TAntecedentResult]], TResult]) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAll(self, tasks: ArrayType[Task[TAntecedentResult]], continuationFunction: Func[ArrayType[Task[TAntecedentResult]], TResult], cancellationToken: CancellationToken) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAll(self, tasks: ArrayType[Task[TAntecedentResult]], continuationFunction: Func[ArrayType[Task[TAntecedentResult]], TResult], continuationOptions: TaskContinuationOptions) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAll(self, tasks: ArrayType[Task[TAntecedentResult]], continuationFunction: Func[ArrayType[Task[TAntecedentResult]], TResult], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAny(self, tasks: ArrayType[Task], continuationFunction: Func[Task, TResult]) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAny(self, tasks: ArrayType[Task], continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAny(self, tasks: ArrayType[Task], continuationFunction: Func[Task, TResult], continuationOptions: TaskContinuationOptions) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAny(self, tasks: ArrayType[Task], continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAny(self, tasks: ArrayType[Task[TAntecedentResult]], continuationFunction: Func[Task[TAntecedentResult], TResult]) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAny(self, tasks: ArrayType[Task[TAntecedentResult]], continuationFunction: Func[Task[TAntecedentResult], TResult], cancellationToken: CancellationToken) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAny(self, tasks: ArrayType[Task[TAntecedentResult]], continuationFunction: Func[Task[TAntecedentResult], TResult], continuationOptions: TaskContinuationOptions) -> Task[TResult]: ...
    
    @overload
    def ContinueWhenAny(self, tasks: ArrayType[Task[TAntecedentResult]], continuationFunction: Func[Task[TAntecedentResult], TResult], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task[TResult]: ...
    
    @overload
    def FromAsync(self, asyncResult: IAsyncResult, endMethod: Func[IAsyncResult, TResult]) -> Task[TResult]: ...
    
    @overload
    def FromAsync(self, asyncResult: IAsyncResult, endMethod: Func[IAsyncResult, TResult], creationOptions: TaskCreationOptions) -> Task[TResult]: ...
    
    @overload
    def FromAsync(self, asyncResult: IAsyncResult, endMethod: Func[IAsyncResult, TResult], creationOptions: TaskCreationOptions, scheduler: TaskScheduler) -> Task[TResult]: ...
    
    @overload
    def FromAsync(self, beginMethod: Func[AsyncCallback, ObjectType, IAsyncResult], endMethod: Func[IAsyncResult, TResult], state: ObjectType) -> Task[TResult]: ...
    
    @overload
    def FromAsync(self, beginMethod: Func[AsyncCallback, ObjectType, IAsyncResult], endMethod: Func[IAsyncResult, TResult], state: ObjectType, creationOptions: TaskCreationOptions) -> Task[TResult]: ...
    
    @overload
    def FromAsync(self, beginMethod: Func[TArg1, AsyncCallback, ObjectType, IAsyncResult], endMethod: Func[IAsyncResult, TResult], arg1: TArg1, state: ObjectType) -> Task[TResult]: ...
    
    @overload
    def FromAsync(self, beginMethod: Func[TArg1, AsyncCallback, ObjectType, IAsyncResult], endMethod: Func[IAsyncResult, TResult], arg1: TArg1, state: ObjectType, creationOptions: TaskCreationOptions) -> Task[TResult]: ...
    
    @overload
    def FromAsync(self, beginMethod: Func[TArg1, TArg2, AsyncCallback, ObjectType, IAsyncResult], endMethod: Func[IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, state: ObjectType) -> Task[TResult]: ...
    
    @overload
    def FromAsync(self, beginMethod: Func[TArg1, TArg2, AsyncCallback, ObjectType, IAsyncResult], endMethod: Func[IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, state: ObjectType, creationOptions: TaskCreationOptions) -> Task[TResult]: ...
    
    @overload
    def FromAsync(self, beginMethod: Func[TArg1, TArg2, TArg3, AsyncCallback, ObjectType, IAsyncResult], endMethod: Func[IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, arg3: TArg3, state: ObjectType) -> Task[TResult]: ...
    
    @overload
    def FromAsync(self, beginMethod: Func[TArg1, TArg2, TArg3, AsyncCallback, ObjectType, IAsyncResult], endMethod: Func[IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, arg3: TArg3, state: ObjectType, creationOptions: TaskCreationOptions) -> Task[TResult]: ...
    
    @overload
    def StartNew(self, function: Func[TResult]) -> Task[TResult]: ...
    
    @overload
    def StartNew(self, function: Func[TResult], cancellationToken: CancellationToken) -> Task[TResult]: ...
    
    @overload
    def StartNew(self, function: Func[TResult], creationOptions: TaskCreationOptions) -> Task[TResult]: ...
    
    @overload
    def StartNew(self, function: Func[TResult], cancellationToken: CancellationToken, creationOptions: TaskCreationOptions, scheduler: TaskScheduler) -> Task[TResult]: ...
    
    @overload
    def StartNew(self, function: Func[ObjectType, TResult], state: ObjectType) -> Task[TResult]: ...
    
    @overload
    def StartNew(self, function: Func[ObjectType, TResult], state: ObjectType, cancellationToken: CancellationToken) -> Task[TResult]: ...
    
    @overload
    def StartNew(self, function: Func[ObjectType, TResult], state: ObjectType, creationOptions: TaskCreationOptions) -> Task[TResult]: ...
    
    @overload
    def StartNew(self, function: Func[ObjectType, TResult], state: ObjectType, cancellationToken: CancellationToken, creationOptions: TaskCreationOptions, scheduler: TaskScheduler) -> Task[TResult]: ...
    
    def get_CancellationToken(self) -> CancellationToken: ...
    
    def get_ContinuationOptions(self) -> TaskContinuationOptions: ...
    
    def get_CreationOptions(self) -> TaskCreationOptions: ...
    
    def get_Scheduler(self) -> TaskScheduler: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TaskScheduler(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Current() -> TaskScheduler: ...
    
    @staticmethod
    @property
    def Default() -> TaskScheduler: ...
    
    @property
    def Id(self) -> IntType: ...
    
    @property
    def MaximumConcurrencyLevel(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def FromCurrentSynchronizationContext() -> TaskScheduler: ...
    
    @staticmethod
    def add_UnobservedTaskException(value: EventHandler[UnobservedTaskExceptionEventArgs]) -> VoidType: ...
    
    @staticmethod
    def get_Current() -> TaskScheduler: ...
    
    @staticmethod
    def get_Default() -> TaskScheduler: ...
    
    def get_Id(self) -> IntType: ...
    
    def get_MaximumConcurrencyLevel(self) -> IntType: ...
    
    @staticmethod
    def remove_UnobservedTaskException(value: EventHandler[UnobservedTaskExceptionEventArgs]) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    UnobservedTaskException: EventType[EventHandler[UnobservedTaskExceptionEventArgs]] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TaskSchedulerAwaitTaskContinuation(AwaitTaskContinuation, IThreadPoolWorkItem):
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


class TaskSchedulerException(Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, innerException: Exception): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TaskToApm(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Begin(task: Task, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    @staticmethod
    @overload
    def End(asyncResult: IAsyncResult) -> VoidType: ...
    
    @staticmethod
    @overload
    def End(asyncResult: IAsyncResult) -> TResult: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ThreadPoolTaskScheduler(TaskScheduler):
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


class TplEtwProvider(EventSource, IDisposable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Log() -> TplEtwProvider: ...
    
    @staticmethod
    @Log.setter
    def Log(value: TplEtwProvider) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AwaitTaskContinuationScheduled(self, OriginatingTaskSchedulerID: IntType, OriginatingTaskID: IntType, ContinuwWithTaskId: IntType) -> VoidType: ...
    
    def DebugFacilityMessage(self, Facility: StringType, Message: StringType) -> VoidType: ...
    
    def DebugFacilityMessage1(self, Facility: StringType, Message: StringType, Value1: StringType) -> VoidType: ...
    
    def DebugMessage(self, Message: StringType) -> VoidType: ...
    
    def NewID(self, TaskID: IntType) -> VoidType: ...
    
    def ParallelFork(self, OriginatingTaskSchedulerID: IntType, OriginatingTaskID: IntType, ForkJoinContextID: IntType) -> VoidType: ...
    
    def ParallelInvokeBegin(self, OriginatingTaskSchedulerID: IntType, OriginatingTaskID: IntType, ForkJoinContextID: IntType, OperationType: ForkJoinOperationType, ActionCount: IntType) -> VoidType: ...
    
    def ParallelInvokeEnd(self, OriginatingTaskSchedulerID: IntType, OriginatingTaskID: IntType, ForkJoinContextID: IntType) -> VoidType: ...
    
    def ParallelJoin(self, OriginatingTaskSchedulerID: IntType, OriginatingTaskID: IntType, ForkJoinContextID: IntType) -> VoidType: ...
    
    def ParallelLoopBegin(self, OriginatingTaskSchedulerID: IntType, OriginatingTaskID: IntType, ForkJoinContextID: IntType, OperationType: ForkJoinOperationType, InclusiveFrom: LongType, ExclusiveTo: LongType) -> VoidType: ...
    
    def ParallelLoopEnd(self, OriginatingTaskSchedulerID: IntType, OriginatingTaskID: IntType, ForkJoinContextID: IntType, TotalIterations: LongType) -> VoidType: ...
    
    def RunningContinuation(self, TaskID: IntType, Object: ObjectType) -> VoidType: ...
    
    @overload
    def RunningContinuationList(self, TaskID: IntType, Index: IntType, Object: ObjectType) -> VoidType: ...
    
    @overload
    def RunningContinuationList(self, TaskID: IntType, Index: IntType, Object: LongType) -> VoidType: ...
    
    def SetActivityId(self, NewId: Guid) -> VoidType: ...
    
    def TaskCompleted(self, OriginatingTaskSchedulerID: IntType, OriginatingTaskID: IntType, TaskID: IntType, IsExceptional: BooleanType) -> VoidType: ...
    
    def TaskScheduled(self, OriginatingTaskSchedulerID: IntType, OriginatingTaskID: IntType, TaskID: IntType, CreatingTaskID: IntType, TaskCreationOptions: IntType, appDomain: IntType) -> VoidType: ...
    
    def TaskStarted(self, OriginatingTaskSchedulerID: IntType, OriginatingTaskID: IntType, TaskID: IntType) -> VoidType: ...
    
    def TaskWaitBegin(self, OriginatingTaskSchedulerID: IntType, OriginatingTaskID: IntType, TaskID: IntType, Behavior: TaskWaitBehavior, ContinueWithTaskID: IntType, appDomain: IntType) -> VoidType: ...
    
    def TaskWaitContinuationComplete(self, TaskID: IntType) -> VoidType: ...
    
    def TaskWaitContinuationStarted(self, TaskID: IntType) -> VoidType: ...
    
    def TaskWaitEnd(self, OriginatingTaskSchedulerID: IntType, OriginatingTaskID: IntType, TaskID: IntType) -> VoidType: ...
    
    def TraceOperationBegin(self, TaskID: IntType, OperationName: StringType, RelatedContext: LongType) -> VoidType: ...
    
    def TraceOperationEnd(self, TaskID: IntType, Status: AsyncCausalityStatus) -> VoidType: ...
    
    def TraceOperationRelation(self, TaskID: IntType, Relation: CausalityRelation) -> VoidType: ...
    
    def TraceSynchronousWorkBegin(self, TaskID: IntType, Work: CausalitySynchronousWork) -> VoidType: ...
    
    def TraceSynchronousWorkEnd(self, Work: CausalitySynchronousWork) -> VoidType: ...
    
    # No Events
    
    
    # ---------- Sub Classes ---------- #
    
    class Tasks(ObjectType):
        # ---------- Fields ---------- #
        
        @staticmethod
        @property
        def AwaitTaskContinuationScheduled() -> EventTask: ...
        
        @staticmethod
        @property
        def ForkJoin() -> EventTask: ...
        
        @staticmethod
        @property
        def Invoke() -> EventTask: ...
        
        @staticmethod
        @property
        def Loop() -> EventTask: ...
        
        @staticmethod
        @property
        def TaskExecute() -> EventTask: ...
        
        @staticmethod
        @property
        def TaskScheduled() -> EventTask: ...
        
        @staticmethod
        @property
        def TaskWait() -> EventTask: ...
        
        @staticmethod
        @property
        def TraceOperation() -> EventTask: ...
        
        @staticmethod
        @property
        def TraceSynchronousWork() -> EventTask: ...
        
        # ---------- Constructors ---------- #
        
        def __init__(self): ...
        
        # No Properties
        
        # No Methods
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    class Keywords(ObjectType):
        # ---------- Fields ---------- #
        
        @staticmethod
        @property
        def AsyncCausalityOperation() -> EventKeywords: ...
        
        @staticmethod
        @property
        def AsyncCausalityRelation() -> EventKeywords: ...
        
        @staticmethod
        @property
        def AsyncCausalitySynchronousWork() -> EventKeywords: ...
        
        @staticmethod
        @property
        def Debug() -> EventKeywords: ...
        
        @staticmethod
        @property
        def DebugActivityId() -> EventKeywords: ...
        
        @staticmethod
        @property
        def Parallel() -> EventKeywords: ...
        
        @staticmethod
        @property
        def TaskStops() -> EventKeywords: ...
        
        @staticmethod
        @property
        def TaskTransfer() -> EventKeywords: ...
        
        @staticmethod
        @property
        def Tasks() -> EventKeywords: ...
        
        @staticmethod
        @property
        def TasksFlowActivityIds() -> EventKeywords: ...
        
        @staticmethod
        @property
        def TasksSetActivityIds() -> EventKeywords: ...
        
        # ---------- Constructors ---------- #
        
        def __init__(self): ...
        
        # No Properties
        
        # No Methods
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class ForkJoinOperationType(Enum):
        ParallelInvoke = 1
        ParallelFor = 2
        ParallelForEach = 3
    
    
    class TaskWaitBehavior(Enum):
        Synchronous = 1
        Asynchronous = 2
    


class UnobservedTaskExceptionEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, exception: AggregateException): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Exception(self) -> AggregateException: ...
    
    @property
    def Observed(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def SetObserved(self) -> VoidType: ...
    
    def get_Exception(self) -> AggregateException: ...
    
    def get_Observed(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnwrapPromise(Generic[TResult], Task[TResult], IThreadPoolWorkItem, IAsyncResult, IDisposable, ITaskCompletionAction):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, outerTask: Task, lookForOce: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Invoke(self, completingTask: Task) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class IndexRange(ValueType):
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


class PaddingFor32(ValueType):
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


class ParallelLoopResult(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsCompleted(self) -> BooleanType: ...
    
    @property
    def LowestBreakIteration(self) -> NullableType[Nullable[LongType]]: ...
    
    # ---------- Methods ---------- #
    
    def get_IsCompleted(self) -> BooleanType: ...
    
    def get_LowestBreakIteration(self) -> NullableType[Nullable[LongType]]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RangeWorker(ValueType):
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


class VoidTaskResult(ValueType):
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

class IProducerConsumerQueue(Protocol[T], IEnumerable[T], IEnumerable):
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsEmpty(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Enqueue(self, item: T) -> VoidType: ...
    
    def GetCountSafe(self, syncObj: ObjectType) -> IntType: ...
    
    def TryDequeue(self, result: T) -> Tuple[BooleanType, T]: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsEmpty(self) -> BooleanType: ...
    
    # No Events


class ITaskCompletionAction(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Invoke(self, completingTask: Task) -> VoidType: ...
    
    # No Events


# ---------- Enums ---------- #

class AsyncCausalityStatus(Enum):
    Started = 0
    Completed = 1
    Canceled = 2
    Error = 3


class CausalityRelation(Enum):
    AssignDelegate = 0
    Join = 1
    Choice = 2
    Cancel = 3
    Error = 4


class CausalitySynchronousWork(Enum):
    CompletionNotification = 0
    ProgressNotification = 1
    Execution = 2


class CausalityTraceLevel(Enum):
    Required = 0
    Important = 1
    Verbose = 2


class InternalTaskOptions(Enum):
    #None = 0
    ChildReplica = 256
    ContinuationTask = 512
    PromiseTask = 1024
    SelfReplicating = 2048
    LazyCancellation = 4096
    QueuedByRuntime = 8192
    DoNotDispose = 16384
    InternalOptionsMask = 65280


class TaskContinuationOptions(Enum):
    #None = 0
    PreferFairness = 1
    LongRunning = 2
    AttachedToParent = 4
    DenyChildAttach = 8
    HideScheduler = 16
    LazyCancellation = 32
    RunContinuationsAsynchronously = 64
    NotOnRanToCompletion = 65536
    NotOnFaulted = 131072
    OnlyOnCanceled = 196608
    NotOnCanceled = 262144
    OnlyOnFaulted = 327680
    OnlyOnRanToCompletion = 393216
    ExecuteSynchronously = 524288


class TaskCreationOptions(Enum):
    #None = 0
    PreferFairness = 1
    LongRunning = 2
    AttachedToParent = 4
    DenyChildAttach = 8
    HideScheduler = 16
    RunContinuationsAsynchronously = 64


class TaskStatus(Enum):
    Created = 0
    WaitingForActivation = 1
    WaitingToRun = 2
    Running = 3
    WaitingForChildrenToComplete = 4
    RanToCompletion = 5
    Canceled = 6
    Faulted = 7


# No Delegates

__all__ = [
    AsyncCausalityTracer,
    AwaitTaskContinuation,
    BeginEndAwaitableAdapter,
    CompletionActionInvoker,
    ConcurrentExclusiveSchedulerPair,
    ContinuationResultTaskFromResultTask,
    ContinuationResultTaskFromTask,
    ContinuationTaskFromResultTask,
    ContinuationTaskFromTask,
    GenericDelegateCache,
    MultiProducerMultiConsumerQueue,
    PaddingHelpers,
    Parallel,
    ParallelForReplicaTask,
    ParallelForReplicatingTask,
    ParallelLoopState,
    ParallelLoopState32,
    ParallelLoopState64,
    ParallelLoopStateFlags,
    ParallelLoopStateFlags32,
    ParallelLoopStateFlags64,
    ParallelOptions,
    RangeManager,
    Shared,
    SingleProducerSingleConsumerQueue,
    StackGuard,
    StandardTaskContinuation,
    SynchronizationContextAwaitTaskContinuation,
    SynchronizationContextTaskScheduler,
    SystemThreadingTasks_FutureDebugView,
    SystemThreadingTasks_TaskDebugView,
    Task,
    TaskCanceledException,
    TaskCompletionSource,
    TaskContinuation,
    TaskExceptionHolder,
    TaskExtensions,
    TaskFactory,
    TaskScheduler,
    TaskSchedulerAwaitTaskContinuation,
    TaskSchedulerException,
    TaskToApm,
    ThreadPoolTaskScheduler,
    TplEtwProvider,
    UnobservedTaskExceptionEventArgs,
    UnwrapPromise,
    IndexRange,
    PaddingFor32,
    ParallelLoopResult,
    RangeWorker,
    VoidTaskResult,
    IProducerConsumerQueue,
    ITaskCompletionAction,
    AsyncCausalityStatus,
    CausalityRelation,
    CausalitySynchronousWork,
    CausalityTraceLevel,
    InternalTaskOptions,
    TaskContinuationOptions,
    TaskCreationOptions,
    TaskStatus,
]
