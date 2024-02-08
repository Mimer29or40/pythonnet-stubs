from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Tuple
from typing import TypeVar
from typing import overload

from Microsoft.Win32.SafeHandles import SafeWaitHandle
from System import Action
from System import AppDomain
from System import ApplicationException
from System import Array
from System import Enum
from System import EventArgs
from System import EventHandler
from System import Exception
from System import Func
from System import Guid
from System import IAsyncResult
from System import IDisposable
from System import IEquatable
from System import IntPtr
from System import LocalDataStoreSlot
from System import MarshalByRefObject
from System import Object
from System import Random
from System import SystemException
from System import TimeSpan
from System import Type
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
from System.Threading.ThreadPoolWorkQueue import WorkStealingQueue

T = TypeVar("T")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class AbandonedMutexException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, location: int, handle: WaitHandle):
        """

        :param location:
        :param handle:
        """
    @overload
    def __init__(self, message: str, inner: Exception):
        """

        :param message:
        :param inner:
        """
    @overload
    def __init__(self, message: str, location: int, handle: WaitHandle):
        """

        :param message:
        :param location:
        :param handle:
        """
    @overload
    def __init__(self, message: str, inner: Exception, location: int, handle: WaitHandle):
        """

        :param message:
        :param inner:
        :param location:
        :param handle:
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
    def Mutex(self) -> Mutex:
        """

        :return:
        """
    @property
    def MutexIndex(self) -> int:
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
    def Undo(self) -> None:
        """"""
    def __eq__(self, other: AsyncFlowControl) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: AsyncFlowControl) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, a: AsyncFlowControl, b: AsyncFlowControl) -> bool:
        """

        :param a:
        :param b:
        :return:
        """
    @classmethod
    def op_Inequality(cls, a: AsyncFlowControl, b: AsyncFlowControl) -> bool:
        """

        :param a:
        :param b:
        :return:
        """

class AsyncLocalValueChangedArgs(Generic[T], ValueType):
    """"""

    @property
    def CurrentValue(self) -> T:
        """

        :return:
        """
    @property
    def PreviousValue(self) -> T:
        """

        :return:
        """
    @property
    def ThreadContextChanged(self) -> bool:
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

class AsyncLocalValueMap(ABC, Object):
    """"""

    @classmethod
    @property
    def Empty(cls) -> IAsyncLocalValueMap:
        """

        :return:
        """
    @classmethod
    def Create(
        cls, key: IAsyncLocal, value: object, treatNullValueAsNonexistent: bool
    ) -> IAsyncLocalValueMap:
        """

        :param key:
        :param value:
        :param treatNullValueAsNonexistent:
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
    def IsEmpty(cls, asyncLocalValueMap: IAsyncLocalValueMap) -> bool:
        """

        :param asyncLocalValueMap:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class AsyncLocal(Generic[T], Object, IAsyncLocal):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, valueChangedHandler: Action[AsyncLocalValueChangedArgs[T]]):
        """

        :param valueChangedHandler:
        """
    @property
    def Value(self) -> T:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: T) -> None: ...
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
    def OnValueChanged(
        self, previousValue: object, currentValue: object, contextChanged: bool
    ) -> None:
        """

        :param previousValue:
        :param currentValue:
        :param contextChanged:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class AutoResetEvent(EventWaitHandle, IDisposable):
    """"""

    def __init__(self, initialState: bool):
        """

        :param initialState:
        """
    @property
    def Handle(self) -> IntPtr:
        """

        :return:
        """
    @Handle.setter
    def Handle(self, value: IntPtr) -> None: ...
    @property
    def SafeWaitHandle(self) -> SafeWaitHandle:
        """

        :return:
        """
    @SafeWaitHandle.setter
    def SafeWaitHandle(self, value: SafeWaitHandle) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAccessControl(self) -> EventWaitHandleSecurity:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Reset(self) -> bool:
        """

        :return:
        """
    def Set(self) -> bool:
        """

        :return:
        """
    def SetAccessControl(self, eventSecurity: EventWaitHandleSecurity) -> None:
        """

        :param eventSecurity:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def WaitOne(self) -> bool:
        """

        :return:
        """
    @overload
    def WaitOne(self, millisecondsTimeout: int) -> bool:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def WaitOne(self, timeout: TimeSpan) -> bool:
        """

        :param timeout:
        :return:
        """
    @overload
    def WaitOne(self, millisecondsTimeout: int, exitContext: bool) -> bool:
        """

        :param millisecondsTimeout:
        :param exitContext:
        :return:
        """
    @overload
    def WaitOne(self, timeout: TimeSpan, exitContext: bool) -> bool:
        """

        :param timeout:
        :param exitContext:
        :return:
        """

class Barrier(Object, IDisposable):
    """"""

    @overload
    def __init__(self, participantCount: int):
        """

        :param participantCount:
        """
    @overload
    def __init__(self, participantCount: int, postPhaseAction: Action[Barrier]):
        """

        :param participantCount:
        :param postPhaseAction:
        """
    @property
    def CurrentPhaseNumber(self) -> int:
        """

        :return:
        """
    @property
    def ParticipantCount(self) -> int:
        """

        :return:
        """
    @property
    def ParticipantsRemaining(self) -> int:
        """

        :return:
        """
    def AddParticipant(self) -> int:
        """

        :return:
        """
    def AddParticipants(self, participantCount: int) -> int:
        """

        :param participantCount:
        :return:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def RemoveParticipant(self) -> None:
        """"""
    def RemoveParticipants(self, participantCount: int) -> None:
        """

        :param participantCount:
        """
    @overload
    def SignalAndWait(self) -> None:
        """"""
    @overload
    def SignalAndWait(self, cancellationToken: CancellationToken) -> None:
        """

        :param cancellationToken:
        """
    @overload
    def SignalAndWait(self, millisecondsTimeout: int) -> bool:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def SignalAndWait(self, timeout: TimeSpan) -> bool:
        """

        :param timeout:
        :return:
        """
    @overload
    def SignalAndWait(self, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool:
        """

        :param millisecondsTimeout:
        :param cancellationToken:
        :return:
        """
    @overload
    def SignalAndWait(self, timeout: TimeSpan, cancellationToken: CancellationToken) -> bool:
        """

        :param timeout:
        :param cancellationToken:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class BarrierPostPhaseException(Exception, _Exception, ISerializable):
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

class CancellationCallbackCoreWorkArguments(ValueType):
    """"""

    def __init__(
        self,
        currArrayFragment: SparselyPopulatedArrayFragment[CancellationCallbackInfo],
        currArrayIndex: int,
    ):
        """

        :param currArrayFragment:
        :param currArrayIndex:
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

class CancellationCallbackInfo(Object):
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

class CancellationToken(ValueType):
    """"""

    def __init__(self, canceled: bool):
        """

        :param canceled:
        """
    @property
    def CanBeCanceled(self) -> bool:
        """

        :return:
        """
    @property
    def IsCancellationRequested(self) -> bool:
        """

        :return:
        """
    @property
    def WaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @classmethod
    @property
    def _None(cls) -> CancellationToken:
        """

        :return:
        """
    @overload
    def Equals(self, other: CancellationToken) -> bool:
        """

        :param other:
        :return:
        """
    @overload
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
    @overload
    def Register(self, callback: Action) -> CancellationTokenRegistration:
        """

        :param callback:
        :return:
        """
    @overload
    def Register(
        self, callback: Action, useSynchronizationContext: bool
    ) -> CancellationTokenRegistration:
        """

        :param callback:
        :param useSynchronizationContext:
        :return:
        """
    @overload
    def Register(self, callback: Action[object], state: object) -> CancellationTokenRegistration:
        """

        :param callback:
        :param state:
        :return:
        """
    @overload
    def Register(
        self, callback: Action[object], state: object, useSynchronizationContext: bool
    ) -> CancellationTokenRegistration:
        """

        :param callback:
        :param state:
        :param useSynchronizationContext:
        :return:
        """
    def ThrowIfCancellationRequested(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def __eq__(self, other: CancellationToken) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: CancellationToken) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: CancellationToken, right: CancellationToken) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: CancellationToken, right: CancellationToken) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class CancellationTokenRegistration(
    ValueType, IDisposable, IEquatable[CancellationTokenRegistration]
):
    """"""

    def Dispose(self) -> None:
        """"""
    @overload
    def Equals(self, other: CancellationTokenRegistration) -> bool:
        """

        :param other:
        :return:
        """
    @overload
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
    def __eq__(self, other: CancellationTokenRegistration) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: CancellationTokenRegistration) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(
        cls, left: CancellationTokenRegistration, right: CancellationTokenRegistration
    ) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(
        cls, left: CancellationTokenRegistration, right: CancellationTokenRegistration
    ) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class CancellationTokenSource(Object, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, millisecondsDelay: int):
        """

        :param millisecondsDelay:
        """
    @overload
    def __init__(self, delay: TimeSpan):
        """

        :param delay:
        """
    @property
    def IsCancellationRequested(self) -> bool:
        """

        :return:
        """
    @property
    def Token(self) -> CancellationToken:
        """

        :return:
        """
    @overload
    def Cancel(self) -> None:
        """"""
    @overload
    def Cancel(self, throwOnFirstException: bool) -> None:
        """

        :param throwOnFirstException:
        """
    @overload
    def CancelAfter(self, millisecondsDelay: int) -> None:
        """

        :param millisecondsDelay:
        """
    @overload
    def CancelAfter(self, delay: TimeSpan) -> None:
        """

        :param delay:
        """
    @classmethod
    @overload
    def CreateLinkedTokenSource(cls, tokens: Array[CancellationToken]) -> CancellationTokenSource:
        """

        :param tokens:
        :return:
        """
    @classmethod
    @overload
    def CreateLinkedTokenSource(
        cls, token1: CancellationToken, token2: CancellationToken
    ) -> CancellationTokenSource:
        """

        :param token1:
        :param token2:
        :return:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CdsSyncEtwBCLProvider(EventSource, IDisposable):
    """"""

    Log: Final[ClassVar[CdsSyncEtwBCLProvider]] = ...
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
    def Barrier_PhaseFinished(self, currentSense: bool, phaseNum: int) -> None:
        """

        :param currentSense:
        :param phaseNum:
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
    def SpinLock_FastPathFailed(self, ownerID: int) -> None:
        """

        :param ownerID:
        """
    def SpinWait_NextSpinWillYield(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
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

class CompressedStack(Object, ISerializable):
    """"""

    @classmethod
    def Capture(cls) -> CompressedStack:
        """

        :return:
        """
    def CreateCopy(self) -> CompressedStack:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetCompressedStack(cls) -> CompressedStack:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def Run(
        cls, compressedStack: CompressedStack, callback: ContextCallback, state: object
    ) -> None:
        """

        :param compressedStack:
        :param callback:
        :param state:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CompressedStackSwitcher(ValueType, IDisposable):
    """"""

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
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Undo(self) -> None:
        """"""
    def __eq__(self, other: CompressedStackSwitcher) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: CompressedStackSwitcher) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, c1: CompressedStackSwitcher, c2: CompressedStackSwitcher) -> bool:
        """

        :param c1:
        :param c2:
        :return:
        """
    @classmethod
    def op_Inequality(cls, c1: CompressedStackSwitcher, c2: CompressedStackSwitcher) -> bool:
        """

        :param c1:
        :param c2:
        :return:
        """

ContextCallback: Callable[[object], None] = ...
"""

:param state: 
"""

class CountdownEvent(Object, IDisposable):
    """"""

    def __init__(self, initialCount: int):
        """

        :param initialCount:
        """
    @property
    def CurrentCount(self) -> int:
        """

        :return:
        """
    @property
    def InitialCount(self) -> int:
        """

        :return:
        """
    @property
    def IsSet(self) -> bool:
        """

        :return:
        """
    @property
    def WaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @overload
    def AddCount(self) -> None:
        """"""
    @overload
    def AddCount(self, signalCount: int) -> None:
        """

        :param signalCount:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def Reset(self) -> None:
        """"""
    @overload
    def Reset(self, count: int) -> None:
        """

        :param count:
        """
    @overload
    def Signal(self) -> bool:
        """

        :return:
        """
    @overload
    def Signal(self, signalCount: int) -> bool:
        """

        :param signalCount:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def TryAddCount(self) -> bool:
        """

        :return:
        """
    @overload
    def TryAddCount(self, signalCount: int) -> bool:
        """

        :param signalCount:
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
    @overload
    def Wait(self, timeout: TimeSpan, cancellationToken: CancellationToken) -> bool:
        """

        :param timeout:
        :param cancellationToken:
        :return:
        """

class DeferredDisposableLifetime(Generic[T], ValueType):
    """"""

    def AddRef(self, obj: T) -> bool:
        """

        :param obj:
        :return:
        """
    def Dispose(self, obj: T) -> None:
        """

        :param obj:
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
    def Release(self, obj: T) -> None:
        """

        :param obj:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DomainCompressedStack(Object):
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

class EventResetMode(Enum):
    """"""

    AutoReset: EventResetMode = ...
    """"""
    ManualReset: EventResetMode = ...
    """"""

class EventWaitHandle(WaitHandle, IDisposable):
    """"""

    @overload
    def __init__(self, initialState: bool, mode: EventResetMode):
        """

        :param initialState:
        :param mode:
        """
    @overload
    def __init__(self, initialState: bool, mode: EventResetMode, name: str):
        """

        :param initialState:
        :param mode:
        :param name:
        """
    @overload
    def __init__(self, initialState: bool, mode: EventResetMode, name: str, createdNew: bool):
        """

        :param initialState:
        :param mode:
        :param name:
        :param createdNew:
        """
    @overload
    def __init__(
        self,
        initialState: bool,
        mode: EventResetMode,
        name: str,
        createdNew: bool,
        eventSecurity: EventWaitHandleSecurity,
    ):
        """

        :param initialState:
        :param mode:
        :param name:
        :param createdNew:
        :param eventSecurity:
        """
    @property
    def Handle(self) -> IntPtr:
        """

        :return:
        """
    @Handle.setter
    def Handle(self, value: IntPtr) -> None: ...
    @property
    def SafeWaitHandle(self) -> SafeWaitHandle:
        """

        :return:
        """
    @SafeWaitHandle.setter
    def SafeWaitHandle(self, value: SafeWaitHandle) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAccessControl(self) -> EventWaitHandleSecurity:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    @classmethod
    @overload
    def OpenExisting(cls, name: str) -> EventWaitHandle:
        """

        :param name:
        :return:
        """
    @classmethod
    @overload
    def OpenExisting(cls, name: str, rights: EventWaitHandleRights) -> EventWaitHandle:
        """

        :param name:
        :param rights:
        :return:
        """
    def Reset(self) -> bool:
        """

        :return:
        """
    def Set(self) -> bool:
        """

        :return:
        """
    def SetAccessControl(self, eventSecurity: EventWaitHandleSecurity) -> None:
        """

        :param eventSecurity:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    @overload
    def TryOpenExisting(cls, name: str, result: EventWaitHandle) -> Tuple[bool, EventWaitHandle]:
        """

        :param name:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryOpenExisting(
        cls, name: str, rights: EventWaitHandleRights, result: EventWaitHandle
    ) -> Tuple[bool, EventWaitHandle]:
        """

        :param name:
        :param rights:
        :param result:
        :return:
        """
    @overload
    def WaitOne(self) -> bool:
        """

        :return:
        """
    @overload
    def WaitOne(self, millisecondsTimeout: int) -> bool:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def WaitOne(self, timeout: TimeSpan) -> bool:
        """

        :param timeout:
        :return:
        """
    @overload
    def WaitOne(self, millisecondsTimeout: int, exitContext: bool) -> bool:
        """

        :param millisecondsTimeout:
        :param exitContext:
        :return:
        """
    @overload
    def WaitOne(self, timeout: TimeSpan, exitContext: bool) -> bool:
        """

        :param timeout:
        :param exitContext:
        :return:
        """

class ExecutionContext(Object, ISerializable, IDisposable):
    """"""

    @classmethod
    def Capture(cls) -> ExecutionContext:
        """

        :return:
        """
    def CreateCopy(self) -> ExecutionContext:
        """

        :return:
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
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def IsFlowSuppressed(cls) -> bool:
        """

        :return:
        """
    @classmethod
    def RestoreFlow(cls) -> None:
        """"""
    @classmethod
    def Run(
        cls, executionContext: ExecutionContext, callback: ContextCallback, state: object
    ) -> None:
        """

        :param executionContext:
        :param callback:
        :param state:
        """
    @classmethod
    def SuppressFlow(cls) -> AsyncFlowControl:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ExecutionContextSwitcher(ValueType):
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

class Gen2GcCallback(CriticalFinalizerObject):
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
    @classmethod
    def Register(cls, callback: Func[object, bool], targetObj: object) -> None:
        """

        :param callback:
        :param targetObj:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class HostExecutionContext(Object, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, state: object):
        """

        :param state:
        """
    def CreateCopy(self) -> HostExecutionContext:
        """

        :return:
        """
    @overload
    def Dispose(self) -> None:
        """"""
    @overload
    def Dispose(self, disposing: bool) -> None:
        """

        :param disposing:
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

class HostExecutionContextManager(Object):
    """"""

    def __init__(self):
        """"""
    def Capture(self) -> HostExecutionContext:
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
    def Revert(self, previousState: object) -> None:
        """

        :param previousState:
        """
    def SetHostExecutionContext(self, hostExecutionContext: HostExecutionContext) -> object:
        """

        :param hostExecutionContext:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class HostExecutionContextSwitcher(Object):
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
    @classmethod
    def Undo(cls, switcherObject: object) -> None:
        """

        :param switcherObject:
        """

class IAsyncLocal:
    """"""

    def OnValueChanged(
        self, previousValue: object, currentValue: object, contextChanged: bool
    ) -> None:
        """

        :param previousValue:
        :param currentValue:
        :param contextChanged:
        """

class IAsyncLocalValueMap:
    """"""

    def Set(
        self, key: IAsyncLocal, value: object, treatNullValueAsNonexistent: bool
    ) -> IAsyncLocalValueMap:
        """

        :param key:
        :param value:
        :param treatNullValueAsNonexistent:
        :return:
        """
    def TryGetValue(self, key: IAsyncLocal, value: object) -> Tuple[bool, object]:
        """

        :param key:
        :param value:
        :return:
        """

class IDeferredDisposable:
    """"""

    def OnFinalRelease(self, disposed: bool) -> None:
        """

        :param disposed:
        """

IOCompletionCallback: Callable[[int, int, NativeOverlapped], None] = ...
"""

:param errorCode: 
:param numBytes: 
:param pOVERLAP: 
"""

class IThreadPoolWorkItem:
    """"""

    def ExecuteWorkItem(self) -> None:
        """"""
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """

        :param tae:
        """

class IUnknownSafeHandle(SafeHandle, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class Interlocked(ABC, Object):
    """"""

    @classmethod
    @overload
    def Add(cls, location1: int, value: int) -> int:
        """

        :param location1:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def Add(cls, location1: int, value: int) -> int:
        """

        :param location1:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def CompareExchange(cls, location1: T, value: T, comparand: T) -> T:
        """

        :param location1:
        :param value:
        :param comparand:
        :return:
        """
    @classmethod
    @overload
    def CompareExchange(cls, location1: float, value: float, comparand: float) -> float:
        """

        :param location1:
        :param value:
        :param comparand:
        :return:
        """
    @classmethod
    @overload
    def CompareExchange(cls, location1: int, value: int, comparand: int) -> int:
        """

        :param location1:
        :param value:
        :param comparand:
        :return:
        """
    @classmethod
    @overload
    def CompareExchange(cls, location1: int, value: int, comparand: int) -> int:
        """

        :param location1:
        :param value:
        :param comparand:
        :return:
        """
    @classmethod
    @overload
    def CompareExchange(cls, location1: IntPtr, value: IntPtr, comparand: IntPtr) -> IntPtr:
        """

        :param location1:
        :param value:
        :param comparand:
        :return:
        """
    @classmethod
    @overload
    def CompareExchange(cls, location1: object, value: object, comparand: object) -> object:
        """

        :param location1:
        :param value:
        :param comparand:
        :return:
        """
    @classmethod
    @overload
    def CompareExchange(cls, location1: float, value: float, comparand: float) -> float:
        """

        :param location1:
        :param value:
        :param comparand:
        :return:
        """
    @classmethod
    @overload
    def Decrement(cls, location: int) -> int:
        """

        :param location:
        :return:
        """
    @classmethod
    @overload
    def Decrement(cls, location: int) -> int:
        """

        :param location:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def Exchange(cls, location1: T, value: T) -> T:
        """

        :param location1:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def Exchange(cls, location1: float, value: float) -> float:
        """

        :param location1:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def Exchange(cls, location1: int, value: int) -> int:
        """

        :param location1:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def Exchange(cls, location1: int, value: int) -> int:
        """

        :param location1:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def Exchange(cls, location1: IntPtr, value: IntPtr) -> IntPtr:
        """

        :param location1:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def Exchange(cls, location1: object, value: object) -> object:
        """

        :param location1:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def Exchange(cls, location1: float, value: float) -> float:
        """

        :param location1:
        :param value:
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
    def Increment(cls, location: int) -> int:
        """

        :param location:
        :return:
        """
    @classmethod
    @overload
    def Increment(cls, location: int) -> int:
        """

        :param location:
        :return:
        """
    @classmethod
    def MemoryBarrier(cls) -> None:
        """"""
    @classmethod
    def Read(cls, location: int) -> int:
        """

        :param location:
        :return:
        """
    @classmethod
    def SpeculationBarrier(cls) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

InternalCrossContextDelegate: Callable[[Array[object]], object] = ...
"""

:param args: 
:return: 
"""

class LazyHelpers(ABC, Generic[T], Object):
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

class LazyInitializer(ABC, Object):
    """"""

    @classmethod
    @overload
    def EnsureInitialized(cls, target: T) -> T:
        """

        :param target:
        :return:
        """
    @classmethod
    @overload
    def EnsureInitialized(cls, target: T, valueFactory: Func[T]) -> T:
        """

        :param target:
        :param valueFactory:
        :return:
        """
    @classmethod
    @overload
    def EnsureInitialized(cls, target: T, initialized: bool, syncLock: object) -> T:
        """

        :param target:
        :param initialized:
        :param syncLock:
        :return:
        """
    @classmethod
    @overload
    def EnsureInitialized(
        cls, target: T, initialized: bool, syncLock: object, valueFactory: Func[T]
    ) -> T:
        """

        :param target:
        :param initialized:
        :param syncLock:
        :param valueFactory:
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
    def __eq__(self, other: LockCookie) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: LockCookie) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, a: LockCookie, b: LockCookie) -> bool:
        """

        :param a:
        :param b:
        :return:
        """
    @classmethod
    def op_Inequality(cls, a: LockCookie, b: LockCookie) -> bool:
        """

        :param a:
        :param b:
        :return:
        """

class LockRecursionException(Exception, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
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

class LockRecursionPolicy(Enum):
    """"""

    NoRecursion: LockRecursionPolicy = ...
    """"""
    SupportsRecursion: LockRecursionPolicy = ...
    """"""

class ManualResetEvent(EventWaitHandle, IDisposable):
    """"""

    def __init__(self, initialState: bool):
        """

        :param initialState:
        """
    @property
    def Handle(self) -> IntPtr:
        """

        :return:
        """
    @Handle.setter
    def Handle(self, value: IntPtr) -> None: ...
    @property
    def SafeWaitHandle(self) -> SafeWaitHandle:
        """

        :return:
        """
    @SafeWaitHandle.setter
    def SafeWaitHandle(self, value: SafeWaitHandle) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAccessControl(self) -> EventWaitHandleSecurity:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Reset(self) -> bool:
        """

        :return:
        """
    def Set(self) -> bool:
        """

        :return:
        """
    def SetAccessControl(self, eventSecurity: EventWaitHandleSecurity) -> None:
        """

        :param eventSecurity:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def WaitOne(self) -> bool:
        """

        :return:
        """
    @overload
    def WaitOne(self, millisecondsTimeout: int) -> bool:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def WaitOne(self, timeout: TimeSpan) -> bool:
        """

        :param timeout:
        :return:
        """
    @overload
    def WaitOne(self, millisecondsTimeout: int, exitContext: bool) -> bool:
        """

        :param millisecondsTimeout:
        :param exitContext:
        :return:
        """
    @overload
    def WaitOne(self, timeout: TimeSpan, exitContext: bool) -> bool:
        """

        :param timeout:
        :param exitContext:
        :return:
        """

class ManualResetEventSlim(Object, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, initialState: bool):
        """

        :param initialState:
        """
    @overload
    def __init__(self, initialState: bool, spinCount: int):
        """

        :param initialState:
        :param spinCount:
        """
    @property
    def IsSet(self) -> bool:
        """

        :return:
        """
    @property
    def SpinCount(self) -> int:
        """

        :return:
        """
    @property
    def WaitHandle(self) -> WaitHandle:
        """

        :return:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def Set(self) -> None:
        """"""
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
    @overload
    def Wait(self, timeout: TimeSpan, cancellationToken: CancellationToken) -> bool:
        """

        :param timeout:
        :param cancellationToken:
        :return:
        """

class Monitor(ABC, Object):
    """"""

    @classmethod
    @overload
    def Enter(cls, obj: object) -> None:
        """

        :param obj:
        """
    @classmethod
    @overload
    def Enter(cls, obj: object, lockTaken: bool) -> None:
        """

        :param obj:
        :param lockTaken:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def Exit(cls, obj: object) -> None:
        """

        :param obj:
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
    def IsEntered(cls, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def Pulse(cls, obj: object) -> None:
        """

        :param obj:
        """
    @classmethod
    def PulseAll(cls, obj: object) -> None:
        """

        :param obj:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    @overload
    def TryEnter(cls, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def TryEnter(cls, obj: object, lockTaken: bool) -> None:
        """

        :param obj:
        :param lockTaken:
        """
    @classmethod
    @overload
    def TryEnter(cls, obj: object, millisecondsTimeout: int) -> bool:
        """

        :param obj:
        :param millisecondsTimeout:
        :return:
        """
    @classmethod
    @overload
    def TryEnter(cls, obj: object, timeout: TimeSpan) -> bool:
        """

        :param obj:
        :param timeout:
        :return:
        """
    @classmethod
    @overload
    def TryEnter(cls, obj: object, millisecondsTimeout: int, lockTaken: bool) -> None:
        """

        :param obj:
        :param millisecondsTimeout:
        :param lockTaken:
        """
    @classmethod
    @overload
    def TryEnter(cls, obj: object, timeout: TimeSpan, lockTaken: bool) -> None:
        """

        :param obj:
        :param timeout:
        :param lockTaken:
        """
    @classmethod
    @overload
    def Wait(cls, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def Wait(cls, obj: object, millisecondsTimeout: int) -> bool:
        """

        :param obj:
        :param millisecondsTimeout:
        :return:
        """
    @classmethod
    @overload
    def Wait(cls, obj: object, timeout: TimeSpan) -> bool:
        """

        :param obj:
        :param timeout:
        :return:
        """
    @classmethod
    @overload
    def Wait(cls, obj: object, millisecondsTimeout: int, exitContext: bool) -> bool:
        """

        :param obj:
        :param millisecondsTimeout:
        :param exitContext:
        :return:
        """
    @classmethod
    @overload
    def Wait(cls, obj: object, timeout: TimeSpan, exitContext: bool) -> bool:
        """

        :param obj:
        :param timeout:
        :param exitContext:
        :return:
        """

class Mutex(WaitHandle, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, initiallyOwned: bool):
        """

        :param initiallyOwned:
        """
    @overload
    def __init__(self, initiallyOwned: bool, name: str):
        """

        :param initiallyOwned:
        :param name:
        """
    @overload
    def __init__(self, initiallyOwned: bool, name: str, createdNew: bool):
        """

        :param initiallyOwned:
        :param name:
        :param createdNew:
        """
    @overload
    def __init__(
        self, initiallyOwned: bool, name: str, createdNew: bool, mutexSecurity: MutexSecurity
    ):
        """

        :param initiallyOwned:
        :param name:
        :param createdNew:
        :param mutexSecurity:
        """
    @property
    def Handle(self) -> IntPtr:
        """

        :return:
        """
    @Handle.setter
    def Handle(self, value: IntPtr) -> None: ...
    @property
    def SafeWaitHandle(self) -> SafeWaitHandle:
        """

        :return:
        """
    @SafeWaitHandle.setter
    def SafeWaitHandle(self, value: SafeWaitHandle) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAccessControl(self) -> MutexSecurity:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    @classmethod
    @overload
    def OpenExisting(cls, name: str) -> Mutex:
        """

        :param name:
        :return:
        """
    @classmethod
    @overload
    def OpenExisting(cls, name: str, rights: MutexRights) -> Mutex:
        """

        :param name:
        :param rights:
        :return:
        """
    def ReleaseMutex(self) -> None:
        """"""
    def SetAccessControl(self, mutexSecurity: MutexSecurity) -> None:
        """

        :param mutexSecurity:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    @overload
    def TryOpenExisting(cls, name: str, result: Mutex) -> Tuple[bool, Mutex]:
        """

        :param name:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryOpenExisting(cls, name: str, rights: MutexRights, result: Mutex) -> Tuple[bool, Mutex]:
        """

        :param name:
        :param rights:
        :param result:
        :return:
        """
    @overload
    def WaitOne(self) -> bool:
        """

        :return:
        """
    @overload
    def WaitOne(self, millisecondsTimeout: int) -> bool:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def WaitOne(self, timeout: TimeSpan) -> bool:
        """

        :param timeout:
        :return:
        """
    @overload
    def WaitOne(self, millisecondsTimeout: int, exitContext: bool) -> bool:
        """

        :param millisecondsTimeout:
        :param exitContext:
        :return:
        """
    @overload
    def WaitOne(self, timeout: TimeSpan, exitContext: bool) -> bool:
        """

        :param timeout:
        :param exitContext:
        :return:
        """

class NativeOverlapped(ValueType):
    """"""

    EventHandle: Final[IntPtr] = ...
    """
    
    :return: 
    """
    InternalHigh: Final[IntPtr] = ...
    """
    
    :return: 
    """
    InternalLow: Final[IntPtr] = ...
    """
    
    :return: 
    """
    OffsetHigh: Final[int] = ...
    """
    
    :return: 
    """
    OffsetLow: Final[int] = ...
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

class Overlapped(Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, offsetLo: int, offsetHi: int, hEvent: int, ar: IAsyncResult):
        """

        :param offsetLo:
        :param offsetHi:
        :param hEvent:
        :param ar:
        """
    @overload
    def __init__(self, offsetLo: int, offsetHi: int, hEvent: IntPtr, ar: IAsyncResult):
        """

        :param offsetLo:
        :param offsetHi:
        :param hEvent:
        :param ar:
        """
    @property
    def AsyncResult(self) -> IAsyncResult:
        """

        :return:
        """
    @AsyncResult.setter
    def AsyncResult(self, value: IAsyncResult) -> None: ...
    @property
    def EventHandle(self) -> int:
        """

        :return:
        """
    @EventHandle.setter
    def EventHandle(self, value: int) -> None: ...
    @property
    def EventHandleIntPtr(self) -> IntPtr:
        """

        :return:
        """
    @EventHandleIntPtr.setter
    def EventHandleIntPtr(self, value: IntPtr) -> None: ...
    @property
    def OffsetHigh(self) -> int:
        """

        :return:
        """
    @OffsetHigh.setter
    def OffsetHigh(self, value: int) -> None: ...
    @property
    def OffsetLow(self) -> int:
        """

        :return:
        """
    @OffsetLow.setter
    def OffsetLow(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def Free(cls, nativeOverlappedPtr: NativeOverlapped) -> None:
        """

        :param nativeOverlappedPtr:
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
    def Pack(self, iocb: IOCompletionCallback) -> NativeOverlapped:
        """

        :param iocb:
        :return:
        """
    @overload
    def Pack(self, iocb: IOCompletionCallback, userData: object) -> NativeOverlapped:
        """

        :param iocb:
        :param userData:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def Unpack(cls, nativeOverlappedPtr: NativeOverlapped) -> Overlapped:
        """

        :param nativeOverlappedPtr:
        :return:
        """
    @overload
    def UnsafePack(self, iocb: IOCompletionCallback) -> NativeOverlapped:
        """

        :param iocb:
        :return:
        """
    @overload
    def UnsafePack(self, iocb: IOCompletionCallback, userData: object) -> NativeOverlapped:
        """

        :param iocb:
        :param userData:
        :return:
        """

class OverlappedData(Object):
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

ParameterizedThreadStart: Callable[[object], None] = ...
"""

:param obj: 
"""

class PinnableBufferCache(Object):
    """"""

    def __init__(self, cacheName: str, numberOfElements: int):
        """

        :param cacheName:
        :param numberOfElements:
        """
    def AllocateBuffer(self) -> Array[int]:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FreeBuffer(self, buffer: Array[int]) -> None:
        """

        :param buffer:
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

class PinnableBufferCacheEventSource(EventSource, IDisposable):
    """"""

    Log: Final[ClassVar[PinnableBufferCacheEventSource]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
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
    def AgePendingBuffersResults(
        self, cacheName: str, promotedToFreeListCount: int, heldBackCount: int
    ) -> None:
        """

        :param cacheName:
        :param promotedToFreeListCount:
        :param heldBackCount:
        """
    def AllocateBuffer(
        self, cacheName: str, objectId: int, objectHash: int, objectGen: int, freeCountAfter: int
    ) -> None:
        """

        :param cacheName:
        :param objectId:
        :param objectHash:
        :param objectGen:
        :param freeCountAfter:
        """
    def AllocateBufferAged(self, cacheName: str, agedCount: int) -> None:
        """

        :param cacheName:
        :param agedCount:
        """
    def AllocateBufferCreatingNewBuffers(
        self, cacheName: str, totalBuffsBefore: int, objectCount: int
    ) -> None:
        """

        :param cacheName:
        :param totalBuffsBefore:
        :param objectCount:
        """
    def AllocateBufferFreeListEmpty(self, cacheName: str, notGen2CountBefore: int) -> None:
        """

        :param cacheName:
        :param notGen2CountBefore:
        """
    def AllocateBufferFromNotGen2(self, cacheName: str, notGen2CountAfter: int) -> None:
        """

        :param cacheName:
        :param notGen2CountAfter:
        """
    def Create(self, cacheName: str) -> None:
        """

        :param cacheName:
        """
    def DebugMessage(self, message: str) -> None:
        """

        :param message:
        """
    def DebugMessage1(self, message: str, value: int) -> None:
        """

        :param message:
        :param value:
        """
    def DebugMessage2(self, message: str, value1: int, value2: int) -> None:
        """

        :param message:
        :param value1:
        :param value2:
        """
    def DebugMessage3(self, message: str, value1: int, value2: int, value3: int) -> None:
        """

        :param message:
        :param value1:
        :param value2:
        :param value3:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FreeBuffer(
        self, cacheName: str, objectId: int, objectHash: int, freeCountBefore: int
    ) -> None:
        """

        :param cacheName:
        :param objectId:
        :param objectHash:
        :param freeCountBefore:
        """
    def FreeBufferNull(self, cacheName: str, freeCountBefore: int) -> None:
        """

        :param cacheName:
        :param freeCountBefore:
        """
    def FreeBufferStillTooYoung(self, cacheName: str, notGen2CountBefore: int) -> None:
        """

        :param cacheName:
        :param notGen2CountBefore:
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
    def ToString(self) -> str:
        """

        :return:
        """
    def TrimCheck(
        self, cacheName: str, totalBuffs: int, neededMoreThanFreeList: bool, deltaMSec: int
    ) -> None:
        """

        :param cacheName:
        :param totalBuffs:
        :param neededMoreThanFreeList:
        :param deltaMSec:
        """
    def TrimExperiment(
        self, cacheName: str, totalBuffs: int, freeListCount: int, numTrimTrial: int
    ) -> None:
        """

        :param cacheName:
        :param totalBuffs:
        :param freeListCount:
        :param numTrimTrial:
        """
    def TrimFlush(
        self, cacheName: str, totalBuffs: int, freeListCount: int, notGen2CountBefore: int
    ) -> None:
        """

        :param cacheName:
        :param totalBuffs:
        :param freeListCount:
        :param notGen2CountBefore:
        """
    def TrimFree(self, cacheName: str, totalBuffs: int, freeListCount: int, toBeFreed: int) -> None:
        """

        :param cacheName:
        :param totalBuffs:
        :param freeListCount:
        :param toBeFreed:
        """
    def TrimFreeSizeOK(self, cacheName: str, totalBuffs: int, freeListCount: int) -> None:
        """

        :param cacheName:
        :param totalBuffs:
        :param freeListCount:
        """
    def WalkFreeListResult(
        self, cacheName: str, freeListCount: int, gen0BuffersInFreeList: int
    ) -> None:
        """

        :param cacheName:
        :param freeListCount:
        :param gen0BuffersInFreeList:
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

class PlatformHelper(ABC, Object):
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

class PreAllocatedOverlapped(Object, IDeferredDisposable, IDisposable):
    """"""

    def __init__(self, callback: IOCompletionCallback, state: object, pinData: object):
        """

        :param callback:
        :param state:
        :param pinData:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def OnFinalRelease(self, disposed: bool) -> None:
        """

        :param disposed:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class QueueUserWorkItemCallback(Object, IThreadPoolWorkItem):
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

class ReaderWriterCount(Object):
    """"""

    lockID: Final[int] = ...
    """
    
    :return: 
    """
    next: Final[ReaderWriterCount] = ...
    """
    
    :return: 
    """
    readercount: Final[int] = ...
    """
    
    :return: 
    """
    upgradecount: Final[int] = ...
    """
    
    :return: 
    """
    writercount: Final[int] = ...
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

class ReaderWriterLock(CriticalFinalizerObject):
    """"""

    def __init__(self):
        """"""
    @property
    def IsReaderLockHeld(self) -> bool:
        """

        :return:
        """
    @property
    def IsWriterLockHeld(self) -> bool:
        """

        :return:
        """
    @property
    def WriterSeqNum(self) -> int:
        """

        :return:
        """
    @overload
    def AcquireReaderLock(self, millisecondsTimeout: int) -> None:
        """

        :param millisecondsTimeout:
        """
    @overload
    def AcquireReaderLock(self, timeout: TimeSpan) -> None:
        """

        :param timeout:
        """
    @overload
    def AcquireWriterLock(self, millisecondsTimeout: int) -> None:
        """

        :param millisecondsTimeout:
        """
    @overload
    def AcquireWriterLock(self, timeout: TimeSpan) -> None:
        """

        :param timeout:
        """
    def AnyWritersSince(self, seqNum: int) -> bool:
        """

        :param seqNum:
        :return:
        """
    def DowngradeFromWriterLock(self, lockCookie: LockCookie) -> None:
        """

        :param lockCookie:
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
    def ReleaseLock(self) -> LockCookie:
        """

        :return:
        """
    def ReleaseReaderLock(self) -> None:
        """"""
    def ReleaseWriterLock(self) -> None:
        """"""
    def RestoreLock(self, lockCookie: LockCookie) -> None:
        """

        :param lockCookie:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def UpgradeToWriterLock(self, millisecondsTimeout: int) -> LockCookie:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def UpgradeToWriterLock(self, timeout: TimeSpan) -> LockCookie:
        """

        :param timeout:
        :return:
        """

class ReaderWriterLockSlim(Object, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, recursionPolicy: LockRecursionPolicy):
        """

        :param recursionPolicy:
        """
    @property
    def CurrentReadCount(self) -> int:
        """

        :return:
        """
    @property
    def IsReadLockHeld(self) -> bool:
        """

        :return:
        """
    @property
    def IsUpgradeableReadLockHeld(self) -> bool:
        """

        :return:
        """
    @property
    def IsWriteLockHeld(self) -> bool:
        """

        :return:
        """
    @property
    def RecursionPolicy(self) -> LockRecursionPolicy:
        """

        :return:
        """
    @property
    def RecursiveReadCount(self) -> int:
        """

        :return:
        """
    @property
    def RecursiveUpgradeCount(self) -> int:
        """

        :return:
        """
    @property
    def RecursiveWriteCount(self) -> int:
        """

        :return:
        """
    @property
    def WaitingReadCount(self) -> int:
        """

        :return:
        """
    @property
    def WaitingUpgradeCount(self) -> int:
        """

        :return:
        """
    @property
    def WaitingWriteCount(self) -> int:
        """

        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EnterReadLock(self) -> None:
        """"""
    def EnterUpgradeableReadLock(self) -> None:
        """"""
    def EnterWriteLock(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExitReadLock(self) -> None:
        """"""
    def ExitUpgradeableReadLock(self) -> None:
        """"""
    def ExitWriteLock(self) -> None:
        """"""
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
    @overload
    def TryEnterReadLock(self, millisecondsTimeout: int) -> bool:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def TryEnterReadLock(self, timeout: TimeSpan) -> bool:
        """

        :param timeout:
        :return:
        """
    @overload
    def TryEnterUpgradeableReadLock(self, millisecondsTimeout: int) -> bool:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def TryEnterUpgradeableReadLock(self, timeout: TimeSpan) -> bool:
        """

        :param timeout:
        :return:
        """
    @overload
    def TryEnterWriteLock(self, millisecondsTimeout: int) -> bool:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def TryEnterWriteLock(self, timeout: TimeSpan) -> bool:
        """

        :param timeout:
        :return:
        """

class RegisteredWaitHandle(MarshalByRefObject):
    """"""

    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
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
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Unregister(self, waitObject: WaitHandle) -> bool:
        """

        :param waitObject:
        :return:
        """

class RegisteredWaitHandleSafe(CriticalFinalizerObject):
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

class SafeCompressedStackHandle(SafeHandle, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class Semaphore(WaitHandle, IDisposable):
    """"""

    @overload
    def __init__(self, initialCount: int, maximumCount: int):
        """

        :param initialCount:
        :param maximumCount:
        """
    @overload
    def __init__(self, initialCount: int, maximumCount: int, name: str):
        """

        :param initialCount:
        :param maximumCount:
        :param name:
        """
    @overload
    def __init__(self, initialCount: int, maximumCount: int, name: str, createdNew: bool):
        """

        :param initialCount:
        :param maximumCount:
        :param name:
        :param createdNew:
        """
    @overload
    def __init__(
        self,
        initialCount: int,
        maximumCount: int,
        name: str,
        createdNew: bool,
        semaphoreSecurity: SemaphoreSecurity,
    ):
        """

        :param initialCount:
        :param maximumCount:
        :param name:
        :param createdNew:
        :param semaphoreSecurity:
        """
    @property
    def Handle(self) -> IntPtr:
        """

        :return:
        """
    @Handle.setter
    def Handle(self, value: IntPtr) -> None: ...
    @property
    def SafeWaitHandle(self) -> SafeWaitHandle:
        """

        :return:
        """
    @SafeWaitHandle.setter
    def SafeWaitHandle(self, value: SafeWaitHandle) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAccessControl(self) -> SemaphoreSecurity:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    @classmethod
    @overload
    def OpenExisting(cls, name: str) -> Semaphore:
        """

        :param name:
        :return:
        """
    @classmethod
    @overload
    def OpenExisting(cls, name: str, rights: SemaphoreRights) -> Semaphore:
        """

        :param name:
        :param rights:
        :return:
        """
    @overload
    def Release(self) -> int:
        """

        :return:
        """
    @overload
    def Release(self, releaseCount: int) -> int:
        """

        :param releaseCount:
        :return:
        """
    def SetAccessControl(self, semaphoreSecurity: SemaphoreSecurity) -> None:
        """

        :param semaphoreSecurity:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    @overload
    def TryOpenExisting(cls, name: str, result: Semaphore) -> Tuple[bool, Semaphore]:
        """

        :param name:
        :param result:
        :return:
        """
    @classmethod
    @overload
    def TryOpenExisting(
        cls, name: str, rights: SemaphoreRights, result: Semaphore
    ) -> Tuple[bool, Semaphore]:
        """

        :param name:
        :param rights:
        :param result:
        :return:
        """
    @overload
    def WaitOne(self) -> bool:
        """

        :return:
        """
    @overload
    def WaitOne(self, millisecondsTimeout: int) -> bool:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def WaitOne(self, timeout: TimeSpan) -> bool:
        """

        :param timeout:
        :return:
        """
    @overload
    def WaitOne(self, millisecondsTimeout: int, exitContext: bool) -> bool:
        """

        :param millisecondsTimeout:
        :param exitContext:
        :return:
        """
    @overload
    def WaitOne(self, timeout: TimeSpan, exitContext: bool) -> bool:
        """

        :param timeout:
        :param exitContext:
        :return:
        """

class SemaphoreFullException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
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

class SemaphoreSlim(Object, IDisposable):
    """"""

    @overload
    def __init__(self, initialCount: int):
        """

        :param initialCount:
        """
    @overload
    def __init__(self, initialCount: int, maxCount: int):
        """

        :param initialCount:
        :param maxCount:
        """
    @property
    def AvailableWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CurrentCount(self) -> int:
        """

        :return:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def Release(self) -> int:
        """

        :return:
        """
    @overload
    def Release(self, releaseCount: int) -> int:
        """

        :param releaseCount:
        :return:
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
    @overload
    def Wait(self, timeout: TimeSpan, cancellationToken: CancellationToken) -> bool:
        """

        :param timeout:
        :param cancellationToken:
        :return:
        """
    @overload
    def WaitAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def WaitAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    @overload
    def WaitAsync(self, millisecondsTimeout: int) -> Task[bool]:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def WaitAsync(self, timeout: TimeSpan) -> Task[bool]:
        """

        :param timeout:
        :return:
        """
    @overload
    def WaitAsync(
        self, millisecondsTimeout: int, cancellationToken: CancellationToken
    ) -> Task[bool]:
        """

        :param millisecondsTimeout:
        :param cancellationToken:
        :return:
        """
    @overload
    def WaitAsync(self, timeout: TimeSpan, cancellationToken: CancellationToken) -> Task[bool]:
        """

        :param timeout:
        :param cancellationToken:
        :return:
        """

SendOrPostCallback: Callable[[object], None] = ...
"""

:param state: 
"""

class SparselyPopulatedArrayAddInfo(Generic[T], ValueType):
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

class SparselyPopulatedArrayFragment(Generic[T], Object):
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

class SparselyPopulatedArray(Generic[T], Object):
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

class SpinLock(ValueType):
    """"""

    def __init__(self, enableThreadOwnerTracking: bool):
        """

        :param enableThreadOwnerTracking:
        """
    @property
    def IsHeld(self) -> bool:
        """

        :return:
        """
    @property
    def IsHeldByCurrentThread(self) -> bool:
        """

        :return:
        """
    @property
    def IsThreadOwnerTrackingEnabled(self) -> bool:
        """

        :return:
        """
    def Enter(self, lockTaken: bool) -> None:
        """

        :param lockTaken:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Exit(self) -> None:
        """"""
    @overload
    def Exit(self, useMemoryBarrier: bool) -> None:
        """

        :param useMemoryBarrier:
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
    @overload
    def TryEnter(self, lockTaken: bool) -> None:
        """

        :param lockTaken:
        """
    @overload
    def TryEnter(self, millisecondsTimeout: int, lockTaken: bool) -> None:
        """

        :param millisecondsTimeout:
        :param lockTaken:
        """
    @overload
    def TryEnter(self, timeout: TimeSpan, lockTaken: bool) -> None:
        """

        :param timeout:
        :param lockTaken:
        """

class SpinWait(ValueType):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def NextSpinWillYield(self) -> bool:
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
    def Reset(self) -> None:
        """"""
    def SpinOnce(self) -> None:
        """"""
    @classmethod
    @overload
    def SpinUntil(cls, condition: Func[bool]) -> None:
        """

        :param condition:
        """
    @classmethod
    @overload
    def SpinUntil(cls, condition: Func[bool], millisecondsTimeout: int) -> bool:
        """

        :param condition:
        :param millisecondsTimeout:
        :return:
        """
    @classmethod
    @overload
    def SpinUntil(cls, condition: Func[bool], timeout: TimeSpan) -> bool:
        """

        :param condition:
        :param timeout:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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

    def __init__(self):
        """"""
    @classmethod
    @property
    def Current(cls) -> SynchronizationContext:
        """

        :return:
        """
    def CreateCopy(self) -> SynchronizationContext:
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
    def IsWaitNotificationRequired(self) -> bool:
        """

        :return:
        """
    def OperationCompleted(self) -> None:
        """"""
    def OperationStarted(self) -> None:
        """"""
    def Post(self, d: SendOrPostCallback, state: object) -> None:
        """

        :param d:
        :param state:
        """
    def Send(self, d: SendOrPostCallback, state: object) -> None:
        """

        :param d:
        :param state:
        """
    @classmethod
    def SetSynchronizationContext(cls, syncContext: SynchronizationContext) -> None:
        """

        :param syncContext:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Wait(self, waitHandles: Array[IntPtr], waitAll: bool, millisecondsTimeout: int) -> int:
        """

        :param waitHandles:
        :param waitAll:
        :param millisecondsTimeout:
        :return:
        """

class SynchronizationContextProperties(Enum):
    """"""

    _None: SynchronizationContextProperties = ...
    """"""
    RequireWaitNotification: SynchronizationContextProperties = ...
    """"""

class SynchronizationLockException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
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

class SystemThreading_ThreadLocalDebugView(Generic[T], Object):
    """"""

    def __init__(self, tlocal: ThreadLocal[T]):
        """

        :param tlocal:
        """
    @property
    def IsValueCreated(self) -> bool:
        """

        :return:
        """
    @property
    def Value(self) -> T:
        """

        :return:
        """
    @property
    def Values(self) -> List[T]:
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

class Thread(CriticalFinalizerObject, _Thread):
    """"""

    @overload
    def __init__(self, start: ParameterizedThreadStart):
        """

        :param start:
        """
    @overload
    def __init__(self, start: ThreadStart):
        """

        :param start:
        """
    @overload
    def __init__(self, start: ParameterizedThreadStart, maxStackSize: int):
        """

        :param start:
        :param maxStackSize:
        """
    @overload
    def __init__(self, start: ThreadStart, maxStackSize: int):
        """

        :param start:
        :param maxStackSize:
        """
    @property
    def ApartmentState(self) -> ApartmentState:
        """

        :return:
        """
    @ApartmentState.setter
    def ApartmentState(self, value: ApartmentState) -> None: ...
    @classmethod
    @property
    def CurrentContext(cls) -> Context:
        """

        :return:
        """
    @property
    def CurrentCulture(self) -> CultureInfo:
        """

        :return:
        """
    @CurrentCulture.setter
    def CurrentCulture(self, value: CultureInfo) -> None: ...
    @classmethod
    @property
    def CurrentPrincipal(cls) -> IPrincipal:
        """

        :return:
        """
    @classmethod
    @CurrentPrincipal.setter
    def CurrentPrincipal(cls, value: IPrincipal) -> None: ...
    @classmethod
    @property
    def CurrentThread(cls) -> Thread:
        """

        :return:
        """
    @property
    def CurrentUICulture(self) -> CultureInfo:
        """

        :return:
        """
    @CurrentUICulture.setter
    def CurrentUICulture(self, value: CultureInfo) -> None: ...
    @property
    def ExecutionContext(self) -> ExecutionContext:
        """

        :return:
        """
    @property
    def IsAlive(self) -> bool:
        """

        :return:
        """
    @property
    def IsBackground(self) -> bool:
        """

        :return:
        """
    @IsBackground.setter
    def IsBackground(self, value: bool) -> None: ...
    @property
    def IsThreadPoolThread(self) -> bool:
        """

        :return:
        """
    @property
    def ManagedThreadId(self) -> int:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Priority(self) -> ThreadPriority:
        """

        :return:
        """
    @Priority.setter
    def Priority(self, value: ThreadPriority) -> None: ...
    @property
    def ThreadState(self) -> ThreadState:
        """

        :return:
        """
    @overload
    def Abort(self) -> None:
        """"""
    @overload
    def Abort(self, stateInfo: object) -> None:
        """

        :param stateInfo:
        """
    @classmethod
    def AllocateDataSlot(cls) -> LocalDataStoreSlot:
        """

        :return:
        """
    @classmethod
    def AllocateNamedDataSlot(cls, name: str) -> LocalDataStoreSlot:
        """

        :param name:
        :return:
        """
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
        """

        :param obj:
        :return:
        """
    @classmethod
    def FreeNamedDataSlot(cls, name: str) -> None:
        """

        :param name:
        """
    def GetApartmentState(self) -> ApartmentState:
        """

        :return:
        """
    def GetCompressedStack(self) -> CompressedStack:
        """

        :return:
        """
    @classmethod
    def GetData(cls, slot: LocalDataStoreSlot) -> object:
        """

        :param slot:
        :return:
        """
    @classmethod
    def GetDomain(cls) -> AppDomain:
        """

        :return:
        """
    @classmethod
    def GetDomainID(cls) -> int:
        """

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
    @classmethod
    def GetNamedDataSlot(cls, name: str) -> LocalDataStoreSlot:
        """

        :param name:
        :return:
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
    @overload
    def Join(self) -> None:
        """"""
    @overload
    def Join(self, millisecondsTimeout: int) -> bool:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def Join(self, timeout: TimeSpan) -> bool:
        """

        :param timeout:
        :return:
        """
    @classmethod
    def MemoryBarrier(cls) -> None:
        """"""
    @classmethod
    def ResetAbort(cls) -> None:
        """"""
    def Resume(self) -> None:
        """"""
    def SetApartmentState(self, state: ApartmentState) -> None:
        """

        :param state:
        """
    def SetCompressedStack(self, stack: CompressedStack) -> None:
        """

        :param stack:
        """
    @classmethod
    def SetData(cls, slot: LocalDataStoreSlot, data: object) -> None:
        """

        :param slot:
        :param data:
        """
    @classmethod
    @overload
    def Sleep(cls, millisecondsTimeout: int) -> None:
        """

        :param millisecondsTimeout:
        """
    @classmethod
    @overload
    def Sleep(cls, timeout: TimeSpan) -> None:
        """

        :param timeout:
        """
    @classmethod
    def SpinWait(cls, iterations: int) -> None:
        """

        :param iterations:
        """
    @overload
    def Start(self) -> None:
        """"""
    @overload
    def Start(self, parameter: object) -> None:
        """

        :param parameter:
        """
    def Suspend(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TrySetApartmentState(self, state: ApartmentState) -> bool:
        """

        :param state:
        :return:
        """
    @classmethod
    @overload
    def VolatileRead(cls, address: int) -> int:
        """

        :param address:
        :return:
        """
    @classmethod
    @overload
    def VolatileRead(cls, address: float) -> float:
        """

        :param address:
        :return:
        """
    @classmethod
    @overload
    def VolatileRead(cls, address: int) -> int:
        """

        :param address:
        :return:
        """
    @classmethod
    @overload
    def VolatileRead(cls, address: int) -> int:
        """

        :param address:
        :return:
        """
    @classmethod
    @overload
    def VolatileRead(cls, address: int) -> int:
        """

        :param address:
        :return:
        """
    @classmethod
    @overload
    def VolatileRead(cls, address: IntPtr) -> IntPtr:
        """

        :param address:
        :return:
        """
    @classmethod
    @overload
    def VolatileRead(cls, address: object) -> object:
        """

        :param address:
        :return:
        """
    @classmethod
    @overload
    def VolatileRead(cls, address: int) -> int:
        """

        :param address:
        :return:
        """
    @classmethod
    @overload
    def VolatileRead(cls, address: float) -> float:
        """

        :param address:
        :return:
        """
    @classmethod
    @overload
    def VolatileRead(cls, address: int) -> int:
        """

        :param address:
        :return:
        """
    @classmethod
    @overload
    def VolatileRead(cls, address: int) -> int:
        """

        :param address:
        :return:
        """
    @classmethod
    @overload
    def VolatileRead(cls, address: int) -> int:
        """

        :param address:
        :return:
        """
    @classmethod
    @overload
    def VolatileRead(cls, address: UIntPtr) -> UIntPtr:
        """

        :param address:
        :return:
        """
    @classmethod
    @overload
    def VolatileWrite(cls, address: int, value: int) -> None:
        """

        :param address:
        :param value:
        """
    @classmethod
    @overload
    def VolatileWrite(cls, address: float, value: float) -> None:
        """

        :param address:
        :param value:
        """
    @classmethod
    @overload
    def VolatileWrite(cls, address: int, value: int) -> None:
        """

        :param address:
        :param value:
        """
    @classmethod
    @overload
    def VolatileWrite(cls, address: int, value: int) -> None:
        """

        :param address:
        :param value:
        """
    @classmethod
    @overload
    def VolatileWrite(cls, address: int, value: int) -> None:
        """

        :param address:
        :param value:
        """
    @classmethod
    @overload
    def VolatileWrite(cls, address: IntPtr, value: IntPtr) -> None:
        """

        :param address:
        :param value:
        """
    @classmethod
    @overload
    def VolatileWrite(cls, address: object, value: object) -> None:
        """

        :param address:
        :param value:
        """
    @classmethod
    @overload
    def VolatileWrite(cls, address: int, value: int) -> None:
        """

        :param address:
        :param value:
        """
    @classmethod
    @overload
    def VolatileWrite(cls, address: float, value: float) -> None:
        """

        :param address:
        :param value:
        """
    @classmethod
    @overload
    def VolatileWrite(cls, address: int, value: int) -> None:
        """

        :param address:
        :param value:
        """
    @classmethod
    @overload
    def VolatileWrite(cls, address: int, value: int) -> None:
        """

        :param address:
        :param value:
        """
    @classmethod
    @overload
    def VolatileWrite(cls, address: int, value: int) -> None:
        """

        :param address:
        :param value:
        """
    @classmethod
    @overload
    def VolatileWrite(cls, address: UIntPtr, value: UIntPtr) -> None:
        """

        :param address:
        :param value:
        """
    @classmethod
    def Yield(cls) -> bool:
        """

        :return:
        """

class ThreadAbortException(SystemException, _Exception, ISerializable):
    """"""

    @property
    def Data(self) -> IDictionary:
        """

        :return:
        """
    @property
    def ExceptionState(self) -> object:
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

class ThreadExceptionEventArgs(EventArgs):
    """"""

    def __init__(self, t: Exception):
        """

        :param t:
        """
    @property
    def Exception(self) -> Exception:
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

ThreadExceptionEventHandler: Callable[[object, ThreadExceptionEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class ThreadHandle(ValueType):
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

class ThreadHelper(Object):
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

class ThreadInterruptedException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
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

class ThreadLocal(Generic[T], Object, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, trackAllValues: bool):
        """

        :param trackAllValues:
        """
    @overload
    def __init__(self, valueFactory: Func[T]):
        """

        :param valueFactory:
        """
    @overload
    def __init__(self, valueFactory: Func[T], trackAllValues: bool):
        """

        :param valueFactory:
        :param trackAllValues:
        """
    @property
    def IsValueCreated(self) -> bool:
        """

        :return:
        """
    @property
    def Value(self) -> T:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: T) -> None: ...
    @property
    def Values(self) -> IList[T]:
        """

        :return:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ThreadPool(ABC, Object):
    """"""

    @classmethod
    @overload
    def BindHandle(cls, osHandle: SafeHandle) -> bool:
        """

        :param osHandle:
        :return:
        """
    @classmethod
    @overload
    def BindHandle(cls, osHandle: IntPtr) -> bool:
        """

        :param osHandle:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetAvailableThreads(
        cls, workerThreads: int, completionPortThreads: int
    ) -> Tuple[None, int, int]:
        """

        :param workerThreads:
        :param completionPortThreads:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    def GetMaxThreads(cls, workerThreads: int, completionPortThreads: int) -> Tuple[None, int, int]:
        """

        :param workerThreads:
        :param completionPortThreads:
        """
    @classmethod
    def GetMinThreads(cls, workerThreads: int, completionPortThreads: int) -> Tuple[None, int, int]:
        """

        :param workerThreads:
        :param completionPortThreads:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @overload
    def QueueUserWorkItem(cls, callBack: WaitCallback) -> bool:
        """

        :param callBack:
        :return:
        """
    @classmethod
    @overload
    def QueueUserWorkItem(cls, callBack: WaitCallback, state: object) -> bool:
        """

        :param callBack:
        :param state:
        :return:
        """
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
        """

        :param waitObject:
        :param callBack:
        :param state:
        :param millisecondsTimeOutInterval:
        :param executeOnlyOnce:
        :return:
        """
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
        """

        :param waitObject:
        :param callBack:
        :param state:
        :param millisecondsTimeOutInterval:
        :param executeOnlyOnce:
        :return:
        """
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
        """

        :param waitObject:
        :param callBack:
        :param state:
        :param timeout:
        :param executeOnlyOnce:
        :return:
        """
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
        """

        :param waitObject:
        :param callBack:
        :param state:
        :param millisecondsTimeOutInterval:
        :param executeOnlyOnce:
        :return:
        """
    @classmethod
    def SetMaxThreads(cls, workerThreads: int, completionPortThreads: int) -> bool:
        """

        :param workerThreads:
        :param completionPortThreads:
        :return:
        """
    @classmethod
    def SetMinThreads(cls, workerThreads: int, completionPortThreads: int) -> bool:
        """

        :param workerThreads:
        :param completionPortThreads:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def UnsafeQueueNativeOverlapped(cls, overlapped: NativeOverlapped) -> bool:
        """

        :param overlapped:
        :return:
        """
    @classmethod
    def UnsafeQueueUserWorkItem(cls, callBack: WaitCallback, state: object) -> bool:
        """

        :param callBack:
        :param state:
        :return:
        """
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
        """

        :param waitObject:
        :param callBack:
        :param state:
        :param millisecondsTimeOutInterval:
        :param executeOnlyOnce:
        :return:
        """
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
        """

        :param waitObject:
        :param callBack:
        :param state:
        :param millisecondsTimeOutInterval:
        :param executeOnlyOnce:
        :return:
        """
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
        """

        :param waitObject:
        :param callBack:
        :param state:
        :param timeout:
        :param executeOnlyOnce:
        :return:
        """
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
        """

        :param waitObject:
        :param callBack:
        :param state:
        :param millisecondsTimeOutInterval:
        :param executeOnlyOnce:
        :return:
        """

class ThreadPoolBoundHandle(Object, IDisposable):
    """"""

    @property
    def Handle(self) -> SafeHandle:
        """

        :return:
        """
    @overload
    def AllocateNativeOverlapped(self, preAllocated: PreAllocatedOverlapped) -> NativeOverlapped:
        """

        :param preAllocated:
        :return:
        """
    @overload
    def AllocateNativeOverlapped(
        self, callback: IOCompletionCallback, state: object, pinData: object
    ) -> NativeOverlapped:
        """

        :param callback:
        :param state:
        :param pinData:
        :return:
        """
    @classmethod
    def BindHandle(cls, handle: SafeHandle) -> ThreadPoolBoundHandle:
        """

        :param handle:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FreeNativeOverlapped(self, overlapped: NativeOverlapped) -> None:
        """

        :param overlapped:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    def GetNativeOverlappedState(cls, overlapped: NativeOverlapped) -> object:
        """

        :param overlapped:
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

class ThreadPoolBoundHandleOverlapped(Overlapped):
    """"""

    def __init__(
        self,
        callback: IOCompletionCallback,
        state: object,
        pinData: object,
        preAllocated: PreAllocatedOverlapped,
    ):
        """

        :param callback:
        :param state:
        :param pinData:
        :param preAllocated:
        """
    @property
    def AsyncResult(self) -> IAsyncResult:
        """

        :return:
        """
    @AsyncResult.setter
    def AsyncResult(self, value: IAsyncResult) -> None: ...
    @property
    def EventHandle(self) -> int:
        """

        :return:
        """
    @EventHandle.setter
    def EventHandle(self, value: int) -> None: ...
    @property
    def EventHandleIntPtr(self) -> IntPtr:
        """

        :return:
        """
    @EventHandleIntPtr.setter
    def EventHandleIntPtr(self, value: IntPtr) -> None: ...
    @property
    def OffsetHigh(self) -> int:
        """

        :return:
        """
    @OffsetHigh.setter
    def OffsetHigh(self, value: int) -> None: ...
    @property
    def OffsetLow(self) -> int:
        """

        :return:
        """
    @OffsetLow.setter
    def OffsetLow(self, value: int) -> None: ...
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
    @overload
    def Pack(self, iocb: IOCompletionCallback) -> NativeOverlapped:
        """

        :param iocb:
        :return:
        """
    @overload
    def Pack(self, iocb: IOCompletionCallback, userData: object) -> NativeOverlapped:
        """

        :param iocb:
        :param userData:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def UnsafePack(self, iocb: IOCompletionCallback) -> NativeOverlapped:
        """

        :param iocb:
        :return:
        """
    @overload
    def UnsafePack(self, iocb: IOCompletionCallback, userData: object) -> NativeOverlapped:
        """

        :param iocb:
        :param userData:
        :return:
        """

class ThreadPoolGlobals(ABC, Object):
    """"""

    enableWorkerTracking: Final[ClassVar[bool]] = ...
    """
    
    :return: 
    """
    processorCount: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    tpHosted: Final[ClassVar[bool]] = ...
    """
    
    :return: 
    """
    tpQuantum: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    vmTpInitialized: Final[ClassVar[bool]] = ...
    """
    
    :return: 
    """
    workQueue: Final[ClassVar[ThreadPoolWorkQueue]] = ...
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

class ThreadPoolWorkQueue(Object):
    """"""

    def __init__(self):
        """"""
    def Dequeue(
        self, tl: ThreadPoolWorkQueueThreadLocals, callback: IThreadPoolWorkItem, missedSteal: bool
    ) -> Tuple[None, IThreadPoolWorkItem, bool]:
        """

        :param tl:
        :param callback:
        :param missedSteal:
        """
    def Enqueue(self, callback: IThreadPoolWorkItem, forceGlobal: bool) -> None:
        """

        :param callback:
        :param forceGlobal:
        """
    def EnsureCurrentThreadHasQueue(self) -> ThreadPoolWorkQueueThreadLocals:
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

class ThreadPoolWorkQueueThreadLocals(Object):
    """"""

    random: Final[Random] = ...
    """
    
    :return: 
    """
    threadLocals: Final[ClassVar[ThreadPoolWorkQueueThreadLocals]] = ...
    """
    
    :return: 
    """
    workQueue: Final[ThreadPoolWorkQueue] = ...
    """
    
    :return: 
    """
    workStealingQueue: Final[ThreadPoolWorkQueue.WorkStealingQueue] = ...
    """
    
    :return: 
    """
    def __init__(self, tpq: ThreadPoolWorkQueue):
        """

        :param tpq:
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
    def __init__(self):
        """"""
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

class Timeout(ABC, Object):
    """"""

    Infinite: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    InfiniteTimeSpan: Final[ClassVar[TimeSpan]] = ...
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

class TimeoutHelper(ABC, Object):
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
    @classmethod
    def GetTime(cls) -> int:
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
    def UpdateTimeOut(cls, startTime: int, originalWaitMillisecondsTimeout: int) -> int:
        """

        :param startTime:
        :param originalWaitMillisecondsTimeout:
        :return:
        """

class Timer(MarshalByRefObject, IDisposable):
    """"""

    @overload
    def __init__(self, callback: TimerCallback):
        """

        :param callback:
        """
    @overload
    def __init__(self, callback: TimerCallback, state: object, dueTime: int, period: int):
        """

        :param callback:
        :param state:
        :param dueTime:
        :param period:
        """
    @overload
    def __init__(self, callback: TimerCallback, state: object, dueTime: int, period: int):
        """

        :param callback:
        :param state:
        :param dueTime:
        :param period:
        """
    @overload
    def __init__(self, callback: TimerCallback, state: object, dueTime: TimeSpan, period: TimeSpan):
        """

        :param callback:
        :param state:
        :param dueTime:
        :param period:
        """
    @overload
    def __init__(self, callback: TimerCallback, state: object, dueTime: int, period: int):
        """

        :param callback:
        :param state:
        :param dueTime:
        :param period:
        """
    @overload
    def Change(self, dueTime: int, period: int) -> bool:
        """

        :param dueTime:
        :param period:
        :return:
        """
    @overload
    def Change(self, dueTime: int, period: int) -> bool:
        """

        :param dueTime:
        :param period:
        :return:
        """
    @overload
    def Change(self, dueTime: TimeSpan, period: TimeSpan) -> bool:
        """

        :param dueTime:
        :param period:
        :return:
        """
    @overload
    def Change(self, dueTime: int, period: int) -> bool:
        """

        :param dueTime:
        :param period:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    @overload
    def Dispose(self) -> None:
        """"""
    @overload
    def Dispose(self, notifyObject: WaitHandle) -> bool:
        """

        :param notifyObject:
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
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

TimerCallback: Callable[[object], None] = ...
"""

:param state: 
"""

class TimerHolder(Object):
    """"""

    def __init__(self, timer: object):
        """

        :param timer:
        """
    def Change(self, dueTime: int, period: int) -> bool:
        """

        :param dueTime:
        :param period:
        :return:
        """
    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, notifyObject: WaitHandle) -> bool:
        """

        :param notifyObject:
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

class TimerQueue(Object):
    """"""

    @classmethod
    @property
    def Instance(cls) -> TimerQueue:
        """

        :return:
        """
    def DeleteTimer(self, timer: TimerQueueTimer) -> None:
        """

        :param timer:
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
    def UpdateTimer(self, timer: TimerQueueTimer, dueTime: int, period: int) -> bool:
        """

        :param timer:
        :param dueTime:
        :param period:
        :return:
        """

class TimerQueueTimer(Object):
    """"""

    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, toSignal: WaitHandle) -> bool:
        """

        :param toSignal:
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

class Volatile(ABC, Object):
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
    @overload
    def Read(cls, location: T) -> T:
        """

        :param location:
        :return:
        """
    @classmethod
    @overload
    def Read(cls, location: bool) -> bool:
        """

        :param location:
        :return:
        """
    @classmethod
    @overload
    def Read(cls, location: int) -> int:
        """

        :param location:
        :return:
        """
    @classmethod
    @overload
    def Read(cls, location: float) -> float:
        """

        :param location:
        :return:
        """
    @classmethod
    @overload
    def Read(cls, location: int) -> int:
        """

        :param location:
        :return:
        """
    @classmethod
    @overload
    def Read(cls, location: int) -> int:
        """

        :param location:
        :return:
        """
    @classmethod
    @overload
    def Read(cls, location: int) -> int:
        """

        :param location:
        :return:
        """
    @classmethod
    @overload
    def Read(cls, location: IntPtr) -> IntPtr:
        """

        :param location:
        :return:
        """
    @classmethod
    @overload
    def Read(cls, location: int) -> int:
        """

        :param location:
        :return:
        """
    @classmethod
    @overload
    def Read(cls, location: float) -> float:
        """

        :param location:
        :return:
        """
    @classmethod
    @overload
    def Read(cls, location: int) -> int:
        """

        :param location:
        :return:
        """
    @classmethod
    @overload
    def Read(cls, location: int) -> int:
        """

        :param location:
        :return:
        """
    @classmethod
    @overload
    def Read(cls, location: int) -> int:
        """

        :param location:
        :return:
        """
    @classmethod
    @overload
    def Read(cls, location: UIntPtr) -> UIntPtr:
        """

        :param location:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    @overload
    def Write(cls, location: T, value: T) -> None:
        """

        :param location:
        :param value:
        """
    @classmethod
    @overload
    def Write(cls, location: bool, value: bool) -> None:
        """

        :param location:
        :param value:
        """
    @classmethod
    @overload
    def Write(cls, location: int, value: int) -> None:
        """

        :param location:
        :param value:
        """
    @classmethod
    @overload
    def Write(cls, location: float, value: float) -> None:
        """

        :param location:
        :param value:
        """
    @classmethod
    @overload
    def Write(cls, location: int, value: int) -> None:
        """

        :param location:
        :param value:
        """
    @classmethod
    @overload
    def Write(cls, location: int, value: int) -> None:
        """

        :param location:
        :param value:
        """
    @classmethod
    @overload
    def Write(cls, location: int, value: int) -> None:
        """

        :param location:
        :param value:
        """
    @classmethod
    @overload
    def Write(cls, location: IntPtr, value: IntPtr) -> None:
        """

        :param location:
        :param value:
        """
    @classmethod
    @overload
    def Write(cls, location: int, value: int) -> None:
        """

        :param location:
        :param value:
        """
    @classmethod
    @overload
    def Write(cls, location: float, value: float) -> None:
        """

        :param location:
        :param value:
        """
    @classmethod
    @overload
    def Write(cls, location: int, value: int) -> None:
        """

        :param location:
        :param value:
        """
    @classmethod
    @overload
    def Write(cls, location: int, value: int) -> None:
        """

        :param location:
        :param value:
        """
    @classmethod
    @overload
    def Write(cls, location: int, value: int) -> None:
        """

        :param location:
        :param value:
        """
    @classmethod
    @overload
    def Write(cls, location: UIntPtr, value: UIntPtr) -> None:
        """

        :param location:
        :param value:
        """

WaitCallback: Callable[[object], None] = ...
"""

:param state: 
"""

class WaitHandle(ABC, MarshalByRefObject, IDisposable):
    """"""

    WaitTimeout: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @property
    def Handle(self) -> IntPtr:
        """

        :return:
        """
    @Handle.setter
    def Handle(self, value: IntPtr) -> None: ...
    @property
    def SafeWaitHandle(self) -> SafeWaitHandle:
        """

        :return:
        """
    @SafeWaitHandle.setter
    def SafeWaitHandle(self, value: SafeWaitHandle) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
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
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    @classmethod
    @overload
    def SignalAndWait(cls, toSignal: WaitHandle, toWaitOn: WaitHandle) -> bool:
        """

        :param toSignal:
        :param toWaitOn:
        :return:
        """
    @classmethod
    @overload
    def SignalAndWait(
        cls, toSignal: WaitHandle, toWaitOn: WaitHandle, millisecondsTimeout: int, exitContext: bool
    ) -> bool:
        """

        :param toSignal:
        :param toWaitOn:
        :param millisecondsTimeout:
        :param exitContext:
        :return:
        """
    @classmethod
    @overload
    def SignalAndWait(
        cls, toSignal: WaitHandle, toWaitOn: WaitHandle, timeout: TimeSpan, exitContext: bool
    ) -> bool:
        """

        :param toSignal:
        :param toWaitOn:
        :param timeout:
        :param exitContext:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    @overload
    def WaitAll(cls, waitHandles: Array[WaitHandle]) -> bool:
        """

        :param waitHandles:
        :return:
        """
    @classmethod
    @overload
    def WaitAll(cls, waitHandles: Array[WaitHandle], millisecondsTimeout: int) -> bool:
        """

        :param waitHandles:
        :param millisecondsTimeout:
        :return:
        """
    @classmethod
    @overload
    def WaitAll(cls, waitHandles: Array[WaitHandle], timeout: TimeSpan) -> bool:
        """

        :param waitHandles:
        :param timeout:
        :return:
        """
    @classmethod
    @overload
    def WaitAll(
        cls, waitHandles: Array[WaitHandle], millisecondsTimeout: int, exitContext: bool
    ) -> bool:
        """

        :param waitHandles:
        :param millisecondsTimeout:
        :param exitContext:
        :return:
        """
    @classmethod
    @overload
    def WaitAll(cls, waitHandles: Array[WaitHandle], timeout: TimeSpan, exitContext: bool) -> bool:
        """

        :param waitHandles:
        :param timeout:
        :param exitContext:
        :return:
        """
    @classmethod
    @overload
    def WaitAny(cls, waitHandles: Array[WaitHandle]) -> int:
        """

        :param waitHandles:
        :return:
        """
    @classmethod
    @overload
    def WaitAny(cls, waitHandles: Array[WaitHandle], millisecondsTimeout: int) -> int:
        """

        :param waitHandles:
        :param millisecondsTimeout:
        :return:
        """
    @classmethod
    @overload
    def WaitAny(cls, waitHandles: Array[WaitHandle], timeout: TimeSpan) -> int:
        """

        :param waitHandles:
        :param timeout:
        :return:
        """
    @classmethod
    @overload
    def WaitAny(
        cls, waitHandles: Array[WaitHandle], millisecondsTimeout: int, exitContext: bool
    ) -> int:
        """

        :param waitHandles:
        :param millisecondsTimeout:
        :param exitContext:
        :return:
        """
    @classmethod
    @overload
    def WaitAny(cls, waitHandles: Array[WaitHandle], timeout: TimeSpan, exitContext: bool) -> int:
        """

        :param waitHandles:
        :param timeout:
        :param exitContext:
        :return:
        """
    @overload
    def WaitOne(self) -> bool:
        """

        :return:
        """
    @overload
    def WaitOne(self, millisecondsTimeout: int) -> bool:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def WaitOne(self, timeout: TimeSpan) -> bool:
        """

        :param timeout:
        :return:
        """
    @overload
    def WaitOne(self, millisecondsTimeout: int, exitContext: bool) -> bool:
        """

        :param millisecondsTimeout:
        :param exitContext:
        :return:
        """
    @overload
    def WaitOne(self, timeout: TimeSpan, exitContext: bool) -> bool:
        """

        :param timeout:
        :param exitContext:
        :return:
        """

class WaitHandleCannotBeOpenedException(ApplicationException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
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

class WaitHandleExtensions(ABC, Object):
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
    @classmethod
    def GetSafeWaitHandle(cls, waitHandle: WaitHandle) -> SafeWaitHandle:
        """

        :param waitHandle:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def SetSafeWaitHandle(cls, waitHandle: WaitHandle, value: SafeWaitHandle) -> None:
        """

        :param waitHandle:
        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """

WaitOrTimerCallback: Callable[[object, bool], None] = ...
"""

:param state: 
:param timedOut: 
"""

class WinRTSynchronizationContextFactoryBase(Object):
    """"""

    def __init__(self):
        """"""
    def Create(self, coreDispatcher: object) -> SynchronizationContext:
        """

        :param coreDispatcher:
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

class _IOCompletionCallback(Object):
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

class _ThreadPoolWaitCallback(ABC, Object):
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

class _ThreadPoolWaitOrTimerCallback(Object):
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
