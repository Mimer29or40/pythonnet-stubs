from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final
from typing import Tuple
from typing import overload

from Microsoft.Win32.SafeHandles import SafeFileHandle
from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from System import Array
from System import AsyncCallback
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
        """

        :return:
        """

class IsolatedStorage(ABC, MarshalByRefObject):
    """"""

    @property
    def ApplicationIdentity(self) -> object:
        """

        :return:
        """
    @property
    def AssemblyIdentity(self) -> object:
        """

        :return:
        """
    @property
    def AvailableFreeSpace(self) -> int:
        """

        :return:
        """
    @property
    def CurrentSize(self) -> int:
        """

        :return:
        """
    @property
    def DomainIdentity(self) -> object:
        """

        :return:
        """
    @property
    def MaximumSize(self) -> int:
        """

        :return:
        """
    @property
    def Quota(self) -> int:
        """

        :return:
        """
    @property
    def Scope(self) -> IsolatedStorageScope:
        """

        :return:
        """
    @property
    def UsedSize(self) -> int:
        """

        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
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
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def IncreaseQuotaTo(self, newQuotaSize: int) -> bool:
        """

        :param newQuotaSize:
        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Remove(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class IsolatedStorageException(Exception, _Exception, ISerializable):
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

class IsolatedStorageFile(IsolatedStorage, IDisposable):
    """"""

    @property
    def ApplicationIdentity(self) -> object:
        """

        :return:
        """
    @property
    def AssemblyIdentity(self) -> object:
        """

        :return:
        """
    @property
    def AvailableFreeSpace(self) -> int:
        """

        :return:
        """
    @property
    def CurrentSize(self) -> int:
        """

        :return:
        """
    @property
    def DomainIdentity(self) -> object:
        """

        :return:
        """
    @classmethod
    @property
    def IsEnabled(cls) -> bool:
        """

        :return:
        """
    @property
    def MaximumSize(self) -> int:
        """

        :return:
        """
    @property
    def Quota(self) -> int:
        """

        :return:
        """
    @property
    def Scope(self) -> IsolatedStorageScope:
        """

        :return:
        """
    @property
    def UsedSize(self) -> int:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    @overload
    def CopyFile(self, sourceFileName: str, destinationFileName: str) -> None:
        """

        :param sourceFileName:
        :param destinationFileName:
        """
    @overload
    def CopyFile(self, sourceFileName: str, destinationFileName: str, overwrite: bool) -> None:
        """

        :param sourceFileName:
        :param destinationFileName:
        :param overwrite:
        """
    def CreateDirectory(self, dir: str) -> None:
        """

        :param dir:
        """
    def CreateFile(self, path: str) -> IsolatedStorageFileStream:
        """

        :param path:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def DeleteDirectory(self, dir: str) -> None:
        """

        :param dir:
        """
    def DeleteFile(self, file: str) -> None:
        """

        :param file:
        """
    def DirectoryExists(self, path: str) -> bool:
        """

        :param path:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FileExists(self, path: str) -> bool:
        """

        :param path:
        :return:
        """
    def GetCreationTime(self, path: str) -> DateTimeOffset:
        """

        :param path:
        :return:
        """
    @overload
    def GetDirectoryNames(self) -> Array[str]:
        """

        :return:
        """
    @overload
    def GetDirectoryNames(self, searchPattern: str) -> Array[str]:
        """

        :param searchPattern:
        :return:
        """
    @classmethod
    def GetEnumerator(cls, scope: IsolatedStorageScope) -> IEnumerator:
        """

        :param scope:
        :return:
        """
    @overload
    def GetFileNames(self) -> Array[str]:
        """

        :return:
        """
    @overload
    def GetFileNames(self, searchPattern: str) -> Array[str]:
        """

        :param searchPattern:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLastAccessTime(self, path: str) -> DateTimeOffset:
        """

        :param path:
        :return:
        """
    def GetLastWriteTime(self, path: str) -> DateTimeOffset:
        """

        :param path:
        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    @classmethod
    def GetMachineStoreForApplication(cls) -> IsolatedStorageFile:
        """

        :return:
        """
    @classmethod
    def GetMachineStoreForAssembly(cls) -> IsolatedStorageFile:
        """

        :return:
        """
    @classmethod
    def GetMachineStoreForDomain(cls) -> IsolatedStorageFile:
        """

        :return:
        """
    @classmethod
    @overload
    def GetStore(
        cls, scope: IsolatedStorageScope, applicationIdentity: object
    ) -> IsolatedStorageFile:
        """

        :param scope:
        :param applicationIdentity:
        :return:
        """
    @classmethod
    @overload
    def GetStore(
        cls, scope: IsolatedStorageScope, applicationEvidenceType: Type
    ) -> IsolatedStorageFile:
        """

        :param scope:
        :param applicationEvidenceType:
        :return:
        """
    @classmethod
    @overload
    def GetStore(
        cls, scope: IsolatedStorageScope, domainIdentity: object, assemblyIdentity: object
    ) -> IsolatedStorageFile:
        """

        :param scope:
        :param domainIdentity:
        :param assemblyIdentity:
        :return:
        """
    @classmethod
    @overload
    def GetStore(
        cls, scope: IsolatedStorageScope, domainEvidenceType: Type, assemblyEvidenceType: Type
    ) -> IsolatedStorageFile:
        """

        :param scope:
        :param domainEvidenceType:
        :param assemblyEvidenceType:
        :return:
        """
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
        """

        :param scope:
        :param domainEvidence:
        :param domainEvidenceType:
        :param assemblyEvidence:
        :param assemblyEvidenceType:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def GetUserStoreForApplication(cls) -> IsolatedStorageFile:
        """

        :return:
        """
    @classmethod
    def GetUserStoreForAssembly(cls) -> IsolatedStorageFile:
        """

        :return:
        """
    @classmethod
    def GetUserStoreForDomain(cls) -> IsolatedStorageFile:
        """

        :return:
        """
    @classmethod
    def GetUserStoreForSite(cls) -> IsolatedStorageFile:
        """

        :return:
        """
    def IncreaseQuotaTo(self, newQuotaSize: int) -> bool:
        """

        :param newQuotaSize:
        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def MoveDirectory(self, sourceDirectoryName: str, destinationDirectoryName: str) -> None:
        """

        :param sourceDirectoryName:
        :param destinationDirectoryName:
        """
    def MoveFile(self, sourceFileName: str, destinationFileName: str) -> None:
        """

        :param sourceFileName:
        :param destinationFileName:
        """
    @overload
    def OpenFile(self, path: str, mode: FileMode) -> IsolatedStorageFileStream:
        """

        :param path:
        :param mode:
        :return:
        """
    @overload
    def OpenFile(self, path: str, mode: FileMode, access: FileAccess) -> IsolatedStorageFileStream:
        """

        :param path:
        :param mode:
        :param access:
        :return:
        """
    @overload
    def OpenFile(
        self, path: str, mode: FileMode, access: FileAccess, share: FileShare
    ) -> IsolatedStorageFileStream:
        """

        :param path:
        :param mode:
        :param access:
        :param share:
        :return:
        """
    @overload
    def Remove(self) -> None:
        """"""
    @classmethod
    @overload
    def Remove(cls, scope: IsolatedStorageScope) -> None:
        """

        :param scope:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class IsolatedStorageFileEnumerator(Object, IEnumerator):
    """"""

    @property
    def Current(self) -> object:
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

class IsolatedStorageFileStream(FileStream, IDisposable):
    """"""

    @overload
    def __init__(self, path: str, mode: FileMode):
        """

        :param path:
        :param mode:
        """
    @overload
    def __init__(self, path: str, mode: FileMode, isf: IsolatedStorageFile):
        """

        :param path:
        :param mode:
        :param isf:
        """
    @overload
    def __init__(self, path: str, mode: FileMode, access: FileAccess):
        """

        :param path:
        :param mode:
        :param access:
        """
    @overload
    def __init__(self, path: str, mode: FileMode, access: FileAccess, isf: IsolatedStorageFile):
        """

        :param path:
        :param mode:
        :param access:
        :param isf:
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
        self,
        path: str,
        mode: FileMode,
        access: FileAccess,
        share: FileShare,
        isf: IsolatedStorageFile,
    ):
        """

        :param path:
        :param mode:
        :param access:
        :param share:
        :param isf:
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
        isf: IsolatedStorageFile,
    ):
        """

        :param path:
        :param mode:
        :param access:
        :param share:
        :param bufferSize:
        :param isf:
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
        """

        :return:
        """
    @property
    def Quota(self) -> int:
        """

        :return:
        """
    @Quota.setter
    def Quota(self, value: int) -> None: ...
    @property
    def UsedSize(self) -> int:
        """

        :return:
        """
    def EnsureState(self) -> None:
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
    def IsStateAvailable(self) -> bool:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SafeIsolatedStorageFileHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class TwoLevelFileEnumerator(Object, IEnumerator):
    """"""

    def __init__(self, root: str):
        """

        :param root:
        """
    @property
    def Current(self) -> object:
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

class TwoPaths(Object):
    """"""

    Path1: Final[str] = ...
    """
    
    :return: 
    """
    Path2: Final[str] = ...
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

class __HResults(ABC, Object):
    """"""

    COR_E_ISOSTORE: Final[ClassVar[int]] = ...
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
