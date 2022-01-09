from __future__ import annotations

from abc import ABC
from typing import Generic, List, Optional, Protocol, Tuple, TypeVar, Union, overload

from System import Action, Array, Boolean, Byte, Comparison, Converter, Exception, IDisposable, IWellKnownStringEqualityComparer, Int32, Nullable, Object, Predicate, String, SystemException, ValueType, Void
from System.Collections import IDictionaryEnumerator
from System.Collections.ObjectModel import KeyedCollection, ReadOnlyCollection
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import IDeserializationCallback, ISerializable, SerializationInfo, StreamingContext

# ---------- Types ---------- #

K = TypeVar('K')
T = TypeVar('T')
TKey = TypeVar('TKey')
TOutput = TypeVar('TOutput')
TValue = TypeVar('TValue')
V = TypeVar('V')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
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
    
    def BinarySearch(self, array: ArrayType[T], index: IntType, length: IntType, value: T, comparer: IComparer[T]) -> IntType: ...
    
    def Sort(self, keys: ArrayType[T], index: IntType, length: IntType, comparer: IComparer[T]) -> VoidType: ...
    
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
    
    def Sort(self, keys: ArrayType[TKey], values: ArrayType[TValue], index: IntType, length: IntType, comparer: IComparer[TKey]) -> VoidType: ...
    
    @staticmethod
    def get_Default() -> IArraySortHelper[TKey, TValue]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ByteEqualityComparer(EqualityComparer[ByteType], IEqualityComparer, IEqualityComparer[ByteType]):
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


class Dictionary(Generic[TKey, TValue], ObjectType, IDictionary[TKey, TValue], ICollection[KeyValuePair[TKey, TValue]], IEnumerable[KeyValuePair[TKey, TValue]], IEnumerable, IDictionary, ICollection, IReadOnlyDictionary[TKey, TValue], IReadOnlyCollection[KeyValuePair[TKey, TValue]], ISerializable, IDeserializationCallback):
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
    def __init__(self, dictionary: IDictionary[TKey, TValue], comparer: IEqualityComparer[TKey]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Comparer(self) -> IEqualityComparer[TKey]: ...
    
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
    
    class KeyCollection(Generic[TKey, TValue], ObjectType, ICollection[TKey], IEnumerable[TKey], IEnumerable, ICollection, IReadOnlyCollection[TKey]):
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


class EnumEqualityComparer(Generic[T], EqualityComparer[T], IEqualityComparer, IEqualityComparer[T], ISerializable):
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
    
    def BinarySearch(self, array: ArrayType[T], index: IntType, length: IntType, value: T, comparer: IComparer[T]) -> IntType: ...
    
    def Sort(self, keys: ArrayType[T], index: IntType, length: IntType, comparer: IComparer[T]) -> VoidType: ...
    
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
    
    def Sort(self, keys: ArrayType[TKey], values: ArrayType[TValue], index: IntType, length: IntType, comparer: IComparer[TKey]) -> VoidType: ...
    
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


class GenericEqualityComparer(Generic[T], EqualityComparer[T], IEqualityComparer, IEqualityComparer[T]):
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


class List(Generic[T], ObjectType, IList[T], ICollection[T], IEnumerable[T], IEnumerable, IList, ICollection, IReadOnlyList[T], IReadOnlyCollection[T]):
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
    
    @property
    def Item(self) -> T: ...
    
    @Item.setter
    def Item(self, value: T) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, item: T) -> VoidType: ...
    
    def AddRange(self, collection: IEnumerable[T]) -> VoidType: ...
    
    def AsReadOnly(self) -> ReadOnlyCollection[T]: ...
    
    @overload
    def BinarySearch(self, index: IntType, count: IntType, item: T, comparer: IComparer[T]) -> IntType: ...
    
    @overload
    def BinarySearch(self, item: T) -> IntType: ...
    
    @overload
    def BinarySearch(self, item: T, comparer: IComparer[T]) -> IntType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, item: T) -> BooleanType: ...
    
    def ConvertAll(self, converter: Converter[T, TOutput]) -> List[TOutput]: ...
    
    @overload
    def CopyTo(self, index: IntType, array: ArrayType[T], arrayIndex: IntType, count: IntType) -> VoidType: ...
    
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
    def FindLastIndex(self, startIndex: IntType, count: IntType, match: Predicate[T]) -> IntType: ...
    
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


