from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import Generic
from typing import Iterator
from typing import Optional
from typing import Tuple
from typing import TypeVar
from typing import overload

from System import Action
from System import Array
from System import Byte
from System import Comparison
from System import Converter
from System import Enum
from System import Exception
from System import IDisposable
from System import IWellKnownStringEqualityComparer
from System import Object
from System import Predicate
from System import String
from System import SystemException
from System import Type
from System import ValueType
from System.Collections import DictionaryEntry
from System.Collections import ICollection
from System.Collections import IComparer
from System.Collections import IDictionary
from System.Collections import IDictionaryEnumerator
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IEqualityComparer
from System.Collections import IList
from System.Collections.Generic.SortedSet import Node
from System.Collections.ObjectModel import KeyedCollection
from System.Collections.ObjectModel import ReadOnlyCollection
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import IDeserializationCallback
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext

K = TypeVar("K")
T = TypeVar("T")
TKey = TypeVar("TKey")
TOutput = TypeVar("TOutput")
TValue = TypeVar("TValue")
V = TypeVar("V")

class ArrayBuilder(Generic[T], ValueType):
    """"""

    def __init__(self, capacity: int):
        """

        :param capacity:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @property
    def Count(self) -> int:
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
    def Add(self, item: T) -> None:
        """

        :param item:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def First(self) -> T:
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
    def Last(self) -> T:
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
    def UncheckedAdd(self, item: T) -> None:
        """

        :param item:
        """
    def __getitem__(self, index: int) -> T:
        """

        :param index:
        :return:
        """
    def __setitem__(self, index: int, value: T) -> None:
        """

        :param index:
        :param value:
        """

class ArraySortHelper(Generic[TKey, TValue], Object, IArraySortHelper[TKey, TValue]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Default(cls) -> IArraySortHelper[TKey, TValue]:
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
    def Sort(
        self,
        keys: Array[TKey],
        values: Array[TValue],
        index: int,
        length: int,
        comparer: IComparer[TKey],
    ) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class ArraySortHelper(Generic[T], Object, IArraySortHelper[T]):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Default(cls) -> IArraySortHelper[T]:
        """

        :return:
        """
    def BinarySearch(
        self, keys: Array[T], index: int, length: int, value: T, comparer: IComparer[T]
    ) -> int:
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
    def Sort(self, keys: Array[T], index: int, length: int, comparer: IComparer[T]) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class BitHelper(Object):
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

class ByteEqualityComparer(EqualityComparer[Byte], IEqualityComparer[Byte], IEqualityComparer):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Default(cls) -> EqualityComparer[int]:
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
    def Equals(self, x: int, y: int) -> bool:
        """

        :param x:
        :param y:
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
    def GetHashCode(self, obj: int) -> int:
        """

        :param obj:
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

class Comparer(ABC, Generic[T], Object, IComparer[T], IComparer):
    """"""

    @classmethod
    @property
    def Default(cls) -> Comparer[T]:
        """

        :return:
        """
    @overload
    def Compare(self, x: T, y: T) -> int:
        """

        :param x:
        :param y:
        :return:
        """
    @overload
    def Compare(self, x: object, y: object) -> int:
        """

        :param x:
        :param y:
        :return:
        """
    @classmethod
    def Create(cls, comparison: Comparison[T]) -> Comparer[T]:
        """

        :param comparison:
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

class ComparisonComparer(Generic[T], Comparer[T], IComparer[T], IComparer):
    """"""

    def __init__(self, comparison: Comparison[T]):
        """

        :param comparison:
        """
    @classmethod
    @property
    def Default(cls) -> Comparer[T]:
        """

        :return:
        """
    @overload
    def Compare(self, x: T, y: T) -> int:
        """

        :param x:
        :param y:
        :return:
        """
    @overload
    def Compare(self, x: object, y: object) -> int:
        """

        :param x:
        :param y:
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

class CopyPosition(ValueType):
    """"""

    @classmethod
    @property
    def Start(cls) -> CopyPosition:
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

class Dictionary(
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
    IDeserializationCallback,
    ISerializable,
):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, dictionary: IDictionary[TKey, TValue]):
        """

        :param dictionary:
        """
    @overload
    def __init__(self, comparer: IEqualityComparer[TKey]):
        """

        :param comparer:
        """
    @overload
    def __init__(self, capacity: int):
        """

        :param capacity:
        """
    @overload
    def __init__(self, dictionary: IDictionary[TKey, TValue], comparer: IEqualityComparer[TKey]):
        """

        :param dictionary:
        :param comparer:
        """
    @overload
    def __init__(self, capacity: int, comparer: IEqualityComparer[TKey]):
        """

        :param capacity:
        :param comparer:
        """
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
    def Item(self) -> TValue:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: TValue) -> None: ...
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
    def ContainsValue(self, value: TValue) -> bool:
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
        """

        :param key:
        :param value:
        :return:
        """
    @overload
    def TryGetValue(self, key: TKey, value: TValue) -> Tuple[bool, TValue]:
        """

        :param key:
        :param value:
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

    class Enumerator(
        Generic[TKey, TValue],
        ValueType,
        IEnumerator[KeyValuePair, TValue],
        IDictionaryEnumerator,
        IEnumerator,
        IDisposable,
    ):
        """"""

        @property
        def Current(self) -> object:
            """

            :return:
            """
        @property
        def Entry(self) -> DictionaryEntry:
            """

            :return:
            """
        @property
        def Key(self) -> object:
            """

            :return:
            """
        @property
        def Value(self) -> object:
            """

            :return:
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

        def __init__(self, dictionary: Dictionary[TKey, TValue]):
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

        class Enumerator(
            Generic[TKey, TValue], ValueType, IEnumerator[TKey], IEnumerator, IDisposable
        ):
            """"""

            @property
            def Current(self) -> object:
                """

                :return:
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

        def __init__(self, dictionary: Dictionary[TKey, TValue]):
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

        class Enumerator(
            Generic[TKey, TValue], ValueType, IEnumerator[TValue], IEnumerator, IDisposable
        ):
            """"""

            @property
            def Current(self) -> object:
                """

                :return:
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

