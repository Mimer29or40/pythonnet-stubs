from __future__ import annotations

from abc import ABC
from typing import Callable, Generic, Union, overload

from System import AsyncCallback, Boolean, Enum, EventArgs, Exception, IAsyncResult, ICloneable, IDisposable, Int32, IntPtr, MulticastDelegate, Object, String, SystemException, ValueType, Void
from System.ComponentModel import Component, DescriptionAttribute, IComponent, ISite, ISupportInitialize, ISynchronizeInvoke
from System.Runtime.InteropServices import _Attribute, _Exception
from System.Runtime.Serialization import ISerializable

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...


# ---------- Classes ---------- #

class Direct(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def FILE_ACTION_ADDED() -> IntType: ...
    
    @staticmethod
    @property
    def FILE_ACTION_MODIFIED() -> IntType: ...
    
    @staticmethod
    @property
    def FILE_ACTION_REMOVED() -> IntType: ...
    
    @staticmethod
    @property
    def FILE_ACTION_RENAMED_NEW_NAME() -> IntType: ...
    
    @staticmethod
    @property
    def FILE_ACTION_RENAMED_OLD_NAME() -> IntType: ...
    
    @staticmethod
    @property
    def FILE_NOTIFY_CHANGE_ATTRIBUTES() -> IntType: ...
    
    @staticmethod
    @property
    def FILE_NOTIFY_CHANGE_CREATION() -> IntType: ...
    
    @staticmethod
    @property
    def FILE_NOTIFY_CHANGE_DIR_NAME() -> IntType: ...
    
    @staticmethod
    @property
    def FILE_NOTIFY_CHANGE_FILE_NAME() -> IntType: ...
    
    @staticmethod
    @property
    def FILE_NOTIFY_CHANGE_LAST_ACCESS() -> IntType: ...
    
    @staticmethod
    @property
    def FILE_NOTIFY_CHANGE_LAST_WRITE() -> IntType: ...
    
    @staticmethod
    @property
    def FILE_NOTIFY_CHANGE_NAME() -> IntType: ...
    
    @staticmethod
    @property
    def FILE_NOTIFY_CHANGE_SECURITY() -> IntType: ...
    
    @staticmethod
    @property
    def FILE_NOTIFY_CHANGE_SIZE() -> IntType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ErrorEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, exception: Exception): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetException(self) -> Exception: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ErrorEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: ErrorEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: ErrorEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileSystemEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, changeType: WatcherChangeTypes, directory: StringType, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ChangeType(self) -> WatcherChangeTypes: ...
    
    @property
    def FullPath(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_ChangeType(self) -> WatcherChangeTypes: ...
    
    def get_FullPath(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileSystemEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: FileSystemEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: FileSystemEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileSystemWatcher(Component, IComponent, IDisposable, ISupportInitialize):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, path: StringType): ...
    
    @overload
    def __init__(self, path: StringType, filter: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EnableRaisingEvents(self) -> BooleanType: ...
    
    @EnableRaisingEvents.setter
    def EnableRaisingEvents(self, value: BooleanType) -> None: ...
    
    @property
    def Filter(self) -> StringType: ...
    
    @Filter.setter
    def Filter(self, value: StringType) -> None: ...
    
    @property
    def IncludeSubdirectories(self) -> BooleanType: ...
    
    @IncludeSubdirectories.setter
    def IncludeSubdirectories(self, value: BooleanType) -> None: ...
    
    @property
    def InternalBufferSize(self) -> IntType: ...
    
    @InternalBufferSize.setter
    def InternalBufferSize(self, value: IntType) -> None: ...
    
    @property
    def NotifyFilter(self) -> NotifyFilters: ...
    
    @NotifyFilter.setter
    def NotifyFilter(self, value: NotifyFilters) -> None: ...
    
    @property
    def Path(self) -> StringType: ...
    
    @Path.setter
    def Path(self, value: StringType) -> None: ...
    
    @property
    def Site(self) -> ISite: ...
    
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    
    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke: ...
    
    @SynchronizingObject.setter
    def SynchronizingObject(self, value: ISynchronizeInvoke) -> None: ...
    
    # ---------- Methods ---------- #
    
    def BeginInit(self) -> VoidType: ...
    
    def EndInit(self) -> VoidType: ...
    
    @overload
    def WaitForChanged(self, changeType: WatcherChangeTypes) -> WaitForChangedResult: ...
    
    @overload
    def WaitForChanged(self, changeType: WatcherChangeTypes, timeout: IntType) -> WaitForChangedResult: ...
    
    def add_Changed(self, value: FileSystemEventHandler) -> VoidType: ...
    
    def add_Created(self, value: FileSystemEventHandler) -> VoidType: ...
    
    def add_Deleted(self, value: FileSystemEventHandler) -> VoidType: ...
    
    def add_Error(self, value: ErrorEventHandler) -> VoidType: ...
    
    def add_Renamed(self, value: RenamedEventHandler) -> VoidType: ...
    
    def get_EnableRaisingEvents(self) -> BooleanType: ...
    
    def get_Filter(self) -> StringType: ...
    
    def get_IncludeSubdirectories(self) -> BooleanType: ...
    
    def get_InternalBufferSize(self) -> IntType: ...
    
    def get_NotifyFilter(self) -> NotifyFilters: ...
    
    def get_Path(self) -> StringType: ...
    
    def get_Site(self) -> ISite: ...
    
    def get_SynchronizingObject(self) -> ISynchronizeInvoke: ...
    
    def remove_Changed(self, value: FileSystemEventHandler) -> VoidType: ...
    
    def remove_Created(self, value: FileSystemEventHandler) -> VoidType: ...
    
    def remove_Deleted(self, value: FileSystemEventHandler) -> VoidType: ...
    
    def remove_Error(self, value: ErrorEventHandler) -> VoidType: ...
    
    def remove_Renamed(self, value: RenamedEventHandler) -> VoidType: ...
    
    def set_EnableRaisingEvents(self, value: BooleanType) -> VoidType: ...
    
    def set_Filter(self, value: StringType) -> VoidType: ...
    
    def set_IncludeSubdirectories(self, value: BooleanType) -> VoidType: ...
    
    def set_InternalBufferSize(self, value: IntType) -> VoidType: ...
    
    def set_NotifyFilter(self, value: NotifyFilters) -> VoidType: ...
    
    def set_Path(self, value: StringType) -> VoidType: ...
    
    def set_Site(self, value: ISite) -> VoidType: ...
    
    def set_SynchronizingObject(self, value: ISynchronizeInvoke) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    Changed: EventType[FileSystemEventHandler] = ...
    
    Created: EventType[FileSystemEventHandler] = ...
    
    Deleted: EventType[FileSystemEventHandler] = ...
    
    Error: EventType[ErrorEventHandler] = ...
    
    Renamed: EventType[RenamedEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IODescriptionAttribute(DescriptionAttribute, _Attribute):
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


class InternalBufferOverflowException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InvalidDataException(SystemException, ISerializable, _Exception):
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


class PatternMatcher(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def StrictMatchPattern(expression: StringType, name: StringType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RenamedEventArgs(FileSystemEventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, changeType: WatcherChangeTypes, directory: StringType, name: StringType, oldName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def OldFullPath(self) -> StringType: ...
    
    @property
    def OldName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_OldFullPath(self) -> StringType: ...
    
    def get_OldName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RenamedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: RenamedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: RenamedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class WaitForChangedResult(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ChangeType(self) -> WatcherChangeTypes: ...
    
    @ChangeType.setter
    def ChangeType(self, value: WatcherChangeTypes) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def OldName(self) -> StringType: ...
    
    @OldName.setter
    def OldName(self, value: StringType) -> None: ...
    
    @property
    def TimedOut(self) -> BooleanType: ...
    
    @TimedOut.setter
    def TimedOut(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ChangeType(self) -> WatcherChangeTypes: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_OldName(self) -> StringType: ...
    
    def get_TimedOut(self) -> BooleanType: ...
    
    def set_ChangeType(self, value: WatcherChangeTypes) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_OldName(self, value: StringType) -> VoidType: ...
    
    def set_TimedOut(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Interfaces

# ---------- Enums ---------- #

class NotifyFilters(Enum):
    FileName: IntType = 1
    DirectoryName: IntType = 2
    Attributes: IntType = 4
    Size: IntType = 8
    LastWrite: IntType = 16
    LastAccess: IntType = 32
    CreationTime: IntType = 64
    Security: IntType = 256


class WatcherChangeTypes(Enum):
    Created: IntType = 1
    Deleted: IntType = 2
    Changed: IntType = 4
    Renamed: IntType = 8
    All: IntType = 15


# ---------- Delegates ---------- #

ErrorEventHandler = Callable[[ObjectType, ErrorEventArgs], VoidType]

FileSystemEventHandler = Callable[[ObjectType, FileSystemEventArgs], VoidType]

RenamedEventHandler = Callable[[ObjectType, RenamedEventArgs], VoidType]

__all__ = [
    Direct,
    ErrorEventArgs,
    ErrorEventHandler,
    FileSystemEventArgs,
    FileSystemEventHandler,
    FileSystemWatcher,
    IODescriptionAttribute,
    InternalBufferOverflowException,
    InvalidDataException,
    PatternMatcher,
    RenamedEventArgs,
    RenamedEventHandler,
    WaitForChangedResult,
    NotifyFilters,
    WatcherChangeTypes,
    ErrorEventHandler,
    FileSystemEventHandler,
    RenamedEventHandler,
]
