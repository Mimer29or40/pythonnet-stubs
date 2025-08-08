"""Automatically generated stubs for C# namespace: System.Threading.Tasks."""

from abc import ABC
from collections.abc import Iterator
from typing import ClassVar
from typing import Self
from typing import overload

from System import Action
from System import AggregateException
from System import Array
from System import AsyncCallback
from System import Delegate
from System import Enum
from System import EventArgs
from System import EventHandler
from System import Exception
from System import Func
from System import Guid
from System import IAsyncResult
from System import IDisposable
from System import Object
from System import OperationCanceledException
from System import Predicate
from System import TimeSpan
from System import Type
from System import ValueType
from System.Collections import ICollection
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections.Concurrent import ConcurrentQueue
from System.Collections.Concurrent import IProducerConsumerCollection
from System.Collections.Concurrent import OrderablePartitioner
from System.Collections.Concurrent import Partitioner
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEnumerator
from System.Collections.Generic import IReadOnlyCollection
from System.Diagnostics.Tracing import EventChannel
from System.Diagnostics.Tracing import EventCommandEventArgs
from System.Diagnostics.Tracing import EventKeywords
from System.Diagnostics.Tracing import EventLevel
from System.Diagnostics.Tracing import EventSource
from System.Diagnostics.Tracing import EventSourceOptions
from System.Diagnostics.Tracing import EventSourceSettings
from System.Diagnostics.Tracing import EventTask
from System.Diagnostics.Tracing import T
from System.Reflection import MethodBase
from System.Runtime.CompilerServices import ConfiguredTaskAwaitable
from System.Runtime.CompilerServices import ICriticalNotifyCompletion
from System.Runtime.CompilerServices import INotifyCompletion
from System.Runtime.CompilerServices import TaskAwaiter
from System.Runtime.CompilerServices import YieldAwaitable
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Threading import CancellationToken
from System.Threading import IThreadPoolWorkItem
from System.Threading import StackCrawlMark
from System.Threading import ThreadAbortException
from System.Threading import WaitHandle

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

class AsyncCausalityStatus(Enum):
    """"""

    Started: AsyncCausalityStatus = ...
    """"""
    Completed: AsyncCausalityStatus = ...
    """"""
    Canceled: AsyncCausalityStatus = ...
    """"""
    Error: AsyncCausalityStatus = ...
    """"""

class AsyncCausalityTracer(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class AwaitTaskContinuation(TaskContinuation, IThreadPoolWorkItem):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class BeginEndAwaitableAdapter(Object, ICriticalNotifyCompletion, INotifyCompletion):
    """"""

    Callback: ClassVar[AsyncCallback]
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAwaiter(self) -> BeginEndAwaitableAdapter:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetResult(self) -> IAsyncResult:
        """"""
    def GetType(self) -> Type:
        """"""
    def OnCompleted(self, continuation: Action) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def UnsafeOnCompleted(self, continuation: Action) -> None:
        """"""

class CausalityRelation(Enum):
    """"""

    AssignDelegate: CausalityRelation = ...
    """"""
    Join: CausalityRelation = ...
    """"""
    Choice: CausalityRelation = ...
    """"""
    Cancel: CausalityRelation = ...
    """"""
    Error: CausalityRelation = ...
    """"""

class CausalitySynchronousWork(Enum):
    """"""

    CompletionNotification: CausalitySynchronousWork = ...
    """"""
    ProgressNotification: CausalitySynchronousWork = ...
    """"""
    Execution: CausalitySynchronousWork = ...
    """"""

class CausalityTraceLevel(Enum):
    """"""

    Required: CausalityTraceLevel = ...
    """"""
    Important: CausalityTraceLevel = ...
    """"""
    Verbose: CausalityTraceLevel = ...
    """"""

class CompletionActionInvoker(Object, IThreadPoolWorkItem):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class ConcurrentExclusiveSchedulerPair(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, taskScheduler: TaskScheduler) -> None:
        """"""
    @overload
    def __init__(self, taskScheduler: TaskScheduler, maxConcurrencyLevel: int) -> None:
        """"""
    @overload
    def __init__(
        self, taskScheduler: TaskScheduler, maxConcurrencyLevel: int, maxItemsPerTask: int
    ) -> None:
        """"""
    @property
    def Completion(self) -> Task:
        """"""
    @property
    def ConcurrentScheduler(self) -> TaskScheduler:
        """"""
    @property
    def ExclusiveScheduler(self) -> TaskScheduler:
        """"""
    def Complete(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ContinuationResultTaskFromResultTask[TAntecedentResult, TResult](
    Task[TResult], IThreadPoolWorkItem, IAsyncResult, IDisposable
):
    """"""
    def __init__(
        self,
        antecedent: Task[TAntecedentResult],
        function: Delegate,
        state: object,
        creationOptions: TaskCreationOptions,
        internalOptions: InternalTaskOptions,
        stackMark: StackCrawlMark,
    ) -> None:
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
    def CreationOptions(self) -> TaskCreationOptions:
        """"""
    @property
    def Exception(self) -> AggregateException:
        """"""
    @property
    def Id(self) -> int:
        """"""
    @property
    def IsCanceled(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    @property
    def IsFaulted(self) -> bool:
        """"""
    @property
    def Result(self) -> TResult:
        """"""
    @property
    def Status(self) -> TaskStatus:
        """"""
    def ConfigureAwait(self, continueOnCapturedContext: bool) -> ConfiguredTaskAwaitable:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task, object], state: object) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task, object], state: object, scheduler: TaskScheduler
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task[TResult], object], state: object
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task[TResult], object],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task[TResult], object],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task[TResult], object],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task[TResult], object],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task[TResult]]) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task[TResult]],
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task[TResult]], scheduler: TaskScheduler
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task[TResult]], cancellationToken: CancellationToken
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task[TResult]],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task]) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], continuationOptions: TaskContinuationOptions
    ) -> Task:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task], scheduler: TaskScheduler) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], cancellationToken: CancellationToken
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith[TResult](self, continuationFunction: Func[Task, TResult]) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, TResult], scheduler: TaskScheduler
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, object, TResult], state: object
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self, continuationFunction: Func[Task[TResult], TNewResult]
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], TNewResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self, continuationFunction: Func[Task[TResult], TNewResult], scheduler: TaskScheduler
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], TNewResult],
        cancellationToken: CancellationToken,
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], TNewResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self, continuationFunction: Func[Task[TResult], object, TNewResult], state: object
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], object, TNewResult],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], object, TNewResult],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], object, TNewResult],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], object, TNewResult],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TNewResult]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetAwaiter(self) -> TaskAwaiter:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """"""
    @overload
    def RunSynchronously(self) -> None:
        """"""
    @overload
    def RunSynchronously(self, scheduler: TaskScheduler) -> None:
        """"""
    @overload
    def Start(self) -> None:
        """"""
    @overload
    def Start(self, scheduler: TaskScheduler) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Wait(self) -> None:
        """"""
    @overload
    def Wait(self, cancellationToken: CancellationToken) -> None:
        """"""
    @overload
    def Wait(self, millisecondsTimeout: int) -> bool:
        """"""
    @overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool:
        """"""
    @overload
    def Wait(self, timeout: TimeSpan) -> bool:
        """"""

class ContinuationResultTaskFromTask[TResult](
    Task[TResult], IThreadPoolWorkItem, IAsyncResult, IDisposable
):
    """"""
    def __init__(
        self,
        antecedent: Task,
        function: Delegate,
        state: object,
        creationOptions: TaskCreationOptions,
        internalOptions: InternalTaskOptions,
        stackMark: StackCrawlMark,
    ) -> None:
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
    def CreationOptions(self) -> TaskCreationOptions:
        """"""
    @property
    def Exception(self) -> AggregateException:
        """"""
    @property
    def Id(self) -> int:
        """"""
    @property
    def IsCanceled(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    @property
    def IsFaulted(self) -> bool:
        """"""
    @property
    def Result(self) -> TResult:
        """"""
    @property
    def Status(self) -> TaskStatus:
        """"""
    def ConfigureAwait(self, continueOnCapturedContext: bool) -> ConfiguredTaskAwaitable:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task, object], state: object) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task, object], state: object, scheduler: TaskScheduler
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task[TResult], object], state: object
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task[TResult], object],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task[TResult], object],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task[TResult], object],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task[TResult], object],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task[TResult]]) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task[TResult]],
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task[TResult]], scheduler: TaskScheduler
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task[TResult]], cancellationToken: CancellationToken
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task[TResult]],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task]) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], continuationOptions: TaskContinuationOptions
    ) -> Task:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task], scheduler: TaskScheduler) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], cancellationToken: CancellationToken
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith[TResult](self, continuationFunction: Func[Task, TResult]) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, TResult], scheduler: TaskScheduler
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, object, TResult], state: object
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self, continuationFunction: Func[Task[TResult], TNewResult]
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], TNewResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self, continuationFunction: Func[Task[TResult], TNewResult], scheduler: TaskScheduler
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], TNewResult],
        cancellationToken: CancellationToken,
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], TNewResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self, continuationFunction: Func[Task[TResult], object, TNewResult], state: object
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], object, TNewResult],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], object, TNewResult],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], object, TNewResult],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], object, TNewResult],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TNewResult]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetAwaiter(self) -> TaskAwaiter:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """"""
    @overload
    def RunSynchronously(self) -> None:
        """"""
    @overload
    def RunSynchronously(self, scheduler: TaskScheduler) -> None:
        """"""
    @overload
    def Start(self) -> None:
        """"""
    @overload
    def Start(self, scheduler: TaskScheduler) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Wait(self) -> None:
        """"""
    @overload
    def Wait(self, cancellationToken: CancellationToken) -> None:
        """"""
    @overload
    def Wait(self, millisecondsTimeout: int) -> bool:
        """"""
    @overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool:
        """"""
    @overload
    def Wait(self, timeout: TimeSpan) -> bool:
        """"""

