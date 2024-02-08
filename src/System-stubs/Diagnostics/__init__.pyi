from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Iterator
from typing import Tuple
from typing import TypeVar
from typing import overload

from Microsoft.Win32.NativeMethods import ShellExecuteInfo
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
from System import IntPtr
from System import MarshalByRefObject
from System import Object
from System import Predicate
from System import TimeSpan
from System import Type
from System import ValueType
from System.Collections import ArrayList
from System.Collections import CollectionBase
from System.Collections import DictionaryBase
from System.Collections import Hashtable
from System.Collections import ICollection
from System.Collections import IComparer
from System.Collections import IDictionary
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
from System.ComponentModel.TypeConverter import StandardValuesCollection
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
from System.Diagnostics.DebuggableAttribute import DebuggingModes
from System.Diagnostics.StackTrace import TraceFormat
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

T = TypeVar("T")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class AlphabeticalEnumConverter(EnumConverter):
    """"""

    def __init__(self, type: Type):
        """

        :param type:
        """
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class Assert(ABC, Object):
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
        """

        :param condition:
        :param message:
        :param location:
        :param stackTraceFormat:
        :param windowTitle:
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

class AssertSection(ConfigurationElement):
    """"""

    def __init__(self):
        """"""
    @property
    def AssertUIEnabled(self) -> bool:
        """

        :return:
        """
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
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class AssertWrapper(ABC, Object):
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
    @classmethod
    def ShowAssert(
        cls, stackTrace: str, frame: StackFrame, message: str, detailMessage: str
    ) -> None:
        """

        :param stackTrace:
        :param frame:
        :param message:
        :param detailMessage:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class AsyncStreamReader(Object, IDisposable):
    """"""

    @property
    def BaseStream(self) -> Stream:
        """

        :return:
        """
    @property
    def CurrentEncoding(self) -> Encoding:
        """

        :return:
        """
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class BooleanSwitch(Switch):
    """"""

    @overload
    def __init__(self, displayName: str, description: str):
        """

        :param displayName:
        :param description:
        """
    @overload
    def __init__(self, displayName: str, description: str, defaultSwitchValue: str):
        """

        :param displayName:
        :param description:
        :param defaultSwitchValue:
        """
    @property
    def Attributes(self) -> StringDictionary:
        """

        :return:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @property
    def DisplayName(self) -> str:
        """

        :return:
        """
    @property
    def Enabled(self) -> bool:
        """

        :return:
        """
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
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

class CategoryEntry(Object):
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

class CategorySample(Object):
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

class ConditionalAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, conditionString: str):
        """

        :param conditionString:
        """
    @property
    def ConditionString(self) -> str:
        """

        :return:
        """
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

class ConsoleTraceListener(TextWriterTraceListener, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, useErrorStream: bool):
        """

        :param useErrorStream:
        """
    @property
    def Attributes(self) -> StringDictionary:
        """

        :return:
        """
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
    @property
    def Writer(self) -> TextWriter:
        """

        :return:
        """
    @Writer.setter
    def Writer(self, value: TextWriter) -> None: ...
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

class CorrelationManager(Object):
    """"""

    @property
    def ActivityId(self) -> Guid:
        """

        :return:
        """
    @ActivityId.setter
    def ActivityId(self, value: Guid) -> None: ...
    @property
    def LogicalOperationStack(self) -> Stack:
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
    @overload
    def StartLogicalOperation(self) -> None:
        """"""
    @overload
    def StartLogicalOperation(self, operationId: object) -> None:
        """

        :param operationId:
        """
    def StopLogicalOperation(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class CounterCreationData(Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, counterName: str, counterHelp: str, counterType: PerformanceCounterType):
        """

        :param counterName:
        :param counterHelp:
        :param counterType:
        """
    @property
    def CounterHelp(self) -> str:
        """

        :return:
        """
    @CounterHelp.setter
    def CounterHelp(self, value: str) -> None: ...
    @property
    def CounterName(self) -> str:
        """

        :return:
        """
    @CounterName.setter
    def CounterName(self, value: str) -> None: ...
    @property
    def CounterType(self) -> PerformanceCounterType:
        """

        :return:
        """
    @CounterType.setter
    def CounterType(self, value: PerformanceCounterType) -> None: ...
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

class CounterCreationDataCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: CounterCreationDataCollection):
        """

        :param value:
        """
    @overload
    def __init__(self, value: Array[CounterCreationData]):
        """

        :param value:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
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
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, value: CounterCreationData) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def AddRange(self, value: CounterCreationDataCollection) -> None:
        """

        :param value:
        """
    @overload
    def AddRange(self, value: Array[CounterCreationData]) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CounterCreationData) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[CounterCreationData], index: int) -> None:
        """

        :param array:
        :param index:
        """
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
    def IndexOf(self, value: CounterCreationData) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: CounterCreationData) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, value: CounterCreationData) -> None:
        """

        :param value:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: CounterCreationData) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class CounterDefinitionSample(Object):
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

class CounterSample(ValueType):
    """"""

    Empty: Final[ClassVar[CounterSample]] = ...
    """
    
    :return: 
    """
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
    ):
        """

        :param rawValue:
        :param baseValue:
        :param counterFrequency:
        :param systemFrequency:
        :param timeStamp:
        :param timeStamp100nSec:
        :param counterType:
        """
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
    ):
        """

        :param rawValue:
        :param baseValue:
        :param counterFrequency:
        :param systemFrequency:
        :param timeStamp:
        :param timeStamp100nSec:
        :param counterType:
        :param counterTimeStamp:
        """
    @property
    def BaseValue(self) -> int:
        """

        :return:
        """
    @property
    def CounterFrequency(self) -> int:
        """

        :return:
        """
    @property
    def CounterTimeStamp(self) -> int:
        """

        :return:
        """
    @property
    def CounterType(self) -> PerformanceCounterType:
        """

        :return:
        """
    @property
    def RawValue(self) -> int:
        """

        :return:
        """
    @property
    def SystemFrequency(self) -> int:
        """

        :return:
        """
    @property
    def TimeStamp(self) -> int:
        """

        :return:
        """
    @property
    def TimeStamp100nSec(self) -> int:
        """

        :return:
        """
    @classmethod
    @overload
    def Calculate(cls, counterSample: CounterSample) -> float:
        """

        :param counterSample:
        :return:
        """
    @classmethod
    @overload
    def Calculate(cls, counterSample: CounterSample, nextCounterSample: CounterSample) -> float:
        """

        :param counterSample:
        :param nextCounterSample:
        :return:
        """
    @overload
    def Equals(self, sample: CounterSample) -> bool:
        """

        :param sample:
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
    def __eq__(self, other: CounterSample) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: CounterSample) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, a: CounterSample, b: CounterSample) -> bool:
        """

        :param a:
        :param b:
        :return:
        """
    @classmethod
    def op_Inequality(cls, a: CounterSample, b: CounterSample) -> bool:
        """

        :param a:
        :param b:
        :return:
        """

class CounterSampleCalculator(ABC, Object):
    """"""

    @classmethod
    @overload
    def ComputeCounterValue(cls, newSample: CounterSample) -> float:
        """

        :param newSample:
        :return:
        """
    @classmethod
    @overload
    def ComputeCounterValue(cls, oldSample: CounterSample, newSample: CounterSample) -> float:
        """

        :param oldSample:
        :param newSample:
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

class DataReceivedEventArgs(EventArgs):
    """"""

    @property
    def Data(self) -> str:
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

DataReceivedEventHandler: Callable[[object, DataReceivedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class Debug(ABC, Object):
    """"""

    @classmethod
    @property
    def AutoFlush(cls) -> bool:
        """

        :return:
        """
    @classmethod
    @AutoFlush.setter
    def AutoFlush(cls, value: bool) -> None: ...
    @classmethod
    @property
    def IndentLevel(cls) -> int:
        """

        :return:
        """
    @classmethod
    @IndentLevel.setter
    def IndentLevel(cls, value: int) -> None: ...
    @classmethod
    @property
    def IndentSize(cls) -> int:
        """

        :return:
        """
    @classmethod
    @IndentSize.setter
    def IndentSize(cls, value: int) -> None: ...
    @classmethod
    @property
    def Listeners(cls) -> TraceListenerCollection:
        """

        :return:
        """
    @classmethod
    @overload
    def Assert(cls, condition: bool) -> None:
        """

        :param condition:
        """
    @classmethod
    @overload
    def Assert(cls, condition: bool, message: str) -> None:
        """

        :param condition:
        :param message:
        """
    @classmethod
    @overload
    def Assert(cls, condition: bool, message: str, detailMessage: str) -> None:
        """

        :param condition:
        :param message:
        :param detailMessage:
        """
    @classmethod
    @overload
    def Assert(
        cls, condition: bool, message: str, detailMessageFormat: str, args: Array[object]
    ) -> None:
        """

        :param condition:
        :param message:
        :param detailMessageFormat:
        :param args:
        """
    @classmethod
    def Close(cls) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def Fail(cls, message: str) -> None:
        """

        :param message:
        """
    @classmethod
    @overload
    def Fail(cls, message: str, detailMessage: str) -> None:
        """

        :param message:
        :param detailMessage:
        """
    @classmethod
    def Flush(cls) -> None:
        """"""
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def Indent(cls) -> None:
        """"""
    @classmethod
    @overload
    def Print(cls, message: str) -> None:
        """

        :param message:
        """
    @classmethod
    @overload
    def Print(cls, format: str, args: Array[object]) -> None:
        """

        :param format:
        :param args:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def Unindent(cls) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, value: object) -> None:
        """

        :param value:
        """
    @classmethod
    @overload
    def Write(cls, message: str) -> None:
        """

        :param message:
        """
    @classmethod
    @overload
    def Write(cls, value: object, category: str) -> None:
        """

        :param value:
        :param category:
        """
    @classmethod
    @overload
    def Write(cls, message: str, category: str) -> None:
        """

        :param message:
        :param category:
        """
    @classmethod
    @overload
    def WriteIf(cls, condition: bool, value: object) -> None:
        """

        :param condition:
        :param value:
        """
    @classmethod
    @overload
    def WriteIf(cls, condition: bool, message: str) -> None:
        """

        :param condition:
        :param message:
        """
    @classmethod
    @overload
    def WriteIf(cls, condition: bool, value: object, category: str) -> None:
        """

        :param condition:
        :param value:
        :param category:
        """
    @classmethod
    @overload
    def WriteIf(cls, condition: bool, message: str, category: str) -> None:
        """

        :param condition:
        :param message:
        :param category:
        """
    @classmethod
    @overload
    def WriteLine(cls, value: object) -> None:
        """

        :param value:
        """
    @classmethod
    @overload
    def WriteLine(cls, message: str) -> None:
        """

        :param message:
        """
    @classmethod
    @overload
    def WriteLine(cls, value: object, category: str) -> None:
        """

        :param value:
        :param category:
        """
    @classmethod
    @overload
    def WriteLine(cls, format: str, args: Array[object]) -> None:
        """

        :param format:
        :param args:
        """
    @classmethod
    @overload
    def WriteLine(cls, message: str, category: str) -> None:
        """

        :param message:
        :param category:
        """
    @classmethod
    @overload
    def WriteLineIf(cls, condition: bool, value: object) -> None:
        """

        :param condition:
        :param value:
        """
    @classmethod
    @overload
    def WriteLineIf(cls, condition: bool, message: str) -> None:
        """

        :param condition:
        :param message:
        """
    @classmethod
    @overload
    def WriteLineIf(cls, condition: bool, value: object, category: str) -> None:
        """

        :param condition:
        :param value:
        :param category:
        """
    @classmethod
    @overload
    def WriteLineIf(cls, condition: bool, message: str, category: str) -> None:
        """

        :param condition:
        :param message:
        :param category:
        """

class DebuggableAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, modes: DebuggableAttribute.DebuggingModes):
        """

        :param modes:
        """
    @overload
    def __init__(self, isJITTrackingEnabled: bool, isJITOptimizerDisabled: bool):
        """

        :param isJITTrackingEnabled:
        :param isJITOptimizerDisabled:
        """
    @property
    def DebuggingFlags(self) -> DebuggableAttribute.DebuggingModes:
        """

        :return:
        """
    @property
    def IsJITOptimizerDisabled(self) -> bool:
        """

        :return:
        """
    @property
    def IsJITTrackingEnabled(self) -> bool:
        """

        :return:
        """
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

    class DebuggingModes(Enum):
        """"""

        _None: DebuggingModes = ...
        """"""
        Default: DebuggingModes = ...
        """"""
        IgnoreSymbolStoreSequencePoints: DebuggingModes = ...
        """"""
        EnableEditAndContinue: DebuggingModes = ...
        """"""
        DisableOptimizations: DebuggingModes = ...
        """"""

class Debugger(Object):
    """"""

    DefaultCategory: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @classmethod
    @property
    def IsAttached(cls) -> bool:
        """

        :return:
        """
    @classmethod
    def Break(cls) -> None:
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
    @classmethod
    def IsLogging(cls) -> bool:
        """

        :return:
        """
    @classmethod
    def Launch(cls) -> bool:
        """

        :return:
        """
    @classmethod
    def Log(cls, level: int, category: str, message: str) -> None:
        """

        :param level:
        :param category:
        :param message:
        """
    @classmethod
    def NotifyOfCrossThreadDependency(cls) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class DebuggerBrowsableAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, state: DebuggerBrowsableState):
        """

        :param state:
        """
    @property
    def State(self) -> DebuggerBrowsableState:
        """

        :return:
        """
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

class DebuggerBrowsableState(Enum):
    """"""

    Never: DebuggerBrowsableState = ...
    """"""
    Collapsed: DebuggerBrowsableState = ...
    """"""
    RootHidden: DebuggerBrowsableState = ...
    """"""

class DebuggerDisplayAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, value: str):
        """

        :param value:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Target(self) -> Type:
        """

        :return:
        """
    @Target.setter
    def Target(self, value: Type) -> None: ...
    @property
    def TargetTypeName(self) -> str:
        """

        :return:
        """
    @TargetTypeName.setter
    def TargetTypeName(self, value: str) -> None: ...
    @property
    def Type(self) -> str:
        """

        :return:
        """
    @Type.setter
    def Type(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Value(self) -> str:
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

class DebuggerHiddenAttribute(Attribute, _Attribute):
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

class DebuggerNonUserCodeAttribute(Attribute, _Attribute):
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

class DebuggerStepThroughAttribute(Attribute, _Attribute):
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

class DebuggerStepperBoundaryAttribute(Attribute, _Attribute):
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

class DebuggerTypeProxyAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, typeName: str):
        """

        :param typeName:
        """
    @overload
    def __init__(self, type: Type):
        """

        :param type:
        """
    @property
    def ProxyTypeName(self) -> str:
        """

        :return:
        """
    @property
    def Target(self) -> Type:
        """

        :return:
        """
    @Target.setter
    def Target(self, value: Type) -> None: ...
    @property
    def TargetTypeName(self) -> str:
        """

        :return:
        """
    @TargetTypeName.setter
    def TargetTypeName(self, value: str) -> None: ...
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

class DebuggerVisualizerAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, visualizerTypeName: str):
        """

        :param visualizerTypeName:
        """
    @overload
    def __init__(self, visualizer: Type):
        """

        :param visualizer:
        """
    @overload
    def __init__(self, visualizerTypeName: str, visualizerObjectSourceTypeName: str):
        """

        :param visualizerTypeName:
        :param visualizerObjectSourceTypeName:
        """
    @overload
    def __init__(self, visualizerTypeName: str, visualizerObjectSource: Type):
        """

        :param visualizerTypeName:
        :param visualizerObjectSource:
        """
    @overload
    def __init__(self, visualizer: Type, visualizerObjectSourceTypeName: str):
        """

        :param visualizer:
        :param visualizerObjectSourceTypeName:
        """
    @overload
    def __init__(self, visualizer: Type, visualizerObjectSource: Type):
        """

        :param visualizer:
        :param visualizerObjectSource:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @Description.setter
    def Description(self, value: str) -> None: ...
    @property
    def Target(self) -> Type:
        """

        :return:
        """
    @Target.setter
    def Target(self, value: Type) -> None: ...
    @property
    def TargetTypeName(self) -> str:
        """

        :return:
        """
    @TargetTypeName.setter
    def TargetTypeName(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def VisualizerObjectSourceTypeName(self) -> str:
        """

        :return:
        """
    @property
    def VisualizerTypeName(self) -> str:
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
        """

        :param condition:
        :param message:
        :param location:
        :param stackTraceFormat:
        :param windowTitle:
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

class DefaultTraceListener(TraceListener, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def AssertUiEnabled(self) -> bool:
        """

        :return:
        """
    @AssertUiEnabled.setter
    def AssertUiEnabled(self, value: bool) -> None: ...
    @property
    def Attributes(self) -> StringDictionary:
        """

        :return:
        """
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
    def LogFileName(self) -> str:
        """

        :return:
        """
    @LogFileName.setter
    def LogFileName(self, value: str) -> None: ...
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

class DelimitedListTraceListener(TextWriterTraceListener, IDisposable):
    """"""

    @overload
    def __init__(self, stream: Stream):
        """

        :param stream:
        """
    @overload
    def __init__(self, writer: TextWriter):
        """

        :param writer:
        """
    @overload
    def __init__(self, fileName: str):
        """

        :param fileName:
        """
    @overload
    def __init__(self, stream: Stream, name: str):
        """

        :param stream:
        :param name:
        """
    @overload
    def __init__(self, writer: TextWriter, name: str):
        """

        :param writer:
        :param name:
        """
    @overload
    def __init__(self, fileName: str, name: str):
        """

        :param fileName:
        :param name:
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
    @property
    def Writer(self) -> TextWriter:
        """

        :return:
        """
    @Writer.setter
    def Writer(self, value: TextWriter) -> None: ...
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

class DiagnosticsConfiguration(ABC, Object):
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

class DiagnosticsConfigurationHandler(Object, IConfigurationSectionHandler):
    """"""

    def __init__(self):
        """"""
    def Create(self, parent: object, configContext: object, section: XmlNode) -> object:
        """

        :param parent:
        :param configContext:
        :param section:
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

class EditAndContinueHelper(Object):
    """"""

    def __init__(self):
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

class EntryWrittenEventArgs(EventArgs):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, entry: EventLogEntry):
        """

        :param entry:
        """
    @property
    def Entry(self) -> EventLogEntry:
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

EntryWrittenEventHandler: Callable[[object, EntryWrittenEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class EnvironmentBlock(ABC, Object):
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
    @classmethod
    def ToByteArray(cls, sd: StringDictionary, unicode: bool) -> Array[int]:
        """

        :param sd:
        :param unicode:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EventInstance(Object):
    """"""

    @overload
    def __init__(self, instanceId: int, categoryId: int):
        """

        :param instanceId:
        :param categoryId:
        """
    @overload
    def __init__(self, instanceId: int, categoryId: int, entryType: EventLogEntryType):
        """

        :param instanceId:
        :param categoryId:
        :param entryType:
        """
    @property
    def CategoryId(self) -> int:
        """

        :return:
        """
    @CategoryId.setter
    def CategoryId(self, value: int) -> None: ...
    @property
    def EntryType(self) -> EventLogEntryType:
        """

        :return:
        """
    @EntryType.setter
    def EntryType(self, value: EventLogEntryType) -> None: ...
    @property
    def InstanceId(self) -> int:
        """

        :return:
        """
    @InstanceId.setter
    def InstanceId(self, value: int) -> None: ...
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

class EventLog(Component, IComponent, ISupportInitialize, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, logName: str):
        """

        :param logName:
        """
    @overload
    def __init__(self, logName: str, machineName: str):
        """

        :param logName:
        :param machineName:
        """
    @overload
    def __init__(self, logName: str, machineName: str, source: str):
        """

        :param logName:
        :param machineName:
        :param source:
        """
    @property
    def Container(self) -> IContainer:
        """

        :return:
        """
    @property
    def EnableRaisingEvents(self) -> bool:
        """

        :return:
        """
    @EnableRaisingEvents.setter
    def EnableRaisingEvents(self, value: bool) -> None: ...
    @property
    def Entries(self) -> EventLogEntryCollection:
        """

        :return:
        """
    @property
    def Log(self) -> str:
        """

        :return:
        """
    @Log.setter
    def Log(self, value: str) -> None: ...
    @property
    def LogDisplayName(self) -> str:
        """

        :return:
        """
    @property
    def MachineName(self) -> str:
        """

        :return:
        """
    @MachineName.setter
    def MachineName(self, value: str) -> None: ...
    @property
    def MaximumKilobytes(self) -> int:
        """

        :return:
        """
    @MaximumKilobytes.setter
    def MaximumKilobytes(self, value: int) -> None: ...
    @property
    def MinimumRetentionDays(self) -> int:
        """

        :return:
        """
    @property
    def OverflowAction(self) -> OverflowAction:
        """

        :return:
        """
    @property
    def Site(self) -> ISite:
        """

        :return:
        """
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    @property
    def Source(self) -> str:
        """

        :return:
        """
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke:
        """

        :return:
        """
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
        """

        :param sourceData:
        """
    @classmethod
    @overload
    def CreateEventSource(cls, source: str, logName: str) -> None:
        """

        :param source:
        :param logName:
        """
    @classmethod
    @overload
    def CreateEventSource(cls, source: str, logName: str, machineName: str) -> None:
        """

        :param source:
        :param logName:
        :param machineName:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    @classmethod
    @overload
    def Delete(cls, logName: str) -> None:
        """

        :param logName:
        """
    @classmethod
    @overload
    def Delete(cls, logName: str, machineName: str) -> None:
        """

        :param logName:
        :param machineName:
        """
    @classmethod
    @overload
    def DeleteEventSource(cls, source: str) -> None:
        """

        :param source:
        """
    @classmethod
    @overload
    def DeleteEventSource(cls, source: str, machineName: str) -> None:
        """

        :param source:
        :param machineName:
        """
    def Dispose(self) -> None:
        """"""
    def EndInit(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def Exists(cls, logName: str) -> bool:
        """

        :param logName:
        :return:
        """
    @classmethod
    @overload
    def Exists(cls, logName: str, machineName: str) -> bool:
        """

        :param logName:
        :param machineName:
        :return:
        """
    @classmethod
    @overload
    def GetEventLogs(cls) -> Array[EventLog]:
        """

        :return:
        """
    @classmethod
    @overload
    def GetEventLogs(cls, machineName: str) -> Array[EventLog]:
        """

        :param machineName:
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
    @classmethod
    def LogNameFromSourceName(cls, source: str, machineName: str) -> str:
        """

        :param source:
        :param machineName:
        :return:
        """
    def ModifyOverflowPolicy(self, action: OverflowAction, retentionDays: int) -> None:
        """

        :param action:
        :param retentionDays:
        """
    def RegisterDisplayName(self, resourceFile: str, resourceId: int) -> None:
        """

        :param resourceFile:
        :param resourceId:
        """
    @classmethod
    @overload
    def SourceExists(cls, source: str) -> bool:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def SourceExists(cls, source: str, machineName: str) -> bool:
        """

        :param source:
        :param machineName:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def WriteEntry(self, message: str) -> None:
        """

        :param message:
        """
    @overload
    def WriteEntry(self, message: str, type: EventLogEntryType) -> None:
        """

        :param message:
        :param type:
        """
    @classmethod
    @overload
    def WriteEntry(cls, source: str, message: str) -> None:
        """

        :param source:
        :param message:
        """
    @overload
    def WriteEntry(self, message: str, type: EventLogEntryType, eventID: int) -> None:
        """

        :param message:
        :param type:
        :param eventID:
        """
    @classmethod
    @overload
    def WriteEntry(cls, source: str, message: str, type: EventLogEntryType) -> None:
        """

        :param source:
        :param message:
        :param type:
        """
    @overload
    def WriteEntry(
        self, message: str, type: EventLogEntryType, eventID: int, category: int
    ) -> None:
        """

        :param message:
        :param type:
        :param eventID:
        :param category:
        """
    @classmethod
    @overload
    def WriteEntry(cls, source: str, message: str, type: EventLogEntryType, eventID: int) -> None:
        """

        :param source:
        :param message:
        :param type:
        :param eventID:
        """
    @overload
    def WriteEntry(
        self,
        message: str,
        type: EventLogEntryType,
        eventID: int,
        category: int,
        rawData: Array[int],
    ) -> None:
        """

        :param message:
        :param type:
        :param eventID:
        :param category:
        :param rawData:
        """
    @classmethod
    @overload
    def WriteEntry(
        cls, source: str, message: str, type: EventLogEntryType, eventID: int, category: int
    ) -> None:
        """

        :param source:
        :param message:
        :param type:
        :param eventID:
        :param category:
        """
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
        """

        :param source:
        :param message:
        :param type:
        :param eventID:
        :param category:
        :param rawData:
        """
    @overload
    def WriteEvent(self, instance: EventInstance, values: Array[object]) -> None:
        """

        :param instance:
        :param values:
        """
    @overload
    def WriteEvent(self, instance: EventInstance, data: Array[int], values: Array[object]) -> None:
        """

        :param instance:
        :param data:
        :param values:
        """
    @classmethod
    @overload
    def WriteEvent(cls, source: str, instance: EventInstance, values: Array[object]) -> None:
        """

        :param source:
        :param instance:
        :param values:
        """
    @classmethod
    @overload
    def WriteEvent(
        cls, source: str, instance: EventInstance, data: Array[int], values: Array[object]
    ) -> None:
        """

        :param source:
        :param instance:
        :param data:
        :param values:
        """
    Disposed: EventType[EventHandler] = ...
    """"""
    EntryWritten: EventType[EntryWrittenEventHandler] = ...
    """"""

class EventLogEntry(Component, IComponent, ISerializable, IDisposable):
    """"""

    @property
    def Category(self) -> str:
        """

        :return:
        """
    @property
    def CategoryNumber(self) -> int:
        """

        :return:
        """
    @property
    def Container(self) -> IContainer:
        """

        :return:
        """
    @property
    def Data(self) -> Array[int]:
        """

        :return:
        """
    @property
    def EntryType(self) -> EventLogEntryType:
        """

        :return:
        """
    @property
    def EventID(self) -> int:
        """

        :return:
        """
    @property
    def Index(self) -> int:
        """

        :return:
        """
    @property
    def InstanceId(self) -> int:
        """

        :return:
        """
    @property
    def MachineName(self) -> str:
        """

        :return:
        """
    @property
    def Message(self) -> str:
        """

        :return:
        """
    @property
    def ReplacementStrings(self) -> Array[str]:
        """

        :return:
        """
    @property
    def Site(self) -> ISite:
        """

        :return:
        """
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    @property
    def Source(self) -> str:
        """

        :return:
        """
    @property
    def TimeGenerated(self) -> DateTime:
        """

        :return:
        """
    @property
    def TimeWritten(self) -> DateTime:
        """

        :return:
        """
    @property
    def UserName(self) -> str:
        """

        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    @overload
    def Equals(self, otherEntry: EventLogEntry) -> bool:
        """

        :param otherEntry:
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
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
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
    Disposed: EventType[EventHandler] = ...
    """"""

class EventLogEntryCollection(Object, ICollection, IEnumerable):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> EventLogEntry:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, entries: Array[EventLogEntry], index: int) -> None:
        """

        :param entries:
        :param index:
        """
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
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> EventLogEntry:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

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

class EventLogInternal(Object, ISupportInitialize, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, logName: str):
        """

        :param logName:
        """
    @overload
    def __init__(self, logName: str, machineName: str):
        """

        :param logName:
        :param machineName:
        """
    @overload
    def __init__(self, logName: str, machineName: str, source: str):
        """

        :param logName:
        :param machineName:
        :param source:
        """
    @overload
    def __init__(self, logName: str, machineName: str, source: str, parent: EventLog):
        """

        :param logName:
        :param machineName:
        :param source:
        :param parent:
        """
    @property
    def EnableRaisingEvents(self) -> bool:
        """

        :return:
        """
    @EnableRaisingEvents.setter
    def EnableRaisingEvents(self, value: bool) -> None: ...
    @property
    def Entries(self) -> EventLogEntryCollection:
        """

        :return:
        """
    @property
    def Log(self) -> str:
        """

        :return:
        """
    @property
    def LogDisplayName(self) -> str:
        """

        :return:
        """
    @property
    def MachineName(self) -> str:
        """

        :return:
        """
    @property
    def MaximumKilobytes(self) -> int:
        """

        :return:
        """
    @MaximumKilobytes.setter
    def MaximumKilobytes(self, value: int) -> None: ...
    @property
    def MinimumRetentionDays(self) -> int:
        """

        :return:
        """
    @property
    def OverflowAction(self) -> OverflowAction:
        """

        :return:
        """
    @property
    def Source(self) -> str:
        """

        :return:
        """
    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke:
        """

        :return:
        """
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
    def ModifyOverflowPolicy(self, action: OverflowAction, retentionDays: int) -> None:
        """

        :param action:
        :param retentionDays:
        """
    def RegisterDisplayName(self, resourceFile: str, resourceId: int) -> None:
        """

        :param resourceFile:
        :param resourceId:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def WriteEntry(self, message: str) -> None:
        """

        :param message:
        """
    @overload
    def WriteEntry(self, message: str, type: EventLogEntryType) -> None:
        """

        :param message:
        :param type:
        """
    @overload
    def WriteEntry(self, message: str, type: EventLogEntryType, eventID: int) -> None:
        """

        :param message:
        :param type:
        :param eventID:
        """
    @overload
    def WriteEntry(
        self, message: str, type: EventLogEntryType, eventID: int, category: int
    ) -> None:
        """

        :param message:
        :param type:
        :param eventID:
        :param category:
        """
    @overload
    def WriteEntry(
        self,
        message: str,
        type: EventLogEntryType,
        eventID: int,
        category: int,
        rawData: Array[int],
    ) -> None:
        """

        :param message:
        :param type:
        :param eventID:
        :param category:
        :param rawData:
        """
    @overload
    def WriteEvent(self, instance: EventInstance, values: Array[object]) -> None:
        """

        :param instance:
        :param values:
        """
    @overload
    def WriteEvent(self, instance: EventInstance, data: Array[int], values: Array[object]) -> None:
        """

        :param instance:
        :param data:
        :param values:
        """
    EntryWritten: EventType[EntryWrittenEventHandler] = ...
    """"""

class EventLogPermission(
    ResourcePermissionBase, IUnrestrictedPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    @overload
    def __init__(self, permissionAccessEntries: Array[EventLogPermissionEntry]):
        """

        :param permissionAccessEntries:
        """
    @overload
    def __init__(self, permissionAccess: EventLogPermissionAccess, machineName: str):
        """

        :param permissionAccess:
        :param machineName:
        """
    @property
    def PermissionEntries(self) -> EventLogPermissionEntryCollection:
        """

        :return:
        """
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """

        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

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

class EventLogPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def MachineName(self) -> str:
        """

        :return:
        """
    @MachineName.setter
    def MachineName(self, value: str) -> None: ...
    @property
    def PermissionAccess(self) -> EventLogPermissionAccess:
        """

        :return:
        """
    @PermissionAccess.setter
    def PermissionAccess(self, value: EventLogPermissionAccess) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
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

class EventLogPermissionEntry(Object):
    """"""

    def __init__(self, permissionAccess: EventLogPermissionAccess, machineName: str):
        """

        :param permissionAccess:
        :param machineName:
        """
    @property
    def MachineName(self) -> str:
        """

        :return:
        """
    @property
    def PermissionAccess(self) -> EventLogPermissionAccess:
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

class EventLogPermissionEntryCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""

    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
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
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, value: EventLogPermissionEntry) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def AddRange(self, value: EventLogPermissionEntryCollection) -> None:
        """

        :param value:
        """
    @overload
    def AddRange(self, value: Array[EventLogPermissionEntry]) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: EventLogPermissionEntry) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[EventLogPermissionEntry], index: int) -> None:
        """

        :param array:
        :param index:
        """
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
    def IndexOf(self, value: EventLogPermissionEntry) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: EventLogPermissionEntry) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, value: EventLogPermissionEntry) -> None:
        """

        :param value:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: EventLogPermissionEntry) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class EventLogTraceListener(TraceListener, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, eventLog: EventLog):
        """

        :param eventLog:
        """
    @overload
    def __init__(self, source: str):
        """

        :param source:
        """
    @property
    def Attributes(self) -> StringDictionary:
        """

        :return:
        """
    @property
    def EventLog(self) -> EventLog:
        """

        :return:
        """
    @EventLog.setter
    def EventLog(self, value: EventLog) -> None: ...
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

class EventSchemaTraceListener(TextWriterTraceListener, IDisposable):
    """"""

    @overload
    def __init__(self, fileName: str):
        """

        :param fileName:
        """
    @overload
    def __init__(self, fileName: str, name: str):
        """

        :param fileName:
        :param name:
        """
    @overload
    def __init__(self, fileName: str, name: str, bufferSize: int):
        """

        :param fileName:
        :param name:
        :param bufferSize:
        """
    @overload
    def __init__(
        self, fileName: str, name: str, bufferSize: int, logRetentionOption: TraceLogRetentionOption
    ):
        """

        :param fileName:
        :param name:
        :param bufferSize:
        :param logRetentionOption:
        """
    @overload
    def __init__(
        self,
        fileName: str,
        name: str,
        bufferSize: int,
        logRetentionOption: TraceLogRetentionOption,
        maximumFileSize: int,
    ):
        """

        :param fileName:
        :param name:
        :param bufferSize:
        :param logRetentionOption:
        :param maximumFileSize:
        """
    @overload
    def __init__(
        self,
        fileName: str,
        name: str,
        bufferSize: int,
        logRetentionOption: TraceLogRetentionOption,
        maximumFileSize: int,
        maximumNumberOfFiles: int,
    ):
        """

        :param fileName:
        :param name:
        :param bufferSize:
        :param logRetentionOption:
        :param maximumFileSize:
        :param maximumNumberOfFiles:
        """
    @property
    def Attributes(self) -> StringDictionary:
        """

        :return:
        """
    @property
    def BufferSize(self) -> int:
        """

        :return:
        """
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
    def MaximumFileSize(self) -> int:
        """

        :return:
        """
    @property
    def MaximumNumberOfFiles(self) -> int:
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
    def TraceLogRetentionOption(self) -> TraceLogRetentionOption:
        """

        :return:
        """
    @property
    def TraceOutputOptions(self) -> TraceOptions:
        """

        :return:
        """
    @TraceOutputOptions.setter
    def TraceOutputOptions(self, value: TraceOptions) -> None: ...
    @property
    def Writer(self) -> TextWriter:
        """

        :return:
        """
    @Writer.setter
    def Writer(self, value: TextWriter) -> None: ...
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

class EventSourceCreationData(Object):
    """"""

    def __init__(self, source: str, logName: str):
        """

        :param source:
        :param logName:
        """
    @property
    def CategoryCount(self) -> int:
        """

        :return:
        """
    @CategoryCount.setter
    def CategoryCount(self, value: int) -> None: ...
    @property
    def CategoryResourceFile(self) -> str:
        """

        :return:
        """
    @CategoryResourceFile.setter
    def CategoryResourceFile(self, value: str) -> None: ...
    @property
    def LogName(self) -> str:
        """

        :return:
        """
    @LogName.setter
    def LogName(self, value: str) -> None: ...
    @property
    def MachineName(self) -> str:
        """

        :return:
        """
    @MachineName.setter
    def MachineName(self, value: str) -> None: ...
    @property
    def MessageResourceFile(self) -> str:
        """

        :return:
        """
    @MessageResourceFile.setter
    def MessageResourceFile(self, value: str) -> None: ...
    @property
    def ParameterResourceFile(self) -> str:
        """

        :return:
        """
    @ParameterResourceFile.setter
    def ParameterResourceFile(self, value: str) -> None: ...
    @property
    def Source(self) -> str:
        """

        :return:
        """
    @Source.setter
    def Source(self, value: str) -> None: ...
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

class EventTypeFilter(TraceFilter):
    """"""

    def __init__(self, level: SourceLevels):
        """

        :param level:
        """
    @property
    def EventType(self) -> SourceLevels:
        """

        :return:
        """
    @EventType.setter
    def EventType(self, value: SourceLevels) -> None: ...
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
        """

        :param cache:
        :param source:
        :param eventType:
        :param id:
        :param formatOrMessage:
        :param args:
        :param data1:
        :param data:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class FileVersionInfo(Object):
    """"""

    @property
    def Comments(self) -> str:
        """

        :return:
        """
    @property
    def CompanyName(self) -> str:
        """

        :return:
        """
    @property
    def FileBuildPart(self) -> int:
        """

        :return:
        """
    @property
    def FileDescription(self) -> str:
        """

        :return:
        """
    @property
    def FileMajorPart(self) -> int:
        """

        :return:
        """
    @property
    def FileMinorPart(self) -> int:
        """

        :return:
        """
    @property
    def FileName(self) -> str:
        """

        :return:
        """
    @property
    def FilePrivatePart(self) -> int:
        """

        :return:
        """
    @property
    def FileVersion(self) -> str:
        """

        :return:
        """
    @property
    def InternalName(self) -> str:
        """

        :return:
        """
    @property
    def IsDebug(self) -> bool:
        """

        :return:
        """
    @property
    def IsPatched(self) -> bool:
        """

        :return:
        """
    @property
    def IsPreRelease(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivateBuild(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialBuild(self) -> bool:
        """

        :return:
        """
    @property
    def Language(self) -> str:
        """

        :return:
        """
    @property
    def LegalCopyright(self) -> str:
        """

        :return:
        """
    @property
    def LegalTrademarks(self) -> str:
        """

        :return:
        """
    @property
    def OriginalFilename(self) -> str:
        """

        :return:
        """
    @property
    def PrivateBuild(self) -> str:
        """

        :return:
        """
    @property
    def ProductBuildPart(self) -> int:
        """

        :return:
        """
    @property
    def ProductMajorPart(self) -> int:
        """

        :return:
        """
    @property
    def ProductMinorPart(self) -> int:
        """

        :return:
        """
    @property
    def ProductName(self) -> str:
        """

        :return:
        """
    @property
    def ProductPrivatePart(self) -> int:
        """

        :return:
        """
    @property
    def ProductVersion(self) -> str:
        """

        :return:
        """
    @property
    def SpecialBuild(self) -> str:
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
    @classmethod
    def GetVersionInfo(cls, fileName: str) -> FileVersionInfo:
        """

        :param fileName:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class FilterElement(TypedElement):
    """"""

    def __init__(self):
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def InitData(self) -> str:
        """

        :return:
        """
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
        """

        :return:
        """
    @TypeName.setter
    def TypeName(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetRuntimeObject(self) -> TraceFilter:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class ICollectData:
    """"""

    def CloseData(self) -> None:
        """"""
    def CollectData(
        self, id: int, valueName: IntPtr, data: IntPtr, totalBytes: int, res: IntPtr
    ) -> Tuple[None, IntPtr]:
        """

        :param id:
        :param valueName:
        :param data:
        :param totalBytes:
        :param res:
        """

class ICustomDebuggerNotification:
    """"""

class InitState(Enum):
    """"""

    NotInitialized: InitState = ...
    """"""
    Initializing: InitState = ...
    """"""
    Initialized: InitState = ...
    """"""

class InstanceData(Object):
    """"""

    def __init__(self, instanceName: str, sample: CounterSample):
        """

        :param instanceName:
        :param sample:
        """
    @property
    def InstanceName(self) -> str:
        """

        :return:
        """
    @property
    def RawValue(self) -> int:
        """

        :return:
        """
    @property
    def Sample(self) -> CounterSample:
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

class InstanceDataCollection(DictionaryBase, ICollection, IDictionary, IEnumerable):
    """"""

    def __init__(self, counterName: str):
        """

        :param counterName:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def CounterName(self) -> str:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
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
    def Keys(self) -> ICollection:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection:
        """

        :return:
        """
    def Add(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, key: object) -> bool:
        """

        :param key:
        :return:
        """
    @overload
    def Contains(self, instanceName: str) -> bool:
        """

        :param instanceName:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, instances: Array[InstanceData], index: int) -> None:
        """

        :param instances:
        :param index:
        """
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
    def Remove(self, key: object) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __getitem__(self, key: object) -> object:
        """

        :param key:
        :return:
        """
    @overload
    def __getitem__(self, instanceName: str) -> InstanceData:
        """

        :param instanceName:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class InstanceDataCollectionCollection(DictionaryBase, ICollection, IDictionary, IEnumerable):
    """"""

    def __init__(self):
        """"""
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
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
    def Keys(self) -> ICollection:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection:
        """

        :return:
        """
    def Add(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, key: object) -> bool:
        """

        :param key:
        :return:
        """
    @overload
    def Contains(self, counterName: str) -> bool:
        """

        :param counterName:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, counters: Array[InstanceDataCollection], index: int) -> None:
        """

        :param counters:
        :param index:
        """
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
    def Remove(self, key: object) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __getitem__(self, key: object) -> object:
        """

        :param key:
        :return:
        """
    @overload
    def __getitem__(self, counterName: str) -> InstanceDataCollection:
        """

        :param counterName:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class ListenerElement(TypedElement):
    """"""

    def __init__(self, allowReferences: bool):
        """

        :param allowReferences:
        """
    @property
    def Attributes(self) -> Hashtable:
        """

        :return:
        """
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def Filter(self) -> FilterElement:
        """

        :return:
        """
    @property
    def InitData(self) -> str:
        """

        :return:
        """
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
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    @TypeName.setter
    def TypeName(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetRuntimeObject(self) -> TraceListener:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class ListenerElementsCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    """"""

    def __init__(self):
        """"""
    @property
    def CollectionType(self) -> ConfigurationElementCollectionType:
        """"""
    @property
    def Count(self) -> int:
        """

        :return:
        """
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
        """

        :return:
        """
    @property
    def Item(self) -> ListenerElement:
        """

        :return:
        """
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
        """

        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[ConfigurationElement], index: int) -> None:
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
    def GetRuntimeObject(self) -> TraceListenerCollection:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, name: str) -> ListenerElement:
        """

        :param name:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class Log(ABC, Object):
    """"""

    GlobalSwitch: Final[ClassVar[LogSwitch]] = ...
    """
    
    :return: 
    """
    @classmethod
    @property
    def IsConsoleEnabled(cls) -> bool:
        """

        :return:
        """
    @classmethod
    @IsConsoleEnabled.setter
    def IsConsoleEnabled(cls, value: bool) -> None: ...
    @classmethod
    def AddOnLogMessage(cls, handler: LogMessageEventHandler) -> None:
        """

        :param handler:
        """
    @classmethod
    def AddOnLogSwitchLevel(cls, handler: LogSwitchLevelHandler) -> None:
        """

        :param handler:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def Error(cls, message: str) -> None:
        """

        :param message:
        """
    @classmethod
    @overload
    def Error(cls, logswitch: LogSwitch, message: str) -> None:
        """

        :param logswitch:
        :param message:
        """
    @classmethod
    @overload
    def Error(cls, switchname: str, message: str) -> None:
        """

        :param switchname:
        :param message:
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
    @overload
    def LogMessage(cls, level: LoggingLevels, message: str) -> None:
        """

        :param level:
        :param message:
        """
    @classmethod
    @overload
    def LogMessage(cls, level: LoggingLevels, logswitch: LogSwitch, message: str) -> None:
        """

        :param level:
        :param logswitch:
        :param message:
        """
    @classmethod
    def Panic(cls, message: str) -> None:
        """

        :param message:
        """
    @classmethod
    def RemoveOnLogMessage(cls, handler: LogMessageEventHandler) -> None:
        """

        :param handler:
        """
    @classmethod
    def RemoveOnLogSwitchLevel(cls, handler: LogSwitchLevelHandler) -> None:
        """

        :param handler:
        """
    @classmethod
    @overload
    def Status(cls, message: str) -> None:
        """

        :param message:
        """
    @classmethod
    @overload
    def Status(cls, logswitch: LogSwitch, message: str) -> None:
        """

        :param logswitch:
        :param message:
        """
    @classmethod
    @overload
    def Status(cls, switchname: str, message: str) -> None:
        """

        :param switchname:
        :param message:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    @overload
    def Trace(cls, message: str) -> None:
        """

        :param message:
        """
    @classmethod
    @overload
    def Trace(cls, logswitch: LogSwitch, message: str) -> None:
        """

        :param logswitch:
        :param message:
        """
    @classmethod
    @overload
    def Trace(cls, switchname: str, message: str) -> None:
        """

        :param switchname:
        :param message:
        """
    @classmethod
    @overload
    def Warning(cls, message: str) -> None:
        """

        :param message:
        """
    @classmethod
    @overload
    def Warning(cls, logswitch: LogSwitch, message: str) -> None:
        """

        :param logswitch:
        :param message:
        """
    @classmethod
    @overload
    def Warning(cls, switchname: str, message: str) -> None:
        """

        :param switchname:
        :param message:
        """

