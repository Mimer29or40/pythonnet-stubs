from __future__ import annotations

from typing import Union, overload

from Microsoft.Win32 import UnsafeNativeMethods
from System import Attribute, Int32, MarshalByRefObject, Object, String, Void
from System.Runtime.InteropServices import _Attribute

# ---------- Types ---------- #

IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class DefaultParameterValueAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, value: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_Value(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HandleCollector(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, name: StringType, initialThreshold: IntType): ...
    
    @overload
    def __init__(self, name: StringType, initialThreshold: IntType, maximumThreshold: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def InitialThreshold(self) -> IntType: ...
    
    @property
    def MaximumThreshold(self) -> IntType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self) -> VoidType: ...
    
    def Remove(self) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_InitialThreshold(self) -> IntType: ...
    
    def get_MaximumThreshold(self) -> IntType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StandardOleMarshalObject(MarshalByRefObject, IMarshal):
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
    DefaultParameterValueAttribute,
    HandleCollector,
    StandardOleMarshalObject,
]
