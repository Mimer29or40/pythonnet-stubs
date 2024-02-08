from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Iterator
from typing import Tuple
from typing import TypeVar
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
from System.Collections import IEnumerator
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
from System.Diagnostics.Tracing import T
from System.Threading import CancellationToken

T = TypeVar("T")
TArg = TypeVar("TArg")
TKey = TypeVar("TKey")
TSource = TypeVar("TSource")
TValue = TypeVar("TValue")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class BlockingCollection(
    Generic[T],
    Object,
    IEnumerable[T],
    IReadOnlyCollection[T],
    ICollection,
    IEnumerable,
    IDisposable,
):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, collection: IProducerConsumerCollection[T]):
        """

        :param collection:
        """
    @overload
    def __init__(self, boundedCapacity: int):
        """

        :param boundedCapacity:
        """
    @overload
    def __init__(self, collection: IProducerConsumerCollection[T], boundedCapacity: int):
        """

        :param collection:
        :param boundedCapacity:
        """
    @property
    def BoundedCapacity(self) -> int:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsAddingCompleted(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, item: T) -> None:
        """

        :param item:
        """
    @overload
    def Add(self, item: T, cancellationToken: CancellationToken) -> None:
        """

        :param item:
        :param cancellationToken:
        """
    @classmethod
    @overload
    def AddToAny(cls, collections: Array[BlockingCollection[T]], item: T) -> int:
        """

        :param collections:
        :param item:
        :return:
        """
    @classmethod
    @overload
    def AddToAny(
        cls,
        collections: Array[BlockingCollection[T]],
        item: T,
        cancellationToken: CancellationToken,
    ) -> int:
        """

        :param collections:
        :param item:
        :param cancellationToken:
        :return:
        """
    def CompleteAdding(self) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[T], index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetConsumingEnumerable(self) -> IEnumerable[T]:
        """

        :return:
        """
    @overload
    def GetConsumingEnumerable(self, cancellationToken: CancellationToken) -> IEnumerable[T]:
        """

        :param cancellationToken:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
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
    @overload
    def Take(self) -> T:
        """

        :return:
        """
    @overload
    def Take(self, cancellationToken: CancellationToken) -> T:
        """

        :param cancellationToken:
        :return:
        """
    @classmethod
    @overload
    def TakeFromAny(cls, collections: Array[BlockingCollection[T]], item: T) -> Tuple[int, T]:
        """

        :param collections:
        :param item:
        :return:
        """
    @classmethod
    @overload
    def TakeFromAny(
        cls,
        collections: Array[BlockingCollection[T]],
        item: T,
        cancellationToken: CancellationToken,
    ) -> Tuple[int, T]:
        """

        :param collections:
        :param item:
        :param cancellationToken:
        :return:
        """
    def ToArray(self) -> Array[T]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def TryAdd(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def TryAdd(self, item: T, millisecondsTimeout: int) -> bool:
        """

        :param item:
        :param millisecondsTimeout:
        :return:
        """
    @overload
    def TryAdd(self, item: T, timeout: TimeSpan) -> bool:
        """

        :param item:
        :param timeout:
        :return:
        """
    @overload
    def TryAdd(
        self, item: T, millisecondsTimeout: int, cancellationToken: CancellationToken
    ) -> bool:
        """

        :param item:
        :param millisecondsTimeout:
        :param cancellationToken:
        :return:
        """
    @classmethod
    @overload
    def TryAddToAny(cls, collections: Array[BlockingCollection[T]], item: T) -> int:
        """

        :param collections:
        :param item:
        :return:
        """
    @classmethod
    @overload
    def TryAddToAny(
        cls, collections: Array[BlockingCollection[T]], item: T, millisecondsTimeout: int
    ) -> int:
        """

        :param collections:
        :param item:
        :param millisecondsTimeout:
        :return:
        """
    @classmethod
    @overload
    def TryAddToAny(
        cls, collections: Array[BlockingCollection[T]], item: T, timeout: TimeSpan
    ) -> int:
        """

        :param collections:
        :param item:
        :param timeout:
        :return:
        """
    @classmethod
    @overload
    def TryAddToAny(
        cls,
        collections: Array[BlockingCollection[T]],
        item: T,
        millisecondsTimeout: int,
        cancellationToken: CancellationToken,
    ) -> int:
        """

        :param collections:
        :param item:
        :param millisecondsTimeout:
        :param cancellationToken:
        :return:
        """
    @overload
    def TryTake(self, item: T) -> Tuple[bool, T]:
        """

        :param item:
        :return:
        """
    @overload
    def TryTake(self, item: T, millisecondsTimeout: int) -> Tuple[bool, T]:
        """

        :param item:
        :param millisecondsTimeout:
        :return:
        """
    @overload
    def TryTake(self, item: T, timeout: TimeSpan) -> Tuple[bool, T]:
        """

        :param item:
        :param timeout:
        :return:
        """
    @overload
    def TryTake(
        self, item: T, millisecondsTimeout: int, cancellationToken: CancellationToken
    ) -> Tuple[bool, T]:
        """

        :param item:
        :param millisecondsTimeout:
        :param cancellationToken:
        :return:
        """
    @classmethod
    @overload
    def TryTakeFromAny(cls, collections: Array[BlockingCollection[T]], item: T) -> Tuple[int, T]:
        """

        :param collections:
        :param item:
        :return:
        """
    @classmethod
    @overload
    def TryTakeFromAny(
        cls, collections: Array[BlockingCollection[T]], item: T, millisecondsTimeout: int
    ) -> Tuple[int, T]:
        """

        :param collections:
        :param item:
        :param millisecondsTimeout:
        :return:
        """
    @classmethod
    @overload
    def TryTakeFromAny(
        cls, collections: Array[BlockingCollection[T]], item: T, timeout: TimeSpan
    ) -> Tuple[int, T]:
        """

        :param collections:
        :param item:
        :param timeout:
        :return:
        """
    @classmethod
    @overload
    def TryTakeFromAny(
        cls,
        collections: Array[BlockingCollection[T]],
        item: T,
        millisecondsTimeout: int,
        cancellationToken: CancellationToken,
    ) -> Tuple[int, T]:
        """

        :param collections:
        :param item:
        :param millisecondsTimeout:
        :param cancellationToken:
        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[T]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class CDSCollectionETWBCLProvider(EventSource, IDisposable):
    """"""

    Log: Final[ClassVar[CDSCollectionETWBCLProvider]] = ...
    """
    
    :return: 
    """
    @property
    def ConstructionException(self) -> Exception:
        """

        :return:
        """
    @classmethod
    @property
    def CurrentThreadActivityId(cls) -> Guid:
        """

        :return:
        """
    @property
    def Guid(self) -> Guid:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Settings(self) -> EventSourceSettings:
        """

        :return:
        """
    def ConcurrentBag_TryPeekSteals(self) -> None:
        """"""
    def ConcurrentBag_TryTakeSteals(self) -> None:
        """"""
    def ConcurrentDictionary_AcquiringAllLocks(self, numOfBuckets: int) -> None:
        """

        :param numOfBuckets:
        """
    def ConcurrentStack_FastPopFailed(self, spinCount: int) -> None:
        """

        :param spinCount:
        """
    def ConcurrentStack_FastPushFailed(self, spinCount: int) -> None:
        """

        :param spinCount:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetTrait(self, key: str) -> str:
        """

        :param key:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsEnabled(self) -> bool:
        """

        :return:
        """
    @overload
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords) -> bool:
        """

        :param level:
        :param keywords:
        :return:
        """
    @overload
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords, channel: EventChannel) -> bool:
        """

        :param level:
        :param keywords:
        :param channel:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Write(self, eventName: str) -> None:
        """

        :param eventName:
        """
    @overload
    def Write(self, eventName: str, data: T) -> None:
        """

        :param eventName:
        :param data:
        """
    @overload
    def Write(self, eventName: str, options: EventSourceOptions) -> None:
        """

        :param eventName:
        :param options:
        """
    @overload
    def Write(self, eventName: str, options: EventSourceOptions, data: T) -> None:
        """

        :param eventName:
        :param options:
        :param data:
        """
    @overload
    def Write(self, eventName: str, options: EventSourceOptions, data: T) -> None:
        """

        :param eventName:
        :param options:
        :param data:
        """
    @overload
    def Write(
        self,
        eventName: str,
        options: EventSourceOptions,
        activityId: Guid,
        relatedActivityId: Guid,
        data: T,
    ) -> None:
        """

        :param eventName:
        :param options:
        :param activityId:
        :param relatedActivityId:
        :param data:
        """
    EventCommandExecuted: EventType[EventHandler[EventCommandEventArgs]] = ...
    """"""

class ConcurrentBag(
    Generic[T],
    Object,
    IProducerConsumerCollection[T],
    IEnumerable[T],
    IReadOnlyCollection[T],
    ICollection,
    IEnumerable,
):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, collection: IEnumerable[T]):
        """

        :param collection:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsEmpty(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    def Add(self, item: T) -> None:
        """

        :param item:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[T], index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
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
    def ToArray(self) -> Array[T]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TryAdd(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    def TryPeek(self, result: T) -> Tuple[bool, T]:
        """

        :param result:
        :return:
        """
    def TryTake(self, item: T) -> Tuple[bool, T]:
        """

        :param item:
        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[T]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class ConcurrentDictionary(
    Generic[TKey, TValue],
    Object,
    ICollection[KeyValuePair, TValue],
    IDictionary[TKey, TValue],
    IEnumerable[KeyValuePair, TValue],
    IReadOnlyCollection[KeyValuePair, TValue],
    IReadOnlyDictionary[TKey, TValue],
    ICollection,
    IDictionary,
    IEnumerable,
):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, collection: IEnumerable[KeyValuePair, TValue]):
        """"""
    @overload
    def __init__(self, comparer: IEqualityComparer[TKey]):
        """

        :param comparer:
        """
    @overload
    def __init__(
        self, collection: IEnumerable[KeyValuePair, TValue], comparer: IEqualityComparer[TKey]
    ):
        """"""
    @overload
    def __init__(self, concurrencyLevel: int, capacity: int):
        """

        :param concurrencyLevel:
        :param capacity:
        """
    @overload
    def __init__(
        self,
        concurrencyLevel: int,
        collection: IEnumerable[KeyValuePair, TValue],
        comparer: IEqualityComparer[TKey],
    ):
        """"""
    @overload
    def __init__(self, concurrencyLevel: int, capacity: int, comparer: IEqualityComparer[TKey]):
        """

        :param concurrencyLevel:
        :param capacity:
        :param comparer:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsEmpty(self) -> bool:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Item(self) -> TValue:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: TValue) -> None: ...
    @property
    def Item(self) -> TValue:
        """

        :return:
        """
    @property
    def Keys(self) -> ICollection:
        """

        :return:
        """
    @property
    def Keys(self) -> ICollection[TKey]:
        """

        :return:
        """
    @property
    def Keys(self) -> IEnumerable[TKey]:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection[TValue]:
        """

        :return:
        """
    @property
    def Values(self) -> IEnumerable[TValue]:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection:
        """

        :return:
        """
    @overload
    def Add(self, item: KeyValuePair[TKey, TValue]) -> None:
        """

        :param item:
        """
    @overload
    def Add(self, key: TKey, value: TValue) -> None:
        """

        :param key:
        :param value:
        """
    @overload
    def Add(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """
    @overload
    def AddOrUpdate(
        self, key: TKey, addValue: TValue, updateValueFactory: Func[TKey, TValue, TValue]
    ) -> TValue:
        """

        :param key:
        :param addValue:
        :param updateValueFactory:
        :return:
        """
    @overload
    def AddOrUpdate(
        self,
        key: TKey,
        addValueFactory: Func[TKey, TValue],
        updateValueFactory: Func[TKey, TValue, TValue],
    ) -> TValue:
        """

        :param key:
        :param addValueFactory:
        :param updateValueFactory:
        :return:
        """
    @overload
    def AddOrUpdate(
        self,
        key: TKey,
        addValueFactory: Func[TKey, TArg, TValue],
        updateValueFactory: Func[TKey, TValue, TArg, TValue],
        factoryArgument: TArg,
    ) -> TValue:
        """

        :param key:
        :param addValueFactory:
        :param updateValueFactory:
        :param factoryArgument:
        :return:
        """
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: KeyValuePair[TKey, TValue]) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def Contains(self, key: object) -> bool:
        """

        :param key:
        :return:
        """
    @overload
    def ContainsKey(self, key: TKey) -> bool:
        """

        :param key:
        :return:
        """
    @overload
    def ContainsKey(self, key: TKey) -> bool:
        """

        :param key:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[KeyValuePair, TValue], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetOrAdd(self, key: TKey, value: TValue) -> TValue:
        """

        :param key:
        :param value:
        :return:
        """
    @overload
    def GetOrAdd(self, key: TKey, valueFactory: Func[TKey, TValue]) -> TValue:
        """

        :param key:
        :param valueFactory:
        :return:
        """
    @overload
    def GetOrAdd(
        self, key: TKey, valueFactory: Func[TKey, TArg, TValue], factoryArgument: TArg
    ) -> TValue:
        """

        :param key:
        :param valueFactory:
        :param factoryArgument:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def Remove(self, item: KeyValuePair[TKey, TValue]) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def Remove(self, key: object) -> None:
        """

        :param key:
        """
    def ToArray(self) -> Array[KeyValuePair, TValue]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TryAdd(self, key: TKey, value: TValue) -> bool:
        """

        :param key:
        :param value:
        :return:
        """
    @overload
    def TryGetValue(self, key: TKey, value: TValue) -> Tuple[bool, TValue]:
        """"""
    @overload
    def TryGetValue(self, key: TKey, value: TValue) -> Tuple[bool, TValue]:
        """"""
    def TryRemove(self, key: TKey, value: TValue) -> Tuple[bool, TValue]:
        """

        :param key:
        :param value:
        :return:
        """
    def TryUpdate(self, key: TKey, newValue: TValue, comparisonValue: TValue) -> bool:
        """

        :param key:
        :param newValue:
        :param comparisonValue:
        :return:
        """
    @overload
    def __contains__(self, value: KeyValuePair[TKey, TValue]) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __getitem__(self, key: TKey) -> TValue:
        """

        :param key:
        :return:
        """
    @overload
    def __getitem__(self, key: TKey) -> TValue:
        """

        :param key:
        :return:
        """
    @overload
    def __getitem__(self, key: object) -> object:
        """

        :param key:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[KeyValuePair, TValue]:
        """

        :return:
        """
    @overload
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, key: TKey, value: TValue) -> None:
        """

        :param key:
        :param value:
        """
    @overload
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class ConcurrentQueue(
    Generic[T],
    Object,
    IProducerConsumerCollection[T],
    IEnumerable[T],
    IReadOnlyCollection[T],
    ICollection,
    IEnumerable,
):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, collection: IEnumerable[T]):
        """

        :param collection:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsEmpty(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[T], index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Enqueue(self, item: T) -> None:
        """

        :param item:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
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
    def ToArray(self) -> Array[T]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TryAdd(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    def TryDequeue(self, result: T) -> Tuple[bool, T]:
        """

        :param result:
        :return:
        """
    def TryPeek(self, result: T) -> Tuple[bool, T]:
        """

        :param result:
        :return:
        """
    def TryTake(self, item: T) -> Tuple[bool, T]:
        """

        :param item:
        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[T]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class ConcurrentStack(
    Generic[T],
    Object,
    IProducerConsumerCollection[T],
    IEnumerable[T],
    IReadOnlyCollection[T],
    ICollection,
    IEnumerable,
):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, collection: IEnumerable[T]):
        """

        :param collection:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsEmpty(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[T], index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
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
    def Push(self, item: T) -> None:
        """

        :param item:
        """
    @overload
    def PushRange(self, items: Array[T]) -> None:
        """

        :param items:
        """
    @overload
    def PushRange(self, items: Array[T], startIndex: int, count: int) -> None:
        """

        :param items:
        :param startIndex:
        :param count:
        """
    def ToArray(self) -> Array[T]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TryAdd(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    def TryPeek(self, result: T) -> Tuple[bool, T]:
        """

        :param result:
        :return:
        """
    def TryPop(self, result: T) -> Tuple[bool, T]:
        """

        :param result:
        :return:
        """
    @overload
    def TryPopRange(self, items: Array[T]) -> int:
        """

        :param items:
        :return:
        """
    @overload
    def TryPopRange(self, items: Array[T], startIndex: int, count: int) -> int:
        """

        :param items:
        :param startIndex:
        :param count:
        :return:
        """
    def TryTake(self, item: T) -> Tuple[bool, T]:
        """

        :param item:
        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[T]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class EnumerablePartitionerOptions(Enum):
    """"""

    _None: EnumerablePartitionerOptions = ...
    """"""
    NoBuffering: EnumerablePartitionerOptions = ...
    """"""

