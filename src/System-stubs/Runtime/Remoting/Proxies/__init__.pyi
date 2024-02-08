from __future__ import annotations

from abc import ABC
from typing import Tuple

from System import Attribute
from System import Enum
from System import Guid
from System import IntPtr
from System import MarshalByRefObject
from System import Object
from System import Type
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

class AgileAsyncWorkerItem(Object):
    """"""

    def __init__(self, message: IMethodCallMessage, ar: AsyncResult, target: object):
        """

        :param message:
        :param ar:
        :param target:
        """
    def DoAsyncCall(self) -> None:
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
    def ThreadPoolCallBack(cls, o: object) -> None:
        """

        :param o:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CallType(Enum):
    """"""

    InvalidCall: CallType = ...
    """"""
    MethodCall: CallType = ...
    """"""
    ConstructorCall: CallType = ...
    """"""

class MessageData(ValueType):
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

class ProxyAttribute(Attribute, _Attribute, IContextAttribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    def CreateInstance(self, serverType: Type) -> MarshalByRefObject:
        """

        :param serverType:
        :return:
        """
    def CreateProxy(
        self, objRef: ObjRef, serverType: Type, serverObject: object, serverContext: Context
    ) -> RealProxy:
        """

        :param objRef:
        :param serverType:
        :param serverObject:
        :param serverContext:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetPropertiesForNewContext(self, msg: IConstructionCallMessage) -> None:
        """

        :param msg:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsContextOK(self, ctx: Context, msg: IConstructionCallMessage) -> bool:
        """

        :param ctx:
        :param msg:
        :return:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class RealProxy(ABC, Object):
    """"""

    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetCOMIUnknown(self, fIsMarshalled: bool) -> IntPtr:
        """

        :param fIsMarshalled:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetProxiedType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def GetStubData(cls, rp: RealProxy) -> object:
        """

        :param rp:
        :return:
        """
    def GetTransparentProxy(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeServerObject(
        self, ctorMsg: IConstructionCallMessage
    ) -> IConstructionReturnMessage:
        """

        :param ctorMsg:
        :return:
        """
    def Invoke(self, msg: IMessage) -> IMessage:
        """

        :param msg:
        :return:
        """
    def SetCOMIUnknown(self, i: IntPtr) -> None:
        """

        :param i:
        """
    @classmethod
    def SetStubData(cls, rp: RealProxy, stubData: object) -> None:
        """

        :param rp:
        :param stubData:
        """
    def SupportsInterface(self, iid: Guid) -> IntPtr:
        """

        :param iid:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class RealProxyFlags(Enum):
    """"""

    _None: RealProxyFlags = ...
    """"""
    RemotingProxy: RealProxyFlags = ...
    """"""
    Initialized: RealProxyFlags = ...
    """"""

class RemotingProxy(RealProxy, IRemotingTypeInfo):
    """"""

    def __init__(self, serverType: Type):
        """

        :param serverType:
        """
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    @TypeName.setter
    def TypeName(self, value: str) -> None: ...
    def CanCastTo(self, fromType: Type, o: object) -> bool:
        """

        :param fromType:
        :param o:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetCOMIUnknown(self, fIsMarshalled: bool) -> IntPtr:
        """

        :param fIsMarshalled:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetProxiedType(self) -> Type:
        """

        :return:
        """
    def GetTransparentProxy(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeServerObject(
        self, ctorMsg: IConstructionCallMessage
    ) -> IConstructionReturnMessage:
        """

        :param ctorMsg:
        :return:
        """
    def Invoke(self, msg: IMessage) -> IMessage:
        """

        :param msg:
        :return:
        """
    def SetCOMIUnknown(self, i: IntPtr) -> None:
        """

        :param i:
        """
    def SupportsInterface(self, iid: Guid) -> IntPtr:
        """

        :param iid:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
