"""Automatically generated stubs for C# namespace: System.IO."""

from abc import ABC
from collections.abc import Callable
from collections.abc import Iterator
from typing import ClassVar
from typing import Self
from typing import overload

from Microsoft.Win32.SafeHandles import SafeFileHandle
from System import Array
from System import ArraySegment
from System import AsyncCallback
from System import Char
from System import DateTime
from System import Decimal
from System import Enum
from System import EventArgs
from System import EventHandler
from System import Exception
from System import Guid
from System import IAsyncResult
from System import IDisposable
from System import IFormatProvider
from System import IntPtr
from System import MarshalByRefObject
from System import Object
from System import String
from System import SystemException
from System import Type
from System import UInt32
from System import ValueType
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEnumerator
from System.ComponentModel import Component
from System.ComponentModel import DescriptionAttribute
from System.ComponentModel import IComponent
from System.ComponentModel import IContainer
from System.ComponentModel import ISite
from System.ComponentModel import ISupportInitialize
from System.ComponentModel import ISynchronizeInvoke
from System.Reflection import MethodBase
from System.Runtime.InteropServices import SafeBuffer
from System.Runtime.InteropServices import _Attribute
from System.Runtime.InteropServices import _Exception
from System.Runtime.Remoting import ObjRef
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Security.AccessControl import AccessControlSections
from System.Security.AccessControl import DirectorySecurity
from System.Security.AccessControl import FileSecurity
from System.Security.AccessControl import FileSystemRights
from System.Text import Encoding
from System.Text import StringBuilder
from System.Threading import CancellationToken
from System.Threading import WaitHandle
from System.Threading.Tasks import Task

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BinaryReader(Object, IDisposable):
    """"""
    @overload
    def __init__(self, input: Stream) -> None:
        """"""
    @overload
    def __init__(self, input: Stream, encoding: Encoding) -> None:
        """"""
    @overload
    def __init__(self, input: Stream, encoding: Encoding, leaveOpen: bool) -> None:
        """"""
    @property
    def BaseStream(self) -> Stream:
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
    def PeekChar(self) -> int:
        """"""
    @overload
    def Read(self) -> int:
        """"""
    @overload
    def Read(self, buffer: Array[int], index: int, count: int) -> int:
        """"""
    @overload
    def Read(self, buffer: Array[Char], index: int, count: int) -> int:
        """"""
    def ReadBoolean(self) -> bool:
        """"""
    def ReadByte(self) -> int:
        """"""
    def ReadBytes(self, count: int) -> Array[int]:
        """"""
    def ReadChar(self) -> Char:
        """"""
    def ReadChars(self, count: int) -> Array[Char]:
        """"""
    def ReadDecimal(self) -> Decimal:
        """"""
    def ReadDouble(self) -> float:
        """"""
    def ReadInt16(self) -> int:
        """"""
    def ReadInt32(self) -> int:
        """"""
    def ReadInt64(self) -> int:
        """"""
    def ReadSByte(self) -> int:
        """"""
    def ReadSingle(self) -> float:
        """"""
    def ReadString(self) -> str:
        """"""
    def ReadUInt16(self) -> int:
        """"""
    def ReadUInt32(self) -> int:
        """"""
    def ReadUInt64(self) -> int:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BinaryWriter(Object, IDisposable):
    """"""

    Null: ClassVar[BinaryWriter]
    """"""
    @overload
    def __init__(self, output: Stream) -> None:
        """"""
    @overload
    def __init__(self, output: Stream, encoding: Encoding) -> None:
        """"""
    @overload
    def __init__(self, output: Stream, encoding: Encoding, leaveOpen: bool) -> None:
        """"""
    @property
    def BaseStream(self) -> Stream:
        """"""
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Write(self, buffer: Array[int]) -> None:
        """"""
    @overload
    def Write(self, buffer: Array[int], index: int, count: int) -> None:
        """"""
    @overload
    def Write(self, chars: Array[Char]) -> None:
        """"""
    @overload
    def Write(self, chars: Array[Char], index: int, count: int) -> None:
        """"""
    @overload
    def Write(self, value: bool) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, ch: Char) -> None:
        """"""
    @overload
    def Write(self, value: Decimal) -> None:
        """"""
    @overload
    def Write(self, value: float) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, value: float) -> None:
        """"""
    @overload
    def Write(self, value: str) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BufferedStream(Stream, IDisposable):
    """"""
    @overload
    def __init__(self, stream: Stream) -> None:
        """"""
    @overload
    def __init__(self, stream: Stream, bufferSize: int) -> None:
        """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, array: Array[int], offset: int, count: int) -> tuple[int, Array[int]]:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, array: Array[int], offset: int, count: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BufferedStream2(ABC, Stream, IDisposable):
    """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, count: int) -> tuple[int, Array[int]]:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, array: Array[int], offset: int, count: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Direct(ABC, Object):
    """"""

    FILE_ACTION_ADDED: ClassVar[int]
    """"""
    FILE_ACTION_MODIFIED: ClassVar[int]
    """"""
    FILE_ACTION_REMOVED: ClassVar[int]
    """"""
    FILE_ACTION_RENAMED_NEW_NAME: ClassVar[int]
    """"""
    FILE_ACTION_RENAMED_OLD_NAME: ClassVar[int]
    """"""
    FILE_NOTIFY_CHANGE_ATTRIBUTES: ClassVar[int]
    """"""
    FILE_NOTIFY_CHANGE_CREATION: ClassVar[int]
    """"""
    FILE_NOTIFY_CHANGE_DIR_NAME: ClassVar[int]
    """"""
    FILE_NOTIFY_CHANGE_FILE_NAME: ClassVar[int]
    """"""
    FILE_NOTIFY_CHANGE_LAST_ACCESS: ClassVar[int]
    """"""
    FILE_NOTIFY_CHANGE_LAST_WRITE: ClassVar[int]
    """"""
    FILE_NOTIFY_CHANGE_NAME: ClassVar[int]
    """"""
    FILE_NOTIFY_CHANGE_SECURITY: ClassVar[int]
    """"""
    FILE_NOTIFY_CHANGE_SIZE: ClassVar[int]
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
class Directory(ABC, Object):
    """"""
    @classmethod
    @overload
    def CreateDirectory(cls, path: str) -> DirectoryInfo:
        """"""
    @classmethod
    @overload
    def CreateDirectory(cls, path: str, directorySecurity: DirectorySecurity) -> DirectoryInfo:
        """"""
    @classmethod
    @overload
    def Delete(cls, path: str) -> None:
        """"""
    @classmethod
    @overload
    def Delete(cls, path: str, recursive: bool) -> None:
        """"""
    @classmethod
    @overload
    def EnumerateDirectories(cls, path: str) -> IEnumerable[str]:
        """"""
    @classmethod
    @overload
    def EnumerateDirectories(cls, path: str, searchPattern: str) -> IEnumerable[str]:
        """"""
    @classmethod
    @overload
    def EnumerateDirectories(
        cls, path: str, searchPattern: str, searchOption: SearchOption
    ) -> IEnumerable[str]:
        """"""
    @classmethod
    @overload
    def EnumerateFileSystemEntries(cls, path: str) -> IEnumerable[str]:
        """"""
    @classmethod
    @overload
    def EnumerateFileSystemEntries(cls, path: str, searchPattern: str) -> IEnumerable[str]:
        """"""
    @classmethod
    @overload
    def EnumerateFileSystemEntries(
        cls, path: str, searchPattern: str, searchOption: SearchOption
    ) -> IEnumerable[str]:
        """"""
    @classmethod
    @overload
    def EnumerateFiles(cls, path: str) -> IEnumerable[str]:
        """"""
    @classmethod
    @overload
    def EnumerateFiles(cls, path: str, searchPattern: str) -> IEnumerable[str]:
        """"""
    @classmethod
    @overload
    def EnumerateFiles(
        cls, path: str, searchPattern: str, searchOption: SearchOption
    ) -> IEnumerable[str]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def Exists(cls, path: str) -> bool:
        """"""
    @classmethod
    @overload
    def GetAccessControl(cls, path: str) -> DirectorySecurity:
        """"""
    @classmethod
    @overload
    def GetAccessControl(
        cls, path: str, includeSections: AccessControlSections
    ) -> DirectorySecurity:
        """"""
    @classmethod
    def GetCreationTime(cls, path: str) -> DateTime:
        """"""
    @classmethod
    def GetCreationTimeUtc(cls, path: str) -> DateTime:
        """"""
    @classmethod
    def GetCurrentDirectory(cls) -> str:
        """"""
    @classmethod
    @overload
    def GetDirectories(cls, path: str) -> Array[str]:
        """"""
    @classmethod
    @overload
    def GetDirectories(cls, path: str, searchPattern: str) -> Array[str]:
        """"""
    @classmethod
    @overload
    def GetDirectories(
        cls, path: str, searchPattern: str, searchOption: SearchOption
    ) -> Array[str]:
        """"""
    @classmethod
    def GetDirectoryRoot(cls, path: str) -> str:
        """"""
    @classmethod
    @overload
    def GetFileSystemEntries(cls, path: str) -> Array[str]:
        """"""
    @classmethod
    @overload
    def GetFileSystemEntries(cls, path: str, searchPattern: str) -> Array[str]:
        """"""
    @classmethod
    @overload
    def GetFileSystemEntries(
        cls, path: str, searchPattern: str, searchOption: SearchOption
    ) -> Array[str]:
        """"""
    @classmethod
    @overload
    def GetFiles(cls, path: str) -> Array[str]:
        """"""
    @classmethod
    @overload
    def GetFiles(cls, path: str, searchPattern: str) -> Array[str]:
        """"""
    @classmethod
    @overload
    def GetFiles(cls, path: str, searchPattern: str, searchOption: SearchOption) -> Array[str]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetLastAccessTime(cls, path: str) -> DateTime:
        """"""
    @classmethod
    def GetLastAccessTimeUtc(cls, path: str) -> DateTime:
        """"""
    @classmethod
    def GetLastWriteTime(cls, path: str) -> DateTime:
        """"""
    @classmethod
    def GetLastWriteTimeUtc(cls, path: str) -> DateTime:
        """"""
    @classmethod
    def GetLogicalDrives(cls) -> Array[str]:
        """"""
    @classmethod
    def GetParent(cls, path: str) -> DirectoryInfo:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Move(cls, sourceDirName: str, destDirName: str) -> None:
        """"""
    @classmethod
    def SetAccessControl(cls, path: str, directorySecurity: DirectorySecurity) -> None:
        """"""
    @classmethod
    def SetCreationTime(cls, path: str, creationTime: DateTime) -> None:
        """"""
    @classmethod
    def SetCreationTimeUtc(cls, path: str, creationTimeUtc: DateTime) -> None:
        """"""
    @classmethod
    def SetCurrentDirectory(cls, path: str) -> None:
        """"""
    @classmethod
    def SetLastAccessTime(cls, path: str, lastAccessTime: DateTime) -> None:
        """"""
    @classmethod
    def SetLastAccessTimeUtc(cls, path: str, lastAccessTimeUtc: DateTime) -> None:
        """"""
    @classmethod
    def SetLastWriteTime(cls, path: str, lastWriteTime: DateTime) -> None:
        """"""
    @classmethod
    def SetLastWriteTimeUtc(cls, path: str, lastWriteTimeUtc: DateTime) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DirectoryInfo(FileSystemInfo, ISerializable):
    """"""
    def __init__(self, path: str) -> None:
        """"""
    @property
    def Attributes(self) -> FileAttributes:
        """"""
    @Attributes.setter
    def Attributes(self, value: FileAttributes) -> None: ...
    @property
    def CreationTime(self) -> DateTime:
        """"""
    @CreationTime.setter
    def CreationTime(self, value: DateTime) -> None: ...
    @property
    def CreationTimeUtc(self) -> DateTime:
        """"""
    @CreationTimeUtc.setter
    def CreationTimeUtc(self, value: DateTime) -> None: ...
    @property
    def Exists(self) -> bool:
        """"""
    @property
    def Extension(self) -> str:
        """"""
    @property
    def FullName(self) -> str:
        """"""
    @property
    def LastAccessTime(self) -> DateTime:
        """"""
    @LastAccessTime.setter
    def LastAccessTime(self, value: DateTime) -> None: ...
    @property
    def LastAccessTimeUtc(self) -> DateTime:
        """"""
    @LastAccessTimeUtc.setter
    def LastAccessTimeUtc(self, value: DateTime) -> None: ...
    @property
    def LastWriteTime(self) -> DateTime:
        """"""
    @LastWriteTime.setter
    def LastWriteTime(self, value: DateTime) -> None: ...
    @property
    def LastWriteTimeUtc(self) -> DateTime:
        """"""
    @LastWriteTimeUtc.setter
    def LastWriteTimeUtc(self, value: DateTime) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @property
    def Parent(self) -> DirectoryInfo:
        """"""
    @property
    def Root(self) -> DirectoryInfo:
        """"""
    @overload
    def Create(self) -> None:
        """"""
    @overload
    def Create(self, directorySecurity: DirectorySecurity) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    @overload
    def CreateSubdirectory(self, path: str) -> DirectoryInfo:
        """"""
    @overload
    def CreateSubdirectory(self, path: str, directorySecurity: DirectorySecurity) -> DirectoryInfo:
        """"""
    @overload
    def Delete(self) -> None:
        """"""
    @overload
    def Delete(self, recursive: bool) -> None:
        """"""
    @overload
    def EnumerateDirectories(self) -> IEnumerable[DirectoryInfo]:
        """"""
    @overload
    def EnumerateDirectories(self, searchPattern: str) -> IEnumerable[DirectoryInfo]:
        """"""
    @overload
    def EnumerateDirectories(
        self, searchPattern: str, searchOption: SearchOption
    ) -> IEnumerable[DirectoryInfo]:
        """"""
    @overload
    def EnumerateFileSystemInfos(self) -> IEnumerable[FileSystemInfo]:
        """"""
    @overload
    def EnumerateFileSystemInfos(self, searchPattern: str) -> IEnumerable[FileSystemInfo]:
        """"""
    @overload
    def EnumerateFileSystemInfos(
        self, searchPattern: str, searchOption: SearchOption
    ) -> IEnumerable[FileSystemInfo]:
        """"""
    @overload
    def EnumerateFiles(self) -> IEnumerable[FileInfo]:
        """"""
    @overload
    def EnumerateFiles(self, searchPattern: str) -> IEnumerable[FileInfo]:
        """"""
    @overload
    def EnumerateFiles(
        self, searchPattern: str, searchOption: SearchOption
    ) -> IEnumerable[FileInfo]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetAccessControl(self) -> DirectorySecurity:
        """"""
    @overload
    def GetAccessControl(self, includeSections: AccessControlSections) -> DirectorySecurity:
        """"""
    @overload
    def GetDirectories(self) -> Array[DirectoryInfo]:
        """"""
    @overload
    def GetDirectories(self, searchPattern: str) -> Array[DirectoryInfo]:
        """"""
    @overload
    def GetDirectories(
        self, searchPattern: str, searchOption: SearchOption
    ) -> Array[DirectoryInfo]:
        """"""
    @overload
    def GetFileSystemInfos(self) -> Array[FileSystemInfo]:
        """"""
    @overload
    def GetFileSystemInfos(self, searchPattern: str) -> Array[FileSystemInfo]:
        """"""
    @overload
    def GetFileSystemInfos(
        self, searchPattern: str, searchOption: SearchOption
    ) -> Array[FileSystemInfo]:
        """"""
    @overload
    def GetFiles(self) -> Array[FileInfo]:
        """"""
    @overload
    def GetFiles(self, searchPattern: str) -> Array[FileInfo]:
        """"""
    @overload
    def GetFiles(self, searchPattern: str, searchOption: SearchOption) -> Array[FileInfo]:
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
    def MoveTo(self, destDirName: str) -> None:
        """"""
    def Refresh(self) -> None:
        """"""
    def SetAccessControl(self, directorySecurity: DirectorySecurity) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DirectoryInfoResultHandler(SearchResultHandler[DirectoryInfo]):
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
class DirectoryNotFoundException(IOException, _Exception, ISerializable):
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
class DriveInfo(Object, ISerializable):
    """"""
    def __init__(self, driveName: str) -> None:
        """"""
    @property
    def AvailableFreeSpace(self) -> int:
        """"""
    @property
    def DriveFormat(self) -> str:
        """"""
    @property
    def DriveType(self) -> DriveType:
        """"""
    @property
    def IsReady(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def RootDirectory(self) -> DirectoryInfo:
        """"""
    @property
    def TotalFreeSpace(self) -> int:
        """"""
    @property
    def TotalSize(self) -> int:
        """"""
    @property
    def VolumeLabel(self) -> str:
        """"""
    @VolumeLabel.setter
    def VolumeLabel(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetDrives(cls) -> Array[DriveInfo]:
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
class DriveNotFoundException(IOException, _Exception, ISerializable):
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
class DriveType(Enum):
    """"""

    Unknown: DriveType = ...
    """"""
    NoRootDirectory: DriveType = ...
    """"""
    Removable: DriveType = ...
    """"""
    Fixed: DriveType = ...
    """"""
    Network: DriveType = ...
    """"""
    CDRom: DriveType = ...
    """"""
    Ram: DriveType = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EndOfStreamException(IOException, _Exception, ISerializable):
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
class ErrorEventArgs(EventArgs):
    """"""
    def __init__(self, exception: Exception) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type ErrorEventHandler = Callable[[object, ErrorEventArgs], None]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class File(ABC, Object):
    """"""
    @classmethod
    @overload
    def AppendAllLines(cls, path: str, contents: IEnumerable[str]) -> None:
        """"""
    @classmethod
    @overload
    def AppendAllLines(cls, path: str, contents: IEnumerable[str], encoding: Encoding) -> None:
        """"""
    @classmethod
    @overload
    def AppendAllText(cls, path: str, contents: str) -> None:
        """"""
    @classmethod
    @overload
    def AppendAllText(cls, path: str, contents: str, encoding: Encoding) -> None:
        """"""
    @classmethod
    def AppendText(cls, path: str) -> StreamWriter:
        """"""
    @classmethod
    @overload
    def Copy(cls, sourceFileName: str, destFileName: str) -> None:
        """"""
    @classmethod
    @overload
    def Copy(cls, sourceFileName: str, destFileName: str, overwrite: bool) -> None:
        """"""
    @classmethod
    @overload
    def Create(cls, path: str) -> FileStream:
        """"""
    @classmethod
    @overload
    def Create(cls, path: str, bufferSize: int) -> FileStream:
        """"""
    @classmethod
    @overload
    def Create(cls, path: str, bufferSize: int, options: FileOptions) -> FileStream:
        """"""
    @classmethod
    @overload
    def Create(
        cls, path: str, bufferSize: int, options: FileOptions, fileSecurity: FileSecurity
    ) -> FileStream:
        """"""
    @classmethod
    def CreateText(cls, path: str) -> StreamWriter:
        """"""
    @classmethod
    def Decrypt(cls, path: str) -> None:
        """"""
    @classmethod
    def Delete(cls, path: str) -> None:
        """"""
    @classmethod
    def Encrypt(cls, path: str) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def Exists(cls, path: str) -> bool:
        """"""
    @classmethod
    @overload
    def GetAccessControl(cls, path: str) -> FileSecurity:
        """"""
    @classmethod
    @overload
    def GetAccessControl(cls, path: str, includeSections: AccessControlSections) -> FileSecurity:
        """"""
    @classmethod
    def GetAttributes(cls, path: str) -> FileAttributes:
        """"""
    @classmethod
    def GetCreationTime(cls, path: str) -> DateTime:
        """"""
    @classmethod
    def GetCreationTimeUtc(cls, path: str) -> DateTime:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetLastAccessTime(cls, path: str) -> DateTime:
        """"""
    @classmethod
    def GetLastAccessTimeUtc(cls, path: str) -> DateTime:
        """"""
    @classmethod
    def GetLastWriteTime(cls, path: str) -> DateTime:
        """"""
    @classmethod
    def GetLastWriteTimeUtc(cls, path: str) -> DateTime:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Move(cls, sourceFileName: str, destFileName: str) -> None:
        """"""
    @classmethod
    @overload
    def Open(cls, path: str, mode: FileMode) -> FileStream:
        """"""
    @classmethod
    @overload
    def Open(cls, path: str, mode: FileMode, access: FileAccess) -> FileStream:
        """"""
    @classmethod
    @overload
    def Open(cls, path: str, mode: FileMode, access: FileAccess, share: FileShare) -> FileStream:
        """"""
    @classmethod
    def OpenRead(cls, path: str) -> FileStream:
        """"""
    @classmethod
    def OpenText(cls, path: str) -> StreamReader:
        """"""
    @classmethod
    def OpenWrite(cls, path: str) -> FileStream:
        """"""
    @classmethod
    def ReadAllBytes(cls, path: str) -> Array[int]:
        """"""
    @classmethod
    @overload
    def ReadAllLines(cls, path: str) -> Array[str]:
        """"""
    @classmethod
    @overload
    def ReadAllLines(cls, path: str, encoding: Encoding) -> Array[str]:
        """"""
    @classmethod
    @overload
    def ReadAllText(cls, path: str) -> str:
        """"""
    @classmethod
    @overload
    def ReadAllText(cls, path: str, encoding: Encoding) -> str:
        """"""
    @classmethod
    @overload
    def ReadLines(cls, path: str) -> IEnumerable[str]:
        """"""
    @classmethod
    @overload
    def ReadLines(cls, path: str, encoding: Encoding) -> IEnumerable[str]:
        """"""
    @classmethod
    @overload
    def Replace(
        cls, sourceFileName: str, destinationFileName: str, destinationBackupFileName: str
    ) -> None:
        """"""
    @classmethod
    @overload
    def Replace(
        cls,
        sourceFileName: str,
        destinationFileName: str,
        destinationBackupFileName: str,
        ignoreMetadataErrors: bool,
    ) -> None:
        """"""
    @classmethod
    def SetAccessControl(cls, path: str, fileSecurity: FileSecurity) -> None:
        """"""
    @classmethod
    def SetAttributes(cls, path: str, fileAttributes: FileAttributes) -> None:
        """"""
    @classmethod
    def SetCreationTime(cls, path: str, creationTime: DateTime) -> None:
        """"""
    @classmethod
    def SetCreationTimeUtc(cls, path: str, creationTimeUtc: DateTime) -> None:
        """"""
    @classmethod
    def SetLastAccessTime(cls, path: str, lastAccessTime: DateTime) -> None:
        """"""
    @classmethod
    def SetLastAccessTimeUtc(cls, path: str, lastAccessTimeUtc: DateTime) -> None:
        """"""
    @classmethod
    def SetLastWriteTime(cls, path: str, lastWriteTime: DateTime) -> None:
        """"""
    @classmethod
    def SetLastWriteTimeUtc(cls, path: str, lastWriteTimeUtc: DateTime) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def WriteAllBytes(cls, path: str, bytes: Array[int]) -> None:
        """"""
    @classmethod
    @overload
    def WriteAllLines(cls, path: str, contents: IEnumerable[str]) -> None:
        """"""
    @classmethod
    @overload
    def WriteAllLines(cls, path: str, contents: IEnumerable[str], encoding: Encoding) -> None:
        """"""
    @classmethod
    @overload
    def WriteAllLines(cls, path: str, contents: Array[str]) -> None:
        """"""
    @classmethod
    @overload
    def WriteAllLines(cls, path: str, contents: Array[str], encoding: Encoding) -> None:
        """"""
    @classmethod
    @overload
    def WriteAllText(cls, path: str, contents: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteAllText(cls, path: str, contents: str, encoding: Encoding) -> None:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class FileAccess(Enum):
    """"""

    Read: FileAccess = ...
    """"""
    Write: FileAccess = ...
    """"""
    ReadWrite: FileAccess = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class FileAttributes(Enum):
    """"""

    ReadOnly: FileAttributes = ...
    """"""
    Hidden: FileAttributes = ...
    """"""
    System: FileAttributes = ...
    """"""
    Directory: FileAttributes = ...
    """"""
    Archive: FileAttributes = ...
    """"""
    Device: FileAttributes = ...
    """"""
    Normal: FileAttributes = ...
    """"""
    Temporary: FileAttributes = ...
    """"""
    SparseFile: FileAttributes = ...
    """"""
    ReparsePoint: FileAttributes = ...
    """"""
    Compressed: FileAttributes = ...
    """"""
    Offline: FileAttributes = ...
    """"""
    NotContentIndexed: FileAttributes = ...
    """"""
    Encrypted: FileAttributes = ...
    """"""
    IntegrityStream: FileAttributes = ...
    """"""
    NoScrubData: FileAttributes = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FileInfo(FileSystemInfo, ISerializable):
    """"""
    def __init__(self, fileName: str) -> None:
        """"""
    @property
    def Attributes(self) -> FileAttributes:
        """"""
    @Attributes.setter
    def Attributes(self, value: FileAttributes) -> None: ...
    @property
    def CreationTime(self) -> DateTime:
        """"""
    @CreationTime.setter
    def CreationTime(self, value: DateTime) -> None: ...
    @property
    def CreationTimeUtc(self) -> DateTime:
        """"""
    @CreationTimeUtc.setter
    def CreationTimeUtc(self, value: DateTime) -> None: ...
    @property
    def Directory(self) -> DirectoryInfo:
        """"""
    @property
    def DirectoryName(self) -> str:
        """"""
    @property
    def Exists(self) -> bool:
        """"""
    @property
    def Extension(self) -> str:
        """"""
    @property
    def FullName(self) -> str:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @IsReadOnly.setter
    def IsReadOnly(self, value: bool) -> None: ...
    @property
    def LastAccessTime(self) -> DateTime:
        """"""
    @LastAccessTime.setter
    def LastAccessTime(self, value: DateTime) -> None: ...
    @property
    def LastAccessTimeUtc(self) -> DateTime:
        """"""
    @LastAccessTimeUtc.setter
    def LastAccessTimeUtc(self, value: DateTime) -> None: ...
    @property
    def LastWriteTime(self) -> DateTime:
        """"""
    @LastWriteTime.setter
    def LastWriteTime(self, value: DateTime) -> None: ...
    @property
    def LastWriteTimeUtc(self) -> DateTime:
        """"""
    @LastWriteTimeUtc.setter
    def LastWriteTimeUtc(self, value: DateTime) -> None: ...
    @property
    def Length(self) -> int:
        """"""
    @property
    def Name(self) -> str:
        """"""
    def AppendText(self) -> StreamWriter:
        """"""
    @overload
    def CopyTo(self, destFileName: str) -> FileInfo:
        """"""
    @overload
    def CopyTo(self, destFileName: str, overwrite: bool) -> FileInfo:
        """"""
    def Create(self) -> FileStream:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def CreateText(self) -> StreamWriter:
        """"""
    def Decrypt(self) -> None:
        """"""
    def Delete(self) -> None:
        """"""
    def Encrypt(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetAccessControl(self) -> FileSecurity:
        """"""
    @overload
    def GetAccessControl(self, includeSections: AccessControlSections) -> FileSecurity:
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
    def MoveTo(self, destFileName: str) -> None:
        """"""
    @overload
    def Open(self, mode: FileMode) -> FileStream:
        """"""
    @overload
    def Open(self, mode: FileMode, access: FileAccess) -> FileStream:
        """"""
    @overload
    def Open(self, mode: FileMode, access: FileAccess, share: FileShare) -> FileStream:
        """"""
    def OpenRead(self) -> FileStream:
        """"""
    def OpenText(self) -> StreamReader:
        """"""
    def OpenWrite(self) -> FileStream:
        """"""
    def Refresh(self) -> None:
        """"""
    @overload
    def Replace(self, destinationFileName: str, destinationBackupFileName: str) -> FileInfo:
        """"""
    @overload
    def Replace(
        self, destinationFileName: str, destinationBackupFileName: str, ignoreMetadataErrors: bool
    ) -> FileInfo:
        """"""
    def SetAccessControl(self, fileSecurity: FileSecurity) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FileInfoResultHandler(SearchResultHandler[FileInfo]):
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
class FileLoadException(IOException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, inner: Exception) -> None:
        """"""
    @overload
    def __init__(self, message: str, fileName: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, fileName: str, inner: Exception) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def FileName(self) -> str:
        """"""
    @property
    def FusionLog(self) -> str:
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
class FileMode(Enum):
    """"""

    CreateNew: FileMode = ...
    """"""
    Create: FileMode = ...
    """"""
    Open: FileMode = ...
    """"""
    OpenOrCreate: FileMode = ...
    """"""
    Truncate: FileMode = ...
    """"""
    Append: FileMode = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FileNotFoundException(IOException, _Exception, ISerializable):
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
    @overload
    def __init__(self, message: str, fileName: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, fileName: str, innerException: Exception) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def FileName(self) -> str:
        """"""
    @property
    def FusionLog(self) -> str:
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
class FileOptions(Enum):
    """"""

    _None: FileOptions = ...
    """"""
    Encrypted: FileOptions = ...
    """"""
    DeleteOnClose: FileOptions = ...
    """"""
    SequentialScan: FileOptions = ...
    """"""
    RandomAccess: FileOptions = ...
    """"""
    Asynchronous: FileOptions = ...
    """"""
    WriteThrough: FileOptions = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class FileSecurityStateAccess(Enum):
    """"""

    NoAccess: FileSecurityStateAccess = ...
    """"""
    Read: FileSecurityStateAccess = ...
    """"""
    Write: FileSecurityStateAccess = ...
    """"""
    Append: FileSecurityStateAccess = ...
    """"""
    PathDiscovery: FileSecurityStateAccess = ...
    """"""
    AllAccess: FileSecurityStateAccess = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class FileShare(Enum):
    """"""

    _None: FileShare = ...
    """"""
    Read: FileShare = ...
    """"""
    Write: FileShare = ...
    """"""
    ReadWrite: FileShare = ...
    """"""
    Delete: FileShare = ...
    """"""
    Inheritable: FileShare = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FileStream(Stream, IDisposable):
    """"""
    @overload
    def __init__(self, path: str, mode: FileMode) -> None:
        """"""
    @overload
    def __init__(self, path: str, mode: FileMode, access: FileAccess) -> None:
        """"""
    @overload
    def __init__(self, path: str, mode: FileMode, access: FileAccess, share: FileShare) -> None:
        """"""
    @overload
    def __init__(
        self, path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        path: str,
        mode: FileMode,
        access: FileAccess,
        share: FileShare,
        bufferSize: int,
        options: FileOptions,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        path: str,
        mode: FileMode,
        access: FileAccess,
        share: FileShare,
        bufferSize: int,
        useAsync: bool,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        path: str,
        mode: FileMode,
        rights: FileSystemRights,
        share: FileShare,
        bufferSize: int,
        options: FileOptions,
        fileSecurity: FileSecurity,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        path: str,
        mode: FileMode,
        rights: FileSystemRights,
        share: FileShare,
        bufferSize: int,
        options: FileOptions,
    ) -> None:
        """"""
    @overload
    def __init__(self, handle: IntPtr, access: FileAccess) -> None:
        """"""
    @overload
    def __init__(self, handle: IntPtr, access: FileAccess, ownsHandle: bool) -> None:
        """"""
    @overload
    def __init__(
        self, handle: IntPtr, access: FileAccess, ownsHandle: bool, bufferSize: int
    ) -> None:
        """"""
    @overload
    def __init__(
        self, handle: IntPtr, access: FileAccess, ownsHandle: bool, bufferSize: int, isAsync: bool
    ) -> None:
        """"""
    @overload
    def __init__(self, handle: SafeFileHandle, access: FileAccess) -> None:
        """"""
    @overload
    def __init__(self, handle: SafeFileHandle, access: FileAccess, bufferSize: int) -> None:
        """"""
    @overload
    def __init__(
        self, handle: SafeFileHandle, access: FileAccess, bufferSize: int, isAsync: bool
    ) -> None:
        """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Handle(self) -> IntPtr:
        """"""
    @property
    def IsAsync(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def SafeFileHandle(self) -> SafeFileHandle:
        """"""
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self,
        array: Array[int],
        offset: int,
        numBytes: int,
        userCallback: AsyncCallback,
        stateObject: object,
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self,
        array: Array[int],
        offset: int,
        numBytes: int,
        userCallback: AsyncCallback,
        stateObject: object,
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Flush(self) -> None:
        """"""
    @overload
    def Flush(self, flushToDisk: bool) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetAccessControl(self) -> FileSecurity:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Lock(self, position: int, length: int) -> None:
        """"""
    def Read(self, array: Array[int], offset: int, count: int) -> tuple[int, Array[int]]:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetAccessControl(self, fileSecurity: FileSecurity) -> None:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Unlock(self, position: int, length: int) -> None:
        """"""
    def Write(self, array: Array[int], offset: int, count: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FileStreamAsyncResult(Object, IAsyncResult):
    """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CompletedSynchronously(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
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
class FileSystemEnumerableFactory(ABC, Object):
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
class FileSystemEnumerableIterator[TSource](
    Iterator[TSource],
    IEnumerable[TSource],
    IEnumerator[TSource],
    IEnumerable,
    IEnumerator,
    IDisposable,
):
    """"""
    @property
    def Current(self) -> TSource:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[TSource](self) -> IEnumerator[TSource]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__[TSource](self) -> Iterator[TSource]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FileSystemEventArgs(EventArgs):
    """"""
    def __init__(self, changeType: WatcherChangeTypes, directory: str, name: str) -> None:
        """"""
    @property
    def ChangeType(self) -> WatcherChangeTypes:
        """"""
    @property
    def FullPath(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type FileSystemEventHandler = Callable[[object, FileSystemEventArgs], None]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FileSystemInfo(ABC, MarshalByRefObject, ISerializable):
    """"""
    @property
    def Attributes(self) -> FileAttributes:
        """"""
    @Attributes.setter
    def Attributes(self, value: FileAttributes) -> None: ...
    @property
    def CreationTime(self) -> DateTime:
        """"""
    @CreationTime.setter
    def CreationTime(self, value: DateTime) -> None: ...
    @property
    def CreationTimeUtc(self) -> DateTime:
        """"""
    @CreationTimeUtc.setter
    def CreationTimeUtc(self, value: DateTime) -> None: ...
    @property
    def Exists(self) -> bool:
        """"""
    @property
    def Extension(self) -> str:
        """"""
    @property
    def FullName(self) -> str:
        """"""
    @property
    def LastAccessTime(self) -> DateTime:
        """"""
    @LastAccessTime.setter
    def LastAccessTime(self, value: DateTime) -> None: ...
    @property
    def LastAccessTimeUtc(self) -> DateTime:
        """"""
    @LastAccessTimeUtc.setter
    def LastAccessTimeUtc(self, value: DateTime) -> None: ...
    @property
    def LastWriteTime(self) -> DateTime:
        """"""
    @LastWriteTime.setter
    def LastWriteTime(self, value: DateTime) -> None: ...
    @property
    def LastWriteTimeUtc(self) -> DateTime:
        """"""
    @LastWriteTimeUtc.setter
    def LastWriteTimeUtc(self, value: DateTime) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Delete(self) -> None:
        """"""
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
    def Refresh(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FileSystemInfoResultHandler(SearchResultHandler[FileSystemInfo]):
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
class FileSystemWatcher(Component, IComponent, ISupportInitialize, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, path: str) -> None:
        """"""
    @overload
    def __init__(self, path: str, filter: str) -> None:
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
    def Filter(self) -> str:
        """"""
    @Filter.setter
    def Filter(self, value: str) -> None: ...
    @property
    def IncludeSubdirectories(self) -> bool:
        """"""
    @IncludeSubdirectories.setter
    def IncludeSubdirectories(self, value: bool) -> None: ...
    @property
    def InternalBufferSize(self) -> int:
        """"""
    @InternalBufferSize.setter
    def InternalBufferSize(self, value: int) -> None: ...
    @property
    def NotifyFilter(self) -> NotifyFilters:
        """"""
    @NotifyFilter.setter
    def NotifyFilter(self, value: NotifyFilters) -> None: ...
    @property
    def Path(self) -> str:
        """"""
    @Path.setter
    def Path(self, value: str) -> None: ...
    @property
    def Site(self) -> ISite:
        """"""
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke:
        """"""
    @SynchronizingObject.setter
    def SynchronizingObject(self, value: ISynchronizeInvoke) -> None: ...
    def BeginInit(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
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
    def InitializeLifetimeService(self) -> object:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def WaitForChanged(self, changeType: WatcherChangeTypes) -> WaitForChangedResult:
        """"""
    @overload
    def WaitForChanged(self, changeType: WatcherChangeTypes, timeout: int) -> WaitForChangedResult:
        """"""
    Changed: EventType[FileSystemEventHandler] = ...
    """"""
    Created: EventType[FileSystemEventHandler] = ...
    """"""
    Deleted: EventType[FileSystemEventHandler] = ...
    """"""
    Disposed: EventType[EventHandler] = ...
    """"""
    Error: EventType[ErrorEventHandler] = ...
    """"""
    Renamed: EventType[RenamedEventHandler] = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class HandleInheritability(Enum):
    """"""

    _None: HandleInheritability = ...
    """"""
    Inheritable: HandleInheritability = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IODescriptionAttribute(DescriptionAttribute, _Attribute):
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
class IOException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, hresult: int) -> None:
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
class InternalBufferOverflowException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, inner: Exception) -> None:
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
class InvalidDataException(SystemException, _Exception, ISerializable):
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
class Iterator[TSource](
    ABC, Object, IEnumerable[TSource], IEnumerator[TSource], IEnumerable, IEnumerator, IDisposable
):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Current(self) -> TSource:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[TSource](self) -> IEnumerator[TSource]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__[TSource](self) -> Iterator[TSource]:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class LogRetentionOption(Enum):
    """"""

    UnlimitedSequentialFiles: LogRetentionOption = ...
    """"""
    LimitedCircularFiles: LogRetentionOption = ...
    """"""
    SingleFileUnboundedSize: LogRetentionOption = ...
    """"""
    LimitedSequentialFiles: LogRetentionOption = ...
    """"""
    SingleFileBoundedSize: LogRetentionOption = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class LogStream(BufferedStream2, IDisposable):
    """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, array: Array[int], offset: int, count: int) -> int:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, array: Array[int], offset: int, count: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class LongPath(ABC, Object):
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
class LongPathDirectory(ABC, Object):
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
class LongPathFile(ABC, Object):
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
class LongPathHelper(Object):
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
class MemoryStream(Stream, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, capacity: int) -> None:
        """"""
    @overload
    def __init__(self, buffer: Array[int]) -> None:
        """"""
    @overload
    def __init__(self, buffer: Array[int], writable: bool) -> None:
        """"""
    @overload
    def __init__(self, buffer: Array[int], index: int, count: int) -> None:
        """"""
    @overload
    def __init__(self, buffer: Array[int], index: int, count: int, writable: bool) -> None:
        """"""
    @overload
    def __init__(
        self, buffer: Array[int], index: int, count: int, writable: bool, publiclyVisible: bool
    ) -> None:
        """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetBuffer(self) -> Array[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, count: int) -> tuple[int, Array[int]]:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, loc: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToArray(self) -> Array[int]:
        """"""
    def ToString(self) -> str:
        """"""
    def TryGetBuffer(self, buffer: ArraySegment[int]) -> tuple[bool, ArraySegment[int]]:
        """"""
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""
    def WriteTo(self, stream: Stream) -> None:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class NotifyFilters(Enum):
    """"""

    FileName: NotifyFilters = ...
    """"""
    DirectoryName: NotifyFilters = ...
    """"""
    Attributes: NotifyFilters = ...
    """"""
    Size: NotifyFilters = ...
    """"""
    LastWrite: NotifyFilters = ...
    """"""
    LastAccess: NotifyFilters = ...
    """"""
    CreationTime: NotifyFilters = ...
    """"""
    Security: NotifyFilters = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Path(ABC, Object):
    """"""

    AltDirectorySeparatorChar: ClassVar[Char]
    """"""
    DirectorySeparatorChar: ClassVar[Char]
    """"""
    InvalidPathChars: ClassVar[Array[Char]]
    """"""
    PathSeparator: ClassVar[Char]
    """"""
    VolumeSeparatorChar: ClassVar[Char]
    """"""
    @classmethod
    def ChangeExtension(cls, path: str, extension: str) -> str:
        """"""
    @classmethod
    @overload
    def Combine(cls, paths: Array[str]) -> str:
        """"""
    @classmethod
    @overload
    def Combine(cls, path1: str, path2: str) -> str:
        """"""
    @classmethod
    @overload
    def Combine(cls, path1: str, path2: str, path3: str) -> str:
        """"""
    @classmethod
    @overload
    def Combine(cls, path1: str, path2: str, path3: str, path4: str) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetDirectoryName(cls, path: str) -> str:
        """"""
    @classmethod
    def GetExtension(cls, path: str) -> str:
        """"""
    @classmethod
    def GetFileName(cls, path: str) -> str:
        """"""
    @classmethod
    def GetFileNameWithoutExtension(cls, path: str) -> str:
        """"""
    @classmethod
    def GetFullPath(cls, path: str) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetInvalidFileNameChars(cls) -> Array[Char]:
        """"""
    @classmethod
    def GetInvalidPathChars(cls) -> Array[Char]:
        """"""
    @classmethod
    def GetPathRoot(cls, path: str) -> str:
        """"""
    @classmethod
    def GetRandomFileName(cls) -> str:
        """"""
    @classmethod
    def GetTempFileName(cls) -> str:
        """"""
    @classmethod
    def GetTempPath(cls) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def HasExtension(cls, path: str) -> bool:
        """"""
    @classmethod
    def IsPathRooted(cls, path: str) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PathHelper(ValueType):
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
class PathInternal(ABC, Object):
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
class PathTooLongException(IOException, _Exception, ISerializable):
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
class PatternMatcher(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def StrictMatchPattern(cls, expression: str, name: str) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PinnedBufferMemoryStream(UnmanagedMemoryStream, IDisposable):
    """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def PositionPointer(self) -> int:
        """"""
    @PositionPointer.setter
    def PositionPointer(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, count: int) -> tuple[int, Array[int]]:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, loc: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ReadLinesIterator(
    Iterator[String],
    IEnumerable[String],
    IEnumerator[String],
    IEnumerable,
    IEnumerator,
    IDisposable,
):
    """"""
    @property
    def Current(self) -> str:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[str]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator[str]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RenamedEventArgs(FileSystemEventArgs):
    """"""
    def __init__(
        self, changeType: WatcherChangeTypes, directory: str, name: str, oldName: str
    ) -> None:
        """"""
    @property
    def ChangeType(self) -> WatcherChangeTypes:
        """"""
    @property
    def FullPath(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def OldFullPath(self) -> str:
        """"""
    @property
    def OldName(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type RenamedEventHandler = Callable[[object, RenamedEventArgs], None]
""""""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class SearchOption(Enum):
    """"""

    TopDirectoryOnly: SearchOption = ...
    """"""
    AllDirectories: SearchOption = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SearchResultHandler[TSource](ABC, Object):
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
class SeekOrigin(Enum):
    """"""

    Begin: SeekOrigin = ...
    """"""
    Current: SeekOrigin = ...
    """"""
    End: SeekOrigin = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Stream(ABC, MarshalByRefObject, IDisposable):
    """"""

    Null: ClassVar[Stream]
    """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, count: int) -> tuple[int, Array[int]]:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    @classmethod
    def Synchronized(cls, stream: Stream) -> Stream:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StreamReader(TextReader, IDisposable):
    """"""

    Null: ClassVar[StreamReader]
    """"""
    @overload
    def __init__(self, stream: Stream) -> None:
        """"""
    @overload
    def __init__(self, stream: Stream, detectEncodingFromByteOrderMarks: bool) -> None:
        """"""
    @overload
    def __init__(self, stream: Stream, encoding: Encoding) -> None:
        """"""
    @overload
    def __init__(
        self, stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        stream: Stream,
        encoding: Encoding,
        detectEncodingFromByteOrderMarks: bool,
        bufferSize: int,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        stream: Stream,
        encoding: Encoding,
        detectEncodingFromByteOrderMarks: bool,
        bufferSize: int,
        leaveOpen: bool,
    ) -> None:
        """"""
    @overload
    def __init__(self, path: str) -> None:
        """"""
    @overload
    def __init__(self, path: str, detectEncodingFromByteOrderMarks: bool) -> None:
        """"""
    @overload
    def __init__(self, path: str, encoding: Encoding) -> None:
        """"""
    @overload
    def __init__(
        self, path: str, encoding: Encoding, detectEncodingFromByteOrderMarks: bool
    ) -> None:
        """"""
    @overload
    def __init__(
        self, path: str, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int
    ) -> None:
        """"""
    @property
    def BaseStream(self) -> Stream:
        """"""
    @property
    def CurrentEncoding(self) -> Encoding:
        """"""
    @property
    def EndOfStream(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def DiscardBufferedData(self) -> None:
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
    def Peek(self) -> int:
        """"""
    @overload
    def Read(self) -> int:
        """"""
    @overload
    def Read(self, buffer: Array[Char], index: int, count: int) -> tuple[int, Array[Char]]:
        """"""
    def ReadAsync(self, buffer: Array[Char], index: int, count: int) -> Task[int]:
        """"""
    def ReadBlock(self, buffer: Array[Char], index: int, count: int) -> tuple[int, Array[Char]]:
        """"""
    def ReadBlockAsync(self, buffer: Array[Char], index: int, count: int) -> Task[int]:
        """"""
    def ReadLine(self) -> str:
        """"""
    def ReadLineAsync(self) -> Task[str]:
        """"""
    def ReadToEnd(self) -> str:
        """"""
    def ReadToEndAsync(self) -> Task[str]:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StreamWriter(TextWriter, IDisposable):
    """"""

    Null: ClassVar[StreamWriter]
    """"""
    @overload
    def __init__(self, stream: Stream) -> None:
        """"""
    @overload
    def __init__(self, stream: Stream, encoding: Encoding) -> None:
        """"""
    @overload
    def __init__(self, stream: Stream, encoding: Encoding, bufferSize: int) -> None:
        """"""
    @overload
    def __init__(
        self, stream: Stream, encoding: Encoding, bufferSize: int, leaveOpen: bool
    ) -> None:
        """"""
    @overload
    def __init__(self, path: str) -> None:
        """"""
    @overload
    def __init__(self, path: str, append: bool) -> None:
        """"""
    @overload
    def __init__(self, path: str, append: bool, encoding: Encoding) -> None:
        """"""
    @overload
    def __init__(self, path: str, append: bool, encoding: Encoding, bufferSize: int) -> None:
        """"""
    @property
    def AutoFlush(self) -> bool:
        """"""
    @AutoFlush.setter
    def AutoFlush(self, value: bool) -> None: ...
    @property
    def BaseStream(self) -> Stream:
        """"""
    @property
    def Encoding(self) -> Encoding:
        """"""
    @property
    def FormatProvider(self) -> IFormatProvider:
        """"""
    @property
    def NewLine(self) -> str:
        """"""
    @NewLine.setter
    def NewLine(self, value: str) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    def FlushAsync(self) -> Task:
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
    def Write(self, buffer: Array[Char]) -> None:
        """"""
    @overload
    def Write(self, buffer: Array[Char], index: int, count: int) -> None:
        """"""
    @overload
    def Write(self, value: bool) -> None:
        """"""
    @overload
    def Write(self, value: Char) -> None:
        """"""
    @overload
    def Write(self, value: Decimal) -> None:
        """"""
    @overload
    def Write(self, value: float) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, value: object) -> None:
        """"""
    @overload
    def Write(self, value: float) -> None:
        """"""
    @overload
    def Write(self, value: str) -> None:
        """"""
    @overload
    def Write(self, format: str, arg: Array[object]) -> None:
        """"""
    @overload
    def Write(self, format: str, arg0: object) -> None:
        """"""
    @overload
    def Write(self, format: str, arg0: object, arg1: object) -> None:
        """"""
    @overload
    def Write(self, format: str, arg0: object, arg1: object, arg2: object) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[Char]) -> Task:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[Char], index: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(self, value: Char) -> Task:
        """"""
    @overload
    def WriteAsync(self, value: str) -> Task:
        """"""
    @overload
    def WriteLine(self) -> None:
        """"""
    @overload
    def WriteLine(self, buffer: Array[Char]) -> None:
        """"""
    @overload
    def WriteLine(self, buffer: Array[Char], index: int, count: int) -> None:
        """"""
    @overload
    def WriteLine(self, value: bool) -> None:
        """"""
    @overload
    def WriteLine(self, value: Char) -> None:
        """"""
    @overload
    def WriteLine(self, value: Decimal) -> None:
        """"""
    @overload
    def WriteLine(self, value: float) -> None:
        """"""
    @overload
    def WriteLine(self, value: int) -> None:
        """"""
    @overload
    def WriteLine(self, value: int) -> None:
        """"""
    @overload
    def WriteLine(self, value: object) -> None:
        """"""
    @overload
    def WriteLine(self, value: float) -> None:
        """"""
    @overload
    def WriteLine(self, value: str) -> None:
        """"""
    @overload
    def WriteLine(self, format: str, arg: Array[object]) -> None:
        """"""
    @overload
    def WriteLine(self, format: str, arg0: object) -> None:
        """"""
    @overload
    def WriteLine(self, format: str, arg0: object, arg1: object) -> None:
        """"""
    @overload
    def WriteLine(self, format: str, arg0: object, arg1: object, arg2: object) -> None:
        """"""
    @overload
    def WriteLine(self, value: int) -> None:
        """"""
    @overload
    def WriteLine(self, value: int) -> None:
        """"""
    @overload
    def WriteLineAsync(self) -> Task:
        """"""
    @overload
    def WriteLineAsync(self, buffer: Array[Char]) -> Task:
        """"""
    @overload
    def WriteLineAsync(self, buffer: Array[Char], index: int, count: int) -> Task:
        """"""
    @overload
    def WriteLineAsync(self, value: Char) -> Task:
        """"""
    @overload
    def WriteLineAsync(self, value: str) -> Task:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StringReader(TextReader, IDisposable):
    """"""
    def __init__(self, s: str) -> None:
        """"""
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
    def Peek(self) -> int:
        """"""
    @overload
    def Read(self) -> int:
        """"""
    @overload
    def Read(self, buffer: Array[Char], index: int, count: int) -> tuple[int, Array[Char]]:
        """"""
    def ReadAsync(self, buffer: Array[Char], index: int, count: int) -> Task[int]:
        """"""
    def ReadBlock(self, buffer: Array[Char], index: int, count: int) -> tuple[int, Array[Char]]:
        """"""
    def ReadBlockAsync(self, buffer: Array[Char], index: int, count: int) -> Task[int]:
        """"""
    def ReadLine(self) -> str:
        """"""
    def ReadLineAsync(self) -> Task[str]:
        """"""
    def ReadToEnd(self) -> str:
        """"""
    def ReadToEndAsync(self) -> Task[str]:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StringResultHandler(SearchResultHandler[String]):
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
class StringWriter(TextWriter, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, formatProvider: IFormatProvider) -> None:
        """"""
    @overload
    def __init__(self, sb: StringBuilder) -> None:
        """"""
    @overload
    def __init__(self, sb: StringBuilder, formatProvider: IFormatProvider) -> None:
        """"""
    @property
    def Encoding(self) -> Encoding:
        """"""
    @property
    def FormatProvider(self) -> IFormatProvider:
        """"""
    @property
    def NewLine(self) -> str:
        """"""
    @NewLine.setter
    def NewLine(self, value: str) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    def FlushAsync(self) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetStringBuilder(self) -> StringBuilder:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Write(self, buffer: Array[Char]) -> None:
        """"""
    @overload
    def Write(self, buffer: Array[Char], index: int, count: int) -> None:
        """"""
    @overload
    def Write(self, value: bool) -> None:
        """"""
    @overload
    def Write(self, value: Char) -> None:
        """"""
    @overload
    def Write(self, value: Decimal) -> None:
        """"""
    @overload
    def Write(self, value: float) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, value: object) -> None:
        """"""
    @overload
    def Write(self, value: float) -> None:
        """"""
    @overload
    def Write(self, value: str) -> None:
        """"""
    @overload
    def Write(self, format: str, arg: Array[object]) -> None:
        """"""
    @overload
    def Write(self, format: str, arg0: object) -> None:
        """"""
    @overload
    def Write(self, format: str, arg0: object, arg1: object) -> None:
        """"""
    @overload
    def Write(self, format: str, arg0: object, arg1: object, arg2: object) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[Char]) -> Task:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[Char], index: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(self, value: Char) -> Task:
        """"""
    @overload
    def WriteAsync(self, value: str) -> Task:
        """"""
    @overload
    def WriteLine(self) -> None:
        """"""
    @overload
    def WriteLine(self, buffer: Array[Char]) -> None:
        """"""
    @overload
    def WriteLine(self, buffer: Array[Char], index: int, count: int) -> None:
        """"""
    @overload
    def WriteLine(self, value: bool) -> None:
        """"""
    @overload
    def WriteLine(self, value: Char) -> None:
        """"""
    @overload
    def WriteLine(self, value: Decimal) -> None:
        """"""
    @overload
    def WriteLine(self, value: float) -> None:
        """"""
    @overload
    def WriteLine(self, value: int) -> None:
        """"""
    @overload
    def WriteLine(self, value: int) -> None:
        """"""
    @overload
    def WriteLine(self, value: object) -> None:
        """"""
    @overload
    def WriteLine(self, value: float) -> None:
        """"""
    @overload
    def WriteLine(self, value: str) -> None:
        """"""
    @overload
    def WriteLine(self, format: str, arg: Array[object]) -> None:
        """"""
    @overload
    def WriteLine(self, format: str, arg0: object) -> None:
        """"""
    @overload
    def WriteLine(self, format: str, arg0: object, arg1: object) -> None:
        """"""
    @overload
    def WriteLine(self, format: str, arg0: object, arg1: object, arg2: object) -> None:
        """"""
    @overload
    def WriteLine(self, value: int) -> None:
        """"""
    @overload
    def WriteLine(self, value: int) -> None:
        """"""
    @overload
    def WriteLineAsync(self) -> Task:
        """"""
    @overload
    def WriteLineAsync(self, buffer: Array[Char]) -> Task:
        """"""
    @overload
    def WriteLineAsync(self, buffer: Array[Char], index: int, count: int) -> Task:
        """"""
    @overload
    def WriteLineAsync(self, value: Char) -> Task:
        """"""
    @overload
    def WriteLineAsync(self, value: str) -> Task:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TextReader(ABC, MarshalByRefObject, IDisposable):
    """"""

    Null: ClassVar[TextReader]
    """"""
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
    def Peek(self) -> int:
        """"""
    @overload
    def Read(self) -> int:
        """"""
    @overload
    def Read(self, buffer: Array[Char], index: int, count: int) -> tuple[int, Array[Char]]:
        """"""
    def ReadAsync(self, buffer: Array[Char], index: int, count: int) -> Task[int]:
        """"""
    def ReadBlock(self, buffer: Array[Char], index: int, count: int) -> tuple[int, Array[Char]]:
        """"""
    def ReadBlockAsync(self, buffer: Array[Char], index: int, count: int) -> Task[int]:
        """"""
    def ReadLine(self) -> str:
        """"""
    def ReadLineAsync(self) -> Task[str]:
        """"""
    def ReadToEnd(self) -> str:
        """"""
    def ReadToEndAsync(self) -> Task[str]:
        """"""
    @classmethod
    def Synchronized(cls, reader: TextReader) -> TextReader:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TextWriter(ABC, MarshalByRefObject, IDisposable):
    """"""

    Null: ClassVar[TextWriter]
    """"""
    @property
    def Encoding(self) -> Encoding:
        """"""
    @property
    def FormatProvider(self) -> IFormatProvider:
        """"""
    @property
    def NewLine(self) -> str:
        """"""
    @NewLine.setter
    def NewLine(self, value: str) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    def FlushAsync(self) -> Task:
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
    def Synchronized(cls, writer: TextWriter) -> TextWriter:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Write(self, buffer: Array[Char]) -> None:
        """"""
    @overload
    def Write(self, buffer: Array[Char], index: int, count: int) -> None:
        """"""
    @overload
    def Write(self, value: bool) -> None:
        """"""
    @overload
    def Write(self, value: Char) -> None:
        """"""
    @overload
    def Write(self, value: Decimal) -> None:
        """"""
    @overload
    def Write(self, value: float) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, value: object) -> None:
        """"""
    @overload
    def Write(self, value: float) -> None:
        """"""
    @overload
    def Write(self, value: str) -> None:
        """"""
    @overload
    def Write(self, format: str, arg: Array[object]) -> None:
        """"""
    @overload
    def Write(self, format: str, arg0: object) -> None:
        """"""
    @overload
    def Write(self, format: str, arg0: object, arg1: object) -> None:
        """"""
    @overload
    def Write(self, format: str, arg0: object, arg1: object, arg2: object) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[Char]) -> Task:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[Char], index: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(self, value: Char) -> Task:
        """"""
    @overload
    def WriteAsync(self, value: str) -> Task:
        """"""
    @overload
    def WriteLine(self) -> None:
        """"""
    @overload
    def WriteLine(self, buffer: Array[Char]) -> None:
        """"""
    @overload
    def WriteLine(self, buffer: Array[Char], index: int, count: int) -> None:
        """"""
    @overload
    def WriteLine(self, value: bool) -> None:
        """"""
    @overload
    def WriteLine(self, value: Char) -> None:
        """"""
    @overload
    def WriteLine(self, value: Decimal) -> None:
        """"""
    @overload
    def WriteLine(self, value: float) -> None:
        """"""
    @overload
    def WriteLine(self, value: int) -> None:
        """"""
    @overload
    def WriteLine(self, value: int) -> None:
        """"""
    @overload
    def WriteLine(self, value: object) -> None:
        """"""
    @overload
    def WriteLine(self, value: float) -> None:
        """"""
    @overload
    def WriteLine(self, value: str) -> None:
        """"""
    @overload
    def WriteLine(self, format: str, arg: Array[object]) -> None:
        """"""
    @overload
    def WriteLine(self, format: str, arg0: object) -> None:
        """"""
    @overload
    def WriteLine(self, format: str, arg0: object, arg1: object) -> None:
        """"""
    @overload
    def WriteLine(self, format: str, arg0: object, arg1: object, arg2: object) -> None:
        """"""
    @overload
    def WriteLine(self, value: int) -> None:
        """"""
    @overload
    def WriteLine(self, value: int) -> None:
        """"""
    @overload
    def WriteLineAsync(self) -> Task:
        """"""
    @overload
    def WriteLineAsync(self, buffer: Array[Char]) -> Task:
        """"""
    @overload
    def WriteLineAsync(self, buffer: Array[Char], index: int, count: int) -> Task:
        """"""
    @overload
    def WriteLineAsync(self, value: Char) -> Task:
        """"""
    @overload
    def WriteLineAsync(self, value: str) -> Task:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class UnmanagedMemoryAccessor(Object, IDisposable):
    """"""
    @overload
    def __init__(self, buffer: SafeBuffer, offset: int, capacity: int) -> None:
        """"""
    @overload
    def __init__(self, buffer: SafeBuffer, offset: int, capacity: int, access: FileAccess) -> None:
        """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Read(self, position: int, structure: T) -> tuple[None, T]:
        """"""
    def ReadArray[T](self, position: int, array: Array[T], offset: int, count: int) -> int:
        """"""
    def ReadBoolean(self, position: int) -> bool:
        """"""
    def ReadByte(self, position: int) -> int:
        """"""
    def ReadChar(self, position: int) -> Char:
        """"""
    def ReadDecimal(self, position: int) -> Decimal:
        """"""
    def ReadDouble(self, position: int) -> float:
        """"""
    def ReadInt16(self, position: int) -> int:
        """"""
    def ReadInt32(self, position: int) -> int:
        """"""
    def ReadInt64(self, position: int) -> int:
        """"""
    def ReadSByte(self, position: int) -> int:
        """"""
    def ReadSingle(self, position: int) -> float:
        """"""
    def ReadUInt16(self, position: int) -> int:
        """"""
    def ReadUInt32(self, position: int) -> int:
        """"""
    def ReadUInt64(self, position: int) -> int:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Write(self, position: int, structure: T) -> None:
        """"""
    @overload
    def Write(self, position: int, value: bool) -> None:
        """"""
    @overload
    def Write(self, position: int, value: int) -> None:
        """"""
    @overload
    def Write(self, position: int, value: Char) -> None:
        """"""
    @overload
    def Write(self, position: int, value: Decimal) -> None:
        """"""
    @overload
    def Write(self, position: int, value: float) -> None:
        """"""
    @overload
    def Write(self, position: int, value: int) -> None:
        """"""
    @overload
    def Write(self, position: int, value: int) -> None:
        """"""
    @overload
    def Write(self, position: int, value: int) -> None:
        """"""
    @overload
    def Write(self, position: int, value: int) -> None:
        """"""
    @overload
    def Write(self, position: int, value: float) -> None:
        """"""
    @overload
    def Write(self, position: int, value: int) -> None:
        """"""
    @overload
    def Write(self, position: int, value: int) -> None:
        """"""
    @overload
    def Write(self, position: int, value: int) -> None:
        """"""
    def WriteArray[T](self, position: int, array: Array[T], offset: int, count: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class UnmanagedMemoryStream(Stream, IDisposable):
    """"""
    @overload
    def __init__(self, buffer: SafeBuffer, offset: int, length: int) -> None:
        """"""
    @overload
    def __init__(self, buffer: SafeBuffer, offset: int, length: int, access: FileAccess) -> None:
        """"""
    @overload
    def __init__(self, pointer: int, length: int) -> None:
        """"""
    @overload
    def __init__(self, pointer: int, length: int, capacity: int, access: FileAccess) -> None:
        """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def PositionPointer(self) -> int:
        """"""
    @PositionPointer.setter
    def PositionPointer(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, count: int) -> tuple[int, Array[int]]:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, loc: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class UnmanagedMemoryStreamWrapper(MemoryStream, IDisposable):
    """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetBuffer(self) -> Array[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, count: int) -> tuple[int, Array[int]]:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, loc: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToArray(self) -> Array[int]:
        """"""
    def ToString(self) -> str:
        """"""
    def TryGetBuffer(self, buffer: ArraySegment[int]) -> tuple[bool, ArraySegment[int]]:
        """"""
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""
    def WriteTo(self, stream: Stream) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class WaitForChangedResult(ValueType):
    """"""
    @property
    def ChangeType(self) -> WatcherChangeTypes:
        """"""
    @ChangeType.setter
    def ChangeType(self, value: WatcherChangeTypes) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def OldName(self) -> str:
        """"""
    @OldName.setter
    def OldName(self, value: str) -> None: ...
    @property
    def TimedOut(self) -> bool:
        """"""
    @TimedOut.setter
    def TimedOut(self, value: bool) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class WatcherChangeTypes(Enum):
    """"""

    Created: WatcherChangeTypes = ...
    """"""
    Deleted: WatcherChangeTypes = ...
    """"""
    Changed: WatcherChangeTypes = ...
    """"""
    Renamed: WatcherChangeTypes = ...
    """"""
    All: WatcherChangeTypes = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class __ConsoleStream(Stream, IDisposable):
    """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, count: int) -> tuple[int, Array[int]]:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class __Error(ABC, Object):
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
class __HResults(ABC, Object):
    """"""

    COR_E_DIRECTORYNOTFOUND: ClassVar[int]
    """"""
    COR_E_ENDOFSTREAM: ClassVar[int]
    """"""
    COR_E_FILELOAD: ClassVar[int]
    """"""
    COR_E_FILENOTFOUND: ClassVar[int]
    """"""
    COR_E_IO: ClassVar[int]
    """"""
    COR_E_PATHTOOLONG: ClassVar[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
