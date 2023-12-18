from __future__ import annotations

from abc import ABC
from typing import Union

from System import Boolean
from System import Object
from System import Type
from System import TypeCode
from System.Reflection import Assembly

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
ObjectType = Object
TypeType = Union[type, Type]

# ---------- Classes ---------- #

class ReflectionExtensions(ABC, ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    def Assembly(type: TypeType) -> Assembly: ...
    @staticmethod
    def BaseType(type: TypeType) -> TypeType: ...
    @staticmethod
    def GetTypeCode(type: TypeType) -> TypeCode: ...
    @staticmethod
    def IsAbstract(type: TypeType) -> BooleanType: ...
    @staticmethod
    def IsEnum(type: TypeType) -> BooleanType: ...
    @staticmethod
    def IsSealed(type: TypeType) -> BooleanType: ...
    @staticmethod
    def ReflectionOnly(assm: Assembly) -> BooleanType: ...

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
    ReflectionExtensions,
]
