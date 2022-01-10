from __future__ import annotations

from abc import ABC
from typing import Generic, List, TypeVar, Union

from System import Array, Boolean, Func, Int32, Object, ValueType, Void

# ---------- Types ---------- #

T = TypeVar('T')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
ObjectType = Object
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class ImmutableArray(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CreateBuilder(capacity: IntType) -> Builder[T]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ImmutableArray(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CreateBuilder(capacity: IntType) -> Builder[T]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class ImmutableArray(Generic[T], ValueType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Empty() -> ImmutableArray[T]: ...
    
    @staticmethod
    @Empty.setter
    def Empty(value: ImmutableArray[T]) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, array: ArrayType[T]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def Item(self) -> T: ...
    
    @property
    def Length(self) -> IntType: ...
    
    @property
    def UnderlyingArray(self) -> ArrayType[T]: ...
    
    # ---------- Methods ---------- #
    
    def CopyTo(self, sourceIndex: IntType, destination: ArrayType[T], destinationIndex: IntType, length: IntType) -> VoidType: ...
    
    def FirstOrDefault(self, predicate: Func[T, BooleanType]) -> T: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> T: ...
    
    def get_Length(self) -> IntType: ...
    
    def get_UnderlyingArray(self) -> ArrayType[T]: ...
    
    # No Events
    
    
    # ---------- Sub Classes ---------- #
    
    class Builder(Generic[T], ObjectType):
        # No Fields
        
        # No Constructors
        
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
        
        def MoveToImmutable(self) -> ImmutableArray[T]: ...
        
        def get_Capacity(self) -> IntType: ...
        
        def get_Count(self) -> IntType: ...
        
        def get_Item(self, index: IntType) -> T: ...
        
        def set_Item(self, index: IntType, value: T) -> VoidType: ...
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ImmutableArray(Generic[T], ValueType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Empty() -> ImmutableArray[T]: ...
    
    @staticmethod
    @Empty.setter
    def Empty(value: ImmutableArray[T]) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, array: ArrayType[T]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def Item(self) -> T: ...
    
    @property
    def Length(self) -> IntType: ...
    
    @property
    def UnderlyingArray(self) -> ArrayType[T]: ...
    
    # ---------- Methods ---------- #
    
    def CopyTo(self, sourceIndex: IntType, destination: ArrayType[T], destinationIndex: IntType, length: IntType) -> VoidType: ...
    
    def FirstOrDefault(self, predicate: Func[T, BooleanType]) -> T: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> T: ...
    
    def get_Length(self) -> IntType: ...
    
    def get_UnderlyingArray(self) -> ArrayType[T]: ...
    
    # No Events
    
    
    # ---------- Sub Classes ---------- #
    
    class Builder(Generic[T], ObjectType):
        # No Fields
        
        # No Constructors
        
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
        
        def MoveToImmutable(self) -> ImmutableArray[T]: ...
        
        def get_Capacity(self) -> IntType: ...
        
        def get_Count(self) -> IntType: ...
        
        def get_Item(self, index: IntType) -> T: ...
        
        def set_Item(self, index: IntType, value: T) -> VoidType: ...
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Interfaces

# No Enums

# No Delegates

__all__ = [
    ImmutableArray,
    ImmutableArray,
]
