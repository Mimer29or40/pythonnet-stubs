from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Iterator
from typing import Optional
from typing import Tuple
from typing import TypeVar
from typing import overload

from System import Array
from System import Attribute
from System import Boolean
from System import Byte
from System import Char
from System import DateTime
from System import DateTimeOffset
from System import Decimal
from System import Delegate
from System import Double
from System import Enum
from System import EventArgs
from System import EventHandler
from System import Exception
from System import Guid
from System import IDisposable
from System import Int16
from System import Int32
from System import Int64
from System import IntPtr
from System import Object
from System import SByte
from System import Single
from System import String
from System import TimeSpan
from System import Tuple
from System import Type
from System import UInt16
from System import UInt32
from System import UInt64
from System import UIntPtr
from System import ValueType
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections.Generic import ICollection
from System.Collections.Generic import IDictionary
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IList
from System.Collections.Generic import KeyValuePair
from System.Collections.Generic import List
from System.Collections.ObjectModel import ReadOnlyCollection
from System.Diagnostics.Tracing.EventProvider import WriteEventErrorCode
from System.Diagnostics.Tracing.ManifestEnvelope import ManifestFormats
from System.Reflection import Assembly
from System.Reflection import MethodBase
from System.Reflection import MethodInfo
from System.Reflection import PropertyInfo
from System.Resources import ResourceManager
from System.Runtime.InteropServices import _Attribute
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext

AttributeType = TypeVar("AttributeType")
ContainerType = TypeVar("ContainerType")
DataType = TypeVar("DataType")
ElementType = TypeVar("ElementType")
EnumType = TypeVar("EnumType")
ItemType = TypeVar("ItemType")
IterableType = TypeVar("IterableType")
K = TypeVar("K")
KeyType = TypeVar("KeyType")
T = TypeVar("T")
UnderlyingType = TypeVar("UnderlyingType")
V = TypeVar("V")
ValueType = TypeVar("ValueType")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class ActivityFilter(Object, IDisposable):
    """"""

    @classmethod
    def DisableFilter(cls, filterList: ActivityFilter, source: EventSource) -> None:
        """

        :param filterList:
        :param source:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def FlowActivityIfNeeded(
        cls, filterList: ActivityFilter, currentActivityId: Guid, childActivityID: Guid
    ) -> None:
        """

        :param filterList:
        :param currentActivityId:
        :param childActivityID:
        """
    @classmethod
    def GetFilter(cls, filterList: ActivityFilter, source: EventSource) -> ActivityFilter:
        """

        :param filterList:
        :param source:
        :return:
        """
    def GetFilterAsTuple(self, sourceGuid: Guid) -> IEnumerable[Tuple, int]:
        """

        :param sourceGuid:
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
    @classmethod
    def IsCurrentActivityActive(cls, filterList: ActivityFilter) -> bool:
        """

        :param filterList:
        :return:
        """
    @classmethod
    def PassesActivityFilter(
        cls,
        filterList: ActivityFilter,
        childActivityID: Guid,
        triggeringEvent: bool,
        source: EventSource,
        eventId: int,
    ) -> bool:
        """

        :param filterList:
        :param childActivityID:
        :param triggeringEvent:
        :param source:
        :param eventId:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def UpdateFilter(
        cls,
        filterList: ActivityFilter,
        source: EventSource,
        perEventSourceSessionId: int,
        startEvents: str,
    ) -> None:
        """

        :param filterList:
        :param source:
        :param perEventSourceSessionId:
        :param startEvents:
        """
    @classmethod
    def UpdateKwdTriggers(
        cls,
        activityFilter: ActivityFilter,
        sourceGuid: Guid,
        source: EventSource,
        sessKeywords: EventKeywords,
    ) -> None:
        """

        :param activityFilter:
        :param sourceGuid:
        :param source:
        :param sessKeywords:
        """

class ActivityTracker(Object):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> ActivityTracker:
        """

        :return:
        """
    def Enable(self) -> None:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def OnStart(
        self,
        providerName: str,
        activityName: str,
        task: int,
        activityId: Guid,
        relatedActivityId: Guid,
        options: EventActivityOptions,
    ) -> None:
        """

        :param providerName:
        :param activityName:
        :param task:
        :param activityId:
        :param relatedActivityId:
        :param options:
        """
    def OnStop(self, providerName: str, activityName: str, task: int, activityId: Guid) -> None:
        """

        :param providerName:
        :param activityName:
        :param task:
        :param activityId:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ArrayTypeInfo(Generic[ElementType], TraceLoggingTypeInfo[Array[ElementType]]):
    """"""

    def __init__(self, elementInfo: TraceLoggingTypeInfo[ElementType]):
        """

        :param elementInfo:
        """
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[Array[ElementType]]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: ElementType) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class BooleanArrayTypeInfo(TraceLoggingTypeInfo[Array[Boolean]]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[Array[bool]]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: bool) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class BooleanTypeInfo(TraceLoggingTypeInfo[Boolean]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[bool]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: bool) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class ByteArrayTypeInfo(TraceLoggingTypeInfo[Array[Byte]]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[Array[int]]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: int) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class ByteTypeInfo(TraceLoggingTypeInfo[Byte]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[int]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: int) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class CharArrayTypeInfo(TraceLoggingTypeInfo[Array[Char]]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[Array[Char]]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: Char) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class CharTypeInfo(TraceLoggingTypeInfo[Char]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[Char]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: Char) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class ClassPropertyWriter(Generic[ContainerType, ValueType], PropertyAccessor[ContainerType]):
    """"""

    def __init__(self, property: PropertyAnalysis):
        """

        :param property:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: ContainerType) -> object:
        """

        :param value:
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
    def Write(self, collector: TraceLoggingDataCollector, value: ContainerType) -> None:
        """

        :param collector:
        :param value:
        """

class ConcurrentSet(Generic[KeyType, ItemType], ValueType):
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
    def GetOrAdd(self, newItem: ItemType) -> ItemType:
        """

        :param newItem:
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
    def TryGet(self, key: KeyType) -> ItemType:
        """

        :param key:
        :return:
        """

class ConcurrentSetItem(ABC, Generic[KeyType, ItemType], Object):
    """"""

    @overload
    def Compare(self, other: ItemType) -> int:
        """

        :param other:
        :return:
        """
    @overload
    def Compare(self, key: KeyType) -> int:
        """

        :param key:
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

class ControllerCommand(Enum):
    """"""

    Update: ControllerCommand = ...
    """"""
    Disable: ControllerCommand = ...
    """"""
    Enable: ControllerCommand = ...
    """"""
    SendManifest: ControllerCommand = ...
    """"""

