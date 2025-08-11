"""Automatically generated stubs for C# namespace: System.Media."""

from typing import Self
from typing import overload

from System import EventHandler
from System import IDisposable
from System import Object
from System import Type
from System.ComponentModel import AsyncCompletedEventHandler
from System.ComponentModel import Component
from System.ComponentModel import IComponent
from System.ComponentModel import IContainer
from System.ComponentModel import ISite
from System.IO import Stream
from System.Runtime.Remoting import ObjRef
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SoundPlayer(Component, IComponent, ISerializable, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, soundLocation: str) -> None:
        """"""
    @overload
    def __init__(self, stream: Stream) -> None:
        """"""
    @property
    def Container(self) -> IContainer:
        """"""
    @property
    def IsLoadCompleted(self) -> bool:
        """"""
    @property
    def LoadTimeout(self) -> int:
        """"""
    @LoadTimeout.setter
    def LoadTimeout(self, value: int) -> None: ...
    @property
    def Site(self) -> ISite:
        """"""
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    @property
    def SoundLocation(self) -> str:
        """"""
    @SoundLocation.setter
    def SoundLocation(self, value: str) -> None: ...
    @property
    def Stream(self) -> Stream:
        """"""
    @Stream.setter
    def Stream(self, value: Stream) -> None: ...
    @property
    def Tag(self) -> object:
        """"""
    @Tag.setter
    def Tag(self, value: object) -> None: ...
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Load(self) -> None:
        """"""
    def LoadAsync(self) -> None:
        """"""
    def Play(self) -> None:
        """"""
    def PlayLooping(self) -> None:
        """"""
    def PlaySync(self) -> None:
        """"""
    def Stop(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    Disposed: EventType[EventHandler] = ...
    """"""
    LoadCompleted: EventType[AsyncCompletedEventHandler] = ...
    """"""
    SoundLocationChanged: EventType[EventHandler] = ...
    """"""
    StreamChanged: EventType[EventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SystemSound(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Play(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SystemSounds(Object):
    """"""
    @classmethod
    @property
    def Asterisk(cls) -> SystemSound:
        """"""
    @classmethod
    @property
    def Beep(cls) -> SystemSound:
        """"""
    @classmethod
    @property
    def Exclamation(cls) -> SystemSound:
        """"""
    @classmethod
    @property
    def Hand(cls) -> SystemSound:
        """"""
    @classmethod
    @property
    def Question(cls) -> SystemSound:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