class EnumEqualityComparer(
    Generic[T], EqualityComparer[T], IEqualityComparer[T], IEqualityComparer, ISerializable
):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Default(cls) -> EqualityComparer[T]:
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
    def Equals(self, x: T, y: T) -> bool:
        """

        :param x:
        :param y:
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
    def GetHashCode(self, obj: T) -> int:
        """

        :param obj:
        :return:
        """
    @overload
    def GetHashCode(self, obj: object) -> int:
        """

        :param obj:
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
    def ToString(self) -> str:
        """

        :return:
        """

class EnumerableHelpers(ABC, Object):
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

class EqualityComparer(ABC, Generic[T], Object, IEqualityComparer[T], IEqualityComparer):
    """"""

    @classmethod
    @property
    def Default(cls) -> EqualityComparer[T]:
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
    def Equals(self, x: T, y: T) -> bool:
        """

        :param x:
        :param y:
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
    def GetHashCode(self, obj: T) -> int:
        """

        :param obj:
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

class GenericArraySortHelper(Generic[TKey, TValue], Object, IArraySortHelper[TKey, TValue]):
    """"""

    def __init__(self):
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
    def Sort(
        self,
        keys: Array[TKey],
        values: Array[TValue],
        index: int,
        length: int,
        comparer: IComparer[TKey],
    ) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class GenericArraySortHelper(Generic[T], Object, IArraySortHelper[T]):
    """"""

    def __init__(self):
        """"""
    def BinarySearch(
        self, keys: Array[T], index: int, length: int, value: T, comparer: IComparer[T]
    ) -> int:
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
    def Sort(self, keys: Array[T], index: int, length: int, comparer: IComparer[T]) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class GenericComparer(Generic[T], Comparer[T], IComparer[T], IComparer):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Default(cls) -> Comparer[T]:
        """

        :return:
        """
    @overload
    def Compare(self, x: T, y: T) -> int:
        """

        :param x:
        :param y:
        :return:
        """
    @overload
    def Compare(self, x: object, y: object) -> int:
        """

        :param x:
        :param y:
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

class GenericEqualityComparer(
    Generic[T], EqualityComparer[T], IEqualityComparer[T], IEqualityComparer
):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Default(cls) -> EqualityComparer[T]:
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
    def Equals(self, x: T, y: T) -> bool:
        """

        :param x:
        :param y:
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
    def GetHashCode(self, obj: T) -> int:
        """

        :param obj:
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

class HashSetDebugView(Generic[T], Object):
    """"""

    def __init__(self, set: HashSet[T]):
        """

        :param set:
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

class HashSetEqualityComparer(Generic[T], Object, IEqualityComparer[HashSet[T]]):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, comparer: IEqualityComparer[T]):
        """

        :param comparer:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, x: HashSet[T], y: HashSet[T]) -> bool:
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
    def GetHashCode(self, obj: HashSet[T]) -> int:
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

class HashSet(
    Generic[T],
    Object,
    ICollection[T],
    IEnumerable[T],
    IReadOnlyCollection[T],
    ISet[T],
    IEnumerable,
    IDeserializationCallback,
    ISerializable,
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
    def __init__(self, comparer: IEqualityComparer[T]):
        """

        :param comparer:
        """
    @overload
    def __init__(self, capacity: int):
        """

        :param capacity:
        """
    @overload
    def __init__(self, collection: IEnumerable[T], comparer: IEqualityComparer[T]):
        """

        :param collection:
        :param comparer:
        """
    @overload
    def __init__(self, capacity: int, comparer: IEqualityComparer[T]):
        """

        :param capacity:
        :param comparer:
        """
    @property
    def Comparer(self) -> IEqualityComparer[T]:
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
    def Add(self, item: T) -> None:
        """

        :param item:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def CopyTo(self, array: Array[T]) -> None:
        """

        :param array:
        """
    @overload
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """

        :param array:
        :param arrayIndex:
        """
    @overload
    def CopyTo(self, array: Array[T], arrayIndex: int, count: int) -> None:
        """

        :param array:
        :param arrayIndex:
        :param count:
        """
    @classmethod
    def CreateSetComparer(cls) -> IEqualityComparer[HashSet[T]]:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExceptWith(self, other: IEnumerable[T]) -> None:
        """

        :param other:
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
    def IntersectWith(self, other: IEnumerable[T]) -> None:
        """

        :param other:
        """
    def IsProperSubsetOf(self, other: IEnumerable[T]) -> bool:
        """

        :param other:
        :return:
        """
    def IsProperSupersetOf(self, other: IEnumerable[T]) -> bool:
        """

        :param other:
        :return:
        """
    def IsSubsetOf(self, other: IEnumerable[T]) -> bool:
        """

        :param other:
        :return:
        """
    def IsSupersetOf(self, other: IEnumerable[T]) -> bool:
        """

        :param other:
        :return:
        """
    def OnDeserialization(self, sender: object) -> None:
        """

        :param sender:
        """
    def Overlaps(self, other: IEnumerable[T]) -> bool:
        """

        :param other:
        :return:
        """
    def Remove(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    def RemoveWhere(self, match: Predicate[T]) -> int:
        """

        :param match:
        :return:
        """
    def SetEquals(self, other: IEnumerable[T]) -> bool:
        """

        :param other:
        :return:
        """
    def SymmetricExceptWith(self, other: IEnumerable[T]) -> None:
        """

        :param other:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TrimExcess(self) -> None:
        """"""
    def TryGetValue(self, equalValue: T, actualValue: T) -> Tuple[bool, T]:
        """

        :param equalValue:
        :param actualValue:
        :return:
        """
    def UnionWith(self, other: IEnumerable[T]) -> None:
        """

        :param other:
        """
    def __contains__(self, value: T) -> bool:
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

    class Enumerator(Generic[T], ValueType, IEnumerator[T], IEnumerator, IDisposable):
        """"""

        @property
        def Current(self) -> object:
            """

            :return:
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

class IArraySortHelper(Generic[TKey, TValue]):
    """"""

    def Sort(
        self,
        keys: Array[TKey],
        values: Array[TValue],
        index: int,
        length: int,
        comparer: IComparer[TKey],
    ) -> None:
        """"""

class IArraySortHelper(Generic[TKey]):
    """"""

    def BinarySearch(
        self, keys: Array[TKey], index: int, length: int, value: TKey, comparer: IComparer[TKey]
    ) -> int:
        """

        :param keys:
        :param index:
        :param length:
        :param value:
        :param comparer:
        :return:
        """
    def Sort(self, keys: Array[TKey], index: int, length: int, comparer: IComparer[TKey]) -> None:
        """

        :param keys:
        :param index:
        :param length:
        :param comparer:
        """

class ICollection(Generic[T], IEnumerable[T], IEnumerable):
    """"""

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
    def Add(self, item: T) -> None:
        """

        :param item:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """

        :param array:
        :param arrayIndex:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def Remove(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    def __contains__(self, value: T) -> bool:
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

class IComparer(Generic[T]):
    """"""

    def Compare(self, x: T, y: T) -> int:
        """

        :param x:
        :param y:
        :return:
        """

class IDictionary(
    Generic[TKey, TValue],
    ICollection[KeyValuePair, TValue],
    IEnumerable[KeyValuePair, TValue],
    IEnumerable,
):
    """"""

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
    def Clear(self) -> None:
        """"""
    def Contains(self, item: KeyValuePair[TKey, TValue]) -> bool:
        """

        :param item:
        :return:
        """
    def ContainsKey(self, key: TKey) -> bool:
        """

        :param key:
        :return:
        """
    def CopyTo(self, array: Array[KeyValuePair, TValue], arrayIndex: int) -> None:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def Remove(self, item: KeyValuePair[TKey, TValue]) -> bool:
        """

        :param item:
        :return:
        """
    def TryGetValue(self, key: TKey, value: TValue) -> Tuple[bool, TValue]:
        """

        :param key:
        :param value:
        :return:
        """
    def __contains__(self, value: KeyValuePair[TKey, TValue]) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, key: TKey) -> TValue:
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
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, key: TKey, value: TValue) -> None:
        """

        :param key:
        :param value:
        """

class IEnumerable(Generic[T], IEnumerable):
    """"""

    def GetEnumerator(self) -> IEnumerator:
        """

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

