"""Automatically generated stubs for C# namespace: System.Collections.ObjectModel."""

from abc import ABC
from collections.abc import Iterator
from typing import Self
from typing import overload

from System import Array
from System import Object
from System import Type
from System.Collections import ICollection
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IList
from System.Collections.Generic import ICollection
from System.Collections.Generic import IDictionary
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEnumerator
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

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Collection[T](
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
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, list: IList[T]) -> None:
        """"""
    @property
    def Count(self) -> int:
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
    def Item(self) -> T:
        """"""
    @Item.setter
    def Item(self, value: T) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, item: T) -> None:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: T) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
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
    @overload
    def IndexOf(self, item: T) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, item: T) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, item: T) -> bool:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, item: T) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__[T](self) -> Iterator[T]:
        """"""
    @overload
    def __delitem__(self, item: T) -> bool:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> T:
        """"""
    @overload
    def __setitem__(self, index: int, value: T) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class KeyedCollection[TKey, TItem](
    ABC,
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
        """"""
    @property
    def Count(self) -> int:
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
    def Item(self) -> TItem:
        """"""
    @Item.setter
    def Item(self, value: TItem) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add[TItem](self, item: TItem) -> None:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains[TItem](self, item: TItem) -> bool:
        """"""
    @overload
    def Contains(self, key: TKey) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo[TItem](self, array: Array[TItem], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[TItem](self) -> IEnumerator[TItem]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf[TItem](self, item: TItem) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert[TItem](self, index: int, item: TItem) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove[TItem](self, item: TItem) -> bool:
        """"""
    @overload
    def Remove(self, key: TKey) -> bool:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__[TItem](self, item: TItem) -> bool:
        """"""
    @overload
    def __contains__(self, key: TKey) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__[TItem](self) -> Iterator[TItem]:
        """"""
    @overload
    def __delitem__[TItem](self, item: TItem) -> bool:
        """"""
    @overload
    def __delitem__(self, key: TKey) -> bool:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, key: TKey) -> TItem:
        """"""
    @overload
    def __getitem__[TItem](self, index: int) -> TItem:
        """"""
    @overload
    def __setitem__[TItem](self, index: int, value: TItem) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ObservableCollection[T](
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
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, list: List[T]) -> None:
        """"""
    @overload
    def __init__(self, collection: IEnumerable[T]) -> None:
        """"""
    @property
    def Count(self) -> int:
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
    def Item(self) -> T:
        """"""
    @Item.setter
    def Item(self, value: T) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, item: T) -> None:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: T) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
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
    @overload
    def IndexOf(self, item: T) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, item: T) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    def Move(self, oldIndex: int, newIndex: int) -> None:
        """"""
    @overload
    def Remove(self, item: T) -> bool:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, item: T) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__[T](self) -> Iterator[T]:
        """"""
    @overload
    def __delitem__(self, item: T) -> bool:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> T:
        """"""
    @overload
    def __setitem__(self, index: int, value: T) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""
    CollectionChanged: EventType[NotifyCollectionChangedEventHandler] = ...
    """"""
    PropertyChanged: EventType[PropertyChangedEventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ReadOnlyCollection[T](
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
    def __init__(self, list: IList[T]) -> None:
        """"""
    @property
    def Count(self) -> int:
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
    def Item(self) -> T:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, item: T) -> None:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: T) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
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
    @overload
    def IndexOf(self, value: T) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, item: T) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, item: T) -> bool:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: T) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__[T](self) -> Iterator[T]:
        """"""
    @overload
    def __delitem__(self, item: T) -> bool:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> T:
        """"""
    @overload
    def __setitem__(self, index: int, value: T) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ReadOnlyDictionaryHelpers(ABC, Object):
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
class ReadOnlyDictionary[TKey, TValue](
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
    def __init__(self, dictionary: IDictionary[TKey, TValue]) -> None:
        """"""
    @property
    def Count(self) -> int:
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
    @property
    def Keys(self) -> ReadOnlyDictionary.KeyCollection[TKey, TValue]:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> ReadOnlyDictionary.ValueCollection[TKey, TValue]:
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
    def ToString(self) -> str:
        """"""
    def TryGetValue(self, key: TKey, value: TValue) -> tuple[bool, TValue]:
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
    class KeyCollection[TKey, TValue](
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
            """"""
        @property
        def IsReadOnly(self) -> bool:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def Add[TKey](self, item: TKey) -> None:
            """"""
        def Clear(self) -> None:
            """"""
        def Contains[TKey](self, item: TKey) -> bool:
            """"""
        @overload
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        @overload
        def CopyTo[TKey](self, array: Array[TKey], arrayIndex: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator[TKey](self) -> IEnumerator[TKey]:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def Remove[TKey](self, item: TKey) -> bool:
            """"""
        def ToString(self) -> str:
            """"""
        def __contains__[TKey](self, item: TKey) -> bool:
            """"""
        def __iter__[TKey](self) -> Iterator[TKey]:
            """"""
        def __delitem__[TKey](self, item: TKey) -> bool:
            """"""
        def __len__(self) -> int:
            """"""

    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class ValueCollection[TKey, TValue](
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
            """"""
        @property
        def IsReadOnly(self) -> bool:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def Add[TValue](self, item: TValue) -> None:
            """"""
        def Clear(self) -> None:
            """"""
        def Contains[TValue](self, item: TValue) -> bool:
            """"""
        @overload
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        @overload
        def CopyTo[TValue](self, array: Array[TValue], arrayIndex: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator[TValue](self) -> IEnumerator[TValue]:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def Remove[TValue](self, item: TValue) -> bool:
            """"""
        def ToString(self) -> str:
            """"""
        def __contains__[TValue](self, item: TValue) -> bool:
            """"""
        def __iter__[TValue](self) -> Iterator[TValue]:
            """"""
        def __delitem__[TValue](self, item: TValue) -> bool:
            """"""
        def __len__(self) -> int:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ReadOnlyObservableCollection[T](
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
    def __init__(self, list: ObservableCollection[T]) -> None:
        """"""
    @property
    def Count(self) -> int:
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
    def Item(self) -> T:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, item: T) -> None:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: T) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
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
    @overload
    def IndexOf(self, value: T) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, item: T) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, item: T) -> bool:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: T) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__[T](self) -> Iterator[T]:
        """"""
    @overload
    def __delitem__(self, item: T) -> bool:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> T:
        """"""
    @overload
    def __setitem__(self, index: int, value: T) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""
    CollectionChanged: EventType[NotifyCollectionChangedEventHandler] = ...
    """"""
    PropertyChanged: EventType[PropertyChangedEventHandler] = ...
    """"""