class ContinuationTaskFromResultTask[TAntecedentResult](
    Task, IThreadPoolWorkItem, IAsyncResult, IDisposable
):
    """"""
    def __init__(
        self,
        antecedent: Task[TAntecedentResult],
        action: Delegate,
        state: object,
        creationOptions: TaskCreationOptions,
        internalOptions: InternalTaskOptions,
        stackMark: StackCrawlMark,
    ) -> None:
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
    def CreationOptions(self) -> TaskCreationOptions:
        """"""
    @property
    def Exception(self) -> AggregateException:
        """"""
    @property
    def Id(self) -> int:
        """"""
    @property
    def IsCanceled(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    @property
    def IsFaulted(self) -> bool:
        """"""
    @property
    def Status(self) -> TaskStatus:
        """"""
    def ConfigureAwait(self, continueOnCapturedContext: bool) -> ConfiguredTaskAwaitable:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task, object], state: object) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task, object], state: object, scheduler: TaskScheduler
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task]) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], continuationOptions: TaskContinuationOptions
    ) -> Task:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task], scheduler: TaskScheduler) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], cancellationToken: CancellationToken
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith[TResult](self, continuationFunction: Func[Task, TResult]) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, TResult], scheduler: TaskScheduler
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, object, TResult], state: object
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetAwaiter(self) -> TaskAwaiter:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """"""
    @overload
    def RunSynchronously(self) -> None:
        """"""
    @overload
    def RunSynchronously(self, scheduler: TaskScheduler) -> None:
        """"""
    @overload
    def Start(self) -> None:
        """"""
    @overload
    def Start(self, scheduler: TaskScheduler) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Wait(self) -> None:
        """"""
    @overload
    def Wait(self, cancellationToken: CancellationToken) -> None:
        """"""
    @overload
    def Wait(self, millisecondsTimeout: int) -> bool:
        """"""
    @overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool:
        """"""
    @overload
    def Wait(self, timeout: TimeSpan) -> bool:
        """"""

class ContinuationTaskFromTask(Task, IThreadPoolWorkItem, IAsyncResult, IDisposable):
    """"""
    def __init__(
        self,
        antecedent: Task,
        action: Delegate,
        state: object,
        creationOptions: TaskCreationOptions,
        internalOptions: InternalTaskOptions,
        stackMark: StackCrawlMark,
    ) -> None:
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
    def CreationOptions(self) -> TaskCreationOptions:
        """"""
    @property
    def Exception(self) -> AggregateException:
        """"""
    @property
    def Id(self) -> int:
        """"""
    @property
    def IsCanceled(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    @property
    def IsFaulted(self) -> bool:
        """"""
    @property
    def Status(self) -> TaskStatus:
        """"""
    def ConfigureAwait(self, continueOnCapturedContext: bool) -> ConfiguredTaskAwaitable:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task, object], state: object) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task, object], state: object, scheduler: TaskScheduler
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task]) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], continuationOptions: TaskContinuationOptions
    ) -> Task:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task], scheduler: TaskScheduler) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], cancellationToken: CancellationToken
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith[TResult](self, continuationFunction: Func[Task, TResult]) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, TResult], scheduler: TaskScheduler
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, object, TResult], state: object
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetAwaiter(self) -> TaskAwaiter:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """"""
    @overload
    def RunSynchronously(self) -> None:
        """"""
    @overload
    def RunSynchronously(self, scheduler: TaskScheduler) -> None:
        """"""
    @overload
    def Start(self) -> None:
        """"""
    @overload
    def Start(self, scheduler: TaskScheduler) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Wait(self) -> None:
        """"""
    @overload
    def Wait(self, cancellationToken: CancellationToken) -> None:
        """"""
    @overload
    def Wait(self, millisecondsTimeout: int) -> bool:
        """"""
    @overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool:
        """"""
    @overload
    def Wait(self, timeout: TimeSpan) -> bool:
        """"""

