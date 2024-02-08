from __future__ import annotations

from typing import Generic
from typing import TypeVar
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

T = TypeVar("T")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class SoundPlayer(Component, IComponent, ISerializable, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, stream: Stream):
        """

        :param stream:
        """
    @overload
    def __init__(self, soundLocation: str):
        """

        :param soundLocation:
        """
    @property
    def Container(self) -> IContainer:
        """

        :return:
        """
    @property
    def IsLoadCompleted(self) -> bool:
        """

        :return:
        """
    @property
    def LoadTimeout(self) -> int:
        """

        :return:
        """
    @LoadTimeout.setter
    def LoadTimeout(self, value: int) -> None: ...
    @property
    def Site(self) -> ISite:
        """

        :return:
        """
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    @property
    def SoundLocation(self) -> str:
        """

        :return:
        """
    @SoundLocation.setter
    def SoundLocation(self, value: str) -> None: ...
    @property
    def Stream(self) -> Stream:
        """

        :return:
        """
    @Stream.setter
    def Stream(self, value: Stream) -> None: ...
    @property
    def Tag(self) -> object:
        """

        :return:
        """
    @Tag.setter
    def Tag(self, value: object) -> None: ...
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
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
        """

        :return:
        """
    Disposed: EventType[EventHandler] = ...
    """"""
    LoadCompleted: EventType[AsyncCompletedEventHandler] = ...
    """"""
    SoundLocationChanged: EventType[EventHandler] = ...
    """"""
    StreamChanged: EventType[EventHandler] = ...
    """"""

class SystemSound(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Play(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SystemSounds(Object):
    """"""

    @classmethod
    @property
    def Asterisk(cls) -> SystemSound:
        """

        :return:
        """
    @classmethod
    @property
    def Beep(cls) -> SystemSound:
        """

        :return:
        """
    @classmethod
    @property
    def Exclamation(cls) -> SystemSound:
        """

        :return:
        """
    @classmethod
    @property
    def Hand(cls) -> SystemSound:
        """

        :return:
        """
    @classmethod
    @property
    def Question(cls) -> SystemSound:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
