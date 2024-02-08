from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import Generic
from typing import Iterator
from typing import TypeVar
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
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IEqualityComparer
from System.Collections import IHashCodeProvider
from System.Collections import IList
from System.Collections import SortedList
from System.Collections.Specialized.BitVector32 import Section
from System.Collections.Specialized.NameObjectCollectionBase import KeysCollection
from System.Runtime.Serialization import IDeserializationCallback
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext

T = TypeVar("T")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class BackCompatibleStringComparer(Object, IEqualityComparer):
    """"""

    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """

        :param x:
        :param y:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self, obj: object) -> int:
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def GetHashCode(cls, obj: str) -> int:
        """

        :param obj:
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

class BitVector32(ValueType):
    """"""

    @overload
    def __init__(self, value: BitVector32):
        """

        :param value:
        """
    @overload
    def __init__(self, data: int):
        """

        :param data:
        """
    @property
    def Data(self) -> int:
        """

        :return:
        """
    @property
    def Item(self) -> bool:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: bool) -> None: ...
    @classmethod
    @overload
    def CreateMask(cls) -> int:
        """

        :return:
        """
    @classmethod
    @overload
    def CreateMask(cls, previous: int) -> int:
        """

        :param previous:
        :return:
        """
    @classmethod
    @overload
    def CreateSection(cls, maxValue: int) -> BitVector32.Section:
        """

        :param maxValue:
        :return:
        """
    @classmethod
    @overload
    def CreateSection(cls, maxValue: int, previous: BitVector32.Section) -> BitVector32.Section:
        """

        :param maxValue:
        :param previous:
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
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: BitVector32) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def __getitem__(self, section: BitVector32.Section) -> int:
        """

        :param section:
        :return:
        """
    @overload
    def __getitem__(self, bit: int) -> bool:
        """

        :param bit:
        :return:
        """
    @overload
    def __setitem__(self, section: BitVector32.Section, value: int) -> None:
        """

        :param section:
        :param value:
        """
    @overload
    def __setitem__(self, bit: int, value: bool) -> None:
        """

        :param bit:
        :param value:
        """

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
        @overload
        def ToString(self) -> str:
            """

            :return:
            """
        @classmethod
        @overload
        def ToString(cls, value: BitVector32.Section) -> str:
            """"""
        def __eq__(self, other: BitVector32.Section) -> bool:
            """"""
        def __ne__(self, other: BitVector32.Section) -> bool:
            """"""
        @classmethod
        def op_Equality(cls, a: BitVector32.Section, b: BitVector32.Section) -> bool:
            """"""
        @classmethod
        def op_Inequality(cls, a: BitVector32.Section, b: BitVector32.Section) -> bool:
            """"""

class CollectionsUtil(Object):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @overload
    def CreateCaseInsensitiveHashtable(cls) -> Hashtable:
        """

        :return:
        """
    @classmethod
    @overload
    def CreateCaseInsensitiveHashtable(cls, d: IDictionary) -> Hashtable:
        """

        :param d:
        :return:
        """
    @classmethod
    @overload
    def CreateCaseInsensitiveHashtable(cls, capacity: int) -> Hashtable:
        """

        :param capacity:
        :return:
        """
    @classmethod
    def CreateCaseInsensitiveSortedList(cls) -> SortedList:
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

class CompatibleComparer(Object, IEqualityComparer):
    """"""

    @property
    def Comparer(self) -> IComparer:
        """

        :return:
        """
    @classmethod
    @property
    def DefaultComparer(cls) -> IComparer:
        """

        :return:
        """
    @classmethod
    @property
    def DefaultHashCodeProvider(cls) -> IHashCodeProvider:
        """

        :return:
        """
    @property
    def HashCodeProvider(self) -> IHashCodeProvider:
        """

        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """

        :param x:
        :param y:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self, obj: object) -> int:
        """

        :param obj:
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

class FixedStringLookup(ABC, Object):
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

