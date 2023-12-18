from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import Generic
from typing import Protocol
from typing import TypeVar
from typing import Union
from typing import overload

from System import AsyncCallback
from System import Attribute
from System import Boolean
from System import EventArgs
from System import EventHandler
from System import IAsyncResult
from System import ICloneable
from System import IDisposable
from System import Int32
from System import IntPtr
from System import IServiceProvider
from System import MulticastDelegate
from System import Object
from System import String
from System import Type
from System import ValueType
from System import Void
from System.Collections import ICollection
from System.ComponentModel import IContainer
from System.ComponentModel import MemberDescriptor
from System.ComponentModel import PropertyDescriptorCollection
from System.ComponentModel.Design import IDesignerHost
from System.ComponentModel.Design import IServiceContainer
from System.IO import Stream
from System.Reflection import MemberInfo
from System.Runtime.InteropServices import _Attribute
from System.Runtime.Serialization import ISerializable

# ---------- Types ---------- #

T = TypeVar("T")

BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

# ---------- Classes ---------- #

class ComponentSerializationService(ABC, ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def CreateStore(self) -> SerializationStore: ...
    @overload
    def Deserialize(self, store: SerializationStore) -> ICollection: ...
    @overload
    def Deserialize(self, store: SerializationStore, container: IContainer) -> ICollection: ...
    @overload
    def DeserializeTo(self, store: SerializationStore, container: IContainer) -> VoidType: ...
    @overload
    def DeserializeTo(
        self, store: SerializationStore, container: IContainer, validateRecycledTypes: BooleanType
    ) -> VoidType: ...
    @overload
    def DeserializeTo(
        self,
        store: SerializationStore,
        container: IContainer,
        validateRecycledTypes: BooleanType,
        applyDefaults: BooleanType,
    ) -> VoidType: ...
    def LoadStore(self, stream: Stream) -> SerializationStore: ...
    def Serialize(self, store: SerializationStore, value: ObjectType) -> VoidType: ...
    def SerializeAbsolute(self, store: SerializationStore, value: ObjectType) -> VoidType: ...
    def SerializeMember(
        self, store: SerializationStore, owningObject: ObjectType, member: MemberDescriptor
    ) -> VoidType: ...
    def SerializeMemberAbsolute(
        self, store: SerializationStore, owningObject: ObjectType, member: MemberDescriptor
    ) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ContextStack(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def Current(self) -> ObjectType: ...
    def __getitem__(self, key: IntType) -> ObjectType: ...
    def __getitem__(self, key: TypeType) -> ObjectType: ...

    # ---------- Methods ---------- #

    def Append(self, context: ObjectType) -> VoidType: ...
    def Pop(self) -> ObjectType: ...
    def Push(self, context: ObjectType) -> VoidType: ...
    def get_Current(self) -> ObjectType: ...
    @overload
    def get_Item(self, level: IntType) -> ObjectType: ...
    @overload
    def get_Item(self, type: TypeType) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DefaultSerializationProviderAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, providerType: TypeType): ...
    @overload
    def __init__(self, providerTypeName: StringType): ...

    # ---------- Properties ---------- #

    @property
    def ProviderTypeName(self) -> StringType: ...

    # ---------- Methods ---------- #

    def get_ProviderTypeName(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DesignerLoader(ABC, ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Loading(self) -> BooleanType: ...

    # ---------- Methods ---------- #

    def BeginLoad(self, host: IDesignerLoaderHost) -> VoidType: ...
    def Dispose(self) -> VoidType: ...
    def Flush(self) -> VoidType: ...
    def get_Loading(self) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DesignerSerializerAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, serializerType: TypeType, baseSerializerType: TypeType): ...
    @overload
    def __init__(self, serializerTypeName: StringType, baseSerializerType: TypeType): ...
    @overload
    def __init__(self, serializerTypeName: StringType, baseSerializerTypeName: StringType): ...

    # ---------- Properties ---------- #

    @property
    def SerializerBaseTypeName(self) -> StringType: ...
    @property
    def SerializerTypeName(self) -> StringType: ...
    @property
    def TypeId(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def get_SerializerBaseTypeName(self) -> StringType: ...
    def get_SerializerTypeName(self) -> StringType: ...
    def get_TypeId(self) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class InstanceDescriptor(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, member: MemberInfo, arguments: ICollection): ...
    @overload
    def __init__(self, member: MemberInfo, arguments: ICollection, isComplete: BooleanType): ...

    # ---------- Properties ---------- #

    @property
    def Arguments(self) -> ICollection: ...
    @property
    def IsComplete(self) -> BooleanType: ...
    @property
    def MemberInfo(self) -> MemberInfo: ...

    # ---------- Methods ---------- #

    def Invoke(self) -> ObjectType: ...
    def get_Arguments(self) -> ICollection: ...
    def get_IsComplete(self) -> BooleanType: ...
    def get_MemberInfo(self) -> MemberInfo: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class MemberRelationshipService(ABC, ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    def __getitem__(self, key: MemberRelationship) -> MemberRelationship: ...
    def __setitem__(self, key: MemberRelationship, value: MemberRelationship) -> None: ...
    def __getitem__(self, key: ObjectType) -> MemberRelationship: ...
    def __setitem__(self, key: ObjectType, value: MemberRelationship) -> None: ...

    # ---------- Methods ---------- #

    def SupportsRelationship(
        self, source: MemberRelationship, relationship: MemberRelationship
    ) -> BooleanType: ...
    @overload
    def get_Item(self, source: MemberRelationship) -> MemberRelationship: ...
    @overload
    def get_Item(
        self, sourceOwner: ObjectType, sourceMember: MemberDescriptor
    ) -> MemberRelationship: ...
    @overload
    def set_Item(self, source: MemberRelationship, value: MemberRelationship) -> VoidType: ...
    @overload
    def set_Item(
        self, sourceOwner: ObjectType, sourceMember: MemberDescriptor, value: MemberRelationship
    ) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ResolveNameEventArgs(EventArgs):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, name: StringType): ...

    # ---------- Properties ---------- #

    @property
    def Name(self) -> StringType: ...
    @property
    def Value(self) -> ObjectType: ...
    @Value.setter
    def Value(self, value: ObjectType) -> None: ...

    # ---------- Methods ---------- #

    def get_Name(self) -> StringType: ...
    def get_Value(self) -> ObjectType: ...
    def set_Value(self, value: ObjectType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ResolveNameEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, object: ObjectType, method: NIntType): ...

    # No Properties

    # ---------- Methods ---------- #

    def BeginInvoke(
        self,
        sender: ObjectType,
        e: ResolveNameEventArgs,
        callback: AsyncCallback,
        object: ObjectType,
    ) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    def Invoke(self, sender: ObjectType, e: ResolveNameEventArgs) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RootDesignerSerializerAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(
        self, serializerType: TypeType, baseSerializerType: TypeType, reloadable: BooleanType
    ): ...
    @overload
    def __init__(
        self, serializerTypeName: StringType, baseSerializerType: TypeType, reloadable: BooleanType
    ): ...
    @overload
    def __init__(
        self,
        serializerTypeName: StringType,
        baseSerializerTypeName: StringType,
        reloadable: BooleanType,
    ): ...

    # ---------- Properties ---------- #

    @property
    def Reloadable(self) -> BooleanType: ...
    @property
    def SerializerBaseTypeName(self) -> StringType: ...
    @property
    def SerializerTypeName(self) -> StringType: ...
    @property
    def TypeId(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def get_Reloadable(self) -> BooleanType: ...
    def get_SerializerBaseTypeName(self) -> StringType: ...
    def get_SerializerTypeName(self) -> StringType: ...
    def get_TypeId(self) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SerializationStore(ABC, ObjectType, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Errors(self) -> ICollection: ...

    # ---------- Methods ---------- #

    def Close(self) -> VoidType: ...
    def Save(self, stream: Stream) -> VoidType: ...
    def get_Errors(self) -> ICollection: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# ---------- Structs ---------- #

class MemberRelationship(ValueType):
    # ---------- Fields ---------- #

    @staticmethod
    @property
    def Empty() -> MemberRelationship: ...

    # ---------- Constructors ---------- #

    def __init__(self, owner: ObjectType, member: MemberDescriptor): ...

    # ---------- Properties ---------- #

    @property
    def IsEmpty(self) -> BooleanType: ...
    @property
    def Member(self) -> MemberDescriptor: ...
    @property
    def Owner(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def Equals(self, obj: ObjectType) -> BooleanType: ...
    def GetHashCode(self) -> IntType: ...
    def get_IsEmpty(self) -> BooleanType: ...
    def get_Member(self) -> MemberDescriptor: ...
    def get_Owner(self) -> ObjectType: ...
    @staticmethod
    def op_Equality(left: MemberRelationship, right: MemberRelationship) -> BooleanType: ...
    @staticmethod
    def op_Inequality(left: MemberRelationship, right: MemberRelationship) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# ---------- Interfaces ---------- #

class IDesignerLoaderHost(Protocol, IDesignerHost, IServiceContainer, IServiceProvider):
    # No Properties

    # ---------- Methods ---------- #

    def EndLoad(
        self, baseClassName: StringType, successful: BooleanType, errorCollection: ICollection
    ) -> VoidType: ...
    def Reload(self) -> VoidType: ...

    # No Events

class IDesignerLoaderHost2(
    Protocol, IDesignerLoaderHost, IDesignerHost, IServiceContainer, IServiceProvider
):
    # ---------- Properties ---------- #

    @property
    def CanReloadWithErrors(self) -> BooleanType: ...
    @CanReloadWithErrors.setter
    def CanReloadWithErrors(self, value: BooleanType) -> None: ...
    @property
    def IgnoreErrorsDuringReload(self) -> BooleanType: ...
    @IgnoreErrorsDuringReload.setter
    def IgnoreErrorsDuringReload(self, value: BooleanType) -> None: ...

    # ---------- Methods ---------- #

    def get_CanReloadWithErrors(self) -> BooleanType: ...
    def get_IgnoreErrorsDuringReload(self) -> BooleanType: ...
    def set_CanReloadWithErrors(self, value: BooleanType) -> VoidType: ...
    def set_IgnoreErrorsDuringReload(self, value: BooleanType) -> VoidType: ...

    # No Events

class IDesignerLoaderService(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def AddLoadDependency(self) -> VoidType: ...
    def DependentLoadComplete(
        self, successful: BooleanType, errorCollection: ICollection
    ) -> VoidType: ...
    def Reload(self) -> BooleanType: ...

    # No Events

class IDesignerSerializationManager(Protocol, IServiceProvider):
    # ---------- Properties ---------- #

    @property
    def Context(self) -> ContextStack: ...
    @property
    def Properties(self) -> PropertyDescriptorCollection: ...

    # ---------- Methods ---------- #

    def AddSerializationProvider(self, provider: IDesignerSerializationProvider) -> VoidType: ...
    def CreateInstance(
        self, type: TypeType, arguments: ICollection, name: StringType, addToContainer: BooleanType
    ) -> ObjectType: ...
    def GetInstance(self, name: StringType) -> ObjectType: ...
    def GetName(self, value: ObjectType) -> StringType: ...
    def GetSerializer(self, objectType: TypeType, serializerType: TypeType) -> ObjectType: ...
    def GetType(self, typeName: StringType) -> TypeType: ...
    def RemoveSerializationProvider(self, provider: IDesignerSerializationProvider) -> VoidType: ...
    def ReportError(self, errorInformation: ObjectType) -> VoidType: ...
    def SetName(self, instance: ObjectType, name: StringType) -> VoidType: ...
    def add_ResolveName(self, value: ResolveNameEventHandler) -> VoidType: ...
    def add_SerializationComplete(self, value: EventHandler) -> VoidType: ...
    def get_Context(self) -> ContextStack: ...
    def get_Properties(self) -> PropertyDescriptorCollection: ...
    def remove_ResolveName(self, value: ResolveNameEventHandler) -> VoidType: ...
    def remove_SerializationComplete(self, value: EventHandler) -> VoidType: ...

    # ---------- Events ---------- #

    ResolveName: EventType[ResolveNameEventHandler] = ...

    SerializationComplete: EventType[EventHandler] = ...

class IDesignerSerializationProvider(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetSerializer(
        self,
        manager: IDesignerSerializationManager,
        currentSerializer: ObjectType,
        objectType: TypeType,
        serializerType: TypeType,
    ) -> ObjectType: ...

    # No Events

class IDesignerSerializationService(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Deserialize(self, serializationData: ObjectType) -> ICollection: ...
    def Serialize(self, objects: ICollection) -> ObjectType: ...

    # No Events

class INameCreationService(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def CreateName(self, container: IContainer, dataType: TypeType) -> StringType: ...
    def IsValidName(self, name: StringType) -> BooleanType: ...
    def ValidateName(self, name: StringType) -> VoidType: ...

    # No Events

# No Enums

# ---------- Delegates ---------- #

ResolveNameEventHandler = Callable[[ObjectType, ResolveNameEventArgs], VoidType]

__all__ = [
    ComponentSerializationService,
    ContextStack,
    DefaultSerializationProviderAttribute,
    DesignerLoader,
    DesignerSerializerAttribute,
    InstanceDescriptor,
    MemberRelationshipService,
    ResolveNameEventArgs,
    ResolveNameEventHandler,
    RootDesignerSerializerAttribute,
    SerializationStore,
    MemberRelationship,
    IDesignerLoaderHost,
    IDesignerLoaderHost2,
    IDesignerLoaderService,
    IDesignerSerializationManager,
    IDesignerSerializationProvider,
    IDesignerSerializationService,
    INameCreationService,
    ResolveNameEventHandler,
]