LogMessageEventHandler: Callable[[LoggingLevels, LogSwitch, str, StackTrace], None] = ...
"""

:param level: 
:param category: 
:param message: 
:param location: 
"""

class LogSwitch(Object):
    """"""

    def __init__(self, name: str, description: str, parent: LogSwitch):
        """

        :param name:
        :param description:
        :param parent:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @property
    def MinimumLevel(self) -> LoggingLevels:
        """

        :return:
        """
    @MinimumLevel.setter
    def MinimumLevel(self, value: LoggingLevels) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Parent(self) -> LogSwitch:
        """

        :return:
        """
    def CheckLevel(self, level: LoggingLevels) -> bool:
        """

        :param level:
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
    @classmethod
    def GetSwitch(cls, name: str) -> LogSwitch:
        """

        :param name:
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

LogSwitchLevelHandler: Callable[[LogSwitch, LoggingLevels], None] = ...
"""

:param ls: 
:param newLevel: 
"""

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

class MainWindowFinder(Object):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FindMainWindow(self, processId: int) -> IntPtr:
        """

        :param processId:
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

class MessageBoxPopup(Object):
    """"""

    def __init__(self, body: str, title: str, flags: int):
        """

        :param body:
        :param title:
        :param flags:
        """
    @property
    def ReturnValue(self) -> int:
        """

        :return:
        """
    @ReturnValue.setter
    def ReturnValue(self, value: int) -> None: ...
    def DoPopup(self) -> None:
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
    def ShowMessageBox(self) -> int:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ModuleInfo(Object):
    """"""

    Id: Final[int] = ...
    """
    
    :return: 
    """
    baseName: Final[str] = ...
    """
    
    :return: 
    """
    baseOfDll: Final[IntPtr] = ...
    """
    
    :return: 
    """
    entryPoint: Final[IntPtr] = ...
    """
    
    :return: 
    """
    fileName: Final[str] = ...
    """
    
    :return: 
    """
    sizeOfImage: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self):
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

