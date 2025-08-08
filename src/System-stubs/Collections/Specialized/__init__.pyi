"""Automatically generated stubs for C# namespace: System.Collections.Specialized."""

from abc import ABC
from collections.abc import Callable
from collections.abc import Iterator
from typing import Self
from typing import overload

from System import Array
from System import Enum
from System import EventArgs
from System import Object
from System import Type
from System import ValueType
from System.Collections import Hashtable
from System.Collections import ICollection
from System.Collections import IComparer
from System.Collections import IDictionary
from System.Collections import IDictionaryEnumerator
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IEqualityComparer
from System.Collections import IHashCodeProvider
from System.Collections import IList
from System.Collections import SortedList
from System.Runtime.Serialization import IDeserializationCallback
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

class BackCompatibleStringComparer(Object, IEqualityComparer):
    """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, o: object) -> int:
        """"""
    @classmethod
    @overload
    def GetHashCode(cls, obj: str) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class BitVector32(ValueType):
    """"""
    @overload
    def __init__(self, data: int) -> None:
        """"""
    @overload
    def __init__(self, value: BitVector32) -> None:
        """"""
    @property
    def Data(self) -> int:
        """"""
    @property
    def Item(self) -> int:
        """"""
    @Item.setter
    def Item(self, value: int) -> None: ...
    @classmethod
    @overload
    def CreateMask(cls) -> int:
        """"""
    @classmethod
    @overload
    def CreateMask(cls, previous: int) -> int:
        """"""
    @classmethod
    @overload
    def CreateSection(cls, maxValue: int) -> BitVector32.Section:
        """"""
    @classmethod
    @overload
    def CreateSection(cls, maxValue: int, previous: BitVector32.Section) -> BitVector32.Section:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: BitVector32) -> str:
        """"""
    @overload
    def __getitem__(self, section: BitVector32.Section) -> int:
        """"""
    @overload
    def __getitem__(self, bit: int) -> bool:
        """"""
    @overload
    def __setitem__(self, section: BitVector32.Section, value: int) -> None:
        """"""
    @overload
    def __setitem__(self, bit: int, value: bool) -> None:
        """"""
    class Section(ValueType):
        """"""
        @property
        def Mask(self) -> int:
            """"""
        @property
        def Offset(self) -> int:
            """"""
        @overload
        def Equals(self, obj: BitVector32.Section) -> bool:
            """"""
        @overload
        def Equals(self, o: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        @overload
        def ToString(self) -> str:
            """"""
        @classmethod
        @overload
        def ToString(cls, value: BitVector32.Section) -> str:
            """"""
        @classmethod
        def op_Equality(cls, a: BitVector32.Section, b: BitVector32.Section) -> bool:
            """"""
        @classmethod
        def op_Inequality(cls, a: BitVector32.Section, b: BitVector32.Section) -> bool:
            """"""
        def __eq__(self, other: BitVector32.Section) -> bool:
            """"""
        def __ne__(self, other: BitVector32.Section) -> bool:
            """"""

class CollectionsUtil(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @classmethod
    @overload
    def CreateCaseInsensitiveHashtable(cls) -> Hashtable:
        """"""
    @classmethod
    @overload
    def CreateCaseInsensitiveHashtable(cls, d: IDictionary) -> Hashtable:
        """"""
    @classmethod
    @overload
    def CreateCaseInsensitiveHashtable(cls, capacity: int) -> Hashtable:
        """"""
    @classmethod
    def CreateCaseInsensitiveSortedList(cls) -> SortedList:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CompatibleComparer(Object, IEqualityComparer):
    """"""
    @property
    def Comparer(self) -> IComparer:
        """"""
    @classmethod
    @property
    def DefaultComparer(cls) -> IComparer:
        """"""
    @classmethod
    @property
    def DefaultHashCodeProvider(cls) -> IHashCodeProvider:
        """"""
    @property
    def HashCodeProvider(self) -> IHashCodeProvider:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, a: object, b: object) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: object) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class FixedStringLookup(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HybridDictionary(Object, ICollection, IDictionary, IEnumerable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, initialSize: int) -> None:
        """"""
    @overload
    def __init__(self, caseInsensitive: bool) -> None:
        """"""
    @overload
    def __init__(self, initialSize: int, caseInsensitive: bool) -> None:
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
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> ICollection:
        """"""
    def Add(self, key: object, value: object) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, key: object) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, key: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, key: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, key: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, key: object) -> object:
        """"""
    def __setitem__(self, key: object, value: object) -> None:
        """"""

class INotifyCollectionChanged(ABC):
    """"""

    CollectionChanged: EventType[NotifyCollectionChangedEventHandler] = ...
    """"""

class IOrderedDictionary(ABC, ICollection, IDictionary, IEnumerable):
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
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> ICollection:
        """"""
    def Add(self, key: object, value: object) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, key: object) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """"""
    def Insert(self, index: int, key: object, value: object) -> None:
        """"""
    def Remove(self, key: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def __contains__(self, key: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, key: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, index: int) -> object:
        """"""
    @overload
    def __getitem__(self, key: object) -> object:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""
    @overload
    def __setitem__(self, key: object, value: object) -> None:
        """"""

class ListDictionary(Object, ICollection, IDictionary, IEnumerable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, comparer: IComparer) -> None:
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
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> ICollection:
        """"""
    def Add(self, key: object, value: object) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, key: object) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, key: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, key: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, key: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, key: object) -> object:
        """"""
    def __setitem__(self, key: object, value: object) -> None:
        """"""

class NameObjectCollectionBase(
    ABC, Object, ICollection, IEnumerable, IDeserializationCallback, ISerializable
):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Keys(self) -> NameObjectCollectionBase.KeysCollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""
    class KeysCollection(Object, ICollection, IEnumerable):
        """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> str:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def Get(self, index: int) -> str:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> str:
            """"""

