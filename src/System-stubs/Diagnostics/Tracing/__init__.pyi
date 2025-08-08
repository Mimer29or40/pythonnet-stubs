"""Automatically generated stubs for C# namespace: System.Diagnostics.Tracing."""

from abc import ABC
from collections.abc import Iterator
from typing import ClassVar
from typing import Final
from typing import Self
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
from System import Nullable
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
from System.Collections.Generic import ICollection
from System.Collections.Generic import IDictionary
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEnumerator
from System.Collections.Generic import IList
from System.Collections.Generic import KeyValuePair
from System.Collections.Generic import List
from System.Collections.ObjectModel import ReadOnlyCollection
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

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

class ActivityFilter(Object, IDisposable):
    """"""
    @classmethod
    def DisableFilter(cls, filterList: ActivityFilter, source: EventSource) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FlowActivityIfNeeded(
        cls, filterList: ActivityFilter, currentActivityId: Guid, childActivityID: Guid
    ) -> None:
        """"""
    @classmethod
    def GetFilter(cls, filterList: ActivityFilter, source: EventSource) -> ActivityFilter:
        """"""
    def GetFilterAsTuple(self, sourceGuid: Guid) -> IEnumerable[Tuple[int, int]]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsCurrentActivityActive(cls, filterList: ActivityFilter) -> bool:
        """"""
    @classmethod
    def PassesActivityFilter(
        cls,
        filterList: ActivityFilter,
        childActivityID: Guid,
        triggeringEvent: bool,
        source: EventSource,
        eventId: int,
    ) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def UpdateFilter(
        cls,
        filterList: ActivityFilter,
        source: EventSource,
        perEventSourceSessionId: int,
        startEvents: str,
    ) -> None:
        """"""
    @classmethod
    def UpdateKwdTriggers(
        cls,
        activityFilter: ActivityFilter,
        sourceGuid: Guid,
        source: EventSource,
        sessKeywords: EventKeywords,
    ) -> None:
        """"""

class ActivityTracker(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @classmethod
    @property
    def Instance(cls) -> ActivityTracker:
        """"""
    def Enable(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def OnStart(
        self,
        providerName: str,
        activityName: str,
        task: int,
        activityId: Guid,
        relatedActivityId: Guid,
        options: EventActivityOptions,
    ) -> None:
        """"""
    def OnStop(self, providerName: str, activityName: str, task: int, activityId: Guid) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class ArrayTypeInfo[ElementType](TraceLoggingTypeInfo[Array[ElementType]]):
    """"""
    def __init__(self, elementInfo: TraceLoggingTypeInfo[ElementType]) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: ElementType) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class BooleanArrayTypeInfo(TraceLoggingTypeInfo[Array[Boolean]]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: Boolean) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class BooleanTypeInfo(TraceLoggingTypeInfo[Boolean]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: Boolean) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class ByteArrayTypeInfo(TraceLoggingTypeInfo[Array[Byte]]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: Byte) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class ByteTypeInfo(TraceLoggingTypeInfo[Byte]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: Byte) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class CharArrayTypeInfo(TraceLoggingTypeInfo[Array[Char]]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: Char) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class CharTypeInfo(TraceLoggingTypeInfo[Char]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: Char) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class ClassPropertyWriter[ContainerType, ValueType](PropertyAccessor[ContainerType]):
    """"""
    def __init__(self, property: PropertyAnalysis) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, container: ContainerType) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, collector: TraceLoggingDataCollector, container: ContainerType) -> None:
        """"""