class GenericDelegateCache[TAntecedentResult, TResult](ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IProducerConsumerQueue[T](ABC, IEnumerable[T], IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsEmpty(self) -> bool:
        """"""
    def Enqueue(self, item: T) -> None:
        """"""
    def GetCountSafe(self, syncObj: object) -> int:
        """"""
    def GetEnumerator[T](self) -> IEnumerator[T]:
        """"""
    def TryDequeue(self, result: T) -> tuple[bool, T]:
        """"""
    def __iter__[T](self) -> Iterator[T]:
        """"""
    def __len__(self) -> int:
        """"""

class ITaskCompletionAction(ABC):
    """"""
    def Invoke(self, completingTask: Task) -> None:
        """"""

class IndexRange(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class InternalTaskOptions(Enum):
    """"""

    _None: InternalTaskOptions = ...
    """"""
    ChildReplica: InternalTaskOptions = ...
    """"""
    ContinuationTask: InternalTaskOptions = ...
    """"""
    PromiseTask: InternalTaskOptions = ...
    """"""
    SelfReplicating: InternalTaskOptions = ...
    """"""
    LazyCancellation: InternalTaskOptions = ...
    """"""
    QueuedByRuntime: InternalTaskOptions = ...
    """"""
    DoNotDispose: InternalTaskOptions = ...
    """"""
    InternalOptionsMask: InternalTaskOptions = ...
    """"""

class MultiProducerMultiConsumerQueue[T](
    ConcurrentQueue[T],
    IProducerConsumerCollection[T],
    IEnumerable[T],
    IReadOnlyCollection[T],
    ICollection,
    IEnumerable,
    IProducerConsumerQueue[T],
):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsEmpty(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[T], index: int) -> None:
        """"""
    def Enqueue(self, item: T) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetCountSafe(self, syncObj: object) -> int:
        """"""
    def GetEnumerator[T](self) -> IEnumerator[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToArray(self) -> Array[T]:
        """"""
    def ToString(self) -> str:
        """"""
    def TryAdd(self, item: T) -> bool:
        """"""
    def TryDequeue(self, result: T) -> tuple[bool, T]:
        """"""
    def TryPeek(self, result: T) -> tuple[bool, T]:
        """"""
    def TryTake(self, item: T) -> tuple[bool, T]:
        """"""
    def __iter__[T](self) -> Iterator[T]:
        """"""
    def __len__(self) -> int:
        """"""

class PaddingFor32(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PaddingHelpers(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Parallel(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def For(
        cls,
        fromInclusive: int,
        toExclusive: int,
        parallelOptions: ParallelOptions,
        body: Action[int, ParallelLoopState],
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def For(
        cls,
        fromInclusive: int,
        toExclusive: int,
        parallelOptions: ParallelOptions,
        body: Action[int],
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def For[TLocal](
        cls,
        fromInclusive: int,
        toExclusive: int,
        parallelOptions: ParallelOptions,
        localInit: Func[TLocal],
        body: Func[int, ParallelLoopState, TLocal, TLocal],
        localFinally: Action[TLocal],
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def For(
        cls, fromInclusive: int, toExclusive: int, body: Action[int, ParallelLoopState]
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def For(cls, fromInclusive: int, toExclusive: int, body: Action[int]) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def For[TLocal](
        cls,
        fromInclusive: int,
        toExclusive: int,
        localInit: Func[TLocal],
        body: Func[int, ParallelLoopState, TLocal, TLocal],
        localFinally: Action[TLocal],
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def For(
        cls,
        fromInclusive: int,
        toExclusive: int,
        parallelOptions: ParallelOptions,
        body: Action[int, ParallelLoopState],
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def For(
        cls,
        fromInclusive: int,
        toExclusive: int,
        parallelOptions: ParallelOptions,
        body: Action[int],
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def For[TLocal](
        cls,
        fromInclusive: int,
        toExclusive: int,
        parallelOptions: ParallelOptions,
        localInit: Func[TLocal],
        body: Func[int, ParallelLoopState, TLocal, TLocal],
        localFinally: Action[TLocal],
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def For(
        cls, fromInclusive: int, toExclusive: int, body: Action[int, ParallelLoopState]
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def For(cls, fromInclusive: int, toExclusive: int, body: Action[int]) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def For[TLocal](
        cls,
        fromInclusive: int,
        toExclusive: int,
        localInit: Func[TLocal],
        body: Func[int, ParallelLoopState, TLocal, TLocal],
        localFinally: Action[TLocal],
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def ForEach[TSource](
        cls,
        source: OrderablePartitioner[TSource],
        parallelOptions: ParallelOptions,
        body: Action[TSource, ParallelLoopState, int],
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def ForEach[TSource, TLocal](
        cls,
        source: OrderablePartitioner[TSource],
        parallelOptions: ParallelOptions,
        localInit: Func[TLocal],
        body: Func[TSource, ParallelLoopState, int, TLocal, TLocal],
        localFinally: Action[TLocal],
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def ForEach[TSource](
        cls, source: OrderablePartitioner[TSource], body: Action[TSource, ParallelLoopState, int]
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def ForEach[TSource, TLocal](
        cls,
        source: OrderablePartitioner[TSource],
        localInit: Func[TLocal],
        body: Func[TSource, ParallelLoopState, int, TLocal, TLocal],
        localFinally: Action[TLocal],
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def ForEach[TSource](
        cls,
        source: Partitioner[TSource],
        parallelOptions: ParallelOptions,
        body: Action[TSource, ParallelLoopState],
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def ForEach[TSource](
        cls, source: Partitioner[TSource], parallelOptions: ParallelOptions, body: Action[TSource]
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def ForEach[TSource, TLocal](
        cls,
        source: Partitioner[TSource],
        parallelOptions: ParallelOptions,
        localInit: Func[TLocal],
        body: Func[TSource, ParallelLoopState, TLocal, TLocal],
        localFinally: Action[TLocal],
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def ForEach[TSource](
        cls, source: Partitioner[TSource], body: Action[TSource, ParallelLoopState]
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def ForEach[TSource](
        cls, source: Partitioner[TSource], body: Action[TSource]
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def ForEach[TSource, TLocal](
        cls,
        source: Partitioner[TSource],
        localInit: Func[TLocal],
        body: Func[TSource, ParallelLoopState, TLocal, TLocal],
        localFinally: Action[TLocal],
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def ForEach[TSource](
        cls,
        source: IEnumerable[TSource],
        parallelOptions: ParallelOptions,
        body: Action[TSource, ParallelLoopState, int],
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def ForEach[TSource](
        cls,
        source: IEnumerable[TSource],
        parallelOptions: ParallelOptions,
        body: Action[TSource, ParallelLoopState],
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def ForEach[TSource](
        cls, source: IEnumerable[TSource], parallelOptions: ParallelOptions, body: Action[TSource]
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def ForEach[TSource, TLocal](
        cls,
        source: IEnumerable[TSource],
        parallelOptions: ParallelOptions,
        localInit: Func[TLocal],
        body: Func[TSource, ParallelLoopState, TLocal, TLocal],
        localFinally: Action[TLocal],
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def ForEach[TSource, TLocal](
        cls,
        source: IEnumerable[TSource],
        parallelOptions: ParallelOptions,
        localInit: Func[TLocal],
        body: Func[TSource, ParallelLoopState, int, TLocal, TLocal],
        localFinally: Action[TLocal],
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def ForEach[TSource](
        cls, source: IEnumerable[TSource], body: Action[TSource, ParallelLoopState, int]
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def ForEach[TSource](
        cls, source: IEnumerable[TSource], body: Action[TSource, ParallelLoopState]
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def ForEach[TSource](
        cls, source: IEnumerable[TSource], body: Action[TSource]
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def ForEach[TSource, TLocal](
        cls,
        source: IEnumerable[TSource],
        localInit: Func[TLocal],
        body: Func[TSource, ParallelLoopState, TLocal, TLocal],
        localFinally: Action[TLocal],
    ) -> ParallelLoopResult:
        """"""
    @classmethod
    @overload
    def ForEach[TSource, TLocal](
        cls,
        source: IEnumerable[TSource],
        localInit: Func[TLocal],
        body: Func[TSource, ParallelLoopState, int, TLocal, TLocal],
        localFinally: Action[TLocal],
    ) -> ParallelLoopResult:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def Invoke(cls, parallelOptions: ParallelOptions, actions: Array[Action]) -> None:
        """"""
    @classmethod
    @overload
    def Invoke(cls, actions: Array[Action]) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class ParallelForReplicaTask(Task, IThreadPoolWorkItem, IAsyncResult, IDisposable):
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
    def CreationOptions(self) -> TaskCreationOptions:
        """"""
    @property
    def Exception(self) -> AggregateException:
        """"""
    @property
    def Id(self) -> int:
        """"""
    @property
    def IsCanceled(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    @property
    def IsFaulted(self) -> bool:
        """"""
    @property
    def Status(self) -> TaskStatus:
        """"""
    def ConfigureAwait(self, continueOnCapturedContext: bool) -> ConfiguredTaskAwaitable:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task, object], state: object) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task, object], state: object, scheduler: TaskScheduler
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task]) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], continuationOptions: TaskContinuationOptions
    ) -> Task:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task], scheduler: TaskScheduler) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], cancellationToken: CancellationToken
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith[TResult](self, continuationFunction: Func[Task, TResult]) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, TResult], scheduler: TaskScheduler
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, object, TResult], state: object
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetAwaiter(self) -> TaskAwaiter:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """"""
    @overload
    def RunSynchronously(self) -> None:
        """"""
    @overload
    def RunSynchronously(self, scheduler: TaskScheduler) -> None:
        """"""
    @overload
    def Start(self) -> None:
        """"""
    @overload
    def Start(self, scheduler: TaskScheduler) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Wait(self) -> None:
        """"""
    @overload
    def Wait(self, cancellationToken: CancellationToken) -> None:
        """"""
    @overload
    def Wait(self, millisecondsTimeout: int) -> bool:
        """"""
    @overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool:
        """"""
    @overload
    def Wait(self, timeout: TimeSpan) -> bool:
        """"""

class ParallelForReplicatingTask(Task, IThreadPoolWorkItem, IAsyncResult, IDisposable):
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
    def CreationOptions(self) -> TaskCreationOptions:
        """"""
    @property
    def Exception(self) -> AggregateException:
        """"""
    @property
    def Id(self) -> int:
        """"""
    @property
    def IsCanceled(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    @property
    def IsFaulted(self) -> bool:
        """"""
    @property
    def Status(self) -> TaskStatus:
        """"""
    def ConfigureAwait(self, continueOnCapturedContext: bool) -> ConfiguredTaskAwaitable:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task, object], state: object) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task, object], state: object, scheduler: TaskScheduler
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task]) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], continuationOptions: TaskContinuationOptions
    ) -> Task:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task], scheduler: TaskScheduler) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], cancellationToken: CancellationToken
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith[TResult](self, continuationFunction: Func[Task, TResult]) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, TResult], scheduler: TaskScheduler
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, object, TResult], state: object
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetAwaiter(self) -> TaskAwaiter:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """"""
    @overload
    def RunSynchronously(self) -> None:
        """"""
    @overload
    def RunSynchronously(self, scheduler: TaskScheduler) -> None:
        """"""
    @overload
    def Start(self) -> None:
        """"""
    @overload
    def Start(self, scheduler: TaskScheduler) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Wait(self) -> None:
        """"""
    @overload
    def Wait(self, cancellationToken: CancellationToken) -> None:
        """"""
    @overload
    def Wait(self, millisecondsTimeout: int) -> bool:
        """"""
    @overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool:
        """"""
    @overload
    def Wait(self, timeout: TimeSpan) -> bool:
        """"""

class ParallelLoopResult(ValueType):
    """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    @property
    def LowestBreakIteration(self) -> int | None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ParallelLoopState(Object):
    """"""
    @property
    def IsExceptional(self) -> bool:
        """"""
    @property
    def IsStopped(self) -> bool:
        """"""
    @property
    def LowestBreakIteration(self) -> int | None:
        """"""
    @property
    def ShouldExitCurrentIteration(self) -> bool:
        """"""
    def Break(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Stop(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class ParallelLoopState32(ParallelLoopState):
    """"""
    @property
    def IsExceptional(self) -> bool:
        """"""
    @property
    def IsStopped(self) -> bool:
        """"""
    @property
    def LowestBreakIteration(self) -> int | None:
        """"""
    @property
    def ShouldExitCurrentIteration(self) -> bool:
        """"""
    def Break(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Stop(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class ParallelLoopState64(ParallelLoopState):
    """"""
    @property
    def IsExceptional(self) -> bool:
        """"""
    @property
    def IsStopped(self) -> bool:
        """"""
    @property
    def LowestBreakIteration(self) -> int | None:
        """"""
    @property
    def ShouldExitCurrentIteration(self) -> bool:
        """"""
    def Break(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Stop(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class ParallelLoopStateFlags(Object):
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

class ParallelLoopStateFlags32(ParallelLoopStateFlags):
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

class ParallelLoopStateFlags64(ParallelLoopStateFlags):
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

class ParallelOptions(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CancellationToken(self) -> CancellationToken:
        """"""
    @CancellationToken.setter
    def CancellationToken(self, value: CancellationToken) -> None: ...
    @property
    def MaxDegreeOfParallelism(self) -> int:
        """"""
    @MaxDegreeOfParallelism.setter
    def MaxDegreeOfParallelism(self, value: int) -> None: ...
    @property
    def TaskScheduler(self) -> TaskScheduler:
        """"""
    @TaskScheduler.setter
    def TaskScheduler(self, value: TaskScheduler) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RangeManager(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RangeWorker(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Shared[T](Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SingleProducerSingleConsumerQueue[T](
    Object, IEnumerable[T], IEnumerable, IProducerConsumerQueue[T]
):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsEmpty(self) -> bool:
        """"""
    def Clear(self) -> None:
        """"""
    def Enqueue(self, item: T) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetCountSafe(self, syncObj: object) -> int:
        """"""
    def GetEnumerator[T](self) -> IEnumerator[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def TryDequeue(self, result: T) -> tuple[bool, T]:
        """"""
    def TryDequeueIf(self, predicate: Predicate[T], result: T) -> tuple[bool, T]:
        """"""
    def TryPeek(self, result: T) -> tuple[bool, T]:
        """"""
    def __iter__[T](self) -> Iterator[T]:
        """"""
    def __len__(self) -> int:
        """"""

class StackGuard(Object):
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

class StandardTaskContinuation(TaskContinuation):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SynchronizationContextAwaitTaskContinuation(AwaitTaskContinuation, IThreadPoolWorkItem):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SynchronizationContextTaskScheduler(TaskScheduler):
    """"""
    @property
    def Id(self) -> int:
        """"""
    @property
    def MaximumConcurrencyLevel(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SystemThreadingTasks_FutureDebugView[TResult](Object):
    """"""
    def __init__(self, task: Task[TResult]) -> None:
        """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def CancellationPending(self) -> bool:
        """"""
    @property
    def CreationOptions(self) -> TaskCreationOptions:
        """"""
    @property
    def Exception(self) -> Exception:
        """"""
    @property
    def Id(self) -> int:
        """"""
    @property
    def Result(self) -> TResult:
        """"""
    @property
    def Status(self) -> TaskStatus:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SystemThreadingTasks_TaskDebugView(Object):
    """"""
    def __init__(self, task: Task) -> None:
        """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def CancellationPending(self) -> bool:
        """"""
    @property
    def CreationOptions(self) -> TaskCreationOptions:
        """"""
    @property
    def Exception(self) -> Exception:
        """"""
    @property
    def Id(self) -> int:
        """"""
    @property
    def Status(self) -> TaskStatus:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Task(Object, IThreadPoolWorkItem, IAsyncResult, IDisposable):
    """"""
    @overload
    def __init__(self, action: Action) -> None:
        """"""
    @overload
    def __init__(self, action: Action, cancellationToken: CancellationToken) -> None:
        """"""
    @overload
    def __init__(self, action: Action, creationOptions: TaskCreationOptions) -> None:
        """"""
    @overload
    def __init__(
        self,
        action: Action,
        cancellationToken: CancellationToken,
        creationOptions: TaskCreationOptions,
    ) -> None:
        """"""
    @overload
    def __init__(self, action: Action[object], state: object) -> None:
        """"""
    @overload
    def __init__(
        self, action: Action[object], state: object, cancellationToken: CancellationToken
    ) -> None:
        """"""
    @overload
    def __init__(
        self, action: Action[object], state: object, creationOptions: TaskCreationOptions
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        action: Action[object],
        state: object,
        cancellationToken: CancellationToken,
        creationOptions: TaskCreationOptions,
    ) -> None:
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
    @classmethod
    @property
    def CompletedTask(cls) -> Task:
        """"""
    @property
    def CreationOptions(self) -> TaskCreationOptions:
        """"""
    @classmethod
    @property
    def CurrentId(cls) -> int | None:
        """"""
    @property
    def Exception(self) -> AggregateException:
        """"""
    @classmethod
    @property
    def Factory(cls) -> TaskFactory:
        """"""
    @property
    def Id(self) -> int:
        """"""
    @property
    def IsCanceled(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    @property
    def IsFaulted(self) -> bool:
        """"""
    @property
    def Status(self) -> TaskStatus:
        """"""
    def ConfigureAwait(self, continueOnCapturedContext: bool) -> ConfiguredTaskAwaitable:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task, object], state: object) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task, object], state: object, scheduler: TaskScheduler
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task]) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], continuationOptions: TaskContinuationOptions
    ) -> Task:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task], scheduler: TaskScheduler) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], cancellationToken: CancellationToken
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith[TResult](self, continuationFunction: Func[Task, TResult]) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, TResult], scheduler: TaskScheduler
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, object, TResult], state: object
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @classmethod
    @overload
    def Delay(cls, millisecondsDelay: int) -> Task:
        """"""
    @classmethod
    @overload
    def Delay(cls, millisecondsDelay: int, cancellationToken: CancellationToken) -> Task:
        """"""
    @classmethod
    @overload
    def Delay(cls, delay: TimeSpan) -> Task:
        """"""
    @classmethod
    @overload
    def Delay(cls, delay: TimeSpan, cancellationToken: CancellationToken) -> Task:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExecuteWorkItem(self) -> None:
        """"""
    @classmethod
    def FromCanceled[TResult](cls, cancellationToken: CancellationToken) -> Task[TResult]:
        """"""
    @classmethod
    def FromException[TResult](cls, exception: Exception) -> Task[TResult]:
        """"""
    @classmethod
    def FromResult[TResult](cls, result: TResult) -> Task[TResult]:
        """"""
    def GetAwaiter(self) -> TaskAwaiter:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """"""
    @classmethod
    @overload
    def Run(cls, action: Action) -> Task:
        """"""
    @classmethod
    @overload
    def Run(cls, action: Action, cancellationToken: CancellationToken) -> Task:
        """"""
    @classmethod
    @overload
    def Run[TResult](cls, function: Func[TResult]) -> Task[TResult]:
        """"""
    @classmethod
    @overload
    def Run[TResult](
        cls, function: Func[TResult], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """"""
    @classmethod
    @overload
    def Run[TResult](cls, function: Func[Task[TResult]]) -> Task[TResult]:
        """"""
    @classmethod
    @overload
    def Run[TResult](
        cls, function: Func[Task[TResult]], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """"""
    @classmethod
    @overload
    def Run(cls, function: Func[Task]) -> Task:
        """"""
    @classmethod
    @overload
    def Run(cls, function: Func[Task], cancellationToken: CancellationToken) -> Task:
        """"""
    @overload
    def RunSynchronously(self) -> None:
        """"""
    @overload
    def RunSynchronously(self, scheduler: TaskScheduler) -> None:
        """"""
    @overload
    def Start(self) -> None:
        """"""
    @overload
    def Start(self, scheduler: TaskScheduler) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Wait(self) -> None:
        """"""
    @overload
    def Wait(self, cancellationToken: CancellationToken) -> None:
        """"""
    @overload
    def Wait(self, millisecondsTimeout: int) -> bool:
        """"""
    @overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool:
        """"""
    @overload
    def Wait(self, timeout: TimeSpan) -> bool:
        """"""
    @classmethod
    @overload
    def WaitAll(cls, tasks: Array[Task]) -> None:
        """"""
    @classmethod
    @overload
    def WaitAll(cls, tasks: Array[Task], cancellationToken: CancellationToken) -> None:
        """"""
    @classmethod
    @overload
    def WaitAll(cls, tasks: Array[Task], millisecondsTimeout: int) -> bool:
        """"""
    @classmethod
    @overload
    def WaitAll(
        cls, tasks: Array[Task], millisecondsTimeout: int, cancellationToken: CancellationToken
    ) -> bool:
        """"""
    @classmethod
    @overload
    def WaitAll(cls, tasks: Array[Task], timeout: TimeSpan) -> bool:
        """"""
    @classmethod
    @overload
    def WaitAny(cls, tasks: Array[Task]) -> int:
        """"""
    @classmethod
    @overload
    def WaitAny(cls, tasks: Array[Task], cancellationToken: CancellationToken) -> int:
        """"""
    @classmethod
    @overload
    def WaitAny(cls, tasks: Array[Task], millisecondsTimeout: int) -> int:
        """"""
    @classmethod
    @overload
    def WaitAny(
        cls, tasks: Array[Task], millisecondsTimeout: int, cancellationToken: CancellationToken
    ) -> int:
        """"""
    @classmethod
    @overload
    def WaitAny(cls, tasks: Array[Task], timeout: TimeSpan) -> int:
        """"""
    @classmethod
    @overload
    def WhenAll[TResult](cls, tasks: IEnumerable[Task[TResult]]) -> Task[Array[TResult]]:
        """"""
    @classmethod
    @overload
    def WhenAll(cls, tasks: IEnumerable[Task]) -> Task:
        """"""
    @classmethod
    @overload
    def WhenAll[TResult](cls, tasks: Array[Task[TResult]]) -> Task[Array[TResult]]:
        """"""
    @classmethod
    @overload
    def WhenAll(cls, tasks: Array[Task]) -> Task:
        """"""
    @classmethod
    @overload
    def WhenAny[TResult](cls, tasks: IEnumerable[Task[TResult]]) -> Task[Task[TResult]]:
        """"""
    @classmethod
    @overload
    def WhenAny(cls, tasks: IEnumerable[Task]) -> Task[Task]:
        """"""
    @classmethod
    @overload
    def WhenAny[TResult](cls, tasks: Array[Task[TResult]]) -> Task[Task[TResult]]:
        """"""
    @classmethod
    @overload
    def WhenAny(cls, tasks: Array[Task]) -> Task[Task]:
        """"""
    @classmethod
    def Yield(cls) -> YieldAwaitable:
        """"""

class TaskCanceledException(OperationCanceledException, _Exception, ISerializable):
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
    def __init__(self, task: Task) -> None:
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
    @property
    def Task(self) -> Task:
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

class TaskCompletionSource[TResult](Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, creationOptions: TaskCreationOptions) -> None:
        """"""
    @overload
    def __init__(self, state: object) -> None:
        """"""
    @overload
    def __init__(self, state: object, creationOptions: TaskCreationOptions) -> None:
        """"""
    @property
    def Task(self) -> Task[TResult]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetCanceled(self) -> None:
        """"""
    @overload
    def SetException(self, exceptions: IEnumerable[Exception]) -> None:
        """"""
    @overload
    def SetException(self, exception: Exception) -> None:
        """"""
    def SetResult(self, result: TResult) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def TrySetCanceled(self) -> bool:
        """"""
    @overload
    def TrySetCanceled(self, cancellationToken: CancellationToken) -> bool:
        """"""
    @overload
    def TrySetException(self, exceptions: IEnumerable[Exception]) -> bool:
        """"""
    @overload
    def TrySetException(self, exception: Exception) -> bool:
        """"""
    def TrySetResult(self, result: TResult) -> bool:
        """"""

class TaskContinuation(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TaskContinuationOptions(Enum):
    """"""

    _None: TaskContinuationOptions = ...
    """"""
    PreferFairness: TaskContinuationOptions = ...
    """"""
    LongRunning: TaskContinuationOptions = ...
    """"""
    AttachedToParent: TaskContinuationOptions = ...
    """"""
    DenyChildAttach: TaskContinuationOptions = ...
    """"""
    HideScheduler: TaskContinuationOptions = ...
    """"""
    LazyCancellation: TaskContinuationOptions = ...
    """"""
    RunContinuationsAsynchronously: TaskContinuationOptions = ...
    """"""
    NotOnRanToCompletion: TaskContinuationOptions = ...
    """"""
    NotOnFaulted: TaskContinuationOptions = ...
    """"""
    OnlyOnCanceled: TaskContinuationOptions = ...
    """"""
    NotOnCanceled: TaskContinuationOptions = ...
    """"""
    OnlyOnFaulted: TaskContinuationOptions = ...
    """"""
    OnlyOnRanToCompletion: TaskContinuationOptions = ...
    """"""
    ExecuteSynchronously: TaskContinuationOptions = ...
    """"""

class TaskCreationOptions(Enum):
    """"""

    _None: TaskCreationOptions = ...
    """"""
    PreferFairness: TaskCreationOptions = ...
    """"""
    LongRunning: TaskCreationOptions = ...
    """"""
    AttachedToParent: TaskCreationOptions = ...
    """"""
    DenyChildAttach: TaskCreationOptions = ...
    """"""
    HideScheduler: TaskCreationOptions = ...
    """"""
    RunContinuationsAsynchronously: TaskCreationOptions = ...
    """"""

class TaskExceptionHolder(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TaskExtensions(ABC, Object):
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
    def Unwrap[TResult](cls, task: Task[Task[TResult]]) -> Task[TResult]:
        """"""
    @classmethod
    @overload
    def Unwrap(cls, task: Task[Task]) -> Task:
        """"""

class TaskFactory(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, cancellationToken: CancellationToken) -> None:
        """"""
    @overload
    def __init__(self, scheduler: TaskScheduler) -> None:
        """"""
    @overload
    def __init__(
        self, creationOptions: TaskCreationOptions, continuationOptions: TaskContinuationOptions
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        cancellationToken: CancellationToken,
        creationOptions: TaskCreationOptions,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> None:
        """"""
    @property
    def CancellationToken(self) -> CancellationToken:
        """"""
    @property
    def ContinuationOptions(self) -> TaskContinuationOptions:
        """"""
    @property
    def CreationOptions(self) -> TaskCreationOptions:
        """"""
    @property
    def Scheduler(self) -> TaskScheduler:
        """"""
    @overload
    def ContinueWhenAll[TAntecedentResult](
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationAction: Action[Array[Task[TAntecedentResult]]],
    ) -> Task:
        """"""
    @overload
    def ContinueWhenAll[TAntecedentResult](
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationAction: Action[Array[Task[TAntecedentResult]]],
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """"""
    @overload
    def ContinueWhenAll[TAntecedentResult](
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationAction: Action[Array[Task[TAntecedentResult]]],
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    @overload
    def ContinueWhenAll[TAntecedentResult](
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationAction: Action[Array[Task[TAntecedentResult]]],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWhenAll[TAntecedentResult, TResult](
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Array[Task[TAntecedentResult]], TResult],
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAll[TAntecedentResult, TResult](
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Array[Task[TAntecedentResult]], TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAll[TAntecedentResult, TResult](
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Array[Task[TAntecedentResult]], TResult],
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAll[TAntecedentResult, TResult](
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Array[Task[TAntecedentResult]], TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAll(self, tasks: Array[Task], continuationAction: Action[Array[Task]]) -> Task:
        """"""
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task],
        continuationAction: Action[Array[Task]],
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """"""
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task],
        continuationAction: Action[Array[Task]],
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task],
        continuationAction: Action[Array[Task]],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWhenAll[TResult](
        self, tasks: Array[Task], continuationFunction: Func[Array[Task], TResult]
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAll[TResult](
        self,
        tasks: Array[Task],
        continuationFunction: Func[Array[Task], TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAll[TResult](
        self,
        tasks: Array[Task],
        continuationFunction: Func[Array[Task], TResult],
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAll[TResult](
        self,
        tasks: Array[Task],
        continuationFunction: Func[Array[Task], TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAny[TAntecedentResult](
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationAction: Action[Task[TAntecedentResult]],
    ) -> Task:
        """"""
    @overload
    def ContinueWhenAny[TAntecedentResult](
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationAction: Action[Task[TAntecedentResult]],
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """"""
    @overload
    def ContinueWhenAny[TAntecedentResult](
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationAction: Action[Task[TAntecedentResult]],
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    @overload
    def ContinueWhenAny[TAntecedentResult](
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationAction: Action[Task[TAntecedentResult]],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWhenAny[TAntecedentResult, TResult](
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Task[TAntecedentResult], TResult],
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAny[TAntecedentResult, TResult](
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Task[TAntecedentResult], TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAny[TAntecedentResult, TResult](
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Task[TAntecedentResult], TResult],
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAny[TAntecedentResult, TResult](
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Task[TAntecedentResult], TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAny(self, tasks: Array[Task], continuationAction: Action[Task]) -> Task:
        """"""
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task],
        continuationAction: Action[Task],
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """"""
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task],
        continuationAction: Action[Task],
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task],
        continuationAction: Action[Task],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWhenAny[TResult](
        self, tasks: Array[Task], continuationFunction: Func[Task, TResult]
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAny[TResult](
        self,
        tasks: Array[Task],
        continuationFunction: Func[Task, TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAny[TResult](
        self,
        tasks: Array[Task],
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAny[TResult](
        self,
        tasks: Array[Task],
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def FromAsync[TArg1, TArg2, TArg3](
        self,
        beginMethod: Func[TArg1, TArg2, TArg3, AsyncCallback, object, IAsyncResult],
        endMethod: Action[IAsyncResult],
        arg1: TArg1,
        arg2: TArg2,
        arg3: TArg3,
        state: object,
    ) -> Task:
        """"""
    @overload
    def FromAsync[TArg1, TArg2, TArg3](
        self,
        beginMethod: Func[TArg1, TArg2, TArg3, AsyncCallback, object, IAsyncResult],
        endMethod: Action[IAsyncResult],
        arg1: TArg1,
        arg2: TArg2,
        arg3: TArg3,
        state: object,
        creationOptions: TaskCreationOptions,
    ) -> Task:
        """"""
    @overload
    def FromAsync[TArg1, TArg2, TArg3, TResult](
        self,
        beginMethod: Func[TArg1, TArg2, TArg3, AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        arg1: TArg1,
        arg2: TArg2,
        arg3: TArg3,
        state: object,
    ) -> Task[TResult]:
        """"""
    @overload
    def FromAsync[TArg1, TArg2, TArg3, TResult](
        self,
        beginMethod: Func[TArg1, TArg2, TArg3, AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        arg1: TArg1,
        arg2: TArg2,
        arg3: TArg3,
        state: object,
        creationOptions: TaskCreationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def FromAsync[TArg1, TArg2](
        self,
        beginMethod: Func[TArg1, TArg2, AsyncCallback, object, IAsyncResult],
        endMethod: Action[IAsyncResult],
        arg1: TArg1,
        arg2: TArg2,
        state: object,
    ) -> Task:
        """"""
    @overload
    def FromAsync[TArg1, TArg2](
        self,
        beginMethod: Func[TArg1, TArg2, AsyncCallback, object, IAsyncResult],
        endMethod: Action[IAsyncResult],
        arg1: TArg1,
        arg2: TArg2,
        state: object,
        creationOptions: TaskCreationOptions,
    ) -> Task:
        """"""
    @overload
    def FromAsync[TArg1, TArg2, TResult](
        self,
        beginMethod: Func[TArg1, TArg2, AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        arg1: TArg1,
        arg2: TArg2,
        state: object,
    ) -> Task[TResult]:
        """"""
    @overload
    def FromAsync[TArg1, TArg2, TResult](
        self,
        beginMethod: Func[TArg1, TArg2, AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        arg1: TArg1,
        arg2: TArg2,
        state: object,
        creationOptions: TaskCreationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def FromAsync[TArg1](
        self,
        beginMethod: Func[TArg1, AsyncCallback, object, IAsyncResult],
        endMethod: Action[IAsyncResult],
        arg1: TArg1,
        state: object,
    ) -> Task:
        """"""
    @overload
    def FromAsync[TArg1](
        self,
        beginMethod: Func[TArg1, AsyncCallback, object, IAsyncResult],
        endMethod: Action[IAsyncResult],
        arg1: TArg1,
        state: object,
        creationOptions: TaskCreationOptions,
    ) -> Task:
        """"""
    @overload
    def FromAsync[TArg1, TResult](
        self,
        beginMethod: Func[TArg1, AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        arg1: TArg1,
        state: object,
    ) -> Task[TResult]:
        """"""
    @overload
    def FromAsync[TArg1, TResult](
        self,
        beginMethod: Func[TArg1, AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        arg1: TArg1,
        state: object,
        creationOptions: TaskCreationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def FromAsync(
        self,
        beginMethod: Func[AsyncCallback, object, IAsyncResult],
        endMethod: Action[IAsyncResult],
        state: object,
    ) -> Task:
        """"""
    @overload
    def FromAsync(
        self,
        beginMethod: Func[AsyncCallback, object, IAsyncResult],
        endMethod: Action[IAsyncResult],
        state: object,
        creationOptions: TaskCreationOptions,
    ) -> Task:
        """"""
    @overload
    def FromAsync[TResult](
        self,
        beginMethod: Func[AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        state: object,
    ) -> Task[TResult]:
        """"""
    @overload
    def FromAsync[TResult](
        self,
        beginMethod: Func[AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        state: object,
        creationOptions: TaskCreationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def FromAsync(self, asyncResult: IAsyncResult, endMethod: Action[IAsyncResult]) -> Task:
        """"""
    @overload
    def FromAsync(
        self,
        asyncResult: IAsyncResult,
        endMethod: Action[IAsyncResult],
        creationOptions: TaskCreationOptions,
    ) -> Task:
        """"""
    @overload
    def FromAsync(
        self,
        asyncResult: IAsyncResult,
        endMethod: Action[IAsyncResult],
        creationOptions: TaskCreationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def FromAsync[TResult](
        self, asyncResult: IAsyncResult, endMethod: Func[IAsyncResult, TResult]
    ) -> Task[TResult]:
        """"""
    @overload
    def FromAsync[TResult](
        self,
        asyncResult: IAsyncResult,
        endMethod: Func[IAsyncResult, TResult],
        creationOptions: TaskCreationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def FromAsync[TResult](
        self,
        asyncResult: IAsyncResult,
        endMethod: Func[IAsyncResult, TResult],
        creationOptions: TaskCreationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def StartNew(self, action: Action) -> Task:
        """"""
    @overload
    def StartNew(self, action: Action, creationOptions: TaskCreationOptions) -> Task:
        """"""
    @overload
    def StartNew(self, action: Action, cancellationToken: CancellationToken) -> Task:
        """"""
    @overload
    def StartNew(
        self,
        action: Action,
        cancellationToken: CancellationToken,
        creationOptions: TaskCreationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def StartNew(self, action: Action[object], state: object) -> Task:
        """"""
    @overload
    def StartNew(
        self, action: Action[object], state: object, creationOptions: TaskCreationOptions
    ) -> Task:
        """"""
    @overload
    def StartNew(
        self, action: Action[object], state: object, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    @overload
    def StartNew(
        self,
        action: Action[object],
        state: object,
        cancellationToken: CancellationToken,
        creationOptions: TaskCreationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def StartNew[TResult](self, function: Func[TResult]) -> Task[TResult]:
        """"""
    @overload
    def StartNew[TResult](
        self, function: Func[TResult], creationOptions: TaskCreationOptions
    ) -> Task[TResult]:
        """"""
    @overload
    def StartNew[TResult](
        self, function: Func[TResult], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """"""
    @overload
    def StartNew[TResult](
        self,
        function: Func[TResult],
        cancellationToken: CancellationToken,
        creationOptions: TaskCreationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def StartNew[TResult](self, function: Func[object, TResult], state: object) -> Task[TResult]:
        """"""
    @overload
    def StartNew[TResult](
        self, function: Func[object, TResult], state: object, creationOptions: TaskCreationOptions
    ) -> Task[TResult]:
        """"""
    @overload
    def StartNew[TResult](
        self, function: Func[object, TResult], state: object, cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """"""
    @overload
    def StartNew[TResult](
        self,
        function: Func[object, TResult],
        state: object,
        cancellationToken: CancellationToken,
        creationOptions: TaskCreationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    def ToString(self) -> str:
        """"""

class TaskFactory[TResult](Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, cancellationToken: CancellationToken) -> None:
        """"""
    @overload
    def __init__(self, scheduler: TaskScheduler) -> None:
        """"""
    @overload
    def __init__(
        self, creationOptions: TaskCreationOptions, continuationOptions: TaskContinuationOptions
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        cancellationToken: CancellationToken,
        creationOptions: TaskCreationOptions,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> None:
        """"""
    @property
    def CancellationToken(self) -> CancellationToken:
        """"""
    @property
    def ContinuationOptions(self) -> TaskContinuationOptions:
        """"""
    @property
    def CreationOptions(self) -> TaskCreationOptions:
        """"""
    @property
    def Scheduler(self) -> TaskScheduler:
        """"""
    @overload
    def ContinueWhenAll[TAntecedentResult](
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Array[Task[TAntecedentResult]], TResult],
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAll[TAntecedentResult](
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Array[Task[TAntecedentResult]], TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAll[TAntecedentResult](
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Array[Task[TAntecedentResult]], TResult],
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAll[TAntecedentResult](
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Array[Task[TAntecedentResult]], TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAll(
        self, tasks: Array[Task], continuationFunction: Func[Array[Task], TResult]
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task],
        continuationFunction: Func[Array[Task], TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task],
        continuationFunction: Func[Array[Task], TResult],
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task],
        continuationFunction: Func[Array[Task], TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAny[TAntecedentResult](
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Task[TAntecedentResult], TResult],
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAny[TAntecedentResult](
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Task[TAntecedentResult], TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAny[TAntecedentResult](
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Task[TAntecedentResult], TResult],
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAny[TAntecedentResult](
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Task[TAntecedentResult], TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAny(
        self, tasks: Array[Task], continuationFunction: Func[Task, TResult]
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task],
        continuationFunction: Func[Task, TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task],
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task],
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def FromAsync[TArg1, TArg2, TArg3](
        self,
        beginMethod: Func[TArg1, TArg2, TArg3, AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        arg1: TArg1,
        arg2: TArg2,
        arg3: TArg3,
        state: object,
    ) -> Task[TResult]:
        """"""
    @overload
    def FromAsync[TArg1, TArg2, TArg3](
        self,
        beginMethod: Func[TArg1, TArg2, TArg3, AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        arg1: TArg1,
        arg2: TArg2,
        arg3: TArg3,
        state: object,
        creationOptions: TaskCreationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def FromAsync[TArg1, TArg2](
        self,
        beginMethod: Func[TArg1, TArg2, AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        arg1: TArg1,
        arg2: TArg2,
        state: object,
    ) -> Task[TResult]:
        """"""
    @overload
    def FromAsync[TArg1, TArg2](
        self,
        beginMethod: Func[TArg1, TArg2, AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        arg1: TArg1,
        arg2: TArg2,
        state: object,
        creationOptions: TaskCreationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def FromAsync[TArg1](
        self,
        beginMethod: Func[TArg1, AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        arg1: TArg1,
        state: object,
    ) -> Task[TResult]:
        """"""
    @overload
    def FromAsync[TArg1](
        self,
        beginMethod: Func[TArg1, AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        arg1: TArg1,
        state: object,
        creationOptions: TaskCreationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def FromAsync(
        self,
        beginMethod: Func[AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        state: object,
    ) -> Task[TResult]:
        """"""
    @overload
    def FromAsync(
        self,
        beginMethod: Func[AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        state: object,
        creationOptions: TaskCreationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def FromAsync(
        self, asyncResult: IAsyncResult, endMethod: Func[IAsyncResult, TResult]
    ) -> Task[TResult]:
        """"""
    @overload
    def FromAsync(
        self,
        asyncResult: IAsyncResult,
        endMethod: Func[IAsyncResult, TResult],
        creationOptions: TaskCreationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def FromAsync(
        self,
        asyncResult: IAsyncResult,
        endMethod: Func[IAsyncResult, TResult],
        creationOptions: TaskCreationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def StartNew(self, function: Func[TResult]) -> Task[TResult]:
        """"""
    @overload
    def StartNew(
        self, function: Func[TResult], creationOptions: TaskCreationOptions
    ) -> Task[TResult]:
        """"""
    @overload
    def StartNew(
        self, function: Func[TResult], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """"""
    @overload
    def StartNew(
        self,
        function: Func[TResult],
        cancellationToken: CancellationToken,
        creationOptions: TaskCreationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def StartNew(self, function: Func[object, TResult], state: object) -> Task[TResult]:
        """"""
    @overload
    def StartNew(
        self, function: Func[object, TResult], state: object, creationOptions: TaskCreationOptions
    ) -> Task[TResult]:
        """"""
    @overload
    def StartNew(
        self, function: Func[object, TResult], state: object, cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """"""
    @overload
    def StartNew(
        self,
        function: Func[object, TResult],
        state: object,
        cancellationToken: CancellationToken,
        creationOptions: TaskCreationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    def ToString(self) -> str:
        """"""

class TaskScheduler(ABC, Object):
    """"""
    @classmethod
    @property
    def Current(cls) -> TaskScheduler:
        """"""
    @classmethod
    @property
    def Default(cls) -> TaskScheduler:
        """"""
    @property
    def Id(self) -> int:
        """"""
    @property
    def MaximumConcurrencyLevel(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FromCurrentSynchronizationContext(cls) -> TaskScheduler:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    UnobservedTaskException: EventType[EventHandler[UnobservedTaskExceptionEventArgs]] = ...
    """"""

class TaskSchedulerAwaitTaskContinuation(AwaitTaskContinuation, IThreadPoolWorkItem):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class TaskSchedulerException(Exception, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, innerException: Exception) -> None:
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

class TaskStatus(Enum):
    """"""

    Created: TaskStatus = ...
    """"""
    WaitingForActivation: TaskStatus = ...
    """"""
    WaitingToRun: TaskStatus = ...
    """"""
    Running: TaskStatus = ...
    """"""
    WaitingForChildrenToComplete: TaskStatus = ...
    """"""
    RanToCompletion: TaskStatus = ...
    """"""
    Canceled: TaskStatus = ...
    """"""
    Faulted: TaskStatus = ...
    """"""

class TaskToApm(ABC, Object):
    """"""
    @classmethod
    def Begin(cls, task: Task, callback: AsyncCallback, state: object) -> IAsyncResult:
        """"""
    @classmethod
    def End[TResult](cls, asyncResult: IAsyncResult) -> TResult:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Task[TResult](Task, IThreadPoolWorkItem, IAsyncResult, IDisposable):
    """"""
    @overload
    def __init__(self, function: Func[TResult]) -> None:
        """"""
    @overload
    def __init__(self, function: Func[TResult], cancellationToken: CancellationToken) -> None:
        """"""
    @overload
    def __init__(self, function: Func[TResult], creationOptions: TaskCreationOptions) -> None:
        """"""
    @overload
    def __init__(
        self,
        function: Func[TResult],
        cancellationToken: CancellationToken,
        creationOptions: TaskCreationOptions,
    ) -> None:
        """"""
    @overload
    def __init__(self, function: Func[object, TResult], state: object) -> None:
        """"""
    @overload
    def __init__(
        self, function: Func[object, TResult], state: object, cancellationToken: CancellationToken
    ) -> None:
        """"""
    @overload
    def __init__(
        self, function: Func[object, TResult], state: object, creationOptions: TaskCreationOptions
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        function: Func[object, TResult],
        state: object,
        cancellationToken: CancellationToken,
        creationOptions: TaskCreationOptions,
    ) -> None:
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
    def CreationOptions(self) -> TaskCreationOptions:
        """"""
    @property
    def Exception(self) -> AggregateException:
        """"""
    @classmethod
    @property
    def Factory(cls) -> TaskFactory[TResult]:
        """"""
    @property
    def Id(self) -> int:
        """"""
    @property
    def IsCanceled(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    @property
    def IsFaulted(self) -> bool:
        """"""
    @property
    def Result(self) -> TResult:
        """"""
    @property
    def Status(self) -> TaskStatus:
        """"""
    def ConfigureAwait(self, continueOnCapturedContext: bool) -> ConfiguredTaskAwaitable:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task, object], state: object) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task, object], state: object, scheduler: TaskScheduler
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task[TResult], object], state: object
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task[TResult], object],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task[TResult], object],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task[TResult], object],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task[TResult], object],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task[TResult]]) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task[TResult]],
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task[TResult]], scheduler: TaskScheduler
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task[TResult]], cancellationToken: CancellationToken
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task[TResult]],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task]) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], continuationOptions: TaskContinuationOptions
    ) -> Task:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task], scheduler: TaskScheduler) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], cancellationToken: CancellationToken
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith[TResult](self, continuationFunction: Func[Task, TResult]) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, TResult], scheduler: TaskScheduler
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, object, TResult], state: object
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self, continuationFunction: Func[Task[TResult], TNewResult]
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], TNewResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self, continuationFunction: Func[Task[TResult], TNewResult], scheduler: TaskScheduler
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], TNewResult],
        cancellationToken: CancellationToken,
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], TNewResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self, continuationFunction: Func[Task[TResult], object, TNewResult], state: object
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], object, TNewResult],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], object, TNewResult],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], object, TNewResult],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], object, TNewResult],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TNewResult]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetAwaiter(self) -> TaskAwaiter:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """"""
    @overload
    def RunSynchronously(self) -> None:
        """"""
    @overload
    def RunSynchronously(self, scheduler: TaskScheduler) -> None:
        """"""
    @overload
    def Start(self) -> None:
        """"""
    @overload
    def Start(self, scheduler: TaskScheduler) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Wait(self) -> None:
        """"""
    @overload
    def Wait(self, cancellationToken: CancellationToken) -> None:
        """"""
    @overload
    def Wait(self, millisecondsTimeout: int) -> bool:
        """"""
    @overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool:
        """"""
    @overload
    def Wait(self, timeout: TimeSpan) -> bool:
        """"""

class ThreadPoolTaskScheduler(TaskScheduler):
    """"""
    @property
    def Id(self) -> int:
        """"""
    @property
    def MaximumConcurrencyLevel(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TplEtwProvider(EventSource, IDisposable):
    """"""

    Log: ClassVar[TplEtwProvider]
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
    def AwaitTaskContinuationScheduled(
        self, OriginatingTaskSchedulerID: int, OriginatingTaskID: int, ContinuwWithTaskId: int
    ) -> None:
        """"""
    def DebugFacilityMessage(self, Facility: str, Message: str) -> None:
        """"""
    def DebugFacilityMessage1(self, Facility: str, Message: str, Value1: str) -> None:
        """"""
    def DebugMessage(self, Message: str) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
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
    def NewID(self, TaskID: int) -> None:
        """"""
    def ParallelFork(
        self, OriginatingTaskSchedulerID: int, OriginatingTaskID: int, ForkJoinContextID: int
    ) -> None:
        """"""
    def ParallelInvokeBegin(
        self,
        OriginatingTaskSchedulerID: int,
        OriginatingTaskID: int,
        ForkJoinContextID: int,
        OperationType: TplEtwProvider.ForkJoinOperationType,
        ActionCount: int,
    ) -> None:
        """"""
    def ParallelInvokeEnd(
        self, OriginatingTaskSchedulerID: int, OriginatingTaskID: int, ForkJoinContextID: int
    ) -> None:
        """"""
    def ParallelJoin(
        self, OriginatingTaskSchedulerID: int, OriginatingTaskID: int, ForkJoinContextID: int
    ) -> None:
        """"""
    def ParallelLoopBegin(
        self,
        OriginatingTaskSchedulerID: int,
        OriginatingTaskID: int,
        ForkJoinContextID: int,
        OperationType: TplEtwProvider.ForkJoinOperationType,
        InclusiveFrom: int,
        ExclusiveTo: int,
    ) -> None:
        """"""
    def ParallelLoopEnd(
        self,
        OriginatingTaskSchedulerID: int,
        OriginatingTaskID: int,
        ForkJoinContextID: int,
        TotalIterations: int,
    ) -> None:
        """"""
    def RunningContinuation(self, TaskID: int, Object: object) -> None:
        """"""
    @overload
    def RunningContinuationList(self, TaskID: int, Index: int, Object: int) -> None:
        """"""
    @overload
    def RunningContinuationList(self, TaskID: int, Index: int, Object: object) -> None:
        """"""
    def SetActivityId(self, NewId: Guid) -> None:
        """"""
    def TaskCompleted(
        self,
        OriginatingTaskSchedulerID: int,
        OriginatingTaskID: int,
        TaskID: int,
        IsExceptional: bool,
    ) -> None:
        """"""
    def TaskScheduled(
        self,
        OriginatingTaskSchedulerID: int,
        OriginatingTaskID: int,
        TaskID: int,
        CreatingTaskID: int,
        TaskCreationOptions: int,
        appDomain: int,
    ) -> None:
        """"""
    def TaskStarted(
        self, OriginatingTaskSchedulerID: int, OriginatingTaskID: int, TaskID: int
    ) -> None:
        """"""
    def TaskWaitBegin(
        self,
        OriginatingTaskSchedulerID: int,
        OriginatingTaskID: int,
        TaskID: int,
        Behavior: TplEtwProvider.TaskWaitBehavior,
        ContinueWithTaskID: int,
        appDomain: int,
    ) -> None:
        """"""
    def TaskWaitContinuationComplete(self, TaskID: int) -> None:
        """"""
    def TaskWaitContinuationStarted(self, TaskID: int) -> None:
        """"""
    def TaskWaitEnd(
        self, OriginatingTaskSchedulerID: int, OriginatingTaskID: int, TaskID: int
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TraceOperationBegin(self, TaskID: int, OperationName: str, RelatedContext: int) -> None:
        """"""
    def TraceOperationEnd(self, TaskID: int, Status: AsyncCausalityStatus) -> None:
        """"""
    def TraceOperationRelation(self, TaskID: int, Relation: CausalityRelation) -> None:
        """"""
    def TraceSynchronousWorkBegin(self, TaskID: int, Work: CausalitySynchronousWork) -> None:
        """"""
    def TraceSynchronousWorkEnd(self, Work: CausalitySynchronousWork) -> None:
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
    class ForkJoinOperationType(Enum):
        """"""

        ParallelInvoke: TplEtwProvider.ForkJoinOperationType = ...
        """"""
        ParallelFor: TplEtwProvider.ForkJoinOperationType = ...
        """"""
        ParallelForEach: TplEtwProvider.ForkJoinOperationType = ...
        """"""

    class Keywords(Object):
        """"""

        AsyncCausalityOperation: ClassVar[EventKeywords]
        """"""
        AsyncCausalityRelation: ClassVar[EventKeywords]
        """"""
        AsyncCausalitySynchronousWork: ClassVar[EventKeywords]
        """"""
        Debug: ClassVar[EventKeywords]
        """"""
        DebugActivityId: ClassVar[EventKeywords]
        """"""
        Parallel: ClassVar[EventKeywords]
        """"""
        TaskStops: ClassVar[EventKeywords]
        """"""
        TaskTransfer: ClassVar[EventKeywords]
        """"""
        Tasks: ClassVar[EventKeywords]
        """"""
        TasksFlowActivityIds: ClassVar[EventKeywords]
        """"""
        TasksSetActivityIds: ClassVar[EventKeywords]
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

    class TaskWaitBehavior(Enum):
        """"""

        Synchronous: TplEtwProvider.TaskWaitBehavior = ...
        """"""
        Asynchronous: TplEtwProvider.TaskWaitBehavior = ...
        """"""

    class Tasks(Object):
        """"""

        AwaitTaskContinuationScheduled: ClassVar[EventTask]
        """"""
        ForkJoin: ClassVar[EventTask]
        """"""
        Invoke: ClassVar[EventTask]
        """"""
        Loop: ClassVar[EventTask]
        """"""
        TaskExecute: ClassVar[EventTask]
        """"""
        TaskScheduled: ClassVar[EventTask]
        """"""
        TaskWait: ClassVar[EventTask]
        """"""
        TraceOperation: ClassVar[EventTask]
        """"""
        TraceSynchronousWork: ClassVar[EventTask]
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

class UnobservedTaskExceptionEventArgs(EventArgs):
    """"""
    def __init__(self, exception: AggregateException) -> None:
        """"""
    @property
    def Exception(self) -> AggregateException:
        """"""
    @property
    def Observed(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetObserved(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class UnwrapPromise[TResult](
    Task[TResult], ITaskCompletionAction, IThreadPoolWorkItem, IAsyncResult, IDisposable
):
    """"""
    def __init__(self, outerTask: Task, lookForOce: bool) -> None:
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
    def CreationOptions(self) -> TaskCreationOptions:
        """"""
    @property
    def Exception(self) -> AggregateException:
        """"""
    @property
    def Id(self) -> int:
        """"""
    @property
    def IsCanceled(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    @property
    def IsFaulted(self) -> bool:
        """"""
    @property
    def Result(self) -> TResult:
        """"""
    @property
    def Status(self) -> TaskStatus:
        """"""
    def ConfigureAwait(self, continueOnCapturedContext: bool) -> ConfiguredTaskAwaitable:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task, object], state: object) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task, object], state: object, scheduler: TaskScheduler
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task[TResult], object], state: object
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task[TResult], object],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task[TResult], object],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task[TResult], object],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task[TResult], object],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task[TResult]]) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task[TResult]],
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task[TResult]], scheduler: TaskScheduler
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task[TResult]], cancellationToken: CancellationToken
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task[TResult]],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task]) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], continuationOptions: TaskContinuationOptions
    ) -> Task:
        """"""
    @overload
    def ContinueWith(self, continuationAction: Action[Task], scheduler: TaskScheduler) -> Task:
        """"""
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], cancellationToken: CancellationToken
    ) -> Task:
        """"""
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """"""
    @overload
    def ContinueWith[TResult](self, continuationFunction: Func[Task, TResult]) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, TResult], scheduler: TaskScheduler
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self, continuationFunction: Func[Task, object, TResult], state: object
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TResult](
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self, continuationFunction: Func[Task[TResult], TNewResult]
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], TNewResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self, continuationFunction: Func[Task[TResult], TNewResult], scheduler: TaskScheduler
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], TNewResult],
        cancellationToken: CancellationToken,
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], TNewResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self, continuationFunction: Func[Task[TResult], object, TNewResult], state: object
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], object, TNewResult],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], object, TNewResult],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], object, TNewResult],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task[TNewResult]:
        """"""
    @overload
    def ContinueWith[TNewResult](
        self,
        continuationFunction: Func[Task[TResult], object, TNewResult],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TNewResult]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetAwaiter(self) -> TaskAwaiter:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Invoke(self, completingTask: Task) -> None:
        """"""
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """"""
    @overload
    def RunSynchronously(self) -> None:
        """"""
    @overload
    def RunSynchronously(self, scheduler: TaskScheduler) -> None:
        """"""
    @overload
    def Start(self) -> None:
        """"""
    @overload
    def Start(self, scheduler: TaskScheduler) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Wait(self) -> None:
        """"""
    @overload
    def Wait(self, cancellationToken: CancellationToken) -> None:
        """"""
    @overload
    def Wait(self, millisecondsTimeout: int) -> bool:
        """"""
    @overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool:
        """"""
    @overload
    def Wait(self, timeout: TimeSpan) -> bool:
        """"""

class VoidTaskResult(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
