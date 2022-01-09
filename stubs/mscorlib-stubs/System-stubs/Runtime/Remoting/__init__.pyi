from __future__ import annotations

from abc import ABC
from typing import List, Protocol, Tuple, Union, overload

from System import Array, Boolean, Enum, Exception, Int32, MarshalByRefObject, Object, String, SystemException, Type, ValueType, Void
from System.Reflection import Assembly, MethodBase
from System.Runtime.InteropServices import _Exception
from System.Runtime.Remoting.Contexts import IContextAttribute
from System.Runtime.Remoting.Messaging import IMessage, IMessageCtrl, IMessageSink, IMethodCallMessage, IMethodMessage, IMethodReturnMessage, MethodCall
from System.Runtime.Remoting.Metadata import SoapAttribute
from System.Runtime.Remoting.Proxies import RealProxy
from System.Runtime.Serialization import IObjectReference, ISerializable, SerializationInfo, StreamingContext

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class ActivatedClientTypeEntry(TypeEntry):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, typeName: StringType, assemblyName: StringType, appUrl: StringType): ...
    
    @overload
    def __init__(self, type: TypeType, appUrl: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ApplicationUrl(self) -> StringType: ...
    
    @property
    def ContextAttributes(self) -> ArrayType[IContextAttribute]: ...
    
    @ContextAttributes.setter
    def ContextAttributes(self, value: ArrayType[IContextAttribute]) -> None: ...
    
    @property
    def ObjectType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    def get_ApplicationUrl(self) -> StringType: ...
    
    def get_ContextAttributes(self) -> ArrayType[IContextAttribute]: ...
    
    def get_ObjectType(self) -> TypeType: ...
    
    def set_ContextAttributes(self, value: ArrayType[IContextAttribute]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ActivatedServiceTypeEntry(TypeEntry):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, typeName: StringType, assemblyName: StringType): ...
    
    @overload
    def __init__(self, type: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ContextAttributes(self) -> ArrayType[IContextAttribute]: ...
    
    @ContextAttributes.setter
    def ContextAttributes(self, value: ArrayType[IContextAttribute]) -> None: ...
    
    @property
    def ObjectType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    def get_ContextAttributes(self) -> ArrayType[IContextAttribute]: ...
    
    def get_ObjectType(self) -> TypeType: ...
    
    def set_ContextAttributes(self, value: ArrayType[IContextAttribute]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ChannelInfo(ObjectType, IChannelInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ChannelData(self) -> ArrayType[ObjectType]: ...
    
    @ChannelData.setter
    def ChannelData(self, value: ArrayType[ObjectType]) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ChannelData(self) -> ArrayType[ObjectType]: ...
    
    def set_ChannelData(self, value: ArrayType[ObjectType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ComRedirectionProxy(MarshalByRefObject, IMessageSink):
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


class DelayLoadClientChannelEntry(ObjectType):
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


class DomainSpecificRemotingData(ObjectType):
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


class DynamicTypeInfo(TypeInfo, IRemotingTypeInfo):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CanCastTo(self, castType: TypeType, o: ObjectType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EnvoyInfo(ObjectType, IEnvoyInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def EnvoySinks(self) -> IMessageSink: ...
    
    @EnvoySinks.setter
    def EnvoySinks(self, value: IMessageSink) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_EnvoySinks(self) -> IMessageSink: ...
    
    def set_EnvoySinks(self, value: IMessageSink) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Identity(ObjectType):
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


class IdentityHolder(ObjectType):
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


class InternalRemotingServices(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def DebugOutChnl(s: StringType) -> VoidType: ...
    
    @staticmethod
    def GetCachedSoapAttribute(reflectionObject: ObjectType) -> SoapAttribute: ...
    
    @staticmethod
    def RemotingAssert(condition: BooleanType, message: StringType) -> VoidType: ...
    
    @staticmethod
    def RemotingTrace(messages: ArrayType[ObjectType]) -> VoidType: ...
    
    @staticmethod
    def SetServerIdentity(m: MethodCall, srvID: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ObjRef(ObjectType, IObjectReference, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, o: MarshalByRefObject, requestedType: TypeType): ...
    
    @overload
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ChannelInfo(self) -> IChannelInfo: ...
    
    @ChannelInfo.setter
    def ChannelInfo(self, value: IChannelInfo) -> None: ...
    
    @property
    def EnvoyInfo(self) -> IEnvoyInfo: ...
    
    @EnvoyInfo.setter
    def EnvoyInfo(self, value: IEnvoyInfo) -> None: ...
    
    @property
    def TypeInfo(self) -> IRemotingTypeInfo: ...
    
    @TypeInfo.setter
    def TypeInfo(self, value: IRemotingTypeInfo) -> None: ...
    
    @property
    def URI(self) -> StringType: ...
    
    @URI.setter
    def URI(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def GetRealObject(self, context: StreamingContext) -> ObjectType: ...
    
    def IsFromThisAppDomain(self) -> BooleanType: ...
    
    def IsFromThisProcess(self) -> BooleanType: ...
    
    def get_ChannelInfo(self) -> IChannelInfo: ...
    
    def get_EnvoyInfo(self) -> IEnvoyInfo: ...
    
    def get_TypeInfo(self) -> IRemotingTypeInfo: ...
    
    def get_URI(self) -> StringType: ...
    
    def set_ChannelInfo(self, value: IChannelInfo) -> VoidType: ...
    
    def set_EnvoyInfo(self, value: IEnvoyInfo) -> VoidType: ...
    
    def set_TypeInfo(self, value: IRemotingTypeInfo) -> VoidType: ...
    
    def set_URI(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ObjectHandle(MarshalByRefObject, IObjectHandle):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, o: ObjectType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def InitializeLifetimeService(self) -> ObjectType: ...
    
    def Unwrap(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RedirectionProxy(MarshalByRefObject, IMessageSink):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def NextSink(self) -> IMessageSink: ...
    
    @ObjectMode.setter
    def ObjectMode(self, value: WellKnownObjectMode) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AsyncProcessMessage(self, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl: ...
    
    def SyncProcessMessage(self, msg: IMessage) -> IMessage: ...
    
    def get_NextSink(self) -> IMessageSink: ...
    
    def set_ObjectMode(self, value: WellKnownObjectMode) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RemoteAppEntry(ObjectType):
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


class RemotingConfigHandler(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Info() -> RemotingConfigInfo: ...
    
    @staticmethod
    @Info.setter
    def Info(value: RemotingConfigInfo) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RemotingConfiguration(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def ApplicationId() -> StringType: ...
    
    @staticmethod
    @property
    def ApplicationName() -> StringType: ...
    
    @staticmethod
    @ApplicationName.setter
    def ApplicationName(value: StringType) -> None: ...
    
    @staticmethod
    @property
    def CustomErrorsMode() -> CustomErrorsModes: ...
    
    @staticmethod
    @CustomErrorsMode.setter
    def CustomErrorsMode(value: CustomErrorsModes) -> None: ...
    
    @staticmethod
    @property
    def ProcessId() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Configure(filename: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Configure(filename: StringType, ensureSecurity: BooleanType) -> VoidType: ...
    
    @staticmethod
    def CustomErrorsEnabled(isLocalRequest: BooleanType) -> BooleanType: ...
    
    @staticmethod
    def GetRegisteredActivatedClientTypes() -> ArrayType[ActivatedClientTypeEntry]: ...
    
    @staticmethod
    def GetRegisteredActivatedServiceTypes() -> ArrayType[ActivatedServiceTypeEntry]: ...
    
    @staticmethod
    def GetRegisteredWellKnownClientTypes() -> ArrayType[WellKnownClientTypeEntry]: ...
    
    @staticmethod
    def GetRegisteredWellKnownServiceTypes() -> ArrayType[WellKnownServiceTypeEntry]: ...
    
    @staticmethod
    def IsActivationAllowed(svrType: TypeType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsRemotelyActivatedClientType(svrType: TypeType) -> ActivatedClientTypeEntry: ...
    
    @staticmethod
    @overload
    def IsRemotelyActivatedClientType(typeName: StringType, assemblyName: StringType) -> ActivatedClientTypeEntry: ...
    
    @staticmethod
    @overload
    def IsWellKnownClientType(svrType: TypeType) -> WellKnownClientTypeEntry: ...
    
    @staticmethod
    @overload
    def IsWellKnownClientType(typeName: StringType, assemblyName: StringType) -> WellKnownClientTypeEntry: ...
    
    @staticmethod
    @overload
    def RegisterActivatedClientType(type: TypeType, appUrl: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def RegisterActivatedClientType(entry: ActivatedClientTypeEntry) -> VoidType: ...
    
    @staticmethod
    @overload
    def RegisterActivatedServiceType(type: TypeType) -> VoidType: ...
    
    @staticmethod
    @overload
    def RegisterActivatedServiceType(entry: ActivatedServiceTypeEntry) -> VoidType: ...
    
    @staticmethod
    @overload
    def RegisterWellKnownClientType(type: TypeType, objectUrl: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def RegisterWellKnownClientType(entry: WellKnownClientTypeEntry) -> VoidType: ...
    
    @staticmethod
    @overload
    def RegisterWellKnownServiceType(type: TypeType, objectUri: StringType, mode: WellKnownObjectMode) -> VoidType: ...
    
    @staticmethod
    @overload
    def RegisterWellKnownServiceType(entry: WellKnownServiceTypeEntry) -> VoidType: ...
    
    @staticmethod
    def get_ApplicationId() -> StringType: ...
    
    @staticmethod
    def get_ApplicationName() -> StringType: ...
    
    @staticmethod
    def get_CustomErrorsMode() -> CustomErrorsModes: ...
    
    @staticmethod
    def get_ProcessId() -> StringType: ...
    
    @staticmethod
    def set_ApplicationName(value: StringType) -> VoidType: ...
    
    @staticmethod
    def set_CustomErrorsMode(value: CustomErrorsModes) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RemotingException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, InnerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RemotingServices(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Connect(classToProxy: TypeType, url: StringType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def Connect(classToProxy: TypeType, url: StringType, data: ObjectType) -> ObjectType: ...
    
    @staticmethod
    def Disconnect(obj: MarshalByRefObject) -> BooleanType: ...
    
    @staticmethod
    def ExecuteMessage(target: MarshalByRefObject, reqMsg: IMethodCallMessage) -> IMethodReturnMessage: ...
    
    @staticmethod
    def GetEnvoyChainForProxy(obj: MarshalByRefObject) -> IMessageSink: ...
    
    @staticmethod
    def GetLifetimeService(obj: MarshalByRefObject) -> ObjectType: ...
    
    @staticmethod
    def GetMethodBaseFromMethodMessage(msg: IMethodMessage) -> MethodBase: ...
    
    @staticmethod
    def GetObjRefForProxy(obj: MarshalByRefObject) -> ObjRef: ...
    
    @staticmethod
    def GetObjectData(obj: ObjectType, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    @staticmethod
    def GetObjectUri(obj: MarshalByRefObject) -> StringType: ...
    
    @staticmethod
    def GetRealProxy(proxy: ObjectType) -> RealProxy: ...
    
    @staticmethod
    def GetServerTypeForUri(URI: StringType) -> TypeType: ...
    
    @staticmethod
    def GetSessionIdForMethodMessage(msg: IMethodMessage) -> StringType: ...
    
    @staticmethod
    def IsMethodOverloaded(msg: IMethodMessage) -> BooleanType: ...
    
    @staticmethod
    def IsObjectOutOfAppDomain(tp: ObjectType) -> BooleanType: ...
    
    @staticmethod
    def IsObjectOutOfContext(tp: ObjectType) -> BooleanType: ...
    
    @staticmethod
    def IsOneWay(method: MethodBase) -> BooleanType: ...
    
    @staticmethod
    def IsTransparentProxy(proxy: ObjectType) -> BooleanType: ...
    
    @staticmethod
    def LogRemotingStage(stage: IntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Marshal(Obj: MarshalByRefObject) -> ObjRef: ...
    
    @staticmethod
    @overload
    def Marshal(Obj: MarshalByRefObject, URI: StringType) -> ObjRef: ...
    
    @staticmethod
    @overload
    def Marshal(Obj: MarshalByRefObject, ObjURI: StringType, RequestedType: TypeType) -> ObjRef: ...
    
    @staticmethod
    def SetObjectUriForMarshal(obj: MarshalByRefObject, uri: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Unmarshal(objectRef: ObjRef) -> ObjectType: ...
    
    @staticmethod
    @overload
    def Unmarshal(objectRef: ObjRef, fRefine: BooleanType) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RemotingTimeoutException(RemotingException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, InnerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ServerException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, InnerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ServerIdentity(Identity):
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


class SoapServices(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def XmlNsForClrType() -> StringType: ...
    
    @staticmethod
    @property
    def XmlNsForClrTypeWithAssembly() -> StringType: ...
    
    @staticmethod
    @property
    def XmlNsForClrTypeWithNs() -> StringType: ...
    
    @staticmethod
    @property
    def XmlNsForClrTypeWithNsAndAssembly() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CodeXmlNamespaceForClrTypeNamespace(typeNamespace: StringType, assemblyName: StringType) -> StringType: ...
    
    @staticmethod
    def DecodeXmlNamespaceForClrTypeNamespace(inNamespace: StringType, typeNamespace: StringType, assemblyName: StringType) -> Tuple[BooleanType, StringType, StringType]: ...
    
    @staticmethod
    def GetInteropFieldTypeAndNameFromXmlAttribute(containingType: TypeType, xmlAttribute: StringType, xmlNamespace: StringType, type: TypeType, name: StringType) -> Tuple[VoidType, TypeType, StringType]: ...
    
    @staticmethod
    def GetInteropFieldTypeAndNameFromXmlElement(containingType: TypeType, xmlElement: StringType, xmlNamespace: StringType, type: TypeType, name: StringType) -> Tuple[VoidType, TypeType, StringType]: ...
    
    @staticmethod
    def GetInteropTypeFromXmlElement(xmlElement: StringType, xmlNamespace: StringType) -> TypeType: ...
    
    @staticmethod
    def GetInteropTypeFromXmlType(xmlType: StringType, xmlTypeNamespace: StringType) -> TypeType: ...
    
    @staticmethod
    def GetSoapActionFromMethodBase(mb: MethodBase) -> StringType: ...
    
    @staticmethod
    def GetTypeAndMethodNameFromSoapAction(soapAction: StringType, typeName: StringType, methodName: StringType) -> Tuple[BooleanType, StringType, StringType]: ...
    
    @staticmethod
    def GetXmlElementForInteropType(type: TypeType, xmlElement: StringType, xmlNamespace: StringType) -> Tuple[BooleanType, StringType, StringType]: ...
    
    @staticmethod
    def GetXmlNamespaceForMethodCall(mb: MethodBase) -> StringType: ...
    
    @staticmethod
    def GetXmlNamespaceForMethodResponse(mb: MethodBase) -> StringType: ...
    
    @staticmethod
    def GetXmlTypeForInteropType(type: TypeType, xmlType: StringType, xmlTypeNamespace: StringType) -> Tuple[BooleanType, StringType, StringType]: ...
    
    @staticmethod
    def IsClrTypeNamespace(namespaceString: StringType) -> BooleanType: ...
    
    @staticmethod
    def IsSoapActionValidForMethodBase(soapAction: StringType, mb: MethodBase) -> BooleanType: ...
    
    @staticmethod
    @overload
    def PreLoad(assembly: Assembly) -> VoidType: ...
    
    @staticmethod
    @overload
    def PreLoad(type: TypeType) -> VoidType: ...
    
    @staticmethod
    def RegisterInteropXmlElement(xmlElement: StringType, xmlNamespace: StringType, type: TypeType) -> VoidType: ...
    
    @staticmethod
    def RegisterInteropXmlType(xmlType: StringType, xmlTypeNamespace: StringType, type: TypeType) -> VoidType: ...
    
    @staticmethod
    @overload
    def RegisterSoapActionForMethodBase(mb: MethodBase) -> VoidType: ...
    
    @staticmethod
    @overload
    def RegisterSoapActionForMethodBase(mb: MethodBase, soapAction: StringType) -> VoidType: ...
    
    @staticmethod
    def get_XmlNsForClrType() -> StringType: ...
    
    @staticmethod
    def get_XmlNsForClrTypeWithAssembly() -> StringType: ...
    
    @staticmethod
    def get_XmlNsForClrTypeWithNs() -> StringType: ...
    
    @staticmethod
    def get_XmlNsForClrTypeWithNsAndAssembly() -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeEntry(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AssemblyName(self) -> StringType: ...
    
    @AssemblyName.setter
    def AssemblyName(self, value: StringType) -> None: ...
    
    @property
    def TypeName(self) -> StringType: ...
    
    @TypeName.setter
    def TypeName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_AssemblyName(self) -> StringType: ...
    
    def get_TypeName(self) -> StringType: ...
    
    def set_AssemblyName(self, value: StringType) -> VoidType: ...
    
    def set_TypeName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeInfo(ObjectType, IRemotingTypeInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def TypeName(self) -> StringType: ...
    
    @TypeName.setter
    def TypeName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CanCastTo(self, castType: TypeType, o: ObjectType) -> BooleanType: ...
    
    def get_TypeName(self) -> StringType: ...
    
    def set_TypeName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WellKnownClientTypeEntry(TypeEntry):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, typeName: StringType, assemblyName: StringType, objectUrl: StringType): ...
    
    @overload
    def __init__(self, type: TypeType, objectUrl: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ApplicationUrl(self) -> StringType: ...
    
    @ApplicationUrl.setter
    def ApplicationUrl(self, value: StringType) -> None: ...
    
    @property
    def ObjectType(self) -> TypeType: ...
    
    @property
    def ObjectUrl(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    def get_ApplicationUrl(self) -> StringType: ...
    
    def get_ObjectType(self) -> TypeType: ...
    
    def get_ObjectUrl(self) -> StringType: ...
    
    def set_ApplicationUrl(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WellKnownServiceTypeEntry(TypeEntry):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, typeName: StringType, assemblyName: StringType, objectUri: StringType, mode: WellKnownObjectMode): ...
    
    @overload
    def __init__(self, type: TypeType, objectUri: StringType, mode: WellKnownObjectMode): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ContextAttributes(self) -> ArrayType[IContextAttribute]: ...
    
    @ContextAttributes.setter
    def ContextAttributes(self, value: ArrayType[IContextAttribute]) -> None: ...
    
    @property
    def Mode(self) -> WellKnownObjectMode: ...
    
    @property
    def ObjectType(self) -> TypeType: ...
    
    @property
    def ObjectUri(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    def get_ContextAttributes(self) -> ArrayType[IContextAttribute]: ...
    
    def get_Mode(self) -> WellKnownObjectMode: ...
    
    def get_ObjectType(self) -> TypeType: ...
    
    def get_ObjectUri(self) -> StringType: ...
    
    def set_ContextAttributes(self, value: ArrayType[IContextAttribute]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNamespaceEncoder(ABC, ObjectType):
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


class __HResults(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def COR_E_REMOTING() -> IntType: ...
    
    @staticmethod
    @property
    def COR_E_SERVER() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class IdOps(ValueType):
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

class IChannelInfo(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def ChannelData(self) -> ArrayType[ObjectType]: ...
    
    @ChannelData.setter
    def ChannelData(self, value: ArrayType[ObjectType]) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ChannelData(self) -> ArrayType[ObjectType]: ...
    
    def set_ChannelData(self, value: ArrayType[ObjectType]) -> VoidType: ...
    
    # No Events


class IEnvoyInfo(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def EnvoySinks(self) -> IMessageSink: ...
    
    @EnvoySinks.setter
    def EnvoySinks(self, value: IMessageSink) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_EnvoySinks(self) -> IMessageSink: ...
    
    def set_EnvoySinks(self, value: IMessageSink) -> VoidType: ...
    
    # No Events


class IObjectHandle(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Unwrap(self) -> ObjectType: ...
    
    # No Events


class IRemotingTypeInfo(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def TypeName(self) -> StringType: ...
    
    @TypeName.setter
    def TypeName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CanCastTo(self, fromType: TypeType, o: ObjectType) -> BooleanType: ...
    
    def get_TypeName(self) -> StringType: ...
    
    def set_TypeName(self, value: StringType) -> VoidType: ...
    
    # No Events


# ---------- Enums ---------- #

class CustomErrorsModes(Enum):
    On: IntType = 0
    Off: IntType = 1
    RemoteOnly: IntType = 2


class DuplicateIdentityOption(Enum):
    Unique: IntType = 0
    UseExisting: IntType = 1


class WellKnownObjectMode(Enum):
    Singleton: IntType = 1
    SingleCall: IntType = 2


# No Delegates

__all__ = [
    ActivatedClientTypeEntry,
    ActivatedServiceTypeEntry,
    ChannelInfo,
    ComRedirectionProxy,
    DelayLoadClientChannelEntry,
    DomainSpecificRemotingData,
    DynamicTypeInfo,
    EnvoyInfo,
    Identity,
    IdentityHolder,
    InternalRemotingServices,
    ObjRef,
    ObjectHandle,
    RedirectionProxy,
    RemoteAppEntry,
    RemotingConfigHandler,
    RemotingConfiguration,
    RemotingException,
    RemotingServices,
    RemotingTimeoutException,
    ServerException,
    ServerIdentity,
    SoapServices,
    TypeEntry,
    TypeInfo,
    WellKnownClientTypeEntry,
    WellKnownServiceTypeEntry,
    XmlNamespaceEncoder,
    __HResults,
    IdOps,
    IChannelInfo,
    IEnvoyInfo,
    IObjectHandle,
    IRemotingTypeInfo,
    CustomErrorsModes,
    DuplicateIdentityOption,
    WellKnownObjectMode,
]
