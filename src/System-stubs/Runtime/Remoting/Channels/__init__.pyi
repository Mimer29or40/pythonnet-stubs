"""Automatically generated stubs for C# namespace: System.Runtime.Remoting.Channels."""

from abc import ABC
from collections.abc import Iterator
from typing import overload

from System import Array
from System import Enum
from System import Exception
from System import IAsyncResult
from System import MarshalByRefObject
from System import Object
from System import String
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ADAsyncWorkItem(Object):
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
class AggregateDictionary(Object, ICollection, IDictionary, IEnumerable):
    """"""
    def __init__(self, dictionaries: ICollection) -> None:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AsyncMessageHelper(ABC, Object):
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
class AsyncWorkItem(Object, IMessageSink):
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
    def SyncProcessMessage(self, msg: IMessage) -> IMessage:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BaseChannelObjectWithProperties(ABC, Object, ICollection, IDictionary, IEnumerable):
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
    def Properties(self) -> IDictionary:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BaseChannelSinkWithProperties(
    ABC, BaseChannelObjectWithProperties, ICollection, IDictionary, IEnumerable
):
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
    def Properties(self) -> IDictionary:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BaseChannelWithProperties(
    ABC, BaseChannelObjectWithProperties, ICollection, IDictionary, IEnumerable
):
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
    def Properties(self) -> IDictionary:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ChannelDataStore(Object, IChannelDataStore):
    """"""
    def __init__(self, channelURIs: Array[str]) -> None:
        """"""
    @property
    def ChannelUris(self) -> Array[str]:
        """"""
    @ChannelUris.setter
    def ChannelUris(self, value: Array[str]) -> None: ...
    @property
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __getitem__(self, key: object) -> object:
        """"""
    def __setitem__(self, key: object, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ChannelServices(Object):
    """"""
    @classmethod
    @property
    def RegisteredChannels(cls) -> Array[IChannel]:
        """"""
    @classmethod
    def AsyncDispatchMessage(cls, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl:
        """"""
    @classmethod
    def CreateServerChannelSinkChain(
        cls, provider: IServerChannelSinkProvider, channel: IChannelReceiver
    ) -> IServerChannelSink:
        """"""
    @classmethod
    def DispatchMessage(
        cls, sinkStack: IServerChannelSinkStack, msg: IMessage, replyMsg: IMessage
    ) -> tuple[ServerProcessing, IMessage]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetChannel(cls, name: str) -> IChannel:
        """"""
    @classmethod
    def GetChannelSinkProperties(cls, obj: object) -> IDictionary:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetUrlsForObject(cls, obj: MarshalByRefObject) -> Array[str]:
        """"""
    @classmethod
    @overload
    def RegisterChannel(cls, chnl: IChannel) -> None:
        """"""
    @classmethod
    @overload
    def RegisterChannel(cls, chnl: IChannel, ensureSecurity: bool) -> None:
        """"""
    @classmethod
    def SyncDispatchMessage(cls, msg: IMessage) -> IMessage:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def UnregisterChannel(cls, chnl: IChannel) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ChannelServicesData(Object):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ClientChannelSinkStack(Object, IClientChannelSinkStack, IClientResponseChannelSinkStack):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, replySink: IMessageSink) -> None:
        """"""
    def AsyncProcessResponse(self, headers: ITransportHeaders, stream: Stream) -> None:
        """"""
    def DispatchException(self, e: Exception) -> None:
        """"""
    def DispatchReplyMessage(self, msg: IMessage) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Pop(self, sink: IClientChannelSink) -> object:
        """"""
    def Push(self, sink: IClientChannelSink, state: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CrossAppDomainChannel(Object, IChannel, IChannelReceiver, IChannelSender):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def ChannelData(self) -> object:
        """"""
    @property
    def ChannelName(self) -> str:
        """"""
    @property
    def ChannelPriority(self) -> int:
        """"""
    @property
    def ChannelURI(self) -> str:
        """"""
    def CreateMessageSink(
        self, url: str, data: object, objectURI: String
    ) -> tuple[IMessageSink, String]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUrlsForUri(self, objectURI: str) -> Array[str]:
        """"""
    def Parse(self, url: str, objectURI: String) -> tuple[str, String]:
        """"""
    def StartListening(self, data: object) -> None:
        """"""
    def StopListening(self, data: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CrossAppDomainData(Object):
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
class CrossAppDomainSerializer(ABC, Object):
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
class CrossAppDomainSink(InternalSink, IMessageSink):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CrossContextChannel(InternalSink, IMessageSink):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DictionaryEnumeratorByKeys(Object, IDictionaryEnumerator, IEnumerator):
    """"""
    def __init__(self, properties: IDictionary) -> None:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DispatchChannelSink(Object, IChannelSinkBase, IServerChannelSink):
    """"""
    @property
    def NextChannelSink(self) -> IServerChannelSink:
        """"""
    @property
    def Properties(self) -> IDictionary:
        """"""
    def AsyncProcessResponse(
        self,
        sinkStack: IServerResponseChannelSinkStack,
        state: object,
        msg: IMessage,
        headers: ITransportHeaders,
        stream: Stream,
    ) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetResponseStream(
        self,
        sinkStack: IServerResponseChannelSinkStack,
        state: object,
        msg: IMessage,
        headers: ITransportHeaders,
    ) -> Stream:
        """"""
    def GetType(self) -> Type:
        """"""
    def ProcessMessage(
        self,
        sinkStack: IServerChannelSinkStack,
        requestMsg: IMessage,
        requestHeaders: ITransportHeaders,
        requestStream: Stream,
        responseMsg: IMessage,
        responseHeaders: ITransportHeaders,
        responseStream: Stream,
    ) -> tuple[ServerProcessing, IMessage, ITransportHeaders, Stream]:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DispatchChannelSinkProvider(Object, IServerChannelSinkProvider):
    """"""
    @property
    def Next(self) -> IServerChannelSinkProvider:
        """"""
    @Next.setter
    def Next(self, value: IServerChannelSinkProvider) -> None: ...
    def CreateSink(self, channel: IChannelReceiver) -> IServerChannelSink:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetChannelData(self, channelData: IChannelDataStore) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IChannel(ABC):
    """"""
    @property
    def ChannelName(self) -> str:
        """"""
    @property
    def ChannelPriority(self) -> int:
        """"""
    def Parse(self, url: str, objectURI: String) -> tuple[str, String]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IChannelDataStore(ABC):
    """"""
    @property
    def ChannelUris(self) -> Array[str]:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    def __getitem__(self, key: object) -> object:
        """"""
    def __setitem__(self, key: object, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IChannelReceiver(ABC, IChannel):
    """"""
    @property
    def ChannelData(self) -> object:
        """"""
    @property
    def ChannelName(self) -> str:
        """"""
    @property
    def ChannelPriority(self) -> int:
        """"""
    def GetUrlsForUri(self, objectURI: str) -> Array[str]:
        """"""
    def Parse(self, url: str, objectURI: String) -> tuple[str, String]:
        """"""
    def StartListening(self, data: object) -> None:
        """"""
    def StopListening(self, data: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IChannelReceiverHook(ABC):
    """"""
    @property
    def ChannelScheme(self) -> str:
        """"""
    @property
    def ChannelSinkChain(self) -> IServerChannelSink:
        """"""
    @property
    def WantsToListen(self) -> bool:
        """"""
    def AddHookChannelUri(self, channelUri: str) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IChannelSender(ABC, IChannel):
    """"""
    @property
    def ChannelName(self) -> str:
        """"""
    @property
    def ChannelPriority(self) -> int:
        """"""
    def CreateMessageSink(
        self, url: str, remoteChannelData: object, objectURI: String
    ) -> tuple[IMessageSink, String]:
        """"""
    def Parse(self, url: str, objectURI: String) -> tuple[str, String]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IChannelSinkBase(ABC):
    """"""
    @property
    def Properties(self) -> IDictionary:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IClientChannelSink(ABC, IChannelSinkBase):
    """"""
    @property
    def NextChannelSink(self) -> IClientChannelSink:
        """"""
    @property
    def Properties(self) -> IDictionary:
        """"""
    def AsyncProcessRequest(
        self,
        sinkStack: IClientChannelSinkStack,
        msg: IMessage,
        headers: ITransportHeaders,
        stream: Stream,
    ) -> None:
        """"""
    def AsyncProcessResponse(
        self,
        sinkStack: IClientResponseChannelSinkStack,
        state: object,
        headers: ITransportHeaders,
        stream: Stream,
    ) -> None:
        """"""
    def GetRequestStream(self, msg: IMessage, headers: ITransportHeaders) -> Stream:
        """"""
    def ProcessMessage(
        self,
        msg: IMessage,
        requestHeaders: ITransportHeaders,
        requestStream: Stream,
        responseHeaders: ITransportHeaders,
        responseStream: Stream,
    ) -> tuple[None, ITransportHeaders, Stream]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IClientChannelSinkProvider(ABC):
    """"""
    @property
    def Next(self) -> IClientChannelSinkProvider:
        """"""
    @Next.setter
    def Next(self, value: IClientChannelSinkProvider) -> None: ...
    def CreateSink(
        self, channel: IChannelSender, url: str, remoteChannelData: object
    ) -> IClientChannelSink:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IClientChannelSinkStack(ABC, IClientResponseChannelSinkStack):
    """"""
    def AsyncProcessResponse(self, headers: ITransportHeaders, stream: Stream) -> None:
        """"""
    def DispatchException(self, e: Exception) -> None:
        """"""
    def DispatchReplyMessage(self, msg: IMessage) -> None:
        """"""
    def Pop(self, sink: IClientChannelSink) -> object:
        """"""
    def Push(self, sink: IClientChannelSink, state: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IClientFormatterSink(ABC, IChannelSinkBase, IClientChannelSink, IMessageSink):
    """"""
    @property
    def NextChannelSink(self) -> IClientChannelSink:
        """"""
    @property
    def NextSink(self) -> IMessageSink:
        """"""
    @property
    def Properties(self) -> IDictionary:
        """"""
    def AsyncProcessMessage(self, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl:
        """"""
    def AsyncProcessRequest(
        self,
        sinkStack: IClientChannelSinkStack,
        msg: IMessage,
        headers: ITransportHeaders,
        stream: Stream,
    ) -> None:
        """"""
    def AsyncProcessResponse(
        self,
        sinkStack: IClientResponseChannelSinkStack,
        state: object,
        headers: ITransportHeaders,
        stream: Stream,
    ) -> None:
        """"""
    def GetRequestStream(self, msg: IMessage, headers: ITransportHeaders) -> Stream:
        """"""
    def ProcessMessage(
        self,
        msg: IMessage,
        requestHeaders: ITransportHeaders,
        requestStream: Stream,
        responseHeaders: ITransportHeaders,
        responseStream: Stream,
    ) -> tuple[None, ITransportHeaders, Stream]:
        """"""
    def SyncProcessMessage(self, msg: IMessage) -> IMessage:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IClientFormatterSinkProvider(ABC, IClientChannelSinkProvider):
    """"""
    @property
    def Next(self) -> IClientChannelSinkProvider:
        """"""
    @Next.setter
    def Next(self, value: IClientChannelSinkProvider) -> None: ...
    def CreateSink(
        self, channel: IChannelSender, url: str, remoteChannelData: object
    ) -> IClientChannelSink:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IClientResponseChannelSinkStack(ABC):
    """"""
    def AsyncProcessResponse(self, headers: ITransportHeaders, stream: Stream) -> None:
        """"""
    def DispatchException(self, e: Exception) -> None:
        """"""
    def DispatchReplyMessage(self, msg: IMessage) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ISecurableChannel(ABC):
    """"""
    @property
    def IsSecured(self) -> bool:
        """"""
    @IsSecured.setter
    def IsSecured(self, value: bool) -> None: ...

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IServerChannelSink(ABC, IChannelSinkBase):
    """"""
    @property
    def NextChannelSink(self) -> IServerChannelSink:
        """"""
    @property
    def Properties(self) -> IDictionary:
        """"""
    def AsyncProcessResponse(
        self,
        sinkStack: IServerResponseChannelSinkStack,
        state: object,
        msg: IMessage,
        headers: ITransportHeaders,
        stream: Stream,
    ) -> None:
        """"""
    def GetResponseStream(
        self,
        sinkStack: IServerResponseChannelSinkStack,
        state: object,
        msg: IMessage,
        headers: ITransportHeaders,
    ) -> Stream:
        """"""
    def ProcessMessage(
        self,
        sinkStack: IServerChannelSinkStack,
        requestMsg: IMessage,
        requestHeaders: ITransportHeaders,
        requestStream: Stream,
        responseMsg: IMessage,
        responseHeaders: ITransportHeaders,
        responseStream: Stream,
    ) -> tuple[ServerProcessing, IMessage, ITransportHeaders, Stream]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IServerChannelSinkProvider(ABC):
    """"""
    @property
    def Next(self) -> IServerChannelSinkProvider:
        """"""
    @Next.setter
    def Next(self, value: IServerChannelSinkProvider) -> None: ...
    def CreateSink(self, channel: IChannelReceiver) -> IServerChannelSink:
        """"""
    def GetChannelData(self, channelData: IChannelDataStore) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IServerChannelSinkStack(ABC, IServerResponseChannelSinkStack):
    """"""
    def AsyncProcessResponse(
        self, msg: IMessage, headers: ITransportHeaders, stream: Stream
    ) -> None:
        """"""
    def GetResponseStream(self, msg: IMessage, headers: ITransportHeaders) -> Stream:
        """"""
    def Pop(self, sink: IServerChannelSink) -> object:
        """"""
    def Push(self, sink: IServerChannelSink, state: object) -> None:
        """"""
    def ServerCallback(self, ar: IAsyncResult) -> None:
        """"""
    def Store(self, sink: IServerChannelSink, state: object) -> None:
        """"""
    def StoreAndDispatch(self, sink: IServerChannelSink, state: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IServerFormatterSinkProvider(ABC, IServerChannelSinkProvider):
    """"""
    @property
    def Next(self) -> IServerChannelSinkProvider:
        """"""
    @Next.setter
    def Next(self, value: IServerChannelSinkProvider) -> None: ...
    def CreateSink(self, channel: IChannelReceiver) -> IServerChannelSink:
        """"""
    def GetChannelData(self, channelData: IChannelDataStore) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IServerResponseChannelSinkStack(ABC):
    """"""
    def AsyncProcessResponse(
        self, msg: IMessage, headers: ITransportHeaders, stream: Stream
    ) -> None:
        """"""
    def GetResponseStream(self, msg: IMessage, headers: ITransportHeaders) -> Stream:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ITransportHeaders(ABC):
    """"""
    @property
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __getitem__(self, key: object) -> object:
        """"""
    def __setitem__(self, key: object, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Perf_Contexts(ValueType):
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
class RegisteredChannel(Object):
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
class RegisteredChannelList(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class RemotingProfilerEvent(Enum):
    """"""

    ClientSend: RemotingProfilerEvent = ...
    """"""
    ClientReceive: RemotingProfilerEvent = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ServerAsyncReplyTerminatorSink(Object, IMessageSink):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ServerChannelSinkStack(Object, IServerChannelSinkStack, IServerResponseChannelSinkStack):
    """"""
    def __init__(self) -> None:
        """"""
    def AsyncProcessResponse(
        self, msg: IMessage, headers: ITransportHeaders, stream: Stream
    ) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetResponseStream(self, msg: IMessage, headers: ITransportHeaders) -> Stream:
        """"""
    def GetType(self) -> Type:
        """"""
    def Pop(self, sink: IServerChannelSink) -> object:
        """"""
    def Push(self, sink: IServerChannelSink, state: object) -> None:
        """"""
    def ServerCallback(self, ar: IAsyncResult) -> None:
        """"""
    def Store(self, sink: IServerChannelSink, state: object) -> None:
        """"""
    def StoreAndDispatch(self, sink: IServerChannelSink, state: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class ServerProcessing(Enum):
    """"""

    Complete: ServerProcessing = ...
    """"""
    OneWay: ServerProcessing = ...
    """"""
    Async: ServerProcessing = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SinkProviderData(Object):
    """"""
    def __init__(self, name: str) -> None:
        """"""
    @property
    def Children(self) -> IList:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Properties(self) -> IDictionary:
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
class TransportHeaders(Object, ITransportHeaders):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __getitem__(self, key: object) -> object:
        """"""
    def __setitem__(self, key: object, value: object) -> None:
        """"""
