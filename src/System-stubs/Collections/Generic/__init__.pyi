from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import Generic
from typing import List
from typing import Optional
from typing import Protocol
from typing import Tuple
from typing import TypeVar
from typing import Union
from typing import overload

from System import Action
from System import Array
from System import AsyncCallback
from System import Boolean
from System import Byte
from System import Comparison
from System import Converter
from System import Enum
from System import Exception
from System import IAsyncResult
from System import ICloneable
from System import IDisposable
from System import Int32
from System import IntPtr
from System import IWellKnownStringEqualityComparer
from System import MulticastDelegate
from System import Nullable
from System import Object
from System import Predicate
from System import String
from System import SystemException
from System import ValueType
from System import Void
from System.Collections import IDictionaryEnumerator
from System.Collections.ObjectModel import KeyedCollection
from System.Collections.ObjectModel import ReadOnlyCollection
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import IDeserializationCallback
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext

# ---------- Types ---------- #

K = TypeVar("K")
T = TypeVar("T")
TKey = TypeVar("TKey")
TOutput = TypeVar("TOutput")
TValue = TypeVar("TValue")
V = TypeVar("V")

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
NIntType = Union[int, IntPtr]
NullableType = Union[Optional, Nullable]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class ArraySortHelper(Generic[T], ObjectType, IArraySortHelper[T]):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @staticmethod
    @property
    def Default() -> IArraySortHelper[T]: ...

    # ---------- Methods ---------- #

    def BinarySearch(
        self, array: ArrayType[T], index: IntType, length: IntType, value: T, comparer: IComparer[T]
    ) -> IntType: ...
    def Sort(
        self, keys: ArrayType[T], index: IntType, length: IntType, comparer: IComparer[T]
    ) -> VoidType: ...
    @staticmethod
    def get_Default() -> IArraySortHelper[T]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ArraySortHelper(Generic[TKey, TValue], ObjectType, IArraySortHelper[TKey, TValue]):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @staticmethod
    @property
    def Default() -> IArraySortHelper[TKey, TValue]: ...

    # ---------- Methods ---------- #

    def Sort(
        self,
        keys: ArrayType[TKey],
        values: ArrayType[TValue],
        index: IntType,
        length: IntType,
        comparer: IComparer[TKey],
    ) -> VoidType: ...
    @staticmethod
    def get_Default() -> IArraySortHelper[TKey, TValue]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class BitHelper(ObjectType):
    """"""

    # No Fields

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ByteEqualityComparer(
    EqualityComparer[ByteType], IEqualityComparer, IEqualityComparer[ByteType]
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def Equals(self, x: ByteType, y: ByteType) -> BooleanType: ...
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    @overload
    def GetHashCode(self, b: ByteType) -> IntType: ...
    @overload
    def GetHashCode(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Comparer(Protocol[T], ObjectType, IComparer, IComparer[T]):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @staticmethod
    @property
    def Default() -> Comparer[T]: ...

    # ---------- Methods ---------- #

    def Compare(self, x: T, y: T) -> IntType: ...
    @staticmethod
    def Create(comparison: Comparison[T]) -> Comparer[T]: ...
    @staticmethod
    def get_Default() -> Comparer[T]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ComparisonComparer(Generic[T], Comparer[T], IComparer, IComparer[T]):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, comparison: Comparison[T]): ...

    # No Properties

    # ---------- Methods ---------- #

    def Compare(self, x: T, y: T) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Dictionary(
    Generic[TKey, TValue],
    ObjectType,
    IDictionary[TKey, TValue],
    ICollection[KeyValuePair[TKey, TValue]],
    IEnumerable[KeyValuePair[TKey, TValue]],
    IEnumerable,
    IDictionary,
    ICollection,
    IReadOnlyDictionary[TKey, TValue],
    IReadOnlyCollection[KeyValuePair[TKey, TValue]],
    ISerializable,
    IDeserializationCallback,
):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, capacity: IntType): ...
    @overload
    def __init__(self, comparer: IEqualityComparer[TKey]): ...
    @overload
    def __init__(self, capacity: IntType, comparer: IEqualityComparer[TKey]): ...
    @overload
    def __init__(self, dictionary: IDictionary[TKey, TValue]): ...
    @overload
    def __init__(
        self, dictionary: IDictionary[TKey, TValue], comparer: IEqualityComparer[TKey]
    ): ...

    # ---------- Properties ---------- #

    @property
    def Comparer(self) -> IEqualityComparer[TKey]: ...
    @property
    def Count(self) -> IntType: ...
    def __getitem__(self, key: TKey) -> TValue: ...
    def __setitem__(self, key: TKey, value: TValue) -> None: ...
    @property
    def Keys(self) -> KeyCollection[TKey, TValue]: ...
    @property
    def Values(self) -> ValueCollection[TKey, TValue]: ...

    # ---------- Methods ---------- #

    def Add(self, key: TKey, value: TValue) -> VoidType: ...
    def Clear(self) -> VoidType: ...
    def ContainsKey(self, key: TKey) -> BooleanType: ...
    def ContainsValue(self, value: TValue) -> BooleanType: ...
    def GetEnumerator(self) -> Enumerator[TKey, TValue]: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    def OnDeserialization(self, sender: ObjectType) -> VoidType: ...
    def Remove(self, key: TKey) -> BooleanType: ...
    def TryGetValue(self, key: TKey, value: TValue) -> Tuple[BooleanType, TValue]: ...
    def get_Comparer(self) -> IEqualityComparer[TKey]: ...
    def get_Count(self) -> IntType: ...
    def get_Item(self, key: TKey) -> TValue: ...
    def get_Keys(self) -> KeyCollection[TKey, TValue]: ...
    def get_Values(self) -> ValueCollection[TKey, TValue]: ...
    def set_Item(self, key: TKey, value: TValue) -> VoidType: ...

    # No Events

    # ---------- Sub Classes ---------- #

    class KeyCollection(
        Generic[TKey, TValue],
        ObjectType,
        ICollection[TKey],
        IEnumerable[TKey],
        IEnumerable,
        ICollection,
        IReadOnlyCollection[TKey],
    ):
        # No Fields

        # ---------- Constructors ---------- #

        def __init__(self, dictionary: Dictionary[TKey, TValue]): ...

        # ---------- Properties ---------- #

        @property
        def Count(self) -> IntType: ...

        # ---------- Methods ---------- #

        def CopyTo(self, array: ArrayType[TKey], index: IntType) -> VoidType: ...
        def GetEnumerator(self) -> Enumerator[TKey, TValue]: ...
        def get_Count(self) -> IntType: ...

        # No Events

        # No Sub Classes

        # ---------- Sub Structs ---------- #

        class Enumerator(
            Generic[TKey, TValue], ValueType, IEnumerator[TKey], IDisposable, IEnumerator
        ):
            # No Fields

            # No Constructors

            # ---------- Properties ---------- #

            @property
            def Current(self) -> TKey: ...

            # ---------- Methods ---------- #

            def Dispose(self) -> VoidType: ...
            def MoveNext(self) -> BooleanType: ...
            def get_Current(self) -> TKey: ...

            # No Events

            # No Sub Classes

            # No Sub Structs

            # No Sub Interfaces

            # No Sub Enums
        # No Sub Interfaces

        # No Sub Enums

    class ValueCollection(
        Generic[TKey, TValue],
        ObjectType,
        ICollection[TValue],
        IEnumerable[TValue],
        IEnumerable,
        ICollection,
        IReadOnlyCollection[TValue],
    ):
        # No Fields

        # ---------- Constructors ---------- #

        def __init__(self, dictionary: Dictionary[TKey, TValue]): ...

        # ---------- Properties ---------- #

        @property
        def Count(self) -> IntType: ...

        # ---------- Methods ---------- #

        def CopyTo(self, array: ArrayType[TValue], index: IntType) -> VoidType: ...
        def GetEnumerator(self) -> Enumerator[TKey, TValue]: ...
        def get_Count(self) -> IntType: ...

        # No Events

        # No Sub Classes

        # ---------- Sub Structs ---------- #

        class Enumerator(
            Generic[TKey, TValue], ValueType, IEnumerator[TValue], IDisposable, IEnumerator
        ):
            # No Fields

            # No Constructors

            # ---------- Properties ---------- #

            @property
            def Current(self) -> TValue: ...

            # ---------- Methods ---------- #

            def Dispose(self) -> VoidType: ...
            def MoveNext(self) -> BooleanType: ...
            def get_Current(self) -> TValue: ...

            # No Events

            # No Sub Classes

            # No Sub Structs

            # No Sub Interfaces

            # No Sub Enums
        # No Sub Interfaces

        # No Sub Enums
    # ---------- Sub Structs ---------- #

    class Enumerator(
        Generic[TKey, TValue],
        ValueType,
        IEnumerator[KeyValuePair[TKey, TValue]],
        IDisposable,
        IEnumerator,
        IDictionaryEnumerator,
    ):
        # No Fields

        # No Constructors

        # ---------- Properties ---------- #

        @property
        def Current(self) -> KeyValuePair[TKey, TValue]: ...

        # ---------- Methods ---------- #

        def Dispose(self) -> VoidType: ...
        def MoveNext(self) -> BooleanType: ...
        def get_Current(self) -> KeyValuePair[TKey, TValue]: ...

        # No Events

        # No Sub Classes

        # No Sub Structs

        # No Sub Interfaces

        # No Sub Enums
    # No Sub Interfaces

    # No Sub Enums

