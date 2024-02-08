from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Iterator
from typing import Optional
from typing import Tuple
from typing import TypeVar
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
from System.Collections import IEnumerator
from System.Collections.Concurrent import ConcurrentQueue
from System.Collections.Concurrent import IProducerConsumerCollection
from System.Collections.Concurrent import OrderablePartitioner
from System.Collections.Concurrent import Partitioner
from System.Collections.Generic import IEnumerable
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
from System.Threading.Tasks.TplEtwProvider import ForkJoinOperationType
from System.Threading.Tasks.TplEtwProvider import TaskWaitBehavior

T = TypeVar("T")
TAntecedentResult = TypeVar("TAntecedentResult")
TArg1 = TypeVar("TArg1")
TArg2 = TypeVar("TArg2")
TArg3 = TypeVar("TArg3")
TLocal = TypeVar("TLocal")
TResult = TypeVar("TResult")
TSource = TypeVar("TSource")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

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

class AwaitTaskContinuation(TaskContinuation, IThreadPoolWorkItem):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """

        :param tae:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class BeginEndAwaitableAdapter(Object, ICriticalNotifyCompletion, INotifyCompletion):
    """"""

    Callback: Final[ClassVar[AsyncCallback]] = ...
    """
    
    :return: 
    """
    def __init__(self):
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
    def GetAwaiter(self) -> BeginEndAwaitableAdapter:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetResult(self) -> IAsyncResult:
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
        """

        :param obj:
        :return:
        """
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """

        :param tae:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ConcurrentExclusiveSchedulerPair(Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, taskScheduler: TaskScheduler):
        """

        :param taskScheduler:
        """
    @overload
    def __init__(self, taskScheduler: TaskScheduler, maxConcurrencyLevel: int):
        """

        :param taskScheduler:
        :param maxConcurrencyLevel:
        """
    @overload
    def __init__(
        self, taskScheduler: TaskScheduler, maxConcurrencyLevel: int, maxItemsPerTask: int
    ):
        """

        :param taskScheduler:
        :param maxConcurrencyLevel:
        :param maxItemsPerTask:
        """
    @property
    def Completion(self) -> Task:
        """

        :return:
        """
    @property
    def ConcurrentScheduler(self) -> TaskScheduler:
        """

        :return:
        """
    @property
    def ExclusiveScheduler(self) -> TaskScheduler:
        """

        :return:
        """
    def Complete(self) -> None:
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

class ContinuationResultTaskFromResultTask(
    Generic[TAntecedentResult, TResult],
    Task[TResult],
    IThreadPoolWorkItem,
    IAsyncResult,
    IDisposable,
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
    ):
        """

        :param antecedent:
        :param function:
        :param state:
        :param creationOptions:
        :param internalOptions:
        :param stackMark:
        """
    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def CompletedTask(cls) -> Task:
        """

        :return:
        """
    @property
    def CreationOptions(self) -> TaskCreationOptions:
        """

        :return:
        """
    @classmethod
    @property
    def CurrentId(cls) -> Optional[int]:
        """

        :return:
        """
    @property
    def Exception(self) -> AggregateException:
        """

        :return:
        """
    @classmethod
    @property
    def Factory(cls) -> TaskFactory:
        """

        :return:
        """
    @property
    def Id(self) -> int:
        """

        :return:
        """
    @property
    def IsCanceled(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
        """

        :return:
        """
    @property
    def IsFaulted(self) -> bool:
        """

        :return:
        """
    @property
    def Result(self) -> TResult:
        """

        :return:
        """
    @property
    def Status(self) -> TaskStatus:
        """

        :return:
        """
    def ConfigureAwait(self, continueOnCapturedContext: bool) -> ConfiguredTaskAwaitable:
        """

        :param continueOnCapturedContext:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task]) -> Task:
        """

        :param continuationAction:
        :return:
        """
    @overload
    def ContinueWith(self, continuationFunction: Func[Task, TResult]) -> Task[TResult]:
        """

        :param continuationFunction:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task, object], state: object) -> Task:
        """

        :param continuationAction:
        :param state:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], continuationOptions: TaskContinuationOptions
    ) -> Task:
        """

        :param continuationAction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task], scheduler: TaskScheduler) -> Task:
        """

        :param continuationAction:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], cancellationToken: CancellationToken
    ) -> Task:
        """

        :param continuationAction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, TResult], scheduler: TaskScheduler
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, object, TResult], state: object
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task, object], state: object, scheduler: TaskScheduler
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param continuationAction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetAwaiter(self) -> TaskAwaiter:
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
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """

        :param tae:
        """
    @overload
    def RunSynchronously(self) -> None:
        """"""
    @overload
    def RunSynchronously(self, scheduler: TaskScheduler) -> None:
        """

        :param scheduler:
        """
    @overload
    def Start(self) -> None:
        """"""
    @overload
    def Start(self, scheduler: TaskScheduler) -> None:
        """

        :param scheduler:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Wait(self) -> None:
        """"""
    @overload
    def Wait(self, cancellationToken: CancellationToken) -> None:
        """

        :param cancellationToken:
        """
    @overload
    def Wait(self, millisecondsTimeout: int) -> bool:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def Wait(self, timeout: TimeSpan) -> bool:
        """

        :param timeout:
        :return:
        """
    @overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool:
        """

        :param millisecondsTimeout:
        :param cancellationToken:
        :return:
        """

class ContinuationResultTaskFromTask(
    Generic[TResult], Task[TResult], IThreadPoolWorkItem, IAsyncResult, IDisposable
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
    ):
        """

        :param antecedent:
        :param function:
        :param state:
        :param creationOptions:
        :param internalOptions:
        :param stackMark:
        """
    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def CompletedTask(cls) -> Task:
        """

        :return:
        """
    @property
    def CreationOptions(self) -> TaskCreationOptions:
        """

        :return:
        """
    @classmethod
    @property
    def CurrentId(cls) -> Optional[int]:
        """

        :return:
        """
    @property
    def Exception(self) -> AggregateException:
        """

        :return:
        """
    @classmethod
    @property
    def Factory(cls) -> TaskFactory:
        """

        :return:
        """
    @property
    def Id(self) -> int:
        """

        :return:
        """
    @property
    def IsCanceled(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
        """

        :return:
        """
    @property
    def IsFaulted(self) -> bool:
        """

        :return:
        """
    @property
    def Result(self) -> TResult:
        """

        :return:
        """
    @property
    def Status(self) -> TaskStatus:
        """

        :return:
        """
    def ConfigureAwait(self, continueOnCapturedContext: bool) -> ConfiguredTaskAwaitable:
        """

        :param continueOnCapturedContext:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task]) -> Task:
        """

        :param continuationAction:
        :return:
        """
    @overload
    def ContinueWith(self, continuationFunction: Func[Task, TResult]) -> Task[TResult]:
        """

        :param continuationFunction:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task, object], state: object) -> Task:
        """

        :param continuationAction:
        :param state:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], continuationOptions: TaskContinuationOptions
    ) -> Task:
        """

        :param continuationAction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task], scheduler: TaskScheduler) -> Task:
        """

        :param continuationAction:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], cancellationToken: CancellationToken
    ) -> Task:
        """

        :param continuationAction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, TResult], scheduler: TaskScheduler
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, object, TResult], state: object
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task, object], state: object, scheduler: TaskScheduler
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param continuationAction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetAwaiter(self) -> TaskAwaiter:
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
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """

        :param tae:
        """
    @overload
    def RunSynchronously(self) -> None:
        """"""
    @overload
    def RunSynchronously(self, scheduler: TaskScheduler) -> None:
        """

        :param scheduler:
        """
    @overload
    def Start(self) -> None:
        """"""
    @overload
    def Start(self, scheduler: TaskScheduler) -> None:
        """

        :param scheduler:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Wait(self) -> None:
        """"""
    @overload
    def Wait(self, cancellationToken: CancellationToken) -> None:
        """

        :param cancellationToken:
        """
    @overload
    def Wait(self, millisecondsTimeout: int) -> bool:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def Wait(self, timeout: TimeSpan) -> bool:
        """

        :param timeout:
        :return:
        """
    @overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool:
        """

        :param millisecondsTimeout:
        :param cancellationToken:
        :return:
        """

class ContinuationTaskFromResultTask(
    Generic[TAntecedentResult], Task, IThreadPoolWorkItem, IAsyncResult, IDisposable
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
    ):
        """

        :param antecedent:
        :param action:
        :param state:
        :param creationOptions:
        :param internalOptions:
        :param stackMark:
        """
    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def CompletedTask(cls) -> Task:
        """

        :return:
        """
    @property
    def CreationOptions(self) -> TaskCreationOptions:
        """

        :return:
        """
    @classmethod
    @property
    def CurrentId(cls) -> Optional[int]:
        """

        :return:
        """
    @property
    def Exception(self) -> AggregateException:
        """

        :return:
        """
    @classmethod
    @property
    def Factory(cls) -> TaskFactory:
        """

        :return:
        """
    @property
    def Id(self) -> int:
        """

        :return:
        """
    @property
    def IsCanceled(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
        """

        :return:
        """
    @property
    def IsFaulted(self) -> bool:
        """

        :return:
        """
    @property
    def Status(self) -> TaskStatus:
        """

        :return:
        """
    def ConfigureAwait(self, continueOnCapturedContext: bool) -> ConfiguredTaskAwaitable:
        """

        :param continueOnCapturedContext:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task]) -> Task:
        """

        :param continuationAction:
        :return:
        """
    @overload
    def ContinueWith(self, continuationFunction: Func[Task, TResult]) -> Task[TResult]:
        """

        :param continuationFunction:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task, object], state: object) -> Task:
        """

        :param continuationAction:
        :param state:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], continuationOptions: TaskContinuationOptions
    ) -> Task:
        """

        :param continuationAction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task], scheduler: TaskScheduler) -> Task:
        """

        :param continuationAction:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], cancellationToken: CancellationToken
    ) -> Task:
        """

        :param continuationAction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, TResult], scheduler: TaskScheduler
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, object, TResult], state: object
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task, object], state: object, scheduler: TaskScheduler
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param continuationAction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetAwaiter(self) -> TaskAwaiter:
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
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """

        :param tae:
        """
    @overload
    def RunSynchronously(self) -> None:
        """"""
    @overload
    def RunSynchronously(self, scheduler: TaskScheduler) -> None:
        """

        :param scheduler:
        """
    @overload
    def Start(self) -> None:
        """"""
    @overload
    def Start(self, scheduler: TaskScheduler) -> None:
        """

        :param scheduler:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Wait(self) -> None:
        """"""
    @overload
    def Wait(self, cancellationToken: CancellationToken) -> None:
        """

        :param cancellationToken:
        """
    @overload
    def Wait(self, millisecondsTimeout: int) -> bool:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def Wait(self, timeout: TimeSpan) -> bool:
        """

        :param timeout:
        :return:
        """
    @overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool:
        """

        :param millisecondsTimeout:
        :param cancellationToken:
        :return:
        """

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
    ):
        """

        :param antecedent:
        :param action:
        :param state:
        :param creationOptions:
        :param internalOptions:
        :param stackMark:
        """
    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def CompletedTask(cls) -> Task:
        """

        :return:
        """
    @property
    def CreationOptions(self) -> TaskCreationOptions:
        """

        :return:
        """
    @classmethod
    @property
    def CurrentId(cls) -> Optional[int]:
        """

        :return:
        """
    @property
    def Exception(self) -> AggregateException:
        """

        :return:
        """
    @classmethod
    @property
    def Factory(cls) -> TaskFactory:
        """

        :return:
        """
    @property
    def Id(self) -> int:
        """

        :return:
        """
    @property
    def IsCanceled(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
        """

        :return:
        """
    @property
    def IsFaulted(self) -> bool:
        """

        :return:
        """
    @property
    def Status(self) -> TaskStatus:
        """

        :return:
        """
    def ConfigureAwait(self, continueOnCapturedContext: bool) -> ConfiguredTaskAwaitable:
        """

        :param continueOnCapturedContext:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task]) -> Task:
        """

        :param continuationAction:
        :return:
        """
    @overload
    def ContinueWith(self, continuationFunction: Func[Task, TResult]) -> Task[TResult]:
        """

        :param continuationFunction:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task, object], state: object) -> Task:
        """

        :param continuationAction:
        :param state:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], continuationOptions: TaskContinuationOptions
    ) -> Task:
        """

        :param continuationAction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task], scheduler: TaskScheduler) -> Task:
        """

        :param continuationAction:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], cancellationToken: CancellationToken
    ) -> Task:
        """

        :param continuationAction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, TResult], scheduler: TaskScheduler
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, object, TResult], state: object
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task, object], state: object, scheduler: TaskScheduler
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param continuationAction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetAwaiter(self) -> TaskAwaiter:
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
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """

        :param tae:
        """
    @overload
    def RunSynchronously(self) -> None:
        """"""
    @overload
    def RunSynchronously(self, scheduler: TaskScheduler) -> None:
        """

        :param scheduler:
        """
    @overload
    def Start(self) -> None:
        """"""
    @overload
    def Start(self, scheduler: TaskScheduler) -> None:
        """

        :param scheduler:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Wait(self) -> None:
        """"""
    @overload
    def Wait(self, cancellationToken: CancellationToken) -> None:
        """

        :param cancellationToken:
        """
    @overload
    def Wait(self, millisecondsTimeout: int) -> bool:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def Wait(self, timeout: TimeSpan) -> bool:
        """

        :param timeout:
        :return:
        """
    @overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool:
        """

        :param millisecondsTimeout:
        :param cancellationToken:
        :return:
        """