class IEnumerator(Generic[T], IEnumerator, IDisposable):
    """"""

    @property
    def Current(self) -> object:
        """

        :return:
        """
    def Dispose(self) -> None:
        """"""
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""

class IEqualityComparer(Generic[T]):
    """"""

    def Equals(self, x: T, y: T) -> bool:
        """

        :param x:
        :param y:
        :return:
        """
    def GetHashCode(self, obj: T) -> int:
        """

        :param obj:
        :return:
        """

class IList(Generic[T], ICollection[T], IEnumerable[T], IEnumerable):
    """"""

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
    def Item(self) -> T:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: T) -> None: ...
    def Add(self, item: T) -> None:
        """

        :param item:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """

        :param array:
        :param arrayIndex:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def IndexOf(self, item: T) -> int:
        """

        :param item:
        :return:
        """
    def Insert(self, index: int, item: T) -> None:
        """

        :param index:
        :param item:
        """
    def Remove(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def __contains__(self, value: T) -> bool:
        """

        :param value:
        :return:
        """
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
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, index: int, value: T) -> None:
        """

        :param index:
        :param value:
        """

class IReadOnlyCollection(Generic[T], IEnumerable[T], IEnumerable):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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

class IReadOnlyDictionary(
    Generic[TKey, TValue],
    IEnumerable[KeyValuePair, TValue],
    IReadOnlyCollection[KeyValuePair, TValue],
    IEnumerable,
):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def Item(self) -> TValue:
        """

        :return:
        """
    @property
    def Keys(self) -> IEnumerable[TKey]:
        """

        :return:
        """
    @property
    def Values(self) -> IEnumerable[TValue]:
        """

        :return:
        """
    def ContainsKey(self, key: TKey) -> bool:
        """

        :param key:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def TryGetValue(self, key: TKey, value: TValue) -> Tuple[bool, TValue]:
        """

        :param key:
        :param value:
        :return:
        """
    def __getitem__(self, key: TKey) -> TValue:
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

class IReadOnlyList(Generic[T], IEnumerable[T], IReadOnlyCollection[T], IEnumerable):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def Item(self) -> T:
        """

        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
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

