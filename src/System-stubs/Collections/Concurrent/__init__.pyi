from __future__ import annotations

from abc import ABC
from typing import Generic, List, Protocol, Tuple, TypeVar, Union, overload

from System import Array, Boolean, Enum, Func, IDisposable, Int32, Int64, Object, TimeSpan, Tuple, ValueType, Void
from System.Collections import ICollection, IDictionary, IEnumerable
from System.Collections.Generic import ICollection, IDictionary, IEnumerable, IEnumerator, IEqualityComparer, IList, IReadOnlyCollection, IReadOnlyDictionary, KeyValuePair
from System.Diagnostics.Tracing import EventSource
from System.Threading import CancellationToken

# ---------- Types ---------- #

T = TypeVar('T')
TArg = TypeVar('TArg')
TKey = TypeVar('TKey')
TSource = TypeVar('TSource')
TValue = TypeVar('TValue')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
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


class CDSCollectionETWBCLProvider(EventSource, IDisposable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Log() -> CDSCollectionETWBCLProvider: ...
    
    @staticmethod
    @Log.setter
    def Log(value: CDSCollectionETWBCLProvider) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ConcurrentBag_TryPeekSteals(self) -> VoidType: ...
    
    def ConcurrentBag_TryTakeSteals(self) -> VoidType: ...
    
    def ConcurrentDictionary_AcquiringAllLocks(self, numOfBuckets: IntType) -> VoidType: ...
    
    def ConcurrentStack_FastPopFailed(self, spinCount: IntType) -> VoidType: ...
    
    def ConcurrentStack_FastPushFailed(self, spinCount: IntType) -> VoidType: ...
    
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


class ConcurrentDictionary(Generic[TKey, TValue], ObjectType, IDictionary[TKey, TValue], ICollection[KeyValuePair[TKey, TValue]], IEnumerable[KeyValuePair[TKey, TValue]], IEnumerable, IDictionary, ICollection, IReadOnlyDictionary[TKey, TValue], IReadOnlyCollection[KeyValuePair[TKey, TValue]]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, concurrencyLevel: IntType, capacity: IntType): ...
    
    @overload
    def __init__(self, collection: IEnumerable[KeyValuePair[TKey, TValue]]): ...
    
    @overload
    def __init__(self, comparer: IEqualityComparer[TKey]): ...
    
    @overload
    def __init__(self, collection: IEnumerable[KeyValuePair[TKey, TValue]], comparer: IEqualityComparer[TKey]): ...
    
    @overload
    def __init__(self, concurrencyLevel: IntType, collection: IEnumerable[KeyValuePair[TKey, TValue]], comparer: IEqualityComparer[TKey]): ...
    
    @overload
    def __init__(self, concurrencyLevel: IntType, capacity: IntType, comparer: IEqualityComparer[TKey]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsEmpty(self) -> BooleanType: ...
    
    def __getitem__(self, key: TKey) -> TValue: ...
    
    def __setitem__(self, key: TKey, value: TValue) -> None: ...
    
    @property
    def Keys(self) -> ICollection[TKey]: ...
    
    @property
    def Values(self) -> ICollection[TValue]: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AddOrUpdate(self, key: TKey, addValueFactory: Func[TKey, TArg, TValue], updateValueFactory: Func[TKey, TValue, TArg, TValue], factoryArgument: TArg) -> TValue: ...
    
    @overload
    def AddOrUpdate(self, key: TKey, addValueFactory: Func[TKey, TValue], updateValueFactory: Func[TKey, TValue, TValue]) -> TValue: ...
    
    @overload
    def AddOrUpdate(self, key: TKey, addValue: TValue, updateValueFactory: Func[TKey, TValue, TValue]) -> TValue: ...
    
    def Clear(self) -> VoidType: ...
    
    def ContainsKey(self, key: TKey) -> BooleanType: ...
    
    def GetEnumerator(self) -> IEnumerator[KeyValuePair[TKey, TValue]]: ...
    
    @overload
    def GetOrAdd(self, key: TKey, valueFactory: Func[TKey, TValue]) -> TValue: ...
    
    @overload
    def GetOrAdd(self, key: TKey, value: TValue) -> TValue: ...
    
    @overload
    def GetOrAdd(self, key: TKey, valueFactory: Func[TKey, TArg, TValue], factoryArgument: TArg) -> TValue: ...
    
    def ToArray(self) -> ArrayType[KeyValuePair[TKey, TValue]]: ...
    
    def TryAdd(self, key: TKey, value: TValue) -> BooleanType: ...
    
    def TryGetValue(self, key: TKey, value: TValue) -> Tuple[BooleanType, TValue]: ...
    
    def TryRemove(self, key: TKey, value: TValue) -> Tuple[BooleanType, TValue]: ...
    
    def TryUpdate(self, key: TKey, newValue: TValue, comparisonValue: TValue) -> BooleanType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsEmpty(self) -> BooleanType: ...
    
    def get_Item(self, key: TKey) -> TValue: ...
    
    def get_Keys(self) -> ICollection[TKey]: ...
    
    def get_Values(self) -> ICollection[TValue]: ...
    
    def set_Item(self, key: TKey, value: TValue) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConcurrentQueue(Generic[T], ObjectType, IProducerConsumerCollection[T], IEnumerable[T], IEnumerable, ICollection, IReadOnlyCollection[T]):
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
    
    def CopyTo(self, array: ArrayType[T], index: IntType) -> VoidType: ...
    
    def Enqueue(self, item: T) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[T]: ...
    
    def ToArray(self) -> ArrayType[T]: ...
    
    def TryDequeue(self, result: T) -> Tuple[BooleanType, T]: ...
    
    def TryPeek(self, result: T) -> Tuple[BooleanType, T]: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsEmpty(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConcurrentStack(Generic[T], ObjectType, IProducerConsumerCollection[T], IEnumerable[T], IEnumerable, ICollection, IReadOnlyCollection[T]):
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
    
    def Clear(self) -> VoidType: ...
    
    def CopyTo(self, array: ArrayType[T], index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[T]: ...
    
    def Push(self, item: T) -> VoidType: ...
    
    @overload
    def PushRange(self, items: ArrayType[T]) -> VoidType: ...
    
    @overload
    def PushRange(self, items: ArrayType[T], startIndex: IntType, count: IntType) -> VoidType: ...
    
    def ToArray(self) -> ArrayType[T]: ...
    
    def TryPeek(self, result: T) -> Tuple[BooleanType, T]: ...
    
    def TryPop(self, result: T) -> Tuple[BooleanType, T]: ...
    
    @overload
    def TryPopRange(self, items: ArrayType[T]) -> IntType: ...
    
    @overload
    def TryPopRange(self, items: ArrayType[T], startIndex: IntType, count: IntType) -> IntType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsEmpty(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OrderablePartitioner(Protocol[TSource], Partitioner[TSource]):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def KeysNormalized(self) -> BooleanType: ...
    
    @property
    def KeysOrderedAcrossPartitions(self) -> BooleanType: ...
    
    @property
    def KeysOrderedInEachPartition(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def GetDynamicPartitions(self) -> IEnumerable[TSource]: ...
    
    def GetOrderableDynamicPartitions(self) -> IEnumerable[KeyValuePair[LongType, TSource]]: ...
    
    def GetOrderablePartitions(self, partitionCount: IntType) -> IList[IEnumerator[KeyValuePair[LongType, TSource]]]: ...
    
    def GetPartitions(self, partitionCount: IntType) -> IList[IEnumerator[TSource]]: ...
    
    def get_KeysNormalized(self) -> BooleanType: ...
    
    def get_KeysOrderedAcrossPartitions(self) -> BooleanType: ...
    
    def get_KeysOrderedInEachPartition(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Partitioner(Protocol[TSource], ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def SupportsDynamicPartitions(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def GetDynamicPartitions(self) -> IEnumerable[TSource]: ...
    
    def GetPartitions(self, partitionCount: IntType) -> IList[IEnumerator[TSource]]: ...
    
    def get_SupportsDynamicPartitions(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Partitioner(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Create(fromInclusive: LongType, toExclusive: LongType) -> OrderablePartitioner[Tuple[LongType, LongType]]: ...
    
    @staticmethod
    @overload
    def Create(fromInclusive: LongType, toExclusive: LongType, rangeSize: LongType) -> OrderablePartitioner[Tuple[LongType, LongType]]: ...
    
    @staticmethod
    @overload
    def Create(fromInclusive: IntType, toExclusive: IntType) -> OrderablePartitioner[Tuple[IntType, IntType]]: ...
    
    @staticmethod
    @overload
    def Create(fromInclusive: IntType, toExclusive: IntType, rangeSize: IntType) -> OrderablePartitioner[Tuple[IntType, IntType]]: ...
    
    @staticmethod
    @overload
    def Create(list: IList[TSource], loadBalance: BooleanType) -> OrderablePartitioner[TSource]: ...
    
    @staticmethod
    @overload
    def Create(array: ArrayType[TSource], loadBalance: BooleanType) -> OrderablePartitioner[TSource]: ...
    
    @staticmethod
    @overload
    def Create(source: IEnumerable[TSource]) -> OrderablePartitioner[TSource]: ...
    
    @staticmethod
    @overload
    def Create(source: IEnumerable[TSource], partitionerOptions: EnumerablePartitionerOptions) -> OrderablePartitioner[TSource]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemCollectionsConcurrent_ProducerConsumerCollectionDebugView(Generic[T], ObjectType):
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


# ---------- Structs ---------- #

class VolatileBool(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def m_value(self) -> BooleanType: ...
    
    @m_value.setter
    def m_value(self, value: BooleanType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, value: BooleanType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Interfaces ---------- #

class IProducerConsumerCollection(Protocol[T], IEnumerable[T], IEnumerable, ICollection):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CopyTo(self, array: ArrayType[T], index: IntType) -> VoidType: ...
    
    def ToArray(self) -> ArrayType[T]: ...
    
    def TryAdd(self, item: T) -> BooleanType: ...
    
    def TryTake(self, item: T) -> Tuple[BooleanType, T]: ...
    
    # No Events


# ---------- Enums ---------- #

class EnumerablePartitionerOptions(Enum):
    #None = 0
    NoBuffering = 1


# No Delegates

__all__ = [
    BlockingCollection,
    CDSCollectionETWBCLProvider,
    ConcurrentBag,
    ConcurrentDictionary,
    ConcurrentQueue,
    ConcurrentStack,
    OrderablePartitioner,
    Partitioner,
    SystemCollectionsConcurrent_ProducerConsumerCollectionDebugView,
    SystemThreadingCollection_IProducerConsumerCollectionDebugView,
    SystemThreadingCollections_BlockingCollectionDebugView,
    VolatileBool,
    IProducerConsumerCollection,
    EnumerablePartitionerOptions,
]
