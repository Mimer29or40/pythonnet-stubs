from __future__ import annotations

from typing import Callable, List, Protocol, Union, overload

from System import Array, AsyncCallback, Attribute, Boolean, ContextBoundObject, IAsyncResult, ICloneable, Int32, IntPtr, LocalDataStoreSlot, MarshalByRefObject, MulticastDelegate, Object, String, Void
from System.Runtime.InteropServices import _Attribute
from System.Runtime.Remoting.Activation import IConstructionCallMessage, IConstructionReturnMessage
from System.Runtime.Remoting.Messaging import IMessage, IMessageCtrl, IMessageSink, InternalSink
from System.Runtime.Serialization import ISerializable

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class ArrayWithSize(ObjectType):
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


class ArrayWithSize(ObjectType):
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


class ArrayWithSize(ObjectType):
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


class CallBackHelper(ObjectType):
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


class CallBackHelper(ObjectType):
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


class CallBackHelper(ObjectType):
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


class Context(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ContextID(self) -> IntType: ...
    
    @property
    def ContextProperties(self) -> ArrayType[IContextProperty]: ...
    
    @staticmethod
    @property
    def DefaultContext() -> Context: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def AllocateDataSlot() -> LocalDataStoreSlot: ...
    
    @staticmethod
    def AllocateNamedDataSlot(name: StringType) -> LocalDataStoreSlot: ...
    
    def DoCallBack(self, deleg: CrossContextDelegate) -> VoidType: ...
    
    @staticmethod
    def FreeNamedDataSlot(name: StringType) -> VoidType: ...
    
    def Freeze(self) -> VoidType: ...
    
    @staticmethod
    def GetData(slot: LocalDataStoreSlot) -> ObjectType: ...
    
    @staticmethod
    def GetNamedDataSlot(name: StringType) -> LocalDataStoreSlot: ...
    
    def GetProperty(self, name: StringType) -> IContextProperty: ...
    
    @staticmethod
    def RegisterDynamicProperty(prop: IDynamicProperty, obj: ContextBoundObject, ctx: Context) -> BooleanType: ...
    
    @staticmethod
    def SetData(slot: LocalDataStoreSlot, data: ObjectType) -> VoidType: ...
    
    def SetProperty(self, prop: IContextProperty) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    @staticmethod
    def UnregisterDynamicProperty(name: StringType, obj: ContextBoundObject, ctx: Context) -> BooleanType: ...
    
    def get_ContextID(self) -> IntType: ...
    
    def get_ContextProperties(self) -> ArrayType[IContextProperty]: ...
    
    @staticmethod
    def get_DefaultContext() -> Context: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Context(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ContextID(self) -> IntType: ...
    
    @property
    def ContextProperties(self) -> ArrayType[IContextProperty]: ...
    
    @staticmethod
    @property
    def DefaultContext() -> Context: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def AllocateDataSlot() -> LocalDataStoreSlot: ...
    
    @staticmethod
    def AllocateNamedDataSlot(name: StringType) -> LocalDataStoreSlot: ...
    
    def DoCallBack(self, deleg: CrossContextDelegate) -> VoidType: ...
    
    @staticmethod
    def FreeNamedDataSlot(name: StringType) -> VoidType: ...
    
    def Freeze(self) -> VoidType: ...
    
    @staticmethod
    def GetData(slot: LocalDataStoreSlot) -> ObjectType: ...
    
    @staticmethod
    def GetNamedDataSlot(name: StringType) -> LocalDataStoreSlot: ...
    
    def GetProperty(self, name: StringType) -> IContextProperty: ...
    
    @staticmethod
    def RegisterDynamicProperty(prop: IDynamicProperty, obj: ContextBoundObject, ctx: Context) -> BooleanType: ...
    
    @staticmethod
    def SetData(slot: LocalDataStoreSlot, data: ObjectType) -> VoidType: ...
    
    def SetProperty(self, prop: IContextProperty) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    @staticmethod
    def UnregisterDynamicProperty(name: StringType, obj: ContextBoundObject, ctx: Context) -> BooleanType: ...
    
    def get_ContextID(self) -> IntType: ...
    
    def get_ContextProperties(self) -> ArrayType[IContextProperty]: ...
    
    @staticmethod
    def get_DefaultContext() -> Context: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Context(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ContextID(self) -> IntType: ...
    
    @property
    def ContextProperties(self) -> ArrayType[IContextProperty]: ...
    
    @staticmethod
    @property
    def DefaultContext() -> Context: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def AllocateDataSlot() -> LocalDataStoreSlot: ...
    
    @staticmethod
    def AllocateNamedDataSlot(name: StringType) -> LocalDataStoreSlot: ...
    
    def DoCallBack(self, deleg: CrossContextDelegate) -> VoidType: ...
    
    @staticmethod
    def FreeNamedDataSlot(name: StringType) -> VoidType: ...
    
    def Freeze(self) -> VoidType: ...
    
    @staticmethod
    def GetData(slot: LocalDataStoreSlot) -> ObjectType: ...
    
    @staticmethod
    def GetNamedDataSlot(name: StringType) -> LocalDataStoreSlot: ...
    
    def GetProperty(self, name: StringType) -> IContextProperty: ...
    
    @staticmethod
    def RegisterDynamicProperty(prop: IDynamicProperty, obj: ContextBoundObject, ctx: Context) -> BooleanType: ...
    
    @staticmethod
    def SetData(slot: LocalDataStoreSlot, data: ObjectType) -> VoidType: ...
    
    def SetProperty(self, prop: IContextProperty) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    @staticmethod
    def UnregisterDynamicProperty(name: StringType, obj: ContextBoundObject, ctx: Context) -> BooleanType: ...
    
    def get_ContextID(self) -> IntType: ...
    
    def get_ContextProperties(self) -> ArrayType[IContextProperty]: ...
    
    @staticmethod
    def get_DefaultContext() -> Context: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContextAttribute(Attribute, _Attribute, IContextAttribute, IContextProperty):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def Freeze(self, newContext: Context) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetPropertiesForNewContext(self, ctorMsg: IConstructionCallMessage) -> VoidType: ...
    
    def IsContextOK(self, ctx: Context, ctorMsg: IConstructionCallMessage) -> BooleanType: ...
    
    def IsNewContextOK(self, newCtx: Context) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContextAttribute(Attribute, _Attribute, IContextAttribute, IContextProperty):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def Freeze(self, newContext: Context) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetPropertiesForNewContext(self, ctorMsg: IConstructionCallMessage) -> VoidType: ...
    
    def IsContextOK(self, ctx: Context, ctorMsg: IConstructionCallMessage) -> BooleanType: ...
    
    def IsNewContextOK(self, newCtx: Context) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContextAttribute(Attribute, _Attribute, IContextAttribute, IContextProperty):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def Freeze(self, newContext: Context) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetPropertiesForNewContext(self, ctorMsg: IConstructionCallMessage) -> VoidType: ...
    
    def IsContextOK(self, ctx: Context, ctorMsg: IConstructionCallMessage) -> BooleanType: ...
    
    def IsNewContextOK(self, newCtx: Context) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContextProperty(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Property(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    def get_Property(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContextProperty(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Property(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    def get_Property(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContextProperty(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Property(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    def get_Property(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CrossContextDelegate(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CrossContextDelegate(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CrossContextDelegate(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DynamicPropertyHolder(ObjectType):
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


class DynamicPropertyHolder(ObjectType):
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


class DynamicPropertyHolder(ObjectType):
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


class SynchronizationAttribute(ContextAttribute, _Attribute, IContextAttribute, IContextProperty, IContributeServerContextSink, IContributeClientContextSink):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def NOT_SUPPORTED() -> IntType: ...
    
    @staticmethod
    @property
    def REQUIRED() -> IntType: ...
    
    @staticmethod
    @property
    def REQUIRES_NEW() -> IntType: ...
    
    @staticmethod
    @property
    def SUPPORTED() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, reEntrant: BooleanType): ...
    
    @overload
    def __init__(self, flag: IntType): ...
    
    @overload
    def __init__(self, flag: IntType, reEntrant: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsReEntrant(self) -> BooleanType: ...
    
    @property
    def Locked(self) -> BooleanType: ...
    
    @Locked.setter
    def Locked(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetClientContextSink(self, nextSink: IMessageSink) -> IMessageSink: ...
    
    def GetPropertiesForNewContext(self, ctorMsg: IConstructionCallMessage) -> VoidType: ...
    
    def GetServerContextSink(self, nextSink: IMessageSink) -> IMessageSink: ...
    
    def IsContextOK(self, ctx: Context, msg: IConstructionCallMessage) -> BooleanType: ...
    
    def get_IsReEntrant(self) -> BooleanType: ...
    
    def get_Locked(self) -> BooleanType: ...
    
    def set_Locked(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SynchronizationAttribute(ContextAttribute, _Attribute, IContextAttribute, IContextProperty, IContributeServerContextSink, IContributeClientContextSink):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def NOT_SUPPORTED() -> IntType: ...
    
    @staticmethod
    @property
    def REQUIRED() -> IntType: ...
    
    @staticmethod
    @property
    def REQUIRES_NEW() -> IntType: ...
    
    @staticmethod
    @property
    def SUPPORTED() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, reEntrant: BooleanType): ...
    
    @overload
    def __init__(self, flag: IntType): ...
    
    @overload
    def __init__(self, flag: IntType, reEntrant: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsReEntrant(self) -> BooleanType: ...
    
    @property
    def Locked(self) -> BooleanType: ...
    
    @Locked.setter
    def Locked(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetClientContextSink(self, nextSink: IMessageSink) -> IMessageSink: ...
    
    def GetPropertiesForNewContext(self, ctorMsg: IConstructionCallMessage) -> VoidType: ...
    
    def GetServerContextSink(self, nextSink: IMessageSink) -> IMessageSink: ...
    
    def IsContextOK(self, ctx: Context, msg: IConstructionCallMessage) -> BooleanType: ...
    
    def get_IsReEntrant(self) -> BooleanType: ...
    
    def get_Locked(self) -> BooleanType: ...
    
    def set_Locked(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SynchronizationAttribute(ContextAttribute, _Attribute, IContextAttribute, IContextProperty, IContributeServerContextSink, IContributeClientContextSink):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def NOT_SUPPORTED() -> IntType: ...
    
    @staticmethod
    @property
    def REQUIRED() -> IntType: ...
    
    @staticmethod
    @property
    def REQUIRES_NEW() -> IntType: ...
    
    @staticmethod
    @property
    def SUPPORTED() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, reEntrant: BooleanType): ...
    
    @overload
    def __init__(self, flag: IntType): ...
    
    @overload
    def __init__(self, flag: IntType, reEntrant: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsReEntrant(self) -> BooleanType: ...
    
    @property
    def Locked(self) -> BooleanType: ...
    
    @Locked.setter
    def Locked(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetClientContextSink(self, nextSink: IMessageSink) -> IMessageSink: ...
    
    def GetPropertiesForNewContext(self, ctorMsg: IConstructionCallMessage) -> VoidType: ...
    
    def GetServerContextSink(self, nextSink: IMessageSink) -> IMessageSink: ...
    
    def IsContextOK(self, ctx: Context, msg: IConstructionCallMessage) -> BooleanType: ...
    
    def get_IsReEntrant(self) -> BooleanType: ...
    
    def get_Locked(self) -> BooleanType: ...
    
    def set_Locked(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SynchronizedClientContextSink(InternalSink, IMessageSink):
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


class SynchronizedClientContextSink(InternalSink, IMessageSink):
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


class SynchronizedClientContextSink(InternalSink, IMessageSink):
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


class SynchronizedServerContextSink(InternalSink, IMessageSink):
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


class SynchronizedServerContextSink(InternalSink, IMessageSink):
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


class SynchronizedServerContextSink(InternalSink, IMessageSink):
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


class WorkItem(ObjectType):
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


class WorkItem(ObjectType):
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


class WorkItem(ObjectType):
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


# No Structs

# ---------- Interfaces ---------- #

class IContextAttribute(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetPropertiesForNewContext(self, msg: IConstructionCallMessage) -> VoidType: ...
    
    def IsContextOK(self, ctx: Context, msg: IConstructionCallMessage) -> BooleanType: ...
    
    # No Events


class IContextAttribute(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetPropertiesForNewContext(self, msg: IConstructionCallMessage) -> VoidType: ...
    
    def IsContextOK(self, ctx: Context, msg: IConstructionCallMessage) -> BooleanType: ...
    
    # No Events


class IContextAttribute(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetPropertiesForNewContext(self, msg: IConstructionCallMessage) -> VoidType: ...
    
    def IsContextOK(self, ctx: Context, msg: IConstructionCallMessage) -> BooleanType: ...
    
    # No Events


class IContextProperty(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Freeze(self, newContext: Context) -> VoidType: ...
    
    def IsNewContextOK(self, newCtx: Context) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events


class IContextProperty(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Freeze(self, newContext: Context) -> VoidType: ...
    
    def IsNewContextOK(self, newCtx: Context) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events


class IContextProperty(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Freeze(self, newContext: Context) -> VoidType: ...
    
    def IsNewContextOK(self, newCtx: Context) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events


class IContextPropertyActivator(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CollectFromClientContext(self, msg: IConstructionCallMessage) -> VoidType: ...
    
    def CollectFromServerContext(self, msg: IConstructionReturnMessage) -> VoidType: ...
    
    def DeliverClientContextToServerContext(self, msg: IConstructionCallMessage) -> BooleanType: ...
    
    def DeliverServerContextToClientContext(self, msg: IConstructionReturnMessage) -> BooleanType: ...
    
    def IsOKToActivate(self, msg: IConstructionCallMessage) -> BooleanType: ...
    
    # No Events


class IContextPropertyActivator(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CollectFromClientContext(self, msg: IConstructionCallMessage) -> VoidType: ...
    
    def CollectFromServerContext(self, msg: IConstructionReturnMessage) -> VoidType: ...
    
    def DeliverClientContextToServerContext(self, msg: IConstructionCallMessage) -> BooleanType: ...
    
    def DeliverServerContextToClientContext(self, msg: IConstructionReturnMessage) -> BooleanType: ...
    
    def IsOKToActivate(self, msg: IConstructionCallMessage) -> BooleanType: ...
    
    # No Events


class IContextPropertyActivator(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CollectFromClientContext(self, msg: IConstructionCallMessage) -> VoidType: ...
    
    def CollectFromServerContext(self, msg: IConstructionReturnMessage) -> VoidType: ...
    
    def DeliverClientContextToServerContext(self, msg: IConstructionCallMessage) -> BooleanType: ...
    
    def DeliverServerContextToClientContext(self, msg: IConstructionReturnMessage) -> BooleanType: ...
    
    def IsOKToActivate(self, msg: IConstructionCallMessage) -> BooleanType: ...
    
    # No Events


class IContributeClientContextSink(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetClientContextSink(self, nextSink: IMessageSink) -> IMessageSink: ...
    
    # No Events


class IContributeClientContextSink(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetClientContextSink(self, nextSink: IMessageSink) -> IMessageSink: ...
    
    # No Events


class IContributeClientContextSink(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetClientContextSink(self, nextSink: IMessageSink) -> IMessageSink: ...
    
    # No Events


class IContributeDynamicSink(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetDynamicSink(self) -> IDynamicMessageSink: ...
    
    # No Events


class IContributeDynamicSink(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetDynamicSink(self) -> IDynamicMessageSink: ...
    
    # No Events


class IContributeDynamicSink(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetDynamicSink(self) -> IDynamicMessageSink: ...
    
    # No Events


class IContributeEnvoySink(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetEnvoySink(self, obj: MarshalByRefObject, nextSink: IMessageSink) -> IMessageSink: ...
    
    # No Events


class IContributeEnvoySink(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetEnvoySink(self, obj: MarshalByRefObject, nextSink: IMessageSink) -> IMessageSink: ...
    
    # No Events


class IContributeEnvoySink(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetEnvoySink(self, obj: MarshalByRefObject, nextSink: IMessageSink) -> IMessageSink: ...
    
    # No Events


class IContributeObjectSink(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetObjectSink(self, obj: MarshalByRefObject, nextSink: IMessageSink) -> IMessageSink: ...
    
    # No Events


class IContributeObjectSink(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetObjectSink(self, obj: MarshalByRefObject, nextSink: IMessageSink) -> IMessageSink: ...
    
    # No Events


class IContributeObjectSink(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetObjectSink(self, obj: MarshalByRefObject, nextSink: IMessageSink) -> IMessageSink: ...
    
    # No Events


class IContributeServerContextSink(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetServerContextSink(self, nextSink: IMessageSink) -> IMessageSink: ...
    
    # No Events


class IContributeServerContextSink(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetServerContextSink(self, nextSink: IMessageSink) -> IMessageSink: ...
    
    # No Events


class IContributeServerContextSink(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetServerContextSink(self, nextSink: IMessageSink) -> IMessageSink: ...
    
    # No Events


class IDynamicMessageSink(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ProcessMessageFinish(self, replyMsg: IMessage, bCliSide: BooleanType, bAsync: BooleanType) -> VoidType: ...
    
    def ProcessMessageStart(self, reqMsg: IMessage, bCliSide: BooleanType, bAsync: BooleanType) -> VoidType: ...
    
    # No Events


class IDynamicMessageSink(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ProcessMessageFinish(self, replyMsg: IMessage, bCliSide: BooleanType, bAsync: BooleanType) -> VoidType: ...
    
    def ProcessMessageStart(self, reqMsg: IMessage, bCliSide: BooleanType, bAsync: BooleanType) -> VoidType: ...
    
    # No Events


class IDynamicMessageSink(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ProcessMessageFinish(self, replyMsg: IMessage, bCliSide: BooleanType, bAsync: BooleanType) -> VoidType: ...
    
    def ProcessMessageStart(self, reqMsg: IMessage, bCliSide: BooleanType, bAsync: BooleanType) -> VoidType: ...
    
    # No Events


class IDynamicProperty(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    # No Events


class IDynamicProperty(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    # No Events


class IDynamicProperty(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    # No Events


# No Enums

# ---------- Delegates ---------- #

CrossContextDelegate = Callable[[], VoidType]

CrossContextDelegate = Callable[[], VoidType]

CrossContextDelegate = Callable[[], VoidType]

__all__ = [
    ArrayWithSize,
    CallBackHelper,
    Context,
    ContextAttribute,
    ContextProperty,
    CrossContextDelegate,
    DynamicPropertyHolder,
    SynchronizationAttribute,
    SynchronizedClientContextSink,
    SynchronizedServerContextSink,
    WorkItem,
    IContextAttribute,
    IContextProperty,
    IContextPropertyActivator,
    IContributeClientContextSink,
    IContributeDynamicSink,
    IContributeEnvoySink,
    IContributeObjectSink,
    IContributeServerContextSink,
    IDynamicMessageSink,
    IDynamicProperty,
    CrossContextDelegate,
]
