from __future__ import annotations

from abc import ABC
from typing import Generic, List, Protocol, Tuple, TypeVar, Union, overload

from System import Array, Boolean, Int32, Object, Void
from System.Collections import ICollection, IDictionary, IEnumerable, IList
from System.Collections.Generic import ICollection, IDictionary, IEnumerable, IEnumerator, IEqualityComparer, IList, IReadOnlyCollection, IReadOnlyDictionary, IReadOnlyList, KeyValuePair

# ---------- Types ---------- #

T = TypeVar('T')
TItem = TypeVar('TItem')
TKey = TypeVar('TKey')
TValue = TypeVar('TValue')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
ObjectType = Object
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class Collection(Generic[T], ObjectType, IList[T], ICollection[T], IEnumerable[T], IEnumerable, IList, ICollection, IReadOnlyList[T], IReadOnlyCollection[T]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, list: IList[T]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Item(self) -> T: ...
    
    @Item.setter
    def Item(self, value: T) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, item: T) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, item: T) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[T], index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[T]: ...
    
    def IndexOf(self, item: T) -> IntType: ...
    
    def Insert(self, index: IntType, item: T) -> VoidType: ...
    
    def Remove(self, item: T) -> BooleanType: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Item(self, index: IntType) -> T: ...
    
    def set_Item(self, index: IntType, value: T) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class KeyedCollection(Protocol[TKey, TItem], Collection[TItem], IList[TItem], ICollection[TItem], IEnumerable[TItem], IEnumerable, IList, ICollection, IReadOnlyList[TItem], IReadOnlyCollection[TItem]):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Comparer(self) -> IEqualityComparer[TKey]: ...
    
    @property
    def Item(self) -> TItem: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Contains(self, key: TKey) -> BooleanType: ...
    
    @overload
    def Remove(self, key: TKey) -> BooleanType: ...
    
    def get_Comparer(self) -> IEqualityComparer[TKey]: ...
    
    @overload
    def get_Item(self, key: TKey) -> TItem: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReadOnlyCollection(Generic[T], ObjectType, IList[T], ICollection[T], IEnumerable[T], IEnumerable, IList, ICollection, IReadOnlyList[T], IReadOnlyCollection[T]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, list: IList[T]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Item(self) -> T: ...
    
    # ---------- Methods ---------- #
    
    def Contains(self, value: T) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[T], index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[T]: ...
    
    def IndexOf(self, value: T) -> IntType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Item(self, index: IntType) -> T: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReadOnlyDictionary(Generic[TKey, TValue], ObjectType, IDictionary[TKey, TValue], ICollection[KeyValuePair[TKey, TValue]], IEnumerable[KeyValuePair[TKey, TValue]], IEnumerable, IDictionary, ICollection, IReadOnlyDictionary[TKey, TValue], IReadOnlyCollection[KeyValuePair[TKey, TValue]]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, dictionary: IDictionary[TKey, TValue]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Item(self) -> TValue: ...
    
    @property
    def Keys(self) -> KeyCollection[TKey, TValue]: ...
    
    @property
    def Values(self) -> ValueCollection[TKey, TValue]: ...
    
    # ---------- Methods ---------- #
    
    def ContainsKey(self, key: TKey) -> BooleanType: ...
    
    def GetEnumerator(self) -> IEnumerator[KeyValuePair[TKey, TValue]]: ...
    
    def TryGetValue(self, key: TKey, value: TValue) -> Tuple[BooleanType, TValue]: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Item(self, key: TKey) -> TValue: ...
    
    def get_Keys(self) -> KeyCollection[TKey, TValue]: ...
    
    def get_Values(self) -> ValueCollection[TKey, TValue]: ...
    
    # No Events
    
    
    # ---------- Sub Classes ---------- #
    
    class KeyCollection(Generic[TKey, TValue], ObjectType, ICollection[TKey], IEnumerable[TKey], IEnumerable, ICollection, IReadOnlyCollection[TKey]):
        # No Fields
        
        # No Constructors
        
        # ---------- Properties ---------- #
        
        @property
        def Count(self) -> IntType: ...
        
        # ---------- Methods ---------- #
        
        def CopyTo(self, array: ArrayType[TKey], arrayIndex: IntType) -> VoidType: ...
        
        def GetEnumerator(self) -> IEnumerator[TKey]: ...
        
        def get_Count(self) -> IntType: ...
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    class ValueCollection(Generic[TKey, TValue], ObjectType, ICollection[TValue], IEnumerable[TValue], IEnumerable, ICollection, IReadOnlyCollection[TValue]):
        # No Fields
        
        # No Constructors
        
        # ---------- Properties ---------- #
        
        @property
        def Count(self) -> IntType: ...
        
        # ---------- Methods ---------- #
        
        def CopyTo(self, array: ArrayType[TValue], arrayIndex: IntType) -> VoidType: ...
        
        def GetEnumerator(self) -> IEnumerator[TValue]: ...
        
        def get_Count(self) -> IntType: ...
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReadOnlyDictionaryHelpers(ABC, ObjectType):
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


# No Structs

# No Interfaces

# No Enums

# No Delegates

__all__ = [
    Collection,
    KeyedCollection,
    ReadOnlyCollection,
    ReadOnlyDictionary,
    ReadOnlyDictionaryHelpers,
]
