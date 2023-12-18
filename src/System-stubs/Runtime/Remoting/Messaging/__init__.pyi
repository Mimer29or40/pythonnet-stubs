from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import List
from typing import Protocol
from typing import Tuple
from typing import Union
from typing import overload

from System import Array
from System import AsyncCallback
from System import Attribute
from System import Boolean
from System import Exception
from System import IAsyncResult
from System import ICloneable
from System import Int32
from System import IntPtr
from System import MarshalByRefObject
from System import MulticastDelegate
from System import Object
from System import RuntimeMethodHandle
from System import String
from System import Type
from System import Void
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
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Runtime.Serialization.Formatters import IFieldInfo
from System.Threading import WaitHandle

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class ArgMapper(ObjectType):
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

class AsyncReplySink(ObjectType, IMessageSink):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def NextSink(self) -> IMessageSink: ...

    # ---------- Methods ---------- #

    def AsyncProcessMessage(self, reqMsg: IMessage, replySink: IMessageSink) -> IMessageCtrl: ...
    def SyncProcessMessage(self, reqMsg: IMessage) -> IMessage: ...
    def get_NextSink(self) -> IMessageSink: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class AsyncResult(ObjectType, IAsyncResult, IMessageSink):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def AsyncDelegate(self) -> ObjectType: ...
    @property
    def AsyncState(self) -> ObjectType: ...
    @property
    def AsyncWaitHandle(self) -> WaitHandle: ...
    @property
    def CompletedSynchronously(self) -> BooleanType: ...
    @property
    def EndInvokeCalled(self) -> BooleanType: ...
    @EndInvokeCalled.setter
    def EndInvokeCalled(self, value: BooleanType) -> None: ...
    @property
    def IsCompleted(self) -> BooleanType: ...
    @property
    def NextSink(self) -> IMessageSink: ...

    # ---------- Methods ---------- #

    def AsyncProcessMessage(self, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl: ...
    def GetReplyMessage(self) -> IMessage: ...
    def SetMessageCtrl(self, mc: IMessageCtrl) -> VoidType: ...
    def SyncProcessMessage(self, msg: IMessage) -> IMessage: ...
    def get_AsyncDelegate(self) -> ObjectType: ...
    def get_AsyncState(self) -> ObjectType: ...
    def get_AsyncWaitHandle(self) -> WaitHandle: ...
    def get_CompletedSynchronously(self) -> BooleanType: ...
    def get_EndInvokeCalled(self) -> BooleanType: ...
    def get_IsCompleted(self) -> BooleanType: ...
    def get_NextSink(self) -> IMessageSink: ...
    def set_EndInvokeCalled(self, value: BooleanType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CCMDictionary(MessageDictionary, IDictionary, ICollection, IEnumerable):
    # ---------- Fields ---------- #

    @staticmethod
    @property
    def CCMkeys() -> ArrayType[StringType]: ...
    @staticmethod
    @CCMkeys.setter
    def CCMkeys(value: ArrayType[StringType]) -> None: ...

    # ---------- Constructors ---------- #

    def __init__(self, msg: IConstructionCallMessage, idict: IDictionary): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CRMDictionary(MessageDictionary, IDictionary, ICollection, IEnumerable):
    # ---------- Fields ---------- #

    @staticmethod
    @property
    def CRMkeysFault() -> ArrayType[StringType]: ...
    @staticmethod
    @CRMkeysFault.setter
    def CRMkeysFault(value: ArrayType[StringType]) -> None: ...
    @staticmethod
    @property
    def CRMkeysNoFault() -> ArrayType[StringType]: ...
    @staticmethod
    @CRMkeysNoFault.setter
    def CRMkeysNoFault(value: ArrayType[StringType]) -> None: ...

    # ---------- Constructors ---------- #

    def __init__(self, msg: IConstructionReturnMessage, idict: IDictionary): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CallContext(ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @staticmethod
    @property
    def HostContext() -> ObjectType: ...
    @staticmethod
    @HostContext.setter
    def HostContext(value: ObjectType) -> None: ...

    # ---------- Methods ---------- #

    @staticmethod
    def FreeNamedDataSlot(name: StringType) -> VoidType: ...
    @staticmethod
    def GetData(name: StringType) -> ObjectType: ...
    @staticmethod
    def GetHeaders() -> ArrayType[Header]: ...
    @staticmethod
    def LogicalGetData(name: StringType) -> ObjectType: ...
    @staticmethod
    def LogicalSetData(name: StringType, data: ObjectType) -> VoidType: ...
    @staticmethod
    def SetData(name: StringType, data: ObjectType) -> VoidType: ...
    @staticmethod
    def SetHeaders(headers: ArrayType[Header]) -> VoidType: ...
    @staticmethod
    def get_HostContext() -> ObjectType: ...
    @staticmethod
    def set_HostContext(value: ObjectType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CallContextRemotingData(ObjectType, ICloneable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Clone(self) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CallContextSecurityData(ObjectType, ICloneable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Clone(self) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ClientAsyncReplyTerminatorSink(ObjectType, IMessageSink):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def NextSink(self) -> IMessageSink: ...

    # ---------- Methods ---------- #

    def AsyncProcessMessage(self, replyMsg: IMessage, replySink: IMessageSink) -> IMessageCtrl: ...
    def SyncProcessMessage(self, replyMsg: IMessage) -> IMessage: ...
    def get_NextSink(self) -> IMessageSink: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ClientContextTerminatorSink(InternalSink, IMessageSink):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def NextSink(self) -> IMessageSink: ...

    # ---------- Methods ---------- #

    def AsyncProcessMessage(self, reqMsg: IMessage, replySink: IMessageSink) -> IMessageCtrl: ...
    def SyncProcessMessage(self, reqMsg: IMessage) -> IMessage: ...
    def get_NextSink(self) -> IMessageSink: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConstructionCall(
    MethodCall,
    IMethodCallMessage,
    IMethodMessage,
    IMessage,
    ISerializable,
    IInternalMessage,
    ISerializationRootObject,
    IConstructionCallMessage,
):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, headers: ArrayType[Header]): ...
    @overload
    def __init__(self, m: IMessage): ...

    # ---------- Properties ---------- #

    @property
    def ActivationType(self) -> TypeType: ...
    @property
    def ActivationTypeName(self) -> StringType: ...
    @property
    def Activator(self) -> IActivator: ...
    @Activator.setter
    def Activator(self, value: IActivator) -> None: ...
    @property
    def CallSiteActivationAttributes(self) -> ArrayType[ObjectType]: ...
    @property
    def ContextProperties(self) -> IList: ...
    @property
    def Properties(self) -> IDictionary: ...

    # ---------- Methods ---------- #

    def get_ActivationType(self) -> TypeType: ...
    def get_ActivationTypeName(self) -> StringType: ...
    def get_Activator(self) -> IActivator: ...
    def get_CallSiteActivationAttributes(self) -> ArrayType[ObjectType]: ...
    def get_ContextProperties(self) -> IList: ...
    def get_Properties(self) -> IDictionary: ...
    def set_Activator(self, value: IActivator) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConstructionResponse(
    MethodResponse,
    IMethodReturnMessage,
    IMethodMessage,
    IMessage,
    ISerializable,
    ISerializationRootObject,
    IInternalMessage,
    IConstructionReturnMessage,
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, h: ArrayType[Header], mcm: IMethodCallMessage): ...

    # ---------- Properties ---------- #

    @property
    def Properties(self) -> IDictionary: ...

    # ---------- Methods ---------- #

    def get_Properties(self) -> IDictionary: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConstructorCallMessage(
    ObjectType, IConstructionCallMessage, IMethodCallMessage, IMethodMessage, IMessage
):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def ActivationType(self) -> TypeType: ...
    @property
    def ActivationTypeName(self) -> StringType: ...
    @property
    def Activator(self) -> IActivator: ...
    @Activator.setter
    def Activator(self, value: IActivator) -> None: ...
    @property
    def ArgCount(self) -> IntType: ...
    @property
    def Args(self) -> ArrayType[ObjectType]: ...
    @property
    def CallSiteActivationAttributes(self) -> ArrayType[ObjectType]: ...
    @property
    def ContextProperties(self) -> IList: ...
    @property
    def HasVarArgs(self) -> BooleanType: ...
    @property
    def InArgCount(self) -> IntType: ...
    @property
    def InArgs(self) -> ArrayType[ObjectType]: ...
    @property
    def LogicalCallContext(self) -> LogicalCallContext: ...
    @property
    def MethodBase(self) -> MethodBase: ...
    @property
    def MethodName(self) -> StringType: ...
    @property
    def MethodSignature(self) -> ObjectType: ...
    @property
    def Properties(self) -> IDictionary: ...
    @property
    def TypeName(self) -> StringType: ...
    @property
    def Uri(self) -> StringType: ...
    @Uri.setter
    def Uri(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def GetArg(self, argNum: IntType) -> ObjectType: ...
    def GetArgName(self, index: IntType) -> StringType: ...
    def GetInArg(self, argNum: IntType) -> ObjectType: ...
    def GetInArgName(self, index: IntType) -> StringType: ...
    def GetThisPtr(self) -> ObjectType: ...
    def get_ActivationType(self) -> TypeType: ...
    def get_ActivationTypeName(self) -> StringType: ...
    def get_Activator(self) -> IActivator: ...
    def get_ArgCount(self) -> IntType: ...
    def get_Args(self) -> ArrayType[ObjectType]: ...
    def get_CallSiteActivationAttributes(self) -> ArrayType[ObjectType]: ...
    def get_ContextProperties(self) -> IList: ...
    def get_HasVarArgs(self) -> BooleanType: ...
    def get_InArgCount(self) -> IntType: ...
    def get_InArgs(self) -> ArrayType[ObjectType]: ...
    def get_LogicalCallContext(self) -> LogicalCallContext: ...
    def get_MethodBase(self) -> MethodBase: ...
    def get_MethodName(self) -> StringType: ...
    def get_MethodSignature(self) -> ObjectType: ...
    def get_Properties(self) -> IDictionary: ...
    def get_TypeName(self) -> StringType: ...
    def get_Uri(self) -> StringType: ...
    def set_Activator(self, value: IActivator) -> VoidType: ...
    def set_Uri(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConstructorReturnMessage(
    ReturnMessage, IMethodReturnMessage, IMethodMessage, IMessage, IConstructionReturnMessage
):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(
        self,
        o: MarshalByRefObject,
        outArgs: ArrayType[ObjectType],
        outArgsCount: IntType,
        callCtx: LogicalCallContext,
        ccm: IConstructionCallMessage,
    ): ...
    @overload
    def __init__(self, e: Exception, ccm: IConstructionCallMessage): ...

    # ---------- Properties ---------- #

    @property
    def Properties(self) -> IDictionary: ...
    @property
    def ReturnValue(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def get_Properties(self) -> IDictionary: ...
    def get_ReturnValue(self) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DisposeSink(ObjectType, IMessageSink):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def NextSink(self) -> IMessageSink: ...

    # ---------- Methods ---------- #

    def AsyncProcessMessage(self, reqMsg: IMessage, replySink: IMessageSink) -> IMessageCtrl: ...
    def SyncProcessMessage(self, reqMsg: IMessage) -> IMessage: ...
    def get_NextSink(self) -> IMessageSink: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EnvoyTerminatorSink(InternalSink, IMessageSink):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def NextSink(self) -> IMessageSink: ...

    # ---------- Methods ---------- #

    def AsyncProcessMessage(self, reqMsg: IMessage, replySink: IMessageSink) -> IMessageCtrl: ...
    def SyncProcessMessage(self, reqMsg: IMessage) -> IMessage: ...
    def get_NextSink(self) -> IMessageSink: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ErrorMessage(ObjectType, IMethodCallMessage, IMethodMessage, IMessage):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def ArgCount(self) -> IntType: ...
    @property
    def Args(self) -> ArrayType[ObjectType]: ...
    @property
    def HasVarArgs(self) -> BooleanType: ...
    @property
    def InArgCount(self) -> IntType: ...
    @property
    def InArgs(self) -> ArrayType[ObjectType]: ...
    @property
    def LogicalCallContext(self) -> LogicalCallContext: ...
    @property
    def MethodBase(self) -> MethodBase: ...
    @property
    def MethodName(self) -> StringType: ...
    @property
    def MethodSignature(self) -> ObjectType: ...
    @property
    def Properties(self) -> IDictionary: ...
    @property
    def TypeName(self) -> StringType: ...
    @property
    def Uri(self) -> StringType: ...

    # ---------- Methods ---------- #

    def GetArg(self, argNum: IntType) -> ObjectType: ...
    def GetArgName(self, index: IntType) -> StringType: ...
    def GetInArg(self, argNum: IntType) -> ObjectType: ...
    def GetInArgName(self, index: IntType) -> StringType: ...
    def get_ArgCount(self) -> IntType: ...
    def get_Args(self) -> ArrayType[ObjectType]: ...
    def get_HasVarArgs(self) -> BooleanType: ...
    def get_InArgCount(self) -> IntType: ...
    def get_InArgs(self) -> ArrayType[ObjectType]: ...
    def get_LogicalCallContext(self) -> LogicalCallContext: ...
    def get_MethodBase(self) -> MethodBase: ...
    def get_MethodName(self) -> StringType: ...
    def get_MethodSignature(self) -> ObjectType: ...
    def get_Properties(self) -> IDictionary: ...
    def get_TypeName(self) -> StringType: ...
    def get_Uri(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Header(ObjectType):
    # ---------- Fields ---------- #

    @property
    def HeaderNamespace(self) -> StringType: ...
    @HeaderNamespace.setter
    def HeaderNamespace(self, value: StringType) -> None: ...
    @property
    def MustUnderstand(self) -> BooleanType: ...
    @MustUnderstand.setter
    def MustUnderstand(self, value: BooleanType) -> None: ...
    @property
    def Name(self) -> StringType: ...
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    @property
    def Value(self) -> ObjectType: ...
    @Value.setter
    def Value(self, value: ObjectType) -> None: ...

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, _Name: StringType, _Value: ObjectType): ...
    @overload
    def __init__(self, _Name: StringType, _Value: ObjectType, _MustUnderstand: BooleanType): ...
    @overload
    def __init__(
        self,
        _Name: StringType,
        _Value: ObjectType,
        _MustUnderstand: BooleanType,
        _HeaderNamespace: StringType,
    ): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class HeaderHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, object: ObjectType, method: NIntType): ...

    # No Properties

    # ---------- Methods ---------- #

    def BeginInvoke(
        self, headers: ArrayType[Header], callback: AsyncCallback, object: ObjectType
    ) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> ObjectType: ...
    def Invoke(self, headers: ArrayType[Header]) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class IllogicalCallContext(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def CreateCopy(self) -> IllogicalCallContext: ...
    def FreeNamedDataSlot(self, name: StringType) -> VoidType: ...
    def GetData(self, name: StringType) -> ObjectType: ...
    def SetData(self, name: StringType, data: ObjectType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class InternalMessageWrapper(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, msg: IMessage): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class InternalSink(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class LogicalCallContext(ObjectType, ISerializable, ICloneable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def HasInfo(self) -> BooleanType: ...

    # ---------- Methods ---------- #

    def Clone(self) -> ObjectType: ...
    def FreeNamedDataSlot(self, name: StringType) -> VoidType: ...
    def GetData(self, name: StringType) -> ObjectType: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    def SetData(self, name: StringType, data: ObjectType) -> VoidType: ...
    def get_HasInfo(self) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class MCMDictionary(MessageDictionary, IDictionary, ICollection, IEnumerable):
    # ---------- Fields ---------- #

    @staticmethod
    @property
    def MCMkeys() -> ArrayType[StringType]: ...
    @staticmethod
    @MCMkeys.setter
    def MCMkeys(value: ArrayType[StringType]) -> None: ...

    # ---------- Constructors ---------- #

    def __init__(self, msg: IMethodCallMessage, idict: IDictionary): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class MRMDictionary(MessageDictionary, IDictionary, ICollection, IEnumerable):
    # ---------- Fields ---------- #

    @staticmethod
    @property
    def MCMkeysFault() -> ArrayType[StringType]: ...
    @staticmethod
    @MCMkeysFault.setter
    def MCMkeysFault(value: ArrayType[StringType]) -> None: ...
    @staticmethod
    @property
    def MCMkeysNoFault() -> ArrayType[StringType]: ...
    @staticmethod
    @MCMkeysNoFault.setter
    def MCMkeysNoFault(value: ArrayType[StringType]) -> None: ...

    # ---------- Constructors ---------- #

    def __init__(self, msg: IMethodReturnMessage, idict: IDictionary): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Message(
    ObjectType, IMethodCallMessage, IMethodMessage, IMessage, IInternalMessage, ISerializable
):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def ArgCount(self) -> IntType: ...
    @property
    def Args(self) -> ArrayType[ObjectType]: ...
    @property
    def HasVarArgs(self) -> BooleanType: ...
    @property
    def InArgCount(self) -> IntType: ...
    @property
    def InArgs(self) -> ArrayType[ObjectType]: ...
    @property
    def LogicalCallContext(self) -> LogicalCallContext: ...
    @property
    def MethodBase(self) -> MethodBase: ...
    @property
    def MethodName(self) -> StringType: ...
    @property
    def MethodSignature(self) -> ObjectType: ...
    @property
    def Properties(self) -> IDictionary: ...
    @property
    def TypeName(self) -> StringType: ...
    @property
    def Uri(self) -> StringType: ...
    @Uri.setter
    def Uri(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    @staticmethod
    def DebugOut(s: StringType) -> VoidType: ...
    def Dispatch(self, target: ObjectType) -> BooleanType: ...
    def GetArg(self, argNum: IntType) -> ObjectType: ...
    def GetArgName(self, index: IntType) -> StringType: ...
    def GetAsyncBeginInfo(
        self, acbd: AsyncCallback, state: ObjectType
    ) -> Tuple[VoidType, AsyncCallback, ObjectType]: ...
    def GetAsyncResult(self) -> IAsyncResult: ...
    def GetCallType(self) -> IntType: ...
    def GetFault(self) -> Exception: ...
    def GetInArg(self, argNum: IntType) -> ObjectType: ...
    def GetInArgName(self, index: IntType) -> StringType: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    def GetReturnValue(self) -> ObjectType: ...
    def GetThisPtr(self) -> ObjectType: ...
    def Init(self) -> VoidType: ...
    def PropagateOutParameters(
        self, OutArgs: ArrayType[ObjectType], retVal: ObjectType
    ) -> VoidType: ...
    def SetFault(self, e: Exception) -> VoidType: ...
    def get_ArgCount(self) -> IntType: ...
    def get_Args(self) -> ArrayType[ObjectType]: ...
    def get_HasVarArgs(self) -> BooleanType: ...
    def get_InArgCount(self) -> IntType: ...
    def get_InArgs(self) -> ArrayType[ObjectType]: ...
    def get_LogicalCallContext(self) -> LogicalCallContext: ...
    def get_MethodBase(self) -> MethodBase: ...
    def get_MethodName(self) -> StringType: ...
    def get_MethodSignature(self) -> ObjectType: ...
    def get_Properties(self) -> IDictionary: ...
    def get_TypeName(self) -> StringType: ...
    def get_Uri(self) -> StringType: ...
    def set_Uri(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class MessageDictionary(ABC, ObjectType, IDictionary, ICollection, IEnumerable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...
    @property
    def IsFixedSize(self) -> BooleanType: ...
    @property
    def IsReadOnly(self) -> BooleanType: ...
    @property
    def IsSynchronized(self) -> BooleanType: ...
    def __getitem__(self, key: ObjectType) -> ObjectType: ...
    def __setitem__(self, key: ObjectType, value: ObjectType) -> None: ...
    @property
    def Keys(self) -> ICollection: ...
    @property
    def SyncRoot(self) -> ObjectType: ...
    @property
    def Values(self) -> ICollection: ...

    # ---------- Methods ---------- #

    def Add(self, key: ObjectType, value: ObjectType) -> VoidType: ...
    def Clear(self) -> VoidType: ...
    def Contains(self, key: ObjectType) -> BooleanType: ...
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    def Remove(self, key: ObjectType) -> VoidType: ...
    def get_Count(self) -> IntType: ...
    def get_IsFixedSize(self) -> BooleanType: ...
    def get_IsReadOnly(self) -> BooleanType: ...
    def get_IsSynchronized(self) -> BooleanType: ...
    def get_Item(self, key: ObjectType) -> ObjectType: ...
    def get_Keys(self) -> ICollection: ...
    def get_SyncRoot(self) -> ObjectType: ...
    def get_Values(self) -> ICollection: ...
    def set_Item(self, key: ObjectType, value: ObjectType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class MessageDictionaryEnumerator(ObjectType, IDictionaryEnumerator, IEnumerator):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, md: MessageDictionary, hashtable: IDictionary): ...

    # ---------- Properties ---------- #

    @property
    def Current(self) -> ObjectType: ...
    @property
    def Entry(self) -> DictionaryEntry: ...
    @property
    def Key(self) -> ObjectType: ...
    @property
    def Value(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def MoveNext(self) -> BooleanType: ...
    def Reset(self) -> VoidType: ...
    def get_Current(self) -> ObjectType: ...
    def get_Entry(self) -> DictionaryEntry: ...
    def get_Key(self) -> ObjectType: ...
    def get_Value(self) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class MessageSmuggler(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class MessageSurrogate(ObjectType, ISerializationSurrogate):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def GetObjectData(
        self, obj: ObjectType, info: SerializationInfo, context: StreamingContext
    ) -> VoidType: ...
    def SetObjectData(
        self,
        obj: ObjectType,
        info: SerializationInfo,
        context: StreamingContext,
        selector: ISurrogateSelector,
    ) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class MessageSurrogateFilter(MulticastDelegate, ICloneable, ISerializable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, object: ObjectType, method: NIntType): ...

    # No Properties

    # ---------- Methods ---------- #

    def BeginInvoke(
        self, key: StringType, value: ObjectType, callback: AsyncCallback, object: ObjectType
    ) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> BooleanType: ...
    def Invoke(self, key: StringType, value: ObjectType) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class MethodCall(
    ObjectType,
    IMethodCallMessage,
    IMethodMessage,
    IMessage,
    ISerializable,
    IInternalMessage,
    ISerializationRootObject,
):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, h1: ArrayType[Header]): ...
    @overload
    def __init__(self, msg: IMessage): ...

    # ---------- Properties ---------- #

    @property
    def ArgCount(self) -> IntType: ...
    @property
    def Args(self) -> ArrayType[ObjectType]: ...
    @property
    def HasVarArgs(self) -> BooleanType: ...
    @property
    def InArgCount(self) -> IntType: ...
    @property
    def InArgs(self) -> ArrayType[ObjectType]: ...
    @property
    def LogicalCallContext(self) -> LogicalCallContext: ...
    @property
    def MethodBase(self) -> MethodBase: ...
    @property
    def MethodName(self) -> StringType: ...
    @property
    def MethodSignature(self) -> ObjectType: ...
    @property
    def Properties(self) -> IDictionary: ...
    @property
    def TypeName(self) -> StringType: ...
    @property
    def Uri(self) -> StringType: ...
    @Uri.setter
    def Uri(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def GetArg(self, argNum: IntType) -> ObjectType: ...
    def GetArgName(self, index: IntType) -> StringType: ...
    def GetInArg(self, argNum: IntType) -> ObjectType: ...
    def GetInArgName(self, index: IntType) -> StringType: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    def HeaderHandler(self, h: ArrayType[Header]) -> ObjectType: ...
    def Init(self) -> VoidType: ...
    def ResolveMethod(self) -> VoidType: ...
    def RootSetObjectData(self, info: SerializationInfo, ctx: StreamingContext) -> VoidType: ...
    def get_ArgCount(self) -> IntType: ...
    def get_Args(self) -> ArrayType[ObjectType]: ...
    def get_HasVarArgs(self) -> BooleanType: ...
    def get_InArgCount(self) -> IntType: ...
    def get_InArgs(self) -> ArrayType[ObjectType]: ...
    def get_LogicalCallContext(self) -> LogicalCallContext: ...
    def get_MethodBase(self) -> MethodBase: ...
    def get_MethodName(self) -> StringType: ...
    def get_MethodSignature(self) -> ObjectType: ...
    def get_Properties(self) -> IDictionary: ...
    def get_TypeName(self) -> StringType: ...
    def get_Uri(self) -> StringType: ...
    def set_Uri(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class MethodCallMessageWrapper(
    InternalMessageWrapper, IMethodCallMessage, IMethodMessage, IMessage
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, msg: IMethodCallMessage): ...

    # ---------- Properties ---------- #

    @property
    def ArgCount(self) -> IntType: ...
    @property
    def Args(self) -> ArrayType[ObjectType]: ...
    @Args.setter
    def Args(self, value: ArrayType[ObjectType]) -> None: ...
    @property
    def HasVarArgs(self) -> BooleanType: ...
    @property
    def InArgCount(self) -> IntType: ...
    @property
    def InArgs(self) -> ArrayType[ObjectType]: ...
    @property
    def LogicalCallContext(self) -> LogicalCallContext: ...
    @property
    def MethodBase(self) -> MethodBase: ...
    @property
    def MethodName(self) -> StringType: ...
    @property
    def MethodSignature(self) -> ObjectType: ...
    @property
    def Properties(self) -> IDictionary: ...
    @property
    def TypeName(self) -> StringType: ...
    @property
    def Uri(self) -> StringType: ...
    @Uri.setter
    def Uri(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def GetArg(self, argNum: IntType) -> ObjectType: ...
    def GetArgName(self, index: IntType) -> StringType: ...
    def GetInArg(self, argNum: IntType) -> ObjectType: ...
    def GetInArgName(self, index: IntType) -> StringType: ...
    def get_ArgCount(self) -> IntType: ...
    def get_Args(self) -> ArrayType[ObjectType]: ...
    def get_HasVarArgs(self) -> BooleanType: ...
    def get_InArgCount(self) -> IntType: ...
    def get_InArgs(self) -> ArrayType[ObjectType]: ...
    def get_LogicalCallContext(self) -> LogicalCallContext: ...
    def get_MethodBase(self) -> MethodBase: ...
    def get_MethodName(self) -> StringType: ...
    def get_MethodSignature(self) -> ObjectType: ...
    def get_Properties(self) -> IDictionary: ...
    def get_TypeName(self) -> StringType: ...
    def get_Uri(self) -> StringType: ...
    def set_Args(self, value: ArrayType[ObjectType]) -> VoidType: ...
    def set_Uri(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class MethodResponse(
    ObjectType,
    IMethodReturnMessage,
    IMethodMessage,
    IMessage,
    ISerializable,
    ISerializationRootObject,
    IInternalMessage,
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, h1: ArrayType[Header], mcm: IMethodCallMessage): ...

    # ---------- Properties ---------- #

    @property
    def ArgCount(self) -> IntType: ...
    @property
    def Args(self) -> ArrayType[ObjectType]: ...
    @property
    def Exception(self) -> Exception: ...
    @property
    def HasVarArgs(self) -> BooleanType: ...
    @property
    def LogicalCallContext(self) -> LogicalCallContext: ...
    @property
    def MethodBase(self) -> MethodBase: ...
    @property
    def MethodName(self) -> StringType: ...
    @property
    def MethodSignature(self) -> ObjectType: ...
    @property
    def OutArgCount(self) -> IntType: ...
    @property
    def OutArgs(self) -> ArrayType[ObjectType]: ...
    @property
    def Properties(self) -> IDictionary: ...
    @property
    def ReturnValue(self) -> ObjectType: ...
    @property
    def TypeName(self) -> StringType: ...
    @property
    def Uri(self) -> StringType: ...
    @Uri.setter
    def Uri(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def GetArg(self, argNum: IntType) -> ObjectType: ...
    def GetArgName(self, index: IntType) -> StringType: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    def GetOutArg(self, argNum: IntType) -> ObjectType: ...
    def GetOutArgName(self, index: IntType) -> StringType: ...
    def HeaderHandler(self, h: ArrayType[Header]) -> ObjectType: ...
    def RootSetObjectData(self, info: SerializationInfo, ctx: StreamingContext) -> VoidType: ...
    def get_ArgCount(self) -> IntType: ...
    def get_Args(self) -> ArrayType[ObjectType]: ...
    def get_Exception(self) -> Exception: ...
    def get_HasVarArgs(self) -> BooleanType: ...
    def get_LogicalCallContext(self) -> LogicalCallContext: ...
    def get_MethodBase(self) -> MethodBase: ...
    def get_MethodName(self) -> StringType: ...
    def get_MethodSignature(self) -> ObjectType: ...
    def get_OutArgCount(self) -> IntType: ...
    def get_OutArgs(self) -> ArrayType[ObjectType]: ...
    def get_Properties(self) -> IDictionary: ...
    def get_ReturnValue(self) -> ObjectType: ...
    def get_TypeName(self) -> StringType: ...
    def get_Uri(self) -> StringType: ...
    def set_Uri(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class MethodReturnMessageWrapper(
    InternalMessageWrapper, IMethodReturnMessage, IMethodMessage, IMessage
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, msg: IMethodReturnMessage): ...

    # ---------- Properties ---------- #

    @property
    def ArgCount(self) -> IntType: ...
    @property
    def Args(self) -> ArrayType[ObjectType]: ...
    @Args.setter
    def Args(self, value: ArrayType[ObjectType]) -> None: ...
    @property
    def Exception(self) -> Exception: ...
    @Exception.setter
    def Exception(self, value: Exception) -> None: ...
    @property
    def HasVarArgs(self) -> BooleanType: ...
    @property
    def LogicalCallContext(self) -> LogicalCallContext: ...
    @property
    def MethodBase(self) -> MethodBase: ...
    @property
    def MethodName(self) -> StringType: ...
    @property
    def MethodSignature(self) -> ObjectType: ...
    @property
    def OutArgCount(self) -> IntType: ...
    @property
    def OutArgs(self) -> ArrayType[ObjectType]: ...
    @property
    def Properties(self) -> IDictionary: ...
    @property
    def ReturnValue(self) -> ObjectType: ...
    @ReturnValue.setter
    def ReturnValue(self, value: ObjectType) -> None: ...
    @property
    def TypeName(self) -> StringType: ...
    @property
    def Uri(self) -> StringType: ...
    @Uri.setter
    def Uri(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def GetArg(self, argNum: IntType) -> ObjectType: ...
    def GetArgName(self, index: IntType) -> StringType: ...
    def GetOutArg(self, argNum: IntType) -> ObjectType: ...
    def GetOutArgName(self, index: IntType) -> StringType: ...
    def get_ArgCount(self) -> IntType: ...
    def get_Args(self) -> ArrayType[ObjectType]: ...
    def get_Exception(self) -> Exception: ...
    def get_HasVarArgs(self) -> BooleanType: ...
    def get_LogicalCallContext(self) -> LogicalCallContext: ...
    def get_MethodBase(self) -> MethodBase: ...
    def get_MethodName(self) -> StringType: ...
    def get_MethodSignature(self) -> ObjectType: ...
    def get_OutArgCount(self) -> IntType: ...
    def get_OutArgs(self) -> ArrayType[ObjectType]: ...
    def get_Properties(self) -> IDictionary: ...
    def get_ReturnValue(self) -> ObjectType: ...
    def get_TypeName(self) -> StringType: ...
    def get_Uri(self) -> StringType: ...
    def set_Args(self, value: ArrayType[ObjectType]) -> VoidType: ...
    def set_Exception(self, value: Exception) -> VoidType: ...
    def set_ReturnValue(self, value: ObjectType) -> VoidType: ...
    def set_Uri(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ObjRefSurrogate(ObjectType, ISerializationSurrogate):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def GetObjectData(
        self, obj: ObjectType, info: SerializationInfo, context: StreamingContext
    ) -> VoidType: ...
    def SetObjectData(
        self,
        obj: ObjectType,
        info: SerializationInfo,
        context: StreamingContext,
        selector: ISurrogateSelector,
    ) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class OneWayAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RemotingSurrogate(ObjectType, ISerializationSurrogate):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def GetObjectData(
        self, obj: ObjectType, info: SerializationInfo, context: StreamingContext
    ) -> VoidType: ...
    def SetObjectData(
        self,
        obj: ObjectType,
        info: SerializationInfo,
        context: StreamingContext,
        selector: ISurrogateSelector,
    ) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RemotingSurrogateSelector(ObjectType, ISurrogateSelector):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def Filter(self) -> MessageSurrogateFilter: ...
    @Filter.setter
    def Filter(self, value: MessageSurrogateFilter) -> None: ...

    # ---------- Methods ---------- #

    def ChainSelector(self, selector: ISurrogateSelector) -> VoidType: ...
    def GetNextSelector(self) -> ISurrogateSelector: ...
    def GetRootObject(self) -> ObjectType: ...
    def GetSurrogate(
        self, type: TypeType, context: StreamingContext, ssout: ISurrogateSelector
    ) -> Tuple[ISerializationSurrogate, ISurrogateSelector]: ...
    def SetRootObject(self, obj: ObjectType) -> VoidType: ...
    def UseSoapFormat(self) -> VoidType: ...
    def get_Filter(self) -> MessageSurrogateFilter: ...
    def set_Filter(self, value: MessageSurrogateFilter) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ReturnMessage(ObjectType, IMethodReturnMessage, IMethodMessage, IMessage):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(
        self,
        ret: ObjectType,
        outArgs: ArrayType[ObjectType],
        outArgsCount: IntType,
        callCtx: LogicalCallContext,
        mcm: IMethodCallMessage,
    ): ...
    @overload
    def __init__(self, e: Exception, mcm: IMethodCallMessage): ...

    # ---------- Properties ---------- #

    @property
    def ArgCount(self) -> IntType: ...
    @property
    def Args(self) -> ArrayType[ObjectType]: ...
    @property
    def Exception(self) -> Exception: ...
    @property
    def HasVarArgs(self) -> BooleanType: ...
    @property
    def LogicalCallContext(self) -> LogicalCallContext: ...
    @property
    def MethodBase(self) -> MethodBase: ...
    @property
    def MethodName(self) -> StringType: ...
    @property
    def MethodSignature(self) -> ObjectType: ...
    @property
    def OutArgCount(self) -> IntType: ...
    @property
    def OutArgs(self) -> ArrayType[ObjectType]: ...
    @property
    def Properties(self) -> IDictionary: ...
    @property
    def ReturnValue(self) -> ObjectType: ...
    @property
    def TypeName(self) -> StringType: ...
    @property
    def Uri(self) -> StringType: ...
    @Uri.setter
    def Uri(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def GetArg(self, argNum: IntType) -> ObjectType: ...
    def GetArgName(self, index: IntType) -> StringType: ...
    def GetOutArg(self, argNum: IntType) -> ObjectType: ...
    def GetOutArgName(self, index: IntType) -> StringType: ...
    def get_ArgCount(self) -> IntType: ...
    def get_Args(self) -> ArrayType[ObjectType]: ...
    def get_Exception(self) -> Exception: ...
    def get_HasVarArgs(self) -> BooleanType: ...
    def get_LogicalCallContext(self) -> LogicalCallContext: ...
    def get_MethodBase(self) -> MethodBase: ...
    def get_MethodName(self) -> StringType: ...
    def get_MethodSignature(self) -> ObjectType: ...
    def get_OutArgCount(self) -> IntType: ...
    def get_OutArgs(self) -> ArrayType[ObjectType]: ...
    def get_Properties(self) -> IDictionary: ...
    def get_ReturnValue(self) -> ObjectType: ...
    def get_TypeName(self) -> StringType: ...
    def get_Uri(self) -> StringType: ...
    def set_Uri(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SerializationMonkey(ObjectType, ISerializable, IFieldInfo):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def FieldNames(self) -> ArrayType[StringType]: ...
    @FieldNames.setter
    def FieldNames(self, value: ArrayType[StringType]) -> None: ...
    @property
    def FieldTypes(self) -> ArrayType[TypeType]: ...
    @FieldTypes.setter
    def FieldTypes(self, value: ArrayType[TypeType]) -> None: ...

    # ---------- Methods ---------- #

    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    def get_FieldNames(self) -> ArrayType[StringType]: ...
    def get_FieldTypes(self) -> ArrayType[TypeType]: ...
    def set_FieldNames(self, value: ArrayType[StringType]) -> VoidType: ...
    def set_FieldTypes(self, value: ArrayType[TypeType]) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ServerContextTerminatorSink(InternalSink, IMessageSink):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def NextSink(self) -> IMessageSink: ...

    # ---------- Methods ---------- #

    def AsyncProcessMessage(self, reqMsg: IMessage, replySink: IMessageSink) -> IMessageCtrl: ...
    def SyncProcessMessage(self, reqMsg: IMessage) -> IMessage: ...
    def get_NextSink(self) -> IMessageSink: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ServerObjectTerminatorSink(InternalSink, IMessageSink):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def NextSink(self) -> IMessageSink: ...

    # ---------- Methods ---------- #

    def AsyncProcessMessage(self, reqMsg: IMessage, replySink: IMessageSink) -> IMessageCtrl: ...
    def SyncProcessMessage(self, reqMsg: IMessage) -> IMessage: ...
    def get_NextSink(self) -> IMessageSink: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SmuggledMethodCallMessage(MessageSmuggler):
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

class SmuggledMethodReturnMessage(MessageSmuggler):
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

class SmuggledObjRef(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, objRef: ObjRef): ...

    # ---------- Properties ---------- #

    @property
    def ObjRef(self) -> ObjRef: ...

    # ---------- Methods ---------- #

    def get_ObjRef(self) -> ObjRef: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SoapMessageSurrogate(ObjectType, ISerializationSurrogate):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def GetObjectData(
        self, obj: ObjectType, info: SerializationInfo, context: StreamingContext
    ) -> VoidType: ...
    def SetObjectData(
        self,
        obj: ObjectType,
        info: SerializationInfo,
        context: StreamingContext,
        selector: ISurrogateSelector,
    ) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class StackBasedReturnMessage(
    ObjectType, IMethodReturnMessage, IMethodMessage, IMessage, IInternalMessage
):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def ArgCount(self) -> IntType: ...
    @property
    def Args(self) -> ArrayType[ObjectType]: ...
    @property
    def Exception(self) -> Exception: ...
    @property
    def HasVarArgs(self) -> BooleanType: ...
    @property
    def LogicalCallContext(self) -> LogicalCallContext: ...
    @property
    def MethodBase(self) -> MethodBase: ...
    @property
    def MethodName(self) -> StringType: ...
    @property
    def MethodSignature(self) -> ObjectType: ...
    @property
    def OutArgCount(self) -> IntType: ...
    @property
    def OutArgs(self) -> ArrayType[ObjectType]: ...
    @property
    def Properties(self) -> IDictionary: ...
    @property
    def ReturnValue(self) -> ObjectType: ...
    @property
    def TypeName(self) -> StringType: ...
    @property
    def Uri(self) -> StringType: ...

    # ---------- Methods ---------- #

    def GetArg(self, argNum: IntType) -> ObjectType: ...
    def GetArgName(self, index: IntType) -> StringType: ...
    def GetOutArg(self, argNum: IntType) -> ObjectType: ...
    def GetOutArgName(self, index: IntType) -> StringType: ...
    def get_ArgCount(self) -> IntType: ...
    def get_Args(self) -> ArrayType[ObjectType]: ...
    def get_Exception(self) -> Exception: ...
    def get_HasVarArgs(self) -> BooleanType: ...
    def get_LogicalCallContext(self) -> LogicalCallContext: ...
    def get_MethodBase(self) -> MethodBase: ...
    def get_MethodName(self) -> StringType: ...
    def get_MethodSignature(self) -> ObjectType: ...
    def get_OutArgCount(self) -> IntType: ...
    def get_OutArgs(self) -> ArrayType[ObjectType]: ...
    def get_Properties(self) -> IDictionary: ...
    def get_ReturnValue(self) -> ObjectType: ...
    def get_TypeName(self) -> StringType: ...
    def get_Uri(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class StackBuilderSink(ObjectType, IMessageSink):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, server: MarshalByRefObject): ...
    @overload
    def __init__(self, server: ObjectType): ...

    # ---------- Properties ---------- #

    @property
    def NextSink(self) -> IMessageSink: ...

    # ---------- Methods ---------- #

    def AsyncProcessMessage(self, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl: ...
    def PrivateProcessMessage(
        self,
        md: RuntimeMethodHandle,
        args: ArrayType[ObjectType],
        server: ObjectType,
        outArgs: ObjectType,
    ) -> Tuple[ObjectType, ObjectType]: ...
    def SyncProcessMessage(self, msg: IMessage) -> IMessage: ...
    def get_NextSink(self) -> IMessageSink: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TransitionCall(ObjectType, IMessage, IInternalMessage, IMessageSink, ISerializable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def NextSink(self) -> IMessageSink: ...
    @property
    def Properties(self) -> IDictionary: ...

    # ---------- Methods ---------- #

    def AsyncProcessMessage(self, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    def SyncProcessMessage(self, msg: IMessage) -> IMessage: ...
    def get_NextSink(self) -> IMessageSink: ...
    def get_Properties(self) -> IDictionary: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# No Structs

# ---------- Interfaces ---------- #

class IInternalMessage(Protocol):
    # ---------- Properties ---------- #

    @property
    def IdentityObject(self) -> Identity: ...
    @IdentityObject.setter
    def IdentityObject(self, value: Identity) -> None: ...
    @property
    def ServerIdentityObject(self) -> ServerIdentity: ...
    @ServerIdentityObject.setter
    def ServerIdentityObject(self, value: ServerIdentity) -> None: ...

    # ---------- Methods ---------- #

    def HasProperties(self) -> BooleanType: ...
    def SetCallContext(self, callContext: LogicalCallContext) -> VoidType: ...
    def SetURI(self, uri: StringType) -> VoidType: ...
    def get_IdentityObject(self) -> Identity: ...
    def get_ServerIdentityObject(self) -> ServerIdentity: ...
    def set_IdentityObject(self, value: Identity) -> VoidType: ...
    def set_ServerIdentityObject(self, value: ServerIdentity) -> VoidType: ...

    # No Events

class ILogicalThreadAffinative(Protocol):
    """"""

    # No Properties

    # No Methods

    # No Events

class IMessage(Protocol):
    # ---------- Properties ---------- #

    @property
    def Properties(self) -> IDictionary: ...

    # ---------- Methods ---------- #

    def get_Properties(self) -> IDictionary: ...

    # No Events

class IMessageCtrl(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Cancel(self, msToCancel: IntType) -> VoidType: ...

    # No Events

class IMessageSink(Protocol):
    # ---------- Properties ---------- #

    @property
    def NextSink(self) -> IMessageSink: ...

    # ---------- Methods ---------- #

    def AsyncProcessMessage(self, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl: ...
    def SyncProcessMessage(self, msg: IMessage) -> IMessage: ...
    def get_NextSink(self) -> IMessageSink: ...

    # No Events

class IMethodCallMessage(Protocol, IMethodMessage, IMessage):
    # ---------- Properties ---------- #

    @property
    def InArgCount(self) -> IntType: ...
    @property
    def InArgs(self) -> ArrayType[ObjectType]: ...

    # ---------- Methods ---------- #

    def GetInArg(self, argNum: IntType) -> ObjectType: ...
    def GetInArgName(self, index: IntType) -> StringType: ...
    def get_InArgCount(self) -> IntType: ...
    def get_InArgs(self) -> ArrayType[ObjectType]: ...

    # No Events

class IMethodMessage(Protocol, IMessage):
    # ---------- Properties ---------- #

    @property
    def ArgCount(self) -> IntType: ...
    @property
    def Args(self) -> ArrayType[ObjectType]: ...
    @property
    def HasVarArgs(self) -> BooleanType: ...
    @property
    def LogicalCallContext(self) -> LogicalCallContext: ...
    @property
    def MethodBase(self) -> MethodBase: ...
    @property
    def MethodName(self) -> StringType: ...
    @property
    def MethodSignature(self) -> ObjectType: ...
    @property
    def TypeName(self) -> StringType: ...
    @property
    def Uri(self) -> StringType: ...

    # ---------- Methods ---------- #

    def GetArg(self, argNum: IntType) -> ObjectType: ...
    def GetArgName(self, index: IntType) -> StringType: ...
    def get_ArgCount(self) -> IntType: ...
    def get_Args(self) -> ArrayType[ObjectType]: ...
    def get_HasVarArgs(self) -> BooleanType: ...
    def get_LogicalCallContext(self) -> LogicalCallContext: ...
    def get_MethodBase(self) -> MethodBase: ...
    def get_MethodName(self) -> StringType: ...
    def get_MethodSignature(self) -> ObjectType: ...
    def get_TypeName(self) -> StringType: ...
    def get_Uri(self) -> StringType: ...

    # No Events

class IMethodReturnMessage(Protocol, IMethodMessage, IMessage):
    # ---------- Properties ---------- #

    @property
    def Exception(self) -> Exception: ...
    @property
    def OutArgCount(self) -> IntType: ...
    @property
    def OutArgs(self) -> ArrayType[ObjectType]: ...
    @property
    def ReturnValue(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def GetOutArg(self, argNum: IntType) -> ObjectType: ...
    def GetOutArgName(self, index: IntType) -> StringType: ...
    def get_Exception(self) -> Exception: ...
    def get_OutArgCount(self) -> IntType: ...
    def get_OutArgs(self) -> ArrayType[ObjectType]: ...
    def get_ReturnValue(self) -> ObjectType: ...

    # No Events

class IRemotingFormatter(Protocol, IFormatter):
    # No Properties

    # ---------- Methods ---------- #

    def Deserialize(self, serializationStream: Stream, handler: HeaderHandler) -> ObjectType: ...
    def Serialize(
        self, serializationStream: Stream, graph: ObjectType, headers: ArrayType[Header]
    ) -> VoidType: ...

    # No Events

class ISerializationRootObject(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def RootSetObjectData(self, info: SerializationInfo, ctx: StreamingContext) -> VoidType: ...

    # No Events

# No Enums

# ---------- Delegates ---------- #

HeaderHandler = Callable[[ArrayType[Header]], ObjectType]

MessageSurrogateFilter = Callable[[StringType, ObjectType], BooleanType]

__all__ = [
    ArgMapper,
    AsyncReplySink,
    AsyncResult,
    CCMDictionary,
    CRMDictionary,
    CallContext,
    CallContextRemotingData,
    CallContextSecurityData,
    ClientAsyncReplyTerminatorSink,
    ClientContextTerminatorSink,
    ConstructionCall,
    ConstructionResponse,
    ConstructorCallMessage,
    ConstructorReturnMessage,
    DisposeSink,
    EnvoyTerminatorSink,
    ErrorMessage,
    Header,
    HeaderHandler,
    IllogicalCallContext,
    InternalMessageWrapper,
    InternalSink,
    LogicalCallContext,
    MCMDictionary,
    MRMDictionary,
    Message,
    MessageDictionary,
    MessageDictionaryEnumerator,
    MessageSmuggler,
    MessageSurrogate,
    MessageSurrogateFilter,
    MethodCall,
    MethodCallMessageWrapper,
    MethodResponse,
    MethodReturnMessageWrapper,
    ObjRefSurrogate,
    OneWayAttribute,
    RemotingSurrogate,
    RemotingSurrogateSelector,
    ReturnMessage,
    SerializationMonkey,
    ServerContextTerminatorSink,
    ServerObjectTerminatorSink,
    SmuggledMethodCallMessage,
    SmuggledMethodReturnMessage,
    SmuggledObjRef,
    SoapMessageSurrogate,
    StackBasedReturnMessage,
    StackBuilderSink,
    TransitionCall,
    IInternalMessage,
    ILogicalThreadAffinative,
    IMessage,
    IMessageCtrl,
    IMessageSink,
    IMethodCallMessage,
    IMethodMessage,
    IMethodReturnMessage,
    IRemotingFormatter,
    ISerializationRootObject,
    HeaderHandler,
    MessageSurrogateFilter,
]