class ISet(Generic[T], ICollection[T], IEnumerable[T], IEnumerable):
    """"""

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
    def Add(self, item: T) -> None:
        """

        :param item:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """

        :param array:
        :param arrayIndex:
        """
    def ExceptWith(self, other: IEnumerable[T]) -> None:
        """

        :param other:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def IntersectWith(self, other: IEnumerable[T]) -> None:
        """

        :param other:
        """
    def IsProperSubsetOf(self, other: IEnumerable[T]) -> bool:
        """

        :param other:
        :return:
        """
    def IsProperSupersetOf(self, other: IEnumerable[T]) -> bool:
        """

        :param other:
        :return:
        """
    def IsSubsetOf(self, other: IEnumerable[T]) -> bool:
        """

        :param other:
        :return:
        """
    def IsSupersetOf(self, other: IEnumerable[T]) -> bool:
        """

        :param other:
        :return:
        """
    def Overlaps(self, other: IEnumerable[T]) -> bool:
        """

        :param other:
        :return:
        """
    def Remove(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    def SetEquals(self, other: IEnumerable[T]) -> bool:
        """

        :param other:
        :return:
        """
    def SymmetricExceptWith(self, other: IEnumerable[T]) -> None:
        """

        :param other:
        """
    def UnionWith(self, other: IEnumerable[T]) -> None:
        """

        :param other:
        """
    def __contains__(self, value: T) -> bool:
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

class IntrospectiveSortUtilities(ABC, Object):
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

class KeyNotFoundException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, message: str, innerException: Exception):
        """

        :param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """

        :return:
        """
    @property
    def HResult(self) -> int:
        """

        :return:
        """
    @property
    def HelpLink(self) -> str:
        """

        :return:
        """
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """

        :return:
        """
    @property
    def Message(self) -> str:
        """

        :return:
        """
    @property
    def Source(self) -> str:
        """

        :return:
        """
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """

        :return:
        """
    @property
    def TargetSite(self) -> MethodBase:
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
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class KeyValuePair(Generic[TKey, TValue], ValueType):
    """"""

    def __init__(self, key: TKey, value: TValue):
        """

        :param key:
        :param value:
        """
    @property
    def Key(self) -> TKey:
        """

        :return:
        """
    @property
    def Value(self) -> TValue:
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

class LargeArrayBuilder(Generic[T], ValueType):
    """"""

    @overload
    def __init__(self, initialize: bool):
        """

        :param initialize:
        """
    @overload
    def __init__(self, maxCapacity: int):
        """

        :param maxCapacity:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    def Add(self, item: T) -> None:
        """

        :param item:
        """
    def AddRange(self, items: IEnumerable[T]) -> None:
        """

        :param items:
        """
    @overload
    def CopyTo(self, array: Array[T], arrayIndex: int, count: int) -> None:
        """

        :param array:
        :param arrayIndex:
        :param count:
        """
    @overload
    def CopyTo(
        self, position: CopyPosition, array: Array[T], arrayIndex: int, count: int
    ) -> CopyPosition:
        """

        :param position:
        :param array:
        :param arrayIndex:
        :param count:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBuffer(self, index: int) -> Array[T]:
        """

        :param index:
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
    def SlowAdd(self, item: T) -> None:
        """

        :param item:
        """
    def ToArray(self) -> Array[T]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TryMove(self, array: T) -> Tuple[bool, T]:
        """

        :param array:
        :return:
        """

class LinkedListNode(Generic[T], Object):
    """"""

    def __init__(self, value: T):
        """

        :param value:
        """
    @property
    def List(self) -> LinkedList[T]:
        """

        :return:
        """
    @property
    def Next(self) -> LinkedListNode[T]:
        """

        :return:
        """
    @property
    def Previous(self) -> LinkedListNode[T]:
        """

        :return:
        """
    @property
    def Value(self) -> T:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: T) -> None: ...
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

