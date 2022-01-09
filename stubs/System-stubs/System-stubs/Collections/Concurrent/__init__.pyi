from __future__ import annotations

from typing import Generic, List, Tuple, TypeVar, Union, overload

from System import Array, Boolean, IDisposable, Int32, Object, TimeSpan, Void
from System.Collections import ICollection, IEnumerable
from System.Collections.Concurrent import IProducerConsumerCollection
from System.Collections.Generic import IEnumerable, IEnumerator, IReadOnlyCollection
from System.Threading import CancellationToken

# ---------- Types ---------- #

T = TypeVar('T')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
ObjectType = Object
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class BlockingCollection(Generic[T], ObjectType, IEnumerable[T], IEnumerable, ICollection, IDisposable, IReadOnlyCollection[T]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, boundedCapacity: IntType): ...
    
    @overload
    def __init__(self, collection: IProducerConsumerCollection[T], boundedCapacity: IntType): ...
    
    @overload
    def __init__(self, collection: IProducerConsumerCollection[T]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BoundedCapacity(self) -> IntType: ...
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsAddingCompleted(self) -> BooleanType: ...
    
    @property
    def IsCompleted(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, item: T) -> VoidType: ...
    
    @overload
    def Add(self, item: T, cancellationToken: CancellationToken) -> VoidType: ...
    
    @staticmethod
    @overload
    def AddToAny(collections: ArrayType[BlockingCollection[T]], item: T) -> IntType: ...
    
    @staticmethod
    @overload
    def AddToAny(collections: ArrayType[BlockingCollection[T]], item: T, cancellationToken: CancellationToken) -> IntType: ...
    
    def CompleteAdding(self) -> VoidType: ...
    
    def CopyTo(self, array: ArrayType[T], index: IntType) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    @overload
    def GetConsumingEnumerable(self) -> IEnumerable[T]: ...
    
    @overload
    def GetConsumingEnumerable(self, cancellationToken: CancellationToken) -> IEnumerable[T]: ...
    
    @overload
    def Take(self) -> T: ...
    
    @overload
    def Take(self, cancellationToken: CancellationToken) -> T: ...
    
    @staticmethod
    @overload
    def TakeFromAny(collections: ArrayType[BlockingCollection[T]], item: T) -> Tuple[IntType, T]: ...
    
    @staticmethod
    @overload
    def TakeFromAny(collections: ArrayType[BlockingCollection[T]], item: T, cancellationToken: CancellationToken) -> Tuple[IntType, T]: ...
    
    def ToArray(self) -> ArrayType[T]: ...
    
    @overload
    def TryAdd(self, item: T) -> BooleanType: ...
    
    @overload
    def TryAdd(self, item: T, timeout: TimeSpan) -> BooleanType: ...
    
    @overload
    def TryAdd(self, item: T, millisecondsTimeout: IntType) -> BooleanType: ...
    
    @overload
    def TryAdd(self, item: T, millisecondsTimeout: IntType, cancellationToken: CancellationToken) -> BooleanType: ...
    
    @staticmethod
    @overload
    def TryAddToAny(collections: ArrayType[BlockingCollection[T]], item: T) -> IntType: ...
    
    @staticmethod
    @overload
    def TryAddToAny(collections: ArrayType[BlockingCollection[T]], item: T, timeout: TimeSpan) -> IntType: ...
    
    @staticmethod
    @overload
    def TryAddToAny(collections: ArrayType[BlockingCollection[T]], item: T, millisecondsTimeout: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def TryAddToAny(collections: ArrayType[BlockingCollection[T]], item: T, millisecondsTimeout: IntType, cancellationToken: CancellationToken) -> IntType: ...
    
    @overload
    def TryTake(self, item: T) -> Tuple[BooleanType, T]: ...
    
    @overload
    def TryTake(self, item: T, timeout: TimeSpan) -> Tuple[BooleanType, T]: ...
    
    @overload
    def TryTake(self, item: T, millisecondsTimeout: IntType) -> Tuple[BooleanType, T]: ...
    
    @overload
    def TryTake(self, item: T, millisecondsTimeout: IntType, cancellationToken: CancellationToken) -> Tuple[BooleanType, T]: ...
    
    @staticmethod
    @overload
    def TryTakeFromAny(collections: ArrayType[BlockingCollection[T]], item: T) -> Tuple[IntType, T]: ...
    
    @staticmethod
    @overload
    def TryTakeFromAny(collections: ArrayType[BlockingCollection[T]], item: T, timeout: TimeSpan) -> Tuple[IntType, T]: ...
    
    @staticmethod
    @overload
    def TryTakeFromAny(collections: ArrayType[BlockingCollection[T]], item: T, millisecondsTimeout: IntType) -> Tuple[IntType, T]: ...
    
    @staticmethod
    @overload
    def TryTakeFromAny(collections: ArrayType[BlockingCollection[T]], item: T, millisecondsTimeout: IntType, cancellationToken: CancellationToken) -> Tuple[IntType, T]: ...
    
    def get_BoundedCapacity(self) -> IntType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsAddingCompleted(self) -> BooleanType: ...
    
    def get_IsCompleted(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConcurrentBag(Generic[T], ObjectType, IProducerConsumerCollection[T], IEnumerable[T], IEnumerable, ICollection, IReadOnlyCollection[T]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, collection: IEnumerable[T]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsEmpty(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, item: T) -> VoidType: ...
    
    def CopyTo(self, array: ArrayType[T], index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[T]: ...
    
    def ToArray(self) -> ArrayType[T]: ...
    
    def TryPeek(self, result: T) -> Tuple[BooleanType, T]: ...
    
    def TryTake(self, result: T) -> Tuple[BooleanType, T]: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsEmpty(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemThreadingCollection_IProducerConsumerCollectionDebugView(Generic[T], ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, collection: IProducerConsumerCollection[T]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Items(self) -> ArrayType[T]: ...
    
    # ---------- Methods ---------- #
    
    def get_Items(self) -> ArrayType[T]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemThreadingCollections_BlockingCollectionDebugView(Generic[T], ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, collection: BlockingCollection[T]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Items(self) -> ArrayType[T]: ...
    
    # ---------- Methods ---------- #
    
    def get_Items(self) -> ArrayType[T]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# No Enums

# No Delegates

__all__ = [
    BlockingCollection,
    ConcurrentBag,
    SystemThreadingCollection_IProducerConsumerCollectionDebugView,
    SystemThreadingCollections_BlockingCollectionDebugView,
]
