from __future__ import annotations

from typing import Callable, Generic, List, Protocol, Tuple, TypeVar, Union, overload

from System import Array, AsyncCallback, Boolean, Enum, IAsyncResult, ICloneable, IDisposable, Int32, IntPtr, MulticastDelegate, Object, Predicate, ValueType, Void
from System.Collections import ICollection, IDictionary, IDictionaryEnumerator, IEnumerable, IEnumerator
from System.Collections.Generic import ICollection, IComparer, IDictionary, IEnumerable, IEnumerator, IEqualityComparer, IList, IReadOnlyCollection, IReadOnlyDictionary, KeyValuePair
from System.Runtime.Serialization import IDeserializationCallback, ISerializable, SerializationInfo, StreamingContext

# ---------- Types ---------- #

K = TypeVar('K')
T = TypeVar('T')
TKey = TypeVar('TKey')
TValue = TypeVar('TValue')
V = TypeVar('V')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
NIntType = Union[int, IntPtr]
ObjectType = Object
VoidType = Union[None, Void]

# ---------- Classes ---------- #

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


class LinkedList(Generic[T], ObjectType, ICollection[T], IEnumerable[T], IEnumerable, ICollection, IReadOnlyCollection[T], ISerializable, IDeserializationCallback):
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
    
    class Enumerator(Generic[T], ValueType, IEnumerator[T], IDisposable, IEnumerator, ISerializable, IDeserializationCallback):
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


class Queue(Generic[T], ObjectType, IEnumerable[T], IEnumerable, ICollection, IReadOnlyCollection[T]):
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


class SortedDictionary(Generic[TKey, TValue], ObjectType, IDictionary[TKey, TValue], ICollection[KeyValuePair[TKey, TValue]], IEnumerable[KeyValuePair[TKey, TValue]], IEnumerable, IDictionary, ICollection, IReadOnlyDictionary[TKey, TValue], IReadOnlyCollection[KeyValuePair[TKey, TValue]]):
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
    
    @property
    def Item(self) -> TValue: ...
    
    @Item.setter
    def Item(self, value: TValue) -> None: ...
    
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
    
    class KeyCollection(Generic[TKey, TValue], ObjectType, ICollection[TKey], IEnumerable[TKey], IEnumerable, ICollection, IReadOnlyCollection[TKey]):
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
        
        class Enumerator(Generic[TKey, TValue], ValueType, IEnumerator[TKey], IDisposable, IEnumerator):
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
    
    
    class ValueCollection(Generic[TKey, TValue], ObjectType, ICollection[TValue], IEnumerable[TValue], IEnumerable, ICollection, IReadOnlyCollection[TValue]):
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
        
        class Enumerator(Generic[TKey, TValue], ValueType, IEnumerator[TValue], IDisposable, IEnumerator):
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
    
    class Enumerator(Generic[TKey, TValue], ValueType, IEnumerator[KeyValuePair[TKey, TValue]], IDisposable, IEnumerator, IDictionaryEnumerator):
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


class SortedList(Generic[TKey, TValue], ObjectType, IDictionary[TKey, TValue], ICollection[KeyValuePair[TKey, TValue]], IEnumerable[KeyValuePair[TKey, TValue]], IEnumerable, IDictionary, ICollection, IReadOnlyDictionary[TKey, TValue], IReadOnlyCollection[KeyValuePair[TKey, TValue]]):
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
    
    @property
    def Item(self) -> TValue: ...
    
    @Item.setter
    def Item(self, value: TValue) -> None: ...
    
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


class SortedSet(Generic[T], ObjectType, ISet[T], ICollection[T], IEnumerable[T], IEnumerable, ICollection, ISerializable, IDeserializationCallback, IReadOnlyCollection[T]):
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
    def CreateSetComparer(memberEqualityComparer: IEqualityComparer[T]) -> IEqualityComparer[SortedSet[T]]: ...
    
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
    
    class Enumerator(Generic[T], ValueType, IEnumerator[T], IDisposable, IEnumerator, ISerializable, IDeserializationCallback):
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


class Stack(Generic[T], ObjectType, IEnumerable[T], IEnumerable, ICollection, IReadOnlyCollection[T]):
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


class TreeSet(Generic[T], SortedSet[T], ISet[T], ICollection[T], IEnumerable[T], IEnumerable, ICollection, ISerializable, IDeserializationCallback, IReadOnlyCollection[T]):
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
    
    def BeginInvoke(self, node: Node[T], callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> BooleanType: ...
    
    def Invoke(self, node: Node[T]) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# ---------- Interfaces ---------- #

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
    LeftRotation: IntType = 1
    RightRotation: IntType = 2
    RightLeftRotation: IntType = 3
    LeftRightRotation: IntType = 4


# ---------- Delegates ---------- #

TreeWalkPredicate = Callable[[Node[T]], BooleanType]

__all__ = [
    BitHelper,
    LinkedList,
    LinkedListNode,
    Queue,
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
    ISet,
    TreeRotation,
    TreeWalkPredicate,
]
