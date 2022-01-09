from __future__ import annotations

from typing import Callable, Tuple, Union, overload

from System import Action, AsyncCallback, Boolean, EventArgs, Exception, IAsyncResult, ICloneable, IDisposable, Int32, Int64, IntPtr, MulticastDelegate, Object, String, TimeSpan, Void
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable
from System.Security.AccessControl import SemaphoreRights, SemaphoreSecurity
from System.Threading import CancellationToken, WaitHandle

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

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


# No Structs

# No Interfaces

# No Enums

# ---------- Delegates ---------- #

ThreadExceptionEventHandler = Callable[[ObjectType, ThreadExceptionEventArgs], VoidType]

__all__ = [
    Barrier,
    BarrierPostPhaseException,
    Semaphore,
    ThreadExceptionEventArgs,
    ThreadExceptionEventHandler,
    ThreadExceptionEventHandler,
]
