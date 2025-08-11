"""Automatically generated stubs for C# namespace: System.Collections.Immutable."""

from abc import ABC
from typing import ClassVar

from System import Array
from System import Func
from System import Object
from System import Type
from System import ValueType

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ImmutableArray(ABC, Object):
    """"""
    @classmethod
    def CreateBuilder[T](cls, capacity: int) -> ImmutableArray.Builder[T]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ImmutableArray[T](ValueType):
    """"""

    Empty: ClassVar[ImmutableArray[T]]
    """"""
    def __init__(self, array: Array[T]) -> None:
        """"""
    @property
    def IsDefault(self) -> bool:
        """"""
    @property
    def Item(self) -> T:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def UnderlyingArray(self) -> Array[T]:
        """"""
    def CopyTo(
        self, sourceIndex: int, destination: Array[T], destinationIndex: int, length: int
    ) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FirstOrDefault(self, predicate: Func[T, bool]) -> T:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __getitem__(self, index: int) -> T:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class Builder[T](Object):
        """"""
        @property
        def Capacity(self) -> int:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def Item(self) -> T:
            """"""
        @Item.setter
        def Item(self, value: T) -> None: ...
        def Add(self, item: T) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def MoveToImmutable(self) -> ImmutableArray[T]:
            """"""
        def ToString(self) -> str:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> T:
            """"""
        def __setitem__(self, index: int, value: T) -> None:
            """"""
