from __future__ import annotations

from typing import List, Union, overload

from System import Array, Boolean, Delegate, Object, String, Type, Void
from System.Reflection import EventAttributes, EventInfo, ICustomAttributeProvider, MethodInfo
from System.Runtime.InteropServices import _EventInfo, _MemberInfo

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class ComAwareEventInfo(EventInfo, ICustomAttributeProvider, _MemberInfo, _EventInfo):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, type: TypeType, eventName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> EventAttributes: ...
    
    @property
    def DeclaringType(self) -> TypeType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ReflectedType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def AddEventHandler(self, target: ObjectType, handler: Delegate) -> VoidType: ...
    
    @overload
    def GetAddMethod(self, nonPublic: BooleanType) -> MethodInfo: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetRaiseMethod(self, nonPublic: BooleanType) -> MethodInfo: ...
    
    @overload
    def GetRemoveMethod(self, nonPublic: BooleanType) -> MethodInfo: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def RemoveEventHandler(self, target: ObjectType, handler: Delegate) -> VoidType: ...
    
    def get_Attributes(self) -> EventAttributes: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ReflectedType(self) -> TypeType: ...
    
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
    ComAwareEventInfo,
]
