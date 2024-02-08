from __future__ import annotations

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
from System.Diagnostics.Eventing.EventProvider import WriteEventErrorCode
from System.Runtime.Remoting import ObjRef

class EventDescriptor(ValueType):
    """"""

    def __init__(
        self, id: int, version: int, channel: int, level: int, opcode: int, task: int, keywords: int
    ):
        """

        :param id:
        :param version:
        :param channel:
        :param level:
        :param opcode:
        :param task:
        :param keywords:
        """
    @property
    def Channel(self) -> int:
        """

        :return:
        """
    @property
    def EventId(self) -> int:
        """

        :return:
        """
    @property
    def Keywords(self) -> int:
        """

        :return:
        """
    @property
    def Level(self) -> int:
        """

        :return:
        """
    @property
    def Opcode(self) -> int:
        """

        :return:
        """
    @property
    def Task(self) -> int:
        """

        :return:
        """
    @property
    def Version(self) -> int:
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

class EventProvider(Object, IDisposable):
    """"""

    def __init__(self, providerGuid: Guid):
        """

        :param providerGuid:
        """
    def Close(self) -> None:
        """"""
    @classmethod
    def CreateActivityId(cls) -> Guid:
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
    @classmethod
    def GetLastWriteEventError(cls) -> EventProvider.WriteEventErrorCode:
        """

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
    def IsEnabled(self, level: int, keywords: int) -> bool:
        """

        :param level:
        :param keywords:
        :return:
        """
    @classmethod
    def SetActivityId(cls, id: Guid) -> None:
        """

        :param id:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def WriteEvent(self, eventDescriptor: EventDescriptor, eventPayload: Array[object]) -> bool:
        """

        :param eventDescriptor:
        :param eventPayload:
        :return:
        """
    @overload
    def WriteEvent(self, eventDescriptor: EventDescriptor, data: str) -> bool:
        """

        :param eventDescriptor:
        :param data:
        :return:
        """
    @overload
    def WriteMessageEvent(self, eventMessage: str) -> bool:
        """

        :param eventMessage:
        :return:
        """
    @overload
    def WriteMessageEvent(self, eventMessage: str, eventLevel: int, eventKeywords: int) -> bool:
        """

        :param eventMessage:
        :param eventLevel:
        :param eventKeywords:
        :return:
        """
    def WriteTransferEvent(
        self, eventDescriptor: EventDescriptor, relatedActivityId: Guid, eventPayload: Array[object]
    ) -> bool:
        """

        :param eventDescriptor:
        :param relatedActivityId:
        :param eventPayload:
        :return:
        """

    class WriteEventErrorCode(Enum):
        """"""

        NoError: WriteEventErrorCode = ...
        """"""
        NoFreeBuffers: WriteEventErrorCode = ...
        """"""
        EventTooBig: WriteEventErrorCode = ...
        """"""

class EventProviderTraceListener(TraceListener, IDisposable):
    """"""

    @overload
    def __init__(self, providerId: str):
        """

        :param providerId:
        """
    @overload
    def __init__(self, providerId: str, name: str):
        """

        :param providerId:
        :param name:
        """
    @overload
    def __init__(self, providerId: str, name: str, delimiter: str):
        """

        :param providerId:
        :param name:
        :param delimiter:
        """
    @property
    def Attributes(self) -> StringDictionary:
        """

        :return:
        """
    @property
    def Delimiter(self) -> str:
        """

        :return:
        """
    @Delimiter.setter
    def Delimiter(self, value: str) -> None: ...
    @property
    def Filter(self) -> TraceFilter:
        """

        :return:
        """
    @Filter.setter
    def Filter(self, value: TraceFilter) -> None: ...
    @property
    def IndentLevel(self) -> int:
        """

        :return:
        """
    @IndentLevel.setter
    def IndentLevel(self, value: int) -> None: ...
    @property
    def IndentSize(self) -> int:
        """

        :return:
        """
    @IndentSize.setter
    def IndentSize(self, value: int) -> None: ...
    @property
    def IsThreadSafe(self) -> bool:
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
    def TraceOutputOptions(self) -> TraceOptions:
        """

        :return:
        """
    @TraceOutputOptions.setter
    def TraceOutputOptions(self, value: TraceOptions) -> None: ...
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
    @overload
    def Fail(self, message: str) -> None:
        """

        :param message:
        """
    @overload
    def Fail(self, message: str, detailMessage: str) -> None:
        """

        :param message:
        :param detailMessage:
        """
    def Flush(self) -> None:
        """"""
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
    @overload
    def TraceData(
        self,
        eventCache: TraceEventCache,
        source: str,
        eventType: TraceEventType,
        id: int,
        data: Array[object],
    ) -> None:
        """

        :param eventCache:
        :param source:
        :param eventType:
        :param id:
        :param data:
        """
    @overload
    def TraceData(
        self,
        eventCache: TraceEventCache,
        source: str,
        eventType: TraceEventType,
        id: int,
        data: object,
    ) -> None:
        """

        :param eventCache:
        :param source:
        :param eventType:
        :param id:
        :param data:
        """
    @overload
    def TraceEvent(
        self, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int
    ) -> None:
        """

        :param eventCache:
        :param source:
        :param eventType:
        :param id:
        """
    @overload
    def TraceEvent(
        self,
        eventCache: TraceEventCache,
        source: str,
        eventType: TraceEventType,
        id: int,
        message: str,
    ) -> None:
        """

        :param eventCache:
        :param source:
        :param eventType:
        :param id:
        :param message:
        """
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
        """

        :param eventCache:
        :param source:
        :param eventType:
        :param id:
        :param format:
        :param args:
        """
    def TraceTransfer(
        self,
        eventCache: TraceEventCache,
        source: str,
        id: int,
        message: str,
        relatedActivityId: Guid,
    ) -> None:
        """

        :param eventCache:
        :param source:
        :param id:
        :param message:
        :param relatedActivityId:
        """
    @overload
    def Write(self, o: object) -> None:
        """

        :param o:
        """
    @overload
    def Write(self, message: str) -> None:
        """

        :param message:
        """
    @overload
    def Write(self, o: object, category: str) -> None:
        """

        :param o:
        :param category:
        """
    @overload
    def Write(self, message: str, category: str) -> None:
        """

        :param message:
        :param category:
        """
    @overload
    def WriteLine(self, o: object) -> None:
        """

        :param o:
        """
    @overload
    def WriteLine(self, message: str) -> None:
        """

        :param message:
        """
    @overload
    def WriteLine(self, o: object, category: str) -> None:
        """

        :param o:
        :param category:
        """
    @overload
    def WriteLine(self, message: str, category: str) -> None:
        """

        :param message:
        :param category:
        """
