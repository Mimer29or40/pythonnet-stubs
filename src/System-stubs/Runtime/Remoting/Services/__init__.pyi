"""Automatically generated stubs for C# namespace: System.Runtime.Remoting.Services."""

from abc import ABC

from System import Array
from System import IntPtr
from System import MarshalByRefObject
from System import Object
from System import Type
from System.Runtime.Remoting import ObjRef
from System.Runtime.Remoting.Activation import IConstructionCallMessage
from System.Runtime.Remoting.Activation import IConstructionReturnMessage
from System.Runtime.Remoting.Proxies import RealProxy

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EnterpriseServicesHelper(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @classmethod
    def CreateConstructionReturnMessage(
        cls, ctorMsg: IConstructionCallMessage, retObj: MarshalByRefObject
    ) -> IConstructionReturnMessage:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def SwitchWrappers(cls, oldcp: RealProxy, newcp: RealProxy) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def WrapIUnknownWithComObject(cls, punk: IntPtr) -> object:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ITrackingHandler(ABC):
    """"""
    def DisconnectedObject(self, obj: object) -> None:
        """"""
    def MarshaledObject(self, obj: object, _or: ObjRef) -> None:
        """"""
    def UnmarshaledObject(self, obj: object, _or: ObjRef) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TrackingServices(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @classmethod
    @property
    def RegisteredHandlers(cls) -> Array[ITrackingHandler]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def RegisterTrackingHandler(cls, handler: ITrackingHandler) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def UnregisterTrackingHandler(cls, handler: ITrackingHandler) -> None:
        """"""
