"""Automatically generated stubs for C# namespace: System.Diagnostics.Contracts.Internal."""

from abc import ABC

from System import Exception
from System import Object
from System import Type
from System.Diagnostics.Contracts import ContractFailureKind

class ContractHelper(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def RaiseContractFailedEvent(
        cls,
        failureKind: ContractFailureKind,
        userMessage: str,
        conditionText: str,
        innerException: Exception,
    ) -> str:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def TriggerFailure(
        cls,
        kind: ContractFailureKind,
        displayMessage: str,
        userMessage: str,
        conditionText: str,
        innerException: Exception,
    ) -> None:
        """"""
