from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final
from typing import Tuple
from typing import overload

from System import Array
from System import Enum
from System import Exception
from System import MarshalByRefObject
from System import Object
from System import SystemException
from System import Type
from System import ValueType
from System.Collections import IDictionary
from System.Reflection import Assembly
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Exception
from System.Runtime.Remoting.Contexts import IContextAttribute
from System.Runtime.Remoting.Messaging import IMessage
from System.Runtime.Remoting.Messaging import IMessageCtrl
from System.Runtime.Remoting.Messaging import IMessageSink
from System.Runtime.Remoting.Messaging import IMethodCallMessage
from System.Runtime.Remoting.Messaging import IMethodMessage
from System.Runtime.Remoting.Messaging import IMethodReturnMessage
from System.Runtime.Remoting.Messaging import MethodCall
from System.Runtime.Remoting.Metadata import SoapAttribute
from System.Runtime.Remoting.Proxies import RealProxy
from System.Runtime.Remoting.RemotingConfigHandler import RemotingConfigInfo
from System.Runtime.Serialization import IObjectReference
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext

class ActivatedClientTypeEntry(TypeEntry):
    """"""

    @overload
    def __init__(self, type: Type, appUrl: str):
        """

        :param type:
        :param appUrl:
        """
    @overload
    def __init__(self, typeName: str, assemblyName: str, appUrl: str):
        """

        :param typeName:
        :param assemblyName:
        :param appUrl:
        """
    @property
    def ApplicationUrl(self) -> str:
        """

        :return:
        """
    @property
    def AssemblyName(self) -> str:
        """

        :return:
        """
    @AssemblyName.setter
    def AssemblyName(self, value: str) -> None: ...
    @property
    def ContextAttributes(self) -> Array[IContextAttribute]:
        """

        :return:
        """
    @ContextAttributes.setter
    def ContextAttributes(self, value: Array[IContextAttribute]) -> None: ...
    @property
    def ObjectType(self) -> Type:
        """

        :return:
        """
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    @TypeName.setter
    def TypeName(self, value: str) -> None: ...
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

class ActivatedServiceTypeEntry(TypeEntry):
    """"""

    @overload
    def __init__(self, type: Type):
        """

        :param type:
        """
    @overload
    def __init__(self, typeName: str, assemblyName: str):
        """

        :param typeName:
        :param assemblyName:
        """
    @property
    def AssemblyName(self) -> str:
        """

        :return:
        """
    @AssemblyName.setter
    def AssemblyName(self, value: str) -> None: ...
    @property
    def ContextAttributes(self) -> Array[IContextAttribute]:
        """

        :return:
        """
    @ContextAttributes.setter
    def ContextAttributes(self, value: Array[IContextAttribute]) -> None: ...
    @property
    def ObjectType(self) -> Type:
        """

        :return:
        """
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    @TypeName.setter
    def TypeName(self, value: str) -> None: ...
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

class ChannelInfo(Object, IChannelInfo):
    """"""

    @property
    def ChannelData(self) -> Array[object]:
        """

        :return:
        """
    @ChannelData.setter
    def ChannelData(self, value: Array[object]) -> None: ...
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

class ComRedirectionProxy(MarshalByRefObject, IMessageSink):
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
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
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

class CustomErrorsModes(Enum):
    """"""

    On: CustomErrorsModes = ...
    """"""
    Off: CustomErrorsModes = ...
    """"""
    RemoteOnly: CustomErrorsModes = ...
    """"""

class DelayLoadClientChannelEntry(Object):
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

class DomainSpecificRemotingData(Object):
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

class DuplicateIdentityOption(Enum):
    """"""

    Unique: DuplicateIdentityOption = ...
    """"""
    UseExisting: DuplicateIdentityOption = ...
    """"""

class DynamicTypeInfo(TypeInfo, IRemotingTypeInfo):
    """"""

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

class EnvoyInfo(Object, IEnvoyInfo):
    """"""

    @property
    def EnvoySinks(self) -> IMessageSink:
        """

        :return:
        """
    @EnvoySinks.setter
    def EnvoySinks(self, value: IMessageSink) -> None: ...
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

