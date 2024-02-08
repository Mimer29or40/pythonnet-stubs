from __future__ import annotations

from abc import ABC
from typing import Final
from typing import Generic
from typing import Optional
from typing import TypeVar
from typing import overload

from Microsoft.Win32 import EvtRpcLogin
from Microsoft.Win32.SafeHandles import SafeWaitHandle
from Microsoft.Win32.UnsafeNativeMethods import EvtChannelConfigPropertyId
from Microsoft.Win32.UnsafeNativeMethods import EvtEventMetadataPropertyId
from Microsoft.Win32.UnsafeNativeMethods import EvtEventPropertyId
from Microsoft.Win32.UnsafeNativeMethods import EvtFormatMessageFlags
from Microsoft.Win32.UnsafeNativeMethods import EvtLoginClass
from Microsoft.Win32.UnsafeNativeMethods import EvtLogPropertyId
from Microsoft.Win32.UnsafeNativeMethods import EvtPublisherMetadataPropertyId
from Microsoft.Win32.UnsafeNativeMethods import EvtQueryPropertyId
from Microsoft.Win32.UnsafeNativeMethods import EvtRenderContextFlags
from Microsoft.Win32.UnsafeNativeMethods import EvtRenderFlags
from Microsoft.Win32.UnsafeNativeMethods import EvtSeekFlags
from Microsoft.Win32.UnsafeNativeMethods import EvtVariant
from Microsoft.Win32.UnsafeNativeMethods import EvtVariantType
from System import Array
from System import DateTime
from System import Enum
from System import EventArgs
from System import EventHandler
from System import Exception
from System import Guid
from System import IDisposable
from System import IntPtr
from System import Object
from System import TimeSpan
from System import Type
from System import Uri
from System.Collections import IDictionary
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IList
from System.Diagnostics import EventLogPermission
from System.Diagnostics.Eventing.Reader.NativeWrapper import SystemProperties
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

