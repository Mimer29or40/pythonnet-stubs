from __future__ import annotations

from abc import ABC
from typing import Iterator
from typing import Tuple
from typing import overload

from System import Array
from System import Enum
from System import Exception
from System import IAsyncResult
from System import MarshalByRefObject
from System import Object
from System import Type
from System import ValueType
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

class ADAsyncWorkItem(Object):
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

class AggregateDictionary(Object, ICollection, IDictionary, IEnumerable):
    """"""

    def __init__(self, dictionaries: ICollection):
        """

        :param dictionaries:
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

class AsyncMessageHelper(ABC, Object):
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

class AsyncWorkItem(Object, IMessageSink):
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

class BaseChannelObjectWithProperties(ABC, Object, ICollection, IDictionary, IEnumerable):
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
    def Properties(self) -> IDictionary:
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

class BaseChannelSinkWithProperties(
    ABC, BaseChannelObjectWithProperties, ICollection, IDictionary, IEnumerable
):
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
    def Properties(self) -> IDictionary:
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

class BaseChannelWithProperties(
    ABC, BaseChannelObjectWithProperties, ICollection, IDictionary, IEnumerable
):
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
    def Properties(self) -> IDictionary:
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

class ChannelDataStore(Object, IChannelDataStore):
    """"""

    def __init__(self, channelURIs: Array[str]):
        """

        :param channelURIs:
        """
    @property
    def ChannelUris(self) -> Array[str]:
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
    def __getitem__(self, key: object) -> object:
        """

        :param key:
        :return:
        """
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class ChannelServices(Object):
    """"""

    @classmethod
    @property
    def RegisteredChannels(cls) -> Array[IChannel]:
        """

        :return:
        """
    @classmethod
    def AsyncDispatchMessage(cls, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl:
        """

        :param msg:
        :param replySink:
        :return:
        """
    @classmethod
    def CreateServerChannelSinkChain(
        cls, provider: IServerChannelSinkProvider, channel: IChannelReceiver
    ) -> IServerChannelSink:
        """

        :param provider:
        :param channel:
        :return:
        """
    @classmethod
    def DispatchMessage(
        cls, sinkStack: IServerChannelSinkStack, msg: IMessage, replyMsg: IMessage
    ) -> Tuple[ServerProcessing, IMessage]:
        """

        :param sinkStack:
        :param msg:
        :param replyMsg:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetChannel(cls, name: str) -> IChannel:
        """

        :param name:
        :return:
        """
    @classmethod
    def GetChannelSinkProperties(cls, obj: object) -> IDictionary:
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
    def GetUrlsForObject(cls, obj: MarshalByRefObject) -> Array[str]:
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def RegisterChannel(cls, chnl: IChannel) -> None:
        """

        :param chnl:
        """
    @classmethod
    @overload
    def RegisterChannel(cls, chnl: IChannel, ensureSecurity: bool) -> None:
        """

        :param chnl:
        :param ensureSecurity:
        """
    @classmethod
    def SyncDispatchMessage(cls, msg: IMessage) -> IMessage:
        """

        :param msg:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def UnregisterChannel(cls, chnl: IChannel) -> None:
        """

        :param chnl:
        """

class ChannelServicesData(Object):
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

class ClientChannelSinkStack(Object, IClientChannelSinkStack, IClientResponseChannelSinkStack):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, replySink: IMessageSink):
        """

        :param replySink:
        """
    def AsyncProcessResponse(self, headers: ITransportHeaders, stream: Stream) -> None:
        """

        :param headers:
        :param stream:
        """
    def DispatchException(self, e: Exception) -> None:
        """

        :param e:
        """
    def DispatchReplyMessage(self, msg: IMessage) -> None:
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
    def Pop(self, sink: IClientChannelSink) -> object:
        """

        :param sink:
        :return:
        """
    def Push(self, sink: IClientChannelSink, state: object) -> None:
        """

        :param sink:
        :param state:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CrossAppDomainChannel(Object, IChannel, IChannelReceiver, IChannelSender):
    """"""

    def __init__(self):
        """"""
    @property
    def ChannelData(self) -> object:
        """

        :return:
        """
    @property
    def ChannelName(self) -> str:
        """

        :return:
        """
    @property
    def ChannelPriority(self) -> int:
        """

        :return:
        """
    @property
    def ChannelURI(self) -> str:
        """

        :return:
        """
    def CreateMessageSink(
        self, url: str, remoteChannelData: object, objectURI: str
    ) -> Tuple[IMessageSink, str]:
        """

        :param url:
        :param remoteChannelData:
        :param objectURI:
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
    def GetUrlsForUri(self, objectURI: str) -> Array[str]:
        """

        :param objectURI:
        :return:
        """
    def Parse(self, url: str, objectURI: str) -> Tuple[str, str]:
        """

        :param url:
        :param objectURI:
        :return:
        """
    def StartListening(self, data: object) -> None:
        """

        :param data:
        """
    def StopListening(self, data: object) -> None:
        """

        :param data:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CrossAppDomainData(Object):
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

