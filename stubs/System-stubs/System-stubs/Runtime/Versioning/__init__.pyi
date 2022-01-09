from __future__ import annotations

from typing import Union, overload

from System import Boolean, IEquatable, Int32, Object, String, Version

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]

# ---------- Classes ---------- #

class FrameworkName(ObjectType, IEquatable[FrameworkName]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, identifier: StringType, version: Version): ...
    
    @overload
    def __init__(self, identifier: StringType, version: Version, profile: StringType): ...
    
    @overload
    def __init__(self, frameworkName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def FullName(self) -> StringType: ...
    
    @property
    def Identifier(self) -> StringType: ...
    
    @property
    def Profile(self) -> StringType: ...
    
    @property
    def Version(self) -> Version: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: FrameworkName) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_FullName(self) -> StringType: ...
    
    def get_Identifier(self) -> StringType: ...
    
    def get_Profile(self) -> StringType: ...
    
    def get_Version(self) -> Version: ...
    
    @staticmethod
    def op_Equality(left: FrameworkName, right: FrameworkName) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: FrameworkName, right: FrameworkName) -> BooleanType: ...
    
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
    FrameworkName,
]
