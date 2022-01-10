from __future__ import annotations

from typing import List, Protocol, Union

from System import Array, IntPtr, MarshalByRefObject, Object, Void
from System.Runtime.Remoting import ObjRef
from System.Runtime.Remoting.Activation import IConstructionCallMessage, IConstructionReturnMessage
from System.Runtime.Remoting.Proxies import RealProxy

# ---------- Types ---------- #

ArrayType = Union[List, Array]
NIntType = Union[int, IntPtr]
ObjectType = Object
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class EnterpriseServicesHelper(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CreateConstructionReturnMessage(ctorMsg: IConstructionCallMessage, retObj: MarshalByRefObject) -> IConstructionReturnMessage: ...
    
    @staticmethod
    def SwitchWrappers(oldcp: RealProxy, newcp: RealProxy) -> VoidType: ...
    
    @staticmethod
    def WrapIUnknownWithComObject(punk: NIntType) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EnterpriseServicesHelper(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CreateConstructionReturnMessage(ctorMsg: IConstructionCallMessage, retObj: MarshalByRefObject) -> IConstructionReturnMessage: ...
    
    @staticmethod
    def SwitchWrappers(oldcp: RealProxy, newcp: RealProxy) -> VoidType: ...
    
    @staticmethod
    def WrapIUnknownWithComObject(punk: NIntType) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EnterpriseServicesHelper(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CreateConstructionReturnMessage(ctorMsg: IConstructionCallMessage, retObj: MarshalByRefObject) -> IConstructionReturnMessage: ...
    
    @staticmethod
    def SwitchWrappers(oldcp: RealProxy, newcp: RealProxy) -> VoidType: ...
    
    @staticmethod
    def WrapIUnknownWithComObject(punk: NIntType) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TrackingServices(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def RegisteredHandlers() -> ArrayType[ITrackingHandler]: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def RegisterTrackingHandler(handler: ITrackingHandler) -> VoidType: ...
    
    @staticmethod
    def UnregisterTrackingHandler(handler: ITrackingHandler) -> VoidType: ...
    
    @staticmethod
    def get_RegisteredHandlers() -> ArrayType[ITrackingHandler]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TrackingServices(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def RegisteredHandlers() -> ArrayType[ITrackingHandler]: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def RegisterTrackingHandler(handler: ITrackingHandler) -> VoidType: ...
    
    @staticmethod
    def UnregisterTrackingHandler(handler: ITrackingHandler) -> VoidType: ...
    
    @staticmethod
    def get_RegisteredHandlers() -> ArrayType[ITrackingHandler]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TrackingServices(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def RegisteredHandlers() -> ArrayType[ITrackingHandler]: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def RegisterTrackingHandler(handler: ITrackingHandler) -> VoidType: ...
    
    @staticmethod
    def UnregisterTrackingHandler(handler: ITrackingHandler) -> VoidType: ...
    
    @staticmethod
    def get_RegisteredHandlers() -> ArrayType[ITrackingHandler]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# ---------- Interfaces ---------- #

class ITrackingHandler(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def DisconnectedObject(self, obj: ObjectType) -> VoidType: ...
    
    def MarshaledObject(self, obj: ObjectType, _or: ObjRef) -> VoidType: ...
    
    def UnmarshaledObject(self, obj: ObjectType, _or: ObjRef) -> VoidType: ...
    
    # No Events


class ITrackingHandler(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def DisconnectedObject(self, obj: ObjectType) -> VoidType: ...
    
    def MarshaledObject(self, obj: ObjectType, _or: ObjRef) -> VoidType: ...
    
    def UnmarshaledObject(self, obj: ObjectType, _or: ObjRef) -> VoidType: ...
    
    # No Events


class ITrackingHandler(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def DisconnectedObject(self, obj: ObjectType) -> VoidType: ...
    
    def MarshaledObject(self, obj: ObjectType, _or: ObjRef) -> VoidType: ...
    
    def UnmarshaledObject(self, obj: ObjectType, _or: ObjRef) -> VoidType: ...
    
    # No Events


# No Enums

# No Delegates

__all__ = [
    EnterpriseServicesHelper,
    TrackingServices,
    ITrackingHandler,
]
