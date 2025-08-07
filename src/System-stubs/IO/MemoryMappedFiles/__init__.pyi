"""Automatically generated stubs for C# namespace: System.IO.MemoryMappedFiles."""

from typing import overload

from Microsoft.Win32.SafeHandles import SafeMemoryMappedFileHandle
from Microsoft.Win32.SafeHandles import SafeMemoryMappedViewHandle
from System import Array
from System import AsyncCallback
from System import Boolean
from System import Char
from System import Decimal
from System import Enum
from System import IAsyncResult
from System import IDisposable
from System import IntPtr
from System import Object
from System import Type
from System.IO import FileMode
from System.IO import FileStream
from System.IO import HandleInheritability
from System.IO import SeekOrigin
from System.IO import Stream
from System.IO import T
from System.IO import UnmanagedMemoryAccessor
from System.IO import UnmanagedMemoryStream
from System.Runtime.Remoting import ObjRef
from System.Security.AccessControl import AccessControlModification
from System.Security.AccessControl import AccessControlSections
from System.Security.AccessControl import AccessControlType
from System.Security.AccessControl import AccessRule
from System.Security.AccessControl import AuditFlags
from System.Security.AccessControl import AuditRule
from System.Security.AccessControl import AuthorizationRuleCollection
from System.Security.AccessControl import InheritanceFlags
from System.Security.AccessControl import ObjectSecurity
from System.Security.AccessControl import PropagationFlags
from System.Security.Principal import IdentityReference
from System.Threading import CancellationToken
from System.Threading.Tasks import Task

class MemoryMappedFile(Object, IDisposable):
    """"""
    @property
    def SafeMemoryMappedFileHandle(self) -> SafeMemoryMappedFileHandle:
        """"""
    @classmethod
    @overload
    def CreateFromFile(
        cls,
        fileStream: FileStream,
        mapName: str,
        capacity: int,
        access: MemoryMappedFileAccess,
        memoryMappedFileSecurity: MemoryMappedFileSecurity,
        inheritability: HandleInheritability,
        leaveOpen: bool,
    ) -> MemoryMappedFile:
        """"""
    @classmethod
    @overload
    def CreateFromFile(
        cls,
        fileStream: FileStream,
        mapName: str,
        capacity: int,
        access: MemoryMappedFileAccess,
        inheritability: HandleInheritability,
        leaveOpen: bool,
    ) -> MemoryMappedFile:
        """"""
    @classmethod
    @overload
    def CreateFromFile(cls, path: str) -> MemoryMappedFile:
        """"""
    @classmethod
    @overload
    def CreateFromFile(cls, path: str, mode: FileMode) -> MemoryMappedFile:
        """"""
    @classmethod
    @overload
    def CreateFromFile(cls, path: str, mode: FileMode, mapName: str) -> MemoryMappedFile:
        """"""
    @classmethod
    @overload
    def CreateFromFile(
        cls, path: str, mode: FileMode, mapName: str, capacity: int
    ) -> MemoryMappedFile:
        """"""
    @classmethod
    @overload
    def CreateFromFile(
        cls, path: str, mode: FileMode, mapName: str, capacity: int, access: MemoryMappedFileAccess
    ) -> MemoryMappedFile:
        """"""
    @classmethod
    @overload
    def CreateNew(cls, mapName: str, capacity: int) -> MemoryMappedFile:
        """"""
    @classmethod
    @overload
    def CreateNew(
        cls, mapName: str, capacity: int, access: MemoryMappedFileAccess
    ) -> MemoryMappedFile:
        """"""
    @classmethod
    @overload
    def CreateNew(
        cls,
        mapName: str,
        capacity: int,
        access: MemoryMappedFileAccess,
        options: MemoryMappedFileOptions,
        memoryMappedFileSecurity: MemoryMappedFileSecurity,
        inheritability: HandleInheritability,
    ) -> MemoryMappedFile:
        """"""
    @classmethod
    @overload
    def CreateNew(
        cls,
        mapName: str,
        capacity: int,
        access: MemoryMappedFileAccess,
        options: MemoryMappedFileOptions,
        inheritability: HandleInheritability,
    ) -> MemoryMappedFile:
        """"""
    @classmethod
    @overload
    def CreateOrOpen(cls, mapName: str, capacity: int) -> MemoryMappedFile:
        """"""
    @classmethod
    @overload
    def CreateOrOpen(
        cls, mapName: str, capacity: int, access: MemoryMappedFileAccess
    ) -> MemoryMappedFile:
        """"""
    @classmethod
    @overload
    def CreateOrOpen(
        cls,
        mapName: str,
        capacity: int,
        access: MemoryMappedFileAccess,
        options: MemoryMappedFileOptions,
        memoryMappedFileSecurity: MemoryMappedFileSecurity,
        inheritability: HandleInheritability,
    ) -> MemoryMappedFile:
        """"""
    @classmethod
    @overload
    def CreateOrOpen(
        cls,
        mapName: str,
        capacity: int,
        access: MemoryMappedFileAccess,
        options: MemoryMappedFileOptions,
        inheritability: HandleInheritability,
    ) -> MemoryMappedFile:
        """"""
    @overload
    def CreateViewAccessor(self) -> MemoryMappedViewAccessor:
        """"""
    @overload
    def CreateViewAccessor(self, offset: int, size: int) -> MemoryMappedViewAccessor:
        """"""
    @overload
    def CreateViewAccessor(
        self, offset: int, size: int, access: MemoryMappedFileAccess
    ) -> MemoryMappedViewAccessor:
        """"""
    @overload
    def CreateViewStream(self) -> MemoryMappedViewStream:
        """"""
    @overload
    def CreateViewStream(self, offset: int, size: int) -> MemoryMappedViewStream:
        """"""
    @overload
    def CreateViewStream(
        self, offset: int, size: int, access: MemoryMappedFileAccess
    ) -> MemoryMappedViewStream:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAccessControl(self) -> MemoryMappedFileSecurity:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def OpenExisting(cls, mapName: str) -> MemoryMappedFile:
        """"""
    @classmethod
    @overload
    def OpenExisting(
        cls, mapName: str, desiredAccessRights: MemoryMappedFileRights
    ) -> MemoryMappedFile:
        """"""
    @classmethod
    @overload
    def OpenExisting(
        cls,
        mapName: str,
        desiredAccessRights: MemoryMappedFileRights,
        inheritability: HandleInheritability,
    ) -> MemoryMappedFile:
        """"""
    def SetAccessControl(self, memoryMappedFileSecurity: MemoryMappedFileSecurity) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class MemoryMappedFileAccess(Enum):
    """"""

    ReadWrite: MemoryMappedFileAccess = ...
    """"""
    Read: MemoryMappedFileAccess = ...
    """"""
    Write: MemoryMappedFileAccess = ...
    """"""
    CopyOnWrite: MemoryMappedFileAccess = ...
    """"""
    ReadExecute: MemoryMappedFileAccess = ...
    """"""
    ReadWriteExecute: MemoryMappedFileAccess = ...
    """"""

class MemoryMappedFileOptions(Enum):
    """"""

    _None: MemoryMappedFileOptions = ...
    """"""
    DelayAllocatePages: MemoryMappedFileOptions = ...
    """"""

class MemoryMappedFileRights(Enum):
    """"""

    CopyOnWrite: MemoryMappedFileRights = ...
    """"""
    Write: MemoryMappedFileRights = ...
    """"""
    Read: MemoryMappedFileRights = ...
    """"""
    ReadWrite: MemoryMappedFileRights = ...
    """"""
    Execute: MemoryMappedFileRights = ...
    """"""
    ReadExecute: MemoryMappedFileRights = ...
    """"""
    ReadWriteExecute: MemoryMappedFileRights = ...
    """"""
    Delete: MemoryMappedFileRights = ...
    """"""
    ReadPermissions: MemoryMappedFileRights = ...
    """"""
    ChangePermissions: MemoryMappedFileRights = ...
    """"""
    TakeOwnership: MemoryMappedFileRights = ...
    """"""
    FullControl: MemoryMappedFileRights = ...
    """"""
    AccessSystemSecurity: MemoryMappedFileRights = ...
    """"""

class MemoryMappedFileSecurity(ObjectSecurity[MemoryMappedFileRights]):
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
    def AddAccessRule(self, rule: AccessRule[MemoryMappedFileRights]) -> None:
        """"""
    def AddAuditRule(self, rule: AuditRule[MemoryMappedFileRights]) -> None:
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
    def RemoveAccessRule(self, rule: AccessRule[MemoryMappedFileRights]) -> bool:
        """"""
    def RemoveAccessRuleAll(self, rule: AccessRule[MemoryMappedFileRights]) -> None:
        """"""
    def RemoveAccessRuleSpecific(self, rule: AccessRule[MemoryMappedFileRights]) -> None:
        """"""
    def RemoveAuditRule(self, rule: AuditRule[MemoryMappedFileRights]) -> bool:
        """"""
    def RemoveAuditRuleAll(self, rule: AuditRule[MemoryMappedFileRights]) -> None:
        """"""
    def RemoveAuditRuleSpecific(self, rule: AuditRule[MemoryMappedFileRights]) -> None:
        """"""
    def ResetAccessRule(self, rule: AccessRule[MemoryMappedFileRights]) -> None:
        """"""
    def SetAccessRule(self, rule: AccessRule[MemoryMappedFileRights]) -> None:
        """"""
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetAuditRule(self, rule: AuditRule[MemoryMappedFileRights]) -> None:
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

class MemoryMappedView(Object, IDisposable):
    """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self, capacity: IntPtr) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MemoryMappedViewAccessor(UnmanagedMemoryAccessor, IDisposable):
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
    @property
    def PointerOffset(self) -> int:
        """"""
    @property
    def SafeMemoryMappedViewHandle(self) -> SafeMemoryMappedViewHandle:
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
    def Read(self, position: int, structure: T) -> tuple[None, T]:
        """"""
    def ReadArray(self, position: int, array: Array[T], offset: int, count: int) -> int:
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
    def WriteArray(self, position: int, array: Array[T], offset: int, count: int) -> None:
        """"""

class MemoryMappedViewStream(UnmanagedMemoryStream, IDisposable):
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
    def PointerOffset(self) -> int:
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
    def SafeMemoryMappedViewHandle(self) -> SafeMemoryMappedViewHandle:
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
