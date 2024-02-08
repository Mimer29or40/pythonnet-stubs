from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import ClassVar
from typing import Final
from typing import Tuple
from typing import overload

from Microsoft.Win32.SafeHandles import SafePipeHandle
from System import Array
from System import AsyncCallback
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
    def __init__(self, pipeHandleAsString: str):
        """

        :param pipeHandleAsString:
        """
    @overload
    def __init__(self, direction: PipeDirection, safePipeHandle: SafePipeHandle):
        """

        :param direction:
        :param safePipeHandle:
        """
    @overload
    def __init__(self, direction: PipeDirection, pipeHandleAsString: str):
        """

        :param direction:
        :param pipeHandleAsString:
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
    def InBufferSize(self) -> int:
        """

        :return:
        """
    @property
    def IsAsync(self) -> bool:
        """

        :return:
        """
    @property
    def IsConnected(self) -> bool:
        """

        :return:
        """
    @property
    def IsMessageComplete(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def OutBufferSize(self) -> int:
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
    def ReadMode(self) -> PipeTransmissionMode:
        """

        :return:
        """
    @ReadMode.setter
    def ReadMode(self, value: PipeTransmissionMode) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def SafePipeHandle(self) -> SafePipeHandle:
        """

        :return:
        """
    @property
    def TransmissionMode(self) -> PipeTransmissionMode:
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
    def GetAccessControl(self) -> PipeSecurity:
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
    def SetAccessControl(self, pipeSecurity: PipeSecurity) -> None:
        """

        :param pipeSecurity:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def WaitForPipeDrain(self) -> None:
        """"""
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

class AnonymousPipeServerStream(PipeStream, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, direction: PipeDirection):
        """

        :param direction:
        """
    @overload
    def __init__(self, direction: PipeDirection, inheritability: HandleInheritability):
        """

        :param direction:
        :param inheritability:
        """
    @overload
    def __init__(
        self,
        direction: PipeDirection,
        serverSafePipeHandle: SafePipeHandle,
        clientSafePipeHandle: SafePipeHandle,
    ):
        """

        :param direction:
        :param serverSafePipeHandle:
        :param clientSafePipeHandle:
        """
    @overload
    def __init__(
        self, direction: PipeDirection, inheritability: HandleInheritability, bufferSize: int
    ):
        """

        :param direction:
        :param inheritability:
        :param bufferSize:
        """
    @overload
    def __init__(
        self,
        direction: PipeDirection,
        inheritability: HandleInheritability,
        bufferSize: int,
        pipeSecurity: PipeSecurity,
    ):
        """

        :param direction:
        :param inheritability:
        :param bufferSize:
        :param pipeSecurity:
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
    def ClientSafePipeHandle(self) -> SafePipeHandle:
        """

        :return:
        """
    @property
    def InBufferSize(self) -> int:
        """

        :return:
        """
    @property
    def IsAsync(self) -> bool:
        """

        :return:
        """
    @property
    def IsConnected(self) -> bool:
        """

        :return:
        """
    @property
    def IsMessageComplete(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def OutBufferSize(self) -> int:
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
    def ReadMode(self) -> PipeTransmissionMode:
        """

        :return:
        """
    @ReadMode.setter
    def ReadMode(self, value: PipeTransmissionMode) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def SafePipeHandle(self) -> SafePipeHandle:
        """

        :return:
        """
    @property
    def TransmissionMode(self) -> PipeTransmissionMode:
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
    def DisposeLocalCopyOfClientHandle(self) -> None:
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
    def GetAccessControl(self) -> PipeSecurity:
        """

        :return:
        """
    def GetClientHandleAsString(self) -> str:
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
    def SetAccessControl(self, pipeSecurity: PipeSecurity) -> None:
        """

        :param pipeSecurity:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def WaitForPipeDrain(self) -> None:
        """"""
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

class IOCancellationHelper(Object):
    """"""

    def __init__(self, cancellationToken: CancellationToken):
        """

        :param cancellationToken:
        """
    def AllowCancellation(self, handle: SafeHandle, overlapped: NativeOverlapped) -> None:
        """

        :param handle:
        :param overlapped:
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
    def SetOperationCompleted(self) -> None:
        """"""
    def ThrowIOOperationAborted(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class NamedPipeClientStream(PipeStream, IDisposable):
    """"""

    @overload
    def __init__(self, pipeName: str):
        """

        :param pipeName:
        """
    @overload
    def __init__(self, serverName: str, pipeName: str):
        """

        :param serverName:
        :param pipeName:
        """
    @overload
    def __init__(self, serverName: str, pipeName: str, direction: PipeDirection):
        """

        :param serverName:
        :param pipeName:
        :param direction:
        """
    @overload
    def __init__(
        self,
        direction: PipeDirection,
        isAsync: bool,
        isConnected: bool,
        safePipeHandle: SafePipeHandle,
    ):
        """

        :param direction:
        :param isAsync:
        :param isConnected:
        :param safePipeHandle:
        """
    @overload
    def __init__(
        self, serverName: str, pipeName: str, direction: PipeDirection, options: PipeOptions
    ):
        """

        :param serverName:
        :param pipeName:
        :param direction:
        :param options:
        """
    @overload
    def __init__(
        self,
        serverName: str,
        pipeName: str,
        direction: PipeDirection,
        options: PipeOptions,
        impersonationLevel: TokenImpersonationLevel,
    ):
        """

        :param serverName:
        :param pipeName:
        :param direction:
        :param options:
        :param impersonationLevel:
        """
    @overload
    def __init__(
        self,
        serverName: str,
        pipeName: str,
        desiredAccessRights: PipeAccessRights,
        options: PipeOptions,
        impersonationLevel: TokenImpersonationLevel,
        inheritability: HandleInheritability,
    ):
        """

        :param serverName:
        :param pipeName:
        :param desiredAccessRights:
        :param options:
        :param impersonationLevel:
        :param inheritability:
        """
    @overload
    def __init__(
        self,
        serverName: str,
        pipeName: str,
        direction: PipeDirection,
        options: PipeOptions,
        impersonationLevel: TokenImpersonationLevel,
        inheritability: HandleInheritability,
    ):
        """

        :param serverName:
        :param pipeName:
        :param direction:
        :param options:
        :param impersonationLevel:
        :param inheritability:
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
    def InBufferSize(self) -> int:
        """

        :return:
        """
    @property
    def IsAsync(self) -> bool:
        """

        :return:
        """
    @property
    def IsConnected(self) -> bool:
        """

        :return:
        """
    @property
    def IsMessageComplete(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def NumberOfServerInstances(self) -> int:
        """

        :return:
        """
    @property
    def OutBufferSize(self) -> int:
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
    def ReadMode(self) -> PipeTransmissionMode:
        """

        :return:
        """
    @ReadMode.setter
    def ReadMode(self, value: PipeTransmissionMode) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def SafePipeHandle(self) -> SafePipeHandle:
        """

        :return:
        """
    @property
    def TransmissionMode(self) -> PipeTransmissionMode:
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
    def Connect(self) -> None:
        """"""
    @overload
    def Connect(self, timeout: int) -> None:
        """

        :param timeout:
        """
    @overload
    def ConnectAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def ConnectAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    @overload
    def ConnectAsync(self, timeout: int) -> Task:
        """

        :param timeout:
        :return:
        """
    @overload
    def ConnectAsync(self, timeout: int, cancellationToken: CancellationToken) -> Task:
        """

        :param timeout:
        :param cancellationToken:
        :return:
        """
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
    def GetAccessControl(self) -> PipeSecurity:
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
    def SetAccessControl(self, pipeSecurity: PipeSecurity) -> None:
        """

        :param pipeSecurity:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def WaitForPipeDrain(self) -> None:
        """"""
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

class NamedPipeServerStream(PipeStream, IDisposable):
    """"""

    MaxAllowedServerInstances: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, pipeName: str):
        """

        :param pipeName:
        """
    @overload
    def __init__(self, pipeName: str, direction: PipeDirection):
        """

        :param pipeName:
        :param direction:
        """
    @overload
    def __init__(self, pipeName: str, direction: PipeDirection, maxNumberOfServerInstances: int):
        """

        :param pipeName:
        :param direction:
        :param maxNumberOfServerInstances:
        """
    @overload
    def __init__(
        self,
        direction: PipeDirection,
        isAsync: bool,
        isConnected: bool,
        safePipeHandle: SafePipeHandle,
    ):
        """

        :param direction:
        :param isAsync:
        :param isConnected:
        :param safePipeHandle:
        """
    @overload
    def __init__(
        self,
        pipeName: str,
        direction: PipeDirection,
        maxNumberOfServerInstances: int,
        transmissionMode: PipeTransmissionMode,
    ):
        """

        :param pipeName:
        :param direction:
        :param maxNumberOfServerInstances:
        :param transmissionMode:
        """
    @overload
    def __init__(
        self,
        pipeName: str,
        direction: PipeDirection,
        maxNumberOfServerInstances: int,
        transmissionMode: PipeTransmissionMode,
        options: PipeOptions,
    ):
        """

        :param pipeName:
        :param direction:
        :param maxNumberOfServerInstances:
        :param transmissionMode:
        :param options:
        """
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
    ):
        """

        :param pipeName:
        :param direction:
        :param maxNumberOfServerInstances:
        :param transmissionMode:
        :param options:
        :param inBufferSize:
        :param outBufferSize:
        """
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
    ):
        """

        :param pipeName:
        :param direction:
        :param maxNumberOfServerInstances:
        :param transmissionMode:
        :param options:
        :param inBufferSize:
        :param outBufferSize:
        :param pipeSecurity:
        """
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
    ):
        """

        :param pipeName:
        :param direction:
        :param maxNumberOfServerInstances:
        :param transmissionMode:
        :param options:
        :param inBufferSize:
        :param outBufferSize:
        :param pipeSecurity:
        :param inheritability:
        """
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
    ):
        """

        :param pipeName:
        :param direction:
        :param maxNumberOfServerInstances:
        :param transmissionMode:
        :param options:
        :param inBufferSize:
        :param outBufferSize:
        :param pipeSecurity:
        :param inheritability:
        :param additionalAccessRights:
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
    def InBufferSize(self) -> int:
        """

        :return:
        """
    @property
    def IsAsync(self) -> bool:
        """

        :return:
        """
    @property
    def IsConnected(self) -> bool:
        """

        :return:
        """
    @property
    def IsMessageComplete(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def OutBufferSize(self) -> int:
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
    def ReadMode(self) -> PipeTransmissionMode:
        """

        :return:
        """
    @ReadMode.setter
    def ReadMode(self, value: PipeTransmissionMode) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def SafePipeHandle(self) -> SafePipeHandle:
        """

        :return:
        """
    @property
    def TransmissionMode(self) -> PipeTransmissionMode:
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
    def BeginWaitForConnection(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """

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
    def Disconnect(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWaitForConnection(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
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
    def GetAccessControl(self) -> PipeSecurity:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetImpersonationUserName(self) -> str:
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
    def RunAsClient(self, impersonationWorker: PipeStreamImpersonationWorker) -> None:
        """

        :param impersonationWorker:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetAccessControl(self, pipeSecurity: PipeSecurity) -> None:
        """

        :param pipeSecurity:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def WaitForConnection(self) -> None:
        """"""
    @overload
    def WaitForConnectionAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def WaitForConnectionAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def WaitForPipeDrain(self) -> None:
        """"""
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
    def __init__(
        self, identity: IdentityReference, rights: PipeAccessRights, type: AccessControlType
    ):
        """

        :param identity:
        :param rights:
        :param type:
        """
    @overload
    def __init__(self, identity: str, rights: PipeAccessRights, type: AccessControlType):
        """

        :param identity:
        :param rights:
        :param type:
        """
    @property
    def AccessControlType(self) -> AccessControlType:
        """

        :return:
        """
    @property
    def IdentityReference(self) -> IdentityReference:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def PipeAccessRights(self) -> PipeAccessRights:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
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

class PipeAsyncResult(Object, IAsyncResult):
    """"""

    def __init__(self):
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

class PipeAuditRule(AuditRule):
    """"""

    @overload
    def __init__(self, identity: IdentityReference, rights: PipeAccessRights, flags: AuditFlags):
        """

        :param identity:
        :param rights:
        :param flags:
        """
    @overload
    def __init__(self, identity: str, rights: PipeAccessRights, flags: AuditFlags):
        """

        :param identity:
        :param rights:
        :param flags:
        """
    @property
    def AuditFlags(self) -> AuditFlags:
        """

        :return:
        """
    @property
    def IdentityReference(self) -> IdentityReference:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def PipeAccessRights(self) -> PipeAccessRights:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
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

    def __init__(self):
        """"""
    @property
    def AccessRightType(self) -> Type:
        """

        :return:
        """
    @property
    def AccessRuleType(self) -> Type:
        """

        :return:
        """
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAccessRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AuditRuleType(self) -> Type:
        """

        :return:
        """
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param type:
        :return:
        """
    def AddAccessRule(self, rule: PipeAccessRule) -> None:
        """

        :param rule:
        """
    def AddAuditRule(self, rule: PipeAuditRule) -> None:
        """

        :param rule:
        """
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param flags:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """

        :return:
        """
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """

        :param includeSections:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def RemoveAccessRule(self, rule: PipeAccessRule) -> bool:
        """

        :param rule:
        :return:
        """
    def RemoveAccessRuleSpecific(self, rule: PipeAccessRule) -> None:
        """

        :param rule:
        """
    def RemoveAuditRule(self, rule: PipeAuditRule) -> bool:
        """

        :param rule:
        :return:
        """
    def RemoveAuditRuleAll(self, rule: PipeAuditRule) -> None:
        """

        :param rule:
        """
    def RemoveAuditRuleSpecific(self, rule: PipeAuditRule) -> None:
        """

        :param rule:
        """
    def ResetAccessRule(self, rule: PipeAccessRule) -> None:
        """

        :param rule:
        """
    def SetAccessRule(self, rule: PipeAccessRule) -> None:
        """

        :param rule:
        """
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetAuditRule(self, rule: PipeAuditRule) -> None:
        """

        :param rule:
        """
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetGroup(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def SetOwner(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """

        :param binaryForm:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """

        :param binaryForm:
        :param includeSections:
        """
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """

        :param sddlForm:
        """
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """

        :param sddlForm:
        :param includeSections:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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
    def InBufferSize(self) -> int:
        """

        :return:
        """
    @property
    def IsAsync(self) -> bool:
        """

        :return:
        """
    @property
    def IsConnected(self) -> bool:
        """

        :return:
        """
    @property
    def IsMessageComplete(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def OutBufferSize(self) -> int:
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
    def ReadMode(self) -> PipeTransmissionMode:
        """

        :return:
        """
    @ReadMode.setter
    def ReadMode(self, value: PipeTransmissionMode) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def SafePipeHandle(self) -> SafePipeHandle:
        """

        :return:
        """
    @property
    def TransmissionMode(self) -> PipeTransmissionMode:
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
    def GetAccessControl(self) -> PipeSecurity:
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
    def SetAccessControl(self, pipeSecurity: PipeSecurity) -> None:
        """

        :param pipeSecurity:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def WaitForPipeDrain(self) -> None:
        """"""
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

class PipeStreamAsyncResult(Object, IAsyncResult):
    """"""

    def __init__(self):
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

PipeStreamImpersonationWorker: Callable[[], None] = ...
""""""

class PipeTransmissionMode(Enum):
    """"""

    Byte: PipeTransmissionMode = ...
    """"""
    Message: PipeTransmissionMode = ...
    """"""
