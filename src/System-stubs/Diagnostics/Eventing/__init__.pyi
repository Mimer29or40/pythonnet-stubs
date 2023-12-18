from __future__ import annotations

from typing import List
from typing import Tuple
from typing import Union
from typing import overload

from System import Array
from System import Boolean
from System import Byte
from System import Enum
from System import Guid
from System import IDisposable
from System import Int32
from System import Int64
from System import Object
from System import String
from System import ValueType
from System import Void
from System.Diagnostics import TraceEventCache
from System.Diagnostics import TraceEventType
from System.Diagnostics import TraceListener

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class EventProvider(ObjectType, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, providerGuid: Guid): ...

    # No Properties

    # ---------- Methods ---------- #

    def Close(self) -> VoidType: ...
    @staticmethod
    def CreateActivityId() -> Guid: ...
    def Dispose(self) -> VoidType: ...
    @staticmethod
    def GetLastWriteEventError() -> WriteEventErrorCode: ...
    @overload
    def IsEnabled(self) -> BooleanType: ...
    @overload
    def IsEnabled(self, level: ByteType, keywords: LongType) -> BooleanType: ...
    @staticmethod
    def SetActivityId(id: Guid) -> Tuple[VoidType, Guid]: ...
    @overload
    def WriteEvent(
        self, eventDescriptor: EventDescriptor, eventPayload: ArrayType[ObjectType]
    ) -> Tuple[BooleanType, EventDescriptor]: ...
    @overload
    def WriteEvent(
        self, eventDescriptor: EventDescriptor, data: StringType
    ) -> Tuple[BooleanType, EventDescriptor]: ...
    @overload
    def WriteMessageEvent(
        self, eventMessage: StringType, eventLevel: ByteType, eventKeywords: LongType
    ) -> BooleanType: ...
    @overload
    def WriteMessageEvent(self, eventMessage: StringType) -> BooleanType: ...
    def WriteTransferEvent(
        self,
        eventDescriptor: EventDescriptor,
        relatedActivityId: Guid,
        eventPayload: ArrayType[ObjectType],
    ) -> Tuple[BooleanType, EventDescriptor]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # ---------- Sub Enums ---------- #

    class WriteEventErrorCode(Enum):
        NoError = 0
        NoFreeBuffers = 1
        EventTooBig = 2

class EventProviderTraceListener(TraceListener, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, providerId: StringType): ...
    @overload
    def __init__(self, providerId: StringType, name: StringType): ...
    @overload
    def __init__(self, providerId: StringType, name: StringType, delimiter: StringType): ...

    # ---------- Properties ---------- #

    @property
    def Delimiter(self) -> StringType: ...
    @Delimiter.setter
    def Delimiter(self, value: StringType) -> None: ...
    @property
    def IsThreadSafe(self) -> BooleanType: ...

    # ---------- Methods ---------- #

    def Close(self) -> VoidType: ...
    @overload
    def Fail(self, message: StringType, detailMessage: StringType) -> VoidType: ...
    def Flush(self) -> VoidType: ...
    @overload
    def TraceData(
        self,
        eventCache: TraceEventCache,
        source: StringType,
        eventType: TraceEventType,
        id: IntType,
        data: ObjectType,
    ) -> VoidType: ...
    @overload
    def TraceData(
        self,
        eventCache: TraceEventCache,
        source: StringType,
        eventType: TraceEventType,
        id: IntType,
        data: ArrayType[ObjectType],
    ) -> VoidType: ...
    @overload
    def TraceEvent(
        self,
        eventCache: TraceEventCache,
        source: StringType,
        eventType: TraceEventType,
        id: IntType,
    ) -> VoidType: ...
    @overload
    def TraceEvent(
        self,
        eventCache: TraceEventCache,
        source: StringType,
        eventType: TraceEventType,
        id: IntType,
        message: StringType,
    ) -> VoidType: ...
    @overload
    def TraceEvent(
        self,
        eventCache: TraceEventCache,
        source: StringType,
        eventType: TraceEventType,
        id: IntType,
        format: StringType,
        args: ArrayType[ObjectType],
    ) -> VoidType: ...
    def TraceTransfer(
        self,
        eventCache: TraceEventCache,
        source: StringType,
        id: IntType,
        message: StringType,
        relatedActivityId: Guid,
    ) -> VoidType: ...
    @overload
    def Write(self, message: StringType) -> VoidType: ...
    @overload
    def WriteLine(self, message: StringType) -> VoidType: ...
    def get_Delimiter(self) -> StringType: ...
    def get_IsThreadSafe(self) -> BooleanType: ...
    def set_Delimiter(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# ---------- Structs ---------- #

class EventDescriptor(ValueType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self,
        id: IntType,
        version: ByteType,
        channel: ByteType,
        level: ByteType,
        opcode: ByteType,
        task: IntType,
        keywords: LongType,
    ): ...

    # ---------- Properties ---------- #

    @property
    def Channel(self) -> ByteType: ...
    @property
    def EventId(self) -> IntType: ...
    @property
    def Keywords(self) -> LongType: ...
    @property
    def Level(self) -> ByteType: ...
    @property
    def Opcode(self) -> ByteType: ...
    @property
    def Task(self) -> IntType: ...
    @property
    def Version(self) -> ByteType: ...

    # ---------- Methods ---------- #

    def get_Channel(self) -> ByteType: ...
    def get_EventId(self) -> IntType: ...
    def get_Keywords(self) -> LongType: ...
    def get_Level(self) -> ByteType: ...
    def get_Opcode(self) -> ByteType: ...
    def get_Task(self) -> IntType: ...
    def get_Version(self) -> ByteType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# No Interfaces

# No Enums

# No Delegates

__all__ = [
    EventProvider,
    EventProviderTraceListener,
    EventDescriptor,
]
