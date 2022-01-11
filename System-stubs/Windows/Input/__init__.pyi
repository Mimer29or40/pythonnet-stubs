from __future__ import annotations

from typing import Generic, Protocol, TypeVar, Union

from System import Boolean, EventHandler, Object, String, Void

# ---------- Types ---------- #

T = TypeVar('T')

BooleanType = Union[bool, Boolean]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...



# ---------- Classes ---------- #

class BuildInfo(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def WCP_PUBLIC_KEY_TOKEN() -> StringType: ...
    
    @staticmethod
    @property
    def WCP_VERSION() -> StringType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BuildInfo(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def WCP_PUBLIC_KEY_TOKEN() -> StringType: ...
    
    @staticmethod
    @property
    def WCP_VERSION() -> StringType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# ---------- Interfaces ---------- #

class ICommand(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CanExecute(self, parameter: ObjectType) -> BooleanType: ...
    
    def Execute(self, parameter: ObjectType) -> VoidType: ...
    
    def add_CanExecuteChanged(self, value: EventHandler) -> VoidType: ...
    
    def remove_CanExecuteChanged(self, value: EventHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    CanExecuteChanged: EventType[EventHandler] = ...


class ICommand(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CanExecute(self, parameter: ObjectType) -> BooleanType: ...
    
    def Execute(self, parameter: ObjectType) -> VoidType: ...
    
    def add_CanExecuteChanged(self, value: EventHandler) -> VoidType: ...
    
    def remove_CanExecuteChanged(self, value: EventHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    CanExecuteChanged: EventType[EventHandler] = ...


# No Enums

# No Delegates

__all__ = [
    BuildInfo,
    ICommand,
]