class HybridDictionary(Object, ICollection, IDictionary, IEnumerable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, caseInsensitive: bool):
        """

        :param caseInsensitive:
        """
    @overload
    def __init__(self, initialSize: int):
        """

        :param initialSize:
        """
    @overload
    def __init__(self, initialSize: int, caseInsensitive: bool):
        """

        :param initialSize:
        :param caseInsensitive:
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
    def Add(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, key: object) -> bool:
        """

        :param key:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
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
    def Remove(self, key: object) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, key: object) -> object:
        """

        :param key:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class INotifyCollectionChanged:
    """"""

    CollectionChanged: EventType[NotifyCollectionChangedEventHandler] = ...
    """"""

class IOrderedDictionary(ICollection, IDictionary, IEnumerable):
    """"""

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
    def Add(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, key: object) -> bool:
        """

        :param key:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def Insert(self, index: int, key: object, value: object) -> None:
        """

        :param index:
        :param key:
        :param value:
        """
    def Remove(self, key: object) -> None:
        """

        :param key:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, key: object) -> object:
        """

        :param key:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class ListDictionary(Object, ICollection, IDictionary, IEnumerable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, comparer: IComparer):
        """

        :param comparer:
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
    def Add(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, key: object) -> bool:
        """

        :param key:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
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
    def Remove(self, key: object) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, key: object) -> object:
        """

        :param key:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class NameObjectCollectionBase(
    ABC, Object, ICollection, IEnumerable, IDeserializationCallback, ISerializable
):
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
    def Keys(self) -> NameObjectCollectionBase.KeysCollection:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
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
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def OnDeserialization(self, sender: object) -> None:
        """

        :param sender:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

    class KeysCollection(Object, ICollection, IEnumerable):
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
        def Item(self) -> str:
            """"""
        @property
        def SyncRoot(self) -> object:
            """

            :return:
            """
        def CopyTo(self, array: Array, index: int) -> None:
            """

            :param array:
            :param index:
            """
        def Equals(self, obj: object) -> bool:
            """

            :param obj:
            :return:
            """
        def Get(self, index: int) -> str:
            """"""
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
        def ToString(self) -> str:
            """

            :return:
            """
        def __contains__(self, value: object) -> bool:
            """

            :param value:
            :return:
            """
        def __getitem__(self, index: int) -> str:
            """"""
        def __iter__(self) -> Iterator[object]:
            """

            :return:
            """
        def __len__(self) -> int:
            """

            :return:
            """

class NameValueCollection(
    NameObjectCollectionBase, ICollection, IEnumerable, IDeserializationCallback, ISerializable
):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, col: NameValueCollection):
        """

        :param col:
        """
    @overload
    def __init__(self, equalityComparer: IEqualityComparer):
        """

        :param equalityComparer:
        """
    @overload
    def __init__(self, capacity: int):
        """

        :param capacity:
        """
    @overload
    def __init__(self, hashProvider: IHashCodeProvider, comparer: IComparer):
        """

        :param hashProvider:
        :param comparer:
        """
    @overload
    def __init__(self, capacity: int, col: NameValueCollection):
        """

        :param capacity:
        :param col:
        """
    @overload
    def __init__(self, capacity: int, equalityComparer: IEqualityComparer):
        """

        :param capacity:
        :param equalityComparer:
        """
    @overload
    def __init__(self, capacity: int, hashProvider: IHashCodeProvider, comparer: IComparer):
        """

        :param capacity:
        :param hashProvider:
        :param comparer:
        """
    @property
    def AllKeys(self) -> Array[str]:
        """

        :return:
        """
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
    def Item(self) -> str:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: str) -> None: ...
    @property
    def Keys(self) -> NameObjectCollectionBase.KeysCollection:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, c: NameValueCollection) -> None:
        """

        :param c:
        """
    @overload
    def Add(self, name: str, value: str) -> None:
        """

        :param name:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Get(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    @overload
    def Get(self, name: str) -> str:
        """

        :param name:
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
    def GetKey(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetValues(self, index: int) -> Array[str]:
        """

        :param index:
        :return:
        """
    @overload
    def GetValues(self, name: str) -> Array[str]:
        """

        :param name:
        :return:
        """
    def HasKeys(self) -> bool:
        """

        :return:
        """
    def OnDeserialization(self, sender: object) -> None:
        """

        :param sender:
        """
    def Remove(self, name: str) -> None:
        """

        :param name:
        """
    def Set(self, name: str, value: str) -> None:
        """

        :param name:
        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, name: str) -> str:
        """

        :param name:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, name: str, value: str) -> None:
        """

        :param name:
        :param value:
        """

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
    def __init__(self, action: NotifyCollectionChangedAction):
        """

        :param action:
        """
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, changedItems: IList):
        """

        :param action:
        :param changedItems:
        """
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, changedItem: object):
        """

        :param action:
        :param changedItem:
        """
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, newItems: IList, oldItems: IList):
        """

        :param action:
        :param newItems:
        :param oldItems:
        """
    @overload
    def __init__(
        self, action: NotifyCollectionChangedAction, changedItems: IList, startingIndex: int
    ):
        """

        :param action:
        :param changedItems:
        :param startingIndex:
        """
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, changedItem: object, index: int):
        """

        :param action:
        :param changedItem:
        :param index:
        """
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, newItem: object, oldItem: object):
        """

        :param action:
        :param newItem:
        :param oldItem:
        """
    @overload
    def __init__(
        self,
        action: NotifyCollectionChangedAction,
        newItems: IList,
        oldItems: IList,
        startingIndex: int,
    ):
        """

        :param action:
        :param newItems:
        :param oldItems:
        :param startingIndex:
        """
    @overload
    def __init__(
        self, action: NotifyCollectionChangedAction, changedItems: IList, index: int, oldIndex: int
    ):
        """

        :param action:
        :param changedItems:
        :param index:
        :param oldIndex:
        """
    @overload
    def __init__(
        self, action: NotifyCollectionChangedAction, changedItem: object, index: int, oldIndex: int
    ):
        """

        :param action:
        :param changedItem:
        :param index:
        :param oldIndex:
        """
    @overload
    def __init__(
        self, action: NotifyCollectionChangedAction, newItem: object, oldItem: object, index: int
    ):
        """

        :param action:
        :param newItem:
        :param oldItem:
        :param index:
        """
    @property
    def Action(self) -> NotifyCollectionChangedAction:
        """

        :return:
        """
    @property
    def NewItems(self) -> IList:
        """

        :return:
        """
    @property
    def NewStartingIndex(self) -> int:
        """

        :return:
        """
    @property
    def OldItems(self) -> IList:
        """

        :return:
        """
    @property
    def OldStartingIndex(self) -> int:
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

