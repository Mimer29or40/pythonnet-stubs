from __future__ import annotations

from abc import ABC
from typing import Generic
from typing import Iterator
from typing import Tuple
from typing import TypeVar
from typing import overload

from System import Array
from System import Object
from System import Type
from System.Collections import ICollection
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IList
from System.Collections.Generic import ICollection
from System.Collections.Generic import IDictionary
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEqualityComparer
from System.Collections.Generic import IList
from System.Collections.Generic import IReadOnlyCollection
from System.Collections.Generic import IReadOnlyDictionary
from System.Collections.Generic import IReadOnlyList
from System.Collections.Generic import KeyValuePair
from System.Collections.Generic import List
from System.Collections.Specialized import INotifyCollectionChanged
from System.Collections.Specialized import NotifyCollectionChangedEventHandler
from System.ComponentModel import INotifyPropertyChanged
from System.ComponentModel import PropertyChangedEventHandler

T = TypeVar("T")
TItem = TypeVar("TItem")
TKey = TypeVar("TKey")
TValue = TypeVar("TValue")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class Collection(
    Generic[T],
    Object,
    ICollection[T],
    IEnumerable[T],
    IList[T],
    IReadOnlyCollection[T],
    IReadOnlyList[T],
    ICollection,
    IEnumerable,
    IList,
):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, list: IList[T]):
        """

        :param list:
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
    def Item(self) -> T:
        """

        :return:
        """
    @property
    def Item(self) -> T:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: T) -> None: ...
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
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IndexOf(self, item: T) -> int:
        """

        :param item:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, item: T) -> None:
        """

        :param index:
        :param item:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    @overload
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    @overload
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def __contains__(self, value: T) -> bool:
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
    def __getitem__(self, index: int) -> T:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> T:
        """

        :param index:
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
    def __setitem__(self, index: int, value: T) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class KeyedCollection(
    ABC,
    Generic[TKey, TItem],
    Collection[TItem],
    ICollection[TItem],
    IEnumerable[TItem],
    IList[TItem],
    IReadOnlyCollection[TItem],
    IReadOnlyList[TItem],
    ICollection,
    IEnumerable,
    IList,
):
    """"""

    @property
    def Comparer(self) -> IEqualityComparer[TKey]:
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
    def Count(self) -> int:
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
    def Item(self) -> TItem:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: TItem) -> None: ...
    @property
    def Item(self) -> TItem:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, item: TItem) -> None:
        """

        :param item:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: TItem) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[TItem], arrayIndex: int) -> None:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IndexOf(self, item: TItem) -> int:
        """

        :param item:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, item: TItem) -> None:
        """

        :param index:
        :param item:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, item: TItem) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    @overload
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    @overload
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def __contains__(self, value: TItem) -> bool:
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
    def __getitem__(self, key: TKey) -> TItem:
        """

        :param key:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> TItem:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> TItem:
        """

        :param index:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TItem]:
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
    def __setitem__(self, index: int, value: TItem) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class ObservableCollection(
    Generic[T],
    Collection[T],
    ICollection[T],
    IEnumerable[T],
    IList[T],
    IReadOnlyCollection[T],
    IReadOnlyList[T],
    INotifyCollectionChanged,
    ICollection,
    IEnumerable,
    IList,
    INotifyPropertyChanged,
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
    @overload
    def __init__(self, list: List[T]):
        """

        :param list:
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
    def Item(self) -> T:
        """

        :return:
        """
    @property
    def Item(self) -> T:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: T) -> None: ...
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
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
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IndexOf(self, item: T) -> int:
        """

        :param item:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, item: T) -> None:
        """

        :param index:
        :param item:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    def Move(self, oldIndex: int, newIndex: int) -> None:
        """

        :param oldIndex:
        :param newIndex:
        """
    @overload
    def Remove(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    @overload
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    @overload
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def __contains__(self, value: T) -> bool:
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
    def __getitem__(self, index: int) -> T:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> T:
        """

        :param index:
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
    def __setitem__(self, index: int, value: T) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    CollectionChanged: EventType[NotifyCollectionChangedEventHandler] = ...
    """"""
    PropertyChanged: EventType[PropertyChangedEventHandler] = ...
    """"""

class ReadOnlyCollection(
    Generic[T],
    Object,
    ICollection[T],
    IEnumerable[T],
    IList[T],
    IReadOnlyCollection[T],
    IReadOnlyList[T],
    ICollection,
    IEnumerable,
    IList,
):
    """"""

    def __init__(self, list: IList[T]):
        """

        :param list:
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
    def Item(self) -> T:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: T) -> None: ...
    @property
    def Item(self) -> T:
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
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IndexOf(self, item: T) -> int:
        """

        :param item:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, item: T) -> None:
        """

        :param index:
        :param item:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    @overload
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    @overload
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def __contains__(self, value: T) -> bool:
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
    def __getitem__(self, index: int) -> T:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> T:
        """

        :param index:
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
    def __setitem__(self, index: int, value: T) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class ReadOnlyDictionaryHelpers(ABC, Object):
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ReadOnlyDictionary(
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

    def __init__(self, dictionary: IDictionary[TKey, TValue]):
        """

        :param dictionary:
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
    @property
    def Item(self) -> TValue:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: TValue) -> None: ...
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
    def Keys(self) -> ICollection:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection:
        """

        :return:
        """
    @property
    def Values(self) -> IEnumerable[TValue]:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection[TValue]:
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
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def TryGetValue(self, key: TKey, value: TValue) -> Tuple[bool, TValue]:
        """"""
    @overload
    def TryGetValue(self, key: TKey, value: TValue) -> Tuple[bool, TValue]:
        """"""
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

    class KeyCollection(
        Generic[TKey, TValue],
        Object,
        ICollection[TKey],
        IEnumerable[TKey],
        IReadOnlyCollection[TKey],
        ICollection,
        IEnumerable,
    ):
        """"""

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
        def SyncRoot(self) -> object:
            """

            :return:
            """
        def Add(self, item: TKey) -> None:
            """

            :param item:
            """
        def Clear(self) -> None:
            """"""
        def Contains(self, item: TKey) -> bool:
            """

            :param item:
            :return:
            """
        @overload
        def CopyTo(self, array: Array, index: int) -> None:
            """

            :param array:
            :param index:
            """
        @overload
        def CopyTo(self, array: Array[TKey], arrayIndex: int) -> None:
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
        def GetType(self) -> Type:
            """

            :return:
            """
        def Remove(self, item: TKey) -> bool:
            """

            :param item:
            :return:
            """
        def ToString(self) -> str:
            """

            :return:
            """
        @overload
        def __contains__(self, value: TKey) -> bool:
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
        def __iter__(self) -> Iterator[object]:
            """

            :return:
            """
        @overload
        def __iter__(self) -> Iterator[TKey]:
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

    class ValueCollection(
        Generic[TKey, TValue],
        Object,
        ICollection[TValue],
        IEnumerable[TValue],
        IReadOnlyCollection[TValue],
        ICollection,
        IEnumerable,
    ):
        """"""

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
        def SyncRoot(self) -> object:
            """

            :return:
            """
        def Add(self, item: TValue) -> None:
            """

            :param item:
            """
        def Clear(self) -> None:
            """"""
        def Contains(self, item: TValue) -> bool:
            """

            :param item:
            :return:
            """
        @overload
        def CopyTo(self, array: Array, index: int) -> None:
            """

            :param array:
            :param index:
            """
        @overload
        def CopyTo(self, array: Array[TValue], arrayIndex: int) -> None:
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
        def GetType(self) -> Type:
            """

            :return:
            """
        def Remove(self, item: TValue) -> bool:
            """

            :param item:
            :return:
            """
        def ToString(self) -> str:
            """

            :return:
            """
        @overload
        def __contains__(self, value: TValue) -> bool:
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
        def __iter__(self) -> Iterator[object]:
            """

            :return:
            """
        @overload
        def __iter__(self) -> Iterator[TValue]:
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

class ReadOnlyObservableCollection(
    Generic[T],
    ReadOnlyCollection[T],
    ICollection[T],
    IEnumerable[T],
    IList[T],
    IReadOnlyCollection[T],
    IReadOnlyList[T],
    INotifyCollectionChanged,
    ICollection,
    IEnumerable,
    IList,
    INotifyPropertyChanged,
):
    """"""

    def __init__(self, list: ObservableCollection[T]):
        """

        :param list:
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
    def Item(self) -> T:
        """

        :return:
        """
    @property
    def Item(self) -> T:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: T) -> None: ...
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
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
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IndexOf(self, item: T) -> int:
        """

        :param item:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, item: T) -> None:
        """

        :param index:
        :param item:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    @overload
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    @overload
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def __contains__(self, value: T) -> bool:
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
    def __getitem__(self, index: int) -> T:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> T:
        """

        :param index:
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
    def __setitem__(self, index: int, value: T) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    CollectionChanged: EventType[NotifyCollectionChangedEventHandler] = ...
    """"""
    PropertyChanged: EventType[PropertyChangedEventHandler] = ...
    """"""
