from __future__ import annotations

from abc import ABC
from typing import Generic, List, Tuple, TypeVar, Union, overload

from System import Array, Boolean, IDisposable, Int32, Object, Predicate, ValueType, Void
from System.Collections import IEnumerable, IEnumerator
from System.Collections.Generic import ICollection, IEnumerable, IEnumerator, IEqualityComparer, IReadOnlyCollection, ISet
from System.Runtime.Serialization import IDeserializationCallback, ISerializable, SerializationInfo, StreamingContext

# ---------- Types ---------- #

T = TypeVar('T')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
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


class HashSet(Generic[T], ObjectType, ICollection[T], IEnumerable[T], IEnumerable, ISerializable, IDeserializationCallback, ISet[T], IReadOnlyCollection[T]):
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
    
    @property
    def Item(self) -> T: ...
    
    @Item.setter
    def Item(self, value: T) -> None: ...
    
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
    def CopyTo(self, position: CopyPosition, array: ArrayType[T], arrayIndex: IntType, count: IntType) -> CopyPosition: ...
    
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


# No Interfaces

# No Enums

# No Delegates

__all__ = [
    BitHelper,
    EnumerableHelpers,
    HashSet,
    HashSetDebugView,
    HashSetEqualityComparer,
    ArrayBuilder,
    CopyPosition,
    LargeArrayBuilder,
    Marker,
    SparseArrayBuilder,
]
