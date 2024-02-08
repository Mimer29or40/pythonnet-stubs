from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Tuple
from typing import TypeVar
from typing import overload

from System import Attribute
from System import EventArgs
from System import EventHandler
from System import Guid
from System import IDisposable
from System import IntPtr
from System import IServiceProvider
from System import Object
from System import Type
from System import ValueType
from System.Collections import ICollection
from System.ComponentModel import IComponent
from System.ComponentModel import IContainer
from System.ComponentModel import MemberDescriptor
from System.ComponentModel import PropertyDescriptorCollection
from System.ComponentModel.Design import DesignerTransaction
from System.ComponentModel.Design import DesignerTransactionCloseEventHandler
from System.ComponentModel.Design import IDesigner
from System.ComponentModel.Design import IDesignerHost
from System.ComponentModel.Design import IServiceContainer
from System.ComponentModel.Design import ServiceCreatorCallback
from System.IO import Stream
from System.Reflection import MemberInfo
from System.Runtime.InteropServices import _Attribute

T = TypeVar("T")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class ComponentSerializationService(ABC, Object):
    """"""

    def CreateStore(self) -> SerializationStore:
        """

        :return:
        """
    @overload
    def Deserialize(self, store: SerializationStore) -> ICollection:
        """

        :param store:
        :return:
        """
    @overload
    def Deserialize(self, store: SerializationStore, container: IContainer) -> ICollection:
        """

        :param store:
        :param container:
        :return:
        """
    @overload
    def DeserializeTo(self, store: SerializationStore, container: IContainer) -> None:
        """

        :param store:
        :param container:
        """
    @overload
    def DeserializeTo(
        self, store: SerializationStore, container: IContainer, validateRecycledTypes: bool
    ) -> None:
        """

        :param store:
        :param container:
        :param validateRecycledTypes:
        """
    @overload
    def DeserializeTo(
        self,
        store: SerializationStore,
        container: IContainer,
        validateRecycledTypes: bool,
        applyDefaults: bool,
    ) -> None:
        """

        :param store:
        :param container:
        :param validateRecycledTypes:
        :param applyDefaults:
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
    def LoadStore(self, stream: Stream) -> SerializationStore:
        """

        :param stream:
        :return:
        """
    def Serialize(self, store: SerializationStore, value: object) -> None:
        """

        :param store:
        :param value:
        """
    def SerializeAbsolute(self, store: SerializationStore, value: object) -> None:
        """

        :param store:
        :param value:
        """
    def SerializeMember(
        self, store: SerializationStore, owningObject: object, member: MemberDescriptor
    ) -> None:
        """

        :param store:
        :param owningObject:
        :param member:
        """
    def SerializeMemberAbsolute(
        self, store: SerializationStore, owningObject: object, member: MemberDescriptor
    ) -> None:
        """

        :param store:
        :param owningObject:
        :param member:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ContextStack(Object):
    """"""

    def __init__(self):
        """"""
    @property
    def Current(self) -> object:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    def Append(self, context: object) -> None:
        """

        :param context:
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
    def Pop(self) -> object:
        """

        :return:
        """
    def Push(self, context: object) -> None:
        """

        :param context:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def __getitem__(self, level: int) -> object:
        """

        :param level:
        :return:
        """
    @overload
    def __getitem__(self, type: Type) -> object:
        """

        :param type:
        :return:
        """

class DefaultSerializationProviderAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, providerTypeName: str):
        """

        :param providerTypeName:
        """
    @overload
    def __init__(self, providerType: Type):
        """

        :param providerType:
        """
    @property
    def ProviderTypeName(self) -> str:
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

