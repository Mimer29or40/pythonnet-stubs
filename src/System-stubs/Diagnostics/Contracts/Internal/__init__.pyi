from __future__ import annotations

from abc import ABC

from System import Exception
from System import Object
from System import Type
from System.Diagnostics.Contracts import ContractFailureKind

class ContractHelper(ABC, Object):
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
    @classmethod
    def RaiseContractFailedEvent(
        cls,
        failureKind: ContractFailureKind,
        userMessage: str,
        conditionText: str,
        innerException: Exception,
    ) -> str:
        """

        :param failureKind:
        :param userMessage:
        :param conditionText:
        :param innerException:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def TriggerFailure(
        cls,
        kind: ContractFailureKind,
        displayMessage: str,
        userMessage: str,
        conditionText: str,
        innerException: Exception,
    ) -> None:
        """

        :param kind:
        :param displayMessage:
        :param userMessage:
        :param conditionText:
        :param innerException:
        """