class MonitoringDescriptionAttribute(DescriptionAttribute, _Attribute):
    """"""

    def __init__(self, description: str):
        """

        :param description:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
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

class NtProcessInfoHelper(ABC, Object):
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
    def GetProcessInfos(cls, processIdFilter: Predicate[int] = ...) -> Array[ProcessInfo]:
        """

        :param processIdFilter:
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

class NtProcessManager(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetFirstModuleInfo(cls, processId: int) -> ModuleInfo:
        """

        :param processId:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    def GetModuleInfos(cls, processId: int) -> Array[ModuleInfo]:
        """

        :param processId:
        :return:
        """
    @classmethod
    def GetProcessIdFromHandle(cls, processHandle: SafeProcessHandle) -> int:
        """

        :param processHandle:
        :return:
        """
    @classmethod
    @overload
    def GetProcessIds(cls) -> Array[int]:
        """

        :return:
        """
    @classmethod
    @overload
    def GetProcessIds(cls, machineName: str, isRemoteMachine: bool) -> Array[int]:
        """

        :param machineName:
        :param isRemoteMachine:
        :return:
        """
    @classmethod
    def GetProcessInfos(cls, machineName: str, isRemoteMachine: bool) -> Array[ProcessInfo]:
        """

        :param machineName:
        :param isRemoteMachine:
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

class OrdinalCaseInsensitiveComparer(Object, IComparer):
    """"""

    def __init__(self):
        """"""
    def Compare(self, x: object, y: object) -> int:
        """

        :param x:
        :param y:
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

class OverflowAction(Enum):
    """"""

    OverwriteAsNeeded: OverflowAction = ...
    """"""
    OverwriteOlder: OverflowAction = ...
    """"""
    DoNotOverwrite: OverflowAction = ...
    """"""

class PerfCounterSection(ConfigurationElement):
    """"""

    def __init__(self):
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def FileMappingSize(self) -> int:
        """

        :return:
        """
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
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class PerformanceCounter(Component, IComponent, ISupportInitialize, IDisposable):
    """"""

    DefaultFileMappingSize: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, categoryName: str, counterName: str):
        """

        :param categoryName:
        :param counterName:
        """
    @overload
    def __init__(self, categoryName: str, counterName: str, readOnly: bool):
        """

        :param categoryName:
        :param counterName:
        :param readOnly:
        """
    @overload
    def __init__(self, categoryName: str, counterName: str, instanceName: str):
        """

        :param categoryName:
        :param counterName:
        :param instanceName:
        """
    @overload
    def __init__(self, categoryName: str, counterName: str, instanceName: str, readOnly: bool):
        """

        :param categoryName:
        :param counterName:
        :param instanceName:
        :param readOnly:
        """
    @overload
    def __init__(self, categoryName: str, counterName: str, instanceName: str, machineName: str):
        """

        :param categoryName:
        :param counterName:
        :param instanceName:
        :param machineName:
        """
    @property
    def CategoryName(self) -> str:
        """

        :return:
        """
    @CategoryName.setter
    def CategoryName(self, value: str) -> None: ...
    @property
    def Container(self) -> IContainer:
        """

        :return:
        """
    @property
    def CounterHelp(self) -> str:
        """

        :return:
        """
    @property
    def CounterName(self) -> str:
        """

        :return:
        """
    @CounterName.setter
    def CounterName(self, value: str) -> None: ...
    @property
    def CounterType(self) -> PerformanceCounterType:
        """

        :return:
        """
    @property
    def InstanceLifetime(self) -> PerformanceCounterInstanceLifetime:
        """

        :return:
        """
    @InstanceLifetime.setter
    def InstanceLifetime(self, value: PerformanceCounterInstanceLifetime) -> None: ...
    @property
    def InstanceName(self) -> str:
        """

        :return:
        """
    @InstanceName.setter
    def InstanceName(self, value: str) -> None: ...
    @property
    def MachineName(self) -> str:
        """

        :return:
        """
    @MachineName.setter
    def MachineName(self, value: str) -> None: ...
    @property
    def RawValue(self) -> int:
        """

        :return:
        """
    @RawValue.setter
    def RawValue(self, value: int) -> None: ...
    @property
    def ReadOnly(self) -> bool:
        """

        :return:
        """
    @ReadOnly.setter
    def ReadOnly(self, value: bool) -> None: ...
    @property
    def Site(self) -> ISite:
        """

        :return:
        """
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
        """

        :param requestedType:
        :return:
        """
    def Decrement(self) -> int:
        """

        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndInit(self) -> None:
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
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Increment(self) -> int:
        """

        :return:
        """
    def IncrementBy(self, value: int) -> int:
        """

        :param value:
        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def NextSample(self) -> CounterSample:
        """

        :return:
        """
    def NextValue(self) -> float:
        """

        :return:
        """
    def RemoveInstance(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    Disposed: EventType[EventHandler] = ...
    """"""

class PerformanceCounterCategory(Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, categoryName: str):
        """

        :param categoryName:
        """
    @overload
    def __init__(self, categoryName: str, machineName: str):
        """

        :param categoryName:
        :param machineName:
        """
    @property
    def CategoryHelp(self) -> str:
        """

        :return:
        """
    @property
    def CategoryName(self) -> str:
        """

        :return:
        """
    @CategoryName.setter
    def CategoryName(self, value: str) -> None: ...
    @property
    def CategoryType(self) -> PerformanceCounterCategoryType:
        """

        :return:
        """
    @property
    def MachineName(self) -> str:
        """

        :return:
        """
    @MachineName.setter
    def MachineName(self, value: str) -> None: ...
    @overload
    def CounterExists(self, counterName: str) -> bool:
        """

        :param counterName:
        :return:
        """
    @classmethod
    @overload
    def CounterExists(cls, counterName: str, categoryName: str) -> bool:
        """

        :param counterName:
        :param categoryName:
        :return:
        """
    @classmethod
    @overload
    def CounterExists(cls, counterName: str, categoryName: str, machineName: str) -> bool:
        """

        :param counterName:
        :param categoryName:
        :param machineName:
        :return:
        """
    @classmethod
    @overload
    def Create(
        cls, categoryName: str, categoryHelp: str, counterData: CounterCreationDataCollection
    ) -> PerformanceCounterCategory:
        """

        :param categoryName:
        :param categoryHelp:
        :param counterData:
        :return:
        """
    @classmethod
    @overload
    def Create(
        cls,
        categoryName: str,
        categoryHelp: str,
        categoryType: PerformanceCounterCategoryType,
        counterData: CounterCreationDataCollection,
    ) -> PerformanceCounterCategory:
        """

        :param categoryName:
        :param categoryHelp:
        :param categoryType:
        :param counterData:
        :return:
        """
    @classmethod
    @overload
    def Create(
        cls, categoryName: str, categoryHelp: str, counterName: str, counterHelp: str
    ) -> PerformanceCounterCategory:
        """

        :param categoryName:
        :param categoryHelp:
        :param counterName:
        :param counterHelp:
        :return:
        """
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
        """

        :param categoryName:
        :param categoryHelp:
        :param categoryType:
        :param counterName:
        :param counterHelp:
        :return:
        """
    @classmethod
    def Delete(cls, categoryName: str) -> None:
        """

        :param categoryName:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def Exists(cls, categoryName: str) -> bool:
        """

        :param categoryName:
        :return:
        """
    @classmethod
    @overload
    def Exists(cls, categoryName: str, machineName: str) -> bool:
        """

        :param categoryName:
        :param machineName:
        :return:
        """
    @classmethod
    @overload
    def GetCategories(cls) -> Array[PerformanceCounterCategory]:
        """

        :return:
        """
    @classmethod
    @overload
    def GetCategories(cls, machineName: str) -> Array[PerformanceCounterCategory]:
        """

        :param machineName:
        :return:
        """
    @overload
    def GetCounters(self) -> Array[PerformanceCounter]:
        """

        :return:
        """
    @overload
    def GetCounters(self, instanceName: str) -> Array[PerformanceCounter]:
        """

        :param instanceName:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetInstanceNames(self) -> Array[str]:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def InstanceExists(self, instanceName: str) -> bool:
        """

        :param instanceName:
        :return:
        """
    @classmethod
    @overload
    def InstanceExists(cls, instanceName: str, categoryName: str) -> bool:
        """

        :param instanceName:
        :param categoryName:
        :return:
        """
    @classmethod
    @overload
    def InstanceExists(cls, instanceName: str, categoryName: str, machineName: str) -> bool:
        """

        :param instanceName:
        :param categoryName:
        :param machineName:
        :return:
        """
    def ReadCategory(self) -> InstanceDataCollectionCollection:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class PerformanceCounterCategoryOptions(Enum):
    """"""

    EnableReuse: PerformanceCounterCategoryOptions = ...
    """"""
    UseUniqueSharedMemory: PerformanceCounterCategoryOptions = ...
    """"""

class PerformanceCounterCategoryType(Enum):
    """"""

    SingleInstance: PerformanceCounterCategoryType = ...
    """"""
    MultiInstance: PerformanceCounterCategoryType = ...
    """"""
    Unknown: PerformanceCounterCategoryType = ...
    """"""

class PerformanceCounterInstanceLifetime(Enum):
    """"""

    Global: PerformanceCounterInstanceLifetime = ...
    """"""
    Process: PerformanceCounterInstanceLifetime = ...
    """"""

class PerformanceCounterLib(Object):
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

class PerformanceCounterManager(Object, ICollectData):
    """"""

    def __init__(self):
        """"""
    def CloseData(self) -> None:
        """"""
    def CollectData(
        self, id: int, valueName: IntPtr, data: IntPtr, totalBytes: int, res: IntPtr
    ) -> Tuple[None, IntPtr]:
        """

        :param id:
        :param valueName:
        :param data:
        :param totalBytes:
        :param res:
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

class PerformanceCounterPermission(
    ResourcePermissionBase, IUnrestrictedPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    @overload
    def __init__(self, permissionAccessEntries: Array[PerformanceCounterPermissionEntry]):
        """

        :param permissionAccessEntries:
        """
    @overload
    def __init__(
        self,
        permissionAccess: PerformanceCounterPermissionAccess,
        machineName: str,
        categoryName: str,
    ):
        """

        :param permissionAccess:
        :param machineName:
        :param categoryName:
        """
    @property
    def PermissionEntries(self) -> PerformanceCounterPermissionEntryCollection:
        """

        :return:
        """
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """

        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

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

class PerformanceCounterPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def CategoryName(self) -> str:
        """

        :return:
        """
    @CategoryName.setter
    def CategoryName(self, value: str) -> None: ...
    @property
    def MachineName(self) -> str:
        """

        :return:
        """
    @MachineName.setter
    def MachineName(self, value: str) -> None: ...
    @property
    def PermissionAccess(self) -> PerformanceCounterPermissionAccess:
        """

        :return:
        """
    @PermissionAccess.setter
    def PermissionAccess(self, value: PerformanceCounterPermissionAccess) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
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

class PerformanceCounterPermissionEntry(Object):
    """"""

    def __init__(
        self,
        permissionAccess: PerformanceCounterPermissionAccess,
        machineName: str,
        categoryName: str,
    ):
        """

        :param permissionAccess:
        :param machineName:
        :param categoryName:
        """
    @property
    def CategoryName(self) -> str:
        """

        :return:
        """
    @property
    def MachineName(self) -> str:
        """

        :return:
        """
    @property
    def PermissionAccess(self) -> PerformanceCounterPermissionAccess:
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

class PerformanceCounterPermissionEntryCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""

    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
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
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, value: PerformanceCounterPermissionEntry) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def AddRange(self, value: PerformanceCounterPermissionEntryCollection) -> None:
        """

        :param value:
        """
    @overload
    def AddRange(self, value: Array[PerformanceCounterPermissionEntry]) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: PerformanceCounterPermissionEntry) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[PerformanceCounterPermissionEntry], index: int) -> None:
        """

        :param array:
        :param index:
        """
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
    def IndexOf(self, value: PerformanceCounterPermissionEntry) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: PerformanceCounterPermissionEntry) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, value: PerformanceCounterPermissionEntry) -> None:
        """

        :param value:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: PerformanceCounterPermissionEntry) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

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

class PerformanceMonitor(Object):
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

class Process(Component, IComponent, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def BasePriority(self) -> int:
        """

        :return:
        """
    @property
    def Container(self) -> IContainer:
        """

        :return:
        """
    @property
    def EnableRaisingEvents(self) -> bool:
        """

        :return:
        """
    @EnableRaisingEvents.setter
    def EnableRaisingEvents(self, value: bool) -> None: ...
    @property
    def ExitCode(self) -> int:
        """

        :return:
        """
    @property
    def ExitTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def Handle(self) -> IntPtr:
        """

        :return:
        """
    @property
    def HandleCount(self) -> int:
        """

        :return:
        """
    @property
    def HasExited(self) -> bool:
        """

        :return:
        """
    @property
    def Id(self) -> int:
        """

        :return:
        """
    @property
    def MachineName(self) -> str:
        """

        :return:
        """
    @property
    def MainModule(self) -> ProcessModule:
        """

        :return:
        """
    @property
    def MainWindowHandle(self) -> IntPtr:
        """

        :return:
        """
    @property
    def MainWindowTitle(self) -> str:
        """

        :return:
        """
    @property
    def MaxWorkingSet(self) -> IntPtr:
        """

        :return:
        """
    @MaxWorkingSet.setter
    def MaxWorkingSet(self, value: IntPtr) -> None: ...
    @property
    def MinWorkingSet(self) -> IntPtr:
        """

        :return:
        """
    @MinWorkingSet.setter
    def MinWorkingSet(self, value: IntPtr) -> None: ...
    @property
    def Modules(self) -> ProcessModuleCollection:
        """

        :return:
        """
    @property
    def NonpagedSystemMemorySize(self) -> int:
        """

        :return:
        """
    @property
    def NonpagedSystemMemorySize64(self) -> int:
        """

        :return:
        """
    @property
    def PagedMemorySize(self) -> int:
        """

        :return:
        """
    @property
    def PagedMemorySize64(self) -> int:
        """

        :return:
        """
    @property
    def PagedSystemMemorySize(self) -> int:
        """

        :return:
        """
    @property
    def PagedSystemMemorySize64(self) -> int:
        """

        :return:
        """
    @property
    def PeakPagedMemorySize(self) -> int:
        """

        :return:
        """
    @property
    def PeakPagedMemorySize64(self) -> int:
        """

        :return:
        """
    @property
    def PeakVirtualMemorySize(self) -> int:
        """

        :return:
        """
    @property
    def PeakVirtualMemorySize64(self) -> int:
        """

        :return:
        """
    @property
    def PeakWorkingSet(self) -> int:
        """

        :return:
        """
    @property
    def PeakWorkingSet64(self) -> int:
        """

        :return:
        """
    @property
    def PriorityBoostEnabled(self) -> bool:
        """

        :return:
        """
    @PriorityBoostEnabled.setter
    def PriorityBoostEnabled(self, value: bool) -> None: ...
    @property
    def PriorityClass(self) -> ProcessPriorityClass:
        """

        :return:
        """
    @PriorityClass.setter
    def PriorityClass(self, value: ProcessPriorityClass) -> None: ...
    @property
    def PrivateMemorySize(self) -> int:
        """

        :return:
        """
    @property
    def PrivateMemorySize64(self) -> int:
        """

        :return:
        """
    @property
    def PrivilegedProcessorTime(self) -> TimeSpan:
        """

        :return:
        """
    @property
    def ProcessName(self) -> str:
        """

        :return:
        """
    @property
    def ProcessorAffinity(self) -> IntPtr:
        """

        :return:
        """
    @ProcessorAffinity.setter
    def ProcessorAffinity(self, value: IntPtr) -> None: ...
    @property
    def Responding(self) -> bool:
        """

        :return:
        """
    @property
    def SafeHandle(self) -> SafeProcessHandle:
        """

        :return:
        """
    @property
    def SessionId(self) -> int:
        """

        :return:
        """
    @property
    def Site(self) -> ISite:
        """

        :return:
        """
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    @property
    def StandardError(self) -> StreamReader:
        """

        :return:
        """
    @property
    def StandardInput(self) -> StreamWriter:
        """

        :return:
        """
    @property
    def StandardOutput(self) -> StreamReader:
        """

        :return:
        """
    @property
    def StartInfo(self) -> ProcessStartInfo:
        """

        :return:
        """
    @StartInfo.setter
    def StartInfo(self, value: ProcessStartInfo) -> None: ...
    @property
    def StartTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke:
        """

        :return:
        """
    @SynchronizingObject.setter
    def SynchronizingObject(self, value: ISynchronizeInvoke) -> None: ...
    @property
    def Threads(self) -> ProcessThreadCollection:
        """

        :return:
        """
    @property
    def TotalProcessorTime(self) -> TimeSpan:
        """

        :return:
        """
    @property
    def UserProcessorTime(self) -> TimeSpan:
        """

        :return:
        """
    @property
    def VirtualMemorySize(self) -> int:
        """

        :return:
        """
    @property
    def VirtualMemorySize64(self) -> int:
        """

        :return:
        """
    @property
    def WorkingSet(self) -> int:
        """

        :return:
        """
    @property
    def WorkingSet64(self) -> int:
        """

        :return:
        """
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
        """

        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    @classmethod
    def EnterDebugMode(cls) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetCurrentProcess(cls) -> Process:
        """

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
    @classmethod
    @overload
    def GetProcessById(cls, processId: int) -> Process:
        """

        :param processId:
        :return:
        """
    @classmethod
    @overload
    def GetProcessById(cls, processId: int, machineName: str) -> Process:
        """

        :param processId:
        :param machineName:
        :return:
        """
    @classmethod
    @overload
    def GetProcesses(cls) -> Array[Process]:
        """

        :return:
        """
    @classmethod
    @overload
    def GetProcesses(cls, machineName: str) -> Array[Process]:
        """

        :param machineName:
        :return:
        """
    @classmethod
    @overload
    def GetProcessesByName(cls, processName: str) -> Array[Process]:
        """

        :param processName:
        :return:
        """
    @classmethod
    @overload
    def GetProcessesByName(cls, processName: str, machineName: str) -> Array[Process]:
        """

        :param processName:
        :param machineName:
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
    def Kill(self) -> None:
        """"""
    @classmethod
    def LeaveDebugMode(cls) -> None:
        """"""
    def Refresh(self) -> None:
        """"""
    @overload
    def Start(self) -> bool:
        """

        :return:
        """
    @classmethod
    @overload
    def Start(cls, startInfo: ProcessStartInfo) -> Process:
        """

        :param startInfo:
        :return:
        """
    @classmethod
    @overload
    def Start(cls, fileName: str) -> Process:
        """

        :param fileName:
        :return:
        """
    @classmethod
    @overload
    def Start(cls, fileName: str, arguments: str) -> Process:
        """

        :param fileName:
        :param arguments:
        :return:
        """
    @classmethod
    @overload
    def Start(cls, fileName: str, userName: str, password: SecureString, domain: str) -> Process:
        """

        :param fileName:
        :param userName:
        :param password:
        :param domain:
        :return:
        """
    @classmethod
    @overload
    def Start(
        cls, fileName: str, arguments: str, userName: str, password: SecureString, domain: str
    ) -> Process:
        """

        :param fileName:
        :param arguments:
        :param userName:
        :param password:
        :param domain:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def WaitForExit(self) -> None:
        """"""
    @overload
    def WaitForExit(self, milliseconds: int) -> bool:
        """

        :param milliseconds:
        :return:
        """
    @overload
    def WaitForInputIdle(self) -> bool:
        """

        :return:
        """
    @overload
    def WaitForInputIdle(self, milliseconds: int) -> bool:
        """

        :param milliseconds:
        :return:
        """
    Disposed: EventType[EventHandler] = ...
    """"""
    ErrorDataReceived: EventType[DataReceivedEventHandler] = ...
    """"""
    Exited: EventType[EventHandler] = ...
    """"""
    OutputDataReceived: EventType[DataReceivedEventHandler] = ...
    """"""

class ProcessData(Object):
    """"""

    ProcessId: Final[int] = ...
    """
    
    :return: 
    """
    StartupTime: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self, pid: int, startTime: int):
        """

        :param pid:
        :param startTime:
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

class ProcessInfo(Object):
    """"""

    basePriority: Final[int] = ...
    """
    
    :return: 
    """
    handleCount: Final[int] = ...
    """
    
    :return: 
    """
    mainModuleId: Final[int] = ...
    """
    
    :return: 
    """
    pageFileBytes: Final[int] = ...
    """
    
    :return: 
    """
    pageFileBytesPeak: Final[int] = ...
    """
    
    :return: 
    """
    poolNonpagedBytes: Final[int] = ...
    """
    
    :return: 
    """
    poolPagedBytes: Final[int] = ...
    """
    
    :return: 
    """
    privateBytes: Final[int] = ...
    """
    
    :return: 
    """
    processId: Final[int] = ...
    """
    
    :return: 
    """
    processName: Final[str] = ...
    """
    
    :return: 
    """
    sessionId: Final[int] = ...
    """
    
    :return: 
    """
    threadInfoList: Final[ArrayList] = ...
    """
    
    :return: 
    """
    virtualBytes: Final[int] = ...
    """
    
    :return: 
    """
    virtualBytesPeak: Final[int] = ...
    """
    
    :return: 
    """
    workingSet: Final[int] = ...
    """
    
    :return: 
    """
    workingSetPeak: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self):
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

class ProcessManager(ABC, Object):
    """"""

    @classmethod
    @property
    def IsNt(cls) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def IsOSOlderThanXP(cls) -> bool:
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
    @classmethod
    def GetMainWindowHandle(cls, processId: int) -> IntPtr:
        """

        :param processId:
        :return:
        """
    @classmethod
    def GetModuleInfos(cls, processId: int) -> Array[ModuleInfo]:
        """

        :param processId:
        :return:
        """
    @classmethod
    def GetProcessIdFromHandle(cls, processHandle: SafeProcessHandle) -> int:
        """

        :param processHandle:
        :return:
        """
    @classmethod
    @overload
    def GetProcessIds(cls) -> Array[int]:
        """

        :return:
        """
    @classmethod
    @overload
    def GetProcessIds(cls, machineName: str) -> Array[int]:
        """

        :param machineName:
        :return:
        """
    @classmethod
    def GetProcessInfo(cls, processId: int, machineName: str) -> ProcessInfo:
        """

        :param processId:
        :param machineName:
        :return:
        """
    @classmethod
    def GetProcessInfos(cls, machineName: str) -> Array[ProcessInfo]:
        """

        :param machineName:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @overload
    def IsProcessRunning(cls, processId: int) -> bool:
        """

        :param processId:
        :return:
        """
    @classmethod
    @overload
    def IsProcessRunning(cls, processId: int, machineName: str) -> bool:
        """

        :param processId:
        :param machineName:
        :return:
        """
    @classmethod
    def IsRemoteMachine(cls, machineName: str) -> bool:
        """

        :param machineName:
        :return:
        """
    @classmethod
    def OpenProcess(cls, processId: int, access: int, throwIfExited: bool) -> SafeProcessHandle:
        """

        :param processId:
        :param access:
        :param throwIfExited:
        :return:
        """
    @classmethod
    def OpenThread(cls, threadId: int, access: int) -> SafeThreadHandle:
        """

        :param threadId:
        :param access:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ProcessModule(Component, IComponent, IDisposable):
    """"""

    @property
    def BaseAddress(self) -> IntPtr:
        """

        :return:
        """
    @property
    def Container(self) -> IContainer:
        """

        :return:
        """
    @property
    def EntryPointAddress(self) -> IntPtr:
        """

        :return:
        """
    @property
    def FileName(self) -> str:
        """

        :return:
        """
    @property
    def FileVersionInfo(self) -> FileVersionInfo:
        """

        :return:
        """
    @property
    def ModuleMemorySize(self) -> int:
        """

        :return:
        """
    @property
    def ModuleName(self) -> str:
        """

        :return:
        """
    @property
    def Site(self) -> ISite:
        """

        :return:
        """
    @Site.setter
    def Site(self, value: ISite) -> None: ...
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
    Disposed: EventType[EventHandler] = ...
    """"""

class ProcessModuleCollection(ReadOnlyCollectionBase, ICollection, IEnumerable):
    """"""

    def __init__(self, processModules: Array[ProcessModule]):
        """

        :param processModules:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> ProcessModule:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    def Contains(self, module: ProcessModule) -> bool:
        """

        :param module:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[ProcessModule], index: int) -> None:
        """

        :param array:
        :param index:
        """
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
    def IndexOf(self, module: ProcessModule) -> int:
        """

        :param module:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> ProcessModule:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

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

class ProcessStartInfo(Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, fileName: str):
        """

        :param fileName:
        """
    @overload
    def __init__(self, fileName: str, arguments: str):
        """

        :param fileName:
        :param arguments:
        """
    @property
    def Arguments(self) -> str:
        """

        :return:
        """
    @Arguments.setter
    def Arguments(self, value: str) -> None: ...
    @property
    def CreateNoWindow(self) -> bool:
        """

        :return:
        """
    @CreateNoWindow.setter
    def CreateNoWindow(self, value: bool) -> None: ...
    @property
    def Domain(self) -> str:
        """

        :return:
        """
    @Domain.setter
    def Domain(self, value: str) -> None: ...
    @property
    def Environment(self) -> IDictionary[str, str]:
        """

        :return:
        """
    @property
    def EnvironmentVariables(self) -> StringDictionary:
        """

        :return:
        """
    @property
    def ErrorDialog(self) -> bool:
        """

        :return:
        """
    @ErrorDialog.setter
    def ErrorDialog(self, value: bool) -> None: ...
    @property
    def ErrorDialogParentHandle(self) -> IntPtr:
        """

        :return:
        """
    @ErrorDialogParentHandle.setter
    def ErrorDialogParentHandle(self, value: IntPtr) -> None: ...
    @property
    def FileName(self) -> str:
        """

        :return:
        """
    @FileName.setter
    def FileName(self, value: str) -> None: ...
    @property
    def LoadUserProfile(self) -> bool:
        """

        :return:
        """
    @LoadUserProfile.setter
    def LoadUserProfile(self, value: bool) -> None: ...
    @property
    def Password(self) -> SecureString:
        """

        :return:
        """
    @Password.setter
    def Password(self, value: SecureString) -> None: ...
    @property
    def PasswordInClearText(self) -> str:
        """

        :return:
        """
    @PasswordInClearText.setter
    def PasswordInClearText(self, value: str) -> None: ...
    @property
    def RedirectStandardError(self) -> bool:
        """

        :return:
        """
    @RedirectStandardError.setter
    def RedirectStandardError(self, value: bool) -> None: ...
    @property
    def RedirectStandardInput(self) -> bool:
        """

        :return:
        """
    @RedirectStandardInput.setter
    def RedirectStandardInput(self, value: bool) -> None: ...
    @property
    def RedirectStandardOutput(self) -> bool:
        """

        :return:
        """
    @RedirectStandardOutput.setter
    def RedirectStandardOutput(self, value: bool) -> None: ...
    @property
    def StandardErrorEncoding(self) -> Encoding:
        """

        :return:
        """
    @StandardErrorEncoding.setter
    def StandardErrorEncoding(self, value: Encoding) -> None: ...
    @property
    def StandardOutputEncoding(self) -> Encoding:
        """

        :return:
        """
    @StandardOutputEncoding.setter
    def StandardOutputEncoding(self, value: Encoding) -> None: ...
    @property
    def UseShellExecute(self) -> bool:
        """

        :return:
        """
    @UseShellExecute.setter
    def UseShellExecute(self, value: bool) -> None: ...
    @property
    def UserName(self) -> str:
        """

        :return:
        """
    @UserName.setter
    def UserName(self, value: str) -> None: ...
    @property
    def Verb(self) -> str:
        """

        :return:
        """
    @Verb.setter
    def Verb(self, value: str) -> None: ...
    @property
    def Verbs(self) -> Array[str]:
        """

        :return:
        """
    @property
    def WindowStyle(self) -> ProcessWindowStyle:
        """

        :return:
        """
    @WindowStyle.setter
    def WindowStyle(self, value: ProcessWindowStyle) -> None: ...
    @property
    def WorkingDirectory(self) -> str:
        """

        :return:
        """
    @WorkingDirectory.setter
    def WorkingDirectory(self, value: str) -> None: ...
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

class ProcessThread(Component, IComponent, IDisposable):
    """"""

    @property
    def BasePriority(self) -> int:
        """

        :return:
        """
    @property
    def Container(self) -> IContainer:
        """

        :return:
        """
    @property
    def CurrentPriority(self) -> int:
        """

        :return:
        """
    @property
    def Id(self) -> int:
        """

        :return:
        """
    @property
    def IdealProcessor(self) -> int:
        """

        :return:
        """
    @IdealProcessor.setter
    def IdealProcessor(self, value: int) -> None: ...
    @property
    def PriorityBoostEnabled(self) -> bool:
        """

        :return:
        """
    @PriorityBoostEnabled.setter
    def PriorityBoostEnabled(self, value: bool) -> None: ...
    @property
    def PriorityLevel(self) -> ThreadPriorityLevel:
        """

        :return:
        """
    @PriorityLevel.setter
    def PriorityLevel(self, value: ThreadPriorityLevel) -> None: ...
    @property
    def PrivilegedProcessorTime(self) -> TimeSpan:
        """

        :return:
        """
    @property
    def ProcessorAffinity(self) -> IntPtr:
        """

        :return:
        """
    @ProcessorAffinity.setter
    def ProcessorAffinity(self, value: IntPtr) -> None: ...
    @property
    def Site(self) -> ISite:
        """

        :return:
        """
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    @property
    def StartAddress(self) -> IntPtr:
        """

        :return:
        """
    @property
    def StartTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def ThreadState(self) -> ThreadState:
        """

        :return:
        """
    @property
    def TotalProcessorTime(self) -> TimeSpan:
        """

        :return:
        """
    @property
    def UserProcessorTime(self) -> TimeSpan:
        """

        :return:
        """
    @property
    def WaitReason(self) -> ThreadWaitReason:
        """

        :return:
        """
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
    def ResetIdealProcessor(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    Disposed: EventType[EventHandler] = ...
    """"""

class ProcessThreadCollection(ReadOnlyCollectionBase, ICollection, IEnumerable):
    """"""

    def __init__(self, processThreads: Array[ProcessThread]):
        """

        :param processThreads:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> ProcessThread:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    def Add(self, thread: ProcessThread) -> int:
        """

        :param thread:
        :return:
        """
    def Contains(self, thread: ProcessThread) -> bool:
        """

        :param thread:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[ProcessThread], index: int) -> None:
        """

        :param array:
        :param index:
        """
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
    def IndexOf(self, thread: ProcessThread) -> int:
        """

        :param thread:
        :return:
        """
    def Insert(self, index: int, thread: ProcessThread) -> None:
        """

        :param index:
        :param thread:
        """
    def Remove(self, thread: ProcessThread) -> None:
        """

        :param thread:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> ProcessThread:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class ProcessThreadTimes(Object):
    """"""

    def __init__(self):
        """"""
    @property
    def ExitTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def PrivilegedProcessorTime(self) -> TimeSpan:
        """

        :return:
        """
    @property
    def StartTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def TotalProcessorTime(self) -> TimeSpan:
        """

        :return:
        """
    @property
    def UserProcessorTime(self) -> TimeSpan:
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

class ProcessWaitHandle(WaitHandle, IDisposable):
    """"""

    @property
    def Handle(self) -> IntPtr:
        """

        :return:
        """
    @Handle.setter
    def Handle(self, value: IntPtr) -> None: ...
    @property
    def SafeWaitHandle(self) -> SafeWaitHandle:
        """

        :return:
        """
    @SafeWaitHandle.setter
    def SafeWaitHandle(self, value: SafeWaitHandle) -> None: ...
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
    def WaitOne(self) -> bool:
        """

        :return:
        """
    @overload
    def WaitOne(self, millisecondsTimeout: int) -> bool:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def WaitOne(self, timeout: TimeSpan) -> bool:
        """

        :param timeout:
        :return:
        """
    @overload
    def WaitOne(self, millisecondsTimeout: int, exitContext: bool) -> bool:
        """

        :param millisecondsTimeout:
        :param exitContext:
        :return:
        """
    @overload
    def WaitOne(self, timeout: TimeSpan, exitContext: bool) -> bool:
        """

        :param timeout:
        :param exitContext:
        :return:
        """

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

class SharedListenerElementsCollection(ListenerElementsCollection, ICollection, IEnumerable):
    """"""

    def __init__(self):
        """"""
    @property
    def CollectionType(self) -> ConfigurationElementCollectionType:
        """"""
    @property
    def Count(self) -> int:
        """

        :return:
        """
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
        """

        :return:
        """
    @property
    def Item(self) -> ListenerElement:
        """

        :return:
        """
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
        """

        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[ConfigurationElement], index: int) -> None:
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
    def GetRuntimeObject(self) -> TraceListenerCollection:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, name: str) -> ListenerElement:
        """

        :param name:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class SharedPerformanceCounter(Object):
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

class SharedUtils(ABC, Object):
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

class ShellExecuteHelper(Object):
    """"""

    def __init__(self, executeInfo: NativeMethods.ShellExecuteInfo):
        """

        :param executeInfo:
        """
    @property
    def ErrorCode(self) -> int:
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
    def ShellExecuteFunction(self) -> None:
        """"""
    def ShellExecuteOnSTAThread(self) -> bool:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SourceElement(ConfigurationElement):
    """"""

    def __init__(self):
        """"""
    @property
    def Attributes(self) -> Hashtable:
        """

        :return:
        """
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def Listeners(self) -> ListenerElementsCollection:
        """

        :return:
        """
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
        """

        :return:
        """
    @property
    def SwitchName(self) -> str:
        """

        :return:
        """
    @property
    def SwitchType(self) -> str:
        """

        :return:
        """
    @property
    def SwitchValue(self) -> str:
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
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SourceElementsCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    """"""

    def __init__(self):
        """"""
    @property
    def CollectionType(self) -> ConfigurationElementCollectionType:
        """"""
    @property
    def Count(self) -> int:
        """

        :return:
        """
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
        """

        :return:
        """
    @property
    def Item(self) -> SourceElement:
        """

        :return:
        """
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
        """

        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[ConfigurationElement], index: int) -> None:
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
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, name: str) -> SourceElement:
        """

        :param name:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class SourceFilter(TraceFilter):
    """"""

    def __init__(self, source: str):
        """

        :param source:
        """
    @property
    def Source(self) -> str:
        """

        :return:
        """
    @Source.setter
    def Source(self, value: str) -> None: ...
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
        """

        :param cache:
        :param source:
        :param eventType:
        :param id:
        :param formatOrMessage:
        :param args:
        :param data1:
        :param data:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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

