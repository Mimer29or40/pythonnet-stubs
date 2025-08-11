"""Automatically generated stubs for C# namespace: System.Diagnostics.Eventing.Reader."""

from abc import ABC
from typing import Final
from typing import Self
from typing import overload

from Microsoft.Win32 import EvtRpcLogin
from Microsoft.Win32.SafeHandles import SafeWaitHandle
from System import Array
from System import Boolean
from System import DateTime
from System import Enum
from System import EventArgs
from System import EventHandler
from System import Exception
from System import Guid
from System import IDisposable
from System import Int32
from System import IntPtr
from System import Object
from System import TimeSpan
from System import Type
from System import Uri
from System.Collections import IDictionary
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IList
from System.Diagnostics import EventLogPermission
from System.Globalization import CultureInfo
from System.IO import SeekOrigin
from System.Reflection import MethodBase
from System.Runtime.InteropServices import SafeHandle
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Security import SecureString
from System.Security.Principal import SecurityIdentifier
from System.Text import StringBuilder

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CoTaskMemSafeHandle(SafeHandle, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    @classmethod
    @property
    def Zero(cls) -> CoTaskMemSafeHandle:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CoTaskMemUnicodeSafeHandle(SafeHandle, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    @classmethod
    @property
    def Zero(cls) -> CoTaskMemUnicodeSafeHandle:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventBookmark(Object, ISerializable):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventKeyword(Object):
    """"""
    @property
    def DisplayName(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Value(self) -> int:
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
class EventLevel(Object):
    """"""
    @property
    def DisplayName(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Value(self) -> int:
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
class EventLogConfiguration(Object, IDisposable):
    """"""
    @overload
    def __init__(self, logName: str) -> None:
        """"""
    @overload
    def __init__(self, logName: str, session: EventLogSession) -> None:
        """"""
    @property
    def IsClassicLog(self) -> bool:
        """"""
    @property
    def IsEnabled(self) -> bool:
        """"""
    @IsEnabled.setter
    def IsEnabled(self, value: bool) -> None: ...
    @property
    def LogFilePath(self) -> str:
        """"""
    @LogFilePath.setter
    def LogFilePath(self, value: str) -> None: ...
    @property
    def LogIsolation(self) -> EventLogIsolation:
        """"""
    @property
    def LogMode(self) -> EventLogMode:
        """"""
    @LogMode.setter
    def LogMode(self, value: EventLogMode) -> None: ...
    @property
    def LogName(self) -> str:
        """"""
    @property
    def LogType(self) -> EventLogType:
        """"""
    @property
    def MaximumSizeInBytes(self) -> int:
        """"""
    @MaximumSizeInBytes.setter
    def MaximumSizeInBytes(self, value: int) -> None: ...
    @property
    def OwningProviderName(self) -> str:
        """"""
    @property
    def ProviderBufferSize(self) -> int | None:
        """"""
    @property
    def ProviderControlGuid(self) -> Guid | None:
        """"""
    @property
    def ProviderKeywords(self) -> int | None:
        """"""
    @ProviderKeywords.setter
    def ProviderKeywords(self, value: int | None) -> None: ...
    @property
    def ProviderLatency(self) -> int | None:
        """"""
    @property
    def ProviderLevel(self) -> int | None:
        """"""
    @ProviderLevel.setter
    def ProviderLevel(self, value: int | None) -> None: ...
    @property
    def ProviderMaximumNumberOfBuffers(self) -> int | None:
        """"""
    @property
    def ProviderMinimumNumberOfBuffers(self) -> int | None:
        """"""
    @property
    def ProviderNames(self) -> IEnumerable[str]:
        """"""
    @property
    def SecurityDescriptor(self) -> str:
        """"""
    @SecurityDescriptor.setter
    def SecurityDescriptor(self, value: str) -> None: ...
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SaveChanges(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventLogException(Exception, _Exception, ISerializable):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventLogHandle(SafeHandle, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    @classmethod
    @property
    def Zero(cls) -> EventLogHandle:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventLogInformation(Object):
    """"""
    @property
    def Attributes(self) -> int | None:
        """"""
    @property
    def CreationTime(self) -> DateTime | None:
        """"""
    @property
    def FileSize(self) -> int | None:
        """"""
    @property
    def IsLogFull(self) -> bool | None:
        """"""
    @property
    def LastAccessTime(self) -> DateTime | None:
        """"""
    @property
    def LastWriteTime(self) -> DateTime | None:
        """"""
    @property
    def OldestRecordNumber(self) -> int | None:
        """"""
    @property
    def RecordCount(self) -> int | None:
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
class EventLogInvalidDataException(EventLogException, _Exception, ISerializable):
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class EventLogIsolation(Enum):
    """"""

    Application: EventLogIsolation = ...
    """"""
    System: EventLogIsolation = ...
    """"""
    Custom: EventLogIsolation = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventLogLink(Object):
    """"""
    @property
    def DisplayName(self) -> str:
        """"""
    @property
    def IsImported(self) -> bool:
        """"""
    @property
    def LogName(self) -> str:
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
class EventLogMode(Enum):
    """"""

    Circular: EventLogMode = ...
    """"""
    AutoBackup: EventLogMode = ...
    """"""
    Retain: EventLogMode = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventLogNotFoundException(EventLogException, _Exception, ISerializable):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventLogPermissionHolder(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetEventLogPermission(cls) -> EventLogPermission:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventLogPropertySelector(Object, IDisposable):
    """"""
    def __init__(self, propertyQueries: IEnumerable[str]) -> None:
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
class EventLogProviderDisabledException(EventLogException, _Exception, ISerializable):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventLogQuery(Object):
    """"""
    @overload
    def __init__(self, path: str, pathType: PathType) -> None:
        """"""
    @overload
    def __init__(self, path: str, pathType: PathType, query: str) -> None:
        """"""
    @property
    def ReverseDirection(self) -> bool:
        """"""
    @ReverseDirection.setter
    def ReverseDirection(self, value: bool) -> None: ...
    @property
    def Session(self) -> EventLogSession:
        """"""
    @Session.setter
    def Session(self, value: EventLogSession) -> None: ...
    @property
    def TolerateQueryErrors(self) -> bool:
        """"""
    @TolerateQueryErrors.setter
    def TolerateQueryErrors(self, value: bool) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventLogReader(Object, IDisposable):
    """"""
    @overload
    def __init__(self, path: str) -> None:
        """"""
    @overload
    def __init__(self, path: str, pathType: PathType) -> None:
        """"""
    @overload
    def __init__(self, eventQuery: EventLogQuery) -> None:
        """"""
    @overload
    def __init__(self, eventQuery: EventLogQuery, bookmark: EventBookmark) -> None:
        """"""
    @property
    def BatchSize(self) -> int:
        """"""
    @BatchSize.setter
    def BatchSize(self, value: int) -> None: ...
    @property
    def LogStatus(self) -> IList[EventLogStatus]:
        """"""
    def CancelReading(self) -> None:
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
    def ReadEvent(self) -> EventRecord:
        """"""
    @overload
    def ReadEvent(self, timeout: TimeSpan) -> EventRecord:
        """"""
    @overload
    def Seek(self, bookmark: EventBookmark) -> None:
        """"""
    @overload
    def Seek(self, bookmark: EventBookmark, offset: int) -> None:
        """"""
    @overload
    def Seek(self, origin: SeekOrigin, offset: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventLogReadingException(EventLogException, _Exception, ISerializable):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventLogRecord(EventRecord, IDisposable):
    """"""
    @property
    def ActivityId(self) -> Guid | None:
        """"""
    @property
    def Bookmark(self) -> EventBookmark:
        """"""
    @property
    def ContainerLog(self) -> str:
        """"""
    @property
    def Id(self) -> int:
        """"""
    @property
    def Keywords(self) -> int | None:
        """"""
    @property
    def KeywordsDisplayNames(self) -> IEnumerable[str]:
        """"""
    @property
    def Level(self) -> int | None:
        """"""
    @property
    def LevelDisplayName(self) -> str:
        """"""
    @property
    def LogName(self) -> str:
        """"""
    @property
    def MachineName(self) -> str:
        """"""
    @property
    def MatchedQueryIds(self) -> IEnumerable[int]:
        """"""
    @property
    def Opcode(self) -> int | None:
        """"""
    @property
    def OpcodeDisplayName(self) -> str:
        """"""
    @property
    def ProcessId(self) -> int | None:
        """"""
    @property
    def Properties(self) -> IList[EventProperty]:
        """"""
    @property
    def ProviderId(self) -> Guid | None:
        """"""
    @property
    def ProviderName(self) -> str:
        """"""
    @property
    def Qualifiers(self) -> int | None:
        """"""
    @property
    def RecordId(self) -> int | None:
        """"""
    @property
    def RelatedActivityId(self) -> Guid | None:
        """"""
    @property
    def Task(self) -> int | None:
        """"""
    @property
    def TaskDisplayName(self) -> str:
        """"""
    @property
    def ThreadId(self) -> int | None:
        """"""
    @property
    def TimeCreated(self) -> DateTime | None:
        """"""
    @property
    def UserId(self) -> SecurityIdentifier:
        """"""
    @property
    def Version(self) -> int | None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def FormatDescription(self) -> str:
        """"""
    @overload
    def FormatDescription(self, values: IEnumerable[object]) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetPropertyValues(self, propertySelector: EventLogPropertySelector) -> IList[object]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventLogSession(Object, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, server: str) -> None:
        """"""
    @overload
    def __init__(
        self,
        server: str,
        domain: str,
        user: str,
        password: SecureString,
        logOnType: SessionAuthentication,
    ) -> None:
        """"""
    @classmethod
    @property
    def GlobalSession(cls) -> EventLogSession:
        """"""
    def CancelCurrentOperations(self) -> None:
        """"""
    @overload
    def ClearLog(self, logName: str) -> None:
        """"""
    @overload
    def ClearLog(self, logName: str, backupPath: str) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def ExportLog(self, path: str, pathType: PathType, query: str, targetFilePath: str) -> None:
        """"""
    @overload
    def ExportLog(
        self,
        path: str,
        pathType: PathType,
        query: str,
        targetFilePath: str,
        tolerateQueryErrors: bool,
    ) -> None:
        """"""
    @overload
    def ExportLogAndMessages(
        self, path: str, pathType: PathType, query: str, targetFilePath: str
    ) -> None:
        """"""
    @overload
    def ExportLogAndMessages(
        self,
        path: str,
        pathType: PathType,
        query: str,
        targetFilePath: str,
        tolerateQueryErrors: bool,
        targetCultureInfo: CultureInfo,
    ) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLogInformation(self, logName: str, pathType: PathType) -> EventLogInformation:
        """"""
    def GetLogNames(self) -> IEnumerable[str]:
        """"""
    def GetProviderNames(self) -> IEnumerable[str]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventLogStatus(Object):
    """"""
    @property
    def LogName(self) -> str:
        """"""
    @property
    def StatusCode(self) -> int:
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
class EventLogType(Enum):
    """"""

    Administrative: EventLogType = ...
    """"""
    Operational: EventLogType = ...
    """"""
    Analytical: EventLogType = ...
    """"""
    Debug: EventLogType = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventLogWatcher(Object, IDisposable):
    """"""
    @overload
    def __init__(self, path: str) -> None:
        """"""
    @overload
    def __init__(self, eventQuery: EventLogQuery) -> None:
        """"""
    @overload
    def __init__(self, eventQuery: EventLogQuery, bookmark: EventBookmark) -> None:
        """"""
    @overload
    def __init__(
        self, eventQuery: EventLogQuery, bookmark: EventBookmark, readExistingEvents: bool
    ) -> None:
        """"""
    @property
    def Enabled(self) -> bool:
        """"""
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
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
    EventRecordWritten: EventType[EventHandler[EventRecordWrittenEventArgs]] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventMetadata(Object):
    """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def Id(self) -> int:
        """"""
    @property
    def Keywords(self) -> IEnumerable[EventKeyword]:
        """"""
    @property
    def Level(self) -> EventLevel:
        """"""
    @property
    def LogLink(self) -> EventLogLink:
        """"""
    @property
    def Opcode(self) -> EventOpcode:
        """"""
    @property
    def Task(self) -> EventTask:
        """"""
    @property
    def Template(self) -> str:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventOpcode(Object):
    """"""
    @property
    def DisplayName(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Value(self) -> int:
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
class EventProperty(Object):
    """"""
    @property
    def Value(self) -> object:
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
class EventRecord(ABC, Object, IDisposable):
    """"""
    @property
    def ActivityId(self) -> Guid | None:
        """"""
    @property
    def Bookmark(self) -> EventBookmark:
        """"""
    @property
    def Id(self) -> int:
        """"""
    @property
    def Keywords(self) -> int | None:
        """"""
    @property
    def KeywordsDisplayNames(self) -> IEnumerable[str]:
        """"""
    @property
    def Level(self) -> int | None:
        """"""
    @property
    def LevelDisplayName(self) -> str:
        """"""
    @property
    def LogName(self) -> str:
        """"""
    @property
    def MachineName(self) -> str:
        """"""
    @property
    def Opcode(self) -> int | None:
        """"""
    @property
    def OpcodeDisplayName(self) -> str:
        """"""
    @property
    def ProcessId(self) -> int | None:
        """"""
    @property
    def Properties(self) -> IList[EventProperty]:
        """"""
    @property
    def ProviderId(self) -> Guid | None:
        """"""
    @property
    def ProviderName(self) -> str:
        """"""
    @property
    def Qualifiers(self) -> int | None:
        """"""
    @property
    def RecordId(self) -> int | None:
        """"""
    @property
    def RelatedActivityId(self) -> Guid | None:
        """"""
    @property
    def Task(self) -> int | None:
        """"""
    @property
    def TaskDisplayName(self) -> str:
        """"""
    @property
    def ThreadId(self) -> int | None:
        """"""
    @property
    def TimeCreated(self) -> DateTime | None:
        """"""
    @property
    def UserId(self) -> SecurityIdentifier:
        """"""
    @property
    def Version(self) -> int | None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def FormatDescription(self) -> str:
        """"""
    @overload
    def FormatDescription(self, values: IEnumerable[object]) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventRecordWrittenEventArgs(EventArgs):
    """"""
    @property
    def EventException(self) -> Exception:
        """"""
    @property
    def EventRecord(self) -> EventRecord:
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
class EventTask(Object):
    """"""
    @property
    def DisplayName(self) -> str:
        """"""
    @property
    def EventGuid(self) -> Guid:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Value(self) -> int:
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
class NativeWrapper(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @classmethod
    def ConvertToAnsiString(cls, val: UnsafeNativeMethods.EvtVariant) -> str:
        """"""
    @classmethod
    def ConvertToArray(cls, val: UnsafeNativeMethods.EvtVariant, objType: Type, size: int) -> Array:
        """"""
    @classmethod
    def ConvertToBoolArray(cls, val: UnsafeNativeMethods.EvtVariant) -> Array:
        """"""
    @classmethod
    def ConvertToFileTimeArray(cls, val: UnsafeNativeMethods.EvtVariant) -> Array:
        """"""
    @classmethod
    def ConvertToObject(
        cls, val: UnsafeNativeMethods.EvtVariant, desiredType: UnsafeNativeMethods.EvtVariantType
    ) -> object:
        """"""
    @classmethod
    def ConvertToSafeHandle(cls, val: UnsafeNativeMethods.EvtVariant) -> EventLogHandle:
        """"""
    @classmethod
    def ConvertToString(cls, val: UnsafeNativeMethods.EvtVariant) -> str:
        """"""
    @classmethod
    def ConvertToStringArray(cls, val: UnsafeNativeMethods.EvtVariant, ansi: bool) -> Array[str]:
        """"""
    @classmethod
    def ConvertToSysTimeArray(cls, val: UnsafeNativeMethods.EvtVariant) -> Array:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def EvtArchiveExportedLog(
        cls, session: EventLogHandle, logFilePath: str, locale: int, flags: int
    ) -> None:
        """"""
    @classmethod
    def EvtCancel(cls, handle: EventLogHandle) -> None:
        """"""
    @classmethod
    def EvtClearLog(
        cls, session: EventLogHandle, channelPath: str, targetFilePath: str, flags: int
    ) -> None:
        """"""
    @classmethod
    def EvtClose(cls, handle: IntPtr) -> None:
        """"""
    @classmethod
    def EvtCreateBookmark(cls, bookmarkXml: str) -> EventLogHandle:
        """"""
    @classmethod
    def EvtCreateRenderContext(
        cls,
        valuePathsCount: int,
        valuePaths: Array[str],
        flags: UnsafeNativeMethods.EvtRenderContextFlags,
    ) -> EventLogHandle:
        """"""
    @classmethod
    def EvtExportLog(
        cls, session: EventLogHandle, channelPath: str, query: str, targetFilePath: str, flags: int
    ) -> None:
        """"""
    @classmethod
    def EvtFormatMessage(cls, handle: EventLogHandle, msgId: int) -> str:
        """"""
    @classmethod
    def EvtFormatMessageFormatDescription(
        cls, handle: EventLogHandle, eventHandle: EventLogHandle, values: Array[str]
    ) -> str:
        """"""
    @classmethod
    def EvtFormatMessageRenderKeywords(
        cls,
        pmHandle: EventLogHandle,
        eventHandle: EventLogHandle,
        flag: UnsafeNativeMethods.EvtFormatMessageFlags,
    ) -> IEnumerable[str]:
        """"""
    @classmethod
    def EvtFormatMessageRenderName(
        cls,
        pmHandle: EventLogHandle,
        eventHandle: EventLogHandle,
        flag: UnsafeNativeMethods.EvtFormatMessageFlags,
    ) -> str:
        """"""
    @classmethod
    def EvtGetChannelConfigProperty(
        cls, handle: EventLogHandle, enumType: UnsafeNativeMethods.EvtChannelConfigPropertyId
    ) -> object:
        """"""
    @classmethod
    def EvtGetEventInfo(
        cls, handle: EventLogHandle, enumType: UnsafeNativeMethods.EvtEventPropertyId
    ) -> object:
        """"""
    @classmethod
    def EvtGetEventMetadataProperty(
        cls, handle: EventLogHandle, enumType: UnsafeNativeMethods.EvtEventMetadataPropertyId
    ) -> object:
        """"""
    @classmethod
    def EvtGetLogInfo(
        cls, handle: EventLogHandle, enumType: UnsafeNativeMethods.EvtLogPropertyId
    ) -> object:
        """"""
    @classmethod
    def EvtGetObjectArrayProperty(
        cls, objArrayHandle: EventLogHandle, index: int, thePropertyId: int
    ) -> object:
        """"""
    @classmethod
    def EvtGetObjectArraySize(cls, objectArray: EventLogHandle) -> int:
        """"""
    @classmethod
    def EvtGetPublisherMetadataProperty(
        cls,
        pmHandle: EventLogHandle,
        thePropertyId: UnsafeNativeMethods.EvtPublisherMetadataPropertyId,
    ) -> object:
        """"""
    @classmethod
    def EvtGetQueryInfo(
        cls, handle: EventLogHandle, enumType: UnsafeNativeMethods.EvtQueryPropertyId
    ) -> object:
        """"""
    @classmethod
    def EvtNext(
        cls,
        queryHandle: EventLogHandle,
        eventSize: int,
        events: Array[IntPtr],
        timeout: int,
        flags: int,
        returned: Int32,
    ) -> bool:
        """"""
    @classmethod
    def EvtNextChannelPath(cls, handle: EventLogHandle, finish: Boolean) -> str:
        """"""
    @classmethod
    def EvtNextEventMetadata(cls, eventMetadataEnum: EventLogHandle, flags: int) -> EventLogHandle:
        """"""
    @classmethod
    def EvtNextPublisherId(cls, handle: EventLogHandle, finish: Boolean) -> str:
        """"""
    @classmethod
    def EvtOpenChannelConfig(
        cls, session: EventLogHandle, channelPath: str, flags: int
    ) -> EventLogHandle:
        """"""
    @classmethod
    def EvtOpenChannelEnum(cls, session: EventLogHandle, flags: int) -> EventLogHandle:
        """"""
    @classmethod
    def EvtOpenEventMetadataEnum(
        cls, ProviderMetadata: EventLogHandle, flags: int
    ) -> EventLogHandle:
        """"""
    @classmethod
    def EvtOpenLog(cls, session: EventLogHandle, path: str, flags: PathType) -> EventLogHandle:
        """"""
    @classmethod
    def EvtOpenProviderEnum(cls, session: EventLogHandle, flags: int) -> EventLogHandle:
        """"""
    @classmethod
    def EvtOpenProviderMetadata(
        cls, session: EventLogHandle, ProviderId: str, logFilePath: str, locale: int, flags: int
    ) -> EventLogHandle:
        """"""
    @classmethod
    def EvtOpenSession(
        cls,
        loginClass: UnsafeNativeMethods.EvtLoginClass,
        login: EvtRpcLogin,
        timeout: int,
        flags: int,
    ) -> EventLogHandle:
        """"""
    @classmethod
    def EvtQuery(cls, session: EventLogHandle, path: str, query: str, flags: int) -> EventLogHandle:
        """"""
    @classmethod
    def EvtRender(
        cls,
        context: EventLogHandle,
        eventHandle: EventLogHandle,
        flags: UnsafeNativeMethods.EvtRenderFlags,
        buffer: StringBuilder,
    ) -> None:
        """"""
    @classmethod
    def EvtRenderBookmark(cls, eventHandle: EventLogHandle) -> str:
        """"""
    @classmethod
    def EvtRenderBufferWithContextSystem(
        cls,
        contextHandle: EventLogHandle,
        eventHandle: EventLogHandle,
        flag: UnsafeNativeMethods.EvtRenderFlags,
        systemProperties: NativeWrapper.SystemProperties,
        SYSTEM_PROPERTY_COUNT: int,
    ) -> None:
        """"""
    @classmethod
    def EvtRenderBufferWithContextUserOrValues(
        cls, contextHandle: EventLogHandle, eventHandle: EventLogHandle
    ) -> IList[object]:
        """"""
    @classmethod
    def EvtSaveChannelConfig(cls, channelConfig: EventLogHandle, flags: int) -> None:
        """"""
    @classmethod
    def EvtSeek(
        cls,
        resultSet: EventLogHandle,
        position: int,
        bookmark: EventLogHandle,
        timeout: int,
        flags: UnsafeNativeMethods.EvtSeekFlags,
    ) -> None:
        """"""
    @classmethod
    def EvtSetChannelConfigProperty(
        cls,
        handle: EventLogHandle,
        enumType: UnsafeNativeMethods.EvtChannelConfigPropertyId,
        val: object,
    ) -> None:
        """"""
    @classmethod
    def EvtSubscribe(
        cls,
        session: EventLogHandle,
        signalEvent: SafeWaitHandle,
        path: str,
        query: str,
        bookmark: EventLogHandle,
        context: IntPtr,
        callback: IntPtr,
        flags: int,
    ) -> EventLogHandle:
        """"""
    @classmethod
    def EvtUpdateBookmark(cls, bookmark: EventLogHandle, eventHandle: EventLogHandle) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class SystemProperties(Object):
        """"""

        ActivityId: Final[Guid | None]
        """"""
        ChannelName: Final[str]
        """"""
        ComputerName: Final[str]
        """"""
        Id: Final[int | None]
        """"""
        Keywords: Final[int | None]
        """"""
        Level: Final[int | None]
        """"""
        Opcode: Final[int | None]
        """"""
        ProcessId: Final[int | None]
        """"""
        ProviderId: Final[Guid | None]
        """"""
        ProviderName: Final[str]
        """"""
        Qualifiers: Final[int | None]
        """"""
        RecordId: Final[int | None]
        """"""
        RelatedActivityId: Final[Guid | None]
        """"""
        Task: Final[int | None]
        """"""
        ThreadId: Final[int | None]
        """"""
        TimeCreated: Final[DateTime | None]
        """"""
        UserId: Final[SecurityIdentifier]
        """"""
        Version: Final[int | None]
        """"""
        filled: Final[bool]
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
class PathType(Enum):
    """"""

    LogName: PathType = ...
    """"""
    FilePath: PathType = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ProviderMetadata(Object, IDisposable):
    """"""
    @overload
    def __init__(self, providerName: str) -> None:
        """"""
    @overload
    def __init__(
        self, providerName: str, session: EventLogSession, targetCultureInfo: CultureInfo
    ) -> None:
        """"""
    @property
    def DisplayName(self) -> str:
        """"""
    @property
    def Events(self) -> IEnumerable[EventMetadata]:
        """"""
    @property
    def HelpLink(self) -> Uri:
        """"""
    @property
    def Id(self) -> Guid:
        """"""
    @property
    def Keywords(self) -> IList[EventKeyword]:
        """"""
    @property
    def Levels(self) -> IList[EventLevel]:
        """"""
    @property
    def LogLinks(self) -> IList[EventLogLink]:
        """"""
    @property
    def MessageFilePath(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Opcodes(self) -> IList[EventOpcode]:
        """"""
    @property
    def ParameterFilePath(self) -> str:
        """"""
    @property
    def ResourceFilePath(self) -> str:
        """"""
    @property
    def Tasks(self) -> IList[EventTask]:
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
class ProviderMetadataCachedInformation(Object):
    """"""
    def __init__(self, session: EventLogSession, logfile: str, maximumCacheSize: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetFormatDescription(self, ProviderName: str, eventHandle: EventLogHandle) -> str:
        """"""
    @overload
    def GetFormatDescription(
        self, ProviderName: str, eventHandle: EventLogHandle, values: Array[str]
    ) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetKeywordDisplayNames(
        self, ProviderName: str, eventHandle: EventLogHandle
    ) -> IEnumerable[str]:
        """"""
    def GetLevelDisplayName(self, ProviderName: str, eventHandle: EventLogHandle) -> str:
        """"""
    def GetOpcodeDisplayName(self, ProviderName: str, eventHandle: EventLogHandle) -> str:
        """"""
    def GetTaskDisplayName(self, ProviderName: str, eventHandle: EventLogHandle) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class SessionAuthentication(Enum):
    """"""

    Default: SessionAuthentication = ...
    """"""
    Negotiate: SessionAuthentication = ...
    """"""
    Kerberos: SessionAuthentication = ...
    """"""
    Ntlm: SessionAuthentication = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class StandardEventKeywords(Enum):
    """"""

    _None: StandardEventKeywords = ...
    """"""
    ResponseTime: StandardEventKeywords = ...
    """"""
    WdiContext: StandardEventKeywords = ...
    """"""
    WdiDiagnostic: StandardEventKeywords = ...
    """"""
    Sqm: StandardEventKeywords = ...
    """"""
    CorrelationHint: StandardEventKeywords = ...
    """"""
    AuditFailure: StandardEventKeywords = ...
    """"""
    AuditSuccess: StandardEventKeywords = ...
    """"""
    CorrelationHint2: StandardEventKeywords = ...
    """"""
    EventLogClassic: StandardEventKeywords = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class StandardEventLevel(Enum):
    """"""

    LogAlways: StandardEventLevel = ...
    """"""
    Critical: StandardEventLevel = ...
    """"""
    Error: StandardEventLevel = ...
    """"""
    Warning: StandardEventLevel = ...
    """"""
    Informational: StandardEventLevel = ...
    """"""
    Verbose: StandardEventLevel = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class StandardEventOpcode(Enum):
    """"""

    Info: StandardEventOpcode = ...
    """"""
    Start: StandardEventOpcode = ...
    """"""
    Stop: StandardEventOpcode = ...
    """"""
    DataCollectionStart: StandardEventOpcode = ...
    """"""
    DataCollectionStop: StandardEventOpcode = ...
    """"""
    Extension: StandardEventOpcode = ...
    """"""
    Reply: StandardEventOpcode = ...
    """"""
    Resume: StandardEventOpcode = ...
    """"""
    Suspend: StandardEventOpcode = ...
    """"""
    Send: StandardEventOpcode = ...
    """"""
    Receive: StandardEventOpcode = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class StandardEventTask(Enum):
    """"""

    _None: StandardEventTask = ...
    """"""
