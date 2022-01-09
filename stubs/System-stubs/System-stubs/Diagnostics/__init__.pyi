from __future__ import annotations

from abc import ABC
from typing import Callable, Generic, List, Protocol, Tuple, Union, overload

from Microsoft.Win32 import NativeMethods
from Microsoft.Win32.SafeHandles import SafeProcessHandle, SafeThreadHandle
from System import Array, AsyncCallback, Attribute, Boolean, Byte, DateTime, Enum, EventArgs, EventHandler, Guid, IAsyncResult, ICloneable, IDisposable, Int16, Int32, Int64, IntPtr, MarshalByRefObject, MulticastDelegate, Object, Predicate, Single, String, TimeSpan, Type, ValueType, Void
from System.Collections import ArrayList, CollectionBase, DictionaryBase, Hashtable, ICollection, IComparer, IDictionary, IEnumerable, IEnumerator, IList, ReadOnlyCollectionBase, Stack
from System.Collections.Generic import IDictionary
from System.Collections.Specialized import StringDictionary
from System.ComponentModel import Component, DescriptionAttribute, EnumConverter, IComponent, ISupportInitialize, ISynchronizeInvoke, ITypeDescriptorContext, TypeConverter
from System.Configuration import ConfigurationElement, ConfigurationElementCollection, ConfigurationElementCollectionType, ConfigurationSection, DictionarySectionHandler, IConfigurationSectionHandler
from System.Diagnostics import StackFrame
from System.IO import Stream, StreamReader, StreamWriter, TextWriter
from System.Reflection import Assembly
from System.Runtime.InteropServices import _Attribute
from System.Runtime.Serialization import ISerializable
from System.Security import IPermission, ISecurityEncodable, IStackWalk, SecureString
from System.Security.Permissions import CodeAccessSecurityAttribute, IUnrestrictedPermission, PermissionState, ResourcePermissionBase, SecurityAction
from System.Text import Encoding
from System.Threading import WaitHandle
from System.Xml import XmlNode

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
FloatType = Union[float, Single]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
ShortType = Union[int, Int16]
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...


# ---------- Classes ---------- #

