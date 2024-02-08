from __future__ import annotations

from typing import overload

from System import Object
from System import Type
from System.Collections.Generic import IEnumerable
from System.Reflection import Assembly

class WindowsRuntimeDesignerContext(Object):
    """"""

    def __init__(self, paths: IEnumerable[str], name: str):
        """

        :param paths:
        :param name:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAssembly(self, assemblyName: str) -> Assembly:
        """

        :param assemblyName:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self, typeName: str) -> Type:
        """

        :param typeName:
        :return:
        """
    @classmethod
    def InitializeSharedContext(cls, paths: IEnumerable[str]) -> None:
        """

        :param paths:
        """
    @classmethod
    def SetIterationContext(cls, context: WindowsRuntimeDesignerContext) -> None:
        """

        :param context:
        """
    def ToString(self) -> str:
        """

        :return:
        """
