from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final

from System import Array
from System import Object
from System import Type

class Environment(ABC, Object):
    """"""

    NewLine: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    @classmethod
    @property
    def TickCount(cls) -> int:
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
    @classmethod
    def GetResourceString(cls, key: str, args: Array[object]) -> str:
        """

        :param key:
        :param args:
        :return:
        """
    @classmethod
    def GetRuntimeResourceString(cls, key: str, args: Array[object]) -> str:
        """

        :param key:
        :param args:
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
