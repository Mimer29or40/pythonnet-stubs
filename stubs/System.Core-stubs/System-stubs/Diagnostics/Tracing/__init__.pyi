from __future__ import annotations

from abc import ABC
from typing import Generic, List, Optional, Protocol, Tuple, TypeVar, Union, overload

from System import Array, Attribute, Boolean, Byte, Char, DateTime, DateTimeOffset, Decimal, Delegate, Double, Enum, EventArgs, EventHandler, Exception, Guid, IDisposable, Int16, Int32, Int64, IntPtr, Nullable, Object, SByte, Single, String, TimeSpan, Tuple, Type, UInt16, UInt32, UInt64, UIntPtr, ValueType, Void
from System.Collections import IEnumerable
from System.Collections.Generic import ICollection, IDictionary, IEnumerable, IEnumerator, IList, KeyValuePair, List
from System.Collections.ObjectModel import ReadOnlyCollection
from System.Reflection import Assembly, MethodInfo, PropertyInfo
from System.Resources import ResourceManager
from System.Runtime.InteropServices import _Attribute, _Exception
from System.Runtime.Serialization import ISerializable

# ---------- Types ---------- #

AttributeType = TypeVar('AttributeType', bound=Attribute)
ContainerType = TypeVar('ContainerType')
DataType = TypeVar('DataType')
ElementType = TypeVar('ElementType')
EnumType = TypeVar('EnumType')
ItemType = TypeVar('ItemType', bound=ConcurrentSetItem[KeyType, ItemType])
IterableType = TypeVar('IterableType', bound=IEnumerable[ElementType])
K = TypeVar('K')
KeyType = TypeVar('KeyType')
T = TypeVar('T')
UnderlyingType = TypeVar('UnderlyingType')
V = TypeVar('V')
ValueType = TypeVar('ValueType')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
CharType = Union[str, Char]
DecimalType = Union[float, Decimal]
DoubleType = Union[float, Double]
FloatType = Union[float, Single]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
NUIntType = Union[int, UIntPtr]
NullableType = Union[Optional, Nullable]
ObjectType = Object
SByteType = Union[int, SByte]
ShortType = Union[int, Int16]
StringType = Union[str, String]
TypeType = Union[type, Type]
UIntType = Union[int, UInt32]
ULongType = Union[int, UInt64]
UShortType = Union[int, UInt16]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...


# ---------- Classes ---------- #