class DesignerLoader(ABC, Object):
    """"""

    @property
    def Loading(self) -> bool:
        """

        :return:
        """
    def BeginLoad(self, host: IDesignerLoaderHost) -> None:
        """

        :param host:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
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

class DesignerSerializerAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, serializerTypeName: str, baseSerializerTypeName: str):
        """

        :param serializerTypeName:
        :param baseSerializerTypeName:
        """
    @overload
    def __init__(self, serializerTypeName: str, baseSerializerType: Type):
        """

        :param serializerTypeName:
        :param baseSerializerType:
        """
    @overload
    def __init__(self, serializerType: Type, baseSerializerType: Type):
        """

        :param serializerType:
        :param baseSerializerType:
        """
    @property
    def SerializerBaseTypeName(self) -> str:
        """

        :return:
        """
    @property
    def SerializerTypeName(self) -> str:
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

class IDesignerLoaderHost(IDesignerHost, IServiceContainer, IServiceProvider):
    """"""

    @property
    def Container(self) -> IContainer:
        """

        :return:
        """
    @property
    def InTransaction(self) -> bool:
        """

        :return:
        """
    @property
    def Loading(self) -> bool:
        """

        :return:
        """
    @property
    def RootComponent(self) -> IComponent:
        """

        :return:
        """
    @property
    def RootComponentClassName(self) -> str:
        """

        :return:
        """
    @property
    def TransactionDescription(self) -> str:
        """

        :return:
        """
    def Activate(self) -> None:
        """"""
    @overload
    def AddService(self, serviceType: Type, callback: ServiceCreatorCallback) -> None:
        """

        :param serviceType:
        :param callback:
        """
    @overload
    def AddService(self, serviceType: Type, serviceInstance: object) -> None:
        """

        :param serviceType:
        :param serviceInstance:
        """
    @overload
    def AddService(
        self, serviceType: Type, callback: ServiceCreatorCallback, promote: bool
    ) -> None:
        """

        :param serviceType:
        :param callback:
        :param promote:
        """
    @overload
    def AddService(self, serviceType: Type, serviceInstance: object, promote: bool) -> None:
        """

        :param serviceType:
        :param serviceInstance:
        :param promote:
        """
    @overload
    def CreateComponent(self, componentClass: Type) -> IComponent:
        """

        :param componentClass:
        :return:
        """
    @overload
    def CreateComponent(self, componentClass: Type, name: str) -> IComponent:
        """

        :param componentClass:
        :param name:
        :return:
        """
    @overload
    def CreateTransaction(self) -> DesignerTransaction:
        """

        :return:
        """
    @overload
    def CreateTransaction(self, description: str) -> DesignerTransaction:
        """

        :param description:
        :return:
        """
    def DestroyComponent(self, component: IComponent) -> None:
        """

        :param component:
        """
    def EndLoad(self, baseClassName: str, successful: bool, errorCollection: ICollection) -> None:
        """

        :param baseClassName:
        :param successful:
        :param errorCollection:
        """
    def GetDesigner(self, component: IComponent) -> IDesigner:
        """

        :param component:
        :return:
        """
    def GetService(self, serviceType: Type) -> object:
        """

        :param serviceType:
        :return:
        """
    def GetType(self, typeName: str) -> Type:
        """

        :param typeName:
        :return:
        """
    def Reload(self) -> None:
        """"""
    @overload
    def RemoveService(self, serviceType: Type) -> None:
        """

        :param serviceType:
        """
    @overload
    def RemoveService(self, serviceType: Type, promote: bool) -> None:
        """

        :param serviceType:
        :param promote:
        """
    Activated: EventType[EventHandler] = ...
    """"""
    Deactivated: EventType[EventHandler] = ...
    """"""
    LoadComplete: EventType[EventHandler] = ...
    """"""
    TransactionClosed: EventType[DesignerTransactionCloseEventHandler] = ...
    """"""
    TransactionClosing: EventType[DesignerTransactionCloseEventHandler] = ...
    """"""
    TransactionOpened: EventType[EventHandler] = ...
    """"""
    TransactionOpening: EventType[EventHandler] = ...
    """"""

class IDesignerLoaderHost2(IDesignerLoaderHost, IDesignerHost, IServiceContainer, IServiceProvider):
    """"""

    @property
    def CanReloadWithErrors(self) -> bool:
        """

        :return:
        """
    @CanReloadWithErrors.setter
    def CanReloadWithErrors(self, value: bool) -> None: ...
    @property
    def Container(self) -> IContainer:
        """

        :return:
        """
    @property
    def IgnoreErrorsDuringReload(self) -> bool:
        """

        :return:
        """
    @IgnoreErrorsDuringReload.setter
    def IgnoreErrorsDuringReload(self, value: bool) -> None: ...
    @property
    def InTransaction(self) -> bool:
        """

        :return:
        """
    @property
    def Loading(self) -> bool:
        """

        :return:
        """
    @property
    def RootComponent(self) -> IComponent:
        """

        :return:
        """
    @property
    def RootComponentClassName(self) -> str:
        """

        :return:
        """
    @property
    def TransactionDescription(self) -> str:
        """

        :return:
        """
    def Activate(self) -> None:
        """"""
    @overload
    def AddService(self, serviceType: Type, callback: ServiceCreatorCallback) -> None:
        """

        :param serviceType:
        :param callback:
        """
    @overload
    def AddService(self, serviceType: Type, serviceInstance: object) -> None:
        """

        :param serviceType:
        :param serviceInstance:
        """
    @overload
    def AddService(
        self, serviceType: Type, callback: ServiceCreatorCallback, promote: bool
    ) -> None:
        """

        :param serviceType:
        :param callback:
        :param promote:
        """
    @overload
    def AddService(self, serviceType: Type, serviceInstance: object, promote: bool) -> None:
        """

        :param serviceType:
        :param serviceInstance:
        :param promote:
        """
    @overload
    def CreateComponent(self, componentClass: Type) -> IComponent:
        """

        :param componentClass:
        :return:
        """
    @overload
    def CreateComponent(self, componentClass: Type, name: str) -> IComponent:
        """

        :param componentClass:
        :param name:
        :return:
        """
    @overload
    def CreateTransaction(self) -> DesignerTransaction:
        """

        :return:
        """
    @overload
    def CreateTransaction(self, description: str) -> DesignerTransaction:
        """

        :param description:
        :return:
        """
    def DestroyComponent(self, component: IComponent) -> None:
        """

        :param component:
        """
    def EndLoad(self, baseClassName: str, successful: bool, errorCollection: ICollection) -> None:
        """

        :param baseClassName:
        :param successful:
        :param errorCollection:
        """
    def GetDesigner(self, component: IComponent) -> IDesigner:
        """

        :param component:
        :return:
        """
    def GetService(self, serviceType: Type) -> object:
        """

        :param serviceType:
        :return:
        """
    def GetType(self, typeName: str) -> Type:
        """

        :param typeName:
        :return:
        """
    def Reload(self) -> None:
        """"""
    @overload
    def RemoveService(self, serviceType: Type) -> None:
        """

        :param serviceType:
        """
    @overload
    def RemoveService(self, serviceType: Type, promote: bool) -> None:
        """

        :param serviceType:
        :param promote:
        """
    Activated: EventType[EventHandler] = ...
    """"""
    Deactivated: EventType[EventHandler] = ...
    """"""
    LoadComplete: EventType[EventHandler] = ...
    """"""
    TransactionClosed: EventType[DesignerTransactionCloseEventHandler] = ...
    """"""
    TransactionClosing: EventType[DesignerTransactionCloseEventHandler] = ...
    """"""
    TransactionOpened: EventType[EventHandler] = ...
    """"""
    TransactionOpening: EventType[EventHandler] = ...
    """"""

class IDesignerLoaderService:
    """"""

    def AddLoadDependency(self) -> None:
        """"""
    def DependentLoadComplete(self, successful: bool, errorCollection: ICollection) -> None:
        """

        :param successful:
        :param errorCollection:
        """
    def Reload(self) -> bool:
        """

        :return:
        """

class IDesignerSerializationManager(IServiceProvider):
    """"""

    @property
    def Context(self) -> ContextStack:
        """

        :return:
        """
    @property
    def Properties(self) -> PropertyDescriptorCollection:
        """

        :return:
        """
    def AddSerializationProvider(self, provider: IDesignerSerializationProvider) -> None:
        """

        :param provider:
        """
    def CreateInstance(
        self, type: Type, arguments: ICollection, name: str, addToContainer: bool
    ) -> object:
        """

        :param type:
        :param arguments:
        :param name:
        :param addToContainer:
        :return:
        """
    def GetInstance(self, name: str) -> object:
        """

        :param name:
        :return:
        """
    def GetName(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    def GetSerializer(self, objectType: Type, serializerType: Type) -> object:
        """

        :param objectType:
        :param serializerType:
        :return:
        """
    def GetService(self, serviceType: Type) -> object:
        """

        :param serviceType:
        :return:
        """
    def GetType(self, typeName: str) -> Type:
        """

        :param typeName:
        :return:
        """
    def RemoveSerializationProvider(self, provider: IDesignerSerializationProvider) -> None:
        """

        :param provider:
        """
    def ReportError(self, errorInformation: object) -> None:
        """

        :param errorInformation:
        """
    def SetName(self, instance: object, name: str) -> None:
        """

        :param instance:
        :param name:
        """
    ResolveName: EventType[ResolveNameEventHandler] = ...
    """"""
    SerializationComplete: EventType[EventHandler] = ...
    """"""

class IDesignerSerializationProvider:
    """"""

    def GetSerializer(
        self,
        manager: IDesignerSerializationManager,
        currentSerializer: object,
        objectType: Type,
        serializerType: Type,
    ) -> object:
        """

        :param manager:
        :param currentSerializer:
        :param objectType:
        :param serializerType:
        :return:
        """

class IDesignerSerializationService:
    """"""

    def Deserialize(self, serializationData: object) -> ICollection:
        """

        :param serializationData:
        :return:
        """
    def Serialize(self, objects: ICollection) -> object:
        """

        :param objects:
        :return:
        """

class INameCreationService:
    """"""

    def CreateName(self, container: IContainer, dataType: Type) -> str:
        """

        :param container:
        :param dataType:
        :return:
        """
    def IsValidName(self, name: str) -> bool:
        """

        :param name:
        :return:
        """
    def ValidateName(self, name: str) -> None:
        """

        :param name:
        """

class InstanceDescriptor(Object):
    """"""

    @overload
    def __init__(self, member: MemberInfo, arguments: ICollection):
        """

        :param member:
        :param arguments:
        """
    @overload
    def __init__(self, member: MemberInfo, arguments: ICollection, isComplete: bool):
        """

        :param member:
        :param arguments:
        :param isComplete:
        """
    @property
    def Arguments(self) -> ICollection:
        """

        :return:
        """
    @property
    def IsComplete(self) -> bool:
        """

        :return:
        """
    @property
    def MemberInfo(self) -> MemberInfo:
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
    def Invoke(self) -> object:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class MemberRelationship(ValueType):
    """"""

    Empty: Final[ClassVar[MemberRelationship]] = ...
    """
    
    :return: 
    """
    def __init__(self, owner: object, member: MemberDescriptor):
        """

        :param owner:
        :param member:
        """
    @property
    def IsEmpty(self) -> bool:
        """

        :return:
        """
    @property
    def Member(self) -> MemberDescriptor:
        """

        :return:
        """
    @property
    def Owner(self) -> object:
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
    def __eq__(self, other: MemberRelationship) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: MemberRelationship) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: MemberRelationship, right: MemberRelationship) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: MemberRelationship, right: MemberRelationship) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class MemberRelationshipService(ABC, Object):
    """"""

    @property
    def Item(self) -> MemberRelationship:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: MemberRelationship) -> None: ...
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
    def SupportsRelationship(
        self, source: MemberRelationship, relationship: MemberRelationship
    ) -> bool:
        """

        :param source:
        :param relationship:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def __getitem__(self, source: MemberRelationship) -> MemberRelationship:
        """

        :param source:
        :return:
        """
    @overload
    def __getitem__(
        self, sourceOwner: object, sourceMember: MemberDescriptor
    ) -> MemberRelationship:
        """

        :param sourceOwner:
        :param sourceMember:
        :return:
        """
    @overload
    def __setitem__(self, source: MemberRelationship, value: MemberRelationship) -> None:
        """

        :param source:
        :param value:
        """
    @overload
    def __setitem__(
        self, sourceOwner: object, sourceMember: MemberDescriptor, value: MemberRelationship
    ) -> None:
        """

        :param sourceOwner:
        :param sourceMember:
        :param value:
        """

