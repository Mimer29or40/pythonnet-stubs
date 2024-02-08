from __future__ import annotations

from typing import ClassVar
from typing import Final
from typing import Generic
from typing import TypeVar

from System import EventHandler
from System import Object
from System import Type

T = TypeVar("T")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class BuildInfo(Object):
    """"""

    WCP_PUBLIC_KEY_TOKEN: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    WCP_VERSION: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    def __init__(self):
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
    def ToString(self) -> str:
        """

        :return:
        """

class ICommand:
    """"""

    def CanExecute(self, parameter: object) -> bool:
        """

        :param parameter:
        :return:
        """
    def Execute(self, parameter: object) -> None:
        """

        :param parameter:
        """
    CanExecuteChanged: EventType[EventHandler] = ...
    """"""