class ConcurrentSetItem[KeyType, ItemType](ABC, Object):
    """"""
    @overload
    def Compare(self, other: ItemType) -> int:
        """"""
    @overload
    def Compare(self, key: KeyType) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ConcurrentSet[KeyType, ItemType](ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOrAdd(self, newItem: ItemType) -> ItemType:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def TryGet(self, key: KeyType) -> ItemType:
        """"""

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
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DateTimeOffsetTypeInfo(TraceLoggingTypeInfo[DateTimeOffset]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: DateTimeOffset) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class DateTimeTypeInfo(TraceLoggingTypeInfo[DateTime]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: DateTime) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class DecimalTypeInfo(TraceLoggingTypeInfo[Decimal]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: Decimal) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class DoubleArrayTypeInfo(TraceLoggingTypeInfo[Array[Double]]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: Double) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class DoubleTypeInfo(TraceLoggingTypeInfo[Double]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: Double) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class EmptyStruct(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EnumByteTypeInfo[EnumType](TraceLoggingTypeInfo[EnumType]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: EnumType) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class EnumHelper[UnderlyingType](ABC, Object):
    """"""
    @classmethod
    def Cast[ValueType](cls, value: ValueType) -> UnderlyingType:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EnumInt16TypeInfo[EnumType](TraceLoggingTypeInfo[EnumType]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: EnumType) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class EnumInt32TypeInfo[EnumType](TraceLoggingTypeInfo[EnumType]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: EnumType) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class EnumInt64TypeInfo[EnumType](TraceLoggingTypeInfo[EnumType]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: EnumType) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class EnumSByteTypeInfo[EnumType](TraceLoggingTypeInfo[EnumType]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: EnumType) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class EnumUInt16TypeInfo[EnumType](TraceLoggingTypeInfo[EnumType]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: EnumType) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class EnumUInt32TypeInfo[EnumType](TraceLoggingTypeInfo[EnumType]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: EnumType) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class EnumUInt64TypeInfo[EnumType](TraceLoggingTypeInfo[EnumType]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: EnumType) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class EnumerableTypeInfo[IterableType, ElementType](TraceLoggingTypeInfo[IterableType]):
    """"""
    def __init__(self, elementInfo: TraceLoggingTypeInfo[ElementType]) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: IterableType) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class EtwSession(Object):
    """"""

    m_activityFilter: Final[ActivityFilter]
    """"""
    m_etwSessionId: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetEtwSession(cls, etwSessionId: int, bCreateIfNeeded: bool = ...) -> EtwSession:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def RemoveEtwSession(cls, etwSession: EtwSession) -> None:
        """"""
    def ToString(self) -> str:
        """"""

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
    def __init__(self, eventId: int) -> None:
        """"""
    @property
    def ActivityOptions(self) -> EventActivityOptions:
        """"""
    @ActivityOptions.setter
    def ActivityOptions(self, value: EventActivityOptions) -> None: ...
    @property
    def Channel(self) -> EventChannel:
        """"""
    @Channel.setter
    def Channel(self, value: EventChannel) -> None: ...
    @property
    def EventId(self) -> int:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @Keywords.setter
    def Keywords(self, value: EventKeywords) -> None: ...
    @property
    def Level(self) -> EventLevel:
        """"""
    @Level.setter
    def Level(self, value: EventLevel) -> None: ...
    @property
    def Message(self) -> str:
        """"""
    @Message.setter
    def Message(self, value: str) -> None: ...
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @Opcode.setter
    def Opcode(self, value: EventOpcode) -> None: ...
    @property
    def Tags(self) -> EventTags:
        """"""
    @Tags.setter
    def Tags(self, value: EventTags) -> None: ...
    @property
    def Task(self) -> EventTask:
        """"""
    @Task.setter
    def Task(self, value: EventTask) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Version(self) -> int:
        """"""
    @Version.setter
    def Version(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
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
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

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
    def __init__(self) -> None:
        """"""
    @property
    def Enabled(self) -> bool:
        """"""
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
    @property
    def EventChannelType(self) -> EventChannelType:
        """"""
    @EventChannelType.setter
    def EventChannelType(self, value: EventChannelType) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
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
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

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
        """"""
    @property
    def Command(self) -> EventCommand:
        """"""
    def DisableEvent(self, eventId: int) -> bool:
        """"""
    def EnableEvent(self, eventId: int) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EventDataAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
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
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class EventDescriptor(ValueType):
    """"""
    @overload
    def __init__(self, traceloggingId: int, level: int, opcode: int, keywords: int) -> None:
        """"""
    @overload
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
    @overload
    def Equals(self, other: EventDescriptor) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, event1: EventDescriptor, event2: EventDescriptor) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, event1: EventDescriptor, event2: EventDescriptor) -> bool:
        """"""
    def __eq__(self, other: EventDescriptor) -> bool:
        """"""
    def __ne__(self, other: EventDescriptor) -> bool:
        """"""

class EventDispatcher(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EventFieldAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Format(self) -> EventFieldFormat:
        """"""
    @Format.setter
    def Format(self, value: EventFieldFormat) -> None: ...
    @property
    def Tags(self) -> EventFieldTags:
        """"""
    @Tags.setter
    def Tags(self, value: EventFieldTags) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
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
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

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
    def __init__(self) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
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
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

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
    def __init__(self) -> None:
        """"""
    def DisableEvents(self, eventSource: EventSource) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    @overload
    def EnableEvents(self, eventSource: EventSource, level: EventLevel) -> None:
        """"""
    @overload
    def EnableEvents(
        self, eventSource: EventSource, level: EventLevel, matchAnyKeyword: EventKeywords
    ) -> None:
        """"""
    @overload
    def EnableEvents(
        self,
        eventSource: EventSource,
        level: EventLevel,
        matchAnyKeyword: EventKeywords,
        arguments: IDictionary[str, str],
    ) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def EventSourceIndex(cls, eventSource: EventSource) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
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
    ICollection[KeyValuePair[String, Object]],
    IDictionary[String, Object],
    IEnumerable[KeyValuePair[String, Object]],
    IEnumerable,
):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection[str]:
        """"""
    @property
    def Values(self) -> ICollection[object]:
        """"""
    @overload
    def Add(self, payloadEntry: KeyValuePair[str, object]) -> None:
        """"""
    @overload
    def Add(self, key: str, value: object) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, entry: KeyValuePair[str, object]) -> bool:
        """"""
    def ContainsKey(self, key: str) -> bool:
        """"""
    def CopyTo(self, payloadEntries: Array[KeyValuePair[str, object]], count: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[KeyValuePair[str, object]]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Remove(self, entry: KeyValuePair[str, object]) -> bool:
        """"""
    @overload
    def Remove(self, key: str) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def TryGetValue(self, key: str, value: Object) -> tuple[bool, Object]:
        """"""
    @overload
    def __contains__(self, entry: KeyValuePair[str, object]) -> bool:
        """"""
    @overload
    def __contains__(self, key: str) -> bool:
        """"""
    def __iter__(self) -> Iterator[KeyValuePair[str, object]]:
        """"""
    @overload
    def __delitem__(self, entry: KeyValuePair[str, object]) -> bool:
        """"""
    @overload
    def __delitem__(self, key: str) -> bool:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, key: str) -> object:
        """"""
    def __setitem__(self, key: str, value: object) -> None:
        """"""