class CrossAppDomainSerializer(ABC, Object):
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

class CrossAppDomainSink(InternalSink, IMessageSink):
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

class CrossContextChannel(InternalSink, IMessageSink):
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

class DictionaryEnumeratorByKeys(Object, IDictionaryEnumerator, IEnumerator):
    """"""

    def __init__(self, properties: IDictionary):
        """

        :param properties:
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

class DispatchChannelSink(Object, IChannelSinkBase, IServerChannelSink):
    """"""

    @property
    def NextChannelSink(self) -> IServerChannelSink:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """
    def AsyncProcessResponse(
        self,
        sinkStack: IServerResponseChannelSinkStack,
        state: object,
        msg: IMessage,
        headers: ITransportHeaders,
        stream: Stream,
    ) -> None:
        """

        :param sinkStack:
        :param state:
        :param msg:
        :param headers:
        :param stream:
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
    def GetResponseStream(
        self,
        sinkStack: IServerResponseChannelSinkStack,
        state: object,
        msg: IMessage,
        headers: ITransportHeaders,
    ) -> Stream:
        """

        :param sinkStack:
        :param state:
        :param msg:
        :param headers:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ProcessMessage(
        self,
        sinkStack: IServerChannelSinkStack,
        requestMsg: IMessage,
        requestHeaders: ITransportHeaders,
        requestStream: Stream,
        responseMsg: IMessage,
        responseHeaders: ITransportHeaders,
        responseStream: Stream,
    ) -> Tuple[ServerProcessing, IMessage, ITransportHeaders, Stream]:
        """

        :param sinkStack:
        :param requestMsg:
        :param requestHeaders:
        :param requestStream:
        :param responseMsg:
        :param responseHeaders:
        :param responseStream:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DispatchChannelSinkProvider(Object, IServerChannelSinkProvider):
    """"""

    @property
    def Next(self) -> IServerChannelSinkProvider:
        """

        :return:
        """
    @Next.setter
    def Next(self, value: IServerChannelSinkProvider) -> None: ...
    def CreateSink(self, channel: IChannelReceiver) -> IServerChannelSink:
        """

        :param channel:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetChannelData(self, channelData: IChannelDataStore) -> None:
        """

        :param channelData:
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

class IChannel:
    """"""

    @property
    def ChannelName(self) -> str:
        """

        :return:
        """
    @property
    def ChannelPriority(self) -> int:
        """

        :return:
        """
    def Parse(self, url: str, objectURI: str) -> Tuple[str, str]:
        """

        :param url:
        :param objectURI:
        :return:
        """

class IChannelDataStore:
    """"""

    @property
    def ChannelUris(self) -> Array[str]:
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
    def __getitem__(self, key: object) -> object:
        """

        :param key:
        :return:
        """
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class IChannelReceiver(IChannel):
    """"""

    @property
    def ChannelData(self) -> object:
        """

        :return:
        """
    @property
    def ChannelName(self) -> str:
        """

        :return:
        """
    @property
    def ChannelPriority(self) -> int:
        """

        :return:
        """
    def GetUrlsForUri(self, objectURI: str) -> Array[str]:
        """

        :param objectURI:
        :return:
        """
    def Parse(self, url: str, objectURI: str) -> Tuple[str, str]:
        """

        :param url:
        :param objectURI:
        :return:
        """
    def StartListening(self, data: object) -> None:
        """

        :param data:
        """
    def StopListening(self, data: object) -> None:
        """

        :param data:
        """

class IChannelReceiverHook:
    """"""

    @property
    def ChannelScheme(self) -> str:
        """

        :return:
        """
    @property
    def ChannelSinkChain(self) -> IServerChannelSink:
        """

        :return:
        """
    @property
    def WantsToListen(self) -> bool:
        """

        :return:
        """
    def AddHookChannelUri(self, channelUri: str) -> None:
        """

        :param channelUri:
        """

class IChannelSender(IChannel):
    """"""

    @property
    def ChannelName(self) -> str:
        """

        :return:
        """
    @property
    def ChannelPriority(self) -> int:
        """

        :return:
        """
    def CreateMessageSink(
        self, url: str, remoteChannelData: object, objectURI: str
    ) -> Tuple[IMessageSink, str]:
        """

        :param url:
        :param remoteChannelData:
        :param objectURI:
        :return:
        """
    def Parse(self, url: str, objectURI: str) -> Tuple[str, str]:
        """

        :param url:
        :param objectURI:
        :return:
        """

class IChannelSinkBase:
    """"""

    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """

