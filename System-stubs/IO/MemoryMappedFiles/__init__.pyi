from __future__ import annotations

from typing import Union, overload

from Microsoft.Win32.SafeHandles import SafeMemoryMappedFileHandle, SafeMemoryMappedViewHandle
from System import Boolean, Enum, IDisposable, Int32, Int64, IntPtr, Object, String, Void
from System.IO import FileMode, FileStream, HandleInheritability, UnmanagedMemoryAccessor, UnmanagedMemoryStream
from System.Security.AccessControl import ObjectSecurity

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class MemoryMappedFile(ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def SafeMemoryMappedFileHandle(self) -> SafeMemoryMappedFileHandle: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def CreateFromFile(path: StringType) -> MemoryMappedFile: ...
    
    @staticmethod
    @overload
    def CreateFromFile(path: StringType, mode: FileMode) -> MemoryMappedFile: ...
    
    @staticmethod
    @overload
    def CreateFromFile(path: StringType, mode: FileMode, mapName: StringType) -> MemoryMappedFile: ...
    
    @staticmethod
    @overload
    def CreateFromFile(path: StringType, mode: FileMode, mapName: StringType, capacity: LongType) -> MemoryMappedFile: ...
    
    @staticmethod
    @overload
    def CreateFromFile(path: StringType, mode: FileMode, mapName: StringType, capacity: LongType, access: MemoryMappedFileAccess) -> MemoryMappedFile: ...
    
    @staticmethod
    @overload
    def CreateFromFile(fileStream: FileStream, mapName: StringType, capacity: LongType, access: MemoryMappedFileAccess, inheritability: HandleInheritability, leaveOpen: BooleanType) -> MemoryMappedFile: ...
    
    @staticmethod
    @overload
    def CreateFromFile(fileStream: FileStream, mapName: StringType, capacity: LongType, access: MemoryMappedFileAccess, memoryMappedFileSecurity: MemoryMappedFileSecurity, inheritability: HandleInheritability, leaveOpen: BooleanType) -> MemoryMappedFile: ...
    
    @staticmethod
    @overload
    def CreateNew(mapName: StringType, capacity: LongType) -> MemoryMappedFile: ...
    
    @staticmethod
    @overload
    def CreateNew(mapName: StringType, capacity: LongType, access: MemoryMappedFileAccess) -> MemoryMappedFile: ...
    
    @staticmethod
    @overload
    def CreateNew(mapName: StringType, capacity: LongType, access: MemoryMappedFileAccess, options: MemoryMappedFileOptions, inheritability: HandleInheritability) -> MemoryMappedFile: ...
    
    @staticmethod
    @overload
    def CreateNew(mapName: StringType, capacity: LongType, access: MemoryMappedFileAccess, options: MemoryMappedFileOptions, memoryMappedFileSecurity: MemoryMappedFileSecurity, inheritability: HandleInheritability) -> MemoryMappedFile: ...
    
    @staticmethod
    @overload
    def CreateOrOpen(mapName: StringType, capacity: LongType) -> MemoryMappedFile: ...
    
    @staticmethod
    @overload
    def CreateOrOpen(mapName: StringType, capacity: LongType, access: MemoryMappedFileAccess) -> MemoryMappedFile: ...
    
    @staticmethod
    @overload
    def CreateOrOpen(mapName: StringType, capacity: LongType, access: MemoryMappedFileAccess, options: MemoryMappedFileOptions, inheritability: HandleInheritability) -> MemoryMappedFile: ...
    
    @staticmethod
    @overload
    def CreateOrOpen(mapName: StringType, capacity: LongType, access: MemoryMappedFileAccess, options: MemoryMappedFileOptions, memoryMappedFileSecurity: MemoryMappedFileSecurity, inheritability: HandleInheritability) -> MemoryMappedFile: ...
    
    @overload
    def CreateViewAccessor(self) -> MemoryMappedViewAccessor: ...
    
    @overload
    def CreateViewAccessor(self, offset: LongType, size: LongType) -> MemoryMappedViewAccessor: ...
    
    @overload
    def CreateViewAccessor(self, offset: LongType, size: LongType, access: MemoryMappedFileAccess) -> MemoryMappedViewAccessor: ...
    
    @overload
    def CreateViewStream(self) -> MemoryMappedViewStream: ...
    
    @overload
    def CreateViewStream(self, offset: LongType, size: LongType) -> MemoryMappedViewStream: ...
    
    @overload
    def CreateViewStream(self, offset: LongType, size: LongType, access: MemoryMappedFileAccess) -> MemoryMappedViewStream: ...
    
    def Dispose(self) -> VoidType: ...
    
    def GetAccessControl(self) -> MemoryMappedFileSecurity: ...
    
    @staticmethod
    @overload
    def OpenExisting(mapName: StringType) -> MemoryMappedFile: ...
    
    @staticmethod
    @overload
    def OpenExisting(mapName: StringType, desiredAccessRights: MemoryMappedFileRights) -> MemoryMappedFile: ...
    
    @staticmethod
    @overload
    def OpenExisting(mapName: StringType, desiredAccessRights: MemoryMappedFileRights, inheritability: HandleInheritability) -> MemoryMappedFile: ...
    
    def SetAccessControl(self, memoryMappedFileSecurity: MemoryMappedFileSecurity) -> VoidType: ...
    
    def get_SafeMemoryMappedFileHandle(self) -> SafeMemoryMappedFileHandle: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MemoryMappedFileSecurity(ObjectSecurity[MemoryMappedFileRights]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MemoryMappedView(ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def Flush(self, capacity: NIntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MemoryMappedViewAccessor(UnmanagedMemoryAccessor, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def PointerOffset(self) -> LongType: ...
    
    @property
    def SafeMemoryMappedViewHandle(self) -> SafeMemoryMappedViewHandle: ...
    
    # ---------- Methods ---------- #
    
    def Flush(self) -> VoidType: ...
    
    def get_PointerOffset(self) -> LongType: ...
    
    def get_SafeMemoryMappedViewHandle(self) -> SafeMemoryMappedViewHandle: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MemoryMappedViewStream(UnmanagedMemoryStream, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def PointerOffset(self) -> LongType: ...
    
    @property
    def SafeMemoryMappedViewHandle(self) -> SafeMemoryMappedViewHandle: ...
    
    # ---------- Methods ---------- #
    
    def Flush(self) -> VoidType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def get_PointerOffset(self) -> LongType: ...
    
    def get_SafeMemoryMappedViewHandle(self) -> SafeMemoryMappedViewHandle: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class MemoryMappedFileAccess(Enum):
    ReadWrite = 0
    Read = 1
    Write = 2
    CopyOnWrite = 3
    ReadExecute = 4
    ReadWriteExecute = 5


class MemoryMappedFileOptions(Enum):
    #None = 0
    DelayAllocatePages = 67108864


class MemoryMappedFileRights(Enum):
    CopyOnWrite = 1
    Write = 2
    Read = 4
    ReadWrite = 6
    Execute = 8
    ReadExecute = 12
    ReadWriteExecute = 14
    Delete = 65536
    ReadPermissions = 131072
    ChangePermissions = 262144
    TakeOwnership = 524288
    FullControl = 983055
    AccessSystemSecurity = 16777216


# No Delegates

__all__ = [
    MemoryMappedFile,
    MemoryMappedFileSecurity,
    MemoryMappedView,
    MemoryMappedViewAccessor,
    MemoryMappedViewStream,
    MemoryMappedFileAccess,
    MemoryMappedFileOptions,
    MemoryMappedFileRights,
]
