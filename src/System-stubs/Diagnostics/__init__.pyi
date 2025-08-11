"""Automatically generated stubs for C# namespace: System.Diagnostics."""

from abc import ABC
from collections.abc import Callable
from collections.abc import Iterator
from typing import ClassVar
from typing import Final
from typing import Self
from typing import overload

from Microsoft.Win32.SafeHandles import SafeProcessHandle
from Microsoft.Win32.SafeHandles import SafeThreadHandle
from Microsoft.Win32.SafeHandles import SafeWaitHandle
from System import Array
from System import Attribute
from System import DateTime
from System import Enum
from System import EventArgs
from System import EventHandler
from System import Exception
from System import Guid
from System import IDisposable
from System import Int32
from System import IntPtr
from System import MarshalByRefObject
from System import Object
from System import Predicate
from System import String
from System import TimeSpan
from System import Type
from System import UInt32
from System import ValueType
from System.Collections import ArrayList
from System.Collections import CollectionBase
from System.Collections import DictionaryBase
from System.Collections import Hashtable
from System.Collections import ICollection
from System.Collections import IComparer
from System.Collections import IDictionary
from System.Collections import IDictionaryEnumerator
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IList
from System.Collections import ReadOnlyCollectionBase
from System.Collections import Stack
from System.Collections.Generic import IDictionary
from System.Collections.Specialized import StringDictionary
from System.ComponentModel import Component
from System.ComponentModel import DescriptionAttribute
from System.ComponentModel import EnumConverter
from System.ComponentModel import IComponent
from System.ComponentModel import IContainer
from System.ComponentModel import ISite
from System.ComponentModel import ISupportInitialize
from System.ComponentModel import ISynchronizeInvoke
from System.ComponentModel import ITypeDescriptorContext
from System.ComponentModel import PropertyDescriptorCollection
from System.Configuration import Configuration
from System.Configuration import ConfigurationElement
from System.Configuration import ConfigurationElementCollection
from System.Configuration import ConfigurationElementCollectionType
from System.Configuration import ConfigurationLockCollection
from System.Configuration import ConfigurationSection
from System.Configuration import DictionarySectionHandler
from System.Configuration import ElementInformation
from System.Configuration import IConfigurationSectionHandler
from System.Configuration import SectionInformation
from System.Globalization import CultureInfo
from System.IO import Stream
from System.IO import StreamReader
from System.IO import StreamWriter
from System.IO import TextWriter
from System.Reflection import Assembly
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Attribute
from System.Runtime.Remoting import ObjRef
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Security import IPermission
from System.Security import ISecurityEncodable
from System.Security import IStackWalk
from System.Security import SecureString
from System.Security import SecurityElement
from System.Security.Permissions import CodeAccessSecurityAttribute
from System.Security.Permissions import IUnrestrictedPermission
from System.Security.Permissions import PermissionState
from System.Security.Permissions import ResourcePermissionBase
from System.Security.Permissions import SecurityAction
from System.Text import Encoding
from System.Threading import Thread
from System.Threading import WaitHandle
from System.Xml import XmlNode

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AlphabeticalEnumConverter(EnumConverter):
    """"""
    def __init__(self, type: Type) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Assert(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssertFilter(ABC, Object):
    """"""
    def AssertFailure(
        self,
        condition: str,
        message: str,
        location: StackTrace,
        stackTraceFormat: StackTrace.TraceFormat,
        windowTitle: str,
    ) -> AssertFilters:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class AssertFilters(Enum):
    """"""

    FailDebug: AssertFilters = ...
    """"""
    FailIgnore: AssertFilters = ...
    """"""
    FailTerminate: AssertFilters = ...
    """"""
    FailContinueFilter: AssertFilters = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssertSection(ConfigurationElement):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AssertUIEnabled(self) -> bool:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def LockAllAttributesExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAllElementsExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAttributes(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockElements(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockItem(self) -> bool:
        """"""
    @LockItem.setter
    def LockItem(self, value: bool) -> None: ...
    @property
    def LogFileName(self) -> str:
        """"""
    def Equals(self, compareTo: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssertWrapper(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ShowAssert(
        cls, stackTrace: str, frame: StackFrame, message: str, detailMessage: str
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AsyncStreamReader(Object, IDisposable):
    """"""
    @property
    def BaseStream(self) -> Stream:
        """"""
    @property
    def CurrentEncoding(self) -> Encoding:
        """"""
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BooleanSwitch(Switch):
    """"""
    @overload
    def __init__(self, displayName: str, description: str) -> None:
        """"""
    @overload
    def __init__(self, displayName: str, description: str, defaultSwitchValue: str) -> None:
        """"""
    @property
    def Attributes(self) -> StringDictionary:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def DisplayName(self) -> str:
        """"""
    @property
    def Enabled(self) -> bool:
        """"""
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CategoryEntry(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CategorySample(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ConditionalAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, conditionString: str) -> None:
        """"""
    @property
    def ConditionString(self) -> str:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ConsoleTraceListener(TextWriterTraceListener, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, useErrorStream: bool) -> None:
        """"""
    @property
    def Attributes(self) -> StringDictionary:
        """"""
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
    @property
    def Writer(self) -> TextWriter:
        """"""
    @Writer.setter
    def Writer(self, value: TextWriter) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CorrelationManager(Object):
    """"""
    @property
    def ActivityId(self) -> Guid:
        """"""
    @ActivityId.setter
    def ActivityId(self, value: Guid) -> None: ...
    @property
    def LogicalOperationStack(self) -> Stack:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def StartLogicalOperation(self) -> None:
        """"""
    @overload
    def StartLogicalOperation(self, operationId: object) -> None:
        """"""
    def StopLogicalOperation(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CounterCreationData(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(
        self, counterName: str, counterHelp: str, counterType: PerformanceCounterType
    ) -> None:
        """"""
    @property
    def CounterHelp(self) -> str:
        """"""
    @CounterHelp.setter
    def CounterHelp(self, value: str) -> None: ...
    @property
    def CounterName(self) -> str:
        """"""
    @CounterName.setter
    def CounterName(self, value: str) -> None: ...
    @property
    def CounterType(self) -> PerformanceCounterType:
        """"""
    @CounterType.setter
    def CounterType(self, value: PerformanceCounterType) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CounterCreationDataCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: CounterCreationDataCollection) -> None:
        """"""
    @overload
    def __init__(self, value: Array[CounterCreationData]) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> CounterCreationData:
        """"""
    @Item.setter
    def Item(self, value: CounterCreationData) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, value: CounterCreationData) -> int:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    @overload
    def AddRange(self, value: CounterCreationDataCollection) -> None:
        """"""
    @overload
    def AddRange(self, value: Array[CounterCreationData]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CounterCreationData) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[CounterCreationData], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, value: CounterCreationData) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, value: CounterCreationData) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, value: CounterCreationData) -> None:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: CounterCreationData) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, value: CounterCreationData) -> None:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> CounterCreationData:
        """"""
    @overload
    def __setitem__(self, index: int, value: CounterCreationData) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CounterDefinitionSample(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CounterSample(ValueType):
    """"""

    Empty: ClassVar[CounterSample]
    """"""
    @overload
    def __init__(
        self,
        rawValue: int,
        baseValue: int,
        counterFrequency: int,
        systemFrequency: int,
        timeStamp: int,
        timeStamp100nSec: int,
        counterType: PerformanceCounterType,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        rawValue: int,
        baseValue: int,
        counterFrequency: int,
        systemFrequency: int,
        timeStamp: int,
        timeStamp100nSec: int,
        counterType: PerformanceCounterType,
        counterTimeStamp: int,
    ) -> None:
        """"""
    @property
    def BaseValue(self) -> int:
        """"""
    @property
    def CounterFrequency(self) -> int:
        """"""
    @property
    def CounterTimeStamp(self) -> int:
        """"""
    @property
    def CounterType(self) -> PerformanceCounterType:
        """"""
    @property
    def RawValue(self) -> int:
        """"""
    @property
    def SystemFrequency(self) -> int:
        """"""
    @property
    def TimeStamp(self) -> int:
        """"""
    @property
    def TimeStamp100nSec(self) -> int:
        """"""
    @classmethod
    @overload
    def Calculate(cls, counterSample: CounterSample) -> float:
        """"""
    @classmethod
    @overload
    def Calculate(cls, counterSample: CounterSample, nextCounterSample: CounterSample) -> float:
        """"""
    @overload
    def Equals(self, sample: CounterSample) -> bool:
        """"""
    @overload
    def Equals(self, o: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, a: CounterSample, b: CounterSample) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, a: CounterSample, b: CounterSample) -> bool:
        """"""
    def __eq__(self, other: CounterSample) -> bool:
        """"""
    def __ne__(self, other: CounterSample) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CounterSampleCalculator(ABC, Object):
    """"""
    @classmethod
    @overload
    def ComputeCounterValue(cls, newSample: CounterSample) -> float:
        """"""
    @classmethod
    @overload
    def ComputeCounterValue(cls, oldSample: CounterSample, newSample: CounterSample) -> float:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DataReceivedEventArgs(EventArgs):
    """"""
    @property
    def Data(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type DataReceivedEventHandler = Callable[[object, DataReceivedEventArgs], None]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Debug(ABC, Object):
    """"""
    @classmethod
    @property
    def AutoFlush(cls) -> bool:
        """"""
    @classmethod
    @AutoFlush.setter
    def AutoFlush(cls, value: bool) -> None: ...
    @classmethod
    @property
    def IndentLevel(cls) -> int:
        """"""
    @classmethod
    @IndentLevel.setter
    def IndentLevel(cls, value: int) -> None: ...
    @classmethod
    @property
    def IndentSize(cls) -> int:
        """"""
    @classmethod
    @IndentSize.setter
    def IndentSize(cls, value: int) -> None: ...
    @classmethod
    @property
    def Listeners(cls) -> TraceListenerCollection:
        """"""
    @classmethod
    @overload
    def Assert(cls, condition: bool) -> None:
        """"""
    @classmethod
    @overload
    def Assert(cls, condition: bool, message: str) -> None:
        """"""
    @classmethod
    @overload
    def Assert(cls, condition: bool, message: str, detailMessage: str) -> None:
        """"""
    @classmethod
    @overload
    def Assert(
        cls, condition: bool, message: str, detailMessageFormat: str, args: Array[object]
    ) -> None:
        """"""
    @classmethod
    def Close(cls) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def Fail(cls, message: str) -> None:
        """"""
    @classmethod
    @overload
    def Fail(cls, message: str, detailMessage: str) -> None:
        """"""
    @classmethod
    def Flush(cls) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Indent(cls) -> None:
        """"""
    @classmethod
    @overload
    def Print(cls, message: str) -> None:
        """"""
    @classmethod
    @overload
    def Print(cls, format: str, args: Array[object]) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def Unindent(cls) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, value: object) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, value: object, category: str) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, message: str) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, message: str, category: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteIf(cls, condition: bool, value: object) -> None:
        """"""
    @classmethod
    @overload
    def WriteIf(cls, condition: bool, value: object, category: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteIf(cls, condition: bool, message: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteIf(cls, condition: bool, message: str, category: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, value: object) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, value: object, category: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, message: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, format: str, args: Array[object]) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, message: str, category: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteLineIf(cls, condition: bool, value: object) -> None:
        """"""
    @classmethod
    @overload
    def WriteLineIf(cls, condition: bool, value: object, category: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteLineIf(cls, condition: bool, message: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteLineIf(cls, condition: bool, message: str, category: str) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DebuggableAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, isJITTrackingEnabled: bool, isJITOptimizerDisabled: bool) -> None:
        """"""
    @overload
    def __init__(self, modes: DebuggableAttribute.DebuggingModes) -> None:
        """"""
    @property
    def DebuggingFlags(self) -> DebuggableAttribute.DebuggingModes:
        """"""
    @property
    def IsJITOptimizerDisabled(self) -> bool:
        """"""
    @property
    def IsJITTrackingEnabled(self) -> bool:
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
    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class DebuggingModes(Enum):
        """"""

        _None: DebuggableAttribute.DebuggingModes = ...
        """"""
        Default: DebuggableAttribute.DebuggingModes = ...
        """"""
        IgnoreSymbolStoreSequencePoints: DebuggableAttribute.DebuggingModes = ...
        """"""
        EnableEditAndContinue: DebuggableAttribute.DebuggingModes = ...
        """"""
        DisableOptimizations: DebuggableAttribute.DebuggingModes = ...
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Debugger(Object):
    """"""

    DefaultCategory: ClassVar[str]
    """"""
    def __init__(self) -> None:
        """"""
    @classmethod
    @property
    def IsAttached(cls) -> bool:
        """"""
    @classmethod
    def Break(cls) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsLogging(cls) -> bool:
        """"""
    @classmethod
    def Launch(cls) -> bool:
        """"""
    @classmethod
    def Log(cls, level: int, category: str, message: str) -> None:
        """"""
    @classmethod
    def NotifyOfCrossThreadDependency(cls) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DebuggerBrowsableAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, state: DebuggerBrowsableState) -> None:
        """"""
    @property
    def State(self) -> DebuggerBrowsableState:
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class DebuggerBrowsableState(Enum):
    """"""

    Never: DebuggerBrowsableState = ...
    """"""
    Collapsed: DebuggerBrowsableState = ...
    """"""
    RootHidden: DebuggerBrowsableState = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DebuggerDisplayAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, value: str) -> None:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Target(self) -> Type:
        """"""
    @Target.setter
    def Target(self, value: Type) -> None: ...
    @property
    def TargetTypeName(self) -> str:
        """"""
    @TargetTypeName.setter
    def TargetTypeName(self, value: str) -> None: ...
    @property
    def Type(self) -> str:
        """"""
    @Type.setter
    def Type(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Value(self) -> str:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DebuggerHiddenAttribute(Attribute, _Attribute):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DebuggerNonUserCodeAttribute(Attribute, _Attribute):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DebuggerStepThroughAttribute(Attribute, _Attribute):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DebuggerStepperBoundaryAttribute(Attribute, _Attribute):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DebuggerTypeProxyAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, type: Type) -> None:
        """"""
    @overload
    def __init__(self, typeName: str) -> None:
        """"""
    @property
    def ProxyTypeName(self) -> str:
        """"""
    @property
    def Target(self) -> Type:
        """"""
    @Target.setter
    def Target(self, value: Type) -> None: ...
    @property
    def TargetTypeName(self) -> str:
        """"""
    @TargetTypeName.setter
    def TargetTypeName(self, value: str) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DebuggerVisualizerAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, visualizerTypeName: str) -> None:
        """"""
    @overload
    def __init__(self, visualizerTypeName: str, visualizerObjectSourceTypeName: str) -> None:
        """"""
    @overload
    def __init__(self, visualizerTypeName: str, visualizerObjectSource: Type) -> None:
        """"""
    @overload
    def __init__(self, visualizer: Type) -> None:
        """"""
    @overload
    def __init__(self, visualizer: Type, visualizerObjectSource: Type) -> None:
        """"""
    @overload
    def __init__(self, visualizer: Type, visualizerObjectSourceTypeName: str) -> None:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @Description.setter
    def Description(self, value: str) -> None: ...
    @property
    def Target(self) -> Type:
        """"""
    @Target.setter
    def Target(self, value: Type) -> None: ...
    @property
    def TargetTypeName(self) -> str:
        """"""
    @TargetTypeName.setter
    def TargetTypeName(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def VisualizerObjectSourceTypeName(self) -> str:
        """"""
    @property
    def VisualizerTypeName(self) -> str:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DefaultFilter(AssertFilter):
    """"""
    def AssertFailure(
        self,
        condition: str,
        message: str,
        location: StackTrace,
        stackTraceFormat: StackTrace.TraceFormat,
        windowTitle: str,
    ) -> AssertFilters:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DefaultTraceListener(TraceListener, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AssertUiEnabled(self) -> bool:
        """"""
    @AssertUiEnabled.setter
    def AssertUiEnabled(self, value: bool) -> None: ...
    @property
    def Attributes(self) -> StringDictionary:
        """"""
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
    def LogFileName(self) -> str:
        """"""
    @LogFileName.setter
    def LogFileName(self, value: str) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DelimitedListTraceListener(TextWriterTraceListener, IDisposable):
    """"""
    @overload
    def __init__(self, stream: Stream) -> None:
        """"""
    @overload
    def __init__(self, stream: Stream, name: str) -> None:
        """"""
    @overload
    def __init__(self, writer: TextWriter) -> None:
        """"""
    @overload
    def __init__(self, writer: TextWriter, name: str) -> None:
        """"""
    @overload
    def __init__(self, fileName: str) -> None:
        """"""
    @overload
    def __init__(self, fileName: str, name: str) -> None:
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
    @property
    def Writer(self) -> TextWriter:
        """"""
    @Writer.setter
    def Writer(self, value: TextWriter) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DiagnosticsConfiguration(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DiagnosticsConfigurationHandler(Object, IConfigurationSectionHandler):
    """"""
    def __init__(self) -> None:
        """"""
    def Create(self, parent: object, configContext: object, section: XmlNode) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EditAndContinueHelper(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EntryWrittenEventArgs(EventArgs):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, entry: EventLogEntry) -> None:
        """"""
    @property
    def Entry(self) -> EventLogEntry:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type EntryWrittenEventHandler = Callable[[object, EntryWrittenEventArgs], None]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EnvironmentBlock(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ToByteArray(cls, sd: StringDictionary, unicode: bool) -> Array[int]:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventInstance(Object):
    """"""
    @overload
    def __init__(self, instanceId: int, categoryId: int) -> None:
        """"""
    @overload
    def __init__(self, instanceId: int, categoryId: int, entryType: EventLogEntryType) -> None:
        """"""
    @property
    def CategoryId(self) -> int:
        """"""
    @CategoryId.setter
    def CategoryId(self, value: int) -> None: ...
    @property
    def EntryType(self) -> EventLogEntryType:
        """"""
    @EntryType.setter
    def EntryType(self, value: EventLogEntryType) -> None: ...
    @property
    def InstanceId(self) -> int:
        """"""
    @InstanceId.setter
    def InstanceId(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventLog(Component, IComponent, ISupportInitialize, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, logName: str) -> None:
        """"""
    @overload
    def __init__(self, logName: str, machineName: str) -> None:
        """"""
    @overload
    def __init__(self, logName: str, machineName: str, source: str) -> None:
        """"""
    @property
    def Container(self) -> IContainer:
        """"""
    @property
    def EnableRaisingEvents(self) -> bool:
        """"""
    @EnableRaisingEvents.setter
    def EnableRaisingEvents(self, value: bool) -> None: ...
    @property
    def Entries(self) -> EventLogEntryCollection:
        """"""
    @property
    def Log(self) -> str:
        """"""
    @Log.setter
    def Log(self, value: str) -> None: ...
    @property
    def LogDisplayName(self) -> str:
        """"""
    @property
    def MachineName(self) -> str:
        """"""
    @MachineName.setter
    def MachineName(self, value: str) -> None: ...
    @property
    def MaximumKilobytes(self) -> int:
        """"""
    @MaximumKilobytes.setter
    def MaximumKilobytes(self, value: int) -> None: ...
    @property
    def MinimumRetentionDays(self) -> int:
        """"""
    @property
    def OverflowAction(self) -> OverflowAction:
        """"""
    @property
    def Site(self) -> ISite:
        """"""
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    @property
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke:
        """"""
    @SynchronizingObject.setter
    def SynchronizingObject(self, value: ISynchronizeInvoke) -> None: ...
    def BeginInit(self) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Close(self) -> None:
        """"""
    @classmethod
    @overload
    def CreateEventSource(cls, sourceData: EventSourceCreationData) -> None:
        """"""
    @classmethod
    @overload
    def CreateEventSource(cls, source: str, logName: str) -> None:
        """"""
    @classmethod
    @overload
    def CreateEventSource(cls, source: str, logName: str, machineName: str) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    @classmethod
    @overload
    def Delete(cls, logName: str) -> None:
        """"""
    @classmethod
    @overload
    def Delete(cls, logName: str, machineName: str) -> None:
        """"""
    @classmethod
    @overload
    def DeleteEventSource(cls, source: str) -> None:
        """"""
    @classmethod
    @overload
    def DeleteEventSource(cls, source: str, machineName: str) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndInit(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def Exists(cls, logName: str) -> bool:
        """"""
    @classmethod
    @overload
    def Exists(cls, logName: str, machineName: str) -> bool:
        """"""
    @classmethod
    @overload
    def GetEventLogs(cls) -> Array[EventLog]:
        """"""
    @classmethod
    @overload
    def GetEventLogs(cls, machineName: str) -> Array[EventLog]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    @classmethod
    def LogNameFromSourceName(cls, source: str, machineName: str) -> str:
        """"""
    def ModifyOverflowPolicy(self, action: OverflowAction, retentionDays: int) -> None:
        """"""
    def RegisterDisplayName(self, resourceFile: str, resourceId: int) -> None:
        """"""
    @classmethod
    @overload
    def SourceExists(cls, source: str) -> bool:
        """"""
    @classmethod
    @overload
    def SourceExists(cls, source: str, machineName: str) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def WriteEntry(self, message: str) -> None:
        """"""
    @overload
    def WriteEntry(self, message: str, type: EventLogEntryType) -> None:
        """"""
    @overload
    def WriteEntry(self, message: str, type: EventLogEntryType, eventID: int) -> None:
        """"""
    @overload
    def WriteEntry(
        self, message: str, type: EventLogEntryType, eventID: int, category: int
    ) -> None:
        """"""
    @overload
    def WriteEntry(
        self,
        message: str,
        type: EventLogEntryType,
        eventID: int,
        category: int,
        rawData: Array[int],
    ) -> None:
        """"""
    @classmethod
    @overload
    def WriteEntry(cls, source: str, message: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteEntry(cls, source: str, message: str, type: EventLogEntryType) -> None:
        """"""
    @classmethod
    @overload
    def WriteEntry(cls, source: str, message: str, type: EventLogEntryType, eventID: int) -> None:
        """"""
    @classmethod
    @overload
    def WriteEntry(
        cls, source: str, message: str, type: EventLogEntryType, eventID: int, category: int
    ) -> None:
        """"""
    @classmethod
    @overload
    def WriteEntry(
        cls,
        source: str,
        message: str,
        type: EventLogEntryType,
        eventID: int,
        category: int,
        rawData: Array[int],
    ) -> None:
        """"""
    @overload
    def WriteEvent(self, instance: EventInstance, data: Array[int], values: Array[object]) -> None:
        """"""
    @overload
    def WriteEvent(self, instance: EventInstance, values: Array[object]) -> None:
        """"""
    @classmethod
    @overload
    def WriteEvent(
        cls, source: str, instance: EventInstance, data: Array[int], values: Array[object]
    ) -> None:
        """"""
    @classmethod
    @overload
    def WriteEvent(cls, source: str, instance: EventInstance, values: Array[object]) -> None:
        """"""
    Disposed: EventType[EventHandler] = ...
    """"""
    EntryWritten: EventType[EntryWrittenEventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventLogEntry(Component, IComponent, ISerializable, IDisposable):
    """"""
    @property
    def Category(self) -> str:
        """"""
    @property
    def CategoryNumber(self) -> int:
        """"""
    @property
    def Container(self) -> IContainer:
        """"""
    @property
    def Data(self) -> Array[int]:
        """"""
    @property
    def EntryType(self) -> EventLogEntryType:
        """"""
    @property
    def EventID(self) -> int:
        """"""
    @property
    def Index(self) -> int:
        """"""
    @property
    def InstanceId(self) -> int:
        """"""
    @property
    def MachineName(self) -> str:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def ReplacementStrings(self) -> Array[str]:
        """"""
    @property
    def Site(self) -> ISite:
        """"""
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    @property
    def Source(self) -> str:
        """"""
    @property
    def TimeGenerated(self) -> DateTime:
        """"""
    @property
    def TimeWritten(self) -> DateTime:
        """"""
    @property
    def UserName(self) -> str:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    @overload
    def Equals(self, otherEntry: EventLogEntry) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def ToString(self) -> str:
        """"""
    Disposed: EventType[EventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventLogEntryCollection(Object, ICollection, IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> EventLogEntry:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, entries: Array[EventLogEntry], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> EventLogEntry:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class EventLogEntryType(Enum):
    """"""

    Error: EventLogEntryType = ...
    """"""
    Warning: EventLogEntryType = ...
    """"""
    Information: EventLogEntryType = ...
    """"""
    SuccessAudit: EventLogEntryType = ...
    """"""
    FailureAudit: EventLogEntryType = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventLogInternal(Object, ISupportInitialize, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, logName: str) -> None:
        """"""
    @overload
    def __init__(self, logName: str, machineName: str) -> None:
        """"""
    @overload
    def __init__(self, logName: str, machineName: str, source: str) -> None:
        """"""
    @overload
    def __init__(self, logName: str, machineName: str, source: str, parent: EventLog) -> None:
        """"""
    @property
    def EnableRaisingEvents(self) -> bool:
        """"""
    @EnableRaisingEvents.setter
    def EnableRaisingEvents(self, value: bool) -> None: ...
    @property
    def Entries(self) -> EventLogEntryCollection:
        """"""
    @property
    def Log(self) -> str:
        """"""
    @property
    def LogDisplayName(self) -> str:
        """"""
    @property
    def MachineName(self) -> str:
        """"""
    @property
    def MaximumKilobytes(self) -> int:
        """"""
    @MaximumKilobytes.setter
    def MaximumKilobytes(self, value: int) -> None: ...
    @property
    def MinimumRetentionDays(self) -> int:
        """"""
    @property
    def OverflowAction(self) -> OverflowAction:
        """"""
    @property
    def Source(self) -> str:
        """"""
    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke:
        """"""
    @SynchronizingObject.setter
    def SynchronizingObject(self, value: ISynchronizeInvoke) -> None: ...
    def BeginInit(self) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndInit(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ModifyOverflowPolicy(self, action: OverflowAction, retentionDays: int) -> None:
        """"""
    def RegisterDisplayName(self, resourceFile: str, resourceId: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def WriteEntry(self, message: str) -> None:
        """"""
    @overload
    def WriteEntry(self, message: str, type: EventLogEntryType) -> None:
        """"""
    @overload
    def WriteEntry(self, message: str, type: EventLogEntryType, eventID: int) -> None:
        """"""
    @overload
    def WriteEntry(
        self, message: str, type: EventLogEntryType, eventID: int, category: int
    ) -> None:
        """"""
    @overload
    def WriteEntry(
        self,
        message: str,
        type: EventLogEntryType,
        eventID: int,
        category: int,
        rawData: Array[int],
    ) -> None:
        """"""
    @overload
    def WriteEvent(self, instance: EventInstance, data: Array[int], values: Array[object]) -> None:
        """"""
    @overload
    def WriteEvent(self, instance: EventInstance, values: Array[object]) -> None:
        """"""
    EntryWritten: EventType[EntryWrittenEventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventLogPermission(
    ResourcePermissionBase, IUnrestrictedPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(self, permissionAccess: EventLogPermissionAccess, machineName: str) -> None:
        """"""
    @overload
    def __init__(self, permissionAccessEntries: Array[EventLogPermissionEntry]) -> None:
        """"""
    @property
    def PermissionEntries(self) -> EventLogPermissionEntryCollection:
        """"""
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """"""
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FromXml(self, securityElement: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, target: IPermission) -> IPermission:
        """"""
    def IsSubsetOf(self, target: IPermission) -> bool:
        """"""
    def IsUnrestricted(self) -> bool:
        """"""
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""
    def Union(self, target: IPermission) -> IPermission:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class EventLogPermissionAccess(Enum):
    """"""

    _None: EventLogPermissionAccess = ...
    """"""
    Browse: EventLogPermissionAccess = ...
    """"""
    Instrument: EventLogPermissionAccess = ...
    """"""
    Audit: EventLogPermissionAccess = ...
    """"""
    Write: EventLogPermissionAccess = ...
    """"""
    Administer: EventLogPermissionAccess = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventLogPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def MachineName(self) -> str:
        """"""
    @MachineName.setter
    def MachineName(self, value: str) -> None: ...
    @property
    def PermissionAccess(self) -> EventLogPermissionAccess:
        """"""
    @PermissionAccess.setter
    def PermissionAccess(self, value: EventLogPermissionAccess) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Unrestricted(self) -> bool:
        """"""
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventLogPermissionEntry(Object):
    """"""
    def __init__(self, permissionAccess: EventLogPermissionAccess, machineName: str) -> None:
        """"""
    @property
    def MachineName(self) -> str:
        """"""
    @property
    def PermissionAccess(self) -> EventLogPermissionAccess:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventLogPermissionEntryCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> EventLogPermissionEntry:
        """"""
    @Item.setter
    def Item(self, value: EventLogPermissionEntry) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, value: EventLogPermissionEntry) -> int:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    @overload
    def AddRange(self, value: EventLogPermissionEntryCollection) -> None:
        """"""
    @overload
    def AddRange(self, value: Array[EventLogPermissionEntry]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: EventLogPermissionEntry) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[EventLogPermissionEntry], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, value: EventLogPermissionEntry) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, value: EventLogPermissionEntry) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, value: EventLogPermissionEntry) -> None:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: EventLogPermissionEntry) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, value: EventLogPermissionEntry) -> None:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> EventLogPermissionEntry:
        """"""
    @overload
    def __setitem__(self, index: int, value: EventLogPermissionEntry) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventLogTraceListener(TraceListener, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, eventLog: EventLog) -> None:
        """"""
    @overload
    def __init__(self, source: str) -> None:
        """"""
    @property
    def Attributes(self) -> StringDictionary:
        """"""
    @property
    def EventLog(self) -> EventLog:
        """"""
    @EventLog.setter
    def EventLog(self, value: EventLog) -> None: ...
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
        severity: TraceEventType,
        id: int,
        data: Array[object],
    ) -> None:
        """"""
    @overload
    def TraceData(
        self,
        eventCache: TraceEventCache,
        source: str,
        severity: TraceEventType,
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
        severity: TraceEventType,
        id: int,
        message: str,
    ) -> None:
        """"""
    @overload
    def TraceEvent(
        self,
        eventCache: TraceEventCache,
        source: str,
        severity: TraceEventType,
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventSchemaTraceListener(TextWriterTraceListener, IDisposable):
    """"""
    @overload
    def __init__(self, fileName: str) -> None:
        """"""
    @overload
    def __init__(self, fileName: str, name: str) -> None:
        """"""
    @overload
    def __init__(self, fileName: str, name: str, bufferSize: int) -> None:
        """"""
    @overload
    def __init__(
        self, fileName: str, name: str, bufferSize: int, logRetentionOption: TraceLogRetentionOption
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        fileName: str,
        name: str,
        bufferSize: int,
        logRetentionOption: TraceLogRetentionOption,
        maximumFileSize: int,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        fileName: str,
        name: str,
        bufferSize: int,
        logRetentionOption: TraceLogRetentionOption,
        maximumFileSize: int,
        maximumNumberOfFiles: int,
    ) -> None:
        """"""
    @property
    def Attributes(self) -> StringDictionary:
        """"""
    @property
    def BufferSize(self) -> int:
        """"""
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
    def MaximumFileSize(self) -> int:
        """"""
    @property
    def MaximumNumberOfFiles(self) -> int:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def TraceLogRetentionOption(self) -> TraceLogRetentionOption:
        """"""
    @property
    def TraceOutputOptions(self) -> TraceOptions:
        """"""
    @TraceOutputOptions.setter
    def TraceOutputOptions(self, value: TraceOptions) -> None: ...
    @property
    def Writer(self) -> TextWriter:
        """"""
    @Writer.setter
    def Writer(self, value: TextWriter) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventSourceCreationData(Object):
    """"""
    def __init__(self, source: str, logName: str) -> None:
        """"""
    @property
    def CategoryCount(self) -> int:
        """"""
    @CategoryCount.setter
    def CategoryCount(self, value: int) -> None: ...
    @property
    def CategoryResourceFile(self) -> str:
        """"""
    @CategoryResourceFile.setter
    def CategoryResourceFile(self, value: str) -> None: ...
    @property
    def LogName(self) -> str:
        """"""
    @LogName.setter
    def LogName(self, value: str) -> None: ...
    @property
    def MachineName(self) -> str:
        """"""
    @MachineName.setter
    def MachineName(self, value: str) -> None: ...
    @property
    def MessageResourceFile(self) -> str:
        """"""
    @MessageResourceFile.setter
    def MessageResourceFile(self, value: str) -> None: ...
    @property
    def ParameterResourceFile(self) -> str:
        """"""
    @ParameterResourceFile.setter
    def ParameterResourceFile(self, value: str) -> None: ...
    @property
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventTypeFilter(TraceFilter):
    """"""
    def __init__(self, level: SourceLevels) -> None:
        """"""
    @property
    def EventType(self) -> SourceLevels:
        """"""
    @EventType.setter
    def EventType(self, value: SourceLevels) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ShouldTrace(
        self,
        cache: TraceEventCache,
        source: str,
        eventType: TraceEventType,
        id: int,
        formatOrMessage: str,
        args: Array[object],
        data1: object,
        data: Array[object],
    ) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FileVersionInfo(Object):
    """"""
    @property
    def Comments(self) -> str:
        """"""
    @property
    def CompanyName(self) -> str:
        """"""
    @property
    def FileBuildPart(self) -> int:
        """"""
    @property
    def FileDescription(self) -> str:
        """"""
    @property
    def FileMajorPart(self) -> int:
        """"""
    @property
    def FileMinorPart(self) -> int:
        """"""
    @property
    def FileName(self) -> str:
        """"""
    @property
    def FilePrivatePart(self) -> int:
        """"""
    @property
    def FileVersion(self) -> str:
        """"""
    @property
    def InternalName(self) -> str:
        """"""
    @property
    def IsDebug(self) -> bool:
        """"""
    @property
    def IsPatched(self) -> bool:
        """"""
    @property
    def IsPreRelease(self) -> bool:
        """"""
    @property
    def IsPrivateBuild(self) -> bool:
        """"""
    @property
    def IsSpecialBuild(self) -> bool:
        """"""
    @property
    def Language(self) -> str:
        """"""
    @property
    def LegalCopyright(self) -> str:
        """"""
    @property
    def LegalTrademarks(self) -> str:
        """"""
    @property
    def OriginalFilename(self) -> str:
        """"""
    @property
    def PrivateBuild(self) -> str:
        """"""
    @property
    def ProductBuildPart(self) -> int:
        """"""
    @property
    def ProductMajorPart(self) -> int:
        """"""
    @property
    def ProductMinorPart(self) -> int:
        """"""
    @property
    def ProductName(self) -> str:
        """"""
    @property
    def ProductPrivatePart(self) -> int:
        """"""
    @property
    def ProductVersion(self) -> str:
        """"""
    @property
    def SpecialBuild(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetVersionInfo(cls, fileName: str) -> FileVersionInfo:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FilterElement(TypedElement):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def InitData(self) -> str:
        """"""
    @InitData.setter
    def InitData(self, value: str) -> None: ...
    @property
    def LockAllAttributesExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAllElementsExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAttributes(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockElements(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockItem(self) -> bool:
        """"""
    @LockItem.setter
    def LockItem(self, value: bool) -> None: ...
    @property
    def TypeName(self) -> str:
        """"""
    @TypeName.setter
    def TypeName(self, value: str) -> None: ...
    def Equals(self, compareTo: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetRuntimeObject(self) -> TraceFilter:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ICollectData(ABC):
    """"""
    def CloseData(self) -> None:
        """"""
    def CollectData(
        self, id: int, valueName: IntPtr, data: IntPtr, totalBytes: int, res: IntPtr
    ) -> tuple[None, IntPtr]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ICustomDebuggerNotification(ABC):
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class InitState(Enum):
    """"""

    NotInitialized: InitState = ...
    """"""
    Initializing: InitState = ...
    """"""
    Initialized: InitState = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class InstanceData(Object):
    """"""
    def __init__(self, instanceName: str, sample: CounterSample) -> None:
        """"""
    @property
    def InstanceName(self) -> str:
        """"""
    @property
    def RawValue(self) -> int:
        """"""
    @property
    def Sample(self) -> CounterSample:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class InstanceDataCollection(DictionaryBase, ICollection, IDictionary, IEnumerable):
    """"""
    def __init__(self, counterName: str) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def CounterName(self) -> str:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> InstanceData:
        """"""
    @property
    def Keys(self) -> ICollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> ICollection:
        """"""
    def Add(self, key: object, value: object) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, key: object) -> bool:
        """"""
    @overload
    def Contains(self, instanceName: str) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, instances: Array[InstanceData], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, key: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, key: object) -> bool:
        """"""
    @overload
    def __contains__(self, instanceName: str) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, key: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, key: object) -> object:
        """"""
    @overload
    def __getitem__(self, instanceName: str) -> InstanceData:
        """"""
    def __setitem__(self, key: object, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class InstanceDataCollectionCollection(DictionaryBase, ICollection, IDictionary, IEnumerable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> InstanceDataCollection:
        """"""
    @property
    def Keys(self) -> ICollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> ICollection:
        """"""
    def Add(self, key: object, value: object) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, key: object) -> bool:
        """"""
    @overload
    def Contains(self, counterName: str) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, counters: Array[InstanceDataCollection], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, key: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, key: object) -> bool:
        """"""
    @overload
    def __contains__(self, counterName: str) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, key: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, key: object) -> object:
        """"""
    @overload
    def __getitem__(self, counterName: str) -> InstanceDataCollection:
        """"""
    def __setitem__(self, key: object, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ListenerElement(TypedElement):
    """"""
    def __init__(self, allowReferences: bool) -> None:
        """"""
    @property
    def Attributes(self) -> Hashtable:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def Filter(self) -> FilterElement:
        """"""
    @property
    def InitData(self) -> str:
        """"""
    @InitData.setter
    def InitData(self, value: str) -> None: ...
    @property
    def LockAllAttributesExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAllElementsExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAttributes(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockElements(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockItem(self) -> bool:
        """"""
    @LockItem.setter
    def LockItem(self, value: bool) -> None: ...
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
    @property
    def TypeName(self) -> str:
        """"""
    @TypeName.setter
    def TypeName(self, value: str) -> None: ...
    def Equals(self, compareTo: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetRuntimeObject(self) -> TraceListener:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ListenerElementsCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CollectionType(self) -> ConfigurationElementCollectionType:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def EmitClear(self) -> bool:
        """"""
    @EmitClear.setter
    def EmitClear(self, value: bool) -> None: ...
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> ListenerElement:
        """"""
    @property
    def LockAllAttributesExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAllElementsExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAttributes(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockElements(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockItem(self) -> bool:
        """"""
    @LockItem.setter
    def LockItem(self, value: bool) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[ConfigurationElement], index: int) -> None:
        """"""
    def Equals(self, compareTo: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetRuntimeObject(self) -> TraceListenerCollection:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, name: str) -> ListenerElement:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Log(ABC, Object):
    """"""

    GlobalSwitch: ClassVar[LogSwitch]
    """"""
    @classmethod
    @property
    def IsConsoleEnabled(cls) -> bool:
        """"""
    @classmethod
    @IsConsoleEnabled.setter
    def IsConsoleEnabled(cls, value: bool) -> None: ...
    @classmethod
    def AddOnLogMessage(cls, handler: LogMessageEventHandler) -> None:
        """"""
    @classmethod
    def AddOnLogSwitchLevel(cls, handler: LogSwitchLevelHandler) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def Error(cls, logswitch: LogSwitch, message: str) -> None:
        """"""
    @classmethod
    @overload
    def Error(cls, message: str) -> None:
        """"""
    @classmethod
    @overload
    def Error(cls, switchname: str, message: str) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def LogMessage(cls, level: LoggingLevels, logswitch: LogSwitch, message: str) -> None:
        """"""
    @classmethod
    @overload
    def LogMessage(cls, level: LoggingLevels, message: str) -> None:
        """"""
    @classmethod
    def Panic(cls, message: str) -> None:
        """"""
    @classmethod
    def RemoveOnLogMessage(cls, handler: LogMessageEventHandler) -> None:
        """"""
    @classmethod
    def RemoveOnLogSwitchLevel(cls, handler: LogSwitchLevelHandler) -> None:
        """"""
    @classmethod
    @overload
    def Status(cls, logswitch: LogSwitch, message: str) -> None:
        """"""
    @classmethod
    @overload
    def Status(cls, message: str) -> None:
        """"""
    @classmethod
    @overload
    def Status(cls, switchname: str, message: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def Trace(cls, logswitch: LogSwitch, message: str) -> None:
        """"""
    @classmethod
    @overload
    def Trace(cls, message: str) -> None:
        """"""
    @classmethod
    @overload
    def Trace(cls, switchname: str, message: str) -> None:
        """"""
    @classmethod
    @overload
    def Warning(cls, logswitch: LogSwitch, message: str) -> None:
        """"""
    @classmethod
    @overload
    def Warning(cls, message: str) -> None:
        """"""
    @classmethod
    @overload
    def Warning(cls, switchname: str, message: str) -> None:
        """"""

type LogMessageEventHandler = Callable[[LoggingLevels, LogSwitch, str, StackTrace], None]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class LogSwitch(Object):
    """"""
    def __init__(self, name: str, description: str, parent: LogSwitch) -> None:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def MinimumLevel(self) -> LoggingLevels:
        """"""
    @MinimumLevel.setter
    def MinimumLevel(self, value: LoggingLevels) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @property
    def Parent(self) -> LogSwitch:
        """"""
    def CheckLevel(self, level: LoggingLevels) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetSwitch(cls, name: str) -> LogSwitch:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type LogSwitchLevelHandler = Callable[[LogSwitch, LoggingLevels], None]
""""""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class LoggingLevels(Enum):
    """"""

    TraceLevel0: LoggingLevels = ...
    """"""
    TraceLevel1: LoggingLevels = ...
    """"""
    TraceLevel2: LoggingLevels = ...
    """"""
    TraceLevel3: LoggingLevels = ...
    """"""
    TraceLevel4: LoggingLevels = ...
    """"""
    StatusLevel0: LoggingLevels = ...
    """"""
    StatusLevel1: LoggingLevels = ...
    """"""
    StatusLevel2: LoggingLevels = ...
    """"""
    StatusLevel3: LoggingLevels = ...
    """"""
    StatusLevel4: LoggingLevels = ...
    """"""
    WarningLevel: LoggingLevels = ...
    """"""
    ErrorLevel: LoggingLevels = ...
    """"""
    PanicLevel: LoggingLevels = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MainWindowFinder(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FindMainWindow(self, processId: int) -> IntPtr:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MessageBoxPopup(Object):
    """"""
    def __init__(self, body: str, title: str, flags: int) -> None:
        """"""
    @property
    def ReturnValue(self) -> int:
        """"""
    @ReturnValue.setter
    def ReturnValue(self, value: int) -> None: ...
    def DoPopup(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ShowMessageBox(self) -> int:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ModuleInfo(Object):
    """"""

    Id: Final[int]
    """"""
    baseName: Final[str]
    """"""
    baseOfDll: Final[IntPtr]
    """"""
    entryPoint: Final[IntPtr]
    """"""
    fileName: Final[str]
    """"""
    sizeOfImage: Final[int]
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MonitoringDescriptionAttribute(DescriptionAttribute, _Attribute):
    """"""
    def __init__(self, description: str) -> None:
        """"""
    @property
    def Description(self) -> str:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NtProcessInfoHelper(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetProcessInfos(cls, processIdFilter: Predicate[int] = ...) -> Array[ProcessInfo]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NtProcessManager(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetFirstModuleInfo(cls, processId: int) -> ModuleInfo:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetModuleInfos(cls, processId: int) -> Array[ModuleInfo]:
        """"""
    @classmethod
    def GetProcessIdFromHandle(cls, processHandle: SafeProcessHandle) -> int:
        """"""
    @classmethod
    @overload
    def GetProcessIds(cls) -> Array[int]:
        """"""
    @classmethod
    @overload
    def GetProcessIds(cls, machineName: str, isRemoteMachine: bool) -> Array[int]:
        """"""
    @classmethod
    def GetProcessInfos(cls, machineName: str, isRemoteMachine: bool) -> Array[ProcessInfo]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class OrdinalCaseInsensitiveComparer(Object, IComparer):
    """"""
    def __init__(self) -> None:
        """"""
    def Compare(self, a: object, b: object) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class OverflowAction(Enum):
    """"""

    OverwriteAsNeeded: OverflowAction = ...
    """"""
    OverwriteOlder: OverflowAction = ...
    """"""
    DoNotOverwrite: OverflowAction = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PerfCounterSection(ConfigurationElement):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def FileMappingSize(self) -> int:
        """"""
    @property
    def LockAllAttributesExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAllElementsExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAttributes(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockElements(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockItem(self) -> bool:
        """"""
    @LockItem.setter
    def LockItem(self, value: bool) -> None: ...
    def Equals(self, compareTo: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PerformanceCounter(Component, IComponent, ISupportInitialize, IDisposable):
    """"""

    DefaultFileMappingSize: ClassVar[int]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(
        self, categoryName: str, counterName: str, instanceName: str, machineName: str
    ) -> None:
        """"""
    @overload
    def __init__(self, categoryName: str, counterName: str, instanceName: str) -> None:
        """"""
    @overload
    def __init__(
        self, categoryName: str, counterName: str, instanceName: str, readOnly: bool
    ) -> None:
        """"""
    @overload
    def __init__(self, categoryName: str, counterName: str) -> None:
        """"""
    @overload
    def __init__(self, categoryName: str, counterName: str, readOnly: bool) -> None:
        """"""
    @property
    def CategoryName(self) -> str:
        """"""
    @CategoryName.setter
    def CategoryName(self, value: str) -> None: ...
    @property
    def Container(self) -> IContainer:
        """"""
    @property
    def CounterHelp(self) -> str:
        """"""
    @property
    def CounterName(self) -> str:
        """"""
    @CounterName.setter
    def CounterName(self, value: str) -> None: ...
    @property
    def CounterType(self) -> PerformanceCounterType:
        """"""
    @property
    def InstanceLifetime(self) -> PerformanceCounterInstanceLifetime:
        """"""
    @InstanceLifetime.setter
    def InstanceLifetime(self, value: PerformanceCounterInstanceLifetime) -> None: ...
    @property
    def InstanceName(self) -> str:
        """"""
    @InstanceName.setter
    def InstanceName(self, value: str) -> None: ...
    @property
    def MachineName(self) -> str:
        """"""
    @MachineName.setter
    def MachineName(self, value: str) -> None: ...
    @property
    def RawValue(self) -> int:
        """"""
    @RawValue.setter
    def RawValue(self, value: int) -> None: ...
    @property
    def ReadOnly(self) -> bool:
        """"""
    @ReadOnly.setter
    def ReadOnly(self, value: bool) -> None: ...
    @property
    def Site(self) -> ISite:
        """"""
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    def BeginInit(self) -> None:
        """"""
    def Close(self) -> None:
        """"""
    @classmethod
    def CloseSharedResources(cls) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Decrement(self) -> int:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndInit(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def Increment(self) -> int:
        """"""
    def IncrementBy(self, value: int) -> int:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def NextSample(self) -> CounterSample:
        """"""
    def NextValue(self) -> float:
        """"""
    def RemoveInstance(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    Disposed: EventType[EventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PerformanceCounterCategory(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, categoryName: str) -> None:
        """"""
    @overload
    def __init__(self, categoryName: str, machineName: str) -> None:
        """"""
    @property
    def CategoryHelp(self) -> str:
        """"""
    @property
    def CategoryName(self) -> str:
        """"""
    @CategoryName.setter
    def CategoryName(self, value: str) -> None: ...
    @property
    def CategoryType(self) -> PerformanceCounterCategoryType:
        """"""
    @property
    def MachineName(self) -> str:
        """"""
    @MachineName.setter
    def MachineName(self, value: str) -> None: ...
    @overload
    def CounterExists(self, counterName: str) -> bool:
        """"""
    @classmethod
    @overload
    def CounterExists(cls, counterName: str, categoryName: str) -> bool:
        """"""
    @classmethod
    @overload
    def CounterExists(cls, counterName: str, categoryName: str, machineName: str) -> bool:
        """"""
    @classmethod
    @overload
    def Create(
        cls, categoryName: str, categoryHelp: str, counterData: CounterCreationDataCollection
    ) -> PerformanceCounterCategory:
        """"""
    @classmethod
    @overload
    def Create(
        cls,
        categoryName: str,
        categoryHelp: str,
        categoryType: PerformanceCounterCategoryType,
        counterData: CounterCreationDataCollection,
    ) -> PerformanceCounterCategory:
        """"""
    @classmethod
    @overload
    def Create(
        cls,
        categoryName: str,
        categoryHelp: str,
        categoryType: PerformanceCounterCategoryType,
        counterName: str,
        counterHelp: str,
    ) -> PerformanceCounterCategory:
        """"""
    @classmethod
    @overload
    def Create(
        cls, categoryName: str, categoryHelp: str, counterName: str, counterHelp: str
    ) -> PerformanceCounterCategory:
        """"""
    @classmethod
    def Delete(cls, categoryName: str) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def Exists(cls, categoryName: str) -> bool:
        """"""
    @classmethod
    @overload
    def Exists(cls, categoryName: str, machineName: str) -> bool:
        """"""
    @classmethod
    @overload
    def GetCategories(cls) -> Array[PerformanceCounterCategory]:
        """"""
    @classmethod
    @overload
    def GetCategories(cls, machineName: str) -> Array[PerformanceCounterCategory]:
        """"""
    @overload
    def GetCounters(self) -> Array[PerformanceCounter]:
        """"""
    @overload
    def GetCounters(self, instanceName: str) -> Array[PerformanceCounter]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetInstanceNames(self) -> Array[str]:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def InstanceExists(self, instanceName: str) -> bool:
        """"""
    @classmethod
    @overload
    def InstanceExists(cls, instanceName: str, categoryName: str) -> bool:
        """"""
    @classmethod
    @overload
    def InstanceExists(cls, instanceName: str, categoryName: str, machineName: str) -> bool:
        """"""
    def ReadCategory(self) -> InstanceDataCollectionCollection:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class PerformanceCounterCategoryOptions(Enum):
    """"""

    EnableReuse: PerformanceCounterCategoryOptions = ...
    """"""
    UseUniqueSharedMemory: PerformanceCounterCategoryOptions = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class PerformanceCounterCategoryType(Enum):
    """"""

    SingleInstance: PerformanceCounterCategoryType = ...
    """"""
    MultiInstance: PerformanceCounterCategoryType = ...
    """"""
    Unknown: PerformanceCounterCategoryType = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class PerformanceCounterInstanceLifetime(Enum):
    """"""

    Global: PerformanceCounterInstanceLifetime = ...
    """"""
    Process: PerformanceCounterInstanceLifetime = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PerformanceCounterLib(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PerformanceCounterManager(Object, ICollectData):
    """"""
    def __init__(self) -> None:
        """"""
    def CloseData(self) -> None:
        """"""
    def CollectData(
        self, id: int, valueName: IntPtr, data: IntPtr, totalBytes: int, res: IntPtr
    ) -> tuple[None, IntPtr]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PerformanceCounterPermission(
    ResourcePermissionBase, IUnrestrictedPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(
        self,
        permissionAccess: PerformanceCounterPermissionAccess,
        machineName: str,
        categoryName: str,
    ) -> None:
        """"""
    @overload
    def __init__(self, permissionAccessEntries: Array[PerformanceCounterPermissionEntry]) -> None:
        """"""
    @property
    def PermissionEntries(self) -> PerformanceCounterPermissionEntryCollection:
        """"""
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """"""
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FromXml(self, securityElement: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, target: IPermission) -> IPermission:
        """"""
    def IsSubsetOf(self, target: IPermission) -> bool:
        """"""
    def IsUnrestricted(self) -> bool:
        """"""
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""
    def Union(self, target: IPermission) -> IPermission:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class PerformanceCounterPermissionAccess(Enum):
    """"""

    _None: PerformanceCounterPermissionAccess = ...
    """"""
    Read: PerformanceCounterPermissionAccess = ...
    """"""
    Browse: PerformanceCounterPermissionAccess = ...
    """"""
    Write: PerformanceCounterPermissionAccess = ...
    """"""
    Instrument: PerformanceCounterPermissionAccess = ...
    """"""
    Administer: PerformanceCounterPermissionAccess = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PerformanceCounterPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def CategoryName(self) -> str:
        """"""
    @CategoryName.setter
    def CategoryName(self, value: str) -> None: ...
    @property
    def MachineName(self) -> str:
        """"""
    @MachineName.setter
    def MachineName(self, value: str) -> None: ...
    @property
    def PermissionAccess(self) -> PerformanceCounterPermissionAccess:
        """"""
    @PermissionAccess.setter
    def PermissionAccess(self, value: PerformanceCounterPermissionAccess) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Unrestricted(self) -> bool:
        """"""
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PerformanceCounterPermissionEntry(Object):
    """"""
    def __init__(
        self,
        permissionAccess: PerformanceCounterPermissionAccess,
        machineName: str,
        categoryName: str,
    ) -> None:
        """"""
    @property
    def CategoryName(self) -> str:
        """"""
    @property
    def MachineName(self) -> str:
        """"""
    @property
    def PermissionAccess(self) -> PerformanceCounterPermissionAccess:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PerformanceCounterPermissionEntryCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> PerformanceCounterPermissionEntry:
        """"""
    @Item.setter
    def Item(self, value: PerformanceCounterPermissionEntry) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, value: PerformanceCounterPermissionEntry) -> int:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    @overload
    def AddRange(self, value: PerformanceCounterPermissionEntryCollection) -> None:
        """"""
    @overload
    def AddRange(self, value: Array[PerformanceCounterPermissionEntry]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: PerformanceCounterPermissionEntry) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[PerformanceCounterPermissionEntry], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, value: PerformanceCounterPermissionEntry) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, value: PerformanceCounterPermissionEntry) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, value: PerformanceCounterPermissionEntry) -> None:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: PerformanceCounterPermissionEntry) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, value: PerformanceCounterPermissionEntry) -> None:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> PerformanceCounterPermissionEntry:
        """"""
    @overload
    def __setitem__(self, index: int, value: PerformanceCounterPermissionEntry) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class PerformanceCounterType(Enum):
    """"""

    NumberOfItemsHEX32: PerformanceCounterType = ...
    """"""
    NumberOfItemsHEX64: PerformanceCounterType = ...
    """"""
    NumberOfItems32: PerformanceCounterType = ...
    """"""
    NumberOfItems64: PerformanceCounterType = ...
    """"""
    CounterDelta32: PerformanceCounterType = ...
    """"""
    CounterDelta64: PerformanceCounterType = ...
    """"""
    SampleCounter: PerformanceCounterType = ...
    """"""
    CountPerTimeInterval32: PerformanceCounterType = ...
    """"""
    CountPerTimeInterval64: PerformanceCounterType = ...
    """"""
    RateOfCountsPerSecond32: PerformanceCounterType = ...
    """"""
    RateOfCountsPerSecond64: PerformanceCounterType = ...
    """"""
    RawFraction: PerformanceCounterType = ...
    """"""
    CounterTimer: PerformanceCounterType = ...
    """"""
    Timer100Ns: PerformanceCounterType = ...
    """"""
    SampleFraction: PerformanceCounterType = ...
    """"""
    CounterTimerInverse: PerformanceCounterType = ...
    """"""
    Timer100NsInverse: PerformanceCounterType = ...
    """"""
    CounterMultiTimer: PerformanceCounterType = ...
    """"""
    CounterMultiTimer100Ns: PerformanceCounterType = ...
    """"""
    CounterMultiTimerInverse: PerformanceCounterType = ...
    """"""
    CounterMultiTimer100NsInverse: PerformanceCounterType = ...
    """"""
    AverageTimer32: PerformanceCounterType = ...
    """"""
    ElapsedTime: PerformanceCounterType = ...
    """"""
    AverageCount64: PerformanceCounterType = ...
    """"""
    SampleBase: PerformanceCounterType = ...
    """"""
    AverageBase: PerformanceCounterType = ...
    """"""
    RawBase: PerformanceCounterType = ...
    """"""
    CounterMultiBase: PerformanceCounterType = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PerformanceMonitor(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Process(Component, IComponent, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def BasePriority(self) -> int:
        """"""
    @property
    def Container(self) -> IContainer:
        """"""
    @property
    def EnableRaisingEvents(self) -> bool:
        """"""
    @EnableRaisingEvents.setter
    def EnableRaisingEvents(self, value: bool) -> None: ...
    @property
    def ExitCode(self) -> int:
        """"""
    @property
    def ExitTime(self) -> DateTime:
        """"""
    @property
    def Handle(self) -> IntPtr:
        """"""
    @property
    def HandleCount(self) -> int:
        """"""
    @property
    def HasExited(self) -> bool:
        """"""
    @property
    def Id(self) -> int:
        """"""
    @property
    def MachineName(self) -> str:
        """"""
    @property
    def MainModule(self) -> ProcessModule:
        """"""
    @property
    def MainWindowHandle(self) -> IntPtr:
        """"""
    @property
    def MainWindowTitle(self) -> str:
        """"""
    @property
    def MaxWorkingSet(self) -> IntPtr:
        """"""
    @MaxWorkingSet.setter
    def MaxWorkingSet(self, value: IntPtr) -> None: ...
    @property
    def MinWorkingSet(self) -> IntPtr:
        """"""
    @MinWorkingSet.setter
    def MinWorkingSet(self, value: IntPtr) -> None: ...
    @property
    def Modules(self) -> ProcessModuleCollection:
        """"""
    @property
    def NonpagedSystemMemorySize(self) -> int:
        """"""
    @property
    def NonpagedSystemMemorySize64(self) -> int:
        """"""
    @property
    def PagedMemorySize(self) -> int:
        """"""
    @property
    def PagedMemorySize64(self) -> int:
        """"""
    @property
    def PagedSystemMemorySize(self) -> int:
        """"""
    @property
    def PagedSystemMemorySize64(self) -> int:
        """"""
    @property
    def PeakPagedMemorySize(self) -> int:
        """"""
    @property
    def PeakPagedMemorySize64(self) -> int:
        """"""
    @property
    def PeakVirtualMemorySize(self) -> int:
        """"""
    @property
    def PeakVirtualMemorySize64(self) -> int:
        """"""
    @property
    def PeakWorkingSet(self) -> int:
        """"""
    @property
    def PeakWorkingSet64(self) -> int:
        """"""
    @property
    def PriorityBoostEnabled(self) -> bool:
        """"""
    @PriorityBoostEnabled.setter
    def PriorityBoostEnabled(self, value: bool) -> None: ...
    @property
    def PriorityClass(self) -> ProcessPriorityClass:
        """"""
    @PriorityClass.setter
    def PriorityClass(self, value: ProcessPriorityClass) -> None: ...
    @property
    def PrivateMemorySize(self) -> int:
        """"""
    @property
    def PrivateMemorySize64(self) -> int:
        """"""
    @property
    def PrivilegedProcessorTime(self) -> TimeSpan:
        """"""
    @property
    def ProcessName(self) -> str:
        """"""
    @property
    def ProcessorAffinity(self) -> IntPtr:
        """"""
    @ProcessorAffinity.setter
    def ProcessorAffinity(self, value: IntPtr) -> None: ...
    @property
    def Responding(self) -> bool:
        """"""
    @property
    def SafeHandle(self) -> SafeProcessHandle:
        """"""
    @property
    def SessionId(self) -> int:
        """"""
    @property
    def Site(self) -> ISite:
        """"""
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    @property
    def StandardError(self) -> StreamReader:
        """"""
    @property
    def StandardInput(self) -> StreamWriter:
        """"""
    @property
    def StandardOutput(self) -> StreamReader:
        """"""
    @property
    def StartInfo(self) -> ProcessStartInfo:
        """"""
    @StartInfo.setter
    def StartInfo(self, value: ProcessStartInfo) -> None: ...
    @property
    def StartTime(self) -> DateTime:
        """"""
    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke:
        """"""
    @SynchronizingObject.setter
    def SynchronizingObject(self, value: ISynchronizeInvoke) -> None: ...
    @property
    def Threads(self) -> ProcessThreadCollection:
        """"""
    @property
    def TotalProcessorTime(self) -> TimeSpan:
        """"""
    @property
    def UserProcessorTime(self) -> TimeSpan:
        """"""
    @property
    def VirtualMemorySize(self) -> int:
        """"""
    @property
    def VirtualMemorySize64(self) -> int:
        """"""
    @property
    def WorkingSet(self) -> int:
        """"""
    @property
    def WorkingSet64(self) -> int:
        """"""
    def BeginErrorReadLine(self) -> None:
        """"""
    def BeginOutputReadLine(self) -> None:
        """"""
    def CancelErrorRead(self) -> None:
        """"""
    def CancelOutputRead(self) -> None:
        """"""
    def Close(self) -> None:
        """"""
    def CloseMainWindow(self) -> bool:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    @classmethod
    def EnterDebugMode(cls) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetCurrentProcess(cls) -> Process:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    @classmethod
    @overload
    def GetProcessById(cls, processId: int) -> Process:
        """"""
    @classmethod
    @overload
    def GetProcessById(cls, processId: int, machineName: str) -> Process:
        """"""
    @classmethod
    @overload
    def GetProcesses(cls) -> Array[Process]:
        """"""
    @classmethod
    @overload
    def GetProcesses(cls, machineName: str) -> Array[Process]:
        """"""
    @classmethod
    @overload
    def GetProcessesByName(cls, processName: str) -> Array[Process]:
        """"""
    @classmethod
    @overload
    def GetProcessesByName(cls, processName: str, machineName: str) -> Array[Process]:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Kill(self) -> None:
        """"""
    @classmethod
    def LeaveDebugMode(cls) -> None:
        """"""
    def Refresh(self) -> None:
        """"""
    @overload
    def Start(self) -> bool:
        """"""
    @classmethod
    @overload
    def Start(cls, startInfo: ProcessStartInfo) -> Process:
        """"""
    @classmethod
    @overload
    def Start(cls, fileName: str) -> Process:
        """"""
    @classmethod
    @overload
    def Start(cls, fileName: str, arguments: str) -> Process:
        """"""
    @classmethod
    @overload
    def Start(cls, fileName: str, userName: str, password: SecureString, domain: str) -> Process:
        """"""
    @classmethod
    @overload
    def Start(
        cls, fileName: str, arguments: str, userName: str, password: SecureString, domain: str
    ) -> Process:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def WaitForExit(self) -> None:
        """"""
    @overload
    def WaitForExit(self, milliseconds: int) -> bool:
        """"""
    @overload
    def WaitForInputIdle(self) -> bool:
        """"""
    @overload
    def WaitForInputIdle(self, milliseconds: int) -> bool:
        """"""
    Disposed: EventType[EventHandler] = ...
    """"""
    ErrorDataReceived: EventType[DataReceivedEventHandler] = ...
    """"""
    Exited: EventType[EventHandler] = ...
    """"""
    OutputDataReceived: EventType[DataReceivedEventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ProcessData(Object):
    """"""

    ProcessId: Final[int]
    """"""
    StartupTime: Final[int]
    """"""
    def __init__(self, pid: int, startTime: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ProcessInfo(Object):
    """"""

    basePriority: Final[int]
    """"""
    handleCount: Final[int]
    """"""
    mainModuleId: Final[int]
    """"""
    pageFileBytes: Final[int]
    """"""
    pageFileBytesPeak: Final[int]
    """"""
    poolNonpagedBytes: Final[int]
    """"""
    poolPagedBytes: Final[int]
    """"""
    privateBytes: Final[int]
    """"""
    processId: Final[int]
    """"""
    processName: Final[str]
    """"""
    sessionId: Final[int]
    """"""
    threadInfoList: Final[ArrayList]
    """"""
    virtualBytes: Final[int]
    """"""
    virtualBytesPeak: Final[int]
    """"""
    workingSet: Final[int]
    """"""
    workingSetPeak: Final[int]
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ProcessManager(ABC, Object):
    """"""
    @classmethod
    @property
    def IsNt(cls) -> bool:
        """"""
    @classmethod
    @property
    def IsOSOlderThanXP(cls) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetMainWindowHandle(cls, processId: int) -> IntPtr:
        """"""
    @classmethod
    def GetModuleInfos(cls, processId: int) -> Array[ModuleInfo]:
        """"""
    @classmethod
    def GetProcessIdFromHandle(cls, processHandle: SafeProcessHandle) -> int:
        """"""
    @classmethod
    @overload
    def GetProcessIds(cls) -> Array[int]:
        """"""
    @classmethod
    @overload
    def GetProcessIds(cls, machineName: str) -> Array[int]:
        """"""
    @classmethod
    def GetProcessInfo(cls, processId: int, machineName: str) -> ProcessInfo:
        """"""
    @classmethod
    def GetProcessInfos(cls, machineName: str) -> Array[ProcessInfo]:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def IsProcessRunning(cls, processId: int) -> bool:
        """"""
    @classmethod
    @overload
    def IsProcessRunning(cls, processId: int, machineName: str) -> bool:
        """"""
    @classmethod
    def IsRemoteMachine(cls, machineName: str) -> bool:
        """"""
    @classmethod
    def OpenProcess(cls, processId: int, access: int, throwIfExited: bool) -> SafeProcessHandle:
        """"""
    @classmethod
    def OpenThread(cls, threadId: int, access: int) -> SafeThreadHandle:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ProcessModule(Component, IComponent, IDisposable):
    """"""
    @property
    def BaseAddress(self) -> IntPtr:
        """"""
    @property
    def Container(self) -> IContainer:
        """"""
    @property
    def EntryPointAddress(self) -> IntPtr:
        """"""
    @property
    def FileName(self) -> str:
        """"""
    @property
    def FileVersionInfo(self) -> FileVersionInfo:
        """"""
    @property
    def ModuleMemorySize(self) -> int:
        """"""
    @property
    def ModuleName(self) -> str:
        """"""
    @property
    def Site(self) -> ISite:
        """"""
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
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
    Disposed: EventType[EventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ProcessModuleCollection(ReadOnlyCollectionBase, ICollection, IEnumerable):
    """"""
    def __init__(self, processModules: Array[ProcessModule]) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> ProcessModule:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def Contains(self, module: ProcessModule) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[ProcessModule], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IndexOf(self, module: ProcessModule) -> int:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, module: ProcessModule) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> ProcessModule:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class ProcessPriorityClass(Enum):
    """"""

    Normal: ProcessPriorityClass = ...
    """"""
    Idle: ProcessPriorityClass = ...
    """"""
    High: ProcessPriorityClass = ...
    """"""
    RealTime: ProcessPriorityClass = ...
    """"""
    BelowNormal: ProcessPriorityClass = ...
    """"""
    AboveNormal: ProcessPriorityClass = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ProcessStartInfo(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, fileName: str) -> None:
        """"""
    @overload
    def __init__(self, fileName: str, arguments: str) -> None:
        """"""
    @property
    def Arguments(self) -> str:
        """"""
    @Arguments.setter
    def Arguments(self, value: str) -> None: ...
    @property
    def CreateNoWindow(self) -> bool:
        """"""
    @CreateNoWindow.setter
    def CreateNoWindow(self, value: bool) -> None: ...
    @property
    def Domain(self) -> str:
        """"""
    @Domain.setter
    def Domain(self, value: str) -> None: ...
    @property
    def Environment(self) -> IDictionary[str, str]:
        """"""
    @property
    def EnvironmentVariables(self) -> StringDictionary:
        """"""
    @property
    def ErrorDialog(self) -> bool:
        """"""
    @ErrorDialog.setter
    def ErrorDialog(self, value: bool) -> None: ...
    @property
    def ErrorDialogParentHandle(self) -> IntPtr:
        """"""
    @ErrorDialogParentHandle.setter
    def ErrorDialogParentHandle(self, value: IntPtr) -> None: ...
    @property
    def FileName(self) -> str:
        """"""
    @FileName.setter
    def FileName(self, value: str) -> None: ...
    @property
    def LoadUserProfile(self) -> bool:
        """"""
    @LoadUserProfile.setter
    def LoadUserProfile(self, value: bool) -> None: ...
    @property
    def Password(self) -> SecureString:
        """"""
    @Password.setter
    def Password(self, value: SecureString) -> None: ...
    @property
    def PasswordInClearText(self) -> str:
        """"""
    @PasswordInClearText.setter
    def PasswordInClearText(self, value: str) -> None: ...
    @property
    def RedirectStandardError(self) -> bool:
        """"""
    @RedirectStandardError.setter
    def RedirectStandardError(self, value: bool) -> None: ...
    @property
    def RedirectStandardInput(self) -> bool:
        """"""
    @RedirectStandardInput.setter
    def RedirectStandardInput(self, value: bool) -> None: ...
    @property
    def RedirectStandardOutput(self) -> bool:
        """"""
    @RedirectStandardOutput.setter
    def RedirectStandardOutput(self, value: bool) -> None: ...
    @property
    def StandardErrorEncoding(self) -> Encoding:
        """"""
    @StandardErrorEncoding.setter
    def StandardErrorEncoding(self, value: Encoding) -> None: ...
    @property
    def StandardOutputEncoding(self) -> Encoding:
        """"""
    @StandardOutputEncoding.setter
    def StandardOutputEncoding(self, value: Encoding) -> None: ...
    @property
    def UseShellExecute(self) -> bool:
        """"""
    @UseShellExecute.setter
    def UseShellExecute(self, value: bool) -> None: ...
    @property
    def UserName(self) -> str:
        """"""
    @UserName.setter
    def UserName(self, value: str) -> None: ...
    @property
    def Verb(self) -> str:
        """"""
    @Verb.setter
    def Verb(self, value: str) -> None: ...
    @property
    def Verbs(self) -> Array[str]:
        """"""
    @property
    def WindowStyle(self) -> ProcessWindowStyle:
        """"""
    @WindowStyle.setter
    def WindowStyle(self, value: ProcessWindowStyle) -> None: ...
    @property
    def WorkingDirectory(self) -> str:
        """"""
    @WorkingDirectory.setter
    def WorkingDirectory(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ProcessThread(Component, IComponent, IDisposable):
    """"""
    @property
    def BasePriority(self) -> int:
        """"""
    @property
    def Container(self) -> IContainer:
        """"""
    @property
    def CurrentPriority(self) -> int:
        """"""
    @property
    def Id(self) -> int:
        """"""
    @property
    def IdealProcessor(self) -> int:
        """"""
    @IdealProcessor.setter
    def IdealProcessor(self, value: int) -> None: ...
    @property
    def PriorityBoostEnabled(self) -> bool:
        """"""
    @PriorityBoostEnabled.setter
    def PriorityBoostEnabled(self, value: bool) -> None: ...
    @property
    def PriorityLevel(self) -> ThreadPriorityLevel:
        """"""
    @PriorityLevel.setter
    def PriorityLevel(self, value: ThreadPriorityLevel) -> None: ...
    @property
    def PrivilegedProcessorTime(self) -> TimeSpan:
        """"""
    @property
    def ProcessorAffinity(self) -> IntPtr:
        """"""
    @ProcessorAffinity.setter
    def ProcessorAffinity(self, value: IntPtr) -> None: ...
    @property
    def Site(self) -> ISite:
        """"""
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    @property
    def StartAddress(self) -> IntPtr:
        """"""
    @property
    def StartTime(self) -> DateTime:
        """"""
    @property
    def ThreadState(self) -> ThreadState:
        """"""
    @property
    def TotalProcessorTime(self) -> TimeSpan:
        """"""
    @property
    def UserProcessorTime(self) -> TimeSpan:
        """"""
    @property
    def WaitReason(self) -> ThreadWaitReason:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
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
    def ResetIdealProcessor(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    Disposed: EventType[EventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ProcessThreadCollection(ReadOnlyCollectionBase, ICollection, IEnumerable):
    """"""
    def __init__(self, processThreads: Array[ProcessThread]) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> ProcessThread:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def Add(self, thread: ProcessThread) -> int:
        """"""
    def Contains(self, thread: ProcessThread) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[ProcessThread], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IndexOf(self, thread: ProcessThread) -> int:
        """"""
    def Insert(self, index: int, thread: ProcessThread) -> None:
        """"""
    def Remove(self, thread: ProcessThread) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, thread: ProcessThread) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, thread: ProcessThread) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> ProcessThread:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ProcessThreadTimes(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def ExitTime(self) -> DateTime:
        """"""
    @property
    def PrivilegedProcessorTime(self) -> TimeSpan:
        """"""
    @property
    def StartTime(self) -> DateTime:
        """"""
    @property
    def TotalProcessorTime(self) -> TimeSpan:
        """"""
    @property
    def UserProcessorTime(self) -> TimeSpan:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ProcessWaitHandle(WaitHandle, IDisposable):
    """"""
    @property
    def Handle(self) -> IntPtr:
        """"""
    @Handle.setter
    def Handle(self, value: IntPtr) -> None: ...
    @property
    def SafeWaitHandle(self) -> SafeWaitHandle:
        """"""
    @SafeWaitHandle.setter
    def SafeWaitHandle(self, value: SafeWaitHandle) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
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
    @overload
    def WaitOne(self) -> bool:
        """"""
    @overload
    def WaitOne(self, millisecondsTimeout: int) -> bool:
        """"""
    @overload
    def WaitOne(self, millisecondsTimeout: int, exitContext: bool) -> bool:
        """"""
    @overload
    def WaitOne(self, timeout: TimeSpan) -> bool:
        """"""
    @overload
    def WaitOne(self, timeout: TimeSpan, exitContext: bool) -> bool:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class ProcessWindowStyle(Enum):
    """"""

    Normal: ProcessWindowStyle = ...
    """"""
    Hidden: ProcessWindowStyle = ...
    """"""
    Minimized: ProcessWindowStyle = ...
    """"""
    Maximized: ProcessWindowStyle = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SharedListenerElementsCollection(ListenerElementsCollection, ICollection, IEnumerable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CollectionType(self) -> ConfigurationElementCollectionType:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def EmitClear(self) -> bool:
        """"""
    @EmitClear.setter
    def EmitClear(self, value: bool) -> None: ...
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> ListenerElement:
        """"""
    @property
    def LockAllAttributesExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAllElementsExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAttributes(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockElements(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockItem(self) -> bool:
        """"""
    @LockItem.setter
    def LockItem(self, value: bool) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[ConfigurationElement], index: int) -> None:
        """"""
    def Equals(self, compareTo: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetRuntimeObject(self) -> TraceListenerCollection:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, name: str) -> ListenerElement:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SharedPerformanceCounter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SharedUtils(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ShellExecuteHelper(Object):
    """"""
    def __init__(self, executeInfo: NativeMethods.ShellExecuteInfo) -> None:
        """"""
    @property
    def ErrorCode(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ShellExecuteFunction(self) -> None:
        """"""
    def ShellExecuteOnSTAThread(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SourceElement(ConfigurationElement):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Attributes(self) -> Hashtable:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def Listeners(self) -> ListenerElementsCollection:
        """"""
    @property
    def LockAllAttributesExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAllElementsExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAttributes(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockElements(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockItem(self) -> bool:
        """"""
    @LockItem.setter
    def LockItem(self, value: bool) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @property
    def SwitchName(self) -> str:
        """"""
    @property
    def SwitchType(self) -> str:
        """"""
    @property
    def SwitchValue(self) -> str:
        """"""
    def Equals(self, compareTo: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SourceElementsCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CollectionType(self) -> ConfigurationElementCollectionType:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def EmitClear(self) -> bool:
        """"""
    @EmitClear.setter
    def EmitClear(self, value: bool) -> None: ...
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> SourceElement:
        """"""
    @property
    def LockAllAttributesExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAllElementsExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAttributes(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockElements(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockItem(self) -> bool:
        """"""
    @LockItem.setter
    def LockItem(self, value: bool) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[ConfigurationElement], index: int) -> None:
        """"""
    def Equals(self, compareTo: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, name: str) -> SourceElement:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SourceFilter(TraceFilter):
    """"""
    def __init__(self, source: str) -> None:
        """"""
    @property
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ShouldTrace(
        self,
        cache: TraceEventCache,
        source: str,
        eventType: TraceEventType,
        id: int,
        formatOrMessage: str,
        args: Array[object],
        data1: object,
        data: Array[object],
    ) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class SourceLevels(Enum):
    """"""

    Off: SourceLevels = ...
    """"""
    Critical: SourceLevels = ...
    """"""
    Error: SourceLevels = ...
    """"""
    Warning: SourceLevels = ...
    """"""
    Information: SourceLevels = ...
    """"""
    Verbose: SourceLevels = ...
    """"""
    ActivityTracing: SourceLevels = ...
    """"""
    All: SourceLevels = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SourceSwitch(Switch):
    """"""
    @overload
    def __init__(self, name: str) -> None:
        """"""
    @overload
    def __init__(self, displayName: str, defaultSwitchValue: str) -> None:
        """"""
    @property
    def Attributes(self) -> StringDictionary:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def DisplayName(self) -> str:
        """"""
    @property
    def Level(self) -> SourceLevels:
        """"""
    @Level.setter
    def Level(self, value: SourceLevels) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ShouldTrace(self, eventType: TraceEventType) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StackFrame(Object):
    """"""

    OFFSET_UNKNOWN: ClassVar[int]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, fNeedFileInfo: bool) -> None:
        """"""
    @overload
    def __init__(self, skipFrames: int) -> None:
        """"""
    @overload
    def __init__(self, skipFrames: int, fNeedFileInfo: bool) -> None:
        """"""
    @overload
    def __init__(self, fileName: str, lineNumber: int) -> None:
        """"""
    @overload
    def __init__(self, fileName: str, lineNumber: int, colNumber: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetFileColumnNumber(self) -> int:
        """"""
    def GetFileLineNumber(self) -> int:
        """"""
    def GetFileName(self) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetILOffset(self) -> int:
        """"""
    def GetMethod(self) -> MethodBase:
        """"""
    def GetNativeOffset(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StackFrameExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetNativeIP(cls, stackFrame: StackFrame) -> IntPtr:
        """"""
    @classmethod
    def GetNativeImageBase(cls, stackFrame: StackFrame) -> IntPtr:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def HasILOffset(cls, stackFrame: StackFrame) -> bool:
        """"""
    @classmethod
    def HasMethod(cls, stackFrame: StackFrame) -> bool:
        """"""
    @classmethod
    def HasNativeImage(cls, stackFrame: StackFrame) -> bool:
        """"""
    @classmethod
    def HasSource(cls, stackFrame: StackFrame) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StackFrameHelper(Object, IDisposable):
    """"""
    def __init__(self, target: Thread) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetColumnNumber(self, i: int) -> int:
        """"""
    def GetFilename(self, i: int) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetILOffset(self, i: int) -> int:
        """"""
    def GetLineNumber(self, i: int) -> int:
        """"""
    def GetMethodBase(self, i: int) -> MethodBase:
        """"""
    def GetNumberOfFrames(self) -> int:
        """"""
    def GetOffset(self, i: int) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsLastFrameFromForeignExceptionStackTrace(self, i: int) -> bool:
        """"""
    def SetNumberOfFrames(self, i: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StackTrace(Object):
    """"""

    METHODS_TO_SKIP: ClassVar[int]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, fNeedFileInfo: bool) -> None:
        """"""
    @overload
    def __init__(self, skipFrames: int) -> None:
        """"""
    @overload
    def __init__(self, skipFrames: int, fNeedFileInfo: bool) -> None:
        """"""
    @overload
    def __init__(self, e: Exception) -> None:
        """"""
    @overload
    def __init__(self, e: Exception, fNeedFileInfo: bool) -> None:
        """"""
    @overload
    def __init__(self, e: Exception, skipFrames: int) -> None:
        """"""
    @overload
    def __init__(self, e: Exception, skipFrames: int, fNeedFileInfo: bool) -> None:
        """"""
    @overload
    def __init__(self, frame: StackFrame) -> None:
        """"""
    @overload
    def __init__(self, targetThread: Thread, needFileInfo: bool) -> None:
        """"""
    @property
    def FrameCount(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetFrame(self, index: int) -> StackFrame:
        """"""
    def GetFrames(self) -> Array[StackFrame]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StackTraceSymbols(Object, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetSourceLineInfo(
        self,
        assemblyPath: str,
        loadedPeAddress: IntPtr,
        loadedPeSize: int,
        inMemoryPdbAddress: IntPtr,
        inMemoryPdbSize: int,
        methodToken: int,
        ilOffset: int,
        sourceFile: String,
        sourceLine: Int32,
        sourceColumn: Int32,
    ) -> tuple[None, String, Int32, Int32]:
        """"""
    def GetSourceLineInfoWithoutCasAssert(
        self,
        assemblyPath: str,
        loadedPeAddress: IntPtr,
        loadedPeSize: int,
        inMemoryPdbAddress: IntPtr,
        inMemoryPdbSize: int,
        methodToken: int,
        ilOffset: int,
        sourceFile: String,
        sourceLine: Int32,
        sourceColumn: Int32,
    ) -> tuple[None, String, Int32, Int32]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Stopwatch(Object):
    """"""

    Frequency: ClassVar[int]
    """"""
    IsHighResolution: ClassVar[bool]
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Elapsed(self) -> TimeSpan:
        """"""
    @property
    def ElapsedMilliseconds(self) -> int:
        """"""
    @property
    def ElapsedTicks(self) -> int:
        """"""
    @property
    def IsRunning(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetTimestamp(cls) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Reset(self) -> None:
        """"""
    def Restart(self) -> None:
        """"""
    def Start(self) -> None:
        """"""
    @classmethod
    def StartNew(cls) -> Stopwatch:
        """"""
    def Stop(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Switch(ABC, Object):
    """"""
    @property
    def Attributes(self) -> StringDictionary:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def DisplayName(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SwitchAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, switchName: str, switchType: Type) -> None:
        """"""
    @property
    def SwitchDescription(self) -> str:
        """"""
    @SwitchDescription.setter
    def SwitchDescription(self, value: str) -> None: ...
    @property
    def SwitchName(self) -> str:
        """"""
    @SwitchName.setter
    def SwitchName(self, value: str) -> None: ...
    @property
    def SwitchType(self) -> Type:
        """"""
    @SwitchType.setter
    def SwitchType(self, value: Type) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetAll(cls, assembly: Assembly) -> Array[SwitchAttribute]:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SwitchElement(ConfigurationElement):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Attributes(self) -> Hashtable:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def LockAllAttributesExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAllElementsExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAttributes(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockElements(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockItem(self) -> bool:
        """"""
    @LockItem.setter
    def LockItem(self, value: bool) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @property
    def Value(self) -> str:
        """"""
    def Equals(self, compareTo: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SwitchElementsCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CollectionType(self) -> ConfigurationElementCollectionType:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def EmitClear(self) -> bool:
        """"""
    @EmitClear.setter
    def EmitClear(self, value: bool) -> None: ...
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> SwitchElement:
        """"""
    @property
    def LockAllAttributesExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAllElementsExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAttributes(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockElements(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockItem(self) -> bool:
        """"""
    @LockItem.setter
    def LockItem(self, value: bool) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[ConfigurationElement], index: int) -> None:
        """"""
    def Equals(self, compareTo: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, name: str) -> SwitchElement:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SwitchLevelAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, switchLevelType: Type) -> None:
        """"""
    @property
    def SwitchLevelType(self) -> Type:
        """"""
    @SwitchLevelType.setter
    def SwitchLevelType(self, value: Type) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SwitchesDictionarySectionHandler(DictionarySectionHandler, IConfigurationSectionHandler):
    """"""
    def __init__(self) -> None:
        """"""
    def Create(self, parent: object, context: object, section: XmlNode) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SystemDiagnosticsSection(ConfigurationSection):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Assert(self) -> AssertSection:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def LockAllAttributesExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAllElementsExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAttributes(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockElements(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockItem(self) -> bool:
        """"""
    @LockItem.setter
    def LockItem(self, value: bool) -> None: ...
    @property
    def PerfCounters(self) -> PerfCounterSection:
        """"""
    @property
    def SectionInformation(self) -> SectionInformation:
        """"""
    @property
    def SharedListeners(self) -> ListenerElementsCollection:
        """"""
    @property
    def Sources(self) -> SourceElementsCollection:
        """"""
    @property
    def Switches(self) -> SwitchElementsCollection:
        """"""
    @property
    def Trace(self) -> TraceSection:
        """"""
    def Equals(self, compareTo: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TextWriterTraceListener(TraceListener, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, stream: Stream) -> None:
        """"""
    @overload
    def __init__(self, stream: Stream, name: str) -> None:
        """"""
    @overload
    def __init__(self, writer: TextWriter) -> None:
        """"""
    @overload
    def __init__(self, writer: TextWriter, name: str) -> None:
        """"""
    @overload
    def __init__(self, fileName: str) -> None:
        """"""
    @overload
    def __init__(self, fileName: str, name: str) -> None:
        """"""
    @property
    def Attributes(self) -> StringDictionary:
        """"""
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
    @property
    def Writer(self) -> TextWriter:
        """"""
    @Writer.setter
    def Writer(self, value: TextWriter) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ThreadInfo(Object):
    """"""

    basePriority: Final[int]
    """"""
    currentPriority: Final[int]
    """"""
    processId: Final[int]
    """"""
    startAddress: Final[IntPtr]
    """"""
    threadId: Final[int]
    """"""
    threadState: Final[ThreadState]
    """"""
    threadWaitReason: Final[ThreadWaitReason]
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class ThreadPriorityLevel(Enum):
    """"""

    Normal: ThreadPriorityLevel = ...
    """"""
    AboveNormal: ThreadPriorityLevel = ...
    """"""
    Highest: ThreadPriorityLevel = ...
    """"""
    TimeCritical: ThreadPriorityLevel = ...
    """"""
    Idle: ThreadPriorityLevel = ...
    """"""
    Lowest: ThreadPriorityLevel = ...
    """"""
    BelowNormal: ThreadPriorityLevel = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class ThreadState(Enum):
    """"""

    Initialized: ThreadState = ...
    """"""
    Ready: ThreadState = ...
    """"""
    Running: ThreadState = ...
    """"""
    Standby: ThreadState = ...
    """"""
    Terminated: ThreadState = ...
    """"""
    Wait: ThreadState = ...
    """"""
    Transition: ThreadState = ...
    """"""
    Unknown: ThreadState = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class ThreadWaitReason(Enum):
    """"""

    Executive: ThreadWaitReason = ...
    """"""
    FreePage: ThreadWaitReason = ...
    """"""
    PageIn: ThreadWaitReason = ...
    """"""
    SystemAllocation: ThreadWaitReason = ...
    """"""
    ExecutionDelay: ThreadWaitReason = ...
    """"""
    Suspended: ThreadWaitReason = ...
    """"""
    UserRequest: ThreadWaitReason = ...
    """"""
    EventPairHigh: ThreadWaitReason = ...
    """"""
    EventPairLow: ThreadWaitReason = ...
    """"""
    LpcReceive: ThreadWaitReason = ...
    """"""
    LpcReply: ThreadWaitReason = ...
    """"""
    VirtualMemory: ThreadWaitReason = ...
    """"""
    PageOut: ThreadWaitReason = ...
    """"""
    Unknown: ThreadWaitReason = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Trace(Object):
    """"""
    @classmethod
    @property
    def AutoFlush(cls) -> bool:
        """"""
    @classmethod
    @AutoFlush.setter
    def AutoFlush(cls, value: bool) -> None: ...
    @classmethod
    @property
    def CorrelationManager(cls) -> CorrelationManager:
        """"""
    @classmethod
    @property
    def IndentLevel(cls) -> int:
        """"""
    @classmethod
    @IndentLevel.setter
    def IndentLevel(cls, value: int) -> None: ...
    @classmethod
    @property
    def IndentSize(cls) -> int:
        """"""
    @classmethod
    @IndentSize.setter
    def IndentSize(cls, value: int) -> None: ...
    @classmethod
    @property
    def Listeners(cls) -> TraceListenerCollection:
        """"""
    @classmethod
    @property
    def UseGlobalLock(cls) -> bool:
        """"""
    @classmethod
    @UseGlobalLock.setter
    def UseGlobalLock(cls, value: bool) -> None: ...
    @classmethod
    @overload
    def Assert(cls, condition: bool) -> None:
        """"""
    @classmethod
    @overload
    def Assert(cls, condition: bool, message: str) -> None:
        """"""
    @classmethod
    @overload
    def Assert(cls, condition: bool, message: str, detailMessage: str) -> None:
        """"""
    @classmethod
    def Close(cls) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def Fail(cls, message: str) -> None:
        """"""
    @classmethod
    @overload
    def Fail(cls, message: str, detailMessage: str) -> None:
        """"""
    @classmethod
    def Flush(cls) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Indent(cls) -> None:
        """"""
    @classmethod
    def Refresh(cls) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def TraceError(cls, message: str) -> None:
        """"""
    @classmethod
    @overload
    def TraceError(cls, format: str, args: Array[object]) -> None:
        """"""
    @classmethod
    @overload
    def TraceInformation(cls, message: str) -> None:
        """"""
    @classmethod
    @overload
    def TraceInformation(cls, format: str, args: Array[object]) -> None:
        """"""
    @classmethod
    @overload
    def TraceWarning(cls, message: str) -> None:
        """"""
    @classmethod
    @overload
    def TraceWarning(cls, format: str, args: Array[object]) -> None:
        """"""
    @classmethod
    def Unindent(cls) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, value: object) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, value: object, category: str) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, message: str) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, message: str, category: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteIf(cls, condition: bool, value: object) -> None:
        """"""
    @classmethod
    @overload
    def WriteIf(cls, condition: bool, value: object, category: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteIf(cls, condition: bool, message: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteIf(cls, condition: bool, message: str, category: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, value: object) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, value: object, category: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, message: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, message: str, category: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteLineIf(cls, condition: bool, value: object) -> None:
        """"""
    @classmethod
    @overload
    def WriteLineIf(cls, condition: bool, value: object, category: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteLineIf(cls, condition: bool, message: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteLineIf(cls, condition: bool, message: str, category: str) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TraceEventCache(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Callstack(self) -> str:
        """"""
    @property
    def DateTime(self) -> DateTime:
        """"""
    @property
    def LogicalOperationStack(self) -> Stack:
        """"""
    @property
    def ProcessId(self) -> int:
        """"""
    @property
    def ThreadId(self) -> str:
        """"""
    @property
    def Timestamp(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class TraceEventType(Enum):
    """"""

    Critical: TraceEventType = ...
    """"""
    Error: TraceEventType = ...
    """"""
    Warning: TraceEventType = ...
    """"""
    Information: TraceEventType = ...
    """"""
    Verbose: TraceEventType = ...
    """"""
    Start: TraceEventType = ...
    """"""
    Stop: TraceEventType = ...
    """"""
    Suspend: TraceEventType = ...
    """"""
    Resume: TraceEventType = ...
    """"""
    Transfer: TraceEventType = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TraceFilter(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ShouldTrace(
        self,
        cache: TraceEventCache,
        source: str,
        eventType: TraceEventType,
        id: int,
        formatOrMessage: str,
        args: Array[object],
        data1: object,
        data: Array[object],
    ) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TraceInternal(ABC, Object):
    """"""
    @classmethod
    @property
    def AutoFlush(cls) -> bool:
        """"""
    @classmethod
    @AutoFlush.setter
    def AutoFlush(cls, value: bool) -> None: ...
    @classmethod
    @property
    def IndentLevel(cls) -> int:
        """"""
    @classmethod
    @IndentLevel.setter
    def IndentLevel(cls, value: int) -> None: ...
    @classmethod
    @property
    def IndentSize(cls) -> int:
        """"""
    @classmethod
    @IndentSize.setter
    def IndentSize(cls, value: int) -> None: ...
    @classmethod
    @property
    def Listeners(cls) -> TraceListenerCollection:
        """"""
    @classmethod
    @property
    def UseGlobalLock(cls) -> bool:
        """"""
    @classmethod
    @UseGlobalLock.setter
    def UseGlobalLock(cls, value: bool) -> None: ...
    @classmethod
    @overload
    def Assert(cls, condition: bool) -> None:
        """"""
    @classmethod
    @overload
    def Assert(cls, condition: bool, message: str) -> None:
        """"""
    @classmethod
    @overload
    def Assert(cls, condition: bool, message: str, detailMessage: str) -> None:
        """"""
    @classmethod
    def Close(cls) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def Fail(cls, message: str) -> None:
        """"""
    @classmethod
    @overload
    def Fail(cls, message: str, detailMessage: str) -> None:
        """"""
    @classmethod
    def Flush(cls) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Indent(cls) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def TraceEvent(
        cls, eventType: TraceEventType, id: int, format: str, args: Array[object]
    ) -> None:
        """"""
    @classmethod
    def Unindent(cls) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, value: object) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, value: object, category: str) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, message: str) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, message: str, category: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteIf(cls, condition: bool, value: object) -> None:
        """"""
    @classmethod
    @overload
    def WriteIf(cls, condition: bool, value: object, category: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteIf(cls, condition: bool, message: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteIf(cls, condition: bool, message: str, category: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, value: object) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, value: object, category: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, message: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, message: str, category: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteLineIf(cls, condition: bool, value: object) -> None:
        """"""
    @classmethod
    @overload
    def WriteLineIf(cls, condition: bool, value: object, category: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteLineIf(cls, condition: bool, message: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteLineIf(cls, condition: bool, message: str, category: str) -> None:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class TraceLevel(Enum):
    """"""

    Off: TraceLevel = ...
    """"""
    Error: TraceLevel = ...
    """"""
    Warning: TraceLevel = ...
    """"""
    Info: TraceLevel = ...
    """"""
    Verbose: TraceLevel = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TraceListener(ABC, MarshalByRefObject, IDisposable):
    """"""
    @property
    def Attributes(self) -> StringDictionary:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TraceListenerCollection(Object, ICollection, IEnumerable, IList):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> TraceListener:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, listener: TraceListener) -> int:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    @overload
    def AddRange(self, value: TraceListenerCollection) -> None:
        """"""
    @overload
    def AddRange(self, value: Array[TraceListener]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, listener: TraceListener) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, listeners: Array[TraceListener], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, listener: TraceListener) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, listener: TraceListener) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, listener: TraceListener) -> None:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    @overload
    def Remove(self, name: str) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, listener: TraceListener) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, listener: TraceListener) -> None:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    @overload
    def __delitem__(self, name: str) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, i: int) -> TraceListener:
        """"""
    @overload
    def __getitem__(self, name: str) -> TraceListener:
        """"""
    @overload
    def __setitem__(self, i: int, value: TraceListener) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class TraceLogRetentionOption(Enum):
    """"""

    UnlimitedSequentialFiles: TraceLogRetentionOption = ...
    """"""
    LimitedCircularFiles: TraceLogRetentionOption = ...
    """"""
    SingleFileUnboundedSize: TraceLogRetentionOption = ...
    """"""
    LimitedSequentialFiles: TraceLogRetentionOption = ...
    """"""
    SingleFileBoundedSize: TraceLogRetentionOption = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class TraceOptions(Enum):
    """"""

    _None: TraceOptions = ...
    """"""
    LogicalOperationStack: TraceOptions = ...
    """"""
    DateTime: TraceOptions = ...
    """"""
    Timestamp: TraceOptions = ...
    """"""
    ProcessId: TraceOptions = ...
    """"""
    ThreadId: TraceOptions = ...
    """"""
    Callstack: TraceOptions = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TraceSection(ConfigurationElement):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AutoFlush(self) -> bool:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def IndentSize(self) -> int:
        """"""
    @property
    def Listeners(self) -> ListenerElementsCollection:
        """"""
    @property
    def LockAllAttributesExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAllElementsExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAttributes(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockElements(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockItem(self) -> bool:
        """"""
    @LockItem.setter
    def LockItem(self, value: bool) -> None: ...
    @property
    def UseGlobalLock(self) -> bool:
        """"""
    def Equals(self, compareTo: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TraceSource(Object):
    """"""
    @overload
    def __init__(self, name: str) -> None:
        """"""
    @overload
    def __init__(self, name: str, defaultLevel: SourceLevels) -> None:
        """"""
    @property
    def Attributes(self) -> StringDictionary:
        """"""
    @property
    def Listeners(self) -> TraceListenerCollection:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Switch(self) -> SourceSwitch:
        """"""
    @Switch.setter
    def Switch(self, value: SourceSwitch) -> None: ...
    def Close(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def TraceData(self, eventType: TraceEventType, id: int, data: Array[object]) -> None:
        """"""
    @overload
    def TraceData(self, eventType: TraceEventType, id: int, data: object) -> None:
        """"""
    @overload
    def TraceEvent(self, eventType: TraceEventType, id: int) -> None:
        """"""
    @overload
    def TraceEvent(self, eventType: TraceEventType, id: int, message: str) -> None:
        """"""
    @overload
    def TraceEvent(
        self, eventType: TraceEventType, id: int, format: str, args: Array[object]
    ) -> None:
        """"""
    @overload
    def TraceInformation(self, message: str) -> None:
        """"""
    @overload
    def TraceInformation(self, format: str, args: Array[object]) -> None:
        """"""
    def TraceTransfer(self, id: int, message: str, relatedActivityId: Guid) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TraceSwitch(Switch):
    """"""
    @overload
    def __init__(self, displayName: str, description: str) -> None:
        """"""
    @overload
    def __init__(self, displayName: str, description: str, defaultSwitchValue: str) -> None:
        """"""
    @property
    def Attributes(self) -> StringDictionary:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def DisplayName(self) -> str:
        """"""
    @property
    def Level(self) -> TraceLevel:
        """"""
    @Level.setter
    def Level(self, value: TraceLevel) -> None: ...
    @property
    def TraceError(self) -> bool:
        """"""
    @property
    def TraceInfo(self) -> bool:
        """"""
    @property
    def TraceVerbose(self) -> bool:
        """"""
    @property
    def TraceWarning(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TraceUtils(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TypedElement(ConfigurationElement):
    """"""
    def __init__(self, baseType: Type) -> None:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def InitData(self) -> str:
        """"""
    @InitData.setter
    def InitData(self, value: str) -> None: ...
    @property
    def LockAllAttributesExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAllElementsExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAttributes(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockElements(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockItem(self) -> bool:
        """"""
    @LockItem.setter
    def LockItem(self, value: bool) -> None: ...
    @property
    def TypeName(self) -> str:
        """"""
    @TypeName.setter
    def TypeName(self, value: str) -> None: ...
    def Equals(self, compareTo: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class UnescapedXmlDiagnosticData(Object):
    """"""
    def __init__(self, xmlPayload: str) -> None:
        """"""
    @property
    def UnescapedXml(self) -> str:
        """"""
    @UnescapedXml.setter
    def UnescapedXml(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type UserCallBack = Callable[[str], None]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class WinProcessManager(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetModuleInfos(cls, processId: int) -> Array[ModuleInfo]:
        """"""
    @classmethod
    def GetProcessIds(cls) -> Array[int]:
        """"""
    @classmethod
    def GetProcessInfos(cls) -> Array[ProcessInfo]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class XmlWriterTraceListener(TextWriterTraceListener, IDisposable):
    """"""
    @overload
    def __init__(self, stream: Stream) -> None:
        """"""
    @overload
    def __init__(self, stream: Stream, name: str) -> None:
        """"""
    @overload
    def __init__(self, writer: TextWriter) -> None:
        """"""
    @overload
    def __init__(self, writer: TextWriter, name: str) -> None:
        """"""
    @overload
    def __init__(self, filename: str) -> None:
        """"""
    @overload
    def __init__(self, filename: str, name: str) -> None:
        """"""
    @property
    def Attributes(self) -> StringDictionary:
        """"""
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
    @property
    def Writer(self) -> TextWriter:
        """"""
    @Writer.setter
    def Writer(self, value: TextWriter) -> None: ...
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