class IClientChannelSink(IChannelSinkBase):
    """"""

    @property
    def NextChannelSink(self) -> IClientChannelSink:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """
    def AsyncProcessRequest(
        self,
        sinkStack: IClientChannelSinkStack,
        msg: IMessage,
        headers: ITransportHeaders,
        stream: Stream,
    ) -> None:
        """

        :param sinkStack:
        :param msg:
        :param headers:
        :param stream:
        """
    def AsyncProcessResponse(
        self,
        sinkStack: IClientResponseChannelSinkStack,
        state: object,
        headers: ITransportHeaders,
        stream: Stream,
    ) -> None:
        """

        :param sinkStack:
        :param state:
        :param headers:
        :param stream:
        """
    def GetRequestStream(self, msg: IMessage, headers: ITransportHeaders) -> Stream:
        """

        :param msg:
        :param headers:
        :return:
        """
    def ProcessMessage(
        self,
        msg: IMessage,
        requestHeaders: ITransportHeaders,
        requestStream: Stream,
        responseHeaders: ITransportHeaders,
        responseStream: Stream,
    ) -> Tuple[None, ITransportHeaders, Stream]:
        """

        :param msg:
        :param requestHeaders:
        :param requestStream:
        :param responseHeaders:
        :param responseStream:
        """

class IClientChannelSinkProvider:
    """"""

    @property
    def Next(self) -> IClientChannelSinkProvider:
        """

        :return:
        """
    @Next.setter
    def Next(self, value: IClientChannelSinkProvider) -> None: ...
    def CreateSink(
        self, channel: IChannelSender, url: str, remoteChannelData: object
    ) -> IClientChannelSink:
        """

        :param channel:
        :param url:
        :param remoteChannelData:
        :return:
        """

class IClientChannelSinkStack(IClientResponseChannelSinkStack):
    """"""

    def AsyncProcessResponse(self, headers: ITransportHeaders, stream: Stream) -> None:
        """

        :param headers:
        :param stream:
        """
    def DispatchException(self, e: Exception) -> None:
        """

        :param e:
        """
    def DispatchReplyMessage(self, msg: IMessage) -> None:
        """

        :param msg:
        """
    def Pop(self, sink: IClientChannelSink) -> object:
        """

        :param sink:
        :return:
        """
    def Push(self, sink: IClientChannelSink, state: object) -> None:
        """

        :param sink:
        :param state:
        """

class IClientFormatterSink(IChannelSinkBase, IClientChannelSink, IMessageSink):
    """"""

    @property
    def NextChannelSink(self) -> IClientChannelSink:
        """

        :return:
        """
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
    def AsyncProcessMessage(self, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl:
        """

        :param msg:
        :param replySink:
        :return:
        """
    def AsyncProcessRequest(
        self,
        sinkStack: IClientChannelSinkStack,
        msg: IMessage,
        headers: ITransportHeaders,
        stream: Stream,
    ) -> None:
        """

        :param sinkStack:
        :param msg:
        :param headers:
        :param stream:
        """
    def AsyncProcessResponse(
        self,
        sinkStack: IClientResponseChannelSinkStack,
        state: object,
        headers: ITransportHeaders,
        stream: Stream,
    ) -> None:
        """

        :param sinkStack:
        :param state:
        :param headers:
        :param stream:
        """
    def GetRequestStream(self, msg: IMessage, headers: ITransportHeaders) -> Stream:
        """

        :param msg:
        :param headers:
        :return:
        """
    def ProcessMessage(
        self,
        msg: IMessage,
        requestHeaders: ITransportHeaders,
        requestStream: Stream,
        responseHeaders: ITransportHeaders,
        responseStream: Stream,
    ) -> Tuple[None, ITransportHeaders, Stream]:
        """

        :param msg:
        :param requestHeaders:
        :param requestStream:
        :param responseHeaders:
        :param responseStream:
        """
    def SyncProcessMessage(self, msg: IMessage) -> IMessage:
        """

        :param msg:
        :return:
        """

class IClientFormatterSinkProvider(IClientChannelSinkProvider):
    """"""

    @property
    def Next(self) -> IClientChannelSinkProvider:
        """

        :return:
        """
    @Next.setter
    def Next(self, value: IClientChannelSinkProvider) -> None: ...
    def CreateSink(
        self, channel: IChannelSender, url: str, remoteChannelData: object
    ) -> IClientChannelSink:
        """

        :param channel:
        :param url:
        :param remoteChannelData:
        :return:
        """

class IClientResponseChannelSinkStack:
    """"""

    def AsyncProcessResponse(self, headers: ITransportHeaders, stream: Stream) -> None:
        """

        :param headers:
        :param stream:
        """
    def DispatchException(self, e: Exception) -> None:
        """

        :param e:
        """
    def DispatchReplyMessage(self, msg: IMessage) -> None:
        """

        :param msg:
        """

class ISecurableChannel:
    """"""

    @property
    def IsSecured(self) -> bool:
        """

        :return:
        """
    @IsSecured.setter
    def IsSecured(self, value: bool) -> None: ...

class IServerChannelSink(IChannelSinkBase):
    """"""

    @property
    def NextChannelSink(self) -> IServerChannelSink:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """
    def AsyncProcessResponse(
        self,
        sinkStack: IServerResponseChannelSinkStack,
        state: object,
        msg: IMessage,
        headers: ITransportHeaders,
        stream: Stream,
    ) -> None:
        """

        :param sinkStack:
        :param state:
        :param msg:
        :param headers:
        :param stream:
        """
    def GetResponseStream(
        self,
        sinkStack: IServerResponseChannelSinkStack,
        state: object,
        msg: IMessage,
        headers: ITransportHeaders,
    ) -> Stream:
        """

        :param sinkStack:
        :param state:
        :param msg:
        :param headers:
        :return:
        """
    def ProcessMessage(
        self,
        sinkStack: IServerChannelSinkStack,
        requestMsg: IMessage,
        requestHeaders: ITransportHeaders,
        requestStream: Stream,
        responseMsg: IMessage,
        responseHeaders: ITransportHeaders,
        responseStream: Stream,
    ) -> Tuple[ServerProcessing, IMessage, ITransportHeaders, Stream]:
        """

        :param sinkStack:
        :param requestMsg:
        :param requestHeaders:
        :param requestStream:
        :param responseMsg:
        :param responseHeaders:
        :param responseStream:
        :return:
        """