class EventProvider(Object, IDisposable):
    """"""
    def Close(self) -> None:
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
    def ToString(self) -> str:
        """"""
    class EventData(ValueType):
        """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""

    class SessionInfo(ValueType):
        """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""

    class WriteEventErrorCode(Enum):
        """"""

        NoError: EventProvider.WriteEventErrorCode = ...
        """"""
        NoFreeBuffers: EventProvider.WriteEventErrorCode = ...
        """"""
        EventTooBig: EventProvider.WriteEventErrorCode = ...
        """"""
        NullInput: EventProvider.WriteEventErrorCode = ...
        """"""
        TooManyArgs: EventProvider.WriteEventErrorCode = ...
        """"""
        Other: EventProvider.WriteEventErrorCode = ...
        """"""

class EventSource(Object, IDisposable):
    """"""
    @overload
    def __init__(self, eventSourceName: str) -> None:
        """"""
    @overload
    def __init__(self, eventSourceName: str, config: EventSourceSettings) -> None:
        """"""
    @overload
    def __init__(
        self, eventSourceName: str, config: EventSourceSettings, traits: Array[str]
    ) -> None:
        """"""
    @property
    def ConstructionException(self) -> Exception:
        """"""
    @classmethod
    @property
    def CurrentThreadActivityId(cls) -> Guid:
        """"""
    @property
    def Guid(self) -> Guid:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Settings(self) -> EventSourceSettings:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def GenerateManifest(cls, eventSourceType: Type, assemblyPathToIncludeInManifest: str) -> str:
        """"""
    @classmethod
    @overload
    def GenerateManifest(
        cls,
        eventSourceType: Type,
        assemblyPathToIncludeInManifest: str,
        flags: EventManifestOptions,
    ) -> str:
        """"""
    @classmethod
    def GetGuid(cls, eventSourceType: Type) -> Guid:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetName(cls, eventSourceType: Type) -> str:
        """"""
    @classmethod
    def GetSources(cls) -> IEnumerable[EventSource]:
        """"""
    def GetTrait(self, key: str) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsEnabled(self) -> bool:
        """"""
    @overload
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords) -> bool:
        """"""
    @overload
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords, channel: EventChannel) -> bool:
        """"""
    @classmethod
    def SendCommand(
        cls,
        eventSource: EventSource,
        command: EventCommand,
        commandArguments: IDictionary[str, str],
    ) -> None:
        """"""
    @classmethod
    @overload
    def SetCurrentThreadActivityId(cls, activityId: Guid) -> None:
        """"""
    @classmethod
    @overload
    def SetCurrentThreadActivityId(
        cls, activityId: Guid, oldActivityThatWillContinue: Guid
    ) -> tuple[None, Guid]:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Write(self, eventName: str) -> None:
        """"""
    @overload
    def Write[T](self, eventName: str, data: T) -> None:
        """"""
    @overload
    def Write(self, eventName: str, options: EventSourceOptions, data: T) -> None:
        """"""
    @overload
    def Write(
        self,
        eventName: str,
        options: EventSourceOptions,
        activityId: Guid,
        relatedActivityId: Guid,
        data: T,
    ) -> None:
        """"""
    @overload
    def Write(self, eventName: str, options: EventSourceOptions) -> None:
        """"""
    @overload
    def Write[T](self, eventName: str, options: EventSourceOptions, data: T) -> None:
        """"""
    EventCommandExecuted: EventType[EventHandler[EventCommandEventArgs]] = ...
    """"""

class EventSourceActivity(Object, IDisposable):
    """"""
    def __init__(self, eventSource: EventSource) -> None:
        """"""
    @property
    def EventSource(self) -> EventSource:
        """"""
    @property
    def Id(self) -> Guid:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Start(self, eventName: str) -> EventSourceActivity:
        """"""
    @overload
    def Start[T](self, eventName: str, data: T) -> EventSourceActivity:
        """"""
    @overload
    def Start(self, eventName: str, options: EventSourceOptions) -> EventSourceActivity:
        """"""
    @overload
    def Start[T](self, eventName: str, options: EventSourceOptions, data: T) -> EventSourceActivity:
        """"""
    @overload
    def Stop[T](self, data: T) -> None:
        """"""
    @overload
    def Stop(self, eventName: str) -> None:
        """"""
    @overload
    def Stop[T](self, eventName: str, data: T) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Write[T](
        self, source: EventSource, eventName: str, options: EventSourceOptions, data: T
    ) -> None:
        """"""
    @overload
    def Write(self, eventName: str) -> None:
        """"""
    @overload
    def Write[T](self, eventName: str, data: T) -> None:
        """"""
    @overload
    def Write(self, eventName: str, options: EventSourceOptions) -> None:
        """"""
    @overload
    def Write[T](self, eventName: str, options: EventSourceOptions, data: T) -> None:
        """"""
    @classmethod
    def op_Implicit(cls, eventSource: EventSource) -> EventSourceActivity:
        """"""

class EventSourceAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Guid(self) -> str:
        """"""
    @Guid.setter
    def Guid(self, value: str) -> None: ...
    @property
    def LocalizationResources(self) -> str:
        """"""
    @LocalizationResources.setter
    def LocalizationResources(self, value: str) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
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
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class EventSourceCreatedEventArgs(EventArgs):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def EventSource(self) -> EventSource:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EventSourceException(Exception, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def HResult(self) -> int:
        """"""
    @property
    def HelpLink(self) -> str:
        """"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """"""
    @property
    def TargetSite(self) -> MethodBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EventSourceOptions(ValueType):
    """"""
    @property
    def ActivityOptions(self) -> EventActivityOptions:
        """"""
    @ActivityOptions.setter
    def ActivityOptions(self, value: EventActivityOptions) -> None: ...
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @Keywords.setter
    def Keywords(self, value: EventKeywords) -> None: ...
    @property
    def Level(self) -> EventLevel:
        """"""
    @Level.setter
    def Level(self, value: EventLevel) -> None: ...
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @Opcode.setter
    def Opcode(self, value: EventOpcode) -> None: ...
    @property
    def Tags(self) -> EventTags:
        """"""
    @Tags.setter
    def Tags(self, value: EventTags) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

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
        """"""
    @property
    def Channel(self) -> EventChannel:
        """"""
    @property
    def EventId(self) -> int:
        """"""
    @property
    def EventName(self) -> str:
        """"""
    @property
    def EventSource(self) -> EventSource:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Payload(self) -> ReadOnlyCollection[object]:
        """"""
    @property
    def PayloadNames(self) -> ReadOnlyCollection[str]:
        """"""
    @property
    def RelatedActivityId(self) -> Guid:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    @property
    def Task(self) -> EventTask:
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

class FieldMetadata(Object):
    """"""
    @overload
    def __init__(
        self, name: str, type: TraceLoggingDataType, tags: EventFieldTags, variableCount: bool
    ) -> None:
        """"""
    @overload
    def __init__(
        self, name: str, type: TraceLoggingDataType, tags: EventFieldTags, fixedCount: int
    ) -> None:
        """"""
    @overload
    def __init__(
        self, name: str, type: TraceLoggingDataType, tags: EventFieldTags, custom: Array[int]
    ) -> None:
        """"""
    def Encode(self, pos: Int32, metadata: Array[int]) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IncrementStructFieldCount(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class FrameworkEventSource(EventSource, IDisposable):
    """"""

    Log: ClassVar[FrameworkEventSource]
    """"""
    @property
    def ConstructionException(self) -> Exception:
        """"""
    @property
    def Guid(self) -> Guid:
        """"""
    @classmethod
    @property
    def IsInitialized(cls) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Settings(self) -> EventSourceSettings:
        """"""
    def BeginGetRequestStream(self, id: object, uri: str, success: bool, synchronous: bool) -> None:
        """"""
    def BeginGetResponse(self, id: object, uri: str, success: bool, synchronous: bool) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndGetRequestStream(self, id: object, success: bool, synchronous: bool) -> None:
        """"""
    def EndGetResponse(self, id: object, success: bool, synchronous: bool, statusCode: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTrait(self, key: str) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsEnabled(self) -> bool:
        """"""
    @overload
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords) -> bool:
        """"""
    @overload
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords, channel: EventChannel) -> bool:
        """"""
    @overload
    def ResourceManagerAddingCultureFromConfigFile(
        self, baseName: str, mainAssembly: Assembly, cultureName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerAddingCultureFromConfigFile(
        self, baseName: str, mainAssemblyName: str, cultureName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerCaseInsensitiveResourceStreamLookupFailed(
        self, baseName: str, mainAssembly: Assembly, assemblyName: str, resourceFileName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerCaseInsensitiveResourceStreamLookupFailed(
        self, baseName: str, mainAssemblyName: str, assemblyName: str, resourceFileName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerCaseInsensitiveResourceStreamLookupSucceeded(
        self, baseName: str, mainAssembly: Assembly, assemblyName: str, resourceFileName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerCaseInsensitiveResourceStreamLookupSucceeded(
        self, baseName: str, mainAssemblyName: str, assemblyName: str, resourceFileName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerCreatingResourceSet(
        self, baseName: str, mainAssembly: Assembly, cultureName: str, fileName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerCreatingResourceSet(
        self, baseName: str, mainAssemblyName: str, cultureName: str, fileName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerCultureFoundInConfigFile(
        self, baseName: str, mainAssembly: Assembly, cultureName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerCultureFoundInConfigFile(
        self, baseName: str, mainAssemblyName: str, cultureName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerCultureNotFoundInConfigFile(
        self, baseName: str, mainAssembly: Assembly, cultureName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerCultureNotFoundInConfigFile(
        self, baseName: str, mainAssemblyName: str, cultureName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerFoundResourceSetInCache(
        self, baseName: str, mainAssembly: Assembly, cultureName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerFoundResourceSetInCache(
        self, baseName: str, mainAssemblyName: str, cultureName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerFoundResourceSetInCacheUnexpected(
        self, baseName: str, mainAssembly: Assembly, cultureName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerFoundResourceSetInCacheUnexpected(
        self, baseName: str, mainAssemblyName: str, cultureName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerGetSatelliteAssemblyFailed(
        self, baseName: str, mainAssembly: Assembly, cultureName: str, assemblyName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerGetSatelliteAssemblyFailed(
        self, baseName: str, mainAssemblyName: str, cultureName: str, assemblyName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerGetSatelliteAssemblySucceeded(
        self, baseName: str, mainAssembly: Assembly, cultureName: str, assemblyName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerGetSatelliteAssemblySucceeded(
        self, baseName: str, mainAssemblyName: str, cultureName: str, assemblyName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerLookingForResourceSet(
        self, baseName: str, mainAssembly: Assembly, cultureName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerLookingForResourceSet(
        self, baseName: str, mainAssemblyName: str, cultureName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerLookupFailed(
        self, baseName: str, mainAssembly: Assembly, cultureName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerLookupFailed(
        self, baseName: str, mainAssemblyName: str, cultureName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerLookupStarted(
        self, baseName: str, mainAssembly: Assembly, cultureName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerLookupStarted(
        self, baseName: str, mainAssemblyName: str, cultureName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerManifestResourceAccessDenied(
        self, baseName: str, mainAssembly: Assembly, assemblyName: str, canonicalName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerManifestResourceAccessDenied(
        self, baseName: str, mainAssemblyName: str, assemblyName: str, canonicalName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerNeutralResourceAttributeMissing(self, mainAssembly: Assembly) -> None:
        """"""
    @overload
    def ResourceManagerNeutralResourceAttributeMissing(self, mainAssemblyName: str) -> None:
        """"""
    @overload
    def ResourceManagerNeutralResourcesFound(
        self, baseName: str, mainAssembly: Assembly, resName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerNeutralResourcesFound(
        self, baseName: str, mainAssemblyName: str, resName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerNeutralResourcesNotFound(
        self, baseName: str, mainAssembly: Assembly, resName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerNeutralResourcesNotFound(
        self, baseName: str, mainAssemblyName: str, resName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerNeutralResourcesSufficient(
        self, baseName: str, mainAssembly: Assembly, cultureName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerNeutralResourcesSufficient(
        self, baseName: str, mainAssemblyName: str, cultureName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerNotCreatingResourceSet(
        self, baseName: str, mainAssembly: Assembly, cultureName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerNotCreatingResourceSet(
        self, baseName: str, mainAssemblyName: str, cultureName: str
    ) -> None:
        """"""
    @overload
    def ResourceManagerReleasingResources(self, baseName: str, mainAssembly: Assembly) -> None:
        """"""
    @overload
    def ResourceManagerReleasingResources(self, baseName: str, mainAssemblyName: str) -> None:
        """"""
    @overload
    def ResourceManagerStreamFound(
        self,
        baseName: str,
        mainAssembly: Assembly,
        cultureName: str,
        loadedAssembly: Assembly,
        resourceFileName: str,
    ) -> None:
        """"""
    @overload
    def ResourceManagerStreamFound(
        self,
        baseName: str,
        mainAssemblyName: str,
        cultureName: str,
        loadedAssemblyName: str,
        resourceFileName: str,
    ) -> None:
        """"""
    @overload
    def ResourceManagerStreamNotFound(
        self,
        baseName: str,
        mainAssembly: Assembly,
        cultureName: str,
        loadedAssembly: Assembly,
        resourceFileName: str,
    ) -> None:
        """"""
    @overload
    def ResourceManagerStreamNotFound(
        self,
        baseName: str,
        mainAssemblyName: str,
        cultureName: str,
        loadedAssemblyName: str,
        resourceFileName: str,
    ) -> None:
        """"""
    def ThreadPoolDequeueWork(self, workID: int) -> None:
        """"""
    def ThreadPoolDequeueWorkObject(self, workID: object) -> None:
        """"""
    def ThreadPoolEnqueueWork(self, workID: int) -> None:
        """"""
    def ThreadPoolEnqueueWorkObject(self, workID: object) -> None:
        """"""
    def ThreadTransferReceive(self, id: int, kind: int, info: str) -> None:
        """"""
    def ThreadTransferReceiveHandled(self, id: int, kind: int, info: str) -> None:
        """"""
    def ThreadTransferReceiveHandledObj(self, id: object, kind: int, info: str) -> None:
        """"""
    def ThreadTransferReceiveObj(self, id: object, kind: int, info: str) -> None:
        """"""
    def ThreadTransferSend(self, id: int, kind: int, info: str, multiDequeues: bool) -> None:
        """"""
    def ThreadTransferSendObj(self, id: object, kind: int, info: str, multiDequeues: bool) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Write(self, eventName: str) -> None:
        """"""
    @overload
    def Write[T](self, eventName: str, data: T) -> None:
        """"""
    @overload
    def Write(self, eventName: str, options: EventSourceOptions, data: T) -> None:
        """"""
    @overload
    def Write(
        self,
        eventName: str,
        options: EventSourceOptions,
        activityId: Guid,
        relatedActivityId: Guid,
        data: T,
    ) -> None:
        """"""
    @overload
    def Write(self, eventName: str, options: EventSourceOptions) -> None:
        """"""
    @overload
    def Write[T](self, eventName: str, options: EventSourceOptions, data: T) -> None:
        """"""
    EventCommandExecuted: EventType[EventHandler[EventCommandEventArgs]] = ...
    """"""
    class Keywords(ABC, Object):
        """"""

        DynamicTypeUsage: ClassVar[EventKeywords]
        """"""
        Loader: ClassVar[EventKeywords]
        """"""
        NetClient: ClassVar[EventKeywords]
        """"""
        ThreadPool: ClassVar[EventKeywords]
        """"""
        ThreadTransfer: ClassVar[EventKeywords]
        """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""

    class Opcodes(ABC, Object):
        """"""

        ReceiveHandled: ClassVar[EventOpcode]
        """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""

    class Tasks(ABC, Object):
        """"""

        GetRequestStream: ClassVar[EventTask]
        """"""
        GetResponse: ClassVar[EventTask]
        """"""
        ThreadTransfer: ClassVar[EventTask]
        """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""

class GuidArrayTypeInfo(TraceLoggingTypeInfo[Array[Guid]]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: Guid) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class GuidTypeInfo(TraceLoggingTypeInfo[Guid]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: Guid) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class Int16ArrayTypeInfo(TraceLoggingTypeInfo[Array[Int16]]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: Int16) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class Int16TypeInfo(TraceLoggingTypeInfo[Int16]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: Int16) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class Int32ArrayTypeInfo(TraceLoggingTypeInfo[Array[Int32]]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: Int32) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class Int32TypeInfo(TraceLoggingTypeInfo[Int32]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: Int32) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class Int64ArrayTypeInfo(TraceLoggingTypeInfo[Array[Int64]]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: Int64) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class Int64TypeInfo(TraceLoggingTypeInfo[Int64]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: Int64) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class IntPtrArrayTypeInfo(TraceLoggingTypeInfo[Array[IntPtr]]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: IntPtr) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class IntPtrTypeInfo(TraceLoggingTypeInfo[IntPtr]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: IntPtr) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class InvokeTypeInfo[ContainerType](TraceLoggingTypeInfo[ContainerType]):
    """"""
    def __init__(self, typeAnalysis: TypeAnalysis) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: ContainerType) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, valueObj: object) -> None:
        """"""

