from __future__ import annotations

from abc import ABC
from typing import Callable, Generic, List, Protocol, Tuple, TypeVar, Union, overload

from Microsoft.Win32.SafeHandles import SafeWaitHandle
from System import Action, AppDomain, ApplicationException, Array, AsyncCallback, Boolean, Byte, Double, Enum, EventArgs, Exception, Func, IAsyncResult, ICloneable, IDisposable, IEquatable, Int16, Int32, Int64, IntPtr, LocalDataStoreSlot, MarshalByRefObject, MulticastDelegate, Object, Random, SByte, Single, String, SystemException, TimeSpan, UInt16, UInt32, UInt64, UIntPtr, ValueType, Void
from System.Collections.Generic import IList, List
from System.Diagnostics.Tracing import EventSource
from System.Globalization import CultureInfo
from System.Runtime.ConstrainedExecution import CriticalFinalizerObject
from System.Runtime.InteropServices import SafeHandle, _Exception, _Thread
from System.Runtime.Remoting.Contexts import Context
from System.Runtime.Serialization import ISerializable, SerializationInfo, StreamingContext
from System.Security.AccessControl import EventWaitHandleRights, EventWaitHandleSecurity, MutexRights, MutexSecurity, SemaphoreRights, SemaphoreSecurity
from System.Security.Principal import IPrincipal
from System.Threading.Tasks import Task

# ---------- Types ---------- #

