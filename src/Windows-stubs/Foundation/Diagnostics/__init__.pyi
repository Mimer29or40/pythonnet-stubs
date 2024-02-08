from __future__ import annotations

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
        """

        :param traceLevel:
        :param source:
        :param platformId:
        :param operationId:
        :param status:
        """
    def TraceOperationCreation(
        self,
        traceLevel: CausalityTraceLevel,
        source: CausalitySource,
        platformId: Guid,
        operationId: int,
        operationName: str,
        relatedContext: int,
    ) -> None:
        """

        :param traceLevel:
        :param source:
        :param platformId:
        :param operationId:
        :param operationName:
        :param relatedContext:
        """
    def TraceOperationRelation(
        self,
        traceLevel: CausalityTraceLevel,
        source: CausalitySource,
        platformId: Guid,
        operationId: int,
        relation: CausalityRelation,
    ) -> None:
        """

        :param traceLevel:
        :param source:
        :param platformId:
        :param operationId:
        :param relation:
        """
    def TraceSynchronousWorkCompletion(
        self,
        traceLevel: CausalityTraceLevel,
        source: CausalitySource,
        work: CausalitySynchronousWork,
    ) -> None:
        """

        :param traceLevel:
        :param source:
        :param work:
        """
    def TraceSynchronousWorkStart(
        self,
        traceLevel: CausalityTraceLevel,
        source: CausalitySource,
        platformId: Guid,
        operationId: int,
        work: CausalitySynchronousWork,
    ) -> None:
        """

        :param traceLevel:
        :param source:
        :param platformId:
        :param operationId:
        :param work:
        """

class ITracingStatusChangedEventArgs:
    """"""

    @property
    def Enabled(self) -> bool:
        """

        :return:
        """
    @property
    def TraceLevel(self) -> CausalityTraceLevel:
        """

        :return:
        """

class TracingStatusChangedEventArgs(RuntimeClass, ITracingStatusChangedEventArgs):
    """"""

    def __init__(self):
        """"""
    @property
    def Enabled(self) -> bool:
        """

        :return:
        """
    @property
    def TraceLevel(self) -> CausalityTraceLevel:
        """

        :return:
        """
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
