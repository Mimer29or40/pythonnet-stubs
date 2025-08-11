"""Automatically generated stubs for C# namespace: System.Runtime.DesignerServices."""

from typing import overload

from System import Object
from System import Type
from System.Collections.Generic import IEnumerable
from System.Reflection import Assembly

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class WindowsRuntimeDesignerContext(Object):
    """"""
    def __init__(self, paths: IEnumerable[str], name: str) -> None:
        """"""
    @property
    def Name(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAssembly(self, assemblyName: str) -> Assembly:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetType(self) -> Type:
        """"""
    @overload
    def GetType(self, typeName: str) -> Type:
        """"""
    @classmethod
    def InitializeSharedContext(cls, paths: IEnumerable[str]) -> None:
        """"""
    @classmethod
    def SetIterationContext(cls, context: WindowsRuntimeDesignerContext) -> None:
        """"""
    def ToString(self) -> str:
        """"""