class IServerChannelSinkProvider:
    """"""

    @property
    def Next(self) -> IServerChannelSinkProvider:
        """

        :return:
        """
    @Next.setter
    def Next(self, value: IServerChannelSinkProvider) -> None: ...
    def CreateSink(self, channel: IChannelReceiver) -> IServerChannelSink:
        """

        :param channel:
        :return:
        """
    def GetChannelData(self, channelData: IChannelDataStore) -> None:
        """

        :param channelData:
        """

class IServerChannelSinkStack(IServerResponseChannelSinkStack):
    """"""

    def AsyncProcessResponse(
        self, msg: IMessage, headers: ITransportHeaders, stream: Stream
    ) -> None:
        """

        :param msg:
        :param headers:
        :param stream:
        """
    def GetResponseStream(self, msg: IMessage, headers: ITransportHeaders) -> Stream:
        """

        :param msg:
        :param headers:
        :return:
        """
    def Pop(self, sink: IServerChannelSink) -> object:
        """

        :param sink:
        :return:
        """
    def Push(self, sink: IServerChannelSink, state: object) -> None:
        """

        :param sink:
        :param state:
        """
    def ServerCallback(self, ar: IAsyncResult) -> None:
        """

        :param ar:
        """
    def Store(self, sink: IServerChannelSink, state: object) -> None:
        """

        :param sink:
        :param state:
        """
    def StoreAndDispatch(self, sink: IServerChannelSink, state: object) -> None:
        """

        :param sink:
        :param state:
        """

