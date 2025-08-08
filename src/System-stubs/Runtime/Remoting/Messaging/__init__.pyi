"""Automatically generated stubs for C# namespace: System.Runtime.Remoting.Messaging."""

from abc import ABC
from collections.abc import Callable
from collections.abc import Iterator
from typing import ClassVar
from typing import Final
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
from System import UInt32
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
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class AsyncReplySink(Object, IMessageSink):
    """"""
    @property
    def NextSink(self) -> IMessageSink:
        """"""
    def AsyncProcessMessage(self, reqMsg: IMessage, replySink: IMessageSink) -> IMessageCtrl:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SyncProcessMessage(self, reqMsg: IMessage) -> IMessage:
        """"""
    def ToString(self) -> str:
        """"""

class AsyncResult(Object, IMessageSink, IAsyncResult):
    """"""
    @property
    def AsyncDelegate(self) -> object:
        """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CompletedSynchronously(self) -> bool:
        """"""
    @property
    def EndInvokeCalled(self) -> bool:
        """"""
    @EndInvokeCalled.setter
    def EndInvokeCalled(self, value: bool) -> None: ...
    @property
    def IsCompleted(self) -> bool:
        """"""
    @property
    def NextSink(self) -> IMessageSink:
        """"""
    def AsyncProcessMessage(self, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetReplyMessage(self) -> IMessage:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetMessageCtrl(self, mc: IMessageCtrl) -> None:
        """"""
    def SyncProcessMessage(self, msg: IMessage) -> IMessage:
        """"""
    def ToString(self) -> str:
        """"""

class CCMDictionary(MessageDictionary, ICollection, IDictionary, IEnumerable):
    """"""

    CCMkeys: ClassVar[Array[str]]
    """"""
    def __init__(self, msg: IConstructionCallMessage, idict: IDictionary) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> ICollection:
        """"""
    def Add(self, key: object, value: object) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, key: object) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, key: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, key: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, key: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, key: object) -> object:
        """"""
    def __setitem__(self, key: object, value: object) -> None:
        """"""

class CRMDictionary(MessageDictionary, ICollection, IDictionary, IEnumerable):
    """"""

    CRMkeysFault: ClassVar[Array[str]]
    """"""
    CRMkeysNoFault: ClassVar[Array[str]]
    """"""
    def __init__(self, msg: IConstructionReturnMessage, idict: IDictionary) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> ICollection:
        """"""
    def Add(self, key: object, value: object) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, key: object) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, key: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, key: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, key: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, key: object) -> object:
        """"""
    def __setitem__(self, key: object, value: object) -> None:
        """"""

class CallContext(Object):
    """"""
    @classmethod
    @property
    def HostContext(cls) -> object:
        """"""
    @classmethod
    @HostContext.setter
    def HostContext(cls, value: object) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FreeNamedDataSlot(cls, name: str) -> None:
        """"""
    @classmethod
    def GetData(cls, name: str) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetHeaders(cls) -> Array[Header]:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def LogicalGetData(cls, name: str) -> object:
        """"""
    @classmethod
    def LogicalSetData(cls, name: str, data: object) -> None:
        """"""
    @classmethod
    def SetData(cls, name: str, data: object) -> None:
        """"""
    @classmethod
    def SetHeaders(cls, headers: Array[Header]) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class CallContextRemotingData(Object, ICloneable):
    """"""
    def __init__(self) -> None:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CallContextSecurityData(Object, ICloneable):
    """"""
    def __init__(self) -> None:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ClientAsyncReplyTerminatorSink(Object, IMessageSink):
    """"""
    @property
    def NextSink(self) -> IMessageSink:
        """"""
    def AsyncProcessMessage(self, replyMsg: IMessage, replySink: IMessageSink) -> IMessageCtrl:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SyncProcessMessage(self, replyMsg: IMessage) -> IMessage:
        """"""
    def ToString(self) -> str:
        """"""

class ClientContextTerminatorSink(InternalSink, IMessageSink):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def NextSink(self) -> IMessageSink:
        """"""
    def AsyncProcessMessage(self, reqMsg: IMessage, replySink: IMessageSink) -> IMessageCtrl:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SyncProcessMessage(self, reqMsg: IMessage) -> IMessage:
        """"""
    def ToString(self) -> str:
        """"""

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
    def __init__(self, headers: Array[Header]) -> None:
        """"""
    @overload
    def __init__(self, m: IMessage) -> None:
        """"""
    @property
    def ActivationType(self) -> Type:
        """"""
    @property
    def ActivationTypeName(self) -> str:
        """"""
    @property
    def Activator(self) -> IActivator:
        """"""
    @Activator.setter
    def Activator(self, value: IActivator) -> None: ...
    @property
    def ArgCount(self) -> int:
        """"""
    @property
    def Args(self) -> Array[object]:
        """"""
    @property
    def CallSiteActivationAttributes(self) -> Array[object]:
        """"""
    @property
    def ContextProperties(self) -> IList:
        """"""
    @property
    def HasVarArgs(self) -> bool:
        """"""
    @property
    def IdentityObject(self) -> Identity:
        """"""
    @IdentityObject.setter
    def IdentityObject(self, value: Identity) -> None: ...
    @property
    def InArgCount(self) -> int:
        """"""
    @property
    def InArgs(self) -> Array[object]:
        """"""
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """"""
    @property
    def MethodBase(self) -> MethodBase:
        """"""
    @property
    def MethodName(self) -> str:
        """"""
    @property
    def MethodSignature(self) -> object:
        """"""
    @property
    def Properties(self) -> IDictionary:
        """"""
    @property
    def ServerIdentityObject(self) -> ServerIdentity:
        """"""
    @ServerIdentityObject.setter
    def ServerIdentityObject(self, value: ServerIdentity) -> None: ...
    @property
    def TypeName(self) -> str:
        """"""
    @property
    def Uri(self) -> str:
        """"""
    @Uri.setter
    def Uri(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArg(self, argNum: int) -> object:
        """"""
    def GetArgName(self, index: int) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetInArg(self, argNum: int) -> object:
        """"""
    def GetInArgName(self, index: int) -> str:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def HasProperties(self) -> bool:
        """"""
    def HeaderHandler(self, h: Array[Header]) -> object:
        """"""
    def Init(self) -> None:
        """"""
    def ResolveMethod(self) -> None:
        """"""
    def RootSetObjectData(self, info: SerializationInfo, ctx: StreamingContext) -> None:
        """"""
    def SetCallContext(self, callContext: LogicalCallContext) -> None:
        """"""
    def SetURI(self, uri: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""

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
    def __init__(self, h: Array[Header], mcm: IMethodCallMessage) -> None:
        """"""
    @property
    def ArgCount(self) -> int:
        """"""
    @property
    def Args(self) -> Array[object]:
        """"""
    @property
    def Exception(self) -> Exception:
        """"""
    @property
    def HasVarArgs(self) -> bool:
        """"""
    @property
    def IdentityObject(self) -> Identity:
        """"""
    @IdentityObject.setter
    def IdentityObject(self, value: Identity) -> None: ...
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """"""
    @property
    def MethodBase(self) -> MethodBase:
        """"""
    @property
    def MethodName(self) -> str:
        """"""
    @property
    def MethodSignature(self) -> object:
        """"""
    @property
    def OutArgCount(self) -> int:
        """"""
    @property
    def OutArgs(self) -> Array[object]:
        """"""
    @property
    def Properties(self) -> IDictionary:
        """"""
    @property
    def ReturnValue(self) -> object:
        """"""
    @property
    def ServerIdentityObject(self) -> ServerIdentity:
        """"""
    @ServerIdentityObject.setter
    def ServerIdentityObject(self, value: ServerIdentity) -> None: ...
    @property
    def TypeName(self) -> str:
        """"""
    @property
    def Uri(self) -> str:
        """"""
    @Uri.setter
    def Uri(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArg(self, argNum: int) -> object:
        """"""
    def GetArgName(self, index: int) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetOutArg(self, argNum: int) -> object:
        """"""
    def GetOutArgName(self, index: int) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def HasProperties(self) -> bool:
        """"""
    def HeaderHandler(self, h: Array[Header]) -> object:
        """"""
    def RootSetObjectData(self, info: SerializationInfo, ctx: StreamingContext) -> None:
        """"""
    def SetCallContext(self, callContext: LogicalCallContext) -> None:
        """"""
    def SetURI(self, uri: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class ConstructorCallMessage(
    Object, IConstructionCallMessage, IMessage, IMethodCallMessage, IMethodMessage
):
    """"""
    @property
    def ActivationType(self) -> Type:
        """"""
    @property
    def ActivationTypeName(self) -> str:
        """"""
    @property
    def Activator(self) -> IActivator:
        """"""
    @Activator.setter
    def Activator(self, value: IActivator) -> None: ...
    @property
    def ArgCount(self) -> int:
        """"""
    @property
    def Args(self) -> Array[object]:
        """"""
    @property
    def CallSiteActivationAttributes(self) -> Array[object]:
        """"""
    @property
    def ContextProperties(self) -> IList:
        """"""
    @property
    def HasVarArgs(self) -> bool:
        """"""
    @property
    def InArgCount(self) -> int:
        """"""
    @property
    def InArgs(self) -> Array[object]:
        """"""
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """"""
    @property
    def MethodBase(self) -> MethodBase:
        """"""
    @property
    def MethodName(self) -> str:
        """"""
    @property
    def MethodSignature(self) -> object:
        """"""
    @property
    def Properties(self) -> IDictionary:
        """"""
    @property
    def TypeName(self) -> str:
        """"""
    @property
    def Uri(self) -> str:
        """"""
    @Uri.setter
    def Uri(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArg(self, argNum: int) -> object:
        """"""
    def GetArgName(self, index: int) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetInArg(self, argNum: int) -> object:
        """"""
    def GetInArgName(self, index: int) -> str:
        """"""
    def GetThisPtr(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ConstructorReturnMessage(
    ReturnMessage, IConstructionReturnMessage, IMessage, IMethodMessage, IMethodReturnMessage
):
    """"""
    @overload
    def __init__(
        self,
        o: MarshalByRefObject,
        outArgs: Array[object],
        outArgsCount: int,
        callCtx: LogicalCallContext,
        ccm: IConstructionCallMessage,
    ) -> None:
        """"""
    @overload
    def __init__(self, e: Exception, ccm: IConstructionCallMessage) -> None:
        """"""
    @property
    def ArgCount(self) -> int:
        """"""
    @property
    def Args(self) -> Array[object]:
        """"""
    @property
    def Exception(self) -> Exception:
        """"""
    @property
    def HasVarArgs(self) -> bool:
        """"""
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """"""
    @property
    def MethodBase(self) -> MethodBase:
        """"""
    @property
    def MethodName(self) -> str:
        """"""
    @property
    def MethodSignature(self) -> object:
        """"""
    @property
    def OutArgCount(self) -> int:
        """"""
    @property
    def OutArgs(self) -> Array[object]:
        """"""
    @property
    def Properties(self) -> IDictionary:
        """"""
    @property
    def ReturnValue(self) -> object:
        """"""
    @property
    def TypeName(self) -> str:
        """"""
    @property
    def Uri(self) -> str:
        """"""
    @Uri.setter
    def Uri(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArg(self, argNum: int) -> object:
        """"""
    def GetArgName(self, index: int) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOutArg(self, argNum: int) -> object:
        """"""
    def GetOutArgName(self, index: int) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DisposeSink(Object, IMessageSink):
    """"""
    @property
    def NextSink(self) -> IMessageSink:
        """"""
    def AsyncProcessMessage(self, reqMsg: IMessage, replySink: IMessageSink) -> IMessageCtrl:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SyncProcessMessage(self, reqMsg: IMessage) -> IMessage:
        """"""
    def ToString(self) -> str:
        """"""

class EnvoyTerminatorSink(InternalSink, IMessageSink):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def NextSink(self) -> IMessageSink:
        """"""
    def AsyncProcessMessage(self, reqMsg: IMessage, replySink: IMessageSink) -> IMessageCtrl:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SyncProcessMessage(self, reqMsg: IMessage) -> IMessage:
        """"""
    def ToString(self) -> str:
        """"""

class ErrorMessage(Object, IMessage, IMethodCallMessage, IMethodMessage):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def ArgCount(self) -> int:
        """"""
    @property
    def Args(self) -> Array[object]:
        """"""
    @property
    def HasVarArgs(self) -> bool:
        """"""
    @property
    def InArgCount(self) -> int:
        """"""
    @property
    def InArgs(self) -> Array[object]:
        """"""
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """"""
    @property
    def MethodBase(self) -> MethodBase:
        """"""
    @property
    def MethodName(self) -> str:
        """"""
    @property
    def MethodSignature(self) -> object:
        """"""
    @property
    def Properties(self) -> IDictionary:
        """"""
    @property
    def TypeName(self) -> str:
        """"""
    @property
    def Uri(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArg(self, argNum: int) -> object:
        """"""
    def GetArgName(self, index: int) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetInArg(self, argNum: int) -> object:
        """"""
    def GetInArgName(self, index: int) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Header(Object):
    """"""

    HeaderNamespace: Final[str]
    """"""
    MustUnderstand: Final[bool]
    """"""
    Name: Final[str]
    """"""
    Value: Final[object]
    """"""
    @overload
    def __init__(self, _Name: str, _Value: object) -> None:
        """"""
    @overload
    def __init__(self, _Name: str, _Value: object, _MustUnderstand: bool) -> None:
        """"""
    @overload
    def __init__(
        self, _Name: str, _Value: object, _MustUnderstand: bool, _HeaderNamespace: str
    ) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type HeaderHandler = Callable[[Array[Header]], object]
""""""

class IInternalMessage(ABC):
    """"""
    @property
    def IdentityObject(self) -> Identity:
        """"""
    @IdentityObject.setter
    def IdentityObject(self, value: Identity) -> None: ...
    @property
    def ServerIdentityObject(self) -> ServerIdentity:
        """"""
    @ServerIdentityObject.setter
    def ServerIdentityObject(self, value: ServerIdentity) -> None: ...
    def HasProperties(self) -> bool:
        """"""
    def SetCallContext(self, callContext: LogicalCallContext) -> None:
        """"""
    def SetURI(self, uri: str) -> None:
        """"""

class ILogicalThreadAffinative(ABC):
    """"""

class IMessage(ABC):
    """"""
    @property
    def Properties(self) -> IDictionary:
        """"""

class IMessageCtrl(ABC):
    """"""
    def Cancel(self, msToCancel: int) -> None:
        """"""

class IMessageSink(ABC):
    """"""
    @property
    def NextSink(self) -> IMessageSink:
        """"""
    def AsyncProcessMessage(self, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl:
        """"""
    def SyncProcessMessage(self, msg: IMessage) -> IMessage:
        """"""

class IMethodCallMessage(ABC, IMessage, IMethodMessage):
    """"""
    @property
    def ArgCount(self) -> int:
        """"""
    @property
    def Args(self) -> Array[object]:
        """"""
    @property
    def HasVarArgs(self) -> bool:
        """"""
    @property
    def InArgCount(self) -> int:
        """"""
    @property
    def InArgs(self) -> Array[object]:
        """"""
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """"""
    @property
    def MethodBase(self) -> MethodBase:
        """"""
    @property
    def MethodName(self) -> str:
        """"""
    @property
    def MethodSignature(self) -> object:
        """"""
    @property
    def Properties(self) -> IDictionary:
        """"""
    @property
    def TypeName(self) -> str:
        """"""
    @property
    def Uri(self) -> str:
        """"""
    def GetArg(self, argNum: int) -> object:
        """"""
    def GetArgName(self, index: int) -> str:
        """"""
    def GetInArg(self, argNum: int) -> object:
        """"""
    def GetInArgName(self, index: int) -> str:
        """"""

class IMethodMessage(ABC, IMessage):
    """"""
    @property
    def ArgCount(self) -> int:
        """"""
    @property
    def Args(self) -> Array[object]:
        """"""
    @property
    def HasVarArgs(self) -> bool:
        """"""
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """"""
    @property
    def MethodBase(self) -> MethodBase:
        """"""
    @property
    def MethodName(self) -> str:
        """"""
    @property
    def MethodSignature(self) -> object:
        """"""
    @property
    def Properties(self) -> IDictionary:
        """"""
    @property
    def TypeName(self) -> str:
        """"""
    @property
    def Uri(self) -> str:
        """"""
    def GetArg(self, argNum: int) -> object:
        """"""
    def GetArgName(self, index: int) -> str:
        """"""

class IMethodReturnMessage(ABC, IMessage, IMethodMessage):
    """"""
    @property
    def ArgCount(self) -> int:
        """"""
    @property
    def Args(self) -> Array[object]:
        """"""
    @property
    def Exception(self) -> Exception:
        """"""
    @property
    def HasVarArgs(self) -> bool:
        """"""
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """"""
    @property
    def MethodBase(self) -> MethodBase:
        """"""
    @property
    def MethodName(self) -> str:
        """"""
    @property
    def MethodSignature(self) -> object:
        """"""
    @property
    def OutArgCount(self) -> int:
        """"""
    @property
    def OutArgs(self) -> Array[object]:
        """"""
    @property
    def Properties(self) -> IDictionary:
        """"""
    @property
    def ReturnValue(self) -> object:
        """"""
    @property
    def TypeName(self) -> str:
        """"""
    @property
    def Uri(self) -> str:
        """"""
    def GetArg(self, argNum: int) -> object:
        """"""
    def GetArgName(self, index: int) -> str:
        """"""
    def GetOutArg(self, argNum: int) -> object:
        """"""
    def GetOutArgName(self, index: int) -> str:
        """"""

class IRemotingFormatter(ABC, IFormatter):
    """"""
    @property
    def Binder(self) -> SerializationBinder:
        """"""
    @Binder.setter
    def Binder(self, value: SerializationBinder) -> None: ...
    @property
    def Context(self) -> StreamingContext:
        """"""
    @Context.setter
    def Context(self, value: StreamingContext) -> None: ...
    @property
    def SurrogateSelector(self) -> ISurrogateSelector:
        """"""
    @SurrogateSelector.setter
    def SurrogateSelector(self, value: ISurrogateSelector) -> None: ...
    @overload
    def Deserialize(self, serializationStream: Stream) -> object:
        """"""
    @overload
    def Deserialize(self, serializationStream: Stream, handler: HeaderHandler) -> object:
        """"""
    @overload
    def Serialize(self, serializationStream: Stream, graph: object) -> None:
        """"""
    @overload
    def Serialize(self, serializationStream: Stream, graph: object, headers: Array[Header]) -> None:
        """"""

class ISerializationRootObject(ABC):
    """"""
    def RootSetObjectData(self, info: SerializationInfo, ctx: StreamingContext) -> None:
        """"""

class IllogicalCallContext(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def CreateCopy(self) -> IllogicalCallContext:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FreeNamedDataSlot(self, name: str) -> None:
        """"""
    def GetData(self, name: str) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetData(self, name: str, data: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class InternalMessageWrapper(Object):
    """"""
    def __init__(self, msg: IMessage) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class InternalSink(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class LogicalCallContext(Object, ISerializable, ICloneable):
    """"""
    @property
    def HasInfo(self) -> bool:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FreeNamedDataSlot(self, name: str) -> None:
        """"""
    def GetData(self, name: str) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetData(self, name: str, data: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class MCMDictionary(MessageDictionary, ICollection, IDictionary, IEnumerable):
    """"""

    MCMkeys: ClassVar[Array[str]]
    """"""
    def __init__(self, msg: IMethodCallMessage, idict: IDictionary) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> ICollection:
        """"""
    def Add(self, key: object, value: object) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, key: object) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, key: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, key: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, key: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, key: object) -> object:
        """"""
    def __setitem__(self, key: object, value: object) -> None:
        """"""

class MRMDictionary(MessageDictionary, ICollection, IDictionary, IEnumerable):
    """"""

    MCMkeysFault: ClassVar[Array[str]]
    """"""
    MCMkeysNoFault: ClassVar[Array[str]]
    """"""
    def __init__(self, msg: IMethodReturnMessage, idict: IDictionary) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> ICollection:
        """"""
    def Add(self, key: object, value: object) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, key: object) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, key: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, key: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, key: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, key: object) -> object:
        """"""
    def __setitem__(self, key: object, value: object) -> None:
        """"""

class Message(
    Object, IInternalMessage, IMessage, IMethodCallMessage, IMethodMessage, ISerializable
):
    """"""
    @property
    def ArgCount(self) -> int:
        """"""
    @property
    def Args(self) -> Array[object]:
        """"""
    @property
    def HasVarArgs(self) -> bool:
        """"""
    @property
    def IdentityObject(self) -> Identity:
        """"""
    @IdentityObject.setter
    def IdentityObject(self, value: Identity) -> None: ...
    @property
    def InArgCount(self) -> int:
        """"""
    @property
    def InArgs(self) -> Array[object]:
        """"""
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """"""
    @property
    def MethodBase(self) -> MethodBase:
        """"""
    @property
    def MethodName(self) -> str:
        """"""
    @property
    def MethodSignature(self) -> object:
        """"""
    @property
    def Properties(self) -> IDictionary:
        """"""
    @property
    def ServerIdentityObject(self) -> ServerIdentity:
        """"""
    @ServerIdentityObject.setter
    def ServerIdentityObject(self, value: ServerIdentity) -> None: ...
    @property
    def TypeName(self) -> str:
        """"""
    @property
    def Uri(self) -> str:
        """"""
    @Uri.setter
    def Uri(self, value: str) -> None: ...
    @classmethod
    def DebugOut(cls, s: str) -> None:
        """"""
    def Dispatch(self, target: object) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArg(self, argNum: int) -> object:
        """"""
    def GetArgName(self, index: int) -> str:
        """"""
    def GetAsyncBeginInfo(
        self, acbd: AsyncCallback, state: Object
    ) -> tuple[None, AsyncCallback, Object]:
        """"""
    def GetAsyncResult(self) -> IAsyncResult:
        """"""
    def GetCallType(self) -> int:
        """"""
    def GetFault(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetInArg(self, argNum: int) -> object:
        """"""
    def GetInArgName(self, index: int) -> str:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetReturnValue(self) -> object:
        """"""
    def GetThisPtr(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def HasProperties(self) -> bool:
        """"""
    def Init(self) -> None:
        """"""
    def PropagateOutParameters(self, OutArgs: Array[object], retVal: object) -> None:
        """"""
    def SetCallContext(self, callContext: LogicalCallContext) -> None:
        """"""
    def SetFault(self, e: Exception) -> None:
        """"""
    def SetURI(self, uri: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class MessageDictionary(ABC, Object, ICollection, IDictionary, IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> ICollection:
        """"""
    def Add(self, key: object, value: object) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, key: object) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, key: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, key: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, key: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, key: object) -> object:
        """"""
    def __setitem__(self, key: object, value: object) -> None:
        """"""

class MessageDictionaryEnumerator(Object, IDictionaryEnumerator, IEnumerator):
    """"""
    def __init__(self, md: MessageDictionary, hashtable: IDictionary) -> None:
        """"""
    @property
    def Current(self) -> object:
        """"""
    @property
    def Entry(self) -> DictionaryEntry:
        """"""
    @property
    def Key(self) -> object:
        """"""
    @property
    def Value(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class MessageSmuggler(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MessageSurrogate(Object, ISerializationSurrogate):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(
        self, obj: object, info: SerializationInfo, context: StreamingContext
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetObjectData(
        self,
        obj: object,
        info: SerializationInfo,
        context: StreamingContext,
        selector: ISurrogateSelector,
    ) -> object:
        """"""
    def ToString(self) -> str:
        """"""

type MessageSurrogateFilter = Callable[[str, object], bool]
""""""

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
    def __init__(self, h1: Array[Header]) -> None:
        """"""
    @overload
    def __init__(self, msg: IMessage) -> None:
        """"""
    @property
    def ArgCount(self) -> int:
        """"""
    @property
    def Args(self) -> Array[object]:
        """"""
    @property
    def HasVarArgs(self) -> bool:
        """"""
    @property
    def IdentityObject(self) -> Identity:
        """"""
    @IdentityObject.setter
    def IdentityObject(self, value: Identity) -> None: ...
    @property
    def InArgCount(self) -> int:
        """"""
    @property
    def InArgs(self) -> Array[object]:
        """"""
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """"""
    @property
    def MethodBase(self) -> MethodBase:
        """"""
    @property
    def MethodName(self) -> str:
        """"""
    @property
    def MethodSignature(self) -> object:
        """"""
    @property
    def Properties(self) -> IDictionary:
        """"""
    @property
    def ServerIdentityObject(self) -> ServerIdentity:
        """"""
    @ServerIdentityObject.setter
    def ServerIdentityObject(self, value: ServerIdentity) -> None: ...
    @property
    def TypeName(self) -> str:
        """"""
    @property
    def Uri(self) -> str:
        """"""
    @Uri.setter
    def Uri(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArg(self, argNum: int) -> object:
        """"""
    def GetArgName(self, index: int) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetInArg(self, argNum: int) -> object:
        """"""
    def GetInArgName(self, index: int) -> str:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def HasProperties(self) -> bool:
        """"""
    def HeaderHandler(self, h: Array[Header]) -> object:
        """"""
    def Init(self) -> None:
        """"""
    def ResolveMethod(self) -> None:
        """"""
    def RootSetObjectData(self, info: SerializationInfo, ctx: StreamingContext) -> None:
        """"""
    def SetCallContext(self, callContext: LogicalCallContext) -> None:
        """"""
    def SetURI(self, uri: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class MethodCallMessageWrapper(
    InternalMessageWrapper, IMessage, IMethodCallMessage, IMethodMessage
):
    """"""
    def __init__(self, msg: IMethodCallMessage) -> None:
        """"""
    @property
    def ArgCount(self) -> int:
        """"""
    @property
    def Args(self) -> Array[object]:
        """"""
    @Args.setter
    def Args(self, value: Array[object]) -> None: ...
    @property
    def HasVarArgs(self) -> bool:
        """"""
    @property
    def InArgCount(self) -> int:
        """"""
    @property
    def InArgs(self) -> Array[object]:
        """"""
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """"""
    @property
    def MethodBase(self) -> MethodBase:
        """"""
    @property
    def MethodName(self) -> str:
        """"""
    @property
    def MethodSignature(self) -> object:
        """"""
    @property
    def Properties(self) -> IDictionary:
        """"""
    @property
    def TypeName(self) -> str:
        """"""
    @property
    def Uri(self) -> str:
        """"""
    @Uri.setter
    def Uri(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArg(self, argNum: int) -> object:
        """"""
    def GetArgName(self, index: int) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetInArg(self, argNum: int) -> object:
        """"""
    def GetInArgName(self, index: int) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

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
    def __init__(self, h1: Array[Header], mcm: IMethodCallMessage) -> None:
        """"""
    @property
    def ArgCount(self) -> int:
        """"""
    @property
    def Args(self) -> Array[object]:
        """"""
    @property
    def Exception(self) -> Exception:
        """"""
    @property
    def HasVarArgs(self) -> bool:
        """"""
    @property
    def IdentityObject(self) -> Identity:
        """"""
    @IdentityObject.setter
    def IdentityObject(self, value: Identity) -> None: ...
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """"""
    @property
    def MethodBase(self) -> MethodBase:
        """"""
    @property
    def MethodName(self) -> str:
        """"""
    @property
    def MethodSignature(self) -> object:
        """"""
    @property
    def OutArgCount(self) -> int:
        """"""
    @property
    def OutArgs(self) -> Array[object]:
        """"""
    @property
    def Properties(self) -> IDictionary:
        """"""
    @property
    def ReturnValue(self) -> object:
        """"""
    @property
    def ServerIdentityObject(self) -> ServerIdentity:
        """"""
    @ServerIdentityObject.setter
    def ServerIdentityObject(self, value: ServerIdentity) -> None: ...
    @property
    def TypeName(self) -> str:
        """"""
    @property
    def Uri(self) -> str:
        """"""
    @Uri.setter
    def Uri(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArg(self, argNum: int) -> object:
        """"""
    def GetArgName(self, index: int) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetOutArg(self, argNum: int) -> object:
        """"""
    def GetOutArgName(self, index: int) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def HasProperties(self) -> bool:
        """"""
    def HeaderHandler(self, h: Array[Header]) -> object:
        """"""
    def RootSetObjectData(self, info: SerializationInfo, ctx: StreamingContext) -> None:
        """"""
    def SetCallContext(self, callContext: LogicalCallContext) -> None:
        """"""
    def SetURI(self, uri: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class MethodReturnMessageWrapper(
    InternalMessageWrapper, IMessage, IMethodMessage, IMethodReturnMessage
):
    """"""
    def __init__(self, msg: IMethodReturnMessage) -> None:
        """"""
    @property
    def ArgCount(self) -> int:
        """"""
    @property
    def Args(self) -> Array[object]:
        """"""
    @Args.setter
    def Args(self, value: Array[object]) -> None: ...
    @property
    def Exception(self) -> Exception:
        """"""
    @Exception.setter
    def Exception(self, value: Exception) -> None: ...
    @property
    def HasVarArgs(self) -> bool:
        """"""
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """"""
    @property
    def MethodBase(self) -> MethodBase:
        """"""
    @property
    def MethodName(self) -> str:
        """"""
    @property
    def MethodSignature(self) -> object:
        """"""
    @property
    def OutArgCount(self) -> int:
        """"""
    @property
    def OutArgs(self) -> Array[object]:
        """"""
    @property
    def Properties(self) -> IDictionary:
        """"""
    @property
    def ReturnValue(self) -> object:
        """"""
    @ReturnValue.setter
    def ReturnValue(self, value: object) -> None: ...
    @property
    def TypeName(self) -> str:
        """"""
    @property
    def Uri(self) -> str:
        """"""
    @Uri.setter
    def Uri(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArg(self, argNum: int) -> object:
        """"""
    def GetArgName(self, index: int) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOutArg(self, argNum: int) -> object:
        """"""
    def GetOutArgName(self, index: int) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ObjRefSurrogate(Object, ISerializationSurrogate):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(
        self, obj: object, info: SerializationInfo, context: StreamingContext
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetObjectData(
        self,
        obj: object,
        info: SerializationInfo,
        context: StreamingContext,
        selector: ISurrogateSelector,
    ) -> object:
        """"""
    def ToString(self) -> str:
        """"""

class OneWayAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
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
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class RemotingSurrogate(Object, ISerializationSurrogate):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(
        self, obj: object, info: SerializationInfo, context: StreamingContext
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetObjectData(
        self,
        obj: object,
        info: SerializationInfo,
        context: StreamingContext,
        selector: ISurrogateSelector,
    ) -> object:
        """"""
    def ToString(self) -> str:
        """"""

class RemotingSurrogateSelector(Object, ISurrogateSelector):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Filter(self) -> MessageSurrogateFilter:
        """"""
    @Filter.setter
    def Filter(self, value: MessageSurrogateFilter) -> None: ...
    def ChainSelector(self, selector: ISurrogateSelector) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNextSelector(self) -> ISurrogateSelector:
        """"""
    def GetRootObject(self) -> object:
        """"""
    def GetSurrogate(
        self, type: Type, context: StreamingContext, ssout: ISurrogateSelector
    ) -> tuple[ISerializationSurrogate, ISurrogateSelector]:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetRootObject(self, obj: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def UseSoapFormat(self) -> None:
        """"""

class ReturnMessage(Object, IMessage, IMethodMessage, IMethodReturnMessage):
    """"""
    @overload
    def __init__(
        self,
        ret: object,
        outArgs: Array[object],
        outArgsCount: int,
        callCtx: LogicalCallContext,
        mcm: IMethodCallMessage,
    ) -> None:
        """"""
    @overload
    def __init__(self, e: Exception, mcm: IMethodCallMessage) -> None:
        """"""
    @property
    def ArgCount(self) -> int:
        """"""
    @property
    def Args(self) -> Array[object]:
        """"""
    @property
    def Exception(self) -> Exception:
        """"""
    @property
    def HasVarArgs(self) -> bool:
        """"""
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """"""
    @property
    def MethodBase(self) -> MethodBase:
        """"""
    @property
    def MethodName(self) -> str:
        """"""
    @property
    def MethodSignature(self) -> object:
        """"""
    @property
    def OutArgCount(self) -> int:
        """"""
    @property
    def OutArgs(self) -> Array[object]:
        """"""
    @property
    def Properties(self) -> IDictionary:
        """"""
    @property
    def ReturnValue(self) -> object:
        """"""
    @property
    def TypeName(self) -> str:
        """"""
    @property
    def Uri(self) -> str:
        """"""
    @Uri.setter
    def Uri(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArg(self, argNum: int) -> object:
        """"""
    def GetArgName(self, index: int) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOutArg(self, argNum: int) -> object:
        """"""
    def GetOutArgName(self, index: int) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SerializationMonkey(Object, IFieldInfo, ISerializable):
    """"""
    @property
    def FieldNames(self) -> Array[str]:
        """"""
    @FieldNames.setter
    def FieldNames(self, value: Array[str]) -> None: ...
    @property
    def FieldTypes(self) -> Array[Type]:
        """"""
    @FieldTypes.setter
    def FieldTypes(self, value: Array[Type]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ServerContextTerminatorSink(InternalSink, IMessageSink):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def NextSink(self) -> IMessageSink:
        """"""
    def AsyncProcessMessage(self, reqMsg: IMessage, replySink: IMessageSink) -> IMessageCtrl:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SyncProcessMessage(self, reqMsg: IMessage) -> IMessage:
        """"""
    def ToString(self) -> str:
        """"""

class ServerObjectTerminatorSink(InternalSink, IMessageSink):
    """"""
    @property
    def NextSink(self) -> IMessageSink:
        """"""
    def AsyncProcessMessage(self, reqMsg: IMessage, replySink: IMessageSink) -> IMessageCtrl:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SyncProcessMessage(self, reqMsg: IMessage) -> IMessage:
        """"""
    def ToString(self) -> str:
        """"""

class SmuggledMethodCallMessage(MessageSmuggler):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SmuggledMethodReturnMessage(MessageSmuggler):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SmuggledObjRef(Object):
    """"""
    def __init__(self, objRef: ObjRef) -> None:
        """"""
    @property
    def ObjRef(self) -> ObjRef:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SoapMessageSurrogate(Object, ISerializationSurrogate):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(
        self, obj: object, info: SerializationInfo, context: StreamingContext
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetObjectData(
        self,
        obj: object,
        info: SerializationInfo,
        context: StreamingContext,
        selector: ISurrogateSelector,
    ) -> object:
        """"""
    def ToString(self) -> str:
        """"""

class StackBasedReturnMessage(
    Object, IInternalMessage, IMessage, IMethodMessage, IMethodReturnMessage
):
    """"""
    @property
    def ArgCount(self) -> int:
        """"""
    @property
    def Args(self) -> Array[object]:
        """"""
    @property
    def Exception(self) -> Exception:
        """"""
    @property
    def HasVarArgs(self) -> bool:
        """"""
    @property
    def IdentityObject(self) -> Identity:
        """"""
    @IdentityObject.setter
    def IdentityObject(self, value: Identity) -> None: ...
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """"""
    @property
    def MethodBase(self) -> MethodBase:
        """"""
    @property
    def MethodName(self) -> str:
        """"""
    @property
    def MethodSignature(self) -> object:
        """"""
    @property
    def OutArgCount(self) -> int:
        """"""
    @property
    def OutArgs(self) -> Array[object]:
        """"""
    @property
    def Properties(self) -> IDictionary:
        """"""
    @property
    def ReturnValue(self) -> object:
        """"""
    @property
    def ServerIdentityObject(self) -> ServerIdentity:
        """"""
    @ServerIdentityObject.setter
    def ServerIdentityObject(self, value: ServerIdentity) -> None: ...
    @property
    def TypeName(self) -> str:
        """"""
    @property
    def Uri(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArg(self, argNum: int) -> object:
        """"""
    def GetArgName(self, index: int) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOutArg(self, argNum: int) -> object:
        """"""
    def GetOutArgName(self, index: int) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def HasProperties(self) -> bool:
        """"""
    def SetCallContext(self, callContext: LogicalCallContext) -> None:
        """"""
    def SetURI(self, uri: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class StackBuilderSink(Object, IMessageSink):
    """"""
    @overload
    def __init__(self, server: MarshalByRefObject) -> None:
        """"""
    @overload
    def __init__(self, server: object) -> None:
        """"""
    @property
    def NextSink(self) -> IMessageSink:
        """"""
    def AsyncProcessMessage(self, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PrivateProcessMessage(
        self, md: RuntimeMethodHandle, args: Array[object], server: object, outArgs: Object
    ) -> tuple[object, Object]:
        """"""
    def SyncProcessMessage(self, msg: IMessage) -> IMessage:
        """"""
    def ToString(self) -> str:
        """"""

class TransitionCall(Object, IInternalMessage, IMessage, IMessageSink, ISerializable):
    """"""
    @property
    def IdentityObject(self) -> Identity:
        """"""
    @IdentityObject.setter
    def IdentityObject(self, value: Identity) -> None: ...
    @property
    def NextSink(self) -> IMessageSink:
        """"""
    @property
    def Properties(self) -> IDictionary:
        """"""
    @property
    def ServerIdentityObject(self) -> ServerIdentity:
        """"""
    @ServerIdentityObject.setter
    def ServerIdentityObject(self, value: ServerIdentity) -> None: ...
    def AsyncProcessMessage(self, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def HasProperties(self) -> bool:
        """"""
    def SetCallContext(self, callContext: LogicalCallContext) -> None:
        """"""
    def SetURI(self, uri: str) -> None:
        """"""
    def SyncProcessMessage(self, msg: IMessage) -> IMessage:
        """"""
    def ToString(self) -> str:
        """"""
