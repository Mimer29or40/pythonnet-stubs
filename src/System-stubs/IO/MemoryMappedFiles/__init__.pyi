from __future__ import annotations

from typing import Tuple
from typing import overload

from Microsoft.Win32.SafeHandles import SafeMemoryMappedFileHandle
from Microsoft.Win32.SafeHandles import SafeMemoryMappedViewHandle
from System import Array
from System import AsyncCallback
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
        """

        :return:
        """
    @classmethod
    @overload
    def CreateFromFile(cls, path: str) -> MemoryMappedFile:
        """

        :param path:
        :return:
        """
    @classmethod
    @overload
    def CreateFromFile(cls, path: str, mode: FileMode) -> MemoryMappedFile:
        """

        :param path:
        :param mode:
        :return:
        """
    @classmethod
    @overload
    def CreateFromFile(cls, path: str, mode: FileMode, mapName: str) -> MemoryMappedFile:
        """

        :param path:
        :param mode:
        :param mapName:
        :return:
        """
    @classmethod
    @overload
    def CreateFromFile(
        cls, path: str, mode: FileMode, mapName: str, capacity: int
    ) -> MemoryMappedFile:
        """

        :param path:
        :param mode:
        :param mapName:
        :param capacity:
        :return:
        """
    @classmethod
    @overload
    def CreateFromFile(
        cls, path: str, mode: FileMode, mapName: str, capacity: int, access: MemoryMappedFileAccess
    ) -> MemoryMappedFile:
        """

        :param path:
        :param mode:
        :param mapName:
        :param capacity:
        :param access:
        :return:
        """
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
        """

        :param fileStream:
        :param mapName:
        :param capacity:
        :param access:
        :param inheritability:
        :param leaveOpen:
        :return:
        """
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
        """

        :param fileStream:
        :param mapName:
        :param capacity:
        :param access:
        :param memoryMappedFileSecurity:
        :param inheritability:
        :param leaveOpen:
        :return:
        """
    @classmethod
    @overload
    def CreateNew(cls, mapName: str, capacity: int) -> MemoryMappedFile:
        """

        :param mapName:
        :param capacity:
        :return:
        """
    @classmethod
    @overload
    def CreateNew(
        cls, mapName: str, capacity: int, access: MemoryMappedFileAccess
    ) -> MemoryMappedFile:
        """

        :param mapName:
        :param capacity:
        :param access:
        :return:
        """
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
        """

        :param mapName:
        :param capacity:
        :param access:
        :param options:
        :param inheritability:
        :return:
        """
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
        """

        :param mapName:
        :param capacity:
        :param access:
        :param options:
        :param memoryMappedFileSecurity:
        :param inheritability:
        :return:
        """
    @classmethod
    @overload
    def CreateOrOpen(cls, mapName: str, capacity: int) -> MemoryMappedFile:
        """

        :param mapName:
        :param capacity:
        :return:
        """
    @classmethod
    @overload
    def CreateOrOpen(
        cls, mapName: str, capacity: int, access: MemoryMappedFileAccess
    ) -> MemoryMappedFile:
        """

        :param mapName:
        :param capacity:
        :param access:
        :return:
        """
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
        """

        :param mapName:
        :param capacity:
        :param access:
        :param options:
        :param inheritability:
        :return:
        """
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
        """

        :param mapName:
        :param capacity:
        :param access:
        :param options:
        :param memoryMappedFileSecurity:
        :param inheritability:
        :return:
        """
    @overload
    def CreateViewAccessor(self) -> MemoryMappedViewAccessor:
        """

        :return:
        """
    @overload
    def CreateViewAccessor(self, offset: int, size: int) -> MemoryMappedViewAccessor:
        """

        :param offset:
        :param size:
        :return:
        """
    @overload
    def CreateViewAccessor(
        self, offset: int, size: int, access: MemoryMappedFileAccess
    ) -> MemoryMappedViewAccessor:
        """

        :param offset:
        :param size:
        :param access:
        :return:
        """
    @overload
    def CreateViewStream(self) -> MemoryMappedViewStream:
        """

        :return:
        """
    @overload
    def CreateViewStream(self, offset: int, size: int) -> MemoryMappedViewStream:
        """

        :param offset:
        :param size:
        :return:
        """
    @overload
    def CreateViewStream(
        self, offset: int, size: int, access: MemoryMappedFileAccess
    ) -> MemoryMappedViewStream:
        """

        :param offset:
        :param size:
        :param access:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAccessControl(self) -> MemoryMappedFileSecurity:
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
    @classmethod
    @overload
    def OpenExisting(cls, mapName: str) -> MemoryMappedFile:
        """

        :param mapName:
        :return:
        """
    @classmethod
    @overload
    def OpenExisting(
        cls, mapName: str, desiredAccessRights: MemoryMappedFileRights
    ) -> MemoryMappedFile:
        """

        :param mapName:
        :param desiredAccessRights:
        :return:
        """
    @classmethod
    @overload
    def OpenExisting(
        cls,
        mapName: str,
        desiredAccessRights: MemoryMappedFileRights,
        inheritability: HandleInheritability,
    ) -> MemoryMappedFile:
        """

        :param mapName:
        :param desiredAccessRights:
        :param inheritability:
        :return:
        """
    def SetAccessControl(self, memoryMappedFileSecurity: MemoryMappedFileSecurity) -> None:
        """

        :param memoryMappedFileSecurity:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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
    def AddAccessRule(self, rule: AccessRule[MemoryMappedFileRights]) -> None:
        """

        :param rule:
        """
    def AddAuditRule(self, rule: AuditRule[MemoryMappedFileRights]) -> None:
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
    def RemoveAccessRule(self, rule: AccessRule[MemoryMappedFileRights]) -> bool:
        """

        :param rule:
        :return:
        """
    def RemoveAccessRuleAll(self, rule: AccessRule[MemoryMappedFileRights]) -> None:
        """

        :param rule:
        """
    def RemoveAccessRuleSpecific(self, rule: AccessRule[MemoryMappedFileRights]) -> None:
        """

        :param rule:
        """
    def RemoveAuditRule(self, rule: AuditRule[MemoryMappedFileRights]) -> bool:
        """

        :param rule:
        :return:
        """
    def RemoveAuditRuleAll(self, rule: AuditRule[MemoryMappedFileRights]) -> None:
        """

        :param rule:
        """
    def RemoveAuditRuleSpecific(self, rule: AuditRule[MemoryMappedFileRights]) -> None:
        """

        :param rule:
        """
    def ResetAccessRule(self, rule: AccessRule[MemoryMappedFileRights]) -> None:
        """

        :param rule:
        """
    def SetAccessRule(self, rule: AccessRule[MemoryMappedFileRights]) -> None:
        """

        :param rule:
        """
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetAuditRule(self, rule: AuditRule[MemoryMappedFileRights]) -> None:
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

class MemoryMappedView(Object, IDisposable):
    """"""

    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self, capacity: IntPtr) -> None:
        """

        :param capacity:
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

class MemoryMappedViewAccessor(UnmanagedMemoryAccessor, IDisposable):
    """"""

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
    @property
    def PointerOffset(self) -> int:
        """

        :return:
        """
    @property
    def SafeMemoryMappedViewHandle(self) -> SafeMemoryMappedViewHandle:
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

class MemoryMappedViewStream(UnmanagedMemoryStream, IDisposable):
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
    def PointerOffset(self) -> int:
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
    def SafeMemoryMappedViewHandle(self) -> SafeMemoryMappedViewHandle:
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