class IServerFormatterSinkProvider(IServerChannelSinkProvider):
    """"""

    @property
    def Next(self) -> IServerChannelSinkProvider:
        """

        :return:
        """
    @Next.setter
    def Next(self, value: IServerChannelSinkProvider) -> None: ...
    def CreateSink(self, channel: IChannelReceiver) -> IServerChannelSink:
        """

        :param channel:
        :return:
        """
    def GetChannelData(self, channelData: IChannelDataStore) -> None:
        """

        :param channelData:
        """

class IServerResponseChannelSinkStack:
    """"""

    def AsyncProcessResponse(
        self, msg: IMessage, headers: ITransportHeaders, stream: Stream
    ) -> None:
        """

        :param msg:
        :param headers:
        :param stream:
        """
    def GetResponseStream(self, msg: IMessage, headers: ITransportHeaders) -> Stream:
        """

        :param msg:
        :param headers:
        :return:
        """

class ITransportHeaders:
    """"""

    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def __getitem__(self, key: object) -> object:
        """

        :param key:
        :return:
        """
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class Perf_Contexts(ValueType):
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

class RegisteredChannel(Object):
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

class RegisteredChannelList(Object):
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

class RemotingProfilerEvent(Enum):
    """"""

    ClientSend: RemotingProfilerEvent = ...
    """"""
    ClientReceive: RemotingProfilerEvent = ...
    """"""

class ServerAsyncReplyTerminatorSink(Object, IMessageSink):
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

class ServerChannelSinkStack(Object, IServerChannelSinkStack, IServerResponseChannelSinkStack):
    """"""

    def __init__(self):
        """"""
    def AsyncProcessResponse(
        self, msg: IMessage, headers: ITransportHeaders, stream: Stream
    ) -> None:
        """

        :param msg:
        :param headers:
        :param stream:
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
    def GetResponseStream(self, msg: IMessage, headers: ITransportHeaders) -> Stream:
        """

        :param msg:
        :param headers:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Pop(self, sink: IServerChannelSink) -> object:
        """

        :param sink:
        :return:
        """
    def Push(self, sink: IServerChannelSink, state: object) -> None:
        """

        :param sink:
        :param state:
        """
    def ServerCallback(self, ar: IAsyncResult) -> None:
        """

        :param ar:
        """
    def Store(self, sink: IServerChannelSink, state: object) -> None:
        """

        :param sink:
        :param state:
        """
    def StoreAndDispatch(self, sink: IServerChannelSink, state: object) -> None:
        """

        :param sink:
        :param state:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ServerProcessing(Enum):
    """"""

    Complete: ServerProcessing = ...
    """"""
    OneWay: ServerProcessing = ...
    """"""
    Async: ServerProcessing = ...
    """"""

class SinkProviderData(Object):
    """"""

    def __init__(self, name: str):
        """

        :param name:
        """
    @property
    def Children(self) -> IList:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary:
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

class TransportHeaders(Object, ITransportHeaders):
    """"""

    def __init__(self):
        """"""
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
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
    def ToString(self) -> str:
        """

        :return:
        """
    def __getitem__(self, key: object) -> object:
        """

        :param key:
        :return:
        """
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """
