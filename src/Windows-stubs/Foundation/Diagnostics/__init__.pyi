"""Automatically generated stubs for C# namespace: Windows.Foundation.Diagnostics."""

from abc import ABC

from System import Enum
from System import Guid
from System import Type
from System.Runtime.InteropServices.WindowsRuntime import RuntimeClass
from System.Runtime.Remoting import ObjRef

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CausalitySource(Enum):
    """"""

    Application: CausalitySource = ...
    """"""
    Library: CausalitySource = ...
    """"""
    System: CausalitySource = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CausalitySynchronousWork(Enum):
    """"""

    CompletionNotification: CausalitySynchronousWork = ...
    """"""
    ProgressNotification: CausalitySynchronousWork = ...
    """"""
    Execution: CausalitySynchronousWork = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CausalityTraceLevel(Enum):
    """"""

    Required: CausalityTraceLevel = ...
    """"""
    Important: CausalityTraceLevel = ...
    """"""
    Verbose: CausalityTraceLevel = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IAsyncCausalityTracerStatics(ABC):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ITracingStatusChangedEventArgs(ABC):
    """"""
    @property
    def Enabled(self) -> bool:
        """"""
    @property
    def TraceLevel(self) -> CausalityTraceLevel:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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
