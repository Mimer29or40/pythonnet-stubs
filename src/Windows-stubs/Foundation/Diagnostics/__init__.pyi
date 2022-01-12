from __future__ import annotations

from typing import Protocol, Union

from System import Boolean, Enum, EventHandler, Guid, Int32, String, UInt64, Void
from System.Runtime.InteropServices.WindowsRuntime import EventRegistrationToken, RuntimeClass

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
StringType = Union[str, String]
ULongType = Union[int, UInt64]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class TracingStatusChangedEventArgs(RuntimeClass, ITracingStatusChangedEventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Enabled(self) -> BooleanType: ...
    
    @property
    def TraceLevel(self) -> CausalityTraceLevel: ...
    
    # ---------- Methods ---------- #
    
    def get_Enabled(self) -> BooleanType: ...
    
    def get_TraceLevel(self) -> CausalityTraceLevel: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# ---------- Interfaces ---------- #

class IAsyncCausalityTracerStatics(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def TraceOperationCompletion(self, traceLevel: CausalityTraceLevel, source: CausalitySource, platformId: Guid, operationId: ULongType, status: AsyncCausalityStatus) -> VoidType: ...
    
    def TraceOperationCreation(self, traceLevel: CausalityTraceLevel, source: CausalitySource, platformId: Guid, operationId: ULongType, operationName: StringType, relatedContext: ULongType) -> VoidType: ...
    
    def TraceOperationRelation(self, traceLevel: CausalityTraceLevel, source: CausalitySource, platformId: Guid, operationId: ULongType, relation: CausalityRelation) -> VoidType: ...
    
    def TraceSynchronousWorkCompletion(self, traceLevel: CausalityTraceLevel, source: CausalitySource, work: CausalitySynchronousWork) -> VoidType: ...
    
    def TraceSynchronousWorkStart(self, traceLevel: CausalityTraceLevel, source: CausalitySource, platformId: Guid, operationId: ULongType, work: CausalitySynchronousWork) -> VoidType: ...
    
    def add_TracingStatusChanged(self, eventHandler: EventHandler[TracingStatusChangedEventArgs]) -> EventRegistrationToken: ...
    
    def remove_TracingStatusChanged(self, token: EventRegistrationToken) -> VoidType: ...
    
    # No Events


class ITracingStatusChangedEventArgs(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Enabled(self) -> BooleanType: ...
    
    @property
    def TraceLevel(self) -> CausalityTraceLevel: ...
    
    # ---------- Methods ---------- #
    
    def get_Enabled(self) -> BooleanType: ...
    
    def get_TraceLevel(self) -> CausalityTraceLevel: ...
    
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


class CausalitySource(Enum):
    Application = 0
    Library = 1
    System = 2


class CausalitySynchronousWork(Enum):
    CompletionNotification = 0
    ProgressNotification = 1
    Execution = 2


class CausalityTraceLevel(Enum):
    Required = 0
    Important = 1
    Verbose = 2


# No Delegates

__all__ = [
    TracingStatusChangedEventArgs,
    IAsyncCausalityTracerStatics,
    ITracingStatusChangedEventArgs,
    AsyncCausalityStatus,
    CausalityRelation,
    CausalitySource,
    CausalitySynchronousWork,
    CausalityTraceLevel,
]
