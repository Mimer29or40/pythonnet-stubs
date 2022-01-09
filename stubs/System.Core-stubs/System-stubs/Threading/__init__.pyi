from __future__ import annotations

from typing import Union, overload

from System import Boolean, Enum, IDisposable, Int32, Int64, Object, TimeSpan, Void

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
ObjectType = Object
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class ReaderWriterCount(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def lockID(self) -> LongType: ...
    
    @lockID.setter
    def lockID(self, value: LongType) -> None: ...
    
    @property
    def next(self) -> ReaderWriterCount: ...
    
    @next.setter
    def next(self, value: ReaderWriterCount) -> None: ...
    
    @property
    def readercount(self) -> IntType: ...
    
    @readercount.setter
    def readercount(self, value: IntType) -> None: ...
    
    @property
    def upgradecount(self) -> IntType: ...
    
    @upgradecount.setter
    def upgradecount(self, value: IntType) -> None: ...
    
    @property
    def writercount(self) -> IntType: ...
    
    @writercount.setter
    def writercount(self, value: IntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReaderWriterLockSlim(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, recursionPolicy: LockRecursionPolicy): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CurrentReadCount(self) -> IntType: ...
    
    @property
    def IsReadLockHeld(self) -> BooleanType: ...
    
    @property
    def IsUpgradeableReadLockHeld(self) -> BooleanType: ...
    
    @property
    def IsWriteLockHeld(self) -> BooleanType: ...
    
    @property
    def RecursionPolicy(self) -> LockRecursionPolicy: ...
    
    @property
    def RecursiveReadCount(self) -> IntType: ...
    
    @property
    def RecursiveUpgradeCount(self) -> IntType: ...
    
    @property
    def RecursiveWriteCount(self) -> IntType: ...
    
    @property
    def WaitingReadCount(self) -> IntType: ...
    
    @property
    def WaitingUpgradeCount(self) -> IntType: ...
    
    @property
    def WaitingWriteCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def EnterReadLock(self) -> VoidType: ...
    
    def EnterUpgradeableReadLock(self) -> VoidType: ...
    
    def EnterWriteLock(self) -> VoidType: ...
    
    def ExitReadLock(self) -> VoidType: ...
    
    def ExitUpgradeableReadLock(self) -> VoidType: ...
    
    def ExitWriteLock(self) -> VoidType: ...
    
    @overload
    def TryEnterReadLock(self, timeout: TimeSpan) -> BooleanType: ...
    
    @overload
    def TryEnterReadLock(self, millisecondsTimeout: IntType) -> BooleanType: ...
    
    @overload
    def TryEnterUpgradeableReadLock(self, timeout: TimeSpan) -> BooleanType: ...
    
    @overload
    def TryEnterUpgradeableReadLock(self, millisecondsTimeout: IntType) -> BooleanType: ...
    
    @overload
    def TryEnterWriteLock(self, timeout: TimeSpan) -> BooleanType: ...
    
    @overload
    def TryEnterWriteLock(self, millisecondsTimeout: IntType) -> BooleanType: ...
    
    def get_CurrentReadCount(self) -> IntType: ...
    
    def get_IsReadLockHeld(self) -> BooleanType: ...
    
    def get_IsUpgradeableReadLockHeld(self) -> BooleanType: ...
    
    def get_IsWriteLockHeld(self) -> BooleanType: ...
    
    def get_RecursionPolicy(self) -> LockRecursionPolicy: ...
    
    def get_RecursiveReadCount(self) -> IntType: ...
    
    def get_RecursiveUpgradeCount(self) -> IntType: ...
    
    def get_RecursiveWriteCount(self) -> IntType: ...
    
    def get_WaitingReadCount(self) -> IntType: ...
    
    def get_WaitingUpgradeCount(self) -> IntType: ...
    
    def get_WaitingWriteCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class LockRecursionPolicy(Enum):
    NoRecursion: IntType = 0
    SupportsRecursion: IntType = 1


# No Delegates

__all__ = [
    ReaderWriterCount,
    ReaderWriterLockSlim,
    LockRecursionPolicy,
]