class NameValueCollection(
    NameObjectCollectionBase, ICollection, IEnumerable, IDeserializationCallback, ISerializable
):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, col: NameValueCollection) -> None:
        """"""
    @overload
    def __init__(self, hashProvider: IHashCodeProvider, comparer: IComparer) -> None:
        """"""
    @overload
    def __init__(self, capacity: int) -> None:
        """"""
    @overload
    def __init__(self, equalityComparer: IEqualityComparer) -> None:
        """"""
    @overload
    def __init__(self, capacity: int, equalityComparer: IEqualityComparer) -> None:
        """"""
    @overload
    def __init__(self, capacity: int, col: NameValueCollection) -> None:
        """"""
    @overload
    def __init__(self, capacity: int, hashProvider: IHashCodeProvider, comparer: IComparer) -> None:
        """"""
    @property
    def AllKeys(self) -> Array[str]:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> str:
        """"""
    @property
    def Keys(self) -> NameObjectCollectionBase.KeysCollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, c: NameValueCollection) -> None:
        """"""
    @overload
    def Add(self, name: str, value: str) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def CopyTo(self, dest: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Get(self, index: int) -> str:
        """"""
    @overload
    def Get(self, name: str) -> str:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetKey(self, index: int) -> str:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def GetValues(self, index: int) -> Array[str]:
        """"""
    @overload
    def GetValues(self, name: str) -> Array[str]:
        """"""
    def HasKeys(self) -> bool:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    def Remove(self, name: str) -> None:
        """"""
    def Set(self, name: str, value: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, name: str) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, index: int) -> str:
        """"""
    @overload
    def __getitem__(self, name: str) -> str:
        """"""
    def __setitem__(self, name: str, value: str) -> None:
        """"""
    class KeysCollection(Object, ICollection, IEnumerable):
        """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> str:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def Get(self, index: int) -> str:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> str:
            """"""

class NotifyCollectionChangedAction(Enum):
    """"""

    Add: NotifyCollectionChangedAction = ...
    """"""
    Remove: NotifyCollectionChangedAction = ...
    """"""
    Replace: NotifyCollectionChangedAction = ...
    """"""
    Move: NotifyCollectionChangedAction = ...
    """"""
    Reset: NotifyCollectionChangedAction = ...
    """"""

class NotifyCollectionChangedEventArgs(EventArgs):
    """"""
    @overload
    def __init__(self, action: NotifyCollectionChangedAction) -> None:
        """"""
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, changedItem: object) -> None:
        """"""
    @overload
    def __init__(
        self, action: NotifyCollectionChangedAction, changedItem: object, index: int
    ) -> None:
        """"""
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, changedItems: IList) -> None:
        """"""
    @overload
    def __init__(
        self, action: NotifyCollectionChangedAction, changedItems: IList, startingIndex: int
    ) -> None:
        """"""
    @overload
    def __init__(
        self, action: NotifyCollectionChangedAction, newItem: object, oldItem: object
    ) -> None:
        """"""
    @overload
    def __init__(
        self, action: NotifyCollectionChangedAction, newItem: object, oldItem: object, index: int
    ) -> None:
        """"""
    @overload
    def __init__(
        self, action: NotifyCollectionChangedAction, newItems: IList, oldItems: IList
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        action: NotifyCollectionChangedAction,
        newItems: IList,
        oldItems: IList,
        startingIndex: int,
    ) -> None:
        """"""
    @overload
    def __init__(
        self, action: NotifyCollectionChangedAction, changedItem: object, index: int, oldIndex: int
    ) -> None:
        """"""
    @overload
    def __init__(
        self, action: NotifyCollectionChangedAction, changedItems: IList, index: int, oldIndex: int
    ) -> None:
        """"""
    @property
    def Action(self) -> NotifyCollectionChangedAction:
        """"""
    @property
    def NewItems(self) -> IList:
        """"""
    @property
    def NewStartingIndex(self) -> int:
        """"""
    @property
    def OldItems(self) -> IList:
        """"""
    @property
    def OldStartingIndex(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type NotifyCollectionChangedEventHandler = Callable[
    [object, NotifyCollectionChangedEventArgs], None
]
""""""

class OrderedDictionary(
    Object,
    IOrderedDictionary,
    ICollection,
    IDictionary,
    IEnumerable,
    IDeserializationCallback,
    ISerializable,
):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, capacity: int) -> None:
        """"""
    @overload
    def __init__(self, comparer: IEqualityComparer) -> None:
        """"""
    @overload
    def __init__(self, capacity: int, comparer: IEqualityComparer) -> None:
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
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> ICollection:
        """"""
    def Add(self, key: object, value: object) -> None:
        """"""
    def AsReadOnly(self) -> OrderedDictionary:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, key: object) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def Insert(self, index: int, key: object, value: object) -> None:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    def Remove(self, key: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, key: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, key: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, index: int) -> object:
        """"""
    @overload
    def __getitem__(self, key: object) -> object:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""
    @overload
    def __setitem__(self, key: object, value: object) -> None:
        """"""

class StringCollection(Object, ICollection, IEnumerable, IList):
    """"""
    def __init__(self) -> None:
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
    def Item(self) -> str:
        """"""
    @Item.setter
    def Item(self, value: str) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    @overload
    def Add(self, value: str) -> int:
        """"""
    def AddRange(self, value: Array[str]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def Contains(self, value: str) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[str], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> StringEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def IndexOf(self, value: str) -> int:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: str) -> None:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    @overload
    def Remove(self, value: str) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    @overload
    def __contains__(self, value: str) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    @overload
    def __delitem__(self, value: str) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> str:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: str) -> None:
        """"""

class StringDictionary(Object, IEnumerable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> str:
        """"""
    @Item.setter
    def Item(self, value: str) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> ICollection:
        """"""
    def Add(self, key: str, value: str) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def ContainsKey(self, key: str) -> bool:
        """"""
    def ContainsValue(self, value: str) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, key: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, key: str) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, key: str) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, key: str) -> str:
        """"""
    def __setitem__(self, key: str, value: str) -> None:
        """"""

class StringDictionaryWithComparer(StringDictionary, IEnumerable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, comparer: IEqualityComparer) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> str:
        """"""
    @Item.setter
    def Item(self, value: str) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> ICollection:
        """"""
    def Add(self, key: str, value: str) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def ContainsKey(self, key: str) -> bool:
        """"""
    def ContainsValue(self, value: str) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, key: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, key: str) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, key: str) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, key: str) -> str:
        """"""
    def __setitem__(self, key: str, value: str) -> None:
        """"""

class StringEnumerator(Object):
    """"""
    @property
    def Current(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