class ActivityFilter(ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def DisableFilter(filterList: ActivityFilter, source: EventSource) -> Tuple[VoidType, ActivityFilter]: ...
    
    def Dispose(self) -> VoidType: ...
    
    @staticmethod
    def FlowActivityIfNeeded(filterList: ActivityFilter, currentActivityId: Guid, childActivityID: Guid) -> VoidType: ...
    
    @staticmethod
    def GetFilter(filterList: ActivityFilter, source: EventSource) -> ActivityFilter: ...
    
    def GetFilterAsTuple(self, sourceGuid: Guid) -> IEnumerable[Tuple[IntType, IntType]]: ...
    
    @staticmethod
    def IsCurrentActivityActive(filterList: ActivityFilter) -> BooleanType: ...
    
    @staticmethod
    def PassesActivityFilter(filterList: ActivityFilter, childActivityID: Guid, triggeringEvent: BooleanType, source: EventSource, eventId: IntType) -> BooleanType: ...
    
    @staticmethod
    def UpdateFilter(filterList: ActivityFilter, source: EventSource, perEventSourceSessionId: IntType, startEvents: StringType) -> Tuple[VoidType, ActivityFilter]: ...
    
    @staticmethod
    def UpdateKwdTriggers(activityFilter: ActivityFilter, sourceGuid: Guid, source: EventSource, sessKeywords: EventKeywords) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ActivityTracker(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Instance() -> ActivityTracker: ...
    
    # ---------- Methods ---------- #
    
    def Enable(self) -> VoidType: ...
    
    def OnStart(self, providerName: StringType, activityName: StringType, task: IntType, activityId: Guid, relatedActivityId: Guid, options: EventActivityOptions) -> Tuple[VoidType, Guid, Guid]: ...
    
    def OnStop(self, providerName: StringType, activityName: StringType, task: IntType, activityId: Guid) -> Tuple[VoidType, Guid]: ...
    
    @staticmethod
    def get_Instance() -> ActivityTracker: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ArrayTypeInfo(Generic[ElementType], TraceLoggingTypeInfo[ArrayType[ElementType]]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, elementInfo: TraceLoggingTypeInfo[ElementType]): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetData(self, value: ObjectType) -> ObjectType: ...
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: ElementType) -> Tuple[VoidType, ElementType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BooleanArrayTypeInfo(TraceLoggingTypeInfo[ArrayType[BooleanType]]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: BooleanType) -> Tuple[VoidType, BooleanType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BooleanTypeInfo(TraceLoggingTypeInfo[BooleanType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: BooleanType) -> Tuple[VoidType, BooleanType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ByteArrayTypeInfo(TraceLoggingTypeInfo[ArrayType[ByteType]]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: ByteType) -> Tuple[VoidType, ByteType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ByteTypeInfo(TraceLoggingTypeInfo[ByteType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: ByteType) -> Tuple[VoidType, ByteType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CharArrayTypeInfo(TraceLoggingTypeInfo[ArrayType[CharType]]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: CharType) -> Tuple[VoidType, CharType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CharTypeInfo(TraceLoggingTypeInfo[CharType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: CharType) -> Tuple[VoidType, CharType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ClassPropertyWriter(Generic[ContainerType, ValueType], PropertyAccessor[ContainerType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, property: PropertyAnalysis): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetData(self, container: ContainerType) -> ObjectType: ...
    
    def Write(self, collector: TraceLoggingDataCollector, container: ContainerType) -> Tuple[VoidType, ContainerType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConcurrentSetItem(Protocol[KeyType, ItemType], ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Compare(self, other: ItemType) -> IntType: ...
    
    @overload
    def Compare(self, key: KeyType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DateTimeOffsetTypeInfo(TraceLoggingTypeInfo[DateTimeOffset]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: DateTimeOffset) -> Tuple[VoidType, DateTimeOffset]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DateTimeTypeInfo(TraceLoggingTypeInfo[DateTime]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: DateTime) -> Tuple[VoidType, DateTime]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecimalTypeInfo(TraceLoggingTypeInfo[DecimalType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: DecimalType) -> Tuple[VoidType, DecimalType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DoubleArrayTypeInfo(TraceLoggingTypeInfo[ArrayType[DoubleType]]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: DoubleType) -> Tuple[VoidType, DoubleType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DoubleTypeInfo(TraceLoggingTypeInfo[DoubleType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: DoubleType) -> Tuple[VoidType, DoubleType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EnumByteTypeInfo(Generic[EnumType], TraceLoggingTypeInfo[EnumType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetData(self, value: ObjectType) -> ObjectType: ...
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: EnumType) -> Tuple[VoidType, EnumType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EnumHelper(Protocol[UnderlyingType], ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Cast(value: ValueType) -> UnderlyingType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EnumInt16TypeInfo(Generic[EnumType], TraceLoggingTypeInfo[EnumType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetData(self, value: ObjectType) -> ObjectType: ...
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: EnumType) -> Tuple[VoidType, EnumType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EnumInt32TypeInfo(Generic[EnumType], TraceLoggingTypeInfo[EnumType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetData(self, value: ObjectType) -> ObjectType: ...
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: EnumType) -> Tuple[VoidType, EnumType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EnumInt64TypeInfo(Generic[EnumType], TraceLoggingTypeInfo[EnumType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetData(self, value: ObjectType) -> ObjectType: ...
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: EnumType) -> Tuple[VoidType, EnumType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EnumSByteTypeInfo(Generic[EnumType], TraceLoggingTypeInfo[EnumType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetData(self, value: ObjectType) -> ObjectType: ...
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: EnumType) -> Tuple[VoidType, EnumType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EnumUInt16TypeInfo(Generic[EnumType], TraceLoggingTypeInfo[EnumType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetData(self, value: ObjectType) -> ObjectType: ...
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: EnumType) -> Tuple[VoidType, EnumType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EnumUInt32TypeInfo(Generic[EnumType], TraceLoggingTypeInfo[EnumType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetData(self, value: ObjectType) -> ObjectType: ...
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: EnumType) -> Tuple[VoidType, EnumType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EnumUInt64TypeInfo(Generic[EnumType], TraceLoggingTypeInfo[EnumType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetData(self, value: ObjectType) -> ObjectType: ...
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: EnumType) -> Tuple[VoidType, EnumType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EnumerableTypeInfo(Generic[IterableType, ElementType], TraceLoggingTypeInfo[IterableType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, elementInfo: TraceLoggingTypeInfo[ElementType]): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetData(self, value: ObjectType) -> ObjectType: ...
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: IterableType) -> Tuple[VoidType, IterableType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EtwSession(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def m_activityFilter(self) -> ActivityFilter: ...
    
    @m_activityFilter.setter
    def m_activityFilter(self, value: ActivityFilter) -> None: ...
    
    @property
    def m_etwSessionId(self) -> IntType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetEtwSession(etwSessionId: IntType, bCreateIfNeeded: BooleanType) -> EtwSession: ...
    
    @staticmethod
    def RemoveEtwSession(etwSession: EtwSession) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, eventId: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ActivityOptions(self) -> EventActivityOptions: ...
    
    @ActivityOptions.setter
    def ActivityOptions(self, value: EventActivityOptions) -> None: ...
    
    @property
    def Channel(self) -> EventChannel: ...
    
    @Channel.setter
    def Channel(self, value: EventChannel) -> None: ...
    
    @property
    def EventId(self) -> IntType: ...
    
    @property
    def Keywords(self) -> EventKeywords: ...
    
    @Keywords.setter
    def Keywords(self, value: EventKeywords) -> None: ...
    
    @property
    def Level(self) -> EventLevel: ...
    
    @Level.setter
    def Level(self, value: EventLevel) -> None: ...
    
    @property
    def Message(self) -> StringType: ...
    
    @Message.setter
    def Message(self, value: StringType) -> None: ...
    
    @property
    def Opcode(self) -> EventOpcode: ...
    
    @Opcode.setter
    def Opcode(self, value: EventOpcode) -> None: ...
    
    @property
    def Tags(self) -> EventTags: ...
    
    @Tags.setter
    def Tags(self, value: EventTags) -> None: ...
    
    @property
    def Task(self) -> EventTask: ...
    
    @Task.setter
    def Task(self, value: EventTask) -> None: ...
    
    @property
    def Version(self) -> ByteType: ...
    
    @Version.setter
    def Version(self, value: ByteType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ActivityOptions(self) -> EventActivityOptions: ...
    
    def get_Channel(self) -> EventChannel: ...
    
    def get_EventId(self) -> IntType: ...
    
    def get_Keywords(self) -> EventKeywords: ...
    
    def get_Level(self) -> EventLevel: ...
    
    def get_Message(self) -> StringType: ...
    
    def get_Opcode(self) -> EventOpcode: ...
    
    def get_Tags(self) -> EventTags: ...
    
    def get_Task(self) -> EventTask: ...
    
    def get_Version(self) -> ByteType: ...
    
    def set_ActivityOptions(self, value: EventActivityOptions) -> VoidType: ...
    
    def set_Channel(self, value: EventChannel) -> VoidType: ...
    
    def set_Keywords(self, value: EventKeywords) -> VoidType: ...
    
    def set_Level(self, value: EventLevel) -> VoidType: ...
    
    def set_Message(self, value: StringType) -> VoidType: ...
    
    def set_Opcode(self, value: EventOpcode) -> VoidType: ...
    
    def set_Tags(self, value: EventTags) -> VoidType: ...
    
    def set_Task(self, value: EventTask) -> VoidType: ...
    
    def set_Version(self, value: ByteType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventChannelAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Enabled(self) -> BooleanType: ...
    
    @Enabled.setter
    def Enabled(self, value: BooleanType) -> None: ...
    
    @property
    def EventChannelType(self) -> EventChannelType: ...
    
    @EventChannelType.setter
    def EventChannelType(self, value: EventChannelType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Enabled(self) -> BooleanType: ...
    
    def get_EventChannelType(self) -> EventChannelType: ...
    
    def set_Enabled(self, value: BooleanType) -> VoidType: ...
    
    def set_EventChannelType(self, value: EventChannelType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventCommandEventArgs(EventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Arguments(self) -> IDictionary[StringType, StringType]: ...
    
    @property
    def Command(self) -> EventCommand: ...
    
    # ---------- Methods ---------- #
    
    def DisableEvent(self, eventId: IntType) -> BooleanType: ...
    
    def EnableEvent(self, eventId: IntType) -> BooleanType: ...
    
    def get_Arguments(self) -> IDictionary[StringType, StringType]: ...
    
    def get_Command(self) -> EventCommand: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventDataAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventDispatcher(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventFieldAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Format(self) -> EventFieldFormat: ...
    
    @Format.setter
    def Format(self, value: EventFieldFormat) -> None: ...
    
    @property
    def Tags(self) -> EventFieldTags: ...
    
    @Tags.setter
    def Tags(self, value: EventFieldTags) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Format(self) -> EventFieldFormat: ...
    
    def get_Tags(self) -> EventFieldTags: ...
    
    def set_Format(self, value: EventFieldFormat) -> VoidType: ...
    
    def set_Tags(self, value: EventFieldTags) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventIgnoreAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventListener(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def DisableEvents(self, eventSource: EventSource) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    @overload
    def EnableEvents(self, eventSource: EventSource, level: EventLevel) -> VoidType: ...
    
    @overload
    def EnableEvents(self, eventSource: EventSource, level: EventLevel, matchAnyKeyword: EventKeywords) -> VoidType: ...
    
    @overload
    def EnableEvents(self, eventSource: EventSource, level: EventLevel, matchAnyKeyword: EventKeywords, arguments: IDictionary[StringType, StringType]) -> VoidType: ...
    
    @staticmethod
    def EventSourceIndex(eventSource: EventSource) -> IntType: ...
    
    def add_EventSourceCreated(self, value: EventHandler[EventSourceCreatedEventArgs]) -> VoidType: ...
    
    def add_EventWritten(self, value: EventHandler[EventWrittenEventArgs]) -> VoidType: ...
    
    def remove_EventSourceCreated(self, value: EventHandler[EventSourceCreatedEventArgs]) -> VoidType: ...
    
    def remove_EventWritten(self, value: EventHandler[EventWrittenEventArgs]) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    EventSourceCreated: EventType[EventHandler[EventSourceCreatedEventArgs]] = ...
    
    EventWritten: EventType[EventHandler[EventWrittenEventArgs]] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventPayload(ObjectType, IDictionary[StringType, ObjectType], ICollection[KeyValuePair[StringType, ObjectType]], IEnumerable[KeyValuePair[StringType, ObjectType]], IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def Item(self) -> ObjectType: ...
    
    @Item.setter
    def Item(self, value: ObjectType) -> None: ...
    
    @property
    def Keys(self) -> ICollection[StringType]: ...
    
    @property
    def Values(self) -> ICollection[ObjectType]: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, key: StringType, value: ObjectType) -> VoidType: ...
    
    @overload
    def Add(self, payloadEntry: KeyValuePair[StringType, ObjectType]) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, entry: KeyValuePair[StringType, ObjectType]) -> BooleanType: ...
    
    def ContainsKey(self, key: StringType) -> BooleanType: ...
    
    def CopyTo(self, payloadEntries: ArrayType[KeyValuePair[StringType, ObjectType]], count: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[KeyValuePair[StringType, ObjectType]]: ...
    
    @overload
    def Remove(self, key: StringType) -> BooleanType: ...
    
    @overload
    def Remove(self, entry: KeyValuePair[StringType, ObjectType]) -> BooleanType: ...
    
    def TryGetValue(self, key: StringType, value: ObjectType) -> Tuple[BooleanType, ObjectType]: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_Item(self, key: StringType) -> ObjectType: ...
    
    def get_Keys(self) -> ICollection[StringType]: ...
    
    def get_Values(self) -> ICollection[ObjectType]: ...
    
    def set_Item(self, key: StringType, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventProvider(ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    @staticmethod
    def GetLastWriteEventError() -> WriteEventErrorCode: ...
    
    @overload
    def IsEnabled(self) -> BooleanType: ...
    
    @overload
    def IsEnabled(self, level: ByteType, keywords: LongType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # ---------- Sub Structs ---------- #
    
    class EventData(ValueType):
        """"""
        
        # No Fields
        
        # No Constructors
        
        # No Properties
        
        # No Methods
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    class SessionInfo(ValueType):
        """"""
        
        # No Fields
        
        # No Constructors
        
        # No Properties
        
        # No Methods
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class WriteEventErrorCode(Enum):
        NoError: IntType = 0
        NoFreeBuffers: IntType = 1
        EventTooBig: IntType = 2
        NullInput: IntType = 3
        TooManyArgs: IntType = 4
        Other: IntType = 5
    


class EventSource(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, eventSourceName: StringType): ...
    
    @overload
    def __init__(self, eventSourceName: StringType, config: EventSourceSettings): ...
    
    @overload
    def __init__(self, eventSourceName: StringType, config: EventSourceSettings, traits: ArrayType[StringType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ConstructionException(self) -> Exception: ...
    
    @staticmethod
    @property
    def CurrentThreadActivityId() -> Guid: ...
    
    @property
    def Guid(self) -> Guid: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Settings(self) -> EventSourceSettings: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    @staticmethod
    @overload
    def GenerateManifest(eventSourceType: TypeType, assemblyPathToIncludeInManifest: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def GenerateManifest(eventSourceType: TypeType, assemblyPathToIncludeInManifest: StringType, flags: EventManifestOptions) -> StringType: ...
    
    @staticmethod
    def GetGuid(eventSourceType: TypeType) -> Guid: ...
    
    @staticmethod
    def GetName(eventSourceType: TypeType) -> StringType: ...
    
    @staticmethod
    def GetSources() -> IEnumerable[EventSource]: ...
    
    def GetTrait(self, key: StringType) -> StringType: ...
    
    @overload
    def IsEnabled(self) -> BooleanType: ...
    
    @overload
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords) -> BooleanType: ...
    
    @overload
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords, channel: EventChannel) -> BooleanType: ...
    
    @staticmethod
    def SendCommand(eventSource: EventSource, command: EventCommand, commandArguments: IDictionary[StringType, StringType]) -> VoidType: ...
    
    @staticmethod
    @overload
    def SetCurrentThreadActivityId(activityId: Guid) -> VoidType: ...
    
    @staticmethod
    @overload
    def SetCurrentThreadActivityId(activityId: Guid, oldActivityThatWillContinue: Guid) -> Tuple[VoidType, Guid]: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def Write(self, eventName: StringType) -> VoidType: ...
    
    @overload
    def Write(self, eventName: StringType, options: EventSourceOptions) -> VoidType: ...
    
    @overload
    def Write(self, eventName: StringType, data: T) -> VoidType: ...
    
    @overload
    def Write(self, eventName: StringType, options: EventSourceOptions, data: T) -> VoidType: ...
    
    @overload
    def Write(self, eventName: StringType, options: EventSourceOptions, data: T) -> Tuple[VoidType, EventSourceOptions, T]: ...
    
    @overload
    def Write(self, eventName: StringType, options: EventSourceOptions, activityId: Guid, relatedActivityId: Guid, data: T) -> Tuple[VoidType, EventSourceOptions, Guid, Guid, T]: ...
    
    def add_EventCommandExecuted(self, value: EventHandler[EventCommandEventArgs]) -> VoidType: ...
    
    def get_ConstructionException(self) -> Exception: ...
    
    @staticmethod
    def get_CurrentThreadActivityId() -> Guid: ...
    
    def get_Guid(self) -> Guid: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Settings(self) -> EventSourceSettings: ...
    
    def remove_EventCommandExecuted(self, value: EventHandler[EventCommandEventArgs]) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    EventCommandExecuted: EventType[EventHandler[EventCommandEventArgs]] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventSourceActivity(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, eventSource: EventSource): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EventSource(self) -> EventSource: ...
    
    @property
    def Id(self) -> Guid: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    @overload
    def Start(self, eventName: StringType) -> EventSourceActivity: ...
    
    @overload
    def Start(self, eventName: StringType, options: EventSourceOptions) -> EventSourceActivity: ...
    
    @overload
    def Start(self, eventName: StringType, options: EventSourceOptions, data: T) -> EventSourceActivity: ...
    
    @overload
    def Start(self, eventName: StringType, data: T) -> EventSourceActivity: ...
    
    @overload
    def Stop(self, data: T) -> VoidType: ...
    
    @overload
    def Stop(self, eventName: StringType) -> VoidType: ...
    
    @overload
    def Stop(self, eventName: StringType, data: T) -> VoidType: ...
    
    @overload
    def Write(self, eventName: StringType, options: EventSourceOptions) -> VoidType: ...
    
    @overload
    def Write(self, eventName: StringType) -> VoidType: ...
    
    @overload
    def Write(self, eventName: StringType, options: EventSourceOptions, data: T) -> VoidType: ...
    
    @overload
    def Write(self, eventName: StringType, data: T) -> VoidType: ...
    
    @overload
    def Write(self, source: EventSource, eventName: StringType, options: EventSourceOptions, data: T) -> VoidType: ...
    
    def get_EventSource(self) -> EventSource: ...
    
    def get_Id(self) -> Guid: ...
    
    @staticmethod
    def op_Implicit(eventSource: EventSource) -> EventSourceActivity: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventSourceAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Guid(self) -> StringType: ...
    
    @Guid.setter
    def Guid(self, value: StringType) -> None: ...
    
    @property
    def LocalizationResources(self) -> StringType: ...
    
    @LocalizationResources.setter
    def LocalizationResources(self, value: StringType) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Guid(self) -> StringType: ...
    
    def get_LocalizationResources(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def set_Guid(self, value: StringType) -> VoidType: ...
    
    def set_LocalizationResources(self, value: StringType) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventSourceCreatedEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EventSource(self) -> EventSource: ...
    
    # ---------- Methods ---------- #
    
    def get_EventSource(self) -> EventSource: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventSourceException(Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventWrittenEventArgs(EventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ActivityId(self) -> Guid: ...
    
    @property
    def Channel(self) -> EventChannel: ...
    
    @property
    def EventId(self) -> IntType: ...
    
    @property
    def EventName(self) -> StringType: ...
    
    @property
    def EventSource(self) -> EventSource: ...
    
    @property
    def Keywords(self) -> EventKeywords: ...
    
    @property
    def Level(self) -> EventLevel: ...
    
    @property
    def Message(self) -> StringType: ...
    
    @property
    def Opcode(self) -> EventOpcode: ...
    
    @property
    def Payload(self) -> ReadOnlyCollection[ObjectType]: ...
    
    @property
    def PayloadNames(self) -> ReadOnlyCollection[StringType]: ...
    
    @property
    def RelatedActivityId(self) -> Guid: ...
    
    @property
    def Tags(self) -> EventTags: ...
    
    @property
    def Task(self) -> EventTask: ...
    
    @property
    def Version(self) -> ByteType: ...
    
    # ---------- Methods ---------- #
    
    def get_ActivityId(self) -> Guid: ...
    
    def get_Channel(self) -> EventChannel: ...
    
    def get_EventId(self) -> IntType: ...
    
    def get_EventName(self) -> StringType: ...
    
    def get_EventSource(self) -> EventSource: ...
    
    def get_Keywords(self) -> EventKeywords: ...
    
    def get_Level(self) -> EventLevel: ...
    
    def get_Message(self) -> StringType: ...
    
    def get_Opcode(self) -> EventOpcode: ...
    
    def get_Payload(self) -> ReadOnlyCollection[ObjectType]: ...
    
    def get_PayloadNames(self) -> ReadOnlyCollection[StringType]: ...
    
    def get_RelatedActivityId(self) -> Guid: ...
    
    def get_Tags(self) -> EventTags: ...
    
    def get_Task(self) -> EventTask: ...
    
    def get_Version(self) -> ByteType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FieldMetadata(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, name: StringType, type: TraceLoggingDataType, tags: EventFieldTags, variableCount: BooleanType): ...
    
    @overload
    def __init__(self, name: StringType, type: TraceLoggingDataType, tags: EventFieldTags, fixedCount: UShortType): ...
    
    @overload
    def __init__(self, name: StringType, type: TraceLoggingDataType, tags: EventFieldTags, custom: ArrayType[ByteType]): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Encode(self, pos: IntType, metadata: ArrayType[ByteType]) -> Tuple[VoidType, IntType]: ...
    
    def IncrementStructFieldCount(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FrameworkEventSource(EventSource, IDisposable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Log() -> FrameworkEventSource: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def IsInitialized() -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def BeginGetRequestStream(self, id: ObjectType, uri: StringType, success: BooleanType, synchronous: BooleanType) -> VoidType: ...
    
    def BeginGetResponse(self, id: ObjectType, uri: StringType, success: BooleanType, synchronous: BooleanType) -> VoidType: ...
    
    def EndGetRequestStream(self, id: ObjectType, success: BooleanType, synchronous: BooleanType) -> VoidType: ...
    
    def EndGetResponse(self, id: ObjectType, success: BooleanType, synchronous: BooleanType, statusCode: IntType) -> VoidType: ...
    
    @overload
    def ResourceManagerAddingCultureFromConfigFile(self, baseName: StringType, mainAssemblyName: StringType, cultureName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerAddingCultureFromConfigFile(self, baseName: StringType, mainAssembly: Assembly, cultureName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerCaseInsensitiveResourceStreamLookupFailed(self, baseName: StringType, mainAssemblyName: StringType, assemblyName: StringType, resourceFileName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerCaseInsensitiveResourceStreamLookupFailed(self, baseName: StringType, mainAssembly: Assembly, assemblyName: StringType, resourceFileName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerCaseInsensitiveResourceStreamLookupSucceeded(self, baseName: StringType, mainAssemblyName: StringType, assemblyName: StringType, resourceFileName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerCaseInsensitiveResourceStreamLookupSucceeded(self, baseName: StringType, mainAssembly: Assembly, assemblyName: StringType, resourceFileName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerCreatingResourceSet(self, baseName: StringType, mainAssemblyName: StringType, cultureName: StringType, fileName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerCreatingResourceSet(self, baseName: StringType, mainAssembly: Assembly, cultureName: StringType, fileName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerCultureFoundInConfigFile(self, baseName: StringType, mainAssemblyName: StringType, cultureName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerCultureFoundInConfigFile(self, baseName: StringType, mainAssembly: Assembly, cultureName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerCultureNotFoundInConfigFile(self, baseName: StringType, mainAssemblyName: StringType, cultureName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerCultureNotFoundInConfigFile(self, baseName: StringType, mainAssembly: Assembly, cultureName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerFoundResourceSetInCache(self, baseName: StringType, mainAssemblyName: StringType, cultureName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerFoundResourceSetInCache(self, baseName: StringType, mainAssembly: Assembly, cultureName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerFoundResourceSetInCacheUnexpected(self, baseName: StringType, mainAssemblyName: StringType, cultureName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerFoundResourceSetInCacheUnexpected(self, baseName: StringType, mainAssembly: Assembly, cultureName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerGetSatelliteAssemblyFailed(self, baseName: StringType, mainAssemblyName: StringType, cultureName: StringType, assemblyName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerGetSatelliteAssemblyFailed(self, baseName: StringType, mainAssembly: Assembly, cultureName: StringType, assemblyName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerGetSatelliteAssemblySucceeded(self, baseName: StringType, mainAssemblyName: StringType, cultureName: StringType, assemblyName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerGetSatelliteAssemblySucceeded(self, baseName: StringType, mainAssembly: Assembly, cultureName: StringType, assemblyName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerLookingForResourceSet(self, baseName: StringType, mainAssemblyName: StringType, cultureName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerLookingForResourceSet(self, baseName: StringType, mainAssembly: Assembly, cultureName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerLookupFailed(self, baseName: StringType, mainAssemblyName: StringType, cultureName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerLookupFailed(self, baseName: StringType, mainAssembly: Assembly, cultureName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerLookupStarted(self, baseName: StringType, mainAssemblyName: StringType, cultureName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerLookupStarted(self, baseName: StringType, mainAssembly: Assembly, cultureName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerManifestResourceAccessDenied(self, baseName: StringType, mainAssemblyName: StringType, assemblyName: StringType, canonicalName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerManifestResourceAccessDenied(self, baseName: StringType, mainAssembly: Assembly, assemblyName: StringType, canonicalName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerNeutralResourceAttributeMissing(self, mainAssemblyName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerNeutralResourceAttributeMissing(self, mainAssembly: Assembly) -> VoidType: ...
    
    @overload
    def ResourceManagerNeutralResourcesFound(self, baseName: StringType, mainAssemblyName: StringType, resName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerNeutralResourcesFound(self, baseName: StringType, mainAssembly: Assembly, resName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerNeutralResourcesNotFound(self, baseName: StringType, mainAssemblyName: StringType, resName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerNeutralResourcesNotFound(self, baseName: StringType, mainAssembly: Assembly, resName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerNeutralResourcesSufficient(self, baseName: StringType, mainAssemblyName: StringType, cultureName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerNeutralResourcesSufficient(self, baseName: StringType, mainAssembly: Assembly, cultureName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerNotCreatingResourceSet(self, baseName: StringType, mainAssemblyName: StringType, cultureName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerNotCreatingResourceSet(self, baseName: StringType, mainAssembly: Assembly, cultureName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerReleasingResources(self, baseName: StringType, mainAssemblyName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerReleasingResources(self, baseName: StringType, mainAssembly: Assembly) -> VoidType: ...
    
    @overload
    def ResourceManagerStreamFound(self, baseName: StringType, mainAssemblyName: StringType, cultureName: StringType, loadedAssemblyName: StringType, resourceFileName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerStreamFound(self, baseName: StringType, mainAssembly: Assembly, cultureName: StringType, loadedAssembly: Assembly, resourceFileName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerStreamNotFound(self, baseName: StringType, mainAssemblyName: StringType, cultureName: StringType, loadedAssemblyName: StringType, resourceFileName: StringType) -> VoidType: ...
    
    @overload
    def ResourceManagerStreamNotFound(self, baseName: StringType, mainAssembly: Assembly, cultureName: StringType, loadedAssembly: Assembly, resourceFileName: StringType) -> VoidType: ...
    
    def ThreadPoolDequeueWork(self, workID: LongType) -> VoidType: ...
    
    def ThreadPoolDequeueWorkObject(self, workID: ObjectType) -> VoidType: ...
    
    def ThreadPoolEnqueueWork(self, workID: LongType) -> VoidType: ...
    
    def ThreadPoolEnqueueWorkObject(self, workID: ObjectType) -> VoidType: ...
    
    def ThreadTransferReceive(self, id: LongType, kind: IntType, info: StringType) -> VoidType: ...
    
    def ThreadTransferReceiveHandled(self, id: LongType, kind: IntType, info: StringType) -> VoidType: ...
    
    def ThreadTransferReceiveHandledObj(self, id: ObjectType, kind: IntType, info: StringType) -> VoidType: ...
    
    def ThreadTransferReceiveObj(self, id: ObjectType, kind: IntType, info: StringType) -> VoidType: ...
    
    def ThreadTransferSend(self, id: LongType, kind: IntType, info: StringType, multiDequeues: BooleanType) -> VoidType: ...
    
    def ThreadTransferSendObj(self, id: ObjectType, kind: IntType, info: StringType, multiDequeues: BooleanType) -> VoidType: ...
    
    @staticmethod
    def get_IsInitialized() -> BooleanType: ...
    
    # No Events
    
    
    # ---------- Sub Classes ---------- #
    
    class Keywords(ABC, ObjectType):
        # ---------- Fields ---------- #
        
        @staticmethod
        @property
        def DynamicTypeUsage() -> EventKeywords: ...
        
        @staticmethod
        @property
        def Loader() -> EventKeywords: ...
        
        @staticmethod
        @property
        def NetClient() -> EventKeywords: ...
        
        @staticmethod
        @property
        def ThreadPool() -> EventKeywords: ...
        
        @staticmethod
        @property
        def ThreadTransfer() -> EventKeywords: ...
        
        # No Constructors
        
        # No Properties
        
        # No Methods
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    class Tasks(ABC, ObjectType):
        # ---------- Fields ---------- #
        
        @staticmethod
        @property
        def GetRequestStream() -> EventTask: ...
        
        @staticmethod
        @property
        def GetResponse() -> EventTask: ...
        
        @staticmethod
        @property
        def ThreadTransfer() -> EventTask: ...
        
        # No Constructors
        
        # No Properties
        
        # No Methods
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    class Opcodes(ABC, ObjectType):
        # ---------- Fields ---------- #
        
        @staticmethod
        @property
        def ReceiveHandled() -> EventOpcode: ...
        
        # No Constructors
        
        # No Properties
        
        # No Methods
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GuidArrayTypeInfo(TraceLoggingTypeInfo[ArrayType[Guid]]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: Guid) -> Tuple[VoidType, Guid]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GuidTypeInfo(TraceLoggingTypeInfo[Guid]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: Guid) -> Tuple[VoidType, Guid]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Int16ArrayTypeInfo(TraceLoggingTypeInfo[ArrayType[ShortType]]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: ShortType) -> Tuple[VoidType, ShortType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Int16TypeInfo(TraceLoggingTypeInfo[ShortType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: ShortType) -> Tuple[VoidType, ShortType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Int32ArrayTypeInfo(TraceLoggingTypeInfo[ArrayType[IntType]]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: IntType) -> Tuple[VoidType, IntType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Int32TypeInfo(TraceLoggingTypeInfo[IntType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: IntType) -> Tuple[VoidType, IntType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Int64ArrayTypeInfo(TraceLoggingTypeInfo[ArrayType[LongType]]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: LongType) -> Tuple[VoidType, LongType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Int64TypeInfo(TraceLoggingTypeInfo[LongType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: LongType) -> Tuple[VoidType, LongType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IntPtrArrayTypeInfo(TraceLoggingTypeInfo[ArrayType[NIntType]]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: NIntType) -> Tuple[VoidType, NIntType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IntPtrTypeInfo(TraceLoggingTypeInfo[NIntType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: NIntType) -> Tuple[VoidType, NIntType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InvokeTypeInfo(Generic[ContainerType], TraceLoggingTypeInfo[ContainerType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, typeAnalysis: TypeAnalysis): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetData(self, value: ObjectType) -> ObjectType: ...
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: ContainerType) -> Tuple[VoidType, ContainerType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    def WriteObjectData(self, collector: TraceLoggingDataCollector, valueObj: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class KeyValuePairTypeInfo(Generic[K, V], TraceLoggingTypeInfo[KeyValuePair[K, V]]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, recursionCheck: List[TypeType]): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetData(self, value: ObjectType) -> ObjectType: ...
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: KeyValuePair[K, V]) -> Tuple[VoidType, KeyValuePair[K, V]]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManifestBuilder(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, providerName: StringType, providerGuid: Guid, dllName: StringType, resources: ResourceManager, flags: EventManifestOptions): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Errors(self) -> IList[StringType]: ...
    
    # ---------- Methods ---------- #
    
    def AddChannel(self, name: StringType, value: IntType, channelAttribute: EventChannelAttribute) -> VoidType: ...
    
    def AddEventParameter(self, type: TypeType, name: StringType) -> VoidType: ...
    
    def AddKeyword(self, name: StringType, value: ULongType) -> VoidType: ...
    
    def AddOpcode(self, name: StringType, value: IntType) -> VoidType: ...
    
    def AddTask(self, name: StringType, value: IntType) -> VoidType: ...
    
    def CreateManifest(self) -> ArrayType[ByteType]: ...
    
    def EndEvent(self) -> VoidType: ...
    
    def GetChannelData(self) -> ArrayType[ULongType]: ...
    
    def GetChannelKeyword(self, channel: EventChannel) -> ULongType: ...
    
    def ManifestError(self, msg: StringType, runtimeCritical: BooleanType) -> VoidType: ...
    
    def StartEvent(self, eventName: StringType, eventAttribute: EventAttribute) -> VoidType: ...
    
    def get_Errors(self) -> IList[StringType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NameInfo(ConcurrentSetItem[KeyValuePair[StringType, EventTags], NameInfo]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType, tags: EventTags, typeMetadataSize: IntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Compare(self, other: NameInfo) -> IntType: ...
    
    @overload
    def Compare(self, key: KeyValuePair[StringType, EventTags]) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NonEventAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NonGenericProperytWriter(Generic[ContainerType], PropertyAccessor[ContainerType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, property: PropertyAnalysis): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetData(self, container: ContainerType) -> ObjectType: ...
    
    def Write(self, collector: TraceLoggingDataCollector, container: ContainerType) -> Tuple[VoidType, ContainerType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NullTypeInfo(Generic[DataType], TraceLoggingTypeInfo[DataType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetData(self, value: ObjectType) -> ObjectType: ...
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: DataType) -> Tuple[VoidType, DataType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NullableTypeInfo(Generic[T], TraceLoggingTypeInfo[NullableType[Nullable[T]]]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, recursionCheck: List[TypeType]): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: Nullable[T]) -> Tuple[VoidType, Nullable[T]]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PropertyAccessor(Protocol[ContainerType], ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Create(property: PropertyAnalysis) -> PropertyAccessor[ContainerType]: ...
    
    def GetData(self, value: ContainerType) -> ObjectType: ...
    
    def Write(self, collector: TraceLoggingDataCollector, value: ContainerType) -> Tuple[VoidType, ContainerType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PropertyAnalysis(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType, getterInfo: MethodInfo, typeInfo: TraceLoggingTypeInfo, fieldAttribute: EventFieldAttribute): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SByteArrayTypeInfo(TraceLoggingTypeInfo[ArrayType[SByteType]]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: SByteType) -> Tuple[VoidType, SByteType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SByteTypeInfo(TraceLoggingTypeInfo[SByteType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: SByteType) -> Tuple[VoidType, SByteType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SimpleEventTypes(Generic[T], TraceLoggingEventTypes):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Instance() -> SimpleEventTypes[T]: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_Instance() -> SimpleEventTypes[T]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SingleArrayTypeInfo(TraceLoggingTypeInfo[ArrayType[FloatType]]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: FloatType) -> Tuple[VoidType, FloatType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SingleTypeInfo(TraceLoggingTypeInfo[FloatType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: FloatType) -> Tuple[VoidType, FloatType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Statics(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def DefaultLevel() -> ByteType: ...
    
    @staticmethod
    @property
    def EventTagsMask() -> EventTags: ...
    
    @staticmethod
    @property
    def HexIntPtrType() -> TraceLoggingDataType: ...
    
    @staticmethod
    @property
    def InTypeChainFlag() -> ByteType: ...
    
    @staticmethod
    @property
    def InTypeCountMask() -> ByteType: ...
    
    @staticmethod
    @property
    def InTypeCustomCountFlag() -> ByteType: ...
    
    @staticmethod
    @property
    def InTypeFixedCountFlag() -> ByteType: ...
    
    @staticmethod
    @property
    def InTypeMask() -> ByteType: ...
    
    @staticmethod
    @property
    def InTypeVariableCountFlag() -> ByteType: ...
    
    @staticmethod
    @property
    def IntPtrType() -> TraceLoggingDataType: ...
    
    @staticmethod
    @property
    def OutTypeChainFlag() -> ByteType: ...
    
    @staticmethod
    @property
    def OutTypeMask() -> ByteType: ...
    
    @staticmethod
    @property
    def TraceLoggingChannel() -> ByteType: ...
    
    @staticmethod
    @property
    def UIntPtrType() -> TraceLoggingDataType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CheckName(name: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Combine(settingValue: IntType, defaultValue: ByteType) -> ByteType: ...
    
    @staticmethod
    @overload
    def Combine(settingValue1: IntType, settingValue2: IntType, defaultValue: ByteType) -> ByteType: ...
    
    @staticmethod
    @overload
    def Combine(settingValue1: IntType, settingValue2: IntType) -> IntType: ...
    
    @staticmethod
    def CreateDefaultTypeInfo(recursionCheck: List[TypeType]) -> TraceLoggingTypeInfo[DataType]: ...
    
    @staticmethod
    def CreateDelegate(delegateType: TypeType, methodInfo: MethodInfo) -> Delegate: ...
    
    @staticmethod
    def CreateInstance(type: TypeType, parameters: ArrayType[ObjectType]) -> ObjectType: ...
    
    @staticmethod
    def EncodeTags(tags: IntType, pos: IntType, metadata: ArrayType[ByteType]) -> Tuple[VoidType, IntType]: ...
    
    @staticmethod
    def FindEnumerableElementType(type: TypeType) -> TypeType: ...
    
    @staticmethod
    def Format16(format: EventFieldFormat, native: TraceLoggingDataType) -> TraceLoggingDataType: ...
    
    @staticmethod
    def Format32(format: EventFieldFormat, native: TraceLoggingDataType) -> TraceLoggingDataType: ...
    
    @staticmethod
    def Format64(format: EventFieldFormat, native: TraceLoggingDataType) -> TraceLoggingDataType: ...
    
    @staticmethod
    def Format8(format: EventFieldFormat, native: TraceLoggingDataType) -> TraceLoggingDataType: ...
    
    @staticmethod
    def FormatPtr(format: EventFieldFormat, native: TraceLoggingDataType) -> TraceLoggingDataType: ...
    
    @staticmethod
    @overload
    def GetCustomAttribute(propInfo: PropertyInfo) -> AttributeType: ...
    
    @staticmethod
    @overload
    def GetCustomAttribute(type: TypeType) -> AttributeType: ...
    
    @staticmethod
    def GetDeclaredStaticMethod(declaringType: TypeType, name: StringType) -> MethodInfo: ...
    
    @staticmethod
    def GetGenericArguments(type: TypeType) -> ArrayType[TypeType]: ...
    
    @staticmethod
    def GetGetMethod(propInfo: PropertyInfo) -> MethodInfo: ...
    
    @staticmethod
    def GetProperties(type: TypeType) -> IEnumerable[PropertyInfo]: ...
    
    @staticmethod
    def GetTypeInfoInstance(dataType: TypeType, recursionCheck: List[TypeType]) -> TraceLoggingTypeInfo: ...
    
    @staticmethod
    def HasCustomAttribute(propInfo: PropertyInfo, attributeType: TypeType) -> BooleanType: ...
    
    @staticmethod
    def IsEnum(type: TypeType) -> BooleanType: ...
    
    @staticmethod
    def IsGenericMatch(type: TypeType, openType: ObjectType) -> BooleanType: ...
    
    @staticmethod
    def IsValueType(type: TypeType) -> BooleanType: ...
    
    @staticmethod
    def MakeDataType(baseType: TraceLoggingDataType, format: EventFieldFormat) -> TraceLoggingDataType: ...
    
    @staticmethod
    def MetadataForString(name: StringType, prefixSize: IntType, suffixSize: IntType, additionalSize: IntType) -> ArrayType[ByteType]: ...
    
    @staticmethod
    def ShouldOverrideFieldName(fieldName: StringType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringTypeInfo(TraceLoggingTypeInfo[StringType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetData(self, value: ObjectType) -> ObjectType: ...
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: StringType) -> Tuple[VoidType, StringType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StructPropertyWriter(Generic[ContainerType, ValueType], PropertyAccessor[ContainerType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, property: PropertyAnalysis): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetData(self, container: ContainerType) -> ObjectType: ...
    
    def Write(self, collector: TraceLoggingDataCollector, container: ContainerType) -> Tuple[VoidType, ContainerType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TimeSpanTypeInfo(TraceLoggingTypeInfo[TimeSpan]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: TimeSpan) -> Tuple[VoidType, TimeSpan]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TraceLoggingDataCollector(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def AddArray(self, value: ArrayType[BooleanType]) -> VoidType: ...
    
    @overload
    def AddArray(self, value: ArrayType[SByteType]) -> VoidType: ...
    
    @overload
    def AddArray(self, value: ArrayType[ShortType]) -> VoidType: ...
    
    @overload
    def AddArray(self, value: ArrayType[UShortType]) -> VoidType: ...
    
    @overload
    def AddArray(self, value: ArrayType[IntType]) -> VoidType: ...
    
    @overload
    def AddArray(self, value: ArrayType[UIntType]) -> VoidType: ...
    
    @overload
    def AddArray(self, value: ArrayType[LongType]) -> VoidType: ...
    
    @overload
    def AddArray(self, value: ArrayType[ULongType]) -> VoidType: ...
    
    @overload
    def AddArray(self, value: ArrayType[NIntType]) -> VoidType: ...
    
    @overload
    def AddArray(self, value: ArrayType[NUIntType]) -> VoidType: ...
    
    @overload
    def AddArray(self, value: ArrayType[FloatType]) -> VoidType: ...
    
    @overload
    def AddArray(self, value: ArrayType[DoubleType]) -> VoidType: ...
    
    @overload
    def AddArray(self, value: ArrayType[CharType]) -> VoidType: ...
    
    @overload
    def AddArray(self, value: ArrayType[Guid]) -> VoidType: ...
    
    @overload
    def AddBinary(self, value: StringType) -> VoidType: ...
    
    @overload
    def AddBinary(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    def AddCustom(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    def AddGroup(self) -> TraceLoggingDataCollector: ...
    
    @overload
    def AddScalar(self, value: BooleanType) -> VoidType: ...
    
    @overload
    def AddScalar(self, value: SByteType) -> VoidType: ...
    
    @overload
    def AddScalar(self, value: ByteType) -> VoidType: ...
    
    @overload
    def AddScalar(self, value: ShortType) -> VoidType: ...
    
    @overload
    def AddScalar(self, value: UShortType) -> VoidType: ...
    
    @overload
    def AddScalar(self, value: IntType) -> VoidType: ...
    
    @overload
    def AddScalar(self, value: UIntType) -> VoidType: ...
    
    @overload
    def AddScalar(self, value: LongType) -> VoidType: ...
    
    @overload
    def AddScalar(self, value: ULongType) -> VoidType: ...
    
    @overload
    def AddScalar(self, value: NIntType) -> VoidType: ...
    
    @overload
    def AddScalar(self, value: NUIntType) -> VoidType: ...
    
    @overload
    def AddScalar(self, value: FloatType) -> VoidType: ...
    
    @overload
    def AddScalar(self, value: DoubleType) -> VoidType: ...
    
    @overload
    def AddScalar(self, value: CharType) -> VoidType: ...
    
    @overload
    def AddScalar(self, value: Guid) -> VoidType: ...
    
    def BeginBufferedArray(self) -> IntType: ...
    
    def EndBufferedArray(self, bookmark: IntType, count: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TraceLoggingEventTypes(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TraceLoggingMetadataCollector(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AddArray(self, name: StringType, type: TraceLoggingDataType) -> VoidType: ...
    
    def AddBinary(self, name: StringType, type: TraceLoggingDataType) -> VoidType: ...
    
    def AddCustom(self, name: StringType, type: TraceLoggingDataType, metadata: ArrayType[ByteType]) -> VoidType: ...
    
    def AddGroup(self, name: StringType) -> TraceLoggingMetadataCollector: ...
    
    def AddScalar(self, name: StringType, type: TraceLoggingDataType) -> VoidType: ...
    
    def BeginBufferedArray(self) -> VoidType: ...
    
    def EndBufferedArray(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TraceLoggingTypeInfo(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Keywords(self) -> EventKeywords: ...
    
    @property
    def Level(self) -> EventLevel: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Opcode(self) -> EventOpcode: ...
    
    @property
    def Tags(self) -> EventTags: ...
    
    # ---------- Methods ---------- #
    
    def GetData(self, value: ObjectType) -> ObjectType: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: ObjectType) -> VoidType: ...
    
    def get_Keywords(self) -> EventKeywords: ...
    
    def get_Level(self) -> EventLevel: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Opcode(self) -> EventOpcode: ...
    
    def get_Tags(self) -> EventTags: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TraceLoggingTypeInfo(Protocol[DataType], TraceLoggingTypeInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Instance() -> TraceLoggingTypeInfo[DataType]: ...
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: DataType) -> Tuple[VoidType, DataType]: ...
    
    def WriteObjectData(self, collector: TraceLoggingDataCollector, value: ObjectType) -> VoidType: ...
    
    @staticmethod
    def get_Instance() -> TraceLoggingTypeInfo[DataType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeAnalysis(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, dataType: TypeType, eventAttrib: EventDataAttribute, recursionCheck: List[TypeType]): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UInt16ArrayTypeInfo(TraceLoggingTypeInfo[ArrayType[UShortType]]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: UShortType) -> Tuple[VoidType, UShortType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UInt16TypeInfo(TraceLoggingTypeInfo[UShortType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: UShortType) -> Tuple[VoidType, UShortType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UInt32ArrayTypeInfo(TraceLoggingTypeInfo[ArrayType[UIntType]]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: UIntType) -> Tuple[VoidType, UIntType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UInt32TypeInfo(TraceLoggingTypeInfo[UIntType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: UIntType) -> Tuple[VoidType, UIntType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UInt64ArrayTypeInfo(TraceLoggingTypeInfo[ArrayType[ULongType]]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: ULongType) -> Tuple[VoidType, ULongType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UInt64TypeInfo(TraceLoggingTypeInfo[ULongType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: ULongType) -> Tuple[VoidType, ULongType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UIntPtrArrayTypeInfo(TraceLoggingTypeInfo[ArrayType[NUIntType]]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: NUIntType) -> Tuple[VoidType, NUIntType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UIntPtrTypeInfo(TraceLoggingTypeInfo[NUIntType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteData(self, collector: TraceLoggingDataCollector, value: NUIntType) -> Tuple[VoidType, NUIntType]: ...
    
    def WriteMetadata(self, collector: TraceLoggingMetadataCollector, name: StringType, format: EventFieldFormat) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class ConcurrentSet(Generic[KeyType, ItemType], ValueType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetOrAdd(self, newItem: ItemType) -> ItemType: ...
    
    def TryGet(self, key: KeyType) -> ItemType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DataCollector(ValueType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EmptyStruct(ValueType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventDescriptor(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, traceloggingId: IntType, level: ByteType, opcode: ByteType, keywords: LongType): ...
    
    @overload
    def __init__(self, id: IntType, version: ByteType, channel: ByteType, level: ByteType, opcode: ByteType, task: IntType, keywords: LongType): ...
    
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
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: EventDescriptor) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Channel(self) -> ByteType: ...
    
    def get_EventId(self) -> IntType: ...
    
    def get_Keywords(self) -> LongType: ...
    
    def get_Level(self) -> ByteType: ...
    
    def get_Opcode(self) -> ByteType: ...
    
    def get_Task(self) -> IntType: ...
    
    def get_Version(self) -> ByteType: ...
    
    @staticmethod
    def op_Equality(event1: EventDescriptor, event2: EventDescriptor) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(event1: EventDescriptor, event2: EventDescriptor) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventSourceOptions(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ActivityOptions(self) -> EventActivityOptions: ...
    
    @ActivityOptions.setter
    def ActivityOptions(self, value: EventActivityOptions) -> None: ...
    
    @property
    def Keywords(self) -> EventKeywords: ...
    
    @Keywords.setter
    def Keywords(self, value: EventKeywords) -> None: ...
    
    @property
    def Level(self) -> EventLevel: ...
    
    @Level.setter
    def Level(self, value: EventLevel) -> None: ...
    
    @property
    def Opcode(self) -> EventOpcode: ...
    
    @Opcode.setter
    def Opcode(self, value: EventOpcode) -> None: ...
    
    @property
    def Tags(self) -> EventTags: ...
    
    @Tags.setter
    def Tags(self, value: EventTags) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ActivityOptions(self) -> EventActivityOptions: ...
    
    def get_Keywords(self) -> EventKeywords: ...
    
    def get_Level(self) -> EventLevel: ...
    
    def get_Opcode(self) -> EventOpcode: ...
    
    def get_Tags(self) -> EventTags: ...
    
    def set_ActivityOptions(self, value: EventActivityOptions) -> VoidType: ...
    
    def set_Keywords(self, value: EventKeywords) -> VoidType: ...
    
    def set_Level(self, value: EventLevel) -> VoidType: ...
    
    def set_Opcode(self, value: EventOpcode) -> VoidType: ...
    
    def set_Tags(self, value: EventTags) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManifestEnvelope(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def ChunkNumber(self) -> UShortType: ...
    
    @ChunkNumber.setter
    def ChunkNumber(self, value: UShortType) -> None: ...
    
    @property
    def Format(self) -> ManifestFormats: ...
    
    @Format.setter
    def Format(self, value: ManifestFormats) -> None: ...
    
    @property
    def Magic(self) -> ByteType: ...
    
    @Magic.setter
    def Magic(self, value: ByteType) -> None: ...
    
    @property
    def MajorVersion(self) -> ByteType: ...
    
    @MajorVersion.setter
    def MajorVersion(self, value: ByteType) -> None: ...
    
    @staticmethod
    @property
    def MaxChunkSize() -> IntType: ...
    
    @property
    def MinorVersion(self) -> ByteType: ...
    
    @MinorVersion.setter
    def MinorVersion(self, value: ByteType) -> None: ...
    
    @property
    def TotalChunks(self) -> UShortType: ...
    
    @TotalChunks.setter
    def TotalChunks(self, value: UShortType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class ManifestFormats(Enum):
        SimpleXmlFormat: ByteType = 1
    


class SessionMask(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, m: SessionMask): ...
    
    @overload
    def __init__(self, mask: UIntType): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def All() -> SessionMask: ...
    
    @property
    def Item(self) -> BooleanType: ...
    
    @Item.setter
    def Item(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def FromEventKeywords(m: ULongType) -> SessionMask: ...
    
    @staticmethod
    def FromId(perEventSourceSessionId: IntType) -> SessionMask: ...
    
    def IsEqualOrSupersetOf(self, m: SessionMask) -> BooleanType: ...
    
    def ToEventKeywords(self) -> ULongType: ...
    
    @staticmethod
    def get_All() -> SessionMask: ...
    
    def get_Item(self, perEventSourceSessionId: IntType) -> BooleanType: ...
    
    @staticmethod
    def op_BitwiseAnd(m1: SessionMask, m2: SessionMask) -> SessionMask: ...
    
    @staticmethod
    def op_BitwiseOr(m1: SessionMask, m2: SessionMask) -> SessionMask: ...
    
    @staticmethod
    def op_ExclusiveOr(m1: SessionMask, m2: SessionMask) -> SessionMask: ...
    
    @staticmethod
    @overload
    def op_Explicit(m: SessionMask) -> ULongType: ...
    
    @staticmethod
    @overload
    def op_Explicit(m: SessionMask) -> UIntType: ...
    
    @staticmethod
    def op_OnesComplement(m: SessionMask) -> SessionMask: ...
    
    def set_Item(self, perEventSourceSessionId: IntType, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Interfaces

# ---------- Enums ---------- #

class ControllerCommand(Enum):
    Disable: IntType = -3
    Enable: IntType = -2
    SendManifest: IntType = -1
    Update: IntType = 0


class EventActivityOptions(Enum):
    #None: IntType = 0
    Disable: IntType = 2
    Recursive: IntType = 4
    Detachable: IntType = 8


class EventChannel(Enum):
    #None: ByteType = 0
    Admin: ByteType = 16
    Operational: ByteType = 17
    Analytic: ByteType = 18
    Debug: ByteType = 19


class EventChannelType(Enum):
    Admin: IntType = 1
    Operational: IntType = 2
    Analytic: IntType = 3
    Debug: IntType = 4


class EventCommand(Enum):
    Disable: IntType = -3
    Enable: IntType = -2
    SendManifest: IntType = -1
    Update: IntType = 0


class EventFieldFormat(Enum):
    Default: IntType = 0
    String: IntType = 2
    Boolean: IntType = 3
    Hexadecimal: IntType = 4
    Xml: IntType = 11
    Json: IntType = 12
    HResult: IntType = 15


class EventFieldTags(Enum):
    #None: IntType = 0


class EventKeywords(Enum):
    All: LongType = -1
    #None: LongType = 0
    MicrosoftTelemetry: LongType = 562949953421312
    WdiContext: LongType = 562949953421312
    WdiDiagnostic: LongType = 1125899906842624
    Sqm: LongType = 2251799813685248
    AuditFailure: LongType = 4503599627370496
    CorrelationHint: LongType = 4503599627370496
    AuditSuccess: LongType = 9007199254740992
    EventLogClassic: LongType = 36028797018963968


class EventLevel(Enum):
    LogAlways: IntType = 0
    Critical: IntType = 1
    Error: IntType = 2
    Warning: IntType = 3
    Informational: IntType = 4
    Verbose: IntType = 5


class EventManifestOptions(Enum):
    #None: IntType = 0
    Strict: IntType = 1
    AllCultures: IntType = 2
    OnlyIfNeededForRegistration: IntType = 4
    AllowEventSourceOverride: IntType = 8


class EventOpcode(Enum):
    Info: IntType = 0
    Start: IntType = 1
    Stop: IntType = 2
    DataCollectionStart: IntType = 3
    DataCollectionStop: IntType = 4
    Extension: IntType = 5
    Reply: IntType = 6
    Resume: IntType = 7
    Suspend: IntType = 8
    Send: IntType = 9
    Receive: IntType = 240


class EventSourceSettings(Enum):
    Default: IntType = 0
    ThrowOnEventWriteErrors: IntType = 1
    EtwManifestEventFormat: IntType = 4
    EtwSelfDescribingEventFormat: IntType = 8


class EventTags(Enum):
    #None: IntType = 0


class EventTask(Enum):
    #None: IntType = 0


class TraceLoggingDataType(Enum):
    Nil: IntType = 0
    Utf16String: IntType = 1
    MbcsString: IntType = 2
    Int8: IntType = 3
    UInt8: IntType = 4
    Int16: IntType = 5
    UInt16: IntType = 6
    Int32: IntType = 7
    UInt32: IntType = 8
    Int64: IntType = 9
    UInt64: IntType = 10
    Float: IntType = 11
    Double: IntType = 12
    Boolean32: IntType = 13
    Binary: IntType = 14
    Guid: IntType = 15
    FileTime: IntType = 17
    SystemTime: IntType = 18
    HexInt32: IntType = 20
    HexInt64: IntType = 21
    CountedUtf16String: IntType = 22
    CountedMbcsString: IntType = 23
    Struct: IntType = 24
    Char8: IntType = 516
    Char16: IntType = 518
    Boolean8: IntType = 772
    HexInt8: IntType = 1028
    HexInt16: IntType = 1030
    Utf16Xml: IntType = 2817
    MbcsXml: IntType = 2818
    CountedUtf16Xml: IntType = 2838
    CountedMbcsXml: IntType = 2839
    Utf16Json: IntType = 3073
    MbcsJson: IntType = 3074
    CountedUtf16Json: IntType = 3094
    CountedMbcsJson: IntType = 3095
    HResult: IntType = 3847


# No Delegates

__all__ = [
    ActivityFilter,
    ActivityTracker,
    ArrayTypeInfo,
    BooleanArrayTypeInfo,
    BooleanTypeInfo,
    ByteArrayTypeInfo,
    ByteTypeInfo,
    CharArrayTypeInfo,
    CharTypeInfo,
    ClassPropertyWriter,
    ConcurrentSetItem,
    DateTimeOffsetTypeInfo,
    DateTimeTypeInfo,
    DecimalTypeInfo,
    DoubleArrayTypeInfo,
    DoubleTypeInfo,
    EnumByteTypeInfo,
    EnumHelper,
    EnumInt16TypeInfo,
    EnumInt32TypeInfo,
    EnumInt64TypeInfo,
    EnumSByteTypeInfo,
    EnumUInt16TypeInfo,
    EnumUInt32TypeInfo,
    EnumUInt64TypeInfo,
    EnumerableTypeInfo,
    EtwSession,
    EventAttribute,
    EventChannelAttribute,
    EventCommandEventArgs,
    EventDataAttribute,
    EventDispatcher,
    EventFieldAttribute,
    EventIgnoreAttribute,
    EventListener,
    EventPayload,
    EventProvider,
    EventSource,
    EventSourceActivity,
    EventSourceAttribute,
    EventSourceCreatedEventArgs,
    EventSourceException,
    EventWrittenEventArgs,
    FieldMetadata,
    FrameworkEventSource,
    GuidArrayTypeInfo,
    GuidTypeInfo,
    Int16ArrayTypeInfo,
    Int16TypeInfo,
    Int32ArrayTypeInfo,
    Int32TypeInfo,
    Int64ArrayTypeInfo,
    Int64TypeInfo,
    IntPtrArrayTypeInfo,
    IntPtrTypeInfo,
    InvokeTypeInfo,
    KeyValuePairTypeInfo,
    ManifestBuilder,
    NameInfo,
    NonEventAttribute,
    NonGenericProperytWriter,
    NullTypeInfo,
    NullableTypeInfo,
    PropertyAccessor,
    PropertyAnalysis,
    SByteArrayTypeInfo,
    SByteTypeInfo,
    SimpleEventTypes,
    SingleArrayTypeInfo,
    SingleTypeInfo,
    Statics,
    StringTypeInfo,
    StructPropertyWriter,
    TimeSpanTypeInfo,
    TraceLoggingDataCollector,
    TraceLoggingEventTypes,
    TraceLoggingMetadataCollector,
    TraceLoggingTypeInfo,
    TypeAnalysis,
    UInt16ArrayTypeInfo,
    UInt16TypeInfo,
    UInt32ArrayTypeInfo,
    UInt32TypeInfo,
    UInt64ArrayTypeInfo,
    UInt64TypeInfo,
    UIntPtrArrayTypeInfo,
    UIntPtrTypeInfo,
    ConcurrentSet,
    DataCollector,
    EmptyStruct,
    EventDescriptor,
    EventSourceOptions,
    ManifestEnvelope,
    SessionMask,
    ControllerCommand,
    EventActivityOptions,
    EventChannel,
    EventChannelType,
    EventCommand,
    EventFieldFormat,
    EventFieldTags,
    EventKeywords,
    EventLevel,
    EventManifestOptions,
    EventOpcode,
    EventSourceSettings,
    EventTags,
    EventTask,
    TraceLoggingDataType,
]
