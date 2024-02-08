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

T = TypeVar("T")
TSource = TypeVar("TSource")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class BinaryReader(Object, IDisposable):
    """"""

    @overload
    def __init__(self, input: Stream):
        """

        :param input:
        """
    @overload
    def __init__(self, input: Stream, encoding: Encoding):
        """

        :param input:
        :param encoding:
        """
    @overload
    def __init__(self, input: Stream, encoding: Encoding, leaveOpen: bool):
        """

        :param input:
        :param encoding:
        :param leaveOpen:
        """
    @property
    def BaseStream(self) -> Stream:
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
    def PeekChar(self) -> int:
        """

        :return:
        """
    @overload
    def Read(self) -> int:
        """

        :return:
        """
    @overload
    def Read(self, buffer: Array[int], index: int, count: int) -> int:
        """

        :param buffer:
        :param index:
        :param count:
        :return:
        """
    @overload
    def Read(self, buffer: Array[Char], index: int, count: int) -> int:
        """

        :param buffer:
        :param index:
        :param count:
        :return:
        """
    def ReadBoolean(self) -> bool:
        """

        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def ReadBytes(self, count: int) -> Array[int]:
        """

        :param count:
        :return:
        """
    def ReadChar(self) -> Char:
        """

        :return:
        """
    def ReadChars(self, count: int) -> Array[Char]:
        """

        :param count:
        :return:
        """
    def ReadDecimal(self) -> Decimal:
        """

        :return:
        """
    def ReadDouble(self) -> float:
        """

        :return:
        """
    def ReadInt16(self) -> int:
        """

        :return:
        """
    def ReadInt32(self) -> int:
        """

        :return:
        """
    def ReadInt64(self) -> int:
        """

        :return:
        """
    def ReadSByte(self) -> int:
        """

        :return:
        """
    def ReadSingle(self) -> float:
        """

        :return:
        """
    def ReadString(self) -> str:
        """

        :return:
        """
    def ReadUInt16(self) -> int:
        """

        :return:
        """
    def ReadUInt32(self) -> int:
        """

        :return:
        """
    def ReadUInt64(self) -> int:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class BinaryWriter(Object, IDisposable):
    """"""

    Null: Final[ClassVar[BinaryWriter]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, output: Stream):
        """

        :param output:
        """
    @overload
    def __init__(self, output: Stream, encoding: Encoding):
        """

        :param output:
        :param encoding:
        """
    @overload
    def __init__(self, output: Stream, encoding: Encoding, leaveOpen: bool):
        """

        :param output:
        :param encoding:
        :param leaveOpen:
        """
    @property
    def BaseStream(self) -> Stream:
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
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Write(self, buffer: Array[int]) -> None:
        """

        :param buffer:
        """
    @overload
    def Write(self, chars: Array[Char]) -> None:
        """

        :param chars:
        """
    @overload
    def Write(self, value: bool) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, ch: Char) -> None:
        """

        :param ch:
        """
    @overload
    def Write(self, value: Decimal) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: float) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: float) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: str) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, buffer: Array[int], index: int, count: int) -> None:
        """

        :param buffer:
        :param index:
        :param count:
        """
    @overload
    def Write(self, chars: Array[Char], index: int, count: int) -> None:
        """

        :param chars:
        :param index:
        :param count:
        """

class BufferedStream(Stream, IDisposable):
    """"""

    @overload
    def __init__(self, stream: Stream):
        """

        :param stream:
        """
    @overload
    def __init__(self, stream: Stream, bufferSize: int):
        """

        :param stream:
        :param bufferSize:
        """
    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
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
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

class BufferedStream2(ABC, Stream, IDisposable):
    """"""

    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
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
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

class Direct(ABC, Object):
    """"""

    FILE_ACTION_ADDED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_ACTION_MODIFIED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_ACTION_REMOVED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_ACTION_RENAMED_NEW_NAME: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_ACTION_RENAMED_OLD_NAME: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_NOTIFY_CHANGE_ATTRIBUTES: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_NOTIFY_CHANGE_CREATION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_NOTIFY_CHANGE_DIR_NAME: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_NOTIFY_CHANGE_FILE_NAME: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_NOTIFY_CHANGE_LAST_ACCESS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_NOTIFY_CHANGE_LAST_WRITE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_NOTIFY_CHANGE_NAME: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_NOTIFY_CHANGE_SECURITY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_NOTIFY_CHANGE_SIZE: Final[ClassVar[int]] = ...
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

class Directory(ABC, Object):
    """"""

    @classmethod
    @overload
    def CreateDirectory(cls, path: str) -> DirectoryInfo:
        """

        :param path:
        :return:
        """
    @classmethod
    @overload
    def CreateDirectory(cls, path: str, directorySecurity: DirectorySecurity) -> DirectoryInfo:
        """

        :param path:
        :param directorySecurity:
        :return:
        """
    @classmethod
    @overload
    def Delete(cls, path: str) -> None:
        """

        :param path:
        """
    @classmethod
    @overload
    def Delete(cls, path: str, recursive: bool) -> None:
        """

        :param path:
        :param recursive:
        """
    @classmethod
    @overload
    def EnumerateDirectories(cls, path: str) -> IEnumerable[str]:
        """

        :param path:
        :return:
        """
    @classmethod
    @overload
    def EnumerateDirectories(cls, path: str, searchPattern: str) -> IEnumerable[str]:
        """

        :param path:
        :param searchPattern:
        :return:
        """
    @classmethod
    @overload
    def EnumerateDirectories(
        cls, path: str, searchPattern: str, searchOption: SearchOption
    ) -> IEnumerable[str]:
        """

        :param path:
        :param searchPattern:
        :param searchOption:
        :return:
        """
    @classmethod
    @overload
    def EnumerateFileSystemEntries(cls, path: str) -> IEnumerable[str]:
        """

        :param path:
        :return:
        """
    @classmethod
    @overload
    def EnumerateFileSystemEntries(cls, path: str, searchPattern: str) -> IEnumerable[str]:
        """

        :param path:
        :param searchPattern:
        :return:
        """
    @classmethod
    @overload
    def EnumerateFileSystemEntries(
        cls, path: str, searchPattern: str, searchOption: SearchOption
    ) -> IEnumerable[str]:
        """

        :param path:
        :param searchPattern:
        :param searchOption:
        :return:
        """
    @classmethod
    @overload
    def EnumerateFiles(cls, path: str) -> IEnumerable[str]:
        """

        :param path:
        :return:
        """
    @classmethod
    @overload
    def EnumerateFiles(cls, path: str, searchPattern: str) -> IEnumerable[str]:
        """

        :param path:
        :param searchPattern:
        :return:
        """
    @classmethod
    @overload
    def EnumerateFiles(
        cls, path: str, searchPattern: str, searchOption: SearchOption
    ) -> IEnumerable[str]:
        """

        :param path:
        :param searchPattern:
        :param searchOption:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def Exists(cls, path: str) -> bool:
        """

        :param path:
        :return:
        """
    @classmethod
    @overload
    def GetAccessControl(cls, path: str) -> DirectorySecurity:
        """

        :param path:
        :return:
        """
    @classmethod
    @overload
    def GetAccessControl(
        cls, path: str, includeSections: AccessControlSections
    ) -> DirectorySecurity:
        """

        :param path:
        :param includeSections:
        :return:
        """
    @classmethod
    def GetCreationTime(cls, path: str) -> DateTime:
        """

        :param path:
        :return:
        """
    @classmethod
    def GetCreationTimeUtc(cls, path: str) -> DateTime:
        """

        :param path:
        :return:
        """
    @classmethod
    def GetCurrentDirectory(cls) -> str:
        """

        :return:
        """
    @classmethod
    @overload
    def GetDirectories(cls, path: str) -> Array[str]:
        """

        :param path:
        :return:
        """
    @classmethod
    @overload
    def GetDirectories(cls, path: str, searchPattern: str) -> Array[str]:
        """

        :param path:
        :param searchPattern:
        :return:
        """
    @classmethod
    @overload
    def GetDirectories(
        cls, path: str, searchPattern: str, searchOption: SearchOption
    ) -> Array[str]:
        """

        :param path:
        :param searchPattern:
        :param searchOption:
        :return:
        """
    @classmethod
    def GetDirectoryRoot(cls, path: str) -> str:
        """

        :param path:
        :return:
        """
    @classmethod
    @overload
    def GetFileSystemEntries(cls, path: str) -> Array[str]:
        """

        :param path:
        :return:
        """
    @classmethod
    @overload
    def GetFileSystemEntries(cls, path: str, searchPattern: str) -> Array[str]:
        """

        :param path:
        :param searchPattern:
        :return:
        """
    @classmethod
    @overload
    def GetFileSystemEntries(
        cls, path: str, searchPattern: str, searchOption: SearchOption
    ) -> Array[str]:
        """

        :param path:
        :param searchPattern:
        :param searchOption:
        :return:
        """
    @classmethod
    @overload
    def GetFiles(cls, path: str) -> Array[str]:
        """

        :param path:
        :return:
        """
    @classmethod
    @overload
    def GetFiles(cls, path: str, searchPattern: str) -> Array[str]:
        """

        :param path:
        :param searchPattern:
        :return:
        """
    @classmethod
    @overload
    def GetFiles(cls, path: str, searchPattern: str, searchOption: SearchOption) -> Array[str]:
        """

        :param path:
        :param searchPattern:
        :param searchOption:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    def GetLastAccessTime(cls, path: str) -> DateTime:
        """

        :param path:
        :return:
        """
    @classmethod
    def GetLastAccessTimeUtc(cls, path: str) -> DateTime:
        """

        :param path:
        :return:
        """
    @classmethod
    def GetLastWriteTime(cls, path: str) -> DateTime:
        """

        :param path:
        :return:
        """
    @classmethod
    def GetLastWriteTimeUtc(cls, path: str) -> DateTime:
        """

        :param path:
        :return:
        """
    @classmethod
    def GetLogicalDrives(cls) -> Array[str]:
        """

        :return:
        """
    @classmethod
    def GetParent(cls, path: str) -> DirectoryInfo:
        """

        :param path:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def Move(cls, sourceDirName: str, destDirName: str) -> None:
        """

        :param sourceDirName:
        :param destDirName:
        """
    @classmethod
    def SetAccessControl(cls, path: str, directorySecurity: DirectorySecurity) -> None:
        """

        :param path:
        :param directorySecurity:
        """
    @classmethod
    def SetCreationTime(cls, path: str, creationTime: DateTime) -> None:
        """

        :param path:
        :param creationTime:
        """
    @classmethod
    def SetCreationTimeUtc(cls, path: str, creationTimeUtc: DateTime) -> None:
        """

        :param path:
        :param creationTimeUtc:
        """
    @classmethod
    def SetCurrentDirectory(cls, path: str) -> None:
        """

        :param path:
        """
    @classmethod
    def SetLastAccessTime(cls, path: str, lastAccessTime: DateTime) -> None:
        """

        :param path:
        :param lastAccessTime:
        """
    @classmethod
    def SetLastAccessTimeUtc(cls, path: str, lastAccessTimeUtc: DateTime) -> None:
        """

        :param path:
        :param lastAccessTimeUtc:
        """
    @classmethod
    def SetLastWriteTime(cls, path: str, lastWriteTime: DateTime) -> None:
        """

        :param path:
        :param lastWriteTime:
        """
    @classmethod
    def SetLastWriteTimeUtc(cls, path: str, lastWriteTimeUtc: DateTime) -> None:
        """

        :param path:
        :param lastWriteTimeUtc:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DirectoryInfo(FileSystemInfo, ISerializable):
    """"""

    def __init__(self, path: str):
        """

        :param path:
        """
    @property
    def Attributes(self) -> FileAttributes:
        """

        :return:
        """
    @Attributes.setter
    def Attributes(self, value: FileAttributes) -> None: ...
    @property
    def CreationTime(self) -> DateTime:
        """

        :return:
        """
    @CreationTime.setter
    def CreationTime(self, value: DateTime) -> None: ...
    @property
    def CreationTimeUtc(self) -> DateTime:
        """

        :return:
        """
    @CreationTimeUtc.setter
    def CreationTimeUtc(self, value: DateTime) -> None: ...
    @property
    def Exists(self) -> bool:
        """

        :return:
        """
    @property
    def Extension(self) -> str:
        """

        :return:
        """
    @property
    def FullName(self) -> str:
        """

        :return:
        """
    @property
    def LastAccessTime(self) -> DateTime:
        """

        :return:
        """
    @LastAccessTime.setter
    def LastAccessTime(self, value: DateTime) -> None: ...
    @property
    def LastAccessTimeUtc(self) -> DateTime:
        """

        :return:
        """
    @LastAccessTimeUtc.setter
    def LastAccessTimeUtc(self, value: DateTime) -> None: ...
    @property
    def LastWriteTime(self) -> DateTime:
        """

        :return:
        """
    @LastWriteTime.setter
    def LastWriteTime(self, value: DateTime) -> None: ...
    @property
    def LastWriteTimeUtc(self) -> DateTime:
        """

        :return:
        """
    @LastWriteTimeUtc.setter
    def LastWriteTimeUtc(self, value: DateTime) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Parent(self) -> DirectoryInfo:
        """

        :return:
        """
    @property
    def Root(self) -> DirectoryInfo:
        """

        :return:
        """
    @overload
    def Create(self) -> None:
        """"""
    @overload
    def Create(self, directorySecurity: DirectorySecurity) -> None:
        """

        :param directorySecurity:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    @overload
    def CreateSubdirectory(self, path: str) -> DirectoryInfo:
        """

        :param path:
        :return:
        """
    @overload
    def CreateSubdirectory(self, path: str, directorySecurity: DirectorySecurity) -> DirectoryInfo:
        """

        :param path:
        :param directorySecurity:
        :return:
        """
    @overload
    def Delete(self) -> None:
        """"""
    @overload
    def Delete(self, recursive: bool) -> None:
        """

        :param recursive:
        """
    @overload
    def EnumerateDirectories(self) -> IEnumerable[DirectoryInfo]:
        """

        :return:
        """
    @overload
    def EnumerateDirectories(self, searchPattern: str) -> IEnumerable[DirectoryInfo]:
        """

        :param searchPattern:
        :return:
        """
    @overload
    def EnumerateDirectories(
        self, searchPattern: str, searchOption: SearchOption
    ) -> IEnumerable[DirectoryInfo]:
        """

        :param searchPattern:
        :param searchOption:
        :return:
        """
    @overload
    def EnumerateFileSystemInfos(self) -> IEnumerable[FileSystemInfo]:
        """

        :return:
        """
    @overload
    def EnumerateFileSystemInfos(self, searchPattern: str) -> IEnumerable[FileSystemInfo]:
        """

        :param searchPattern:
        :return:
        """
    @overload
    def EnumerateFileSystemInfos(
        self, searchPattern: str, searchOption: SearchOption
    ) -> IEnumerable[FileSystemInfo]:
        """

        :param searchPattern:
        :param searchOption:
        :return:
        """
    @overload
    def EnumerateFiles(self) -> IEnumerable[FileInfo]:
        """

        :return:
        """
    @overload
    def EnumerateFiles(self, searchPattern: str) -> IEnumerable[FileInfo]:
        """

        :param searchPattern:
        :return:
        """
    @overload
    def EnumerateFiles(
        self, searchPattern: str, searchOption: SearchOption
    ) -> IEnumerable[FileInfo]:
        """

        :param searchPattern:
        :param searchOption:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetAccessControl(self) -> DirectorySecurity:
        """

        :return:
        """
    @overload
    def GetAccessControl(self, includeSections: AccessControlSections) -> DirectorySecurity:
        """

        :param includeSections:
        :return:
        """
    @overload
    def GetDirectories(self) -> Array[DirectoryInfo]:
        """

        :return:
        """
    @overload
    def GetDirectories(self, searchPattern: str) -> Array[DirectoryInfo]:
        """

        :param searchPattern:
        :return:
        """
    @overload
    def GetDirectories(
        self, searchPattern: str, searchOption: SearchOption
    ) -> Array[DirectoryInfo]:
        """

        :param searchPattern:
        :param searchOption:
        :return:
        """
    @overload
    def GetFileSystemInfos(self) -> Array[FileSystemInfo]:
        """

        :return:
        """
    @overload
    def GetFileSystemInfos(self, searchPattern: str) -> Array[FileSystemInfo]:
        """

        :param searchPattern:
        :return:
        """
    @overload
    def GetFileSystemInfos(
        self, searchPattern: str, searchOption: SearchOption
    ) -> Array[FileSystemInfo]:
        """

        :param searchPattern:
        :param searchOption:
        :return:
        """
    @overload
    def GetFiles(self) -> Array[FileInfo]:
        """

        :return:
        """
    @overload
    def GetFiles(self, searchPattern: str) -> Array[FileInfo]:
        """

        :param searchPattern:
        :return:
        """
    @overload
    def GetFiles(self, searchPattern: str, searchOption: SearchOption) -> Array[FileInfo]:
        """

        :param searchPattern:
        :param searchOption:
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
    def MoveTo(self, destDirName: str) -> None:
        """

        :param destDirName:
        """
    def Refresh(self) -> None:
        """"""
    def SetAccessControl(self, directorySecurity: DirectorySecurity) -> None:
        """

        :param directorySecurity:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DirectoryInfoResultHandler(SearchResultHandler[DirectoryInfo]):
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

class DirectoryNotFoundException(IOException, _Exception, ISerializable):
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

class DriveInfo(Object, ISerializable):
    """"""

    def __init__(self, driveName: str):
        """

        :param driveName:
        """
    @property
    def AvailableFreeSpace(self) -> int:
        """

        :return:
        """
    @property
    def DriveFormat(self) -> str:
        """

        :return:
        """
    @property
    def DriveType(self) -> DriveType:
        """

        :return:
        """
    @property
    def IsReady(self) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def RootDirectory(self) -> DirectoryInfo:
        """

        :return:
        """
    @property
    def TotalFreeSpace(self) -> int:
        """

        :return:
        """
    @property
    def TotalSize(self) -> int:
        """

        :return:
        """
    @property
    def VolumeLabel(self) -> str:
        """

        :return:
        """
    @VolumeLabel.setter
    def VolumeLabel(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetDrives(cls) -> Array[DriveInfo]:
        """

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

