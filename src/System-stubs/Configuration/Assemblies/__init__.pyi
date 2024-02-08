from __future__ import annotations

from typing import ClassVar
from typing import Final
from typing import overload

from System import Array
from System import Enum
from System import ICloneable
from System import Type
from System import ValueType

class AssemblyHash(ValueType, ICloneable):
    """"""

    Empty: Final[ClassVar[AssemblyHash]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, value: Array[int]):
        """

        :param value:
        """
    @overload
    def __init__(self, algorithm: AssemblyHashAlgorithm, value: Array[int]):
        """

        :param algorithm:
        :param value:
        """
    @property
    def Algorithm(self) -> AssemblyHashAlgorithm:
        """

        :return:
        """
    @Algorithm.setter
    def Algorithm(self, value: AssemblyHashAlgorithm) -> None: ...
    def Clone(self) -> object:
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
    def GetValue(self) -> Array[int]:
        """

        :return:
        """
    def SetValue(self, value: Array[int]) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class AssemblyHashAlgorithm(Enum):
    """"""

    _None: AssemblyHashAlgorithm = ...
    """"""
    MD5: AssemblyHashAlgorithm = ...
    """"""
    SHA1: AssemblyHashAlgorithm = ...
    """"""
    SHA256: AssemblyHashAlgorithm = ...
    """"""
    SHA384: AssemblyHashAlgorithm = ...
    """"""
    SHA512: AssemblyHashAlgorithm = ...
    """"""

class AssemblyVersionCompatibility(Enum):
    """"""

    SameMachine: AssemblyVersionCompatibility = ...
    """"""
    SameProcess: AssemblyVersionCompatibility = ...
    """"""
    SameDomain: AssemblyVersionCompatibility = ...
    """"""