class DataCollector(ValueType):
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DateTimeOffsetTypeInfo(TraceLoggingTypeInfo[DateTimeOffset]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[DateTimeOffset]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: DateTimeOffset) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class DateTimeTypeInfo(TraceLoggingTypeInfo[DateTime]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[DateTime]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: DateTime) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class DecimalTypeInfo(TraceLoggingTypeInfo[Decimal]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[Decimal]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: Decimal) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class DoubleArrayTypeInfo(TraceLoggingTypeInfo[Array[Double]]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[Array[float]]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: float) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class DoubleTypeInfo(TraceLoggingTypeInfo[Double]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[float]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: float) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class EmptyStruct(ValueType):
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EnumByteTypeInfo(Generic[EnumType], TraceLoggingTypeInfo[EnumType]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[EnumType]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: EnumType) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class EnumHelper(ABC, Generic[UnderlyingType], Object):
    """"""

    @classmethod
    def Cast(cls, value: ValueType) -> UnderlyingType:
        """

        :param value:
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

class EnumInt16TypeInfo(Generic[EnumType], TraceLoggingTypeInfo[EnumType]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[EnumType]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: EnumType) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class EnumInt32TypeInfo(Generic[EnumType], TraceLoggingTypeInfo[EnumType]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[EnumType]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: EnumType) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class EnumInt64TypeInfo(Generic[EnumType], TraceLoggingTypeInfo[EnumType]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[EnumType]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: EnumType) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class EnumSByteTypeInfo(Generic[EnumType], TraceLoggingTypeInfo[EnumType]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[EnumType]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: EnumType) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class EnumUInt16TypeInfo(Generic[EnumType], TraceLoggingTypeInfo[EnumType]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[EnumType]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: EnumType) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class EnumUInt32TypeInfo(Generic[EnumType], TraceLoggingTypeInfo[EnumType]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[EnumType]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: EnumType) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class EnumUInt64TypeInfo(Generic[EnumType], TraceLoggingTypeInfo[EnumType]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[EnumType]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: EnumType) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class EnumerableTypeInfo(Generic[IterableType, ElementType], TraceLoggingTypeInfo[IterableType]):
    """"""

    def __init__(self, elementInfo: TraceLoggingTypeInfo[ElementType]):
        """

        :param elementInfo:
        """
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[IterableType]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: IterableType) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class EtwSession(Object):
    """"""

    m_activityFilter: Final[ActivityFilter] = ...
    """
    
    :return: 
    """
    m_etwSessionId: Final[int] = ...
    """
    
    :return: 
    """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetEtwSession(cls, etwSessionId: int, bCreateIfNeeded: bool = ...) -> EtwSession:
        """

        :param etwSessionId:
        :param bCreateIfNeeded:
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
    @classmethod
    def RemoveEtwSession(cls, etwSession: EtwSession) -> None:
        """

        :param etwSession:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EventActivityOptions(Enum):
    """"""

    _None: EventActivityOptions = ...
    """"""
    Disable: EventActivityOptions = ...
    """"""
    Recursive: EventActivityOptions = ...
    """"""
    Detachable: EventActivityOptions = ...
    """"""

class EventAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, eventId: int):
        """

        :param eventId:
        """
    @property
    def ActivityOptions(self) -> EventActivityOptions:
        """

        :return:
        """
    @ActivityOptions.setter
    def ActivityOptions(self, value: EventActivityOptions) -> None: ...
    @property
    def Channel(self) -> EventChannel:
        """

        :return:
        """
    @Channel.setter
    def Channel(self, value: EventChannel) -> None: ...
    @property
    def EventId(self) -> int:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @Keywords.setter
    def Keywords(self, value: EventKeywords) -> None: ...
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @Level.setter
    def Level(self, value: EventLevel) -> None: ...
    @property
    def Message(self) -> str:
        """

        :return:
        """
    @Message.setter
    def Message(self, value: str) -> None: ...
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @Opcode.setter
    def Opcode(self, value: EventOpcode) -> None: ...
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    @Tags.setter
    def Tags(self, value: EventTags) -> None: ...
    @property
    def Task(self) -> EventTask:
        """

        :return:
        """
    @Task.setter
    def Task(self, value: EventTask) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Version(self) -> int:
        """

        :return:
        """
    @Version.setter
    def Version(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EventChannel(Enum):
    """"""

    _None: EventChannel = ...
    """"""
    Admin: EventChannel = ...
    """"""
    Operational: EventChannel = ...
    """"""
    Analytic: EventChannel = ...
    """"""
    Debug: EventChannel = ...
    """"""

class EventChannelAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def Enabled(self) -> bool:
        """

        :return:
        """
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
    @property
    def EventChannelType(self) -> EventChannelType:
        """

        :return:
        """
    @EventChannelType.setter
    def EventChannelType(self, value: EventChannelType) -> None: ...
    @property
    def TypeId(self) -> object:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EventChannelType(Enum):
    """"""

    Admin: EventChannelType = ...
    """"""
    Operational: EventChannelType = ...
    """"""
    Analytic: EventChannelType = ...
    """"""
    Debug: EventChannelType = ...
    """"""

class EventCommand(Enum):
    """"""

    Update: EventCommand = ...
    """"""
    Disable: EventCommand = ...
    """"""
    Enable: EventCommand = ...
    """"""
    SendManifest: EventCommand = ...
    """"""

class EventCommandEventArgs(EventArgs):
    """"""

    @property
    def Arguments(self) -> IDictionary[str, str]:
        """

        :return:
        """
    @property
    def Command(self) -> EventCommand:
        """

        :return:
        """
    def DisableEvent(self, eventId: int) -> bool:
        """

        :param eventId:
        :return:
        """
    def EnableEvent(self, eventId: int) -> bool:
        """

        :param eventId:
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

class EventDataAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EventDescriptor(ValueType):
    """"""

    @overload
    def __init__(self, traceloggingId: int, level: int, opcode: int, keywords: int):
        """

        :param traceloggingId:
        :param level:
        :param opcode:
        :param keywords:
        """
    @overload
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
    @overload
    def Equals(self, other: EventDescriptor) -> bool:
        """

        :param other:
        :return:
        """
    @overload
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
    def __eq__(self, other: EventDescriptor) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: EventDescriptor) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, event1: EventDescriptor, event2: EventDescriptor) -> bool:
        """

        :param event1:
        :param event2:
        :return:
        """
    @classmethod
    def op_Inequality(cls, event1: EventDescriptor, event2: EventDescriptor) -> bool:
        """

        :param event1:
        :param event2:
        :return:
        """

class EventDispatcher(Object):
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EventFieldAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def Format(self) -> EventFieldFormat:
        """

        :return:
        """
    @Format.setter
    def Format(self, value: EventFieldFormat) -> None: ...
    @property
    def Tags(self) -> EventFieldTags:
        """

        :return:
        """
    @Tags.setter
    def Tags(self, value: EventFieldTags) -> None: ...
    @property
    def TypeId(self) -> object:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EventFieldFormat(Enum):
    """"""

    Default: EventFieldFormat = ...
    """"""
    String: EventFieldFormat = ...
    """"""
    Boolean: EventFieldFormat = ...
    """"""
    Hexadecimal: EventFieldFormat = ...
    """"""
    Xml: EventFieldFormat = ...
    """"""
    Json: EventFieldFormat = ...
    """"""
    HResult: EventFieldFormat = ...
    """"""

class EventFieldTags(Enum):
    """"""

    _None: EventFieldTags = ...
    """"""

class EventIgnoreAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EventKeywords(Enum):
    """"""

    _None: EventKeywords = ...
    """"""
    MicrosoftTelemetry: EventKeywords = ...
    """"""
    WdiContext: EventKeywords = ...
    """"""
    WdiDiagnostic: EventKeywords = ...
    """"""
    Sqm: EventKeywords = ...
    """"""
    AuditFailure: EventKeywords = ...
    """"""
    CorrelationHint: EventKeywords = ...
    """"""
    AuditSuccess: EventKeywords = ...
    """"""
    EventLogClassic: EventKeywords = ...
    """"""
    All: EventKeywords = ...
    """"""

class EventLevel(Enum):
    """"""

    LogAlways: EventLevel = ...
    """"""
    Critical: EventLevel = ...
    """"""
    Error: EventLevel = ...
    """"""
    Warning: EventLevel = ...
    """"""
    Informational: EventLevel = ...
    """"""
    Verbose: EventLevel = ...
    """"""

class EventListener(Object, IDisposable):
    """"""

    def __init__(self):
        """"""
    def DisableEvents(self, eventSource: EventSource) -> None:
        """

        :param eventSource:
        """
    def Dispose(self) -> None:
        """"""
    @overload
    def EnableEvents(self, eventSource: EventSource, level: EventLevel) -> None:
        """

        :param eventSource:
        :param level:
        """
    @overload
    def EnableEvents(
        self, eventSource: EventSource, level: EventLevel, matchAnyKeyword: EventKeywords
    ) -> None:
        """

        :param eventSource:
        :param level:
        :param matchAnyKeyword:
        """
    @overload
    def EnableEvents(
        self,
        eventSource: EventSource,
        level: EventLevel,
        matchAnyKeyword: EventKeywords,
        arguments: IDictionary[str, str],
    ) -> None:
        """

        :param eventSource:
        :param level:
        :param matchAnyKeyword:
        :param arguments:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def EventSourceIndex(cls, eventSource: EventSource) -> int:
        """

        :param eventSource:
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
    EventSourceCreated: EventType[EventHandler[EventSourceCreatedEventArgs]] = ...
    """"""
    EventWritten: EventType[EventHandler[EventWrittenEventArgs]] = ...
    """"""

class EventManifestOptions(Enum):
    """"""

    _None: EventManifestOptions = ...
    """"""
    Strict: EventManifestOptions = ...
    """"""
    AllCultures: EventManifestOptions = ...
    """"""
    OnlyIfNeededForRegistration: EventManifestOptions = ...
    """"""
    AllowEventSourceOverride: EventManifestOptions = ...
    """"""

