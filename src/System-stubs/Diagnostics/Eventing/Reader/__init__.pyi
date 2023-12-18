from __future__ import annotations

from abc import ABC
from typing import Generic
from typing import List
from typing import Optional
from typing import Tuple
from typing import TypeVar
from typing import Union
from typing import overload

from Microsoft.Win32 import UnsafeNativeMethods
from Microsoft.Win32.SafeHandles import SafeWaitHandle
from System import Array
from System import Boolean
from System import Byte
from System import DateTime
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
from System import String
from System import TimeSpan
from System import Type
from System import UInt16
from System import UInt32
from System import UInt64
from System import Uri
from System import Void
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IList
from System.Diagnostics import EventLogPermission
from System.Globalization import CultureInfo
from System.IO import SeekOrigin
from System.Runtime.InteropServices import SafeHandle
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Security import SecureString
from System.Security.Principal import SecurityIdentifier
from System.Text import StringBuilder

# ---------- Types ---------- #

T = TypeVar("T")

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
NullableType = Union[Optional, Nullable]
ObjectType = Object
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

class CoTaskMemSafeHandle(SafeHandle, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def IsInvalid(self) -> BooleanType: ...
    @staticmethod
    @property
    def Zero() -> CoTaskMemSafeHandle: ...

    # ---------- Methods ---------- #

    def get_IsInvalid(self) -> BooleanType: ...
    @staticmethod
    def get_Zero() -> CoTaskMemSafeHandle: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CoTaskMemUnicodeSafeHandle(SafeHandle, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def IsInvalid(self) -> BooleanType: ...
    @staticmethod
    @property
    def Zero() -> CoTaskMemUnicodeSafeHandle: ...

    # ---------- Methods ---------- #

    def get_IsInvalid(self) -> BooleanType: ...
    @staticmethod
    def get_Zero() -> CoTaskMemUnicodeSafeHandle: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EventBookmark(ObjectType, ISerializable):
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

class EventKeyword(ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def DisplayName(self) -> StringType: ...
    @property
    def Name(self) -> StringType: ...
    @property
    def Value(self) -> LongType: ...

    # ---------- Methods ---------- #

    def get_DisplayName(self) -> StringType: ...
    def get_Name(self) -> StringType: ...
    def get_Value(self) -> LongType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EventLevel(ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def DisplayName(self) -> StringType: ...
    @property
    def Name(self) -> StringType: ...
    @property
    def Value(self) -> IntType: ...

    # ---------- Methods ---------- #

    def get_DisplayName(self) -> StringType: ...
    def get_Name(self) -> StringType: ...
    def get_Value(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EventLogConfiguration(ObjectType, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, logName: StringType): ...
    @overload
    def __init__(self, logName: StringType, session: EventLogSession): ...

    # ---------- Properties ---------- #

    @property
    def IsClassicLog(self) -> BooleanType: ...
    @property
    def IsEnabled(self) -> BooleanType: ...
    @IsEnabled.setter
    def IsEnabled(self, value: BooleanType) -> None: ...
    @property
    def LogFilePath(self) -> StringType: ...
    @LogFilePath.setter
    def LogFilePath(self, value: StringType) -> None: ...
    @property
    def LogIsolation(self) -> EventLogIsolation: ...
    @property
    def LogMode(self) -> EventLogMode: ...
    @LogMode.setter
    def LogMode(self, value: EventLogMode) -> None: ...
    @property
    def LogName(self) -> StringType: ...
    @property
    def LogType(self) -> EventLogType: ...
    @property
    def MaximumSizeInBytes(self) -> LongType: ...
    @MaximumSizeInBytes.setter
    def MaximumSizeInBytes(self, value: LongType) -> None: ...
    @property
    def OwningProviderName(self) -> StringType: ...
    @property
    def ProviderBufferSize(self) -> NullableType[Nullable[IntType]]: ...
    @property
    def ProviderControlGuid(self) -> NullableType[Nullable[Guid]]: ...
    @property
    def ProviderKeywords(self) -> NullableType[Nullable[LongType]]: ...
    @ProviderKeywords.setter
    def ProviderKeywords(self, value: NullableType[Nullable[LongType]]) -> None: ...
    @property
    def ProviderLatency(self) -> NullableType[Nullable[IntType]]: ...
    @property
    def ProviderLevel(self) -> NullableType[Nullable[IntType]]: ...
    @ProviderLevel.setter
    def ProviderLevel(self, value: NullableType[Nullable[IntType]]) -> None: ...
    @property
    def ProviderMaximumNumberOfBuffers(self) -> NullableType[Nullable[IntType]]: ...
    @property
    def ProviderMinimumNumberOfBuffers(self) -> NullableType[Nullable[IntType]]: ...
    @property
    def ProviderNames(self) -> IEnumerable[StringType]: ...
    @property
    def SecurityDescriptor(self) -> StringType: ...
    @SecurityDescriptor.setter
    def SecurityDescriptor(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def Dispose(self) -> VoidType: ...
    def SaveChanges(self) -> VoidType: ...
    def get_IsClassicLog(self) -> BooleanType: ...
    def get_IsEnabled(self) -> BooleanType: ...
    def get_LogFilePath(self) -> StringType: ...
    def get_LogIsolation(self) -> EventLogIsolation: ...
    def get_LogMode(self) -> EventLogMode: ...
    def get_LogName(self) -> StringType: ...
    def get_LogType(self) -> EventLogType: ...
    def get_MaximumSizeInBytes(self) -> LongType: ...
    def get_OwningProviderName(self) -> StringType: ...
    def get_ProviderBufferSize(self) -> NullableType[Nullable[IntType]]: ...
    def get_ProviderControlGuid(self) -> NullableType[Nullable[Guid]]: ...
    def get_ProviderKeywords(self) -> NullableType[Nullable[LongType]]: ...
    def get_ProviderLatency(self) -> NullableType[Nullable[IntType]]: ...
    def get_ProviderLevel(self) -> NullableType[Nullable[IntType]]: ...
    def get_ProviderMaximumNumberOfBuffers(self) -> NullableType[Nullable[IntType]]: ...
    def get_ProviderMinimumNumberOfBuffers(self) -> NullableType[Nullable[IntType]]: ...
    def get_ProviderNames(self) -> IEnumerable[StringType]: ...
    def get_SecurityDescriptor(self) -> StringType: ...
    def set_IsEnabled(self, value: BooleanType) -> VoidType: ...
    def set_LogFilePath(self, value: StringType) -> VoidType: ...
    def set_LogMode(self, value: EventLogMode) -> VoidType: ...
    def set_MaximumSizeInBytes(self, value: LongType) -> VoidType: ...
    def set_ProviderKeywords(self, value: NullableType[Nullable[LongType]]) -> VoidType: ...
    def set_ProviderLevel(self, value: NullableType[Nullable[IntType]]) -> VoidType: ...
    def set_SecurityDescriptor(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EventLogException(Exception, ISerializable, _Exception):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: StringType): ...
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...

    # ---------- Properties ---------- #

    @property
    def Message(self) -> StringType: ...

    # ---------- Methods ---------- #

    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    def get_Message(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EventLogHandle(SafeHandle, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def IsInvalid(self) -> BooleanType: ...
    @staticmethod
    @property
    def Zero() -> EventLogHandle: ...

    # ---------- Methods ---------- #

    def get_IsInvalid(self) -> BooleanType: ...
    @staticmethod
    def get_Zero() -> EventLogHandle: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EventLogInformation(ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Attributes(self) -> NullableType[Nullable[IntType]]: ...
    @property
    def CreationTime(self) -> NullableType[Nullable[DateTime]]: ...
    @property
    def FileSize(self) -> NullableType[Nullable[LongType]]: ...
    @property
    def IsLogFull(self) -> NullableType[Nullable[BooleanType]]: ...
    @property
    def LastAccessTime(self) -> NullableType[Nullable[DateTime]]: ...
    @property
    def LastWriteTime(self) -> NullableType[Nullable[DateTime]]: ...
    @property
    def OldestRecordNumber(self) -> NullableType[Nullable[LongType]]: ...
    @property
    def RecordCount(self) -> NullableType[Nullable[LongType]]: ...

    # ---------- Methods ---------- #

    def get_Attributes(self) -> NullableType[Nullable[IntType]]: ...
    def get_CreationTime(self) -> NullableType[Nullable[DateTime]]: ...
    def get_FileSize(self) -> NullableType[Nullable[LongType]]: ...
    def get_IsLogFull(self) -> NullableType[Nullable[BooleanType]]: ...
    def get_LastAccessTime(self) -> NullableType[Nullable[DateTime]]: ...
    def get_LastWriteTime(self) -> NullableType[Nullable[DateTime]]: ...
    def get_OldestRecordNumber(self) -> NullableType[Nullable[LongType]]: ...
    def get_RecordCount(self) -> NullableType[Nullable[LongType]]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EventLogInvalidDataException(EventLogException, ISerializable, _Exception):
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

class EventLogLink(ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def DisplayName(self) -> StringType: ...
    @property
    def IsImported(self) -> BooleanType: ...
    @property
    def LogName(self) -> StringType: ...

    # ---------- Methods ---------- #

    def get_DisplayName(self) -> StringType: ...
    def get_IsImported(self) -> BooleanType: ...
    def get_LogName(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EventLogNotFoundException(EventLogException, ISerializable, _Exception):
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

class EventLogPermissionHolder(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    def GetEventLogPermission() -> EventLogPermission: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EventLogPropertySelector(ObjectType, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, propertyQueries: IEnumerable[StringType]): ...

    # No Properties

    # ---------- Methods ---------- #

    def Dispose(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EventLogProviderDisabledException(EventLogException, ISerializable, _Exception):
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

class EventLogQuery(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, path: StringType, pathType: PathType): ...
    @overload
    def __init__(self, path: StringType, pathType: PathType, query: StringType): ...

    # ---------- Properties ---------- #

    @property
    def ReverseDirection(self) -> BooleanType: ...
    @ReverseDirection.setter
    def ReverseDirection(self, value: BooleanType) -> None: ...
    @property
    def Session(self) -> EventLogSession: ...
    @Session.setter
    def Session(self, value: EventLogSession) -> None: ...
    @property
    def TolerateQueryErrors(self) -> BooleanType: ...
    @TolerateQueryErrors.setter
    def TolerateQueryErrors(self, value: BooleanType) -> None: ...

    # ---------- Methods ---------- #

    def get_ReverseDirection(self) -> BooleanType: ...
    def get_Session(self) -> EventLogSession: ...
    def get_TolerateQueryErrors(self) -> BooleanType: ...
    def set_ReverseDirection(self, value: BooleanType) -> VoidType: ...
    def set_Session(self, value: EventLogSession) -> VoidType: ...
    def set_TolerateQueryErrors(self, value: BooleanType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EventLogReader(ObjectType, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, path: StringType): ...
    @overload
    def __init__(self, path: StringType, pathType: PathType): ...
    @overload
    def __init__(self, eventQuery: EventLogQuery): ...
    @overload
    def __init__(self, eventQuery: EventLogQuery, bookmark: EventBookmark): ...

    # ---------- Properties ---------- #

    @property
    def BatchSize(self) -> IntType: ...
    @BatchSize.setter
    def BatchSize(self, value: IntType) -> None: ...
    @property
    def LogStatus(self) -> IList[EventLogStatus]: ...

    # ---------- Methods ---------- #

    def CancelReading(self) -> VoidType: ...
    def Dispose(self) -> VoidType: ...
    @overload
    def ReadEvent(self) -> EventRecord: ...
    @overload
    def ReadEvent(self, timeout: TimeSpan) -> EventRecord: ...
    @overload
    def Seek(self, bookmark: EventBookmark) -> VoidType: ...
    @overload
    def Seek(self, bookmark: EventBookmark, offset: LongType) -> VoidType: ...
    @overload
    def Seek(self, origin: SeekOrigin, offset: LongType) -> VoidType: ...
    def get_BatchSize(self) -> IntType: ...
    def get_LogStatus(self) -> IList[EventLogStatus]: ...
    def set_BatchSize(self, value: IntType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EventLogReadingException(EventLogException, ISerializable, _Exception):
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

class EventLogRecord(EventRecord, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def ActivityId(self) -> NullableType[Nullable[Guid]]: ...
    @property
    def Bookmark(self) -> EventBookmark: ...
    @property
    def ContainerLog(self) -> StringType: ...
    @property
    def Id(self) -> IntType: ...
    @property
    def Keywords(self) -> NullableType[Nullable[LongType]]: ...
    @property
    def KeywordsDisplayNames(self) -> IEnumerable[StringType]: ...
    @property
    def Level(self) -> NullableType[Nullable[ByteType]]: ...
    @property
    def LevelDisplayName(self) -> StringType: ...
    @property
    def LogName(self) -> StringType: ...
    @property
    def MachineName(self) -> StringType: ...
    @property
    def MatchedQueryIds(self) -> IEnumerable[IntType]: ...
    @property
    def Opcode(self) -> NullableType[Nullable[ShortType]]: ...
    @property
    def OpcodeDisplayName(self) -> StringType: ...
    @property
    def ProcessId(self) -> NullableType[Nullable[IntType]]: ...
    @property
    def Properties(self) -> IList[EventProperty]: ...
    @property
    def ProviderId(self) -> NullableType[Nullable[Guid]]: ...
    @property
    def ProviderName(self) -> StringType: ...
    @property
    def Qualifiers(self) -> NullableType[Nullable[IntType]]: ...
    @property
    def RecordId(self) -> NullableType[Nullable[LongType]]: ...
    @property
    def RelatedActivityId(self) -> NullableType[Nullable[Guid]]: ...
    @property
    def Task(self) -> NullableType[Nullable[IntType]]: ...
    @property
    def TaskDisplayName(self) -> StringType: ...
    @property
    def ThreadId(self) -> NullableType[Nullable[IntType]]: ...
    @property
    def TimeCreated(self) -> NullableType[Nullable[DateTime]]: ...
    @property
    def UserId(self) -> SecurityIdentifier: ...
    @property
    def Version(self) -> NullableType[Nullable[ByteType]]: ...

    # ---------- Methods ---------- #

    @overload
    def FormatDescription(self) -> StringType: ...
    @overload
    def FormatDescription(self, values: IEnumerable[ObjectType]) -> StringType: ...
    def GetPropertyValues(
        self, propertySelector: EventLogPropertySelector
    ) -> IList[ObjectType]: ...
    def ToXml(self) -> StringType: ...
    def get_ActivityId(self) -> NullableType[Nullable[Guid]]: ...
    def get_Bookmark(self) -> EventBookmark: ...
    def get_ContainerLog(self) -> StringType: ...
    def get_Id(self) -> IntType: ...
    def get_Keywords(self) -> NullableType[Nullable[LongType]]: ...
    def get_KeywordsDisplayNames(self) -> IEnumerable[StringType]: ...
    def get_Level(self) -> NullableType[Nullable[ByteType]]: ...
    def get_LevelDisplayName(self) -> StringType: ...
    def get_LogName(self) -> StringType: ...
    def get_MachineName(self) -> StringType: ...
    def get_MatchedQueryIds(self) -> IEnumerable[IntType]: ...
    def get_Opcode(self) -> NullableType[Nullable[ShortType]]: ...
    def get_OpcodeDisplayName(self) -> StringType: ...
    def get_ProcessId(self) -> NullableType[Nullable[IntType]]: ...
    def get_Properties(self) -> IList[EventProperty]: ...
    def get_ProviderId(self) -> NullableType[Nullable[Guid]]: ...
    def get_ProviderName(self) -> StringType: ...
    def get_Qualifiers(self) -> NullableType[Nullable[IntType]]: ...
    def get_RecordId(self) -> NullableType[Nullable[LongType]]: ...
    def get_RelatedActivityId(self) -> NullableType[Nullable[Guid]]: ...
    def get_Task(self) -> NullableType[Nullable[IntType]]: ...
    def get_TaskDisplayName(self) -> StringType: ...
    def get_ThreadId(self) -> NullableType[Nullable[IntType]]: ...
    def get_TimeCreated(self) -> NullableType[Nullable[DateTime]]: ...
    def get_UserId(self) -> SecurityIdentifier: ...
    def get_Version(self) -> NullableType[Nullable[ByteType]]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EventLogSession(ObjectType, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, server: StringType): ...
    @overload
    def __init__(
        self,
        server: StringType,
        domain: StringType,
        user: StringType,
        password: SecureString,
        logOnType: SessionAuthentication,
    ): ...

    # ---------- Properties ---------- #

    @staticmethod
    @property
    def GlobalSession() -> EventLogSession: ...

    # ---------- Methods ---------- #

    def CancelCurrentOperations(self) -> VoidType: ...
    @overload
    def ClearLog(self, logName: StringType) -> VoidType: ...
    @overload
    def ClearLog(self, logName: StringType, backupPath: StringType) -> VoidType: ...
    def Dispose(self) -> VoidType: ...
    @overload
    def ExportLog(
        self, path: StringType, pathType: PathType, query: StringType, targetFilePath: StringType
    ) -> VoidType: ...
    @overload
    def ExportLog(
        self,
        path: StringType,
        pathType: PathType,
        query: StringType,
        targetFilePath: StringType,
        tolerateQueryErrors: BooleanType,
    ) -> VoidType: ...
    @overload
    def ExportLogAndMessages(
        self, path: StringType, pathType: PathType, query: StringType, targetFilePath: StringType
    ) -> VoidType: ...
    @overload
    def ExportLogAndMessages(
        self,
        path: StringType,
        pathType: PathType,
        query: StringType,
        targetFilePath: StringType,
        tolerateQueryErrors: BooleanType,
        targetCultureInfo: CultureInfo,
    ) -> VoidType: ...
    def GetLogInformation(self, logName: StringType, pathType: PathType) -> EventLogInformation: ...
    def GetLogNames(self) -> IEnumerable[StringType]: ...
    def GetProviderNames(self) -> IEnumerable[StringType]: ...
    @staticmethod
    def get_GlobalSession() -> EventLogSession: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EventLogStatus(ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def LogName(self) -> StringType: ...
    @property
    def StatusCode(self) -> IntType: ...

    # ---------- Methods ---------- #

    def get_LogName(self) -> StringType: ...
    def get_StatusCode(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EventLogWatcher(ObjectType, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, path: StringType): ...
    @overload
    def __init__(self, eventQuery: EventLogQuery): ...
    @overload
    def __init__(self, eventQuery: EventLogQuery, bookmark: EventBookmark): ...
    @overload
    def __init__(
        self, eventQuery: EventLogQuery, bookmark: EventBookmark, readExistingEvents: BooleanType
    ): ...

    # ---------- Properties ---------- #

    @property
    def Enabled(self) -> BooleanType: ...
    @Enabled.setter
    def Enabled(self, value: BooleanType) -> None: ...

    # ---------- Methods ---------- #

    def Dispose(self) -> VoidType: ...
    def add_EventRecordWritten(
        self, value: EventHandler[EventRecordWrittenEventArgs]
    ) -> VoidType: ...
    def get_Enabled(self) -> BooleanType: ...
    def remove_EventRecordWritten(
        self, value: EventHandler[EventRecordWrittenEventArgs]
    ) -> VoidType: ...
    def set_Enabled(self, value: BooleanType) -> VoidType: ...

    # ---------- Events ---------- #

    EventRecordWritten: EventType[EventHandler[EventRecordWrittenEventArgs]] = ...

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EventMetadata(ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Description(self) -> StringType: ...
    @property
    def Id(self) -> LongType: ...
    @property
    def Keywords(self) -> IEnumerable[EventKeyword]: ...
    @property
    def Level(self) -> EventLevel: ...
    @property
    def LogLink(self) -> EventLogLink: ...
    @property
    def Opcode(self) -> EventOpcode: ...
    @property
    def Task(self) -> EventTask: ...
    @property
    def Template(self) -> StringType: ...
    @property
    def Version(self) -> ByteType: ...

    # ---------- Methods ---------- #

    def get_Description(self) -> StringType: ...
    def get_Id(self) -> LongType: ...
    def get_Keywords(self) -> IEnumerable[EventKeyword]: ...
    def get_Level(self) -> EventLevel: ...
    def get_LogLink(self) -> EventLogLink: ...
    def get_Opcode(self) -> EventOpcode: ...
    def get_Task(self) -> EventTask: ...
    def get_Template(self) -> StringType: ...
    def get_Version(self) -> ByteType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EventOpcode(ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def DisplayName(self) -> StringType: ...
    @property
    def Name(self) -> StringType: ...
    @property
    def Value(self) -> IntType: ...

    # ---------- Methods ---------- #

    def get_DisplayName(self) -> StringType: ...
    def get_Name(self) -> StringType: ...
    def get_Value(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EventProperty(ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Value(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def get_Value(self) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EventRecord(ABC, ObjectType, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def ActivityId(self) -> NullableType[Nullable[Guid]]: ...
    @property
    def Bookmark(self) -> EventBookmark: ...
    @property
    def Id(self) -> IntType: ...
    @property
    def Keywords(self) -> NullableType[Nullable[LongType]]: ...
    @property
    def KeywordsDisplayNames(self) -> IEnumerable[StringType]: ...
    @property
    def Level(self) -> NullableType[Nullable[ByteType]]: ...
    @property
    def LevelDisplayName(self) -> StringType: ...
    @property
    def LogName(self) -> StringType: ...
    @property
    def MachineName(self) -> StringType: ...
    @property
    def Opcode(self) -> NullableType[Nullable[ShortType]]: ...
    @property
    def OpcodeDisplayName(self) -> StringType: ...
    @property
    def ProcessId(self) -> NullableType[Nullable[IntType]]: ...
    @property
    def Properties(self) -> IList[EventProperty]: ...
    @property
    def ProviderId(self) -> NullableType[Nullable[Guid]]: ...
    @property
    def ProviderName(self) -> StringType: ...
    @property
    def Qualifiers(self) -> NullableType[Nullable[IntType]]: ...
    @property
    def RecordId(self) -> NullableType[Nullable[LongType]]: ...
    @property
    def RelatedActivityId(self) -> NullableType[Nullable[Guid]]: ...
    @property
    def Task(self) -> NullableType[Nullable[IntType]]: ...
    @property
    def TaskDisplayName(self) -> StringType: ...
    @property
    def ThreadId(self) -> NullableType[Nullable[IntType]]: ...
    @property
    def TimeCreated(self) -> NullableType[Nullable[DateTime]]: ...
    @property
    def UserId(self) -> SecurityIdentifier: ...
    @property
    def Version(self) -> NullableType[Nullable[ByteType]]: ...

    # ---------- Methods ---------- #

    def Dispose(self) -> VoidType: ...
    @overload
    def FormatDescription(self) -> StringType: ...
    @overload
    def FormatDescription(self, values: IEnumerable[ObjectType]) -> StringType: ...
    def ToXml(self) -> StringType: ...
    def get_ActivityId(self) -> NullableType[Nullable[Guid]]: ...
    def get_Bookmark(self) -> EventBookmark: ...
    def get_Id(self) -> IntType: ...
    def get_Keywords(self) -> NullableType[Nullable[LongType]]: ...
    def get_KeywordsDisplayNames(self) -> IEnumerable[StringType]: ...
    def get_Level(self) -> NullableType[Nullable[ByteType]]: ...
    def get_LevelDisplayName(self) -> StringType: ...
    def get_LogName(self) -> StringType: ...
    def get_MachineName(self) -> StringType: ...
    def get_Opcode(self) -> NullableType[Nullable[ShortType]]: ...
    def get_OpcodeDisplayName(self) -> StringType: ...
    def get_ProcessId(self) -> NullableType[Nullable[IntType]]: ...
    def get_Properties(self) -> IList[EventProperty]: ...
    def get_ProviderId(self) -> NullableType[Nullable[Guid]]: ...
    def get_ProviderName(self) -> StringType: ...
    def get_Qualifiers(self) -> NullableType[Nullable[IntType]]: ...
    def get_RecordId(self) -> NullableType[Nullable[LongType]]: ...
    def get_RelatedActivityId(self) -> NullableType[Nullable[Guid]]: ...
    def get_Task(self) -> NullableType[Nullable[IntType]]: ...
    def get_TaskDisplayName(self) -> StringType: ...
    def get_ThreadId(self) -> NullableType[Nullable[IntType]]: ...
    def get_TimeCreated(self) -> NullableType[Nullable[DateTime]]: ...
    def get_UserId(self) -> SecurityIdentifier: ...
    def get_Version(self) -> NullableType[Nullable[ByteType]]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EventRecordWrittenEventArgs(EventArgs):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def EventException(self) -> Exception: ...
    @property
    def EventRecord(self) -> EventRecord: ...

    # ---------- Methods ---------- #

    def get_EventException(self) -> Exception: ...
    def get_EventRecord(self) -> EventRecord: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EventTask(ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def DisplayName(self) -> StringType: ...
    @property
    def EventGuid(self) -> Guid: ...
    @property
    def Name(self) -> StringType: ...
    @property
    def Value(self) -> IntType: ...

    # ---------- Methods ---------- #

    def get_DisplayName(self) -> StringType: ...
    def get_EventGuid(self) -> Guid: ...
    def get_Name(self) -> StringType: ...
    def get_Value(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class NativeWrapper(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    def ConvertToAnsiString(val: EvtVariant) -> StringType: ...
    @staticmethod
    def ConvertToArray(val: EvtVariant, objType: TypeType, size: IntType) -> Array: ...
    @staticmethod
    def ConvertToBoolArray(val: EvtVariant) -> Array: ...
    @staticmethod
    def ConvertToFileTimeArray(val: EvtVariant) -> Array: ...
    @staticmethod
    def ConvertToObject(val: EvtVariant, desiredType: EvtVariantType) -> ObjectType: ...
    @staticmethod
    def ConvertToSafeHandle(val: EvtVariant) -> EventLogHandle: ...
    @staticmethod
    def ConvertToString(val: EvtVariant) -> StringType: ...
    @staticmethod
    def ConvertToStringArray(val: EvtVariant, ansi: BooleanType) -> ArrayType[StringType]: ...
    @staticmethod
    def ConvertToSysTimeArray(val: EvtVariant) -> Array: ...
    @staticmethod
    def EvtArchiveExportedLog(
        session: EventLogHandle, logFilePath: StringType, locale: IntType, flags: IntType
    ) -> VoidType: ...
    @staticmethod
    def EvtCancel(handle: EventLogHandle) -> VoidType: ...
    @staticmethod
    def EvtClearLog(
        session: EventLogHandle, channelPath: StringType, targetFilePath: StringType, flags: IntType
    ) -> VoidType: ...
    @staticmethod
    def EvtClose(handle: NIntType) -> VoidType: ...
    @staticmethod
    def EvtCreateBookmark(bookmarkXml: StringType) -> EventLogHandle: ...
    @staticmethod
    def EvtCreateRenderContext(
        valuePathsCount: IntType, valuePaths: ArrayType[StringType], flags: EvtRenderContextFlags
    ) -> EventLogHandle: ...
    @staticmethod
    def EvtExportLog(
        session: EventLogHandle,
        channelPath: StringType,
        query: StringType,
        targetFilePath: StringType,
        flags: IntType,
    ) -> VoidType: ...
    @staticmethod
    def EvtFormatMessage(handle: EventLogHandle, msgId: UIntType) -> StringType: ...
    @staticmethod
    def EvtFormatMessageFormatDescription(
        handle: EventLogHandle, eventHandle: EventLogHandle, values: ArrayType[StringType]
    ) -> StringType: ...
    @staticmethod
    def EvtFormatMessageRenderKeywords(
        pmHandle: EventLogHandle, eventHandle: EventLogHandle, flag: EvtFormatMessageFlags
    ) -> IEnumerable[StringType]: ...
    @staticmethod
    def EvtFormatMessageRenderName(
        pmHandle: EventLogHandle, eventHandle: EventLogHandle, flag: EvtFormatMessageFlags
    ) -> StringType: ...
    @staticmethod
    def EvtGetChannelConfigProperty(
        handle: EventLogHandle, enumType: EvtChannelConfigPropertyId
    ) -> ObjectType: ...
    @staticmethod
    def EvtGetEventInfo(handle: EventLogHandle, enumType: EvtEventPropertyId) -> ObjectType: ...
    @staticmethod
    def EvtGetEventMetadataProperty(
        handle: EventLogHandle, enumType: EvtEventMetadataPropertyId
    ) -> ObjectType: ...
    @staticmethod
    def EvtGetLogInfo(handle: EventLogHandle, enumType: EvtLogPropertyId) -> ObjectType: ...
    @staticmethod
    def EvtGetObjectArrayProperty(
        objArrayHandle: EventLogHandle, index: IntType, thePropertyId: IntType
    ) -> ObjectType: ...
    @staticmethod
    def EvtGetObjectArraySize(objectArray: EventLogHandle) -> IntType: ...
    @staticmethod
    def EvtGetPublisherMetadataProperty(
        pmHandle: EventLogHandle, thePropertyId: EvtPublisherMetadataPropertyId
    ) -> ObjectType: ...
    @staticmethod
    def EvtGetQueryInfo(handle: EventLogHandle, enumType: EvtQueryPropertyId) -> ObjectType: ...
    @staticmethod
    def EvtNext(
        queryHandle: EventLogHandle,
        eventSize: IntType,
        events: ArrayType[NIntType],
        timeout: IntType,
        flags: IntType,
        returned: IntType,
    ) -> Tuple[BooleanType, IntType]: ...
    @staticmethod
    def EvtNextChannelPath(
        handle: EventLogHandle, finish: BooleanType
    ) -> Tuple[StringType, BooleanType]: ...
    @staticmethod
    def EvtNextEventMetadata(
        eventMetadataEnum: EventLogHandle, flags: IntType
    ) -> EventLogHandle: ...
    @staticmethod
    def EvtNextPublisherId(
        handle: EventLogHandle, finish: BooleanType
    ) -> Tuple[StringType, BooleanType]: ...
    @staticmethod
    def EvtOpenChannelConfig(
        session: EventLogHandle, channelPath: StringType, flags: IntType
    ) -> EventLogHandle: ...
    @staticmethod
    def EvtOpenChannelEnum(session: EventLogHandle, flags: IntType) -> EventLogHandle: ...
    @staticmethod
    def EvtOpenEventMetadataEnum(
        ProviderMetadata: EventLogHandle, flags: IntType
    ) -> EventLogHandle: ...
    @staticmethod
    def EvtOpenLog(
        session: EventLogHandle, path: StringType, flags: PathType
    ) -> EventLogHandle: ...
    @staticmethod
    def EvtOpenProviderEnum(session: EventLogHandle, flags: IntType) -> EventLogHandle: ...
    @staticmethod
    def EvtOpenProviderMetadata(
        session: EventLogHandle,
        ProviderId: StringType,
        logFilePath: StringType,
        locale: IntType,
        flags: IntType,
    ) -> EventLogHandle: ...
    @staticmethod
    def EvtOpenSession(
        loginClass: EvtLoginClass, login: EvtRpcLogin, timeout: IntType, flags: IntType
    ) -> Tuple[EventLogHandle, EvtRpcLogin]: ...
    @staticmethod
    def EvtQuery(
        session: EventLogHandle, path: StringType, query: StringType, flags: IntType
    ) -> EventLogHandle: ...
    @staticmethod
    def EvtRender(
        context: EventLogHandle,
        eventHandle: EventLogHandle,
        flags: EvtRenderFlags,
        buffer: StringBuilder,
    ) -> VoidType: ...
    @staticmethod
    def EvtRenderBookmark(eventHandle: EventLogHandle) -> StringType: ...
    @staticmethod
    def EvtRenderBufferWithContextSystem(
        contextHandle: EventLogHandle,
        eventHandle: EventLogHandle,
        flag: EvtRenderFlags,
        systemProperties: SystemProperties,
        SYSTEM_PROPERTY_COUNT: IntType,
    ) -> VoidType: ...
    @staticmethod
    def EvtRenderBufferWithContextUserOrValues(
        contextHandle: EventLogHandle, eventHandle: EventLogHandle
    ) -> IList[ObjectType]: ...
    @staticmethod
    def EvtSaveChannelConfig(channelConfig: EventLogHandle, flags: IntType) -> VoidType: ...
    @staticmethod
    def EvtSeek(
        resultSet: EventLogHandle,
        position: LongType,
        bookmark: EventLogHandle,
        timeout: IntType,
        flags: EvtSeekFlags,
    ) -> VoidType: ...
    @staticmethod
    def EvtSetChannelConfigProperty(
        handle: EventLogHandle, enumType: EvtChannelConfigPropertyId, val: ObjectType
    ) -> VoidType: ...
    @staticmethod
    def EvtSubscribe(
        session: EventLogHandle,
        signalEvent: SafeWaitHandle,
        path: StringType,
        query: StringType,
        bookmark: EventLogHandle,
        context: NIntType,
        callback: NIntType,
        flags: IntType,
    ) -> EventLogHandle: ...
    @staticmethod
    def EvtUpdateBookmark(bookmark: EventLogHandle, eventHandle: EventLogHandle) -> VoidType: ...

    # No Events

    # ---------- Sub Classes ---------- #

    class SystemProperties(ObjectType):
        # ---------- Fields ---------- #

        @property
        def ActivityId(self) -> NullableType[Nullable[Guid]]: ...
        @ActivityId.setter
        def ActivityId(self, value: NullableType[Nullable[Guid]]) -> None: ...
        @property
        def ChannelName(self) -> StringType: ...
        @ChannelName.setter
        def ChannelName(self, value: StringType) -> None: ...
        @property
        def ComputerName(self) -> StringType: ...
        @ComputerName.setter
        def ComputerName(self, value: StringType) -> None: ...
        @property
        def Id(self) -> NullableType[Nullable[UShortType]]: ...
        @Id.setter
        def Id(self, value: NullableType[Nullable[UShortType]]) -> None: ...
        @property
        def Keywords(self) -> NullableType[Nullable[ULongType]]: ...
        @Keywords.setter
        def Keywords(self, value: NullableType[Nullable[ULongType]]) -> None: ...
        @property
        def Level(self) -> NullableType[Nullable[ByteType]]: ...
        @Level.setter
        def Level(self, value: NullableType[Nullable[ByteType]]) -> None: ...
        @property
        def Opcode(self) -> NullableType[Nullable[ByteType]]: ...
        @Opcode.setter
        def Opcode(self, value: NullableType[Nullable[ByteType]]) -> None: ...
        @property
        def ProcessId(self) -> NullableType[Nullable[UIntType]]: ...
        @ProcessId.setter
        def ProcessId(self, value: NullableType[Nullable[UIntType]]) -> None: ...
        @property
        def ProviderId(self) -> NullableType[Nullable[Guid]]: ...
        @ProviderId.setter
        def ProviderId(self, value: NullableType[Nullable[Guid]]) -> None: ...
        @property
        def ProviderName(self) -> StringType: ...
        @ProviderName.setter
        def ProviderName(self, value: StringType) -> None: ...
        @property
        def Qualifiers(self) -> NullableType[Nullable[UShortType]]: ...
        @Qualifiers.setter
        def Qualifiers(self, value: NullableType[Nullable[UShortType]]) -> None: ...
        @property
        def RecordId(self) -> NullableType[Nullable[ULongType]]: ...
        @RecordId.setter
        def RecordId(self, value: NullableType[Nullable[ULongType]]) -> None: ...
        @property
        def RelatedActivityId(self) -> NullableType[Nullable[Guid]]: ...
        @RelatedActivityId.setter
        def RelatedActivityId(self, value: NullableType[Nullable[Guid]]) -> None: ...
        @property
        def Task(self) -> NullableType[Nullable[UShortType]]: ...
        @Task.setter
        def Task(self, value: NullableType[Nullable[UShortType]]) -> None: ...
        @property
        def ThreadId(self) -> NullableType[Nullable[UIntType]]: ...
        @ThreadId.setter
        def ThreadId(self, value: NullableType[Nullable[UIntType]]) -> None: ...
        @property
        def TimeCreated(self) -> NullableType[Nullable[DateTime]]: ...
        @TimeCreated.setter
        def TimeCreated(self, value: NullableType[Nullable[DateTime]]) -> None: ...
        @property
        def UserId(self) -> SecurityIdentifier: ...
        @UserId.setter
        def UserId(self, value: SecurityIdentifier) -> None: ...
        @property
        def Version(self) -> NullableType[Nullable[ByteType]]: ...
        @Version.setter
        def Version(self, value: NullableType[Nullable[ByteType]]) -> None: ...
        @property
        def filled(self) -> BooleanType: ...
        @filled.setter
        def filled(self, value: BooleanType) -> None: ...

        # ---------- Constructors ---------- #

        def __init__(self): ...

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

class ProviderMetadata(ObjectType, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, providerName: StringType): ...
    @overload
    def __init__(
        self, providerName: StringType, session: EventLogSession, targetCultureInfo: CultureInfo
    ): ...

    # ---------- Properties ---------- #

    @property
    def DisplayName(self) -> StringType: ...
    @property
    def Events(self) -> IEnumerable[EventMetadata]: ...
    @property
    def HelpLink(self) -> Uri: ...
    @property
    def Id(self) -> Guid: ...
    @property
    def Keywords(self) -> IList[EventKeyword]: ...
    @property
    def Levels(self) -> IList[EventLevel]: ...
    @property
    def LogLinks(self) -> IList[EventLogLink]: ...
    @property
    def MessageFilePath(self) -> StringType: ...
    @property
    def Name(self) -> StringType: ...
    @property
    def Opcodes(self) -> IList[EventOpcode]: ...
    @property
    def ParameterFilePath(self) -> StringType: ...
    @property
    def ResourceFilePath(self) -> StringType: ...
    @property
    def Tasks(self) -> IList[EventTask]: ...

    # ---------- Methods ---------- #

    def Dispose(self) -> VoidType: ...
    def get_DisplayName(self) -> StringType: ...
    def get_Events(self) -> IEnumerable[EventMetadata]: ...
    def get_HelpLink(self) -> Uri: ...
    def get_Id(self) -> Guid: ...
    def get_Keywords(self) -> IList[EventKeyword]: ...
    def get_Levels(self) -> IList[EventLevel]: ...
    def get_LogLinks(self) -> IList[EventLogLink]: ...
    def get_MessageFilePath(self) -> StringType: ...
    def get_Name(self) -> StringType: ...
    def get_Opcodes(self) -> IList[EventOpcode]: ...
    def get_ParameterFilePath(self) -> StringType: ...
    def get_ResourceFilePath(self) -> StringType: ...
    def get_Tasks(self) -> IList[EventTask]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ProviderMetadataCachedInformation(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self, session: EventLogSession, logfile: StringType, maximumCacheSize: IntType
    ): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def GetFormatDescription(
        self, ProviderName: StringType, eventHandle: EventLogHandle
    ) -> StringType: ...
    @overload
    def GetFormatDescription(
        self, ProviderName: StringType, eventHandle: EventLogHandle, values: ArrayType[StringType]
    ) -> StringType: ...
    def GetKeywordDisplayNames(
        self, ProviderName: StringType, eventHandle: EventLogHandle
    ) -> IEnumerable[StringType]: ...
    def GetLevelDisplayName(
        self, ProviderName: StringType, eventHandle: EventLogHandle
    ) -> StringType: ...
    def GetOpcodeDisplayName(
        self, ProviderName: StringType, eventHandle: EventLogHandle
    ) -> StringType: ...
    def GetTaskDisplayName(
        self, ProviderName: StringType, eventHandle: EventLogHandle
    ) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# No Structs

# No Interfaces

# ---------- Enums ---------- #

class EventLogIsolation(Enum):
    Application = 0
    System = 1
    Custom = 2

class EventLogMode(Enum):
    Circular = 0
    AutoBackup = 1
    Retain = 2

class EventLogType(Enum):
    Administrative = 0
    Operational = 1
    Analytical = 2
    Debug = 3

class PathType(Enum):
    LogName = 1
    FilePath = 2

class SessionAuthentication(Enum):
    Default = 0
    Negotiate = 1
    Kerberos = 2
    Ntlm = 3

class StandardEventKeywords(Enum):
    # None = 0
    ResponseTime = 281474976710656
    WdiContext = 562949953421312
    WdiDiagnostic = 1125899906842624
    Sqm = 2251799813685248
    CorrelationHint = 4503599627370496
    AuditFailure = 4503599627370496
    AuditSuccess = 9007199254740992
    CorrelationHint2 = 18014398509481984
    EventLogClassic = 36028797018963968

class StandardEventLevel(Enum):
    LogAlways = 0
    Critical = 1
    Error = 2
    Warning = 3
    Informational = 4
    Verbose = 5

class StandardEventOpcode(Enum):
    Info = 0
    Start = 1
    Stop = 2
    DataCollectionStart = 3
    DataCollectionStop = 4
    Extension = 5
    Reply = 6
    Resume = 7
    Suspend = 8
    Send = 9
    Receive = 240

class StandardEventTask(Enum):
    # None = 0
    pass

# No Delegates

__all__ = [
    CoTaskMemSafeHandle,
    CoTaskMemUnicodeSafeHandle,
    EventBookmark,
    EventKeyword,
    EventLevel,
    EventLogConfiguration,
    EventLogException,
    EventLogHandle,
    EventLogInformation,
    EventLogInvalidDataException,
    EventLogLink,
    EventLogNotFoundException,
    EventLogPermissionHolder,
    EventLogPropertySelector,
    EventLogProviderDisabledException,
    EventLogQuery,
    EventLogReader,
    EventLogReadingException,
    EventLogRecord,
    EventLogSession,
    EventLogStatus,
    EventLogWatcher,
    EventMetadata,
    EventOpcode,
    EventProperty,
    EventRecord,
    EventRecordWrittenEventArgs,
    EventTask,
    NativeWrapper,
    ProviderMetadata,
    ProviderMetadataCachedInformation,
    EventLogIsolation,
    EventLogMode,
    EventLogType,
    PathType,
    SessionAuthentication,
    StandardEventKeywords,
    StandardEventLevel,
    StandardEventOpcode,
    StandardEventTask,
]
