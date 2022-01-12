from __future__ import annotations

from abc import ABC
from typing import Tuple, Union

from System import Attribute, Boolean, Enum, Guid, Int32, IntPtr, MarshalByRefObject, Object, String, Type, ValueType, Void
from System.Runtime.InteropServices import _Attribute
from System.Runtime.Remoting import IRemotingTypeInfo, ObjRef
from System.Runtime.Remoting.Activation import IConstructionCallMessage, IConstructionReturnMessage
from System.Runtime.Remoting.Contexts import Context, IContextAttribute
from System.Runtime.Remoting.Messaging import AsyncResult, IMessage, IMethodCallMessage
from System.Runtime.Serialization import SerializationInfo, StreamingContext

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class AgileAsyncWorkerItem(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, message: IMethodCallMessage, ar: AsyncResult, target: ObjectType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def DoAsyncCall(self) -> VoidType: ...
    
    @staticmethod
    def ThreadPoolCallBack(o: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ProxyAttribute(Attribute, _Attribute, IContextAttribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CreateInstance(self, serverType: TypeType) -> MarshalByRefObject: ...
    
    def CreateProxy(self, objRef: ObjRef, serverType: TypeType, serverObject: ObjectType, serverContext: Context) -> RealProxy: ...
    
    def GetPropertiesForNewContext(self, msg: IConstructionCallMessage) -> VoidType: ...
    
    def IsContextOK(self, ctx: Context, msg: IConstructionCallMessage) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RealProxy(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CreateObjRef(self, requestedType: TypeType) -> ObjRef: ...
    
    def GetCOMIUnknown(self, fIsMarshalled: BooleanType) -> NIntType: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def GetProxiedType(self) -> TypeType: ...
    
    @staticmethod
    def GetStubData(rp: RealProxy) -> ObjectType: ...
    
    def GetTransparentProxy(self) -> ObjectType: ...
    
    def InitializeServerObject(self, ctorMsg: IConstructionCallMessage) -> IConstructionReturnMessage: ...
    
    def Invoke(self, msg: IMessage) -> IMessage: ...
    
    def SetCOMIUnknown(self, i: NIntType) -> VoidType: ...
    
    @staticmethod
    def SetStubData(rp: RealProxy, stubData: ObjectType) -> VoidType: ...
    
    def SupportsInterface(self, iid: Guid) -> Tuple[NIntType, Guid]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RemotingProxy(RealProxy, IRemotingTypeInfo):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, serverType: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeName(self) -> StringType: ...
    
    @TypeName.setter
    def TypeName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CanCastTo(self, castType: TypeType, o: ObjectType) -> BooleanType: ...
    
    def GetCOMIUnknown(self, fIsBeingMarshalled: BooleanType) -> NIntType: ...
    
    def Invoke(self, reqMsg: IMessage) -> IMessage: ...
    
    def SetCOMIUnknown(self, i: NIntType) -> VoidType: ...
    
    def get_TypeName(self) -> StringType: ...
    
    def set_TypeName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class MessageData(ValueType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Interfaces

# ---------- Enums ---------- #

class CallType(Enum):
    InvalidCall = 0
    MethodCall = 1
    ConstructorCall = 2


class RealProxyFlags(Enum):
    #None = 0
    RemotingProxy = 1
    Initialized = 2


# No Delegates

__all__ = [
    AgileAsyncWorkerItem,
    ProxyAttribute,
    RealProxy,
    RemotingProxy,
    MessageData,
    CallType,
    RealProxyFlags,
]
