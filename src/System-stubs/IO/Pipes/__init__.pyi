"""Automatically generated stubs for C# namespace: System.IO.Pipes."""

from abc import ABC
from collections.abc import Callable
from typing import ClassVar
from typing import overload

from Microsoft.Win32.SafeHandles import SafePipeHandle
from System import Array
from System import AsyncCallback
from System import Boolean
from System import Enum
from System import IAsyncResult
from System import IDisposable
from System import Object
from System import Type
from System.IO import HandleInheritability
from System.IO import SeekOrigin
from System.IO import Stream
from System.Runtime.InteropServices import SafeHandle
from System.Runtime.Remoting import ObjRef
from System.Security.AccessControl import AccessControlModification
from System.Security.AccessControl import AccessControlSections
from System.Security.AccessControl import AccessControlType
from System.Security.AccessControl import AccessRule
from System.Security.AccessControl import AuditFlags
from System.Security.AccessControl import AuditRule
from System.Security.AccessControl import AuthorizationRuleCollection
from System.Security.AccessControl import InheritanceFlags
from System.Security.AccessControl import NativeObjectSecurity
from System.Security.AccessControl import PropagationFlags
from System.Security.Principal import IdentityReference
from System.Security.Principal import TokenImpersonationLevel
from System.Threading import CancellationToken
from System.Threading import NativeOverlapped
from System.Threading import WaitHandle
from System.Threading.Tasks import Task

