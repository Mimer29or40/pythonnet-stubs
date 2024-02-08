from __future__ import annotations

from abc import ABC

from System import Object
from System import Type

class HashHelpers(ABC, Object):
    """"""

    @classmethod
    def Combine(cls, h1: int, h2: int) -> int:
        """

        :param h1:
        :param h2:
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
