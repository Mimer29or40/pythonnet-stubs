"""Automatically generated stubs for C# namespace: System.Collections.Concurrent."""

from abc import ABC
from collections.abc import Iterator
from typing import ClassVar
from typing import Final
from typing import Self
from typing import overload

from System import Array
from System import Enum
from System import EventHandler
from System import Exception
from System import Func
from System import Guid
from System import IDisposable
from System import Object
from System import TimeSpan
from System import Tuple
from System import Type
from System import ValueType
from System.Collections import ICollection
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections.Generic import ICollection
from System.Collections.Generic import IDictionary
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEnumerator
from System.Collections.Generic import IEqualityComparer
from System.Collections.Generic import IList
from System.Collections.Generic import IReadOnlyCollection
from System.Collections.Generic import IReadOnlyDictionary
from System.Collections.Generic import KeyValuePair
from System.Diagnostics.Tracing import EventChannel
from System.Diagnostics.Tracing import EventCommandEventArgs
from System.Diagnostics.Tracing import EventKeywords
from System.Diagnostics.Tracing import EventLevel
from System.Diagnostics.Tracing import EventSource
from System.Diagnostics.Tracing import EventSourceOptions
from System.Diagnostics.Tracing import EventSourceSettings
from System.Threading import CancellationToken

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BlockingCollection[T](
    Object, IEnumerable[T], IReadOnlyCollection[T], ICollection, IEnumerable, IDisposable
):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, boundedCapacity: int) -> None:
        """"""
    @overload
    def __init__(self, collection: IProducerConsumerCollection[T], boundedCapacity: int) -> None:
        """"""
    @overload
    def __init__(self, collection: IProducerConsumerCollection[T]) -> None:
        """"""
    @property
    def BoundedCapacity(self) -> int:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsAddingCompleted(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, item: T) -> None:
        """"""
    @overload
    def Add(self, item: T, cancellationToken: CancellationToken) -> None:
        """"""
    @classmethod
    @overload
    def AddToAny(cls, collections: Array[BlockingCollection[T]], item: T) -> int:
        """"""
    @classmethod
    @overload
    def AddToAny(
        cls,
        collections: Array[BlockingCollection[T]],
        item: T,
        cancellationToken: CancellationToken,
    ) -> int:
        """"""
    def CompleteAdding(self) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[T], index: int) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetConsumingEnumerable(self) -> IEnumerable[T]:
        """"""
    @overload
    def GetConsumingEnumerable(self, cancellationToken: CancellationToken) -> IEnumerable[T]:
        """"""
    def GetEnumerator[T](self) -> IEnumerator[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Take(self) -> T:
        """"""
    @overload
    def Take(self, cancellationToken: CancellationToken) -> T:
        """"""
    @classmethod
    @overload
    def TakeFromAny(cls, collections: Array[BlockingCollection[T]], item: T) -> tuple[int, T]:
        """"""
    @classmethod
    @overload
    def TakeFromAny(
        cls,
        collections: Array[BlockingCollection[T]],
        item: T,
        cancellationToken: CancellationToken,
    ) -> tuple[int, T]:
        """"""
    def ToArray(self) -> Array[T]:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def TryAdd(self, item: T) -> bool:
        """"""
    @overload
    def TryAdd(self, item: T, millisecondsTimeout: int) -> bool:
        """"""
    @overload
    def TryAdd(
        self, item: T, millisecondsTimeout: int, cancellationToken: CancellationToken
    ) -> bool:
        """"""
    @overload
    def TryAdd(self, item: T, timeout: TimeSpan) -> bool:
        """"""
    @classmethod
    @overload
    def TryAddToAny(cls, collections: Array[BlockingCollection[T]], item: T) -> int:
        """"""
    @classmethod
    @overload
    def TryAddToAny(
        cls, collections: Array[BlockingCollection[T]], item: T, millisecondsTimeout: int
    ) -> int:
        """"""
    @classmethod
    @overload
    def TryAddToAny(
        cls,
        collections: Array[BlockingCollection[T]],
        item: T,
        millisecondsTimeout: int,
        cancellationToken: CancellationToken,
    ) -> int:
        """"""
    @classmethod
    @overload
    def TryAddToAny(
        cls, collections: Array[BlockingCollection[T]], item: T, timeout: TimeSpan
    ) -> int:
        """"""
    @overload
    def TryTake(self, item: T) -> tuple[bool, T]:
        """"""
    @overload
    def TryTake(self, item: T, millisecondsTimeout: int) -> tuple[bool, T]:
        """"""
    @overload
    def TryTake(
        self, item: T, millisecondsTimeout: int, cancellationToken: CancellationToken
    ) -> tuple[bool, T]:
        """"""
    @overload
    def TryTake(self, item: T, timeout: TimeSpan) -> tuple[bool, T]:
        """"""
    @classmethod
    @overload
    def TryTakeFromAny(cls, collections: Array[BlockingCollection[T]], item: T) -> tuple[int, T]:
        """"""
    @classmethod
    @overload
    def TryTakeFromAny(
        cls, collections: Array[BlockingCollection[T]], item: T, millisecondsTimeout: int
    ) -> tuple[int, T]:
        """"""
    @classmethod
    @overload
    def TryTakeFromAny(
        cls,
        collections: Array[BlockingCollection[T]],
        item: T,
        millisecondsTimeout: int,
        cancellationToken: CancellationToken,
    ) -> tuple[int, T]:
        """"""
    @classmethod
    @overload
    def TryTakeFromAny(
        cls, collections: Array[BlockingCollection[T]], item: T, timeout: TimeSpan
    ) -> tuple[int, T]:
        """"""
    def __iter__[T](self) -> Iterator[T]:
        """"""
    def __len__(self) -> int:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CDSCollectionETWBCLProvider(EventSource, IDisposable):
    """"""

    Log: ClassVar[CDSCollectionETWBCLProvider]
    """"""
    @property
    def ConstructionException(self) -> Exception:
        """"""
    @property
    def Guid(self) -> Guid:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Settings(self) -> EventSourceSettings:
        """"""
    def ConcurrentBag_TryPeekSteals(self) -> None:
        """"""
    def ConcurrentBag_TryTakeSteals(self) -> None:
        """"""
    def ConcurrentDictionary_AcquiringAllLocks(self, numOfBuckets: int) -> None:
        """"""
    def ConcurrentStack_FastPopFailed(self, spinCount: int) -> None:
        """"""
    def ConcurrentStack_FastPushFailed(self, spinCount: int) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTrait(self, key: str) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsEnabled(self) -> bool:
        """"""
    @overload
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords) -> bool:
        """"""
    @overload
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords, channel: EventChannel) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Write(self, eventName: str) -> None:
        """"""
    @overload
    def Write[T](self, eventName: str, data: T) -> None:
        """"""
    @overload
    def Write(self, eventName: str, options: EventSourceOptions, data: T) -> None:
        """"""
    @overload
    def Write(
        self,
        eventName: str,
        options: EventSourceOptions,
        activityId: Guid,
        relatedActivityId: Guid,
        data: T,
    ) -> None:
        """"""
    @overload
    def Write(self, eventName: str, options: EventSourceOptions) -> None:
        """"""
    @overload
    def Write[T](self, eventName: str, options: EventSourceOptions, data: T) -> None:
        """"""
    EventCommandExecuted: EventType[EventHandler[EventCommandEventArgs]] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ConcurrentBag[T](
    Object,
    IProducerConsumerCollection[T],
    IEnumerable[T],
    IReadOnlyCollection[T],
    ICollection,
    IEnumerable,
):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, collection: IEnumerable[T]) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsEmpty(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def Add(self, item: T) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[T], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[T](self) -> IEnumerator[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToArray(self) -> Array[T]:
        """"""
    def ToString(self) -> str:
        """"""
    def TryAdd(self, item: T) -> bool:
        """"""
    def TryPeek(self, result: T) -> tuple[bool, T]:
        """"""
    def TryTake(self, result: T) -> tuple[bool, T]:
        """"""
    def __iter__[T](self) -> Iterator[T]:
        """"""
    def __len__(self) -> int:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ConcurrentDictionary[TKey, TValue](
    Object,
    ICollection[KeyValuePair[TKey, TValue]],
    IDictionary[TKey, TValue],
    IEnumerable[KeyValuePair[TKey, TValue]],
    IReadOnlyCollection[KeyValuePair[TKey, TValue]],
    IReadOnlyDictionary[TKey, TValue],
    ICollection,
    IDictionary,
    IEnumerable,
):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, concurrencyLevel: int, capacity: int) -> None:
        """"""
    @overload
    def __init__(self, collection: IEnumerable[KeyValuePair[TKey, TValue]]) -> None:
        """"""
    @overload
    def __init__(self, comparer: IEqualityComparer[TKey]) -> None:
        """"""
    @overload
    def __init__(
        self, collection: IEnumerable[KeyValuePair[TKey, TValue]], comparer: IEqualityComparer[TKey]
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        concurrencyLevel: int,
        collection: IEnumerable[KeyValuePair[TKey, TValue]],
        comparer: IEqualityComparer[TKey],
    ) -> None:
        """"""
    @overload
    def __init__(
        self, concurrencyLevel: int, capacity: int, comparer: IEqualityComparer[TKey]
    ) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsEmpty(self) -> bool:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> TValue:
        """"""
    @Item.setter
    def Item(self, value: TValue) -> None: ...
    @property
    def Keys(self) -> ICollection[TKey]:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> ICollection[TValue]:
        """"""
    @overload
    def Add(self, key: TKey, value: TValue) -> None:
        """"""
    @overload
    def Add[TKey, TValue](self, item: KeyValuePair[TKey, TValue]) -> None:
        """"""
    @overload
    def Add(self, key: object, value: object) -> None:
        """"""
    @overload
    def AddOrUpdate(
        self, key: TKey, addValue: TValue, updateValueFactory: Func[TKey, TValue, TValue]
    ) -> TValue:
        """"""
    @overload
    def AddOrUpdate[TArg](
        self,
        key: TKey,
        addValueFactory: Func[TKey, TArg, TValue],
        updateValueFactory: Func[TKey, TValue, TArg, TValue],
        factoryArgument: TArg,
    ) -> TValue:
        """"""
    @overload
    def AddOrUpdate(
        self,
        key: TKey,
        addValueFactory: Func[TKey, TValue],
        updateValueFactory: Func[TKey, TValue, TValue],
    ) -> TValue:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains[TKey, TValue](self, item: KeyValuePair[TKey, TValue]) -> bool:
        """"""
    @overload
    def Contains(self, key: object) -> bool:
        """"""
    def ContainsKey(self, key: TKey) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo[TKey, TValue](
        self, array: Array[KeyValuePair[TKey, TValue]], arrayIndex: int
    ) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[TKey, TValue](self) -> IEnumerator[KeyValuePair[TKey, TValue]]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetOrAdd(self, key: TKey, value: TValue) -> TValue:
        """"""
    @overload
    def GetOrAdd[TArg](
        self, key: TKey, valueFactory: Func[TKey, TArg, TValue], factoryArgument: TArg
    ) -> TValue:
        """"""
    @overload
    def GetOrAdd(self, key: TKey, valueFactory: Func[TKey, TValue]) -> TValue:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Remove(self, key: TKey) -> bool:
        """"""
    @overload
    def Remove[TKey, TValue](self, item: KeyValuePair[TKey, TValue]) -> bool:
        """"""
    @overload
    def Remove(self, key: object) -> None:
        """"""
    def ToArray(self) -> Array[KeyValuePair[TKey, TValue]]:
        """"""
    def ToString(self) -> str:
        """"""
    def TryAdd(self, key: TKey, value: TValue) -> bool:
        """"""
    def TryGetValue(self, key: TKey, value: TValue) -> tuple[bool, TValue]:
        """"""
    def TryRemove(self, key: TKey, value: TValue) -> tuple[bool, TValue]:
        """"""
    def TryUpdate(self, key: TKey, newValue: TValue, comparisonValue: TValue) -> bool:
        """"""
    @overload
    def __contains__[TKey, TValue](self, item: KeyValuePair[TKey, TValue]) -> bool:
        """"""
    @overload
    def __contains__(self, key: object) -> bool:
        """"""
    @overload
    def __contains__(self, key: TKey) -> bool:
        """"""
    def __iter__[TKey, TValue](self) -> Iterator[KeyValuePair[TKey, TValue]]:
        """"""
    @overload
    def __delitem__(self, key: TKey) -> bool:
        """"""
    @overload
    def __delitem__[TKey, TValue](self, item: KeyValuePair[TKey, TValue]) -> bool:
        """"""
    @overload
    def __delitem__(self, key: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, key: TKey) -> TValue:
        """"""
    @overload
    def __getitem__(self, key: object) -> object:
        """"""
    @overload
    def __setitem__(self, key: TKey, value: TValue) -> None:
        """"""
    @overload
    def __setitem__(self, key: object, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ConcurrentQueue[T](
    Object,
    IProducerConsumerCollection[T],
    IEnumerable[T],
    IReadOnlyCollection[T],
    ICollection,
    IEnumerable,
):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, collection: IEnumerable[T]) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsEmpty(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[T], index: int) -> None:
        """"""
    def Enqueue(self, item: T) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[T](self) -> IEnumerator[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToArray(self) -> Array[T]:
        """"""
    def ToString(self) -> str:
        """"""
    def TryAdd(self, item: T) -> bool:
        """"""
    def TryDequeue(self, result: T) -> tuple[bool, T]:
        """"""
    def TryPeek(self, result: T) -> tuple[bool, T]:
        """"""
    def TryTake(self, item: T) -> tuple[bool, T]:
        """"""
    def __iter__[T](self) -> Iterator[T]:
        """"""
    def __len__(self) -> int:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ConcurrentStack[T](
    Object,
    IProducerConsumerCollection[T],
    IEnumerable[T],
    IReadOnlyCollection[T],
    ICollection,
    IEnumerable,
):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, collection: IEnumerable[T]) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsEmpty(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[T], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[T](self) -> IEnumerator[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Push(self, item: T) -> None:
        """"""
    @overload
    def PushRange(self, items: Array[T]) -> None:
        """"""
    @overload
    def PushRange(self, items: Array[T], startIndex: int, count: int) -> None:
        """"""
    def ToArray(self) -> Array[T]:
        """"""
    def ToString(self) -> str:
        """"""
    def TryAdd(self, item: T) -> bool:
        """"""
    def TryPeek(self, result: T) -> tuple[bool, T]:
        """"""
    def TryPop(self, result: T) -> tuple[bool, T]:
        """"""
    @overload
    def TryPopRange(self, items: Array[T]) -> int:
        """"""
    @overload
    def TryPopRange(self, items: Array[T], startIndex: int, count: int) -> int:
        """"""
    def TryTake(self, item: T) -> tuple[bool, T]:
        """"""
    def __iter__[T](self) -> Iterator[T]:
        """"""
    def __len__(self) -> int:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class EnumerablePartitionerOptions(Enum):
    """"""

    _None: EnumerablePartitionerOptions = ...
    """"""
    NoBuffering: EnumerablePartitionerOptions = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IProducerConsumerCollection[T](ABC, IEnumerable[T], ICollection, IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[T], index: int) -> None:
        """"""
    def GetEnumerator[T](self) -> IEnumerator[T]:
        """"""
    def ToArray(self) -> Array[T]:
        """"""
    def TryAdd(self, item: T) -> bool:
        """"""
    def TryTake(self, item: T) -> tuple[bool, T]:
        """"""
    def __iter__[T](self) -> Iterator[T]:
        """"""
    def __len__(self) -> int:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class OrderablePartitioner[TSource](ABC, Partitioner[TSource]):
    """"""
    @property
    def KeysNormalized(self) -> bool:
        """"""
    @property
    def KeysOrderedAcrossPartitions(self) -> bool:
        """"""
    @property
    def KeysOrderedInEachPartition(self) -> bool:
        """"""
    @property
    def SupportsDynamicPartitions(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetDynamicPartitions(self) -> IEnumerable[TSource]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOrderableDynamicPartitions(self) -> IEnumerable[KeyValuePair[int, TSource]]:
        """"""
    def GetOrderablePartitions(
        self, partitionCount: int
    ) -> IList[IEnumerator[KeyValuePair[int, TSource]]]:
        """"""
    def GetPartitions(self, partitionCount: int) -> IList[IEnumerator[TSource]]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Partitioner(ABC, Object):
    """"""
    @classmethod
    @overload
    def Create[TSource](cls, source: IEnumerable[TSource]) -> OrderablePartitioner[TSource]:
        """"""
    @classmethod
    @overload
    def Create[TSource](
        cls, source: IEnumerable[TSource], partitionerOptions: EnumerablePartitionerOptions
    ) -> OrderablePartitioner[TSource]:
        """"""
    @classmethod
    @overload
    def Create[TSource](
        cls, list: IList[TSource], loadBalance: bool
    ) -> OrderablePartitioner[TSource]:
        """"""
    @classmethod
    @overload
    def Create[TSource](
        cls, array: Array[TSource], loadBalance: bool
    ) -> OrderablePartitioner[TSource]:
        """"""
    @classmethod
    @overload
    def Create(cls, fromInclusive: int, toExclusive: int) -> OrderablePartitioner[Tuple[int, int]]:
        """"""
    @classmethod
    @overload
    def Create(
        cls, fromInclusive: int, toExclusive: int, rangeSize: int
    ) -> OrderablePartitioner[Tuple[int, int]]:
        """"""
    @classmethod
    @overload
    def Create(cls, fromInclusive: int, toExclusive: int) -> OrderablePartitioner[Tuple[int, int]]:
        """"""
    @classmethod
    @overload
    def Create(
        cls, fromInclusive: int, toExclusive: int, rangeSize: int
    ) -> OrderablePartitioner[Tuple[int, int]]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Partitioner[TSource](ABC, Object):
    """"""
    @property
    def SupportsDynamicPartitions(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetDynamicPartitions(self) -> IEnumerable[TSource]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetPartitions(self, partitionCount: int) -> IList[IEnumerator[TSource]]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SystemCollectionsConcurrent_ProducerConsumerCollectionDebugView[T](Object):
    """"""
    def __init__(self, collection: IProducerConsumerCollection[T]) -> None:
        """"""
    @property
    def Items(self) -> Array[T]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SystemThreadingCollection_IProducerConsumerCollectionDebugView[T](Object):
    """"""
    def __init__(self, collection: IProducerConsumerCollection[T]) -> None:
        """"""
    @property
    def Items(self) -> Array[T]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SystemThreadingCollections_BlockingCollectionDebugView[T](Object):
    """"""
    def __init__(self, collection: BlockingCollection[T]) -> None:
        """"""
    @property
    def Items(self) -> Array[T]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class VolatileBool(ValueType):
    """"""

    m_value: Final[bool]
    """"""
    def __init__(self, value: bool) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
