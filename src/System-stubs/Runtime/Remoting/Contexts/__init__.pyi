from __future__ import annotations

from typing import Callable
from typing import ClassVar
from typing import Final
from typing import Tuple
from typing import overload

from System import Array
from System import Attribute
from System import ContextBoundObject
from System import Guid
from System import IntPtr
from System import LocalDataStoreSlot
from System import MarshalByRefObject
from System import Object
from System import Type
from System.Runtime.InteropServices import _Attribute
from System.Runtime.Remoting.Activation import IConstructionCallMessage
from System.Runtime.Remoting.Activation import IConstructionReturnMessage
from System.Runtime.Remoting.Messaging import IMessage
from System.Runtime.Remoting.Messaging import IMessageCtrl
from System.Runtime.Remoting.Messaging import IMessageSink
from System.Runtime.Remoting.Messaging import InternalSink

class ArrayWithSize(Object):
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

class CallBackHelper(Object):
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

class Context(Object):
    """"""

    def __init__(self):
        """"""
    @property
    def ContextID(self) -> int:
        """

        :return:
        """
    @property
    def ContextProperties(self) -> Array[IContextProperty]:
        """

        :return:
        """
    @classmethod
    @property
    def DefaultContext(cls) -> Context:
        """

        :return:
        """
    @classmethod
    def AllocateDataSlot(cls) -> LocalDataStoreSlot:
        """

        :return:
        """
    @classmethod
    def AllocateNamedDataSlot(cls, name: str) -> LocalDataStoreSlot:
        """

        :param name:
        :return:
        """
    def DoCallBack(self, deleg: CrossContextDelegate) -> None:
        """

        :param deleg:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def FreeNamedDataSlot(cls, name: str) -> None:
        """

        :param name:
        """
    def Freeze(self) -> None:
        """"""
    @classmethod
    def GetData(cls, slot: LocalDataStoreSlot) -> object:
        """

        :param slot:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    def GetNamedDataSlot(cls, name: str) -> LocalDataStoreSlot:
        """

        :param name:
        :return:
        """
    def GetProperty(self, name: str) -> IContextProperty:
        """

        :param name:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def RegisterDynamicProperty(
        cls, prop: IDynamicProperty, obj: ContextBoundObject, ctx: Context
    ) -> bool:
        """

        :param prop:
        :param obj:
        :param ctx:
        :return:
        """
    @classmethod
    def SetData(cls, slot: LocalDataStoreSlot, data: object) -> None:
        """

        :param slot:
        :param data:
        """
    def SetProperty(self, prop: IContextProperty) -> None:
        """

        :param prop:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def UnregisterDynamicProperty(cls, name: str, obj: ContextBoundObject, ctx: Context) -> bool:
        """

        :param name:
        :param obj:
        :param ctx:
        :return:
        """