class ResolveNameEventArgs(EventArgs):
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
    def Value(self) -> object:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: object) -> None: ...
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

ResolveNameEventHandler: Callable[[object, ResolveNameEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class RootDesignerSerializerAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, serializerTypeName: str, baseSerializerTypeName: str, reloadable: bool):
        """

        :param serializerTypeName:
        :param baseSerializerTypeName:
        :param reloadable:
        """
    @overload
    def __init__(self, serializerTypeName: str, baseSerializerType: Type, reloadable: bool):
        """

        :param serializerTypeName:
        :param baseSerializerType:
        :param reloadable:
        """
    @overload
    def __init__(self, serializerType: Type, baseSerializerType: Type, reloadable: bool):
        """

        :param serializerType:
        :param baseSerializerType:
        :param reloadable:
        """
    @property
    def Reloadable(self) -> bool:
        """

        :return:
        """
    @property
    def SerializerBaseTypeName(self) -> str:
        """

        :return:
        """
    @property
    def SerializerTypeName(self) -> str:
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

class SerializationStore(ABC, Object, IDisposable):
    """"""

    @property
    def Errors(self) -> ICollection:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def Save(self, stream: Stream) -> None:
        """

        :param stream:
        """
    def ToString(self) -> str:
        """

        :return:
        """