class GenericDelegateCache(ABC, Generic[TAntecedentResult, TResult], Object):
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

class IProducerConsumerQueue(Generic[T], IEnumerable[T], IEnumerable):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsEmpty(self) -> bool:
        """

        :return:
        """
    def Enqueue(self, item: T) -> None:
        """

        :param item:
        """
    def GetCountSafe(self, syncObj: object) -> int:
        """

        :param syncObj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def TryDequeue(self, result: T) -> Tuple[bool, T]:
        """

        :param result:
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

class ITaskCompletionAction:
    """"""

    def Invoke(self, completingTask: Task) -> None:
        """

        :param completingTask:
        """

class IndexRange(ValueType):
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

class MultiProducerMultiConsumerQueue(
    Generic[T],
    ConcurrentQueue[T],
    IProducerConsumerCollection[T],
    IEnumerable[T],
    IReadOnlyCollection[T],
    ICollection,
    IEnumerable,
    IProducerConsumerQueue[T],
):
    """"""

    def __init__(self):
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
    def IsEmpty(self) -> bool:
        """

        :return:
        """
    @property
    def IsEmpty(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[T], index: int) -> None:
        """"""
    @overload
    def Enqueue(self, item: T) -> None:
        """

        :param item:
        """
    @overload
    def Enqueue(self, item: T) -> None:
        """

        :param item:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetCountSafe(self, syncObj: object) -> int:
        """

        :param syncObj:
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
    def ToArray(self) -> Array[T]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TryAdd(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def TryDequeue(self, result: T) -> Tuple[bool, T]:
        """"""
    @overload
    def TryDequeue(self, result: T) -> Tuple[bool, T]:
        """

        :param result:
        :return:
        """
    def TryPeek(self, result: T) -> Tuple[bool, T]:
        """"""
    def TryTake(self, item: T) -> Tuple[bool, T]:
        """"""
    def __contains__(self, value: object) -> bool:
        """

        :param value:
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
    def __len__(self) -> int:
        """

        :return:
        """

class PaddingFor32(ValueType):
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

class PaddingHelpers(ABC, Object):
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

class Parallel(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def For(
        cls, fromInclusive: int, toExclusive: int, body: Action[int, ParallelLoopState]
    ) -> ParallelLoopResult:
        """

        :param fromInclusive:
        :param toExclusive:
        :param body:
        :return:
        """
    @classmethod
    @overload
    def For(cls, fromInclusive: int, toExclusive: int, body: Action[int]) -> ParallelLoopResult:
        """

        :param fromInclusive:
        :param toExclusive:
        :param body:
        :return:
        """
    @classmethod
    @overload
    def For(
        cls, fromInclusive: int, toExclusive: int, body: Action[int, ParallelLoopState]
    ) -> ParallelLoopResult:
        """

        :param fromInclusive:
        :param toExclusive:
        :param body:
        :return:
        """
    @classmethod
    @overload
    def For(cls, fromInclusive: int, toExclusive: int, body: Action[int]) -> ParallelLoopResult:
        """

        :param fromInclusive:
        :param toExclusive:
        :param body:
        :return:
        """
    @classmethod
    @overload
    def For(
        cls,
        fromInclusive: int,
        toExclusive: int,
        parallelOptions: ParallelOptions,
        body: Action[int, ParallelLoopState],
    ) -> ParallelLoopResult:
        """

        :param fromInclusive:
        :param toExclusive:
        :param parallelOptions:
        :param body:
        :return:
        """
    @classmethod
    @overload
    def For(
        cls,
        fromInclusive: int,
        toExclusive: int,
        parallelOptions: ParallelOptions,
        body: Action[int],
    ) -> ParallelLoopResult:
        """

        :param fromInclusive:
        :param toExclusive:
        :param parallelOptions:
        :param body:
        :return:
        """
    @classmethod
    @overload
    def For(
        cls,
        fromInclusive: int,
        toExclusive: int,
        parallelOptions: ParallelOptions,
        body: Action[int, ParallelLoopState],
    ) -> ParallelLoopResult:
        """

        :param fromInclusive:
        :param toExclusive:
        :param parallelOptions:
        :param body:
        :return:
        """
    @classmethod
    @overload
    def For(
        cls,
        fromInclusive: int,
        toExclusive: int,
        parallelOptions: ParallelOptions,
        body: Action[int],
    ) -> ParallelLoopResult:
        """

        :param fromInclusive:
        :param toExclusive:
        :param parallelOptions:
        :param body:
        :return:
        """
    @classmethod
    @overload
    def For(
        cls,
        fromInclusive: int,
        toExclusive: int,
        localInit: Func[TLocal],
        body: Func[int, ParallelLoopState, TLocal, TLocal],
        localFinally: Action[TLocal],
    ) -> ParallelLoopResult:
        """

        :param fromInclusive:
        :param toExclusive:
        :param localInit:
        :param body:
        :param localFinally:
        :return:
        """
    @classmethod
    @overload
    def For(
        cls,
        fromInclusive: int,
        toExclusive: int,
        localInit: Func[TLocal],
        body: Func[int, ParallelLoopState, TLocal, TLocal],
        localFinally: Action[TLocal],
    ) -> ParallelLoopResult:
        """

        :param fromInclusive:
        :param toExclusive:
        :param localInit:
        :param body:
        :param localFinally:
        :return:
        """
    @classmethod
    @overload
    def For(
        cls,
        fromInclusive: int,
        toExclusive: int,
        parallelOptions: ParallelOptions,
        localInit: Func[TLocal],
        body: Func[int, ParallelLoopState, TLocal, TLocal],
        localFinally: Action[TLocal],
    ) -> ParallelLoopResult:
        """

        :param fromInclusive:
        :param toExclusive:
        :param parallelOptions:
        :param localInit:
        :param body:
        :param localFinally:
        :return:
        """
    @classmethod
    @overload
    def For(
        cls,
        fromInclusive: int,
        toExclusive: int,
        parallelOptions: ParallelOptions,
        localInit: Func[TLocal],
        body: Func[int, ParallelLoopState, TLocal, TLocal],
        localFinally: Action[TLocal],
    ) -> ParallelLoopResult:
        """

        :param fromInclusive:
        :param toExclusive:
        :param parallelOptions:
        :param localInit:
        :param body:
        :param localFinally:
        :return:
        """
    @classmethod
    @overload
    def ForEach(
        cls, source: OrderablePartitioner[TSource], body: Action[TSource, ParallelLoopState, int]
    ) -> ParallelLoopResult:
        """

        :param source:
        :param body:
        :return:
        """
    @classmethod
    @overload
    def ForEach(
        cls, source: Partitioner[TSource], body: Action[TSource, ParallelLoopState]
    ) -> ParallelLoopResult:
        """

        :param source:
        :param body:
        :return:
        """
    @classmethod
    @overload
    def ForEach(cls, source: Partitioner[TSource], body: Action[TSource]) -> ParallelLoopResult:
        """

        :param source:
        :param body:
        :return:
        """
    @classmethod
    @overload
    def ForEach(
        cls, source: IEnumerable[TSource], body: Action[TSource, ParallelLoopState, int]
    ) -> ParallelLoopResult:
        """

        :param source:
        :param body:
        :return:
        """
    @classmethod
    @overload
    def ForEach(
        cls, source: IEnumerable[TSource], body: Action[TSource, ParallelLoopState]
    ) -> ParallelLoopResult:
        """

        :param source:
        :param body:
        :return:
        """
    @classmethod
    @overload
    def ForEach(cls, source: IEnumerable[TSource], body: Action[TSource]) -> ParallelLoopResult:
        """

        :param source:
        :param body:
        :return:
        """
    @classmethod
    @overload
    def ForEach(
        cls,
        source: OrderablePartitioner[TSource],
        parallelOptions: ParallelOptions,
        body: Action[TSource, ParallelLoopState, int],
    ) -> ParallelLoopResult:
        """

        :param source:
        :param parallelOptions:
        :param body:
        :return:
        """
    @classmethod
    @overload
    def ForEach(
        cls,
        source: Partitioner[TSource],
        parallelOptions: ParallelOptions,
        body: Action[TSource, ParallelLoopState],
    ) -> ParallelLoopResult:
        """

        :param source:
        :param parallelOptions:
        :param body:
        :return:
        """
    @classmethod
    @overload
    def ForEach(
        cls, source: Partitioner[TSource], parallelOptions: ParallelOptions, body: Action[TSource]
    ) -> ParallelLoopResult:
        """

        :param source:
        :param parallelOptions:
        :param body:
        :return:
        """
    @classmethod
    @overload
    def ForEach(
        cls,
        source: IEnumerable[TSource],
        parallelOptions: ParallelOptions,
        body: Action[TSource, ParallelLoopState, int],
    ) -> ParallelLoopResult:
        """

        :param source:
        :param parallelOptions:
        :param body:
        :return:
        """
    @classmethod
    @overload
    def ForEach(
        cls,
        source: IEnumerable[TSource],
        parallelOptions: ParallelOptions,
        body: Action[TSource, ParallelLoopState],
    ) -> ParallelLoopResult:
        """

        :param source:
        :param parallelOptions:
        :param body:
        :return:
        """
    @classmethod
    @overload
    def ForEach(
        cls, source: IEnumerable[TSource], parallelOptions: ParallelOptions, body: Action[TSource]
    ) -> ParallelLoopResult:
        """

        :param source:
        :param parallelOptions:
        :param body:
        :return:
        """
    @classmethod
    @overload
    def ForEach(
        cls,
        source: OrderablePartitioner[TSource],
        localInit: Func[TLocal],
        body: Func[TSource, ParallelLoopState, int, TLocal, TLocal],
        localFinally: Action[TLocal],
    ) -> ParallelLoopResult:
        """

        :param source:
        :param localInit:
        :param body:
        :param localFinally:
        :return:
        """
    @classmethod
    @overload
    def ForEach(
        cls,
        source: Partitioner[TSource],
        localInit: Func[TLocal],
        body: Func[TSource, ParallelLoopState, TLocal, TLocal],
        localFinally: Action[TLocal],
    ) -> ParallelLoopResult:
        """

        :param source:
        :param localInit:
        :param body:
        :param localFinally:
        :return:
        """
    @classmethod
    @overload
    def ForEach(
        cls,
        source: IEnumerable[TSource],
        localInit: Func[TLocal],
        body: Func[TSource, ParallelLoopState, TLocal, TLocal],
        localFinally: Action[TLocal],
    ) -> ParallelLoopResult:
        """

        :param source:
        :param localInit:
        :param body:
        :param localFinally:
        :return:
        """
    @classmethod
    @overload
    def ForEach(
        cls,
        source: IEnumerable[TSource],
        localInit: Func[TLocal],
        body: Func[TSource, ParallelLoopState, int, TLocal, TLocal],
        localFinally: Action[TLocal],
    ) -> ParallelLoopResult:
        """

        :param source:
        :param localInit:
        :param body:
        :param localFinally:
        :return:
        """
    @classmethod
    @overload
    def ForEach(
        cls,
        source: OrderablePartitioner[TSource],
        parallelOptions: ParallelOptions,
        localInit: Func[TLocal],
        body: Func[TSource, ParallelLoopState, int, TLocal, TLocal],
        localFinally: Action[TLocal],
    ) -> ParallelLoopResult:
        """

        :param source:
        :param parallelOptions:
        :param localInit:
        :param body:
        :param localFinally:
        :return:
        """
    @classmethod
    @overload
    def ForEach(
        cls,
        source: Partitioner[TSource],
        parallelOptions: ParallelOptions,
        localInit: Func[TLocal],
        body: Func[TSource, ParallelLoopState, TLocal, TLocal],
        localFinally: Action[TLocal],
    ) -> ParallelLoopResult:
        """

        :param source:
        :param parallelOptions:
        :param localInit:
        :param body:
        :param localFinally:
        :return:
        """
    @classmethod
    @overload
    def ForEach(
        cls,
        source: IEnumerable[TSource],
        parallelOptions: ParallelOptions,
        localInit: Func[TLocal],
        body: Func[TSource, ParallelLoopState, TLocal, TLocal],
        localFinally: Action[TLocal],
    ) -> ParallelLoopResult:
        """

        :param source:
        :param parallelOptions:
        :param localInit:
        :param body:
        :param localFinally:
        :return:
        """
    @classmethod
    @overload
    def ForEach(
        cls,
        source: IEnumerable[TSource],
        parallelOptions: ParallelOptions,
        localInit: Func[TLocal],
        body: Func[TSource, ParallelLoopState, int, TLocal, TLocal],
        localFinally: Action[TLocal],
    ) -> ParallelLoopResult:
        """

        :param source:
        :param parallelOptions:
        :param localInit:
        :param body:
        :param localFinally:
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
    @overload
    def Invoke(cls, actions: Array[Action]) -> None:
        """

        :param actions:
        """
    @classmethod
    @overload
    def Invoke(cls, parallelOptions: ParallelOptions, actions: Array[Action]) -> None:
        """

        :param parallelOptions:
        :param actions:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ParallelForReplicaTask(Task, IThreadPoolWorkItem, IAsyncResult, IDisposable):
    """"""

    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def CompletedTask(cls) -> Task:
        """

        :return:
        """
    @property
    def CreationOptions(self) -> TaskCreationOptions:
        """

        :return:
        """
    @classmethod
    @property
    def CurrentId(cls) -> Optional[int]:
        """

        :return:
        """
    @property
    def Exception(self) -> AggregateException:
        """

        :return:
        """
    @classmethod
    @property
    def Factory(cls) -> TaskFactory:
        """

        :return:
        """
    @property
    def Id(self) -> int:
        """

        :return:
        """
    @property
    def IsCanceled(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
        """

        :return:
        """
    @property
    def IsFaulted(self) -> bool:
        """

        :return:
        """
    @property
    def Status(self) -> TaskStatus:
        """

        :return:
        """
    def ConfigureAwait(self, continueOnCapturedContext: bool) -> ConfiguredTaskAwaitable:
        """

        :param continueOnCapturedContext:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task]) -> Task:
        """

        :param continuationAction:
        :return:
        """
    @overload
    def ContinueWith(self, continuationFunction: Func[Task, TResult]) -> Task[TResult]:
        """

        :param continuationFunction:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task, object], state: object) -> Task:
        """

        :param continuationAction:
        :param state:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], continuationOptions: TaskContinuationOptions
    ) -> Task:
        """

        :param continuationAction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task], scheduler: TaskScheduler) -> Task:
        """

        :param continuationAction:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], cancellationToken: CancellationToken
    ) -> Task:
        """

        :param continuationAction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, TResult], scheduler: TaskScheduler
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, object, TResult], state: object
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task, object], state: object, scheduler: TaskScheduler
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param continuationAction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetAwaiter(self) -> TaskAwaiter:
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
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """

        :param tae:
        """
    @overload
    def RunSynchronously(self) -> None:
        """"""
    @overload
    def RunSynchronously(self, scheduler: TaskScheduler) -> None:
        """

        :param scheduler:
        """
    @overload
    def Start(self) -> None:
        """"""
    @overload
    def Start(self, scheduler: TaskScheduler) -> None:
        """

        :param scheduler:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Wait(self) -> None:
        """"""
    @overload
    def Wait(self, cancellationToken: CancellationToken) -> None:
        """

        :param cancellationToken:
        """
    @overload
    def Wait(self, millisecondsTimeout: int) -> bool:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def Wait(self, timeout: TimeSpan) -> bool:
        """

        :param timeout:
        :return:
        """
    @overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool:
        """

        :param millisecondsTimeout:
        :param cancellationToken:
        :return:
        """

