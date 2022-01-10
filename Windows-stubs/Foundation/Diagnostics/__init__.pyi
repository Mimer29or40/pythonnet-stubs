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
    Started: IntType = 0
    Completed: IntType = 1
    Canceled: IntType = 2
    Error: IntType = 3


class AsyncCausalityStatus(Enum):
    Started: IntType = 0
    Completed: IntType = 1
    Canceled: IntType = 2
    Error: IntType = 3


class AsyncCausalityStatus(Enum):
    Started: IntType = 0
    Completed: IntType = 1
    Canceled: IntType = 2
    Error: IntType = 3


class CausalityRelation(Enum):
    AssignDelegate: IntType = 0
    Join: IntType = 1
    Choice: IntType = 2
    Cancel: IntType = 3
    Error: IntType = 4


class CausalityRelation(Enum):
    AssignDelegate: IntType = 0
    Join: IntType = 1
    Choice: IntType = 2
    Cancel: IntType = 3
    Error: IntType = 4


class CausalityRelation(Enum):
    AssignDelegate: IntType = 0
    Join: IntType = 1
    Choice: IntType = 2
    Cancel: IntType = 3
    Error: IntType = 4


class CausalitySource(Enum):
    Application: IntType = 0
    Library: IntType = 1
    System: IntType = 2


class CausalitySource(Enum):
    Application: IntType = 0
    Library: IntType = 1
    System: IntType = 2


class CausalitySource(Enum):
    Application: IntType = 0
    Library: IntType = 1
    System: IntType = 2


class CausalitySynchronousWork(Enum):
    CompletionNotification: IntType = 0
    ProgressNotification: IntType = 1
    Execution: IntType = 2


class CausalitySynchronousWork(Enum):
    CompletionNotification: IntType = 0
    ProgressNotification: IntType = 1
    Execution: IntType = 2


class CausalitySynchronousWork(Enum):
    CompletionNotification: IntType = 0
    ProgressNotification: IntType = 1
    Execution: IntType = 2


class CausalityTraceLevel(Enum):
    Required: IntType = 0
    Important: IntType = 1
    Verbose: IntType = 2


class CausalityTraceLevel(Enum):
    Required: IntType = 0
    Important: IntType = 1
    Verbose: IntType = 2


class CausalityTraceLevel(Enum):
    Required: IntType = 0
    Important: IntType = 1
    Verbose: IntType = 2


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
