"""Automatically generated stubs for C# namespace: System.Diagnostics.Eventing."""

from typing import overload

from System import Array
from System import Enum
from System import Guid
from System import IDisposable
from System import Object
from System import Type
from System import ValueType
from System.Collections.Specialized import StringDictionary
from System.Diagnostics import TraceEventCache
from System.Diagnostics import TraceEventType
from System.Diagnostics import TraceFilter
from System.Diagnostics import TraceListener
from System.Diagnostics import TraceOptions
from System.Runtime.Remoting import ObjRef

class EventDescriptor(ValueType):
    """"""
    def __init__(
        self, id: int, version: int, channel: int, level: int, opcode: int, task: int, keywords: int
    ) -> None:
        """"""
    @property
    def Channel(self) -> int:
        """"""
    @property
    def EventId(self) -> int:
        """"""
    @property
    def Keywords(self) -> int:
        """"""
    @property
    def Level(self) -> int:
        """"""
    @property
    def Opcode(self) -> int:
        """"""
    @property
    def Task(self) -> int:
        """"""
    @property
    def Version(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EventProvider(Object, IDisposable):
    """"""
    def __init__(self, providerGuid: Guid) -> None:
        """"""
    def Close(self) -> None:
        """"""
    @classmethod
    def CreateActivityId(cls) -> Guid:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetLastWriteEventError(cls) -> EventProvider.WriteEventErrorCode:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsEnabled(self) -> bool:
        """"""
    @overload
    def IsEnabled(self, level: int, keywords: int) -> bool:
        """"""
    @classmethod
    def SetActivityId(cls, id: Guid) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def WriteEvent(self, eventDescriptor: EventDescriptor, eventPayload: Array[object]) -> bool:
        """"""
    @overload
    def WriteEvent(self, eventDescriptor: EventDescriptor, data: str) -> bool:
        """"""
    @overload
    def WriteMessageEvent(self, eventMessage: str) -> bool:
        """"""
    @overload
    def WriteMessageEvent(self, eventMessage: str, eventLevel: int, eventKeywords: int) -> bool:
        """"""
    def WriteTransferEvent(
        self, eventDescriptor: EventDescriptor, relatedActivityId: Guid, eventPayload: Array[object]
    ) -> bool:
        """"""
    class WriteEventErrorCode(Enum):
        """"""

        NoError: EventProvider.WriteEventErrorCode = ...
        """"""
        NoFreeBuffers: EventProvider.WriteEventErrorCode = ...
        """"""
        EventTooBig: EventProvider.WriteEventErrorCode = ...
        """"""

class EventProviderTraceListener(TraceListener, IDisposable):
    """"""
    @overload
    def __init__(self, providerId: str) -> None:
        """"""
    @overload
    def __init__(self, providerId: str, name: str) -> None:
        """"""
    @overload
    def __init__(self, providerId: str, name: str, delimiter: str) -> None:
        """"""
    @property
    def Attributes(self) -> StringDictionary:
        """"""
    @property
    def Delimiter(self) -> str:
        """"""
    @Delimiter.setter
    def Delimiter(self, value: str) -> None: ...
    @property
    def Filter(self) -> TraceFilter:
        """"""
    @Filter.setter
    def Filter(self, value: TraceFilter) -> None: ...
    @property
    def IndentLevel(self) -> int:
        """"""
    @IndentLevel.setter
    def IndentLevel(self, value: int) -> None: ...
    @property
    def IndentSize(self) -> int:
        """"""
    @IndentSize.setter
    def IndentSize(self, value: int) -> None: ...
    @property
    def IsThreadSafe(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def TraceOutputOptions(self) -> TraceOptions:
        """"""
    @TraceOutputOptions.setter
    def TraceOutputOptions(self, value: TraceOptions) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Fail(self, message: str) -> None:
        """"""
    @overload
    def Fail(self, message: str, detailMessage: str) -> None:
        """"""
    def Flush(self) -> None:
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
    @overload
    def TraceData(
        self,
        eventCache: TraceEventCache,
        source: str,
        eventType: TraceEventType,
        id: int,
        data: Array[object],
    ) -> None:
        """"""
    @overload
    def TraceData(
        self,
        eventCache: TraceEventCache,
        source: str,
        eventType: TraceEventType,
        id: int,
        data: object,
    ) -> None:
        """"""
    @overload
    def TraceEvent(
        self, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int
    ) -> None:
        """"""
    @overload
    def TraceEvent(
        self,
        eventCache: TraceEventCache,
        source: str,
        eventType: TraceEventType,
        id: int,
        message: str,
    ) -> None:
        """"""
    @overload
    def TraceEvent(
        self,
        eventCache: TraceEventCache,
        source: str,
        eventType: TraceEventType,
        id: int,
        format: str,
        args: Array[object],
    ) -> None:
        """"""
    def TraceTransfer(
        self,
        eventCache: TraceEventCache,
        source: str,
        id: int,
        message: str,
        relatedActivityId: Guid,
    ) -> None:
        """"""
    @overload
    def Write(self, o: object) -> None:
        """"""
    @overload
    def Write(self, o: object, category: str) -> None:
        """"""
    @overload
    def Write(self, message: str) -> None:
        """"""
    @overload
    def Write(self, message: str, category: str) -> None:
        """"""
    @overload
    def WriteLine(self, o: object) -> None:
        """"""
    @overload
    def WriteLine(self, o: object, category: str) -> None:
        """"""
    @overload
    def WriteLine(self, message: str) -> None:
        """"""
    @overload
    def WriteLine(self, message: str, category: str) -> None:
        """"""
