from __future__ import annotations

from typing import overload

from System import ActivationContext
from System import ApplicationIdentity
from System import Array
from System import Object
from System import Type
from System.Runtime.Remoting import ObjectHandle
from System.Security.Policy import EvidenceBase

class ActivationArguments(EvidenceBase):
    """"""

    @overload
    def __init__(self, activationData: ActivationContext):
        """

        :param activationData:
        """
    @overload
    def __init__(self, applicationIdentity: ApplicationIdentity):
        """

        :param applicationIdentity:
        """
    @overload
    def __init__(self, activationContext: ActivationContext, activationData: Array[str]):
        """

        :param activationContext:
        :param activationData:
        """
    @overload
    def __init__(self, applicationIdentity: ApplicationIdentity, activationData: Array[str]):
        """

        :param applicationIdentity:
        :param activationData:
        """
    @property
    def ActivationContext(self) -> ActivationContext:
        """

        :return:
        """
    @property
    def ActivationData(self) -> Array[str]:
        """

        :return:
        """
    @property
    def ApplicationIdentity(self) -> ApplicationIdentity:
        """

        :return:
        """
    def Clone(self) -> EvidenceBase:
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
    def ToString(self) -> str:
        """

        :return:
        """

class ApplicationActivator(Object):
    """"""

    def __init__(self):
        """"""
    @overload
    def CreateInstance(self, activationContext: ActivationContext) -> ObjectHandle:
        """

        :param activationContext:
        :return:
        """
    @overload
    def CreateInstance(
        self, activationContext: ActivationContext, activationCustomData: Array[str]
    ) -> ObjectHandle:
        """

        :param activationContext:
        :param activationCustomData:
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

class ManifestRunner(Object):
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
    def ToString(self) -> str:
        """

        :return:
        """
