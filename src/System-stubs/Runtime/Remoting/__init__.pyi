"""Automatically generated stubs for C# namespace: System.Runtime.Remoting."""

from abc import ABC
from typing import ClassVar
from typing import overload

from System import Array
from System import Enum
from System import Exception
from System import MarshalByRefObject
from System import Object
from System import String
from System import SystemException
from System import Type
from System import ValueType
from System.Collections import IDictionary
from System.Reflection import Assembly
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import IObjectReference
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext

from .Contexts import IContextAttribute
from .Messaging import IMessage
from .Messaging import IMessageCtrl
from .Messaging import IMessageSink
from .Messaging import IMethodCallMessage
from .Messaging import IMethodMessage
from .Messaging import IMethodReturnMessage
from .Messaging import MethodCall
from .Metadata import SoapAttribute
from .Proxies import RealProxy

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ActivatedClientTypeEntry(TypeEntry):
    """"""
    @overload
    def __init__(self, typeName: str, assemblyName: str, appUrl: str) -> None:
        """"""
    @overload
    def __init__(self, type: Type, appUrl: str) -> None:
        """"""
    @property
    def ApplicationUrl(self) -> str:
        """"""
    @property
    def AssemblyName(self) -> str:
        """"""
    @AssemblyName.setter
    def AssemblyName(self, value: str) -> None: ...
    @property
    def ContextAttributes(self) -> Array[IContextAttribute]:
        """"""
    @ContextAttributes.setter
    def ContextAttributes(self, value: Array[IContextAttribute]) -> None: ...
    @property
    def ObjectType(self) -> Type:
        """"""
    @property
    def TypeName(self) -> str:
        """"""
    @TypeName.setter
    def TypeName(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ActivatedServiceTypeEntry(TypeEntry):
    """"""
    @overload
    def __init__(self, typeName: str, assemblyName: str) -> None:
        """"""
    @overload
    def __init__(self, type: Type) -> None:
        """"""
    @property
    def AssemblyName(self) -> str:
        """"""
    @AssemblyName.setter
    def AssemblyName(self, value: str) -> None: ...
    @property
    def ContextAttributes(self) -> Array[IContextAttribute]:
        """"""
    @ContextAttributes.setter
    def ContextAttributes(self, value: Array[IContextAttribute]) -> None: ...
    @property
    def ObjectType(self) -> Type:
        """"""
    @property
    def TypeName(self) -> str:
        """"""
    @TypeName.setter
    def TypeName(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ChannelInfo(Object, IChannelInfo):
    """"""
    @property
    def ChannelData(self) -> Array[object]:
        """"""
    @ChannelData.setter
    def ChannelData(self, value: Array[object]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ComRedirectionProxy(MarshalByRefObject, IMessageSink):
    """"""
    @property
    def NextSink(self) -> IMessageSink:
        """"""
    def AsyncProcessMessage(self, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def SyncProcessMessage(self, msg: IMessage) -> IMessage:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CustomErrorsModes(Enum):
    """"""

    On: CustomErrorsModes = ...
    """"""
    Off: CustomErrorsModes = ...
    """"""
    RemoteOnly: CustomErrorsModes = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DelayLoadClientChannelEntry(Object):
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
class DomainSpecificRemotingData(Object):
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
class DuplicateIdentityOption(Enum):
    """"""

    Unique: DuplicateIdentityOption = ...
    """"""
    UseExisting: DuplicateIdentityOption = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DynamicTypeInfo(TypeInfo, IRemotingTypeInfo):
    """"""
    @property
    def TypeName(self) -> str:
        """"""
    @TypeName.setter
    def TypeName(self, value: str) -> None: ...
    def CanCastTo(self, castType: Type, o: object) -> bool:
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
class EnvoyInfo(Object, IEnvoyInfo):
    """"""
    @property
    def EnvoySinks(self) -> IMessageSink:
        """"""
    @EnvoySinks.setter
    def EnvoySinks(self, value: IMessageSink) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IChannelInfo(ABC):
    """"""
    @property
    def ChannelData(self) -> Array[object]:
        """"""
    @ChannelData.setter
    def ChannelData(self, value: Array[object]) -> None: ...

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IEnvoyInfo(ABC):
    """"""
    @property
    def EnvoySinks(self) -> IMessageSink:
        """"""
    @EnvoySinks.setter
    def EnvoySinks(self, value: IMessageSink) -> None: ...

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IObjectHandle(ABC):
    """"""
    def Unwrap(self) -> object:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IRemotingTypeInfo(ABC):
    """"""
    @property
    def TypeName(self) -> str:
        """"""
    @TypeName.setter
    def TypeName(self, value: str) -> None: ...
    def CanCastTo(self, fromType: Type, o: object) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IdOps(ValueType):
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
class Identity(Object):
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
class IdentityHolder(Object):
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
class InternalRemotingServices(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @classmethod
    def DebugOutChnl(cls, s: str) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetCachedSoapAttribute(cls, reflectionObject: object) -> SoapAttribute:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def RemotingAssert(cls, condition: bool, message: str) -> None:
        """"""
    @classmethod
    def RemotingTrace(cls, messages: Array[object]) -> None:
        """"""
    @classmethod
    def SetServerIdentity(cls, m: MethodCall, srvID: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ObjRef(Object, IObjectReference, ISerializable):
    """"""
    @overload
    def __init__(self, o: MarshalByRefObject, requestedType: Type) -> None:
        """"""
    @overload
    def __init__(self) -> None:
        """"""
    @property
    def ChannelInfo(self) -> IChannelInfo:
        """"""
    @ChannelInfo.setter
    def ChannelInfo(self, value: IChannelInfo) -> None: ...
    @property
    def EnvoyInfo(self) -> IEnvoyInfo:
        """"""
    @EnvoyInfo.setter
    def EnvoyInfo(self, value: IEnvoyInfo) -> None: ...
    @property
    def TypeInfo(self) -> IRemotingTypeInfo:
        """"""
    @TypeInfo.setter
    def TypeInfo(self, value: IRemotingTypeInfo) -> None: ...
    @property
    def URI(self) -> str:
        """"""
    @URI.setter
    def URI(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetRealObject(self, context: StreamingContext) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsFromThisAppDomain(self) -> bool:
        """"""
    def IsFromThisProcess(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ObjectHandle(MarshalByRefObject, IObjectHandle):
    """"""
    def __init__(self, o: object) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def ToString(self) -> str:
        """"""
    def Unwrap(self) -> object:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RedirectionProxy(MarshalByRefObject, IMessageSink):
    """"""
    @property
    def NextSink(self) -> IMessageSink:
        """"""
    @property
    def ObjectMode(self) -> WellKnownObjectMode:
        """"""
    @ObjectMode.setter
    def ObjectMode(self, value: WellKnownObjectMode) -> None: ...
    def AsyncProcessMessage(self, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def SyncProcessMessage(self, msg: IMessage) -> IMessage:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RemoteAppEntry(Object):
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
class RemotingConfigHandler(ABC, Object):
    """"""

    Info: ClassVar[RemotingConfigHandler.RemotingConfigInfo]
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
class RemotingConfiguration(ABC, Object):
    """"""
    @classmethod
    @property
    def ApplicationId(cls) -> str:
        """"""
    @classmethod
    @property
    def ApplicationName(cls) -> str:
        """"""
    @classmethod
    @ApplicationName.setter
    def ApplicationName(cls, value: str) -> None: ...
    @classmethod
    @property
    def CustomErrorsMode(cls) -> CustomErrorsModes:
        """"""
    @classmethod
    @CustomErrorsMode.setter
    def CustomErrorsMode(cls, value: CustomErrorsModes) -> None: ...
    @classmethod
    @property
    def ProcessId(cls) -> str:
        """"""
    @classmethod
    @overload
    def Configure(cls, filename: str) -> None:
        """"""
    @classmethod
    @overload
    def Configure(cls, filename: str, ensureSecurity: bool) -> None:
        """"""
    @classmethod
    def CustomErrorsEnabled(cls, isLocalRequest: bool) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetRegisteredActivatedClientTypes(cls) -> Array[ActivatedClientTypeEntry]:
        """"""
    @classmethod
    def GetRegisteredActivatedServiceTypes(cls) -> Array[ActivatedServiceTypeEntry]:
        """"""
    @classmethod
    def GetRegisteredWellKnownClientTypes(cls) -> Array[WellKnownClientTypeEntry]:
        """"""
    @classmethod
    def GetRegisteredWellKnownServiceTypes(cls) -> Array[WellKnownServiceTypeEntry]:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsActivationAllowed(cls, svrType: Type) -> bool:
        """"""
    @classmethod
    @overload
    def IsRemotelyActivatedClientType(
        cls, typeName: str, assemblyName: str
    ) -> ActivatedClientTypeEntry:
        """"""
    @classmethod
    @overload
    def IsRemotelyActivatedClientType(cls, svrType: Type) -> ActivatedClientTypeEntry:
        """"""
    @classmethod
    @overload
    def IsWellKnownClientType(cls, typeName: str, assemblyName: str) -> WellKnownClientTypeEntry:
        """"""
    @classmethod
    @overload
    def IsWellKnownClientType(cls, svrType: Type) -> WellKnownClientTypeEntry:
        """"""
    @classmethod
    @overload
    def RegisterActivatedClientType(cls, entry: ActivatedClientTypeEntry) -> None:
        """"""
    @classmethod
    @overload
    def RegisterActivatedClientType(cls, type: Type, appUrl: str) -> None:
        """"""
    @classmethod
    @overload
    def RegisterActivatedServiceType(cls, entry: ActivatedServiceTypeEntry) -> None:
        """"""
    @classmethod
    @overload
    def RegisterActivatedServiceType(cls, type: Type) -> None:
        """"""
    @classmethod
    @overload
    def RegisterWellKnownClientType(cls, entry: WellKnownClientTypeEntry) -> None:
        """"""
    @classmethod
    @overload
    def RegisterWellKnownClientType(cls, type: Type, objectUrl: str) -> None:
        """"""
    @classmethod
    @overload
    def RegisterWellKnownServiceType(cls, entry: WellKnownServiceTypeEntry) -> None:
        """"""
    @classmethod
    @overload
    def RegisterWellKnownServiceType(
        cls, type: Type, objectUri: str, mode: WellKnownObjectMode
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RemotingException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, InnerException: Exception) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def HResult(self) -> int:
        """"""
    @property
    def HelpLink(self) -> str:
        """"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """"""
    @property
    def TargetSite(self) -> MethodBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RemotingServices(ABC, Object):
    """"""
    @classmethod
    @overload
    def Connect(cls, classToProxy: Type, url: str) -> object:
        """"""
    @classmethod
    @overload
    def Connect(cls, classToProxy: Type, url: str, data: object) -> object:
        """"""
    @classmethod
    def Disconnect(cls, obj: MarshalByRefObject) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def ExecuteMessage(
        cls, target: MarshalByRefObject, reqMsg: IMethodCallMessage
    ) -> IMethodReturnMessage:
        """"""
    @classmethod
    def GetEnvoyChainForProxy(cls, obj: MarshalByRefObject) -> IMessageSink:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetLifetimeService(cls, obj: MarshalByRefObject) -> object:
        """"""
    @classmethod
    def GetMethodBaseFromMethodMessage(cls, msg: IMethodMessage) -> MethodBase:
        """"""
    @classmethod
    def GetObjRefForProxy(cls, obj: MarshalByRefObject) -> ObjRef:
        """"""
    @classmethod
    def GetObjectData(cls, obj: object, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    @classmethod
    def GetObjectUri(cls, obj: MarshalByRefObject) -> str:
        """"""
    @classmethod
    def GetRealProxy(cls, proxy: object) -> RealProxy:
        """"""
    @classmethod
    def GetServerTypeForUri(cls, URI: str) -> Type:
        """"""
    @classmethod
    def GetSessionIdForMethodMessage(cls, msg: IMethodMessage) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsMethodOverloaded(cls, msg: IMethodMessage) -> bool:
        """"""
    @classmethod
    def IsObjectOutOfAppDomain(cls, tp: object) -> bool:
        """"""
    @classmethod
    def IsObjectOutOfContext(cls, tp: object) -> bool:
        """"""
    @classmethod
    def IsOneWay(cls, method: MethodBase) -> bool:
        """"""
    @classmethod
    def IsTransparentProxy(cls, proxy: object) -> bool:
        """"""
    @classmethod
    def LogRemotingStage(cls, stage: int) -> None:
        """"""
    @classmethod
    @overload
    def Marshal(cls, Obj: MarshalByRefObject) -> ObjRef:
        """"""
    @classmethod
    @overload
    def Marshal(cls, Obj: MarshalByRefObject, URI: str) -> ObjRef:
        """"""
    @classmethod
    @overload
    def Marshal(cls, Obj: MarshalByRefObject, ObjURI: str, RequestedType: Type) -> ObjRef:
        """"""
    @classmethod
    def SetObjectUriForMarshal(cls, obj: MarshalByRefObject, uri: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def Unmarshal(cls, objectRef: ObjRef) -> object:
        """"""
    @classmethod
    @overload
    def Unmarshal(cls, objectRef: ObjRef, fRefine: bool) -> object:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RemotingTimeoutException(RemotingException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, InnerException: Exception) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def HResult(self) -> int:
        """"""
    @property
    def HelpLink(self) -> str:
        """"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """"""
    @property
    def TargetSite(self) -> MethodBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ServerException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, InnerException: Exception) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def HResult(self) -> int:
        """"""
    @property
    def HelpLink(self) -> str:
        """"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """"""
    @property
    def TargetSite(self) -> MethodBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ServerIdentity(Identity):
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
class SoapServices(Object):
    """"""
    @classmethod
    @property
    def XmlNsForClrType(cls) -> str:
        """"""
    @classmethod
    @property
    def XmlNsForClrTypeWithAssembly(cls) -> str:
        """"""
    @classmethod
    @property
    def XmlNsForClrTypeWithNs(cls) -> str:
        """"""
    @classmethod
    @property
    def XmlNsForClrTypeWithNsAndAssembly(cls) -> str:
        """"""
    @classmethod
    def CodeXmlNamespaceForClrTypeNamespace(cls, typeNamespace: str, assemblyName: str) -> str:
        """"""
    @classmethod
    def DecodeXmlNamespaceForClrTypeNamespace(
        cls, inNamespace: str, typeNamespace: String, assemblyName: String
    ) -> tuple[bool, String, String]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetInteropFieldTypeAndNameFromXmlAttribute(
        cls, containingType: Type, xmlAttribute: str, xmlNamespace: str, type: Type, name: String
    ) -> tuple[None, Type, String]:
        """"""
    @classmethod
    def GetInteropFieldTypeAndNameFromXmlElement(
        cls, containingType: Type, xmlElement: str, xmlNamespace: str, type: Type, name: String
    ) -> tuple[None, Type, String]:
        """"""
    @classmethod
    def GetInteropTypeFromXmlElement(cls, xmlElement: str, xmlNamespace: str) -> Type:
        """"""
    @classmethod
    def GetInteropTypeFromXmlType(cls, xmlType: str, xmlTypeNamespace: str) -> Type:
        """"""
    @classmethod
    def GetSoapActionFromMethodBase(cls, mb: MethodBase) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetTypeAndMethodNameFromSoapAction(
        cls, soapAction: str, typeName: String, methodName: String
    ) -> tuple[bool, String, String]:
        """"""
    @classmethod
    def GetXmlElementForInteropType(
        cls, type: Type, xmlElement: String, xmlNamespace: String
    ) -> tuple[bool, String, String]:
        """"""
    @classmethod
    def GetXmlNamespaceForMethodCall(cls, mb: MethodBase) -> str:
        """"""
    @classmethod
    def GetXmlNamespaceForMethodResponse(cls, mb: MethodBase) -> str:
        """"""
    @classmethod
    def GetXmlTypeForInteropType(
        cls, type: Type, xmlType: String, xmlTypeNamespace: String
    ) -> tuple[bool, String, String]:
        """"""
    @classmethod
    def IsClrTypeNamespace(cls, namespaceString: str) -> bool:
        """"""
    @classmethod
    def IsSoapActionValidForMethodBase(cls, soapAction: str, mb: MethodBase) -> bool:
        """"""
    @classmethod
    @overload
    def PreLoad(cls, assembly: Assembly) -> None:
        """"""
    @classmethod
    @overload
    def PreLoad(cls, type: Type) -> None:
        """"""
    @classmethod
    def RegisterInteropXmlElement(cls, xmlElement: str, xmlNamespace: str, type: Type) -> None:
        """"""
    @classmethod
    def RegisterInteropXmlType(cls, xmlType: str, xmlTypeNamespace: str, type: Type) -> None:
        """"""
    @classmethod
    @overload
    def RegisterSoapActionForMethodBase(cls, mb: MethodBase) -> None:
        """"""
    @classmethod
    @overload
    def RegisterSoapActionForMethodBase(cls, mb: MethodBase, soapAction: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TypeEntry(Object):
    """"""
    @property
    def AssemblyName(self) -> str:
        """"""
    @AssemblyName.setter
    def AssemblyName(self, value: str) -> None: ...
    @property
    def TypeName(self) -> str:
        """"""
    @TypeName.setter
    def TypeName(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TypeInfo(Object, IRemotingTypeInfo):
    """"""
    @property
    def TypeName(self) -> str:
        """"""
    @TypeName.setter
    def TypeName(self, value: str) -> None: ...
    def CanCastTo(self, castType: Type, o: object) -> bool:
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
class WellKnownClientTypeEntry(TypeEntry):
    """"""
    @overload
    def __init__(self, typeName: str, assemblyName: str, objectUrl: str) -> None:
        """"""
    @overload
    def __init__(self, type: Type, objectUrl: str) -> None:
        """"""
    @property
    def ApplicationUrl(self) -> str:
        """"""
    @ApplicationUrl.setter
    def ApplicationUrl(self, value: str) -> None: ...
    @property
    def AssemblyName(self) -> str:
        """"""
    @AssemblyName.setter
    def AssemblyName(self, value: str) -> None: ...
    @property
    def ObjectType(self) -> Type:
        """"""
    @property
    def ObjectUrl(self) -> str:
        """"""
    @property
    def TypeName(self) -> str:
        """"""
    @TypeName.setter
    def TypeName(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class WellKnownObjectMode(Enum):
    """"""

    Singleton: WellKnownObjectMode = ...
    """"""
    SingleCall: WellKnownObjectMode = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class WellKnownServiceTypeEntry(TypeEntry):
    """"""
    @overload
    def __init__(
        self, typeName: str, assemblyName: str, objectUri: str, mode: WellKnownObjectMode
    ) -> None:
        """"""
    @overload
    def __init__(self, type: Type, objectUri: str, mode: WellKnownObjectMode) -> None:
        """"""
    @property
    def AssemblyName(self) -> str:
        """"""
    @AssemblyName.setter
    def AssemblyName(self, value: str) -> None: ...
    @property
    def ContextAttributes(self) -> Array[IContextAttribute]:
        """"""
    @ContextAttributes.setter
    def ContextAttributes(self, value: Array[IContextAttribute]) -> None: ...
    @property
    def Mode(self) -> WellKnownObjectMode:
        """"""
    @property
    def ObjectType(self) -> Type:
        """"""
    @property
    def ObjectUri(self) -> str:
        """"""
    @property
    def TypeName(self) -> str:
        """"""
    @TypeName.setter
    def TypeName(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class XmlNamespaceEncoder(ABC, Object):
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
class __HResults(Object):
    """"""

    COR_E_REMOTING: ClassVar[int]
    """"""
    COR_E_SERVER: ClassVar[int]
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