class LinkedList(
    Generic[T],
    Object,
    ICollection[T],
    IEnumerable[T],
    IReadOnlyCollection[T],
    ICollection,
    IEnumerable,
    IDeserializationCallback,
    ISerializable,
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
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def First(self) -> LinkedListNode[T]:
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
    def Last(self) -> LinkedListNode[T]:
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
    def AddAfter(self, node: LinkedListNode[T], value: T) -> LinkedListNode[T]:
        """

        :param node:
        :param value:
        :return:
        """
    @overload
    def AddAfter(self, node: LinkedListNode[T], newNode: LinkedListNode[T]) -> None:
        """

        :param node:
        :param newNode:
        """
    @overload
    def AddBefore(self, node: LinkedListNode[T], value: T) -> LinkedListNode[T]:
        """

        :param node:
        :param value:
        :return:
        """
    @overload
    def AddBefore(self, node: LinkedListNode[T], newNode: LinkedListNode[T]) -> None:
        """

        :param node:
        :param newNode:
        """
    @overload
    def AddFirst(self, value: T) -> LinkedListNode[T]:
        """

        :param value:
        :return:
        """
    @overload
    def AddFirst(self, node: LinkedListNode[T]) -> None:
        """

        :param node:
        """
    @overload
    def AddLast(self, value: T) -> LinkedListNode[T]:
        """

        :param value:
        :return:
        """
    @overload
    def AddLast(self, node: LinkedListNode[T]) -> None:
        """

        :param node:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, item: T) -> bool:
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
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """

        :param array:
        :param arrayIndex:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Find(self, value: T) -> LinkedListNode[T]:
        """

        :param value:
        :return:
        """
    def FindLast(self, value: T) -> LinkedListNode[T]:
        """

        :param value:
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
    def Remove(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    def RemoveFirst(self) -> None:
        """"""
    def RemoveLast(self) -> None:
        """"""
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

    class Enumerator(
        Generic[T],
        ValueType,
        IEnumerator[T],
        IEnumerator,
        IDeserializationCallback,
        ISerializable,
        IDisposable,
    ):
        """"""

        @property
        def Current(self) -> object:
            """

            :return:
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
        def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
            """

            :param info:
            :param context:
            """
        def GetType(self) -> Type:
            """

            :return:
            """
        def MoveNext(self) -> bool:
            """

            :return:
            """
        def OnDeserialization(self, sender: object) -> None:
            """

            :param sender:
            """
        def Reset(self) -> None:
            """"""
        def ToString(self) -> str:
            """

            :return:
            """

class List(
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
    def __init__(self, collection: IEnumerable[T]):
        """

        :param collection:
        """
    @overload
    def __init__(self, capacity: int):
        """

        :param capacity:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
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
    @Item.setter
    def Item(self, value: T) -> None: ...
    @property
    def Item(self) -> T:
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
    def AddRange(self, collection: IEnumerable[T]) -> None:
        """

        :param collection:
        """
    def AsReadOnly(self) -> ReadOnlyCollection[T]:
        """

        :return:
        """
    @overload
    def BinarySearch(self, item: T) -> int:
        """

        :param item:
        :return:
        """
    @overload
    def BinarySearch(self, item: T, comparer: IComparer[T]) -> int:
        """

        :param item:
        :param comparer:
        :return:
        """
    @overload
    def BinarySearch(self, index: int, count: int, item: T, comparer: IComparer[T]) -> int:
        """

        :param index:
        :param count:
        :param item:
        :param comparer:
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
    def ConvertAll(self, converter: Converter[T, TOutput]) -> List[TOutput]:
        """

        :param converter:
        :return:
        """
    @overload
    def CopyTo(self, array: Array[T]) -> None:
        """

        :param array:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """

        :param array:
        :param arrayIndex:
        """
    @overload
    def CopyTo(self, index: int, array: Array[T], arrayIndex: int, count: int) -> None:
        """

        :param index:
        :param array:
        :param arrayIndex:
        :param count:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Exists(self, match: Predicate[T]) -> bool:
        """

        :param match:
        :return:
        """
    def Find(self, match: Predicate[T]) -> T:
        """

        :param match:
        :return:
        """
    def FindAll(self, match: Predicate[T]) -> List[T]:
        """

        :param match:
        :return:
        """
    @overload
    def FindIndex(self, match: Predicate[T]) -> int:
        """

        :param match:
        :return:
        """
    @overload
    def FindIndex(self, startIndex: int, match: Predicate[T]) -> int:
        """

        :param startIndex:
        :param match:
        :return:
        """
    @overload
    def FindIndex(self, startIndex: int, count: int, match: Predicate[T]) -> int:
        """

        :param startIndex:
        :param count:
        :param match:
        :return:
        """
    def FindLast(self, match: Predicate[T]) -> T:
        """

        :param match:
        :return:
        """
    @overload
    def FindLastIndex(self, match: Predicate[T]) -> int:
        """

        :param match:
        :return:
        """
    @overload
    def FindLastIndex(self, startIndex: int, match: Predicate[T]) -> int:
        """

        :param startIndex:
        :param match:
        :return:
        """
    @overload
    def FindLastIndex(self, startIndex: int, count: int, match: Predicate[T]) -> int:
        """

        :param startIndex:
        :param count:
        :param match:
        :return:
        """
    def ForEach(self, action: Action[T]) -> None:
        """

        :param action:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetRange(self, index: int, count: int) -> List[T]:
        """

        :param index:
        :param count:
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
    def IndexOf(self, item: T, index: int) -> int:
        """

        :param item:
        :param index:
        :return:
        """
    @overload
    def IndexOf(self, item: T, index: int, count: int) -> int:
        """

        :param item:
        :param index:
        :param count:
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
    def InsertRange(self, index: int, collection: IEnumerable[T]) -> None:
        """

        :param index:
        :param collection:
        """
    @overload
    def LastIndexOf(self, item: T) -> int:
        """

        :param item:
        :return:
        """
    @overload
    def LastIndexOf(self, item: T, index: int) -> int:
        """

        :param item:
        :param index:
        :return:
        """
    @overload
    def LastIndexOf(self, item: T, index: int, count: int) -> int:
        """

        :param item:
        :param index:
        :param count:
        :return:
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
    def RemoveAll(self, match: Predicate[T]) -> int:
        """

        :param match:
        :return:
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
    def RemoveRange(self, index: int, count: int) -> None:
        """

        :param index:
        :param count:
        """
    @overload
    def Reverse(self) -> None:
        """"""
    @overload
    def Reverse(self, index: int, count: int) -> None:
        """

        :param index:
        :param count:
        """
    @overload
    def Sort(self) -> None:
        """"""
    @overload
    def Sort(self, comparer: IComparer[T]) -> None:
        """

        :param comparer:
        """
    @overload
    def Sort(self, comparison: Comparison[T]) -> None:
        """

        :param comparison:
        """
    @overload
    def Sort(self, index: int, count: int, comparer: IComparer[T]) -> None:
        """

        :param index:
        :param count:
        :param comparer:
        """
    def ToArray(self) -> Array[T]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TrimExcess(self) -> None:
        """"""
    def TrueForAll(self, match: Predicate[T]) -> bool:
        """

        :param match:
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

    class Enumerator(Generic[T], ValueType, IEnumerator[T], IEnumerator, IDisposable):
        """"""

        @property
        def Current(self) -> object:
            """

            :return:
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

class LongEnumEqualityComparer(
    Generic[T], EqualityComparer[T], IEqualityComparer[T], IEqualityComparer, ISerializable
):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, information: SerializationInfo, context: StreamingContext):
        """

        :param information:
        :param context:
        """
    @classmethod
    @property
    def Default(cls) -> EqualityComparer[T]:
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
    def Equals(self, x: T, y: T) -> bool:
        """

        :param x:
        :param y:
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
    def GetHashCode(self, obj: T) -> int:
        """

        :param obj:
        :return:
        """
    @overload
    def GetHashCode(self, obj: object) -> int:
        """

        :param obj:
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
    def ToString(self) -> str:
        """

        :return:
        """

class Marker(ValueType):
    """"""

    def __init__(self, count: int, index: int):
        """

        :param count:
        :param index:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def Index(self) -> int:
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

class Mscorlib_CollectionDebugView(Generic[T], Object):
    """"""

    def __init__(self, collection: ICollection[T]):
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

class Mscorlib_DictionaryDebugView(Generic[K, V], Object):
    """"""

    def __init__(self, dictionary: IDictionary[K, V]):
        """

        :param dictionary:
        """
    @property
    def Items(self) -> Array[KeyValuePair, V]:
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

class Mscorlib_DictionaryKeyCollectionDebugView(Generic[TKey, TValue], Object):
    """"""

    def __init__(self, collection: ICollection[TKey]):
        """

        :param collection:
        """
    @property
    def Items(self) -> Array[TKey]:
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

class Mscorlib_DictionaryValueCollectionDebugView(Generic[TKey, TValue], Object):
    """"""

    def __init__(self, collection: ICollection[TValue]):
        """

        :param collection:
        """
    @property
    def Items(self) -> Array[TValue]:
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

class Mscorlib_KeyedCollectionDebugView(Generic[K, T], Object):
    """"""

    def __init__(self, keyedCollection: KeyedCollection[K, T]):
        """

        :param keyedCollection:
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

class NullableComparer(Generic[T], Comparer[T], IComparer[T], IComparer):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Default(cls) -> Comparer[Optional[T]]:
        """

        :return:
        """
    @overload
    def Compare(self, x: Optional[T], y: Optional[T]) -> int:
        """

        :param x:
        :param y:
        :return:
        """
    @overload
    def Compare(self, x: object, y: object) -> int:
        """

        :param x:
        :param y:
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

class NullableEqualityComparer(
    Generic[T], EqualityComparer[T], IEqualityComparer[T], IEqualityComparer
):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Default(cls) -> EqualityComparer[Optional[T]]:
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
    def Equals(self, x: Optional[T], y: Optional[T]) -> bool:
        """

        :param x:
        :param y:
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
    def GetHashCode(self, obj: Optional[T]) -> int:
        """

        :param obj:
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

class ObjectComparer(Generic[T], Comparer[T], IComparer[T], IComparer):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Default(cls) -> Comparer[T]:
        """

        :return:
        """
    @overload
    def Compare(self, x: T, y: T) -> int:
        """

        :param x:
        :param y:
        :return:
        """
    @overload
    def Compare(self, x: object, y: object) -> int:
        """

        :param x:
        :param y:
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

class ObjectEqualityComparer(
    Generic[T], EqualityComparer[T], IEqualityComparer[T], IEqualityComparer
):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Default(cls) -> EqualityComparer[T]:
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
    def Equals(self, x: T, y: T) -> bool:
        """

        :param x:
        :param y:
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
    def GetHashCode(self, obj: T) -> int:
        """

        :param obj:
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

class Queue(Generic[T], Object, IEnumerable[T], IReadOnlyCollection[T], ICollection, IEnumerable):
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
    def __init__(self, capacity: int):
        """

        :param capacity:
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
    def Contains(self, item: T) -> bool:
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
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """

        :param array:
        :param arrayIndex:
        """
    def Dequeue(self) -> T:
        """

        :return:
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
    def Peek(self) -> T:
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
    def TrimExcess(self) -> None:
        """"""
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

    class Enumerator(Generic[T], ValueType, IEnumerator[T], IEnumerator, IDisposable):
        """"""

        @property
        def Current(self) -> object:
            """

            :return:
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

class RandomizedObjectEqualityComparer(Object, IEqualityComparer, IWellKnownStringEqualityComparer):
    """"""

    def __init__(self):
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
    def GetEqualityComparerForSerialization(self) -> IEqualityComparer:
        """

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
    def GetRandomizedEqualityComparer(self) -> IEqualityComparer:
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

class RandomizedStringEqualityComparer(
    Object, IEqualityComparer[String], IEqualityComparer, IWellKnownStringEqualityComparer
):
    """"""

    def __init__(self):
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
    def Equals(self, x: str, y: str) -> bool:
        """

        :param x:
        :param y:
        :return:
        """
    def GetEqualityComparerForSerialization(self) -> IEqualityComparer:
        """

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
    @overload
    def GetHashCode(self, obj: str) -> int:
        """

        :param obj:
        :return:
        """
    def GetRandomizedEqualityComparer(self) -> IEqualityComparer:
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

class SByteEnumEqualityComparer(
    Generic[T], EnumEqualityComparer[T], IEqualityComparer[T], IEqualityComparer, ISerializable
):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, information: SerializationInfo, context: StreamingContext):
        """

        :param information:
        :param context:
        """
    @classmethod
    @property
    def Default(cls) -> EqualityComparer[T]:
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
    def Equals(self, x: T, y: T) -> bool:
        """

        :param x:
        :param y:
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
    def GetHashCode(self, obj: T) -> int:
        """

        :param obj:
        :return:
        """
    @overload
    def GetHashCode(self, obj: object) -> int:
        """

        :param obj:
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
    def ToString(self) -> str:
        """

        :return:
        """

class ShortEnumEqualityComparer(
    Generic[T], EnumEqualityComparer[T], IEqualityComparer[T], IEqualityComparer, ISerializable
):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, information: SerializationInfo, context: StreamingContext):
        """

        :param information:
        :param context:
        """
    @classmethod
    @property
    def Default(cls) -> EqualityComparer[T]:
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
    def Equals(self, x: T, y: T) -> bool:
        """

        :param x:
        :param y:
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
    def GetHashCode(self, obj: T) -> int:
        """

        :param obj:
        :return:
        """
    @overload
    def GetHashCode(self, obj: object) -> int:
        """

        :param obj:
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
    def ToString(self) -> str:
        """

        :return:
        """

