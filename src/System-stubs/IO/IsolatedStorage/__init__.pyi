"""Automatically generated stubs for C# namespace: System.IO.IsolatedStorage."""

from abc import ABC
from collections.abc import Iterator
from typing import ClassVar
from typing import Final
from typing import overload

from Microsoft.Win32.SafeHandles import SafeFileHandle
from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from System import Array
from System import AsyncCallback
from System import Boolean
from System import DateTimeOffset
from System import Enum
from System import Exception
from System import IAsyncResult
from System import IDisposable
from System import IntPtr
from System import MarshalByRefObject
from System import Object
from System import Type
from System.Collections import IDictionary
from System.Collections import IEnumerator
from System.IO import FileAccess
from System.IO import FileMode
from System.IO import FileShare
from System.IO import FileStream
from System.IO import SeekOrigin
from System.IO import Stream
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Exception
from System.Runtime.Remoting import ObjRef
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Security import SecurityState
from System.Security.AccessControl import FileSecurity
from System.Security.Policy import Evidence
from System.Threading import CancellationToken
from System.Threading.Tasks import Task

class INormalizeForIsolatedStorage:
    """"""
    def Normalize(self) -> object:
        """"""

class IsolatedStorage(ABC, MarshalByRefObject):
    """"""
    @property
    def ApplicationIdentity(self) -> object:
        """"""
    @property
    def AssemblyIdentity(self) -> object:
        """"""
    @property
    def AvailableFreeSpace(self) -> int:
        """"""
    @property
    def CurrentSize(self) -> int:
        """"""
    @property
    def DomainIdentity(self) -> object:
        """"""
    @property
    def MaximumSize(self) -> int:
        """"""
    @property
    def Quota(self) -> int:
        """"""
    @property
    def Scope(self) -> IsolatedStorageScope:
        """"""
    @property
    def UsedSize(self) -> int:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def IncreaseQuotaTo(self, newQuotaSize: int) -> bool:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Remove(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __delitem__(self) -> None:
        """"""

class IsolatedStorageException(Exception, _Exception, ISerializable):
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

class IsolatedStorageFile(IsolatedStorage, IDisposable):
    """"""
    @property
    def ApplicationIdentity(self) -> object:
        """"""
    @property
    def AssemblyIdentity(self) -> object:
        """"""
    @property
    def AvailableFreeSpace(self) -> int:
        """"""
    @property
    def CurrentSize(self) -> int:
        """"""
    @property
    def DomainIdentity(self) -> object:
        """"""
    @classmethod
    @property
    def IsEnabled(cls) -> bool:
        """"""
    @property
    def MaximumSize(self) -> int:
        """"""
    @property
    def Quota(self) -> int:
        """"""
    @property
    def Scope(self) -> IsolatedStorageScope:
        """"""
    @property
    def UsedSize(self) -> int:
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def CopyFile(self, sourceFileName: str, destinationFileName: str) -> None:
        """"""
    @overload
    def CopyFile(self, sourceFileName: str, destinationFileName: str, overwrite: bool) -> None:
        """"""
    def CreateDirectory(self, dir: str) -> None:
        """"""
    def CreateFile(self, path: str) -> IsolatedStorageFileStream:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def DeleteDirectory(self, dir: str) -> None:
        """"""
    def DeleteFile(self, file: str) -> None:
        """"""
    def DirectoryExists(self, path: str) -> bool:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FileExists(self, path: str) -> bool:
        """"""
    def GetCreationTime(self, path: str) -> DateTimeOffset:
        """"""
    @overload
    def GetDirectoryNames(self) -> Array[str]:
        """"""
    @overload
    def GetDirectoryNames(self, searchPattern: str) -> Array[str]:
        """"""
    @classmethod
    def GetEnumerator(cls, scope: IsolatedStorageScope) -> IEnumerator:
        """"""
    @overload
    def GetFileNames(self) -> Array[str]:
        """"""
    @overload
    def GetFileNames(self, searchPattern: str) -> Array[str]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLastAccessTime(self, path: str) -> DateTimeOffset:
        """"""
    def GetLastWriteTime(self, path: str) -> DateTimeOffset:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    @classmethod
    def GetMachineStoreForApplication(cls) -> IsolatedStorageFile:
        """"""
    @classmethod
    def GetMachineStoreForAssembly(cls) -> IsolatedStorageFile:
        """"""
    @classmethod
    def GetMachineStoreForDomain(cls) -> IsolatedStorageFile:
        """"""
    @classmethod
    @overload
    def GetStore(
        cls,
        scope: IsolatedStorageScope,
        domainEvidence: Evidence,
        domainEvidenceType: Type,
        assemblyEvidence: Evidence,
        assemblyEvidenceType: Type,
    ) -> IsolatedStorageFile:
        """"""
    @classmethod
    @overload
    def GetStore(
        cls, scope: IsolatedStorageScope, applicationIdentity: object
    ) -> IsolatedStorageFile:
        """"""
    @classmethod
    @overload
    def GetStore(
        cls, scope: IsolatedStorageScope, domainIdentity: object, assemblyIdentity: object
    ) -> IsolatedStorageFile:
        """"""
    @classmethod
    @overload
    def GetStore(
        cls, scope: IsolatedStorageScope, applicationEvidenceType: Type
    ) -> IsolatedStorageFile:
        """"""
    @classmethod
    @overload
    def GetStore(
        cls, scope: IsolatedStorageScope, domainEvidenceType: Type, assemblyEvidenceType: Type
    ) -> IsolatedStorageFile:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetUserStoreForApplication(cls) -> IsolatedStorageFile:
        """"""
    @classmethod
    def GetUserStoreForAssembly(cls) -> IsolatedStorageFile:
        """"""
    @classmethod
    def GetUserStoreForDomain(cls) -> IsolatedStorageFile:
        """"""
    @classmethod
    def GetUserStoreForSite(cls) -> IsolatedStorageFile:
        """"""
    def IncreaseQuotaTo(self, newQuotaSize: int) -> bool:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def MoveDirectory(self, sourceDirectoryName: str, destinationDirectoryName: str) -> None:
        """"""
    def MoveFile(self, sourceFileName: str, destinationFileName: str) -> None:
        """"""
    @overload
    def OpenFile(self, path: str, mode: FileMode) -> IsolatedStorageFileStream:
        """"""
    @overload
    def OpenFile(self, path: str, mode: FileMode, access: FileAccess) -> IsolatedStorageFileStream:
        """"""
    @overload
    def OpenFile(
        self, path: str, mode: FileMode, access: FileAccess, share: FileShare
    ) -> IsolatedStorageFileStream:
        """"""
    @overload
    def Remove(self) -> None:
        """"""
    @classmethod
    @overload
    def Remove(cls, scope: IsolatedStorageScope) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def __iter__(cls, scope: IsolatedStorageScope) -> Iterator:
        """"""
    @overload
    def __delitem__(self) -> None:
        """"""
    @overload
    def __delitem__(self, scope: IsolatedStorageScope) -> None:
        """"""

class IsolatedStorageFileEnumerator(Object, IEnumerator):
    """"""
    @property
    def Current(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
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

class IsolatedStorageFileStream(FileStream, IDisposable):
    """"""
    @overload
    def __init__(self, path: str, mode: FileMode) -> None:
        """"""
    @overload
    def __init__(self, path: str, mode: FileMode, isf: IsolatedStorageFile) -> None:
        """"""
    @overload
    def __init__(self, path: str, mode: FileMode, access: FileAccess) -> None:
        """"""
    @overload
    def __init__(
        self, path: str, mode: FileMode, access: FileAccess, isf: IsolatedStorageFile
    ) -> None:
        """"""
    @overload
    def __init__(self, path: str, mode: FileMode, access: FileAccess, share: FileShare) -> None:
        """"""
    @overload
    def __init__(
        self,
        path: str,
        mode: FileMode,
        access: FileAccess,
        share: FileShare,
        isf: IsolatedStorageFile,
    ) -> None:
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
        isf: IsolatedStorageFile,
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
        buffer: Array[int],
        offset: int,
        numBytes: int,
        userCallback: AsyncCallback,
        stateObject: object,
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self,
        buffer: Array[int],
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
    def Read(self, buffer: Array[int], offset: int, count: int) -> int:
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

class IsolatedStorageScope(Enum):
    """"""

    _None: IsolatedStorageScope = ...
    """"""
    User: IsolatedStorageScope = ...
    """"""
    Domain: IsolatedStorageScope = ...
    """"""
    Assembly: IsolatedStorageScope = ...
    """"""
    Roaming: IsolatedStorageScope = ...
    """"""
    Machine: IsolatedStorageScope = ...
    """"""
    Application: IsolatedStorageScope = ...
    """"""

class IsolatedStorageSecurityOptions(Enum):
    """"""

    IncreaseQuotaForApplication: IsolatedStorageSecurityOptions = ...
    """"""

class IsolatedStorageSecurityState(SecurityState):
    """"""
    @property
    def Options(self) -> IsolatedStorageSecurityOptions:
        """"""
    @property
    def Quota(self) -> int:
        """"""
    @Quota.setter
    def Quota(self, value: int) -> None: ...
    @property
    def UsedSize(self) -> int:
        """"""
    def EnsureState(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsStateAvailable(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SafeIsolatedStorageFileHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
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

class TwoLevelFileEnumerator(Object, IEnumerator):
    """"""
    def __init__(self, root: str) -> None:
        """"""
    @property
    def Current(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
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

class TwoPaths(Object):
    """"""

    Path1: Final[str]
    """"""
    Path2: Final[str]
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

class __HResults(ABC, Object):
    """"""

    COR_E_ISOSTORE: ClassVar[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
