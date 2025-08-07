"""Automatically generated stubs for C# namespace: System.Deployment.Internal."""

from abc import ABC

from System import ActivationContext
from System import ApplicationIdentity
from System import Array
from System import Object
from System import Type

class InternalActivationContextHelper(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetActivationContextData(cls, appInfo: ActivationContext) -> object:
        """"""
    @classmethod
    def GetApplicationComponentManifest(cls, appInfo: ActivationContext) -> object:
        """"""
    @classmethod
    def GetApplicationManifestBytes(cls, appInfo: ActivationContext) -> Array[int]:
        """"""
    @classmethod
    def GetDeploymentComponentManifest(cls, appInfo: ActivationContext) -> object:
        """"""
    @classmethod
    def GetDeploymentManifestBytes(cls, appInfo: ActivationContext) -> Array[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsFirstRun(cls, appInfo: ActivationContext) -> bool:
        """"""
    @classmethod
    def PrepareForExecution(cls, appInfo: ActivationContext) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class InternalApplicationIdentityHelper(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetInternalAppId(cls, id: ApplicationIdentity) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