class KeyValuePairTypeInfo[K, V](TraceLoggingTypeInfo[KeyValuePair[K, V]]):
    """"""
    def __init__(self, recursionCheck: List[Type]) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData[K, V](
        self, collector: TraceLoggingDataCollector, value: KeyValuePair[K, V]
    ) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class ManifestBuilder(Object):
    """"""
    def __init__(
        self,
        providerName: str,
        providerGuid: Guid,
        dllName: str,
        resources: ResourceManager,
        flags: EventManifestOptions,
    ) -> None:
        """"""
    @property
    def Errors(self) -> IList[str]:
        """"""
    def AddChannel(self, name: str, value: int, channelAttribute: EventChannelAttribute) -> None:
        """"""
    def AddEventParameter(self, type: Type, name: str) -> None:
        """"""
    def AddKeyword(self, name: str, value: int) -> None:
        """"""
    def AddOpcode(self, name: str, value: int) -> None:
        """"""
    def AddTask(self, name: str, value: int) -> None:
        """"""
    def CreateManifest(self) -> Array[int]:
        """"""
    def EndEvent(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetChannelData(self) -> Array[int]:
        """"""
    def GetChannelKeyword(self, channel: EventChannel) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ManifestError(self, msg: str, runtimeCritical: bool = ...) -> None:
        """"""
    def StartEvent(self, eventName: str, eventAttribute: EventAttribute) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class ManifestEnvelope(ValueType):
    """"""

    ChunkNumber: Final[int]
    """"""
    Format: Final[ManifestEnvelope.ManifestFormats]
    """"""
    Magic: Final[int]
    """"""
    MajorVersion: Final[int]
    """"""
    MaxChunkSize: ClassVar[int]
    """"""
    MinorVersion: Final[int]
    """"""
    TotalChunks: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    class ManifestFormats(Enum):
        """"""

        SimpleXmlFormat: ManifestEnvelope.ManifestFormats = ...
        """"""

class NameInfo(ConcurrentSetItem[KeyValuePair[String, EventTags], NameInfo]):
    """"""
    def __init__(self, name: str, tags: EventTags, typeMetadataSize: int) -> None:
        """"""
    @overload
    def Compare(self, key: KeyValuePair[str, EventTags]) -> int:
        """"""
    @overload
    def Compare(self, other: NameInfo) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NonEventAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
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
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class NonGenericProperytWriter[ContainerType](PropertyAccessor[ContainerType]):
    """"""
    def __init__(self, property: PropertyAnalysis) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, container: ContainerType) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, collector: TraceLoggingDataCollector, container: ContainerType) -> None:
        """"""

