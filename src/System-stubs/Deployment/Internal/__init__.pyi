from __future__ import annotations

from abc import ABC

from System import ActivationContext
from System import ApplicationIdentity
from System import Array
from System import Object
from System import Type

class InternalActivationContextHelper(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetActivationContextData(cls, appInfo: ActivationContext) -> object:
        """

        :param appInfo:
        :return:
        """
    @classmethod
    def GetApplicationComponentManifest(cls, appInfo: ActivationContext) -> object:
        """

        :param appInfo:
        :return:
        """
    @classmethod
    def GetApplicationManifestBytes(cls, appInfo: ActivationContext) -> Array[int]:
        """

        :param appInfo:
        :return:
        """
    @classmethod
    def GetDeploymentComponentManifest(cls, appInfo: ActivationContext) -> object:
        """

        :param appInfo:
        :return:
        """
    @classmethod
    def GetDeploymentManifestBytes(cls, appInfo: ActivationContext) -> Array[int]:
        """

        :param appInfo:
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
    def IsFirstRun(cls, appInfo: ActivationContext) -> bool:
        """

        :param appInfo:
        :return:
        """
    @classmethod
    def PrepareForExecution(cls, appInfo: ActivationContext) -> None:
        """

        :param appInfo:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class InternalApplicationIdentityHelper(ABC, Object):
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
    @classmethod
    def GetInternalAppId(cls, id: ApplicationIdentity) -> object:
        """

        :param id:
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
