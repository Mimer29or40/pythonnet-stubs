"""Automatically generated stubs for C# namespace: System.Runtime.Remoting.Proxies."""

from abc import ABC

from System import Attribute
from System import Enum
from System import Guid
from System import IntPtr
from System import MarshalByRefObject
from System import Object
from System import Type
from System import UInt32
from System import ValueType
from System.Runtime.InteropServices import _Attribute
from System.Runtime.Remoting import IRemotingTypeInfo
from System.Runtime.Remoting import ObjRef
from System.Runtime.Remoting.Activation import IConstructionCallMessage
from System.Runtime.Remoting.Activation import IConstructionReturnMessage
from System.Runtime.Remoting.Contexts import Context
from System.Runtime.Remoting.Contexts import IContextAttribute
from System.Runtime.Remoting.Messaging import AsyncResult
from System.Runtime.Remoting.Messaging import IMessage
from System.Runtime.Remoting.Messaging import IMethodCallMessage
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AgileAsyncWorkerItem(Object):
    """"""
    def __init__(self, message: IMethodCallMessage, ar: AsyncResult, target: object) -> None:
        """"""
    def DoAsyncCall(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ThreadPoolCallBack(cls, o: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CallType(Enum):
    """"""

    InvalidCall: CallType = ...
    """"""
    MethodCall: CallType = ...
    """"""
    ConstructorCall: CallType = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MessageData(ValueType):
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
class ProxyAttribute(Attribute, _Attribute, IContextAttribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def CreateInstance(self, serverType: Type) -> MarshalByRefObject:
        """"""
    def CreateProxy(
        self, objRef: ObjRef, serverType: Type, serverObject: object, serverContext: Context
    ) -> RealProxy:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetPropertiesForNewContext(self, msg: IConstructionCallMessage) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsContextOK(self, ctx: Context, msg: IConstructionCallMessage) -> bool:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RealProxy(ABC, Object):
    """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetCOMIUnknown(self, fIsMarshalled: bool) -> IntPtr:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetProxiedType(self) -> Type:
        """"""
    @classmethod
    def GetStubData(cls, rp: RealProxy) -> object:
        """"""
    def GetTransparentProxy(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeServerObject(
        self, ctorMsg: IConstructionCallMessage
    ) -> IConstructionReturnMessage:
        """"""
    def Invoke(self, msg: IMessage) -> IMessage:
        """"""
    def SetCOMIUnknown(self, i: IntPtr) -> None:
        """"""
    @classmethod
    def SetStubData(cls, rp: RealProxy, stubData: object) -> None:
        """"""
    def SupportsInterface(self, iid: Guid) -> IntPtr:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class RealProxyFlags(Enum):
    """"""

    _None: RealProxyFlags = ...
    """"""
    RemotingProxy: RealProxyFlags = ...
    """"""
    Initialized: RealProxyFlags = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RemotingProxy(RealProxy, IRemotingTypeInfo):
    """"""
    def __init__(self, serverType: Type) -> None:
        """"""
    @property
    def TypeName(self) -> str:
        """"""
    @TypeName.setter
    def TypeName(self, value: str) -> None: ...
    def CanCastTo(self, castType: Type, o: object) -> bool:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetCOMIUnknown(self, fIsBeingMarshalled: bool) -> IntPtr:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetProxiedType(self) -> Type:
        """"""
    def GetTransparentProxy(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeServerObject(
        self, ctorMsg: IConstructionCallMessage
    ) -> IConstructionReturnMessage:
        """"""
    def Invoke(self, reqMsg: IMessage) -> IMessage:
        """"""
    def SetCOMIUnknown(self, i: IntPtr) -> None:
        """"""
    def SupportsInterface(self, iid: Guid) -> IntPtr:
        """"""
    def ToString(self) -> str:
        """"""