class IProducerConsumerCollection(Generic[T], IEnumerable[T], ICollection, IEnumerable):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[T], index: int) -> None:
        """

        :param array:
        :param index:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def ToArray(self) -> Array[T]:
        """

        :return:
        """
    def TryAdd(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    def TryTake(self, item: T) -> Tuple[bool, T]:
        """

        :param item:
        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[T]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class OrderablePartitioner(ABC, Generic[TSource], Partitioner[TSource]):
    """"""

    @property
    def KeysNormalized(self) -> bool:
        """

        :return:
        """
    @property
    def KeysOrderedAcrossPartitions(self) -> bool:
        """

        :return:
        """
    @property
    def KeysOrderedInEachPartition(self) -> bool:
        """

        :return:
        """
    @property
    def SupportsDynamicPartitions(self) -> bool:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetDynamicPartitions(self) -> IEnumerable[TSource]:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetOrderableDynamicPartitions(self) -> IEnumerable[KeyValuePair, TSource]:
        """

        :return:
        """
    def GetOrderablePartitions(self, partitionCount: int) -> IList[IEnumerator, TSource]:
        """

        :param partitionCount:
        :return:
        """
    def GetPartitions(self, partitionCount: int) -> IList[IEnumerator[TSource]]:
        """

        :param partitionCount:
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

class Partitioner(ABC, Object):
    """"""

    @classmethod
    @overload
    def Create(cls, source: IEnumerable[TSource]) -> OrderablePartitioner[TSource]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Create(
        cls, source: IEnumerable[TSource], partitionerOptions: EnumerablePartitionerOptions
    ) -> OrderablePartitioner[TSource]:
        """

        :param source:
        :param partitionerOptions:
        :return:
        """
    @classmethod
    @overload
    def Create(cls, list: IList[TSource], loadBalance: bool) -> OrderablePartitioner[TSource]:
        """

        :param list:
        :param loadBalance:
        :return:
        """
    @classmethod
    @overload
    def Create(cls, array: Array[TSource], loadBalance: bool) -> OrderablePartitioner[TSource]:
        """

        :param array:
        :param loadBalance:
        :return:
        """
    @classmethod
    @overload
    def Create(cls, fromInclusive: int, toExclusive: int) -> OrderablePartitioner[Tuple, int]:
        """

        :param fromInclusive:
        :param toExclusive:
        :return:
        """
    @classmethod
    @overload
    def Create(cls, fromInclusive: int, toExclusive: int) -> OrderablePartitioner[Tuple, int]:
        """

        :param fromInclusive:
        :param toExclusive:
        :return:
        """
    @classmethod
    @overload
    def Create(
        cls, fromInclusive: int, toExclusive: int, rangeSize: int
    ) -> OrderablePartitioner[Tuple, int]:
        """

        :param fromInclusive:
        :param toExclusive:
        :param rangeSize:
        :return:
        """
    @classmethod
    @overload
    def Create(
        cls, fromInclusive: int, toExclusive: int, rangeSize: int
    ) -> OrderablePartitioner[Tuple, int]:
        """

        :param fromInclusive:
        :param toExclusive:
        :param rangeSize:
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