class NullTypeInfo[DataType](TraceLoggingTypeInfo[DataType]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: DataType) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class NullableTypeInfo[T](TraceLoggingTypeInfo[T | None]):
    """"""
    def __init__(self, recursionCheck: List[Type]) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData[T](self, collector: TraceLoggingDataCollector, value: Nullable[T]) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class PropertyAccessor[ContainerType](ABC, Object):
    """"""
    @classmethod
    def Create(cls, property: PropertyAnalysis) -> PropertyAccessor[ContainerType]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: ContainerType) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, collector: TraceLoggingDataCollector, value: ContainerType) -> None:
        """"""

class PropertyAnalysis(Object):
    """"""
    def __init__(
        self,
        name: str,
        getterInfo: MethodInfo,
        typeInfo: TraceLoggingTypeInfo,
        fieldAttribute: EventFieldAttribute,
    ) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SByteArrayTypeInfo(TraceLoggingTypeInfo[Array[SByte]]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: SByte) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class SByteTypeInfo(TraceLoggingTypeInfo[SByte]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: SByte) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class SessionMask(ValueType):
    """"""
    @overload
    def __init__(self, m: SessionMask) -> None:
        """"""
    @overload
    def __init__(self, mask: int = ...) -> None:
        """"""
    @classmethod
    @property
    def All(cls) -> SessionMask:
        """"""
    @property
    def Item(self) -> bool:
        """"""
    @Item.setter
    def Item(self, value: bool) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FromEventKeywords(cls, m: int) -> SessionMask:
        """"""
    @classmethod
    def FromId(cls, perEventSourceSessionId: int) -> SessionMask:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsEqualOrSupersetOf(self, m: SessionMask) -> bool:
        """"""
    def ToEventKeywords(self) -> int:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_BitwiseAnd(cls, m1: SessionMask, m2: SessionMask) -> SessionMask:
        """"""
    @classmethod
    def op_BitwiseOr(cls, m1: SessionMask, m2: SessionMask) -> SessionMask:
        """"""
    @classmethod
    def op_ExclusiveOr(cls, m1: SessionMask, m2: SessionMask) -> SessionMask:
        """"""
    @classmethod
    def op_Explicit(cls, m: SessionMask) -> int:
        """"""
    @classmethod
    def op_OnesComplement(cls, m: SessionMask) -> SessionMask:
        """"""
    def __getitem__(self, perEventSourceSessionId: int) -> bool:
        """"""
    def __and__(self, other: SessionMask) -> SessionMask:
        """"""
    def __or__(self, other: SessionMask) -> SessionMask:
        """"""
    def __xor__(self, other: SessionMask) -> SessionMask:
        """"""
    def __invert__(self) -> SessionMask:
        """"""
    def __setitem__(self, perEventSourceSessionId: int, value: bool) -> None:
        """"""