class LongEnumEqualityComparer(Generic[T], EqualityComparer[T], IEqualityComparer, IEqualityComparer[T], ISerializable):
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


class NullableComparer(Generic[T], Comparer[NullableType[Nullable[T]]], IComparer, IComparer[NullableType[Nullable[T]]]):
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


class NullableEqualityComparer(Generic[T], EqualityComparer[NullableType[Nullable[T]]], IEqualityComparer, IEqualityComparer[NullableType[Nullable[T]]]):
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


class ObjectEqualityComparer(Generic[T], EqualityComparer[T], IEqualityComparer, IEqualityComparer[T]):
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


class RandomizedObjectEqualityComparer(ObjectType, IEqualityComparer, IWellKnownStringEqualityComparer):
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


class RandomizedStringEqualityComparer(ObjectType, IEqualityComparer[StringType], IEqualityComparer, IWellKnownStringEqualityComparer):
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


class SByteEnumEqualityComparer(Generic[T], EnumEqualityComparer[T], IEqualityComparer, IEqualityComparer[T], ISerializable):
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


class ShortEnumEqualityComparer(Generic[T], EnumEqualityComparer[T], IEqualityComparer, IEqualityComparer[T], ISerializable):
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


# ---------- Structs ---------- #

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


# ---------- Interfaces ---------- #

class IArraySortHelper(Protocol[TKey]):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BinarySearch(self, keys: ArrayType[TKey], index: IntType, length: IntType, value: TKey, comparer: IComparer[TKey]) -> IntType: ...
    
    def Sort(self, keys: ArrayType[TKey], index: IntType, length: IntType, comparer: IComparer[TKey]) -> VoidType: ...
    
    # No Events


class IArraySortHelper(Protocol[TKey, TValue]):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Sort(self, keys: ArrayType[TKey], values: ArrayType[TValue], index: IntType, length: IntType, comparer: IComparer[TKey]) -> VoidType: ...
    
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


class IDictionary(Protocol[TKey, TValue], ICollection[KeyValuePair[TKey, TValue]], IEnumerable[KeyValuePair[TKey, TValue]], IEnumerable):
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> TValue: ...
    
    @Item.setter
    def Item(self, value: TValue) -> None: ...
    
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
    
    @property
    def Item(self) -> T: ...
    
    @Item.setter
    def Item(self, value: T) -> None: ...
    
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


class IReadOnlyDictionary(Protocol[TKey, TValue], IReadOnlyCollection[KeyValuePair[TKey, TValue]], IEnumerable[KeyValuePair[TKey, TValue]], IEnumerable):
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> TValue: ...
    
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
    
    @property
    def Item(self) -> T: ...
    
    # ---------- Methods ---------- #
    
    def get_Item(self, index: IntType) -> T: ...
    
    # No Events


# No Enums

# No Delegates

__all__ = [
    ArraySortHelper,
    ByteEqualityComparer,
    Comparer,
    ComparisonComparer,
    Dictionary,
    EnumEqualityComparer,
    EqualityComparer,
    GenericArraySortHelper,
    GenericComparer,
    GenericEqualityComparer,
    IntrospectiveSortUtilities,
    KeyNotFoundException,
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
    RandomizedObjectEqualityComparer,
    RandomizedStringEqualityComparer,
    SByteEnumEqualityComparer,
    ShortEnumEqualityComparer,
    KeyValuePair,
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
]
