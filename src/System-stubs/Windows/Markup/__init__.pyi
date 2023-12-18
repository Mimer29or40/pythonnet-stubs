from __future__ import annotations

from typing import Union
from typing import overload

from System import Attribute
from System import String
from System import Type
from System.Runtime.InteropServices import _Attribute

# ---------- Types ---------- #

StringType = Union[str, String]
TypeType = Union[type, Type]

# ---------- Classes ---------- #

class ValueSerializerAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, valueSerializerType: TypeType): ...
    @overload
    def __init__(self, valueSerializerTypeName: StringType): ...

    # ---------- Properties ---------- #

    @property
    def ValueSerializerType(self) -> TypeType: ...
    @property
    def ValueSerializerTypeName(self) -> StringType: ...

    # ---------- Methods ---------- #

    def get_ValueSerializerType(self) -> TypeType: ...
    def get_ValueSerializerTypeName(self) -> StringType: ...

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
    ValueSerializerAttribute,
]
