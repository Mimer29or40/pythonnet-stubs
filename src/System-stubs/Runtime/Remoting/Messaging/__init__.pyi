from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import ClassVar
from typing import Final
from typing import Iterator
from typing import Tuple
from typing import overload

from System import Array
from System import AsyncCallback
from System import Attribute
from System import Exception
from System import Guid
from System import IAsyncResult
from System import ICloneable
from System import IntPtr
from System import MarshalByRefObject
from System import Object
from System import RuntimeMethodHandle
from System import Type
from System.Collections import DictionaryEntry
from System.Collections import ICollection
from System.Collections import IDictionary
from System.Collections import IDictionaryEnumerator
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IList
from System.IO import Stream
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Attribute
from System.Runtime.Remoting import Identity
from System.Runtime.Remoting import ObjRef
from System.Runtime.Remoting import ServerIdentity
from System.Runtime.Remoting.Activation import IActivator
from System.Runtime.Remoting.Activation import IConstructionCallMessage
from System.Runtime.Remoting.Activation import IConstructionReturnMessage
from System.Runtime.Serialization import IFormatter
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import ISerializationSurrogate
from System.Runtime.Serialization import ISurrogateSelector
from System.Runtime.Serialization import SerializationBinder
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Runtime.Serialization.Formatters import IFieldInfo
from System.Threading import WaitHandle

class ArgMapper(Object):
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

class AsyncReplySink(Object, IMessageSink):
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

