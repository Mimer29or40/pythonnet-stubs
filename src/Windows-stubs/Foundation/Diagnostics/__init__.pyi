"""Automatically generated stubs for C# namespace: Windows.Foundation.Diagnostics."""

from System import Enum
from System import Guid
from System import Type
from System.Runtime.InteropServices.WindowsRuntime import RuntimeClass
from System.Runtime.Remoting import ObjRef

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

class CausalitySource(Enum):
    """"""

    Application: CausalitySource = ...
    """"""
    Library: CausalitySource = ...
    """"""
    System: CausalitySource = ...
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

class IAsyncCausalityTracerStatics:
    """"""
    def TraceOperationCompletion(
        self,
        traceLevel: CausalityTraceLevel,
        source: CausalitySource,
        platformId: Guid,
        operationId: int,
        status: AsyncCausalityStatus,
    ) -> None:
        """"""
    def TraceOperationCreation(
        self,
        traceLevel: CausalityTraceLevel,
        source: CausalitySource,
        platformId: Guid,
        operationId: int,
        operationName: str,
        relatedContext: int,
    ) -> None:
        """"""
    def TraceOperationRelation(
        self,
        traceLevel: CausalityTraceLevel,
        source: CausalitySource,
        platformId: Guid,
        operationId: int,
        relation: CausalityRelation,
    ) -> None:
        """"""
    def TraceSynchronousWorkCompletion(
        self,
        traceLevel: CausalityTraceLevel,
        source: CausalitySource,
        work: CausalitySynchronousWork,
    ) -> None:
        """"""
    def TraceSynchronousWorkStart(
        self,
        traceLevel: CausalityTraceLevel,
        source: CausalitySource,
        platformId: Guid,
        operationId: int,
        work: CausalitySynchronousWork,
    ) -> None:
        """"""

class ITracingStatusChangedEventArgs:
    """"""
    @property
    def Enabled(self) -> bool:
        """"""
    @property
    def TraceLevel(self) -> CausalityTraceLevel:
        """"""

class TracingStatusChangedEventArgs(RuntimeClass, ITracingStatusChangedEventArgs):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Enabled(self) -> bool:
        """"""
    @property
    def TraceLevel(self) -> CausalityTraceLevel:
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
