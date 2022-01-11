from __future__ import annotations

from abc import ABC
from typing import List, Union

from System import Array, Int32, Object, String

# ---------- Types ---------- #

ArrayType = Union[List, Array]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]


# ---------- Classes ---------- #

class Environment(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def NewLine() -> StringType: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def TickCount() -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetResourceString(key: StringType, args: ArrayType[ObjectType]) -> StringType: ...
    
    @staticmethod
    def GetRuntimeResourceString(key: StringType, args: ArrayType[ObjectType]) -> StringType: ...
    
    @staticmethod
    def get_TickCount() -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Environment(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def NewLine() -> StringType: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def TickCount() -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetResourceString(key: StringType, args: ArrayType[ObjectType]) -> StringType: ...
    
    @staticmethod
    def GetRuntimeResourceString(key: StringType, args: ArrayType[ObjectType]) -> StringType: ...
    
    @staticmethod
    def get_TickCount() -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Environment(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def NewLine() -> StringType: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def TickCount() -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetResourceString(key: StringType, args: ArrayType[ObjectType]) -> StringType: ...
    
    @staticmethod
    def GetRuntimeResourceString(key: StringType, args: ArrayType[ObjectType]) -> StringType: ...
    
    @staticmethod
    def get_TickCount() -> IntType: ...
    
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
    Environment,
]