class AnonymousPipeClientStream(PipeStream, IDisposable):
    """"""
    @overload
    def __init__(self, pipeHandleAsString: str) -> None:
        """"""
    @overload
    def __init__(self, direction: PipeDirection, pipeHandleAsString: str) -> None:
        """"""
    @overload
    def __init__(self, direction: PipeDirection, safePipeHandle: SafePipeHandle) -> None:
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
    def InBufferSize(self) -> int:
        """"""
    @property
    def IsAsync(self) -> bool:
        """"""
    @property
    def IsConnected(self) -> bool:
        """"""
    @property
    def IsMessageComplete(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def OutBufferSize(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadMode(self) -> PipeTransmissionMode:
        """"""
    @ReadMode.setter
    def ReadMode(self, value: PipeTransmissionMode) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def SafePipeHandle(self) -> SafePipeHandle:
        """"""
    @property
    def TransmissionMode(self) -> PipeTransmissionMode:
        """"""
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
    def GetAccessControl(self) -> PipeSecurity:
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
    def SetAccessControl(self, pipeSecurity: PipeSecurity) -> None:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def WaitForPipeDrain(self) -> None:
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

class AnonymousPipeServerStream(PipeStream, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, direction: PipeDirection) -> None:
        """"""
    @overload
    def __init__(self, direction: PipeDirection, inheritability: HandleInheritability) -> None:
        """"""
    @overload
    def __init__(
        self, direction: PipeDirection, inheritability: HandleInheritability, bufferSize: int
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        direction: PipeDirection,
        inheritability: HandleInheritability,
        bufferSize: int,
        pipeSecurity: PipeSecurity,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        direction: PipeDirection,
        serverSafePipeHandle: SafePipeHandle,
        clientSafePipeHandle: SafePipeHandle,
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
    def ClientSafePipeHandle(self) -> SafePipeHandle:
        """"""
    @property
    def InBufferSize(self) -> int:
        """"""
    @property
    def IsAsync(self) -> bool:
        """"""
    @property
    def IsConnected(self) -> bool:
        """"""
    @property
    def IsMessageComplete(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def OutBufferSize(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadMode(self) -> PipeTransmissionMode:
        """"""
    @ReadMode.setter
    def ReadMode(self, value: PipeTransmissionMode) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def SafePipeHandle(self) -> SafePipeHandle:
        """"""
    @property
    def TransmissionMode(self) -> PipeTransmissionMode:
        """"""
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
    def DisposeLocalCopyOfClientHandle(self) -> None:
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
    def GetAccessControl(self) -> PipeSecurity:
        """"""
    def GetClientHandleAsString(self) -> str:
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
    def SetAccessControl(self, pipeSecurity: PipeSecurity) -> None:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def WaitForPipeDrain(self) -> None:
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

class IOCancellationHelper(Object):
    """"""
    def __init__(self, cancellationToken: CancellationToken) -> None:
        """"""
    def AllowCancellation(self, handle: SafeHandle, overlapped: NativeOverlapped) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetOperationCompleted(self) -> None:
        """"""
    def ThrowIOOperationAborted(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class NamedPipeClientStream(PipeStream, IDisposable):
    """"""
    @overload
    def __init__(self, pipeName: str) -> None:
        """"""
    @overload
    def __init__(self, serverName: str, pipeName: str) -> None:
        """"""
    @overload
    def __init__(self, serverName: str, pipeName: str, direction: PipeDirection) -> None:
        """"""
    @overload
    def __init__(
        self, serverName: str, pipeName: str, direction: PipeDirection, options: PipeOptions
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        serverName: str,
        pipeName: str,
        direction: PipeDirection,
        options: PipeOptions,
        impersonationLevel: TokenImpersonationLevel,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        serverName: str,
        pipeName: str,
        direction: PipeDirection,
        options: PipeOptions,
        impersonationLevel: TokenImpersonationLevel,
        inheritability: HandleInheritability,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        serverName: str,
        pipeName: str,
        desiredAccessRights: PipeAccessRights,
        options: PipeOptions,
        impersonationLevel: TokenImpersonationLevel,
        inheritability: HandleInheritability,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        direction: PipeDirection,
        isAsync: bool,
        isConnected: bool,
        safePipeHandle: SafePipeHandle,
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
    def InBufferSize(self) -> int:
        """"""
    @property
    def IsAsync(self) -> bool:
        """"""
    @property
    def IsConnected(self) -> bool:
        """"""
    @property
    def IsMessageComplete(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def NumberOfServerInstances(self) -> int:
        """"""
    @property
    def OutBufferSize(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadMode(self) -> PipeTransmissionMode:
        """"""
    @ReadMode.setter
    def ReadMode(self, value: PipeTransmissionMode) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def SafePipeHandle(self) -> SafePipeHandle:
        """"""
    @property
    def TransmissionMode(self) -> PipeTransmissionMode:
        """"""
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
    def Connect(self) -> None:
        """"""
    @overload
    def Connect(self, timeout: int) -> None:
        """"""
    @overload
    def ConnectAsync(self) -> Task:
        """"""
    @overload
    def ConnectAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    @overload
    def ConnectAsync(self, timeout: int) -> Task:
        """"""
    @overload
    def ConnectAsync(self, timeout: int, cancellationToken: CancellationToken) -> Task:
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
    def GetAccessControl(self) -> PipeSecurity:
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
    def SetAccessControl(self, pipeSecurity: PipeSecurity) -> None:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def WaitForPipeDrain(self) -> None:
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

class NamedPipeServerStream(PipeStream, IDisposable):
    """"""

    MaxAllowedServerInstances: ClassVar[int]
    """"""
    @overload
    def __init__(self, pipeName: str) -> None:
        """"""
    @overload
    def __init__(self, pipeName: str, direction: PipeDirection) -> None:
        """"""
    @overload
    def __init__(
        self, pipeName: str, direction: PipeDirection, maxNumberOfServerInstances: int
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        pipeName: str,
        direction: PipeDirection,
        maxNumberOfServerInstances: int,
        transmissionMode: PipeTransmissionMode,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        pipeName: str,
        direction: PipeDirection,
        maxNumberOfServerInstances: int,
        transmissionMode: PipeTransmissionMode,
        options: PipeOptions,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        pipeName: str,
        direction: PipeDirection,
        maxNumberOfServerInstances: int,
        transmissionMode: PipeTransmissionMode,
        options: PipeOptions,
        inBufferSize: int,
        outBufferSize: int,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        pipeName: str,
        direction: PipeDirection,
        maxNumberOfServerInstances: int,
        transmissionMode: PipeTransmissionMode,
        options: PipeOptions,
        inBufferSize: int,
        outBufferSize: int,
        pipeSecurity: PipeSecurity,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        pipeName: str,
        direction: PipeDirection,
        maxNumberOfServerInstances: int,
        transmissionMode: PipeTransmissionMode,
        options: PipeOptions,
        inBufferSize: int,
        outBufferSize: int,
        pipeSecurity: PipeSecurity,
        inheritability: HandleInheritability,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        pipeName: str,
        direction: PipeDirection,
        maxNumberOfServerInstances: int,
        transmissionMode: PipeTransmissionMode,
        options: PipeOptions,
        inBufferSize: int,
        outBufferSize: int,
        pipeSecurity: PipeSecurity,
        inheritability: HandleInheritability,
        additionalAccessRights: PipeAccessRights,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        direction: PipeDirection,
        isAsync: bool,
        isConnected: bool,
        safePipeHandle: SafePipeHandle,
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
    def InBufferSize(self) -> int:
        """"""
    @property
    def IsAsync(self) -> bool:
        """"""
    @property
    def IsConnected(self) -> bool:
        """"""
    @property
    def IsMessageComplete(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def OutBufferSize(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadMode(self) -> PipeTransmissionMode:
        """"""
    @ReadMode.setter
    def ReadMode(self, value: PipeTransmissionMode) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def SafePipeHandle(self) -> SafePipeHandle:
        """"""
    @property
    def TransmissionMode(self) -> PipeTransmissionMode:
        """"""
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWaitForConnection(self, callback: AsyncCallback, state: object) -> IAsyncResult:
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
    def Disconnect(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWaitForConnection(self, asyncResult: IAsyncResult) -> None:
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
    def GetAccessControl(self) -> PipeSecurity:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetImpersonationUserName(self) -> str:
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
    def RunAsClient(self, impersonationWorker: PipeStreamImpersonationWorker) -> None:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetAccessControl(self, pipeSecurity: PipeSecurity) -> None:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def WaitForConnection(self) -> None:
        """"""
    @overload
    def WaitForConnectionAsync(self) -> Task:
        """"""
    @overload
    def WaitForConnectionAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def WaitForPipeDrain(self) -> None:
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

class PipeAccessRights(Enum):
    """"""

    ReadData: PipeAccessRights = ...
    """"""
    WriteData: PipeAccessRights = ...
    """"""
    CreateNewInstance: PipeAccessRights = ...
    """"""
    ReadExtendedAttributes: PipeAccessRights = ...
    """"""
    WriteExtendedAttributes: PipeAccessRights = ...
    """"""
    ReadAttributes: PipeAccessRights = ...
    """"""
    WriteAttributes: PipeAccessRights = ...
    """"""
    Write: PipeAccessRights = ...
    """"""
    Delete: PipeAccessRights = ...
    """"""
    ReadPermissions: PipeAccessRights = ...
    """"""
    Read: PipeAccessRights = ...
    """"""
    ReadWrite: PipeAccessRights = ...
    """"""
    ChangePermissions: PipeAccessRights = ...
    """"""
    TakeOwnership: PipeAccessRights = ...
    """"""
    Synchronize: PipeAccessRights = ...
    """"""
    FullControl: PipeAccessRights = ...
    """"""
    AccessSystemSecurity: PipeAccessRights = ...
    """"""

class PipeAccessRule(AccessRule):
    """"""
    @overload
    def __init__(self, identity: str, rights: PipeAccessRights, type: AccessControlType) -> None:
        """"""
    @overload
    def __init__(
        self, identity: IdentityReference, rights: PipeAccessRights, type: AccessControlType
    ) -> None:
        """"""
    @property
    def AccessControlType(self) -> AccessControlType:
        """"""
    @property
    def IdentityReference(self) -> IdentityReference:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def PipeAccessRights(self) -> PipeAccessRights:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PipeAsyncResult(Object, IAsyncResult):
    """"""
    def __init__(self) -> None:
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

class PipeAuditRule(AuditRule):
    """"""
    @overload
    def __init__(
        self, identity: IdentityReference, rights: PipeAccessRights, flags: AuditFlags
    ) -> None:
        """"""
    @overload
    def __init__(self, identity: str, rights: PipeAccessRights, flags: AuditFlags) -> None:
        """"""
    @property
    def AuditFlags(self) -> AuditFlags:
        """"""
    @property
    def IdentityReference(self) -> IdentityReference:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def PipeAccessRights(self) -> PipeAccessRights:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PipeDirection(Enum):
    """"""

    In: PipeDirection = ...
    """"""
    Out: PipeDirection = ...
    """"""
    InOut: PipeDirection = ...
    """"""

class PipeOptions(Enum):
    """"""

    _None: PipeOptions = ...
    """"""
    Asynchronous: PipeOptions = ...
    """"""
    WriteThrough: PipeOptions = ...
    """"""

class PipeSecurity(NativeObjectSecurity):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AccessRightType(self) -> Type:
        """"""
    @property
    def AccessRuleType(self) -> Type:
        """"""
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAccessRulesProtected(self) -> bool:
        """"""
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAuditRulesProtected(self) -> bool:
        """"""
    @property
    def AuditRuleType(self) -> Type:
        """"""
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """"""
    def AddAccessRule(self, rule: PipeAccessRule) -> None:
        """"""
    def AddAuditRule(self, rule: PipeAuditRule) -> None:
        """"""
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """"""
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """"""
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """"""
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """"""
    def RemoveAccessRule(self, rule: PipeAccessRule) -> bool:
        """"""
    def RemoveAccessRuleSpecific(self, rule: PipeAccessRule) -> None:
        """"""
    def RemoveAuditRule(self, rule: PipeAuditRule) -> bool:
        """"""
    def RemoveAuditRuleAll(self, rule: PipeAuditRule) -> None:
        """"""
    def RemoveAuditRuleSpecific(self, rule: PipeAuditRule) -> None:
        """"""
    def ResetAccessRule(self, rule: PipeAccessRule) -> None:
        """"""
    def SetAccessRule(self, rule: PipeAccessRule) -> None:
        """"""
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetAuditRule(self, rule: PipeAuditRule) -> None:
        """"""
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetGroup(self, identity: IdentityReference) -> None:
        """"""
    def SetOwner(self, identity: IdentityReference) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class PipeState(Enum):
    """"""

    WaitingToConnect: PipeState = ...
    """"""
    Connected: PipeState = ...
    """"""
    Broken: PipeState = ...
    """"""
    Disconnected: PipeState = ...
    """"""
    Closed: PipeState = ...
    """"""

class PipeStream(ABC, Stream, IDisposable):
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
    def InBufferSize(self) -> int:
        """"""
    @property
    def IsAsync(self) -> bool:
        """"""
    @property
    def IsConnected(self) -> bool:
        """"""
    @property
    def IsMessageComplete(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def OutBufferSize(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadMode(self) -> PipeTransmissionMode:
        """"""
    @ReadMode.setter
    def ReadMode(self, value: PipeTransmissionMode) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def SafePipeHandle(self) -> SafePipeHandle:
        """"""
    @property
    def TransmissionMode(self) -> PipeTransmissionMode:
        """"""
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
    def GetAccessControl(self) -> PipeSecurity:
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
    def SetAccessControl(self, pipeSecurity: PipeSecurity) -> None:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def WaitForPipeDrain(self) -> None:
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

class PipeStreamAsyncResult(Object, IAsyncResult):
    """"""
    def __init__(self) -> None:
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

PipeStreamImpersonationWorker: Callable[[], None] = ...
""""""

class PipeTransmissionMode(Enum):
    """"""

    Byte: PipeTransmissionMode = ...
    """"""
    Message: PipeTransmissionMode = ...
    """"""