class Partitioner(ABC, Generic[TSource], Object):
    """"""

    @property
    def SupportsDynamicPartitions(self) -> bool:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetDynamicPartitions(self) -> IEnumerable[TSource]:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetPartitions(self, partitionCount: int) -> IList[IEnumerator[TSource]]:
        """

        :param partitionCount:
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

class SystemCollectionsConcurrent_ProducerConsumerCollectionDebugView(Generic[T], Object):
    """"""

    def __init__(self, collection: IProducerConsumerCollection[T]):
        """

        :param collection:
        """
    @property
    def Items(self) -> Array[T]:
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

class SystemThreadingCollection_IProducerConsumerCollectionDebugView(Generic[T], Object):
    """"""

    def __init__(self, collection: IProducerConsumerCollection[T]):
        """

        :param collection:
        """
    @property
    def Items(self) -> Array[T]:
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

class SystemThreadingCollections_BlockingCollectionDebugView(Generic[T], Object):
    """"""

    def __init__(self, collection: BlockingCollection[T]):
        """

        :param collection:
        """
    @property
    def Items(self) -> Array[T]:
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

class VolatileBool(ValueType):
    """"""

    m_value: Final[bool] = ...
    """
    
    :return: 
    """
    def __init__(self, value: bool):
        """

        :param value:
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