class SimpleEventTypes[T](TraceLoggingEventTypes):
    """"""
    @classmethod
    @property
    def Instance(cls) -> SimpleEventTypes[T]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SingleArrayTypeInfo(TraceLoggingTypeInfo[Array[Single]]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: Single) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class SingleTypeInfo(TraceLoggingTypeInfo[Single]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: Single) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class Statics(ABC, Object):
    """"""

    DefaultLevel: ClassVar[int]
    """"""
    EventTagsMask: ClassVar[EventTags]
    """"""
    HexIntPtrType: ClassVar[TraceLoggingDataType]
    """"""
    InTypeChainFlag: ClassVar[int]
    """"""
    InTypeCountMask: ClassVar[int]
    """"""
    InTypeCustomCountFlag: ClassVar[int]
    """"""
    InTypeFixedCountFlag: ClassVar[int]
    """"""
    InTypeMask: ClassVar[int]
    """"""
    InTypeVariableCountFlag: ClassVar[int]
    """"""
    IntPtrType: ClassVar[TraceLoggingDataType]
    """"""
    OutTypeChainFlag: ClassVar[int]
    """"""
    OutTypeMask: ClassVar[int]
    """"""
    TraceLoggingChannel: ClassVar[int]
    """"""
    UIntPtrType: ClassVar[TraceLoggingDataType]
    """"""
    @classmethod
    def CheckName(cls, name: str) -> None:
        """"""
    @classmethod
    @overload
    def Combine(cls, settingValue: int, defaultValue: int) -> int:
        """"""
    @classmethod
    @overload
    def Combine(cls, settingValue1: int, settingValue2: int) -> int:
        """"""
    @classmethod
    @overload
    def Combine(cls, settingValue1: int, settingValue2: int, defaultValue: int) -> int:
        """"""
    @classmethod
    def CreateDefaultTypeInfo[DataType](
        cls, recursionCheck: List[Type]
    ) -> TraceLoggingTypeInfo[DataType]:
        """"""
    @classmethod
    def CreateDelegate(cls, delegateType: Type, methodInfo: MethodInfo) -> Delegate:
        """"""
    @classmethod
    def CreateInstance(cls, type: Type, parameters: Array[object]) -> object:
        """"""
    @classmethod
    def EncodeTags(cls, tags: int, pos: Int32, metadata: Array[int]) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FindEnumerableElementType(cls, type: Type) -> Type:
        """"""
    @classmethod
    def Format16(
        cls, format: EventFieldFormat, native: TraceLoggingDataType
    ) -> TraceLoggingDataType:
        """"""
    @classmethod
    def Format32(
        cls, format: EventFieldFormat, native: TraceLoggingDataType
    ) -> TraceLoggingDataType:
        """"""
    @classmethod
    def Format64(
        cls, format: EventFieldFormat, native: TraceLoggingDataType
    ) -> TraceLoggingDataType:
        """"""
    @classmethod
    def Format8(
        cls, format: EventFieldFormat, native: TraceLoggingDataType
    ) -> TraceLoggingDataType:
        """"""
    @classmethod
    def FormatPtr(
        cls, format: EventFieldFormat, native: TraceLoggingDataType
    ) -> TraceLoggingDataType:
        """"""
    @classmethod
    @overload
    def GetCustomAttribute[AttributeType](cls, propInfo: PropertyInfo) -> AttributeType:
        """"""
    @classmethod
    @overload
    def GetCustomAttribute[AttributeType](cls, type: Type) -> AttributeType:
        """"""
    @classmethod
    def GetDeclaredStaticMethod(cls, declaringType: Type, name: str) -> MethodInfo:
        """"""
    @classmethod
    def GetGenericArguments(cls, type: Type) -> Array[Type]:
        """"""
    @classmethod
    def GetGetMethod(cls, propInfo: PropertyInfo) -> MethodInfo:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetProperties(cls, type: Type) -> IEnumerable[PropertyInfo]:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetTypeInfoInstance(
        cls, dataType: Type, recursionCheck: List[Type]
    ) -> TraceLoggingTypeInfo:
        """"""
    @classmethod
    def HasCustomAttribute(cls, propInfo: PropertyInfo, attributeType: Type) -> bool:
        """"""
    @classmethod
    def IsEnum(cls, type: Type) -> bool:
        """"""
    @classmethod
    def IsGenericMatch(cls, type: Type, openType: object) -> bool:
        """"""
    @classmethod
    def IsValueType(cls, type: Type) -> bool:
        """"""
    @classmethod
    def MakeDataType(
        cls, baseType: TraceLoggingDataType, format: EventFieldFormat
    ) -> TraceLoggingDataType:
        """"""
    @classmethod
    def MetadataForString(
        cls, name: str, prefixSize: int, suffixSize: int, additionalSize: int
    ) -> Array[int]:
        """"""
    @classmethod
    def ShouldOverrideFieldName(cls, fieldName: str) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class StringTypeInfo(TraceLoggingTypeInfo[String]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: String) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class StructPropertyWriter[ContainerType, ValueType](PropertyAccessor[ContainerType]):
    """"""
    def __init__(self, property: PropertyAnalysis) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, container: ContainerType) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, collector: TraceLoggingDataCollector, container: ContainerType) -> None:
        """"""