class EventOpcode(Enum):
    """"""

    Info: EventOpcode = ...
    """"""
    Start: EventOpcode = ...
    """"""
    Stop: EventOpcode = ...
    """"""
    DataCollectionStart: EventOpcode = ...
    """"""
    DataCollectionStop: EventOpcode = ...
    """"""
    Extension: EventOpcode = ...
    """"""
    Reply: EventOpcode = ...
    """"""
    Resume: EventOpcode = ...
    """"""
    Suspend: EventOpcode = ...
    """"""
    Send: EventOpcode = ...
    """"""
    Receive: EventOpcode = ...
    """"""

class EventPayload(
    Object,
    ICollection[KeyValuePair, Object],
    IDictionary[String, Object],
    IEnumerable[KeyValuePair, Object],
    IEnumerable,
):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection[str]:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection[object]:
        """

        :return:
        """
    @overload
    def Add(self, item: KeyValuePair[str, object]) -> None:
        """

        :param item:
        """
    @overload
    def Add(self, key: str, value: object) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, item: KeyValuePair[str, object]) -> bool:
        """

        :param item:
        :return:
        """
    def ContainsKey(self, key: str) -> bool:
        """

        :param key:
        :return:
        """
    def CopyTo(self, array: Array[KeyValuePair, object], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    @overload
    def Remove(self, item: KeyValuePair[str, object]) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def Remove(self, key: str) -> bool:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TryGetValue(self, key: str, value: object) -> Tuple[bool, object]:
        """"""
    def __contains__(self, value: KeyValuePair[str, object]) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, key: str) -> object:
        """

        :param key:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[KeyValuePair, object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, key: str, value: object) -> None:
        """

        :param key:
        :param value:
        """

class EventProvider(Object, IDisposable):
    """"""

    def Close(self) -> None:
        """"""
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
    def ToString(self) -> str:
        """

        :return:
        """

    class EventData(ValueType):
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
        def GetType(self) -> Type:
            """

            :return:
            """
        def ToString(self) -> str:
            """

            :return:
            """

    class SessionInfo(ValueType):
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
        def GetType(self) -> Type:
            """

            :return:
            """
        def ToString(self) -> str:
            """

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
        NullInput: WriteEventErrorCode = ...
        """"""
        TooManyArgs: WriteEventErrorCode = ...
        """"""
        Other: WriteEventErrorCode = ...
        """"""

class EventSource(Object, IDisposable):
    """"""

    @overload
    def __init__(self, eventSourceName: str):
        """

        :param eventSourceName:
        """
    @overload
    def __init__(self, eventSourceName: str, config: EventSourceSettings):
        """

        :param eventSourceName:
        :param config:
        """
    @overload
    def __init__(self, eventSourceName: str, config: EventSourceSettings, traits: Array[str]):
        """

        :param eventSourceName:
        :param config:
        :param traits:
        """
    @property
    def ConstructionException(self) -> Exception:
        """

        :return:
        """
    @classmethod
    @property
    def CurrentThreadActivityId(cls) -> Guid:
        """

        :return:
        """
    @property
    def Guid(self) -> Guid:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Settings(self) -> EventSourceSettings:
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
    @classmethod
    @overload
    def GenerateManifest(cls, eventSourceType: Type, assemblyPathToIncludeInManifest: str) -> str:
        """

        :param eventSourceType:
        :param assemblyPathToIncludeInManifest:
        :return:
        """
    @classmethod
    @overload
    def GenerateManifest(
        cls,
        eventSourceType: Type,
        assemblyPathToIncludeInManifest: str,
        flags: EventManifestOptions,
    ) -> str:
        """

        :param eventSourceType:
        :param assemblyPathToIncludeInManifest:
        :param flags:
        :return:
        """
    @classmethod
    def GetGuid(cls, eventSourceType: Type) -> Guid:
        """

        :param eventSourceType:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    def GetName(cls, eventSourceType: Type) -> str:
        """

        :param eventSourceType:
        :return:
        """
    @classmethod
    def GetSources(cls) -> IEnumerable[EventSource]:
        """

        :return:
        """
    def GetTrait(self, key: str) -> str:
        """

        :param key:
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
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords) -> bool:
        """

        :param level:
        :param keywords:
        :return:
        """
    @overload
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords, channel: EventChannel) -> bool:
        """

        :param level:
        :param keywords:
        :param channel:
        :return:
        """
    @classmethod
    def SendCommand(
        cls,
        eventSource: EventSource,
        command: EventCommand,
        commandArguments: IDictionary[str, str],
    ) -> None:
        """

        :param eventSource:
        :param command:
        :param commandArguments:
        """
    @classmethod
    @overload
    def SetCurrentThreadActivityId(cls, activityId: Guid) -> None:
        """

        :param activityId:
        """
    @classmethod
    @overload
    def SetCurrentThreadActivityId(
        cls, activityId: Guid, oldActivityThatWillContinue: Guid
    ) -> Tuple[None, Guid]:
        """

        :param activityId:
        :param oldActivityThatWillContinue:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Write(self, eventName: str) -> None:
        """

        :param eventName:
        """
    @overload
    def Write(self, eventName: str, data: T) -> None:
        """

        :param eventName:
        :param data:
        """
    @overload
    def Write(self, eventName: str, options: EventSourceOptions) -> None:
        """

        :param eventName:
        :param options:
        """
    @overload
    def Write(self, eventName: str, options: EventSourceOptions, data: T) -> None:
        """

        :param eventName:
        :param options:
        :param data:
        """
    @overload
    def Write(self, eventName: str, options: EventSourceOptions, data: T) -> None:
        """

        :param eventName:
        :param options:
        :param data:
        """
    @overload
    def Write(
        self,
        eventName: str,
        options: EventSourceOptions,
        activityId: Guid,
        relatedActivityId: Guid,
        data: T,
    ) -> None:
        """

        :param eventName:
        :param options:
        :param activityId:
        :param relatedActivityId:
        :param data:
        """
    EventCommandExecuted: EventType[EventHandler[EventCommandEventArgs]] = ...
    """"""

class EventSourceActivity(Object, IDisposable):
    """"""

    def __init__(self, eventSource: EventSource):
        """

        :param eventSource:
        """
    @property
    def EventSource(self) -> EventSource:
        """

        :return:
        """
    @property
    def Id(self) -> Guid:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def Start(self, eventName: str) -> EventSourceActivity:
        """

        :param eventName:
        :return:
        """
    @overload
    def Start(self, eventName: str, data: T) -> EventSourceActivity:
        """

        :param eventName:
        :param data:
        :return:
        """
    @overload
    def Start(self, eventName: str, options: EventSourceOptions) -> EventSourceActivity:
        """

        :param eventName:
        :param options:
        :return:
        """
    @overload
    def Start(self, eventName: str, options: EventSourceOptions, data: T) -> EventSourceActivity:
        """

        :param eventName:
        :param options:
        :param data:
        :return:
        """
    @overload
    def Stop(self, data: T) -> None:
        """

        :param data:
        """
    @overload
    def Stop(self, eventName: str) -> None:
        """

        :param eventName:
        """
    @overload
    def Stop(self, eventName: str, data: T) -> None:
        """

        :param eventName:
        :param data:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Write(self, eventName: str) -> None:
        """

        :param eventName:
        """
    @overload
    def Write(self, eventName: str, data: T) -> None:
        """

        :param eventName:
        :param data:
        """
    @overload
    def Write(self, eventName: str, options: EventSourceOptions) -> None:
        """

        :param eventName:
        :param options:
        """
    @overload
    def Write(self, eventName: str, options: EventSourceOptions, data: T) -> None:
        """

        :param eventName:
        :param options:
        :param data:
        """
    @overload
    def Write(
        self, source: EventSource, eventName: str, options: EventSourceOptions, data: T
    ) -> None:
        """

        :param source:
        :param eventName:
        :param options:
        :param data:
        """
    @classmethod
    def op_Implicit(cls, eventSource: EventSource) -> EventSourceActivity:
        """

        :param eventSource:
        :return:
        """

class EventSourceAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def Guid(self) -> str:
        """

        :return:
        """
    @Guid.setter
    def Guid(self, value: str) -> None: ...
    @property
    def LocalizationResources(self) -> str:
        """

        :return:
        """
    @LocalizationResources.setter
    def LocalizationResources(self, value: str) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EventSourceCreatedEventArgs(EventArgs):
    """"""

    def __init__(self):
        """"""
    @property
    def EventSource(self) -> EventSource:
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

class EventSourceException(Exception, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, message: str, innerException: Exception):
        """

        :param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """

        :return:
        """
    @property
    def HResult(self) -> int:
        """

        :return:
        """
    @property
    def HelpLink(self) -> str:
        """

        :return:
        """
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """

        :return:
        """
    @property
    def Message(self) -> str:
        """

        :return:
        """
    @property
    def Source(self) -> str:
        """

        :return:
        """
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """

        :return:
        """
    @property
    def TargetSite(self) -> MethodBase:
        """

        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class EventSourceOptions(ValueType):
    """"""

    @property
    def ActivityOptions(self) -> EventActivityOptions:
        """

        :return:
        """
    @ActivityOptions.setter
    def ActivityOptions(self, value: EventActivityOptions) -> None: ...
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @Keywords.setter
    def Keywords(self, value: EventKeywords) -> None: ...
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @Level.setter
    def Level(self, value: EventLevel) -> None: ...
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @Opcode.setter
    def Opcode(self, value: EventOpcode) -> None: ...
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    @Tags.setter
    def Tags(self, value: EventTags) -> None: ...
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

class EventSourceSettings(Enum):
    """"""

    Default: EventSourceSettings = ...
    """"""
    ThrowOnEventWriteErrors: EventSourceSettings = ...
    """"""
    EtwManifestEventFormat: EventSourceSettings = ...
    """"""
    EtwSelfDescribingEventFormat: EventSourceSettings = ...
    """"""

class EventTags(Enum):
    """"""

    _None: EventTags = ...
    """"""

class EventTask(Enum):
    """"""

    _None: EventTask = ...
    """"""

