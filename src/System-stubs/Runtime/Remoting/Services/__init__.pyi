from __future__ import annotations

from System import Array
from System import IntPtr
from System import MarshalByRefObject
from System import Object
from System import Type
from System.Runtime.Remoting import ObjRef
from System.Runtime.Remoting.Activation import IConstructionCallMessage
from System.Runtime.Remoting.Activation import IConstructionReturnMessage
from System.Runtime.Remoting.Proxies import RealProxy

class EnterpriseServicesHelper(Object):
    """"""

    def __init__(self):
        """"""
    @classmethod
    def CreateConstructionReturnMessage(
        cls, ctorMsg: IConstructionCallMessage, retObj: MarshalByRefObject
    ) -> IConstructionReturnMessage:
        """

        :param ctorMsg:
        :param retObj:
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
    @classmethod
    def SwitchWrappers(cls, oldcp: RealProxy, newcp: RealProxy) -> None:
        """

        :param oldcp:
        :param newcp:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def WrapIUnknownWithComObject(cls, punk: IntPtr) -> object:
        """

        :param punk:
        :return:
        """

class ITrackingHandler:
    """"""

    def DisconnectedObject(self, obj: object) -> None:
        """

        :param obj:
        """
    def MarshaledObject(self, obj: object, _or: ObjRef) -> None:
        """

        :param obj:
        :param _or:
        """
    def UnmarshaledObject(self, obj: object, _or: ObjRef) -> None:
        """

        :param obj:
        :param _or:
        """

class TrackingServices(Object):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def RegisteredHandlers(cls) -> Array[ITrackingHandler]:
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
    @classmethod
    def RegisterTrackingHandler(cls, handler: ITrackingHandler) -> None:
        """

        :param handler:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def UnregisterTrackingHandler(cls, handler: ITrackingHandler) -> None:
        """

        :param handler:
        """
