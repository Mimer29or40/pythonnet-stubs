from __future__ import annotations

from typing import Generic, Union, overload

from System import Boolean, EventHandler, IDisposable, Int32, Object, String, Void
from System.ComponentModel import AsyncCompletedEventHandler, Component, IComponent
from System.IO import Stream
from System.Runtime.Serialization import ISerializable

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...


# ---------- Classes ---------- #

class SoundPlayer(Component, IComponent, IDisposable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, soundLocation: StringType): ...
    
    @overload
    def __init__(self, stream: Stream): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsLoadCompleted(self) -> BooleanType: ...
    
    @property
    def LoadTimeout(self) -> IntType: ...
    
    @LoadTimeout.setter
    def LoadTimeout(self, value: IntType) -> None: ...
    
    @property
    def SoundLocation(self) -> StringType: ...
    
    @SoundLocation.setter
    def SoundLocation(self, value: StringType) -> None: ...
    
    @property
    def Stream(self) -> Stream: ...
    
    @Stream.setter
    def Stream(self, value: Stream) -> None: ...
    
    @property
    def Tag(self) -> ObjectType: ...
    
    @Tag.setter
    def Tag(self, value: ObjectType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Load(self) -> VoidType: ...
    
    def LoadAsync(self) -> VoidType: ...
    
    def Play(self) -> VoidType: ...
    
    def PlayLooping(self) -> VoidType: ...
    
    def PlaySync(self) -> VoidType: ...
    
    def Stop(self) -> VoidType: ...
    
    def add_LoadCompleted(self, value: AsyncCompletedEventHandler) -> VoidType: ...
    
    def add_SoundLocationChanged(self, value: EventHandler) -> VoidType: ...
    
    def add_StreamChanged(self, value: EventHandler) -> VoidType: ...
    
    def get_IsLoadCompleted(self) -> BooleanType: ...
    
    def get_LoadTimeout(self) -> IntType: ...
    
    def get_SoundLocation(self) -> StringType: ...
    
    def get_Stream(self) -> Stream: ...
    
    def get_Tag(self) -> ObjectType: ...
    
    def remove_LoadCompleted(self, value: AsyncCompletedEventHandler) -> VoidType: ...
    
    def remove_SoundLocationChanged(self, value: EventHandler) -> VoidType: ...
    
    def remove_StreamChanged(self, value: EventHandler) -> VoidType: ...
    
    def set_LoadTimeout(self, value: IntType) -> VoidType: ...
    
    def set_SoundLocation(self, value: StringType) -> VoidType: ...
    
    def set_Stream(self, value: Stream) -> VoidType: ...
    
    def set_Tag(self, value: ObjectType) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    LoadCompleted: EventType[AsyncCompletedEventHandler] = ...
    
    SoundLocationChanged: EventType[EventHandler] = ...
    
    StreamChanged: EventType[EventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemSound(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Play(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemSounds(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Asterisk() -> SystemSound: ...
    
    @staticmethod
    @property
    def Beep() -> SystemSound: ...
    
    @staticmethod
    @property
    def Exclamation() -> SystemSound: ...
    
    @staticmethod
    @property
    def Hand() -> SystemSound: ...
    
    @staticmethod
    @property
    def Question() -> SystemSound: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_Asterisk() -> SystemSound: ...
    
    @staticmethod
    def get_Beep() -> SystemSound: ...
    
    @staticmethod
    def get_Exclamation() -> SystemSound: ...
    
    @staticmethod
    def get_Hand() -> SystemSound: ...
    
    @staticmethod
    def get_Question() -> SystemSound: ...
    
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
    SoundPlayer,
    SystemSound,
    SystemSounds,
]
