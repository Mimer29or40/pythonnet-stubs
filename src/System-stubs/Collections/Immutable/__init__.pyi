from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import TypeVar

from System import Array
from System import Func
from System import Object
from System import Type
from System import ValueType
from System.Collections.Immutable.ImmutableArray import Builder

T = TypeVar("T")

class ImmutableArray(ABC, Object):
    """"""

    @classmethod
    def CreateBuilder(cls, capacity: int) -> ImmutableArray.Builder[T]:
        """

        :param capacity:
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

class ImmutableArray(Generic[T], ValueType):
    """"""

    Empty: Final[ClassVar[ImmutableArray[T]]] = ...
    """
    
    :return: 
    """
    def __init__(self, array: Array[T]):
        """

        :param array:
        """
    @property
    def IsDefault(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> T:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def UnderlyingArray(self) -> Array[T]:
        """

        :return:
        """
    def CopyTo(
        self, sourceIndex: int, destination: Array[T], destinationIndex: int, length: int
    ) -> None:
        """

        :param sourceIndex:
        :param destination:
        :param destinationIndex:
        :param length:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FirstOrDefault(self, predicate: Func[T, bool]) -> T:
        """

        :param predicate:
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
    def __getitem__(self, index: int) -> T:
        """

        :param index:
        :return:
        """

    class Builder(Generic[T], Object):
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
        def MoveToImmutable(self) -> ImmutableArray[T]:
            """"""
        def ToString(self) -> str:
            """

            :return:
            """
        def __getitem__(self, index: int) -> T:
            """"""
        def __setitem__(self, index: int, value: T) -> None:
            """"""
