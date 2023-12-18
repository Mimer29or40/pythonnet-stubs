from __future__ import annotations

from abc import ABC
from typing import List
from typing import Union
from typing import overload

from System import Array
from System import Boolean
from System import Exception
from System import Int32
from System import Object
from System import String
from System import Void
from System.Collections import ICollection
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections.Specialized import NameValueCollection
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class ProviderBase(ABC, ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Description(self) -> StringType: ...
    @property
    def Name(self) -> StringType: ...

    # ---------- Methods ---------- #

    def Initialize(self, name: StringType, config: NameValueCollection) -> VoidType: ...
    def get_Description(self) -> StringType: ...
    def get_Name(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ProviderCollection(ObjectType, IEnumerable, ICollection):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...
    @property
    def IsSynchronized(self) -> BooleanType: ...
    def __getitem__(self, key: StringType) -> ProviderBase: ...
    @property
    def SyncRoot(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def Add(self, provider: ProviderBase) -> VoidType: ...
    def Clear(self) -> VoidType: ...
    def CopyTo(self, array: ArrayType[ProviderBase], index: IntType) -> VoidType: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def Remove(self, name: StringType) -> VoidType: ...
    def SetReadOnly(self) -> VoidType: ...
    def get_Count(self) -> IntType: ...
    def get_IsSynchronized(self) -> BooleanType: ...
    def get_Item(self, name: StringType) -> ProviderBase: ...
    def get_SyncRoot(self) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ProviderException(Exception, ISerializable, _Exception):
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

# No Structs

# No Interfaces

# No Enums

# No Delegates

__all__ = [
    ProviderBase,
    ProviderCollection,
    ProviderException,
]