class IChannelInfo:
    """"""

    @property
    def ChannelData(self) -> Array[object]:
        """

        :return:
        """
    @ChannelData.setter
    def ChannelData(self, value: Array[object]) -> None: ...

class IEnvoyInfo:
    """"""

    @property
    def EnvoySinks(self) -> IMessageSink:
        """

        :return:
        """
    @EnvoySinks.setter
    def EnvoySinks(self, value: IMessageSink) -> None: ...

class IObjectHandle:
    """"""

    def Unwrap(self) -> object:
        """

        :return:
        """

class IRemotingTypeInfo:
    """"""

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

class IdOps(ValueType):
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

class Identity(Object):
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

class IdentityHolder(Object):
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

class InternalRemotingServices(Object):
    """"""

    def __init__(self):
        """"""
    @classmethod
    def DebugOutChnl(cls, s: str) -> None:
        """

        :param s:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetCachedSoapAttribute(cls, reflectionObject: object) -> SoapAttribute:
        """

        :param reflectionObject:
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
    def RemotingAssert(cls, condition: bool, message: str) -> None:
        """

        :param condition:
        :param message:
        """
    @classmethod
    def RemotingTrace(cls, messages: Array[object]) -> None:
        """

        :param messages:
        """
    @classmethod
    def SetServerIdentity(cls, m: MethodCall, srvID: object) -> None:
        """

        :param m:
        :param srvID:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ObjRef(Object, IObjectReference, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, o: MarshalByRefObject, requestedType: Type):
        """

        :param o:
        :param requestedType:
        """
    @property
    def ChannelInfo(self) -> IChannelInfo:
        """

        :return:
        """
    @ChannelInfo.setter
    def ChannelInfo(self, value: IChannelInfo) -> None: ...
    @property
    def EnvoyInfo(self) -> IEnvoyInfo:
        """

        :return:
        """
    @EnvoyInfo.setter
    def EnvoyInfo(self, value: IEnvoyInfo) -> None: ...
    @property
    def TypeInfo(self) -> IRemotingTypeInfo:
        """

        :return:
        """
    @TypeInfo.setter
    def TypeInfo(self, value: IRemotingTypeInfo) -> None: ...
    @property
    def URI(self) -> str:
        """

        :return:
        """
    @URI.setter
    def URI(self, value: str) -> None: ...
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
    def GetRealObject(self, context: StreamingContext) -> object:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def IsFromThisAppDomain(self) -> bool:
        """

        :return:
        """
    def IsFromThisProcess(self) -> bool:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ObjectHandle(MarshalByRefObject, IObjectHandle):
    """"""

    def __init__(self, o: object):
        """

        :param o:
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
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Unwrap(self) -> object:
        """

        :return:
        """

