from __future__ import annotations

from abc import ABC
from typing import Callable, List, Tuple, Union, overload

from Microsoft.Win32.SafeHandles import SafePipeHandle
from System import Array, AsyncCallback, Boolean, Byte, Enum, IAsyncResult, ICloneable, IDisposable, Int32, Int64, IntPtr, MulticastDelegate, Object, String, Type, Void
from System.IO import HandleInheritability, SeekOrigin, Stream
from System.Runtime.InteropServices import SafeHandle
from System.Runtime.Serialization import ISerializable
from System.Security.AccessControl import AccessControlType, AccessRule, AuditFlags, AuditRule, InheritanceFlags, NativeObjectSecurity, PropagationFlags
from System.Security.Principal import IdentityReference, TokenImpersonationLevel
from System.Threading import CancellationToken, NativeOverlapped, WaitHandle
from System.Threading.Tasks import Task

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class AnonymousPipeClientStream(PipeStream, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, pipeHandleAsString: StringType): ...
    
    @overload
    def __init__(self, direction: PipeDirection, pipeHandleAsString: StringType): ...
    
    @overload
    def __init__(self, direction: PipeDirection, safePipeHandle: SafePipeHandle): ...
    
    # ---------- Properties ---------- #
    
    @ReadMode.setter
    def ReadMode(self, value: PipeTransmissionMode) -> None: ...
    
    @property
    def TransmissionMode(self) -> PipeTransmissionMode: ...
    
    # ---------- Methods ---------- #
    
    def get_TransmissionMode(self) -> PipeTransmissionMode: ...
    
    def set_ReadMode(self, value: PipeTransmissionMode) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AnonymousPipeServerStream(PipeStream, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, direction: PipeDirection): ...
    
    @overload
    def __init__(self, direction: PipeDirection, inheritability: HandleInheritability): ...
    
    @overload
    def __init__(self, direction: PipeDirection, inheritability: HandleInheritability, bufferSize: IntType): ...
    
    @overload
    def __init__(self, direction: PipeDirection, inheritability: HandleInheritability, bufferSize: IntType, pipeSecurity: PipeSecurity): ...
    
    @overload
    def __init__(self, direction: PipeDirection, serverSafePipeHandle: SafePipeHandle, clientSafePipeHandle: SafePipeHandle): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ClientSafePipeHandle(self) -> SafePipeHandle: ...
    
    @ReadMode.setter
    def ReadMode(self, value: PipeTransmissionMode) -> None: ...
    
    @property
    def TransmissionMode(self) -> PipeTransmissionMode: ...
    
    # ---------- Methods ---------- #
    
    def DisposeLocalCopyOfClientHandle(self) -> VoidType: ...
    
    def GetClientHandleAsString(self) -> StringType: ...
    
    def get_ClientSafePipeHandle(self) -> SafePipeHandle: ...
    
    def get_TransmissionMode(self) -> PipeTransmissionMode: ...
    
    def set_ReadMode(self, value: PipeTransmissionMode) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IOCancellationHelper(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, cancellationToken: CancellationToken): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AllowCancellation(self, handle: SafeHandle, overlapped: NativeOverlapped) -> VoidType: ...
    
    def SetOperationCompleted(self) -> VoidType: ...
    
    def ThrowIOOperationAborted(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NamedPipeClientStream(PipeStream, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, pipeName: StringType): ...
    
    @overload
    def __init__(self, serverName: StringType, pipeName: StringType): ...
    
    @overload
    def __init__(self, serverName: StringType, pipeName: StringType, direction: PipeDirection): ...
    
    @overload
    def __init__(self, serverName: StringType, pipeName: StringType, direction: PipeDirection, options: PipeOptions): ...
    
    @overload
    def __init__(self, serverName: StringType, pipeName: StringType, direction: PipeDirection, options: PipeOptions, impersonationLevel: TokenImpersonationLevel): ...
    
    @overload
    def __init__(self, serverName: StringType, pipeName: StringType, direction: PipeDirection, options: PipeOptions, impersonationLevel: TokenImpersonationLevel, inheritability: HandleInheritability): ...
    
    @overload
    def __init__(self, serverName: StringType, pipeName: StringType, desiredAccessRights: PipeAccessRights, options: PipeOptions, impersonationLevel: TokenImpersonationLevel, inheritability: HandleInheritability): ...
    
    @overload
    def __init__(self, direction: PipeDirection, isAsync: BooleanType, isConnected: BooleanType, safePipeHandle: SafePipeHandle): ...
    
    # ---------- Properties ---------- #
    
    @property
    def NumberOfServerInstances(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Connect(self) -> VoidType: ...
    
    @overload
    def Connect(self, timeout: IntType) -> VoidType: ...
    
    @overload
    def ConnectAsync(self) -> Task: ...
    
    @overload
    def ConnectAsync(self, timeout: IntType) -> Task: ...
    
    @overload
    def ConnectAsync(self, cancellationToken: CancellationToken) -> Task: ...
    
    @overload
    def ConnectAsync(self, timeout: IntType, cancellationToken: CancellationToken) -> Task: ...
    
    def get_NumberOfServerInstances(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NamedPipeServerStream(PipeStream, IDisposable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def MaxAllowedServerInstances() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, pipeName: StringType): ...
    
    @overload
    def __init__(self, pipeName: StringType, direction: PipeDirection): ...
    
    @overload
    def __init__(self, pipeName: StringType, direction: PipeDirection, maxNumberOfServerInstances: IntType): ...
    
    @overload
    def __init__(self, pipeName: StringType, direction: PipeDirection, maxNumberOfServerInstances: IntType, transmissionMode: PipeTransmissionMode): ...
    
    @overload
    def __init__(self, pipeName: StringType, direction: PipeDirection, maxNumberOfServerInstances: IntType, transmissionMode: PipeTransmissionMode, options: PipeOptions): ...
    
    @overload
    def __init__(self, pipeName: StringType, direction: PipeDirection, maxNumberOfServerInstances: IntType, transmissionMode: PipeTransmissionMode, options: PipeOptions, inBufferSize: IntType, outBufferSize: IntType): ...
    
    @overload
    def __init__(self, pipeName: StringType, direction: PipeDirection, maxNumberOfServerInstances: IntType, transmissionMode: PipeTransmissionMode, options: PipeOptions, inBufferSize: IntType, outBufferSize: IntType, pipeSecurity: PipeSecurity): ...
    
    @overload
    def __init__(self, pipeName: StringType, direction: PipeDirection, maxNumberOfServerInstances: IntType, transmissionMode: PipeTransmissionMode, options: PipeOptions, inBufferSize: IntType, outBufferSize: IntType, pipeSecurity: PipeSecurity, inheritability: HandleInheritability): ...
    
    @overload
    def __init__(self, pipeName: StringType, direction: PipeDirection, maxNumberOfServerInstances: IntType, transmissionMode: PipeTransmissionMode, options: PipeOptions, inBufferSize: IntType, outBufferSize: IntType, pipeSecurity: PipeSecurity, inheritability: HandleInheritability, additionalAccessRights: PipeAccessRights): ...
    
    @overload
    def __init__(self, direction: PipeDirection, isAsync: BooleanType, isConnected: BooleanType, safePipeHandle: SafePipeHandle): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginWaitForConnection(self, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def Disconnect(self) -> VoidType: ...
    
    def EndWaitForConnection(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def GetImpersonationUserName(self) -> StringType: ...
    
    def RunAsClient(self, impersonationWorker: PipeStreamImpersonationWorker) -> VoidType: ...
    
    def WaitForConnection(self) -> VoidType: ...
    
    @overload
    def WaitForConnectionAsync(self, cancellationToken: CancellationToken) -> Task: ...
    
    @overload
    def WaitForConnectionAsync(self) -> Task: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PipeAccessRule(AccessRule):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, identity: StringType, rights: PipeAccessRights, type: AccessControlType): ...
    
    @overload
    def __init__(self, identity: IdentityReference, rights: PipeAccessRights, type: AccessControlType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def PipeAccessRights(self) -> PipeAccessRights: ...
    
    # ---------- Methods ---------- #
    
    def get_PipeAccessRights(self) -> PipeAccessRights: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PipeAsyncResult(ObjectType, IAsyncResult):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AsyncState(self) -> ObjectType: ...
    
    @property
    def AsyncWaitHandle(self) -> WaitHandle: ...
    
    @property
    def CompletedSynchronously(self) -> BooleanType: ...
    
    @property
    def IsCompleted(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_AsyncState(self) -> ObjectType: ...
    
    def get_AsyncWaitHandle(self) -> WaitHandle: ...
    
    def get_CompletedSynchronously(self) -> BooleanType: ...
    
    def get_IsCompleted(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PipeAuditRule(AuditRule):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, identity: IdentityReference, rights: PipeAccessRights, flags: AuditFlags): ...
    
    @overload
    def __init__(self, identity: StringType, rights: PipeAccessRights, flags: AuditFlags): ...
    
    # ---------- Properties ---------- #
    
    @property
    def PipeAccessRights(self) -> PipeAccessRights: ...
    
    # ---------- Methods ---------- #
    
    def get_PipeAccessRights(self) -> PipeAccessRights: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PipeSecurity(NativeObjectSecurity):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AccessRightType(self) -> TypeType: ...
    
    @property
    def AccessRuleType(self) -> TypeType: ...
    
    @property
    def AuditRuleType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def AccessRuleFactory(self, identityReference: IdentityReference, accessMask: IntType, isInherited: BooleanType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule: ...
    
    def AddAccessRule(self, rule: PipeAccessRule) -> VoidType: ...
    
    def AddAuditRule(self, rule: PipeAuditRule) -> VoidType: ...
    
    def AuditRuleFactory(self, identityReference: IdentityReference, accessMask: IntType, isInherited: BooleanType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule: ...
    
    def RemoveAccessRule(self, rule: PipeAccessRule) -> BooleanType: ...
    
    def RemoveAccessRuleSpecific(self, rule: PipeAccessRule) -> VoidType: ...
    
    def RemoveAuditRule(self, rule: PipeAuditRule) -> BooleanType: ...
    
    def RemoveAuditRuleAll(self, rule: PipeAuditRule) -> VoidType: ...
    
    def RemoveAuditRuleSpecific(self, rule: PipeAuditRule) -> VoidType: ...
    
    def ResetAccessRule(self, rule: PipeAccessRule) -> VoidType: ...
    
    def SetAccessRule(self, rule: PipeAccessRule) -> VoidType: ...
    
    def SetAuditRule(self, rule: PipeAuditRule) -> VoidType: ...
    
    def get_AccessRightType(self) -> TypeType: ...
    
    def get_AccessRuleType(self) -> TypeType: ...
    
    def get_AuditRuleType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PipeStream(ABC, Stream, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanSeek(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def InBufferSize(self) -> IntType: ...
    
    @property
    def IsAsync(self) -> BooleanType: ...
    
    @property
    def IsConnected(self) -> BooleanType: ...
    
    @property
    def IsMessageComplete(self) -> BooleanType: ...
    
    @property
    def Length(self) -> LongType: ...
    
    @property
    def OutBufferSize(self) -> IntType: ...
    
    @property
    def Position(self) -> LongType: ...
    
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    
    @property
    def ReadMode(self) -> PipeTransmissionMode: ...
    
    @ReadMode.setter
    def ReadMode(self, value: PipeTransmissionMode) -> None: ...
    
    @property
    def SafePipeHandle(self) -> SafePipeHandle: ...
    
    @property
    def TransmissionMode(self) -> PipeTransmissionMode: ...
    
    # ---------- Methods ---------- #
    
    def BeginRead(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def GetAccessControl(self) -> PipeSecurity: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> Tuple[IntType, ArrayType[ByteType]]: ...
    
    def ReadByte(self) -> IntType: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetAccessControl(self, pipeSecurity: PipeSecurity) -> VoidType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def WaitForPipeDrain(self) -> VoidType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    def WriteByte(self, value: ByteType) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_InBufferSize(self) -> IntType: ...
    
    def get_IsAsync(self) -> BooleanType: ...
    
    def get_IsConnected(self) -> BooleanType: ...
    
    def get_IsMessageComplete(self) -> BooleanType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_OutBufferSize(self) -> IntType: ...
    
    def get_Position(self) -> LongType: ...
    
    def get_ReadMode(self) -> PipeTransmissionMode: ...
    
    def get_SafePipeHandle(self) -> SafePipeHandle: ...
    
    def get_TransmissionMode(self) -> PipeTransmissionMode: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    def set_ReadMode(self, value: PipeTransmissionMode) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PipeStreamAsyncResult(ObjectType, IAsyncResult):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AsyncState(self) -> ObjectType: ...
    
    @property
    def AsyncWaitHandle(self) -> WaitHandle: ...
    
    @property
    def CompletedSynchronously(self) -> BooleanType: ...
    
    @property
    def IsCompleted(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_AsyncState(self) -> ObjectType: ...
    
    def get_AsyncWaitHandle(self) -> WaitHandle: ...
    
    def get_CompletedSynchronously(self) -> BooleanType: ...
    
    def get_IsCompleted(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PipeStreamImpersonationWorker(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class PipeAccessRights(Enum):
    ReadData = 1
    WriteData = 2
    CreateNewInstance = 4
    ReadExtendedAttributes = 8
    WriteExtendedAttributes = 16
    ReadAttributes = 128
    WriteAttributes = 256
    Write = 274
    Delete = 65536
    ReadPermissions = 131072
    Read = 131209
    ReadWrite = 131483
    ChangePermissions = 262144
    TakeOwnership = 524288
    Synchronize = 1048576
    FullControl = 2032031
    AccessSystemSecurity = 16777216


class PipeDirection(Enum):
    In = 1
    Out = 2
    InOut = 3


class PipeOptions(Enum):
    WriteThrough = -2147483648
    #None = 0
    Asynchronous = 1073741824


class PipeState(Enum):
    WaitingToConnect = 0
    Connected = 1
    Broken = 2
    Disconnected = 3
    Closed = 4


class PipeTransmissionMode(Enum):
    Byte = 0
    Message = 1


# ---------- Delegates ---------- #

PipeStreamImpersonationWorker = Callable[[], VoidType]

__all__ = [
    AnonymousPipeClientStream,
    AnonymousPipeServerStream,
    IOCancellationHelper,
    NamedPipeClientStream,
    NamedPipeServerStream,
    PipeAccessRule,
    PipeAsyncResult,
    PipeAuditRule,
    PipeSecurity,
    PipeStream,
    PipeStreamAsyncResult,
    PipeStreamImpersonationWorker,
    PipeAccessRights,
    PipeDirection,
    PipeOptions,
    PipeState,
    PipeTransmissionMode,
    PipeStreamImpersonationWorker,
]
