__all__ = [
    'AbandonedMutexException',
    'AsyncLocal',
    'AutoResetEvent',
    'Barrier',
    'BarrierPostPhaseException',
    'CancellationTokenSource',
    'CompressedStack',
    'CountdownEvent',
    'EventWaitHandle',
    'ExecutionContext',
    'HostExecutionContext',
    'HostExecutionContextManager',
    'Interlocked',
    'LazyInitializer',
    'LockRecursionException',
    'ManualResetEvent',
    'ManualResetEventSlim',
    'Monitor',
    'Mutex',
    'Overlapped',
    'PeriodicTimer',
    'PreAllocatedOverlapped',
    'ReaderWriterLock',
    'ReaderWriterLockSlim',
    'RegisteredWaitHandle',
    'Semaphore',
    'SemaphoreFullException',
    'SemaphoreSlim',
    'SynchronizationContext',
    'SynchronizationLockException',
    'Thread',
    'ThreadAbortException',
    'ThreadExceptionEventArgs',
    'ThreadInterruptedException',
    'ThreadLocal',
    'ThreadPool',
    'ThreadPoolBoundHandle',
    'ThreadStartException',
    'ThreadStateException',
    'Timeout',
    'Timer',
    'Volatile',
    'WaitHandle',
    'WaitHandleCannotBeOpenedException',
    'WaitHandleExtensions',
    'AsyncFlowControl',
    'AsyncLocalValueChangedArgs',
    'CancellationToken',
    'CancellationTokenRegistration',
    'LockCookie',
    'NativeOverlapped',
    'SpinLock',
    'SpinWait',
    'IThreadPoolWorkItem',
    'ApartmentState',
    'EventResetMode',
    'LazyThreadSafetyMode',
    'LockRecursionPolicy',
    'ThreadPriority',
    'ThreadState',
    'ContextCallback',
    'IOCompletionCallback',
    'ParameterizedThreadStart',
    'SendOrPostCallback',
    'ThreadExceptionEventHandler',
    'ThreadStart',
    'TimerCallback',
    'WaitCallback',
    'WaitOrTimerCallback',
]

from typing import TypeVar, Generic

T = TypeVar('T')


# TODO

# ---------- CLASSES ---------- #

class AbandonedMutexException:
    """The exception that is thrown when one thread acquires a Mutex object that another thread has abandoned by exiting without releasing it."""


class AsyncLocal(Generic[T]):
    """Represents ambient data that is local to a given asynchronous control flow, such as an asynchronous method."""


class AutoResetEvent:
    """Represents a thread synchronization event that, when signaled, resets automatically after releasing a single waiting thread. This class cannot be inherited."""


class Barrier:
    """Enables multiple tasks to cooperatively work on an algorithm in parallel through multiple phases."""


class BarrierPostPhaseException:
    """The exception that is thrown when the post-phase action of a Barrier fails."""


class CancellationTokenSource:
    """Signals to a CancellationToken that it should be canceled."""


class CompressedStack:
    """Provides methods for setting and capturing the compressed stack on the current thread. This class cannot be inherited."""


class CountdownEvent:
    """Represents a synchronization primitive that is signaled when its count reaches zero."""


class EventWaitHandle:
    """Represents a thread synchronization event."""


class ExecutionContext:
    """Manages the execution context for the current thread. This class cannot be inherited."""


class HostExecutionContext:
    """Encapsulates and propagates the host execution context across threads."""


class HostExecutionContextManager:
    """Provides the functionality that allows a common language runtime host to participate in the flow, or migration, of the execution context."""


class Interlocked:
    """Provides atomic operations for variables that are shared by multiple threads."""


class LazyInitializer:
    """Provides lazy initialization routines."""


class LockRecursionException:
    """The exception that is thrown when recursive entry into a lock is not compatible with the recursion policy for the lock."""


class ManualResetEvent:
    """Represents a thread synchronization event that, when signaled, must be reset manually. This class cannot be inherited."""


class ManualResetEventSlim:
    """Represents a thread synchronization event that, when signaled, must be reset manually. This class is a lightweight alternative to ManualResetEvent."""


class Monitor:
    """Provides a mechanism that synchronizes access to objects."""


class Mutex:
    """A synchronization primitive that can also be used for interprocess synchronization."""


class Overlapped:
    """Provides a managed representation of a Win32 OVERLAPPED structure, including methods to transfer information from an Overlapped instance to a NativeOverlapped structure."""


class PeriodicTimer:
    """Provides a periodic timer that enables waiting asynchronously for timer ticks."""


class PreAllocatedOverlapped:
    """Represents pre-allocated state for native overlapped I/O operations."""


class ReaderWriterLock:
    """Defines a lock that supports single writers and multiple readers."""


class ReaderWriterLockSlim:
    """Represents a lock that is used to manage access to a resource, allowing multiple threads for reading or exclusive access for writing."""


class RegisteredWaitHandle:
    """Represents a handle that has been registered when calling RegisterWaitForSingleObject(WaitHandle, WaitOrTimerCallback, Object, UInt32, Boolean). This class cannot be inherited."""