class RedirectionProxy(MarshalByRefObject, IMessageSink):
    """"""

    @property
    def NextSink(self) -> IMessageSink:
        """

        :return:
        """
    @property
    def ObjectMode(self) -> WellKnownObjectMode:
        """

        :return:
        """
    @ObjectMode.setter
    def ObjectMode(self, value: WellKnownObjectMode) -> None: ...
    def AsyncProcessMessage(self, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl:
        """

        :param msg:
        :param replySink:
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
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
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

class RemoteAppEntry(Object):
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

class RemotingConfigHandler(ABC, Object):
    """"""

    Info: Final[ClassVar[RemotingConfigHandler.RemotingConfigInfo]] = ...
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

class RemotingConfiguration(ABC, Object):
    """"""

    @classmethod
    @property
    def ApplicationId(cls) -> str:
        """

        :return:
        """
    @classmethod
    @property
    def ApplicationName(cls) -> str:
        """

        :return:
        """
    @classmethod
    @ApplicationName.setter
    def ApplicationName(cls, value: str) -> None: ...
    @classmethod
    @property
    def CustomErrorsMode(cls) -> CustomErrorsModes:
        """

        :return:
        """
    @classmethod
    @CustomErrorsMode.setter
    def CustomErrorsMode(cls, value: CustomErrorsModes) -> None: ...
    @classmethod
    @property
    def ProcessId(cls) -> str:
        """

        :return:
        """
    @classmethod
    @overload
    def Configure(cls, filename: str) -> None:
        """

        :param filename:
        """
    @classmethod
    @overload
    def Configure(cls, filename: str, ensureSecurity: bool) -> None:
        """

        :param filename:
        :param ensureSecurity:
        """
    @classmethod
    def CustomErrorsEnabled(cls, isLocalRequest: bool) -> bool:
        """

        :param isLocalRequest:
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
    @classmethod
    def GetRegisteredActivatedClientTypes(cls) -> Array[ActivatedClientTypeEntry]:
        """

        :return:
        """
    @classmethod
    def GetRegisteredActivatedServiceTypes(cls) -> Array[ActivatedServiceTypeEntry]:
        """

        :return:
        """
    @classmethod
    def GetRegisteredWellKnownClientTypes(cls) -> Array[WellKnownClientTypeEntry]:
        """

        :return:
        """
    @classmethod
    def GetRegisteredWellKnownServiceTypes(cls) -> Array[WellKnownServiceTypeEntry]:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def IsActivationAllowed(cls, svrType: Type) -> bool:
        """

        :param svrType:
        :return:
        """
    @classmethod
    @overload
    def IsRemotelyActivatedClientType(cls, svrType: Type) -> ActivatedClientTypeEntry:
        """

        :param svrType:
        :return:
        """
    @classmethod
    @overload
    def IsRemotelyActivatedClientType(
        cls, typeName: str, assemblyName: str
    ) -> ActivatedClientTypeEntry:
        """

        :param typeName:
        :param assemblyName:
        :return:
        """
    @classmethod
    @overload
    def IsWellKnownClientType(cls, svrType: Type) -> WellKnownClientTypeEntry:
        """

        :param svrType:
        :return:
        """
    @classmethod
    @overload
    def IsWellKnownClientType(cls, typeName: str, assemblyName: str) -> WellKnownClientTypeEntry:
        """

        :param typeName:
        :param assemblyName:
        :return:
        """
    @classmethod
    @overload
    def RegisterActivatedClientType(cls, entry: ActivatedClientTypeEntry) -> None:
        """

        :param entry:
        """
    @classmethod
    @overload
    def RegisterActivatedClientType(cls, type: Type, appUrl: str) -> None:
        """

        :param type:
        :param appUrl:
        """
    @classmethod
    @overload
    def RegisterActivatedServiceType(cls, entry: ActivatedServiceTypeEntry) -> None:
        """

        :param entry:
        """
    @classmethod
    @overload
    def RegisterActivatedServiceType(cls, type: Type) -> None:
        """

        :param type:
        """
    @classmethod
    @overload
    def RegisterWellKnownClientType(cls, entry: WellKnownClientTypeEntry) -> None:
        """

        :param entry:
        """
    @classmethod
    @overload
    def RegisterWellKnownClientType(cls, type: Type, objectUrl: str) -> None:
        """

        :param type:
        :param objectUrl:
        """
    @classmethod
    @overload
    def RegisterWellKnownServiceType(cls, entry: WellKnownServiceTypeEntry) -> None:
        """

        :param entry:
        """
    @classmethod
    @overload
    def RegisterWellKnownServiceType(
        cls, type: Type, objectUri: str, mode: WellKnownObjectMode
    ) -> None:
        """

        :param type:
        :param objectUri:
        :param mode:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class RemotingException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, message: str, InnerException: Exception):
        """

        :param message:
        :param InnerException:
        """
    @property
    def Data(self) -> IDictionary:
        """

        :return:
        """
    @property
    def HResult(self) -> int:
        """

        :return:
        """
    @property
    def HelpLink(self) -> str:
        """

        :return:
        """
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """

        :return:
        """
    @property
    def Message(self) -> str:
        """

        :return:
        """
    @property
    def Source(self) -> str:
        """

        :return:
        """
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """

        :return:
        """
    @property
    def TargetSite(self) -> MethodBase:
        """

        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class RemotingServices(ABC, Object):
    """"""

    @classmethod
    @overload
    def Connect(cls, classToProxy: Type, url: str) -> object:
        """

        :param classToProxy:
        :param url:
        :return:
        """
    @classmethod
    @overload
    def Connect(cls, classToProxy: Type, url: str, data: object) -> object:
        """

        :param classToProxy:
        :param url:
        :param data:
        :return:
        """
    @classmethod
    def Disconnect(cls, obj: MarshalByRefObject) -> bool:
        """

        :param obj:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def ExecuteMessage(
        cls, target: MarshalByRefObject, reqMsg: IMethodCallMessage
    ) -> IMethodReturnMessage:
        """

        :param target:
        :param reqMsg:
        :return:
        """
    @classmethod
    def GetEnvoyChainForProxy(cls, obj: MarshalByRefObject) -> IMessageSink:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    def GetLifetimeService(cls, obj: MarshalByRefObject) -> object:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetMethodBaseFromMethodMessage(cls, msg: IMethodMessage) -> MethodBase:
        """

        :param msg:
        :return:
        """
    @classmethod
    def GetObjRefForProxy(cls, obj: MarshalByRefObject) -> ObjRef:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetObjectData(cls, obj: object, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param obj:
        :param info:
        :param context:
        """
    @classmethod
    def GetObjectUri(cls, obj: MarshalByRefObject) -> str:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetRealProxy(cls, proxy: object) -> RealProxy:
        """

        :param proxy:
        :return:
        """
    @classmethod
    def GetServerTypeForUri(cls, URI: str) -> Type:
        """

        :param URI:
        :return:
        """
    @classmethod
    def GetSessionIdForMethodMessage(cls, msg: IMethodMessage) -> str:
        """

        :param msg:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def IsMethodOverloaded(cls, msg: IMethodMessage) -> bool:
        """

        :param msg:
        :return:
        """
    @classmethod
    def IsObjectOutOfAppDomain(cls, tp: object) -> bool:
        """

        :param tp:
        :return:
        """
    @classmethod
    def IsObjectOutOfContext(cls, tp: object) -> bool:
        """

        :param tp:
        :return:
        """
    @classmethod
    def IsOneWay(cls, method: MethodBase) -> bool:
        """

        :param method:
        :return:
        """
    @classmethod
    def IsTransparentProxy(cls, proxy: object) -> bool:
        """

        :param proxy:
        :return:
        """
    @classmethod
    def LogRemotingStage(cls, stage: int) -> None:
        """

        :param stage:
        """
    @classmethod
    @overload
    def Marshal(cls, Obj: MarshalByRefObject) -> ObjRef:
        """

        :param Obj:
        :return:
        """
    @classmethod
    @overload
    def Marshal(cls, Obj: MarshalByRefObject, URI: str) -> ObjRef:
        """

        :param Obj:
        :param URI:
        :return:
        """
    @classmethod
    @overload
    def Marshal(cls, Obj: MarshalByRefObject, ObjURI: str, RequestedType: Type) -> ObjRef:
        """

        :param Obj:
        :param ObjURI:
        :param RequestedType:
        :return:
        """
    @classmethod
    def SetObjectUriForMarshal(cls, obj: MarshalByRefObject, uri: str) -> None:
        """

        :param obj:
        :param uri:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    @overload
    def Unmarshal(cls, objectRef: ObjRef) -> object:
        """

        :param objectRef:
        :return:
        """
    @classmethod
    @overload
    def Unmarshal(cls, objectRef: ObjRef, fRefine: bool) -> object:
        """

        :param objectRef:
        :param fRefine:
        :return:
        """

class RemotingTimeoutException(RemotingException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, message: str, InnerException: Exception):
        """

        :param message:
        :param InnerException:
        """
    @property
    def Data(self) -> IDictionary:
        """

        :return:
        """
    @property
    def HResult(self) -> int:
        """

        :return:
        """
    @property
    def HelpLink(self) -> str:
        """

        :return:
        """
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """

        :return:
        """
    @property
    def Message(self) -> str:
        """

        :return:
        """
    @property
    def Source(self) -> str:
        """

        :return:
        """
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """

        :return:
        """
    @property
    def TargetSite(self) -> MethodBase:
        """

        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class ServerException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, message: str, InnerException: Exception):
        """

        :param message:
        :param InnerException:
        """
    @property
    def Data(self) -> IDictionary:
        """

        :return:
        """
    @property
    def HResult(self) -> int:
        """

        :return:
        """
    @property
    def HelpLink(self) -> str:
        """

        :return:
        """
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """

        :return:
        """
    @property
    def Message(self) -> str:
        """

        :return:
        """
    @property
    def Source(self) -> str:
        """

        :return:
        """
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """

        :return:
        """
    @property
    def TargetSite(self) -> MethodBase:
        """

        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class ServerIdentity(Identity):
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

class SoapServices(Object):
    """"""

    @classmethod
    @property
    def XmlNsForClrType(cls) -> str:
        """

        :return:
        """
    @classmethod
    @property
    def XmlNsForClrTypeWithAssembly(cls) -> str:
        """

        :return:
        """
    @classmethod
    @property
    def XmlNsForClrTypeWithNs(cls) -> str:
        """

        :return:
        """
    @classmethod
    @property
    def XmlNsForClrTypeWithNsAndAssembly(cls) -> str:
        """

        :return:
        """
    @classmethod
    def CodeXmlNamespaceForClrTypeNamespace(cls, typeNamespace: str, assemblyName: str) -> str:
        """

        :param typeNamespace:
        :param assemblyName:
        :return:
        """
    @classmethod
    def DecodeXmlNamespaceForClrTypeNamespace(
        cls, inNamespace: str, typeNamespace: str, assemblyName: str
    ) -> Tuple[bool, str, str]:
        """

        :param inNamespace:
        :param typeNamespace:
        :param assemblyName:
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
    @classmethod
    def GetInteropFieldTypeAndNameFromXmlAttribute(
        cls, containingType: Type, xmlAttribute: str, xmlNamespace: str, type: Type, name: str
    ) -> Tuple[None, Type, str]:
        """

        :param containingType:
        :param xmlAttribute:
        :param xmlNamespace:
        :param type:
        :param name:
        """
    @classmethod
    def GetInteropFieldTypeAndNameFromXmlElement(
        cls, containingType: Type, xmlElement: str, xmlNamespace: str, type: Type, name: str
    ) -> Tuple[None, Type, str]:
        """

        :param containingType:
        :param xmlElement:
        :param xmlNamespace:
        :param type:
        :param name:
        """
    @classmethod
    def GetInteropTypeFromXmlElement(cls, xmlElement: str, xmlNamespace: str) -> Type:
        """

        :param xmlElement:
        :param xmlNamespace:
        :return:
        """
    @classmethod
    def GetInteropTypeFromXmlType(cls, xmlType: str, xmlTypeNamespace: str) -> Type:
        """

        :param xmlType:
        :param xmlTypeNamespace:
        :return:
        """
    @classmethod
    def GetSoapActionFromMethodBase(cls, mb: MethodBase) -> str:
        """

        :param mb:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def GetTypeAndMethodNameFromSoapAction(
        cls, soapAction: str, typeName: str, methodName: str
    ) -> Tuple[bool, str, str]:
        """

        :param soapAction:
        :param typeName:
        :param methodName:
        :return:
        """
    @classmethod
    def GetXmlElementForInteropType(
        cls, type: Type, xmlElement: str, xmlNamespace: str
    ) -> Tuple[bool, str, str]:
        """

        :param type:
        :param xmlElement:
        :param xmlNamespace:
        :return:
        """
    @classmethod
    def GetXmlNamespaceForMethodCall(cls, mb: MethodBase) -> str:
        """

        :param mb:
        :return:
        """
    @classmethod
    def GetXmlNamespaceForMethodResponse(cls, mb: MethodBase) -> str:
        """

        :param mb:
        :return:
        """
    @classmethod
    def GetXmlTypeForInteropType(
        cls, type: Type, xmlType: str, xmlTypeNamespace: str
    ) -> Tuple[bool, str, str]:
        """

        :param type:
        :param xmlType:
        :param xmlTypeNamespace:
        :return:
        """
    @classmethod
    def IsClrTypeNamespace(cls, namespaceString: str) -> bool:
        """

        :param namespaceString:
        :return:
        """
    @classmethod
    def IsSoapActionValidForMethodBase(cls, soapAction: str, mb: MethodBase) -> bool:
        """

        :param soapAction:
        :param mb:
        :return:
        """
    @classmethod
    @overload
    def PreLoad(cls, assembly: Assembly) -> None:
        """

        :param assembly:
        """
    @classmethod
    @overload
    def PreLoad(cls, type: Type) -> None:
        """

        :param type:
        """
    @classmethod
    def RegisterInteropXmlElement(cls, xmlElement: str, xmlNamespace: str, type: Type) -> None:
        """

        :param xmlElement:
        :param xmlNamespace:
        :param type:
        """
    @classmethod
    def RegisterInteropXmlType(cls, xmlType: str, xmlTypeNamespace: str, type: Type) -> None:
        """

        :param xmlType:
        :param xmlTypeNamespace:
        :param type:
        """
    @classmethod
    @overload
    def RegisterSoapActionForMethodBase(cls, mb: MethodBase) -> None:
        """

        :param mb:
        """
    @classmethod
    @overload
    def RegisterSoapActionForMethodBase(cls, mb: MethodBase, soapAction: str) -> None:
        """

        :param mb:
        :param soapAction:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class TypeEntry(Object):
    """"""

    @property
    def AssemblyName(self) -> str:
        """

        :return:
        """
    @AssemblyName.setter
    def AssemblyName(self, value: str) -> None: ...
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    @TypeName.setter
    def TypeName(self, value: str) -> None: ...
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

class TypeInfo(Object, IRemotingTypeInfo):
    """"""

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

class WellKnownClientTypeEntry(TypeEntry):
    """"""

    @overload
    def __init__(self, type: Type, objectUrl: str):
        """

        :param type:
        :param objectUrl:
        """
    @overload
    def __init__(self, typeName: str, assemblyName: str, objectUrl: str):
        """

        :param typeName:
        :param assemblyName:
        :param objectUrl:
        """
    @property
    def ApplicationUrl(self) -> str:
        """

        :return:
        """
    @ApplicationUrl.setter
    def ApplicationUrl(self, value: str) -> None: ...
    @property
    def AssemblyName(self) -> str:
        """

        :return:
        """
    @AssemblyName.setter
    def AssemblyName(self, value: str) -> None: ...
    @property
    def ObjectType(self) -> Type:
        """

        :return:
        """
    @property
    def ObjectUrl(self) -> str:
        """

        :return:
        """
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    @TypeName.setter
    def TypeName(self, value: str) -> None: ...
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

class WellKnownObjectMode(Enum):
    """"""

    Singleton: WellKnownObjectMode = ...
    """"""
    SingleCall: WellKnownObjectMode = ...
    """"""

class WellKnownServiceTypeEntry(TypeEntry):
    """"""

    @overload
    def __init__(self, type: Type, objectUri: str, mode: WellKnownObjectMode):
        """

        :param type:
        :param objectUri:
        :param mode:
        """
    @overload
    def __init__(self, typeName: str, assemblyName: str, objectUri: str, mode: WellKnownObjectMode):
        """

        :param typeName:
        :param assemblyName:
        :param objectUri:
        :param mode:
        """
    @property
    def AssemblyName(self) -> str:
        """

        :return:
        """
    @AssemblyName.setter
    def AssemblyName(self, value: str) -> None: ...
    @property
    def ContextAttributes(self) -> Array[IContextAttribute]:
        """

        :return:
        """
    @ContextAttributes.setter
    def ContextAttributes(self, value: Array[IContextAttribute]) -> None: ...
    @property
    def Mode(self) -> WellKnownObjectMode:
        """

        :return:
        """
    @property
    def ObjectType(self) -> Type:
        """

        :return:
        """
    @property
    def ObjectUri(self) -> str:
        """

        :return:
        """
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    @TypeName.setter
    def TypeName(self, value: str) -> None: ...
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

class XmlNamespaceEncoder(ABC, Object):
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

class __HResults(Object):
    """"""

    COR_E_REMOTING: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    COR_E_SERVER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
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