class AsyncResult(Object, IMessageSink, IAsyncResult):
    """"""

    @property
    def AsyncDelegate(self) -> object:
        """

        :return:
        """
    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @property
    def EndInvokeCalled(self) -> bool:
        """

        :return:
        """
    @EndInvokeCalled.setter
    def EndInvokeCalled(self, value: bool) -> None: ...
    @property
    def IsCompleted(self) -> bool:
        """

        :return:
        """
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
    def GetReplyMessage(self) -> IMessage:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def SetMessageCtrl(self, mc: IMessageCtrl) -> None:
        """

        :param mc:
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

class CCMDictionary(MessageDictionary, ICollection, IDictionary, IEnumerable):
    """"""

    CCMkeys: Final[ClassVar[Array[str]]] = ...
    """
    
    :return: 
    """
    def __init__(self, msg: IConstructionCallMessage, idict: IDictionary):
        """

        :param msg:
        :param idict:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection:
        """

        :return:
        """
    def Add(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, key: object) -> bool:
        """

        :param key:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def Remove(self, key: object) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, key: object) -> object:
        """

        :param key:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class CRMDictionary(MessageDictionary, ICollection, IDictionary, IEnumerable):
    """"""

    CRMkeysFault: Final[ClassVar[Array[str]]] = ...
    """
    
    :return: 
    """
    CRMkeysNoFault: Final[ClassVar[Array[str]]] = ...
    """
    
    :return: 
    """
    def __init__(self, msg: IConstructionReturnMessage, idict: IDictionary):
        """

        :param msg:
        :param idict:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection:
        """

        :return:
        """
    def Add(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, key: object) -> bool:
        """

        :param key:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def Remove(self, key: object) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, key: object) -> object:
        """

        :param key:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class CallContext(Object):
    """"""

    @classmethod
    @property
    def HostContext(cls) -> object:
        """

        :return:
        """
    @classmethod
    @HostContext.setter
    def HostContext(cls, value: object) -> None: ...
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
    @classmethod
    def GetData(cls, name: str) -> object:
        """

        :param name:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    def GetHeaders(cls) -> Array[Header]:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def LogicalGetData(cls, name: str) -> object:
        """

        :param name:
        :return:
        """
    @classmethod
    def LogicalSetData(cls, name: str, data: object) -> None:
        """

        :param name:
        :param data:
        """
    @classmethod
    def SetData(cls, name: str, data: object) -> None:
        """

        :param name:
        :param data:
        """
    @classmethod
    def SetHeaders(cls, headers: Array[Header]) -> None:
        """

        :param headers:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CallContextRemotingData(Object, ICloneable):
    """"""

    def __init__(self):
        """"""
    def Clone(self) -> object:
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

class CallContextSecurityData(Object, ICloneable):
    """"""

    def __init__(self):
        """"""
    def Clone(self) -> object:
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

class ClientAsyncReplyTerminatorSink(Object, IMessageSink):
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

class ClientContextTerminatorSink(InternalSink, IMessageSink):
    """"""

    def __init__(self):
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

class ConstructionCall(
    MethodCall,
    IConstructionCallMessage,
    IInternalMessage,
    IMessage,
    IMethodCallMessage,
    IMethodMessage,
    ISerializationRootObject,
    ISerializable,
):
    """"""

    @overload
    def __init__(self, m: IMessage):
        """

        :param m:
        """
    @overload
    def __init__(self, headers: Array[Header]):
        """

        :param headers:
        """
    @property
    def ActivationType(self) -> Type:
        """

        :return:
        """
    @property
    def ActivationTypeName(self) -> str:
        """

        :return:
        """
    @property
    def Activator(self) -> IActivator:
        """

        :return:
        """
    @Activator.setter
    def Activator(self, value: IActivator) -> None: ...
    @property
    def ArgCount(self) -> int:
        """

        :return:
        """
    @property
    def Args(self) -> Array[object]:
        """

        :return:
        """
    @property
    def CallSiteActivationAttributes(self) -> Array[object]:
        """

        :return:
        """
    @property
    def ContextProperties(self) -> IList:
        """

        :return:
        """
    @property
    def HasVarArgs(self) -> bool:
        """

        :return:
        """
    @property
    def IdentityObject(self) -> Identity:
        """

        :return:
        """
    @IdentityObject.setter
    def IdentityObject(self, value: Identity) -> None: ...
    @property
    def InArgCount(self) -> int:
        """

        :return:
        """
    @property
    def InArgs(self) -> Array[object]:
        """

        :return:
        """
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """

        :return:
        """
    @property
    def MethodBase(self) -> MethodBase:
        """

        :return:
        """
    @property
    def MethodName(self) -> str:
        """

        :return:
        """
    @property
    def MethodSignature(self) -> object:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """
    @property
    def ServerIdentityObject(self) -> ServerIdentity:
        """

        :return:
        """
    @ServerIdentityObject.setter
    def ServerIdentityObject(self, value: ServerIdentity) -> None: ...
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    @property
    def Uri(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetInArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetInArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def HasProperties(self) -> bool:
        """

        :return:
        """
    def HeaderHandler(self, h: Array[Header]) -> object:
        """

        :param h:
        :return:
        """
    def Init(self) -> None:
        """"""
    def ResolveMethod(self) -> None:
        """"""
    def RootSetObjectData(self, info: SerializationInfo, ctx: StreamingContext) -> None:
        """

        :param info:
        :param ctx:
        """
    def SetCallContext(self, callContext: LogicalCallContext) -> None:
        """

        :param callContext:
        """
    def SetURI(self, uri: str) -> None:
        """

        :param uri:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ConstructionResponse(
    MethodResponse,
    IConstructionReturnMessage,
    IInternalMessage,
    IMessage,
    IMethodMessage,
    IMethodReturnMessage,
    ISerializationRootObject,
    ISerializable,
):
    """"""

    def __init__(self, h: Array[Header], mcm: IMethodCallMessage):
        """

        :param h:
        :param mcm:
        """
    @property
    def ArgCount(self) -> int:
        """

        :return:
        """
    @property
    def Args(self) -> Array[object]:
        """

        :return:
        """
    @property
    def Exception(self) -> Exception:
        """

        :return:
        """
    @property
    def HasVarArgs(self) -> bool:
        """

        :return:
        """
    @property
    def IdentityObject(self) -> Identity:
        """

        :return:
        """
    @IdentityObject.setter
    def IdentityObject(self, value: Identity) -> None: ...
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """

        :return:
        """
    @property
    def MethodBase(self) -> MethodBase:
        """

        :return:
        """
    @property
    def MethodName(self) -> str:
        """

        :return:
        """
    @property
    def MethodSignature(self) -> object:
        """

        :return:
        """
    @property
    def OutArgCount(self) -> int:
        """

        :return:
        """
    @property
    def OutArgs(self) -> Array[object]:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """
    @property
    def ReturnValue(self) -> object:
        """

        :return:
        """
    @property
    def ServerIdentityObject(self) -> ServerIdentity:
        """

        :return:
        """
    @ServerIdentityObject.setter
    def ServerIdentityObject(self, value: ServerIdentity) -> None: ...
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    @property
    def Uri(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetArgName(self, index: int) -> str:
        """

        :param index:
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
    def GetOutArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetOutArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def HasProperties(self) -> bool:
        """

        :return:
        """
    def HeaderHandler(self, h: Array[Header]) -> object:
        """

        :param h:
        :return:
        """
    def RootSetObjectData(self, info: SerializationInfo, ctx: StreamingContext) -> None:
        """

        :param info:
        :param ctx:
        """
    def SetCallContext(self, callContext: LogicalCallContext) -> None:
        """

        :param callContext:
        """
    def SetURI(self, uri: str) -> None:
        """

        :param uri:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ConstructorCallMessage(
    Object, IConstructionCallMessage, IMessage, IMethodCallMessage, IMethodMessage
):
    """"""

    @property
    def ActivationType(self) -> Type:
        """

        :return:
        """
    @property
    def ActivationTypeName(self) -> str:
        """

        :return:
        """
    @property
    def Activator(self) -> IActivator:
        """

        :return:
        """
    @Activator.setter
    def Activator(self, value: IActivator) -> None: ...
    @property
    def ArgCount(self) -> int:
        """

        :return:
        """
    @property
    def Args(self) -> Array[object]:
        """

        :return:
        """
    @property
    def CallSiteActivationAttributes(self) -> Array[object]:
        """

        :return:
        """
    @property
    def ContextProperties(self) -> IList:
        """

        :return:
        """
    @property
    def HasVarArgs(self) -> bool:
        """

        :return:
        """
    @property
    def InArgCount(self) -> int:
        """

        :return:
        """
    @property
    def InArgs(self) -> Array[object]:
        """

        :return:
        """
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """

        :return:
        """
    @property
    def MethodBase(self) -> MethodBase:
        """

        :return:
        """
    @property
    def MethodName(self) -> str:
        """

        :return:
        """
    @property
    def MethodSignature(self) -> object:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    @property
    def Uri(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetInArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetInArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    def GetThisPtr(self) -> object:
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

class ConstructorReturnMessage(
    ReturnMessage, IConstructionReturnMessage, IMessage, IMethodMessage, IMethodReturnMessage
):
    """"""

    @overload
    def __init__(self, e: Exception, ccm: IConstructionCallMessage):
        """

        :param e:
        :param ccm:
        """
    @overload
    def __init__(
        self,
        o: MarshalByRefObject,
        outArgs: Array[object],
        outArgsCount: int,
        callCtx: LogicalCallContext,
        ccm: IConstructionCallMessage,
    ):
        """

        :param o:
        :param outArgs:
        :param outArgsCount:
        :param callCtx:
        :param ccm:
        """
    @property
    def ArgCount(self) -> int:
        """

        :return:
        """
    @property
    def Args(self) -> Array[object]:
        """

        :return:
        """
    @property
    def Exception(self) -> Exception:
        """

        :return:
        """
    @property
    def HasVarArgs(self) -> bool:
        """

        :return:
        """
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """

        :return:
        """
    @property
    def MethodBase(self) -> MethodBase:
        """

        :return:
        """
    @property
    def MethodName(self) -> str:
        """

        :return:
        """
    @property
    def MethodSignature(self) -> object:
        """

        :return:
        """
    @property
    def OutArgCount(self) -> int:
        """

        :return:
        """
    @property
    def OutArgs(self) -> Array[object]:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """
    @property
    def ReturnValue(self) -> object:
        """

        :return:
        """
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    @property
    def Uri(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetOutArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetOutArgName(self, index: int) -> str:
        """

        :param index:
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

class DisposeSink(Object, IMessageSink):
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

class EnvoyTerminatorSink(InternalSink, IMessageSink):
    """"""

    def __init__(self):
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

class ErrorMessage(Object, IMessage, IMethodCallMessage, IMethodMessage):
    """"""

    def __init__(self):
        """"""
    @property
    def ArgCount(self) -> int:
        """

        :return:
        """
    @property
    def Args(self) -> Array[object]:
        """

        :return:
        """
    @property
    def HasVarArgs(self) -> bool:
        """

        :return:
        """
    @property
    def InArgCount(self) -> int:
        """

        :return:
        """
    @property
    def InArgs(self) -> Array[object]:
        """

        :return:
        """
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """

        :return:
        """
    @property
    def MethodBase(self) -> MethodBase:
        """

        :return:
        """
    @property
    def MethodName(self) -> str:
        """

        :return:
        """
    @property
    def MethodSignature(self) -> object:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    @property
    def Uri(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetInArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetInArgName(self, index: int) -> str:
        """

        :param index:
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

class Header(Object):
    """"""

    HeaderNamespace: Final[str] = ...
    """
    
    :return: 
    """
    MustUnderstand: Final[bool] = ...
    """
    
    :return: 
    """
    Name: Final[str] = ...
    """
    
    :return: 
    """
    Value: Final[object] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, _Name: str, _Value: object):
        """

        :param _Name:
        :param _Value:
        """
    @overload
    def __init__(self, _Name: str, _Value: object, _MustUnderstand: bool):
        """

        :param _Name:
        :param _Value:
        :param _MustUnderstand:
        """
    @overload
    def __init__(self, _Name: str, _Value: object, _MustUnderstand: bool, _HeaderNamespace: str):
        """

        :param _Name:
        :param _Value:
        :param _MustUnderstand:
        :param _HeaderNamespace:
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

HeaderHandler: Callable[[Array[Header]], object] = ...
"""

:param headers: 
:return: 
"""

class IInternalMessage:
    """"""

    @property
    def IdentityObject(self) -> Identity:
        """

        :return:
        """
    @IdentityObject.setter
    def IdentityObject(self, value: Identity) -> None: ...
    @property
    def ServerIdentityObject(self) -> ServerIdentity:
        """

        :return:
        """
    @ServerIdentityObject.setter
    def ServerIdentityObject(self, value: ServerIdentity) -> None: ...
    def HasProperties(self) -> bool:
        """

        :return:
        """
    def SetCallContext(self, callContext: LogicalCallContext) -> None:
        """

        :param callContext:
        """
    def SetURI(self, uri: str) -> None:
        """

        :param uri:
        """

class ILogicalThreadAffinative:
    """"""

class IMessage:
    """"""

    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """

class IMessageCtrl:
    """"""

    def Cancel(self, msToCancel: int) -> None:
        """

        :param msToCancel:
        """

class IMessageSink:
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
    def SyncProcessMessage(self, msg: IMessage) -> IMessage:
        """

        :param msg:
        :return:
        """

class IMethodCallMessage(IMessage, IMethodMessage):
    """"""

    @property
    def ArgCount(self) -> int:
        """

        :return:
        """
    @property
    def Args(self) -> Array[object]:
        """

        :return:
        """
    @property
    def HasVarArgs(self) -> bool:
        """

        :return:
        """
    @property
    def InArgCount(self) -> int:
        """

        :return:
        """
    @property
    def InArgs(self) -> Array[object]:
        """

        :return:
        """
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """

        :return:
        """
    @property
    def MethodBase(self) -> MethodBase:
        """

        :return:
        """
    @property
    def MethodName(self) -> str:
        """

        :return:
        """
    @property
    def MethodSignature(self) -> object:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    @property
    def Uri(self) -> str:
        """

        :return:
        """
    def GetArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    def GetInArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetInArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """

class IMethodMessage(IMessage):
    """"""

    @property
    def ArgCount(self) -> int:
        """

        :return:
        """
    @property
    def Args(self) -> Array[object]:
        """

        :return:
        """
    @property
    def HasVarArgs(self) -> bool:
        """

        :return:
        """
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """

        :return:
        """
    @property
    def MethodBase(self) -> MethodBase:
        """

        :return:
        """
    @property
    def MethodName(self) -> str:
        """

        :return:
        """
    @property
    def MethodSignature(self) -> object:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    @property
    def Uri(self) -> str:
        """

        :return:
        """
    def GetArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """

class IMethodReturnMessage(IMessage, IMethodMessage):
    """"""

    @property
    def ArgCount(self) -> int:
        """

        :return:
        """
    @property
    def Args(self) -> Array[object]:
        """

        :return:
        """
    @property
    def Exception(self) -> Exception:
        """

        :return:
        """
    @property
    def HasVarArgs(self) -> bool:
        """

        :return:
        """
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """

        :return:
        """
    @property
    def MethodBase(self) -> MethodBase:
        """

        :return:
        """
    @property
    def MethodName(self) -> str:
        """

        :return:
        """
    @property
    def MethodSignature(self) -> object:
        """

        :return:
        """
    @property
    def OutArgCount(self) -> int:
        """

        :return:
        """
    @property
    def OutArgs(self) -> Array[object]:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """
    @property
    def ReturnValue(self) -> object:
        """

        :return:
        """
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    @property
    def Uri(self) -> str:
        """

        :return:
        """
    def GetArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    def GetOutArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetOutArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """

class IRemotingFormatter(IFormatter):
    """"""

    @property
    def Binder(self) -> SerializationBinder:
        """

        :return:
        """
    @Binder.setter
    def Binder(self, value: SerializationBinder) -> None: ...
    @property
    def Context(self) -> StreamingContext:
        """

        :return:
        """
    @Context.setter
    def Context(self, value: StreamingContext) -> None: ...
    @property
    def SurrogateSelector(self) -> ISurrogateSelector:
        """

        :return:
        """
    @SurrogateSelector.setter
    def SurrogateSelector(self, value: ISurrogateSelector) -> None: ...
    @overload
    def Deserialize(self, serializationStream: Stream) -> object:
        """

        :param serializationStream:
        :return:
        """
    @overload
    def Deserialize(self, serializationStream: Stream, handler: HeaderHandler) -> object:
        """

        :param serializationStream:
        :param handler:
        :return:
        """
    @overload
    def Serialize(self, serializationStream: Stream, graph: object) -> None:
        """

        :param serializationStream:
        :param graph:
        """
    @overload
    def Serialize(self, serializationStream: Stream, graph: object, headers: Array[Header]) -> None:
        """

        :param serializationStream:
        :param graph:
        :param headers:
        """

class ISerializationRootObject:
    """"""

    def RootSetObjectData(self, info: SerializationInfo, ctx: StreamingContext) -> None:
        """

        :param info:
        :param ctx:
        """

class IllogicalCallContext(Object):
    """"""

    def __init__(self):
        """"""
    def CreateCopy(self) -> IllogicalCallContext:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FreeNamedDataSlot(self, name: str) -> None:
        """

        :param name:
        """
    def GetData(self, name: str) -> object:
        """

        :param name:
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
    def SetData(self, name: str, data: object) -> None:
        """

        :param name:
        :param data:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class InternalMessageWrapper(Object):
    """"""

    def __init__(self, msg: IMessage):
        """

        :param msg:
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

class InternalSink(Object):
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

class LogicalCallContext(Object, ISerializable, ICloneable):
    """"""

    @property
    def HasInfo(self) -> bool:
        """

        :return:
        """
    def Clone(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FreeNamedDataSlot(self, name: str) -> None:
        """

        :param name:
        """
    def GetData(self, name: str) -> object:
        """

        :param name:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def SetData(self, name: str, data: object) -> None:
        """

        :param name:
        :param data:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class MCMDictionary(MessageDictionary, ICollection, IDictionary, IEnumerable):
    """"""

    MCMkeys: Final[ClassVar[Array[str]]] = ...
    """
    
    :return: 
    """
    def __init__(self, msg: IMethodCallMessage, idict: IDictionary):
        """

        :param msg:
        :param idict:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection:
        """

        :return:
        """
    def Add(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, key: object) -> bool:
        """

        :param key:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def Remove(self, key: object) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, key: object) -> object:
        """

        :param key:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class MRMDictionary(MessageDictionary, ICollection, IDictionary, IEnumerable):
    """"""

    MCMkeysFault: Final[ClassVar[Array[str]]] = ...
    """
    
    :return: 
    """
    MCMkeysNoFault: Final[ClassVar[Array[str]]] = ...
    """
    
    :return: 
    """
    def __init__(self, msg: IMethodReturnMessage, idict: IDictionary):
        """

        :param msg:
        :param idict:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection:
        """

        :return:
        """
    def Add(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, key: object) -> bool:
        """

        :param key:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def Remove(self, key: object) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, key: object) -> object:
        """

        :param key:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class Message(
    Object, IInternalMessage, IMessage, IMethodCallMessage, IMethodMessage, ISerializable
):
    """"""

    @property
    def ArgCount(self) -> int:
        """

        :return:
        """
    @property
    def Args(self) -> Array[object]:
        """

        :return:
        """
    @property
    def HasVarArgs(self) -> bool:
        """

        :return:
        """
    @property
    def IdentityObject(self) -> Identity:
        """

        :return:
        """
    @IdentityObject.setter
    def IdentityObject(self, value: Identity) -> None: ...
    @property
    def InArgCount(self) -> int:
        """

        :return:
        """
    @property
    def InArgs(self) -> Array[object]:
        """

        :return:
        """
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """

        :return:
        """
    @property
    def MethodBase(self) -> MethodBase:
        """

        :return:
        """
    @property
    def MethodName(self) -> str:
        """

        :return:
        """
    @property
    def MethodSignature(self) -> object:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """
    @property
    def ServerIdentityObject(self) -> ServerIdentity:
        """

        :return:
        """
    @ServerIdentityObject.setter
    def ServerIdentityObject(self, value: ServerIdentity) -> None: ...
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    @property
    def Uri(self) -> str:
        """

        :return:
        """
    @classmethod
    def DebugOut(cls, s: str) -> None:
        """

        :param s:
        """
    def Dispatch(self, target: object) -> bool:
        """

        :param target:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    def GetAsyncBeginInfo(
        self, acbd: AsyncCallback, state: object
    ) -> Tuple[None, AsyncCallback, object]:
        """

        :param acbd:
        :param state:
        """
    def GetAsyncResult(self) -> IAsyncResult:
        """

        :return:
        """
    def GetCallType(self) -> int:
        """

        :return:
        """
    def GetFault(self) -> Exception:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetInArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetInArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetReturnValue(self) -> object:
        """

        :return:
        """
    def GetThisPtr(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def HasProperties(self) -> bool:
        """

        :return:
        """
    def Init(self) -> None:
        """"""
    def PropagateOutParameters(self, OutArgs: Array[object], retVal: object) -> None:
        """

        :param OutArgs:
        :param retVal:
        """
    def SetCallContext(self, callContext: LogicalCallContext) -> None:
        """

        :param callContext:
        """
    def SetFault(self, e: Exception) -> None:
        """

        :param e:
        """
    def SetURI(self, uri: str) -> None:
        """

        :param uri:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class MessageDictionary(ABC, Object, ICollection, IDictionary, IEnumerable):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection:
        """

        :return:
        """
    def Add(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, key: object) -> bool:
        """

        :param key:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def Remove(self, key: object) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, key: object) -> object:
        """

        :param key:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class MessageDictionaryEnumerator(Object, IDictionaryEnumerator, IEnumerator):
    """"""

    def __init__(self, md: MessageDictionary, hashtable: IDictionary):
        """

        :param md:
        :param hashtable:
        """
    @property
    def Current(self) -> object:
        """

        :return:
        """
    @property
    def Entry(self) -> DictionaryEntry:
        """

        :return:
        """
    @property
    def Key(self) -> object:
        """

        :return:
        """
    @property
    def Value(self) -> object:
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
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class MessageSmuggler(Object):
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

class MessageSurrogate(Object, ISerializationSurrogate):
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
    def GetObjectData(
        self, obj: object, info: SerializationInfo, context: StreamingContext
    ) -> None:
        """

        :param obj:
        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def SetObjectData(
        self,
        obj: object,
        info: SerializationInfo,
        context: StreamingContext,
        selector: ISurrogateSelector,
    ) -> object:
        """

        :param obj:
        :param info:
        :param context:
        :param selector:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

MessageSurrogateFilter: Callable[[str, object], bool] = ...
"""

:param key: 
:param value: 
:return: 
"""

class MethodCall(
    Object,
    IInternalMessage,
    IMessage,
    IMethodCallMessage,
    IMethodMessage,
    ISerializationRootObject,
    ISerializable,
):
    """"""

    @overload
    def __init__(self, msg: IMessage):
        """

        :param msg:
        """
    @overload
    def __init__(self, h1: Array[Header]):
        """

        :param h1:
        """
    @property
    def ArgCount(self) -> int:
        """

        :return:
        """
    @property
    def Args(self) -> Array[object]:
        """

        :return:
        """
    @property
    def HasVarArgs(self) -> bool:
        """

        :return:
        """
    @property
    def IdentityObject(self) -> Identity:
        """

        :return:
        """
    @IdentityObject.setter
    def IdentityObject(self, value: Identity) -> None: ...
    @property
    def InArgCount(self) -> int:
        """

        :return:
        """
    @property
    def InArgs(self) -> Array[object]:
        """

        :return:
        """
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """

        :return:
        """
    @property
    def MethodBase(self) -> MethodBase:
        """

        :return:
        """
    @property
    def MethodName(self) -> str:
        """

        :return:
        """
    @property
    def MethodSignature(self) -> object:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """
    @property
    def ServerIdentityObject(self) -> ServerIdentity:
        """

        :return:
        """
    @ServerIdentityObject.setter
    def ServerIdentityObject(self, value: ServerIdentity) -> None: ...
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    @property
    def Uri(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetInArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetInArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def HasProperties(self) -> bool:
        """

        :return:
        """
    def HeaderHandler(self, h: Array[Header]) -> object:
        """

        :param h:
        :return:
        """
    def Init(self) -> None:
        """"""
    def ResolveMethod(self) -> None:
        """"""
    def RootSetObjectData(self, info: SerializationInfo, ctx: StreamingContext) -> None:
        """

        :param info:
        :param ctx:
        """
    def SetCallContext(self, callContext: LogicalCallContext) -> None:
        """

        :param callContext:
        """
    def SetURI(self, uri: str) -> None:
        """

        :param uri:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class MethodCallMessageWrapper(
    InternalMessageWrapper, IMessage, IMethodCallMessage, IMethodMessage
):
    """"""

    def __init__(self, msg: IMethodCallMessage):
        """

        :param msg:
        """
    @property
    def ArgCount(self) -> int:
        """

        :return:
        """
    @property
    def Args(self) -> Array[object]:
        """

        :return:
        """
    @property
    def HasVarArgs(self) -> bool:
        """

        :return:
        """
    @property
    def InArgCount(self) -> int:
        """

        :return:
        """
    @property
    def InArgs(self) -> Array[object]:
        """

        :return:
        """
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """

        :return:
        """
    @property
    def MethodBase(self) -> MethodBase:
        """

        :return:
        """
    @property
    def MethodName(self) -> str:
        """

        :return:
        """
    @property
    def MethodSignature(self) -> object:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    @property
    def Uri(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetInArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetInArgName(self, index: int) -> str:
        """

        :param index:
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

class MethodResponse(
    Object,
    IInternalMessage,
    IMessage,
    IMethodMessage,
    IMethodReturnMessage,
    ISerializationRootObject,
    ISerializable,
):
    """"""

    def __init__(self, h1: Array[Header], mcm: IMethodCallMessage):
        """

        :param h1:
        :param mcm:
        """
    @property
    def ArgCount(self) -> int:
        """

        :return:
        """
    @property
    def Args(self) -> Array[object]:
        """

        :return:
        """
    @property
    def Exception(self) -> Exception:
        """

        :return:
        """
    @property
    def HasVarArgs(self) -> bool:
        """

        :return:
        """
    @property
    def IdentityObject(self) -> Identity:
        """

        :return:
        """
    @IdentityObject.setter
    def IdentityObject(self, value: Identity) -> None: ...
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """

        :return:
        """
    @property
    def MethodBase(self) -> MethodBase:
        """

        :return:
        """
    @property
    def MethodName(self) -> str:
        """

        :return:
        """
    @property
    def MethodSignature(self) -> object:
        """

        :return:
        """
    @property
    def OutArgCount(self) -> int:
        """

        :return:
        """
    @property
    def OutArgs(self) -> Array[object]:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """
    @property
    def ReturnValue(self) -> object:
        """

        :return:
        """
    @property
    def ServerIdentityObject(self) -> ServerIdentity:
        """

        :return:
        """
    @ServerIdentityObject.setter
    def ServerIdentityObject(self, value: ServerIdentity) -> None: ...
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    @property
    def Uri(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetArgName(self, index: int) -> str:
        """

        :param index:
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
    def GetOutArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetOutArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def HasProperties(self) -> bool:
        """

        :return:
        """
    def HeaderHandler(self, h: Array[Header]) -> object:
        """

        :param h:
        :return:
        """
    def RootSetObjectData(self, info: SerializationInfo, ctx: StreamingContext) -> None:
        """

        :param info:
        :param ctx:
        """
    def SetCallContext(self, callContext: LogicalCallContext) -> None:
        """

        :param callContext:
        """
    def SetURI(self, uri: str) -> None:
        """

        :param uri:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class MethodReturnMessageWrapper(
    InternalMessageWrapper, IMessage, IMethodMessage, IMethodReturnMessage
):
    """"""

    def __init__(self, msg: IMethodReturnMessage):
        """

        :param msg:
        """
    @property
    def ArgCount(self) -> int:
        """

        :return:
        """
    @property
    def Args(self) -> Array[object]:
        """

        :return:
        """
    @property
    def Exception(self) -> Exception:
        """

        :return:
        """
    @property
    def HasVarArgs(self) -> bool:
        """

        :return:
        """
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """

        :return:
        """
    @property
    def MethodBase(self) -> MethodBase:
        """

        :return:
        """
    @property
    def MethodName(self) -> str:
        """

        :return:
        """
    @property
    def MethodSignature(self) -> object:
        """

        :return:
        """
    @property
    def OutArgCount(self) -> int:
        """

        :return:
        """
    @property
    def OutArgs(self) -> Array[object]:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """
    @property
    def ReturnValue(self) -> object:
        """

        :return:
        """
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    @property
    def Uri(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetOutArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetOutArgName(self, index: int) -> str:
        """

        :param index:
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

class ObjRefSurrogate(Object, ISerializationSurrogate):
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
    def GetObjectData(
        self, obj: object, info: SerializationInfo, context: StreamingContext
    ) -> None:
        """

        :param obj:
        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def SetObjectData(
        self,
        obj: object,
        info: SerializationInfo,
        context: StreamingContext,
        selector: ISurrogateSelector,
    ) -> object:
        """

        :param obj:
        :param info:
        :param context:
        :param selector:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class OneWayAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
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

class RemotingSurrogate(Object, ISerializationSurrogate):
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
    def GetObjectData(
        self, obj: object, info: SerializationInfo, context: StreamingContext
    ) -> None:
        """

        :param obj:
        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def SetObjectData(
        self,
        obj: object,
        info: SerializationInfo,
        context: StreamingContext,
        selector: ISurrogateSelector,
    ) -> object:
        """

        :param obj:
        :param info:
        :param context:
        :param selector:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class RemotingSurrogateSelector(Object, ISurrogateSelector):
    """"""

    def __init__(self):
        """"""
    @property
    def Filter(self) -> MessageSurrogateFilter:
        """

        :return:
        """
    @Filter.setter
    def Filter(self, value: MessageSurrogateFilter) -> None: ...
    def ChainSelector(self, selector: ISurrogateSelector) -> None:
        """

        :param selector:
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
    def GetNextSelector(self) -> ISurrogateSelector:
        """

        :return:
        """
    def GetRootObject(self) -> object:
        """

        :return:
        """
    def GetSurrogate(
        self, type: Type, context: StreamingContext, selector: ISurrogateSelector
    ) -> Tuple[ISerializationSurrogate, ISurrogateSelector]:
        """

        :param type:
        :param context:
        :param selector:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def SetRootObject(self, obj: object) -> None:
        """

        :param obj:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def UseSoapFormat(self) -> None:
        """"""

class ReturnMessage(Object, IMessage, IMethodMessage, IMethodReturnMessage):
    """"""

    @overload
    def __init__(self, e: Exception, mcm: IMethodCallMessage):
        """

        :param e:
        :param mcm:
        """
    @overload
    def __init__(
        self,
        ret: object,
        outArgs: Array[object],
        outArgsCount: int,
        callCtx: LogicalCallContext,
        mcm: IMethodCallMessage,
    ):
        """

        :param ret:
        :param outArgs:
        :param outArgsCount:
        :param callCtx:
        :param mcm:
        """
    @property
    def ArgCount(self) -> int:
        """

        :return:
        """
    @property
    def Args(self) -> Array[object]:
        """

        :return:
        """
    @property
    def Exception(self) -> Exception:
        """

        :return:
        """
    @property
    def HasVarArgs(self) -> bool:
        """

        :return:
        """
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """

        :return:
        """
    @property
    def MethodBase(self) -> MethodBase:
        """

        :return:
        """
    @property
    def MethodName(self) -> str:
        """

        :return:
        """
    @property
    def MethodSignature(self) -> object:
        """

        :return:
        """
    @property
    def OutArgCount(self) -> int:
        """

        :return:
        """
    @property
    def OutArgs(self) -> Array[object]:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """
    @property
    def ReturnValue(self) -> object:
        """

        :return:
        """
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    @property
    def Uri(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetOutArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetOutArgName(self, index: int) -> str:
        """

        :param index:
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

class SerializationMonkey(Object, IFieldInfo, ISerializable):
    """"""

    @property
    def FieldNames(self) -> Array[str]:
        """

        :return:
        """
    @FieldNames.setter
    def FieldNames(self, value: Array[str]) -> None: ...
    @property
    def FieldTypes(self) -> Array[Type]:
        """

        :return:
        """
    @FieldTypes.setter
    def FieldTypes(self, value: Array[Type]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ServerContextTerminatorSink(InternalSink, IMessageSink):
    """"""

    def __init__(self):
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

class ServerObjectTerminatorSink(InternalSink, IMessageSink):
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

class SmuggledMethodCallMessage(MessageSmuggler):
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

class SmuggledMethodReturnMessage(MessageSmuggler):
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

class SmuggledObjRef(Object):
    """"""

    def __init__(self, objRef: ObjRef):
        """

        :param objRef:
        """
    @property
    def ObjRef(self) -> ObjRef:
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

class SoapMessageSurrogate(Object, ISerializationSurrogate):
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
    def GetObjectData(
        self, obj: object, info: SerializationInfo, context: StreamingContext
    ) -> None:
        """

        :param obj:
        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def SetObjectData(
        self,
        obj: object,
        info: SerializationInfo,
        context: StreamingContext,
        selector: ISurrogateSelector,
    ) -> object:
        """

        :param obj:
        :param info:
        :param context:
        :param selector:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class StackBasedReturnMessage(
    Object, IInternalMessage, IMessage, IMethodMessage, IMethodReturnMessage
):
    """"""

    @property
    def ArgCount(self) -> int:
        """

        :return:
        """
    @property
    def Args(self) -> Array[object]:
        """

        :return:
        """
    @property
    def Exception(self) -> Exception:
        """

        :return:
        """
    @property
    def HasVarArgs(self) -> bool:
        """

        :return:
        """
    @property
    def IdentityObject(self) -> Identity:
        """

        :return:
        """
    @IdentityObject.setter
    def IdentityObject(self, value: Identity) -> None: ...
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """

        :return:
        """
    @property
    def MethodBase(self) -> MethodBase:
        """

        :return:
        """
    @property
    def MethodName(self) -> str:
        """

        :return:
        """
    @property
    def MethodSignature(self) -> object:
        """

        :return:
        """
    @property
    def OutArgCount(self) -> int:
        """

        :return:
        """
    @property
    def OutArgs(self) -> Array[object]:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """
    @property
    def ReturnValue(self) -> object:
        """

        :return:
        """
    @property
    def ServerIdentityObject(self) -> ServerIdentity:
        """

        :return:
        """
    @ServerIdentityObject.setter
    def ServerIdentityObject(self, value: ServerIdentity) -> None: ...
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    @property
    def Uri(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetOutArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetOutArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def HasProperties(self) -> bool:
        """

        :return:
        """
    def SetCallContext(self, callContext: LogicalCallContext) -> None:
        """

        :param callContext:
        """
    def SetURI(self, uri: str) -> None:
        """

        :param uri:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class StackBuilderSink(Object, IMessageSink):
    """"""

    @overload
    def __init__(self, server: MarshalByRefObject):
        """

        :param server:
        """
    @overload
    def __init__(self, server: object):
        """

        :param server:
        """
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
    def PrivateProcessMessage(
        self, md: RuntimeMethodHandle, args: Array[object], server: object, outArgs: object
    ) -> Tuple[object, object]:
        """

        :param md:
        :param args:
        :param server:
        :param outArgs:
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

class TransitionCall(Object, IInternalMessage, IMessage, IMessageSink, ISerializable):
    """"""

    @property
    def IdentityObject(self) -> Identity:
        """

        :return:
        """
    @IdentityObject.setter
    def IdentityObject(self, value: Identity) -> None: ...
    @property
    def NextSink(self) -> IMessageSink:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """
    @property
    def ServerIdentityObject(self) -> ServerIdentity:
        """

        :return:
        """
    @ServerIdentityObject.setter
    def ServerIdentityObject(self, value: ServerIdentity) -> None: ...
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
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def HasProperties(self) -> bool:
        """

        :return:
        """
    def SetCallContext(self, callContext: LogicalCallContext) -> None:
        """

        :param callContext:
        """
    def SetURI(self, uri: str) -> None:
        """

        :param uri:
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
