from __future__ import annotations

from abc import ABC
from typing import List
from typing import Protocol
from typing import Tuple
from typing import Union
from typing import overload

from System import Array
from System import Boolean
from System import Enum
from System import Exception
from System import IAsyncResult
from System import Int32
from System import MarshalByRefObject
from System import Object
from System import String
from System import ValueType
from System import Void
from System.Collections import DictionaryEntry
from System.Collections import ICollection
from System.Collections import IDictionary
from System.Collections import IDictionaryEnumerator
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IList
from System.IO import Stream
from System.Runtime.Remoting.Messaging import IMessage
from System.Runtime.Remoting.Messaging import IMessageCtrl
from System.Runtime.Remoting.Messaging import IMessageSink
from System.Runtime.Remoting.Messaging import InternalSink

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class ADAsyncWorkItem(ObjectType):
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

class AggregateDictionary(ObjectType, IDictionary, ICollection, IEnumerable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, dictionaries: ICollection): ...

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
    def GetEnumerator(self) -> IDictionaryEnumerator: ...
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

class AsyncMessageHelper(ABC, ObjectType):
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

class AsyncWorkItem(ObjectType, IMessageSink):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def NextSink(self) -> IMessageSink: ...

    # ---------- Methods ---------- #

    def AsyncProcessMessage(self, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl: ...
    def SyncProcessMessage(self, msg: IMessage) -> IMessage: ...
    def get_NextSink(self) -> IMessageSink: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class BaseChannelObjectWithProperties(ABC, ObjectType, IDictionary, ICollection, IEnumerable):
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
    def Properties(self) -> IDictionary: ...
    @property
    def SyncRoot(self) -> ObjectType: ...
    @property
    def Values(self) -> ICollection: ...

    # ---------- Methods ---------- #

    def Add(self, key: ObjectType, value: ObjectType) -> VoidType: ...
    def Clear(self) -> VoidType: ...
    def Contains(self, key: ObjectType) -> BooleanType: ...
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    def GetEnumerator(self) -> IDictionaryEnumerator: ...
    def Remove(self, key: ObjectType) -> VoidType: ...
    def get_Count(self) -> IntType: ...
    def get_IsFixedSize(self) -> BooleanType: ...
    def get_IsReadOnly(self) -> BooleanType: ...
    def get_IsSynchronized(self) -> BooleanType: ...
    def get_Item(self, key: ObjectType) -> ObjectType: ...
    def get_Keys(self) -> ICollection: ...
    def get_Properties(self) -> IDictionary: ...
    def get_SyncRoot(self) -> ObjectType: ...
    def get_Values(self) -> ICollection: ...
    def set_Item(self, key: ObjectType, value: ObjectType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class BaseChannelSinkWithProperties(
    ABC, BaseChannelObjectWithProperties, IDictionary, ICollection, IEnumerable
):
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

class BaseChannelWithProperties(
    ABC, BaseChannelObjectWithProperties, IDictionary, ICollection, IEnumerable
):
    # No Fields

    # No Constructors

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

class ChannelDataStore(ObjectType, IChannelDataStore):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, channelURIs: ArrayType[StringType]): ...

    # ---------- Properties ---------- #

    @property
    def ChannelUris(self) -> ArrayType[StringType]: ...
    @ChannelUris.setter
    def ChannelUris(self, value: ArrayType[StringType]) -> None: ...
    def __getitem__(self, key: ObjectType) -> ObjectType: ...
    def __setitem__(self, key: ObjectType, value: ObjectType) -> None: ...

    # ---------- Methods ---------- #

    def get_ChannelUris(self) -> ArrayType[StringType]: ...
    def get_Item(self, key: ObjectType) -> ObjectType: ...
    def set_ChannelUris(self, value: ArrayType[StringType]) -> VoidType: ...
    def set_Item(self, key: ObjectType, value: ObjectType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ChannelServices(ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @staticmethod
    @property
    def RegisteredChannels() -> ArrayType[IChannel]: ...

    # ---------- Methods ---------- #

    @staticmethod
    def AsyncDispatchMessage(msg: IMessage, replySink: IMessageSink) -> IMessageCtrl: ...
    @staticmethod
    def CreateServerChannelSinkChain(
        provider: IServerChannelSinkProvider, channel: IChannelReceiver
    ) -> IServerChannelSink: ...
    @staticmethod
    def DispatchMessage(
        sinkStack: IServerChannelSinkStack, msg: IMessage, replyMsg: IMessage
    ) -> Tuple[ServerProcessing, IMessage]: ...
    @staticmethod
    def GetChannel(name: StringType) -> IChannel: ...
    @staticmethod
    def GetChannelSinkProperties(obj: ObjectType) -> IDictionary: ...
    @staticmethod
    def GetUrlsForObject(obj: MarshalByRefObject) -> ArrayType[StringType]: ...
    @staticmethod
    @overload
    def RegisterChannel(chnl: IChannel, ensureSecurity: BooleanType) -> VoidType: ...
    @staticmethod
    @overload
    def RegisterChannel(chnl: IChannel) -> VoidType: ...
    @staticmethod
    def SyncDispatchMessage(msg: IMessage) -> IMessage: ...
    @staticmethod
    def UnregisterChannel(chnl: IChannel) -> VoidType: ...
    @staticmethod
    def get_RegisteredChannels() -> ArrayType[IChannel]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ChannelServicesData(ObjectType):
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

class ClientChannelSinkStack(ObjectType, IClientChannelSinkStack, IClientResponseChannelSinkStack):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, replySink: IMessageSink): ...

    # No Properties

    # ---------- Methods ---------- #

    def AsyncProcessResponse(self, headers: ITransportHeaders, stream: Stream) -> VoidType: ...
    def DispatchException(self, e: Exception) -> VoidType: ...
    def DispatchReplyMessage(self, msg: IMessage) -> VoidType: ...
    def Pop(self, sink: IClientChannelSink) -> ObjectType: ...
    def Push(self, sink: IClientChannelSink, state: ObjectType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CrossAppDomainChannel(ObjectType, IChannel, IChannelSender, IChannelReceiver):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def ChannelData(self) -> ObjectType: ...
    @property
    def ChannelName(self) -> StringType: ...
    @property
    def ChannelPriority(self) -> IntType: ...
    @property
    def ChannelURI(self) -> StringType: ...

    # ---------- Methods ---------- #

    def CreateMessageSink(
        self, url: StringType, data: ObjectType, objectURI: StringType
    ) -> Tuple[IMessageSink, StringType]: ...
    def GetUrlsForUri(self, objectURI: StringType) -> ArrayType[StringType]: ...
    def Parse(self, url: StringType, objectURI: StringType) -> Tuple[StringType, StringType]: ...
    def StartListening(self, data: ObjectType) -> VoidType: ...
    def StopListening(self, data: ObjectType) -> VoidType: ...
    def get_ChannelData(self) -> ObjectType: ...
    def get_ChannelName(self) -> StringType: ...
    def get_ChannelPriority(self) -> IntType: ...
    def get_ChannelURI(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CrossAppDomainData(ObjectType):
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

class CrossAppDomainSerializer(ABC, ObjectType):
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

class CrossAppDomainSink(InternalSink, IMessageSink):
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

class CrossContextChannel(InternalSink, IMessageSink):
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

class DictionaryEnumeratorByKeys(ObjectType, IDictionaryEnumerator, IEnumerator):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, properties: IDictionary): ...

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

class DispatchChannelSink(ObjectType, IServerChannelSink, IChannelSinkBase):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def NextChannelSink(self) -> IServerChannelSink: ...
    @property
    def Properties(self) -> IDictionary: ...

    # ---------- Methods ---------- #

    def AsyncProcessResponse(
        self,
        sinkStack: IServerResponseChannelSinkStack,
        state: ObjectType,
        msg: IMessage,
        headers: ITransportHeaders,
        stream: Stream,
    ) -> VoidType: ...
    def GetResponseStream(
        self,
        sinkStack: IServerResponseChannelSinkStack,
        state: ObjectType,
        msg: IMessage,
        headers: ITransportHeaders,
    ) -> Stream: ...
    def ProcessMessage(
        self,
        sinkStack: IServerChannelSinkStack,
        requestMsg: IMessage,
        requestHeaders: ITransportHeaders,
        requestStream: Stream,
        responseMsg: IMessage,
        responseHeaders: ITransportHeaders,
        responseStream: Stream,
    ) -> Tuple[ServerProcessing, IMessage, ITransportHeaders, Stream]: ...
    def get_NextChannelSink(self) -> IServerChannelSink: ...
    def get_Properties(self) -> IDictionary: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DispatchChannelSinkProvider(ObjectType, IServerChannelSinkProvider):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Next(self) -> IServerChannelSinkProvider: ...
    @Next.setter
    def Next(self, value: IServerChannelSinkProvider) -> None: ...

    # ---------- Methods ---------- #

    def CreateSink(self, channel: IChannelReceiver) -> IServerChannelSink: ...
    def GetChannelData(self, channelData: IChannelDataStore) -> VoidType: ...
    def get_Next(self) -> IServerChannelSinkProvider: ...
    def set_Next(self, value: IServerChannelSinkProvider) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RegisteredChannel(ObjectType):
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

class RegisteredChannelList(ObjectType):
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

class ServerAsyncReplyTerminatorSink(ObjectType, IMessageSink):
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

class ServerChannelSinkStack(ObjectType, IServerChannelSinkStack, IServerResponseChannelSinkStack):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def AsyncProcessResponse(
        self, msg: IMessage, headers: ITransportHeaders, stream: Stream
    ) -> VoidType: ...
    def GetResponseStream(self, msg: IMessage, headers: ITransportHeaders) -> Stream: ...
    def Pop(self, sink: IServerChannelSink) -> ObjectType: ...
    def Push(self, sink: IServerChannelSink, state: ObjectType) -> VoidType: ...
    def ServerCallback(self, ar: IAsyncResult) -> VoidType: ...
    def Store(self, sink: IServerChannelSink, state: ObjectType) -> VoidType: ...
    def StoreAndDispatch(self, sink: IServerChannelSink, state: ObjectType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SinkProviderData(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, name: StringType): ...

    # ---------- Properties ---------- #

    @property
    def Children(self) -> IList: ...
    @property
    def Name(self) -> StringType: ...
    @property
    def Properties(self) -> IDictionary: ...

    # ---------- Methods ---------- #

    def get_Children(self) -> IList: ...
    def get_Name(self) -> StringType: ...
    def get_Properties(self) -> IDictionary: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TransportHeaders(ObjectType, ITransportHeaders):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    def __getitem__(self, key: ObjectType) -> ObjectType: ...
    def __setitem__(self, key: ObjectType, value: ObjectType) -> None: ...

    # ---------- Methods ---------- #

    def GetEnumerator(self) -> IEnumerator: ...
    def get_Item(self, key: ObjectType) -> ObjectType: ...
    def set_Item(self, key: ObjectType, value: ObjectType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# ---------- Structs ---------- #

class Perf_Contexts(ValueType):
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

# ---------- Interfaces ---------- #

class IChannel(Protocol):
    # ---------- Properties ---------- #

    @property
    def ChannelName(self) -> StringType: ...
    @property
    def ChannelPriority(self) -> IntType: ...

    # ---------- Methods ---------- #

    def Parse(self, url: StringType, objectURI: StringType) -> Tuple[StringType, StringType]: ...
    def get_ChannelName(self) -> StringType: ...
    def get_ChannelPriority(self) -> IntType: ...

    # No Events

class IChannelDataStore(Protocol):
    # ---------- Properties ---------- #

    @property
    def ChannelUris(self) -> ArrayType[StringType]: ...
    def __getitem__(self, key: ObjectType) -> ObjectType: ...
    def __setitem__(self, key: ObjectType, value: ObjectType) -> None: ...

    # ---------- Methods ---------- #

    def get_ChannelUris(self) -> ArrayType[StringType]: ...
    def get_Item(self, key: ObjectType) -> ObjectType: ...
    def set_Item(self, key: ObjectType, value: ObjectType) -> VoidType: ...

    # No Events

class IChannelReceiver(Protocol, IChannel):
    # ---------- Properties ---------- #

    @property
    def ChannelData(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def GetUrlsForUri(self, objectURI: StringType) -> ArrayType[StringType]: ...
    def StartListening(self, data: ObjectType) -> VoidType: ...
    def StopListening(self, data: ObjectType) -> VoidType: ...
    def get_ChannelData(self) -> ObjectType: ...

    # No Events

class IChannelReceiverHook(Protocol):
    # ---------- Properties ---------- #

    @property
    def ChannelScheme(self) -> StringType: ...
    @property
    def ChannelSinkChain(self) -> IServerChannelSink: ...
    @property
    def WantsToListen(self) -> BooleanType: ...

    # ---------- Methods ---------- #

    def AddHookChannelUri(self, channelUri: StringType) -> VoidType: ...
    def get_ChannelScheme(self) -> StringType: ...
    def get_ChannelSinkChain(self) -> IServerChannelSink: ...
    def get_WantsToListen(self) -> BooleanType: ...

    # No Events

class IChannelSender(Protocol, IChannel):
    # No Properties

    # ---------- Methods ---------- #

    def CreateMessageSink(
        self, url: StringType, remoteChannelData: ObjectType, objectURI: StringType
    ) -> Tuple[IMessageSink, StringType]: ...

    # No Events

class IChannelSinkBase(Protocol):
    # ---------- Properties ---------- #

    @property
    def Properties(self) -> IDictionary: ...

    # ---------- Methods ---------- #

    def get_Properties(self) -> IDictionary: ...

    # No Events

class IClientChannelSink(Protocol, IChannelSinkBase):
    # ---------- Properties ---------- #

    @property
    def NextChannelSink(self) -> IClientChannelSink: ...

    # ---------- Methods ---------- #

    def AsyncProcessRequest(
        self,
        sinkStack: IClientChannelSinkStack,
        msg: IMessage,
        headers: ITransportHeaders,
        stream: Stream,
    ) -> VoidType: ...
    def AsyncProcessResponse(
        self,
        sinkStack: IClientResponseChannelSinkStack,
        state: ObjectType,
        headers: ITransportHeaders,
        stream: Stream,
    ) -> VoidType: ...
    def GetRequestStream(self, msg: IMessage, headers: ITransportHeaders) -> Stream: ...
    def ProcessMessage(
        self,
        msg: IMessage,
        requestHeaders: ITransportHeaders,
        requestStream: Stream,
        responseHeaders: ITransportHeaders,
        responseStream: Stream,
    ) -> Tuple[VoidType, ITransportHeaders, Stream]: ...
    def get_NextChannelSink(self) -> IClientChannelSink: ...

    # No Events

class IClientChannelSinkProvider(Protocol):
    # ---------- Properties ---------- #

    @property
    def Next(self) -> IClientChannelSinkProvider: ...
    @Next.setter
    def Next(self, value: IClientChannelSinkProvider) -> None: ...

    # ---------- Methods ---------- #

    def CreateSink(
        self, channel: IChannelSender, url: StringType, remoteChannelData: ObjectType
    ) -> IClientChannelSink: ...
    def get_Next(self) -> IClientChannelSinkProvider: ...
    def set_Next(self, value: IClientChannelSinkProvider) -> VoidType: ...

    # No Events

class IClientChannelSinkStack(Protocol, IClientResponseChannelSinkStack):
    # No Properties

    # ---------- Methods ---------- #

    def Pop(self, sink: IClientChannelSink) -> ObjectType: ...
    def Push(self, sink: IClientChannelSink, state: ObjectType) -> VoidType: ...

    # No Events

class IClientFormatterSink(Protocol, IMessageSink, IClientChannelSink, IChannelSinkBase):
    """"""

    # No Properties

    # No Methods

    # No Events

class IClientFormatterSinkProvider(Protocol, IClientChannelSinkProvider):
    """"""

    # No Properties

    # No Methods

    # No Events

class IClientResponseChannelSinkStack(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def AsyncProcessResponse(self, headers: ITransportHeaders, stream: Stream) -> VoidType: ...
    def DispatchException(self, e: Exception) -> VoidType: ...
    def DispatchReplyMessage(self, msg: IMessage) -> VoidType: ...

    # No Events

class ISecurableChannel(Protocol):
    # ---------- Properties ---------- #

    @property
    def IsSecured(self) -> BooleanType: ...
    @IsSecured.setter
    def IsSecured(self, value: BooleanType) -> None: ...

    # ---------- Methods ---------- #

    def get_IsSecured(self) -> BooleanType: ...
    def set_IsSecured(self, value: BooleanType) -> VoidType: ...

    # No Events

class IServerChannelSink(Protocol, IChannelSinkBase):
    # ---------- Properties ---------- #

    @property
    def NextChannelSink(self) -> IServerChannelSink: ...

    # ---------- Methods ---------- #

    def AsyncProcessResponse(
        self,
        sinkStack: IServerResponseChannelSinkStack,
        state: ObjectType,
        msg: IMessage,
        headers: ITransportHeaders,
        stream: Stream,
    ) -> VoidType: ...
    def GetResponseStream(
        self,
        sinkStack: IServerResponseChannelSinkStack,
        state: ObjectType,
        msg: IMessage,
        headers: ITransportHeaders,
    ) -> Stream: ...
    def ProcessMessage(
        self,
        sinkStack: IServerChannelSinkStack,
        requestMsg: IMessage,
        requestHeaders: ITransportHeaders,
        requestStream: Stream,
        responseMsg: IMessage,
        responseHeaders: ITransportHeaders,
        responseStream: Stream,
    ) -> Tuple[ServerProcessing, IMessage, ITransportHeaders, Stream]: ...
    def get_NextChannelSink(self) -> IServerChannelSink: ...

    # No Events

class IServerChannelSinkProvider(Protocol):
    # ---------- Properties ---------- #

    @property
    def Next(self) -> IServerChannelSinkProvider: ...
    @Next.setter
    def Next(self, value: IServerChannelSinkProvider) -> None: ...

    # ---------- Methods ---------- #

    def CreateSink(self, channel: IChannelReceiver) -> IServerChannelSink: ...
    def GetChannelData(self, channelData: IChannelDataStore) -> VoidType: ...
    def get_Next(self) -> IServerChannelSinkProvider: ...
    def set_Next(self, value: IServerChannelSinkProvider) -> VoidType: ...

    # No Events

class IServerChannelSinkStack(Protocol, IServerResponseChannelSinkStack):
    # No Properties

    # ---------- Methods ---------- #

    def Pop(self, sink: IServerChannelSink) -> ObjectType: ...
    def Push(self, sink: IServerChannelSink, state: ObjectType) -> VoidType: ...
    def ServerCallback(self, ar: IAsyncResult) -> VoidType: ...
    def Store(self, sink: IServerChannelSink, state: ObjectType) -> VoidType: ...
    def StoreAndDispatch(self, sink: IServerChannelSink, state: ObjectType) -> VoidType: ...

    # No Events

class IServerFormatterSinkProvider(Protocol, IServerChannelSinkProvider):
    """"""

    # No Properties

    # No Methods

    # No Events

class IServerResponseChannelSinkStack(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def AsyncProcessResponse(
        self, msg: IMessage, headers: ITransportHeaders, stream: Stream
    ) -> VoidType: ...
    def GetResponseStream(self, msg: IMessage, headers: ITransportHeaders) -> Stream: ...

    # No Events

class ITransportHeaders(Protocol):
    # ---------- Properties ---------- #

    def __getitem__(self, key: ObjectType) -> ObjectType: ...
    def __setitem__(self, key: ObjectType, value: ObjectType) -> None: ...

    # ---------- Methods ---------- #

    def GetEnumerator(self) -> IEnumerator: ...
    def get_Item(self, key: ObjectType) -> ObjectType: ...
    def set_Item(self, key: ObjectType, value: ObjectType) -> VoidType: ...

    # No Events

# ---------- Enums ---------- #

class RemotingProfilerEvent(Enum):
    ClientSend = 0
    ClientReceive = 1

class ServerProcessing(Enum):
    Complete = 0
    OneWay = 1
    Async = 2

# No Delegates

__all__ = [
    ADAsyncWorkItem,
    AggregateDictionary,
    AsyncMessageHelper,
    AsyncWorkItem,
    BaseChannelObjectWithProperties,
    BaseChannelSinkWithProperties,
    BaseChannelWithProperties,
    ChannelDataStore,
    ChannelServices,
    ChannelServicesData,
    ClientChannelSinkStack,
    CrossAppDomainChannel,
    CrossAppDomainData,
    CrossAppDomainSerializer,
    CrossAppDomainSink,
    CrossContextChannel,
    DictionaryEnumeratorByKeys,
    DispatchChannelSink,
    DispatchChannelSinkProvider,
    RegisteredChannel,
    RegisteredChannelList,
    ServerAsyncReplyTerminatorSink,
    ServerChannelSinkStack,
    SinkProviderData,
    TransportHeaders,
    Perf_Contexts,
    IChannel,
    IChannelDataStore,
    IChannelReceiver,
    IChannelReceiverHook,
    IChannelSender,
    IChannelSinkBase,
    IClientChannelSink,
    IClientChannelSinkProvider,
    IClientChannelSinkStack,
    IClientFormatterSink,
    IClientFormatterSinkProvider,
    IClientResponseChannelSinkStack,
    ISecurableChannel,
    IServerChannelSink,
    IServerChannelSinkProvider,
    IServerChannelSinkStack,
    IServerFormatterSinkProvider,
    IServerResponseChannelSinkStack,
    ITransportHeaders,
    RemotingProfilerEvent,
    ServerProcessing,
]