class Semaphore:
    """Limits the number of threads that can access a resource or pool of resources concurrently."""


class SemaphoreFullException:
    """The exception that is thrown when the Release method is called on a semaphore whose count is already at the maximum."""


class SemaphoreSlim:
    """Represents a lightweight alternative to Semaphore that limits the number of threads that can access a resource or pool of resources concurrently."""


class SynchronizationContext:
    """Provides the basic functionality for propagating a synchronization context in various synchronization models."""


class SynchronizationLockException:
    """The exception that is thrown when a method requires the caller to own the lock on a given Monitor, and the method is invoked by a caller that does not own that lock."""


class Thread:
    """Creates and controls a thread, sets its priority, and gets its status."""


class ThreadAbortException:
    """The exception that is thrown when a call is made to the Abort(Object) method. This class cannot be inherited."""


class ThreadExceptionEventArgs:
    """Provides data for the ThreadException event."""


class ThreadInterruptedException:
    """The exception that is thrown when a Thread is interrupted while it is in a waiting state."""


class ThreadLocal(Generic[T]):
    """Provides thread-local storage of data."""


class ThreadPool:
    """Provides a pool of threads that can be used to execute tasks, post work items, process asynchronous I/O, wait on behalf of other threads, and process timers."""


class ThreadPoolBoundHandle:
    """Represents an I/O handle that is bound to the system thread pool and enables low-level components to receive notifications for asynchronous I/O operations."""


class ThreadStartException:
    """The exception that is thrown when a failure occurs in a managed thread after the underlying operating system thread has been started, but before the thread is ready to execute user code."""


class ThreadStateException:
    """The exception that is thrown when a Thread is in an invalid ThreadState for the method call."""


class Timeout:
    """Contains constants that specify infinite time-out intervals. This class cannot be inherited."""


class Timer:
    """Provides a mechanism for executing a method on a thread pool thread at specified intervals. This class cannot be inherited."""


class Volatile:
    """Contains methods for performing volatile memory operations."""


class WaitHandle:
    """Encapsulates operating system-specific objects that wait for exclusive access to shared resources."""


class WaitHandleCannotBeOpenedException:
    """The exception that is thrown when an attempt is made to open a system mutex, semaphore, or event wait handle that does not exist."""


class WaitHandleExtensions:
    """Provides convenience methods to for working with a safe handle for a wait handle."""


# ---------- STRUCTS ---------- #

class AsyncFlowControl:
    """Provides the functionality to restore the migration, or flow, of the execution context between threads."""


class AsyncLocalValueChangedArgs(Generic[T]):
    """The class that provides data change information to AsyncLocal<T> instances that register for change notifications."""


class CancellationToken:
    """Propagates notification that operations should be canceled."""


class CancellationTokenRegistration:
    """Represents a callback delegate that has been registered with a CancellationToken."""


class LockCookie:
    """Defines the lock that implements single-writer/multiple-reader semantics. This is a value type."""


class NativeOverlapped:
    """Provides an explicit layout that is visible from unmanaged code and that will have the same layout as the Win32 OVERLAPPED structure with additional reserved fields at the end."""


class SpinLock:
    """Provides a mutual exclusion lock primitive where a thread trying to acquire the lock waits in a loop repeatedly checking until the lock becomes available."""


class SpinWait:
    """Provides support for spin-based waiting."""


# ---------- INTERFACES ---------- #

class IThreadPoolWorkItem:
    """Represents a work item that can be executed by the ThreadPool."""


# ---------- ENUMS ---------- #

class ApartmentState:
    """Specifies the apartment state of a Thread."""


class EventResetMode:
    """Indicates whether an EventWaitHandle is reset automatically or manually after receiving a signal."""


class LazyThreadSafetyMode:
    """Specifies how a Lazy<T> instance synchronizes access among multiple threads."""


class LockRecursionPolicy:
    """Specifies whether a lock can be entered multiple times by the same thread."""


class ThreadPriority:
    """Specifies the scheduling priority of a Thread."""


class ThreadState:
    """Specifies the execution states of a Thread."""


# ---------- DELEGATES ---------- #

class ContextCallback:
    """Represents a method to be called within a new context."""


class IOCompletionCallback:
    """Receives the error code, number of bytes, and overlapped value type when an I/O operation completes on the thread pool."""


class ParameterizedThreadStart:
    """Represents the method that executes on a Thread."""


class SendOrPostCallback:
    """Represents a method to be called when a message is to be dispatched to a synchronization context."""


class ThreadExceptionEventHandler:
    """Represents the method that will handle the ThreadException event of an Application."""


class ThreadStart:
    """Represents the method that executes on a Thread."""


class TimerCallback:
    """Represents the method that handles calls from a Timer."""


class WaitCallback:
    """Represents a callback method to be executed by a thread pool thread."""


class WaitOrTimerCallback:
    """Represents a method to be called when a WaitHandle is signaled or times out."""
