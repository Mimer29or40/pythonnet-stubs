"""Automatically generated stubs for C# namespace: System.Windows.Input."""

from typing import ClassVar
from typing import Self

from System import EventHandler
from System import Object
from System import Type

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

class BuildInfo(Object):
    """"""

    WCP_PUBLIC_KEY_TOKEN: ClassVar[str]
    """"""
    WCP_VERSION: ClassVar[str]
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ICommand:
    """"""
    def CanExecute(self, parameter: object) -> bool:
        """"""
    def Execute(self, parameter: object) -> None:
        """"""
    CanExecuteChanged: EventType[EventHandler] = ...
    """"""
