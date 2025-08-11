"""Automatically generated stubs for C# namespace: System.ComponentModel.Design.Serialization."""

from abc import ABC
from collections.abc import Callable
from typing import ClassVar
from typing import Self
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
from System import UInt32
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

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ComponentSerializationService(ABC, Object):
    """"""
    def CreateStore(self) -> SerializationStore:
        """"""
    @overload
    def Deserialize(self, store: SerializationStore) -> ICollection:
        """"""
    @overload
    def Deserialize(self, store: SerializationStore, container: IContainer) -> ICollection:
        """"""
    @overload
    def DeserializeTo(self, store: SerializationStore, container: IContainer) -> None:
        """"""
    @overload
    def DeserializeTo(
        self, store: SerializationStore, container: IContainer, validateRecycledTypes: bool
    ) -> None:
        """"""
    @overload
    def DeserializeTo(
        self,
        store: SerializationStore,
        container: IContainer,
        validateRecycledTypes: bool,
        applyDefaults: bool,
    ) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def LoadStore(self, stream: Stream) -> SerializationStore:
        """"""
    def Serialize(self, store: SerializationStore, value: object) -> None:
        """"""
    def SerializeAbsolute(self, store: SerializationStore, value: object) -> None:
        """"""
    def SerializeMember(
        self, store: SerializationStore, owningObject: object, member: MemberDescriptor
    ) -> None:
        """"""
    def SerializeMemberAbsolute(
        self, store: SerializationStore, owningObject: object, member: MemberDescriptor
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ContextStack(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Current(self) -> object:
        """"""
    @property
    def Item(self) -> object:
        """"""
    def Append(self, context: object) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Pop(self) -> object:
        """"""
    def Push(self, context: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __getitem__(self, level: int) -> object:
        """"""
    @overload
    def __getitem__(self, type: Type) -> object:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DefaultSerializationProviderAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, providerType: Type) -> None:
        """"""
    @overload
    def __init__(self, providerTypeName: str) -> None:
        """"""
    @property
    def ProviderTypeName(self) -> str:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DesignerLoader(ABC, Object):
    """"""
    @property
    def Loading(self) -> bool:
        """"""
    def BeginLoad(self, host: IDesignerLoaderHost) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DesignerSerializerAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, serializerType: Type, baseSerializerType: Type) -> None:
        """"""
    @overload
    def __init__(self, serializerTypeName: str, baseSerializerType: Type) -> None:
        """"""
    @overload
    def __init__(self, serializerTypeName: str, baseSerializerTypeName: str) -> None:
        """"""
    @property
    def SerializerBaseTypeName(self) -> str:
        """"""
    @property
    def SerializerTypeName(self) -> str:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IDesignerLoaderHost(ABC, IDesignerHost, IServiceContainer, IServiceProvider):
    """"""
    @property
    def Container(self) -> IContainer:
        """"""
    @property
    def InTransaction(self) -> bool:
        """"""
    @property
    def Loading(self) -> bool:
        """"""
    @property
    def RootComponent(self) -> IComponent:
        """"""
    @property
    def RootComponentClassName(self) -> str:
        """"""
    @property
    def TransactionDescription(self) -> str:
        """"""
    def Activate(self) -> None:
        """"""
    @overload
    def AddService(self, serviceType: Type, callback: ServiceCreatorCallback) -> None:
        """"""
    @overload
    def AddService(
        self, serviceType: Type, callback: ServiceCreatorCallback, promote: bool
    ) -> None:
        """"""
    @overload
    def AddService(self, serviceType: Type, serviceInstance: object) -> None:
        """"""
    @overload
    def AddService(self, serviceType: Type, serviceInstance: object, promote: bool) -> None:
        """"""
    @overload
    def CreateComponent(self, componentClass: Type) -> IComponent:
        """"""
    @overload
    def CreateComponent(self, componentClass: Type, name: str) -> IComponent:
        """"""
    @overload
    def CreateTransaction(self) -> DesignerTransaction:
        """"""
    @overload
    def CreateTransaction(self, description: str) -> DesignerTransaction:
        """"""
    def DestroyComponent(self, component: IComponent) -> None:
        """"""
    def EndLoad(self, baseClassName: str, successful: bool, errorCollection: ICollection) -> None:
        """"""
    def GetDesigner(self, component: IComponent) -> IDesigner:
        """"""
    def GetService(self, serviceType: Type) -> object:
        """"""
    def GetType(self, typeName: str) -> Type:
        """"""
    def Reload(self) -> None:
        """"""
    @overload
    def RemoveService(self, serviceType: Type) -> None:
        """"""
    @overload
    def RemoveService(self, serviceType: Type, promote: bool) -> None:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IDesignerLoaderHost2(
    ABC, IDesignerLoaderHost, IDesignerHost, IServiceContainer, IServiceProvider
):
    """"""
    @property
    def CanReloadWithErrors(self) -> bool:
        """"""
    @CanReloadWithErrors.setter
    def CanReloadWithErrors(self, value: bool) -> None: ...
    @property
    def Container(self) -> IContainer:
        """"""
    @property
    def IgnoreErrorsDuringReload(self) -> bool:
        """"""
    @IgnoreErrorsDuringReload.setter
    def IgnoreErrorsDuringReload(self, value: bool) -> None: ...
    @property
    def InTransaction(self) -> bool:
        """"""
    @property
    def Loading(self) -> bool:
        """"""
    @property
    def RootComponent(self) -> IComponent:
        """"""
    @property
    def RootComponentClassName(self) -> str:
        """"""
    @property
    def TransactionDescription(self) -> str:
        """"""
    def Activate(self) -> None:
        """"""
    @overload
    def AddService(self, serviceType: Type, callback: ServiceCreatorCallback) -> None:
        """"""
    @overload
    def AddService(
        self, serviceType: Type, callback: ServiceCreatorCallback, promote: bool
    ) -> None:
        """"""
    @overload
    def AddService(self, serviceType: Type, serviceInstance: object) -> None:
        """"""
    @overload
    def AddService(self, serviceType: Type, serviceInstance: object, promote: bool) -> None:
        """"""
    @overload
    def CreateComponent(self, componentClass: Type) -> IComponent:
        """"""
    @overload
    def CreateComponent(self, componentClass: Type, name: str) -> IComponent:
        """"""
    @overload
    def CreateTransaction(self) -> DesignerTransaction:
        """"""
    @overload
    def CreateTransaction(self, description: str) -> DesignerTransaction:
        """"""
    def DestroyComponent(self, component: IComponent) -> None:
        """"""
    def EndLoad(self, baseClassName: str, successful: bool, errorCollection: ICollection) -> None:
        """"""
    def GetDesigner(self, component: IComponent) -> IDesigner:
        """"""
    def GetService(self, serviceType: Type) -> object:
        """"""
    def GetType(self, typeName: str) -> Type:
        """"""
    def Reload(self) -> None:
        """"""
    @overload
    def RemoveService(self, serviceType: Type) -> None:
        """"""
    @overload
    def RemoveService(self, serviceType: Type, promote: bool) -> None:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IDesignerLoaderService(ABC):
    """"""
    def AddLoadDependency(self) -> None:
        """"""
    def DependentLoadComplete(self, successful: bool, errorCollection: ICollection) -> None:
        """"""
    def Reload(self) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IDesignerSerializationManager(ABC, IServiceProvider):
    """"""
    @property
    def Context(self) -> ContextStack:
        """"""
    @property
    def Properties(self) -> PropertyDescriptorCollection:
        """"""
    def AddSerializationProvider(self, provider: IDesignerSerializationProvider) -> None:
        """"""
    def CreateInstance(
        self, type: Type, arguments: ICollection, name: str, addToContainer: bool
    ) -> object:
        """"""
    def GetInstance(self, name: str) -> object:
        """"""
    def GetName(self, value: object) -> str:
        """"""
    def GetSerializer(self, objectType: Type, serializerType: Type) -> object:
        """"""
    def GetService(self, serviceType: Type) -> object:
        """"""
    def GetType(self, typeName: str) -> Type:
        """"""
    def RemoveSerializationProvider(self, provider: IDesignerSerializationProvider) -> None:
        """"""
    def ReportError(self, errorInformation: object) -> None:
        """"""
    def SetName(self, instance: object, name: str) -> None:
        """"""
    ResolveName: EventType[ResolveNameEventHandler] = ...
    """"""
    SerializationComplete: EventType[EventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IDesignerSerializationProvider(ABC):
    """"""
    def GetSerializer(
        self,
        manager: IDesignerSerializationManager,
        currentSerializer: object,
        objectType: Type,
        serializerType: Type,
    ) -> object:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IDesignerSerializationService(ABC):
    """"""
    def Deserialize(self, serializationData: object) -> ICollection:
        """"""
    def Serialize(self, objects: ICollection) -> object:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class INameCreationService(ABC):
    """"""
    def CreateName(self, container: IContainer, dataType: Type) -> str:
        """"""
    def IsValidName(self, name: str) -> bool:
        """"""
    def ValidateName(self, name: str) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class InstanceDescriptor(Object):
    """"""
    @overload
    def __init__(self, member: MemberInfo, arguments: ICollection) -> None:
        """"""
    @overload
    def __init__(self, member: MemberInfo, arguments: ICollection, isComplete: bool) -> None:
        """"""
    @property
    def Arguments(self) -> ICollection:
        """"""
    @property
    def IsComplete(self) -> bool:
        """"""
    @property
    def MemberInfo(self) -> MemberInfo:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Invoke(self) -> object:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MemberRelationship(ValueType):
    """"""

    Empty: ClassVar[MemberRelationship]
    """"""
    def __init__(self, owner: object, member: MemberDescriptor) -> None:
        """"""
    @property
    def IsEmpty(self) -> bool:
        """"""
    @property
    def Member(self) -> MemberDescriptor:
        """"""
    @property
    def Owner(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: MemberRelationship, right: MemberRelationship) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: MemberRelationship, right: MemberRelationship) -> bool:
        """"""
    def __eq__(self, other: MemberRelationship) -> bool:
        """"""
    def __ne__(self, other: MemberRelationship) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MemberRelationshipService(ABC, Object):
    """"""
    @property
    def Item(self) -> MemberRelationship:
        """"""
    @Item.setter
    def Item(self, value: MemberRelationship) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SupportsRelationship(
        self, source: MemberRelationship, relationship: MemberRelationship
    ) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __getitem__(self, source: MemberRelationship) -> MemberRelationship:
        """"""
    @overload
    def __getitem__(
        self, sourceOwner: object, sourceMember: MemberDescriptor
    ) -> MemberRelationship:
        """"""
    @overload
    def __setitem__(self, source: MemberRelationship, value: MemberRelationship) -> None:
        """"""
    @overload
    def __setitem__(
        self, sourceOwner: object, sourceMember: MemberDescriptor, value: MemberRelationship
    ) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ResolveNameEventArgs(EventArgs):
    """"""
    def __init__(self, name: str) -> None:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Value(self) -> object:
        """"""
    @Value.setter
    def Value(self, value: object) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type ResolveNameEventHandler = Callable[[object, ResolveNameEventArgs], None]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RootDesignerSerializerAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, serializerType: Type, baseSerializerType: Type, reloadable: bool) -> None:
        """"""
    @overload
    def __init__(self, serializerTypeName: str, baseSerializerType: Type, reloadable: bool) -> None:
        """"""
    @overload
    def __init__(
        self, serializerTypeName: str, baseSerializerTypeName: str, reloadable: bool
    ) -> None:
        """"""
    @property
    def Reloadable(self) -> bool:
        """"""
    @property
    def SerializerBaseTypeName(self) -> str:
        """"""
    @property
    def SerializerTypeName(self) -> str:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SerializationStore(ABC, Object, IDisposable):
    """"""
    @property
    def Errors(self) -> ICollection:
        """"""
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Save(self, stream: Stream) -> None:
        """"""
    def ToString(self) -> str:
        """"""