class SourceSwitch(Switch):
    """"""

    @overload
    def __init__(self, name: str):
        """

        :param name:
        """
    @overload
    def __init__(self, displayName: str, defaultSwitchValue: str):
        """

        :param displayName:
        :param defaultSwitchValue:
        """
    @property
    def Attributes(self) -> StringDictionary:
        """

        :return:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @property
    def DisplayName(self) -> str:
        """

        :return:
        """
    @property
    def Level(self) -> SourceLevels:
        """

        :return:
        """
    @Level.setter
    def Level(self, value: SourceLevels) -> None: ...
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
    def ShouldTrace(self, eventType: TraceEventType) -> bool:
        """

        :param eventType:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class StackFrame(Object):
    """"""

    OFFSET_UNKNOWN: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, fNeedFileInfo: bool):
        """

        :param fNeedFileInfo:
        """
    @overload
    def __init__(self, skipFrames: int):
        """

        :param skipFrames:
        """
    @overload
    def __init__(self, skipFrames: int, fNeedFileInfo: bool):
        """

        :param skipFrames:
        :param fNeedFileInfo:
        """
    @overload
    def __init__(self, fileName: str, lineNumber: int):
        """

        :param fileName:
        :param lineNumber:
        """
    @overload
    def __init__(self, fileName: str, lineNumber: int, colNumber: int):
        """

        :param fileName:
        :param lineNumber:
        :param colNumber:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetFileColumnNumber(self) -> int:
        """

        :return:
        """
    def GetFileLineNumber(self) -> int:
        """

        :return:
        """
    def GetFileName(self) -> str:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetILOffset(self) -> int:
        """

        :return:
        """
    def GetMethod(self) -> MethodBase:
        """

        :return:
        """
    def GetNativeOffset(self) -> int:
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

class StackFrameExtensions(ABC, Object):
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
    def GetNativeIP(cls, stackFrame: StackFrame) -> IntPtr:
        """

        :param stackFrame:
        :return:
        """
    @classmethod
    def GetNativeImageBase(cls, stackFrame: StackFrame) -> IntPtr:
        """

        :param stackFrame:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def HasILOffset(cls, stackFrame: StackFrame) -> bool:
        """

        :param stackFrame:
        :return:
        """
    @classmethod
    def HasMethod(cls, stackFrame: StackFrame) -> bool:
        """

        :param stackFrame:
        :return:
        """
    @classmethod
    def HasNativeImage(cls, stackFrame: StackFrame) -> bool:
        """

        :param stackFrame:
        :return:
        """
    @classmethod
    def HasSource(cls, stackFrame: StackFrame) -> bool:
        """

        :param stackFrame:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class StackFrameHelper(Object, IDisposable):
    """"""

    def __init__(self, target: Thread):
        """

        :param target:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetColumnNumber(self, i: int) -> int:
        """

        :param i:
        :return:
        """
    def GetFilename(self, i: int) -> str:
        """

        :param i:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetILOffset(self, i: int) -> int:
        """

        :param i:
        :return:
        """
    def GetLineNumber(self, i: int) -> int:
        """

        :param i:
        :return:
        """
    def GetMethodBase(self, i: int) -> MethodBase:
        """

        :param i:
        :return:
        """
    def GetNumberOfFrames(self) -> int:
        """

        :return:
        """
    def GetOffset(self, i: int) -> int:
        """

        :param i:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def IsLastFrameFromForeignExceptionStackTrace(self, i: int) -> bool:
        """

        :param i:
        :return:
        """
    def SetNumberOfFrames(self, i: int) -> None:
        """

        :param i:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class StackTrace(Object):
    """"""

    METHODS_TO_SKIP: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, frame: StackFrame):
        """

        :param frame:
        """
    @overload
    def __init__(self, fNeedFileInfo: bool):
        """

        :param fNeedFileInfo:
        """
    @overload
    def __init__(self, e: Exception):
        """

        :param e:
        """
    @overload
    def __init__(self, skipFrames: int):
        """

        :param skipFrames:
        """
    @overload
    def __init__(self, targetThread: Thread, needFileInfo: bool):
        """

        :param targetThread:
        :param needFileInfo:
        """
    @overload
    def __init__(self, e: Exception, fNeedFileInfo: bool):
        """

        :param e:
        :param fNeedFileInfo:
        """
    @overload
    def __init__(self, e: Exception, skipFrames: int):
        """

        :param e:
        :param skipFrames:
        """
    @overload
    def __init__(self, skipFrames: int, fNeedFileInfo: bool):
        """

        :param skipFrames:
        :param fNeedFileInfo:
        """
    @overload
    def __init__(self, e: Exception, skipFrames: int, fNeedFileInfo: bool):
        """

        :param e:
        :param skipFrames:
        :param fNeedFileInfo:
        """
    @property
    def FrameCount(self) -> int:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetFrame(self, index: int) -> StackFrame:
        """

        :param index:
        :return:
        """
    def GetFrames(self) -> Array[StackFrame]:
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
    def ToString(self) -> str:
        """

        :return:
        """

class StackTraceSymbols(Object, IDisposable):
    """"""

    def __init__(self):
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
    def GetSourceLineInfo(
        self,
        assemblyPath: str,
        loadedPeAddress: IntPtr,
        loadedPeSize: int,
        inMemoryPdbAddress: IntPtr,
        inMemoryPdbSize: int,
        methodToken: int,
        ilOffset: int,
        sourceFile: str,
        sourceLine: int,
        sourceColumn: int,
    ) -> Tuple[None, str, int, int]:
        """

        :param assemblyPath:
        :param loadedPeAddress:
        :param loadedPeSize:
        :param inMemoryPdbAddress:
        :param inMemoryPdbSize:
        :param methodToken:
        :param ilOffset:
        :param sourceFile:
        :param sourceLine:
        :param sourceColumn:
        """
    def GetSourceLineInfoWithoutCasAssert(
        self,
        assemblyPath: str,
        loadedPeAddress: IntPtr,
        loadedPeSize: int,
        inMemoryPdbAddress: IntPtr,
        inMemoryPdbSize: int,
        methodToken: int,
        ilOffset: int,
        sourceFile: str,
        sourceLine: int,
        sourceColumn: int,
    ) -> Tuple[None, str, int, int]:
        """

        :param assemblyPath:
        :param loadedPeAddress:
        :param loadedPeSize:
        :param inMemoryPdbAddress:
        :param inMemoryPdbSize:
        :param methodToken:
        :param ilOffset:
        :param sourceFile:
        :param sourceLine:
        :param sourceColumn:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class Stopwatch(Object):
    """"""

    Frequency: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    IsHighResolution: Final[ClassVar[bool]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def Elapsed(self) -> TimeSpan:
        """

        :return:
        """
    @property
    def ElapsedMilliseconds(self) -> int:
        """

        :return:
        """
    @property
    def ElapsedTicks(self) -> int:
        """

        :return:
        """
    @property
    def IsRunning(self) -> bool:
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
    @classmethod
    def GetTimestamp(cls) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def Restart(self) -> None:
        """"""
    def Start(self) -> None:
        """"""
    @classmethod
    def StartNew(cls) -> Stopwatch:
        """

        :return:
        """
    def Stop(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class Switch(ABC, Object):
    """"""

    @property
    def Attributes(self) -> StringDictionary:
        """

        :return:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @property
    def DisplayName(self) -> str:
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

class SwitchAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, switchName: str, switchType: Type):
        """

        :param switchName:
        :param switchType:
        """
    @property
    def SwitchDescription(self) -> str:
        """

        :return:
        """
    @SwitchDescription.setter
    def SwitchDescription(self, value: str) -> None: ...
    @property
    def SwitchName(self) -> str:
        """

        :return:
        """
    @SwitchName.setter
    def SwitchName(self, value: str) -> None: ...
    @property
    def SwitchType(self) -> Type:
        """

        :return:
        """
    @SwitchType.setter
    def SwitchType(self, value: Type) -> None: ...
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
    @classmethod
    def GetAll(cls, assembly: Assembly) -> Array[SwitchAttribute]:
        """

        :param assembly:
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

class SwitchElement(ConfigurationElement):
    """"""

    def __init__(self):
        """"""
    @property
    def Attributes(self) -> Hashtable:
        """

        :return:
        """
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
        """

        :return:
        """
    @property
    def Value(self) -> str:
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
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SwitchElementsCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    """"""

    def __init__(self):
        """"""
    @property
    def CollectionType(self) -> ConfigurationElementCollectionType:
        """"""
    @property
    def Count(self) -> int:
        """

        :return:
        """
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
        """

        :return:
        """
    @property
    def Item(self) -> SwitchElement:
        """

        :return:
        """
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
        """

        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[ConfigurationElement], index: int) -> None:
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
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, name: str) -> SwitchElement:
        """

        :param name:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class SwitchLevelAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, switchLevelType: Type):
        """

        :param switchLevelType:
        """
    @property
    def SwitchLevelType(self) -> Type:
        """

        :return:
        """
    @SwitchLevelType.setter
    def SwitchLevelType(self, value: Type) -> None: ...
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

class SwitchesDictionarySectionHandler(DictionarySectionHandler, IConfigurationSectionHandler):
    """"""

    def __init__(self):
        """"""
    def Create(self, parent: object, configContext: object, section: XmlNode) -> object:
        """

        :param parent:
        :param configContext:
        :param section:
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

class SystemDiagnosticsSection(ConfigurationSection):
    """"""

    def __init__(self):
        """"""
    @property
    def Assert(self) -> AssertSection:
        """

        :return:
        """
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
        """

        :return:
        """
    @property
    def SectionInformation(self) -> SectionInformation:
        """"""
    @property
    def SharedListeners(self) -> ListenerElementsCollection:
        """

        :return:
        """
    @property
    def Sources(self) -> SourceElementsCollection:
        """

        :return:
        """
    @property
    def Switches(self) -> SwitchElementsCollection:
        """

        :return:
        """
    @property
    def Trace(self) -> TraceSection:
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
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class TextWriterTraceListener(TraceListener, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, stream: Stream):
        """

        :param stream:
        """
    @overload
    def __init__(self, writer: TextWriter):
        """

        :param writer:
        """
    @overload
    def __init__(self, fileName: str):
        """

        :param fileName:
        """
    @overload
    def __init__(self, stream: Stream, name: str):
        """

        :param stream:
        :param name:
        """
    @overload
    def __init__(self, writer: TextWriter, name: str):
        """

        :param writer:
        :param name:
        """
    @overload
    def __init__(self, fileName: str, name: str):
        """

        :param fileName:
        :param name:
        """
    @property
    def Attributes(self) -> StringDictionary:
        """

        :return:
        """
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
    @property
    def Writer(self) -> TextWriter:
        """

        :return:
        """
    @Writer.setter
    def Writer(self, value: TextWriter) -> None: ...
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

class ThreadInfo(Object):
    """"""

    basePriority: Final[int] = ...
    """
    
    :return: 
    """
    currentPriority: Final[int] = ...
    """
    
    :return: 
    """
    processId: Final[int] = ...
    """
    
    :return: 
    """
    startAddress: Final[IntPtr] = ...
    """
    
    :return: 
    """
    threadId: Final[int] = ...
    """
    
    :return: 
    """
    threadState: Final[ThreadState] = ...
    """
    
    :return: 
    """
    threadWaitReason: Final[ThreadWaitReason] = ...
    """
    
    :return: 
    """
    def __init__(self):
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

class Trace(Object):
    """"""

    @classmethod
    @property
    def AutoFlush(cls) -> bool:
        """

        :return:
        """
    @classmethod
    @AutoFlush.setter
    def AutoFlush(cls, value: bool) -> None: ...
    @classmethod
    @property
    def CorrelationManager(cls) -> CorrelationManager:
        """

        :return:
        """
    @classmethod
    @property
    def IndentLevel(cls) -> int:
        """

        :return:
        """
    @classmethod
    @IndentLevel.setter
    def IndentLevel(cls, value: int) -> None: ...
    @classmethod
    @property
    def IndentSize(cls) -> int:
        """

        :return:
        """
    @classmethod
    @IndentSize.setter
    def IndentSize(cls, value: int) -> None: ...
    @classmethod
    @property
    def Listeners(cls) -> TraceListenerCollection:
        """

        :return:
        """
    @classmethod
    @property
    def UseGlobalLock(cls) -> bool:
        """

        :return:
        """
    @classmethod
    @UseGlobalLock.setter
    def UseGlobalLock(cls, value: bool) -> None: ...
    @classmethod
    @overload
    def Assert(cls, condition: bool) -> None:
        """

        :param condition:
        """
    @classmethod
    @overload
    def Assert(cls, condition: bool, message: str) -> None:
        """

        :param condition:
        :param message:
        """
    @classmethod
    @overload
    def Assert(cls, condition: bool, message: str, detailMessage: str) -> None:
        """

        :param condition:
        :param message:
        :param detailMessage:
        """
    @classmethod
    def Close(cls) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def Fail(cls, message: str) -> None:
        """

        :param message:
        """
    @classmethod
    @overload
    def Fail(cls, message: str, detailMessage: str) -> None:
        """

        :param message:
        :param detailMessage:
        """
    @classmethod
    def Flush(cls) -> None:
        """"""
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def Indent(cls) -> None:
        """"""
    @classmethod
    def Refresh(cls) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    @overload
    def TraceError(cls, message: str) -> None:
        """

        :param message:
        """
    @classmethod
    @overload
    def TraceError(cls, format: str, args: Array[object]) -> None:
        """

        :param format:
        :param args:
        """
    @classmethod
    @overload
    def TraceInformation(cls, message: str) -> None:
        """

        :param message:
        """
    @classmethod
    @overload
    def TraceInformation(cls, format: str, args: Array[object]) -> None:
        """

        :param format:
        :param args:
        """
    @classmethod
    @overload
    def TraceWarning(cls, message: str) -> None:
        """

        :param message:
        """
    @classmethod
    @overload
    def TraceWarning(cls, format: str, args: Array[object]) -> None:
        """

        :param format:
        :param args:
        """
    @classmethod
    def Unindent(cls) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, value: object) -> None:
        """

        :param value:
        """
    @classmethod
    @overload
    def Write(cls, message: str) -> None:
        """

        :param message:
        """
    @classmethod
    @overload
    def Write(cls, value: object, category: str) -> None:
        """

        :param value:
        :param category:
        """
    @classmethod
    @overload
    def Write(cls, message: str, category: str) -> None:
        """

        :param message:
        :param category:
        """
    @classmethod
    @overload
    def WriteIf(cls, condition: bool, value: object) -> None:
        """

        :param condition:
        :param value:
        """
    @classmethod
    @overload
    def WriteIf(cls, condition: bool, message: str) -> None:
        """

        :param condition:
        :param message:
        """
    @classmethod
    @overload
    def WriteIf(cls, condition: bool, value: object, category: str) -> None:
        """

        :param condition:
        :param value:
        :param category:
        """
    @classmethod
    @overload
    def WriteIf(cls, condition: bool, message: str, category: str) -> None:
        """

        :param condition:
        :param message:
        :param category:
        """
    @classmethod
    @overload
    def WriteLine(cls, value: object) -> None:
        """

        :param value:
        """
    @classmethod
    @overload
    def WriteLine(cls, message: str) -> None:
        """

        :param message:
        """
    @classmethod
    @overload
    def WriteLine(cls, value: object, category: str) -> None:
        """

        :param value:
        :param category:
        """
    @classmethod
    @overload
    def WriteLine(cls, message: str, category: str) -> None:
        """

        :param message:
        :param category:
        """
    @classmethod
    @overload
    def WriteLineIf(cls, condition: bool, value: object) -> None:
        """

        :param condition:
        :param value:
        """
    @classmethod
    @overload
    def WriteLineIf(cls, condition: bool, message: str) -> None:
        """

        :param condition:
        :param message:
        """
    @classmethod
    @overload
    def WriteLineIf(cls, condition: bool, value: object, category: str) -> None:
        """

        :param condition:
        :param value:
        :param category:
        """
    @classmethod
    @overload
    def WriteLineIf(cls, condition: bool, message: str, category: str) -> None:
        """

        :param condition:
        :param message:
        :param category:
        """

class TraceEventCache(Object):
    """"""

    def __init__(self):
        """"""
    @property
    def Callstack(self) -> str:
        """

        :return:
        """
    @property
    def DateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def LogicalOperationStack(self) -> Stack:
        """

        :return:
        """
    @property
    def ProcessId(self) -> int:
        """

        :return:
        """
    @property
    def ThreadId(self) -> str:
        """

        :return:
        """
    @property
    def Timestamp(self) -> int:
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

class TraceFilter(ABC, Object):
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
        """

        :param cache:
        :param source:
        :param eventType:
        :param id:
        :param formatOrMessage:
        :param args:
        :param data1:
        :param data:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class TraceInternal(ABC, Object):
    """"""

    @classmethod
    @property
    def AutoFlush(cls) -> bool:
        """

        :return:
        """
    @classmethod
    @AutoFlush.setter
    def AutoFlush(cls, value: bool) -> None: ...
    @classmethod
    @property
    def IndentLevel(cls) -> int:
        """

        :return:
        """
    @classmethod
    @IndentLevel.setter
    def IndentLevel(cls, value: int) -> None: ...
    @classmethod
    @property
    def IndentSize(cls) -> int:
        """

        :return:
        """
    @classmethod
    @IndentSize.setter
    def IndentSize(cls, value: int) -> None: ...
    @classmethod
    @property
    def Listeners(cls) -> TraceListenerCollection:
        """

        :return:
        """
    @classmethod
    @property
    def UseGlobalLock(cls) -> bool:
        """

        :return:
        """
    @classmethod
    @UseGlobalLock.setter
    def UseGlobalLock(cls, value: bool) -> None: ...
    @classmethod
    @overload
    def Assert(cls, condition: bool) -> None:
        """

        :param condition:
        """
    @classmethod
    @overload
    def Assert(cls, condition: bool, message: str) -> None:
        """

        :param condition:
        :param message:
        """
    @classmethod
    @overload
    def Assert(cls, condition: bool, message: str, detailMessage: str) -> None:
        """

        :param condition:
        :param message:
        :param detailMessage:
        """
    @classmethod
    def Close(cls) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def Fail(cls, message: str) -> None:
        """

        :param message:
        """
    @classmethod
    @overload
    def Fail(cls, message: str, detailMessage: str) -> None:
        """

        :param message:
        :param detailMessage:
        """
    @classmethod
    def Flush(cls) -> None:
        """"""
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def Indent(cls) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def TraceEvent(
        cls, eventType: TraceEventType, id: int, format: str, args: Array[object]
    ) -> None:
        """

        :param eventType:
        :param id:
        :param format:
        :param args:
        """
    @classmethod
    def Unindent(cls) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, value: object) -> None:
        """

        :param value:
        """
    @classmethod
    @overload
    def Write(cls, message: str) -> None:
        """

        :param message:
        """
    @classmethod
    @overload
    def Write(cls, value: object, category: str) -> None:
        """

        :param value:
        :param category:
        """
    @classmethod
    @overload
    def Write(cls, message: str, category: str) -> None:
        """

        :param message:
        :param category:
        """
    @classmethod
    @overload
    def WriteIf(cls, condition: bool, value: object) -> None:
        """

        :param condition:
        :param value:
        """
    @classmethod
    @overload
    def WriteIf(cls, condition: bool, message: str) -> None:
        """

        :param condition:
        :param message:
        """
    @classmethod
    @overload
    def WriteIf(cls, condition: bool, value: object, category: str) -> None:
        """

        :param condition:
        :param value:
        :param category:
        """
    @classmethod
    @overload
    def WriteIf(cls, condition: bool, message: str, category: str) -> None:
        """

        :param condition:
        :param message:
        :param category:
        """
    @classmethod
    @overload
    def WriteLine(cls, value: object) -> None:
        """

        :param value:
        """
    @classmethod
    @overload
    def WriteLine(cls, message: str) -> None:
        """

        :param message:
        """
    @classmethod
    @overload
    def WriteLine(cls, value: object, category: str) -> None:
        """

        :param value:
        :param category:
        """
    @classmethod
    @overload
    def WriteLine(cls, message: str, category: str) -> None:
        """

        :param message:
        :param category:
        """
    @classmethod
    @overload
    def WriteLineIf(cls, condition: bool, value: object) -> None:
        """

        :param condition:
        :param value:
        """
    @classmethod
    @overload
    def WriteLineIf(cls, condition: bool, message: str) -> None:
        """

        :param condition:
        :param message:
        """
    @classmethod
    @overload
    def WriteLineIf(cls, condition: bool, value: object, category: str) -> None:
        """

        :param condition:
        :param value:
        :param category:
        """
    @classmethod
    @overload
    def WriteLineIf(cls, condition: bool, message: str, category: str) -> None:
        """

        :param condition:
        :param message:
        :param category:
        """

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

