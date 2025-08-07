"""Automatically generated stubs for C# namespace: System.Threading."""

from abc import ABC
from collections.abc import Callable
from typing import ClassVar
from typing import Final
from typing import Self
from typing import overload

from Microsoft.Win32.SafeHandles import SafeWaitHandle
from System import Action
from System import AppDomain
from System import ApplicationException
from System import Array
from System import Boolean
from System import Byte
from System import Double
from System import Enum
from System import EventArgs
from System import EventHandler
from System import Exception
from System import Func
from System import Guid
from System import IAsyncResult
from System import IDisposable
from System import IEquatable
from System import Int16
from System import Int32
from System import Int64
from System import IntPtr
from System import LocalDataStoreSlot
from System import MarshalByRefObject
from System import Object
from System import Random
from System import SByte
from System import Single
from System import SystemException
from System import TimeSpan
from System import Type
from System import UInt16
from System import UInt32
from System import UInt64
from System import UIntPtr
from System import ValueType
from System.Collections import IDictionary
from System.Collections.Generic import IList
from System.Collections.Generic import List
from System.Diagnostics.Tracing import EventChannel
from System.Diagnostics.Tracing import EventCommandEventArgs
from System.Diagnostics.Tracing import EventKeywords
from System.Diagnostics.Tracing import EventLevel
from System.Diagnostics.Tracing import EventSource
from System.Diagnostics.Tracing import EventSourceOptions
from System.Diagnostics.Tracing import EventSourceSettings
from System.Diagnostics.Tracing import T
from System.Globalization import CultureInfo
from System.Reflection import MethodBase
from System.Runtime.ConstrainedExecution import CriticalFinalizerObject
from System.Runtime.InteropServices import SafeHandle
from System.Runtime.InteropServices import _Exception
from System.Runtime.InteropServices import _Thread
from System.Runtime.Remoting import ObjRef
from System.Runtime.Remoting.Contexts import Context
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Security.AccessControl import EventWaitHandleRights
from System.Security.AccessControl import EventWaitHandleSecurity
from System.Security.AccessControl import MutexRights
from System.Security.AccessControl import MutexSecurity
from System.Security.AccessControl import SemaphoreRights
from System.Security.AccessControl import SemaphoreSecurity
from System.Security.Principal import IPrincipal
from System.Threading.Tasks import Task

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

class AbandonedMutexException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, inner: Exception) -> None:
        """"""
    @overload
    def __init__(self, location: int, handle: WaitHandle) -> None:
        """"""
    @overload
    def __init__(self, message: str, location: int, handle: WaitHandle) -> None:
        """"""
    @overload
    def __init__(self, message: str, inner: Exception, location: int, handle: WaitHandle) -> None:
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
    def Mutex(self) -> Mutex:
        """"""
    @property
    def MutexIndex(self) -> int:
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

class ApartmentState(Enum):
    """"""

    STA: ApartmentState = ...
    """"""
    MTA: ApartmentState = ...
    """"""
    Unknown: ApartmentState = ...
    """"""

class AsyncFlowControl(ValueType, IDisposable):
    """"""
    def Dispose(self) -> None:
        """"""
    @overload
    def Equals(self, obj: AsyncFlowControl) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def Undo(self) -> None:
        """"""
    @classmethod
    def op_Equality(cls, a: AsyncFlowControl, b: AsyncFlowControl) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, a: AsyncFlowControl, b: AsyncFlowControl) -> bool:
        """"""
    def __eq__(self, other: AsyncFlowControl) -> bool:
        """"""
    def __ne__(self, other: AsyncFlowControl) -> bool:
        """"""

