"""Automatically generated stubs for C# namespace: System.Configuration.Assemblies."""

from typing import ClassVar
from typing import overload

from System import Array
from System import Enum
from System import ICloneable
from System import Type
from System import ValueType

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssemblyHash(ValueType, ICloneable):
    """"""

    Empty: ClassVar[AssemblyHash]
    """"""
    @overload
    def __init__(self, value: Array[int]) -> None:
        """"""
    @overload
    def __init__(self, algorithm: AssemblyHashAlgorithm, value: Array[int]) -> None:
        """"""
    @property
    def Algorithm(self) -> AssemblyHashAlgorithm:
        """"""
    @Algorithm.setter
    def Algorithm(self, value: AssemblyHashAlgorithm) -> None: ...
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetValue(self) -> Array[int]:
        """"""
    def SetValue(self, value: Array[int]) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class AssemblyVersionCompatibility(Enum):
    """"""

    SameMachine: AssemblyVersionCompatibility = ...
    """"""
    SameProcess: AssemblyVersionCompatibility = ...
    """"""
    SameDomain: AssemblyVersionCompatibility = ...
    """"""