T = TypeVar('T')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
DoubleType = Union[float, Double]
FloatType = Union[float, Single]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
NUIntType = Union[int, UIntPtr]
ObjectType = Object
SByteType = Union[int, SByte]
ShortType = Union[int, Int16]
StringType = Union[str, String]
UIntType = Union[int, UInt32]
ULongType = Union[int, UInt64]
UShortType = Union[int, UInt16]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class AbandonedMutexException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    @overload
    def __init__(self, location: IntType, handle: WaitHandle): ...
    
    @overload
    def __init__(self, message: StringType, location: IntType, handle: WaitHandle): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception, location: IntType, handle: WaitHandle): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Mutex(self) -> Mutex: ...
    
    @property
    def MutexIndex(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_Mutex(self) -> Mutex: ...
    
    def get_MutexIndex(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsyncLocal(Generic[T], ObjectType, IAsyncLocal):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, valueChangedHandler: Action[AsyncLocalValueChangedArgs[T]]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> T: ...
    
    @Value.setter
    def Value(self, value: T) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Value(self) -> T: ...
    
    def set_Value(self, value: T) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsyncLocalValueMap(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Empty() -> IAsyncLocalValueMap: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Create(key: IAsyncLocal, value: ObjectType, treatNullValueAsNonexistent: BooleanType) -> IAsyncLocalValueMap: ...
    
    @staticmethod
    def IsEmpty(asyncLocalValueMap: IAsyncLocalValueMap) -> BooleanType: ...
    
    @staticmethod
    def get_Empty() -> IAsyncLocalValueMap: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AutoResetEvent(EventWaitHandle, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, initialState: BooleanType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Barrier(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, participantCount: IntType): ...
    
    @overload
    def __init__(self, participantCount: IntType, postPhaseAction: Action[Barrier]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CurrentPhaseNumber(self) -> LongType: ...
    
    @property
    def ParticipantCount(self) -> IntType: ...
    
    @property
    def ParticipantsRemaining(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def AddParticipant(self) -> LongType: ...
    
    def AddParticipants(self, participantCount: IntType) -> LongType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def RemoveParticipant(self) -> VoidType: ...
    
    def RemoveParticipants(self, participantCount: IntType) -> VoidType: ...
    
    @overload
    def SignalAndWait(self) -> VoidType: ...
    
    @overload
    def SignalAndWait(self, cancellationToken: CancellationToken) -> VoidType: ...
    
    @overload
    def SignalAndWait(self, timeout: TimeSpan) -> BooleanType: ...
    
    @overload
    def SignalAndWait(self, timeout: TimeSpan, cancellationToken: CancellationToken) -> BooleanType: ...
    
    @overload
    def SignalAndWait(self, millisecondsTimeout: IntType) -> BooleanType: ...
    
    @overload
    def SignalAndWait(self, millisecondsTimeout: IntType, cancellationToken: CancellationToken) -> BooleanType: ...
    
    def get_CurrentPhaseNumber(self) -> LongType: ...
    
    def get_ParticipantCount(self) -> IntType: ...
    
    def get_ParticipantsRemaining(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BarrierPostPhaseException(Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, innerException: Exception): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CancellationCallbackInfo(ObjectType):
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


class CancellationTokenSource(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, delay: TimeSpan): ...
    
    @overload
    def __init__(self, millisecondsDelay: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsCancellationRequested(self) -> BooleanType: ...
    
    @property
    def Token(self) -> CancellationToken: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Cancel(self, throwOnFirstException: BooleanType) -> VoidType: ...
    
    @overload
    def Cancel(self) -> VoidType: ...
    
    @overload
    def CancelAfter(self, delay: TimeSpan) -> VoidType: ...
    
    @overload
    def CancelAfter(self, millisecondsDelay: IntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def CreateLinkedTokenSource(token1: CancellationToken, token2: CancellationToken) -> CancellationTokenSource: ...
    
    @staticmethod
    @overload
    def CreateLinkedTokenSource(tokens: ArrayType[CancellationToken]) -> CancellationTokenSource: ...
    
    def Dispose(self) -> VoidType: ...
    
    def get_IsCancellationRequested(self) -> BooleanType: ...
    
    def get_Token(self) -> CancellationToken: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CdsSyncEtwBCLProvider(EventSource, IDisposable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Log() -> CdsSyncEtwBCLProvider: ...
    
    @staticmethod
    @Log.setter
    def Log(value: CdsSyncEtwBCLProvider) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Barrier_PhaseFinished(self, currentSense: BooleanType, phaseNum: LongType) -> VoidType: ...
    
    def SpinLock_FastPathFailed(self, ownerID: IntType) -> VoidType: ...
    
    def SpinWait_NextSpinWillYield(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CompressedStack(ObjectType, ISerializable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Capture() -> CompressedStack: ...
    
    def CreateCopy(self) -> CompressedStack: ...
    
    @staticmethod
    def GetCompressedStack() -> CompressedStack: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    @staticmethod
    def Run(compressedStack: CompressedStack, callback: ContextCallback, state: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContextCallback(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, state: ObjectType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, state: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CountdownEvent(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, initialCount: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CurrentCount(self) -> IntType: ...
    
    @property
    def InitialCount(self) -> IntType: ...
    
    @property
    def IsSet(self) -> BooleanType: ...
    
    @property
    def WaitHandle(self) -> WaitHandle: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AddCount(self) -> VoidType: ...
    
    @overload
    def AddCount(self, signalCount: IntType) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    @overload
    def Reset(self) -> VoidType: ...
    
    @overload
    def Reset(self, count: IntType) -> VoidType: ...
    
    @overload
    def Signal(self) -> BooleanType: ...
    
    @overload
    def Signal(self, signalCount: IntType) -> BooleanType: ...
    
    @overload
    def TryAddCount(self) -> BooleanType: ...
    
    @overload
    def TryAddCount(self, signalCount: IntType) -> BooleanType: ...
    
    @overload
    def Wait(self) -> VoidType: ...
    
    @overload
    def Wait(self, cancellationToken: CancellationToken) -> VoidType: ...
    
    @overload
    def Wait(self, timeout: TimeSpan) -> BooleanType: ...
    
    @overload
    def Wait(self, timeout: TimeSpan, cancellationToken: CancellationToken) -> BooleanType: ...
    
    @overload
    def Wait(self, millisecondsTimeout: IntType) -> BooleanType: ...
    
    @overload
    def Wait(self, millisecondsTimeout: IntType, cancellationToken: CancellationToken) -> BooleanType: ...
    
    def get_CurrentCount(self) -> IntType: ...
    
    def get_InitialCount(self) -> IntType: ...
    
    def get_IsSet(self) -> BooleanType: ...
    
    def get_WaitHandle(self) -> WaitHandle: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DomainCompressedStack(ObjectType):
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


class EventWaitHandle(WaitHandle, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, initialState: BooleanType, mode: EventResetMode): ...
    
    @overload
    def __init__(self, initialState: BooleanType, mode: EventResetMode, name: StringType): ...
    
    @overload
    def __init__(self, initialState: BooleanType, mode: EventResetMode, name: StringType, createdNew: BooleanType): ...
    
    @overload
    def __init__(self, initialState: BooleanType, mode: EventResetMode, name: StringType, createdNew: BooleanType, eventSecurity: EventWaitHandleSecurity): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetAccessControl(self) -> EventWaitHandleSecurity: ...
    
    @staticmethod
    @overload
    def OpenExisting(name: StringType) -> EventWaitHandle: ...
    
    @staticmethod
    @overload
    def OpenExisting(name: StringType, rights: EventWaitHandleRights) -> EventWaitHandle: ...
    
    def Reset(self) -> BooleanType: ...
    
    def Set(self) -> BooleanType: ...
    
    def SetAccessControl(self, eventSecurity: EventWaitHandleSecurity) -> VoidType: ...
    
    @staticmethod
    @overload
    def TryOpenExisting(name: StringType, result: EventWaitHandle) -> Tuple[BooleanType, EventWaitHandle]: ...
    
    @staticmethod
    @overload
    def TryOpenExisting(name: StringType, rights: EventWaitHandleRights, result: EventWaitHandle) -> Tuple[BooleanType, EventWaitHandle]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExecutionContext(ObjectType, IDisposable, ISerializable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Capture() -> ExecutionContext: ...
    
    def CreateCopy(self) -> ExecutionContext: ...
    
    def Dispose(self) -> VoidType: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    @staticmethod
    def IsFlowSuppressed() -> BooleanType: ...
    
    @staticmethod
    def RestoreFlow() -> VoidType: ...
    
    @staticmethod
    def Run(executionContext: ExecutionContext, callback: ContextCallback, state: ObjectType) -> VoidType: ...
    
    @staticmethod
    def SuppressFlow() -> AsyncFlowControl: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Gen2GcCallback(CriticalFinalizerObject):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Register(callback: Func[ObjectType, BooleanType], targetObj: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HostExecutionContext(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, state: ObjectType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CreateCopy(self) -> HostExecutionContext: ...
    
    @overload
    def Dispose(self) -> VoidType: ...
    
    @overload
    def Dispose(self, disposing: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HostExecutionContextManager(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Capture(self) -> HostExecutionContext: ...
    
    def Revert(self, previousState: ObjectType) -> VoidType: ...
    
    def SetHostExecutionContext(self, hostExecutionContext: HostExecutionContext) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HostExecutionContextSwitcher(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Undo(switcherObject: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IOCompletionCallback(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, errorCode: UIntType, numBytes: UIntType, pOVERLAP: NativeOverlapped, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, errorCode: UIntType, numBytes: UIntType, pOVERLAP: NativeOverlapped) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IUnknownSafeHandle(SafeHandle, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsInvalid(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_IsInvalid(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Interlocked(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Add(location1: IntType, value: IntType) -> Tuple[IntType, IntType]: ...
    
    @staticmethod
    @overload
    def Add(location1: LongType, value: LongType) -> Tuple[LongType, LongType]: ...
    
    @staticmethod
    @overload
    def CompareExchange(location1: LongType, value: LongType, comparand: LongType) -> Tuple[LongType, LongType]: ...
    
    @staticmethod
    @overload
    def CompareExchange(location1: FloatType, value: FloatType, comparand: FloatType) -> Tuple[FloatType, FloatType]: ...
    
    @staticmethod
    @overload
    def CompareExchange(location1: DoubleType, value: DoubleType, comparand: DoubleType) -> Tuple[DoubleType, DoubleType]: ...
    
    @staticmethod
    @overload
    def CompareExchange(location1: T, value: T, comparand: T) -> Tuple[T, T]: ...
    
    @staticmethod
    @overload
    def CompareExchange(location1: IntType, value: IntType, comparand: IntType) -> Tuple[IntType, IntType]: ...
    
    @staticmethod
    @overload
    def CompareExchange(location1: ObjectType, value: ObjectType, comparand: ObjectType) -> Tuple[ObjectType, ObjectType]: ...
    
    @staticmethod
    @overload
    def CompareExchange(location1: NIntType, value: NIntType, comparand: NIntType) -> Tuple[NIntType, NIntType]: ...
    
    @staticmethod
    @overload
    def Decrement(location: IntType) -> Tuple[IntType, IntType]: ...
    
    @staticmethod
    @overload
    def Decrement(location: LongType) -> Tuple[LongType, LongType]: ...
    
    @staticmethod
    @overload
    def Exchange(location1: LongType, value: LongType) -> Tuple[LongType, LongType]: ...
    
    @staticmethod
    @overload
    def Exchange(location1: FloatType, value: FloatType) -> Tuple[FloatType, FloatType]: ...
    
    @staticmethod
    @overload
    def Exchange(location1: DoubleType, value: DoubleType) -> Tuple[DoubleType, DoubleType]: ...
    
    @staticmethod
    @overload
    def Exchange(location1: T, value: T) -> Tuple[T, T]: ...
    
    @staticmethod
    @overload
    def Exchange(location1: IntType, value: IntType) -> Tuple[IntType, IntType]: ...
    
    @staticmethod
    @overload
    def Exchange(location1: ObjectType, value: ObjectType) -> Tuple[ObjectType, ObjectType]: ...
    
    @staticmethod
    @overload
    def Exchange(location1: NIntType, value: NIntType) -> Tuple[NIntType, NIntType]: ...
    
    @staticmethod
    @overload
    def Increment(location: IntType) -> Tuple[IntType, IntType]: ...
    
    @staticmethod
    @overload
    def Increment(location: LongType) -> Tuple[LongType, LongType]: ...
    
    @staticmethod
    def MemoryBarrier() -> VoidType: ...
    
    @staticmethod
    def Read(location: LongType) -> Tuple[LongType, LongType]: ...
    
    @staticmethod
    def SpeculationBarrier() -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalCrossContextDelegate(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, args: ArrayType[ObjectType], callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> ObjectType: ...
    
    def Invoke(self, args: ArrayType[ObjectType]) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LazyHelpers(Protocol[T], ObjectType):
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


class LazyInitializer(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def EnsureInitialized(target: T, valueFactory: Func[T]) -> Tuple[T, T]: ...
    
    @staticmethod
    @overload
    def EnsureInitialized(target: T) -> Tuple[T, T]: ...
    
    @staticmethod
    @overload
    def EnsureInitialized(target: T, initialized: BooleanType, syncLock: ObjectType) -> Tuple[T, T, BooleanType, ObjectType]: ...
    
    @staticmethod
    @overload
    def EnsureInitialized(target: T, initialized: BooleanType, syncLock: ObjectType, valueFactory: Func[T]) -> Tuple[T, T, BooleanType, ObjectType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LockRecursionException(Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManualResetEvent(EventWaitHandle, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, initialState: BooleanType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManualResetEventSlim(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, initialState: BooleanType): ...
    
    @overload
    def __init__(self, initialState: BooleanType, spinCount: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsSet(self) -> BooleanType: ...
    
    @property
    def SpinCount(self) -> IntType: ...
    
    @property
    def WaitHandle(self) -> WaitHandle: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def Reset(self) -> VoidType: ...
    
    def Set(self) -> VoidType: ...
    
    @overload
    def Wait(self) -> VoidType: ...
    
    @overload
    def Wait(self, cancellationToken: CancellationToken) -> VoidType: ...
    
    @overload
    def Wait(self, timeout: TimeSpan) -> BooleanType: ...
    
    @overload
    def Wait(self, timeout: TimeSpan, cancellationToken: CancellationToken) -> BooleanType: ...
    
    @overload
    def Wait(self, millisecondsTimeout: IntType) -> BooleanType: ...
    
    @overload
    def Wait(self, millisecondsTimeout: IntType, cancellationToken: CancellationToken) -> BooleanType: ...
    
    def get_IsSet(self) -> BooleanType: ...
    
    def get_SpinCount(self) -> IntType: ...
    
    def get_WaitHandle(self) -> WaitHandle: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Monitor(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Enter(obj: ObjectType, lockTaken: BooleanType) -> Tuple[VoidType, BooleanType]: ...
    
    @staticmethod
    @overload
    def Enter(obj: ObjectType) -> VoidType: ...
    
    @staticmethod
    def Exit(obj: ObjectType) -> VoidType: ...
    
    @staticmethod
    def IsEntered(obj: ObjectType) -> BooleanType: ...
    
    @staticmethod
    def Pulse(obj: ObjectType) -> VoidType: ...
    
    @staticmethod
    def PulseAll(obj: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def TryEnter(obj: ObjectType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def TryEnter(obj: ObjectType, lockTaken: BooleanType) -> Tuple[VoidType, BooleanType]: ...
    
    @staticmethod
    @overload
    def TryEnter(obj: ObjectType, millisecondsTimeout: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def TryEnter(obj: ObjectType, timeout: TimeSpan) -> BooleanType: ...
    
    @staticmethod
    @overload
    def TryEnter(obj: ObjectType, millisecondsTimeout: IntType, lockTaken: BooleanType) -> Tuple[VoidType, BooleanType]: ...
    
    @staticmethod
    @overload
    def TryEnter(obj: ObjectType, timeout: TimeSpan, lockTaken: BooleanType) -> Tuple[VoidType, BooleanType]: ...
    
    @staticmethod
    @overload
    def Wait(obj: ObjectType, millisecondsTimeout: IntType, exitContext: BooleanType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Wait(obj: ObjectType, timeout: TimeSpan, exitContext: BooleanType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Wait(obj: ObjectType, millisecondsTimeout: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Wait(obj: ObjectType, timeout: TimeSpan) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Wait(obj: ObjectType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Mutex(WaitHandle, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, initiallyOwned: BooleanType, name: StringType, createdNew: BooleanType): ...
    
    @overload
    def __init__(self, initiallyOwned: BooleanType, name: StringType, createdNew: BooleanType, mutexSecurity: MutexSecurity): ...
    
    @overload
    def __init__(self, initiallyOwned: BooleanType, name: StringType): ...
    
    @overload
    def __init__(self, initiallyOwned: BooleanType): ...
    
    @overload
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetAccessControl(self) -> MutexSecurity: ...
    
    @staticmethod
    @overload
    def OpenExisting(name: StringType) -> Mutex: ...
    
    @staticmethod
    @overload
    def OpenExisting(name: StringType, rights: MutexRights) -> Mutex: ...
    
    def ReleaseMutex(self) -> VoidType: ...
    
    def SetAccessControl(self, mutexSecurity: MutexSecurity) -> VoidType: ...
    
    @staticmethod
    @overload
    def TryOpenExisting(name: StringType, result: Mutex) -> Tuple[BooleanType, Mutex]: ...
    
    @staticmethod
    @overload
    def TryOpenExisting(name: StringType, rights: MutexRights, result: Mutex) -> Tuple[BooleanType, Mutex]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Overlapped(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, offsetLo: IntType, offsetHi: IntType, hEvent: NIntType, ar: IAsyncResult): ...
    
    @overload
    def __init__(self, offsetLo: IntType, offsetHi: IntType, hEvent: IntType, ar: IAsyncResult): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AsyncResult(self) -> IAsyncResult: ...
    
    @AsyncResult.setter
    def AsyncResult(self, value: IAsyncResult) -> None: ...
    
    @property
    def EventHandle(self) -> IntType: ...
    
    @EventHandle.setter
    def EventHandle(self, value: IntType) -> None: ...
    
    @property
    def EventHandleIntPtr(self) -> NIntType: ...
    
    @EventHandleIntPtr.setter
    def EventHandleIntPtr(self, value: NIntType) -> None: ...
    
    @property
    def OffsetHigh(self) -> IntType: ...
    
    @OffsetHigh.setter
    def OffsetHigh(self, value: IntType) -> None: ...
    
    @property
    def OffsetLow(self) -> IntType: ...
    
    @OffsetLow.setter
    def OffsetLow(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Free(nativeOverlappedPtr: NativeOverlapped) -> VoidType: ...
    
    @overload
    def Pack(self, iocb: IOCompletionCallback, userData: ObjectType) -> NativeOverlapped: ...
    
    @overload
    def Pack(self, iocb: IOCompletionCallback) -> NativeOverlapped: ...
    
    @staticmethod
    def Unpack(nativeOverlappedPtr: NativeOverlapped) -> Overlapped: ...
    
    @overload
    def UnsafePack(self, iocb: IOCompletionCallback, userData: ObjectType) -> NativeOverlapped: ...
    
    @overload
    def UnsafePack(self, iocb: IOCompletionCallback) -> NativeOverlapped: ...
    
    def get_AsyncResult(self) -> IAsyncResult: ...
    
    def get_EventHandle(self) -> IntType: ...
    
    def get_EventHandleIntPtr(self) -> NIntType: ...
    
    def get_OffsetHigh(self) -> IntType: ...
    
    def get_OffsetLow(self) -> IntType: ...
    
    def set_AsyncResult(self, value: IAsyncResult) -> VoidType: ...
    
    def set_EventHandle(self, value: IntType) -> VoidType: ...
    
    def set_EventHandleIntPtr(self, value: NIntType) -> VoidType: ...
    
    def set_OffsetHigh(self, value: IntType) -> VoidType: ...
    
    def set_OffsetLow(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OverlappedData(ObjectType):
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


class ParameterizedThreadStart(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, obj: ObjectType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, obj: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PinnableBufferCache(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, cacheName: StringType, numberOfElements: IntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AllocateBuffer(self) -> ArrayType[ByteType]: ...
    
    def FreeBuffer(self, buffer: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PinnableBufferCacheEventSource(EventSource, IDisposable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Log() -> PinnableBufferCacheEventSource: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AgePendingBuffersResults(self, cacheName: StringType, promotedToFreeListCount: IntType, heldBackCount: IntType) -> VoidType: ...
    
    def AllocateBuffer(self, cacheName: StringType, objectId: ULongType, objectHash: IntType, objectGen: IntType, freeCountAfter: IntType) -> VoidType: ...
    
    def AllocateBufferAged(self, cacheName: StringType, agedCount: IntType) -> VoidType: ...
    
    def AllocateBufferCreatingNewBuffers(self, cacheName: StringType, totalBuffsBefore: IntType, objectCount: IntType) -> VoidType: ...
    
    def AllocateBufferFreeListEmpty(self, cacheName: StringType, notGen2CountBefore: IntType) -> VoidType: ...
    
    def AllocateBufferFromNotGen2(self, cacheName: StringType, notGen2CountAfter: IntType) -> VoidType: ...
    
    def Create(self, cacheName: StringType) -> VoidType: ...
    
    def DebugMessage(self, message: StringType) -> VoidType: ...
    
    def DebugMessage1(self, message: StringType, value: LongType) -> VoidType: ...
    
    def DebugMessage2(self, message: StringType, value1: LongType, value2: LongType) -> VoidType: ...
    
    def DebugMessage3(self, message: StringType, value1: LongType, value2: LongType, value3: LongType) -> VoidType: ...
    
    def FreeBuffer(self, cacheName: StringType, objectId: ULongType, objectHash: IntType, freeCountBefore: IntType) -> VoidType: ...
    
    def FreeBufferNull(self, cacheName: StringType, freeCountBefore: IntType) -> VoidType: ...
    
    def FreeBufferStillTooYoung(self, cacheName: StringType, notGen2CountBefore: IntType) -> VoidType: ...
    
    def TrimCheck(self, cacheName: StringType, totalBuffs: IntType, neededMoreThanFreeList: BooleanType, deltaMSec: IntType) -> VoidType: ...
    
    def TrimExperiment(self, cacheName: StringType, totalBuffs: IntType, freeListCount: IntType, numTrimTrial: IntType) -> VoidType: ...
    
    def TrimFlush(self, cacheName: StringType, totalBuffs: IntType, freeListCount: IntType, notGen2CountBefore: IntType) -> VoidType: ...
    
    def TrimFree(self, cacheName: StringType, totalBuffs: IntType, freeListCount: IntType, toBeFreed: IntType) -> VoidType: ...
    
    def TrimFreeSizeOK(self, cacheName: StringType, totalBuffs: IntType, freeListCount: IntType) -> VoidType: ...
    
    def WalkFreeListResult(self, cacheName: StringType, freeListCount: IntType, gen0BuffersInFreeList: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PlatformHelper(ABC, ObjectType):
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


class PreAllocatedOverlapped(ObjectType, IDisposable, IDeferredDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, callback: IOCompletionCallback, state: ObjectType, pinData: ObjectType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class QueueUserWorkItemCallback(ObjectType, IThreadPoolWorkItem):
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


class ReaderWriterCount(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def lockID(self) -> LongType: ...
    
    @lockID.setter
    def lockID(self, value: LongType) -> None: ...
    
    @property
    def next(self) -> ReaderWriterCount: ...
    
    @next.setter
    def next(self, value: ReaderWriterCount) -> None: ...
    
    @property
    def readercount(self) -> IntType: ...
    
    @readercount.setter
    def readercount(self, value: IntType) -> None: ...
    
    @property
    def upgradecount(self) -> IntType: ...
    
    @upgradecount.setter
    def upgradecount(self, value: IntType) -> None: ...
    
    @property
    def writercount(self) -> IntType: ...
    
    @writercount.setter
    def writercount(self, value: IntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReaderWriterLock(CriticalFinalizerObject):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsReaderLockHeld(self) -> BooleanType: ...
    
    @property
    def IsWriterLockHeld(self) -> BooleanType: ...
    
    @property
    def WriterSeqNum(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AcquireReaderLock(self, millisecondsTimeout: IntType) -> VoidType: ...
    
    @overload
    def AcquireReaderLock(self, timeout: TimeSpan) -> VoidType: ...
    
    @overload
    def AcquireWriterLock(self, millisecondsTimeout: IntType) -> VoidType: ...
    
    @overload
    def AcquireWriterLock(self, timeout: TimeSpan) -> VoidType: ...
    
    def AnyWritersSince(self, seqNum: IntType) -> BooleanType: ...
    
    def DowngradeFromWriterLock(self, lockCookie: LockCookie) -> Tuple[VoidType, LockCookie]: ...
    
    def ReleaseLock(self) -> LockCookie: ...
    
    def ReleaseReaderLock(self) -> VoidType: ...
    
    def ReleaseWriterLock(self) -> VoidType: ...
    
    def RestoreLock(self, lockCookie: LockCookie) -> Tuple[VoidType, LockCookie]: ...
    
    @overload
    def UpgradeToWriterLock(self, millisecondsTimeout: IntType) -> LockCookie: ...
    
    @overload
    def UpgradeToWriterLock(self, timeout: TimeSpan) -> LockCookie: ...
    
    def get_IsReaderLockHeld(self) -> BooleanType: ...
    
    def get_IsWriterLockHeld(self) -> BooleanType: ...
    
    def get_WriterSeqNum(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReaderWriterLockSlim(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, recursionPolicy: LockRecursionPolicy): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CurrentReadCount(self) -> IntType: ...
    
    @property
    def IsReadLockHeld(self) -> BooleanType: ...
    
    @property
    def IsUpgradeableReadLockHeld(self) -> BooleanType: ...
    
    @property
    def IsWriteLockHeld(self) -> BooleanType: ...
    
    @property
    def RecursionPolicy(self) -> LockRecursionPolicy: ...
    
    @property
    def RecursiveReadCount(self) -> IntType: ...
    
    @property
    def RecursiveUpgradeCount(self) -> IntType: ...
    
    @property
    def RecursiveWriteCount(self) -> IntType: ...
    
    @property
    def WaitingReadCount(self) -> IntType: ...
    
    @property
    def WaitingUpgradeCount(self) -> IntType: ...
    
    @property
    def WaitingWriteCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def EnterReadLock(self) -> VoidType: ...
    
    def EnterUpgradeableReadLock(self) -> VoidType: ...
    
    def EnterWriteLock(self) -> VoidType: ...
    
    def ExitReadLock(self) -> VoidType: ...
    
    def ExitUpgradeableReadLock(self) -> VoidType: ...
    
    def ExitWriteLock(self) -> VoidType: ...
    
    @overload
    def TryEnterReadLock(self, timeout: TimeSpan) -> BooleanType: ...
    
    @overload
    def TryEnterReadLock(self, millisecondsTimeout: IntType) -> BooleanType: ...
    
    @overload
    def TryEnterUpgradeableReadLock(self, timeout: TimeSpan) -> BooleanType: ...
    
    @overload
    def TryEnterUpgradeableReadLock(self, millisecondsTimeout: IntType) -> BooleanType: ...
    
    @overload
    def TryEnterWriteLock(self, timeout: TimeSpan) -> BooleanType: ...
    
    @overload
    def TryEnterWriteLock(self, millisecondsTimeout: IntType) -> BooleanType: ...
    
    def get_CurrentReadCount(self) -> IntType: ...
    
    def get_IsReadLockHeld(self) -> BooleanType: ...
    
    def get_IsUpgradeableReadLockHeld(self) -> BooleanType: ...
    
    def get_IsWriteLockHeld(self) -> BooleanType: ...
    
    def get_RecursionPolicy(self) -> LockRecursionPolicy: ...
    
    def get_RecursiveReadCount(self) -> IntType: ...
    
    def get_RecursiveUpgradeCount(self) -> IntType: ...
    
    def get_RecursiveWriteCount(self) -> IntType: ...
    
    def get_WaitingReadCount(self) -> IntType: ...
    
    def get_WaitingUpgradeCount(self) -> IntType: ...
    
    def get_WaitingWriteCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegisteredWaitHandle(MarshalByRefObject):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Unregister(self, waitObject: WaitHandle) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegisteredWaitHandleSafe(CriticalFinalizerObject):
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


class SafeCompressedStackHandle(SafeHandle, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsInvalid(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_IsInvalid(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Semaphore(WaitHandle, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, initialCount: IntType, maximumCount: IntType): ...
    
    @overload
    def __init__(self, initialCount: IntType, maximumCount: IntType, name: StringType): ...
    
    @overload
    def __init__(self, initialCount: IntType, maximumCount: IntType, name: StringType, createdNew: BooleanType): ...
    
    @overload
    def __init__(self, initialCount: IntType, maximumCount: IntType, name: StringType, createdNew: BooleanType, semaphoreSecurity: SemaphoreSecurity): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetAccessControl(self) -> SemaphoreSecurity: ...
    
    @staticmethod
    @overload
    def OpenExisting(name: StringType) -> Semaphore: ...
    
    @staticmethod
    @overload
    def OpenExisting(name: StringType, rights: SemaphoreRights) -> Semaphore: ...
    
    @overload
    def Release(self) -> IntType: ...
    
    @overload
    def Release(self, releaseCount: IntType) -> IntType: ...
    
    def SetAccessControl(self, semaphoreSecurity: SemaphoreSecurity) -> VoidType: ...
    
    @staticmethod
    @overload
    def TryOpenExisting(name: StringType, result: Semaphore) -> Tuple[BooleanType, Semaphore]: ...
    
    @staticmethod
    @overload
    def TryOpenExisting(name: StringType, rights: SemaphoreRights, result: Semaphore) -> Tuple[BooleanType, Semaphore]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SemaphoreFullException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SemaphoreSlim(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, initialCount: IntType): ...
    
    @overload
    def __init__(self, initialCount: IntType, maxCount: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AvailableWaitHandle(self) -> WaitHandle: ...
    
    @property
    def CurrentCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    @overload
    def Release(self) -> IntType: ...
    
    @overload
    def Release(self, releaseCount: IntType) -> IntType: ...
    
    @overload
    def Wait(self) -> VoidType: ...
    
    @overload
    def Wait(self, cancellationToken: CancellationToken) -> VoidType: ...
    
    @overload
    def Wait(self, timeout: TimeSpan) -> BooleanType: ...
    
    @overload
    def Wait(self, timeout: TimeSpan, cancellationToken: CancellationToken) -> BooleanType: ...
    
    @overload
    def Wait(self, millisecondsTimeout: IntType) -> BooleanType: ...
    
    @overload
    def Wait(self, millisecondsTimeout: IntType, cancellationToken: CancellationToken) -> BooleanType: ...
    
    @overload
    def WaitAsync(self) -> Task: ...
    
    @overload
    def WaitAsync(self, cancellationToken: CancellationToken) -> Task: ...
    
    @overload
    def WaitAsync(self, millisecondsTimeout: IntType) -> Task[BooleanType]: ...
    
    @overload
    def WaitAsync(self, timeout: TimeSpan) -> Task[BooleanType]: ...
    
    @overload
    def WaitAsync(self, timeout: TimeSpan, cancellationToken: CancellationToken) -> Task[BooleanType]: ...
    
    @overload
    def WaitAsync(self, millisecondsTimeout: IntType, cancellationToken: CancellationToken) -> Task[BooleanType]: ...
    
    def get_AvailableWaitHandle(self) -> WaitHandle: ...
    
    def get_CurrentCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SendOrPostCallback(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, state: ObjectType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, state: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SparselyPopulatedArray(Generic[T], ObjectType):
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


class SparselyPopulatedArrayFragment(Generic[T], ObjectType):
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


class SynchronizationContext(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Current() -> SynchronizationContext: ...
    
    # ---------- Methods ---------- #
    
    def CreateCopy(self) -> SynchronizationContext: ...
    
    def IsWaitNotificationRequired(self) -> BooleanType: ...
    
    def OperationCompleted(self) -> VoidType: ...
    
    def OperationStarted(self) -> VoidType: ...
    
    def Post(self, d: SendOrPostCallback, state: ObjectType) -> VoidType: ...
    
    def Send(self, d: SendOrPostCallback, state: ObjectType) -> VoidType: ...
    
    @staticmethod
    def SetSynchronizationContext(syncContext: SynchronizationContext) -> VoidType: ...
    
    def Wait(self, waitHandles: ArrayType[NIntType], waitAll: BooleanType, millisecondsTimeout: IntType) -> IntType: ...
    
    @staticmethod
    def get_Current() -> SynchronizationContext: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SynchronizationLockException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemThreading_ThreadLocalDebugView(Generic[T], ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, tlocal: ThreadLocal[T]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsValueCreated(self) -> BooleanType: ...
    
    @property
    def Value(self) -> T: ...
    
    @property
    def Values(self) -> List[T]: ...
    
    # ---------- Methods ---------- #
    
    def get_IsValueCreated(self) -> BooleanType: ...
    
    def get_Value(self) -> T: ...
    
    def get_Values(self) -> List[T]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Thread(CriticalFinalizerObject, _Thread):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, start: ThreadStart): ...
    
    @overload
    def __init__(self, start: ThreadStart, maxStackSize: IntType): ...
    
    @overload
    def __init__(self, start: ParameterizedThreadStart): ...
    
    @overload
    def __init__(self, start: ParameterizedThreadStart, maxStackSize: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ApartmentState(self) -> ApartmentState: ...
    
    @ApartmentState.setter
    def ApartmentState(self, value: ApartmentState) -> None: ...
    
    @staticmethod
    @property
    def CurrentContext() -> Context: ...
    
    @property
    def CurrentCulture(self) -> CultureInfo: ...
    
    @CurrentCulture.setter
    def CurrentCulture(self, value: CultureInfo) -> None: ...
    
    @staticmethod
    @property
    def CurrentPrincipal() -> IPrincipal: ...
    
    @staticmethod
    @CurrentPrincipal.setter
    def CurrentPrincipal(value: IPrincipal) -> None: ...
    
    @staticmethod
    @property
    def CurrentThread() -> Thread: ...
    
    @property
    def CurrentUICulture(self) -> CultureInfo: ...
    
    @CurrentUICulture.setter
    def CurrentUICulture(self, value: CultureInfo) -> None: ...
    
    @property
    def ExecutionContext(self) -> ExecutionContext: ...
    
    @property
    def IsAlive(self) -> BooleanType: ...
    
    @property
    def IsBackground(self) -> BooleanType: ...
    
    @IsBackground.setter
    def IsBackground(self, value: BooleanType) -> None: ...
    
    @property
    def IsThreadPoolThread(self) -> BooleanType: ...
    
    @property
    def ManagedThreadId(self) -> IntType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def Priority(self) -> ThreadPriority: ...
    
    @Priority.setter
    def Priority(self, value: ThreadPriority) -> None: ...
    
    @property
    def ThreadState(self) -> ThreadState: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Abort(self, stateInfo: ObjectType) -> VoidType: ...
    
    @overload
    def Abort(self) -> VoidType: ...
    
    @staticmethod
    def AllocateDataSlot() -> LocalDataStoreSlot: ...
    
    @staticmethod
    def AllocateNamedDataSlot(name: StringType) -> LocalDataStoreSlot: ...
    
    @staticmethod
    def BeginCriticalRegion() -> VoidType: ...
    
    @staticmethod
    def BeginThreadAffinity() -> VoidType: ...
    
    def DisableComObjectEagerCleanup(self) -> VoidType: ...
    
    @staticmethod
    def EndCriticalRegion() -> VoidType: ...
    
    @staticmethod
    def EndThreadAffinity() -> VoidType: ...
    
    @staticmethod
    def FreeNamedDataSlot(name: StringType) -> VoidType: ...
    
    def GetApartmentState(self) -> ApartmentState: ...
    
    def GetCompressedStack(self) -> CompressedStack: ...
    
    @staticmethod
    def GetData(slot: LocalDataStoreSlot) -> ObjectType: ...
    
    @staticmethod
    def GetDomain() -> AppDomain: ...
    
    @staticmethod
    def GetDomainID() -> IntType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    def GetNamedDataSlot(name: StringType) -> LocalDataStoreSlot: ...
    
    def Interrupt(self) -> VoidType: ...
    
    @overload
    def Join(self) -> VoidType: ...
    
    @overload
    def Join(self, millisecondsTimeout: IntType) -> BooleanType: ...
    
    @overload
    def Join(self, timeout: TimeSpan) -> BooleanType: ...
    
    @staticmethod
    def MemoryBarrier() -> VoidType: ...
    
    @staticmethod
    def ResetAbort() -> VoidType: ...
    
    def Resume(self) -> VoidType: ...
    
    def SetApartmentState(self, state: ApartmentState) -> VoidType: ...
    
    def SetCompressedStack(self, stack: CompressedStack) -> VoidType: ...
    
    @staticmethod
    def SetData(slot: LocalDataStoreSlot, data: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Sleep(millisecondsTimeout: IntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Sleep(timeout: TimeSpan) -> VoidType: ...
    
    @staticmethod
    def SpinWait(iterations: IntType) -> VoidType: ...
    
    @overload
    def Start(self) -> VoidType: ...
    
    @overload
    def Start(self, parameter: ObjectType) -> VoidType: ...
    
    def Suspend(self) -> VoidType: ...
    
    def TrySetApartmentState(self, state: ApartmentState) -> BooleanType: ...
    
    @staticmethod
    @overload
    def VolatileRead(address: ByteType) -> Tuple[ByteType, ByteType]: ...
    
    @staticmethod
    @overload
    def VolatileRead(address: ShortType) -> Tuple[ShortType, ShortType]: ...
    
    @staticmethod
    @overload
    def VolatileRead(address: IntType) -> Tuple[IntType, IntType]: ...
    
    @staticmethod
    @overload
    def VolatileRead(address: LongType) -> Tuple[LongType, LongType]: ...
    
    @staticmethod
    @overload
    def VolatileRead(address: SByteType) -> Tuple[SByteType, SByteType]: ...
    
    @staticmethod
    @overload
    def VolatileRead(address: UShortType) -> Tuple[UShortType, UShortType]: ...
    
    @staticmethod
    @overload
    def VolatileRead(address: UIntType) -> Tuple[UIntType, UIntType]: ...
    
    @staticmethod
    @overload
    def VolatileRead(address: NIntType) -> Tuple[NIntType, NIntType]: ...
    
    @staticmethod
    @overload
    def VolatileRead(address: NUIntType) -> Tuple[NUIntType, NUIntType]: ...
    
    @staticmethod
    @overload
    def VolatileRead(address: ULongType) -> Tuple[ULongType, ULongType]: ...
    
    @staticmethod
    @overload
    def VolatileRead(address: FloatType) -> Tuple[FloatType, FloatType]: ...
    
    @staticmethod
    @overload
    def VolatileRead(address: DoubleType) -> Tuple[DoubleType, DoubleType]: ...
    
    @staticmethod
    @overload
    def VolatileRead(address: ObjectType) -> Tuple[ObjectType, ObjectType]: ...
    
    @staticmethod
    @overload
    def VolatileWrite(address: ByteType, value: ByteType) -> Tuple[VoidType, ByteType]: ...
    
    @staticmethod
    @overload
    def VolatileWrite(address: ShortType, value: ShortType) -> Tuple[VoidType, ShortType]: ...
    
    @staticmethod
    @overload
    def VolatileWrite(address: IntType, value: IntType) -> Tuple[VoidType, IntType]: ...
    
    @staticmethod
    @overload
    def VolatileWrite(address: LongType, value: LongType) -> Tuple[VoidType, LongType]: ...
    
    @staticmethod
    @overload
    def VolatileWrite(address: SByteType, value: SByteType) -> Tuple[VoidType, SByteType]: ...
    
    @staticmethod
    @overload
    def VolatileWrite(address: UShortType, value: UShortType) -> Tuple[VoidType, UShortType]: ...
    
    @staticmethod
    @overload
    def VolatileWrite(address: UIntType, value: UIntType) -> Tuple[VoidType, UIntType]: ...
    
    @staticmethod
    @overload
    def VolatileWrite(address: NIntType, value: NIntType) -> Tuple[VoidType, NIntType]: ...
    
    @staticmethod
    @overload
    def VolatileWrite(address: NUIntType, value: NUIntType) -> Tuple[VoidType, NUIntType]: ...
    
    @staticmethod
    @overload
    def VolatileWrite(address: ULongType, value: ULongType) -> Tuple[VoidType, ULongType]: ...
    
    @staticmethod
    @overload
    def VolatileWrite(address: FloatType, value: FloatType) -> Tuple[VoidType, FloatType]: ...
    
    @staticmethod
    @overload
    def VolatileWrite(address: DoubleType, value: DoubleType) -> Tuple[VoidType, DoubleType]: ...
    
    @staticmethod
    @overload
    def VolatileWrite(address: ObjectType, value: ObjectType) -> Tuple[VoidType, ObjectType]: ...
    
    @staticmethod
    def Yield() -> BooleanType: ...
    
    def get_ApartmentState(self) -> ApartmentState: ...
    
    @staticmethod
    def get_CurrentContext() -> Context: ...
    
    def get_CurrentCulture(self) -> CultureInfo: ...
    
    @staticmethod
    def get_CurrentPrincipal() -> IPrincipal: ...
    
    @staticmethod
    def get_CurrentThread() -> Thread: ...
    
    def get_CurrentUICulture(self) -> CultureInfo: ...
    
    def get_ExecutionContext(self) -> ExecutionContext: ...
    
    def get_IsAlive(self) -> BooleanType: ...
    
    def get_IsBackground(self) -> BooleanType: ...
    
    def get_IsThreadPoolThread(self) -> BooleanType: ...
    
    def get_ManagedThreadId(self) -> IntType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Priority(self) -> ThreadPriority: ...
    
    def get_ThreadState(self) -> ThreadState: ...
    
    def set_ApartmentState(self, value: ApartmentState) -> VoidType: ...
    
    def set_CurrentCulture(self, value: CultureInfo) -> VoidType: ...
    
    @staticmethod
    def set_CurrentPrincipal(value: IPrincipal) -> VoidType: ...
    
    def set_CurrentUICulture(self, value: CultureInfo) -> VoidType: ...
    
    def set_IsBackground(self, value: BooleanType) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_Priority(self, value: ThreadPriority) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ThreadAbortException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ExceptionState(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_ExceptionState(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ThreadExceptionEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, t: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Exception(self) -> Exception: ...
    
    # ---------- Methods ---------- #
    
    def get_Exception(self) -> Exception: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ThreadExceptionEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: ThreadExceptionEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: ThreadExceptionEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ThreadHelper(ObjectType):
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


class ThreadInterruptedException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ThreadLocal(Generic[T], ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, trackAllValues: BooleanType): ...
    
    @overload
    def __init__(self, valueFactory: Func[T]): ...
    
    @overload
    def __init__(self, valueFactory: Func[T], trackAllValues: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsValueCreated(self) -> BooleanType: ...
    
    @property
    def Value(self) -> T: ...
    
    @Value.setter
    def Value(self, value: T) -> None: ...
    
    @property
    def Values(self) -> IList[T]: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_IsValueCreated(self) -> BooleanType: ...
    
    def get_Value(self) -> T: ...
    
    def get_Values(self) -> IList[T]: ...
    
    def set_Value(self, value: T) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ThreadPool(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def BindHandle(osHandle: NIntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def BindHandle(osHandle: SafeHandle) -> BooleanType: ...
    
    @staticmethod
    def GetAvailableThreads(workerThreads: IntType, completionPortThreads: IntType) -> Tuple[VoidType, IntType, IntType]: ...
    
    @staticmethod
    def GetMaxThreads(workerThreads: IntType, completionPortThreads: IntType) -> Tuple[VoidType, IntType, IntType]: ...
    
    @staticmethod
    def GetMinThreads(workerThreads: IntType, completionPortThreads: IntType) -> Tuple[VoidType, IntType, IntType]: ...
    
    @staticmethod
    @overload
    def QueueUserWorkItem(callBack: WaitCallback, state: ObjectType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def QueueUserWorkItem(callBack: WaitCallback) -> BooleanType: ...
    
    @staticmethod
    @overload
    def RegisterWaitForSingleObject(waitObject: WaitHandle, callBack: WaitOrTimerCallback, state: ObjectType, millisecondsTimeOutInterval: UIntType, executeOnlyOnce: BooleanType) -> RegisteredWaitHandle: ...
    
    @staticmethod
    @overload
    def RegisterWaitForSingleObject(waitObject: WaitHandle, callBack: WaitOrTimerCallback, state: ObjectType, millisecondsTimeOutInterval: IntType, executeOnlyOnce: BooleanType) -> RegisteredWaitHandle: ...
    
    @staticmethod
    @overload
    def RegisterWaitForSingleObject(waitObject: WaitHandle, callBack: WaitOrTimerCallback, state: ObjectType, millisecondsTimeOutInterval: LongType, executeOnlyOnce: BooleanType) -> RegisteredWaitHandle: ...
    
    @staticmethod
    @overload
    def RegisterWaitForSingleObject(waitObject: WaitHandle, callBack: WaitOrTimerCallback, state: ObjectType, timeout: TimeSpan, executeOnlyOnce: BooleanType) -> RegisteredWaitHandle: ...
    
    @staticmethod
    def SetMaxThreads(workerThreads: IntType, completionPortThreads: IntType) -> BooleanType: ...
    
    @staticmethod
    def SetMinThreads(workerThreads: IntType, completionPortThreads: IntType) -> BooleanType: ...
    
    @staticmethod
    def UnsafeQueueNativeOverlapped(overlapped: NativeOverlapped) -> BooleanType: ...
    
    @staticmethod
    def UnsafeQueueUserWorkItem(callBack: WaitCallback, state: ObjectType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def UnsafeRegisterWaitForSingleObject(waitObject: WaitHandle, callBack: WaitOrTimerCallback, state: ObjectType, millisecondsTimeOutInterval: UIntType, executeOnlyOnce: BooleanType) -> RegisteredWaitHandle: ...
    
    @staticmethod
    @overload
    def UnsafeRegisterWaitForSingleObject(waitObject: WaitHandle, callBack: WaitOrTimerCallback, state: ObjectType, millisecondsTimeOutInterval: IntType, executeOnlyOnce: BooleanType) -> RegisteredWaitHandle: ...
    
    @staticmethod
    @overload
    def UnsafeRegisterWaitForSingleObject(waitObject: WaitHandle, callBack: WaitOrTimerCallback, state: ObjectType, millisecondsTimeOutInterval: LongType, executeOnlyOnce: BooleanType) -> RegisteredWaitHandle: ...
    
    @staticmethod
    @overload
    def UnsafeRegisterWaitForSingleObject(waitObject: WaitHandle, callBack: WaitOrTimerCallback, state: ObjectType, timeout: TimeSpan, executeOnlyOnce: BooleanType) -> RegisteredWaitHandle: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ThreadPoolBoundHandle(ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Handle(self) -> SafeHandle: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AllocateNativeOverlapped(self, callback: IOCompletionCallback, state: ObjectType, pinData: ObjectType) -> NativeOverlapped: ...
    
    @overload
    def AllocateNativeOverlapped(self, preAllocated: PreAllocatedOverlapped) -> NativeOverlapped: ...
    
    @staticmethod
    def BindHandle(handle: SafeHandle) -> ThreadPoolBoundHandle: ...
    
    def Dispose(self) -> VoidType: ...
    
    def FreeNativeOverlapped(self, overlapped: NativeOverlapped) -> VoidType: ...
    
    @staticmethod
    def GetNativeOverlappedState(overlapped: NativeOverlapped) -> ObjectType: ...
    
    def get_Handle(self) -> SafeHandle: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ThreadPoolBoundHandleOverlapped(Overlapped):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, callback: IOCompletionCallback, state: ObjectType, pinData: ObjectType, preAllocated: PreAllocatedOverlapped): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ThreadPoolGlobals(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def enableWorkerTracking() -> BooleanType: ...
    
    @staticmethod
    @enableWorkerTracking.setter
    def enableWorkerTracking(value: BooleanType) -> None: ...
    
    @staticmethod
    @property
    def processorCount() -> IntType: ...
    
    @staticmethod
    @processorCount.setter
    def processorCount(value: IntType) -> None: ...
    
    @staticmethod
    @property
    def tpHosted() -> BooleanType: ...
    
    @staticmethod
    @tpHosted.setter
    def tpHosted(value: BooleanType) -> None: ...
    
    @staticmethod
    @property
    def tpQuantum() -> UIntType: ...
    
    @staticmethod
    @tpQuantum.setter
    def tpQuantum(value: UIntType) -> None: ...
    
    @staticmethod
    @property
    def vmTpInitialized() -> BooleanType: ...
    
    @staticmethod
    @vmTpInitialized.setter
    def vmTpInitialized(value: BooleanType) -> None: ...
    
    @staticmethod
    @property
    def workQueue() -> ThreadPoolWorkQueue: ...
    
    @staticmethod
    @workQueue.setter
    def workQueue(value: ThreadPoolWorkQueue) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ThreadPoolWorkQueue(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dequeue(self, tl: ThreadPoolWorkQueueThreadLocals, callback: IThreadPoolWorkItem, missedSteal: BooleanType) -> Tuple[VoidType, IThreadPoolWorkItem, BooleanType]: ...
    
    def Enqueue(self, callback: IThreadPoolWorkItem, forceGlobal: BooleanType) -> VoidType: ...
    
    def EnsureCurrentThreadHasQueue(self) -> ThreadPoolWorkQueueThreadLocals: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ThreadPoolWorkQueueThreadLocals(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def random(self) -> Random: ...
    
    @staticmethod
    @property
    def threadLocals() -> ThreadPoolWorkQueueThreadLocals: ...
    
    @staticmethod
    @threadLocals.setter
    def threadLocals(value: ThreadPoolWorkQueueThreadLocals) -> None: ...
    
    @property
    def workQueue(self) -> ThreadPoolWorkQueue: ...
    
    @property
    def workStealingQueue(self) -> WorkStealingQueue: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, tpq: ThreadPoolWorkQueue): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ThreadStart(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ThreadStartException(SystemException, ISerializable, _Exception):
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


class ThreadStateException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Timeout(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Infinite() -> IntType: ...
    
    @staticmethod
    @property
    def InfiniteTimeSpan() -> TimeSpan: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TimeoutHelper(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetTime() -> UIntType: ...
    
    @staticmethod
    def UpdateTimeOut(startTime: UIntType, originalWaitMillisecondsTimeout: IntType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Timer(MarshalByRefObject, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, callback: TimerCallback, state: ObjectType, dueTime: IntType, period: IntType): ...
    
    @overload
    def __init__(self, callback: TimerCallback, state: ObjectType, dueTime: TimeSpan, period: TimeSpan): ...
    
    @overload
    def __init__(self, callback: TimerCallback, state: ObjectType, dueTime: UIntType, period: UIntType): ...
    
    @overload
    def __init__(self, callback: TimerCallback, state: ObjectType, dueTime: LongType, period: LongType): ...
    
    @overload
    def __init__(self, callback: TimerCallback): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Change(self, dueTime: IntType, period: IntType) -> BooleanType: ...
    
    @overload
    def Change(self, dueTime: TimeSpan, period: TimeSpan) -> BooleanType: ...
    
    @overload
    def Change(self, dueTime: UIntType, period: UIntType) -> BooleanType: ...
    
    @overload
    def Change(self, dueTime: LongType, period: LongType) -> BooleanType: ...
    
    @overload
    def Dispose(self) -> VoidType: ...
    
    @overload
    def Dispose(self, notifyObject: WaitHandle) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TimerCallback(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, state: ObjectType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, state: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TimerHolder(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, timer: ObjectType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Change(self, dueTime: UIntType, period: UIntType) -> BooleanType: ...
    
    @overload
    def Close(self) -> VoidType: ...
    
    @overload
    def Close(self, notifyObject: WaitHandle) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TimerQueue(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Instance() -> TimerQueue: ...
    
    # ---------- Methods ---------- #
    
    def DeleteTimer(self, timer: TimerQueueTimer) -> VoidType: ...
    
    def UpdateTimer(self, timer: TimerQueueTimer, dueTime: UIntType, period: UIntType) -> BooleanType: ...
    
    @staticmethod
    def get_Instance() -> TimerQueue: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TimerQueueTimer(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Close(self) -> VoidType: ...
    
    @overload
    def Close(self, toSignal: WaitHandle) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Volatile(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Read(location: LongType) -> Tuple[LongType, LongType]: ...
    
    @staticmethod
    @overload
    def Read(location: T) -> Tuple[T, T]: ...
    
    @staticmethod
    @overload
    def Read(location: BooleanType) -> Tuple[BooleanType, BooleanType]: ...
    
    @staticmethod
    @overload
    def Read(location: SByteType) -> Tuple[SByteType, SByteType]: ...
    
    @staticmethod
    @overload
    def Read(location: ByteType) -> Tuple[ByteType, ByteType]: ...
    
    @staticmethod
    @overload
    def Read(location: ShortType) -> Tuple[ShortType, ShortType]: ...
    
    @staticmethod
    @overload
    def Read(location: UShortType) -> Tuple[UShortType, UShortType]: ...
    
    @staticmethod
    @overload
    def Read(location: IntType) -> Tuple[IntType, IntType]: ...
    
    @staticmethod
    @overload
    def Read(location: UIntType) -> Tuple[UIntType, UIntType]: ...
    
    @staticmethod
    @overload
    def Read(location: ULongType) -> Tuple[ULongType, ULongType]: ...
    
    @staticmethod
    @overload
    def Read(location: NIntType) -> Tuple[NIntType, NIntType]: ...
    
    @staticmethod
    @overload
    def Read(location: NUIntType) -> Tuple[NUIntType, NUIntType]: ...
    
    @staticmethod
    @overload
    def Read(location: FloatType) -> Tuple[FloatType, FloatType]: ...
    
    @staticmethod
    @overload
    def Read(location: DoubleType) -> Tuple[DoubleType, DoubleType]: ...
    
    @staticmethod
    @overload
    def Write(location: LongType, value: LongType) -> Tuple[VoidType, LongType]: ...
    
    @staticmethod
    @overload
    def Write(location: T, value: T) -> Tuple[VoidType, T]: ...
    
    @staticmethod
    @overload
    def Write(location: BooleanType, value: BooleanType) -> Tuple[VoidType, BooleanType]: ...
    
    @staticmethod
    @overload
    def Write(location: SByteType, value: SByteType) -> Tuple[VoidType, SByteType]: ...
    
    @staticmethod
    @overload
    def Write(location: ByteType, value: ByteType) -> Tuple[VoidType, ByteType]: ...
    
    @staticmethod
    @overload
    def Write(location: ShortType, value: ShortType) -> Tuple[VoidType, ShortType]: ...
    
    @staticmethod
    @overload
    def Write(location: UShortType, value: UShortType) -> Tuple[VoidType, UShortType]: ...
    
    @staticmethod
    @overload
    def Write(location: IntType, value: IntType) -> Tuple[VoidType, IntType]: ...
    
    @staticmethod
    @overload
    def Write(location: UIntType, value: UIntType) -> Tuple[VoidType, UIntType]: ...
    
    @staticmethod
    @overload
    def Write(location: ULongType, value: ULongType) -> Tuple[VoidType, ULongType]: ...
    
    @staticmethod
    @overload
    def Write(location: NIntType, value: NIntType) -> Tuple[VoidType, NIntType]: ...
    
    @staticmethod
    @overload
    def Write(location: NUIntType, value: NUIntType) -> Tuple[VoidType, NUIntType]: ...
    
    @staticmethod
    @overload
    def Write(location: FloatType, value: FloatType) -> Tuple[VoidType, FloatType]: ...
    
    @staticmethod
    @overload
    def Write(location: DoubleType, value: DoubleType) -> Tuple[VoidType, DoubleType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WaitCallback(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, state: ObjectType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, state: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WaitHandle(ABC, MarshalByRefObject, IDisposable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def WaitTimeout() -> IntType: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Handle(self) -> NIntType: ...
    
    @Handle.setter
    def Handle(self, value: NIntType) -> None: ...
    
    @property
    def SafeWaitHandle(self) -> SafeWaitHandle: ...
    
    @SafeWaitHandle.setter
    def SafeWaitHandle(self, value: SafeWaitHandle) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    @staticmethod
    @overload
    def SignalAndWait(toSignal: WaitHandle, toWaitOn: WaitHandle) -> BooleanType: ...
    
    @staticmethod
    @overload
    def SignalAndWait(toSignal: WaitHandle, toWaitOn: WaitHandle, timeout: TimeSpan, exitContext: BooleanType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def SignalAndWait(toSignal: WaitHandle, toWaitOn: WaitHandle, millisecondsTimeout: IntType, exitContext: BooleanType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def WaitAll(waitHandles: ArrayType[WaitHandle], millisecondsTimeout: IntType, exitContext: BooleanType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def WaitAll(waitHandles: ArrayType[WaitHandle], timeout: TimeSpan, exitContext: BooleanType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def WaitAll(waitHandles: ArrayType[WaitHandle]) -> BooleanType: ...
    
    @staticmethod
    @overload
    def WaitAll(waitHandles: ArrayType[WaitHandle], millisecondsTimeout: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def WaitAll(waitHandles: ArrayType[WaitHandle], timeout: TimeSpan) -> BooleanType: ...
    
    @staticmethod
    @overload
    def WaitAny(waitHandles: ArrayType[WaitHandle], millisecondsTimeout: IntType, exitContext: BooleanType) -> IntType: ...
    
    @staticmethod
    @overload
    def WaitAny(waitHandles: ArrayType[WaitHandle], timeout: TimeSpan, exitContext: BooleanType) -> IntType: ...
    
    @staticmethod
    @overload
    def WaitAny(waitHandles: ArrayType[WaitHandle], timeout: TimeSpan) -> IntType: ...
    
    @staticmethod
    @overload
    def WaitAny(waitHandles: ArrayType[WaitHandle]) -> IntType: ...
    
    @staticmethod
    @overload
    def WaitAny(waitHandles: ArrayType[WaitHandle], millisecondsTimeout: IntType) -> IntType: ...
    
    @overload
    def WaitOne(self, millisecondsTimeout: IntType, exitContext: BooleanType) -> BooleanType: ...
    
    @overload
    def WaitOne(self, timeout: TimeSpan, exitContext: BooleanType) -> BooleanType: ...
    
    @overload
    def WaitOne(self) -> BooleanType: ...
    
    @overload
    def WaitOne(self, millisecondsTimeout: IntType) -> BooleanType: ...
    
    @overload
    def WaitOne(self, timeout: TimeSpan) -> BooleanType: ...
    
    def get_Handle(self) -> NIntType: ...
    
    def get_SafeWaitHandle(self) -> SafeWaitHandle: ...
    
    def set_Handle(self, value: NIntType) -> VoidType: ...
    
    def set_SafeWaitHandle(self, value: SafeWaitHandle) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WaitHandleCannotBeOpenedException(ApplicationException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WaitHandleExtensions(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetSafeWaitHandle(waitHandle: WaitHandle) -> SafeWaitHandle: ...
    
    @staticmethod
    def SetSafeWaitHandle(waitHandle: WaitHandle, value: SafeWaitHandle) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WaitOrTimerCallback(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, state: ObjectType, timedOut: BooleanType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, state: ObjectType, timedOut: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WinRTSynchronizationContextFactoryBase(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Create(self, coreDispatcher: ObjectType) -> SynchronizationContext: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class _IOCompletionCallback(ObjectType):
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


class _ThreadPoolWaitCallback(ABC, ObjectType):
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


class _ThreadPoolWaitOrTimerCallback(ObjectType):
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


# ---------- Structs ---------- #

class AsyncFlowControl(ValueType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: AsyncFlowControl) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def Undo(self) -> VoidType: ...
    
    @staticmethod
    def op_Equality(a: AsyncFlowControl, b: AsyncFlowControl) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(a: AsyncFlowControl, b: AsyncFlowControl) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsyncLocalValueChangedArgs(Generic[T], ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CurrentValue(self) -> T: ...
    
    @property
    def PreviousValue(self) -> T: ...
    
    @property
    def ThreadContextChanged(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_CurrentValue(self) -> T: ...
    
    def get_PreviousValue(self) -> T: ...
    
    def get_ThreadContextChanged(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CancellationCallbackCoreWorkArguments(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, currArrayFragment: SparselyPopulatedArrayFragment[CancellationCallbackInfo], currArrayIndex: IntType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CancellationToken(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, canceled: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CanBeCanceled(self) -> BooleanType: ...
    
    @property
    def IsCancellationRequested(self) -> BooleanType: ...
    
    @property
    def WaitHandle(self) -> WaitHandle: ...
    
    @staticmethod
    @property
    def _None() -> CancellationToken: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, other: CancellationToken) -> BooleanType: ...
    
    @overload
    def Equals(self, other: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @overload
    def Register(self, callback: Action) -> CancellationTokenRegistration: ...
    
    @overload
    def Register(self, callback: Action, useSynchronizationContext: BooleanType) -> CancellationTokenRegistration: ...
    
    @overload
    def Register(self, callback: Action[ObjectType], state: ObjectType) -> CancellationTokenRegistration: ...
    
    @overload
    def Register(self, callback: Action[ObjectType], state: ObjectType, useSynchronizationContext: BooleanType) -> CancellationTokenRegistration: ...
    
    def ThrowIfCancellationRequested(self) -> VoidType: ...
    
    def get_CanBeCanceled(self) -> BooleanType: ...
    
    def get_IsCancellationRequested(self) -> BooleanType: ...
    
    @staticmethod
    def get_None() -> CancellationToken: ...
    
    def get_WaitHandle(self) -> WaitHandle: ...
    
    @staticmethod
    def op_Equality(left: CancellationToken, right: CancellationToken) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: CancellationToken, right: CancellationToken) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CancellationTokenRegistration(ValueType, IEquatable[CancellationTokenRegistration], IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: CancellationTokenRegistration) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    def op_Equality(left: CancellationTokenRegistration, right: CancellationTokenRegistration) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: CancellationTokenRegistration, right: CancellationTokenRegistration) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CompressedStackSwitcher(ValueType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def Undo(self) -> VoidType: ...
    
    @staticmethod
    def op_Equality(c1: CompressedStackSwitcher, c2: CompressedStackSwitcher) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(c1: CompressedStackSwitcher, c2: CompressedStackSwitcher) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DeferredDisposableLifetime(Generic[T], ValueType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AddRef(self, obj: T) -> BooleanType: ...
    
    def Dispose(self, obj: T) -> VoidType: ...
    
    def Release(self, obj: T) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExecutionContextSwitcher(ValueType):
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


class LockCookie(ValueType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: LockCookie) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    def op_Equality(a: LockCookie, b: LockCookie) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(a: LockCookie, b: LockCookie) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NativeOverlapped(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def EventHandle(self) -> NIntType: ...
    
    @EventHandle.setter
    def EventHandle(self, value: NIntType) -> None: ...
    
    @property
    def InternalHigh(self) -> NIntType: ...
    
    @InternalHigh.setter
    def InternalHigh(self, value: NIntType) -> None: ...
    
    @property
    def InternalLow(self) -> NIntType: ...
    
    @InternalLow.setter
    def InternalLow(self, value: NIntType) -> None: ...
    
    @property
    def OffsetHigh(self) -> IntType: ...
    
    @OffsetHigh.setter
    def OffsetHigh(self, value: IntType) -> None: ...
    
    @property
    def OffsetLow(self) -> IntType: ...
    
    @OffsetLow.setter
    def OffsetLow(self, value: IntType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SparselyPopulatedArrayAddInfo(Generic[T], ValueType):
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


class SpinLock(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, enableThreadOwnerTracking: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsHeld(self) -> BooleanType: ...
    
    @property
    def IsHeldByCurrentThread(self) -> BooleanType: ...
    
    @property
    def IsThreadOwnerTrackingEnabled(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Enter(self, lockTaken: BooleanType) -> Tuple[VoidType, BooleanType]: ...
    
    @overload
    def Exit(self) -> VoidType: ...
    
    @overload
    def Exit(self, useMemoryBarrier: BooleanType) -> VoidType: ...
    
    @overload
    def TryEnter(self, lockTaken: BooleanType) -> Tuple[VoidType, BooleanType]: ...
    
    @overload
    def TryEnter(self, timeout: TimeSpan, lockTaken: BooleanType) -> Tuple[VoidType, BooleanType]: ...
    
    @overload
    def TryEnter(self, millisecondsTimeout: IntType, lockTaken: BooleanType) -> Tuple[VoidType, BooleanType]: ...
    
    def get_IsHeld(self) -> BooleanType: ...
    
    def get_IsHeldByCurrentThread(self) -> BooleanType: ...
    
    def get_IsThreadOwnerTrackingEnabled(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SpinWait(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def NextSpinWillYield(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Reset(self) -> VoidType: ...
    
    def SpinOnce(self) -> VoidType: ...
    
    @staticmethod
    @overload
    def SpinUntil(condition: Func[BooleanType]) -> VoidType: ...
    
    @staticmethod
    @overload
    def SpinUntil(condition: Func[BooleanType], timeout: TimeSpan) -> BooleanType: ...
    
    @staticmethod
    @overload
    def SpinUntil(condition: Func[BooleanType], millisecondsTimeout: IntType) -> BooleanType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_NextSpinWillYield(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ThreadHandle(ValueType):
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

class IAsyncLocal(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def OnValueChanged(self, previousValue: ObjectType, currentValue: ObjectType, contextChanged: BooleanType) -> VoidType: ...
    
    # No Events


class IAsyncLocalValueMap(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Set(self, key: IAsyncLocal, value: ObjectType, treatNullValueAsNonexistent: BooleanType) -> IAsyncLocalValueMap: ...
    
    def TryGetValue(self, key: IAsyncLocal, value: ObjectType) -> Tuple[BooleanType, ObjectType]: ...
    
    # No Events


class IDeferredDisposable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def OnFinalRelease(self, disposed: BooleanType) -> VoidType: ...
    
    # No Events


class IThreadPoolWorkItem(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ExecuteWorkItem(self) -> VoidType: ...
    
    def MarkAborted(self, tae: ThreadAbortException) -> VoidType: ...
    
    # No Events


# ---------- Enums ---------- #

class ApartmentState(Enum):
    STA: IntType = 0
    MTA: IntType = 1
    Unknown: IntType = 2


class EventResetMode(Enum):
    AutoReset: IntType = 0
    ManualReset: IntType = 1


class LazyThreadSafetyMode(Enum):
    #None: IntType = 0
    PublicationOnly: IntType = 1
    ExecutionAndPublication: IntType = 2


class LockRecursionPolicy(Enum):
    NoRecursion: IntType = 0
    SupportsRecursion: IntType = 1


class StackCrawlMark(Enum):
    LookForMe: IntType = 0
    LookForMyCaller: IntType = 1
    LookForMyCallersCaller: IntType = 2
    LookForThread: IntType = 3


class SynchronizationContextProperties(Enum):
    #None: IntType = 0
    RequireWaitNotification: IntType = 1


class ThreadPriority(Enum):
    Lowest: IntType = 0
    BelowNormal: IntType = 1
    Normal: IntType = 2
    AboveNormal: IntType = 3
    Highest: IntType = 4


class ThreadState(Enum):
    Running: IntType = 0
    StopRequested: IntType = 1
    SuspendRequested: IntType = 2
    Background: IntType = 4
    Unstarted: IntType = 8
    Stopped: IntType = 16
    WaitSleepJoin: IntType = 32
    Suspended: IntType = 64
    AbortRequested: IntType = 128
    Aborted: IntType = 256


# ---------- Delegates ---------- #

ContextCallback = Callable[[ObjectType], VoidType]

IOCompletionCallback = Callable[[UIntType, UIntType, NativeOverlapped], VoidType]

InternalCrossContextDelegate = Callable[[ArrayType[ObjectType]], ObjectType]

ParameterizedThreadStart = Callable[[ObjectType], VoidType]

SendOrPostCallback = Callable[[ObjectType], VoidType]

ThreadExceptionEventHandler = Callable[[ObjectType, ThreadExceptionEventArgs], VoidType]

ThreadStart = Callable[[], VoidType]

TimerCallback = Callable[[ObjectType], VoidType]

WaitCallback = Callable[[ObjectType], VoidType]

WaitOrTimerCallback = Callable[[ObjectType, BooleanType], VoidType]

__all__ = [
    AbandonedMutexException,
    AsyncLocal,
    AsyncLocalValueMap,
    AutoResetEvent,
    Barrier,
    BarrierPostPhaseException,
    CancellationCallbackInfo,
    CancellationTokenSource,
    CdsSyncEtwBCLProvider,
    CompressedStack,
    ContextCallback,
    CountdownEvent,
    DomainCompressedStack,
    EventWaitHandle,
    ExecutionContext,
    Gen2GcCallback,
    HostExecutionContext,
    HostExecutionContextManager,
    HostExecutionContextSwitcher,
    IOCompletionCallback,
    IUnknownSafeHandle,
    Interlocked,
    InternalCrossContextDelegate,
    LazyHelpers,
    LazyInitializer,
    LockRecursionException,
    ManualResetEvent,
    ManualResetEventSlim,
    Monitor,
    Mutex,
    Overlapped,
    OverlappedData,
    ParameterizedThreadStart,
    PinnableBufferCache,
    PinnableBufferCacheEventSource,
    PlatformHelper,
    PreAllocatedOverlapped,
    QueueUserWorkItemCallback,
    ReaderWriterCount,
    ReaderWriterLock,
    ReaderWriterLockSlim,
    RegisteredWaitHandle,
    RegisteredWaitHandleSafe,
    SafeCompressedStackHandle,
    Semaphore,
    SemaphoreFullException,
    SemaphoreSlim,
    SendOrPostCallback,
    SparselyPopulatedArray,
    SparselyPopulatedArrayFragment,
    SynchronizationContext,
    SynchronizationLockException,
    SystemThreading_ThreadLocalDebugView,
    Thread,
    ThreadAbortException,
    ThreadExceptionEventArgs,
    ThreadExceptionEventHandler,
    ThreadHelper,
    ThreadInterruptedException,
    ThreadLocal,
    ThreadPool,
    ThreadPoolBoundHandle,
    ThreadPoolBoundHandleOverlapped,
    ThreadPoolGlobals,
    ThreadPoolWorkQueue,
    ThreadPoolWorkQueueThreadLocals,
    ThreadStart,
    ThreadStartException,
    ThreadStateException,
    Timeout,
    TimeoutHelper,
    Timer,
    TimerCallback,
    TimerHolder,
    TimerQueue,
    TimerQueueTimer,
    Volatile,
    WaitCallback,
    WaitHandle,
    WaitHandleCannotBeOpenedException,
    WaitHandleExtensions,
    WaitOrTimerCallback,
    WinRTSynchronizationContextFactoryBase,
    _IOCompletionCallback,
    _ThreadPoolWaitCallback,
    _ThreadPoolWaitOrTimerCallback,
    AsyncFlowControl,
    AsyncLocalValueChangedArgs,
    CancellationCallbackCoreWorkArguments,
    CancellationToken,
    CancellationTokenRegistration,
    CompressedStackSwitcher,
    DeferredDisposableLifetime,
    ExecutionContextSwitcher,
    LockCookie,
    NativeOverlapped,
    SparselyPopulatedArrayAddInfo,
    SpinLock,
    SpinWait,
    ThreadHandle,
    IAsyncLocal,
    IAsyncLocalValueMap,
    IDeferredDisposable,
    IThreadPoolWorkItem,
    ApartmentState,
    EventResetMode,
    LazyThreadSafetyMode,
    LockRecursionPolicy,
    StackCrawlMark,
    SynchronizationContextProperties,
    ThreadPriority,
    ThreadState,
    ContextCallback,
    IOCompletionCallback,
    InternalCrossContextDelegate,
    ParameterizedThreadStart,
    SendOrPostCallback,
    ThreadExceptionEventHandler,
    ThreadStart,
    TimerCallback,
    WaitCallback,
    WaitOrTimerCallback,
]