class AlphabeticalEnumConverter(EnumConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, type: TypeType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def GetStandardValues(self, context: ITypeDescriptorContext) -> StandardValuesCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssertSection(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AssertUIEnabled(self) -> BooleanType: ...
    
    @property
    def LogFileName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AssertUIEnabled(self) -> BooleanType: ...
    
    def get_LogFileName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssertWrapper(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def ShowAssert(stackTrace: StringType, frame: StackFrame, message: StringType, detailMessage: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsyncStreamReader(ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BaseStream(self) -> Stream: ...
    
    @property
    def CurrentEncoding(self) -> Encoding: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def get_BaseStream(self) -> Stream: ...
    
    def get_CurrentEncoding(self) -> Encoding: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BooleanSwitch(Switch):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, displayName: StringType, description: StringType): ...
    
    @overload
    def __init__(self, displayName: StringType, description: StringType, defaultSwitchValue: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Enabled(self) -> BooleanType: ...
    
    @Enabled.setter
    def Enabled(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Enabled(self) -> BooleanType: ...
    
    def set_Enabled(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CategoryEntry(ObjectType):
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


class CategorySample(ObjectType):
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


class ConsoleTraceListener(TextWriterTraceListener, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, useErrorStream: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CorrelationManager(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ActivityId(self) -> Guid: ...
    
    @ActivityId.setter
    def ActivityId(self, value: Guid) -> None: ...
    
    @property
    def LogicalOperationStack(self) -> Stack: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def StartLogicalOperation(self, operationId: ObjectType) -> VoidType: ...
    
    @overload
    def StartLogicalOperation(self) -> VoidType: ...
    
    def StopLogicalOperation(self) -> VoidType: ...
    
    def get_ActivityId(self) -> Guid: ...
    
    def get_LogicalOperationStack(self) -> Stack: ...
    
    def set_ActivityId(self, value: Guid) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CounterCreationData(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, counterName: StringType, counterHelp: StringType, counterType: PerformanceCounterType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CounterHelp(self) -> StringType: ...
    
    @CounterHelp.setter
    def CounterHelp(self, value: StringType) -> None: ...
    
    @property
    def CounterName(self) -> StringType: ...
    
    @CounterName.setter
    def CounterName(self, value: StringType) -> None: ...
    
    @property
    def CounterType(self) -> PerformanceCounterType: ...
    
    @CounterType.setter
    def CounterType(self, value: PerformanceCounterType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_CounterHelp(self) -> StringType: ...
    
    def get_CounterName(self) -> StringType: ...
    
    def get_CounterType(self) -> PerformanceCounterType: ...
    
    def set_CounterHelp(self, value: StringType) -> VoidType: ...
    
    def set_CounterName(self, value: StringType) -> VoidType: ...
    
    def set_CounterType(self, value: PerformanceCounterType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CounterCreationDataCollection(CollectionBase, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: CounterCreationDataCollection): ...
    
    @overload
    def __init__(self, value: ArrayType[CounterCreationData]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> CounterCreationData: ...
    
    @Item.setter
    def Item(self, value: CounterCreationData) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, value: CounterCreationData) -> IntType: ...
    
    @overload
    def AddRange(self, value: ArrayType[CounterCreationData]) -> VoidType: ...
    
    @overload
    def AddRange(self, value: CounterCreationDataCollection) -> VoidType: ...
    
    def Contains(self, value: CounterCreationData) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[CounterCreationData], index: IntType) -> VoidType: ...
    
    def IndexOf(self, value: CounterCreationData) -> IntType: ...
    
    def Insert(self, index: IntType, value: CounterCreationData) -> VoidType: ...
    
    def Remove(self, value: CounterCreationData) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> CounterCreationData: ...
    
    def set_Item(self, index: IntType, value: CounterCreationData) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CounterDefinitionSample(ObjectType):
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


class CounterSampleCalculator(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def ComputeCounterValue(newSample: CounterSample) -> FloatType: ...
    
    @staticmethod
    @overload
    def ComputeCounterValue(oldSample: CounterSample, newSample: CounterSample) -> FloatType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DataReceivedEventArgs(EventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Data(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Data(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DataReceivedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: DataReceivedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: DataReceivedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Debug(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def AutoFlush() -> BooleanType: ...
    
    @staticmethod
    @AutoFlush.setter
    def AutoFlush(value: BooleanType) -> None: ...
    
    @staticmethod
    @property
    def IndentLevel() -> IntType: ...
    
    @staticmethod
    @IndentLevel.setter
    def IndentLevel(value: IntType) -> None: ...
    
    @staticmethod
    @property
    def IndentSize() -> IntType: ...
    
    @staticmethod
    @IndentSize.setter
    def IndentSize(value: IntType) -> None: ...
    
    @staticmethod
    @property
    def Listeners() -> TraceListenerCollection: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Assert(condition: BooleanType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Assert(condition: BooleanType, message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Assert(condition: BooleanType, message: StringType, detailMessage: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Assert(condition: BooleanType, message: StringType, detailMessageFormat: StringType, args: ArrayType[ObjectType]) -> VoidType: ...
    
    @staticmethod
    def Close() -> VoidType: ...
    
    @staticmethod
    @overload
    def Fail(message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Fail(message: StringType, detailMessage: StringType) -> VoidType: ...
    
    @staticmethod
    def Flush() -> VoidType: ...
    
    @staticmethod
    def Indent() -> VoidType: ...
    
    @staticmethod
    @overload
    def Print(message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Print(format: StringType, args: ArrayType[ObjectType]) -> VoidType: ...
    
    @staticmethod
    def Unindent() -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(value: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(message: StringType, category: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(value: ObjectType, category: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteIf(condition: BooleanType, message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteIf(condition: BooleanType, value: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteIf(condition: BooleanType, message: StringType, category: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteIf(condition: BooleanType, value: ObjectType, category: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(value: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(message: StringType, category: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(value: ObjectType, category: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(format: StringType, args: ArrayType[ObjectType]) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLineIf(condition: BooleanType, message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLineIf(condition: BooleanType, value: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLineIf(condition: BooleanType, message: StringType, category: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLineIf(condition: BooleanType, value: ObjectType, category: StringType) -> VoidType: ...
    
    @staticmethod
    def get_AutoFlush() -> BooleanType: ...
    
    @staticmethod
    def get_IndentLevel() -> IntType: ...
    
    @staticmethod
    def get_IndentSize() -> IntType: ...
    
    @staticmethod
    def get_Listeners() -> TraceListenerCollection: ...
    
    @staticmethod
    def set_AutoFlush(value: BooleanType) -> VoidType: ...
    
    @staticmethod
    def set_IndentLevel(value: IntType) -> VoidType: ...
    
    @staticmethod
    def set_IndentSize(value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DefaultTraceListener(TraceListener, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AssertUiEnabled(self) -> BooleanType: ...
    
    @AssertUiEnabled.setter
    def AssertUiEnabled(self, value: BooleanType) -> None: ...
    
    @property
    def LogFileName(self) -> StringType: ...
    
    @LogFileName.setter
    def LogFileName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Fail(self, message: StringType) -> VoidType: ...
    
    @overload
    def Fail(self, message: StringType, detailMessage: StringType) -> VoidType: ...
    
    @overload
    def Write(self, message: StringType) -> VoidType: ...
    
    @overload
    def WriteLine(self, message: StringType) -> VoidType: ...
    
    def get_AssertUiEnabled(self) -> BooleanType: ...
    
    def get_LogFileName(self) -> StringType: ...
    
    def set_AssertUiEnabled(self, value: BooleanType) -> VoidType: ...
    
    def set_LogFileName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DelimitedListTraceListener(TextWriterTraceListener, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, stream: Stream): ...
    
    @overload
    def __init__(self, stream: Stream, name: StringType): ...
    
    @overload
    def __init__(self, writer: TextWriter): ...
    
    @overload
    def __init__(self, writer: TextWriter, name: StringType): ...
    
    @overload
    def __init__(self, fileName: StringType): ...
    
    @overload
    def __init__(self, fileName: StringType, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Delimiter(self) -> StringType: ...
    
    @Delimiter.setter
    def Delimiter(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def TraceData(self, eventCache: TraceEventCache, source: StringType, eventType: TraceEventType, id: IntType, data: ObjectType) -> VoidType: ...
    
    @overload
    def TraceData(self, eventCache: TraceEventCache, source: StringType, eventType: TraceEventType, id: IntType, data: ArrayType[ObjectType]) -> VoidType: ...
    
    @overload
    def TraceEvent(self, eventCache: TraceEventCache, source: StringType, eventType: TraceEventType, id: IntType, format: StringType, args: ArrayType[ObjectType]) -> VoidType: ...
    
    @overload
    def TraceEvent(self, eventCache: TraceEventCache, source: StringType, eventType: TraceEventType, id: IntType, message: StringType) -> VoidType: ...
    
    def get_Delimiter(self) -> StringType: ...
    
    def set_Delimiter(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DiagnosticsConfiguration(ABC, ObjectType):
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


class DiagnosticsConfigurationHandler(ObjectType, IConfigurationSectionHandler):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Create(self, parent: ObjectType, configContext: ObjectType, section: XmlNode) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EntryWrittenEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, entry: EventLogEntry): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Entry(self) -> EventLogEntry: ...
    
    # ---------- Methods ---------- #
    
    def get_Entry(self) -> EventLogEntry: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EntryWrittenEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: EntryWrittenEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: EntryWrittenEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EnvironmentBlock(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def ToByteArray(sd: StringDictionary, unicode: BooleanType) -> ArrayType[ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventInstance(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, instanceId: LongType, categoryId: IntType): ...
    
    @overload
    def __init__(self, instanceId: LongType, categoryId: IntType, entryType: EventLogEntryType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CategoryId(self) -> IntType: ...
    
    @CategoryId.setter
    def CategoryId(self, value: IntType) -> None: ...
    
    @property
    def EntryType(self) -> EventLogEntryType: ...
    
    @EntryType.setter
    def EntryType(self, value: EventLogEntryType) -> None: ...
    
    @property
    def InstanceId(self) -> LongType: ...
    
    @InstanceId.setter
    def InstanceId(self, value: LongType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_CategoryId(self) -> IntType: ...
    
    def get_EntryType(self) -> EventLogEntryType: ...
    
    def get_InstanceId(self) -> LongType: ...
    
    def set_CategoryId(self, value: IntType) -> VoidType: ...
    
    def set_EntryType(self, value: EventLogEntryType) -> VoidType: ...
    
    def set_InstanceId(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventLog(Component, IComponent, IDisposable, ISupportInitialize):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, logName: StringType): ...
    
    @overload
    def __init__(self, logName: StringType, machineName: StringType): ...
    
    @overload
    def __init__(self, logName: StringType, machineName: StringType, source: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EnableRaisingEvents(self) -> BooleanType: ...
    
    @EnableRaisingEvents.setter
    def EnableRaisingEvents(self, value: BooleanType) -> None: ...
    
    @property
    def Entries(self) -> EventLogEntryCollection: ...
    
    @property
    def Log(self) -> StringType: ...
    
    @Log.setter
    def Log(self, value: StringType) -> None: ...
    
    @property
    def LogDisplayName(self) -> StringType: ...
    
    @property
    def MachineName(self) -> StringType: ...
    
    @MachineName.setter
    def MachineName(self, value: StringType) -> None: ...
    
    @property
    def MaximumKilobytes(self) -> LongType: ...
    
    @MaximumKilobytes.setter
    def MaximumKilobytes(self, value: LongType) -> None: ...
    
    @property
    def MinimumRetentionDays(self) -> IntType: ...
    
    @property
    def OverflowAction(self) -> OverflowAction: ...
    
    @property
    def Source(self) -> StringType: ...
    
    @Source.setter
    def Source(self, value: StringType) -> None: ...
    
    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke: ...
    
    @SynchronizingObject.setter
    def SynchronizingObject(self, value: ISynchronizeInvoke) -> None: ...
    
    # ---------- Methods ---------- #
    
    def BeginInit(self) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Close(self) -> VoidType: ...
    
    @staticmethod
    @overload
    def CreateEventSource(source: StringType, logName: StringType, machineName: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def CreateEventSource(source: StringType, logName: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def CreateEventSource(sourceData: EventSourceCreationData) -> VoidType: ...
    
    @staticmethod
    @overload
    def Delete(logName: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Delete(logName: StringType, machineName: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def DeleteEventSource(source: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def DeleteEventSource(source: StringType, machineName: StringType) -> VoidType: ...
    
    def EndInit(self) -> VoidType: ...
    
    @staticmethod
    @overload
    def Exists(logName: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Exists(logName: StringType, machineName: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def GetEventLogs() -> ArrayType[EventLog]: ...
    
    @staticmethod
    @overload
    def GetEventLogs(machineName: StringType) -> ArrayType[EventLog]: ...
    
    @staticmethod
    def LogNameFromSourceName(source: StringType, machineName: StringType) -> StringType: ...
    
    def ModifyOverflowPolicy(self, action: OverflowAction, retentionDays: IntType) -> VoidType: ...
    
    def RegisterDisplayName(self, resourceFile: StringType, resourceId: LongType) -> VoidType: ...
    
    @staticmethod
    @overload
    def SourceExists(source: StringType, machineName: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def SourceExists(source: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def WriteEntry(source: StringType, message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteEntry(source: StringType, message: StringType, type: EventLogEntryType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteEntry(source: StringType, message: StringType, type: EventLogEntryType, eventID: IntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteEntry(source: StringType, message: StringType, type: EventLogEntryType, eventID: IntType, category: ShortType) -> VoidType: ...
    
    @overload
    def WriteEntry(self, message: StringType) -> VoidType: ...
    
    @overload
    def WriteEntry(self, message: StringType, type: EventLogEntryType) -> VoidType: ...
    
    @overload
    def WriteEntry(self, message: StringType, type: EventLogEntryType, eventID: IntType) -> VoidType: ...
    
    @overload
    def WriteEntry(self, message: StringType, type: EventLogEntryType, eventID: IntType, category: ShortType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteEntry(source: StringType, message: StringType, type: EventLogEntryType, eventID: IntType, category: ShortType, rawData: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def WriteEntry(self, message: StringType, type: EventLogEntryType, eventID: IntType, category: ShortType, rawData: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def WriteEvent(self, instance: EventInstance, values: ArrayType[ObjectType]) -> VoidType: ...
    
    @overload
    def WriteEvent(self, instance: EventInstance, data: ArrayType[ByteType], values: ArrayType[ObjectType]) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteEvent(source: StringType, instance: EventInstance, values: ArrayType[ObjectType]) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteEvent(source: StringType, instance: EventInstance, data: ArrayType[ByteType], values: ArrayType[ObjectType]) -> VoidType: ...
    
    def add_EntryWritten(self, value: EntryWrittenEventHandler) -> VoidType: ...
    
    def get_EnableRaisingEvents(self) -> BooleanType: ...
    
    def get_Entries(self) -> EventLogEntryCollection: ...
    
    def get_Log(self) -> StringType: ...
    
    def get_LogDisplayName(self) -> StringType: ...
    
    def get_MachineName(self) -> StringType: ...
    
    def get_MaximumKilobytes(self) -> LongType: ...
    
    def get_MinimumRetentionDays(self) -> IntType: ...
    
    def get_OverflowAction(self) -> OverflowAction: ...
    
    def get_Source(self) -> StringType: ...
    
    def get_SynchronizingObject(self) -> ISynchronizeInvoke: ...
    
    def remove_EntryWritten(self, value: EntryWrittenEventHandler) -> VoidType: ...
    
    def set_EnableRaisingEvents(self, value: BooleanType) -> VoidType: ...
    
    def set_Log(self, value: StringType) -> VoidType: ...
    
    def set_MachineName(self, value: StringType) -> VoidType: ...
    
    def set_MaximumKilobytes(self, value: LongType) -> VoidType: ...
    
    def set_Source(self, value: StringType) -> VoidType: ...
    
    def set_SynchronizingObject(self, value: ISynchronizeInvoke) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    EntryWritten: EventType[EntryWrittenEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventLogEntry(Component, IComponent, IDisposable, ISerializable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Category(self) -> StringType: ...
    
    @property
    def CategoryNumber(self) -> ShortType: ...
    
    @property
    def Data(self) -> ArrayType[ByteType]: ...
    
    @property
    def EntryType(self) -> EventLogEntryType: ...
    
    @property
    def EventID(self) -> IntType: ...
    
    @property
    def Index(self) -> IntType: ...
    
    @property
    def InstanceId(self) -> LongType: ...
    
    @property
    def MachineName(self) -> StringType: ...
    
    @property
    def Message(self) -> StringType: ...
    
    @property
    def ReplacementStrings(self) -> ArrayType[StringType]: ...
    
    @property
    def Source(self) -> StringType: ...
    
    @property
    def TimeGenerated(self) -> DateTime: ...
    
    @property
    def TimeWritten(self) -> DateTime: ...
    
    @property
    def UserName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, otherEntry: EventLogEntry) -> BooleanType: ...
    
    def get_Category(self) -> StringType: ...
    
    def get_CategoryNumber(self) -> ShortType: ...
    
    def get_Data(self) -> ArrayType[ByteType]: ...
    
    def get_EntryType(self) -> EventLogEntryType: ...
    
    def get_EventID(self) -> IntType: ...
    
    def get_Index(self) -> IntType: ...
    
    def get_InstanceId(self) -> LongType: ...
    
    def get_MachineName(self) -> StringType: ...
    
    def get_Message(self) -> StringType: ...
    
    def get_ReplacementStrings(self) -> ArrayType[StringType]: ...
    
    def get_Source(self) -> StringType: ...
    
    def get_TimeGenerated(self) -> DateTime: ...
    
    def get_TimeWritten(self) -> DateTime: ...
    
    def get_UserName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventLogEntryCollection(ObjectType, ICollection, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Item(self) -> EventLogEntry: ...
    
    # ---------- Methods ---------- #
    
    def CopyTo(self, entries: ArrayType[EventLogEntry], index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Item(self, index: IntType) -> EventLogEntry: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventLogInternal(ObjectType, IDisposable, ISupportInitialize):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, logName: StringType): ...
    
    @overload
    def __init__(self, logName: StringType, machineName: StringType): ...
    
    @overload
    def __init__(self, logName: StringType, machineName: StringType, source: StringType): ...
    
    @overload
    def __init__(self, logName: StringType, machineName: StringType, source: StringType, parent: EventLog): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EnableRaisingEvents(self) -> BooleanType: ...
    
    @EnableRaisingEvents.setter
    def EnableRaisingEvents(self, value: BooleanType) -> None: ...
    
    @property
    def Entries(self) -> EventLogEntryCollection: ...
    
    @property
    def Log(self) -> StringType: ...
    
    @property
    def LogDisplayName(self) -> StringType: ...
    
    @property
    def MachineName(self) -> StringType: ...
    
    @property
    def MaximumKilobytes(self) -> LongType: ...
    
    @MaximumKilobytes.setter
    def MaximumKilobytes(self, value: LongType) -> None: ...
    
    @property
    def MinimumRetentionDays(self) -> IntType: ...
    
    @property
    def OverflowAction(self) -> OverflowAction: ...
    
    @property
    def Source(self) -> StringType: ...
    
    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke: ...
    
    @SynchronizingObject.setter
    def SynchronizingObject(self, value: ISynchronizeInvoke) -> None: ...
    
    # ---------- Methods ---------- #
    
    def BeginInit(self) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Close(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def EndInit(self) -> VoidType: ...
    
    def ModifyOverflowPolicy(self, action: OverflowAction, retentionDays: IntType) -> VoidType: ...
    
    def RegisterDisplayName(self, resourceFile: StringType, resourceId: LongType) -> VoidType: ...
    
    @overload
    def WriteEntry(self, message: StringType) -> VoidType: ...
    
    @overload
    def WriteEntry(self, message: StringType, type: EventLogEntryType) -> VoidType: ...
    
    @overload
    def WriteEntry(self, message: StringType, type: EventLogEntryType, eventID: IntType) -> VoidType: ...
    
    @overload
    def WriteEntry(self, message: StringType, type: EventLogEntryType, eventID: IntType, category: ShortType) -> VoidType: ...
    
    @overload
    def WriteEntry(self, message: StringType, type: EventLogEntryType, eventID: IntType, category: ShortType, rawData: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def WriteEvent(self, instance: EventInstance, values: ArrayType[ObjectType]) -> VoidType: ...
    
    @overload
    def WriteEvent(self, instance: EventInstance, data: ArrayType[ByteType], values: ArrayType[ObjectType]) -> VoidType: ...
    
    def add_EntryWritten(self, value: EntryWrittenEventHandler) -> VoidType: ...
    
    def get_EnableRaisingEvents(self) -> BooleanType: ...
    
    def get_Entries(self) -> EventLogEntryCollection: ...
    
    def get_Log(self) -> StringType: ...
    
    def get_LogDisplayName(self) -> StringType: ...
    
    def get_MachineName(self) -> StringType: ...
    
    def get_MaximumKilobytes(self) -> LongType: ...
    
    def get_MinimumRetentionDays(self) -> IntType: ...
    
    def get_OverflowAction(self) -> OverflowAction: ...
    
    def get_Source(self) -> StringType: ...
    
    def get_SynchronizingObject(self) -> ISynchronizeInvoke: ...
    
    def remove_EntryWritten(self, value: EntryWrittenEventHandler) -> VoidType: ...
    
    def set_EnableRaisingEvents(self, value: BooleanType) -> VoidType: ...
    
    def set_MaximumKilobytes(self, value: LongType) -> VoidType: ...
    
    def set_SynchronizingObject(self, value: ISynchronizeInvoke) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    EntryWritten: EventType[EntryWrittenEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventLogPermission(ResourcePermissionBase, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, permissionAccess: EventLogPermissionAccess, machineName: StringType): ...
    
    @overload
    def __init__(self, permissionAccessEntries: ArrayType[EventLogPermissionEntry]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def PermissionEntries(self) -> EventLogPermissionEntryCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_PermissionEntries(self) -> EventLogPermissionEntryCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventLogPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MachineName(self) -> StringType: ...
    
    @MachineName.setter
    def MachineName(self, value: StringType) -> None: ...
    
    @property
    def PermissionAccess(self) -> EventLogPermissionAccess: ...
    
    @PermissionAccess.setter
    def PermissionAccess(self, value: EventLogPermissionAccess) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def get_MachineName(self) -> StringType: ...
    
    def get_PermissionAccess(self) -> EventLogPermissionAccess: ...
    
    def set_MachineName(self, value: StringType) -> VoidType: ...
    
    def set_PermissionAccess(self, value: EventLogPermissionAccess) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventLogPermissionEntry(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, permissionAccess: EventLogPermissionAccess, machineName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MachineName(self) -> StringType: ...
    
    @property
    def PermissionAccess(self) -> EventLogPermissionAccess: ...
    
    # ---------- Methods ---------- #
    
    def get_MachineName(self) -> StringType: ...
    
    def get_PermissionAccess(self) -> EventLogPermissionAccess: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventLogPermissionEntryCollection(CollectionBase, IList, ICollection, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> EventLogPermissionEntry: ...
    
    @Item.setter
    def Item(self, value: EventLogPermissionEntry) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, value: EventLogPermissionEntry) -> IntType: ...
    
    @overload
    def AddRange(self, value: ArrayType[EventLogPermissionEntry]) -> VoidType: ...
    
    @overload
    def AddRange(self, value: EventLogPermissionEntryCollection) -> VoidType: ...
    
    def Contains(self, value: EventLogPermissionEntry) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[EventLogPermissionEntry], index: IntType) -> VoidType: ...
    
    def IndexOf(self, value: EventLogPermissionEntry) -> IntType: ...
    
    def Insert(self, index: IntType, value: EventLogPermissionEntry) -> VoidType: ...
    
    def Remove(self, value: EventLogPermissionEntry) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> EventLogPermissionEntry: ...
    
    def set_Item(self, index: IntType, value: EventLogPermissionEntry) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventLogTraceListener(TraceListener, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, eventLog: EventLog): ...
    
    @overload
    def __init__(self, source: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EventLog(self) -> EventLog: ...
    
    @EventLog.setter
    def EventLog(self, value: EventLog) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def TraceData(self, eventCache: TraceEventCache, source: StringType, severity: TraceEventType, id: IntType, data: ObjectType) -> VoidType: ...
    
    @overload
    def TraceData(self, eventCache: TraceEventCache, source: StringType, severity: TraceEventType, id: IntType, data: ArrayType[ObjectType]) -> VoidType: ...
    
    @overload
    def TraceEvent(self, eventCache: TraceEventCache, source: StringType, severity: TraceEventType, id: IntType, format: StringType, args: ArrayType[ObjectType]) -> VoidType: ...
    
    @overload
    def TraceEvent(self, eventCache: TraceEventCache, source: StringType, severity: TraceEventType, id: IntType, message: StringType) -> VoidType: ...
    
    @overload
    def Write(self, message: StringType) -> VoidType: ...
    
    @overload
    def WriteLine(self, message: StringType) -> VoidType: ...
    
    def get_EventLog(self) -> EventLog: ...
    
    def get_Name(self) -> StringType: ...
    
    def set_EventLog(self, value: EventLog) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventSourceCreationData(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, source: StringType, logName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CategoryCount(self) -> IntType: ...
    
    @CategoryCount.setter
    def CategoryCount(self, value: IntType) -> None: ...
    
    @property
    def CategoryResourceFile(self) -> StringType: ...
    
    @CategoryResourceFile.setter
    def CategoryResourceFile(self, value: StringType) -> None: ...
    
    @property
    def LogName(self) -> StringType: ...
    
    @LogName.setter
    def LogName(self, value: StringType) -> None: ...
    
    @property
    def MachineName(self) -> StringType: ...
    
    @MachineName.setter
    def MachineName(self, value: StringType) -> None: ...
    
    @property
    def MessageResourceFile(self) -> StringType: ...
    
    @MessageResourceFile.setter
    def MessageResourceFile(self, value: StringType) -> None: ...
    
    @property
    def ParameterResourceFile(self) -> StringType: ...
    
    @ParameterResourceFile.setter
    def ParameterResourceFile(self, value: StringType) -> None: ...
    
    @property
    def Source(self) -> StringType: ...
    
    @Source.setter
    def Source(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_CategoryCount(self) -> IntType: ...
    
    def get_CategoryResourceFile(self) -> StringType: ...
    
    def get_LogName(self) -> StringType: ...
    
    def get_MachineName(self) -> StringType: ...
    
    def get_MessageResourceFile(self) -> StringType: ...
    
    def get_ParameterResourceFile(self) -> StringType: ...
    
    def get_Source(self) -> StringType: ...
    
    def set_CategoryCount(self, value: IntType) -> VoidType: ...
    
    def set_CategoryResourceFile(self, value: StringType) -> VoidType: ...
    
    def set_LogName(self, value: StringType) -> VoidType: ...
    
    def set_MachineName(self, value: StringType) -> VoidType: ...
    
    def set_MessageResourceFile(self, value: StringType) -> VoidType: ...
    
    def set_ParameterResourceFile(self, value: StringType) -> VoidType: ...
    
    def set_Source(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventTypeFilter(TraceFilter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, level: SourceLevels): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EventType(self) -> SourceLevels: ...
    
    @EventType.setter
    def EventType(self, value: SourceLevels) -> None: ...
    
    # ---------- Methods ---------- #
    
    def ShouldTrace(self, cache: TraceEventCache, source: StringType, eventType: TraceEventType, id: IntType, formatOrMessage: StringType, args: ArrayType[ObjectType], data1: ObjectType, data: ArrayType[ObjectType]) -> BooleanType: ...
    
    def get_EventType(self) -> SourceLevels: ...
    
    def set_EventType(self, value: SourceLevels) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileVersionInfo(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Comments(self) -> StringType: ...
    
    @property
    def CompanyName(self) -> StringType: ...
    
    @property
    def FileBuildPart(self) -> IntType: ...
    
    @property
    def FileDescription(self) -> StringType: ...
    
    @property
    def FileMajorPart(self) -> IntType: ...
    
    @property
    def FileMinorPart(self) -> IntType: ...
    
    @property
    def FileName(self) -> StringType: ...
    
    @property
    def FilePrivatePart(self) -> IntType: ...
    
    @property
    def FileVersion(self) -> StringType: ...
    
    @property
    def InternalName(self) -> StringType: ...
    
    @property
    def IsDebug(self) -> BooleanType: ...
    
    @property
    def IsPatched(self) -> BooleanType: ...
    
    @property
    def IsPreRelease(self) -> BooleanType: ...
    
    @property
    def IsPrivateBuild(self) -> BooleanType: ...
    
    @property
    def IsSpecialBuild(self) -> BooleanType: ...
    
    @property
    def Language(self) -> StringType: ...
    
    @property
    def LegalCopyright(self) -> StringType: ...
    
    @property
    def LegalTrademarks(self) -> StringType: ...
    
    @property
    def OriginalFilename(self) -> StringType: ...
    
    @property
    def PrivateBuild(self) -> StringType: ...
    
    @property
    def ProductBuildPart(self) -> IntType: ...
    
    @property
    def ProductMajorPart(self) -> IntType: ...
    
    @property
    def ProductMinorPart(self) -> IntType: ...
    
    @property
    def ProductName(self) -> StringType: ...
    
    @property
    def ProductPrivatePart(self) -> IntType: ...
    
    @property
    def ProductVersion(self) -> StringType: ...
    
    @property
    def SpecialBuild(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetVersionInfo(fileName: StringType) -> FileVersionInfo: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Comments(self) -> StringType: ...
    
    def get_CompanyName(self) -> StringType: ...
    
    def get_FileBuildPart(self) -> IntType: ...
    
    def get_FileDescription(self) -> StringType: ...
    
    def get_FileMajorPart(self) -> IntType: ...
    
    def get_FileMinorPart(self) -> IntType: ...
    
    def get_FileName(self) -> StringType: ...
    
    def get_FilePrivatePart(self) -> IntType: ...
    
    def get_FileVersion(self) -> StringType: ...
    
    def get_InternalName(self) -> StringType: ...
    
    def get_IsDebug(self) -> BooleanType: ...
    
    def get_IsPatched(self) -> BooleanType: ...
    
    def get_IsPreRelease(self) -> BooleanType: ...
    
    def get_IsPrivateBuild(self) -> BooleanType: ...
    
    def get_IsSpecialBuild(self) -> BooleanType: ...
    
    def get_Language(self) -> StringType: ...
    
    def get_LegalCopyright(self) -> StringType: ...
    
    def get_LegalTrademarks(self) -> StringType: ...
    
    def get_OriginalFilename(self) -> StringType: ...
    
    def get_PrivateBuild(self) -> StringType: ...
    
    def get_ProductBuildPart(self) -> IntType: ...
    
    def get_ProductMajorPart(self) -> IntType: ...
    
    def get_ProductMinorPart(self) -> IntType: ...
    
    def get_ProductName(self) -> StringType: ...
    
    def get_ProductPrivatePart(self) -> IntType: ...
    
    def get_ProductVersion(self) -> StringType: ...
    
    def get_SpecialBuild(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FilterElement(TypedElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetRuntimeObject(self) -> TraceFilter: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InstanceData(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, instanceName: StringType, sample: CounterSample): ...
    
    # ---------- Properties ---------- #
    
    @property
    def InstanceName(self) -> StringType: ...
    
    @property
    def RawValue(self) -> LongType: ...
    
    @property
    def Sample(self) -> CounterSample: ...
    
    # ---------- Methods ---------- #
    
    def get_InstanceName(self) -> StringType: ...
    
    def get_RawValue(self) -> LongType: ...
    
    def get_Sample(self) -> CounterSample: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InstanceDataCollection(DictionaryBase, IDictionary, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, counterName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CounterName(self) -> StringType: ...
    
    @property
    def Item(self) -> InstanceData: ...
    
    @property
    def Keys(self) -> ICollection: ...
    
    @property
    def Values(self) -> ICollection: ...
    
    # ---------- Methods ---------- #
    
    def Contains(self, instanceName: StringType) -> BooleanType: ...
    
    @overload
    def CopyTo(self, instances: ArrayType[InstanceData], index: IntType) -> VoidType: ...
    
    def get_CounterName(self) -> StringType: ...
    
    def get_Item(self, instanceName: StringType) -> InstanceData: ...
    
    def get_Keys(self) -> ICollection: ...
    
    def get_Values(self) -> ICollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InstanceDataCollectionCollection(DictionaryBase, IDictionary, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> InstanceDataCollection: ...
    
    @property
    def Keys(self) -> ICollection: ...
    
    @property
    def Values(self) -> ICollection: ...
    
    # ---------- Methods ---------- #
    
    def Contains(self, counterName: StringType) -> BooleanType: ...
    
    @overload
    def CopyTo(self, counters: ArrayType[InstanceDataCollection], index: IntType) -> VoidType: ...
    
    def get_Item(self, counterName: StringType) -> InstanceDataCollection: ...
    
    def get_Keys(self) -> ICollection: ...
    
    def get_Values(self) -> ICollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ListenerElement(TypedElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, allowReferences: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> Hashtable: ...
    
    @property
    def Filter(self) -> FilterElement: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def TraceOutputOptions(self) -> TraceOptions: ...
    
    @TraceOutputOptions.setter
    def TraceOutputOptions(self, value: TraceOptions) -> None: ...
    
    @property
    def TypeName(self) -> StringType: ...
    
    @TypeName.setter
    def TypeName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, compareTo: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetRuntimeObject(self) -> TraceListener: ...
    
    def get_Attributes(self) -> Hashtable: ...
    
    def get_Filter(self) -> FilterElement: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_TraceOutputOptions(self) -> TraceOptions: ...
    
    def get_TypeName(self) -> StringType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_TraceOutputOptions(self, value: TraceOptions) -> VoidType: ...
    
    def set_TypeName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ListenerElementsCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CollectionType(self) -> ConfigurationElementCollectionType: ...
    
    @property
    def Item(self) -> ListenerElement: ...
    
    # ---------- Methods ---------- #
    
    def GetRuntimeObject(self) -> TraceListenerCollection: ...
    
    def get_CollectionType(self) -> ConfigurationElementCollectionType: ...
    
    def get_Item(self, name: StringType) -> ListenerElement: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MainWindowFinder(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def FindMainWindow(self, processId: IntType) -> NIntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MessageBoxPopup(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, body: StringType, title: StringType, flags: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ReturnValue(self) -> IntType: ...
    
    @ReturnValue.setter
    def ReturnValue(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def DoPopup(self) -> VoidType: ...
    
    def ShowMessageBox(self) -> IntType: ...
    
    def get_ReturnValue(self) -> IntType: ...
    
    def set_ReturnValue(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ModuleInfo(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Id(self) -> IntType: ...
    
    @Id.setter
    def Id(self, value: IntType) -> None: ...
    
    @property
    def baseName(self) -> StringType: ...
    
    @baseName.setter
    def baseName(self, value: StringType) -> None: ...
    
    @property
    def baseOfDll(self) -> NIntType: ...
    
    @baseOfDll.setter
    def baseOfDll(self, value: NIntType) -> None: ...
    
    @property
    def entryPoint(self) -> NIntType: ...
    
    @entryPoint.setter
    def entryPoint(self, value: NIntType) -> None: ...
    
    @property
    def fileName(self) -> StringType: ...
    
    @fileName.setter
    def fileName(self, value: StringType) -> None: ...
    
    @property
    def sizeOfImage(self) -> IntType: ...
    
    @sizeOfImage.setter
    def sizeOfImage(self, value: IntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MonitoringDescriptionAttribute(DescriptionAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, description: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Description(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Description(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NtProcessInfoHelper(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetProcessInfos(processIdFilter: Predicate[IntType]) -> ArrayType[ProcessInfo]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NtProcessManager(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetFirstModuleInfo(processId: IntType) -> ModuleInfo: ...
    
    @staticmethod
    def GetModuleInfos(processId: IntType) -> ArrayType[ModuleInfo]: ...
    
    @staticmethod
    def GetProcessIdFromHandle(processHandle: SafeProcessHandle) -> IntType: ...
    
    @staticmethod
    @overload
    def GetProcessIds() -> ArrayType[IntType]: ...
    
    @staticmethod
    @overload
    def GetProcessIds(machineName: StringType, isRemoteMachine: BooleanType) -> ArrayType[IntType]: ...
    
    @staticmethod
    def GetProcessInfos(machineName: StringType, isRemoteMachine: BooleanType) -> ArrayType[ProcessInfo]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OrdinalCaseInsensitiveComparer(ObjectType, IComparer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Compare(self, a: ObjectType, b: ObjectType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PerfCounterSection(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def FileMappingSize(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_FileMappingSize(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PerformanceCounter(Component, IComponent, IDisposable, ISupportInitialize):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def DefaultFileMappingSize() -> IntType: ...
    
    @staticmethod
    @DefaultFileMappingSize.setter
    def DefaultFileMappingSize(value: IntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, categoryName: StringType, counterName: StringType, instanceName: StringType, machineName: StringType): ...
    
    @overload
    def __init__(self, categoryName: StringType, counterName: StringType, instanceName: StringType): ...
    
    @overload
    def __init__(self, categoryName: StringType, counterName: StringType, instanceName: StringType, readOnly: BooleanType): ...
    
    @overload
    def __init__(self, categoryName: StringType, counterName: StringType): ...
    
    @overload
    def __init__(self, categoryName: StringType, counterName: StringType, readOnly: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CategoryName(self) -> StringType: ...
    
    @CategoryName.setter
    def CategoryName(self, value: StringType) -> None: ...
    
    @property
    def CounterHelp(self) -> StringType: ...
    
    @property
    def CounterName(self) -> StringType: ...
    
    @CounterName.setter
    def CounterName(self, value: StringType) -> None: ...
    
    @property
    def CounterType(self) -> PerformanceCounterType: ...
    
    @property
    def InstanceLifetime(self) -> PerformanceCounterInstanceLifetime: ...
    
    @InstanceLifetime.setter
    def InstanceLifetime(self, value: PerformanceCounterInstanceLifetime) -> None: ...
    
    @property
    def InstanceName(self) -> StringType: ...
    
    @InstanceName.setter
    def InstanceName(self, value: StringType) -> None: ...
    
    @property
    def MachineName(self) -> StringType: ...
    
    @MachineName.setter
    def MachineName(self, value: StringType) -> None: ...
    
    @property
    def RawValue(self) -> LongType: ...
    
    @RawValue.setter
    def RawValue(self, value: LongType) -> None: ...
    
    @property
    def ReadOnly(self) -> BooleanType: ...
    
    @ReadOnly.setter
    def ReadOnly(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def BeginInit(self) -> VoidType: ...
    
    def Close(self) -> VoidType: ...
    
    @staticmethod
    def CloseSharedResources() -> VoidType: ...
    
    def Decrement(self) -> LongType: ...
    
    def EndInit(self) -> VoidType: ...
    
    def Increment(self) -> LongType: ...
    
    def IncrementBy(self, value: LongType) -> LongType: ...
    
    def NextSample(self) -> CounterSample: ...
    
    def NextValue(self) -> FloatType: ...
    
    def RemoveInstance(self) -> VoidType: ...
    
    def get_CategoryName(self) -> StringType: ...
    
    def get_CounterHelp(self) -> StringType: ...
    
    def get_CounterName(self) -> StringType: ...
    
    def get_CounterType(self) -> PerformanceCounterType: ...
    
    def get_InstanceLifetime(self) -> PerformanceCounterInstanceLifetime: ...
    
    def get_InstanceName(self) -> StringType: ...
    
    def get_MachineName(self) -> StringType: ...
    
    def get_RawValue(self) -> LongType: ...
    
    def get_ReadOnly(self) -> BooleanType: ...
    
    def set_CategoryName(self, value: StringType) -> VoidType: ...
    
    def set_CounterName(self, value: StringType) -> VoidType: ...
    
    def set_InstanceLifetime(self, value: PerformanceCounterInstanceLifetime) -> VoidType: ...
    
    def set_InstanceName(self, value: StringType) -> VoidType: ...
    
    def set_MachineName(self, value: StringType) -> VoidType: ...
    
    def set_RawValue(self, value: LongType) -> VoidType: ...
    
    def set_ReadOnly(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PerformanceCounterCategory(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, categoryName: StringType): ...
    
    @overload
    def __init__(self, categoryName: StringType, machineName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CategoryHelp(self) -> StringType: ...
    
    @property
    def CategoryName(self) -> StringType: ...
    
    @CategoryName.setter
    def CategoryName(self, value: StringType) -> None: ...
    
    @property
    def CategoryType(self) -> PerformanceCounterCategoryType: ...
    
    @property
    def MachineName(self) -> StringType: ...
    
    @MachineName.setter
    def MachineName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def CounterExists(self, counterName: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def CounterExists(counterName: StringType, categoryName: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def CounterExists(counterName: StringType, categoryName: StringType, machineName: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Create(categoryName: StringType, categoryHelp: StringType, counterData: CounterCreationDataCollection) -> PerformanceCounterCategory: ...
    
    @staticmethod
    @overload
    def Create(categoryName: StringType, categoryHelp: StringType, counterName: StringType, counterHelp: StringType) -> PerformanceCounterCategory: ...
    
    @staticmethod
    @overload
    def Create(categoryName: StringType, categoryHelp: StringType, categoryType: PerformanceCounterCategoryType, counterName: StringType, counterHelp: StringType) -> PerformanceCounterCategory: ...
    
    @staticmethod
    @overload
    def Create(categoryName: StringType, categoryHelp: StringType, categoryType: PerformanceCounterCategoryType, counterData: CounterCreationDataCollection) -> PerformanceCounterCategory: ...
    
    @staticmethod
    def Delete(categoryName: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Exists(categoryName: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Exists(categoryName: StringType, machineName: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def GetCategories() -> ArrayType[PerformanceCounterCategory]: ...
    
    @staticmethod
    @overload
    def GetCategories(machineName: StringType) -> ArrayType[PerformanceCounterCategory]: ...
    
    @overload
    def GetCounters(self) -> ArrayType[PerformanceCounter]: ...
    
    @overload
    def GetCounters(self, instanceName: StringType) -> ArrayType[PerformanceCounter]: ...
    
    def GetInstanceNames(self) -> ArrayType[StringType]: ...
    
    @overload
    def InstanceExists(self, instanceName: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def InstanceExists(instanceName: StringType, categoryName: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def InstanceExists(instanceName: StringType, categoryName: StringType, machineName: StringType) -> BooleanType: ...
    
    def ReadCategory(self) -> InstanceDataCollectionCollection: ...
    
    def get_CategoryHelp(self) -> StringType: ...
    
    def get_CategoryName(self) -> StringType: ...
    
    def get_CategoryType(self) -> PerformanceCounterCategoryType: ...
    
    def get_MachineName(self) -> StringType: ...
    
    def set_CategoryName(self, value: StringType) -> VoidType: ...
    
    def set_MachineName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PerformanceCounterLib(ObjectType):
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


class PerformanceCounterManager(ObjectType, ICollectData):
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


class PerformanceCounterPermission(ResourcePermissionBase, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, permissionAccess: PerformanceCounterPermissionAccess, machineName: StringType, categoryName: StringType): ...
    
    @overload
    def __init__(self, permissionAccessEntries: ArrayType[PerformanceCounterPermissionEntry]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def PermissionEntries(self) -> PerformanceCounterPermissionEntryCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_PermissionEntries(self) -> PerformanceCounterPermissionEntryCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PerformanceCounterPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CategoryName(self) -> StringType: ...
    
    @CategoryName.setter
    def CategoryName(self, value: StringType) -> None: ...
    
    @property
    def MachineName(self) -> StringType: ...
    
    @MachineName.setter
    def MachineName(self, value: StringType) -> None: ...
    
    @property
    def PermissionAccess(self) -> PerformanceCounterPermissionAccess: ...
    
    @PermissionAccess.setter
    def PermissionAccess(self, value: PerformanceCounterPermissionAccess) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def get_CategoryName(self) -> StringType: ...
    
    def get_MachineName(self) -> StringType: ...
    
    def get_PermissionAccess(self) -> PerformanceCounterPermissionAccess: ...
    
    def set_CategoryName(self, value: StringType) -> VoidType: ...
    
    def set_MachineName(self, value: StringType) -> VoidType: ...
    
    def set_PermissionAccess(self, value: PerformanceCounterPermissionAccess) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PerformanceCounterPermissionEntry(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, permissionAccess: PerformanceCounterPermissionAccess, machineName: StringType, categoryName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CategoryName(self) -> StringType: ...
    
    @property
    def MachineName(self) -> StringType: ...
    
    @property
    def PermissionAccess(self) -> PerformanceCounterPermissionAccess: ...
    
    # ---------- Methods ---------- #
    
    def get_CategoryName(self) -> StringType: ...
    
    def get_MachineName(self) -> StringType: ...
    
    def get_PermissionAccess(self) -> PerformanceCounterPermissionAccess: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PerformanceCounterPermissionEntryCollection(CollectionBase, IList, ICollection, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> PerformanceCounterPermissionEntry: ...
    
    @Item.setter
    def Item(self, value: PerformanceCounterPermissionEntry) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, value: PerformanceCounterPermissionEntry) -> IntType: ...
    
    @overload
    def AddRange(self, value: ArrayType[PerformanceCounterPermissionEntry]) -> VoidType: ...
    
    @overload
    def AddRange(self, value: PerformanceCounterPermissionEntryCollection) -> VoidType: ...
    
    def Contains(self, value: PerformanceCounterPermissionEntry) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[PerformanceCounterPermissionEntry], index: IntType) -> VoidType: ...
    
    def IndexOf(self, value: PerformanceCounterPermissionEntry) -> IntType: ...
    
    def Insert(self, index: IntType, value: PerformanceCounterPermissionEntry) -> VoidType: ...
    
    def Remove(self, value: PerformanceCounterPermissionEntry) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> PerformanceCounterPermissionEntry: ...
    
    def set_Item(self, index: IntType, value: PerformanceCounterPermissionEntry) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PerformanceMonitor(ObjectType):
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


class Process(Component, IComponent, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BasePriority(self) -> IntType: ...
    
    @property
    def EnableRaisingEvents(self) -> BooleanType: ...
    
    @EnableRaisingEvents.setter
    def EnableRaisingEvents(self, value: BooleanType) -> None: ...
    
    @property
    def ExitCode(self) -> IntType: ...
    
    @property
    def ExitTime(self) -> DateTime: ...
    
    @property
    def Handle(self) -> NIntType: ...
    
    @property
    def HandleCount(self) -> IntType: ...
    
    @property
    def HasExited(self) -> BooleanType: ...
    
    @property
    def Id(self) -> IntType: ...
    
    @property
    def MachineName(self) -> StringType: ...
    
    @property
    def MainModule(self) -> ProcessModule: ...
    
    @property
    def MainWindowHandle(self) -> NIntType: ...
    
    @property
    def MainWindowTitle(self) -> StringType: ...
    
    @property
    def MaxWorkingSet(self) -> NIntType: ...
    
    @MaxWorkingSet.setter
    def MaxWorkingSet(self, value: NIntType) -> None: ...
    
    @property
    def MinWorkingSet(self) -> NIntType: ...
    
    @MinWorkingSet.setter
    def MinWorkingSet(self, value: NIntType) -> None: ...
    
    @property
    def Modules(self) -> ProcessModuleCollection: ...
    
    @property
    def NonpagedSystemMemorySize(self) -> IntType: ...
    
    @property
    def NonpagedSystemMemorySize64(self) -> LongType: ...
    
    @property
    def PagedMemorySize(self) -> IntType: ...
    
    @property
    def PagedMemorySize64(self) -> LongType: ...
    
    @property
    def PagedSystemMemorySize(self) -> IntType: ...
    
    @property
    def PagedSystemMemorySize64(self) -> LongType: ...
    
    @property
    def PeakPagedMemorySize(self) -> IntType: ...
    
    @property
    def PeakPagedMemorySize64(self) -> LongType: ...
    
    @property
    def PeakVirtualMemorySize(self) -> IntType: ...
    
    @property
    def PeakVirtualMemorySize64(self) -> LongType: ...
    
    @property
    def PeakWorkingSet(self) -> IntType: ...
    
    @property
    def PeakWorkingSet64(self) -> LongType: ...
    
    @property
    def PriorityBoostEnabled(self) -> BooleanType: ...
    
    @PriorityBoostEnabled.setter
    def PriorityBoostEnabled(self, value: BooleanType) -> None: ...
    
    @property
    def PriorityClass(self) -> ProcessPriorityClass: ...
    
    @PriorityClass.setter
    def PriorityClass(self, value: ProcessPriorityClass) -> None: ...
    
    @property
    def PrivateMemorySize(self) -> IntType: ...
    
    @property
    def PrivateMemorySize64(self) -> LongType: ...
    
    @property
    def PrivilegedProcessorTime(self) -> TimeSpan: ...
    
    @property
    def ProcessName(self) -> StringType: ...
    
    @property
    def ProcessorAffinity(self) -> NIntType: ...
    
    @ProcessorAffinity.setter
    def ProcessorAffinity(self, value: NIntType) -> None: ...
    
    @property
    def Responding(self) -> BooleanType: ...
    
    @property
    def SafeHandle(self) -> SafeProcessHandle: ...
    
    @property
    def SessionId(self) -> IntType: ...
    
    @property
    def StandardError(self) -> StreamReader: ...
    
    @property
    def StandardInput(self) -> StreamWriter: ...
    
    @property
    def StandardOutput(self) -> StreamReader: ...
    
    @property
    def StartInfo(self) -> ProcessStartInfo: ...
    
    @StartInfo.setter
    def StartInfo(self, value: ProcessStartInfo) -> None: ...
    
    @property
    def StartTime(self) -> DateTime: ...
    
    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke: ...
    
    @SynchronizingObject.setter
    def SynchronizingObject(self, value: ISynchronizeInvoke) -> None: ...
    
    @property
    def Threads(self) -> ProcessThreadCollection: ...
    
    @property
    def TotalProcessorTime(self) -> TimeSpan: ...
    
    @property
    def UserProcessorTime(self) -> TimeSpan: ...
    
    @property
    def VirtualMemorySize(self) -> IntType: ...
    
    @property
    def VirtualMemorySize64(self) -> LongType: ...
    
    @property
    def WorkingSet(self) -> IntType: ...
    
    @property
    def WorkingSet64(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def BeginErrorReadLine(self) -> VoidType: ...
    
    def BeginOutputReadLine(self) -> VoidType: ...
    
    def CancelErrorRead(self) -> VoidType: ...
    
    def CancelOutputRead(self) -> VoidType: ...
    
    def Close(self) -> VoidType: ...
    
    def CloseMainWindow(self) -> BooleanType: ...
    
    @staticmethod
    def EnterDebugMode() -> VoidType: ...
    
    @staticmethod
    def GetCurrentProcess() -> Process: ...
    
    @staticmethod
    @overload
    def GetProcessById(processId: IntType, machineName: StringType) -> Process: ...
    
    @staticmethod
    @overload
    def GetProcessById(processId: IntType) -> Process: ...
    
    @staticmethod
    @overload
    def GetProcesses() -> ArrayType[Process]: ...
    
    @staticmethod
    @overload
    def GetProcesses(machineName: StringType) -> ArrayType[Process]: ...
    
    @staticmethod
    @overload
    def GetProcessesByName(processName: StringType) -> ArrayType[Process]: ...
    
    @staticmethod
    @overload
    def GetProcessesByName(processName: StringType, machineName: StringType) -> ArrayType[Process]: ...
    
    def Kill(self) -> VoidType: ...
    
    @staticmethod
    def LeaveDebugMode() -> VoidType: ...
    
    def Refresh(self) -> VoidType: ...
    
    @staticmethod
    @overload
    def Start(fileName: StringType, userName: StringType, password: SecureString, domain: StringType) -> Process: ...
    
    @staticmethod
    @overload
    def Start(fileName: StringType, arguments: StringType, userName: StringType, password: SecureString, domain: StringType) -> Process: ...
    
    @staticmethod
    @overload
    def Start(fileName: StringType) -> Process: ...
    
    @staticmethod
    @overload
    def Start(fileName: StringType, arguments: StringType) -> Process: ...
    
    @staticmethod
    @overload
    def Start(startInfo: ProcessStartInfo) -> Process: ...
    
    @overload
    def Start(self) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def WaitForExit(self, milliseconds: IntType) -> BooleanType: ...
    
    @overload
    def WaitForExit(self) -> VoidType: ...
    
    @overload
    def WaitForInputIdle(self, milliseconds: IntType) -> BooleanType: ...
    
    @overload
    def WaitForInputIdle(self) -> BooleanType: ...
    
    def add_ErrorDataReceived(self, value: DataReceivedEventHandler) -> VoidType: ...
    
    def add_Exited(self, value: EventHandler) -> VoidType: ...
    
    def add_OutputDataReceived(self, value: DataReceivedEventHandler) -> VoidType: ...
    
    def get_BasePriority(self) -> IntType: ...
    
    def get_EnableRaisingEvents(self) -> BooleanType: ...
    
    def get_ExitCode(self) -> IntType: ...
    
    def get_ExitTime(self) -> DateTime: ...
    
    def get_Handle(self) -> NIntType: ...
    
    def get_HandleCount(self) -> IntType: ...
    
    def get_HasExited(self) -> BooleanType: ...
    
    def get_Id(self) -> IntType: ...
    
    def get_MachineName(self) -> StringType: ...
    
    def get_MainModule(self) -> ProcessModule: ...
    
    def get_MainWindowHandle(self) -> NIntType: ...
    
    def get_MainWindowTitle(self) -> StringType: ...
    
    def get_MaxWorkingSet(self) -> NIntType: ...
    
    def get_MinWorkingSet(self) -> NIntType: ...
    
    def get_Modules(self) -> ProcessModuleCollection: ...
    
    def get_NonpagedSystemMemorySize(self) -> IntType: ...
    
    def get_NonpagedSystemMemorySize64(self) -> LongType: ...
    
    def get_PagedMemorySize(self) -> IntType: ...
    
    def get_PagedMemorySize64(self) -> LongType: ...
    
    def get_PagedSystemMemorySize(self) -> IntType: ...
    
    def get_PagedSystemMemorySize64(self) -> LongType: ...
    
    def get_PeakPagedMemorySize(self) -> IntType: ...
    
    def get_PeakPagedMemorySize64(self) -> LongType: ...
    
    def get_PeakVirtualMemorySize(self) -> IntType: ...
    
    def get_PeakVirtualMemorySize64(self) -> LongType: ...
    
    def get_PeakWorkingSet(self) -> IntType: ...
    
    def get_PeakWorkingSet64(self) -> LongType: ...
    
    def get_PriorityBoostEnabled(self) -> BooleanType: ...
    
    def get_PriorityClass(self) -> ProcessPriorityClass: ...
    
    def get_PrivateMemorySize(self) -> IntType: ...
    
    def get_PrivateMemorySize64(self) -> LongType: ...
    
    def get_PrivilegedProcessorTime(self) -> TimeSpan: ...
    
    def get_ProcessName(self) -> StringType: ...
    
    def get_ProcessorAffinity(self) -> NIntType: ...
    
    def get_Responding(self) -> BooleanType: ...
    
    def get_SafeHandle(self) -> SafeProcessHandle: ...
    
    def get_SessionId(self) -> IntType: ...
    
    def get_StandardError(self) -> StreamReader: ...
    
    def get_StandardInput(self) -> StreamWriter: ...
    
    def get_StandardOutput(self) -> StreamReader: ...
    
    def get_StartInfo(self) -> ProcessStartInfo: ...
    
    def get_StartTime(self) -> DateTime: ...
    
    def get_SynchronizingObject(self) -> ISynchronizeInvoke: ...
    
    def get_Threads(self) -> ProcessThreadCollection: ...
    
    def get_TotalProcessorTime(self) -> TimeSpan: ...
    
    def get_UserProcessorTime(self) -> TimeSpan: ...
    
    def get_VirtualMemorySize(self) -> IntType: ...
    
    def get_VirtualMemorySize64(self) -> LongType: ...
    
    def get_WorkingSet(self) -> IntType: ...
    
    def get_WorkingSet64(self) -> LongType: ...
    
    def remove_ErrorDataReceived(self, value: DataReceivedEventHandler) -> VoidType: ...
    
    def remove_Exited(self, value: EventHandler) -> VoidType: ...
    
    def remove_OutputDataReceived(self, value: DataReceivedEventHandler) -> VoidType: ...
    
    def set_EnableRaisingEvents(self, value: BooleanType) -> VoidType: ...
    
    def set_MaxWorkingSet(self, value: NIntType) -> VoidType: ...
    
    def set_MinWorkingSet(self, value: NIntType) -> VoidType: ...
    
    def set_PriorityBoostEnabled(self, value: BooleanType) -> VoidType: ...
    
    def set_PriorityClass(self, value: ProcessPriorityClass) -> VoidType: ...
    
    def set_ProcessorAffinity(self, value: NIntType) -> VoidType: ...
    
    def set_StartInfo(self, value: ProcessStartInfo) -> VoidType: ...
    
    def set_SynchronizingObject(self, value: ISynchronizeInvoke) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    ErrorDataReceived: EventType[DataReceivedEventHandler] = ...
    
    Exited: EventType[EventHandler] = ...
    
    OutputDataReceived: EventType[DataReceivedEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ProcessData(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def ProcessId(self) -> IntType: ...
    
    @ProcessId.setter
    def ProcessId(self, value: IntType) -> None: ...
    
    @property
    def StartupTime(self) -> LongType: ...
    
    @StartupTime.setter
    def StartupTime(self, value: LongType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, pid: IntType, startTime: LongType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ProcessInfo(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def basePriority(self) -> IntType: ...
    
    @basePriority.setter
    def basePriority(self, value: IntType) -> None: ...
    
    @property
    def handleCount(self) -> IntType: ...
    
    @handleCount.setter
    def handleCount(self, value: IntType) -> None: ...
    
    @property
    def mainModuleId(self) -> IntType: ...
    
    @mainModuleId.setter
    def mainModuleId(self, value: IntType) -> None: ...
    
    @property
    def pageFileBytes(self) -> LongType: ...
    
    @pageFileBytes.setter
    def pageFileBytes(self, value: LongType) -> None: ...
    
    @property
    def pageFileBytesPeak(self) -> LongType: ...
    
    @pageFileBytesPeak.setter
    def pageFileBytesPeak(self, value: LongType) -> None: ...
    
    @property
    def poolNonpagedBytes(self) -> LongType: ...
    
    @poolNonpagedBytes.setter
    def poolNonpagedBytes(self, value: LongType) -> None: ...
    
    @property
    def poolPagedBytes(self) -> LongType: ...
    
    @poolPagedBytes.setter
    def poolPagedBytes(self, value: LongType) -> None: ...
    
    @property
    def privateBytes(self) -> LongType: ...
    
    @privateBytes.setter
    def privateBytes(self, value: LongType) -> None: ...
    
    @property
    def processId(self) -> IntType: ...
    
    @processId.setter
    def processId(self, value: IntType) -> None: ...
    
    @property
    def processName(self) -> StringType: ...
    
    @processName.setter
    def processName(self, value: StringType) -> None: ...
    
    @property
    def sessionId(self) -> IntType: ...
    
    @sessionId.setter
    def sessionId(self, value: IntType) -> None: ...
    
    @property
    def threadInfoList(self) -> ArrayList: ...
    
    @threadInfoList.setter
    def threadInfoList(self, value: ArrayList) -> None: ...
    
    @property
    def virtualBytes(self) -> LongType: ...
    
    @virtualBytes.setter
    def virtualBytes(self, value: LongType) -> None: ...
    
    @property
    def virtualBytesPeak(self) -> LongType: ...
    
    @virtualBytesPeak.setter
    def virtualBytesPeak(self, value: LongType) -> None: ...
    
    @property
    def workingSet(self) -> LongType: ...
    
    @workingSet.setter
    def workingSet(self, value: LongType) -> None: ...
    
    @property
    def workingSetPeak(self) -> LongType: ...
    
    @workingSetPeak.setter
    def workingSetPeak(self, value: LongType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ProcessManager(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def IsNt() -> BooleanType: ...
    
    @staticmethod
    @property
    def IsOSOlderThanXP() -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetMainWindowHandle(processId: IntType) -> NIntType: ...
    
    @staticmethod
    def GetModuleInfos(processId: IntType) -> ArrayType[ModuleInfo]: ...
    
    @staticmethod
    def GetProcessIdFromHandle(processHandle: SafeProcessHandle) -> IntType: ...
    
    @staticmethod
    @overload
    def GetProcessIds() -> ArrayType[IntType]: ...
    
    @staticmethod
    @overload
    def GetProcessIds(machineName: StringType) -> ArrayType[IntType]: ...
    
    @staticmethod
    def GetProcessInfo(processId: IntType, machineName: StringType) -> ProcessInfo: ...
    
    @staticmethod
    def GetProcessInfos(machineName: StringType) -> ArrayType[ProcessInfo]: ...
    
    @staticmethod
    @overload
    def IsProcessRunning(processId: IntType, machineName: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsProcessRunning(processId: IntType) -> BooleanType: ...
    
    @staticmethod
    def IsRemoteMachine(machineName: StringType) -> BooleanType: ...
    
    @staticmethod
    def OpenProcess(processId: IntType, access: IntType, throwIfExited: BooleanType) -> SafeProcessHandle: ...
    
    @staticmethod
    def OpenThread(threadId: IntType, access: IntType) -> SafeThreadHandle: ...
    
    @staticmethod
    def get_IsNt() -> BooleanType: ...
    
    @staticmethod
    def get_IsOSOlderThanXP() -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ProcessModule(Component, IComponent, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BaseAddress(self) -> NIntType: ...
    
    @property
    def EntryPointAddress(self) -> NIntType: ...
    
    @property
    def FileName(self) -> StringType: ...
    
    @property
    def FileVersionInfo(self) -> FileVersionInfo: ...
    
    @property
    def ModuleMemorySize(self) -> IntType: ...
    
    @property
    def ModuleName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    def get_BaseAddress(self) -> NIntType: ...
    
    def get_EntryPointAddress(self) -> NIntType: ...
    
    def get_FileName(self) -> StringType: ...
    
    def get_FileVersionInfo(self) -> FileVersionInfo: ...
    
    def get_ModuleMemorySize(self) -> IntType: ...
    
    def get_ModuleName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ProcessModuleCollection(ReadOnlyCollectionBase, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, processModules: ArrayType[ProcessModule]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> ProcessModule: ...
    
    # ---------- Methods ---------- #
    
    def Contains(self, module: ProcessModule) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[ProcessModule], index: IntType) -> VoidType: ...
    
    def IndexOf(self, module: ProcessModule) -> IntType: ...
    
    def get_Item(self, index: IntType) -> ProcessModule: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ProcessStartInfo(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, fileName: StringType): ...
    
    @overload
    def __init__(self, fileName: StringType, arguments: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Arguments(self) -> StringType: ...
    
    @Arguments.setter
    def Arguments(self, value: StringType) -> None: ...
    
    @property
    def CreateNoWindow(self) -> BooleanType: ...
    
    @CreateNoWindow.setter
    def CreateNoWindow(self, value: BooleanType) -> None: ...
    
    @property
    def Domain(self) -> StringType: ...
    
    @Domain.setter
    def Domain(self, value: StringType) -> None: ...
    
    @property
    def Environment(self) -> IDictionary[StringType, StringType]: ...
    
    @property
    def EnvironmentVariables(self) -> StringDictionary: ...
    
    @property
    def ErrorDialog(self) -> BooleanType: ...
    
    @ErrorDialog.setter
    def ErrorDialog(self, value: BooleanType) -> None: ...
    
    @property
    def ErrorDialogParentHandle(self) -> NIntType: ...
    
    @ErrorDialogParentHandle.setter
    def ErrorDialogParentHandle(self, value: NIntType) -> None: ...
    
    @property
    def FileName(self) -> StringType: ...
    
    @FileName.setter
    def FileName(self, value: StringType) -> None: ...
    
    @property
    def LoadUserProfile(self) -> BooleanType: ...
    
    @LoadUserProfile.setter
    def LoadUserProfile(self, value: BooleanType) -> None: ...
    
    @property
    def Password(self) -> SecureString: ...
    
    @Password.setter
    def Password(self, value: SecureString) -> None: ...
    
    @property
    def PasswordInClearText(self) -> StringType: ...
    
    @PasswordInClearText.setter
    def PasswordInClearText(self, value: StringType) -> None: ...
    
    @property
    def RedirectStandardError(self) -> BooleanType: ...
    
    @RedirectStandardError.setter
    def RedirectStandardError(self, value: BooleanType) -> None: ...
    
    @property
    def RedirectStandardInput(self) -> BooleanType: ...
    
    @RedirectStandardInput.setter
    def RedirectStandardInput(self, value: BooleanType) -> None: ...
    
    @property
    def RedirectStandardOutput(self) -> BooleanType: ...
    
    @RedirectStandardOutput.setter
    def RedirectStandardOutput(self, value: BooleanType) -> None: ...
    
    @property
    def StandardErrorEncoding(self) -> Encoding: ...
    
    @StandardErrorEncoding.setter
    def StandardErrorEncoding(self, value: Encoding) -> None: ...
    
    @property
    def StandardOutputEncoding(self) -> Encoding: ...
    
    @StandardOutputEncoding.setter
    def StandardOutputEncoding(self, value: Encoding) -> None: ...
    
    @property
    def UseShellExecute(self) -> BooleanType: ...
    
    @UseShellExecute.setter
    def UseShellExecute(self, value: BooleanType) -> None: ...
    
    @property
    def UserName(self) -> StringType: ...
    
    @UserName.setter
    def UserName(self, value: StringType) -> None: ...
    
    @property
    def Verb(self) -> StringType: ...
    
    @Verb.setter
    def Verb(self, value: StringType) -> None: ...
    
    @property
    def Verbs(self) -> ArrayType[StringType]: ...
    
    @property
    def WindowStyle(self) -> ProcessWindowStyle: ...
    
    @WindowStyle.setter
    def WindowStyle(self, value: ProcessWindowStyle) -> None: ...
    
    @property
    def WorkingDirectory(self) -> StringType: ...
    
    @WorkingDirectory.setter
    def WorkingDirectory(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Arguments(self) -> StringType: ...
    
    def get_CreateNoWindow(self) -> BooleanType: ...
    
    def get_Domain(self) -> StringType: ...
    
    def get_Environment(self) -> IDictionary[StringType, StringType]: ...
    
    def get_EnvironmentVariables(self) -> StringDictionary: ...
    
    def get_ErrorDialog(self) -> BooleanType: ...
    
    def get_ErrorDialogParentHandle(self) -> NIntType: ...
    
    def get_FileName(self) -> StringType: ...
    
    def get_LoadUserProfile(self) -> BooleanType: ...
    
    def get_Password(self) -> SecureString: ...
    
    def get_PasswordInClearText(self) -> StringType: ...
    
    def get_RedirectStandardError(self) -> BooleanType: ...
    
    def get_RedirectStandardInput(self) -> BooleanType: ...
    
    def get_RedirectStandardOutput(self) -> BooleanType: ...
    
    def get_StandardErrorEncoding(self) -> Encoding: ...
    
    def get_StandardOutputEncoding(self) -> Encoding: ...
    
    def get_UseShellExecute(self) -> BooleanType: ...
    
    def get_UserName(self) -> StringType: ...
    
    def get_Verb(self) -> StringType: ...
    
    def get_Verbs(self) -> ArrayType[StringType]: ...
    
    def get_WindowStyle(self) -> ProcessWindowStyle: ...
    
    def get_WorkingDirectory(self) -> StringType: ...
    
    def set_Arguments(self, value: StringType) -> VoidType: ...
    
    def set_CreateNoWindow(self, value: BooleanType) -> VoidType: ...
    
    def set_Domain(self, value: StringType) -> VoidType: ...
    
    def set_ErrorDialog(self, value: BooleanType) -> VoidType: ...
    
    def set_ErrorDialogParentHandle(self, value: NIntType) -> VoidType: ...
    
    def set_FileName(self, value: StringType) -> VoidType: ...
    
    def set_LoadUserProfile(self, value: BooleanType) -> VoidType: ...
    
    def set_Password(self, value: SecureString) -> VoidType: ...
    
    def set_PasswordInClearText(self, value: StringType) -> VoidType: ...
    
    def set_RedirectStandardError(self, value: BooleanType) -> VoidType: ...
    
    def set_RedirectStandardInput(self, value: BooleanType) -> VoidType: ...
    
    def set_RedirectStandardOutput(self, value: BooleanType) -> VoidType: ...
    
    def set_StandardErrorEncoding(self, value: Encoding) -> VoidType: ...
    
    def set_StandardOutputEncoding(self, value: Encoding) -> VoidType: ...
    
    def set_UseShellExecute(self, value: BooleanType) -> VoidType: ...
    
    def set_UserName(self, value: StringType) -> VoidType: ...
    
    def set_Verb(self, value: StringType) -> VoidType: ...
    
    def set_WindowStyle(self, value: ProcessWindowStyle) -> VoidType: ...
    
    def set_WorkingDirectory(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ProcessThread(Component, IComponent, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BasePriority(self) -> IntType: ...
    
    @property
    def CurrentPriority(self) -> IntType: ...
    
    @property
    def Id(self) -> IntType: ...
    
    @IdealProcessor.setter
    def IdealProcessor(self, value: IntType) -> None: ...
    
    @property
    def PriorityBoostEnabled(self) -> BooleanType: ...
    
    @PriorityBoostEnabled.setter
    def PriorityBoostEnabled(self, value: BooleanType) -> None: ...
    
    @property
    def PriorityLevel(self) -> ThreadPriorityLevel: ...
    
    @PriorityLevel.setter
    def PriorityLevel(self, value: ThreadPriorityLevel) -> None: ...
    
    @property
    def PrivilegedProcessorTime(self) -> TimeSpan: ...
    
    @ProcessorAffinity.setter
    def ProcessorAffinity(self, value: NIntType) -> None: ...
    
    @property
    def StartAddress(self) -> NIntType: ...
    
    @property
    def StartTime(self) -> DateTime: ...
    
    @property
    def ThreadState(self) -> ThreadState: ...
    
    @property
    def TotalProcessorTime(self) -> TimeSpan: ...
    
    @property
    def UserProcessorTime(self) -> TimeSpan: ...
    
    @property
    def WaitReason(self) -> ThreadWaitReason: ...
    
    # ---------- Methods ---------- #
    
    def ResetIdealProcessor(self) -> VoidType: ...
    
    def get_BasePriority(self) -> IntType: ...
    
    def get_CurrentPriority(self) -> IntType: ...
    
    def get_Id(self) -> IntType: ...
    
    def get_PriorityBoostEnabled(self) -> BooleanType: ...
    
    def get_PriorityLevel(self) -> ThreadPriorityLevel: ...
    
    def get_PrivilegedProcessorTime(self) -> TimeSpan: ...
    
    def get_StartAddress(self) -> NIntType: ...
    
    def get_StartTime(self) -> DateTime: ...
    
    def get_ThreadState(self) -> ThreadState: ...
    
    def get_TotalProcessorTime(self) -> TimeSpan: ...
    
    def get_UserProcessorTime(self) -> TimeSpan: ...
    
    def get_WaitReason(self) -> ThreadWaitReason: ...
    
    def set_IdealProcessor(self, value: IntType) -> VoidType: ...
    
    def set_PriorityBoostEnabled(self, value: BooleanType) -> VoidType: ...
    
    def set_PriorityLevel(self, value: ThreadPriorityLevel) -> VoidType: ...
    
    def set_ProcessorAffinity(self, value: NIntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ProcessThreadCollection(ReadOnlyCollectionBase, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, processThreads: ArrayType[ProcessThread]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> ProcessThread: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, thread: ProcessThread) -> IntType: ...
    
    def Contains(self, thread: ProcessThread) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[ProcessThread], index: IntType) -> VoidType: ...
    
    def IndexOf(self, thread: ProcessThread) -> IntType: ...
    
    def Insert(self, index: IntType, thread: ProcessThread) -> VoidType: ...
    
    def Remove(self, thread: ProcessThread) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> ProcessThread: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ProcessThreadTimes(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ExitTime(self) -> DateTime: ...
    
    @property
    def PrivilegedProcessorTime(self) -> TimeSpan: ...
    
    @property
    def StartTime(self) -> DateTime: ...
    
    @property
    def TotalProcessorTime(self) -> TimeSpan: ...
    
    @property
    def UserProcessorTime(self) -> TimeSpan: ...
    
    # ---------- Methods ---------- #
    
    def get_ExitTime(self) -> DateTime: ...
    
    def get_PrivilegedProcessorTime(self) -> TimeSpan: ...
    
    def get_StartTime(self) -> DateTime: ...
    
    def get_TotalProcessorTime(self) -> TimeSpan: ...
    
    def get_UserProcessorTime(self) -> TimeSpan: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ProcessWaitHandle(WaitHandle, IDisposable):
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


class SharedListenerElementsCollection(ListenerElementsCollection, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CollectionType(self) -> ConfigurationElementCollectionType: ...
    
    # ---------- Methods ---------- #
    
    def get_CollectionType(self) -> ConfigurationElementCollectionType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SharedPerformanceCounter(ObjectType):
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


class SharedUtils(ABC, ObjectType):
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


class ShellExecuteHelper(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, executeInfo: ShellExecuteInfo): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ErrorCode(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def ShellExecuteFunction(self) -> VoidType: ...
    
    def ShellExecuteOnSTAThread(self) -> BooleanType: ...
    
    def get_ErrorCode(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SourceElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> Hashtable: ...
    
    @property
    def Listeners(self) -> ListenerElementsCollection: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def SwitchName(self) -> StringType: ...
    
    @property
    def SwitchType(self) -> StringType: ...
    
    @property
    def SwitchValue(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Attributes(self) -> Hashtable: ...
    
    def get_Listeners(self) -> ListenerElementsCollection: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_SwitchName(self) -> StringType: ...
    
    def get_SwitchType(self) -> StringType: ...
    
    def get_SwitchValue(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SourceElementsCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CollectionType(self) -> ConfigurationElementCollectionType: ...
    
    @property
    def Item(self) -> SourceElement: ...
    
    # ---------- Methods ---------- #
    
    def get_CollectionType(self) -> ConfigurationElementCollectionType: ...
    
    def get_Item(self, name: StringType) -> SourceElement: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SourceFilter(TraceFilter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, source: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Source(self) -> StringType: ...
    
    @Source.setter
    def Source(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def ShouldTrace(self, cache: TraceEventCache, source: StringType, eventType: TraceEventType, id: IntType, formatOrMessage: StringType, args: ArrayType[ObjectType], data1: ObjectType, data: ArrayType[ObjectType]) -> BooleanType: ...
    
    def get_Source(self) -> StringType: ...
    
    def set_Source(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SourceSwitch(Switch):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, name: StringType): ...
    
    @overload
    def __init__(self, displayName: StringType, defaultSwitchValue: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Level(self) -> SourceLevels: ...
    
    @Level.setter
    def Level(self, value: SourceLevels) -> None: ...
    
    # ---------- Methods ---------- #
    
    def ShouldTrace(self, eventType: TraceEventType) -> BooleanType: ...
    
    def get_Level(self) -> SourceLevels: ...
    
    def set_Level(self, value: SourceLevels) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StackFrameExtensions(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetNativeIP(stackFrame: StackFrame) -> NIntType: ...
    
    @staticmethod
    def GetNativeImageBase(stackFrame: StackFrame) -> NIntType: ...
    
    @staticmethod
    def HasILOffset(stackFrame: StackFrame) -> BooleanType: ...
    
    @staticmethod
    def HasMethod(stackFrame: StackFrame) -> BooleanType: ...
    
    @staticmethod
    def HasNativeImage(stackFrame: StackFrame) -> BooleanType: ...
    
    @staticmethod
    def HasSource(stackFrame: StackFrame) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Stopwatch(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Frequency() -> LongType: ...
    
    @staticmethod
    @property
    def IsHighResolution() -> BooleanType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Elapsed(self) -> TimeSpan: ...
    
    @property
    def ElapsedMilliseconds(self) -> LongType: ...
    
    @property
    def ElapsedTicks(self) -> LongType: ...
    
    @property
    def IsRunning(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetTimestamp() -> LongType: ...
    
    def Reset(self) -> VoidType: ...
    
    def Restart(self) -> VoidType: ...
    
    def Start(self) -> VoidType: ...
    
    @staticmethod
    def StartNew() -> Stopwatch: ...
    
    def Stop(self) -> VoidType: ...
    
    def get_Elapsed(self) -> TimeSpan: ...
    
    def get_ElapsedMilliseconds(self) -> LongType: ...
    
    def get_ElapsedTicks(self) -> LongType: ...
    
    def get_IsRunning(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Switch(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> StringDictionary: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @property
    def DisplayName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Attributes(self) -> StringDictionary: ...
    
    def get_Description(self) -> StringType: ...
    
    def get_DisplayName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SwitchAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, switchName: StringType, switchType: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def SwitchDescription(self) -> StringType: ...
    
    @SwitchDescription.setter
    def SwitchDescription(self, value: StringType) -> None: ...
    
    @property
    def SwitchName(self) -> StringType: ...
    
    @SwitchName.setter
    def SwitchName(self, value: StringType) -> None: ...
    
    @property
    def SwitchType(self) -> TypeType: ...
    
    @SwitchType.setter
    def SwitchType(self, value: TypeType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetAll(assembly: Assembly) -> ArrayType[SwitchAttribute]: ...
    
    def get_SwitchDescription(self) -> StringType: ...
    
    def get_SwitchName(self) -> StringType: ...
    
    def get_SwitchType(self) -> TypeType: ...
    
    def set_SwitchDescription(self, value: StringType) -> VoidType: ...
    
    def set_SwitchName(self, value: StringType) -> VoidType: ...
    
    def set_SwitchType(self, value: TypeType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SwitchElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> Hashtable: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Attributes(self) -> Hashtable: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SwitchElementsCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CollectionType(self) -> ConfigurationElementCollectionType: ...
    
    @property
    def Item(self) -> SwitchElement: ...
    
    # ---------- Methods ---------- #
    
    def get_CollectionType(self) -> ConfigurationElementCollectionType: ...
    
    def get_Item(self, name: StringType) -> SwitchElement: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SwitchLevelAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, switchLevelType: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def SwitchLevelType(self) -> TypeType: ...
    
    @SwitchLevelType.setter
    def SwitchLevelType(self, value: TypeType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_SwitchLevelType(self) -> TypeType: ...
    
    def set_SwitchLevelType(self, value: TypeType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SwitchesDictionarySectionHandler(DictionarySectionHandler, IConfigurationSectionHandler):
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


class SystemDiagnosticsSection(ConfigurationSection):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Assert(self) -> AssertSection: ...
    
    @property
    def PerfCounters(self) -> PerfCounterSection: ...
    
    @property
    def SharedListeners(self) -> ListenerElementsCollection: ...
    
    @property
    def Sources(self) -> SourceElementsCollection: ...
    
    @property
    def Switches(self) -> SwitchElementsCollection: ...
    
    @property
    def Trace(self) -> TraceSection: ...
    
    # ---------- Methods ---------- #
    
    def get_Assert(self) -> AssertSection: ...
    
    def get_PerfCounters(self) -> PerfCounterSection: ...
    
    def get_SharedListeners(self) -> ListenerElementsCollection: ...
    
    def get_Sources(self) -> SourceElementsCollection: ...
    
    def get_Switches(self) -> SwitchElementsCollection: ...
    
    def get_Trace(self) -> TraceSection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TextWriterTraceListener(TraceListener, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, stream: Stream): ...
    
    @overload
    def __init__(self, stream: Stream, name: StringType): ...
    
    @overload
    def __init__(self, writer: TextWriter): ...
    
    @overload
    def __init__(self, writer: TextWriter, name: StringType): ...
    
    @overload
    def __init__(self, fileName: StringType): ...
    
    @overload
    def __init__(self, fileName: StringType, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Writer(self) -> TextWriter: ...
    
    @Writer.setter
    def Writer(self, value: TextWriter) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    @overload
    def Write(self, message: StringType) -> VoidType: ...
    
    @overload
    def WriteLine(self, message: StringType) -> VoidType: ...
    
    def get_Writer(self) -> TextWriter: ...
    
    def set_Writer(self, value: TextWriter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ThreadInfo(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def basePriority(self) -> IntType: ...
    
    @basePriority.setter
    def basePriority(self, value: IntType) -> None: ...
    
    @property
    def currentPriority(self) -> IntType: ...
    
    @currentPriority.setter
    def currentPriority(self, value: IntType) -> None: ...
    
    @property
    def processId(self) -> IntType: ...
    
    @processId.setter
    def processId(self, value: IntType) -> None: ...
    
    @property
    def startAddress(self) -> NIntType: ...
    
    @startAddress.setter
    def startAddress(self, value: NIntType) -> None: ...
    
    @property
    def threadId(self) -> IntType: ...
    
    @threadId.setter
    def threadId(self, value: IntType) -> None: ...
    
    @property
    def threadState(self) -> ThreadState: ...
    
    @threadState.setter
    def threadState(self, value: ThreadState) -> None: ...
    
    @property
    def threadWaitReason(self) -> ThreadWaitReason: ...
    
    @threadWaitReason.setter
    def threadWaitReason(self, value: ThreadWaitReason) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Trace(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def AutoFlush() -> BooleanType: ...
    
    @staticmethod
    @AutoFlush.setter
    def AutoFlush(value: BooleanType) -> None: ...
    
    @staticmethod
    @property
    def CorrelationManager() -> CorrelationManager: ...
    
    @staticmethod
    @property
    def IndentLevel() -> IntType: ...
    
    @staticmethod
    @IndentLevel.setter
    def IndentLevel(value: IntType) -> None: ...
    
    @staticmethod
    @property
    def IndentSize() -> IntType: ...
    
    @staticmethod
    @IndentSize.setter
    def IndentSize(value: IntType) -> None: ...
    
    @staticmethod
    @property
    def Listeners() -> TraceListenerCollection: ...
    
    @staticmethod
    @property
    def UseGlobalLock() -> BooleanType: ...
    
    @staticmethod
    @UseGlobalLock.setter
    def UseGlobalLock(value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Assert(condition: BooleanType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Assert(condition: BooleanType, message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Assert(condition: BooleanType, message: StringType, detailMessage: StringType) -> VoidType: ...
    
    @staticmethod
    def Close() -> VoidType: ...
    
    @staticmethod
    @overload
    def Fail(message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Fail(message: StringType, detailMessage: StringType) -> VoidType: ...
    
    @staticmethod
    def Flush() -> VoidType: ...
    
    @staticmethod
    def Indent() -> VoidType: ...
    
    @staticmethod
    def Refresh() -> VoidType: ...
    
    @staticmethod
    @overload
    def TraceError(message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def TraceError(format: StringType, args: ArrayType[ObjectType]) -> VoidType: ...
    
    @staticmethod
    @overload
    def TraceInformation(message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def TraceInformation(format: StringType, args: ArrayType[ObjectType]) -> VoidType: ...
    
    @staticmethod
    @overload
    def TraceWarning(message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def TraceWarning(format: StringType, args: ArrayType[ObjectType]) -> VoidType: ...
    
    @staticmethod
    def Unindent() -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(value: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(message: StringType, category: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(value: ObjectType, category: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteIf(condition: BooleanType, message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteIf(condition: BooleanType, value: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteIf(condition: BooleanType, message: StringType, category: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteIf(condition: BooleanType, value: ObjectType, category: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(value: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(message: StringType, category: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(value: ObjectType, category: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLineIf(condition: BooleanType, message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLineIf(condition: BooleanType, value: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLineIf(condition: BooleanType, message: StringType, category: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLineIf(condition: BooleanType, value: ObjectType, category: StringType) -> VoidType: ...
    
    @staticmethod
    def get_AutoFlush() -> BooleanType: ...
    
    @staticmethod
    def get_CorrelationManager() -> CorrelationManager: ...
    
    @staticmethod
    def get_IndentLevel() -> IntType: ...
    
    @staticmethod
    def get_IndentSize() -> IntType: ...
    
    @staticmethod
    def get_Listeners() -> TraceListenerCollection: ...
    
    @staticmethod
    def get_UseGlobalLock() -> BooleanType: ...
    
    @staticmethod
    def set_AutoFlush(value: BooleanType) -> VoidType: ...
    
    @staticmethod
    def set_IndentLevel(value: IntType) -> VoidType: ...
    
    @staticmethod
    def set_IndentSize(value: IntType) -> VoidType: ...
    
    @staticmethod
    def set_UseGlobalLock(value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TraceEventCache(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Callstack(self) -> StringType: ...
    
    @property
    def DateTime(self) -> DateTime: ...
    
    @property
    def LogicalOperationStack(self) -> Stack: ...
    
    @property
    def ProcessId(self) -> IntType: ...
    
    @property
    def ThreadId(self) -> StringType: ...
    
    @property
    def Timestamp(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def get_Callstack(self) -> StringType: ...
    
    def get_DateTime(self) -> DateTime: ...
    
    def get_LogicalOperationStack(self) -> Stack: ...
    
    def get_ProcessId(self) -> IntType: ...
    
    def get_ThreadId(self) -> StringType: ...
    
    def get_Timestamp(self) -> LongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TraceFilter(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ShouldTrace(self, cache: TraceEventCache, source: StringType, eventType: TraceEventType, id: IntType, formatOrMessage: StringType, args: ArrayType[ObjectType], data1: ObjectType, data: ArrayType[ObjectType]) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TraceInternal(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def AutoFlush() -> BooleanType: ...
    
    @staticmethod
    @AutoFlush.setter
    def AutoFlush(value: BooleanType) -> None: ...
    
    @staticmethod
    @property
    def IndentLevel() -> IntType: ...
    
    @staticmethod
    @IndentLevel.setter
    def IndentLevel(value: IntType) -> None: ...
    
    @staticmethod
    @property
    def IndentSize() -> IntType: ...
    
    @staticmethod
    @IndentSize.setter
    def IndentSize(value: IntType) -> None: ...
    
    @staticmethod
    @property
    def Listeners() -> TraceListenerCollection: ...
    
    @staticmethod
    @property
    def UseGlobalLock() -> BooleanType: ...
    
    @staticmethod
    @UseGlobalLock.setter
    def UseGlobalLock(value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Assert(condition: BooleanType, message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Assert(condition: BooleanType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Assert(condition: BooleanType, message: StringType, detailMessage: StringType) -> VoidType: ...
    
    @staticmethod
    def Close() -> VoidType: ...
    
    @staticmethod
    @overload
    def Fail(message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Fail(message: StringType, detailMessage: StringType) -> VoidType: ...
    
    @staticmethod
    def Flush() -> VoidType: ...
    
    @staticmethod
    def Indent() -> VoidType: ...
    
    @staticmethod
    def TraceEvent(eventType: TraceEventType, id: IntType, format: StringType, args: ArrayType[ObjectType]) -> VoidType: ...
    
    @staticmethod
    def Unindent() -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(value: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(message: StringType, category: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Write(value: ObjectType, category: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteIf(condition: BooleanType, message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteIf(condition: BooleanType, value: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteIf(condition: BooleanType, message: StringType, category: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteIf(condition: BooleanType, value: ObjectType, category: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(message: StringType, category: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(value: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLine(value: ObjectType, category: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLineIf(condition: BooleanType, message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLineIf(condition: BooleanType, value: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLineIf(condition: BooleanType, message: StringType, category: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteLineIf(condition: BooleanType, value: ObjectType, category: StringType) -> VoidType: ...
    
    @staticmethod
    def get_AutoFlush() -> BooleanType: ...
    
    @staticmethod
    def get_IndentLevel() -> IntType: ...
    
    @staticmethod
    def get_IndentSize() -> IntType: ...
    
    @staticmethod
    def get_Listeners() -> TraceListenerCollection: ...
    
    @staticmethod
    def get_UseGlobalLock() -> BooleanType: ...
    
    @staticmethod
    def set_AutoFlush(value: BooleanType) -> VoidType: ...
    
    @staticmethod
    def set_IndentLevel(value: IntType) -> VoidType: ...
    
    @staticmethod
    def set_IndentSize(value: IntType) -> VoidType: ...
    
    @staticmethod
    def set_UseGlobalLock(value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TraceListener(ABC, MarshalByRefObject, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> StringDictionary: ...
    
    @property
    def Filter(self) -> TraceFilter: ...
    
    @Filter.setter
    def Filter(self, value: TraceFilter) -> None: ...
    
    @property
    def IndentLevel(self) -> IntType: ...
    
    @IndentLevel.setter
    def IndentLevel(self, value: IntType) -> None: ...
    
    @property
    def IndentSize(self) -> IntType: ...
    
    @IndentSize.setter
    def IndentSize(self, value: IntType) -> None: ...
    
    @property
    def IsThreadSafe(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def TraceOutputOptions(self) -> TraceOptions: ...
    
    @TraceOutputOptions.setter
    def TraceOutputOptions(self, value: TraceOptions) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    @overload
    def Fail(self, message: StringType) -> VoidType: ...
    
    @overload
    def Fail(self, message: StringType, detailMessage: StringType) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    @overload
    def TraceData(self, eventCache: TraceEventCache, source: StringType, eventType: TraceEventType, id: IntType, data: ObjectType) -> VoidType: ...
    
    @overload
    def TraceData(self, eventCache: TraceEventCache, source: StringType, eventType: TraceEventType, id: IntType, data: ArrayType[ObjectType]) -> VoidType: ...
    
    @overload
    def TraceEvent(self, eventCache: TraceEventCache, source: StringType, eventType: TraceEventType, id: IntType) -> VoidType: ...
    
    @overload
    def TraceEvent(self, eventCache: TraceEventCache, source: StringType, eventType: TraceEventType, id: IntType, message: StringType) -> VoidType: ...
    
    @overload
    def TraceEvent(self, eventCache: TraceEventCache, source: StringType, eventType: TraceEventType, id: IntType, format: StringType, args: ArrayType[ObjectType]) -> VoidType: ...
    
    def TraceTransfer(self, eventCache: TraceEventCache, source: StringType, id: IntType, message: StringType, relatedActivityId: Guid) -> VoidType: ...
    
    @overload
    def Write(self, o: ObjectType) -> VoidType: ...
    
    @overload
    def Write(self, o: ObjectType, category: StringType) -> VoidType: ...
    
    @overload
    def Write(self, message: StringType) -> VoidType: ...
    
    @overload
    def Write(self, message: StringType, category: StringType) -> VoidType: ...
    
    @overload
    def WriteLine(self, o: ObjectType) -> VoidType: ...
    
    @overload
    def WriteLine(self, o: ObjectType, category: StringType) -> VoidType: ...
    
    @overload
    def WriteLine(self, message: StringType) -> VoidType: ...
    
    @overload
    def WriteLine(self, message: StringType, category: StringType) -> VoidType: ...
    
    def get_Attributes(self) -> StringDictionary: ...
    
    def get_Filter(self) -> TraceFilter: ...
    
    def get_IndentLevel(self) -> IntType: ...
    
    def get_IndentSize(self) -> IntType: ...
    
    def get_IsThreadSafe(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_TraceOutputOptions(self) -> TraceOptions: ...
    
    def set_Filter(self, value: TraceFilter) -> VoidType: ...
    
    def set_IndentLevel(self, value: IntType) -> VoidType: ...
    
    def set_IndentSize(self, value: IntType) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_TraceOutputOptions(self, value: TraceOptions) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TraceListenerCollection(ObjectType, IList, ICollection, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Item(self) -> TraceListener: ...
    
    @Item.setter
    def Item(self, value: TraceListener) -> None: ...
    
    @property
    def Item(self) -> TraceListener: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, listener: TraceListener) -> IntType: ...
    
    @overload
    def AddRange(self, value: ArrayType[TraceListener]) -> VoidType: ...
    
    @overload
    def AddRange(self, value: TraceListenerCollection) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, listener: TraceListener) -> BooleanType: ...
    
    def CopyTo(self, listeners: ArrayType[TraceListener], index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def IndexOf(self, listener: TraceListener) -> IntType: ...
    
    def Insert(self, index: IntType, listener: TraceListener) -> VoidType: ...
    
    @overload
    def Remove(self, listener: TraceListener) -> VoidType: ...
    
    @overload
    def Remove(self, name: StringType) -> VoidType: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    @overload
    def get_Item(self, i: IntType) -> TraceListener: ...
    
    @overload
    def get_Item(self, name: StringType) -> TraceListener: ...
    
    def set_Item(self, i: IntType, value: TraceListener) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TraceSection(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AutoFlush(self) -> BooleanType: ...
    
    @property
    def IndentSize(self) -> IntType: ...
    
    @property
    def Listeners(self) -> ListenerElementsCollection: ...
    
    @property
    def UseGlobalLock(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_AutoFlush(self) -> BooleanType: ...
    
    def get_IndentSize(self) -> IntType: ...
    
    def get_Listeners(self) -> ListenerElementsCollection: ...
    
    def get_UseGlobalLock(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TraceSource(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, name: StringType): ...
    
    @overload
    def __init__(self, name: StringType, defaultLevel: SourceLevels): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> StringDictionary: ...
    
    @property
    def Listeners(self) -> TraceListenerCollection: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Switch(self) -> SourceSwitch: ...
    
    @Switch.setter
    def Switch(self, value: SourceSwitch) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    @overload
    def TraceData(self, eventType: TraceEventType, id: IntType, data: ObjectType) -> VoidType: ...
    
    @overload
    def TraceData(self, eventType: TraceEventType, id: IntType, data: ArrayType[ObjectType]) -> VoidType: ...
    
    @overload
    def TraceEvent(self, eventType: TraceEventType, id: IntType) -> VoidType: ...
    
    @overload
    def TraceEvent(self, eventType: TraceEventType, id: IntType, message: StringType) -> VoidType: ...
    
    @overload
    def TraceEvent(self, eventType: TraceEventType, id: IntType, format: StringType, args: ArrayType[ObjectType]) -> VoidType: ...
    
    @overload
    def TraceInformation(self, message: StringType) -> VoidType: ...
    
    @overload
    def TraceInformation(self, format: StringType, args: ArrayType[ObjectType]) -> VoidType: ...
    
    def TraceTransfer(self, id: IntType, message: StringType, relatedActivityId: Guid) -> VoidType: ...
    
    def get_Attributes(self) -> StringDictionary: ...
    
    def get_Listeners(self) -> TraceListenerCollection: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Switch(self) -> SourceSwitch: ...
    
    def set_Switch(self, value: SourceSwitch) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TraceSwitch(Switch):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, displayName: StringType, description: StringType): ...
    
    @overload
    def __init__(self, displayName: StringType, description: StringType, defaultSwitchValue: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Level(self) -> TraceLevel: ...
    
    @Level.setter
    def Level(self, value: TraceLevel) -> None: ...
    
    @property
    def TraceError(self) -> BooleanType: ...
    
    @property
    def TraceInfo(self) -> BooleanType: ...
    
    @property
    def TraceVerbose(self) -> BooleanType: ...
    
    @property
    def TraceWarning(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_Level(self) -> TraceLevel: ...
    
    def get_TraceError(self) -> BooleanType: ...
    
    def get_TraceInfo(self) -> BooleanType: ...
    
    def get_TraceVerbose(self) -> BooleanType: ...
    
    def get_TraceWarning(self) -> BooleanType: ...
    
    def set_Level(self, value: TraceLevel) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TraceUtils(ABC, ObjectType):
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


class TypedElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, baseType: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def InitData(self) -> StringType: ...
    
    @InitData.setter
    def InitData(self, value: StringType) -> None: ...
    
    @property
    def TypeName(self) -> StringType: ...
    
    @TypeName.setter
    def TypeName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_InitData(self) -> StringType: ...
    
    def get_TypeName(self) -> StringType: ...
    
    def set_InitData(self, value: StringType) -> VoidType: ...
    
    def set_TypeName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UserCallBack(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, data: StringType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, data: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WinProcessManager(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetModuleInfos(processId: IntType) -> ArrayType[ModuleInfo]: ...
    
    @staticmethod
    def GetProcessIds() -> ArrayType[IntType]: ...
    
    @staticmethod
    def GetProcessInfos() -> ArrayType[ProcessInfo]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlWriterTraceListener(TextWriterTraceListener, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, stream: Stream): ...
    
    @overload
    def __init__(self, stream: Stream, name: StringType): ...
    
    @overload
    def __init__(self, writer: TextWriter): ...
    
    @overload
    def __init__(self, writer: TextWriter, name: StringType): ...
    
    @overload
    def __init__(self, filename: StringType): ...
    
    @overload
    def __init__(self, filename: StringType, name: StringType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def Fail(self, message: StringType, detailMessage: StringType) -> VoidType: ...
    
    @overload
    def TraceData(self, eventCache: TraceEventCache, source: StringType, eventType: TraceEventType, id: IntType, data: ObjectType) -> VoidType: ...
    
    @overload
    def TraceData(self, eventCache: TraceEventCache, source: StringType, eventType: TraceEventType, id: IntType, data: ArrayType[ObjectType]) -> VoidType: ...
    
    @overload
    def TraceEvent(self, eventCache: TraceEventCache, source: StringType, eventType: TraceEventType, id: IntType, format: StringType, args: ArrayType[ObjectType]) -> VoidType: ...
    
    @overload
    def TraceEvent(self, eventCache: TraceEventCache, source: StringType, eventType: TraceEventType, id: IntType, message: StringType) -> VoidType: ...
    
    def TraceTransfer(self, eventCache: TraceEventCache, source: StringType, id: IntType, message: StringType, relatedActivityId: Guid) -> VoidType: ...
    
    @overload
    def Write(self, message: StringType) -> VoidType: ...
    
    @overload
    def WriteLine(self, message: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class CounterSample(ValueType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Empty() -> CounterSample: ...
    
    @staticmethod
    @Empty.setter
    def Empty(value: CounterSample) -> None: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, rawValue: LongType, baseValue: LongType, counterFrequency: LongType, systemFrequency: LongType, timeStamp: LongType, timeStamp100nSec: LongType, counterType: PerformanceCounterType): ...
    
    @overload
    def __init__(self, rawValue: LongType, baseValue: LongType, counterFrequency: LongType, systemFrequency: LongType, timeStamp: LongType, timeStamp100nSec: LongType, counterType: PerformanceCounterType, counterTimeStamp: LongType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseValue(self) -> LongType: ...
    
    @property
    def CounterFrequency(self) -> LongType: ...
    
    @property
    def CounterTimeStamp(self) -> LongType: ...
    
    @property
    def CounterType(self) -> PerformanceCounterType: ...
    
    @property
    def RawValue(self) -> LongType: ...
    
    @property
    def SystemFrequency(self) -> LongType: ...
    
    @property
    def TimeStamp(self) -> LongType: ...
    
    @property
    def TimeStamp100nSec(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Calculate(counterSample: CounterSample) -> FloatType: ...
    
    @staticmethod
    @overload
    def Calculate(counterSample: CounterSample, nextCounterSample: CounterSample) -> FloatType: ...
    
    @overload
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, sample: CounterSample) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_BaseValue(self) -> LongType: ...
    
    def get_CounterFrequency(self) -> LongType: ...
    
    def get_CounterTimeStamp(self) -> LongType: ...
    
    def get_CounterType(self) -> PerformanceCounterType: ...
    
    def get_RawValue(self) -> LongType: ...
    
    def get_SystemFrequency(self) -> LongType: ...
    
    def get_TimeStamp(self) -> LongType: ...
    
    def get_TimeStamp100nSec(self) -> LongType: ...
    
    @staticmethod
    def op_Equality(a: CounterSample, b: CounterSample) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(a: CounterSample, b: CounterSample) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Interfaces ---------- #

class ICollectData(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CloseData(self) -> VoidType: ...
    
    def CollectData(self, id: IntType, valueName: NIntType, data: NIntType, totalBytes: IntType, res: NIntType) -> Tuple[VoidType, NIntType]: ...
    
    # No Events


# ---------- Enums ---------- #

class EventLogEntryType(Enum):
    Error: IntType = 1
    Warning: IntType = 2
    Information: IntType = 4
    SuccessAudit: IntType = 8
    FailureAudit: IntType = 16


class EventLogPermissionAccess(Enum):
    #None: IntType = 0
    Browse: IntType = 2
    Instrument: IntType = 6
    Audit: IntType = 10
    Write: IntType = 16
    Administer: IntType = 48


class InitState(Enum):
    NotInitialized: IntType = 0
    Initializing: IntType = 1
    Initialized: IntType = 2


class OverflowAction(Enum):
    DoNotOverwrite: IntType = -1
    OverwriteAsNeeded: IntType = 0
    OverwriteOlder: IntType = 1


class PerformanceCounterCategoryOptions(Enum):
    EnableReuse: IntType = 1
    UseUniqueSharedMemory: IntType = 2


class PerformanceCounterCategoryType(Enum):
    Unknown: IntType = -1
    SingleInstance: IntType = 0
    MultiInstance: IntType = 1


class PerformanceCounterInstanceLifetime(Enum):
    Global: IntType = 0
    Process: IntType = 1


class PerformanceCounterPermissionAccess(Enum):
    #None: IntType = 0
    Read: IntType = 1
    Browse: IntType = 1
    Write: IntType = 2
    Instrument: IntType = 3
    Administer: IntType = 7


class PerformanceCounterType(Enum):
    NumberOfItemsHEX32: IntType = 0
    NumberOfItemsHEX64: IntType = 256
    NumberOfItems32: IntType = 65536
    NumberOfItems64: IntType = 65792
    CounterDelta32: IntType = 4195328
    CounterDelta64: IntType = 4195584
    SampleCounter: IntType = 4260864
    CountPerTimeInterval32: IntType = 4523008
    CountPerTimeInterval64: IntType = 4523264
    RateOfCountsPerSecond32: IntType = 272696320
    RateOfCountsPerSecond64: IntType = 272696576
    RawFraction: IntType = 537003008
    CounterTimer: IntType = 541132032
    Timer100Ns: IntType = 542180608
    SampleFraction: IntType = 549585920
    CounterTimerInverse: IntType = 557909248
    Timer100NsInverse: IntType = 558957824
    CounterMultiTimer: IntType = 574686464
    CounterMultiTimer100Ns: IntType = 575735040
    CounterMultiTimerInverse: IntType = 591463680
    CounterMultiTimer100NsInverse: IntType = 592512256
    AverageTimer32: IntType = 805438464
    ElapsedTime: IntType = 807666944
    AverageCount64: IntType = 1073874176
    SampleBase: IntType = 1073939457
    AverageBase: IntType = 1073939458
    RawBase: IntType = 1073939459
    CounterMultiBase: IntType = 1107494144


class ProcessPriorityClass(Enum):
    Normal: IntType = 32
    Idle: IntType = 64
    High: IntType = 128
    RealTime: IntType = 256
    BelowNormal: IntType = 16384
    AboveNormal: IntType = 32768


class ProcessWindowStyle(Enum):
    Normal: IntType = 0
    Hidden: IntType = 1
    Minimized: IntType = 2
    Maximized: IntType = 3


class SourceLevels(Enum):
    All: IntType = -1
    Off: IntType = 0
    Critical: IntType = 1
    Error: IntType = 3
    Warning: IntType = 7
    Information: IntType = 15
    Verbose: IntType = 31
    ActivityTracing: IntType = 65280


class ThreadPriorityLevel(Enum):
    Idle: IntType = -15
    Lowest: IntType = -2
    BelowNormal: IntType = -1
    Normal: IntType = 0
    AboveNormal: IntType = 1
    Highest: IntType = 2
    TimeCritical: IntType = 15


class ThreadState(Enum):
    Initialized: IntType = 0
    Ready: IntType = 1
    Running: IntType = 2
    Standby: IntType = 3
    Terminated: IntType = 4
    Wait: IntType = 5
    Transition: IntType = 6
    Unknown: IntType = 7


class ThreadWaitReason(Enum):
    Executive: IntType = 0
    FreePage: IntType = 1
    PageIn: IntType = 2
    SystemAllocation: IntType = 3
    ExecutionDelay: IntType = 4
    Suspended: IntType = 5
    UserRequest: IntType = 6
    EventPairHigh: IntType = 7
    EventPairLow: IntType = 8
    LpcReceive: IntType = 9
    LpcReply: IntType = 10
    VirtualMemory: IntType = 11
    PageOut: IntType = 12
    Unknown: IntType = 13


class TraceEventType(Enum):
    Critical: IntType = 1
    Error: IntType = 2
    Warning: IntType = 4
    Information: IntType = 8
    Verbose: IntType = 16
    Start: IntType = 256
    Stop: IntType = 512
    Suspend: IntType = 1024
    Resume: IntType = 2048
    Transfer: IntType = 4096


class TraceLevel(Enum):
    Off: IntType = 0
    Error: IntType = 1
    Warning: IntType = 2
    Info: IntType = 3
    Verbose: IntType = 4


class TraceOptions(Enum):
    #None: IntType = 0
    LogicalOperationStack: IntType = 1
    DateTime: IntType = 2
    Timestamp: IntType = 4
    ProcessId: IntType = 8
    ThreadId: IntType = 16
    Callstack: IntType = 32


# ---------- Delegates ---------- #

DataReceivedEventHandler = Callable[[ObjectType, DataReceivedEventArgs], VoidType]

EntryWrittenEventHandler = Callable[[ObjectType, EntryWrittenEventArgs], VoidType]

UserCallBack = Callable[[StringType], VoidType]

__all__ = [
    AlphabeticalEnumConverter,
    AssertSection,
    AssertWrapper,
    AsyncStreamReader,
    BooleanSwitch,
    CategoryEntry,
    CategorySample,
    ConsoleTraceListener,
    CorrelationManager,
    CounterCreationData,
    CounterCreationDataCollection,
    CounterDefinitionSample,
    CounterSampleCalculator,
    DataReceivedEventArgs,
    DataReceivedEventHandler,
    Debug,
    DefaultTraceListener,
    DelimitedListTraceListener,
    DiagnosticsConfiguration,
    DiagnosticsConfigurationHandler,
    EntryWrittenEventArgs,
    EntryWrittenEventHandler,
    EnvironmentBlock,
    EventInstance,
    EventLog,
    EventLogEntry,
    EventLogEntryCollection,
    EventLogInternal,
    EventLogPermission,
    EventLogPermissionAttribute,
    EventLogPermissionEntry,
    EventLogPermissionEntryCollection,
    EventLogTraceListener,
    EventSourceCreationData,
    EventTypeFilter,
    FileVersionInfo,
    FilterElement,
    InstanceData,
    InstanceDataCollection,
    InstanceDataCollectionCollection,
    ListenerElement,
    ListenerElementsCollection,
    MainWindowFinder,
    MessageBoxPopup,
    ModuleInfo,
    MonitoringDescriptionAttribute,
    NtProcessInfoHelper,
    NtProcessManager,
    OrdinalCaseInsensitiveComparer,
    PerfCounterSection,
    PerformanceCounter,
    PerformanceCounterCategory,
    PerformanceCounterLib,
    PerformanceCounterManager,
    PerformanceCounterPermission,
    PerformanceCounterPermissionAttribute,
    PerformanceCounterPermissionEntry,
    PerformanceCounterPermissionEntryCollection,
    PerformanceMonitor,
    Process,
    ProcessData,
    ProcessInfo,
    ProcessManager,
    ProcessModule,
    ProcessModuleCollection,
    ProcessStartInfo,
    ProcessThread,
    ProcessThreadCollection,
    ProcessThreadTimes,
    ProcessWaitHandle,
    SharedListenerElementsCollection,
    SharedPerformanceCounter,
    SharedUtils,
    ShellExecuteHelper,
    SourceElement,
    SourceElementsCollection,
    SourceFilter,
    SourceSwitch,
    StackFrameExtensions,
    Stopwatch,
    Switch,
    SwitchAttribute,
    SwitchElement,
    SwitchElementsCollection,
    SwitchLevelAttribute,
    SwitchesDictionarySectionHandler,
    SystemDiagnosticsSection,
    TextWriterTraceListener,
    ThreadInfo,
    Trace,
    TraceEventCache,
    TraceFilter,
    TraceInternal,
    TraceListener,
    TraceListenerCollection,
    TraceSection,
    TraceSource,
    TraceSwitch,
    TraceUtils,
    TypedElement,
    UserCallBack,
    WinProcessManager,
    XmlWriterTraceListener,
    CounterSample,
    ICollectData,
    EventLogEntryType,
    EventLogPermissionAccess,
    InitState,
    OverflowAction,
    PerformanceCounterCategoryOptions,
    PerformanceCounterCategoryType,
    PerformanceCounterInstanceLifetime,
    PerformanceCounterPermissionAccess,
    PerformanceCounterType,
    ProcessPriorityClass,
    ProcessWindowStyle,
    SourceLevels,
    ThreadPriorityLevel,
    ThreadState,
    ThreadWaitReason,
    TraceEventType,
    TraceLevel,
    TraceOptions,
    DataReceivedEventHandler,
    EntryWrittenEventHandler,
    UserCallBack,
]