class TimeSpanTypeInfo(TraceLoggingTypeInfo[TimeSpan]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: TimeSpan) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class TraceLoggingDataCollector(Object):
    """"""
    @overload
    def AddArray(self, value: Array[bool]) -> None:
        """"""
    @overload
    def AddArray(self, value: Array[Char]) -> None:
        """"""
    @overload
    def AddArray(self, value: Array[float]) -> None:
        """"""
    @overload
    def AddArray(self, value: Array[Guid]) -> None:
        """"""
    @overload
    def AddArray(self, value: Array[int]) -> None:
        """"""
    @overload
    def AddArray(self, value: Array[int]) -> None:
        """"""
    @overload
    def AddArray(self, value: Array[int]) -> None:
        """"""
    @overload
    def AddArray(self, value: Array[IntPtr]) -> None:
        """"""
    @overload
    def AddArray(self, value: Array[int]) -> None:
        """"""
    @overload
    def AddArray(self, value: Array[float]) -> None:
        """"""
    @overload
    def AddArray(self, value: Array[int]) -> None:
        """"""
    @overload
    def AddArray(self, value: Array[int]) -> None:
        """"""
    @overload
    def AddArray(self, value: Array[int]) -> None:
        """"""
    @overload
    def AddArray(self, value: Array[UIntPtr]) -> None:
        """"""
    @overload
    def AddBinary(self, value: Array[int]) -> None:
        """"""
    @overload
    def AddBinary(self, value: str) -> None:
        """"""
    def AddCustom(self, value: Array[int]) -> None:
        """"""
    def AddGroup(self) -> TraceLoggingDataCollector:
        """"""
    @overload
    def AddScalar(self, value: bool) -> None:
        """"""
    @overload
    def AddScalar(self, value: int) -> None:
        """"""
    @overload
    def AddScalar(self, value: Char) -> None:
        """"""
    @overload
    def AddScalar(self, value: float) -> None:
        """"""
    @overload
    def AddScalar(self, value: Guid) -> None:
        """"""
    @overload
    def AddScalar(self, value: int) -> None:
        """"""
    @overload
    def AddScalar(self, value: int) -> None:
        """"""
    @overload
    def AddScalar(self, value: int) -> None:
        """"""
    @overload
    def AddScalar(self, value: IntPtr) -> None:
        """"""
    @overload
    def AddScalar(self, value: int) -> None:
        """"""
    @overload
    def AddScalar(self, value: float) -> None:
        """"""
    @overload
    def AddScalar(self, value: int) -> None:
        """"""
    @overload
    def AddScalar(self, value: int) -> None:
        """"""
    @overload
    def AddScalar(self, value: int) -> None:
        """"""
    @overload
    def AddScalar(self, value: UIntPtr) -> None:
        """"""
    def BeginBufferedArray(self) -> int:
        """"""
    def EndBufferedArray(self, bookmark: int, count: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

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
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TraceLoggingMetadataCollector(Object):
    """"""
    def AddArray(self, name: str, type: TraceLoggingDataType) -> None:
        """"""
    def AddBinary(self, name: str, type: TraceLoggingDataType) -> None:
        """"""
    def AddCustom(self, name: str, type: TraceLoggingDataType, metadata: Array[int]) -> None:
        """"""
    def AddGroup(self, name: str) -> TraceLoggingMetadataCollector:
        """"""
    def AddScalar(self, name: str, type: TraceLoggingDataType) -> None:
        """"""
    def BeginBufferedArray(self) -> None:
        """"""
    def EndBufferedArray(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TraceLoggingTypeInfo(ABC, Object):
    """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class TraceLoggingTypeInfo[DataType](ABC, TraceLoggingTypeInfo):
    """"""
    @classmethod
    @property
    def Instance(cls) -> TraceLoggingTypeInfo[DataType]:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: DataType) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class TypeAnalysis(Object):
    """"""
    def __init__(
        self, dataType: Type, eventAttrib: EventDataAttribute, recursionCheck: List[Type]
    ) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class UInt16ArrayTypeInfo(TraceLoggingTypeInfo[Array[UInt16]]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: UInt16) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class UInt16TypeInfo(TraceLoggingTypeInfo[UInt16]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: UInt16) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class UInt32ArrayTypeInfo(TraceLoggingTypeInfo[Array[UInt32]]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: UInt32) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class UInt32TypeInfo(TraceLoggingTypeInfo[UInt32]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: UInt32) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class UInt64ArrayTypeInfo(TraceLoggingTypeInfo[Array[UInt64]]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: UInt64) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class UInt64TypeInfo(TraceLoggingTypeInfo[UInt64]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: UInt64) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class UIntPtrArrayTypeInfo(TraceLoggingTypeInfo[Array[UIntPtr]]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: UIntPtr) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""

class UIntPtrTypeInfo(TraceLoggingTypeInfo[UIntPtr]):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Keywords(self) -> EventKeywords:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Tags(self) -> EventTags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, value: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteData(self, collector: TraceLoggingDataCollector, value: UIntPtr) -> None:
        """"""
    def WriteMetadata(
        self, collector: TraceLoggingMetadataCollector, name: str, format: EventFieldFormat
    ) -> None:
        """"""
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: object) -> None:
        """"""
