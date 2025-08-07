"""Automatically generated stubs for C# namespace: System.Collections.Generic."""

from abc import ABC
from collections.abc import Callable
from collections.abc import Iterator
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
from System.Collections.ObjectModel import KeyedCollection
from System.Collections.ObjectModel import ReadOnlyCollection
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import IDeserializationCallback
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext

class ArrayBuilder[T](ValueType):
    """"""
    def __init__(self, capacity: int) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def Item(self) -> T:
        """"""
    @Item.setter
    def Item(self, value: T) -> None: ...
    def Add[T](self, item: T) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def First[T](self) -> T:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Last[T](self) -> T:
        """"""
    def ToArray(self) -> Array[T]:
        """"""
    def ToString(self) -> str:
        """"""
    def UncheckedAdd[T](self, item: T) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__[T](self, index: int) -> T:
        """"""
    def __setitem__[T](self, index: int, value: T) -> None:
        """"""

class ArraySortHelper[TKey, TValue](Object, IArraySortHelper[TKey, TValue]):
    """"""
    def __init__(self) -> None:
        """"""
    @classmethod
    @property
    def Default(cls) -> IArraySortHelper[TKey, TValue]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
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
    def ToString(self) -> str:
        """"""

class ArraySortHelper[T](Object, IArraySortHelper[T]):
    """"""
    def __init__(self) -> None:
        """"""
    @classmethod
    @property
    def Default(cls) -> IArraySortHelper[T]:
        """"""
    def BinarySearch[T](
        self, array: Array[T], index: int, length: int, value: T, comparer: IComparer[T]
    ) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Sort(self, keys: Array[T], index: int, length: int, comparer: IComparer[T]) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class BitHelper(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ByteEqualityComparer(EqualityComparer[Byte], IEqualityComparer[Byte], IEqualityComparer):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def Equals(self, x: int, y: int) -> bool:
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
    def GetHashCode(self, b: int) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: object) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Comparer[T](ABC, Object, IComparer[T], IComparer):
    """"""
    @classmethod
    @property
    def Default(cls) -> Comparer[T]:
        """"""
    @overload
    def Compare[T, T](self, x: T, y: T) -> int:
        """"""
    @overload
    def Compare(self, x: object, y: object) -> int:
        """"""
    @classmethod
    def Create(cls, comparison: Comparison[T]) -> Comparer[T]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ComparisonComparer[T](Comparer[T], IComparer[T], IComparer):
    """"""
    def __init__(self, comparison: Comparison[T]) -> None:
        """"""
    @overload
    def Compare[T, T](self, x: T, y: T) -> int:
        """"""
    @overload
    def Compare(self, x: object, y: object) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CopyPosition(ValueType):
    """"""
    @classmethod
    @property
    def Start(cls) -> CopyPosition:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Dictionary[TKey, TValue](
    Object,
    ICollection[KeyValuePair[TKey, TValue]],
    IDictionary[TKey, TValue],
    IEnumerable[KeyValuePair[TKey, TValue]],
    IReadOnlyCollection[KeyValuePair[TKey, TValue]],
    IReadOnlyDictionary[TKey, TValue],
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
    def __init__(self, comparer: IEqualityComparer[TKey]) -> None:
        """"""
    @overload
    def __init__(self, capacity: int, comparer: IEqualityComparer[TKey]) -> None:
        """"""
    @overload
    def __init__(self, dictionary: IDictionary[TKey, TValue]) -> None:
        """"""
    @overload
    def __init__(
        self, dictionary: IDictionary[TKey, TValue], comparer: IEqualityComparer[TKey]
    ) -> None:
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
    def Item(self) -> TValue:
        """"""
    @Item.setter
    def Item(self, value: TValue) -> None: ...
    @property
    def Keys(self) -> Dictionary.KeyCollection[TKey, TValue]:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> Dictionary.ValueCollection[TKey, TValue]:
        """"""
    @overload
    def Add[TKey, TValue](self, key: TKey, value: TValue) -> None:
        """"""
    @overload
    def Add(self, item: KeyValuePair[TKey, TValue]) -> None:
        """"""
    @overload
    def Add(self, key: object, value: object) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: KeyValuePair[TKey, TValue]) -> bool:
        """"""
    @overload
    def Contains(self, key: object) -> bool:
        """"""
    def ContainsKey[TKey](self, key: TKey) -> bool:
        """"""
    def ContainsValue[TValue](self, value: TValue) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[KeyValuePair[TKey, TValue]], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> Dictionary.Enumerator[TKey, TValue]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    @overload
    def Remove[TKey](self, key: TKey) -> bool:
        """"""
    @overload
    def Remove(self, item: KeyValuePair[TKey, TValue]) -> bool:
        """"""
    @overload
    def Remove(self, key: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TryGetValue[TKey](self, key: TKey, value: TValue) -> tuple[bool, TValue]:
        """"""
    @overload
    def __contains__(self, item: KeyValuePair[TKey, TValue]) -> bool:
        """"""
    @overload
    def __contains__(self, key: object) -> bool:
        """"""
    @overload
    def __contains__[TKey](self, key: TKey) -> bool:
        """"""
    def __iter__(self) -> Iterator[TKey, TValue]:
        """"""
    @overload
    def __delitem__[TKey](self, key: TKey) -> bool:
        """"""
    @overload
    def __delitem__(self, item: KeyValuePair[TKey, TValue]) -> bool:
        """"""
    @overload
    def __delitem__(self, key: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__[TKey, TValue](self, key: TKey) -> TValue:
        """"""
    @overload
    def __getitem__(self, key: object) -> object:
        """"""
    @overload
    def __setitem__[TKey, TValue](self, key: TKey, value: TValue) -> None:
        """"""
    @overload
    def __setitem__(self, key: object, value: object) -> None:
        """"""
    class Enumerator[TKey, TValue](
        ValueType,
        IEnumerator[KeyValuePair[TKey, TValue]],
        IDictionaryEnumerator,
        IEnumerator,
        IDisposable,
    ):
        """"""
        @property
        def Current(self) -> KeyValuePair[TKey, TValue]:
            """"""
        @property
        def Entry(self) -> DictionaryEntry:
            """"""
        @property
        def Key(self) -> object:
            """"""
        @property
        def Value(self) -> object:
            """"""
        def Dispose(self) -> None:
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

    class KeyCollection[TKey, TValue](
        Object,
        ICollection[TKey],
        IEnumerable[TKey],
        IReadOnlyCollection[TKey],
        ICollection,
        IEnumerable,
    ):
        """"""
        def __init__(self, dictionary: Dictionary[TKey, TValue]) -> None:
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
        def CopyTo(self, array: Array[TKey], index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> Dictionary.KeyCollection.Enumerator[TKey, TValue]:
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
        def __iter__(self) -> Iterator[TKey, TValue]:
            """"""
        def __delitem__[TKey](self, item: TKey) -> bool:
            """"""
        def __len__(self) -> int:
            """"""
        class Enumerator[TKey, TValue](ValueType, IEnumerator[TKey], IEnumerator, IDisposable):
            """"""
            @property
            def Current(self) -> TKey:
                """"""
            def Dispose(self) -> None:
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

    class ValueCollection[TKey, TValue](
        Object,
        ICollection[TValue],
        IEnumerable[TValue],
        IReadOnlyCollection[TValue],
        ICollection,
        IEnumerable,
    ):
        """"""
        def __init__(self, dictionary: Dictionary[TKey, TValue]) -> None:
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
        def CopyTo(self, array: Array[TValue], index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> Dictionary.ValueCollection.Enumerator[TKey, TValue]:
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
        def __iter__(self) -> Iterator[TKey, TValue]:
            """"""
        def __delitem__[TValue](self, item: TValue) -> bool:
            """"""
        def __len__(self) -> int:
            """"""
        class Enumerator[TKey, TValue](ValueType, IEnumerator[TValue], IEnumerator, IDisposable):
            """"""
            @property
            def Current(self) -> TValue:
                """"""
            def Dispose(self) -> None:
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

class EnumEqualityComparer[T](
    EqualityComparer[T], IEqualityComparer[T], IEqualityComparer, ISerializable
):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def Equals[T, T](self, x: T, y: T) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """"""
    @overload
    def GetHashCode[T](self, obj: T) -> int:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: object) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EnumerableHelpers(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EqualityComparer[T](ABC, Object, IEqualityComparer[T], IEqualityComparer):
    """"""
    @classmethod
    @property
    def Default(cls) -> EqualityComparer[T]:
        """"""
    @overload
    def Equals[T, T](self, x: T, y: T) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """"""
    @overload
    def GetHashCode[T](self, obj: T) -> int:
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

class GenericArraySortHelper[TKey, TValue](Object, IArraySortHelper[TKey, TValue]):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
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
    def ToString(self) -> str:
        """"""

class GenericArraySortHelper[T](Object, IArraySortHelper[T]):
    """"""
    def __init__(self) -> None:
        """"""
    def BinarySearch[T](
        self, array: Array[T], index: int, length: int, value: T, comparer: IComparer[T]
    ) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Sort(self, keys: Array[T], index: int, length: int, comparer: IComparer[T]) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class GenericComparer[T](Comparer[T], IComparer[T], IComparer):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def Compare[T, T](self, x: T, y: T) -> int:
        """"""
    @overload
    def Compare(self, x: object, y: object) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class GenericEqualityComparer[T](EqualityComparer[T], IEqualityComparer[T], IEqualityComparer):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def Equals[T, T](self, x: T, y: T) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """"""
    @overload
    def GetHashCode[T](self, obj: T) -> int:
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

class HashSetDebugView[T](Object):
    """"""
    def __init__(self, set: HashSet[T]) -> None:
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

class HashSetEqualityComparer[T](Object, IEqualityComparer[HashSet[T]]):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, comparer: IEqualityComparer[T]) -> None:
        """"""
    @overload
    def Equals(self, x: HashSet[T], y: HashSet[T]) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: HashSet[T]) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HashSet[T](
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
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, capacity: int) -> None:
        """"""
    @overload
    def __init__(self, comparer: IEqualityComparer[T]) -> None:
        """"""
    @overload
    def __init__(self, collection: IEnumerable[T]) -> None:
        """"""
    @overload
    def __init__(self, collection: IEnumerable[T], comparer: IEqualityComparer[T]) -> None:
        """"""
    @overload
    def __init__(self, capacity: int, comparer: IEqualityComparer[T]) -> None:
        """"""
    @property
    def Comparer(self) -> IEqualityComparer[T]:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    def Add[T](self, item: T) -> bool:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains[T](self, item: T) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array[T]) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[T], arrayIndex: int, count: int) -> None:
        """"""
    @classmethod
    def CreateSetComparer(cls) -> IEqualityComparer[HashSet[T]]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExceptWith(self, other: IEnumerable[T]) -> None:
        """"""
    def GetEnumerator(self) -> HashSet.Enumerator[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def IntersectWith(self, other: IEnumerable[T]) -> None:
        """"""
    def IsProperSubsetOf(self, other: IEnumerable[T]) -> bool:
        """"""
    def IsProperSupersetOf(self, other: IEnumerable[T]) -> bool:
        """"""
    def IsSubsetOf(self, other: IEnumerable[T]) -> bool:
        """"""
    def IsSupersetOf(self, other: IEnumerable[T]) -> bool:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    def Overlaps(self, other: IEnumerable[T]) -> bool:
        """"""
    def Remove[T](self, item: T) -> bool:
        """"""
    def RemoveWhere(self, match: Predicate[T]) -> int:
        """"""
    def SetEquals(self, other: IEnumerable[T]) -> bool:
        """"""
    def SymmetricExceptWith(self, other: IEnumerable[T]) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TrimExcess(self) -> None:
        """"""
    def TryGetValue[T](self, equalValue: T, actualValue: T) -> tuple[bool, T]:
        """"""
    def UnionWith(self, other: IEnumerable[T]) -> None:
        """"""
    def __contains__[T](self, item: T) -> bool:
        """"""
    def __iter__(self) -> Iterator[T]:
        """"""
    def __delitem__[T](self, item: T) -> bool:
        """"""
    def __len__(self) -> int:
        """"""
    class Enumerator[T](ValueType, IEnumerator[T], IEnumerator, IDisposable):
        """"""
        @property
        def Current(self) -> T:
            """"""
        def Dispose(self) -> None:
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

class IArraySortHelper[TKey, TValue]:
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

class IArraySortHelper[TKey]:
    """"""
    def BinarySearch[TKey](
        self, keys: Array[TKey], index: int, length: int, value: TKey, comparer: IComparer[TKey]
    ) -> int:
        """"""
    def Sort(self, keys: Array[TKey], index: int, length: int, comparer: IComparer[TKey]) -> None:
        """"""

class ICollection[T](IEnumerable[T], IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    def Add[T](self, item: T) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains[T](self, item: T) -> bool:
        """"""
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """"""
    def GetEnumerator(self) -> IEnumerator[T]:
        """"""
    def Remove[T](self, item: T) -> bool:
        """"""
    def __contains__[T](self, item: T) -> bool:
        """"""
    def __iter__(self) -> Iterator[T]:
        """"""
    def __delitem__[T](self, item: T) -> bool:
        """"""
    def __len__(self) -> int:
        """"""

class IComparer[T]:
    """"""
    def Compare[T, T](self, x: T, y: T) -> int:
        """"""

class IDictionary[TKey, TValue](
    ICollection[KeyValuePair[TKey, TValue]], IEnumerable[KeyValuePair[TKey, TValue]], IEnumerable
):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
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
    def Values(self) -> ICollection[TValue]:
        """"""
    @overload
    def Add[TKey, TValue](self, key: TKey, value: TValue) -> None:
        """"""
    @overload
    def Add(self, item: KeyValuePair[TKey, TValue]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, item: KeyValuePair[TKey, TValue]) -> bool:
        """"""
    def ContainsKey[TKey](self, key: TKey) -> bool:
        """"""
    def CopyTo(self, array: Array[KeyValuePair[TKey, TValue]], arrayIndex: int) -> None:
        """"""
    def GetEnumerator(self) -> IEnumerator[KeyValuePair[TKey, TValue]]:
        """"""
    @overload
    def Remove[TKey](self, key: TKey) -> bool:
        """"""
    @overload
    def Remove(self, item: KeyValuePair[TKey, TValue]) -> bool:
        """"""
    def TryGetValue[TKey](self, key: TKey, value: TValue) -> tuple[bool, TValue]:
        """"""
    @overload
    def __contains__(self, item: KeyValuePair[TKey, TValue]) -> bool:
        """"""
    @overload
    def __contains__[TKey](self, key: TKey) -> bool:
        """"""
    def __iter__(self) -> Iterator[KeyValuePair[TKey, TValue]]:
        """"""
    @overload
    def __delitem__[TKey](self, key: TKey) -> bool:
        """"""
    @overload
    def __delitem__(self, item: KeyValuePair[TKey, TValue]) -> bool:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__[TKey, TValue](self, key: TKey) -> TValue:
        """"""
    def __setitem__[TKey, TValue](self, key: TKey, value: TValue) -> None:
        """"""

class IEnumerable[T](IEnumerable):
    """"""
    def GetEnumerator(self) -> IEnumerator[T]:
        """"""
    def __iter__(self) -> Iterator[T]:
        """"""

class IEnumerator[T](IEnumerator, IDisposable):
    """"""
    @property
    def Current(self) -> T:
        """"""
    def Dispose(self) -> None:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""

class IEqualityComparer[T]:
    """"""
    def Equals[T, T](self, x: T, y: T) -> bool:
        """"""
    def GetHashCode[T](self, obj: T) -> int:
        """"""

class IList[T](ICollection[T], IEnumerable[T], IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Item(self) -> T:
        """"""
    @Item.setter
    def Item(self, value: T) -> None: ...
    def Add[T](self, item: T) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains[T](self, item: T) -> bool:
        """"""
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """"""
    def GetEnumerator(self) -> IEnumerator[T]:
        """"""
    def IndexOf[T](self, item: T) -> int:
        """"""
    def Insert[T](self, index: int, item: T) -> None:
        """"""
    def Remove[T](self, item: T) -> bool:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def __contains__[T](self, item: T) -> bool:
        """"""
    def __iter__(self) -> Iterator[T]:
        """"""
    def __delitem__[T](self, item: T) -> bool:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__[T](self, index: int) -> T:
        """"""
    def __setitem__[T](self, index: int, value: T) -> None:
        """"""

class IReadOnlyCollection[T](IEnumerable[T], IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    def GetEnumerator(self) -> IEnumerator[T]:
        """"""
    def __iter__(self) -> Iterator[T]:
        """"""
    def __len__(self) -> int:
        """"""

class IReadOnlyDictionary[TKey, TValue](
    IEnumerable[KeyValuePair[TKey, TValue]],
    IReadOnlyCollection[KeyValuePair[TKey, TValue]],
    IEnumerable,
):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def Item(self) -> TValue:
        """"""
    @property
    def Keys(self) -> IEnumerable[TKey]:
        """"""
    @property
    def Values(self) -> IEnumerable[TValue]:
        """"""
    def ContainsKey[TKey](self, key: TKey) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[KeyValuePair[TKey, TValue]]:
        """"""
    def TryGetValue[TKey](self, key: TKey, value: TValue) -> tuple[bool, TValue]:
        """"""
    def __contains__[TKey](self, key: TKey) -> bool:
        """"""
    def __iter__(self) -> Iterator[KeyValuePair[TKey, TValue]]:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__[TKey, TValue](self, key: TKey) -> TValue:
        """"""

class IReadOnlyList[T](IEnumerable[T], IReadOnlyCollection[T], IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def Item(self) -> T:
        """"""
    def GetEnumerator(self) -> IEnumerator[T]:
        """"""
    def __iter__(self) -> Iterator[T]:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__[T](self, index: int) -> T:
        """"""

class ISet[T](ICollection[T], IEnumerable[T], IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    def Add[T](self, item: T) -> bool:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains[T](self, item: T) -> bool:
        """"""
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """"""
    def ExceptWith(self, other: IEnumerable[T]) -> None:
        """"""
    def GetEnumerator(self) -> IEnumerator[T]:
        """"""
    def IntersectWith(self, other: IEnumerable[T]) -> None:
        """"""
    def IsProperSubsetOf(self, other: IEnumerable[T]) -> bool:
        """"""
    def IsProperSupersetOf(self, other: IEnumerable[T]) -> bool:
        """"""
    def IsSubsetOf(self, other: IEnumerable[T]) -> bool:
        """"""
    def IsSupersetOf(self, other: IEnumerable[T]) -> bool:
        """"""
    def Overlaps(self, other: IEnumerable[T]) -> bool:
        """"""
    def Remove[T](self, item: T) -> bool:
        """"""
    def SetEquals(self, other: IEnumerable[T]) -> bool:
        """"""
    def SymmetricExceptWith(self, other: IEnumerable[T]) -> None:
        """"""
    def UnionWith(self, other: IEnumerable[T]) -> None:
        """"""
    def __contains__[T](self, item: T) -> bool:
        """"""
    def __iter__(self) -> Iterator[T]:
        """"""
    def __delitem__[T](self, item: T) -> bool:
        """"""
    def __len__(self) -> int:
        """"""

class IntrospectiveSortUtilities(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class KeyNotFoundException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def HResult(self) -> int:
        """"""
    @property
    def HelpLink(self) -> str:
        """"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """"""
    @property
    def TargetSite(self) -> MethodBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class KeyValuePair[TKey, TValue](ValueType):
    """"""
    def __init__(self, key: TKey, value: TValue) -> None:
        """"""
    @property
    def Key(self) -> TKey:
        """"""
    @property
    def Value(self) -> TValue:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class LargeArrayBuilder[T](ValueType):
    """"""
    @overload
    def __init__(self, initialize: bool) -> None:
        """"""
    @overload
    def __init__(self, maxCapacity: int) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    def Add[T](self, item: T) -> None:
        """"""
    def AddRange(self, items: IEnumerable[T]) -> None:
        """"""
    @overload
    def CopyTo(
        self, position: CopyPosition, array: Array[T], arrayIndex: int, count: int
    ) -> CopyPosition:
        """"""
    @overload
    def CopyTo(self, array: Array[T], arrayIndex: int, count: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBuffer(self, index: int) -> Array[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SlowAdd[T](self, item: T) -> None:
        """"""
    def ToArray(self) -> Array[T]:
        """"""
    def ToString(self) -> str:
        """"""
    def TryMove(self, array: T) -> tuple[bool, T]:
        """"""
    def __len__(self) -> int:
        """"""

class LinkedListNode[T](Object):
    """"""
    def __init__(self, value: T) -> None:
        """"""
    @property
    def List(self) -> LinkedList[T]:
        """"""
    @property
    def Next(self) -> LinkedListNode[T]:
        """"""
    @property
    def Previous(self) -> LinkedListNode[T]:
        """"""
    @property
    def Value(self) -> T:
        """"""
    @Value.setter
    def Value(self, value: T) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class LinkedList[T](
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
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, collection: IEnumerable[T]) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def First(self) -> LinkedListNode[T]:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Last(self) -> LinkedListNode[T]:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def Add[T](self, item: T) -> None:
        """"""
    @overload
    def AddAfter[T](self, node: LinkedListNode[T], value: T) -> LinkedListNode[T]:
        """"""
    @overload
    def AddAfter(self, node: LinkedListNode[T], newNode: LinkedListNode[T]) -> None:
        """"""
    @overload
    def AddBefore[T](self, node: LinkedListNode[T], value: T) -> LinkedListNode[T]:
        """"""
    @overload
    def AddBefore(self, node: LinkedListNode[T], newNode: LinkedListNode[T]) -> None:
        """"""
    @overload
    def AddFirst[T](self, value: T) -> LinkedListNode[T]:
        """"""
    @overload
    def AddFirst(self, node: LinkedListNode[T]) -> None:
        """"""
    @overload
    def AddLast[T](self, value: T) -> LinkedListNode[T]:
        """"""
    @overload
    def AddLast(self, node: LinkedListNode[T]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains[T](self, value: T) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[T], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Find[T](self, value: T) -> LinkedListNode[T]:
        """"""
    def FindLast[T](self, value: T) -> LinkedListNode[T]:
        """"""
    def GetEnumerator(self) -> LinkedList.Enumerator[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    @overload
    def Remove[T](self, value: T) -> bool:
        """"""
    @overload
    def Remove(self, node: LinkedListNode[T]) -> None:
        """"""
    def RemoveFirst(self) -> None:
        """"""
    def RemoveLast(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__[T](self, value: T) -> bool:
        """"""
    def __iter__(self) -> Iterator[T]:
        """"""
    @overload
    def __delitem__[T](self, value: T) -> bool:
        """"""
    @overload
    def __delitem__(self, node: LinkedListNode[T]) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    class Enumerator[T](
        ValueType, IEnumerator[T], IEnumerator, IDeserializationCallback, ISerializable, IDisposable
    ):
        """"""
        @property
        def Current(self) -> T:
            """"""
        def Dispose(self) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
            """"""
        def GetType(self) -> Type:
            """"""
        def MoveNext(self) -> bool:
            """"""
        def OnDeserialization(self, sender: object) -> None:
            """"""
        def Reset(self) -> None:
            """"""
        def ToString(self) -> str:
            """"""

class List[T](
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
    def __init__(self, capacity: int) -> None:
        """"""
    @overload
    def __init__(self, collection: IEnumerable[T]) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
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
    def Add[T](self, item: T) -> None:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    def AddRange(self, collection: IEnumerable[T]) -> None:
        """"""
    def AsReadOnly(self) -> ReadOnlyCollection[T]:
        """"""
    @overload
    def BinarySearch[T](self, item: T) -> int:
        """"""
    @overload
    def BinarySearch[T](self, item: T, comparer: IComparer[T]) -> int:
        """"""
    @overload
    def BinarySearch[T](self, index: int, count: int, item: T, comparer: IComparer[T]) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains[T](self, item: T) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    def ConvertAll(self, converter: Converter[T, TOutput]) -> List[TOutput]:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[T]) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """"""
    @overload
    def CopyTo(self, index: int, array: Array[T], arrayIndex: int, count: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Exists(self, match: Predicate[T]) -> bool:
        """"""
    def Find[T](self, match: Predicate[T]) -> T:
        """"""
    def FindAll(self, match: Predicate[T]) -> List[T]:
        """"""
    @overload
    def FindIndex(self, startIndex: int, count: int, match: Predicate[T]) -> int:
        """"""
    @overload
    def FindIndex(self, startIndex: int, match: Predicate[T]) -> int:
        """"""
    @overload
    def FindIndex(self, match: Predicate[T]) -> int:
        """"""
    def FindLast[T](self, match: Predicate[T]) -> T:
        """"""
    @overload
    def FindLastIndex(self, startIndex: int, count: int, match: Predicate[T]) -> int:
        """"""
    @overload
    def FindLastIndex(self, startIndex: int, match: Predicate[T]) -> int:
        """"""
    @overload
    def FindLastIndex(self, match: Predicate[T]) -> int:
        """"""
    def ForEach(self, action: Action[T]) -> None:
        """"""
    def GetEnumerator(self) -> List.Enumerator[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetRange(self, index: int, count: int) -> List[T]:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf[T](self, item: T) -> int:
        """"""
    @overload
    def IndexOf[T](self, item: T, index: int) -> int:
        """"""
    @overload
    def IndexOf[T](self, item: T, index: int, count: int) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert[T](self, index: int, item: T) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    def InsertRange(self, index: int, collection: IEnumerable[T]) -> None:
        """"""
    @overload
    def LastIndexOf[T](self, item: T) -> int:
        """"""
    @overload
    def LastIndexOf[T](self, item: T, index: int) -> int:
        """"""
    @overload
    def LastIndexOf[T](self, item: T, index: int, count: int) -> int:
        """"""
    @overload
    def Remove[T](self, item: T) -> bool:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAll(self, match: Predicate[T]) -> int:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def RemoveRange(self, index: int, count: int) -> None:
        """"""
    @overload
    def Reverse(self) -> None:
        """"""
    @overload
    def Reverse(self, index: int, count: int) -> None:
        """"""
    @overload
    def Sort(self) -> None:
        """"""
    @overload
    def Sort(self, comparer: IComparer[T]) -> None:
        """"""
    @overload
    def Sort(self, comparison: Comparison[T]) -> None:
        """"""
    @overload
    def Sort(self, index: int, count: int, comparer: IComparer[T]) -> None:
        """"""
    def ToArray(self) -> Array[T]:
        """"""
    def ToString(self) -> str:
        """"""
    def TrimExcess(self) -> None:
        """"""
    def TrueForAll(self, match: Predicate[T]) -> bool:
        """"""
    @overload
    def __contains__[T](self, item: T) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator[T]:
        """"""
    @overload
    def __delitem__[T](self, item: T) -> bool:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__[T](self, index: int) -> T:
        """"""
    @overload
    def __setitem__[T](self, index: int, value: T) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""
    class Enumerator[T](ValueType, IEnumerator[T], IEnumerator, IDisposable):
        """"""
        @property
        def Current(self) -> T:
            """"""
        def Dispose(self) -> None:
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

class LongEnumEqualityComparer[T](
    EqualityComparer[T], IEqualityComparer[T], IEqualityComparer, ISerializable
):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, information: SerializationInfo, context: StreamingContext) -> None:
        """"""
    @overload
    def Equals[T, T](self, x: T, y: T) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """"""
    @overload
    def GetHashCode[T](self, obj: T) -> int:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: object) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Marker(ValueType):
    """"""
    def __init__(self, count: int, index: int) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def Index(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __len__(self) -> int:
        """"""

class Mscorlib_CollectionDebugView[T](Object):
    """"""
    def __init__(self, collection: ICollection[T]) -> None:
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

class Mscorlib_DictionaryDebugView[K, V](Object):
    """"""
    def __init__(self, dictionary: IDictionary[K, V]) -> None:
        """"""
    @property
    def Items(self) -> Array[KeyValuePair[K, V]]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Mscorlib_DictionaryKeyCollectionDebugView[TKey, TValue](Object):
    """"""
    def __init__(self, collection: ICollection[TKey]) -> None:
        """"""
    @property
    def Items(self) -> Array[TKey]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Mscorlib_DictionaryValueCollectionDebugView[TKey, TValue](Object):
    """"""
    def __init__(self, collection: ICollection[TValue]) -> None:
        """"""
    @property
    def Items(self) -> Array[TValue]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Mscorlib_KeyedCollectionDebugView[K, T](Object):
    """"""
    def __init__(self, keyedCollection: KeyedCollection[K, T]) -> None:
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

class NullableComparer[T](Comparer[T | None], IComparer[T | None], IComparer):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def Compare[T, T](self, x: T | None, y: T | None) -> int:
        """"""
    @overload
    def Compare(self, x: object, y: object) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NullableEqualityComparer[T](
    EqualityComparer[T | None], IEqualityComparer[T | None], IEqualityComparer
):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def Equals[T, T](self, x: T | None, y: T | None) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """"""
    @overload
    def GetHashCode[T](self, obj: T | None) -> int:
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

class ObjectComparer[T](Comparer[T], IComparer[T], IComparer):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def Compare[T, T](self, x: T, y: T) -> int:
        """"""
    @overload
    def Compare(self, x: object, y: object) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ObjectEqualityComparer[T](EqualityComparer[T], IEqualityComparer[T], IEqualityComparer):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def Equals[T, T](self, x: T, y: T) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """"""
    @overload
    def GetHashCode[T](self, obj: T) -> int:
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

class Queue[T](Object, IEnumerable[T], IReadOnlyCollection[T], ICollection, IEnumerable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, capacity: int) -> None:
        """"""
    @overload
    def __init__(self, collection: IEnumerable[T]) -> None:
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
    def Clear(self) -> None:
        """"""
    def Contains[T](self, item: T) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """"""
    def Dequeue[T](self) -> T:
        """"""
    def Enqueue[T](self, item: T) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> Queue.Enumerator[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Peek[T](self) -> T:
        """"""
    def ToArray(self) -> Array[T]:
        """"""
    def ToString(self) -> str:
        """"""
    def TrimExcess(self) -> None:
        """"""
    def __contains__[T](self, item: T) -> bool:
        """"""
    def __iter__(self) -> Iterator[T]:
        """"""
    def __len__(self) -> int:
        """"""
    class Enumerator[T](ValueType, IEnumerator[T], IEnumerator, IDisposable):
        """"""
        @property
        def Current(self) -> T:
            """"""
        def Dispose(self) -> None:
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

class RandomizedObjectEqualityComparer(Object, IEqualityComparer, IWellKnownStringEqualityComparer):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """"""
    def GetEqualityComparerForSerialization(self) -> IEqualityComparer:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: object) -> int:
        """"""
    def GetRandomizedEqualityComparer(self) -> IEqualityComparer:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RandomizedStringEqualityComparer(
    Object, IEqualityComparer[String], IEqualityComparer, IWellKnownStringEqualityComparer
):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """"""
    @overload
    def Equals(self, x: str, y: str) -> bool:
        """"""
    def GetEqualityComparerForSerialization(self) -> IEqualityComparer:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: object) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: str) -> int:
        """"""
    def GetRandomizedEqualityComparer(self) -> IEqualityComparer:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SByteEnumEqualityComparer[T](
    EnumEqualityComparer[T], IEqualityComparer[T], IEqualityComparer, ISerializable
):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, information: SerializationInfo, context: StreamingContext) -> None:
        """"""
    @overload
    def Equals[T, T](self, x: T, y: T) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """"""
    @overload
    def GetHashCode[T](self, obj: T) -> int:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: object) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ShortEnumEqualityComparer[T](
    EnumEqualityComparer[T], IEqualityComparer[T], IEqualityComparer, ISerializable
):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, information: SerializationInfo, context: StreamingContext) -> None:
        """"""
    @overload
    def Equals[T, T](self, x: T, y: T) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """"""
    @overload
    def GetHashCode[T](self, obj: T) -> int:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: object) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SortedDictionary[TKey, TValue](
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
    def __init__(self, dictionary: IDictionary[TKey, TValue]) -> None:
        """"""
    @overload
    def __init__(self, dictionary: IDictionary[TKey, TValue], comparer: IComparer[TKey]) -> None:
        """"""
    @overload
    def __init__(self, comparer: IComparer[TKey]) -> None:
        """"""
    @property
    def Comparer(self) -> IComparer[TKey]:
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
    @Item.setter
    def Item(self, value: TValue) -> None: ...
    @property
    def Keys(self) -> SortedDictionary.KeyCollection[TKey, TValue]:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> SortedDictionary.ValueCollection[TKey, TValue]:
        """"""
    @overload
    def Add[TKey, TValue](self, key: TKey, value: TValue) -> None:
        """"""
    @overload
    def Add(self, item: KeyValuePair[TKey, TValue]) -> None:
        """"""
    @overload
    def Add(self, key: object, value: object) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: KeyValuePair[TKey, TValue]) -> bool:
        """"""
    @overload
    def Contains(self, key: object) -> bool:
        """"""
    def ContainsKey[TKey](self, key: TKey) -> bool:
        """"""
    def ContainsValue[TValue](self, value: TValue) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[KeyValuePair[TKey, TValue]], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> SortedDictionary.Enumerator[TKey, TValue]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Remove[TKey](self, key: TKey) -> bool:
        """"""
    @overload
    def Remove(self, item: KeyValuePair[TKey, TValue]) -> bool:
        """"""
    @overload
    def Remove(self, key: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TryGetValue[TKey](self, key: TKey, value: TValue) -> tuple[bool, TValue]:
        """"""
    @overload
    def __contains__(self, item: KeyValuePair[TKey, TValue]) -> bool:
        """"""
    @overload
    def __contains__(self, key: object) -> bool:
        """"""
    @overload
    def __contains__[TKey](self, key: TKey) -> bool:
        """"""
    def __iter__(self) -> Iterator[TKey, TValue]:
        """"""
    @overload
    def __delitem__[TKey](self, key: TKey) -> bool:
        """"""
    @overload
    def __delitem__(self, item: KeyValuePair[TKey, TValue]) -> bool:
        """"""
    @overload
    def __delitem__(self, key: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__[TKey, TValue](self, key: TKey) -> TValue:
        """"""
    @overload
    def __getitem__(self, key: object) -> object:
        """"""
    @overload
    def __setitem__[TKey, TValue](self, key: TKey, value: TValue) -> None:
        """"""
    @overload
    def __setitem__(self, key: object, value: object) -> None:
        """"""
    class Enumerator[TKey, TValue](
        ValueType,
        IEnumerator[KeyValuePair[TKey, TValue]],
        IDictionaryEnumerator,
        IEnumerator,
        IDisposable,
    ):
        """"""
        @property
        def Current(self) -> KeyValuePair[TKey, TValue]:
            """"""
        @property
        def Entry(self) -> DictionaryEntry:
            """"""
        @property
        def Key(self) -> object:
            """"""
        @property
        def Value(self) -> object:
            """"""
        def Dispose(self) -> None:
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

    class KeyCollection[TKey, TValue](
        Object,
        ICollection[TKey],
        IEnumerable[TKey],
        IReadOnlyCollection[TKey],
        ICollection,
        IEnumerable,
    ):
        """"""
        def __init__(self, dictionary: SortedDictionary[TKey, TValue]) -> None:
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
        def CopyTo(self, array: Array[TKey], index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> SortedDictionary.KeyCollection.Enumerator[TKey, TValue]:
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
        def __iter__(self) -> Iterator[TKey, TValue]:
            """"""
        def __delitem__[TKey](self, item: TKey) -> bool:
            """"""
        def __len__(self) -> int:
            """"""
        class Enumerator[TKey, TValue](ValueType, IEnumerator[TKey], IEnumerator, IDisposable):
            """"""
            @property
            def Current(self) -> TKey:
                """"""
            def Dispose(self) -> None:
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

    class ValueCollection[TKey, TValue](
        Object,
        ICollection[TValue],
        IEnumerable[TValue],
        IReadOnlyCollection[TValue],
        ICollection,
        IEnumerable,
    ):
        """"""
        def __init__(self, dictionary: SortedDictionary[TKey, TValue]) -> None:
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
        def CopyTo(self, array: Array[TValue], index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> SortedDictionary.ValueCollection.Enumerator[TKey, TValue]:
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
        def __iter__(self) -> Iterator[TKey, TValue]:
            """"""
        def __delitem__[TValue](self, item: TValue) -> bool:
            """"""
        def __len__(self) -> int:
            """"""
        class Enumerator[TKey, TValue](ValueType, IEnumerator[TValue], IEnumerator, IDisposable):
            """"""
            @property
            def Current(self) -> TValue:
                """"""
            def Dispose(self) -> None:
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

class SortedList[TKey, TValue](
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
    def __init__(self, capacity: int) -> None:
        """"""
    @overload
    def __init__(self, comparer: IComparer[TKey]) -> None:
        """"""
    @overload
    def __init__(self, capacity: int, comparer: IComparer[TKey]) -> None:
        """"""
    @overload
    def __init__(self, dictionary: IDictionary[TKey, TValue]) -> None:
        """"""
    @overload
    def __init__(self, dictionary: IDictionary[TKey, TValue], comparer: IComparer[TKey]) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Comparer(self) -> IComparer[TKey]:
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
    @Item.setter
    def Item(self, value: TValue) -> None: ...
    @property
    def Keys(self) -> IList[TKey]:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> IList[TValue]:
        """"""
    @overload
    def Add[TKey, TValue](self, key: TKey, value: TValue) -> None:
        """"""
    @overload
    def Add(self, item: KeyValuePair[TKey, TValue]) -> None:
        """"""
    @overload
    def Add(self, key: object, value: object) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: KeyValuePair[TKey, TValue]) -> bool:
        """"""
    @overload
    def Contains(self, key: object) -> bool:
        """"""
    def ContainsKey[TKey](self, key: TKey) -> bool:
        """"""
    def ContainsValue[TValue](self, value: TValue) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[KeyValuePair[TKey, TValue]], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[KeyValuePair[TKey, TValue]]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IndexOfKey[TKey](self, key: TKey) -> int:
        """"""
    def IndexOfValue[TValue](self, value: TValue) -> int:
        """"""
    @overload
    def Remove[TKey](self, key: TKey) -> bool:
        """"""
    @overload
    def Remove(self, item: KeyValuePair[TKey, TValue]) -> bool:
        """"""
    @overload
    def Remove(self, key: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TrimExcess(self) -> None:
        """"""
    def TryGetValue[TKey](self, key: TKey, value: TValue) -> tuple[bool, TValue]:
        """"""
    @overload
    def __contains__(self, item: KeyValuePair[TKey, TValue]) -> bool:
        """"""
    @overload
    def __contains__(self, key: object) -> bool:
        """"""
    @overload
    def __contains__[TKey](self, key: TKey) -> bool:
        """"""
    def __iter__(self) -> Iterator[KeyValuePair[TKey, TValue]]:
        """"""
    @overload
    def __delitem__[TKey](self, key: TKey) -> bool:
        """"""
    @overload
    def __delitem__(self, item: KeyValuePair[TKey, TValue]) -> bool:
        """"""
    @overload
    def __delitem__(self, key: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__[TKey, TValue](self, key: TKey) -> TValue:
        """"""
    @overload
    def __getitem__(self, key: object) -> object:
        """"""
    @overload
    def __setitem__[TKey, TValue](self, key: TKey, value: TValue) -> None:
        """"""
    @overload
    def __setitem__(self, key: object, value: object) -> None:
        """"""

class SortedSetDebugView[T](Object):
    """"""
    def __init__(self, set: SortedSet[T]) -> None:
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

class SortedSetEqualityComparer[T](Object, IEqualityComparer[SortedSet[T]]):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, comparer: IComparer[T]) -> None:
        """"""
    @overload
    def __init__(self, memberEqualityComparer: IEqualityComparer[T]) -> None:
        """"""
    @overload
    def __init__(
        self, comparer: IComparer[T], memberEqualityComparer: IEqualityComparer[T]
    ) -> None:
        """"""
    @overload
    def Equals(self, x: SortedSet[T], y: SortedSet[T]) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: SortedSet[T]) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SortedSet[T](
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
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, comparer: IComparer[T]) -> None:
        """"""
    @overload
    def __init__(self, collection: IEnumerable[T]) -> None:
        """"""
    @overload
    def __init__(self, collection: IEnumerable[T], comparer: IComparer[T]) -> None:
        """"""
    @property
    def Comparer(self) -> IComparer[T]:
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
    def Max(self) -> T:
        """"""
    @property
    def Min(self) -> T:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def Add[T](self, item: T) -> bool:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains[T](self, item: T) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[T]) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[T], index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[T], index: int, count: int) -> None:
        """"""
    @classmethod
    @overload
    def CreateSetComparer(cls) -> IEqualityComparer[SortedSet[T]]:
        """"""
    @classmethod
    @overload
    def CreateSetComparer(
        cls, memberEqualityComparer: IEqualityComparer[T]
    ) -> IEqualityComparer[SortedSet[T]]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExceptWith(self, other: IEnumerable[T]) -> None:
        """"""
    def GetEnumerator(self) -> SortedSet.Enumerator[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetViewBetween[T, T](self, lowerValue: T, upperValue: T) -> SortedSet[T]:
        """"""
    def IntersectWith(self, other: IEnumerable[T]) -> None:
        """"""
    def IsProperSubsetOf(self, other: IEnumerable[T]) -> bool:
        """"""
    def IsProperSupersetOf(self, other: IEnumerable[T]) -> bool:
        """"""
    def IsSubsetOf(self, other: IEnumerable[T]) -> bool:
        """"""
    def IsSupersetOf(self, other: IEnumerable[T]) -> bool:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    def Overlaps(self, other: IEnumerable[T]) -> bool:
        """"""
    def Remove[T](self, item: T) -> bool:
        """"""
    def RemoveWhere(self, match: Predicate[T]) -> int:
        """"""
    def Reverse(self) -> IEnumerable[T]:
        """"""
    def SetEquals(self, other: IEnumerable[T]) -> bool:
        """"""
    def SymmetricExceptWith(self, other: IEnumerable[T]) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TryGetValue[T](self, equalValue: T, actualValue: T) -> tuple[bool, T]:
        """"""
    def UnionWith(self, other: IEnumerable[T]) -> None:
        """"""
    def __contains__[T](self, item: T) -> bool:
        """"""
    def __iter__(self) -> Iterator[T]:
        """"""
    def __delitem__[T](self, item: T) -> bool:
        """"""
    def __len__(self) -> int:
        """"""
    class Enumerator[T](
        ValueType, IEnumerator[T], IEnumerator, IDeserializationCallback, ISerializable, IDisposable
    ):
        """"""
        @property
        def Current(self) -> T:
            """"""
        def Dispose(self) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
            """"""
        def GetType(self) -> Type:
            """"""
        def MoveNext(self) -> bool:
            """"""
        def OnDeserialization(self, sender: object) -> None:
            """"""
        def Reset(self) -> None:
            """"""
        def ToString(self) -> str:
            """"""

class SparseArrayBuilder[T](ValueType):
    """"""
    def __init__(self, initialize: bool) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def Markers(self) -> ArrayBuilder[Marker]:
        """"""
    def Add[T](self, item: T) -> None:
        """"""
    def AddRange(self, items: IEnumerable[T]) -> None:
        """"""
    def CopyTo(self, array: Array[T], arrayIndex: int, count: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Reserve(self, count: int) -> None:
        """"""
    def ReserveOrAdd(self, items: IEnumerable[T]) -> bool:
        """"""
    def ToArray(self) -> Array[T]:
        """"""
    def ToString(self) -> str:
        """"""
    def __len__(self) -> int:
        """"""

class Stack[T](Object, IEnumerable[T], IReadOnlyCollection[T], ICollection, IEnumerable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, capacity: int) -> None:
        """"""
    @overload
    def __init__(self, collection: IEnumerable[T]) -> None:
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
    def Clear(self) -> None:
        """"""
    def Contains[T](self, item: T) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> Stack.Enumerator[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Peek[T](self) -> T:
        """"""
    def Pop[T](self) -> T:
        """"""
    def Push[T](self, item: T) -> None:
        """"""
    def ToArray(self) -> Array[T]:
        """"""
    def ToString(self) -> str:
        """"""
    def TrimExcess(self) -> None:
        """"""
    def __contains__[T](self, item: T) -> bool:
        """"""
    def __iter__(self) -> Iterator[T]:
        """"""
    def __len__(self) -> int:
        """"""
    class Enumerator[T](ValueType, IEnumerator[T], IEnumerator, IDisposable):
        """"""
        @property
        def Current(self) -> T:
            """"""
        def Dispose(self) -> None:
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

class System_CollectionDebugView[T](Object):
    """"""
    def __init__(self, collection: ICollection[T]) -> None:
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

class System_DictionaryDebugView[K, V](Object):
    """"""
    def __init__(self, dictionary: IDictionary[K, V]) -> None:
        """"""
    @property
    def Items(self) -> Array[KeyValuePair[K, V]]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class System_DictionaryKeyCollectionDebugView[TKey, TValue](Object):
    """"""
    def __init__(self, collection: ICollection[TKey]) -> None:
        """"""
    @property
    def Items(self) -> Array[TKey]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class System_DictionaryValueCollectionDebugView[TKey, TValue](Object):
    """"""
    def __init__(self, collection: ICollection[TValue]) -> None:
        """"""
    @property
    def Items(self) -> Array[TValue]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class System_QueueDebugView[T](Object):
    """"""
    def __init__(self, queue: Queue[T]) -> None:
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

class System_StackDebugView[T](Object):
    """"""
    def __init__(self, stack: Stack[T]) -> None:
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

class TreeSet[T](
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
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, comparer: IComparer[T]) -> None:
        """"""
    @overload
    def __init__(self, collection: ICollection[T]) -> None:
        """"""
    @overload
    def __init__(self, collection: ICollection[T], comparer: IComparer[T]) -> None:
        """"""
    @overload
    def __init__(self, siInfo: SerializationInfo, context: StreamingContext) -> None:
        """"""
    @property
    def Comparer(self) -> IComparer[T]:
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
    def Max(self) -> T:
        """"""
    @property
    def Min(self) -> T:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def Add[T](self, item: T) -> bool:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains[T](self, item: T) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[T]) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[T], index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[T], index: int, count: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExceptWith(self, other: IEnumerable[T]) -> None:
        """"""
    def GetEnumerator(self) -> SortedSet.Enumerator[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetViewBetween[T, T](self, lowerValue: T, upperValue: T) -> SortedSet[T]:
        """"""
    def IntersectWith(self, other: IEnumerable[T]) -> None:
        """"""
    def IsProperSubsetOf(self, other: IEnumerable[T]) -> bool:
        """"""
    def IsProperSupersetOf(self, other: IEnumerable[T]) -> bool:
        """"""
    def IsSubsetOf(self, other: IEnumerable[T]) -> bool:
        """"""
    def IsSupersetOf(self, other: IEnumerable[T]) -> bool:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    def Overlaps(self, other: IEnumerable[T]) -> bool:
        """"""
    def Remove[T](self, item: T) -> bool:
        """"""
    def RemoveWhere(self, match: Predicate[T]) -> int:
        """"""
    def Reverse(self) -> IEnumerable[T]:
        """"""
    def SetEquals(self, other: IEnumerable[T]) -> bool:
        """"""
    def SymmetricExceptWith(self, other: IEnumerable[T]) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TryGetValue[T](self, equalValue: T, actualValue: T) -> tuple[bool, T]:
        """"""
    def UnionWith(self, other: IEnumerable[T]) -> None:
        """"""
    def __contains__[T](self, item: T) -> bool:
        """"""
    def __iter__(self) -> Iterator[T]:
        """"""
    def __delitem__[T](self, item: T) -> bool:
        """"""
    def __len__(self) -> int:
        """"""
    class Enumerator[T](
        ValueType, IEnumerator[T], IEnumerator, IDeserializationCallback, ISerializable, IDisposable
    ):
        """"""
        @property
        def Current(self) -> T:
            """"""
        def Dispose(self) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
            """"""
        def GetType(self) -> Type:
            """"""
        def MoveNext(self) -> bool:
            """"""
        def OnDeserialization(self, sender: object) -> None:
            """"""
        def Reset(self) -> None:
            """"""
        def ToString(self) -> str:
            """"""

TreeWalkPredicate: Callable[[SortedSet.Node[T]], bool] = ...
""""""