class ParallelForReplicatingTask(Task, IThreadPoolWorkItem, IAsyncResult, IDisposable):
    """"""

    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def CompletedTask(cls) -> Task:
        """

        :return:
        """
    @property
    def CreationOptions(self) -> TaskCreationOptions:
        """

        :return:
        """
    @classmethod
    @property
    def CurrentId(cls) -> Optional[int]:
        """

        :return:
        """
    @property
    def Exception(self) -> AggregateException:
        """

        :return:
        """
    @classmethod
    @property
    def Factory(cls) -> TaskFactory:
        """

        :return:
        """
    @property
    def Id(self) -> int:
        """

        :return:
        """
    @property
    def IsCanceled(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
        """

        :return:
        """
    @property
    def IsFaulted(self) -> bool:
        """

        :return:
        """
    @property
    def Status(self) -> TaskStatus:
        """

        :return:
        """
    def ConfigureAwait(self, continueOnCapturedContext: bool) -> ConfiguredTaskAwaitable:
        """

        :param continueOnCapturedContext:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task]) -> Task:
        """

        :param continuationAction:
        :return:
        """
    @overload
    def ContinueWith(self, continuationFunction: Func[Task, TResult]) -> Task[TResult]:
        """

        :param continuationFunction:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task, object], state: object) -> Task:
        """

        :param continuationAction:
        :param state:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], continuationOptions: TaskContinuationOptions
    ) -> Task:
        """

        :param continuationAction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task], scheduler: TaskScheduler) -> Task:
        """

        :param continuationAction:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], cancellationToken: CancellationToken
    ) -> Task:
        """

        :param continuationAction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, TResult], scheduler: TaskScheduler
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, object, TResult], state: object
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task, object], state: object, scheduler: TaskScheduler
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param continuationAction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetAwaiter(self) -> TaskAwaiter:
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
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """

        :param tae:
        """
    @overload
    def RunSynchronously(self) -> None:
        """"""
    @overload
    def RunSynchronously(self, scheduler: TaskScheduler) -> None:
        """

        :param scheduler:
        """
    @overload
    def Start(self) -> None:
        """"""
    @overload
    def Start(self, scheduler: TaskScheduler) -> None:
        """

        :param scheduler:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Wait(self) -> None:
        """"""
    @overload
    def Wait(self, cancellationToken: CancellationToken) -> None:
        """

        :param cancellationToken:
        """
    @overload
    def Wait(self, millisecondsTimeout: int) -> bool:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def Wait(self, timeout: TimeSpan) -> bool:
        """

        :param timeout:
        :return:
        """
    @overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool:
        """

        :param millisecondsTimeout:
        :param cancellationToken:
        :return:
        """

class ParallelLoopResult(ValueType):
    """"""

    @property
    def IsCompleted(self) -> bool:
        """

        :return:
        """
    @property
    def LowestBreakIteration(self) -> Optional[int]:
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
    def ToString(self) -> str:
        """

        :return:
        """

class ParallelLoopState(Object):
    """"""

    @property
    def IsExceptional(self) -> bool:
        """

        :return:
        """
    @property
    def IsStopped(self) -> bool:
        """

        :return:
        """
    @property
    def LowestBreakIteration(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def ShouldExitCurrentIteration(self) -> bool:
        """

        :return:
        """
    def Break(self) -> None:
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
    def Stop(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class ParallelLoopState32(ParallelLoopState):
    """"""

    @property
    def IsExceptional(self) -> bool:
        """

        :return:
        """
    @property
    def IsStopped(self) -> bool:
        """

        :return:
        """
    @property
    def LowestBreakIteration(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def ShouldExitCurrentIteration(self) -> bool:
        """

        :return:
        """
    def Break(self) -> None:
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
    def Stop(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class ParallelLoopState64(ParallelLoopState):
    """"""

    @property
    def IsExceptional(self) -> bool:
        """

        :return:
        """
    @property
    def IsStopped(self) -> bool:
        """

        :return:
        """
    @property
    def LowestBreakIteration(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def ShouldExitCurrentIteration(self) -> bool:
        """

        :return:
        """
    def Break(self) -> None:
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
    def Stop(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class ParallelLoopStateFlags(Object):
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

class ParallelLoopStateFlags32(ParallelLoopStateFlags):
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

class ParallelLoopStateFlags64(ParallelLoopStateFlags):
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

class ParallelOptions(Object):
    """"""

    def __init__(self):
        """"""
    @property
    def CancellationToken(self) -> CancellationToken:
        """

        :return:
        """
    @CancellationToken.setter
    def CancellationToken(self, value: CancellationToken) -> None: ...
    @property
    def MaxDegreeOfParallelism(self) -> int:
        """

        :return:
        """
    @MaxDegreeOfParallelism.setter
    def MaxDegreeOfParallelism(self, value: int) -> None: ...
    @property
    def TaskScheduler(self) -> TaskScheduler:
        """

        :return:
        """
    @TaskScheduler.setter
    def TaskScheduler(self, value: TaskScheduler) -> None: ...
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

class RangeManager(Object):
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

class RangeWorker(ValueType):
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

class Shared(Generic[T], Object):
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

class SingleProducerSingleConsumerQueue(
    Generic[T], Object, IEnumerable[T], IEnumerable, IProducerConsumerQueue[T]
):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsEmpty(self) -> bool:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    def Enqueue(self, item: T) -> None:
        """

        :param item:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetCountSafe(self, syncObj: object) -> int:
        """

        :param syncObj:
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
    def ToString(self) -> str:
        """

        :return:
        """
    def TryDequeue(self, result: T) -> Tuple[bool, T]:
        """

        :param result:
        :return:
        """
    def TryDequeueIf(self, predicate: Predicate[T], result: T) -> Tuple[bool, T]:
        """

        :param predicate:
        :param result:
        :return:
        """
    def TryPeek(self, result: T) -> Tuple[bool, T]:
        """

        :param result:
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