class SortedDictionary(
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
    def __init__(self, comparer: IComparer[TKey]):
        """

        :param comparer:
        """
    @overload
    def __init__(self, dictionary: IDictionary[TKey, TValue]):
        """

        :param dictionary:
        """
    @overload
    def __init__(self, dictionary: IDictionary[TKey, TValue], comparer: IComparer[TKey]):
        """

        :param dictionary:
        :param comparer:
        """
    @property
    def Comparer(self) -> IComparer[TKey]:
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
    def Item(self) -> TValue:
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
    def Keys(self) -> ICollection:
        """

        :return:
        """
    @property
    def Keys(self) -> IEnumerable[TKey]:
        """

        :return:
        """
    @property
    def Keys(self) -> ICollection[TKey]:
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
    def ContainsValue(self, value: TValue) -> bool:
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
        """

        :param key:
        :param value:
        :return:
        """
    @overload
    def TryGetValue(self, key: TKey, value: TValue) -> Tuple[bool, TValue]:
        """

        :param key:
        :param value:
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

    class Enumerator(
        Generic[TKey, TValue],
        ValueType,
        IEnumerator[KeyValuePair, TValue],
        IDictionaryEnumerator,
        IEnumerator,
        IDisposable,
    ):
        """"""

        @property
        def Current(self) -> object:
            """

            :return:
            """
        @property
        def Entry(self) -> DictionaryEntry:
            """

            :return:
            """
        @property
        def Key(self) -> object:
            """

            :return:
            """
        @property
        def Value(self) -> object:
            """

            :return:
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

        def __init__(self, dictionary: SortedDictionary[TKey, TValue]):
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

        class Enumerator(
            Generic[TKey, TValue], ValueType, IEnumerator[TKey], IEnumerator, IDisposable
        ):
            """"""

            @property
            def Current(self) -> object:
                """

                :return:
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

        def __init__(self, dictionary: SortedDictionary[TKey, TValue]):
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

        class Enumerator(
            Generic[TKey, TValue], ValueType, IEnumerator[TValue], IEnumerator, IDisposable
        ):
            """"""

            @property
            def Current(self) -> object:
                """

                :return:
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

class SortedList(
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
    def __init__(self, comparer: IComparer[TKey]):
        """

        :param comparer:
        """
    @overload
    def __init__(self, dictionary: IDictionary[TKey, TValue]):
        """

        :param dictionary:
        """
    @overload
    def __init__(self, capacity: int):
        """

        :param capacity:
        """
    @overload
    def __init__(self, dictionary: IDictionary[TKey, TValue], comparer: IComparer[TKey]):
        """

        :param dictionary:
        :param comparer:
        """
    @overload
    def __init__(self, capacity: int, comparer: IComparer[TKey]):
        """

        :param capacity:
        :param comparer:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Comparer(self) -> IComparer[TKey]:
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
    def Values(self) -> ICollection:
        """

        :return:
        """
    @property
    def Values(self) -> IEnumerable[TValue]:
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
    def ContainsValue(self, value: TValue) -> bool:
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
    def IndexOfKey(self, key: TKey) -> int:
        """

        :param key:
        :return:
        """
    def IndexOfValue(self, value: TValue) -> int:
        """

        :param value:
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
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TrimExcess(self) -> None:
        """"""
    @overload
    def TryGetValue(self, key: TKey, value: TValue) -> Tuple[bool, TValue]:
        """

        :param key:
        :param value:
        :return:
        """
    @overload
    def TryGetValue(self, key: TKey, value: TValue) -> Tuple[bool, TValue]:
        """

        :param key:
        :param value:
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

class SortedSetDebugView(Generic[T], Object):
    """"""

    def __init__(self, set: SortedSet[T]):
        """

        :param set:
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

class SortedSetEqualityComparer(Generic[T], Object, IEqualityComparer[SortedSet[T]]):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, comparer: IComparer[T]):
        """

        :param comparer:
        """
    @overload
    def __init__(self, memberEqualityComparer: IEqualityComparer[T]):
        """

        :param memberEqualityComparer:
        """
    @overload
    def __init__(self, comparer: IComparer[T], memberEqualityComparer: IEqualityComparer[T]):
        """

        :param comparer:
        :param memberEqualityComparer:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, x: SortedSet[T], y: SortedSet[T]) -> bool:
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
    def GetHashCode(self, obj: SortedSet[T]) -> int:
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

class SortedSet(
    Generic[T],
    Object,
    ICollection[T],
    IEnumerable[T],
    IReadOnlyCollection[T],
    ISet[T],
    ICollection,
    IEnumerable,
    IDeserializationCallback,
    ISerializable,
):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, comparer: IComparer[T]):
        """

        :param comparer:
        """
    @overload
    def __init__(self, collection: IEnumerable[T]):
        """

        :param collection:
        """
    @overload
    def __init__(self, collection: IEnumerable[T], comparer: IComparer[T]):
        """

        :param collection:
        :param comparer:
        """
    @property
    def Comparer(self) -> IComparer[T]:
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
    def Max(self) -> T:
        """

        :return:
        """
    @property
    def Min(self) -> T:
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
    def Clear(self) -> None:
        """"""
    def Contains(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def CopyTo(self, array: Array[T]) -> None:
        """

        :param array:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """

        :param array:
        :param arrayIndex:
        """
    @overload
    def CopyTo(self, array: Array[T], index: int, count: int) -> None:
        """

        :param array:
        :param index:
        :param count:
        """
    @classmethod
    @overload
    def CreateSetComparer(cls) -> IEqualityComparer[SortedSet[T]]:
        """

        :return:
        """
    @classmethod
    @overload
    def CreateSetComparer(
        cls, memberEqualityComparer: IEqualityComparer[T]
    ) -> IEqualityComparer[SortedSet[T]]:
        """

        :param memberEqualityComparer:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExceptWith(self, other: IEnumerable[T]) -> None:
        """

        :param other:
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
    def GetViewBetween(self, lowerValue: T, upperValue: T) -> SortedSet[T]:
        """

        :param lowerValue:
        :param upperValue:
        :return:
        """
    def IntersectWith(self, other: IEnumerable[T]) -> None:
        """

        :param other:
        """
    def IsProperSubsetOf(self, other: IEnumerable[T]) -> bool:
        """

        :param other:
        :return:
        """
    def IsProperSupersetOf(self, other: IEnumerable[T]) -> bool:
        """

        :param other:
        :return:
        """
    def IsSubsetOf(self, other: IEnumerable[T]) -> bool:
        """

        :param other:
        :return:
        """
    def IsSupersetOf(self, other: IEnumerable[T]) -> bool:
        """

        :param other:
        :return:
        """
    def OnDeserialization(self, sender: object) -> None:
        """

        :param sender:
        """
    def Overlaps(self, other: IEnumerable[T]) -> bool:
        """

        :param other:
        :return:
        """
    def Remove(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    def RemoveWhere(self, match: Predicate[T]) -> int:
        """

        :param match:
        :return:
        """
    def Reverse(self) -> IEnumerable[T]:
        """

        :return:
        """
    def SetEquals(self, other: IEnumerable[T]) -> bool:
        """

        :param other:
        :return:
        """
    def SymmetricExceptWith(self, other: IEnumerable[T]) -> None:
        """

        :param other:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TryGetValue(self, equalValue: T, actualValue: T) -> Tuple[bool, T]:
        """

        :param equalValue:
        :param actualValue:
        :return:
        """
    def UnionWith(self, other: IEnumerable[T]) -> None:
        """

        :param other:
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

    class Enumerator(
        Generic[T],
        ValueType,
        IEnumerator[T],
        IEnumerator,
        IDeserializationCallback,
        ISerializable,
        IDisposable,
    ):
        """"""

        @property
        def Current(self) -> object:
            """

            :return:
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
        def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
            """

            :param info:
            :param context:
            """
        def GetType(self) -> Type:
            """

            :return:
            """
        def MoveNext(self) -> bool:
            """

            :return:
            """
        def OnDeserialization(self, sender: object) -> None:
            """

            :param sender:
            """
        def Reset(self) -> None:
            """"""
        def ToString(self) -> str:
            """

            :return:
            """

class SparseArrayBuilder(Generic[T], ValueType):
    """"""

    def __init__(self, initialize: bool):
        """

        :param initialize:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def Markers(self) -> ArrayBuilder[Marker]:
        """

        :return:
        """
    def Add(self, item: T) -> None:
        """

        :param item:
        """
    def AddRange(self, items: IEnumerable[T]) -> None:
        """

        :param items:
        """
    def CopyTo(self, array: Array[T], arrayIndex: int, count: int) -> None:
        """

        :param array:
        :param arrayIndex:
        :param count:
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
    def Reserve(self, count: int) -> None:
        """

        :param count:
        """
    def ReserveOrAdd(self, items: IEnumerable[T]) -> bool:
        """

        :param items:
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

class Stack(Generic[T], Object, IEnumerable[T], IReadOnlyCollection[T], ICollection, IEnumerable):
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
    def __init__(self, capacity: int):
        """

        :param capacity:
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
    def Contains(self, item: T) -> bool:
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
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """

        :param array:
        :param arrayIndex:
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
    def Peek(self) -> T:
        """

        :return:
        """
    def Pop(self) -> T:
        """

        :return:
        """
    def Push(self, item: T) -> None:
        """

        :param item:
        """
    def ToArray(self) -> Array[T]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TrimExcess(self) -> None:
        """"""
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

    class Enumerator(Generic[T], ValueType, IEnumerator[T], IEnumerator, IDisposable):
        """"""

        @property
        def Current(self) -> object:
            """

            :return:
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

class System_CollectionDebugView(Generic[T], Object):
    """"""

    def __init__(self, collection: ICollection[T]):
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

class System_DictionaryDebugView(Generic[K, V], Object):
    """"""

    def __init__(self, dictionary: IDictionary[K, V]):
        """

        :param dictionary:
        """
    @property
    def Items(self) -> Array[KeyValuePair, V]:
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

class System_DictionaryKeyCollectionDebugView(Generic[TKey, TValue], Object):
    """"""

    def __init__(self, collection: ICollection[TKey]):
        """

        :param collection:
        """
    @property
    def Items(self) -> Array[TKey]:
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

class System_DictionaryValueCollectionDebugView(Generic[TKey, TValue], Object):
    """"""

    def __init__(self, collection: ICollection[TValue]):
        """

        :param collection:
        """
    @property
    def Items(self) -> Array[TValue]:
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

class System_QueueDebugView(Generic[T], Object):
    """"""

    def __init__(self, queue: Queue[T]):
        """

        :param queue:
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

class System_StackDebugView(Generic[T], Object):
    """"""

    def __init__(self, stack: Stack[T]):
        """

        :param stack:
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

class TreeRotation(Enum):
    """"""

    LeftRotation: TreeRotation = ...
    """"""
    RightRotation: TreeRotation = ...
    """"""
    RightLeftRotation: TreeRotation = ...
    """"""
    LeftRightRotation: TreeRotation = ...
    """"""

class TreeSet(
    Generic[T],
    SortedSet[T],
    ICollection[T],
    IEnumerable[T],
    IReadOnlyCollection[T],
    ISet[T],
    ICollection,
    IEnumerable,
    IDeserializationCallback,
    ISerializable,
):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, collection: ICollection[T]):
        """

        :param collection:
        """
    @overload
    def __init__(self, comparer: IComparer[T]):
        """

        :param comparer:
        """
    @overload
    def __init__(self, collection: ICollection[T], comparer: IComparer[T]):
        """

        :param collection:
        :param comparer:
        """
    @overload
    def __init__(self, siInfo: SerializationInfo, context: StreamingContext):
        """

        :param siInfo:
        :param context:
        """
    @property
    def Comparer(self) -> IComparer[T]:
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
    def Max(self) -> T:
        """

        :return:
        """
    @property
    def Min(self) -> T:
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
    def Clear(self) -> None:
        """"""
    def Contains(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def CopyTo(self, array: Array[T]) -> None:
        """

        :param array:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """

        :param array:
        :param arrayIndex:
        """
    @overload
    def CopyTo(self, array: Array[T], index: int, count: int) -> None:
        """

        :param array:
        :param index:
        :param count:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExceptWith(self, other: IEnumerable[T]) -> None:
        """

        :param other:
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
    def GetViewBetween(self, lowerValue: T, upperValue: T) -> SortedSet[T]:
        """

        :param lowerValue:
        :param upperValue:
        :return:
        """
    def IntersectWith(self, other: IEnumerable[T]) -> None:
        """

        :param other:
        """
    def IsProperSubsetOf(self, other: IEnumerable[T]) -> bool:
        """

        :param other:
        :return:
        """
    def IsProperSupersetOf(self, other: IEnumerable[T]) -> bool:
        """

        :param other:
        :return:
        """
    def IsSubsetOf(self, other: IEnumerable[T]) -> bool:
        """

        :param other:
        :return:
        """
    def IsSupersetOf(self, other: IEnumerable[T]) -> bool:
        """

        :param other:
        :return:
        """
    def OnDeserialization(self, sender: object) -> None:
        """

        :param sender:
        """
    def Overlaps(self, other: IEnumerable[T]) -> bool:
        """

        :param other:
        :return:
        """
    def Remove(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    def RemoveWhere(self, match: Predicate[T]) -> int:
        """

        :param match:
        :return:
        """
    def Reverse(self) -> IEnumerable[T]:
        """

        :return:
        """
    def SetEquals(self, other: IEnumerable[T]) -> bool:
        """

        :param other:
        :return:
        """
    def SymmetricExceptWith(self, other: IEnumerable[T]) -> None:
        """

        :param other:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TryGetValue(self, equalValue: T, actualValue: T) -> Tuple[bool, T]:
        """

        :param equalValue:
        :param actualValue:
        :return:
        """
    def UnionWith(self, other: IEnumerable[T]) -> None:
        """

        :param other:
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

TreeWalkPredicate: Callable[[SortedSet.Node[T]], bool] = ...
"""

:param node: 
:return: 
"""