class ContextAttribute(Attribute, _Attribute, IContextAttribute, IContextProperty):
    """"""

    def __init__(self, name: str):
        """

        :param name:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Freeze(self, newContext: Context) -> None:
        """

        :param newContext:
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
    def IsNewContextOK(self, newCtx: Context) -> bool:
        """

        :param newCtx:
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

class ContextProperty(Object):
    """"""

    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Property(self) -> object:
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

CrossContextDelegate: Callable[[], None] = ...
""""""

class DynamicPropertyHolder(Object):
    """"""

    def __init__(self):
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

class IContextAttribute:
    """"""

    def GetPropertiesForNewContext(self, msg: IConstructionCallMessage) -> None:
        """

        :param msg:
        """
    def IsContextOK(self, ctx: Context, msg: IConstructionCallMessage) -> bool:
        """

        :param ctx:
        :param msg:
        :return:
        """

class IContextProperty:
    """"""

    @property
    def Name(self) -> str:
        """

        :return:
        """
    def Freeze(self, newContext: Context) -> None:
        """

        :param newContext:
        """
    def IsNewContextOK(self, newCtx: Context) -> bool:
        """

        :param newCtx:
        :return:
        """

class IContextPropertyActivator:
    """"""

    def CollectFromClientContext(self, msg: IConstructionCallMessage) -> None:
        """

        :param msg:
        """
    def CollectFromServerContext(self, msg: IConstructionReturnMessage) -> None:
        """

        :param msg:
        """
    def DeliverClientContextToServerContext(self, msg: IConstructionCallMessage) -> bool:
        """

        :param msg:
        :return:
        """
    def DeliverServerContextToClientContext(self, msg: IConstructionReturnMessage) -> bool:
        """

        :param msg:
        :return:
        """
    def IsOKToActivate(self, msg: IConstructionCallMessage) -> bool:
        """

        :param msg:
        :return:
        """

class IContributeClientContextSink:
    """"""

    def GetClientContextSink(self, nextSink: IMessageSink) -> IMessageSink:
        """

        :param nextSink:
        :return:
        """

class IContributeDynamicSink:
    """"""

    def GetDynamicSink(self) -> IDynamicMessageSink:
        """

        :return:
        """

class IContributeEnvoySink:
    """"""

    def GetEnvoySink(self, obj: MarshalByRefObject, nextSink: IMessageSink) -> IMessageSink:
        """

        :param obj:
        :param nextSink:
        :return:
        """

class IContributeObjectSink:
    """"""

    def GetObjectSink(self, obj: MarshalByRefObject, nextSink: IMessageSink) -> IMessageSink:
        """

        :param obj:
        :param nextSink:
        :return:
        """

class IContributeServerContextSink:
    """"""

    def GetServerContextSink(self, nextSink: IMessageSink) -> IMessageSink:
        """

        :param nextSink:
        :return:
        """

class IDynamicMessageSink:
    """"""

    def ProcessMessageFinish(self, replyMsg: IMessage, bCliSide: bool, bAsync: bool) -> None:
        """

        :param replyMsg:
        :param bCliSide:
        :param bAsync:
        """
    def ProcessMessageStart(self, reqMsg: IMessage, bCliSide: bool, bAsync: bool) -> None:
        """

        :param reqMsg:
        :param bCliSide:
        :param bAsync:
        """

class IDynamicProperty:
    """"""

    @property
    def Name(self) -> str:
        """

        :return:
        """

class SynchronizationAttribute(
    ContextAttribute,
    _Attribute,
    IContextAttribute,
    IContextProperty,
    IContributeClientContextSink,
    IContributeServerContextSink,
):
    """"""

    NOT_SUPPORTED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    REQUIRED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    REQUIRES_NEW: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SUPPORTED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, reEntrant: bool):
        """

        :param reEntrant:
        """
    @overload
    def __init__(self, flag: int):
        """

        :param flag:
        """
    @overload
    def __init__(self, flag: int, reEntrant: bool):
        """

        :param flag:
        :param reEntrant:
        """
    @property
    def IsReEntrant(self) -> bool:
        """

        :return:
        """
    @property
    def Locked(self) -> bool:
        """

        :return:
        """
    @Locked.setter
    def Locked(self, value: bool) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Freeze(self, newContext: Context) -> None:
        """

        :param newContext:
        """
    def GetClientContextSink(self, nextSink: IMessageSink) -> IMessageSink:
        """

        :param nextSink:
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
    def GetServerContextSink(self, nextSink: IMessageSink) -> IMessageSink:
        """

        :param nextSink:
        :return:
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
    def IsNewContextOK(self, newCtx: Context) -> bool:
        """

        :param newCtx:
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

class SynchronizedClientContextSink(InternalSink, IMessageSink):
    """"""

    @property
    def NextSink(self) -> IMessageSink:
        """

        :return:
        """
    def AsyncProcessMessage(self, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl:
        """

        :param msg:
        :param replySink:
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
    def SyncProcessMessage(self, msg: IMessage) -> IMessage:
        """

        :param msg:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SynchronizedServerContextSink(InternalSink, IMessageSink):
    """"""

    @property
    def NextSink(self) -> IMessageSink:
        """

        :return:
        """
    def AsyncProcessMessage(self, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl:
        """

        :param msg:
        :param replySink:
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
    def SyncProcessMessage(self, msg: IMessage) -> IMessage:
        """

        :param msg:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class WorkItem(Object):
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