T = TypeVar("T")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class CoTaskMemSafeHandle(SafeHandle, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def Zero(cls) -> CoTaskMemSafeHandle:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class CoTaskMemUnicodeSafeHandle(SafeHandle, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def Zero(cls) -> CoTaskMemUnicodeSafeHandle:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class EventBookmark(Object, ISerializable):
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
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EventKeyword(Object):
    """"""

    @property
    def DisplayName(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Value(self) -> int:
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

class EventLevel(Object):
    """"""

    @property
    def DisplayName(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Value(self) -> int:
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

class EventLogConfiguration(Object, IDisposable):
    """"""

    @overload
    def __init__(self, logName: str):
        """

        :param logName:
        """
    @overload
    def __init__(self, logName: str, session: EventLogSession):
        """

        :param logName:
        :param session:
        """
    @property
    def IsClassicLog(self) -> bool:
        """

        :return:
        """
    @property
    def IsEnabled(self) -> bool:
        """

        :return:
        """
    @IsEnabled.setter
    def IsEnabled(self, value: bool) -> None: ...
    @property
    def LogFilePath(self) -> str:
        """

        :return:
        """
    @LogFilePath.setter
    def LogFilePath(self, value: str) -> None: ...
    @property
    def LogIsolation(self) -> EventLogIsolation:
        """

        :return:
        """
    @property
    def LogMode(self) -> EventLogMode:
        """

        :return:
        """
    @LogMode.setter
    def LogMode(self, value: EventLogMode) -> None: ...
    @property
    def LogName(self) -> str:
        """

        :return:
        """
    @property
    def LogType(self) -> EventLogType:
        """

        :return:
        """
    @property
    def MaximumSizeInBytes(self) -> int:
        """

        :return:
        """
    @MaximumSizeInBytes.setter
    def MaximumSizeInBytes(self, value: int) -> None: ...
    @property
    def OwningProviderName(self) -> str:
        """

        :return:
        """
    @property
    def ProviderBufferSize(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def ProviderControlGuid(self) -> Optional[Guid]:
        """

        :return:
        """
    @property
    def ProviderKeywords(self) -> Optional[int]:
        """

        :return:
        """
    @ProviderKeywords.setter
    def ProviderKeywords(self, value: Optional[int]) -> None: ...
    @property
    def ProviderLatency(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def ProviderLevel(self) -> Optional[int]:
        """

        :return:
        """
    @ProviderLevel.setter
    def ProviderLevel(self, value: Optional[int]) -> None: ...
    @property
    def ProviderMaximumNumberOfBuffers(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def ProviderMinimumNumberOfBuffers(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def ProviderNames(self) -> IEnumerable[str]:
        """

        :return:
        """
    @property
    def SecurityDescriptor(self) -> str:
        """

        :return:
        """
    @SecurityDescriptor.setter
    def SecurityDescriptor(self, value: str) -> None: ...
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
    def SaveChanges(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class EventLogException(Exception, _Exception, ISerializable):
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

class EventLogHandle(SafeHandle, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def Zero(cls) -> EventLogHandle:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class EventLogInformation(Object):
    """"""

    @property
    def Attributes(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def CreationTime(self) -> Optional[DateTime]:
        """

        :return:
        """
    @property
    def FileSize(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def IsLogFull(self) -> Optional[bool]:
        """

        :return:
        """
    @property
    def LastAccessTime(self) -> Optional[DateTime]:
        """

        :return:
        """
    @property
    def LastWriteTime(self) -> Optional[DateTime]:
        """

        :return:
        """
    @property
    def OldestRecordNumber(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def RecordCount(self) -> Optional[int]:
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

class EventLogInvalidDataException(EventLogException, _Exception, ISerializable):
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

class EventLogIsolation(Enum):
    """"""

    Application: EventLogIsolation = ...
    """"""
    System: EventLogIsolation = ...
    """"""
    Custom: EventLogIsolation = ...
    """"""

class EventLogLink(Object):
    """"""

    @property
    def DisplayName(self) -> str:
        """

        :return:
        """
    @property
    def IsImported(self) -> bool:
        """

        :return:
        """
    @property
    def LogName(self) -> str:
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

class EventLogMode(Enum):
    """"""

    Circular: EventLogMode = ...
    """"""
    AutoBackup: EventLogMode = ...
    """"""
    Retain: EventLogMode = ...
    """"""

class EventLogNotFoundException(EventLogException, _Exception, ISerializable):
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

class EventLogPermissionHolder(Object):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetEventLogPermission(cls) -> EventLogPermission:
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

class EventLogPropertySelector(Object, IDisposable):
    """"""

    def __init__(self, propertyQueries: IEnumerable[str]):
        """

        :param propertyQueries:
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
    def ToString(self) -> str:
        """

        :return:
        """

class EventLogProviderDisabledException(EventLogException, _Exception, ISerializable):
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

class EventLogQuery(Object):
    """"""

    @overload
    def __init__(self, path: str, pathType: PathType):
        """

        :param path:
        :param pathType:
        """
    @overload
    def __init__(self, path: str, pathType: PathType, query: str):
        """

        :param path:
        :param pathType:
        :param query:
        """
    @property
    def ReverseDirection(self) -> bool:
        """

        :return:
        """
    @ReverseDirection.setter
    def ReverseDirection(self, value: bool) -> None: ...
    @property
    def Session(self) -> EventLogSession:
        """

        :return:
        """
    @Session.setter
    def Session(self, value: EventLogSession) -> None: ...
    @property
    def TolerateQueryErrors(self) -> bool:
        """

        :return:
        """
    @TolerateQueryErrors.setter
    def TolerateQueryErrors(self, value: bool) -> None: ...
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

class EventLogReader(Object, IDisposable):
    """"""

    @overload
    def __init__(self, eventQuery: EventLogQuery):
        """

        :param eventQuery:
        """
    @overload
    def __init__(self, path: str):
        """

        :param path:
        """
    @overload
    def __init__(self, eventQuery: EventLogQuery, bookmark: EventBookmark):
        """

        :param eventQuery:
        :param bookmark:
        """
    @overload
    def __init__(self, path: str, pathType: PathType):
        """

        :param path:
        :param pathType:
        """
    @property
    def BatchSize(self) -> int:
        """

        :return:
        """
    @BatchSize.setter
    def BatchSize(self, value: int) -> None: ...
    @property
    def LogStatus(self) -> IList[EventLogStatus]:
        """

        :return:
        """
    def CancelReading(self) -> None:
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
    @overload
    def ReadEvent(self) -> EventRecord:
        """

        :return:
        """
    @overload
    def ReadEvent(self, timeout: TimeSpan) -> EventRecord:
        """

        :param timeout:
        :return:
        """
    @overload
    def Seek(self, bookmark: EventBookmark) -> None:
        """

        :param bookmark:
        """
    @overload
    def Seek(self, bookmark: EventBookmark, offset: int) -> None:
        """

        :param bookmark:
        :param offset:
        """
    @overload
    def Seek(self, origin: SeekOrigin, offset: int) -> None:
        """

        :param origin:
        :param offset:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EventLogReadingException(EventLogException, _Exception, ISerializable):
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

class EventLogRecord(EventRecord, IDisposable):
    """"""

    @property
    def ActivityId(self) -> Optional[Guid]:
        """

        :return:
        """
    @property
    def Bookmark(self) -> EventBookmark:
        """

        :return:
        """
    @property
    def ContainerLog(self) -> str:
        """

        :return:
        """
    @property
    def Id(self) -> int:
        """

        :return:
        """
    @property
    def Keywords(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def KeywordsDisplayNames(self) -> IEnumerable[str]:
        """

        :return:
        """
    @property
    def Level(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def LevelDisplayName(self) -> str:
        """

        :return:
        """
    @property
    def LogName(self) -> str:
        """

        :return:
        """
    @property
    def MachineName(self) -> str:
        """

        :return:
        """
    @property
    def MatchedQueryIds(self) -> IEnumerable[int]:
        """

        :return:
        """
    @property
    def Opcode(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def OpcodeDisplayName(self) -> str:
        """

        :return:
        """
    @property
    def ProcessId(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def Properties(self) -> IList[EventProperty]:
        """

        :return:
        """
    @property
    def ProviderId(self) -> Optional[Guid]:
        """

        :return:
        """
    @property
    def ProviderName(self) -> str:
        """

        :return:
        """
    @property
    def Qualifiers(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def RecordId(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def RelatedActivityId(self) -> Optional[Guid]:
        """

        :return:
        """
    @property
    def Task(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def TaskDisplayName(self) -> str:
        """

        :return:
        """
    @property
    def ThreadId(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def TimeCreated(self) -> Optional[DateTime]:
        """

        :return:
        """
    @property
    def UserId(self) -> SecurityIdentifier:
        """

        :return:
        """
    @property
    def Version(self) -> Optional[int]:
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
    @overload
    def FormatDescription(self) -> str:
        """

        :return:
        """
    @overload
    def FormatDescription(self, values: IEnumerable[object]) -> str:
        """

        :param values:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetPropertyValues(self, propertySelector: EventLogPropertySelector) -> IList[object]:
        """

        :param propertySelector:
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
    def ToXml(self) -> str:
        """

        :return:
        """

class EventLogSession(Object, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, server: str):
        """

        :param server:
        """
    @overload
    def __init__(
        self,
        server: str,
        domain: str,
        user: str,
        password: SecureString,
        logOnType: SessionAuthentication,
    ):
        """

        :param server:
        :param domain:
        :param user:
        :param password:
        :param logOnType:
        """
    @classmethod
    @property
    def GlobalSession(cls) -> EventLogSession:
        """

        :return:
        """
    def CancelCurrentOperations(self) -> None:
        """"""
    @overload
    def ClearLog(self, logName: str) -> None:
        """

        :param logName:
        """
    @overload
    def ClearLog(self, logName: str, backupPath: str) -> None:
        """

        :param logName:
        :param backupPath:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def ExportLog(self, path: str, pathType: PathType, query: str, targetFilePath: str) -> None:
        """

        :param path:
        :param pathType:
        :param query:
        :param targetFilePath:
        """
    @overload
    def ExportLog(
        self,
        path: str,
        pathType: PathType,
        query: str,
        targetFilePath: str,
        tolerateQueryErrors: bool,
    ) -> None:
        """

        :param path:
        :param pathType:
        :param query:
        :param targetFilePath:
        :param tolerateQueryErrors:
        """
    @overload
    def ExportLogAndMessages(
        self, path: str, pathType: PathType, query: str, targetFilePath: str
    ) -> None:
        """

        :param path:
        :param pathType:
        :param query:
        :param targetFilePath:
        """
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
        """

        :param path:
        :param pathType:
        :param query:
        :param targetFilePath:
        :param tolerateQueryErrors:
        :param targetCultureInfo:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLogInformation(self, logName: str, pathType: PathType) -> EventLogInformation:
        """

        :param logName:
        :param pathType:
        :return:
        """
    def GetLogNames(self) -> IEnumerable[str]:
        """

        :return:
        """
    def GetProviderNames(self) -> IEnumerable[str]:
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

class EventLogStatus(Object):
    """"""

    @property
    def LogName(self) -> str:
        """

        :return:
        """
    @property
    def StatusCode(self) -> int:
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

class EventLogWatcher(Object, IDisposable):
    """"""

    @overload
    def __init__(self, eventQuery: EventLogQuery):
        """

        :param eventQuery:
        """
    @overload
    def __init__(self, path: str):
        """

        :param path:
        """
    @overload
    def __init__(self, eventQuery: EventLogQuery, bookmark: EventBookmark):
        """

        :param eventQuery:
        :param bookmark:
        """
    @overload
    def __init__(
        self, eventQuery: EventLogQuery, bookmark: EventBookmark, readExistingEvents: bool
    ):
        """

        :param eventQuery:
        :param bookmark:
        :param readExistingEvents:
        """
    @property
    def Enabled(self) -> bool:
        """

        :return:
        """
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
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
    EventRecordWritten: EventType[EventHandler[EventRecordWrittenEventArgs]] = ...
    """"""

class EventMetadata(Object):
    """"""

    @property
    def Description(self) -> str:
        """

        :return:
        """
    @property
    def Id(self) -> int:
        """

        :return:
        """
    @property
    def Keywords(self) -> IEnumerable[EventKeyword]:
        """

        :return:
        """
    @property
    def Level(self) -> EventLevel:
        """

        :return:
        """
    @property
    def LogLink(self) -> EventLogLink:
        """

        :return:
        """
    @property
    def Opcode(self) -> EventOpcode:
        """

        :return:
        """
    @property
    def Task(self) -> EventTask:
        """

        :return:
        """
    @property
    def Template(self) -> str:
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

class EventOpcode(Object):
    """"""

    @property
    def DisplayName(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Value(self) -> int:
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

class EventProperty(Object):
    """"""

    @property
    def Value(self) -> object:
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

class EventRecord(ABC, Object, IDisposable):
    """"""

    @property
    def ActivityId(self) -> Optional[Guid]:
        """

        :return:
        """
    @property
    def Bookmark(self) -> EventBookmark:
        """

        :return:
        """
    @property
    def Id(self) -> int:
        """

        :return:
        """
    @property
    def Keywords(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def KeywordsDisplayNames(self) -> IEnumerable[str]:
        """

        :return:
        """
    @property
    def Level(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def LevelDisplayName(self) -> str:
        """

        :return:
        """
    @property
    def LogName(self) -> str:
        """

        :return:
        """
    @property
    def MachineName(self) -> str:
        """

        :return:
        """
    @property
    def Opcode(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def OpcodeDisplayName(self) -> str:
        """

        :return:
        """
    @property
    def ProcessId(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def Properties(self) -> IList[EventProperty]:
        """

        :return:
        """
    @property
    def ProviderId(self) -> Optional[Guid]:
        """

        :return:
        """
    @property
    def ProviderName(self) -> str:
        """

        :return:
        """
    @property
    def Qualifiers(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def RecordId(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def RelatedActivityId(self) -> Optional[Guid]:
        """

        :return:
        """
    @property
    def Task(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def TaskDisplayName(self) -> str:
        """

        :return:
        """
    @property
    def ThreadId(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def TimeCreated(self) -> Optional[DateTime]:
        """

        :return:
        """
    @property
    def UserId(self) -> SecurityIdentifier:
        """

        :return:
        """
    @property
    def Version(self) -> Optional[int]:
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
    @overload
    def FormatDescription(self) -> str:
        """

        :return:
        """
    @overload
    def FormatDescription(self, values: IEnumerable[object]) -> str:
        """

        :param values:
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
    def ToXml(self) -> str:
        """

        :return:
        """

class EventRecordWrittenEventArgs(EventArgs):
    """"""

    @property
    def EventException(self) -> Exception:
        """

        :return:
        """
    @property
    def EventRecord(self) -> EventRecord:
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

class EventTask(Object):
    """"""

    @property
    def DisplayName(self) -> str:
        """

        :return:
        """
    @property
    def EventGuid(self) -> Guid:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Value(self) -> int:
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

class NativeWrapper(Object):
    """"""

    def __init__(self):
        """"""
    @classmethod
    def ConvertToAnsiString(cls, val: UnsafeNativeMethods.EvtVariant) -> str:
        """

        :param val:
        :return:
        """
    @classmethod
    def ConvertToArray(cls, val: UnsafeNativeMethods.EvtVariant, objType: Type, size: int) -> Array:
        """

        :param val:
        :param objType:
        :param size:
        :return:
        """
    @classmethod
    def ConvertToBoolArray(cls, val: UnsafeNativeMethods.EvtVariant) -> Array:
        """

        :param val:
        :return:
        """
    @classmethod
    def ConvertToFileTimeArray(cls, val: UnsafeNativeMethods.EvtVariant) -> Array:
        """

        :param val:
        :return:
        """
    @classmethod
    def ConvertToObject(
        cls, val: UnsafeNativeMethods.EvtVariant, desiredType: UnsafeNativeMethods.EvtVariantType
    ) -> object:
        """

        :param val:
        :param desiredType:
        :return:
        """
    @classmethod
    def ConvertToSafeHandle(cls, val: UnsafeNativeMethods.EvtVariant) -> EventLogHandle:
        """

        :param val:
        :return:
        """
    @classmethod
    def ConvertToString(cls, val: UnsafeNativeMethods.EvtVariant) -> str:
        """

        :param val:
        :return:
        """
    @classmethod
    def ConvertToStringArray(cls, val: UnsafeNativeMethods.EvtVariant, ansi: bool) -> Array[str]:
        """

        :param val:
        :param ansi:
        :return:
        """
    @classmethod
    def ConvertToSysTimeArray(cls, val: UnsafeNativeMethods.EvtVariant) -> Array:
        """

        :param val:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def EvtArchiveExportedLog(
        cls, session: EventLogHandle, logFilePath: str, locale: int, flags: int
    ) -> None:
        """

        :param session:
        :param logFilePath:
        :param locale:
        :param flags:
        """
    @classmethod
    def EvtCancel(cls, handle: EventLogHandle) -> None:
        """

        :param handle:
        """
    @classmethod
    def EvtClearLog(
        cls, session: EventLogHandle, channelPath: str, targetFilePath: str, flags: int
    ) -> None:
        """

        :param session:
        :param channelPath:
        :param targetFilePath:
        :param flags:
        """
    @classmethod
    def EvtClose(cls, handle: IntPtr) -> None:
        """

        :param handle:
        """
    @classmethod
    def EvtCreateBookmark(cls, bookmarkXml: str) -> EventLogHandle:
        """

        :param bookmarkXml:
        :return:
        """
    @classmethod
    def EvtCreateRenderContext(
        cls,
        valuePathsCount: int,
        valuePaths: Array[str],
        flags: UnsafeNativeMethods.EvtRenderContextFlags,
    ) -> EventLogHandle:
        """

        :param valuePathsCount:
        :param valuePaths:
        :param flags:
        :return:
        """
    @classmethod
    def EvtExportLog(
        cls, session: EventLogHandle, channelPath: str, query: str, targetFilePath: str, flags: int
    ) -> None:
        """

        :param session:
        :param channelPath:
        :param query:
        :param targetFilePath:
        :param flags:
        """
    @classmethod
    def EvtFormatMessage(cls, handle: EventLogHandle, msgId: int) -> str:
        """

        :param handle:
        :param msgId:
        :return:
        """
    @classmethod
    def EvtFormatMessageFormatDescription(
        cls, handle: EventLogHandle, eventHandle: EventLogHandle, values: Array[str]
    ) -> str:
        """

        :param handle:
        :param eventHandle:
        :param values:
        :return:
        """
    @classmethod
    def EvtFormatMessageRenderKeywords(
        cls,
        pmHandle: EventLogHandle,
        eventHandle: EventLogHandle,
        flag: UnsafeNativeMethods.EvtFormatMessageFlags,
    ) -> IEnumerable[str]:
        """

        :param pmHandle:
        :param eventHandle:
        :param flag:
        :return:
        """
    @classmethod
    def EvtFormatMessageRenderName(
        cls,
        pmHandle: EventLogHandle,
        eventHandle: EventLogHandle,
        flag: UnsafeNativeMethods.EvtFormatMessageFlags,
    ) -> str:
        """

        :param pmHandle:
        :param eventHandle:
        :param flag:
        :return:
        """
    @classmethod
    def EvtGetChannelConfigProperty(
        cls, handle: EventLogHandle, enumType: UnsafeNativeMethods.EvtChannelConfigPropertyId
    ) -> object:
        """

        :param handle:
        :param enumType:
        :return:
        """
    @classmethod
    def EvtGetEventInfo(
        cls, handle: EventLogHandle, enumType: UnsafeNativeMethods.EvtEventPropertyId
    ) -> object:
        """

        :param handle:
        :param enumType:
        :return:
        """
    @classmethod
    def EvtGetEventMetadataProperty(
        cls, handle: EventLogHandle, enumType: UnsafeNativeMethods.EvtEventMetadataPropertyId
    ) -> object:
        """

        :param handle:
        :param enumType:
        :return:
        """
    @classmethod
    def EvtGetLogInfo(
        cls, handle: EventLogHandle, enumType: UnsafeNativeMethods.EvtLogPropertyId
    ) -> object:
        """

        :param handle:
        :param enumType:
        :return:
        """
    @classmethod
    def EvtGetObjectArrayProperty(
        cls, objArrayHandle: EventLogHandle, index: int, thePropertyId: int
    ) -> object:
        """

        :param objArrayHandle:
        :param index:
        :param thePropertyId:
        :return:
        """
    @classmethod
    def EvtGetObjectArraySize(cls, objectArray: EventLogHandle) -> int:
        """

        :param objectArray:
        :return:
        """
    @classmethod
    def EvtGetPublisherMetadataProperty(
        cls,
        pmHandle: EventLogHandle,
        thePropertyId: UnsafeNativeMethods.EvtPublisherMetadataPropertyId,
    ) -> object:
        """

        :param pmHandle:
        :param thePropertyId:
        :return:
        """
    @classmethod
    def EvtGetQueryInfo(
        cls, handle: EventLogHandle, enumType: UnsafeNativeMethods.EvtQueryPropertyId
    ) -> object:
        """

        :param handle:
        :param enumType:
        :return:
        """
    @classmethod
    def EvtNext(
        cls,
        queryHandle: EventLogHandle,
        eventSize: int,
        events: Array[IntPtr],
        timeout: int,
        flags: int,
        returned: int,
    ) -> bool:
        """

        :param queryHandle:
        :param eventSize:
        :param events:
        :param timeout:
        :param flags:
        :param returned:
        :return:
        """
    @classmethod
    def EvtNextChannelPath(cls, handle: EventLogHandle, finish: bool) -> str:
        """

        :param handle:
        :param finish:
        :return:
        """
    @classmethod
    def EvtNextEventMetadata(cls, eventMetadataEnum: EventLogHandle, flags: int) -> EventLogHandle:
        """

        :param eventMetadataEnum:
        :param flags:
        :return:
        """
    @classmethod
    def EvtNextPublisherId(cls, handle: EventLogHandle, finish: bool) -> str:
        """

        :param handle:
        :param finish:
        :return:
        """
    @classmethod
    def EvtOpenChannelConfig(
        cls, session: EventLogHandle, channelPath: str, flags: int
    ) -> EventLogHandle:
        """

        :param session:
        :param channelPath:
        :param flags:
        :return:
        """
    @classmethod
    def EvtOpenChannelEnum(cls, session: EventLogHandle, flags: int) -> EventLogHandle:
        """

        :param session:
        :param flags:
        :return:
        """
    @classmethod
    def EvtOpenEventMetadataEnum(
        cls, ProviderMetadata: EventLogHandle, flags: int
    ) -> EventLogHandle:
        """

        :param ProviderMetadata:
        :param flags:
        :return:
        """
    @classmethod
    def EvtOpenLog(cls, session: EventLogHandle, path: str, flags: PathType) -> EventLogHandle:
        """

        :param session:
        :param path:
        :param flags:
        :return:
        """
    @classmethod
    def EvtOpenProviderEnum(cls, session: EventLogHandle, flags: int) -> EventLogHandle:
        """

        :param session:
        :param flags:
        :return:
        """
    @classmethod
    def EvtOpenProviderMetadata(
        cls, session: EventLogHandle, ProviderId: str, logFilePath: str, locale: int, flags: int
    ) -> EventLogHandle:
        """

        :param session:
        :param ProviderId:
        :param logFilePath:
        :param locale:
        :param flags:
        :return:
        """
    @classmethod
    def EvtOpenSession(
        cls,
        loginClass: UnsafeNativeMethods.EvtLoginClass,
        login: EvtRpcLogin,
        timeout: int,
        flags: int,
    ) -> EventLogHandle:
        """

        :param loginClass:
        :param login:
        :param timeout:
        :param flags:
        :return:
        """
    @classmethod
    def EvtQuery(cls, session: EventLogHandle, path: str, query: str, flags: int) -> EventLogHandle:
        """

        :param session:
        :param path:
        :param query:
        :param flags:
        :return:
        """
    @classmethod
    def EvtRender(
        cls,
        context: EventLogHandle,
        eventHandle: EventLogHandle,
        flags: UnsafeNativeMethods.EvtRenderFlags,
        buffer: StringBuilder,
    ) -> None:
        """

        :param context:
        :param eventHandle:
        :param flags:
        :param buffer:
        """
    @classmethod
    def EvtRenderBookmark(cls, eventHandle: EventLogHandle) -> str:
        """

        :param eventHandle:
        :return:
        """
    @classmethod
    def EvtRenderBufferWithContextSystem(
        cls,
        contextHandle: EventLogHandle,
        eventHandle: EventLogHandle,
        flag: UnsafeNativeMethods.EvtRenderFlags,
        systemProperties: NativeWrapper.SystemProperties,
        SYSTEM_PROPERTY_COUNT: int,
    ) -> None:
        """

        :param contextHandle:
        :param eventHandle:
        :param flag:
        :param systemProperties:
        :param SYSTEM_PROPERTY_COUNT:
        """
    @classmethod
    def EvtRenderBufferWithContextUserOrValues(
        cls, contextHandle: EventLogHandle, eventHandle: EventLogHandle
    ) -> IList[object]:
        """

        :param contextHandle:
        :param eventHandle:
        :return:
        """
    @classmethod
    def EvtSaveChannelConfig(cls, channelConfig: EventLogHandle, flags: int) -> None:
        """

        :param channelConfig:
        :param flags:
        """
    @classmethod
    def EvtSeek(
        cls,
        resultSet: EventLogHandle,
        position: int,
        bookmark: EventLogHandle,
        timeout: int,
        flags: UnsafeNativeMethods.EvtSeekFlags,
    ) -> None:
        """

        :param resultSet:
        :param position:
        :param bookmark:
        :param timeout:
        :param flags:
        """
    @classmethod
    def EvtSetChannelConfigProperty(
        cls,
        handle: EventLogHandle,
        enumType: UnsafeNativeMethods.EvtChannelConfigPropertyId,
        val: object,
    ) -> None:
        """

        :param handle:
        :param enumType:
        :param val:
        """
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
        """

        :param session:
        :param signalEvent:
        :param path:
        :param query:
        :param bookmark:
        :param context:
        :param callback:
        :param flags:
        :return:
        """
    @classmethod
    def EvtUpdateBookmark(cls, bookmark: EventLogHandle, eventHandle: EventLogHandle) -> None:
        """

        :param bookmark:
        :param eventHandle:
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

    class SystemProperties(Object):
        """"""

        ActivityId: Final[Optional[Guid]] = ...
        """"""
        ChannelName: Final[str] = ...
        """"""
        ComputerName: Final[str] = ...
        """"""
        Id: Final[Optional[int]] = ...
        """"""
        Keywords: Final[Optional[int]] = ...
        """"""
        Level: Final[Optional[int]] = ...
        """"""
        Opcode: Final[Optional[int]] = ...
        """"""
        ProcessId: Final[Optional[int]] = ...
        """"""
        ProviderId: Final[Optional[Guid]] = ...
        """"""
        ProviderName: Final[str] = ...
        """"""
        Qualifiers: Final[Optional[int]] = ...
        """"""
        RecordId: Final[Optional[int]] = ...
        """"""
        RelatedActivityId: Final[Optional[Guid]] = ...
        """"""
        Task: Final[Optional[int]] = ...
        """"""
        ThreadId: Final[Optional[int]] = ...
        """"""
        TimeCreated: Final[Optional[DateTime]] = ...
        """"""
        UserId: Final[SecurityIdentifier] = ...
        """"""
        Version: Final[Optional[int]] = ...
        """"""
        filled: Final[bool] = ...
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

class PathType(Enum):
    """"""

    LogName: PathType = ...
    """"""
    FilePath: PathType = ...
    """"""

class ProviderMetadata(Object, IDisposable):
    """"""

    @overload
    def __init__(self, providerName: str):
        """

        :param providerName:
        """
    @overload
    def __init__(self, providerName: str, session: EventLogSession, targetCultureInfo: CultureInfo):
        """

        :param providerName:
        :param session:
        :param targetCultureInfo:
        """
    @property
    def DisplayName(self) -> str:
        """

        :return:
        """
    @property
    def Events(self) -> IEnumerable[EventMetadata]:
        """

        :return:
        """
    @property
    def HelpLink(self) -> Uri:
        """

        :return:
        """
    @property
    def Id(self) -> Guid:
        """

        :return:
        """
    @property
    def Keywords(self) -> IList[EventKeyword]:
        """

        :return:
        """
    @property
    def Levels(self) -> IList[EventLevel]:
        """

        :return:
        """
    @property
    def LogLinks(self) -> IList[EventLogLink]:
        """

        :return:
        """
    @property
    def MessageFilePath(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Opcodes(self) -> IList[EventOpcode]:
        """

        :return:
        """
    @property
    def ParameterFilePath(self) -> str:
        """

        :return:
        """
    @property
    def ResourceFilePath(self) -> str:
        """

        :return:
        """
    @property
    def Tasks(self) -> IList[EventTask]:
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
    def ToString(self) -> str:
        """

        :return:
        """

class ProviderMetadataCachedInformation(Object):
    """"""

    def __init__(self, session: EventLogSession, logfile: str, maximumCacheSize: int):
        """

        :param session:
        :param logfile:
        :param maximumCacheSize:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetFormatDescription(self, ProviderName: str, eventHandle: EventLogHandle) -> str:
        """

        :param ProviderName:
        :param eventHandle:
        :return:
        """
    @overload
    def GetFormatDescription(
        self, ProviderName: str, eventHandle: EventLogHandle, values: Array[str]
    ) -> str:
        """

        :param ProviderName:
        :param eventHandle:
        :param values:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetKeywordDisplayNames(
        self, ProviderName: str, eventHandle: EventLogHandle
    ) -> IEnumerable[str]:
        """

        :param ProviderName:
        :param eventHandle:
        :return:
        """
    def GetLevelDisplayName(self, ProviderName: str, eventHandle: EventLogHandle) -> str:
        """

        :param ProviderName:
        :param eventHandle:
        :return:
        """
    def GetOpcodeDisplayName(self, ProviderName: str, eventHandle: EventLogHandle) -> str:
        """

        :param ProviderName:
        :param eventHandle:
        :return:
        """
    def GetTaskDisplayName(self, ProviderName: str, eventHandle: EventLogHandle) -> str:
        """

        :param ProviderName:
        :param eventHandle:
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

class StandardEventTask(Enum):
    """"""

    _None: StandardEventTask = ...
    """"""