class StackGuard(Object):
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

class StandardTaskContinuation(TaskContinuation):
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

class SynchronizationContextAwaitTaskContinuation(AwaitTaskContinuation, IThreadPoolWorkItem):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """

        :param tae:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SynchronizationContextTaskScheduler(TaskScheduler):
    """"""

    @classmethod
    @property
    def Current(cls) -> TaskScheduler:
        """

        :return:
        """
    @classmethod
    @property
    def Default(cls) -> TaskScheduler:
        """

        :return:
        """
    @property
    def Id(self) -> int:
        """

        :return:
        """
    @property
    def MaximumConcurrencyLevel(self) -> int:
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
    def ToString(self) -> str:
        """

        :return:
        """
    UnobservedTaskException: EventType[EventHandler[UnobservedTaskExceptionEventArgs]] = ...
    """"""

class SystemThreadingTasks_FutureDebugView(Generic[TResult], Object):
    """"""

    def __init__(self, task: Task[TResult]):
        """

        :param task:
        """
    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def CancellationPending(self) -> bool:
        """

        :return:
        """
    @property
    def CreationOptions(self) -> TaskCreationOptions:
        """

        :return:
        """
    @property
    def Exception(self) -> Exception:
        """

        :return:
        """
    @property
    def Id(self) -> int:
        """

        :return:
        """
    @property
    def Result(self) -> TResult:
        """

        :return:
        """
    @property
    def Status(self) -> TaskStatus:
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
    def ToString(self) -> str:
        """

        :return:
        """

class SystemThreadingTasks_TaskDebugView(Object):
    """"""

    def __init__(self, task: Task):
        """

        :param task:
        """
    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def CancellationPending(self) -> bool:
        """

        :return:
        """
    @property
    def CreationOptions(self) -> TaskCreationOptions:
        """

        :return:
        """
    @property
    def Exception(self) -> Exception:
        """

        :return:
        """
    @property
    def Id(self) -> int:
        """

        :return:
        """
    @property
    def Status(self) -> TaskStatus:
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
    def ToString(self) -> str:
        """

        :return:
        """

class Task(Object, IThreadPoolWorkItem, IAsyncResult, IDisposable):
    """"""

    @overload
    def __init__(self, action: Action):
        """

        :param action:
        """
    @overload
    def __init__(self, action: Action, creationOptions: TaskCreationOptions):
        """

        :param action:
        :param creationOptions:
        """
    @overload
    def __init__(self, action: Action, cancellationToken: CancellationToken):
        """

        :param action:
        :param cancellationToken:
        """
    @overload
    def __init__(self, action: Action[object], state: object):
        """

        :param action:
        :param state:
        """
    @overload
    def __init__(
        self,
        action: Action,
        cancellationToken: CancellationToken,
        creationOptions: TaskCreationOptions,
    ):
        """

        :param action:
        :param cancellationToken:
        :param creationOptions:
        """
    @overload
    def __init__(self, action: Action[object], state: object, creationOptions: TaskCreationOptions):
        """

        :param action:
        :param state:
        :param creationOptions:
        """
    @overload
    def __init__(self, action: Action[object], state: object, cancellationToken: CancellationToken):
        """

        :param action:
        :param state:
        :param cancellationToken:
        """
    @overload
    def __init__(
        self,
        action: Action[object],
        state: object,
        cancellationToken: CancellationToken,
        creationOptions: TaskCreationOptions,
    ):
        """

        :param action:
        :param state:
        :param cancellationToken:
        :param creationOptions:
        """
    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def CompletedTask(cls) -> Task:
        """

        :return:
        """
    @property
    def CreationOptions(self) -> TaskCreationOptions:
        """

        :return:
        """
    @classmethod
    @property
    def CurrentId(cls) -> Optional[int]:
        """

        :return:
        """
    @property
    def Exception(self) -> AggregateException:
        """

        :return:
        """
    @classmethod
    @property
    def Factory(cls) -> TaskFactory:
        """

        :return:
        """
    @property
    def Id(self) -> int:
        """

        :return:
        """
    @property
    def IsCanceled(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
        """

        :return:
        """
    @property
    def IsFaulted(self) -> bool:
        """

        :return:
        """
    @property
    def Status(self) -> TaskStatus:
        """

        :return:
        """
    def ConfigureAwait(self, continueOnCapturedContext: bool) -> ConfiguredTaskAwaitable:
        """

        :param continueOnCapturedContext:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task]) -> Task:
        """

        :param continuationAction:
        :return:
        """
    @overload
    def ContinueWith(self, continuationFunction: Func[Task, TResult]) -> Task[TResult]:
        """

        :param continuationFunction:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task, object], state: object) -> Task:
        """

        :param continuationAction:
        :param state:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], continuationOptions: TaskContinuationOptions
    ) -> Task:
        """

        :param continuationAction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task], scheduler: TaskScheduler) -> Task:
        """

        :param continuationAction:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], cancellationToken: CancellationToken
    ) -> Task:
        """

        :param continuationAction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, TResult], scheduler: TaskScheduler
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, object, TResult], state: object
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task, object], state: object, scheduler: TaskScheduler
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param continuationAction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @classmethod
    @overload
    def Delay(cls, millisecondsDelay: int) -> Task:
        """

        :param millisecondsDelay:
        :return:
        """
    @classmethod
    @overload
    def Delay(cls, delay: TimeSpan) -> Task:
        """

        :param delay:
        :return:
        """
    @classmethod
    @overload
    def Delay(cls, millisecondsDelay: int, cancellationToken: CancellationToken) -> Task:
        """

        :param millisecondsDelay:
        :param cancellationToken:
        :return:
        """
    @classmethod
    @overload
    def Delay(cls, delay: TimeSpan, cancellationToken: CancellationToken) -> Task:
        """

        :param delay:
        :param cancellationToken:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExecuteWorkItem(self) -> None:
        """"""
    @classmethod
    def FromCanceled(cls, cancellationToken: CancellationToken) -> Task[TResult]:
        """

        :param cancellationToken:
        :return:
        """
    @classmethod
    def FromException(cls, exception: Exception) -> Task[TResult]:
        """

        :param exception:
        :return:
        """
    @classmethod
    def FromResult(cls, result: TResult) -> Task[TResult]:
        """

        :param result:
        :return:
        """
    def GetAwaiter(self) -> TaskAwaiter:
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
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """

        :param tae:
        """
    @classmethod
    @overload
    def Run(cls, action: Action) -> Task:
        """

        :param action:
        :return:
        """
    @classmethod
    @overload
    def Run(cls, function: Func[TResult]) -> Task[TResult]:
        """

        :param function:
        :return:
        """
    @classmethod
    @overload
    def Run(cls, function: Func[Task[TResult]]) -> Task[TResult]:
        """

        :param function:
        :return:
        """
    @classmethod
    @overload
    def Run(cls, function: Func[Task]) -> Task:
        """

        :param function:
        :return:
        """
    @classmethod
    @overload
    def Run(cls, action: Action, cancellationToken: CancellationToken) -> Task:
        """

        :param action:
        :param cancellationToken:
        :return:
        """
    @classmethod
    @overload
    def Run(cls, function: Func[TResult], cancellationToken: CancellationToken) -> Task[TResult]:
        """

        :param function:
        :param cancellationToken:
        :return:
        """
    @classmethod
    @overload
    def Run(
        cls, function: Func[Task[TResult]], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """

        :param function:
        :param cancellationToken:
        :return:
        """
    @classmethod
    @overload
    def Run(cls, function: Func[Task], cancellationToken: CancellationToken) -> Task:
        """

        :param function:
        :param cancellationToken:
        :return:
        """
    @overload
    def RunSynchronously(self) -> None:
        """"""
    @overload
    def RunSynchronously(self, scheduler: TaskScheduler) -> None:
        """

        :param scheduler:
        """
    @overload
    def Start(self) -> None:
        """"""
    @overload
    def Start(self, scheduler: TaskScheduler) -> None:
        """

        :param scheduler:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Wait(self) -> None:
        """"""
    @overload
    def Wait(self, cancellationToken: CancellationToken) -> None:
        """

        :param cancellationToken:
        """
    @overload
    def Wait(self, millisecondsTimeout: int) -> bool:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def Wait(self, timeout: TimeSpan) -> bool:
        """

        :param timeout:
        :return:
        """
    @overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool:
        """

        :param millisecondsTimeout:
        :param cancellationToken:
        :return:
        """
    @classmethod
    @overload
    def WaitAll(cls, tasks: Array[Task]) -> None:
        """

        :param tasks:
        """
    @classmethod
    @overload
    def WaitAll(cls, tasks: Array[Task], cancellationToken: CancellationToken) -> None:
        """

        :param tasks:
        :param cancellationToken:
        """
    @classmethod
    @overload
    def WaitAll(cls, tasks: Array[Task], millisecondsTimeout: int) -> bool:
        """

        :param tasks:
        :param millisecondsTimeout:
        :return:
        """
    @classmethod
    @overload
    def WaitAll(cls, tasks: Array[Task], timeout: TimeSpan) -> bool:
        """

        :param tasks:
        :param timeout:
        :return:
        """
    @classmethod
    @overload
    def WaitAll(
        cls, tasks: Array[Task], millisecondsTimeout: int, cancellationToken: CancellationToken
    ) -> bool:
        """

        :param tasks:
        :param millisecondsTimeout:
        :param cancellationToken:
        :return:
        """
    @classmethod
    @overload
    def WaitAny(cls, tasks: Array[Task]) -> int:
        """

        :param tasks:
        :return:
        """
    @classmethod
    @overload
    def WaitAny(cls, tasks: Array[Task], cancellationToken: CancellationToken) -> int:
        """

        :param tasks:
        :param cancellationToken:
        :return:
        """
    @classmethod
    @overload
    def WaitAny(cls, tasks: Array[Task], millisecondsTimeout: int) -> int:
        """

        :param tasks:
        :param millisecondsTimeout:
        :return:
        """
    @classmethod
    @overload
    def WaitAny(cls, tasks: Array[Task], timeout: TimeSpan) -> int:
        """

        :param tasks:
        :param timeout:
        :return:
        """
    @classmethod
    @overload
    def WaitAny(
        cls, tasks: Array[Task], millisecondsTimeout: int, cancellationToken: CancellationToken
    ) -> int:
        """

        :param tasks:
        :param millisecondsTimeout:
        :param cancellationToken:
        :return:
        """
    @classmethod
    @overload
    def WhenAll(cls, tasks: IEnumerable[Task[TResult]]) -> Task[Array[TResult]]:
        """

        :param tasks:
        :return:
        """
    @classmethod
    @overload
    def WhenAll(cls, tasks: IEnumerable[Task]) -> Task:
        """

        :param tasks:
        :return:
        """
    @classmethod
    @overload
    def WhenAll(cls, tasks: Array[Task[TResult]]) -> Task[Array[TResult]]:
        """

        :param tasks:
        :return:
        """
    @classmethod
    @overload
    def WhenAll(cls, tasks: Array[Task]) -> Task:
        """

        :param tasks:
        :return:
        """
    @classmethod
    @overload
    def WhenAny(cls, tasks: IEnumerable[Task[TResult]]) -> Task[Task[TResult]]:
        """

        :param tasks:
        :return:
        """
    @classmethod
    @overload
    def WhenAny(cls, tasks: IEnumerable[Task]) -> Task[Task]:
        """

        :param tasks:
        :return:
        """
    @classmethod
    @overload
    def WhenAny(cls, tasks: Array[Task[TResult]]) -> Task[Task[TResult]]:
        """

        :param tasks:
        :return:
        """
    @classmethod
    @overload
    def WhenAny(cls, tasks: Array[Task]) -> Task[Task]:
        """

        :param tasks:
        :return:
        """
    @classmethod
    def Yield(cls) -> YieldAwaitable:
        """

        :return:
        """

class TaskCanceledException(OperationCanceledException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, task: Task):
        """

        :param task:
        """
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, message: str, innerException: Exception):
        """

        :param message:
        :param innerException:
        """
    @property
    def CancellationToken(self) -> CancellationToken:
        """

        :return:
        """
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
    def Task(self) -> Task:
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

class TaskCompletionSource(Generic[TResult], Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, creationOptions: TaskCreationOptions):
        """

        :param creationOptions:
        """
    @overload
    def __init__(self, state: object):
        """

        :param state:
        """
    @overload
    def __init__(self, state: object, creationOptions: TaskCreationOptions):
        """

        :param state:
        :param creationOptions:
        """
    @property
    def Task(self) -> Task[TResult]:
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
    def SetCanceled(self) -> None:
        """"""
    @overload
    def SetException(self, exceptions: IEnumerable[Exception]) -> None:
        """

        :param exceptions:
        """
    @overload
    def SetException(self, exception: Exception) -> None:
        """

        :param exception:
        """
    def SetResult(self, result: TResult) -> None:
        """

        :param result:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def TrySetCanceled(self) -> bool:
        """

        :return:
        """
    @overload
    def TrySetCanceled(self, cancellationToken: CancellationToken) -> bool:
        """

        :param cancellationToken:
        :return:
        """
    @overload
    def TrySetException(self, exceptions: IEnumerable[Exception]) -> bool:
        """

        :param exceptions:
        :return:
        """
    @overload
    def TrySetException(self, exception: Exception) -> bool:
        """

        :param exception:
        :return:
        """
    def TrySetResult(self, result: TResult) -> bool:
        """

        :param result:
        :return:
        """

class TaskContinuation(ABC, Object):
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

class TaskExtensions(ABC, Object):
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
    @classmethod
    @overload
    def Unwrap(cls, task: Task[Task[TResult]]) -> Task[TResult]:
        """

        :param task:
        :return:
        """
    @classmethod
    @overload
    def Unwrap(cls, task: Task[Task]) -> Task:
        """

        :param task:
        :return:
        """

class TaskFactory(Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, scheduler: TaskScheduler):
        """

        :param scheduler:
        """
    @overload
    def __init__(self, cancellationToken: CancellationToken):
        """

        :param cancellationToken:
        """
    @overload
    def __init__(
        self, creationOptions: TaskCreationOptions, continuationOptions: TaskContinuationOptions
    ):
        """

        :param creationOptions:
        :param continuationOptions:
        """
    @overload
    def __init__(
        self,
        cancellationToken: CancellationToken,
        creationOptions: TaskCreationOptions,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ):
        """

        :param cancellationToken:
        :param creationOptions:
        :param continuationOptions:
        :param scheduler:
        """
    @property
    def CancellationToken(self) -> CancellationToken:
        """

        :return:
        """
    @property
    def ContinuationOptions(self) -> TaskContinuationOptions:
        """

        :return:
        """
    @property
    def CreationOptions(self) -> TaskCreationOptions:
        """

        :return:
        """
    @property
    def Scheduler(self) -> TaskScheduler:
        """

        :return:
        """
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationAction: Action[Array[Task[TAntecedentResult]]],
    ) -> Task:
        """

        :param tasks:
        :param continuationAction:
        :return:
        """
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Array[Task[TAntecedentResult]], TResult],
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :return:
        """
    @overload
    def ContinueWhenAll(self, tasks: Array[Task], continuationAction: Action[Array[Task]]) -> Task:
        """

        :param tasks:
        :param continuationAction:
        :return:
        """
    @overload
    def ContinueWhenAll(
        self, tasks: Array[Task], continuationFunction: Func[Array[Task], TResult]
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :return:
        """
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationAction: Action[Array[Task[TAntecedentResult]]],
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """

        :param tasks:
        :param continuationAction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationAction: Action[Array[Task[TAntecedentResult]]],
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param tasks:
        :param continuationAction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Array[Task[TAntecedentResult]], TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Array[Task[TAntecedentResult]], TResult],
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task],
        continuationAction: Action[Array[Task]],
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """

        :param tasks:
        :param continuationAction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task],
        continuationAction: Action[Array[Task]],
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param tasks:
        :param continuationAction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task],
        continuationFunction: Func[Array[Task], TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task],
        continuationFunction: Func[Array[Task], TResult],
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationAction: Action[Array[Task[TAntecedentResult]]],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param tasks:
        :param continuationAction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Array[Task[TAntecedentResult]], TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task],
        continuationAction: Action[Array[Task]],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param tasks:
        :param continuationAction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task],
        continuationFunction: Func[Array[Task], TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationAction: Action[Task[TAntecedentResult]],
    ) -> Task:
        """

        :param tasks:
        :param continuationAction:
        :return:
        """
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Task[TAntecedentResult], TResult],
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :return:
        """
    @overload
    def ContinueWhenAny(self, tasks: Array[Task], continuationAction: Action[Task]) -> Task:
        """

        :param tasks:
        :param continuationAction:
        :return:
        """
    @overload
    def ContinueWhenAny(
        self, tasks: Array[Task], continuationFunction: Func[Task, TResult]
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :return:
        """
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationAction: Action[Task[TAntecedentResult]],
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """

        :param tasks:
        :param continuationAction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationAction: Action[Task[TAntecedentResult]],
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param tasks:
        :param continuationAction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Task[TAntecedentResult], TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Task[TAntecedentResult], TResult],
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task],
        continuationAction: Action[Task],
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """

        :param tasks:
        :param continuationAction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task],
        continuationAction: Action[Task],
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param tasks:
        :param continuationAction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task],
        continuationFunction: Func[Task, TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task],
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationAction: Action[Task[TAntecedentResult]],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param tasks:
        :param continuationAction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Task[TAntecedentResult], TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task],
        continuationAction: Action[Task],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param tasks:
        :param continuationAction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task],
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def FromAsync(self, asyncResult: IAsyncResult, endMethod: Action[IAsyncResult]) -> Task:
        """

        :param asyncResult:
        :param endMethod:
        :return:
        """
    @overload
    def FromAsync(
        self, asyncResult: IAsyncResult, endMethod: Func[IAsyncResult, TResult]
    ) -> Task[TResult]:
        """

        :param asyncResult:
        :param endMethod:
        :return:
        """
    @overload
    def FromAsync(
        self,
        beginMethod: Func[AsyncCallback, object, IAsyncResult],
        endMethod: Action[IAsyncResult],
        state: object,
    ) -> Task:
        """

        :param beginMethod:
        :param endMethod:
        :param state:
        :return:
        """
    @overload
    def FromAsync(
        self,
        beginMethod: Func[AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        state: object,
    ) -> Task[TResult]:
        """

        :param beginMethod:
        :param endMethod:
        :param state:
        :return:
        """
    @overload
    def FromAsync(
        self,
        asyncResult: IAsyncResult,
        endMethod: Action[IAsyncResult],
        creationOptions: TaskCreationOptions,
    ) -> Task:
        """

        :param asyncResult:
        :param endMethod:
        :param creationOptions:
        :return:
        """
    @overload
    def FromAsync(
        self,
        asyncResult: IAsyncResult,
        endMethod: Func[IAsyncResult, TResult],
        creationOptions: TaskCreationOptions,
    ) -> Task[TResult]:
        """

        :param asyncResult:
        :param endMethod:
        :param creationOptions:
        :return:
        """
    @overload
    def FromAsync(
        self,
        beginMethod: Func[TArg1, AsyncCallback, object, IAsyncResult],
        endMethod: Action[IAsyncResult],
        arg1: TArg1,
        state: object,
    ) -> Task:
        """

        :param beginMethod:
        :param endMethod:
        :param arg1:
        :param state:
        :return:
        """
    @overload
    def FromAsync(
        self,
        beginMethod: Func[TArg1, AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        arg1: TArg1,
        state: object,
    ) -> Task[TResult]:
        """

        :param beginMethod:
        :param endMethod:
        :param arg1:
        :param state:
        :return:
        """
    @overload
    def FromAsync(
        self,
        beginMethod: Func[AsyncCallback, object, IAsyncResult],
        endMethod: Action[IAsyncResult],
        state: object,
        creationOptions: TaskCreationOptions,
    ) -> Task:
        """

        :param beginMethod:
        :param endMethod:
        :param state:
        :param creationOptions:
        :return:
        """
    @overload
    def FromAsync(
        self,
        beginMethod: Func[AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        state: object,
        creationOptions: TaskCreationOptions,
    ) -> Task[TResult]:
        """

        :param beginMethod:
        :param endMethod:
        :param state:
        :param creationOptions:
        :return:
        """
    @overload
    def FromAsync(
        self,
        asyncResult: IAsyncResult,
        endMethod: Action[IAsyncResult],
        creationOptions: TaskCreationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param asyncResult:
        :param endMethod:
        :param creationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def FromAsync(
        self,
        asyncResult: IAsyncResult,
        endMethod: Func[IAsyncResult, TResult],
        creationOptions: TaskCreationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param asyncResult:
        :param endMethod:
        :param creationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def FromAsync(
        self,
        beginMethod: Func[TArg1, TArg2, AsyncCallback, object, IAsyncResult],
        endMethod: Action[IAsyncResult],
        arg1: TArg1,
        arg2: TArg2,
        state: object,
    ) -> Task:
        """

        :param beginMethod:
        :param endMethod:
        :param arg1:
        :param arg2:
        :param state:
        :return:
        """
    @overload
    def FromAsync(
        self,
        beginMethod: Func[TArg1, TArg2, AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        arg1: TArg1,
        arg2: TArg2,
        state: object,
    ) -> Task[TResult]:
        """

        :param beginMethod:
        :param endMethod:
        :param arg1:
        :param arg2:
        :param state:
        :return:
        """
    @overload
    def FromAsync(
        self,
        beginMethod: Func[TArg1, AsyncCallback, object, IAsyncResult],
        endMethod: Action[IAsyncResult],
        arg1: TArg1,
        state: object,
        creationOptions: TaskCreationOptions,
    ) -> Task:
        """

        :param beginMethod:
        :param endMethod:
        :param arg1:
        :param state:
        :param creationOptions:
        :return:
        """
    @overload
    def FromAsync(
        self,
        beginMethod: Func[TArg1, AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        arg1: TArg1,
        state: object,
        creationOptions: TaskCreationOptions,
    ) -> Task[TResult]:
        """

        :param beginMethod:
        :param endMethod:
        :param arg1:
        :param state:
        :param creationOptions:
        :return:
        """
    @overload
    def FromAsync(
        self,
        beginMethod: Func[TArg1, TArg2, TArg3, AsyncCallback, object, IAsyncResult],
        endMethod: Action[IAsyncResult],
        arg1: TArg1,
        arg2: TArg2,
        arg3: TArg3,
        state: object,
    ) -> Task:
        """

        :param beginMethod:
        :param endMethod:
        :param arg1:
        :param arg2:
        :param arg3:
        :param state:
        :return:
        """
    @overload
    def FromAsync(
        self,
        beginMethod: Func[TArg1, TArg2, TArg3, AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        arg1: TArg1,
        arg2: TArg2,
        arg3: TArg3,
        state: object,
    ) -> Task[TResult]:
        """

        :param beginMethod:
        :param endMethod:
        :param arg1:
        :param arg2:
        :param arg3:
        :param state:
        :return:
        """
    @overload
    def FromAsync(
        self,
        beginMethod: Func[TArg1, TArg2, AsyncCallback, object, IAsyncResult],
        endMethod: Action[IAsyncResult],
        arg1: TArg1,
        arg2: TArg2,
        state: object,
        creationOptions: TaskCreationOptions,
    ) -> Task:
        """

        :param beginMethod:
        :param endMethod:
        :param arg1:
        :param arg2:
        :param state:
        :param creationOptions:
        :return:
        """
    @overload
    def FromAsync(
        self,
        beginMethod: Func[TArg1, TArg2, AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        arg1: TArg1,
        arg2: TArg2,
        state: object,
        creationOptions: TaskCreationOptions,
    ) -> Task[TResult]:
        """

        :param beginMethod:
        :param endMethod:
        :param arg1:
        :param arg2:
        :param state:
        :param creationOptions:
        :return:
        """
    @overload
    def FromAsync(
        self,
        beginMethod: Func[TArg1, TArg2, TArg3, AsyncCallback, object, IAsyncResult],
        endMethod: Action[IAsyncResult],
        arg1: TArg1,
        arg2: TArg2,
        arg3: TArg3,
        state: object,
        creationOptions: TaskCreationOptions,
    ) -> Task:
        """

        :param beginMethod:
        :param endMethod:
        :param arg1:
        :param arg2:
        :param arg3:
        :param state:
        :param creationOptions:
        :return:
        """
    @overload
    def FromAsync(
        self,
        beginMethod: Func[TArg1, TArg2, TArg3, AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        arg1: TArg1,
        arg2: TArg2,
        arg3: TArg3,
        state: object,
        creationOptions: TaskCreationOptions,
    ) -> Task[TResult]:
        """

        :param beginMethod:
        :param endMethod:
        :param arg1:
        :param arg2:
        :param arg3:
        :param state:
        :param creationOptions:
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
    def StartNew(self, action: Action) -> Task:
        """

        :param action:
        :return:
        """
    @overload
    def StartNew(self, function: Func[TResult]) -> Task[TResult]:
        """

        :param function:
        :return:
        """
    @overload
    def StartNew(self, action: Action, creationOptions: TaskCreationOptions) -> Task:
        """

        :param action:
        :param creationOptions:
        :return:
        """
    @overload
    def StartNew(self, action: Action, cancellationToken: CancellationToken) -> Task:
        """

        :param action:
        :param cancellationToken:
        :return:
        """
    @overload
    def StartNew(self, action: Action[object], state: object) -> Task:
        """

        :param action:
        :param state:
        :return:
        """
    @overload
    def StartNew(
        self, function: Func[TResult], creationOptions: TaskCreationOptions
    ) -> Task[TResult]:
        """

        :param function:
        :param creationOptions:
        :return:
        """
    @overload
    def StartNew(
        self, function: Func[TResult], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """

        :param function:
        :param cancellationToken:
        :return:
        """
    @overload
    def StartNew(self, function: Func[object, TResult], state: object) -> Task[TResult]:
        """

        :param function:
        :param state:
        :return:
        """
    @overload
    def StartNew(
        self, action: Action[object], state: object, creationOptions: TaskCreationOptions
    ) -> Task:
        """

        :param action:
        :param state:
        :param creationOptions:
        :return:
        """
    @overload
    def StartNew(
        self, action: Action[object], state: object, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param action:
        :param state:
        :param cancellationToken:
        :return:
        """
    @overload
    def StartNew(
        self, function: Func[object, TResult], state: object, creationOptions: TaskCreationOptions
    ) -> Task[TResult]:
        """

        :param function:
        :param state:
        :param creationOptions:
        :return:
        """
    @overload
    def StartNew(
        self, function: Func[object, TResult], state: object, cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """

        :param function:
        :param state:
        :param cancellationToken:
        :return:
        """
    @overload
    def StartNew(
        self,
        action: Action,
        cancellationToken: CancellationToken,
        creationOptions: TaskCreationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param action:
        :param cancellationToken:
        :param creationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def StartNew(
        self,
        function: Func[TResult],
        cancellationToken: CancellationToken,
        creationOptions: TaskCreationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param function:
        :param cancellationToken:
        :param creationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def StartNew(
        self,
        action: Action[object],
        state: object,
        cancellationToken: CancellationToken,
        creationOptions: TaskCreationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param action:
        :param state:
        :param cancellationToken:
        :param creationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def StartNew(
        self,
        function: Func[object, TResult],
        state: object,
        cancellationToken: CancellationToken,
        creationOptions: TaskCreationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param function:
        :param state:
        :param cancellationToken:
        :param creationOptions:
        :param scheduler:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class TaskFactory(Generic[TResult], Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, scheduler: TaskScheduler):
        """

        :param scheduler:
        """
    @overload
    def __init__(self, cancellationToken: CancellationToken):
        """

        :param cancellationToken:
        """
    @overload
    def __init__(
        self, creationOptions: TaskCreationOptions, continuationOptions: TaskContinuationOptions
    ):
        """

        :param creationOptions:
        :param continuationOptions:
        """
    @overload
    def __init__(
        self,
        cancellationToken: CancellationToken,
        creationOptions: TaskCreationOptions,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ):
        """

        :param cancellationToken:
        :param creationOptions:
        :param continuationOptions:
        :param scheduler:
        """
    @property
    def CancellationToken(self) -> CancellationToken:
        """

        :return:
        """
    @property
    def ContinuationOptions(self) -> TaskContinuationOptions:
        """

        :return:
        """
    @property
    def CreationOptions(self) -> TaskCreationOptions:
        """

        :return:
        """
    @property
    def Scheduler(self) -> TaskScheduler:
        """

        :return:
        """
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Array[Task[TAntecedentResult]], TResult],
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :return:
        """
    @overload
    def ContinueWhenAll(
        self, tasks: Array[Task], continuationFunction: Func[Array[Task], TResult]
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :return:
        """
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Array[Task[TAntecedentResult]], TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Array[Task[TAntecedentResult]], TResult],
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task],
        continuationFunction: Func[Array[Task], TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task],
        continuationFunction: Func[Array[Task], TResult],
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Array[Task[TAntecedentResult]], TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWhenAll(
        self,
        tasks: Array[Task],
        continuationFunction: Func[Array[Task], TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Task[TAntecedentResult], TResult],
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :return:
        """
    @overload
    def ContinueWhenAny(
        self, tasks: Array[Task], continuationFunction: Func[Task, TResult]
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :return:
        """
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Task[TAntecedentResult], TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Task[TAntecedentResult], TResult],
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task],
        continuationFunction: Func[Task, TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task],
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task[TAntecedentResult]],
        continuationFunction: Func[Task[TAntecedentResult], TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWhenAny(
        self,
        tasks: Array[Task],
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param tasks:
        :param continuationFunction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def FromAsync(
        self, asyncResult: IAsyncResult, endMethod: Func[IAsyncResult, TResult]
    ) -> Task[TResult]:
        """

        :param asyncResult:
        :param endMethod:
        :return:
        """
    @overload
    def FromAsync(
        self,
        beginMethod: Func[AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        state: object,
    ) -> Task[TResult]:
        """

        :param beginMethod:
        :param endMethod:
        :param state:
        :return:
        """
    @overload
    def FromAsync(
        self,
        asyncResult: IAsyncResult,
        endMethod: Func[IAsyncResult, TResult],
        creationOptions: TaskCreationOptions,
    ) -> Task[TResult]:
        """

        :param asyncResult:
        :param endMethod:
        :param creationOptions:
        :return:
        """
    @overload
    def FromAsync(
        self,
        beginMethod: Func[TArg1, AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        arg1: TArg1,
        state: object,
    ) -> Task[TResult]:
        """

        :param beginMethod:
        :param endMethod:
        :param arg1:
        :param state:
        :return:
        """
    @overload
    def FromAsync(
        self,
        beginMethod: Func[AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        state: object,
        creationOptions: TaskCreationOptions,
    ) -> Task[TResult]:
        """

        :param beginMethod:
        :param endMethod:
        :param state:
        :param creationOptions:
        :return:
        """
    @overload
    def FromAsync(
        self,
        asyncResult: IAsyncResult,
        endMethod: Func[IAsyncResult, TResult],
        creationOptions: TaskCreationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param asyncResult:
        :param endMethod:
        :param creationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def FromAsync(
        self,
        beginMethod: Func[TArg1, TArg2, AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        arg1: TArg1,
        arg2: TArg2,
        state: object,
    ) -> Task[TResult]:
        """

        :param beginMethod:
        :param endMethod:
        :param arg1:
        :param arg2:
        :param state:
        :return:
        """
    @overload
    def FromAsync(
        self,
        beginMethod: Func[TArg1, AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        arg1: TArg1,
        state: object,
        creationOptions: TaskCreationOptions,
    ) -> Task[TResult]:
        """

        :param beginMethod:
        :param endMethod:
        :param arg1:
        :param state:
        :param creationOptions:
        :return:
        """
    @overload
    def FromAsync(
        self,
        beginMethod: Func[TArg1, TArg2, TArg3, AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        arg1: TArg1,
        arg2: TArg2,
        arg3: TArg3,
        state: object,
    ) -> Task[TResult]:
        """

        :param beginMethod:
        :param endMethod:
        :param arg1:
        :param arg2:
        :param arg3:
        :param state:
        :return:
        """
    @overload
    def FromAsync(
        self,
        beginMethod: Func[TArg1, TArg2, AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        arg1: TArg1,
        arg2: TArg2,
        state: object,
        creationOptions: TaskCreationOptions,
    ) -> Task[TResult]:
        """

        :param beginMethod:
        :param endMethod:
        :param arg1:
        :param arg2:
        :param state:
        :param creationOptions:
        :return:
        """
    @overload
    def FromAsync(
        self,
        beginMethod: Func[TArg1, TArg2, TArg3, AsyncCallback, object, IAsyncResult],
        endMethod: Func[IAsyncResult, TResult],
        arg1: TArg1,
        arg2: TArg2,
        arg3: TArg3,
        state: object,
        creationOptions: TaskCreationOptions,
    ) -> Task[TResult]:
        """

        :param beginMethod:
        :param endMethod:
        :param arg1:
        :param arg2:
        :param arg3:
        :param state:
        :param creationOptions:
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
    def StartNew(self, function: Func[TResult]) -> Task[TResult]:
        """

        :param function:
        :return:
        """
    @overload
    def StartNew(
        self, function: Func[TResult], creationOptions: TaskCreationOptions
    ) -> Task[TResult]:
        """

        :param function:
        :param creationOptions:
        :return:
        """
    @overload
    def StartNew(
        self, function: Func[TResult], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """

        :param function:
        :param cancellationToken:
        :return:
        """
    @overload
    def StartNew(self, function: Func[object, TResult], state: object) -> Task[TResult]:
        """

        :param function:
        :param state:
        :return:
        """
    @overload
    def StartNew(
        self, function: Func[object, TResult], state: object, creationOptions: TaskCreationOptions
    ) -> Task[TResult]:
        """

        :param function:
        :param state:
        :param creationOptions:
        :return:
        """
    @overload
    def StartNew(
        self, function: Func[object, TResult], state: object, cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """

        :param function:
        :param state:
        :param cancellationToken:
        :return:
        """
    @overload
    def StartNew(
        self,
        function: Func[TResult],
        cancellationToken: CancellationToken,
        creationOptions: TaskCreationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param function:
        :param cancellationToken:
        :param creationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def StartNew(
        self,
        function: Func[object, TResult],
        state: object,
        cancellationToken: CancellationToken,
        creationOptions: TaskCreationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param function:
        :param state:
        :param cancellationToken:
        :param creationOptions:
        :param scheduler:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class TaskScheduler(ABC, Object):
    """"""

    @classmethod
    @property
    def Current(cls) -> TaskScheduler:
        """

        :return:
        """
    @classmethod
    @property
    def Default(cls) -> TaskScheduler:
        """

        :return:
        """
    @property
    def Id(self) -> int:
        """

        :return:
        """
    @property
    def MaximumConcurrencyLevel(self) -> int:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def FromCurrentSynchronizationContext(cls) -> TaskScheduler:
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
    UnobservedTaskException: EventType[EventHandler[UnobservedTaskExceptionEventArgs]] = ...
    """"""

class TaskSchedulerAwaitTaskContinuation(AwaitTaskContinuation, IThreadPoolWorkItem):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """

        :param tae:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class TaskSchedulerException(Exception, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, innerException: Exception):
        """

        :param innerException:
        """
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, message: str, innerException: Exception):
        """

        :param message:
        :param innerException:
        """
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
        """

        :param task:
        :param callback:
        :param state:
        :return:
        """
    @classmethod
    def End(cls, asyncResult: IAsyncResult) -> TResult:
        """

        :param asyncResult:
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

class Task(Generic[TResult], Task, IThreadPoolWorkItem, IAsyncResult, IDisposable):
    """"""

    @overload
    def __init__(self, function: Func[TResult]):
        """

        :param function:
        """
    @overload
    def __init__(self, function: Func[TResult], creationOptions: TaskCreationOptions):
        """

        :param function:
        :param creationOptions:
        """
    @overload
    def __init__(self, function: Func[TResult], cancellationToken: CancellationToken):
        """

        :param function:
        :param cancellationToken:
        """
    @overload
    def __init__(self, function: Func[object, TResult], state: object):
        """

        :param function:
        :param state:
        """
    @overload
    def __init__(
        self,
        function: Func[TResult],
        cancellationToken: CancellationToken,
        creationOptions: TaskCreationOptions,
    ):
        """

        :param function:
        :param cancellationToken:
        :param creationOptions:
        """
    @overload
    def __init__(
        self, function: Func[object, TResult], state: object, creationOptions: TaskCreationOptions
    ):
        """

        :param function:
        :param state:
        :param creationOptions:
        """
    @overload
    def __init__(
        self, function: Func[object, TResult], state: object, cancellationToken: CancellationToken
    ):
        """

        :param function:
        :param state:
        :param cancellationToken:
        """
    @overload
    def __init__(
        self,
        function: Func[object, TResult],
        state: object,
        cancellationToken: CancellationToken,
        creationOptions: TaskCreationOptions,
    ):
        """

        :param function:
        :param state:
        :param cancellationToken:
        :param creationOptions:
        """
    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def CompletedTask(cls) -> Task:
        """

        :return:
        """
    @property
    def CreationOptions(self) -> TaskCreationOptions:
        """

        :return:
        """
    @classmethod
    @property
    def CurrentId(cls) -> Optional[int]:
        """

        :return:
        """
    @property
    def Exception(self) -> AggregateException:
        """

        :return:
        """
    @classmethod
    @property
    def Factory(cls) -> TaskFactory:
        """

        :return:
        """
    @property
    def Id(self) -> int:
        """

        :return:
        """
    @property
    def IsCanceled(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
        """

        :return:
        """
    @property
    def IsFaulted(self) -> bool:
        """

        :return:
        """
    @property
    def Result(self) -> TResult:
        """

        :return:
        """
    @property
    def Status(self) -> TaskStatus:
        """

        :return:
        """
    def ConfigureAwait(self, continueOnCapturedContext: bool) -> ConfiguredTaskAwaitable:
        """

        :param continueOnCapturedContext:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task]) -> Task:
        """

        :param continuationAction:
        :return:
        """
    @overload
    def ContinueWith(self, continuationFunction: Func[Task, TResult]) -> Task[TResult]:
        """

        :param continuationFunction:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task, object], state: object) -> Task:
        """

        :param continuationAction:
        :param state:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], continuationOptions: TaskContinuationOptions
    ) -> Task:
        """

        :param continuationAction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task], scheduler: TaskScheduler) -> Task:
        """

        :param continuationAction:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], cancellationToken: CancellationToken
    ) -> Task:
        """

        :param continuationAction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, TResult], scheduler: TaskScheduler
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, object, TResult], state: object
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task, object], state: object, scheduler: TaskScheduler
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param continuationAction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetAwaiter(self) -> TaskAwaiter:
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
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """

        :param tae:
        """
    @overload
    def RunSynchronously(self) -> None:
        """"""
    @overload
    def RunSynchronously(self, scheduler: TaskScheduler) -> None:
        """

        :param scheduler:
        """
    @overload
    def Start(self) -> None:
        """"""
    @overload
    def Start(self, scheduler: TaskScheduler) -> None:
        """

        :param scheduler:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Wait(self) -> None:
        """"""
    @overload
    def Wait(self, cancellationToken: CancellationToken) -> None:
        """

        :param cancellationToken:
        """
    @overload
    def Wait(self, millisecondsTimeout: int) -> bool:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def Wait(self, timeout: TimeSpan) -> bool:
        """

        :param timeout:
        :return:
        """
    @overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool:
        """

        :param millisecondsTimeout:
        :param cancellationToken:
        :return:
        """

class ThreadPoolTaskScheduler(TaskScheduler):
    """"""

    @classmethod
    @property
    def Current(cls) -> TaskScheduler:
        """

        :return:
        """
    @classmethod
    @property
    def Default(cls) -> TaskScheduler:
        """

        :return:
        """
    @property
    def Id(self) -> int:
        """

        :return:
        """
    @property
    def MaximumConcurrencyLevel(self) -> int:
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
    def ToString(self) -> str:
        """

        :return:
        """
    UnobservedTaskException: EventType[EventHandler[UnobservedTaskExceptionEventArgs]] = ...
    """"""

class TplEtwProvider(EventSource, IDisposable):
    """"""

    Log: Final[ClassVar[TplEtwProvider]] = ...
    """
    
    :return: 
    """
    @property
    def ConstructionException(self) -> Exception:
        """

        :return:
        """
    @classmethod
    @property
    def CurrentThreadActivityId(cls) -> Guid:
        """

        :return:
        """
    @property
    def Guid(self) -> Guid:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Settings(self) -> EventSourceSettings:
        """

        :return:
        """
    def AwaitTaskContinuationScheduled(
        self, OriginatingTaskSchedulerID: int, OriginatingTaskID: int, ContinuwWithTaskId: int
    ) -> None:
        """

        :param OriginatingTaskSchedulerID:
        :param OriginatingTaskID:
        :param ContinuwWithTaskId:
        """
    def DebugFacilityMessage(self, Facility: str, Message: str) -> None:
        """

        :param Facility:
        :param Message:
        """
    def DebugFacilityMessage1(self, Facility: str, Message: str, Value1: str) -> None:
        """

        :param Facility:
        :param Message:
        :param Value1:
        """
    def DebugMessage(self, Message: str) -> None:
        """

        :param Message:
        """
    def Dispose(self) -> None:
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
    def GetTrait(self, key: str) -> str:
        """

        :param key:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsEnabled(self) -> bool:
        """

        :return:
        """
    @overload
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords) -> bool:
        """

        :param level:
        :param keywords:
        :return:
        """
    @overload
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords, channel: EventChannel) -> bool:
        """

        :param level:
        :param keywords:
        :param channel:
        :return:
        """
    def NewID(self, TaskID: int) -> None:
        """

        :param TaskID:
        """
    def ParallelFork(
        self, OriginatingTaskSchedulerID: int, OriginatingTaskID: int, ForkJoinContextID: int
    ) -> None:
        """

        :param OriginatingTaskSchedulerID:
        :param OriginatingTaskID:
        :param ForkJoinContextID:
        """
    def ParallelInvokeBegin(
        self,
        OriginatingTaskSchedulerID: int,
        OriginatingTaskID: int,
        ForkJoinContextID: int,
        OperationType: TplEtwProvider.ForkJoinOperationType,
        ActionCount: int,
    ) -> None:
        """

        :param OriginatingTaskSchedulerID:
        :param OriginatingTaskID:
        :param ForkJoinContextID:
        :param OperationType:
        :param ActionCount:
        """
    def ParallelInvokeEnd(
        self, OriginatingTaskSchedulerID: int, OriginatingTaskID: int, ForkJoinContextID: int
    ) -> None:
        """

        :param OriginatingTaskSchedulerID:
        :param OriginatingTaskID:
        :param ForkJoinContextID:
        """
    def ParallelJoin(
        self, OriginatingTaskSchedulerID: int, OriginatingTaskID: int, ForkJoinContextID: int
    ) -> None:
        """

        :param OriginatingTaskSchedulerID:
        :param OriginatingTaskID:
        :param ForkJoinContextID:
        """
    def ParallelLoopBegin(
        self,
        OriginatingTaskSchedulerID: int,
        OriginatingTaskID: int,
        ForkJoinContextID: int,
        OperationType: TplEtwProvider.ForkJoinOperationType,
        InclusiveFrom: int,
        ExclusiveTo: int,
    ) -> None:
        """

        :param OriginatingTaskSchedulerID:
        :param OriginatingTaskID:
        :param ForkJoinContextID:
        :param OperationType:
        :param InclusiveFrom:
        :param ExclusiveTo:
        """
    def ParallelLoopEnd(
        self,
        OriginatingTaskSchedulerID: int,
        OriginatingTaskID: int,
        ForkJoinContextID: int,
        TotalIterations: int,
    ) -> None:
        """

        :param OriginatingTaskSchedulerID:
        :param OriginatingTaskID:
        :param ForkJoinContextID:
        :param TotalIterations:
        """
    def RunningContinuation(self, TaskID: int, Object: object) -> None:
        """

        :param TaskID:
        :param Object:
        """
    @overload
    def RunningContinuationList(self, TaskID: int, Index: int, Object: int) -> None:
        """

        :param TaskID:
        :param Index:
        :param Object:
        """
    @overload
    def RunningContinuationList(self, TaskID: int, Index: int, Object: object) -> None:
        """

        :param TaskID:
        :param Index:
        :param Object:
        """
    def SetActivityId(self, NewId: Guid) -> None:
        """

        :param NewId:
        """
    def TaskCompleted(
        self,
        OriginatingTaskSchedulerID: int,
        OriginatingTaskID: int,
        TaskID: int,
        IsExceptional: bool,
    ) -> None:
        """

        :param OriginatingTaskSchedulerID:
        :param OriginatingTaskID:
        :param TaskID:
        :param IsExceptional:
        """
    def TaskScheduled(
        self,
        OriginatingTaskSchedulerID: int,
        OriginatingTaskID: int,
        TaskID: int,
        CreatingTaskID: int,
        TaskCreationOptions: int,
        appDomain: int,
    ) -> None:
        """

        :param OriginatingTaskSchedulerID:
        :param OriginatingTaskID:
        :param TaskID:
        :param CreatingTaskID:
        :param TaskCreationOptions:
        :param appDomain:
        """
    def TaskStarted(
        self, OriginatingTaskSchedulerID: int, OriginatingTaskID: int, TaskID: int
    ) -> None:
        """

        :param OriginatingTaskSchedulerID:
        :param OriginatingTaskID:
        :param TaskID:
        """
    def TaskWaitBegin(
        self,
        OriginatingTaskSchedulerID: int,
        OriginatingTaskID: int,
        TaskID: int,
        Behavior: TplEtwProvider.TaskWaitBehavior,
        ContinueWithTaskID: int,
        appDomain: int,
    ) -> None:
        """

        :param OriginatingTaskSchedulerID:
        :param OriginatingTaskID:
        :param TaskID:
        :param Behavior:
        :param ContinueWithTaskID:
        :param appDomain:
        """
    def TaskWaitContinuationComplete(self, TaskID: int) -> None:
        """

        :param TaskID:
        """
    def TaskWaitContinuationStarted(self, TaskID: int) -> None:
        """

        :param TaskID:
        """
    def TaskWaitEnd(
        self, OriginatingTaskSchedulerID: int, OriginatingTaskID: int, TaskID: int
    ) -> None:
        """

        :param OriginatingTaskSchedulerID:
        :param OriginatingTaskID:
        :param TaskID:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TraceOperationBegin(self, TaskID: int, OperationName: str, RelatedContext: int) -> None:
        """

        :param TaskID:
        :param OperationName:
        :param RelatedContext:
        """
    def TraceOperationEnd(self, TaskID: int, Status: AsyncCausalityStatus) -> None:
        """

        :param TaskID:
        :param Status:
        """
    def TraceOperationRelation(self, TaskID: int, Relation: CausalityRelation) -> None:
        """

        :param TaskID:
        :param Relation:
        """
    def TraceSynchronousWorkBegin(self, TaskID: int, Work: CausalitySynchronousWork) -> None:
        """

        :param TaskID:
        :param Work:
        """
    def TraceSynchronousWorkEnd(self, Work: CausalitySynchronousWork) -> None:
        """

        :param Work:
        """
    @overload
    def Write(self, eventName: str) -> None:
        """

        :param eventName:
        """
    @overload
    def Write(self, eventName: str, data: T) -> None:
        """

        :param eventName:
        :param data:
        """
    @overload
    def Write(self, eventName: str, options: EventSourceOptions) -> None:
        """

        :param eventName:
        :param options:
        """
    @overload
    def Write(self, eventName: str, options: EventSourceOptions, data: T) -> None:
        """

        :param eventName:
        :param options:
        :param data:
        """
    @overload
    def Write(self, eventName: str, options: EventSourceOptions, data: T) -> None:
        """

        :param eventName:
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
        """

        :param eventName:
        :param options:
        :param activityId:
        :param relatedActivityId:
        :param data:
        """
    EventCommandExecuted: EventType[EventHandler[EventCommandEventArgs]] = ...
    """"""

    class ForkJoinOperationType(Enum):
        """"""

        ParallelInvoke: ForkJoinOperationType = ...
        """"""
        ParallelFor: ForkJoinOperationType = ...
        """"""
        ParallelForEach: ForkJoinOperationType = ...
        """"""

    class Keywords(Object):
        """"""

        AsyncCausalityOperation: Final[ClassVar[EventKeywords]] = ...
        """"""
        AsyncCausalityRelation: Final[ClassVar[EventKeywords]] = ...
        """"""
        AsyncCausalitySynchronousWork: Final[ClassVar[EventKeywords]] = ...
        """"""
        Debug: Final[ClassVar[EventKeywords]] = ...
        """"""
        DebugActivityId: Final[ClassVar[EventKeywords]] = ...
        """"""
        Parallel: Final[ClassVar[EventKeywords]] = ...
        """"""
        TaskStops: Final[ClassVar[EventKeywords]] = ...
        """"""
        TaskTransfer: Final[ClassVar[EventKeywords]] = ...
        """"""
        Tasks: Final[ClassVar[EventKeywords]] = ...
        """"""
        TasksFlowActivityIds: Final[ClassVar[EventKeywords]] = ...
        """"""
        TasksSetActivityIds: Final[ClassVar[EventKeywords]] = ...
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

    class TaskWaitBehavior(Enum):
        """"""

        Synchronous: TaskWaitBehavior = ...
        """"""
        Asynchronous: TaskWaitBehavior = ...
        """"""

    class Tasks(Object):
        """"""

        AwaitTaskContinuationScheduled: Final[ClassVar[EventTask]] = ...
        """"""
        ForkJoin: Final[ClassVar[EventTask]] = ...
        """"""
        Invoke: Final[ClassVar[EventTask]] = ...
        """"""
        Loop: Final[ClassVar[EventTask]] = ...
        """"""
        TaskExecute: Final[ClassVar[EventTask]] = ...
        """"""
        TaskScheduled: Final[ClassVar[EventTask]] = ...
        """"""
        TaskWait: Final[ClassVar[EventTask]] = ...
        """"""
        TraceOperation: Final[ClassVar[EventTask]] = ...
        """"""
        TraceSynchronousWork: Final[ClassVar[EventTask]] = ...
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

class UnobservedTaskExceptionEventArgs(EventArgs):
    """"""

    def __init__(self, exception: AggregateException):
        """

        :param exception:
        """
    @property
    def Exception(self) -> AggregateException:
        """

        :return:
        """
    @property
    def Observed(self) -> bool:
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
    def SetObserved(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class UnwrapPromise(
    Generic[TResult],
    Task[TResult],
    ITaskCompletionAction,
    IThreadPoolWorkItem,
    IAsyncResult,
    IDisposable,
):
    """"""

    def __init__(self, outerTask: Task, lookForOce: bool):
        """

        :param outerTask:
        :param lookForOce:
        """
    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def CompletedTask(cls) -> Task:
        """

        :return:
        """
    @property
    def CreationOptions(self) -> TaskCreationOptions:
        """

        :return:
        """
    @classmethod
    @property
    def CurrentId(cls) -> Optional[int]:
        """

        :return:
        """
    @property
    def Exception(self) -> AggregateException:
        """

        :return:
        """
    @classmethod
    @property
    def Factory(cls) -> TaskFactory:
        """

        :return:
        """
    @property
    def Id(self) -> int:
        """

        :return:
        """
    @property
    def IsCanceled(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
        """

        :return:
        """
    @property
    def IsFaulted(self) -> bool:
        """

        :return:
        """
    @property
    def Result(self) -> TResult:
        """

        :return:
        """
    @property
    def Status(self) -> TaskStatus:
        """

        :return:
        """
    def ConfigureAwait(self, continueOnCapturedContext: bool) -> ConfiguredTaskAwaitable:
        """

        :param continueOnCapturedContext:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task]) -> Task:
        """

        :param continuationAction:
        :return:
        """
    @overload
    def ContinueWith(self, continuationFunction: Func[Task, TResult]) -> Task[TResult]:
        """

        :param continuationFunction:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task, object], state: object) -> Task:
        """

        :param continuationAction:
        :param state:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], continuationOptions: TaskContinuationOptions
    ) -> Task:
        """

        :param continuationAction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(self, continuationAction: Action[Task], scheduler: TaskScheduler) -> Task:
        """

        :param continuationAction:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task], cancellationToken: CancellationToken
    ) -> Task:
        """

        :param continuationAction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, TResult],
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, TResult], scheduler: TaskScheduler
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationFunction: Func[Task, object, TResult], state: object
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self, continuationAction: Action[Task, object], state: object, scheduler: TaskScheduler
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        continuationOptions: TaskContinuationOptions,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param continuationOptions:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param cancellationToken:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param continuationAction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, TResult],
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationAction: Action[Task, object],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task:
        """

        :param continuationAction:
        :param state:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    @overload
    def ContinueWith(
        self,
        continuationFunction: Func[Task, object, TResult],
        state: object,
        cancellationToken: CancellationToken,
        continuationOptions: TaskContinuationOptions,
        scheduler: TaskScheduler,
    ) -> Task[TResult]:
        """

        :param continuationFunction:
        :param state:
        :param cancellationToken:
        :param continuationOptions:
        :param scheduler:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetAwaiter(self) -> TaskAwaiter:
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
    def Invoke(self, completingTask: Task) -> None:
        """

        :param completingTask:
        """
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """

        :param tae:
        """
    @overload
    def RunSynchronously(self) -> None:
        """"""
    @overload
    def RunSynchronously(self, scheduler: TaskScheduler) -> None:
        """

        :param scheduler:
        """
    @overload
    def Start(self) -> None:
        """"""
    @overload
    def Start(self, scheduler: TaskScheduler) -> None:
        """

        :param scheduler:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Wait(self) -> None:
        """"""
    @overload
    def Wait(self, cancellationToken: CancellationToken) -> None:
        """

        :param cancellationToken:
        """
    @overload
    def Wait(self, millisecondsTimeout: int) -> bool:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def Wait(self, timeout: TimeSpan) -> bool:
        """

        :param timeout:
        :return:
        """
    @overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool:
        """

        :param millisecondsTimeout:
        :param cancellationToken:
        :return:
        """

class VoidTaskResult(ValueType):
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
