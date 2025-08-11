"""Automatically generated stubs for C# namespace: System.Diagnostics.Tracing.Internal."""

from abc import ABC
from typing import ClassVar

from System import Array
from System import Object
from System import Type

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Environment(ABC, Object):
    """"""

    NewLine: ClassVar[str]
    """"""
    @classmethod
    @property
    def TickCount(cls) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetResourceString(cls, key: str, args: Array[object]) -> str:
        """"""
    @classmethod
    def GetRuntimeResourceString(cls, key: str, args: Array[object]) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
