__all__ = [
    'ConcurrentExclusiveSchedulerPair',
    'Parallel',
    'ParallelLoopState',
    'ParallelOptions',
    'Task',
    'Task',
    'TaskAsyncEnumerableExtensions',
    'TaskCanceledException',
    'TaskCompletionSource',
    'TaskCompletionSource',
    'TaskExtensions',
    'TaskFactory',
    'TaskFactory',
    'TaskScheduler',
    'TaskSchedulerException',
    'UnobservedTaskExceptionEventArgs',
    'ParallelLoopResult',
    'ValueTask',
    'ValueTask',
    'TaskContinuationOptions',
    'TaskCreationOptions',
    'TaskStatus',
]

from typing import TypeVar, Generic

TResult = TypeVar('TResult')


# TODO

# ---------- CLASSES ---------- #

class ConcurrentExclusiveSchedulerPair:
    """Provides task schedulers that coordinate to execute tasks while ensuring that concurrent tasks may run concurrently and exclusive tasks never do."""


class Parallel:
    """Provides support for parallel loops and regions."""


class ParallelLoopState:
    """Enables iterations of parallel loops to interact with other iterations. An instance of this class is provided by the Parallel class to each loop; you can not create instances in your code."""


class ParallelOptions:
    """Stores options that configure the operation of methods on the Parallel class."""


class Task:
    """Represents an asynchronous operation."""


class Task(Generic[TResult]):
    """Represents an asynchronous operation that can return a value."""


class TaskAsyncEnumerableExtensions:
    """Provides a set of static methods for configuring task-related behaviors on asynchronous enumerables and disposables."""


class TaskCanceledException:
    """Represents an exception used to communicate task cancellation."""


class TaskCompletionSource:
    """Represents the producer side of a Task unbound to a delegate, providing access to the consumer side through the Task property."""


class TaskCompletionSource(Generic[TResult]):
    """Represents the producer side of a Task<TResult> unbound to a delegate, providing access to the consumer side through the Task property."""


class TaskExtensions:
    """Provides a set of static (Shared in Visual Basic) methods for working with specific kinds of Task instances."""


class TaskFactory:
    """Provides support for creating and scheduling Task objects."""


class TaskFactory(Generic[TResult]):
    """Provides support for creating and scheduling Task<TResult> objects."""


class TaskScheduler:
    """Represents an object that handles the low-level work of queuing tasks onto threads."""


class TaskSchedulerException:
    """Represents an exception used to communicate an invalid operation by a TaskScheduler."""


class UnobservedTaskExceptionEventArgs:
    """Provides data for the event that is raised when a faulted Task's exception goes unobserved."""


# ---------- STRUCTS ---------- #

class ParallelLoopResult:
    """Provides completion status on the execution of a Parallel loop."""


class ValueTask:
    """Provides an awaitable result of an asynchronous operation."""


class ValueTask(Generic[TResult]):
    """Provides a value type that wraps a Task<TResult> and a TResult, only one of which is used."""


# ---------- ENUMS ---------- #

class TaskContinuationOptions:
    """Specifies the behavior for a task that is created by using the ContinueWith(Action<Task>, CancellationToken, TaskContinuationOptions, TaskScheduler) or ContinueWith(Action<Task<TResult>>, TaskContinuationOptions) method."""


class TaskCreationOptions:
    """Specifies flags that control optional behavior for the creation and execution of tasks."""


class TaskStatus:
    """Represents the current stage in the lifecycle of a Task."""