class TraceListener(ABC, MarshalByRefObject, IDisposable):
    """"""

    @property
    def Attributes(self) -> StringDictionary:
        """

        :return:
        """
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

class TraceListenerCollection(Object, ICollection, IEnumerable, IList):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
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
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, listener: TraceListener) -> int:
        """

        :param listener:
        :return:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def AddRange(self, value: TraceListenerCollection) -> None:
        """

        :param value:
        """
    @overload
    def AddRange(self, value: Array[TraceListener]) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, listener: TraceListener) -> bool:
        """

        :param listener:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, listeners: Array[TraceListener], index: int) -> None:
        """

        :param listeners:
        :param index:
        """
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
    def IndexOf(self, listener: TraceListener) -> int:
        """

        :param listener:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, listener: TraceListener) -> None:
        """

        :param index:
        :param listener:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, listener: TraceListener) -> None:
        """

        :param listener:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    @overload
    def Remove(self, name: str) -> None:
        """

        :param name:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, name: str) -> TraceListener:
        """

        :param name:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, i: int, value: TraceListener) -> None:
        """

        :param i:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

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

class TraceSection(ConfigurationElement):
    """"""

    def __init__(self):
        """"""
    @property
    def AutoFlush(self) -> bool:
        """

        :return:
        """
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def IndentSize(self) -> int:
        """

        :return:
        """
    @property
    def Listeners(self) -> ListenerElementsCollection:
        """

        :return:
        """
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
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class TraceSource(Object):
    """"""

    @overload
    def __init__(self, name: str):
        """

        :param name:
        """
    @overload
    def __init__(self, name: str, defaultLevel: SourceLevels):
        """

        :param name:
        :param defaultLevel:
        """
    @property
    def Attributes(self) -> StringDictionary:
        """

        :return:
        """
    @property
    def Listeners(self) -> TraceListenerCollection:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Switch(self) -> SourceSwitch:
        """

        :return:
        """
    @Switch.setter
    def Switch(self, value: SourceSwitch) -> None: ...
    def Close(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
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
    @overload
    def TraceData(self, eventType: TraceEventType, id: int, data: Array[object]) -> None:
        """

        :param eventType:
        :param id:
        :param data:
        """
    @overload
    def TraceData(self, eventType: TraceEventType, id: int, data: object) -> None:
        """

        :param eventType:
        :param id:
        :param data:
        """
    @overload
    def TraceEvent(self, eventType: TraceEventType, id: int) -> None:
        """

        :param eventType:
        :param id:
        """
    @overload
    def TraceEvent(self, eventType: TraceEventType, id: int, message: str) -> None:
        """

        :param eventType:
        :param id:
        :param message:
        """
    @overload
    def TraceEvent(
        self, eventType: TraceEventType, id: int, format: str, args: Array[object]
    ) -> None:
        """

        :param eventType:
        :param id:
        :param format:
        :param args:
        """
    @overload
    def TraceInformation(self, message: str) -> None:
        """

        :param message:
        """
    @overload
    def TraceInformation(self, format: str, args: Array[object]) -> None:
        """

        :param format:
        :param args:
        """
    def TraceTransfer(self, id: int, message: str, relatedActivityId: Guid) -> None:
        """

        :param id:
        :param message:
        :param relatedActivityId:
        """

class TraceSwitch(Switch):
    """"""

    @overload
    def __init__(self, displayName: str, description: str):
        """

        :param displayName:
        :param description:
        """
    @overload
    def __init__(self, displayName: str, description: str, defaultSwitchValue: str):
        """

        :param displayName:
        :param description:
        :param defaultSwitchValue:
        """
    @property
    def Attributes(self) -> StringDictionary:
        """

        :return:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @property
    def DisplayName(self) -> str:
        """

        :return:
        """
    @property
    def Level(self) -> TraceLevel:
        """

        :return:
        """
    @Level.setter
    def Level(self, value: TraceLevel) -> None: ...
    @property
    def TraceError(self) -> bool:
        """

        :return:
        """
    @property
    def TraceInfo(self) -> bool:
        """

        :return:
        """
    @property
    def TraceVerbose(self) -> bool:
        """

        :return:
        """
    @property
    def TraceWarning(self) -> bool:
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

class TraceUtils(ABC, Object):
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

class TypedElement(ConfigurationElement):
    """"""

    def __init__(self, baseType: Type):
        """

        :param baseType:
        """
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def InitData(self) -> str:
        """

        :return:
        """
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
        """

        :return:
        """
    @TypeName.setter
    def TypeName(self, value: str) -> None: ...
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
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class UnescapedXmlDiagnosticData(Object):
    """"""

    def __init__(self, xmlPayload: str):
        """

        :param xmlPayload:
        """
    @property
    def UnescapedXml(self) -> str:
        """

        :return:
        """
    @UnescapedXml.setter
    def UnescapedXml(self, value: str) -> None: ...
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

UserCallBack: Callable[[str], None] = ...
"""

:param data: 
"""

class WinProcessManager(ABC, Object):
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
    def GetModuleInfos(cls, processId: int) -> Array[ModuleInfo]:
        """

        :param processId:
        :return:
        """
    @classmethod
    def GetProcessIds(cls) -> Array[int]:
        """

        :return:
        """
    @classmethod
    def GetProcessInfos(cls) -> Array[ProcessInfo]:
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

class XmlWriterTraceListener(TextWriterTraceListener, IDisposable):
    """"""

    @overload
    def __init__(self, stream: Stream):
        """

        :param stream:
        """
    @overload
    def __init__(self, writer: TextWriter):
        """

        :param writer:
        """
    @overload
    def __init__(self, filename: str):
        """

        :param filename:
        """
    @overload
    def __init__(self, stream: Stream, name: str):
        """

        :param stream:
        :param name:
        """
    @overload
    def __init__(self, writer: TextWriter, name: str):
        """

        :param writer:
        :param name:
        """
    @overload
    def __init__(self, filename: str, name: str):
        """

        :param filename:
        :param name:
        """
    @property
    def Attributes(self) -> StringDictionary:
        """

        :return:
        """
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
    @property
    def Writer(self) -> TextWriter:
        """

        :return:
        """
    @Writer.setter
    def Writer(self, value: TextWriter) -> None: ...
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