class EventWrittenEventArgs(EventArgs):
    """"""

    @property
    def ActivityId(self) -> Guid:
        """

        :return:
        """
    @property
    def Channel(self) -> EventChannel:
        """

        :return:
        """
    @property
    def EventId(self) -> int:
        """

        :return:
        """
    @property
    def EventName(self) -> str:
        """

        :return:
        """
    @property
    def EventSource(self) -> EventSource:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Message(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Payload(self) -> ReadOnlyCollection[object]:
        """

        :return:
        """
    @property
    def PayloadNames(self) -> ReadOnlyCollection[str]:
        """

        :return:
        """
    @property
    def RelatedActivityId(self) -> Guid:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    @property
    def Task(self) -> EventTask:
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

class FieldMetadata(Object):
    """"""

    @overload
    def __init__(
        self, name: str, type: TraceLoggingDataType, tags: EventFieldTags, custom: Array[int]
    ):
        """

        :param name:
        :param type:
        :param tags:
        :param custom:
        """
    @overload
    def __init__(
        self, name: str, type: TraceLoggingDataType, tags: EventFieldTags, variableCount: bool
    ):
        """

        :param name:
        :param type:
        :param tags:
        :param variableCount:
        """
    @overload
    def __init__(
        self, name: str, type: TraceLoggingDataType, tags: EventFieldTags, fixedCount: int
    ):
        """

        :param name:
        :param type:
        :param tags:
        :param fixedCount:
        """
    def Encode(self, pos: int, metadata: Array[int]) -> None:
        """

        :param pos:
        :param metadata:
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
    def IncrementStructFieldCount(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class FrameworkEventSource(EventSource, IDisposable):
    """"""

    Log: Final[ClassVar[FrameworkEventSource]] = ...
    """
    
    :return: 
    """
    @property
    def ConstructionException(self) -> Exception:
        """

        :return:
        """
    @classmethod
    @property
    def CurrentThreadActivityId(cls) -> Guid:
        """

        :return:
        """
    @property
    def Guid(self) -> Guid:
        """

        :return:
        """
    @classmethod
    @property
    def IsInitialized(cls) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Settings(self) -> EventSourceSettings:
        """

        :return:
        """
    def BeginGetRequestStream(self, id: object, uri: str, success: bool, synchronous: bool) -> None:
        """

        :param id:
        :param uri:
        :param success:
        :param synchronous:
        """
    def BeginGetResponse(self, id: object, uri: str, success: bool, synchronous: bool) -> None:
        """

        :param id:
        :param uri:
        :param success:
        :param synchronous:
        """
    def Dispose(self) -> None:
        """"""
    def EndGetRequestStream(self, id: object, success: bool, synchronous: bool) -> None:
        """

        :param id:
        :param success:
        :param synchronous:
        """
    def EndGetResponse(self, id: object, success: bool, synchronous: bool, statusCode: int) -> None:
        """

        :param id:
        :param success:
        :param synchronous:
        :param statusCode:
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
    def GetTrait(self, key: str) -> str:
        """

        :param key:
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
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords) -> bool:
        """

        :param level:
        :param keywords:
        :return:
        """
    @overload
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords, channel: EventChannel) -> bool:
        """

        :param level:
        :param keywords:
        :param channel:
        :return:
        """
    @overload
    def ResourceManagerAddingCultureFromConfigFile(
        self, baseName: str, mainAssembly: Assembly, cultureName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssembly:
        :param cultureName:
        """
    @overload
    def ResourceManagerAddingCultureFromConfigFile(
        self, baseName: str, mainAssemblyName: str, cultureName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssemblyName:
        :param cultureName:
        """
    @overload
    def ResourceManagerCaseInsensitiveResourceStreamLookupFailed(
        self, baseName: str, mainAssembly: Assembly, assemblyName: str, resourceFileName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssembly:
        :param assemblyName:
        :param resourceFileName:
        """
    @overload
    def ResourceManagerCaseInsensitiveResourceStreamLookupFailed(
        self, baseName: str, mainAssemblyName: str, assemblyName: str, resourceFileName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssemblyName:
        :param assemblyName:
        :param resourceFileName:
        """
    @overload
    def ResourceManagerCaseInsensitiveResourceStreamLookupSucceeded(
        self, baseName: str, mainAssembly: Assembly, assemblyName: str, resourceFileName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssembly:
        :param assemblyName:
        :param resourceFileName:
        """
    @overload
    def ResourceManagerCaseInsensitiveResourceStreamLookupSucceeded(
        self, baseName: str, mainAssemblyName: str, assemblyName: str, resourceFileName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssemblyName:
        :param assemblyName:
        :param resourceFileName:
        """
    @overload
    def ResourceManagerCreatingResourceSet(
        self, baseName: str, mainAssembly: Assembly, cultureName: str, fileName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssembly:
        :param cultureName:
        :param fileName:
        """
    @overload
    def ResourceManagerCreatingResourceSet(
        self, baseName: str, mainAssemblyName: str, cultureName: str, fileName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssemblyName:
        :param cultureName:
        :param fileName:
        """
    @overload
    def ResourceManagerCultureFoundInConfigFile(
        self, baseName: str, mainAssembly: Assembly, cultureName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssembly:
        :param cultureName:
        """
    @overload
    def ResourceManagerCultureFoundInConfigFile(
        self, baseName: str, mainAssemblyName: str, cultureName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssemblyName:
        :param cultureName:
        """
    @overload
    def ResourceManagerCultureNotFoundInConfigFile(
        self, baseName: str, mainAssembly: Assembly, cultureName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssembly:
        :param cultureName:
        """
    @overload
    def ResourceManagerCultureNotFoundInConfigFile(
        self, baseName: str, mainAssemblyName: str, cultureName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssemblyName:
        :param cultureName:
        """
    @overload
    def ResourceManagerFoundResourceSetInCache(
        self, baseName: str, mainAssembly: Assembly, cultureName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssembly:
        :param cultureName:
        """
    @overload
    def ResourceManagerFoundResourceSetInCache(
        self, baseName: str, mainAssemblyName: str, cultureName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssemblyName:
        :param cultureName:
        """
    @overload
    def ResourceManagerFoundResourceSetInCacheUnexpected(
        self, baseName: str, mainAssembly: Assembly, cultureName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssembly:
        :param cultureName:
        """
    @overload
    def ResourceManagerFoundResourceSetInCacheUnexpected(
        self, baseName: str, mainAssemblyName: str, cultureName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssemblyName:
        :param cultureName:
        """
    @overload
    def ResourceManagerGetSatelliteAssemblyFailed(
        self, baseName: str, mainAssembly: Assembly, cultureName: str, assemblyName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssembly:
        :param cultureName:
        :param assemblyName:
        """
    @overload
    def ResourceManagerGetSatelliteAssemblyFailed(
        self, baseName: str, mainAssemblyName: str, cultureName: str, assemblyName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssemblyName:
        :param cultureName:
        :param assemblyName:
        """
    @overload
    def ResourceManagerGetSatelliteAssemblySucceeded(
        self, baseName: str, mainAssembly: Assembly, cultureName: str, assemblyName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssembly:
        :param cultureName:
        :param assemblyName:
        """
    @overload
    def ResourceManagerGetSatelliteAssemblySucceeded(
        self, baseName: str, mainAssemblyName: str, cultureName: str, assemblyName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssemblyName:
        :param cultureName:
        :param assemblyName:
        """
    @overload
    def ResourceManagerLookingForResourceSet(
        self, baseName: str, mainAssembly: Assembly, cultureName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssembly:
        :param cultureName:
        """
    @overload
    def ResourceManagerLookingForResourceSet(
        self, baseName: str, mainAssemblyName: str, cultureName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssemblyName:
        :param cultureName:
        """
    @overload
    def ResourceManagerLookupFailed(
        self, baseName: str, mainAssembly: Assembly, cultureName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssembly:
        :param cultureName:
        """
    @overload
    def ResourceManagerLookupFailed(
        self, baseName: str, mainAssemblyName: str, cultureName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssemblyName:
        :param cultureName:
        """
    @overload
    def ResourceManagerLookupStarted(
        self, baseName: str, mainAssembly: Assembly, cultureName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssembly:
        :param cultureName:
        """
    @overload
    def ResourceManagerLookupStarted(
        self, baseName: str, mainAssemblyName: str, cultureName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssemblyName:
        :param cultureName:
        """
    @overload
    def ResourceManagerManifestResourceAccessDenied(
        self, baseName: str, mainAssembly: Assembly, assemblyName: str, canonicalName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssembly:
        :param assemblyName:
        :param canonicalName:
        """
    @overload
    def ResourceManagerManifestResourceAccessDenied(
        self, baseName: str, mainAssemblyName: str, assemblyName: str, canonicalName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssemblyName:
        :param assemblyName:
        :param canonicalName:
        """
    @overload
    def ResourceManagerNeutralResourceAttributeMissing(self, mainAssembly: Assembly) -> None:
        """

        :param mainAssembly:
        """
    @overload
    def ResourceManagerNeutralResourceAttributeMissing(self, mainAssemblyName: str) -> None:
        """

        :param mainAssemblyName:
        """
    @overload
    def ResourceManagerNeutralResourcesFound(
        self, baseName: str, mainAssembly: Assembly, resName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssembly:
        :param resName:
        """
    @overload
    def ResourceManagerNeutralResourcesFound(
        self, baseName: str, mainAssemblyName: str, resName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssemblyName:
        :param resName:
        """
    @overload
    def ResourceManagerNeutralResourcesNotFound(
        self, baseName: str, mainAssembly: Assembly, resName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssembly:
        :param resName:
        """
    @overload
    def ResourceManagerNeutralResourcesNotFound(
        self, baseName: str, mainAssemblyName: str, resName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssemblyName:
        :param resName:
        """
    @overload
    def ResourceManagerNeutralResourcesSufficient(
        self, baseName: str, mainAssembly: Assembly, cultureName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssembly:
        :param cultureName:
        """
    @overload
    def ResourceManagerNeutralResourcesSufficient(
        self, baseName: str, mainAssemblyName: str, cultureName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssemblyName:
        :param cultureName:
        """
    @overload
    def ResourceManagerNotCreatingResourceSet(
        self, baseName: str, mainAssembly: Assembly, cultureName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssembly:
        :param cultureName:
        """
    @overload
    def ResourceManagerNotCreatingResourceSet(
        self, baseName: str, mainAssemblyName: str, cultureName: str
    ) -> None:
        """

        :param baseName:
        :param mainAssemblyName:
        :param cultureName:
        """
    @overload
    def ResourceManagerReleasingResources(self, baseName: str, mainAssembly: Assembly) -> None:
        """

        :param baseName:
        :param mainAssembly:
        """
    @overload
    def ResourceManagerReleasingResources(self, baseName: str, mainAssemblyName: str) -> None:
        """

        :param baseName:
        :param mainAssemblyName:
        """
    @overload
    def ResourceManagerStreamFound(
        self,
        baseName: str,
        mainAssembly: Assembly,
        cultureName: str,
        loadedAssembly: Assembly,
        resourceFileName: str,
    ) -> None:
        """

        :param baseName:
        :param mainAssembly:
        :param cultureName:
        :param loadedAssembly:
        :param resourceFileName:
        """
    @overload
    def ResourceManagerStreamFound(
        self,
        baseName: str,
        mainAssemblyName: str,
        cultureName: str,
        loadedAssemblyName: str,
        resourceFileName: str,
    ) -> None:
        """

        :param baseName:
        :param mainAssemblyName:
        :param cultureName:
        :param loadedAssemblyName:
        :param resourceFileName:
        """
    @overload
    def ResourceManagerStreamNotFound(
        self,
        baseName: str,
        mainAssembly: Assembly,
        cultureName: str,
        loadedAssembly: Assembly,
        resourceFileName: str,
    ) -> None:
        """

        :param baseName:
        :param mainAssembly:
        :param cultureName:
        :param loadedAssembly:
        :param resourceFileName:
        """
    @overload
    def ResourceManagerStreamNotFound(
        self,
        baseName: str,
        mainAssemblyName: str,
        cultureName: str,
        loadedAssemblyName: str,
        resourceFileName: str,
    ) -> None:
        """

        :param baseName:
        :param mainAssemblyName:
        :param cultureName:
        :param loadedAssemblyName:
        :param resourceFileName:
        """
    def ThreadPoolDequeueWork(self, workID: int) -> None:
        """

        :param workID:
        """
    def ThreadPoolDequeueWorkObject(self, workID: object) -> None:
        """

        :param workID:
        """
    def ThreadPoolEnqueueWork(self, workID: int) -> None:
        """

        :param workID:
        """
    def ThreadPoolEnqueueWorkObject(self, workID: object) -> None:
        """

        :param workID:
        """
    def ThreadTransferReceive(self, id: int, kind: int, info: str) -> None:
        """

        :param id:
        :param kind:
        :param info:
        """
    def ThreadTransferReceiveHandled(self, id: int, kind: int, info: str) -> None:
        """

        :param id:
        :param kind:
        :param info:
        """
    def ThreadTransferReceiveHandledObj(self, id: object, kind: int, info: str) -> None:
        """

        :param id:
        :param kind:
        :param info:
        """
    def ThreadTransferReceiveObj(self, id: object, kind: int, info: str) -> None:
        """

        :param id:
        :param kind:
        :param info:
        """
    def ThreadTransferSend(self, id: int, kind: int, info: str, multiDequeues: bool) -> None:
        """

        :param id:
        :param kind:
        :param info:
        :param multiDequeues:
        """
    def ThreadTransferSendObj(self, id: object, kind: int, info: str, multiDequeues: bool) -> None:
        """

        :param id:
        :param kind:
        :param info:
        :param multiDequeues:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Write(self, eventName: str) -> None:
        """

        :param eventName:
        """
    @overload
    def Write(self, eventName: str, data: T) -> None:
        """

        :param eventName:
        :param data:
        """
    @overload
    def Write(self, eventName: str, options: EventSourceOptions) -> None:
        """

        :param eventName:
        :param options:
        """
    @overload
    def Write(self, eventName: str, options: EventSourceOptions, data: T) -> None:
        """

        :param eventName:
        :param options:
        :param data:
        """
    @overload
    def Write(self, eventName: str, options: EventSourceOptions, data: T) -> None:
        """

        :param eventName:
        :param options:
        :param data:
        """
    @overload
    def Write(
        self,
        eventName: str,
        options: EventSourceOptions,
        activityId: Guid,
        relatedActivityId: Guid,
        data: T,
    ) -> None:
        """

        :param eventName:
        :param options:
        :param activityId:
        :param relatedActivityId:
        :param data:
        """
    EventCommandExecuted: EventType[EventHandler[EventCommandEventArgs]] = ...
    """"""

    class Keywords(ABC, Object):
        """"""

        DynamicTypeUsage: Final[ClassVar[EventKeywords]] = ...
        """"""
        Loader: Final[ClassVar[EventKeywords]] = ...
        """"""
        NetClient: Final[ClassVar[EventKeywords]] = ...
        """"""
        ThreadPool: Final[ClassVar[EventKeywords]] = ...
        """"""
        ThreadTransfer: Final[ClassVar[EventKeywords]] = ...
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
        def GetType(self) -> Type:
            """

            :return:
            """
        def ToString(self) -> str:
            """

            :return:
            """

    class Opcodes(ABC, Object):
        """"""

        ReceiveHandled: Final[ClassVar[EventOpcode]] = ...
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
        def GetType(self) -> Type:
            """

            :return:
            """
        def ToString(self) -> str:
            """

            :return:
            """

    class Tasks(ABC, Object):
        """"""

        GetRequestStream: Final[ClassVar[EventTask]] = ...
        """"""
        GetResponse: Final[ClassVar[EventTask]] = ...
        """"""
        ThreadTransfer: Final[ClassVar[EventTask]] = ...
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
        def GetType(self) -> Type:
            """

            :return:
            """
        def ToString(self) -> str:
            """

            :return:
            """

class GuidArrayTypeInfo(TraceLoggingTypeInfo[Array[Guid]]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[Array[Guid]]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: Guid) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class GuidTypeInfo(TraceLoggingTypeInfo[Guid]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[Guid]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: Guid) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class Int16ArrayTypeInfo(TraceLoggingTypeInfo[Array[Int16]]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[Array[int]]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: int) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class Int16TypeInfo(TraceLoggingTypeInfo[Int16]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[int]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: int) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class Int32ArrayTypeInfo(TraceLoggingTypeInfo[Array[Int32]]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[Array[int]]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: int) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class Int32TypeInfo(TraceLoggingTypeInfo[Int32]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[int]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: int) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class Int64ArrayTypeInfo(TraceLoggingTypeInfo[Array[Int64]]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[Array[int]]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: int) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class Int64TypeInfo(TraceLoggingTypeInfo[Int64]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[int]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: int) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class IntPtrArrayTypeInfo(TraceLoggingTypeInfo[Array[IntPtr]]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[Array[IntPtr]]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: IntPtr) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class IntPtrTypeInfo(TraceLoggingTypeInfo[IntPtr]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[IntPtr]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: IntPtr) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class InvokeTypeInfo(Generic[ContainerType], TraceLoggingTypeInfo[ContainerType]):
    """"""

    def __init__(self, typeAnalysis: TypeAnalysis):
        """

        :param typeAnalysis:
        """
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[ContainerType]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: ContainerType) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class KeyValuePairTypeInfo(Generic[K, V], TraceLoggingTypeInfo[KeyValuePair, V]):
    """"""

    def __init__(self, recursionCheck: List[Type]):
        """

        :param recursionCheck:
        """
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[KeyValuePair, V]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: KeyValuePair[K, V]) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class ManifestBuilder(Object):
    """"""

    def __init__(
        self,
        providerName: str,
        providerGuid: Guid,
        dllName: str,
        resources: ResourceManager,
        flags: EventManifestOptions,
    ):
        """

        :param providerName:
        :param providerGuid:
        :param dllName:
        :param resources:
        :param flags:
        """
    @property
    def Errors(self) -> IList[str]:
        """

        :return:
        """
    def AddChannel(self, name: str, value: int, channelAttribute: EventChannelAttribute) -> None:
        """

        :param name:
        :param value:
        :param channelAttribute:
        """
    def AddEventParameter(self, type: Type, name: str) -> None:
        """

        :param type:
        :param name:
        """
    def AddKeyword(self, name: str, value: int) -> None:
        """

        :param name:
        :param value:
        """
    def AddOpcode(self, name: str, value: int) -> None:
        """

        :param name:
        :param value:
        """
    def AddTask(self, name: str, value: int) -> None:
        """

        :param name:
        :param value:
        """
    def CreateManifest(self) -> Array[int]:
        """

        :return:
        """
    def EndEvent(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetChannelData(self) -> Array[int]:
        """

        :return:
        """
    def GetChannelKeyword(self, channel: EventChannel) -> int:
        """

        :param channel:
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
    def ManifestError(self, msg: str, runtimeCritical: bool = ...) -> None:
        """

        :param msg:
        :param runtimeCritical:
        """
    def StartEvent(self, eventName: str, eventAttribute: EventAttribute) -> None:
        """

        :param eventName:
        :param eventAttribute:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ManifestEnvelope(ValueType):
    """"""

    ChunkNumber: Final[int] = ...
    """
    
    :return: 
    """
    Format: Final[ManifestEnvelope.ManifestFormats] = ...
    """
    
    :return: 
    """
    Magic: Final[int] = ...
    """
    
    :return: 
    """
    MajorVersion: Final[int] = ...
    """
    
    :return: 
    """
    MaxChunkSize: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MinorVersion: Final[int] = ...
    """
    
    :return: 
    """
    TotalChunks: Final[int] = ...
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

    class ManifestFormats(Enum):
        """"""

        SimpleXmlFormat: ManifestFormats = ...
        """"""

class NameInfo(ConcurrentSetItem[KeyValuePair, EventTags, NameInfo]):
    """"""

    def __init__(self, name: str, tags: EventTags, typeMetadataSize: int):
        """

        :param name:
        :param tags:
        :param typeMetadataSize:
        """
    @overload
    def Compare(self, key: KeyValuePair[str, EventTags]) -> int:
        """

        :param other:
        :return:
        """
    @overload
    def Compare(self, other: NameInfo) -> int:
        """

        :param other:
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

class NonEventAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class NonGenericProperytWriter(Generic[ContainerType], PropertyAccessor[ContainerType]):
    """"""

    def __init__(self, property: PropertyAnalysis):
        """

        :param property:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: ContainerType) -> object:
        """

        :param value:
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
    def Write(self, collector: TraceLoggingDataCollector, value: ContainerType) -> None:
        """

        :param collector:
        :param value:
        """

class NullTypeInfo(Generic[DataType], TraceLoggingTypeInfo[DataType]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[DataType]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: DataType) -> None:
        """

        :param collector:
        :param value:
        """
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class NullableTypeInfo(Generic[T], TraceLoggingTypeInfo[T]):
    """"""

    def __init__(self, recursionCheck: List[Type]):
        """

        :param recursionCheck:
        """
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[Optional[T]]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: Optional[T]) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class PropertyAccessor(ABC, Generic[ContainerType], Object):
    """"""

    @classmethod
    def Create(cls, property: PropertyAnalysis) -> PropertyAccessor[ContainerType]:
        """

        :param property:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: ContainerType) -> object:
        """

        :param value:
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
    def Write(self, collector: TraceLoggingDataCollector, value: ContainerType) -> None:
        """

        :param collector:
        :param value:
        """

class PropertyAnalysis(Object):
    """"""

    def __init__(
        self,
        name: str,
        getterInfo: MethodInfo,
        typeInfo: TraceLoggingTypeInfo,
        fieldAttribute: EventFieldAttribute,
    ):
        """

        :param name:
        :param getterInfo:
        :param typeInfo:
        :param fieldAttribute:
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

class SByteArrayTypeInfo(TraceLoggingTypeInfo[Array[SByte]]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[Array[int]]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: int) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class SByteTypeInfo(TraceLoggingTypeInfo[SByte]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[int]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: int) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class SessionMask(ValueType):
    """"""

    @overload
    def __init__(self, m: SessionMask):
        """

        :param m:
        """
    @overload
    def __init__(self, mask: int = ...):
        """

        :param mask:
        """
    @classmethod
    @property
    def All(cls) -> SessionMask:
        """

        :return:
        """
    @property
    def Item(self) -> bool:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: bool) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def FromEventKeywords(cls, m: int) -> SessionMask:
        """

        :param m:
        :return:
        """
    @classmethod
    def FromId(cls, perEventSourceSessionId: int) -> SessionMask:
        """

        :param perEventSourceSessionId:
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
    def IsEqualOrSupersetOf(self, m: SessionMask) -> bool:
        """

        :param m:
        :return:
        """
    def ToEventKeywords(self) -> int:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __and__(self, other: SessionMask) -> SessionMask:
        """

        :param other:
        :return:
        """
    def __getitem__(self, perEventSourceSessionId: int) -> bool:
        """

        :param perEventSourceSessionId:
        :return:
        """
    def __invert__(self) -> SessionMask:
        """

        :return:
        """
    def __or__(self, other: SessionMask) -> SessionMask:
        """

        :param other:
        :return:
        """
    def __setitem__(self, perEventSourceSessionId: int, value: bool) -> None:
        """

        :param perEventSourceSessionId:
        :param value:
        """
    def __xor__(self, other: SessionMask) -> SessionMask:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_BitwiseAnd(cls, m1: SessionMask, m2: SessionMask) -> SessionMask:
        """

        :param m1:
        :param m2:
        :return:
        """
    @classmethod
    def op_BitwiseOr(cls, m1: SessionMask, m2: SessionMask) -> SessionMask:
        """

        :param m1:
        :param m2:
        :return:
        """
    @classmethod
    def op_ExclusiveOr(cls, m1: SessionMask, m2: SessionMask) -> SessionMask:
        """

        :param m1:
        :param m2:
        :return:
        """
    @classmethod
    def op_Explicit(cls, m: SessionMask) -> int:
        """

        :param m:
        :return:
        """
    @classmethod
    def op_OnesComplement(cls, m: SessionMask) -> SessionMask:
        """

        :param m:
        :return:
        """

class SimpleEventTypes(Generic[T], TraceLoggingEventTypes):
    """"""

    @classmethod
    @property
    def Instance(cls) -> SimpleEventTypes[T]:
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

class SingleArrayTypeInfo(TraceLoggingTypeInfo[Array[Single]]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[Array[float]]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: float) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class SingleTypeInfo(TraceLoggingTypeInfo[Single]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[float]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: float) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class Statics(ABC, Object):
    """"""

    DefaultLevel: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    EventTagsMask: Final[ClassVar[EventTags]] = ...
    """
    
    :return: 
    """
    HexIntPtrType: Final[ClassVar[TraceLoggingDataType]] = ...
    """
    
    :return: 
    """
    InTypeChainFlag: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    InTypeCountMask: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    InTypeCustomCountFlag: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    InTypeFixedCountFlag: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    InTypeMask: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    InTypeVariableCountFlag: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    IntPtrType: Final[ClassVar[TraceLoggingDataType]] = ...
    """
    
    :return: 
    """
    OutTypeChainFlag: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    OutTypeMask: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    TraceLoggingChannel: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    UIntPtrType: Final[ClassVar[TraceLoggingDataType]] = ...
    """
    
    :return: 
    """
    @classmethod
    def CheckName(cls, name: str) -> None:
        """

        :param name:
        """
    @classmethod
    @overload
    def Combine(cls, settingValue: int, defaultValue: int) -> int:
        """

        :param settingValue:
        :param defaultValue:
        :return:
        """
    @classmethod
    @overload
    def Combine(cls, settingValue1: int, settingValue2: int) -> int:
        """

        :param settingValue1:
        :param settingValue2:
        :return:
        """
    @classmethod
    @overload
    def Combine(cls, settingValue1: int, settingValue2: int, defaultValue: int) -> int:
        """

        :param settingValue1:
        :param settingValue2:
        :param defaultValue:
        :return:
        """
    @classmethod
    def CreateDefaultTypeInfo(cls, recursionCheck: List[Type]) -> TraceLoggingTypeInfo[DataType]:
        """

        :param recursionCheck:
        :return:
        """
    @classmethod
    def CreateDelegate(cls, delegateType: Type, methodInfo: MethodInfo) -> Delegate:
        """

        :param delegateType:
        :param methodInfo:
        :return:
        """
    @classmethod
    def CreateInstance(cls, type: Type, parameters: Array[object]) -> object:
        """

        :param type:
        :param parameters:
        :return:
        """
    @classmethod
    def EncodeTags(cls, tags: int, pos: int, metadata: Array[int]) -> None:
        """

        :param tags:
        :param pos:
        :param metadata:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def FindEnumerableElementType(cls, type: Type) -> Type:
        """

        :param type:
        :return:
        """
    @classmethod
    def Format16(
        cls, format: EventFieldFormat, native: TraceLoggingDataType
    ) -> TraceLoggingDataType:
        """

        :param format:
        :param native:
        :return:
        """
    @classmethod
    def Format32(
        cls, format: EventFieldFormat, native: TraceLoggingDataType
    ) -> TraceLoggingDataType:
        """

        :param format:
        :param native:
        :return:
        """
    @classmethod
    def Format64(
        cls, format: EventFieldFormat, native: TraceLoggingDataType
    ) -> TraceLoggingDataType:
        """

        :param format:
        :param native:
        :return:
        """
    @classmethod
    def Format8(
        cls, format: EventFieldFormat, native: TraceLoggingDataType
    ) -> TraceLoggingDataType:
        """

        :param format:
        :param native:
        :return:
        """
    @classmethod
    def FormatPtr(
        cls, format: EventFieldFormat, native: TraceLoggingDataType
    ) -> TraceLoggingDataType:
        """

        :param format:
        :param native:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttribute(cls, propInfo: PropertyInfo) -> AttributeType:
        """

        :param propInfo:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttribute(cls, type: Type) -> AttributeType:
        """

        :param type:
        :return:
        """
    @classmethod
    def GetDeclaredStaticMethod(cls, declaringType: Type, name: str) -> MethodInfo:
        """

        :param declaringType:
        :param name:
        :return:
        """
    @classmethod
    def GetGenericArguments(cls, type: Type) -> Array[Type]:
        """

        :param type:
        :return:
        """
    @classmethod
    def GetGetMethod(cls, propInfo: PropertyInfo) -> MethodInfo:
        """

        :param propInfo:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    def GetProperties(cls, type: Type) -> IEnumerable[PropertyInfo]:
        """

        :param type:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def GetTypeInfoInstance(
        cls, dataType: Type, recursionCheck: List[Type]
    ) -> TraceLoggingTypeInfo:
        """

        :param dataType:
        :param recursionCheck:
        :return:
        """
    @classmethod
    def HasCustomAttribute(cls, propInfo: PropertyInfo, attributeType: Type) -> bool:
        """

        :param propInfo:
        :param attributeType:
        :return:
        """
    @classmethod
    def IsEnum(cls, type: Type) -> bool:
        """

        :param type:
        :return:
        """
    @classmethod
    def IsGenericMatch(cls, type: Type, openType: object) -> bool:
        """

        :param type:
        :param openType:
        :return:
        """
    @classmethod
    def IsValueType(cls, type: Type) -> bool:
        """

        :param type:
        :return:
        """
    @classmethod
    def MakeDataType(
        cls, baseType: TraceLoggingDataType, format: EventFieldFormat
    ) -> TraceLoggingDataType:
        """

        :param baseType:
        :param format:
        :return:
        """
    @classmethod
    def MetadataForString(
        cls, name: str, prefixSize: int, suffixSize: int, additionalSize: int
    ) -> Array[int]:
        """

        :param name:
        :param prefixSize:
        :param suffixSize:
        :param additionalSize:
        :return:
        """
    @classmethod
    def ShouldOverrideFieldName(cls, fieldName: str) -> bool:
        """

        :param fieldName:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class StringTypeInfo(TraceLoggingTypeInfo[String]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[str]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: str) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class StructPropertyWriter(Generic[ContainerType, ValueType], PropertyAccessor[ContainerType]):
    """"""

    def __init__(self, property: PropertyAnalysis):
        """

        :param property:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: ContainerType) -> object:
        """

        :param value:
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
    def Write(self, collector: TraceLoggingDataCollector, value: ContainerType) -> None:
        """

        :param collector:
        :param value:
        """

class TimeSpanTypeInfo(TraceLoggingTypeInfo[TimeSpan]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[TimeSpan]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: TimeSpan) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class TraceLoggingDataCollector(Object):
    """"""

    @overload
    def AddArray(self, value: Array[bool]) -> None:
        """

        :param value:
        """
    @overload
    def AddArray(self, value: Array[Char]) -> None:
        """

        :param value:
        """
    @overload
    def AddArray(self, value: Array[float]) -> None:
        """

        :param value:
        """
    @overload
    def AddArray(self, value: Array[Guid]) -> None:
        """

        :param value:
        """
    @overload
    def AddArray(self, value: Array[int]) -> None:
        """

        :param value:
        """
    @overload
    def AddArray(self, value: Array[int]) -> None:
        """

        :param value:
        """
    @overload
    def AddArray(self, value: Array[int]) -> None:
        """

        :param value:
        """
    @overload
    def AddArray(self, value: Array[IntPtr]) -> None:
        """

        :param value:
        """
    @overload
    def AddArray(self, value: Array[int]) -> None:
        """

        :param value:
        """
    @overload
    def AddArray(self, value: Array[float]) -> None:
        """

        :param value:
        """
    @overload
    def AddArray(self, value: Array[int]) -> None:
        """

        :param value:
        """
    @overload
    def AddArray(self, value: Array[int]) -> None:
        """

        :param value:
        """
    @overload
    def AddArray(self, value: Array[int]) -> None:
        """

        :param value:
        """
    @overload
    def AddArray(self, value: Array[UIntPtr]) -> None:
        """

        :param value:
        """
    @overload
    def AddBinary(self, value: Array[int]) -> None:
        """

        :param value:
        """
    @overload
    def AddBinary(self, value: str) -> None:
        """

        :param value:
        """
    def AddCustom(self, value: Array[int]) -> None:
        """

        :param value:
        """
    def AddGroup(self) -> TraceLoggingDataCollector:
        """

        :return:
        """
    @overload
    def AddScalar(self, value: bool) -> None:
        """

        :param value:
        """
    @overload
    def AddScalar(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def AddScalar(self, value: Char) -> None:
        """

        :param value:
        """
    @overload
    def AddScalar(self, value: float) -> None:
        """

        :param value:
        """
    @overload
    def AddScalar(self, value: Guid) -> None:
        """

        :param value:
        """
    @overload
    def AddScalar(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def AddScalar(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def AddScalar(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def AddScalar(self, value: IntPtr) -> None:
        """

        :param value:
        """
    @overload
    def AddScalar(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def AddScalar(self, value: float) -> None:
        """

        :param value:
        """
    @overload
    def AddScalar(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def AddScalar(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def AddScalar(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def AddScalar(self, value: UIntPtr) -> None:
        """

        :param value:
        """
    def BeginBufferedArray(self) -> int:
        """

        :return:
        """
    def EndBufferedArray(self, bookmark: int, count: int) -> None:
        """

        :param bookmark:
        :param count:
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

class TraceLoggingDataType(Enum):
    """"""

    Nil: TraceLoggingDataType = ...
    """"""
    Utf16String: TraceLoggingDataType = ...
    """"""
    MbcsString: TraceLoggingDataType = ...
    """"""
    Int8: TraceLoggingDataType = ...
    """"""
    UInt8: TraceLoggingDataType = ...
    """"""
    Int16: TraceLoggingDataType = ...
    """"""
    UInt16: TraceLoggingDataType = ...
    """"""
    Int32: TraceLoggingDataType = ...
    """"""
    UInt32: TraceLoggingDataType = ...
    """"""
    Int64: TraceLoggingDataType = ...
    """"""
    UInt64: TraceLoggingDataType = ...
    """"""
    Float: TraceLoggingDataType = ...
    """"""
    Double: TraceLoggingDataType = ...
    """"""
    Boolean32: TraceLoggingDataType = ...
    """"""
    Binary: TraceLoggingDataType = ...
    """"""
    Guid: TraceLoggingDataType = ...
    """"""
    FileTime: TraceLoggingDataType = ...
    """"""
    SystemTime: TraceLoggingDataType = ...
    """"""
    HexInt32: TraceLoggingDataType = ...
    """"""
    HexInt64: TraceLoggingDataType = ...
    """"""
    CountedUtf16String: TraceLoggingDataType = ...
    """"""
    CountedMbcsString: TraceLoggingDataType = ...
    """"""
    Struct: TraceLoggingDataType = ...
    """"""
    Char8: TraceLoggingDataType = ...
    """"""
    Char16: TraceLoggingDataType = ...
    """"""
    Boolean8: TraceLoggingDataType = ...
    """"""
    HexInt8: TraceLoggingDataType = ...
    """"""
    HexInt16: TraceLoggingDataType = ...
    """"""
    Utf16Xml: TraceLoggingDataType = ...
    """"""
    MbcsXml: TraceLoggingDataType = ...
    """"""
    CountedUtf16Xml: TraceLoggingDataType = ...
    """"""
    CountedMbcsXml: TraceLoggingDataType = ...
    """"""
    Utf16Json: TraceLoggingDataType = ...
    """"""
    MbcsJson: TraceLoggingDataType = ...
    """"""
    CountedUtf16Json: TraceLoggingDataType = ...
    """"""
    CountedMbcsJson: TraceLoggingDataType = ...
    """"""
    HResult: TraceLoggingDataType = ...
    """"""

class TraceLoggingEventTypes(Object):
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class TraceLoggingMetadataCollector(Object):
    """"""

    def AddArray(self, name: str, type: TraceLoggingDataType) -> None:
        """

        :param name:
        :param type:
        """
    def AddBinary(self, name: str, type: TraceLoggingDataType) -> None:
        """

        :param name:
        :param type:
        """
    def AddCustom(self, name: str, type: TraceLoggingDataType, metadata: Array[int]) -> None:
        """

        :param name:
        :param type:
        :param metadata:
        """
    def AddGroup(self, name: str) -> TraceLoggingMetadataCollector:
        """

        :param name:
        :return:
        """
    def AddScalar(self, name: str, type: TraceLoggingDataType) -> None:
        """

        :param name:
        :param type:
        """
    def BeginBufferedArray(self) -> None:
        """"""
    def EndBufferedArray(self) -> None:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class TraceLoggingTypeInfo(ABC, Object):
    """"""

    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class TraceLoggingTypeInfo(ABC, Generic[DataType], TraceLoggingTypeInfo):
    """"""

    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[DataType]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: DataType) -> None:
        """

        :param collector:
        :param value:
        """
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class TypeAnalysis(Object):
    """"""

    def __init__(self, dataType: Type, eventAttrib: EventDataAttribute, recursionCheck: List[Type]):
        """

        :param dataType:
        :param eventAttrib:
        :param recursionCheck:
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

class UInt16ArrayTypeInfo(TraceLoggingTypeInfo[Array[UInt16]]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[Array[int]]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: int) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class UInt16TypeInfo(TraceLoggingTypeInfo[UInt16]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[int]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: int) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class UInt32ArrayTypeInfo(TraceLoggingTypeInfo[Array[UInt32]]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[Array[int]]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: int) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class UInt32TypeInfo(TraceLoggingTypeInfo[UInt32]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[int]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: int) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class UInt64ArrayTypeInfo(TraceLoggingTypeInfo[Array[UInt64]]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[Array[int]]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: int) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class UInt64TypeInfo(TraceLoggingTypeInfo[UInt64]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[int]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: int) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class UIntPtrArrayTypeInfo(TraceLoggingTypeInfo[Array[UIntPtr]]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[Array[UIntPtr]]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: UIntPtr) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """

class UIntPtrTypeInfo(TraceLoggingTypeInfo[UIntPtr]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[UIntPtr]:
        """

        :return:
        """
    @property
    def Keywords(self) -> EventKeywords:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Tags(self) -> EventTags:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetData(self, value: object) -> object:
        """

        :param value:
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
    def WriteData(self, collector: TraceLoggingDataCollector, value: UIntPtr) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """

        :param collector:
        :param name:
        :param format:
        """
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """

        :param collector:
        :param value:
        """