NotifyCollectionChangedEventHandler: Callable[
    [object, NotifyCollectionChangedEventArgs], None
] = ...
"""

:param sender: 
:param e: 
"""

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
    def __init__(self):
        """"""
    @overload
    def __init__(self, comparer: IEqualityComparer):
        """

        :param comparer:
        """
    @overload
    def __init__(self, capacity: int):
        """

        :param capacity:
        """
    @overload
    def __init__(self, capacity: int, comparer: IEqualityComparer):
        """

        :param capacity:
        :param comparer:
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
    def Add(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """
    def AsReadOnly(self) -> OrderedDictionary:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, key: object) -> bool:
        """

        :param key:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
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
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Insert(self, index: int, key: object, value: object) -> None:
        """

        :param index:
        :param key:
        :param value:
        """
    def OnDeserialization(self, sender: object) -> None:
        """

        :param sender:
        """
    def Remove(self, key: object) -> None:
        """

        :param key:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, key: object) -> object:
        """

        :param key:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class StringCollection(Object, ICollection, IEnumerable, IList):
    """"""

    def __init__(self):
        """"""
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
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, value: str) -> int:
        """

        :param value:
        :return:
        """
    def AddRange(self, value: Array[str]) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def Contains(self, value: str) -> bool:
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
    def CopyTo(self, array: Array[str], index: int) -> None:
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
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def IndexOf(self, value: str) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Insert(self, index: int, value: str) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    @overload
    def Remove(self, value: str) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: str) -> None:
        """

        :param index:
        :param value:
        """

class StringDictionary(Object, IEnumerable):
    """"""

    def __init__(self):
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
    def Item(self) -> str:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: str) -> None: ...
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
    def Add(self, key: str, value: str) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def ContainsKey(self, key: str) -> bool:
        """

        :param key:
        :return:
        """
    def ContainsValue(self, value: str) -> bool:
        """

        :param value:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
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
    def Remove(self, key: str) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __getitem__(self, key: str) -> str:
        """

        :param key:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __setitem__(self, key: str, value: str) -> None:
        """

        :param key:
        :param value:
        """

class StringDictionaryWithComparer(StringDictionary, IEnumerable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, comparer: IEqualityComparer):
        """

        :param comparer:
        """
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
    def Item(self) -> str:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: str) -> None: ...
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
    def Add(self, key: str, value: str) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def ContainsKey(self, key: str) -> bool:
        """

        :param key:
        :return:
        """
    def ContainsValue(self, value: str) -> bool:
        """

        :param value:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
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
    def Remove(self, key: str) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __getitem__(self, key: str) -> str:
        """

        :param key:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __setitem__(self, key: str, value: str) -> None:
        """

        :param key:
        :param value:
        """

class StringEnumerator(Object):
    """"""

    @property
    def Current(self) -> str:
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
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