class DriveNotFoundException(IOException, _Exception, ISerializable):
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

class EndOfStreamException(IOException, _Exception, ISerializable):
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

class ErrorEventArgs(EventArgs):
    """"""

    def __init__(self, exception: Exception):
        """

        :param exception:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetException(self) -> Exception:
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

ErrorEventHandler: Callable[[object, ErrorEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class File(ABC, Object):
    """"""

    @classmethod
    @overload
    def AppendAllLines(cls, path: str, contents: IEnumerable[str]) -> None:
        """

        :param path:
        :param contents:
        """
    @classmethod
    @overload
    def AppendAllLines(cls, path: str, contents: IEnumerable[str], encoding: Encoding) -> None:
        """

        :param path:
        :param contents:
        :param encoding:
        """
    @classmethod
    @overload
    def AppendAllText(cls, path: str, contents: str) -> None:
        """

        :param path:
        :param contents:
        """
    @classmethod
    @overload
    def AppendAllText(cls, path: str, contents: str, encoding: Encoding) -> None:
        """

        :param path:
        :param contents:
        :param encoding:
        """
    @classmethod
    def AppendText(cls, path: str) -> StreamWriter:
        """

        :param path:
        :return:
        """
    @classmethod
    @overload
    def Copy(cls, sourceFileName: str, destFileName: str) -> None:
        """

        :param sourceFileName:
        :param destFileName:
        """
    @classmethod
    @overload
    def Copy(cls, sourceFileName: str, destFileName: str, overwrite: bool) -> None:
        """

        :param sourceFileName:
        :param destFileName:
        :param overwrite:
        """
    @classmethod
    @overload
    def Create(cls, path: str) -> FileStream:
        """

        :param path:
        :return:
        """
    @classmethod
    @overload
    def Create(cls, path: str, bufferSize: int) -> FileStream:
        """

        :param path:
        :param bufferSize:
        :return:
        """
    @classmethod
    @overload
    def Create(cls, path: str, bufferSize: int, options: FileOptions) -> FileStream:
        """

        :param path:
        :param bufferSize:
        :param options:
        :return:
        """
    @classmethod
    @overload
    def Create(
        cls, path: str, bufferSize: int, options: FileOptions, fileSecurity: FileSecurity
    ) -> FileStream:
        """

        :param path:
        :param bufferSize:
        :param options:
        :param fileSecurity:
        :return:
        """
    @classmethod
    def CreateText(cls, path: str) -> StreamWriter:
        """

        :param path:
        :return:
        """
    @classmethod
    def Decrypt(cls, path: str) -> None:
        """

        :param path:
        """
    @classmethod
    def Delete(cls, path: str) -> None:
        """

        :param path:
        """
    @classmethod
    def Encrypt(cls, path: str) -> None:
        """

        :param path:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def Exists(cls, path: str) -> bool:
        """

        :param path:
        :return:
        """
    @classmethod
    @overload
    def GetAccessControl(cls, path: str) -> FileSecurity:
        """

        :param path:
        :return:
        """
    @classmethod
    @overload
    def GetAccessControl(cls, path: str, includeSections: AccessControlSections) -> FileSecurity:
        """

        :param path:
        :param includeSections:
        :return:
        """
    @classmethod
    def GetAttributes(cls, path: str) -> FileAttributes:
        """

        :param path:
        :return:
        """
    @classmethod
    def GetCreationTime(cls, path: str) -> DateTime:
        """

        :param path:
        :return:
        """
    @classmethod
    def GetCreationTimeUtc(cls, path: str) -> DateTime:
        """

        :param path:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    def GetLastAccessTime(cls, path: str) -> DateTime:
        """

        :param path:
        :return:
        """
    @classmethod
    def GetLastAccessTimeUtc(cls, path: str) -> DateTime:
        """

        :param path:
        :return:
        """
    @classmethod
    def GetLastWriteTime(cls, path: str) -> DateTime:
        """

        :param path:
        :return:
        """
    @classmethod
    def GetLastWriteTimeUtc(cls, path: str) -> DateTime:
        """

        :param path:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def Move(cls, sourceFileName: str, destFileName: str) -> None:
        """

        :param sourceFileName:
        :param destFileName:
        """
    @classmethod
    @overload
    def Open(cls, path: str, mode: FileMode) -> FileStream:
        """

        :param path:
        :param mode:
        :return:
        """
    @classmethod
    @overload
    def Open(cls, path: str, mode: FileMode, access: FileAccess) -> FileStream:
        """

        :param path:
        :param mode:
        :param access:
        :return:
        """
    @classmethod
    @overload
    def Open(cls, path: str, mode: FileMode, access: FileAccess, share: FileShare) -> FileStream:
        """

        :param path:
        :param mode:
        :param access:
        :param share:
        :return:
        """
    @classmethod
    def OpenRead(cls, path: str) -> FileStream:
        """

        :param path:
        :return:
        """
    @classmethod
    def OpenText(cls, path: str) -> StreamReader:
        """

        :param path:
        :return:
        """
    @classmethod
    def OpenWrite(cls, path: str) -> FileStream:
        """

        :param path:
        :return:
        """
    @classmethod
    def ReadAllBytes(cls, path: str) -> Array[int]:
        """

        :param path:
        :return:
        """
    @classmethod
    @overload
    def ReadAllLines(cls, path: str) -> Array[str]:
        """

        :param path:
        :return:
        """
    @classmethod
    @overload
    def ReadAllLines(cls, path: str, encoding: Encoding) -> Array[str]:
        """

        :param path:
        :param encoding:
        :return:
        """
    @classmethod
    @overload
    def ReadAllText(cls, path: str) -> str:
        """

        :param path:
        :return:
        """
    @classmethod
    @overload
    def ReadAllText(cls, path: str, encoding: Encoding) -> str:
        """

        :param path:
        :param encoding:
        :return:
        """
    @classmethod
    @overload
    def ReadLines(cls, path: str) -> IEnumerable[str]:
        """

        :param path:
        :return:
        """
    @classmethod
    @overload
    def ReadLines(cls, path: str, encoding: Encoding) -> IEnumerable[str]:
        """

        :param path:
        :param encoding:
        :return:
        """
    @classmethod
    @overload
    def Replace(
        cls, sourceFileName: str, destinationFileName: str, destinationBackupFileName: str
    ) -> None:
        """

        :param sourceFileName:
        :param destinationFileName:
        :param destinationBackupFileName:
        """
    @classmethod
    @overload
    def Replace(
        cls,
        sourceFileName: str,
        destinationFileName: str,
        destinationBackupFileName: str,
        ignoreMetadataErrors: bool,
    ) -> None:
        """

        :param sourceFileName:
        :param destinationFileName:
        :param destinationBackupFileName:
        :param ignoreMetadataErrors:
        """
    @classmethod
    def SetAccessControl(cls, path: str, fileSecurity: FileSecurity) -> None:
        """

        :param path:
        :param fileSecurity:
        """
    @classmethod
    def SetAttributes(cls, path: str, fileAttributes: FileAttributes) -> None:
        """

        :param path:
        :param fileAttributes:
        """
    @classmethod
    def SetCreationTime(cls, path: str, creationTime: DateTime) -> None:
        """

        :param path:
        :param creationTime:
        """
    @classmethod
    def SetCreationTimeUtc(cls, path: str, creationTimeUtc: DateTime) -> None:
        """

        :param path:
        :param creationTimeUtc:
        """
    @classmethod
    def SetLastAccessTime(cls, path: str, lastAccessTime: DateTime) -> None:
        """

        :param path:
        :param lastAccessTime:
        """
    @classmethod
    def SetLastAccessTimeUtc(cls, path: str, lastAccessTimeUtc: DateTime) -> None:
        """

        :param path:
        :param lastAccessTimeUtc:
        """
    @classmethod
    def SetLastWriteTime(cls, path: str, lastWriteTime: DateTime) -> None:
        """

        :param path:
        :param lastWriteTime:
        """
    @classmethod
    def SetLastWriteTimeUtc(cls, path: str, lastWriteTimeUtc: DateTime) -> None:
        """

        :param path:
        :param lastWriteTimeUtc:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def WriteAllBytes(cls, path: str, bytes: Array[int]) -> None:
        """

        :param path:
        :param bytes:
        """
    @classmethod
    @overload
    def WriteAllLines(cls, path: str, contents: IEnumerable[str]) -> None:
        """

        :param path:
        :param contents:
        """
    @classmethod
    @overload
    def WriteAllLines(cls, path: str, contents: Array[str]) -> None:
        """

        :param path:
        :param contents:
        """
    @classmethod
    @overload
    def WriteAllLines(cls, path: str, contents: IEnumerable[str], encoding: Encoding) -> None:
        """

        :param path:
        :param contents:
        :param encoding:
        """
    @classmethod
    @overload
    def WriteAllLines(cls, path: str, contents: Array[str], encoding: Encoding) -> None:
        """

        :param path:
        :param contents:
        :param encoding:
        """
    @classmethod
    @overload
    def WriteAllText(cls, path: str, contents: str) -> None:
        """

        :param path:
        :param contents:
        """
    @classmethod
    @overload
    def WriteAllText(cls, path: str, contents: str, encoding: Encoding) -> None:
        """

        :param path:
        :param contents:
        :param encoding:
        """

class FileAccess(Enum):
    """"""

    Read: FileAccess = ...
    """"""
    Write: FileAccess = ...
    """"""
    ReadWrite: FileAccess = ...
    """"""

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

class FileInfo(FileSystemInfo, ISerializable):
    """"""

    def __init__(self, fileName: str):
        """

        :param fileName:
        """
    @property
    def Attributes(self) -> FileAttributes:
        """

        :return:
        """
    @Attributes.setter
    def Attributes(self, value: FileAttributes) -> None: ...
    @property
    def CreationTime(self) -> DateTime:
        """

        :return:
        """
    @CreationTime.setter
    def CreationTime(self, value: DateTime) -> None: ...
    @property
    def CreationTimeUtc(self) -> DateTime:
        """

        :return:
        """
    @CreationTimeUtc.setter
    def CreationTimeUtc(self, value: DateTime) -> None: ...
    @property
    def Directory(self) -> DirectoryInfo:
        """

        :return:
        """
    @property
    def DirectoryName(self) -> str:
        """

        :return:
        """
    @property
    def Exists(self) -> bool:
        """

        :return:
        """
    @property
    def Extension(self) -> str:
        """

        :return:
        """
    @property
    def FullName(self) -> str:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @IsReadOnly.setter
    def IsReadOnly(self, value: bool) -> None: ...
    @property
    def LastAccessTime(self) -> DateTime:
        """

        :return:
        """
    @LastAccessTime.setter
    def LastAccessTime(self, value: DateTime) -> None: ...
    @property
    def LastAccessTimeUtc(self) -> DateTime:
        """

        :return:
        """
    @LastAccessTimeUtc.setter
    def LastAccessTimeUtc(self, value: DateTime) -> None: ...
    @property
    def LastWriteTime(self) -> DateTime:
        """

        :return:
        """
    @LastWriteTime.setter
    def LastWriteTime(self, value: DateTime) -> None: ...
    @property
    def LastWriteTimeUtc(self) -> DateTime:
        """

        :return:
        """
    @LastWriteTimeUtc.setter
    def LastWriteTimeUtc(self, value: DateTime) -> None: ...
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    def AppendText(self) -> StreamWriter:
        """

        :return:
        """
    @overload
    def CopyTo(self, destFileName: str) -> FileInfo:
        """

        :param destFileName:
        :return:
        """
    @overload
    def CopyTo(self, destFileName: str, overwrite: bool) -> FileInfo:
        """

        :param destFileName:
        :param overwrite:
        :return:
        """
    def Create(self) -> FileStream:
        """

        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def CreateText(self) -> StreamWriter:
        """

        :return:
        """
    def Decrypt(self) -> None:
        """"""
    def Delete(self) -> None:
        """"""
    def Encrypt(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetAccessControl(self) -> FileSecurity:
        """

        :return:
        """
    @overload
    def GetAccessControl(self, includeSections: AccessControlSections) -> FileSecurity:
        """

        :param includeSections:
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
    def MoveTo(self, destFileName: str) -> None:
        """

        :param destFileName:
        """
    @overload
    def Open(self, mode: FileMode) -> FileStream:
        """

        :param mode:
        :return:
        """
    @overload
    def Open(self, mode: FileMode, access: FileAccess) -> FileStream:
        """

        :param mode:
        :param access:
        :return:
        """
    @overload
    def Open(self, mode: FileMode, access: FileAccess, share: FileShare) -> FileStream:
        """

        :param mode:
        :param access:
        :param share:
        :return:
        """
    def OpenRead(self) -> FileStream:
        """

        :return:
        """
    def OpenText(self) -> StreamReader:
        """

        :return:
        """
    def OpenWrite(self) -> FileStream:
        """

        :return:
        """
    def Refresh(self) -> None:
        """"""
    @overload
    def Replace(self, destinationFileName: str, destinationBackupFileName: str) -> FileInfo:
        """

        :param destinationFileName:
        :param destinationBackupFileName:
        :return:
        """
    @overload
    def Replace(
        self, destinationFileName: str, destinationBackupFileName: str, ignoreMetadataErrors: bool
    ) -> FileInfo:
        """

        :param destinationFileName:
        :param destinationBackupFileName:
        :param ignoreMetadataErrors:
        :return:
        """
    def SetAccessControl(self, fileSecurity: FileSecurity) -> None:
        """

        :param fileSecurity:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class FileInfoResultHandler(SearchResultHandler[FileInfo]):
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

class FileLoadException(IOException, _Exception, ISerializable):
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
    def __init__(self, message: str, inner: Exception):
        """

        :param message:
        :param inner:
        """
    @overload
    def __init__(self, message: str, fileName: str):
        """

        :param message:
        :param fileName:
        """
    @overload
    def __init__(self, message: str, fileName: str, inner: Exception):
        """

        :param message:
        :param fileName:
        :param inner:
        """
    @property
    def Data(self) -> IDictionary:
        """

        :return:
        """
    @property
    def FileName(self) -> str:
        """

        :return:
        """
    @property
    def FusionLog(self) -> str:
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

class FileNotFoundException(IOException, _Exception, ISerializable):
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
    @overload
    def __init__(self, message: str, fileName: str):
        """

        :param message:
        :param fileName:
        """
    @overload
    def __init__(self, message: str, fileName: str, innerException: Exception):
        """

        :param message:
        :param fileName:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """

        :return:
        """
    @property
    def FileName(self) -> str:
        """

        :return:
        """
    @property
    def FusionLog(self) -> str:
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

class FileStream(Stream, IDisposable):
    """"""

    @overload
    def __init__(self, handle: SafeFileHandle, access: FileAccess):
        """

        :param handle:
        :param access:
        """
    @overload
    def __init__(self, handle: IntPtr, access: FileAccess):
        """

        :param handle:
        :param access:
        """
    @overload
    def __init__(self, path: str, mode: FileMode):
        """

        :param path:
        :param mode:
        """
    @overload
    def __init__(self, handle: SafeFileHandle, access: FileAccess, bufferSize: int):
        """

        :param handle:
        :param access:
        :param bufferSize:
        """
    @overload
    def __init__(self, handle: IntPtr, access: FileAccess, ownsHandle: bool):
        """

        :param handle:
        :param access:
        :param ownsHandle:
        """
    @overload
    def __init__(self, path: str, mode: FileMode, access: FileAccess):
        """

        :param path:
        :param mode:
        :param access:
        """
    @overload
    def __init__(self, handle: SafeFileHandle, access: FileAccess, bufferSize: int, isAsync: bool):
        """

        :param handle:
        :param access:
        :param bufferSize:
        :param isAsync:
        """
    @overload
    def __init__(self, handle: IntPtr, access: FileAccess, ownsHandle: bool, bufferSize: int):
        """

        :param handle:
        :param access:
        :param ownsHandle:
        :param bufferSize:
        """
    @overload
    def __init__(self, path: str, mode: FileMode, access: FileAccess, share: FileShare):
        """

        :param path:
        :param mode:
        :param access:
        :param share:
        """
    @overload
    def __init__(
        self, handle: IntPtr, access: FileAccess, ownsHandle: bool, bufferSize: int, isAsync: bool
    ):
        """

        :param handle:
        :param access:
        :param ownsHandle:
        :param bufferSize:
        :param isAsync:
        """
    @overload
    def __init__(
        self, path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int
    ):
        """

        :param path:
        :param mode:
        :param access:
        :param share:
        :param bufferSize:
        """
    @overload
    def __init__(
        self,
        path: str,
        mode: FileMode,
        access: FileAccess,
        share: FileShare,
        bufferSize: int,
        options: FileOptions,
    ):
        """

        :param path:
        :param mode:
        :param access:
        :param share:
        :param bufferSize:
        :param options:
        """
    @overload
    def __init__(
        self,
        path: str,
        mode: FileMode,
        access: FileAccess,
        share: FileShare,
        bufferSize: int,
        useAsync: bool,
    ):
        """

        :param path:
        :param mode:
        :param access:
        :param share:
        :param bufferSize:
        :param useAsync:
        """
    @overload
    def __init__(
        self,
        path: str,
        mode: FileMode,
        rights: FileSystemRights,
        share: FileShare,
        bufferSize: int,
        options: FileOptions,
    ):
        """

        :param path:
        :param mode:
        :param rights:
        :param share:
        :param bufferSize:
        :param options:
        """
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
    ):
        """

        :param path:
        :param mode:
        :param rights:
        :param share:
        :param bufferSize:
        :param options:
        :param fileSecurity:
        """
    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Handle(self) -> IntPtr:
        """

        :return:
        """
    @property
    def IsAsync(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def SafeFileHandle(self) -> SafeFileHandle:
        """

        :return:
        """
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Flush(self) -> None:
        """"""
    @overload
    def Flush(self, flushToDisk: bool) -> None:
        """

        :param flushToDisk:
        """
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def GetAccessControl(self) -> FileSecurity:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Lock(self, position: int, length: int) -> None:
        """

        :param position:
        :param length:
        """
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetAccessControl(self, fileSecurity: FileSecurity) -> None:
        """

        :param fileSecurity:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Unlock(self, position: int, length: int) -> None:
        """

        :param position:
        :param length:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

class FileStreamAsyncResult(Object, IAsyncResult):
    """"""

    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
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

class FileSystemEnumerableFactory(ABC, Object):
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

class FileSystemEnumerableIterator(
    Generic[TSource],
    Iterator[TSource],
    IEnumerable[TSource],
    IEnumerator[TSource],
    IEnumerable,
    IEnumerator,
    IDisposable,
):
    """"""

    @property
    def Current(self) -> object:
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
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TSource]:
        """

        :return:
        """

class FileSystemEventArgs(EventArgs):
    """"""

    def __init__(self, changeType: WatcherChangeTypes, directory: str, name: str):
        """

        :param changeType:
        :param directory:
        :param name:
        """
    @property
    def ChangeType(self) -> WatcherChangeTypes:
        """

        :return:
        """
    @property
    def FullPath(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
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

FileSystemEventHandler: Callable[[object, FileSystemEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class FileSystemInfo(ABC, MarshalByRefObject, ISerializable):
    """"""

    @property
    def Attributes(self) -> FileAttributes:
        """

        :return:
        """
    @Attributes.setter
    def Attributes(self, value: FileAttributes) -> None: ...
    @property
    def CreationTime(self) -> DateTime:
        """

        :return:
        """
    @CreationTime.setter
    def CreationTime(self, value: DateTime) -> None: ...
    @property
    def CreationTimeUtc(self) -> DateTime:
        """

        :return:
        """
    @CreationTimeUtc.setter
    def CreationTimeUtc(self, value: DateTime) -> None: ...
    @property
    def Exists(self) -> bool:
        """

        :return:
        """
    @property
    def Extension(self) -> str:
        """

        :return:
        """
    @property
    def FullName(self) -> str:
        """

        :return:
        """
    @property
    def LastAccessTime(self) -> DateTime:
        """

        :return:
        """
    @LastAccessTime.setter
    def LastAccessTime(self, value: DateTime) -> None: ...
    @property
    def LastAccessTimeUtc(self) -> DateTime:
        """

        :return:
        """
    @LastAccessTimeUtc.setter
    def LastAccessTimeUtc(self, value: DateTime) -> None: ...
    @property
    def LastWriteTime(self) -> DateTime:
        """

        :return:
        """
    @LastWriteTime.setter
    def LastWriteTime(self, value: DateTime) -> None: ...
    @property
    def LastWriteTimeUtc(self) -> DateTime:
        """

        :return:
        """
    @LastWriteTimeUtc.setter
    def LastWriteTimeUtc(self, value: DateTime) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Delete(self) -> None:
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
    def Refresh(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class FileSystemInfoResultHandler(SearchResultHandler[FileSystemInfo]):
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

class FileSystemWatcher(Component, IComponent, ISupportInitialize, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, path: str):
        """

        :param path:
        """
    @overload
    def __init__(self, path: str, filter: str):
        """

        :param path:
        :param filter:
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
    def Filter(self) -> str:
        """

        :return:
        """
    @Filter.setter
    def Filter(self, value: str) -> None: ...
    @property
    def IncludeSubdirectories(self) -> bool:
        """

        :return:
        """
    @IncludeSubdirectories.setter
    def IncludeSubdirectories(self, value: bool) -> None: ...
    @property
    def InternalBufferSize(self) -> int:
        """

        :return:
        """
    @InternalBufferSize.setter
    def InternalBufferSize(self, value: int) -> None: ...
    @property
    def NotifyFilter(self) -> NotifyFilters:
        """

        :return:
        """
    @NotifyFilter.setter
    def NotifyFilter(self, value: NotifyFilters) -> None: ...
    @property
    def Path(self) -> str:
        """

        :return:
        """
    @Path.setter
    def Path(self, value: str) -> None: ...
    @property
    def Site(self) -> ISite:
        """

        :return:
        """
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke:
        """

        :return:
        """
    @SynchronizingObject.setter
    def SynchronizingObject(self, value: ISynchronizeInvoke) -> None: ...
    def BeginInit(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
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
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def WaitForChanged(self, changeType: WatcherChangeTypes) -> WaitForChangedResult:
        """

        :param changeType:
        :return:
        """
    @overload
    def WaitForChanged(self, changeType: WatcherChangeTypes, timeout: int) -> WaitForChangedResult:
        """

        :param changeType:
        :param timeout:
        :return:
        """
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

class HandleInheritability(Enum):
    """"""

    _None: HandleInheritability = ...
    """"""
    Inheritable: HandleInheritability = ...
    """"""

class IODescriptionAttribute(DescriptionAttribute, _Attribute):
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

class IOException(SystemException, _Exception, ISerializable):
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
    @overload
    def __init__(self, message: str, hresult: int):
        """

        :param message:
        :param hresult:
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

class InternalBufferOverflowException(SystemException, _Exception, ISerializable):
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
    def __init__(self, message: str, inner: Exception):
        """

        :param message:
        :param inner:
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

class InvalidDataException(SystemException, _Exception, ISerializable):
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

class Iterator(
    ABC,
    Generic[TSource],
    Object,
    IEnumerable[TSource],
    IEnumerator[TSource],
    IEnumerable,
    IEnumerator,
    IDisposable,
):
    """"""

    def __init__(self):
        """"""
    @property
    def Current(self) -> object:
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
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TSource]:
        """

        :return:
        """

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

class LogStream(BufferedStream2, IDisposable):
    """"""

    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
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
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

class LongPath(ABC, Object):
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

class LongPathDirectory(ABC, Object):
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

class LongPathFile(ABC, Object):
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

class LongPathHelper(Object):
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

class MemoryStream(Stream, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, buffer: Array[int]):
        """

        :param buffer:
        """
    @overload
    def __init__(self, capacity: int):
        """

        :param capacity:
        """
    @overload
    def __init__(self, buffer: Array[int], writable: bool):
        """

        :param buffer:
        :param writable:
        """
    @overload
    def __init__(self, buffer: Array[int], index: int, count: int):
        """

        :param buffer:
        :param index:
        :param count:
        """
    @overload
    def __init__(self, buffer: Array[int], index: int, count: int, writable: bool):
        """

        :param buffer:
        :param index:
        :param count:
        :param writable:
        """
    @overload
    def __init__(
        self, buffer: Array[int], index: int, count: int, writable: bool, publiclyVisible: bool
    ):
        """

        :param buffer:
        :param index:
        :param count:
        :param writable:
        :param publiclyVisible:
        """
    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def GetBuffer(self) -> Array[int]:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToArray(self) -> Array[int]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TryGetBuffer(self, buffer: ArraySegment[int]) -> Tuple[bool, ArraySegment[int]]:
        """

        :param buffer:
        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """
    def WriteTo(self, stream: Stream) -> None:
        """

        :param stream:
        """

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

class Path(ABC, Object):
    """"""

    AltDirectorySeparatorChar: Final[ClassVar[Char]] = ...
    """
    
    :return: 
    """
    DirectorySeparatorChar: Final[ClassVar[Char]] = ...
    """
    
    :return: 
    """
    InvalidPathChars: Final[ClassVar[Array[Char]]] = ...
    """
    
    :return: 
    """
    PathSeparator: Final[ClassVar[Char]] = ...
    """
    
    :return: 
    """
    VolumeSeparatorChar: Final[ClassVar[Char]] = ...
    """
    
    :return: 
    """
    @classmethod
    def ChangeExtension(cls, path: str, extension: str) -> str:
        """

        :param path:
        :param extension:
        :return:
        """
    @classmethod
    @overload
    def Combine(cls, paths: Array[str]) -> str:
        """

        :param paths:
        :return:
        """
    @classmethod
    @overload
    def Combine(cls, path1: str, path2: str) -> str:
        """

        :param path1:
        :param path2:
        :return:
        """
    @classmethod
    @overload
    def Combine(cls, path1: str, path2: str, path3: str) -> str:
        """

        :param path1:
        :param path2:
        :param path3:
        :return:
        """
    @classmethod
    @overload
    def Combine(cls, path1: str, path2: str, path3: str, path4: str) -> str:
        """

        :param path1:
        :param path2:
        :param path3:
        :param path4:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetDirectoryName(cls, path: str) -> str:
        """

        :param path:
        :return:
        """
    @classmethod
    def GetExtension(cls, path: str) -> str:
        """

        :param path:
        :return:
        """
    @classmethod
    def GetFileName(cls, path: str) -> str:
        """

        :param path:
        :return:
        """
    @classmethod
    def GetFileNameWithoutExtension(cls, path: str) -> str:
        """

        :param path:
        :return:
        """
    @classmethod
    def GetFullPath(cls, path: str) -> str:
        """

        :param path:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    def GetInvalidFileNameChars(cls) -> Array[Char]:
        """

        :return:
        """
    @classmethod
    def GetInvalidPathChars(cls) -> Array[Char]:
        """

        :return:
        """
    @classmethod
    def GetPathRoot(cls, path: str) -> str:
        """

        :param path:
        :return:
        """
    @classmethod
    def GetRandomFileName(cls) -> str:
        """

        :return:
        """
    @classmethod
    def GetTempFileName(cls) -> str:
        """

        :return:
        """
    @classmethod
    def GetTempPath(cls) -> str:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def HasExtension(cls, path: str) -> bool:
        """

        :param path:
        :return:
        """
    @classmethod
    def IsPathRooted(cls, path: str) -> bool:
        """

        :param path:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class PathHelper(ValueType):
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

class PathInternal(ABC, Object):
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

class PathTooLongException(IOException, _Exception, ISerializable):
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

class PatternMatcher(ABC, Object):
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
    def StrictMatchPattern(cls, expression: str, name: str) -> bool:
        """

        :param expression:
        :param name:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class PinnedBufferMemoryStream(UnmanagedMemoryStream, IDisposable):
    """"""

    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def PositionPointer(self) -> int:
        """

        :return:
        """
    @PositionPointer.setter
    def PositionPointer(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
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
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

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
    def Current(self) -> object:
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
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[str]:
        """

        :return:
        """

class RenamedEventArgs(FileSystemEventArgs):
    """"""

    def __init__(self, changeType: WatcherChangeTypes, directory: str, name: str, oldName: str):
        """

        :param changeType:
        :param directory:
        :param name:
        :param oldName:
        """
    @property
    def ChangeType(self) -> WatcherChangeTypes:
        """

        :return:
        """
    @property
    def FullPath(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def OldFullPath(self) -> str:
        """

        :return:
        """
    @property
    def OldName(self) -> str:
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

RenamedEventHandler: Callable[[object, RenamedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class SearchOption(Enum):
    """"""

    TopDirectoryOnly: SearchOption = ...
    """"""
    AllDirectories: SearchOption = ...
    """"""

class SearchResultHandler(ABC, Generic[TSource], Object):
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

class SeekOrigin(Enum):
    """"""

    Begin: SeekOrigin = ...
    """"""
    Current: SeekOrigin = ...
    """"""
    End: SeekOrigin = ...
    """"""

class Stream(ABC, MarshalByRefObject, IDisposable):
    """"""

    Null: Final[ClassVar[Stream]] = ...
    """
    
    :return: 
    """
    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
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
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    @classmethod
    def Synchronized(cls, stream: Stream) -> Stream:
        """

        :param stream:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

class StreamReader(TextReader, IDisposable):
    """"""

    Null: Final[ClassVar[StreamReader]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, stream: Stream):
        """

        :param stream:
        """
    @overload
    def __init__(self, path: str):
        """

        :param path:
        """
    @overload
    def __init__(self, stream: Stream, encoding: Encoding):
        """

        :param stream:
        :param encoding:
        """
    @overload
    def __init__(self, stream: Stream, detectEncodingFromByteOrderMarks: bool):
        """

        :param stream:
        :param detectEncodingFromByteOrderMarks:
        """
    @overload
    def __init__(self, path: str, encoding: Encoding):
        """

        :param path:
        :param encoding:
        """
    @overload
    def __init__(self, path: str, detectEncodingFromByteOrderMarks: bool):
        """

        :param path:
        :param detectEncodingFromByteOrderMarks:
        """
    @overload
    def __init__(self, stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool):
        """

        :param stream:
        :param encoding:
        :param detectEncodingFromByteOrderMarks:
        """
    @overload
    def __init__(self, path: str, encoding: Encoding, detectEncodingFromByteOrderMarks: bool):
        """

        :param path:
        :param encoding:
        :param detectEncodingFromByteOrderMarks:
        """
    @overload
    def __init__(
        self,
        stream: Stream,
        encoding: Encoding,
        detectEncodingFromByteOrderMarks: bool,
        bufferSize: int,
    ):
        """

        :param stream:
        :param encoding:
        :param detectEncodingFromByteOrderMarks:
        :param bufferSize:
        """
    @overload
    def __init__(
        self, path: str, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int
    ):
        """

        :param path:
        :param encoding:
        :param detectEncodingFromByteOrderMarks:
        :param bufferSize:
        """
    @overload
    def __init__(
        self,
        stream: Stream,
        encoding: Encoding,
        detectEncodingFromByteOrderMarks: bool,
        bufferSize: int,
        leaveOpen: bool,
    ):
        """

        :param stream:
        :param encoding:
        :param detectEncodingFromByteOrderMarks:
        :param bufferSize:
        :param leaveOpen:
        """
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
    @property
    def EndOfStream(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def DiscardBufferedData(self) -> None:
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
    def Peek(self) -> int:
        """

        :return:
        """
    @overload
    def Read(self) -> int:
        """

        :return:
        """
    @overload
    def Read(self, buffer: Array[Char], index: int, count: int) -> Tuple[int, Array[Char]]:
        """

        :param buffer:
        :param index:
        :param count:
        :return:
        """
    def ReadAsync(self, buffer: Array[Char], index: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param index:
        :param count:
        :return:
        """
    def ReadBlock(self, buffer: Array[Char], index: int, count: int) -> Tuple[int, Array[Char]]:
        """

        :param buffer:
        :param index:
        :param count:
        :return:
        """
    def ReadBlockAsync(self, buffer: Array[Char], index: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param index:
        :param count:
        :return:
        """
    def ReadLine(self) -> str:
        """

        :return:
        """
    def ReadLineAsync(self) -> Task[str]:
        """

        :return:
        """
    def ReadToEnd(self) -> str:
        """

        :return:
        """
    def ReadToEndAsync(self) -> Task[str]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class StreamWriter(TextWriter, IDisposable):
    """"""

    Null: Final[ClassVar[StreamWriter]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, stream: Stream):
        """

        :param stream:
        """
    @overload
    def __init__(self, path: str):
        """

        :param path:
        """
    @overload
    def __init__(self, stream: Stream, encoding: Encoding):
        """

        :param stream:
        :param encoding:
        """
    @overload
    def __init__(self, path: str, append: bool):
        """

        :param path:
        :param append:
        """
    @overload
    def __init__(self, stream: Stream, encoding: Encoding, bufferSize: int):
        """

        :param stream:
        :param encoding:
        :param bufferSize:
        """
    @overload
    def __init__(self, path: str, append: bool, encoding: Encoding):
        """

        :param path:
        :param append:
        :param encoding:
        """
    @overload
    def __init__(self, stream: Stream, encoding: Encoding, bufferSize: int, leaveOpen: bool):
        """

        :param stream:
        :param encoding:
        :param bufferSize:
        :param leaveOpen:
        """
    @overload
    def __init__(self, path: str, append: bool, encoding: Encoding, bufferSize: int):
        """

        :param path:
        :param append:
        :param encoding:
        :param bufferSize:
        """
    @property
    def AutoFlush(self) -> bool:
        """

        :return:
        """
    @AutoFlush.setter
    def AutoFlush(self, value: bool) -> None: ...
    @property
    def BaseStream(self) -> Stream:
        """

        :return:
        """
    @property
    def Encoding(self) -> Encoding:
        """

        :return:
        """
    @property
    def FormatProvider(self) -> IFormatProvider:
        """

        :return:
        """
    @property
    def NewLine(self) -> str:
        """

        :return:
        """
    @NewLine.setter
    def NewLine(self, value: str) -> None: ...
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
    def Flush(self) -> None:
        """"""
    def FlushAsync(self) -> Task:
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
    def Write(self, buffer: Array[Char]) -> None:
        """

        :param buffer:
        """
    @overload
    def Write(self, value: bool) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: Char) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: Decimal) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: float) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: object) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: float) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: str) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, format: str, arg: Array[object]) -> None:
        """

        :param format:
        :param arg:
        """
    @overload
    def Write(self, format: str, arg0: object) -> None:
        """

        :param format:
        :param arg0:
        """
    @overload
    def Write(self, buffer: Array[Char], index: int, count: int) -> None:
        """

        :param buffer:
        :param index:
        :param count:
        """
    @overload
    def Write(self, format: str, arg0: object, arg1: object) -> None:
        """

        :param format:
        :param arg0:
        :param arg1:
        """
    @overload
    def Write(self, format: str, arg0: object, arg1: object, arg2: object) -> None:
        """

        :param format:
        :param arg0:
        :param arg1:
        :param arg2:
        """
    @overload
    def WriteAsync(self, buffer: Array[Char]) -> Task:
        """

        :param buffer:
        :return:
        """
    @overload
    def WriteAsync(self, value: Char) -> Task:
        """

        :param value:
        :return:
        """
    @overload
    def WriteAsync(self, value: str) -> Task:
        """

        :param value:
        :return:
        """
    @overload
    def WriteAsync(self, buffer: Array[Char], index: int, count: int) -> Task:
        """

        :param buffer:
        :param index:
        :param count:
        :return:
        """
    @overload
    def WriteLine(self) -> None:
        """"""
    @overload
    def WriteLine(self, buffer: Array[Char]) -> None:
        """

        :param buffer:
        """
    @overload
    def WriteLine(self, value: bool) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: Char) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: Decimal) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: float) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: object) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: float) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: str) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, format: str, arg: Array[object]) -> None:
        """

        :param format:
        :param arg:
        """
    @overload
    def WriteLine(self, format: str, arg0: object) -> None:
        """

        :param format:
        :param arg0:
        """
    @overload
    def WriteLine(self, buffer: Array[Char], index: int, count: int) -> None:
        """

        :param buffer:
        :param index:
        :param count:
        """
    @overload
    def WriteLine(self, format: str, arg0: object, arg1: object) -> None:
        """

        :param format:
        :param arg0:
        :param arg1:
        """
    @overload
    def WriteLine(self, format: str, arg0: object, arg1: object, arg2: object) -> None:
        """

        :param format:
        :param arg0:
        :param arg1:
        :param arg2:
        """
    @overload
    def WriteLineAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def WriteLineAsync(self, buffer: Array[Char]) -> Task:
        """

        :param buffer:
        :return:
        """
    @overload
    def WriteLineAsync(self, value: Char) -> Task:
        """

        :param value:
        :return:
        """
    @overload
    def WriteLineAsync(self, value: str) -> Task:
        """

        :param value:
        :return:
        """
    @overload
    def WriteLineAsync(self, buffer: Array[Char], index: int, count: int) -> Task:
        """

        :param buffer:
        :param index:
        :param count:
        :return:
        """

class StringReader(TextReader, IDisposable):
    """"""

    def __init__(self, s: str):
        """

        :param s:
        """
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
    def Peek(self) -> int:
        """

        :return:
        """
    @overload
    def Read(self) -> int:
        """

        :return:
        """
    @overload
    def Read(self, buffer: Array[Char], index: int, count: int) -> Tuple[int, Array[Char]]:
        """

        :param buffer:
        :param index:
        :param count:
        :return:
        """
    def ReadAsync(self, buffer: Array[Char], index: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param index:
        :param count:
        :return:
        """
    def ReadBlock(self, buffer: Array[Char], index: int, count: int) -> Tuple[int, Array[Char]]:
        """

        :param buffer:
        :param index:
        :param count:
        :return:
        """
    def ReadBlockAsync(self, buffer: Array[Char], index: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param index:
        :param count:
        :return:
        """
    def ReadLine(self) -> str:
        """

        :return:
        """
    def ReadLineAsync(self) -> Task[str]:
        """

        :return:
        """
    def ReadToEnd(self) -> str:
        """

        :return:
        """
    def ReadToEndAsync(self) -> Task[str]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class StringResultHandler(SearchResultHandler[String]):
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

class StringWriter(TextWriter, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, sb: StringBuilder):
        """

        :param sb:
        """
    @overload
    def __init__(self, formatProvider: IFormatProvider):
        """

        :param formatProvider:
        """
    @overload
    def __init__(self, sb: StringBuilder, formatProvider: IFormatProvider):
        """

        :param sb:
        :param formatProvider:
        """
    @property
    def Encoding(self) -> Encoding:
        """

        :return:
        """
    @property
    def FormatProvider(self) -> IFormatProvider:
        """

        :return:
        """
    @property
    def NewLine(self) -> str:
        """

        :return:
        """
    @NewLine.setter
    def NewLine(self, value: str) -> None: ...
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
    def Flush(self) -> None:
        """"""
    def FlushAsync(self) -> Task:
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
    def GetStringBuilder(self) -> StringBuilder:
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
    def Write(self, buffer: Array[Char]) -> None:
        """

        :param buffer:
        """
    @overload
    def Write(self, value: bool) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: Char) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: Decimal) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: float) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: object) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: float) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: str) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, format: str, arg: Array[object]) -> None:
        """

        :param format:
        :param arg:
        """
    @overload
    def Write(self, format: str, arg0: object) -> None:
        """

        :param format:
        :param arg0:
        """
    @overload
    def Write(self, buffer: Array[Char], index: int, count: int) -> None:
        """

        :param buffer:
        :param index:
        :param count:
        """
    @overload
    def Write(self, format: str, arg0: object, arg1: object) -> None:
        """

        :param format:
        :param arg0:
        :param arg1:
        """
    @overload
    def Write(self, format: str, arg0: object, arg1: object, arg2: object) -> None:
        """

        :param format:
        :param arg0:
        :param arg1:
        :param arg2:
        """
    @overload
    def WriteAsync(self, buffer: Array[Char]) -> Task:
        """

        :param buffer:
        :return:
        """
    @overload
    def WriteAsync(self, value: Char) -> Task:
        """

        :param value:
        :return:
        """
    @overload
    def WriteAsync(self, value: str) -> Task:
        """

        :param value:
        :return:
        """
    @overload
    def WriteAsync(self, buffer: Array[Char], index: int, count: int) -> Task:
        """

        :param buffer:
        :param index:
        :param count:
        :return:
        """
    @overload
    def WriteLine(self) -> None:
        """"""
    @overload
    def WriteLine(self, buffer: Array[Char]) -> None:
        """

        :param buffer:
        """
    @overload
    def WriteLine(self, value: bool) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: Char) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: Decimal) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: float) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: object) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: float) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: str) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, format: str, arg: Array[object]) -> None:
        """

        :param format:
        :param arg:
        """
    @overload
    def WriteLine(self, format: str, arg0: object) -> None:
        """

        :param format:
        :param arg0:
        """
    @overload
    def WriteLine(self, buffer: Array[Char], index: int, count: int) -> None:
        """

        :param buffer:
        :param index:
        :param count:
        """
    @overload
    def WriteLine(self, format: str, arg0: object, arg1: object) -> None:
        """

        :param format:
        :param arg0:
        :param arg1:
        """
    @overload
    def WriteLine(self, format: str, arg0: object, arg1: object, arg2: object) -> None:
        """

        :param format:
        :param arg0:
        :param arg1:
        :param arg2:
        """
    @overload
    def WriteLineAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def WriteLineAsync(self, buffer: Array[Char]) -> Task:
        """

        :param buffer:
        :return:
        """
    @overload
    def WriteLineAsync(self, value: Char) -> Task:
        """

        :param value:
        :return:
        """
    @overload
    def WriteLineAsync(self, value: str) -> Task:
        """

        :param value:
        :return:
        """
    @overload
    def WriteLineAsync(self, buffer: Array[Char], index: int, count: int) -> Task:
        """

        :param buffer:
        :param index:
        :param count:
        :return:
        """

class TextReader(ABC, MarshalByRefObject, IDisposable):
    """"""

    Null: Final[ClassVar[TextReader]] = ...
    """
    
    :return: 
    """
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
    def Peek(self) -> int:
        """

        :return:
        """
    @overload
    def Read(self) -> int:
        """

        :return:
        """
    @overload
    def Read(self, buffer: Array[Char], index: int, count: int) -> Tuple[int, Array[Char]]:
        """

        :param buffer:
        :param index:
        :param count:
        :return:
        """
    def ReadAsync(self, buffer: Array[Char], index: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param index:
        :param count:
        :return:
        """
    def ReadBlock(self, buffer: Array[Char], index: int, count: int) -> Tuple[int, Array[Char]]:
        """

        :param buffer:
        :param index:
        :param count:
        :return:
        """
    def ReadBlockAsync(self, buffer: Array[Char], index: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param index:
        :param count:
        :return:
        """
    def ReadLine(self) -> str:
        """

        :return:
        """
    def ReadLineAsync(self) -> Task[str]:
        """

        :return:
        """
    def ReadToEnd(self) -> str:
        """

        :return:
        """
    def ReadToEndAsync(self) -> Task[str]:
        """

        :return:
        """
    @classmethod
    def Synchronized(cls, reader: TextReader) -> TextReader:
        """

        :param reader:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class TextWriter(ABC, MarshalByRefObject, IDisposable):
    """"""

    Null: Final[ClassVar[TextWriter]] = ...
    """
    
    :return: 
    """
    @property
    def Encoding(self) -> Encoding:
        """

        :return:
        """
    @property
    def FormatProvider(self) -> IFormatProvider:
        """

        :return:
        """
    @property
    def NewLine(self) -> str:
        """

        :return:
        """
    @NewLine.setter
    def NewLine(self, value: str) -> None: ...
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
    def Flush(self) -> None:
        """"""
    def FlushAsync(self) -> Task:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    @classmethod
    def Synchronized(cls, writer: TextWriter) -> TextWriter:
        """

        :param writer:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Write(self, buffer: Array[Char]) -> None:
        """

        :param buffer:
        """
    @overload
    def Write(self, value: bool) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: Char) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: Decimal) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: float) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: object) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: float) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: str) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, format: str, arg: Array[object]) -> None:
        """

        :param format:
        :param arg:
        """
    @overload
    def Write(self, format: str, arg0: object) -> None:
        """

        :param format:
        :param arg0:
        """
    @overload
    def Write(self, buffer: Array[Char], index: int, count: int) -> None:
        """

        :param buffer:
        :param index:
        :param count:
        """
    @overload
    def Write(self, format: str, arg0: object, arg1: object) -> None:
        """

        :param format:
        :param arg0:
        :param arg1:
        """
    @overload
    def Write(self, format: str, arg0: object, arg1: object, arg2: object) -> None:
        """

        :param format:
        :param arg0:
        :param arg1:
        :param arg2:
        """
    @overload
    def WriteAsync(self, buffer: Array[Char]) -> Task:
        """

        :param buffer:
        :return:
        """
    @overload
    def WriteAsync(self, value: Char) -> Task:
        """

        :param value:
        :return:
        """
    @overload
    def WriteAsync(self, value: str) -> Task:
        """

        :param value:
        :return:
        """
    @overload
    def WriteAsync(self, buffer: Array[Char], index: int, count: int) -> Task:
        """

        :param buffer:
        :param index:
        :param count:
        :return:
        """
    @overload
    def WriteLine(self) -> None:
        """"""
    @overload
    def WriteLine(self, buffer: Array[Char]) -> None:
        """

        :param buffer:
        """
    @overload
    def WriteLine(self, value: bool) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: Char) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: Decimal) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: float) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: object) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: float) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: str) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, format: str, arg: Array[object]) -> None:
        """

        :param format:
        :param arg:
        """
    @overload
    def WriteLine(self, format: str, arg0: object) -> None:
        """

        :param format:
        :param arg0:
        """
    @overload
    def WriteLine(self, buffer: Array[Char], index: int, count: int) -> None:
        """

        :param buffer:
        :param index:
        :param count:
        """
    @overload
    def WriteLine(self, format: str, arg0: object, arg1: object) -> None:
        """

        :param format:
        :param arg0:
        :param arg1:
        """
    @overload
    def WriteLine(self, format: str, arg0: object, arg1: object, arg2: object) -> None:
        """

        :param format:
        :param arg0:
        :param arg1:
        :param arg2:
        """
    @overload
    def WriteLineAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def WriteLineAsync(self, buffer: Array[Char]) -> Task:
        """

        :param buffer:
        :return:
        """
    @overload
    def WriteLineAsync(self, value: Char) -> Task:
        """

        :param value:
        :return:
        """
    @overload
    def WriteLineAsync(self, value: str) -> Task:
        """

        :param value:
        :return:
        """
    @overload
    def WriteLineAsync(self, buffer: Array[Char], index: int, count: int) -> Task:
        """

        :param buffer:
        :param index:
        :param count:
        :return:
        """

class UnmanagedMemoryAccessor(Object, IDisposable):
    """"""

    @overload
    def __init__(self, buffer: SafeBuffer, offset: int, capacity: int):
        """

        :param buffer:
        :param offset:
        :param capacity:
        """
    @overload
    def __init__(self, buffer: SafeBuffer, offset: int, capacity: int, access: FileAccess):
        """

        :param buffer:
        :param offset:
        :param capacity:
        :param access:
        """
    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Capacity(self) -> int:
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
    def Read(self, position: int, structure: T) -> Tuple[None, T]:
        """

        :param position:
        :param structure:
        """
    def ReadArray(self, position: int, array: Array[T], offset: int, count: int) -> int:
        """

        :param position:
        :param array:
        :param offset:
        :param count:
        :return:
        """
    def ReadBoolean(self, position: int) -> bool:
        """

        :param position:
        :return:
        """
    def ReadByte(self, position: int) -> int:
        """

        :param position:
        :return:
        """
    def ReadChar(self, position: int) -> Char:
        """

        :param position:
        :return:
        """
    def ReadDecimal(self, position: int) -> Decimal:
        """

        :param position:
        :return:
        """
    def ReadDouble(self, position: int) -> float:
        """

        :param position:
        :return:
        """
    def ReadInt16(self, position: int) -> int:
        """

        :param position:
        :return:
        """
    def ReadInt32(self, position: int) -> int:
        """

        :param position:
        :return:
        """
    def ReadInt64(self, position: int) -> int:
        """

        :param position:
        :return:
        """
    def ReadSByte(self, position: int) -> int:
        """

        :param position:
        :return:
        """
    def ReadSingle(self, position: int) -> float:
        """

        :param position:
        :return:
        """
    def ReadUInt16(self, position: int) -> int:
        """

        :param position:
        :return:
        """
    def ReadUInt32(self, position: int) -> int:
        """

        :param position:
        :return:
        """
    def ReadUInt64(self, position: int) -> int:
        """

        :param position:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Write(self, position: int, structure: T) -> None:
        """

        :param position:
        :param structure:
        """
    @overload
    def Write(self, position: int, value: bool) -> None:
        """

        :param position:
        :param value:
        """
    @overload
    def Write(self, position: int, value: int) -> None:
        """

        :param position:
        :param value:
        """
    @overload
    def Write(self, position: int, value: Char) -> None:
        """

        :param position:
        :param value:
        """
    @overload
    def Write(self, position: int, value: Decimal) -> None:
        """

        :param position:
        :param value:
        """
    @overload
    def Write(self, position: int, value: float) -> None:
        """

        :param position:
        :param value:
        """
    @overload
    def Write(self, position: int, value: int) -> None:
        """

        :param position:
        :param value:
        """
    @overload
    def Write(self, position: int, value: int) -> None:
        """

        :param position:
        :param value:
        """
    @overload
    def Write(self, position: int, value: int) -> None:
        """

        :param position:
        :param value:
        """
    @overload
    def Write(self, position: int, value: int) -> None:
        """

        :param position:
        :param value:
        """
    @overload
    def Write(self, position: int, value: float) -> None:
        """

        :param position:
        :param value:
        """
    @overload
    def Write(self, position: int, value: int) -> None:
        """

        :param position:
        :param value:
        """
    @overload
    def Write(self, position: int, value: int) -> None:
        """

        :param position:
        :param value:
        """
    @overload
    def Write(self, position: int, value: int) -> None:
        """

        :param position:
        :param value:
        """
    def WriteArray(self, position: int, array: Array[T], offset: int, count: int) -> None:
        """

        :param position:
        :param array:
        :param offset:
        :param count:
        """

class UnmanagedMemoryStream(Stream, IDisposable):
    """"""

    @overload
    def __init__(self, pointer: int, length: int):
        """

        :param pointer:
        :param length:
        """
    @overload
    def __init__(self, buffer: SafeBuffer, offset: int, length: int):
        """

        :param buffer:
        :param offset:
        :param length:
        """
    @overload
    def __init__(self, buffer: SafeBuffer, offset: int, length: int, access: FileAccess):
        """

        :param buffer:
        :param offset:
        :param length:
        :param access:
        """
    @overload
    def __init__(self, pointer: int, length: int, capacity: int, access: FileAccess):
        """

        :param pointer:
        :param length:
        :param capacity:
        :param access:
        """
    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def PositionPointer(self) -> int:
        """

        :return:
        """
    @PositionPointer.setter
    def PositionPointer(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
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
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

class UnmanagedMemoryStreamWrapper(MemoryStream, IDisposable):
    """"""

    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def GetBuffer(self) -> Array[int]:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToArray(self) -> Array[int]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TryGetBuffer(self, buffer: ArraySegment[int]) -> Tuple[bool, ArraySegment[int]]:
        """

        :param buffer:
        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """
    def WriteTo(self, stream: Stream) -> None:
        """

        :param stream:
        """

class WaitForChangedResult(ValueType):
    """"""

    @property
    def ChangeType(self) -> WatcherChangeTypes:
        """

        :return:
        """
    @ChangeType.setter
    def ChangeType(self, value: WatcherChangeTypes) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def OldName(self) -> str:
        """

        :return:
        """
    @OldName.setter
    def OldName(self, value: str) -> None: ...
    @property
    def TimedOut(self) -> bool:
        """

        :return:
        """
    @TimedOut.setter
    def TimedOut(self, value: bool) -> None: ...
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

class __ConsoleStream(Stream, IDisposable):
    """"""

    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
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
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

class __Error(ABC, Object):
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

class __HResults(ABC, Object):
    """"""

    COR_E_DIRECTORYNOTFOUND: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    COR_E_ENDOFSTREAM: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    COR_E_FILELOAD: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    COR_E_FILENOTFOUND: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    COR_E_IO: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    COR_E_PATHTOOLONG: Final[ClassVar[int]] = ...
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