class EnumEqualityComparer(
    Generic[T], EqualityComparer[T], IEqualityComparer, IEqualityComparer[T], ISerializable
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def Equals(self, x: T, y: T) -> BooleanType: ...
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    @overload
    def GetHashCode(self, obj: T) -> IntType: ...
    @overload
    def GetHashCode(self) -> IntType: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EnumerableHelpers(ABC, ObjectType):
    """"""

    # No Fields

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EqualityComparer(Protocol[T], ObjectType, IEqualityComparer, IEqualityComparer[T]):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @staticmethod
    @property
    def Default() -> EqualityComparer[T]: ...

    # ---------- Methods ---------- #

    @overload
    def Equals(self, x: T, y: T) -> BooleanType: ...
    @overload
    def GetHashCode(self, obj: T) -> IntType: ...
    @staticmethod
    def get_Default() -> EqualityComparer[T]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class GenericArraySortHelper(Generic[T], ObjectType, IArraySortHelper[T]):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def BinarySearch(
        self, array: ArrayType[T], index: IntType, length: IntType, value: T, comparer: IComparer[T]
    ) -> IntType: ...
    def Sort(
        self, keys: ArrayType[T], index: IntType, length: IntType, comparer: IComparer[T]
    ) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class GenericArraySortHelper(Generic[TKey, TValue], ObjectType, IArraySortHelper[TKey, TValue]):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Sort(
        self,
        keys: ArrayType[TKey],
        values: ArrayType[TValue],
        index: IntType,
        length: IntType,
        comparer: IComparer[TKey],
    ) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class GenericComparer(Generic[T], Comparer[T], IComparer, IComparer[T]):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Compare(self, x: T, y: T) -> IntType: ...
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    def GetHashCode(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class GenericEqualityComparer(
    Generic[T], EqualityComparer[T], IEqualityComparer, IEqualityComparer[T]
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def Equals(self, x: T, y: T) -> BooleanType: ...
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    @overload
    def GetHashCode(self, obj: T) -> IntType: ...
    @overload
    def GetHashCode(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class HashSet(
    Generic[T],
    ObjectType,
    ICollection[T],
    IEnumerable[T],
    IEnumerable,
    ISerializable,
    IDeserializationCallback,
    ISet[T],
    IReadOnlyCollection[T],
):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, capacity: IntType): ...
    @overload
    def __init__(self, comparer: IEqualityComparer[T]): ...
    @overload
    def __init__(self, collection: IEnumerable[T]): ...
    @overload
    def __init__(self, collection: IEnumerable[T], comparer: IEqualityComparer[T]): ...
    @overload
    def __init__(self, capacity: IntType, comparer: IEqualityComparer[T]): ...

    # ---------- Properties ---------- #

    @property
    def Comparer(self) -> IEqualityComparer[T]: ...
    @property
    def Count(self) -> IntType: ...

    # ---------- Methods ---------- #

    def Add(self, item: T) -> BooleanType: ...
    def Clear(self) -> VoidType: ...
    def Contains(self, item: T) -> BooleanType: ...
    @overload
    def CopyTo(self, array: ArrayType[T], arrayIndex: IntType) -> VoidType: ...
    @overload
    def CopyTo(self, array: ArrayType[T]) -> VoidType: ...
    @overload
    def CopyTo(self, array: ArrayType[T], arrayIndex: IntType, count: IntType) -> VoidType: ...
    @staticmethod
    def CreateSetComparer() -> IEqualityComparer[HashSet[T]]: ...
    def ExceptWith(self, other: IEnumerable[T]) -> VoidType: ...
    def GetEnumerator(self) -> Enumerator[T]: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    def IntersectWith(self, other: IEnumerable[T]) -> VoidType: ...
    def IsProperSubsetOf(self, other: IEnumerable[T]) -> BooleanType: ...
    def IsProperSupersetOf(self, other: IEnumerable[T]) -> BooleanType: ...
    def IsSubsetOf(self, other: IEnumerable[T]) -> BooleanType: ...
    def IsSupersetOf(self, other: IEnumerable[T]) -> BooleanType: ...
    def OnDeserialization(self, sender: ObjectType) -> VoidType: ...
    def Overlaps(self, other: IEnumerable[T]) -> BooleanType: ...
    def Remove(self, item: T) -> BooleanType: ...
    def RemoveWhere(self, match: Predicate[T]) -> IntType: ...
    def SetEquals(self, other: IEnumerable[T]) -> BooleanType: ...
    def SymmetricExceptWith(self, other: IEnumerable[T]) -> VoidType: ...
    def TrimExcess(self) -> VoidType: ...
    def TryGetValue(self, equalValue: T, actualValue: T) -> Tuple[BooleanType, T]: ...
    def UnionWith(self, other: IEnumerable[T]) -> VoidType: ...
    def get_Comparer(self) -> IEqualityComparer[T]: ...
    def get_Count(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # ---------- Sub Structs ---------- #

    class Enumerator(Generic[T], ValueType, IEnumerator[T], IDisposable, IEnumerator):
        # No Fields

        # No Constructors

        # ---------- Properties ---------- #

        @property
        def Current(self) -> T: ...

        # ---------- Methods ---------- #

        def Dispose(self) -> VoidType: ...
        def MoveNext(self) -> BooleanType: ...
        def get_Current(self) -> T: ...

        # No Events

        # No Sub Classes

        # No Sub Structs

        # No Sub Interfaces

        # No Sub Enums
    # No Sub Interfaces

    # No Sub Enums

class HashSetDebugView(Generic[T], ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, set: HashSet[T]): ...

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

class HashSetEqualityComparer(Generic[T], ObjectType, IEqualityComparer[HashSet[T]]):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, comparer: IEqualityComparer[T]): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def Equals(self, x: HashSet[T], y: HashSet[T]) -> BooleanType: ...
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    @overload
    def GetHashCode(self, obj: HashSet[T]) -> IntType: ...
    @overload
    def GetHashCode(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class IntrospectiveSortUtilities(ABC, ObjectType):
    """"""

    # No Fields

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class KeyNotFoundException(SystemException, ISerializable, _Exception):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: StringType): ...
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class LinkedList(
    Generic[T],
    ObjectType,
    ICollection[T],
    IEnumerable[T],
    IEnumerable,
    ICollection,
    IReadOnlyCollection[T],
    ISerializable,
    IDeserializationCallback,
):
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
    def First(self) -> LinkedListNode[T]: ...
    @property
    def Last(self) -> LinkedListNode[T]: ...

    # ---------- Methods ---------- #

    @overload
    def AddAfter(self, node: LinkedListNode[T], newNode: LinkedListNode[T]) -> VoidType: ...
    @overload
    def AddAfter(self, node: LinkedListNode[T], value: T) -> LinkedListNode[T]: ...
    @overload
    def AddBefore(self, node: LinkedListNode[T], value: T) -> LinkedListNode[T]: ...
    @overload
    def AddBefore(self, node: LinkedListNode[T], newNode: LinkedListNode[T]) -> VoidType: ...
    @overload
    def AddFirst(self, value: T) -> LinkedListNode[T]: ...
    @overload
    def AddFirst(self, node: LinkedListNode[T]) -> VoidType: ...
    @overload
    def AddLast(self, value: T) -> LinkedListNode[T]: ...
    @overload
    def AddLast(self, node: LinkedListNode[T]) -> VoidType: ...
    def Clear(self) -> VoidType: ...
    def Contains(self, value: T) -> BooleanType: ...
    def CopyTo(self, array: ArrayType[T], index: IntType) -> VoidType: ...
    def Find(self, value: T) -> LinkedListNode[T]: ...
    def FindLast(self, value: T) -> LinkedListNode[T]: ...
    def GetEnumerator(self) -> Enumerator[T]: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    def OnDeserialization(self, sender: ObjectType) -> VoidType: ...
    @overload
    def Remove(self, value: T) -> BooleanType: ...
    @overload
    def Remove(self, node: LinkedListNode[T]) -> VoidType: ...
    def RemoveFirst(self) -> VoidType: ...
    def RemoveLast(self) -> VoidType: ...
    def get_Count(self) -> IntType: ...
    def get_First(self) -> LinkedListNode[T]: ...
    def get_Last(self) -> LinkedListNode[T]: ...

    # No Events

    # No Sub Classes

    # ---------- Sub Structs ---------- #

    class Enumerator(
        Generic[T],
        ValueType,
        IEnumerator[T],
        IDisposable,
        IEnumerator,
        ISerializable,
        IDeserializationCallback,
    ):
        # No Fields

        # No Constructors

        # ---------- Properties ---------- #

        @property
        def Current(self) -> T: ...

        # ---------- Methods ---------- #

        def Dispose(self) -> VoidType: ...
        def MoveNext(self) -> BooleanType: ...
        def get_Current(self) -> T: ...

        # No Events

        # No Sub Classes

        # No Sub Structs

        # No Sub Interfaces

        # No Sub Enums
    # No Sub Interfaces

    # No Sub Enums

class LinkedListNode(Generic[T], ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, value: T): ...

    # ---------- Properties ---------- #

    @property
    def List(self) -> LinkedList[T]: ...
    @property
    def Next(self) -> LinkedListNode[T]: ...
    @property
    def Previous(self) -> LinkedListNode[T]: ...
    @property
    def Value(self) -> T: ...
    @Value.setter
    def Value(self, value: T) -> None: ...

    # ---------- Methods ---------- #

    def get_List(self) -> LinkedList[T]: ...
    def get_Next(self) -> LinkedListNode[T]: ...
    def get_Previous(self) -> LinkedListNode[T]: ...
    def get_Value(self) -> T: ...
    def set_Value(self, value: T) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class List(
    Generic[T],
    ObjectType,
    IList[T],
    ICollection[T],
    IEnumerable[T],
    IEnumerable,
    IList,
    ICollection,
    IReadOnlyList[T],
    IReadOnlyCollection[T],
):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, capacity: IntType): ...
    @overload
    def __init__(self, collection: IEnumerable[T]): ...

    # ---------- Properties ---------- #

    @property
    def Capacity(self) -> IntType: ...
    @Capacity.setter
    def Capacity(self, value: IntType) -> None: ...
    @property
    def Count(self) -> IntType: ...
    def __getitem__(self, key: IntType) -> T: ...
    def __setitem__(self, key: IntType, value: T) -> None: ...

    # ---------- Methods ---------- #

    def Add(self, item: T) -> VoidType: ...
    def AddRange(self, collection: IEnumerable[T]) -> VoidType: ...
    def AsReadOnly(self) -> ReadOnlyCollection[T]: ...
    @overload
    def BinarySearch(
        self, index: IntType, count: IntType, item: T, comparer: IComparer[T]
    ) -> IntType: ...
    @overload
    def BinarySearch(self, item: T) -> IntType: ...
    @overload
    def BinarySearch(self, item: T, comparer: IComparer[T]) -> IntType: ...
    def Clear(self) -> VoidType: ...
    def Contains(self, item: T) -> BooleanType: ...
    def ConvertAll(self, converter: Converter[T, TOutput]) -> List[TOutput]: ...
    @overload
    def CopyTo(
        self, index: IntType, array: ArrayType[T], arrayIndex: IntType, count: IntType
    ) -> VoidType: ...
    @overload
    def CopyTo(self, array: ArrayType[T]) -> VoidType: ...
    @overload
    def CopyTo(self, array: ArrayType[T], arrayIndex: IntType) -> VoidType: ...
    def Exists(self, match: Predicate[T]) -> BooleanType: ...
    def Find(self, match: Predicate[T]) -> T: ...
    def FindAll(self, match: Predicate[T]) -> List[T]: ...
    @overload
    def FindIndex(self, match: Predicate[T]) -> IntType: ...
    @overload
    def FindIndex(self, startIndex: IntType, match: Predicate[T]) -> IntType: ...
    @overload
    def FindIndex(self, startIndex: IntType, count: IntType, match: Predicate[T]) -> IntType: ...
    def FindLast(self, match: Predicate[T]) -> T: ...
    @overload
    def FindLastIndex(self, match: Predicate[T]) -> IntType: ...
    @overload
    def FindLastIndex(self, startIndex: IntType, match: Predicate[T]) -> IntType: ...
    @overload
    def FindLastIndex(
        self, startIndex: IntType, count: IntType, match: Predicate[T]
    ) -> IntType: ...
    def ForEach(self, action: Action[T]) -> VoidType: ...
    def GetEnumerator(self) -> Enumerator[T]: ...
    def GetRange(self, index: IntType, count: IntType) -> List[T]: ...
    @overload
    def IndexOf(self, item: T) -> IntType: ...
    @overload
    def IndexOf(self, item: T, index: IntType) -> IntType: ...
    @overload
    def IndexOf(self, item: T, index: IntType, count: IntType) -> IntType: ...
    def Insert(self, index: IntType, item: T) -> VoidType: ...
    def InsertRange(self, index: IntType, collection: IEnumerable[T]) -> VoidType: ...
    @overload
    def LastIndexOf(self, item: T) -> IntType: ...
    @overload
    def LastIndexOf(self, item: T, index: IntType) -> IntType: ...
    @overload
    def LastIndexOf(self, item: T, index: IntType, count: IntType) -> IntType: ...
    def Remove(self, item: T) -> BooleanType: ...
    def RemoveAll(self, match: Predicate[T]) -> IntType: ...
    def RemoveAt(self, index: IntType) -> VoidType: ...
    def RemoveRange(self, index: IntType, count: IntType) -> VoidType: ...
    @overload
    def Reverse(self, index: IntType, count: IntType) -> VoidType: ...
    @overload
    def Reverse(self) -> VoidType: ...
    @overload
    def Sort(self) -> VoidType: ...
    @overload
    def Sort(self, comparer: IComparer[T]) -> VoidType: ...
    @overload
    def Sort(self, index: IntType, count: IntType, comparer: IComparer[T]) -> VoidType: ...
    @overload
    def Sort(self, comparison: Comparison[T]) -> VoidType: ...
    def ToArray(self) -> ArrayType[T]: ...
    def TrimExcess(self) -> VoidType: ...
    def TrueForAll(self, match: Predicate[T]) -> BooleanType: ...
    def get_Capacity(self) -> IntType: ...
    def get_Count(self) -> IntType: ...
    def get_Item(self, index: IntType) -> T: ...
    def set_Capacity(self, value: IntType) -> VoidType: ...
    def set_Item(self, index: IntType, value: T) -> VoidType: ...

    # No Events

    # No Sub Classes

    # ---------- Sub Structs ---------- #

    class Enumerator(Generic[T], ValueType, IEnumerator[T], IDisposable, IEnumerator):
        # No Fields

        # No Constructors

        # ---------- Properties ---------- #

        @property
        def Current(self) -> T: ...

        # ---------- Methods ---------- #

        def Dispose(self) -> VoidType: ...
        def MoveNext(self) -> BooleanType: ...
        def get_Current(self) -> T: ...

        # No Events

        # No Sub Classes

        # No Sub Structs

        # No Sub Interfaces

        # No Sub Enums
    # No Sub Interfaces

    # No Sub Enums

class LongEnumEqualityComparer(
    Generic[T], EqualityComparer[T], IEqualityComparer, IEqualityComparer[T], ISerializable
):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, information: SerializationInfo, context: StreamingContext): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def Equals(self, x: T, y: T) -> BooleanType: ...
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    @overload
    def GetHashCode(self, obj: T) -> IntType: ...
    @overload
    def GetHashCode(self) -> IntType: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Mscorlib_CollectionDebugView(Generic[T], ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, collection: ICollection[T]): ...

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

class Mscorlib_DictionaryDebugView(Generic[K, V], ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, dictionary: IDictionary[K, V]): ...

    # ---------- Properties ---------- #

    @property
    def Items(self) -> ArrayType[KeyValuePair[K, V]]: ...

    # ---------- Methods ---------- #

    def get_Items(self) -> ArrayType[KeyValuePair[K, V]]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Mscorlib_DictionaryKeyCollectionDebugView(Generic[TKey, TValue], ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, collection: ICollection[TKey]): ...

    # ---------- Properties ---------- #

    @property
    def Items(self) -> ArrayType[TKey]: ...

    # ---------- Methods ---------- #

    def get_Items(self) -> ArrayType[TKey]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Mscorlib_DictionaryValueCollectionDebugView(Generic[TKey, TValue], ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, collection: ICollection[TValue]): ...

    # ---------- Properties ---------- #

    @property
    def Items(self) -> ArrayType[TValue]: ...

    # ---------- Methods ---------- #

    def get_Items(self) -> ArrayType[TValue]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Mscorlib_KeyedCollectionDebugView(Generic[K, T], ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, keyedCollection: KeyedCollection[K, T]): ...

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

class NullableComparer(
    Generic[T], Comparer[NullableType[Nullable[T]]], IComparer, IComparer[NullableType[Nullable[T]]]
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Compare(self, x: NullableType[Nullable[T]], y: NullableType[Nullable[T]]) -> IntType: ...
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    def GetHashCode(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class NullableEqualityComparer(
    Generic[T],
    EqualityComparer[NullableType[Nullable[T]]],
    IEqualityComparer,
    IEqualityComparer[NullableType[Nullable[T]]],
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def Equals(self, x: NullableType[Nullable[T]], y: NullableType[Nullable[T]]) -> BooleanType: ...
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    @overload
    def GetHashCode(self, obj: NullableType[Nullable[T]]) -> IntType: ...
    @overload
    def GetHashCode(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ObjectComparer(Generic[T], Comparer[T], IComparer, IComparer[T]):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Compare(self, x: T, y: T) -> IntType: ...
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    def GetHashCode(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ObjectEqualityComparer(
    Generic[T], EqualityComparer[T], IEqualityComparer, IEqualityComparer[T]
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def Equals(self, x: T, y: T) -> BooleanType: ...
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    @overload
    def GetHashCode(self, obj: T) -> IntType: ...
    @overload
    def GetHashCode(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Queue(
    Generic[T], ObjectType, IEnumerable[T], IEnumerable, ICollection, IReadOnlyCollection[T]
):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, capacity: IntType): ...
    @overload
    def __init__(self, collection: IEnumerable[T]): ...

    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...

    # ---------- Methods ---------- #

    def Clear(self) -> VoidType: ...
    def Contains(self, item: T) -> BooleanType: ...
    def CopyTo(self, array: ArrayType[T], arrayIndex: IntType) -> VoidType: ...
    def Dequeue(self) -> T: ...
    def Enqueue(self, item: T) -> VoidType: ...
    def GetEnumerator(self) -> Enumerator[T]: ...
    def Peek(self) -> T: ...
    def ToArray(self) -> ArrayType[T]: ...
    def TrimExcess(self) -> VoidType: ...
    def get_Count(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # ---------- Sub Structs ---------- #

    class Enumerator(Generic[T], ValueType, IEnumerator[T], IDisposable, IEnumerator):
        # No Fields

        # No Constructors

        # ---------- Properties ---------- #

        @property
        def Current(self) -> T: ...

        # ---------- Methods ---------- #

        def Dispose(self) -> VoidType: ...
        def MoveNext(self) -> BooleanType: ...
        def get_Current(self) -> T: ...

        # No Events

        # No Sub Classes

        # No Sub Structs

        # No Sub Interfaces

        # No Sub Enums
    # No Sub Interfaces

    # No Sub Enums

class RandomizedObjectEqualityComparer(
    ObjectType, IEqualityComparer, IWellKnownStringEqualityComparer
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def Equals(self, x: ObjectType, y: ObjectType) -> BooleanType: ...
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    @overload
    def GetHashCode(self, obj: ObjectType) -> IntType: ...
    @overload
    def GetHashCode(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RandomizedStringEqualityComparer(
    ObjectType, IEqualityComparer[StringType], IEqualityComparer, IWellKnownStringEqualityComparer
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def Equals(self, x: ObjectType, y: ObjectType) -> BooleanType: ...
    @overload
    def Equals(self, x: StringType, y: StringType) -> BooleanType: ...
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    @overload
    def GetHashCode(self, obj: StringType) -> IntType: ...
    @overload
    def GetHashCode(self, obj: ObjectType) -> IntType: ...
    @overload
    def GetHashCode(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SByteEnumEqualityComparer(
    Generic[T], EnumEqualityComparer[T], IEqualityComparer, IEqualityComparer[T], ISerializable
):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, information: SerializationInfo, context: StreamingContext): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def GetHashCode(self, obj: T) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ShortEnumEqualityComparer(
    Generic[T], EnumEqualityComparer[T], IEqualityComparer, IEqualityComparer[T], ISerializable
):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, information: SerializationInfo, context: StreamingContext): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def GetHashCode(self, obj: T) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SortedDictionary(
    Generic[TKey, TValue],
    ObjectType,
    IDictionary[TKey, TValue],
    ICollection[KeyValuePair[TKey, TValue]],
    IEnumerable[KeyValuePair[TKey, TValue]],
    IEnumerable,
    IDictionary,
    ICollection,
    IReadOnlyDictionary[TKey, TValue],
    IReadOnlyCollection[KeyValuePair[TKey, TValue]],
):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, dictionary: IDictionary[TKey, TValue]): ...
    @overload
    def __init__(self, dictionary: IDictionary[TKey, TValue], comparer: IComparer[TKey]): ...
    @overload
    def __init__(self, comparer: IComparer[TKey]): ...

    # ---------- Properties ---------- #

    @property
    def Comparer(self) -> IComparer[TKey]: ...
    @property
    def Count(self) -> IntType: ...
    def __getitem__(self, key: TKey) -> TValue: ...
    def __setitem__(self, key: TKey, value: TValue) -> None: ...
    @property
    def Keys(self) -> KeyCollection[TKey, TValue]: ...
    @property
    def Values(self) -> ValueCollection[TKey, TValue]: ...

    # ---------- Methods ---------- #

    def Add(self, key: TKey, value: TValue) -> VoidType: ...
    def Clear(self) -> VoidType: ...
    def ContainsKey(self, key: TKey) -> BooleanType: ...
    def ContainsValue(self, value: TValue) -> BooleanType: ...
    def CopyTo(self, array: ArrayType[KeyValuePair[TKey, TValue]], index: IntType) -> VoidType: ...
    def GetEnumerator(self) -> Enumerator[TKey, TValue]: ...
    def Remove(self, key: TKey) -> BooleanType: ...
    def TryGetValue(self, key: TKey, value: TValue) -> Tuple[BooleanType, TValue]: ...
    def get_Comparer(self) -> IComparer[TKey]: ...
    def get_Count(self) -> IntType: ...
    def get_Item(self, key: TKey) -> TValue: ...
    def get_Keys(self) -> KeyCollection[TKey, TValue]: ...
    def get_Values(self) -> ValueCollection[TKey, TValue]: ...
    def set_Item(self, key: TKey, value: TValue) -> VoidType: ...

    # No Events

    # ---------- Sub Classes ---------- #

    class KeyCollection(
        Generic[TKey, TValue],
        ObjectType,
        ICollection[TKey],
        IEnumerable[TKey],
        IEnumerable,
        ICollection,
        IReadOnlyCollection[TKey],
    ):
        # No Fields

        # ---------- Constructors ---------- #

        def __init__(self, dictionary: SortedDictionary[TKey, TValue]): ...

        # ---------- Properties ---------- #

        @property
        def Count(self) -> IntType: ...

        # ---------- Methods ---------- #

        def CopyTo(self, array: ArrayType[TKey], index: IntType) -> VoidType: ...
        def GetEnumerator(self) -> Enumerator[TKey, TValue]: ...
        def get_Count(self) -> IntType: ...

        # No Events

        # No Sub Classes

        # ---------- Sub Structs ---------- #

        class Enumerator(
            Generic[TKey, TValue], ValueType, IEnumerator[TKey], IDisposable, IEnumerator
        ):
            # No Fields

            # No Constructors

            # ---------- Properties ---------- #

            @property
            def Current(self) -> TKey: ...

            # ---------- Methods ---------- #

            def Dispose(self) -> VoidType: ...
            def MoveNext(self) -> BooleanType: ...
            def get_Current(self) -> TKey: ...

            # No Events

            # No Sub Classes

            # No Sub Structs

            # No Sub Interfaces

            # No Sub Enums
        # No Sub Interfaces

        # No Sub Enums

    class ValueCollection(
        Generic[TKey, TValue],
        ObjectType,
        ICollection[TValue],
        IEnumerable[TValue],
        IEnumerable,
        ICollection,
        IReadOnlyCollection[TValue],
    ):
        # No Fields

        # ---------- Constructors ---------- #

        def __init__(self, dictionary: SortedDictionary[TKey, TValue]): ...

        # ---------- Properties ---------- #

        @property
        def Count(self) -> IntType: ...

        # ---------- Methods ---------- #

        def CopyTo(self, array: ArrayType[TValue], index: IntType) -> VoidType: ...
        def GetEnumerator(self) -> Enumerator[TKey, TValue]: ...
        def get_Count(self) -> IntType: ...

        # No Events

        # No Sub Classes

        # ---------- Sub Structs ---------- #

        class Enumerator(
            Generic[TKey, TValue], ValueType, IEnumerator[TValue], IDisposable, IEnumerator
        ):
            # No Fields

            # No Constructors

            # ---------- Properties ---------- #

            @property
            def Current(self) -> TValue: ...

            # ---------- Methods ---------- #

            def Dispose(self) -> VoidType: ...
            def MoveNext(self) -> BooleanType: ...
            def get_Current(self) -> TValue: ...

            # No Events

            # No Sub Classes

            # No Sub Structs

            # No Sub Interfaces

            # No Sub Enums
        # No Sub Interfaces

        # No Sub Enums
    # ---------- Sub Structs ---------- #

    class Enumerator(
        Generic[TKey, TValue],
        ValueType,
        IEnumerator[KeyValuePair[TKey, TValue]],
        IDisposable,
        IEnumerator,
        IDictionaryEnumerator,
    ):
        # No Fields

        # No Constructors

        # ---------- Properties ---------- #

        @property
        def Current(self) -> KeyValuePair[TKey, TValue]: ...

        # ---------- Methods ---------- #

        def Dispose(self) -> VoidType: ...
        def MoveNext(self) -> BooleanType: ...
        def get_Current(self) -> KeyValuePair[TKey, TValue]: ...

        # No Events

        # No Sub Classes

        # No Sub Structs

        # No Sub Interfaces

        # No Sub Enums
    # No Sub Interfaces

    # No Sub Enums

class SortedList(
    Generic[TKey, TValue],
    ObjectType,
    IDictionary[TKey, TValue],
    ICollection[KeyValuePair[TKey, TValue]],
    IEnumerable[KeyValuePair[TKey, TValue]],
    IEnumerable,
    IDictionary,
    ICollection,
    IReadOnlyDictionary[TKey, TValue],
    IReadOnlyCollection[KeyValuePair[TKey, TValue]],
):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, capacity: IntType): ...
    @overload
    def __init__(self, comparer: IComparer[TKey]): ...
    @overload
    def __init__(self, capacity: IntType, comparer: IComparer[TKey]): ...
    @overload
    def __init__(self, dictionary: IDictionary[TKey, TValue]): ...
    @overload
    def __init__(self, dictionary: IDictionary[TKey, TValue], comparer: IComparer[TKey]): ...

    # ---------- Properties ---------- #

    @property
    def Capacity(self) -> IntType: ...
    @Capacity.setter
    def Capacity(self, value: IntType) -> None: ...
    @property
    def Comparer(self) -> IComparer[TKey]: ...
    @property
    def Count(self) -> IntType: ...
    def __getitem__(self, key: TKey) -> TValue: ...
    def __setitem__(self, key: TKey, value: TValue) -> None: ...
    @property
    def Keys(self) -> IList[TKey]: ...
    @property
    def Values(self) -> IList[TValue]: ...

    # ---------- Methods ---------- #

    def Add(self, key: TKey, value: TValue) -> VoidType: ...
    def Clear(self) -> VoidType: ...
    def ContainsKey(self, key: TKey) -> BooleanType: ...
    def ContainsValue(self, value: TValue) -> BooleanType: ...
    def GetEnumerator(self) -> IEnumerator[KeyValuePair[TKey, TValue]]: ...
    def IndexOfKey(self, key: TKey) -> IntType: ...
    def IndexOfValue(self, value: TValue) -> IntType: ...
    def Remove(self, key: TKey) -> BooleanType: ...
    def RemoveAt(self, index: IntType) -> VoidType: ...
    def TrimExcess(self) -> VoidType: ...
    def TryGetValue(self, key: TKey, value: TValue) -> Tuple[BooleanType, TValue]: ...
    def get_Capacity(self) -> IntType: ...
    def get_Comparer(self) -> IComparer[TKey]: ...
    def get_Count(self) -> IntType: ...
    def get_Item(self, key: TKey) -> TValue: ...
    def get_Keys(self) -> IList[TKey]: ...
    def get_Values(self) -> IList[TValue]: ...
    def set_Capacity(self, value: IntType) -> VoidType: ...
    def set_Item(self, key: TKey, value: TValue) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SortedSet(
    Generic[T],
    ObjectType,
    ISet[T],
    ICollection[T],
    IEnumerable[T],
    IEnumerable,
    ICollection,
    ISerializable,
    IDeserializationCallback,
    IReadOnlyCollection[T],
):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, comparer: IComparer[T]): ...
    @overload
    def __init__(self, collection: IEnumerable[T]): ...
    @overload
    def __init__(self, collection: IEnumerable[T], comparer: IComparer[T]): ...

    # ---------- Properties ---------- #

    @property
    def Comparer(self) -> IComparer[T]: ...
    @property
    def Count(self) -> IntType: ...
    @property
    def Max(self) -> T: ...
    @property
    def Min(self) -> T: ...

    # ---------- Methods ---------- #

    def Add(self, item: T) -> BooleanType: ...
    def Clear(self) -> VoidType: ...
    def Contains(self, item: T) -> BooleanType: ...
    @overload
    def CopyTo(self, array: ArrayType[T]) -> VoidType: ...
    @overload
    def CopyTo(self, array: ArrayType[T], index: IntType) -> VoidType: ...
    @overload
    def CopyTo(self, array: ArrayType[T], index: IntType, count: IntType) -> VoidType: ...
    @staticmethod
    @overload
    def CreateSetComparer() -> IEqualityComparer[SortedSet[T]]: ...
    @staticmethod
    @overload
    def CreateSetComparer(
        memberEqualityComparer: IEqualityComparer[T],
    ) -> IEqualityComparer[SortedSet[T]]: ...
    def ExceptWith(self, other: IEnumerable[T]) -> VoidType: ...
    def GetEnumerator(self) -> Enumerator[T]: ...
    def GetViewBetween(self, lowerValue: T, upperValue: T) -> SortedSet[T]: ...
    def IntersectWith(self, other: IEnumerable[T]) -> VoidType: ...
    def IsProperSubsetOf(self, other: IEnumerable[T]) -> BooleanType: ...
    def IsProperSupersetOf(self, other: IEnumerable[T]) -> BooleanType: ...
    def IsSubsetOf(self, other: IEnumerable[T]) -> BooleanType: ...
    def IsSupersetOf(self, other: IEnumerable[T]) -> BooleanType: ...
    def Overlaps(self, other: IEnumerable[T]) -> BooleanType: ...
    def Remove(self, item: T) -> BooleanType: ...
    def RemoveWhere(self, match: Predicate[T]) -> IntType: ...
    def Reverse(self) -> IEnumerable[T]: ...
    def SetEquals(self, other: IEnumerable[T]) -> BooleanType: ...
    def SymmetricExceptWith(self, other: IEnumerable[T]) -> VoidType: ...
    def TryGetValue(self, equalValue: T, actualValue: T) -> Tuple[BooleanType, T]: ...
    def UnionWith(self, other: IEnumerable[T]) -> VoidType: ...
    def get_Comparer(self) -> IComparer[T]: ...
    def get_Count(self) -> IntType: ...
    def get_Max(self) -> T: ...
    def get_Min(self) -> T: ...

    # No Events

    # No Sub Classes

    # ---------- Sub Structs ---------- #

    class Enumerator(
        Generic[T],
        ValueType,
        IEnumerator[T],
        IDisposable,
        IEnumerator,
        ISerializable,
        IDeserializationCallback,
    ):
        # No Fields

        # No Constructors

        # ---------- Properties ---------- #

        @property
        def Current(self) -> T: ...

        # ---------- Methods ---------- #

        def Dispose(self) -> VoidType: ...
        def MoveNext(self) -> BooleanType: ...
        def get_Current(self) -> T: ...

        # No Events

        # No Sub Classes

        # No Sub Structs

        # No Sub Interfaces

        # No Sub Enums
    # No Sub Interfaces

    # No Sub Enums

class SortedSetDebugView(Generic[T], ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, set: SortedSet[T]): ...

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

class SortedSetEqualityComparer(Generic[T], ObjectType, IEqualityComparer[SortedSet[T]]):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, comparer: IComparer[T]): ...
    @overload
    def __init__(self, memberEqualityComparer: IEqualityComparer[T]): ...
    @overload
    def __init__(self, comparer: IComparer[T], memberEqualityComparer: IEqualityComparer[T]): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def Equals(self, x: SortedSet[T], y: SortedSet[T]) -> BooleanType: ...
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    @overload
    def GetHashCode(self, obj: SortedSet[T]) -> IntType: ...
    @overload
    def GetHashCode(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Stack(
    Generic[T], ObjectType, IEnumerable[T], IEnumerable, ICollection, IReadOnlyCollection[T]
):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, capacity: IntType): ...
    @overload
    def __init__(self, collection: IEnumerable[T]): ...

    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...

    # ---------- Methods ---------- #

    def Clear(self) -> VoidType: ...
    def Contains(self, item: T) -> BooleanType: ...
    def CopyTo(self, array: ArrayType[T], arrayIndex: IntType) -> VoidType: ...
    def GetEnumerator(self) -> Enumerator[T]: ...
    def Peek(self) -> T: ...
    def Pop(self) -> T: ...
    def Push(self, item: T) -> VoidType: ...
    def ToArray(self) -> ArrayType[T]: ...
    def TrimExcess(self) -> VoidType: ...
    def get_Count(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # ---------- Sub Structs ---------- #

    class Enumerator(Generic[T], ValueType, IEnumerator[T], IDisposable, IEnumerator):
        # No Fields

        # No Constructors

        # ---------- Properties ---------- #

        @property
        def Current(self) -> T: ...

        # ---------- Methods ---------- #

        def Dispose(self) -> VoidType: ...
        def MoveNext(self) -> BooleanType: ...
        def get_Current(self) -> T: ...

        # No Events

        # No Sub Classes

        # No Sub Structs

        # No Sub Interfaces

        # No Sub Enums
    # No Sub Interfaces

    # No Sub Enums

class System_CollectionDebugView(Generic[T], ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, collection: ICollection[T]): ...

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

class System_DictionaryDebugView(Generic[K, V], ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, dictionary: IDictionary[K, V]): ...

    # ---------- Properties ---------- #

    @property
    def Items(self) -> ArrayType[KeyValuePair[K, V]]: ...

    # ---------- Methods ---------- #

    def get_Items(self) -> ArrayType[KeyValuePair[K, V]]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class System_DictionaryKeyCollectionDebugView(Generic[TKey, TValue], ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, collection: ICollection[TKey]): ...

    # ---------- Properties ---------- #

    @property
    def Items(self) -> ArrayType[TKey]: ...

    # ---------- Methods ---------- #

    def get_Items(self) -> ArrayType[TKey]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class System_DictionaryValueCollectionDebugView(Generic[TKey, TValue], ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, collection: ICollection[TValue]): ...

    # ---------- Properties ---------- #

    @property
    def Items(self) -> ArrayType[TValue]: ...

    # ---------- Methods ---------- #

    def get_Items(self) -> ArrayType[TValue]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class System_QueueDebugView(Generic[T], ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, queue: Queue[T]): ...

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

class System_StackDebugView(Generic[T], ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, stack: Stack[T]): ...

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

class TreeSet(
    Generic[T],
    SortedSet[T],
    ISet[T],
    ICollection[T],
    IEnumerable[T],
    IEnumerable,
    ICollection,
    ISerializable,
    IDeserializationCallback,
    IReadOnlyCollection[T],
):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, comparer: IComparer[T]): ...
    @overload
    def __init__(self, collection: ICollection[T]): ...
    @overload
    def __init__(self, collection: ICollection[T], comparer: IComparer[T]): ...
    @overload
    def __init__(self, siInfo: SerializationInfo, context: StreamingContext): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TreeWalkPredicate(Generic[T], MulticastDelegate, ICloneable, ISerializable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, object: ObjectType, method: NIntType): ...

    # No Properties

    # ---------- Methods ---------- #

    def BeginInvoke(
        self, node: Node[T], callback: AsyncCallback, object: ObjectType
    ) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> BooleanType: ...
    def Invoke(self, node: Node[T]) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# ---------- Structs ---------- #

class ArrayBuilder(Generic[T], ValueType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, capacity: IntType): ...

    # ---------- Properties ---------- #

    @property
    def Capacity(self) -> IntType: ...
    @property
    def Count(self) -> IntType: ...
    def __getitem__(self, key: IntType) -> T: ...
    def __setitem__(self, key: IntType, value: T) -> None: ...

    # ---------- Methods ---------- #

    def Add(self, item: T) -> VoidType: ...
    def First(self) -> T: ...
    def Last(self) -> T: ...
    def ToArray(self) -> ArrayType[T]: ...
    def UncheckedAdd(self, item: T) -> VoidType: ...
    def get_Capacity(self) -> IntType: ...
    def get_Count(self) -> IntType: ...
    def get_Item(self, index: IntType) -> T: ...
    def set_Item(self, index: IntType, value: T) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CopyPosition(ValueType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @staticmethod
    @property
    def Start() -> CopyPosition: ...

    # ---------- Methods ---------- #

    @staticmethod
    def get_Start() -> CopyPosition: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class KeyValuePair(Generic[TKey, TValue], ValueType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, key: TKey, value: TValue): ...

    # ---------- Properties ---------- #

    @property
    def Key(self) -> TKey: ...
    @property
    def Value(self) -> TValue: ...

    # ---------- Methods ---------- #

    def ToString(self) -> StringType: ...
    def get_Key(self) -> TKey: ...
    def get_Value(self) -> TValue: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class LargeArrayBuilder(Generic[T], ValueType):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, initialize: BooleanType): ...
    @overload
    def __init__(self, maxCapacity: IntType): ...

    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...

    # ---------- Methods ---------- #

    def Add(self, item: T) -> VoidType: ...
    def AddRange(self, items: IEnumerable[T]) -> VoidType: ...
    @overload
    def CopyTo(self, array: ArrayType[T], arrayIndex: IntType, count: IntType) -> VoidType: ...
    @overload
    def CopyTo(
        self, position: CopyPosition, array: ArrayType[T], arrayIndex: IntType, count: IntType
    ) -> CopyPosition: ...
    def GetBuffer(self, index: IntType) -> ArrayType[T]: ...
    def SlowAdd(self, item: T) -> VoidType: ...
    def ToArray(self) -> ArrayType[T]: ...
    def TryMove(self, array: T) -> Tuple[BooleanType, T]: ...
    def get_Count(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Marker(ValueType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, count: IntType, index: IntType): ...

    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...
    @property
    def Index(self) -> IntType: ...

    # ---------- Methods ---------- #

    def get_Count(self) -> IntType: ...
    def get_Index(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SparseArrayBuilder(Generic[T], ValueType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, initialize: BooleanType): ...

    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...
    @property
    def Markers(self) -> ArrayBuilder[Marker]: ...

    # ---------- Methods ---------- #

    def Add(self, item: T) -> VoidType: ...
    def AddRange(self, items: IEnumerable[T]) -> VoidType: ...
    def CopyTo(self, array: ArrayType[T], arrayIndex: IntType, count: IntType) -> VoidType: ...
    def Reserve(self, count: IntType) -> VoidType: ...
    def ReserveOrAdd(self, items: IEnumerable[T]) -> BooleanType: ...
    def ToArray(self) -> ArrayType[T]: ...
    def get_Count(self) -> IntType: ...
    def get_Markers(self) -> ArrayBuilder[Marker]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# ---------- Interfaces ---------- #

class IArraySortHelper(Protocol[TKey]):
    # No Properties

    # ---------- Methods ---------- #

    def BinarySearch(
        self,
        keys: ArrayType[TKey],
        index: IntType,
        length: IntType,
        value: TKey,
        comparer: IComparer[TKey],
    ) -> IntType: ...
    def Sort(
        self, keys: ArrayType[TKey], index: IntType, length: IntType, comparer: IComparer[TKey]
    ) -> VoidType: ...

    # No Events

class IArraySortHelper(Protocol[TKey, TValue]):
    # No Properties

    # ---------- Methods ---------- #

    def Sort(
        self,
        keys: ArrayType[TKey],
        values: ArrayType[TValue],
        index: IntType,
        length: IntType,
        comparer: IComparer[TKey],
    ) -> VoidType: ...

    # No Events

class ICollection(Protocol[T], IEnumerable[T], IEnumerable):
    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...
    @property
    def IsReadOnly(self) -> BooleanType: ...

    # ---------- Methods ---------- #

    def Add(self, item: T) -> VoidType: ...
    def Clear(self) -> VoidType: ...
    def Contains(self, item: T) -> BooleanType: ...
    def CopyTo(self, array: ArrayType[T], arrayIndex: IntType) -> VoidType: ...
    def Remove(self, item: T) -> BooleanType: ...
    def get_Count(self) -> IntType: ...
    def get_IsReadOnly(self) -> BooleanType: ...

    # No Events

class IComparer(Protocol[T]):
    # No Properties

    # ---------- Methods ---------- #

    def Compare(self, x: T, y: T) -> IntType: ...

    # No Events

class IDictionary(
    Protocol[TKey, TValue],
    ICollection[KeyValuePair[TKey, TValue]],
    IEnumerable[KeyValuePair[TKey, TValue]],
    IEnumerable,
):
    # ---------- Properties ---------- #

    def __getitem__(self, key: TKey) -> TValue: ...
    def __setitem__(self, key: TKey, value: TValue) -> None: ...
    @property
    def Keys(self) -> ICollection[TKey]: ...
    @property
    def Values(self) -> ICollection[TValue]: ...

    # ---------- Methods ---------- #

    def Add(self, key: TKey, value: TValue) -> VoidType: ...
    def ContainsKey(self, key: TKey) -> BooleanType: ...
    def Remove(self, key: TKey) -> BooleanType: ...
    def TryGetValue(self, key: TKey, value: TValue) -> Tuple[BooleanType, TValue]: ...
    def get_Item(self, key: TKey) -> TValue: ...
    def get_Keys(self) -> ICollection[TKey]: ...
    def get_Values(self) -> ICollection[TValue]: ...
    def set_Item(self, key: TKey, value: TValue) -> VoidType: ...

    # No Events

class IEnumerable(Protocol[T], IEnumerable):
    # No Properties

    # ---------- Methods ---------- #

    def GetEnumerator(self) -> IEnumerator[T]: ...

    # No Events

class IEnumerator(Protocol[T], IDisposable, IEnumerator):
    # ---------- Properties ---------- #

    @property
    def Current(self) -> T: ...

    # ---------- Methods ---------- #

    def get_Current(self) -> T: ...

    # No Events

class IEqualityComparer(Protocol[T]):
    # No Properties

    # ---------- Methods ---------- #

    def Equals(self, x: T, y: T) -> BooleanType: ...
    def GetHashCode(self, obj: T) -> IntType: ...

    # No Events

class IList(Protocol[T], ICollection[T], IEnumerable[T], IEnumerable):
    # ---------- Properties ---------- #

    def __getitem__(self, key: IntType) -> T: ...
    def __setitem__(self, key: IntType, value: T) -> None: ...

    # ---------- Methods ---------- #

    def IndexOf(self, item: T) -> IntType: ...
    def Insert(self, index: IntType, item: T) -> VoidType: ...
    def RemoveAt(self, index: IntType) -> VoidType: ...
    def get_Item(self, index: IntType) -> T: ...
    def set_Item(self, index: IntType, value: T) -> VoidType: ...

    # No Events

class IReadOnlyCollection(Protocol[T], IEnumerable[T], IEnumerable):
    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...

    # ---------- Methods ---------- #

    def get_Count(self) -> IntType: ...

    # No Events

class IReadOnlyDictionary(
    Protocol[TKey, TValue],
    IReadOnlyCollection[KeyValuePair[TKey, TValue]],
    IEnumerable[KeyValuePair[TKey, TValue]],
    IEnumerable,
):
    # ---------- Properties ---------- #

    def __getitem__(self, key: TKey) -> TValue: ...
    @property
    def Keys(self) -> IEnumerable[TKey]: ...
    @property
    def Values(self) -> IEnumerable[TValue]: ...

    # ---------- Methods ---------- #

    def ContainsKey(self, key: TKey) -> BooleanType: ...
    def TryGetValue(self, key: TKey, value: TValue) -> Tuple[BooleanType, TValue]: ...
    def get_Item(self, key: TKey) -> TValue: ...
    def get_Keys(self) -> IEnumerable[TKey]: ...
    def get_Values(self) -> IEnumerable[TValue]: ...

    # No Events

class IReadOnlyList(Protocol[T], IReadOnlyCollection[T], IEnumerable[T], IEnumerable):
    # ---------- Properties ---------- #

    def __getitem__(self, key: IntType) -> T: ...

    # ---------- Methods ---------- #

    def get_Item(self, index: IntType) -> T: ...

    # No Events

class ISet(Protocol[T], ICollection[T], IEnumerable[T], IEnumerable):
    # No Properties

    # ---------- Methods ---------- #

    def Add(self, item: T) -> BooleanType: ...
    def ExceptWith(self, other: IEnumerable[T]) -> VoidType: ...
    def IntersectWith(self, other: IEnumerable[T]) -> VoidType: ...
    def IsProperSubsetOf(self, other: IEnumerable[T]) -> BooleanType: ...
    def IsProperSupersetOf(self, other: IEnumerable[T]) -> BooleanType: ...
    def IsSubsetOf(self, other: IEnumerable[T]) -> BooleanType: ...
    def IsSupersetOf(self, other: IEnumerable[T]) -> BooleanType: ...
    def Overlaps(self, other: IEnumerable[T]) -> BooleanType: ...
    def SetEquals(self, other: IEnumerable[T]) -> BooleanType: ...
    def SymmetricExceptWith(self, other: IEnumerable[T]) -> VoidType: ...
    def UnionWith(self, other: IEnumerable[T]) -> VoidType: ...

    # No Events

# ---------- Enums ---------- #

class TreeRotation(Enum):
    LeftRotation = 1
    RightRotation = 2
    RightLeftRotation = 3
    LeftRightRotation = 4

# ---------- Delegates ---------- #

TreeWalkPredicate = Callable[[Node[T]], BooleanType]

__all__ = [
    ArraySortHelper,
    BitHelper,
    ByteEqualityComparer,
    Comparer,
    ComparisonComparer,
    Dictionary,
    EnumEqualityComparer,
    EnumerableHelpers,
    EqualityComparer,
    GenericArraySortHelper,
    GenericComparer,
    GenericEqualityComparer,
    HashSet,
    HashSetDebugView,
    HashSetEqualityComparer,
    IntrospectiveSortUtilities,
    KeyNotFoundException,
    LinkedList,
    LinkedListNode,
    List,
    LongEnumEqualityComparer,
    Mscorlib_CollectionDebugView,
    Mscorlib_DictionaryDebugView,
    Mscorlib_DictionaryKeyCollectionDebugView,
    Mscorlib_DictionaryValueCollectionDebugView,
    Mscorlib_KeyedCollectionDebugView,
    NullableComparer,
    NullableEqualityComparer,
    ObjectComparer,
    ObjectEqualityComparer,
    Queue,
    RandomizedObjectEqualityComparer,
    RandomizedStringEqualityComparer,
    SByteEnumEqualityComparer,
    ShortEnumEqualityComparer,
    SortedDictionary,
    SortedList,
    SortedSet,
    SortedSetDebugView,
    SortedSetEqualityComparer,
    Stack,
    System_CollectionDebugView,
    System_DictionaryDebugView,
    System_DictionaryKeyCollectionDebugView,
    System_DictionaryValueCollectionDebugView,
    System_QueueDebugView,
    System_StackDebugView,
    TreeSet,
    TreeWalkPredicate,
    ArrayBuilder,
    CopyPosition,
    KeyValuePair,
    LargeArrayBuilder,
    Marker,
    SparseArrayBuilder,
    IArraySortHelper,
    ICollection,
    IComparer,
    IDictionary,
    IEnumerable,
    IEnumerator,
    IEqualityComparer,
    IList,
    IReadOnlyCollection,
    IReadOnlyDictionary,
    IReadOnlyList,
    ISet,
    TreeRotation,
    TreeWalkPredicate,
]
