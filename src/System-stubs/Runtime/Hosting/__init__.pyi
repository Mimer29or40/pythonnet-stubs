"""Automatically generated stubs for C# namespace: System.Runtime.Hosting."""

from typing import overload

from System import ActivationContext
from System import ApplicationIdentity
from System import Array
from System import Object
from System import Type
from System.Runtime.Remoting import ObjectHandle
from System.Security.Policy import EvidenceBase

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ActivationArguments(EvidenceBase):
    """"""
    @overload
    def __init__(self, applicationIdentity: ApplicationIdentity) -> None:
        """"""
    @overload
    def __init__(
        self, applicationIdentity: ApplicationIdentity, activationData: Array[str]
    ) -> None:
        """"""
    @overload
    def __init__(self, activationData: ActivationContext) -> None:
        """"""
    @overload
    def __init__(self, activationContext: ActivationContext, activationData: Array[str]) -> None:
        """"""
    @property
    def ActivationContext(self) -> ActivationContext:
        """"""
    @property
    def ActivationData(self) -> Array[str]:
        """"""
    @property
    def ApplicationIdentity(self) -> ApplicationIdentity:
        """"""
    def Clone(self) -> EvidenceBase:
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
class ApplicationActivator(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CreateInstance(self, activationContext: ActivationContext) -> ObjectHandle:
        """"""
    @overload
    def CreateInstance(
        self, activationContext: ActivationContext, activationCustomData: Array[str]
    ) -> ObjectHandle:
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
class ManifestRunner(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