class AsyncLocalValueChangedArgs[T](ValueType):
    """"""
    @property
    def CurrentValue(self) -> T:
        """"""
    @property
    def PreviousValue(self) -> T:
        """"""
    @property
    def ThreadContextChanged(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class AsyncLocalValueMap(ABC, Object):
    """"""
    @classmethod
    @property
    def Empty(cls) -> IAsyncLocalValueMap:
        """"""
    @classmethod
    def Create(
        cls, key: IAsyncLocal, value: object, treatNullValueAsNonexistent: bool
    ) -> IAsyncLocalValueMap:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsEmpty(cls, asyncLocalValueMap: IAsyncLocalValueMap) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class AsyncLocal[T](Object, IAsyncLocal):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, valueChangedHandler: Action[AsyncLocalValueChangedArgs[T]]) -> None:
        """"""
    @property
    def Value(self) -> T:
        """"""
    @Value.setter
    def Value(self, value: T) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def OnValueChanged(
        self, previousValue: object, currentValue: object, contextChanged: bool
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class AutoResetEvent(EventWaitHandle, IDisposable):
    """"""
    def __init__(self, initialState: bool) -> None:
        """"""
    @property
    def Handle(self) -> IntPtr:
        """"""
    @Handle.setter
    def Handle(self, value: IntPtr) -> None: ...
    @property
    def SafeWaitHandle(self) -> SafeWaitHandle:
        """"""
    @SafeWaitHandle.setter
    def SafeWaitHandle(self, value: SafeWaitHandle) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAccessControl(self) -> EventWaitHandleSecurity:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Reset(self) -> bool:
        """"""
    def Set(self) -> bool:
        """"""
    def SetAccessControl(self, eventSecurity: EventWaitHandleSecurity) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def WaitOne(self) -> bool:
        """"""
    @overload
    def WaitOne(self, millisecondsTimeout: int) -> bool:
        """"""
    @overload
    def WaitOne(self, millisecondsTimeout: int, exitContext: bool) -> bool:
        """"""
    @overload
    def WaitOne(self, timeout: TimeSpan) -> bool:
        """"""
    @overload
    def WaitOne(self, timeout: TimeSpan, exitContext: bool) -> bool:
        """"""

class Barrier(Object, IDisposable):
    """"""
    @overload
    def __init__(self, participantCount: int) -> None:
        """"""
    @overload
    def __init__(self, participantCount: int, postPhaseAction: Action[Barrier]) -> None:
        """"""
    @property
    def CurrentPhaseNumber(self) -> int:
        """"""
    @property
    def ParticipantCount(self) -> int:
        """"""
    @property
    def ParticipantsRemaining(self) -> int:
        """"""
    def AddParticipant(self) -> int:
        """"""
    def AddParticipants(self, participantCount: int) -> int:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def RemoveParticipant(self) -> None:
        """"""
    def RemoveParticipants(self, participantCount: int) -> None:
        """"""
    @overload
    def SignalAndWait(self) -> None:
        """"""
    @overload
    def SignalAndWait(self, cancellationToken: CancellationToken) -> None:
        """"""
    @overload
    def SignalAndWait(self, millisecondsTimeout: int) -> bool:
        """"""
    @overload
    def SignalAndWait(self, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool:
        """"""
    @overload
    def SignalAndWait(self, timeout: TimeSpan) -> bool:
        """"""
    @overload
    def SignalAndWait(self, timeout: TimeSpan, cancellationToken: CancellationToken) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class BarrierPostPhaseException(Exception, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, innerException: Exception) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
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

class CancellationCallbackCoreWorkArguments(ValueType):
    """"""
    def __init__(
        self,
        currArrayFragment: SparselyPopulatedArrayFragment[CancellationCallbackInfo],
        currArrayIndex: int,
    ) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CancellationCallbackInfo(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CancellationToken(ValueType):
    """"""
    def __init__(self, canceled: bool) -> None:
        """"""
    @property
    def CanBeCanceled(self) -> bool:
        """"""
    @property
    def IsCancellationRequested(self) -> bool:
        """"""
    @property
    def WaitHandle(self) -> WaitHandle:
        """"""
    @classmethod
    @property
    def _None(cls) -> CancellationToken:
        """"""
    @overload
    def Equals(self, other: CancellationToken) -> bool:
        """"""
    @overload
    def Equals(self, other: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Register(self, callback: Action) -> CancellationTokenRegistration:
        """"""
    @overload
    def Register(
        self, callback: Action, useSynchronizationContext: bool
    ) -> CancellationTokenRegistration:
        """"""
    @overload
    def Register(self, callback: Action[object], state: object) -> CancellationTokenRegistration:
        """"""
    @overload
    def Register(
        self, callback: Action[object], state: object, useSynchronizationContext: bool
    ) -> CancellationTokenRegistration:
        """"""
    def ThrowIfCancellationRequested(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: CancellationToken, right: CancellationToken) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: CancellationToken, right: CancellationToken) -> bool:
        """"""
    def __eq__(self, other: CancellationToken) -> bool:
        """"""
    def __ne__(self, other: CancellationToken) -> bool:
        """"""

class CancellationTokenRegistration(
    ValueType, IDisposable, IEquatable[CancellationTokenRegistration]
):
    """"""
    def Dispose(self) -> None:
        """"""
    @overload
    def Equals(self, other: CancellationTokenRegistration) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(
        cls, left: CancellationTokenRegistration, right: CancellationTokenRegistration
    ) -> bool:
        """"""
    @classmethod
    def op_Inequality(
        cls, left: CancellationTokenRegistration, right: CancellationTokenRegistration
    ) -> bool:
        """"""
    def __eq__(self, other: CancellationTokenRegistration) -> bool:
        """"""
    def __ne__(self, other: CancellationTokenRegistration) -> bool:
        """"""

class CancellationTokenSource(Object, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, delay: TimeSpan) -> None:
        """"""
    @overload
    def __init__(self, millisecondsDelay: int) -> None:
        """"""
    @property
    def IsCancellationRequested(self) -> bool:
        """"""
    @property
    def Token(self) -> CancellationToken:
        """"""
    @overload
    def Cancel(self) -> None:
        """"""
    @overload
    def Cancel(self, throwOnFirstException: bool) -> None:
        """"""
    @overload
    def CancelAfter(self, millisecondsDelay: int) -> None:
        """"""
    @overload
    def CancelAfter(self, delay: TimeSpan) -> None:
        """"""
    @classmethod
    @overload
    def CreateLinkedTokenSource(
        cls, token1: CancellationToken, token2: CancellationToken
    ) -> CancellationTokenSource:
        """"""
    @classmethod
    @overload
    def CreateLinkedTokenSource(cls, tokens: Array[CancellationToken]) -> CancellationTokenSource:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CdsSyncEtwBCLProvider(EventSource, IDisposable):
    """"""

    Log: ClassVar[CdsSyncEtwBCLProvider]
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
    def Barrier_PhaseFinished(self, currentSense: bool, phaseNum: int) -> None:
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
    def SpinLock_FastPathFailed(self, ownerID: int) -> None:
        """"""
    def SpinWait_NextSpinWillYield(self) -> None:
        """"""
    def ToString(self) -> str:
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

class CompressedStack(Object, ISerializable):
    """"""
    @classmethod
    def Capture(cls) -> CompressedStack:
        """"""
    def CreateCopy(self) -> CompressedStack:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetCompressedStack(cls) -> CompressedStack:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Run(
        cls, compressedStack: CompressedStack, callback: ContextCallback, state: object
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class CompressedStackSwitcher(ValueType, IDisposable):
    """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def Undo(self) -> None:
        """"""
    @classmethod
    def op_Equality(cls, c1: CompressedStackSwitcher, c2: CompressedStackSwitcher) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, c1: CompressedStackSwitcher, c2: CompressedStackSwitcher) -> bool:
        """"""
    def __eq__(self, other: CompressedStackSwitcher) -> bool:
        """"""
    def __ne__(self, other: CompressedStackSwitcher) -> bool:
        """"""

ContextCallback: Callable[[object], None] = ...
""""""

class CountdownEvent(Object, IDisposable):
    """"""
    def __init__(self, initialCount: int) -> None:
        """"""
    @property
    def CurrentCount(self) -> int:
        """"""
    @property
    def InitialCount(self) -> int:
        """"""
    @property
    def IsSet(self) -> bool:
        """"""
    @property
    def WaitHandle(self) -> WaitHandle:
        """"""
    @overload
    def AddCount(self) -> None:
        """"""
    @overload
    def AddCount(self, signalCount: int) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Reset(self) -> None:
        """"""
    @overload
    def Reset(self, count: int) -> None:
        """"""
    @overload
    def Signal(self) -> bool:
        """"""
    @overload
    def Signal(self, signalCount: int) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def TryAddCount(self) -> bool:
        """"""
    @overload
    def TryAddCount(self, signalCount: int) -> bool:
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
    @overload
    def Wait(self, timeout: TimeSpan, cancellationToken: CancellationToken) -> bool:
        """"""

class DeferredDisposableLifetime[T](ValueType):
    """"""
    def AddRef[T](self, obj: T) -> bool:
        """"""
    def Dispose[T](self, obj: T) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Release[T](self, obj: T) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class DomainCompressedStack(Object):
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

class EventResetMode(Enum):
    """"""

    AutoReset: EventResetMode = ...
    """"""
    ManualReset: EventResetMode = ...
    """"""

class EventWaitHandle(WaitHandle, IDisposable):
    """"""
    @overload
    def __init__(self, initialState: bool, mode: EventResetMode) -> None:
        """"""
    @overload
    def __init__(self, initialState: bool, mode: EventResetMode, name: str) -> None:
        """"""
    @overload
    def __init__(
        self, initialState: bool, mode: EventResetMode, name: str, createdNew: Boolean
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        initialState: bool,
        mode: EventResetMode,
        name: str,
        createdNew: Boolean,
        eventSecurity: EventWaitHandleSecurity,
    ) -> None:
        """"""
    @property
    def Handle(self) -> IntPtr:
        """"""
    @Handle.setter
    def Handle(self, value: IntPtr) -> None: ...
    @property
    def SafeWaitHandle(self) -> SafeWaitHandle:
        """"""
    @SafeWaitHandle.setter
    def SafeWaitHandle(self, value: SafeWaitHandle) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAccessControl(self) -> EventWaitHandleSecurity:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    @classmethod
    @overload
    def OpenExisting(cls, name: str) -> EventWaitHandle:
        """"""
    @classmethod
    @overload
    def OpenExisting(cls, name: str, rights: EventWaitHandleRights) -> EventWaitHandle:
        """"""
    def Reset(self) -> bool:
        """"""
    def Set(self) -> bool:
        """"""
    def SetAccessControl(self, eventSecurity: EventWaitHandleSecurity) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def TryOpenExisting(
        cls, name: str, rights: EventWaitHandleRights, result: EventWaitHandle
    ) -> tuple[bool, EventWaitHandle]:
        """"""
    @classmethod
    @overload
    def TryOpenExisting(cls, name: str, result: EventWaitHandle) -> tuple[bool, EventWaitHandle]:
        """"""
    @overload
    def WaitOne(self) -> bool:
        """"""
    @overload
    def WaitOne(self, millisecondsTimeout: int) -> bool:
        """"""
    @overload
    def WaitOne(self, millisecondsTimeout: int, exitContext: bool) -> bool:
        """"""
    @overload
    def WaitOne(self, timeout: TimeSpan) -> bool:
        """"""
    @overload
    def WaitOne(self, timeout: TimeSpan, exitContext: bool) -> bool:
        """"""

class ExecutionContext(Object, ISerializable, IDisposable):
    """"""
    @classmethod
    def Capture(cls) -> ExecutionContext:
        """"""
    def CreateCopy(self) -> ExecutionContext:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsFlowSuppressed(cls) -> bool:
        """"""
    @classmethod
    def RestoreFlow(cls) -> None:
        """"""
    @classmethod
    def Run(
        cls, executionContext: ExecutionContext, callback: ContextCallback, state: object
    ) -> None:
        """"""
    @classmethod
    def SuppressFlow(cls) -> AsyncFlowControl:
        """"""
    def ToString(self) -> str:
        """"""

class ExecutionContextSwitcher(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Gen2GcCallback(CriticalFinalizerObject):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Register(cls, callback: Func[object, bool], targetObj: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class HostExecutionContext(Object, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, state: object) -> None:
        """"""
    def CreateCopy(self) -> HostExecutionContext:
        """"""
    @overload
    def Dispose(self) -> None:
        """"""
    @overload
    def Dispose(self, disposing: bool) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HostExecutionContextManager(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Capture(self) -> HostExecutionContext:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Revert(self, previousState: object) -> None:
        """"""
    def SetHostExecutionContext(self, hostExecutionContext: HostExecutionContext) -> object:
        """"""
    def ToString(self) -> str:
        """"""

class HostExecutionContextSwitcher(Object):
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
    @classmethod
    def Undo(cls, switcherObject: object) -> None:
        """"""

class IAsyncLocal:
    """"""
    def OnValueChanged(
        self, previousValue: object, currentValue: object, contextChanged: bool
    ) -> None:
        """"""

class IAsyncLocalValueMap:
    """"""
    def Set(
        self, key: IAsyncLocal, value: object, treatNullValueAsNonexistent: bool
    ) -> IAsyncLocalValueMap:
        """"""
    def TryGetValue(self, key: IAsyncLocal, value: Object) -> tuple[bool, Object]:
        """"""

class IDeferredDisposable:
    """"""
    def OnFinalRelease(self, disposed: bool) -> None:
        """"""

IOCompletionCallback: Callable[[int, int, NativeOverlapped], None] = ...
""""""

class IThreadPoolWorkItem:
    """"""
    def ExecuteWorkItem(self) -> None:
        """"""
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """"""

class IUnknownSafeHandle(SafeHandle, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class Interlocked(ABC, Object):
    """"""
    @classmethod
    @overload
    def Add(cls, location1: Int32, value: int) -> int:
        """"""
    @classmethod
    @overload
    def Add(cls, location1: Int64, value: int) -> int:
        """"""
    @classmethod
    @overload
    def CompareExchange[T, T, T](cls, location1: T, value: T, comparand: T) -> T:
        """"""
    @classmethod
    @overload
    def CompareExchange(cls, location1: Double, value: float, comparand: float) -> float:
        """"""
    @classmethod
    @overload
    def CompareExchange(cls, location1: Int32, value: int, comparand: int) -> int:
        """"""
    @classmethod
    @overload
    def CompareExchange(cls, location1: Int64, value: int, comparand: int) -> int:
        """"""
    @classmethod
    @overload
    def CompareExchange(cls, location1: IntPtr, value: IntPtr, comparand: IntPtr) -> IntPtr:
        """"""
    @classmethod
    @overload
    def CompareExchange(cls, location1: Object, value: object, comparand: object) -> object:
        """"""
    @classmethod
    @overload
    def CompareExchange(cls, location1: Single, value: float, comparand: float) -> float:
        """"""
    @classmethod
    @overload
    def Decrement(cls, location: Int32) -> int:
        """"""
    @classmethod
    @overload
    def Decrement(cls, location: Int64) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def Exchange[T, T](cls, location1: T, value: T) -> T:
        """"""
    @classmethod
    @overload
    def Exchange(cls, location1: Double, value: float) -> float:
        """"""
    @classmethod
    @overload
    def Exchange(cls, location1: Int32, value: int) -> int:
        """"""
    @classmethod
    @overload
    def Exchange(cls, location1: Int64, value: int) -> int:
        """"""
    @classmethod
    @overload
    def Exchange(cls, location1: IntPtr, value: IntPtr) -> IntPtr:
        """"""
    @classmethod
    @overload
    def Exchange(cls, location1: Object, value: object) -> object:
        """"""
    @classmethod
    @overload
    def Exchange(cls, location1: Single, value: float) -> float:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def Increment(cls, location: Int32) -> int:
        """"""
    @classmethod
    @overload
    def Increment(cls, location: Int64) -> int:
        """"""
    @classmethod
    def MemoryBarrier(cls) -> None:
        """"""
    @classmethod
    def Read(cls, location: Int64) -> int:
        """"""
    @classmethod
    def SpeculationBarrier(cls) -> None:
        """"""
    def ToString(self) -> str:
        """"""

InternalCrossContextDelegate: Callable[[Array[object]], object] = ...
""""""

class LazyHelpers[T](ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class LazyInitializer(ABC, Object):
    """"""
    @classmethod
    @overload
    def EnsureInitialized[T](cls, target: T) -> T:
        """"""
    @classmethod
    @overload
    def EnsureInitialized[T](cls, target: T, initialized: Boolean, syncLock: Object) -> T:
        """"""
    @classmethod
    @overload
    def EnsureInitialized[T](
        cls, target: T, initialized: Boolean, syncLock: Object, valueFactory: Func[T]
    ) -> T:
        """"""
    @classmethod
    @overload
    def EnsureInitialized[T](cls, target: T, valueFactory: Func[T]) -> T:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class LazyThreadSafetyMode(Enum):
    """"""

    _None: LazyThreadSafetyMode = ...
    """"""
    PublicationOnly: LazyThreadSafetyMode = ...
    """"""
    ExecutionAndPublication: LazyThreadSafetyMode = ...
    """"""

class LockCookie(ValueType):
    """"""
    @overload
    def Equals(self, obj: LockCookie) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, a: LockCookie, b: LockCookie) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, a: LockCookie, b: LockCookie) -> bool:
        """"""
    def __eq__(self, other: LockCookie) -> bool:
        """"""
    def __ne__(self, other: LockCookie) -> bool:
        """"""

class LockRecursionException(Exception, _Exception, ISerializable):
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

class LockRecursionPolicy(Enum):
    """"""

    NoRecursion: LockRecursionPolicy = ...
    """"""
    SupportsRecursion: LockRecursionPolicy = ...
    """"""

class ManualResetEvent(EventWaitHandle, IDisposable):
    """"""
    def __init__(self, initialState: bool) -> None:
        """"""
    @property
    def Handle(self) -> IntPtr:
        """"""
    @Handle.setter
    def Handle(self, value: IntPtr) -> None: ...
    @property
    def SafeWaitHandle(self) -> SafeWaitHandle:
        """"""
    @SafeWaitHandle.setter
    def SafeWaitHandle(self, value: SafeWaitHandle) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAccessControl(self) -> EventWaitHandleSecurity:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Reset(self) -> bool:
        """"""
    def Set(self) -> bool:
        """"""
    def SetAccessControl(self, eventSecurity: EventWaitHandleSecurity) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def WaitOne(self) -> bool:
        """"""
    @overload
    def WaitOne(self, millisecondsTimeout: int) -> bool:
        """"""
    @overload
    def WaitOne(self, millisecondsTimeout: int, exitContext: bool) -> bool:
        """"""
    @overload
    def WaitOne(self, timeout: TimeSpan) -> bool:
        """"""
    @overload
    def WaitOne(self, timeout: TimeSpan, exitContext: bool) -> bool:
        """"""

class ManualResetEventSlim(Object, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, initialState: bool) -> None:
        """"""
    @overload
    def __init__(self, initialState: bool, spinCount: int) -> None:
        """"""
    @property
    def IsSet(self) -> bool:
        """"""
    @property
    def SpinCount(self) -> int:
        """"""
    @property
    def WaitHandle(self) -> WaitHandle:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Reset(self) -> None:
        """"""
    def Set(self) -> None:
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
    @overload
    def Wait(self, timeout: TimeSpan, cancellationToken: CancellationToken) -> bool:
        """"""

class Monitor(ABC, Object):
    """"""
    @classmethod
    @overload
    def Enter(cls, obj: object) -> None:
        """"""
    @classmethod
    @overload
    def Enter(cls, obj: object, lockTaken: Boolean) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def Exit(cls, obj: object) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsEntered(cls, obj: object) -> bool:
        """"""
    @classmethod
    def Pulse(cls, obj: object) -> None:
        """"""
    @classmethod
    def PulseAll(cls, obj: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def TryEnter(cls, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def TryEnter(cls, obj: object, lockTaken: Boolean) -> None:
        """"""
    @classmethod
    @overload
    def TryEnter(cls, obj: object, millisecondsTimeout: int) -> bool:
        """"""
    @classmethod
    @overload
    def TryEnter(cls, obj: object, millisecondsTimeout: int, lockTaken: Boolean) -> None:
        """"""
    @classmethod
    @overload
    def TryEnter(cls, obj: object, timeout: TimeSpan) -> bool:
        """"""
    @classmethod
    @overload
    def TryEnter(cls, obj: object, timeout: TimeSpan, lockTaken: Boolean) -> None:
        """"""
    @classmethod
    @overload
    def Wait(cls, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def Wait(cls, obj: object, millisecondsTimeout: int) -> bool:
        """"""
    @classmethod
    @overload
    def Wait(cls, obj: object, millisecondsTimeout: int, exitContext: bool) -> bool:
        """"""
    @classmethod
    @overload
    def Wait(cls, obj: object, timeout: TimeSpan) -> bool:
        """"""
    @classmethod
    @overload
    def Wait(cls, obj: object, timeout: TimeSpan, exitContext: bool) -> bool:
        """"""

class Mutex(WaitHandle, IDisposable):
    """"""
    @overload
    def __init__(self, initiallyOwned: bool, name: str, createdNew: Boolean) -> None:
        """"""
    @overload
    def __init__(
        self, initiallyOwned: bool, name: str, createdNew: Boolean, mutexSecurity: MutexSecurity
    ) -> None:
        """"""
    @overload
    def __init__(self, initiallyOwned: bool, name: str) -> None:
        """"""
    @overload
    def __init__(self, initiallyOwned: bool) -> None:
        """"""
    @overload
    def __init__(self) -> None:
        """"""
    @property
    def Handle(self) -> IntPtr:
        """"""
    @Handle.setter
    def Handle(self, value: IntPtr) -> None: ...
    @property
    def SafeWaitHandle(self) -> SafeWaitHandle:
        """"""
    @SafeWaitHandle.setter
    def SafeWaitHandle(self, value: SafeWaitHandle) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAccessControl(self) -> MutexSecurity:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    @classmethod
    @overload
    def OpenExisting(cls, name: str) -> Mutex:
        """"""
    @classmethod
    @overload
    def OpenExisting(cls, name: str, rights: MutexRights) -> Mutex:
        """"""
    def ReleaseMutex(self) -> None:
        """"""
    def SetAccessControl(self, mutexSecurity: MutexSecurity) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def TryOpenExisting(cls, name: str, rights: MutexRights, result: Mutex) -> tuple[bool, Mutex]:
        """"""
    @classmethod
    @overload
    def TryOpenExisting(cls, name: str, result: Mutex) -> tuple[bool, Mutex]:
        """"""
    @overload
    def WaitOne(self) -> bool:
        """"""
    @overload
    def WaitOne(self, millisecondsTimeout: int) -> bool:
        """"""
    @overload
    def WaitOne(self, millisecondsTimeout: int, exitContext: bool) -> bool:
        """"""
    @overload
    def WaitOne(self, timeout: TimeSpan) -> bool:
        """"""
    @overload
    def WaitOne(self, timeout: TimeSpan, exitContext: bool) -> bool:
        """"""

class NativeOverlapped(ValueType):
    """"""

    EventHandle: Final[IntPtr]
    """"""
    InternalHigh: Final[IntPtr]
    """"""
    InternalLow: Final[IntPtr]
    """"""
    OffsetHigh: Final[int]
    """"""
    OffsetLow: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Overlapped(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, offsetLo: int, offsetHi: int, hEvent: IntPtr, ar: IAsyncResult) -> None:
        """"""
    @overload
    def __init__(self, offsetLo: int, offsetHi: int, hEvent: int, ar: IAsyncResult) -> None:
        """"""
    @property
    def AsyncResult(self) -> IAsyncResult:
        """"""
    @AsyncResult.setter
    def AsyncResult(self, value: IAsyncResult) -> None: ...
    @property
    def EventHandle(self) -> int:
        """"""
    @EventHandle.setter
    def EventHandle(self, value: int) -> None: ...
    @property
    def EventHandleIntPtr(self) -> IntPtr:
        """"""
    @EventHandleIntPtr.setter
    def EventHandleIntPtr(self, value: IntPtr) -> None: ...
    @property
    def OffsetHigh(self) -> int:
        """"""
    @OffsetHigh.setter
    def OffsetHigh(self, value: int) -> None: ...
    @property
    def OffsetLow(self) -> int:
        """"""
    @OffsetLow.setter
    def OffsetLow(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def Free(cls, nativeOverlappedPtr: NativeOverlapped) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Pack(self, iocb: IOCompletionCallback) -> NativeOverlapped:
        """"""
    @overload
    def Pack(self, iocb: IOCompletionCallback, userData: object) -> NativeOverlapped:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def Unpack(cls, nativeOverlappedPtr: NativeOverlapped) -> Overlapped:
        """"""
    @overload
    def UnsafePack(self, iocb: IOCompletionCallback) -> NativeOverlapped:
        """"""
    @overload
    def UnsafePack(self, iocb: IOCompletionCallback, userData: object) -> NativeOverlapped:
        """"""

class OverlappedData(Object):
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

ParameterizedThreadStart: Callable[[object], None] = ...
""""""

class PinnableBufferCache(Object):
    """"""
    def __init__(self, cacheName: str, numberOfElements: int) -> None:
        """"""
    def AllocateBuffer(self) -> Array[int]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FreeBuffer(self, buffer: Array[int]) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PinnableBufferCacheEventSource(EventSource, IDisposable):
    """"""

    Log: ClassVar[PinnableBufferCacheEventSource]
    """"""
    def __init__(self) -> None:
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
    def AgePendingBuffersResults(
        self, cacheName: str, promotedToFreeListCount: int, heldBackCount: int
    ) -> None:
        """"""
    def AllocateBuffer(
        self, cacheName: str, objectId: int, objectHash: int, objectGen: int, freeCountAfter: int
    ) -> None:
        """"""
    def AllocateBufferAged(self, cacheName: str, agedCount: int) -> None:
        """"""
    def AllocateBufferCreatingNewBuffers(
        self, cacheName: str, totalBuffsBefore: int, objectCount: int
    ) -> None:
        """"""
    def AllocateBufferFreeListEmpty(self, cacheName: str, notGen2CountBefore: int) -> None:
        """"""
    def AllocateBufferFromNotGen2(self, cacheName: str, notGen2CountAfter: int) -> None:
        """"""
    def Create(self, cacheName: str) -> None:
        """"""
    def DebugMessage(self, message: str) -> None:
        """"""
    def DebugMessage1(self, message: str, value: int) -> None:
        """"""
    def DebugMessage2(self, message: str, value1: int, value2: int) -> None:
        """"""
    def DebugMessage3(self, message: str, value1: int, value2: int, value3: int) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FreeBuffer(
        self, cacheName: str, objectId: int, objectHash: int, freeCountBefore: int
    ) -> None:
        """"""
    def FreeBufferNull(self, cacheName: str, freeCountBefore: int) -> None:
        """"""
    def FreeBufferStillTooYoung(self, cacheName: str, notGen2CountBefore: int) -> None:
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
    def ToString(self) -> str:
        """"""
    def TrimCheck(
        self, cacheName: str, totalBuffs: int, neededMoreThanFreeList: bool, deltaMSec: int
    ) -> None:
        """"""
    def TrimExperiment(
        self, cacheName: str, totalBuffs: int, freeListCount: int, numTrimTrial: int
    ) -> None:
        """"""
    def TrimFlush(
        self, cacheName: str, totalBuffs: int, freeListCount: int, notGen2CountBefore: int
    ) -> None:
        """"""
    def TrimFree(self, cacheName: str, totalBuffs: int, freeListCount: int, toBeFreed: int) -> None:
        """"""
    def TrimFreeSizeOK(self, cacheName: str, totalBuffs: int, freeListCount: int) -> None:
        """"""
    def WalkFreeListResult(
        self, cacheName: str, freeListCount: int, gen0BuffersInFreeList: int
    ) -> None:
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

class PlatformHelper(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PreAllocatedOverlapped(Object, IDeferredDisposable, IDisposable):
    """"""
    def __init__(self, callback: IOCompletionCallback, state: object, pinData: object) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def OnFinalRelease(self, disposed: bool) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class QueueUserWorkItemCallback(Object, IThreadPoolWorkItem):
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

class ReaderWriterCount(Object):
    """"""

    lockID: Final[int]
    """"""
    next: Final[ReaderWriterCount]
    """"""
    readercount: Final[int]
    """"""
    upgradecount: Final[int]
    """"""
    writercount: Final[int]
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

class ReaderWriterLock(CriticalFinalizerObject):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def IsReaderLockHeld(self) -> bool:
        """"""
    @property
    def IsWriterLockHeld(self) -> bool:
        """"""
    @property
    def WriterSeqNum(self) -> int:
        """"""
    @overload
    def AcquireReaderLock(self, millisecondsTimeout: int) -> None:
        """"""
    @overload
    def AcquireReaderLock(self, timeout: TimeSpan) -> None:
        """"""
    @overload
    def AcquireWriterLock(self, millisecondsTimeout: int) -> None:
        """"""
    @overload
    def AcquireWriterLock(self, timeout: TimeSpan) -> None:
        """"""
    def AnyWritersSince(self, seqNum: int) -> bool:
        """"""
    def DowngradeFromWriterLock(self, lockCookie: LockCookie) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ReleaseLock(self) -> LockCookie:
        """"""
    def ReleaseReaderLock(self) -> None:
        """"""
    def ReleaseWriterLock(self) -> None:
        """"""
    def RestoreLock(self, lockCookie: LockCookie) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def UpgradeToWriterLock(self, millisecondsTimeout: int) -> LockCookie:
        """"""
    @overload
    def UpgradeToWriterLock(self, timeout: TimeSpan) -> LockCookie:
        """"""

class ReaderWriterLockSlim(Object, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, recursionPolicy: LockRecursionPolicy) -> None:
        """"""
    @property
    def CurrentReadCount(self) -> int:
        """"""
    @property
    def IsReadLockHeld(self) -> bool:
        """"""
    @property
    def IsUpgradeableReadLockHeld(self) -> bool:
        """"""
    @property
    def IsWriteLockHeld(self) -> bool:
        """"""
    @property
    def RecursionPolicy(self) -> LockRecursionPolicy:
        """"""
    @property
    def RecursiveReadCount(self) -> int:
        """"""
    @property
    def RecursiveUpgradeCount(self) -> int:
        """"""
    @property
    def RecursiveWriteCount(self) -> int:
        """"""
    @property
    def WaitingReadCount(self) -> int:
        """"""
    @property
    def WaitingUpgradeCount(self) -> int:
        """"""
    @property
    def WaitingWriteCount(self) -> int:
        """"""
    def Dispose(self) -> None:
        """"""
    def EnterReadLock(self) -> None:
        """"""
    def EnterUpgradeableReadLock(self) -> None:
        """"""
    def EnterWriteLock(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExitReadLock(self) -> None:
        """"""
    def ExitUpgradeableReadLock(self) -> None:
        """"""
    def ExitWriteLock(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def TryEnterReadLock(self, millisecondsTimeout: int) -> bool:
        """"""
    @overload
    def TryEnterReadLock(self, timeout: TimeSpan) -> bool:
        """"""
    @overload
    def TryEnterUpgradeableReadLock(self, millisecondsTimeout: int) -> bool:
        """"""
    @overload
    def TryEnterUpgradeableReadLock(self, timeout: TimeSpan) -> bool:
        """"""
    @overload
    def TryEnterWriteLock(self, millisecondsTimeout: int) -> bool:
        """"""
    @overload
    def TryEnterWriteLock(self, timeout: TimeSpan) -> bool:
        """"""

class RegisteredWaitHandle(MarshalByRefObject):
    """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def ToString(self) -> str:
        """"""
    def Unregister(self, waitObject: WaitHandle) -> bool:
        """"""

class RegisteredWaitHandleSafe(CriticalFinalizerObject):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SafeCompressedStackHandle(SafeHandle, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class Semaphore(WaitHandle, IDisposable):
    """"""
    @overload
    def __init__(self, initialCount: int, maximumCount: int) -> None:
        """"""
    @overload
    def __init__(self, initialCount: int, maximumCount: int, name: str) -> None:
        """"""
    @overload
    def __init__(
        self, initialCount: int, maximumCount: int, name: str, createdNew: Boolean
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        initialCount: int,
        maximumCount: int,
        name: str,
        createdNew: Boolean,
        semaphoreSecurity: SemaphoreSecurity,
    ) -> None:
        """"""
    @property
    def Handle(self) -> IntPtr:
        """"""
    @Handle.setter
    def Handle(self, value: IntPtr) -> None: ...
    @property
    def SafeWaitHandle(self) -> SafeWaitHandle:
        """"""
    @SafeWaitHandle.setter
    def SafeWaitHandle(self, value: SafeWaitHandle) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAccessControl(self) -> SemaphoreSecurity:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    @classmethod
    @overload
    def OpenExisting(cls, name: str) -> Semaphore:
        """"""
    @classmethod
    @overload
    def OpenExisting(cls, name: str, rights: SemaphoreRights) -> Semaphore:
        """"""
    @overload
    def Release(self) -> int:
        """"""
    @overload
    def Release(self, releaseCount: int) -> int:
        """"""
    def SetAccessControl(self, semaphoreSecurity: SemaphoreSecurity) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def TryOpenExisting(
        cls, name: str, rights: SemaphoreRights, result: Semaphore
    ) -> tuple[bool, Semaphore]:
        """"""
    @classmethod
    @overload
    def TryOpenExisting(cls, name: str, result: Semaphore) -> tuple[bool, Semaphore]:
        """"""
    @overload
    def WaitOne(self) -> bool:
        """"""
    @overload
    def WaitOne(self, millisecondsTimeout: int) -> bool:
        """"""
    @overload
    def WaitOne(self, millisecondsTimeout: int, exitContext: bool) -> bool:
        """"""
    @overload
    def WaitOne(self, timeout: TimeSpan) -> bool:
        """"""
    @overload
    def WaitOne(self, timeout: TimeSpan, exitContext: bool) -> bool:
        """"""

class SemaphoreFullException(SystemException, _Exception, ISerializable):
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

class SemaphoreSlim(Object, IDisposable):
    """"""
    @overload
    def __init__(self, initialCount: int) -> None:
        """"""
    @overload
    def __init__(self, initialCount: int, maxCount: int) -> None:
        """"""
    @property
    def AvailableWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CurrentCount(self) -> int:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Release(self) -> int:
        """"""
    @overload
    def Release(self, releaseCount: int) -> int:
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
    @overload
    def Wait(self, timeout: TimeSpan, cancellationToken: CancellationToken) -> bool:
        """"""
    @overload
    def WaitAsync(self) -> Task:
        """"""
    @overload
    def WaitAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    @overload
    def WaitAsync(self, millisecondsTimeout: int) -> Task[bool]:
        """"""
    @overload
    def WaitAsync(
        self, millisecondsTimeout: int, cancellationToken: CancellationToken
    ) -> Task[bool]:
        """"""
    @overload
    def WaitAsync(self, timeout: TimeSpan) -> Task[bool]:
        """"""
    @overload
    def WaitAsync(self, timeout: TimeSpan, cancellationToken: CancellationToken) -> Task[bool]:
        """"""

SendOrPostCallback: Callable[[object], None] = ...
""""""

class SparselyPopulatedArrayAddInfo[T](ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SparselyPopulatedArrayFragment[T](Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SparselyPopulatedArray[T](Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SpinLock(ValueType):
    """"""
    def __init__(self, enableThreadOwnerTracking: bool) -> None:
        """"""
    @property
    def IsHeld(self) -> bool:
        """"""
    @property
    def IsHeldByCurrentThread(self) -> bool:
        """"""
    @property
    def IsThreadOwnerTrackingEnabled(self) -> bool:
        """"""
    def Enter(self, lockTaken: Boolean) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Exit(self) -> None:
        """"""
    @overload
    def Exit(self, useMemoryBarrier: bool) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def TryEnter(self, lockTaken: Boolean) -> None:
        """"""
    @overload
    def TryEnter(self, millisecondsTimeout: int, lockTaken: Boolean) -> None:
        """"""
    @overload
    def TryEnter(self, timeout: TimeSpan, lockTaken: Boolean) -> None:
        """"""

class SpinWait(ValueType):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def NextSpinWillYield(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Reset(self) -> None:
        """"""
    def SpinOnce(self) -> None:
        """"""
    @classmethod
    @overload
    def SpinUntil(cls, condition: Func[bool]) -> None:
        """"""
    @classmethod
    @overload
    def SpinUntil(cls, condition: Func[bool], millisecondsTimeout: int) -> bool:
        """"""
    @classmethod
    @overload
    def SpinUntil(cls, condition: Func[bool], timeout: TimeSpan) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def __len__(self) -> int:
        """"""

class StackCrawlMark(Enum):
    """"""

    LookForMe: StackCrawlMark = ...
    """"""
    LookForMyCaller: StackCrawlMark = ...
    """"""
    LookForMyCallersCaller: StackCrawlMark = ...
    """"""
    LookForThread: StackCrawlMark = ...
    """"""

class SynchronizationContext(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @classmethod
    @property
    def Current(cls) -> SynchronizationContext:
        """"""
    def CreateCopy(self) -> SynchronizationContext:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsWaitNotificationRequired(self) -> bool:
        """"""
    def OperationCompleted(self) -> None:
        """"""
    def OperationStarted(self) -> None:
        """"""
    def Post(self, d: SendOrPostCallback, state: object) -> None:
        """"""
    def Send(self, d: SendOrPostCallback, state: object) -> None:
        """"""
    @classmethod
    def SetSynchronizationContext(cls, syncContext: SynchronizationContext) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Wait(self, waitHandles: Array[IntPtr], waitAll: bool, millisecondsTimeout: int) -> int:
        """"""

class SynchronizationContextProperties(Enum):
    """"""

    _None: SynchronizationContextProperties = ...
    """"""
    RequireWaitNotification: SynchronizationContextProperties = ...
    """"""

class SynchronizationLockException(SystemException, _Exception, ISerializable):
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

class SystemThreading_ThreadLocalDebugView[T](Object):
    """"""
    def __init__(self, tlocal: ThreadLocal[T]) -> None:
        """"""
    @property
    def IsValueCreated(self) -> bool:
        """"""
    @property
    def Value(self) -> T:
        """"""
    @property
    def Values(self) -> List[T]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Thread(CriticalFinalizerObject, _Thread):
    """"""
    @overload
    def __init__(self, start: ThreadStart) -> None:
        """"""
    @overload
    def __init__(self, start: ThreadStart, maxStackSize: int) -> None:
        """"""
    @overload
    def __init__(self, start: ParameterizedThreadStart) -> None:
        """"""
    @overload
    def __init__(self, start: ParameterizedThreadStart, maxStackSize: int) -> None:
        """"""
    @property
    def ApartmentState(self) -> ApartmentState:
        """"""
    @ApartmentState.setter
    def ApartmentState(self, value: ApartmentState) -> None: ...
    @classmethod
    @property
    def CurrentContext(cls) -> Context:
        """"""
    @property
    def CurrentCulture(self) -> CultureInfo:
        """"""
    @CurrentCulture.setter
    def CurrentCulture(self, value: CultureInfo) -> None: ...
    @classmethod
    @property
    def CurrentPrincipal(cls) -> IPrincipal:
        """"""
    @classmethod
    @CurrentPrincipal.setter
    def CurrentPrincipal(cls, value: IPrincipal) -> None: ...
    @classmethod
    @property
    def CurrentThread(cls) -> Thread:
        """"""
    @property
    def CurrentUICulture(self) -> CultureInfo:
        """"""
    @CurrentUICulture.setter
    def CurrentUICulture(self, value: CultureInfo) -> None: ...
    @property
    def ExecutionContext(self) -> ExecutionContext:
        """"""
    @property
    def IsAlive(self) -> bool:
        """"""
    @property
    def IsBackground(self) -> bool:
        """"""
    @IsBackground.setter
    def IsBackground(self, value: bool) -> None: ...
    @property
    def IsThreadPoolThread(self) -> bool:
        """"""
    @property
    def ManagedThreadId(self) -> int:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Priority(self) -> ThreadPriority:
        """"""
    @Priority.setter
    def Priority(self, value: ThreadPriority) -> None: ...
    @property
    def ThreadState(self) -> ThreadState:
        """"""
    @overload
    def Abort(self) -> None:
        """"""
    @overload
    def Abort(self, stateInfo: object) -> None:
        """"""
    @classmethod
    def AllocateDataSlot(cls) -> LocalDataStoreSlot:
        """"""
    @classmethod
    def AllocateNamedDataSlot(cls, name: str) -> LocalDataStoreSlot:
        """"""
    @classmethod
    def BeginCriticalRegion(cls) -> None:
        """"""
    @classmethod
    def BeginThreadAffinity(cls) -> None:
        """"""
    def DisableComObjectEagerCleanup(self) -> None:
        """"""
    @classmethod
    def EndCriticalRegion(cls) -> None:
        """"""
    @classmethod
    def EndThreadAffinity(cls) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FreeNamedDataSlot(cls, name: str) -> None:
        """"""
    def GetApartmentState(self) -> ApartmentState:
        """"""
    def GetCompressedStack(self) -> CompressedStack:
        """"""
    @classmethod
    def GetData(cls, slot: LocalDataStoreSlot) -> object:
        """"""
    @classmethod
    def GetDomain(cls) -> AppDomain:
        """"""
    @classmethod
    def GetDomainID(cls) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    @classmethod
    def GetNamedDataSlot(cls, name: str) -> LocalDataStoreSlot:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Interrupt(self) -> None:
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
    @overload
    def Join(self) -> None:
        """"""
    @overload
    def Join(self, millisecondsTimeout: int) -> bool:
        """"""
    @overload
    def Join(self, timeout: TimeSpan) -> bool:
        """"""
    @classmethod
    def MemoryBarrier(cls) -> None:
        """"""
    @classmethod
    def ResetAbort(cls) -> None:
        """"""
    def Resume(self) -> None:
        """"""
    def SetApartmentState(self, state: ApartmentState) -> None:
        """"""
    def SetCompressedStack(self, stack: CompressedStack) -> None:
        """"""
    @classmethod
    def SetData(cls, slot: LocalDataStoreSlot, data: object) -> None:
        """"""
    @classmethod
    @overload
    def Sleep(cls, millisecondsTimeout: int) -> None:
        """"""
    @classmethod
    @overload
    def Sleep(cls, timeout: TimeSpan) -> None:
        """"""
    @classmethod
    def SpinWait(cls, iterations: int) -> None:
        """"""
    @overload
    def Start(self) -> None:
        """"""
    @overload
    def Start(self, parameter: object) -> None:
        """"""
    def Suspend(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TrySetApartmentState(self, state: ApartmentState) -> bool:
        """"""
    @classmethod
    @overload
    def VolatileRead(cls, address: Byte) -> int:
        """"""
    @classmethod
    @overload
    def VolatileRead(cls, address: Double) -> float:
        """"""
    @classmethod
    @overload
    def VolatileRead(cls, address: Int16) -> int:
        """"""
    @classmethod
    @overload
    def VolatileRead(cls, address: Int32) -> int:
        """"""
    @classmethod
    @overload
    def VolatileRead(cls, address: Int64) -> int:
        """"""
    @classmethod
    @overload
    def VolatileRead(cls, address: IntPtr) -> IntPtr:
        """"""
    @classmethod
    @overload
    def VolatileRead(cls, address: Object) -> object:
        """"""
    @classmethod
    @overload
    def VolatileRead(cls, address: SByte) -> int:
        """"""
    @classmethod
    @overload
    def VolatileRead(cls, address: Single) -> float:
        """"""
    @classmethod
    @overload
    def VolatileRead(cls, address: UInt16) -> int:
        """"""
    @classmethod
    @overload
    def VolatileRead(cls, address: UInt32) -> int:
        """"""
    @classmethod
    @overload
    def VolatileRead(cls, address: UInt64) -> int:
        """"""
    @classmethod
    @overload
    def VolatileRead(cls, address: UIntPtr) -> UIntPtr:
        """"""
    @classmethod
    @overload
    def VolatileWrite(cls, address: Byte, value: int) -> None:
        """"""
    @classmethod
    @overload
    def VolatileWrite(cls, address: Double, value: float) -> None:
        """"""
    @classmethod
    @overload
    def VolatileWrite(cls, address: Int16, value: int) -> None:
        """"""
    @classmethod
    @overload
    def VolatileWrite(cls, address: Int32, value: int) -> None:
        """"""
    @classmethod
    @overload
    def VolatileWrite(cls, address: Int64, value: int) -> None:
        """"""
    @classmethod
    @overload
    def VolatileWrite(cls, address: IntPtr, value: IntPtr) -> None:
        """"""
    @classmethod
    @overload
    def VolatileWrite(cls, address: Object, value: object) -> None:
        """"""
    @classmethod
    @overload
    def VolatileWrite(cls, address: SByte, value: int) -> None:
        """"""
    @classmethod
    @overload
    def VolatileWrite(cls, address: Single, value: float) -> None:
        """"""
    @classmethod
    @overload
    def VolatileWrite(cls, address: UInt16, value: int) -> None:
        """"""
    @classmethod
    @overload
    def VolatileWrite(cls, address: UInt32, value: int) -> None:
        """"""
    @classmethod
    @overload
    def VolatileWrite(cls, address: UInt64, value: int) -> None:
        """"""
    @classmethod
    @overload
    def VolatileWrite(cls, address: UIntPtr, value: UIntPtr) -> None:
        """"""
    @classmethod
    def Yield(cls) -> bool:
        """"""

class ThreadAbortException(SystemException, _Exception, ISerializable):
    """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def ExceptionState(self) -> object:
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

class ThreadExceptionEventArgs(EventArgs):
    """"""
    def __init__(self, t: Exception) -> None:
        """"""
    @property
    def Exception(self) -> Exception:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

ThreadExceptionEventHandler: Callable[[object, ThreadExceptionEventArgs], None] = ...
""""""

class ThreadHandle(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ThreadHelper(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ThreadInterruptedException(SystemException, _Exception, ISerializable):
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

class ThreadLocal[T](Object, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, trackAllValues: bool) -> None:
        """"""
    @overload
    def __init__(self, valueFactory: Func[T]) -> None:
        """"""
    @overload
    def __init__(self, valueFactory: Func[T], trackAllValues: bool) -> None:
        """"""
    @property
    def IsValueCreated(self) -> bool:
        """"""
    @property
    def Value(self) -> T:
        """"""
    @Value.setter
    def Value(self, value: T) -> None: ...
    @property
    def Values(self) -> IList[T]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ThreadPool(ABC, Object):
    """"""
    @classmethod
    @overload
    def BindHandle(cls, osHandle: SafeHandle) -> bool:
        """"""
    @classmethod
    @overload
    def BindHandle(cls, osHandle: IntPtr) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetAvailableThreads(
        cls, workerThreads: Int32, completionPortThreads: Int32
    ) -> tuple[None, Int32, Int32]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetMaxThreads(
        cls, workerThreads: Int32, completionPortThreads: Int32
    ) -> tuple[None, Int32, Int32]:
        """"""
    @classmethod
    def GetMinThreads(
        cls, workerThreads: Int32, completionPortThreads: Int32
    ) -> tuple[None, Int32, Int32]:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def QueueUserWorkItem(cls, callBack: WaitCallback) -> bool:
        """"""
    @classmethod
    @overload
    def QueueUserWorkItem(cls, callBack: WaitCallback, state: object) -> bool:
        """"""
    @classmethod
    @overload
    def RegisterWaitForSingleObject(
        cls,
        waitObject: WaitHandle,
        callBack: WaitOrTimerCallback,
        state: object,
        millisecondsTimeOutInterval: int,
        executeOnlyOnce: bool,
    ) -> RegisteredWaitHandle:
        """"""
    @classmethod
    @overload
    def RegisterWaitForSingleObject(
        cls,
        waitObject: WaitHandle,
        callBack: WaitOrTimerCallback,
        state: object,
        millisecondsTimeOutInterval: int,
        executeOnlyOnce: bool,
    ) -> RegisteredWaitHandle:
        """"""
    @classmethod
    @overload
    def RegisterWaitForSingleObject(
        cls,
        waitObject: WaitHandle,
        callBack: WaitOrTimerCallback,
        state: object,
        timeout: TimeSpan,
        executeOnlyOnce: bool,
    ) -> RegisteredWaitHandle:
        """"""
    @classmethod
    @overload
    def RegisterWaitForSingleObject(
        cls,
        waitObject: WaitHandle,
        callBack: WaitOrTimerCallback,
        state: object,
        millisecondsTimeOutInterval: int,
        executeOnlyOnce: bool,
    ) -> RegisteredWaitHandle:
        """"""
    @classmethod
    def SetMaxThreads(cls, workerThreads: int, completionPortThreads: int) -> bool:
        """"""
    @classmethod
    def SetMinThreads(cls, workerThreads: int, completionPortThreads: int) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def UnsafeQueueNativeOverlapped(cls, overlapped: NativeOverlapped) -> bool:
        """"""
    @classmethod
    def UnsafeQueueUserWorkItem(cls, callBack: WaitCallback, state: object) -> bool:
        """"""
    @classmethod
    @overload
    def UnsafeRegisterWaitForSingleObject(
        cls,
        waitObject: WaitHandle,
        callBack: WaitOrTimerCallback,
        state: object,
        millisecondsTimeOutInterval: int,
        executeOnlyOnce: bool,
    ) -> RegisteredWaitHandle:
        """"""
    @classmethod
    @overload
    def UnsafeRegisterWaitForSingleObject(
        cls,
        waitObject: WaitHandle,
        callBack: WaitOrTimerCallback,
        state: object,
        millisecondsTimeOutInterval: int,
        executeOnlyOnce: bool,
    ) -> RegisteredWaitHandle:
        """"""
    @classmethod
    @overload
    def UnsafeRegisterWaitForSingleObject(
        cls,
        waitObject: WaitHandle,
        callBack: WaitOrTimerCallback,
        state: object,
        timeout: TimeSpan,
        executeOnlyOnce: bool,
    ) -> RegisteredWaitHandle:
        """"""
    @classmethod
    @overload
    def UnsafeRegisterWaitForSingleObject(
        cls,
        waitObject: WaitHandle,
        callBack: WaitOrTimerCallback,
        state: object,
        millisecondsTimeOutInterval: int,
        executeOnlyOnce: bool,
    ) -> RegisteredWaitHandle:
        """"""

class ThreadPoolBoundHandle(Object, IDisposable):
    """"""
    @property
    def Handle(self) -> SafeHandle:
        """"""
    @overload
    def AllocateNativeOverlapped(
        self, callback: IOCompletionCallback, state: object, pinData: object
    ) -> NativeOverlapped:
        """"""
    @overload
    def AllocateNativeOverlapped(self, preAllocated: PreAllocatedOverlapped) -> NativeOverlapped:
        """"""
    @classmethod
    def BindHandle(cls, handle: SafeHandle) -> ThreadPoolBoundHandle:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FreeNativeOverlapped(self, overlapped: NativeOverlapped) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetNativeOverlappedState(cls, overlapped: NativeOverlapped) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ThreadPoolBoundHandleOverlapped(Overlapped):
    """"""
    def __init__(
        self,
        callback: IOCompletionCallback,
        state: object,
        pinData: object,
        preAllocated: PreAllocatedOverlapped,
    ) -> None:
        """"""
    @property
    def AsyncResult(self) -> IAsyncResult:
        """"""
    @AsyncResult.setter
    def AsyncResult(self, value: IAsyncResult) -> None: ...
    @property
    def EventHandle(self) -> int:
        """"""
    @EventHandle.setter
    def EventHandle(self, value: int) -> None: ...
    @property
    def EventHandleIntPtr(self) -> IntPtr:
        """"""
    @EventHandleIntPtr.setter
    def EventHandleIntPtr(self, value: IntPtr) -> None: ...
    @property
    def OffsetHigh(self) -> int:
        """"""
    @OffsetHigh.setter
    def OffsetHigh(self, value: int) -> None: ...
    @property
    def OffsetLow(self) -> int:
        """"""
    @OffsetLow.setter
    def OffsetLow(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Pack(self, iocb: IOCompletionCallback) -> NativeOverlapped:
        """"""
    @overload
    def Pack(self, iocb: IOCompletionCallback, userData: object) -> NativeOverlapped:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def UnsafePack(self, iocb: IOCompletionCallback) -> NativeOverlapped:
        """"""
    @overload
    def UnsafePack(self, iocb: IOCompletionCallback, userData: object) -> NativeOverlapped:
        """"""

class ThreadPoolGlobals(ABC, Object):
    """"""

    enableWorkerTracking: ClassVar[bool]
    """"""
    processorCount: ClassVar[int]
    """"""
    tpHosted: ClassVar[bool]
    """"""
    tpQuantum: ClassVar[int]
    """"""
    vmTpInitialized: ClassVar[bool]
    """"""
    workQueue: ClassVar[ThreadPoolWorkQueue]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ThreadPoolWorkQueue(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Dequeue(
        self,
        tl: ThreadPoolWorkQueueThreadLocals,
        callback: IThreadPoolWorkItem,
        missedSteal: Boolean,
    ) -> tuple[None, IThreadPoolWorkItem, Boolean]:
        """"""
    def Enqueue(self, callback: IThreadPoolWorkItem, forceGlobal: bool) -> None:
        """"""
    def EnsureCurrentThreadHasQueue(self) -> ThreadPoolWorkQueueThreadLocals:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ThreadPoolWorkQueueThreadLocals(Object):
    """"""

    random: Final[Random]
    """"""
    threadLocals: ClassVar[ThreadPoolWorkQueueThreadLocals]
    """"""
    workQueue: Final[ThreadPoolWorkQueue]
    """"""
    workStealingQueue: Final[ThreadPoolWorkQueue.WorkStealingQueue]
    """"""
    def __init__(self, tpq: ThreadPoolWorkQueue) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ThreadPriority(Enum):
    """"""

    Lowest: ThreadPriority = ...
    """"""
    BelowNormal: ThreadPriority = ...
    """"""
    Normal: ThreadPriority = ...
    """"""
    AboveNormal: ThreadPriority = ...
    """"""
    Highest: ThreadPriority = ...
    """"""

ThreadStart: Callable[[], None] = ...
""""""

class ThreadStartException(SystemException, _Exception, ISerializable):
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

class ThreadState(Enum):
    """"""

    Running: ThreadState = ...
    """"""
    StopRequested: ThreadState = ...
    """"""
    SuspendRequested: ThreadState = ...
    """"""
    Background: ThreadState = ...
    """"""
    Unstarted: ThreadState = ...
    """"""
    Stopped: ThreadState = ...
    """"""
    WaitSleepJoin: ThreadState = ...
    """"""
    Suspended: ThreadState = ...
    """"""
    AbortRequested: ThreadState = ...
    """"""
    Aborted: ThreadState = ...
    """"""

class ThreadStateException(SystemException, _Exception, ISerializable):
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

class Timeout(ABC, Object):
    """"""

    Infinite: ClassVar[int]
    """"""
    InfiniteTimeSpan: ClassVar[TimeSpan]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TimeoutHelper(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetTime(cls) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def UpdateTimeOut(cls, startTime: int, originalWaitMillisecondsTimeout: int) -> int:
        """"""

class Timer(MarshalByRefObject, IDisposable):
    """"""
    @overload
    def __init__(self, callback: TimerCallback, state: object, dueTime: int, period: int) -> None:
        """"""
    @overload
    def __init__(
        self, callback: TimerCallback, state: object, dueTime: TimeSpan, period: TimeSpan
    ) -> None:
        """"""
    @overload
    def __init__(self, callback: TimerCallback, state: object, dueTime: int, period: int) -> None:
        """"""
    @overload
    def __init__(self, callback: TimerCallback, state: object, dueTime: int, period: int) -> None:
        """"""
    @overload
    def __init__(self, callback: TimerCallback) -> None:
        """"""
    @overload
    def Change(self, dueTime: int, period: int) -> bool:
        """"""
    @overload
    def Change(self, dueTime: int, period: int) -> bool:
        """"""
    @overload
    def Change(self, dueTime: TimeSpan, period: TimeSpan) -> bool:
        """"""
    @overload
    def Change(self, dueTime: int, period: int) -> bool:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    @overload
    def Dispose(self) -> None:
        """"""
    @overload
    def Dispose(self, notifyObject: WaitHandle) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def ToString(self) -> str:
        """"""

TimerCallback: Callable[[object], None] = ...
""""""

class TimerHolder(Object):
    """"""
    def __init__(self, timer: object) -> None:
        """"""
    def Change(self, dueTime: int, period: int) -> bool:
        """"""
    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, notifyObject: WaitHandle) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TimerQueue(Object):
    """"""
    @classmethod
    @property
    def Instance(cls) -> TimerQueue:
        """"""
    def DeleteTimer(self, timer: TimerQueueTimer) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def UpdateTimer(self, timer: TimerQueueTimer, dueTime: int, period: int) -> bool:
        """"""

class TimerQueueTimer(Object):
    """"""
    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, toSignal: WaitHandle) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Volatile(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def Read[T](cls, location: T) -> T:
        """"""
    @classmethod
    @overload
    def Read(cls, location: Boolean) -> bool:
        """"""
    @classmethod
    @overload
    def Read(cls, location: Byte) -> int:
        """"""
    @classmethod
    @overload
    def Read(cls, location: Double) -> float:
        """"""
    @classmethod
    @overload
    def Read(cls, location: Int16) -> int:
        """"""
    @classmethod
    @overload
    def Read(cls, location: Int32) -> int:
        """"""
    @classmethod
    @overload
    def Read(cls, location: Int64) -> int:
        """"""
    @classmethod
    @overload
    def Read(cls, location: IntPtr) -> IntPtr:
        """"""
    @classmethod
    @overload
    def Read(cls, location: SByte) -> int:
        """"""
    @classmethod
    @overload
    def Read(cls, location: Single) -> float:
        """"""
    @classmethod
    @overload
    def Read(cls, location: UInt16) -> int:
        """"""
    @classmethod
    @overload
    def Read(cls, location: UInt32) -> int:
        """"""
    @classmethod
    @overload
    def Read(cls, location: UInt64) -> int:
        """"""
    @classmethod
    @overload
    def Read(cls, location: UIntPtr) -> UIntPtr:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def Write[T](cls, location: T, value: T) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, location: Boolean, value: bool) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, location: Byte, value: int) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, location: Double, value: float) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, location: Int16, value: int) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, location: Int32, value: int) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, location: Int64, value: int) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, location: IntPtr, value: IntPtr) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, location: SByte, value: int) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, location: Single, value: float) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, location: UInt16, value: int) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, location: UInt32, value: int) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, location: UInt64, value: int) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, location: UIntPtr, value: UIntPtr) -> None:
        """"""

WaitCallback: Callable[[object], None] = ...
""""""

class WaitHandle(ABC, MarshalByRefObject, IDisposable):
    """"""

    WaitTimeout: ClassVar[int]
    """"""
    @property
    def Handle(self) -> IntPtr:
        """"""
    @Handle.setter
    def Handle(self, value: IntPtr) -> None: ...
    @property
    def SafeWaitHandle(self) -> SafeWaitHandle:
        """"""
    @SafeWaitHandle.setter
    def SafeWaitHandle(self, value: SafeWaitHandle) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    @classmethod
    @overload
    def SignalAndWait(cls, toSignal: WaitHandle, toWaitOn: WaitHandle) -> bool:
        """"""
    @classmethod
    @overload
    def SignalAndWait(
        cls, toSignal: WaitHandle, toWaitOn: WaitHandle, millisecondsTimeout: int, exitContext: bool
    ) -> bool:
        """"""
    @classmethod
    @overload
    def SignalAndWait(
        cls, toSignal: WaitHandle, toWaitOn: WaitHandle, timeout: TimeSpan, exitContext: bool
    ) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def WaitAll(cls, waitHandles: Array[WaitHandle]) -> bool:
        """"""
    @classmethod
    @overload
    def WaitAll(cls, waitHandles: Array[WaitHandle], millisecondsTimeout: int) -> bool:
        """"""
    @classmethod
    @overload
    def WaitAll(
        cls, waitHandles: Array[WaitHandle], millisecondsTimeout: int, exitContext: bool
    ) -> bool:
        """"""
    @classmethod
    @overload
    def WaitAll(cls, waitHandles: Array[WaitHandle], timeout: TimeSpan) -> bool:
        """"""
    @classmethod
    @overload
    def WaitAll(cls, waitHandles: Array[WaitHandle], timeout: TimeSpan, exitContext: bool) -> bool:
        """"""
    @classmethod
    @overload
    def WaitAny(cls, waitHandles: Array[WaitHandle]) -> int:
        """"""
    @classmethod
    @overload
    def WaitAny(cls, waitHandles: Array[WaitHandle], millisecondsTimeout: int) -> int:
        """"""
    @classmethod
    @overload
    def WaitAny(
        cls, waitHandles: Array[WaitHandle], millisecondsTimeout: int, exitContext: bool
    ) -> int:
        """"""
    @classmethod
    @overload
    def WaitAny(cls, waitHandles: Array[WaitHandle], timeout: TimeSpan) -> int:
        """"""
    @classmethod
    @overload
    def WaitAny(cls, waitHandles: Array[WaitHandle], timeout: TimeSpan, exitContext: bool) -> int:
        """"""
    @overload
    def WaitOne(self) -> bool:
        """"""
    @overload
    def WaitOne(self, millisecondsTimeout: int) -> bool:
        """"""
    @overload
    def WaitOne(self, millisecondsTimeout: int, exitContext: bool) -> bool:
        """"""
    @overload
    def WaitOne(self, timeout: TimeSpan) -> bool:
        """"""
    @overload
    def WaitOne(self, timeout: TimeSpan, exitContext: bool) -> bool:
        """"""

class WaitHandleCannotBeOpenedException(ApplicationException, _Exception, ISerializable):
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

class WaitHandleExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetSafeWaitHandle(cls, waitHandle: WaitHandle) -> SafeWaitHandle:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def SetSafeWaitHandle(cls, waitHandle: WaitHandle, value: SafeWaitHandle) -> None:
        """"""
    def ToString(self) -> str:
        """"""

WaitOrTimerCallback: Callable[[object, bool], None] = ...
""""""

class WinRTSynchronizationContextFactoryBase(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Create(self, coreDispatcher: object) -> SynchronizationContext:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class _IOCompletionCallback(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class _ThreadPoolWaitCallback(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class _ThreadPoolWaitOrTimerCallback(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
