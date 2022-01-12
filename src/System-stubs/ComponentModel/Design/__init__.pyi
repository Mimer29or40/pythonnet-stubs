from __future__ import annotations

from abc import ABC
from typing import Callable, Generic, List, Protocol, TypeVar, Union, overload

from System import Array, AsyncCallback, Attribute, Boolean, Enum, EventArgs, EventHandler, Exception, Guid, IAsyncResult, ICloneable, IDisposable, IServiceProvider, Int32, IntPtr, MulticastDelegate, Object, String, Type, Void
from System.Collections import CollectionBase, ICollection, IDictionary, IEnumerable, IEnumerator, IList
from System.ComponentModel import EventDescriptor, EventDescriptorCollection, IComponent, IContainer, IExtenderProvider, InheritanceAttribute, LicenseContext, LicenseUsageMode, MemberDescriptor, PropertyDescriptor, PropertyDescriptorCollection, TypeDescriptionProvider
from System.Globalization import CultureInfo
from System.IO import Stream
from System.Reflection import Assembly, AssemblyName
from System.Resources import IResourceReader, IResourceWriter
from System.Runtime.InteropServices import ExternalException, _Attribute, _Exception
from System.Runtime.Serialization import ISerializable

# ---------- Types ---------- #

T = TypeVar('T')

ArrayType = Union[List, Array]
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

class ActiveDesignerEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, oldDesigner: IDesignerHost, newDesigner: IDesignerHost): ...
    
    # ---------- Properties ---------- #
    
    @property
    def NewDesigner(self) -> IDesignerHost: ...
    
    @property
    def OldDesigner(self) -> IDesignerHost: ...
    
    # ---------- Methods ---------- #
    
    def get_NewDesigner(self) -> IDesignerHost: ...
    
    def get_OldDesigner(self) -> IDesignerHost: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ActiveDesignerEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: ActiveDesignerEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: ActiveDesignerEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CheckoutException(ExternalException, ISerializable, _Exception):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Canceled() -> CheckoutException: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, errorCode: IntType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CommandID(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, menuGroup: Guid, commandID: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Guid(self) -> Guid: ...
    
    @property
    def ID(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Guid(self) -> Guid: ...
    
    def get_ID(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ComponentChangedEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, component: ObjectType, member: MemberDescriptor, oldValue: ObjectType, newValue: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Component(self) -> ObjectType: ...
    
    @property
    def Member(self) -> MemberDescriptor: ...
    
    @property
    def NewValue(self) -> ObjectType: ...
    
    @property
    def OldValue(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_Component(self) -> ObjectType: ...
    
    def get_Member(self) -> MemberDescriptor: ...
    
    def get_NewValue(self) -> ObjectType: ...
    
    def get_OldValue(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ComponentChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: ComponentChangedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: ComponentChangedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ComponentChangingEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, component: ObjectType, member: MemberDescriptor): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Component(self) -> ObjectType: ...
    
    @property
    def Member(self) -> MemberDescriptor: ...
    
    # ---------- Methods ---------- #
    
    def get_Component(self) -> ObjectType: ...
    
    def get_Member(self) -> MemberDescriptor: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ComponentChangingEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: ComponentChangingEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: ComponentChangingEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ComponentEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, component: IComponent): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Component(self) -> IComponent: ...
    
    # ---------- Methods ---------- #
    
    def get_Component(self) -> IComponent: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ComponentEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: ComponentEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: ComponentEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ComponentRenameEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, component: ObjectType, oldName: StringType, newName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Component(self) -> ObjectType: ...
    
    @property
    def NewName(self) -> StringType: ...
    
    @property
    def OldName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Component(self) -> ObjectType: ...
    
    def get_NewName(self) -> StringType: ...
    
    def get_OldName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ComponentRenameEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: ComponentRenameEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: ComponentRenameEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DesignerCollection(ObjectType, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, designers: ArrayType[IDesignerHost]): ...
    
    @overload
    def __init__(self, designers: IList): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    def __getitem__(self, key: IntType) -> IDesignerHost: ...
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Item(self, index: IntType) -> IDesignerHost: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DesignerEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, host: IDesignerHost): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Designer(self) -> IDesignerHost: ...
    
    # ---------- Methods ---------- #
    
    def get_Designer(self) -> IDesignerHost: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DesignerEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: DesignerEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: DesignerEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DesignerOptionService(ABC, ObjectType, IDesignerOptionService):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Options(self) -> DesignerOptionCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_Options(self) -> DesignerOptionCollection: ...
    
    # No Events
    
    
    # ---------- Sub Classes ---------- #
    
    class DesignerOptionCollection(ObjectType, IList, ICollection, IEnumerable):
        # No Fields
        
        # No Constructors
        
        # ---------- Properties ---------- #
        
        @property
        def Count(self) -> IntType: ...
        
        def __getitem__(self, key: IntType) -> DesignerOptionCollection: ...
        
        def __getitem__(self, key: StringType) -> DesignerOptionCollection: ...
        
        @property
        def Name(self) -> StringType: ...
        
        @property
        def Parent(self) -> DesignerOptionCollection: ...
        
        @property
        def Properties(self) -> PropertyDescriptorCollection: ...
        
        # ---------- Methods ---------- #
        
        def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
        
        def GetEnumerator(self) -> IEnumerator: ...
        
        def IndexOf(self, value: DesignerOptionCollection) -> IntType: ...
        
        def ShowDialog(self) -> BooleanType: ...
        
        def get_Count(self) -> IntType: ...
        
        @overload
        def get_Item(self, index: IntType) -> DesignerOptionCollection: ...
        
        @overload
        def get_Item(self, name: StringType) -> DesignerOptionCollection: ...
        
        def get_Name(self) -> StringType: ...
        
        def get_Parent(self) -> DesignerOptionCollection: ...
        
        def get_Properties(self) -> PropertyDescriptorCollection: ...
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DesignerTransaction(ABC, ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Canceled(self) -> BooleanType: ...
    
    @property
    def Committed(self) -> BooleanType: ...
    
    @property
    def Description(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Cancel(self) -> VoidType: ...
    
    def Commit(self) -> VoidType: ...
    
    def get_Canceled(self) -> BooleanType: ...
    
    def get_Committed(self) -> BooleanType: ...
    
    def get_Description(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DesignerTransactionCloseEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, commit: BooleanType): ...
    
    @overload
    def __init__(self, commit: BooleanType, lastTransaction: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def LastTransaction(self) -> BooleanType: ...
    
    @property
    def TransactionCommitted(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_LastTransaction(self) -> BooleanType: ...
    
    def get_TransactionCommitted(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DesignerTransactionCloseEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: DesignerTransactionCloseEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: DesignerTransactionCloseEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DesignerVerb(MenuCommand):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, text: StringType, handler: EventHandler): ...
    
    @overload
    def __init__(self, text: StringType, handler: EventHandler, startCommandID: CommandID): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Description(self) -> StringType: ...
    
    @Description.setter
    def Description(self, value: StringType) -> None: ...
    
    @property
    def Text(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    def get_Description(self) -> StringType: ...
    
    def get_Text(self) -> StringType: ...
    
    def set_Description(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DesignerVerbCollection(CollectionBase, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: ArrayType[DesignerVerb]): ...
    
    # ---------- Properties ---------- #
    
    def __getitem__(self, key: IntType) -> DesignerVerb: ...
    
    def __setitem__(self, key: IntType, value: DesignerVerb) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, value: DesignerVerb) -> IntType: ...
    
    @overload
    def AddRange(self, value: ArrayType[DesignerVerb]) -> VoidType: ...
    
    @overload
    def AddRange(self, value: DesignerVerbCollection) -> VoidType: ...
    
    def Contains(self, value: DesignerVerb) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[DesignerVerb], index: IntType) -> VoidType: ...
    
    def IndexOf(self, value: DesignerVerb) -> IntType: ...
    
    def Insert(self, index: IntType, value: DesignerVerb) -> VoidType: ...
    
    def Remove(self, value: DesignerVerb) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> DesignerVerb: ...
    
    def set_Item(self, index: IntType, value: DesignerVerb) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DesigntimeLicenseContext(LicenseContext, IServiceProvider):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def UsageMode(self) -> LicenseUsageMode: ...
    
    # ---------- Methods ---------- #
    
    def GetSavedLicenseKey(self, type: TypeType, resourceAssembly: Assembly) -> StringType: ...
    
    def SetSavedLicenseKey(self, type: TypeType, key: StringType) -> VoidType: ...
    
    def get_UsageMode(self) -> LicenseUsageMode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DesigntimeLicenseContextSerializer(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Serialize(o: Stream, cryptoKey: StringType, context: DesigntimeLicenseContext) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HelpKeywordAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> HelpKeywordAttribute: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, keyword: StringType): ...
    
    @overload
    def __init__(self, t: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def HelpKeyword(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    def get_HelpKeyword(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MenuCommand(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, handler: EventHandler, command: CommandID): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Checked(self) -> BooleanType: ...
    
    @Checked.setter
    def Checked(self, value: BooleanType) -> None: ...
    
    @property
    def CommandID(self) -> CommandID: ...
    
    @property
    def Enabled(self) -> BooleanType: ...
    
    @Enabled.setter
    def Enabled(self, value: BooleanType) -> None: ...
    
    @property
    def OleStatus(self) -> IntType: ...
    
    @property
    def Properties(self) -> IDictionary: ...
    
    @property
    def Supported(self) -> BooleanType: ...
    
    @Supported.setter
    def Supported(self, value: BooleanType) -> None: ...
    
    @property
    def Visible(self) -> BooleanType: ...
    
    @Visible.setter
    def Visible(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Invoke(self) -> VoidType: ...
    
    @overload
    def Invoke(self, arg: ObjectType) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def add_CommandChanged(self, value: EventHandler) -> VoidType: ...
    
    def get_Checked(self) -> BooleanType: ...
    
    def get_CommandID(self) -> CommandID: ...
    
    def get_Enabled(self) -> BooleanType: ...
    
    def get_OleStatus(self) -> IntType: ...
    
    def get_Properties(self) -> IDictionary: ...
    
    def get_Supported(self) -> BooleanType: ...
    
    def get_Visible(self) -> BooleanType: ...
    
    def remove_CommandChanged(self, value: EventHandler) -> VoidType: ...
    
    def set_Checked(self, value: BooleanType) -> VoidType: ...
    
    def set_Enabled(self, value: BooleanType) -> VoidType: ...
    
    def set_Supported(self, value: BooleanType) -> VoidType: ...
    
    def set_Visible(self, value: BooleanType) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    CommandChanged: EventType[EventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RuntimeLicenseContext(LicenseContext, IServiceProvider):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetSavedLicenseKey(self, type: TypeType, resourceAssembly: Assembly) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ServiceContainer(ObjectType, IServiceContainer, IServiceProvider, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, parentProvider: IServiceProvider): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def AddService(self, serviceType: TypeType, serviceInstance: ObjectType) -> VoidType: ...
    
    @overload
    def AddService(self, serviceType: TypeType, callback: ServiceCreatorCallback) -> VoidType: ...
    
    @overload
    def AddService(self, serviceType: TypeType, serviceInstance: ObjectType, promote: BooleanType) -> VoidType: ...
    
    @overload
    def AddService(self, serviceType: TypeType, callback: ServiceCreatorCallback, promote: BooleanType) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def GetService(self, serviceType: TypeType) -> ObjectType: ...
    
    @overload
    def RemoveService(self, serviceType: TypeType) -> VoidType: ...
    
    @overload
    def RemoveService(self, serviceType: TypeType, promote: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ServiceCreatorCallback(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, container: IServiceContainer, serviceType: TypeType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> ObjectType: ...
    
    def Invoke(self, container: IServiceContainer, serviceType: TypeType) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StandardCommands(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def AlignBottom() -> CommandID: ...
    
    @staticmethod
    @property
    def AlignHorizontalCenters() -> CommandID: ...
    
    @staticmethod
    @property
    def AlignLeft() -> CommandID: ...
    
    @staticmethod
    @property
    def AlignRight() -> CommandID: ...
    
    @staticmethod
    @property
    def AlignToGrid() -> CommandID: ...
    
    @staticmethod
    @property
    def AlignTop() -> CommandID: ...
    
    @staticmethod
    @property
    def AlignVerticalCenters() -> CommandID: ...
    
    @staticmethod
    @property
    def ArrangeBottom() -> CommandID: ...
    
    @staticmethod
    @property
    def ArrangeIcons() -> CommandID: ...
    
    @staticmethod
    @property
    def ArrangeRight() -> CommandID: ...
    
    @staticmethod
    @property
    def BringForward() -> CommandID: ...
    
    @staticmethod
    @property
    def BringToFront() -> CommandID: ...
    
    @staticmethod
    @property
    def CenterHorizontally() -> CommandID: ...
    
    @staticmethod
    @property
    def CenterVertically() -> CommandID: ...
    
    @staticmethod
    @property
    def Copy() -> CommandID: ...
    
    @staticmethod
    @property
    def Cut() -> CommandID: ...
    
    @staticmethod
    @property
    def Delete() -> CommandID: ...
    
    @staticmethod
    @property
    def DocumentOutline() -> CommandID: ...
    
    @staticmethod
    @property
    def F1Help() -> CommandID: ...
    
    @staticmethod
    @property
    def Group() -> CommandID: ...
    
    @staticmethod
    @property
    def HorizSpaceConcatenate() -> CommandID: ...
    
    @staticmethod
    @property
    def HorizSpaceDecrease() -> CommandID: ...
    
    @staticmethod
    @property
    def HorizSpaceIncrease() -> CommandID: ...
    
    @staticmethod
    @property
    def HorizSpaceMakeEqual() -> CommandID: ...
    
    @staticmethod
    @property
    def LineupIcons() -> CommandID: ...
    
    @staticmethod
    @property
    def LockControls() -> CommandID: ...
    
    @staticmethod
    @property
    def MultiLevelRedo() -> CommandID: ...
    
    @staticmethod
    @property
    def MultiLevelUndo() -> CommandID: ...
    
    @staticmethod
    @property
    def Paste() -> CommandID: ...
    
    @staticmethod
    @property
    def Properties() -> CommandID: ...
    
    @staticmethod
    @property
    def PropertiesWindow() -> CommandID: ...
    
    @staticmethod
    @property
    def Redo() -> CommandID: ...
    
    @staticmethod
    @property
    def Replace() -> CommandID: ...
    
    @staticmethod
    @property
    def SelectAll() -> CommandID: ...
    
    @staticmethod
    @property
    def SendBackward() -> CommandID: ...
    
    @staticmethod
    @property
    def SendToBack() -> CommandID: ...
    
    @staticmethod
    @property
    def ShowGrid() -> CommandID: ...
    
    @staticmethod
    @property
    def ShowLargeIcons() -> CommandID: ...
    
    @staticmethod
    @property
    def SizeToControl() -> CommandID: ...
    
    @staticmethod
    @property
    def SizeToControlHeight() -> CommandID: ...
    
    @staticmethod
    @property
    def SizeToControlWidth() -> CommandID: ...
    
    @staticmethod
    @property
    def SizeToFit() -> CommandID: ...
    
    @staticmethod
    @property
    def SizeToGrid() -> CommandID: ...
    
    @staticmethod
    @property
    def SnapToGrid() -> CommandID: ...
    
    @staticmethod
    @property
    def TabOrder() -> CommandID: ...
    
    @staticmethod
    @property
    def Undo() -> CommandID: ...
    
    @staticmethod
    @property
    def Ungroup() -> CommandID: ...
    
    @staticmethod
    @property
    def VerbFirst() -> CommandID: ...
    
    @staticmethod
    @property
    def VerbLast() -> CommandID: ...
    
    @staticmethod
    @property
    def VertSpaceConcatenate() -> CommandID: ...
    
    @staticmethod
    @property
    def VertSpaceDecrease() -> CommandID: ...
    
    @staticmethod
    @property
    def VertSpaceIncrease() -> CommandID: ...
    
    @staticmethod
    @property
    def VertSpaceMakeEqual() -> CommandID: ...
    
    @staticmethod
    @property
    def ViewCode() -> CommandID: ...
    
    @staticmethod
    @property
    def ViewGrid() -> CommandID: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StandardToolWindows(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def ObjectBrowser() -> Guid: ...
    
    @staticmethod
    @property
    def OutputWindow() -> Guid: ...
    
    @staticmethod
    @property
    def ProjectExplorer() -> Guid: ...
    
    @staticmethod
    @property
    def PropertyBrowser() -> Guid: ...
    
    @staticmethod
    @property
    def RelatedLinks() -> Guid: ...
    
    @staticmethod
    @property
    def ServerExplorer() -> Guid: ...
    
    @staticmethod
    @property
    def TaskList() -> Guid: ...
    
    @staticmethod
    @property
    def Toolbox() -> Guid: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeDescriptionProviderService(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def GetProvider(self, instance: ObjectType) -> TypeDescriptionProvider: ...
    
    @overload
    def GetProvider(self, type: TypeType) -> TypeDescriptionProvider: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# ---------- Interfaces ---------- #

class IComponentChangeService(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def OnComponentChanged(self, component: ObjectType, member: MemberDescriptor, oldValue: ObjectType, newValue: ObjectType) -> VoidType: ...
    
    def OnComponentChanging(self, component: ObjectType, member: MemberDescriptor) -> VoidType: ...
    
    def add_ComponentAdded(self, value: ComponentEventHandler) -> VoidType: ...
    
    def add_ComponentAdding(self, value: ComponentEventHandler) -> VoidType: ...
    
    def add_ComponentChanged(self, value: ComponentChangedEventHandler) -> VoidType: ...
    
    def add_ComponentChanging(self, value: ComponentChangingEventHandler) -> VoidType: ...
    
    def add_ComponentRemoved(self, value: ComponentEventHandler) -> VoidType: ...
    
    def add_ComponentRemoving(self, value: ComponentEventHandler) -> VoidType: ...
    
    def add_ComponentRename(self, value: ComponentRenameEventHandler) -> VoidType: ...
    
    def remove_ComponentAdded(self, value: ComponentEventHandler) -> VoidType: ...
    
    def remove_ComponentAdding(self, value: ComponentEventHandler) -> VoidType: ...
    
    def remove_ComponentChanged(self, value: ComponentChangedEventHandler) -> VoidType: ...
    
    def remove_ComponentChanging(self, value: ComponentChangingEventHandler) -> VoidType: ...
    
    def remove_ComponentRemoved(self, value: ComponentEventHandler) -> VoidType: ...
    
    def remove_ComponentRemoving(self, value: ComponentEventHandler) -> VoidType: ...
    
    def remove_ComponentRename(self, value: ComponentRenameEventHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    ComponentAdded: EventType[ComponentEventHandler] = ...
    
    ComponentAdding: EventType[ComponentEventHandler] = ...
    
    ComponentChanged: EventType[ComponentChangedEventHandler] = ...
    
    ComponentChanging: EventType[ComponentChangingEventHandler] = ...
    
    ComponentRemoved: EventType[ComponentEventHandler] = ...
    
    ComponentRemoving: EventType[ComponentEventHandler] = ...
    
    ComponentRename: EventType[ComponentRenameEventHandler] = ...


class IComponentDiscoveryService(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetComponentTypes(self, designerHost: IDesignerHost, baseType: TypeType) -> ICollection: ...
    
    # No Events


class IComponentInitializer(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def InitializeExistingComponent(self, defaultValues: IDictionary) -> VoidType: ...
    
    def InitializeNewComponent(self, defaultValues: IDictionary) -> VoidType: ...
    
    # No Events


class IDesigner(Protocol, IDisposable):
    # ---------- Properties ---------- #
    
    @property
    def Component(self) -> IComponent: ...
    
    @property
    def Verbs(self) -> DesignerVerbCollection: ...
    
    # ---------- Methods ---------- #
    
    def DoDefaultAction(self) -> VoidType: ...
    
    def Initialize(self, component: IComponent) -> VoidType: ...
    
    def get_Component(self) -> IComponent: ...
    
    def get_Verbs(self) -> DesignerVerbCollection: ...
    
    # No Events


class IDesignerEventService(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def ActiveDesigner(self) -> IDesignerHost: ...
    
    @property
    def Designers(self) -> DesignerCollection: ...
    
    # ---------- Methods ---------- #
    
    def add_ActiveDesignerChanged(self, value: ActiveDesignerEventHandler) -> VoidType: ...
    
    def add_DesignerCreated(self, value: DesignerEventHandler) -> VoidType: ...
    
    def add_DesignerDisposed(self, value: DesignerEventHandler) -> VoidType: ...
    
    def add_SelectionChanged(self, value: EventHandler) -> VoidType: ...
    
    def get_ActiveDesigner(self) -> IDesignerHost: ...
    
    def get_Designers(self) -> DesignerCollection: ...
    
    def remove_ActiveDesignerChanged(self, value: ActiveDesignerEventHandler) -> VoidType: ...
    
    def remove_DesignerCreated(self, value: DesignerEventHandler) -> VoidType: ...
    
    def remove_DesignerDisposed(self, value: DesignerEventHandler) -> VoidType: ...
    
    def remove_SelectionChanged(self, value: EventHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    ActiveDesignerChanged: EventType[ActiveDesignerEventHandler] = ...
    
    DesignerCreated: EventType[DesignerEventHandler] = ...
    
    DesignerDisposed: EventType[DesignerEventHandler] = ...
    
    SelectionChanged: EventType[EventHandler] = ...


class IDesignerFilter(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def PostFilterAttributes(self, attributes: IDictionary) -> VoidType: ...
    
    def PostFilterEvents(self, events: IDictionary) -> VoidType: ...
    
    def PostFilterProperties(self, properties: IDictionary) -> VoidType: ...
    
    def PreFilterAttributes(self, attributes: IDictionary) -> VoidType: ...
    
    def PreFilterEvents(self, events: IDictionary) -> VoidType: ...
    
    def PreFilterProperties(self, properties: IDictionary) -> VoidType: ...
    
    # No Events


class IDesignerHost(Protocol, IServiceContainer, IServiceProvider):
    # ---------- Properties ---------- #
    
    @property
    def Container(self) -> IContainer: ...
    
    @property
    def InTransaction(self) -> BooleanType: ...
    
    @property
    def Loading(self) -> BooleanType: ...
    
    @property
    def RootComponent(self) -> IComponent: ...
    
    @property
    def RootComponentClassName(self) -> StringType: ...
    
    @property
    def TransactionDescription(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Activate(self) -> VoidType: ...
    
    @overload
    def CreateComponent(self, componentClass: TypeType) -> IComponent: ...
    
    @overload
    def CreateComponent(self, componentClass: TypeType, name: StringType) -> IComponent: ...
    
    @overload
    def CreateTransaction(self) -> DesignerTransaction: ...
    
    @overload
    def CreateTransaction(self, description: StringType) -> DesignerTransaction: ...
    
    def DestroyComponent(self, component: IComponent) -> VoidType: ...
    
    def GetDesigner(self, component: IComponent) -> IDesigner: ...
    
    def GetType(self, typeName: StringType) -> TypeType: ...
    
    def add_Activated(self, value: EventHandler) -> VoidType: ...
    
    def add_Deactivated(self, value: EventHandler) -> VoidType: ...
    
    def add_LoadComplete(self, value: EventHandler) -> VoidType: ...
    
    def add_TransactionClosed(self, value: DesignerTransactionCloseEventHandler) -> VoidType: ...
    
    def add_TransactionClosing(self, value: DesignerTransactionCloseEventHandler) -> VoidType: ...
    
    def add_TransactionOpened(self, value: EventHandler) -> VoidType: ...
    
    def add_TransactionOpening(self, value: EventHandler) -> VoidType: ...
    
    def get_Container(self) -> IContainer: ...
    
    def get_InTransaction(self) -> BooleanType: ...
    
    def get_Loading(self) -> BooleanType: ...
    
    def get_RootComponent(self) -> IComponent: ...
    
    def get_RootComponentClassName(self) -> StringType: ...
    
    def get_TransactionDescription(self) -> StringType: ...
    
    def remove_Activated(self, value: EventHandler) -> VoidType: ...
    
    def remove_Deactivated(self, value: EventHandler) -> VoidType: ...
    
    def remove_LoadComplete(self, value: EventHandler) -> VoidType: ...
    
    def remove_TransactionClosed(self, value: DesignerTransactionCloseEventHandler) -> VoidType: ...
    
    def remove_TransactionClosing(self, value: DesignerTransactionCloseEventHandler) -> VoidType: ...
    
    def remove_TransactionOpened(self, value: EventHandler) -> VoidType: ...
    
    def remove_TransactionOpening(self, value: EventHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    Activated: EventType[EventHandler] = ...
    
    Deactivated: EventType[EventHandler] = ...
    
    LoadComplete: EventType[EventHandler] = ...
    
    TransactionClosed: EventType[DesignerTransactionCloseEventHandler] = ...
    
    TransactionClosing: EventType[DesignerTransactionCloseEventHandler] = ...
    
    TransactionOpened: EventType[EventHandler] = ...
    
    TransactionOpening: EventType[EventHandler] = ...


class IDesignerHostTransactionState(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def IsClosingTransaction(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_IsClosingTransaction(self) -> BooleanType: ...
    
    # No Events


class IDesignerOptionService(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetOptionValue(self, pageName: StringType, valueName: StringType) -> ObjectType: ...
    
    def SetOptionValue(self, pageName: StringType, valueName: StringType, value: ObjectType) -> VoidType: ...
    
    # No Events


class IDictionaryService(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetKey(self, value: ObjectType) -> ObjectType: ...
    
    def GetValue(self, key: ObjectType) -> ObjectType: ...
    
    def SetValue(self, key: ObjectType, value: ObjectType) -> VoidType: ...
    
    # No Events


class IEventBindingService(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CreateUniqueMethodName(self, component: IComponent, e: EventDescriptor) -> StringType: ...
    
    def GetCompatibleMethods(self, e: EventDescriptor) -> ICollection: ...
    
    def GetEvent(self, property: PropertyDescriptor) -> EventDescriptor: ...
    
    def GetEventProperties(self, events: EventDescriptorCollection) -> PropertyDescriptorCollection: ...
    
    def GetEventProperty(self, e: EventDescriptor) -> PropertyDescriptor: ...
    
    @overload
    def ShowCode(self) -> BooleanType: ...
    
    @overload
    def ShowCode(self, lineNumber: IntType) -> BooleanType: ...
    
    @overload
    def ShowCode(self, component: IComponent, e: EventDescriptor) -> BooleanType: ...
    
    # No Events


class IExtenderListService(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetExtenderProviders(self) -> ArrayType[IExtenderProvider]: ...
    
    # No Events


class IExtenderProviderService(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AddExtenderProvider(self, provider: IExtenderProvider) -> VoidType: ...
    
    def RemoveExtenderProvider(self, provider: IExtenderProvider) -> VoidType: ...
    
    # No Events


class IHelpService(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AddContextAttribute(self, name: StringType, value: StringType, keywordType: HelpKeywordType) -> VoidType: ...
    
    def ClearContextAttributes(self) -> VoidType: ...
    
    def CreateLocalContext(self, contextType: HelpContextType) -> IHelpService: ...
    
    def RemoveContextAttribute(self, name: StringType, value: StringType) -> VoidType: ...
    
    def RemoveLocalContext(self, localContext: IHelpService) -> VoidType: ...
    
    def ShowHelpFromKeyword(self, helpKeyword: StringType) -> VoidType: ...
    
    def ShowHelpFromUrl(self, helpUrl: StringType) -> VoidType: ...
    
    # No Events


class IInheritanceService(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AddInheritedComponents(self, component: IComponent, container: IContainer) -> VoidType: ...
    
    def GetInheritanceAttribute(self, component: IComponent) -> InheritanceAttribute: ...
    
    # No Events


class IMenuCommandService(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Verbs(self) -> DesignerVerbCollection: ...
    
    # ---------- Methods ---------- #
    
    def AddCommand(self, command: MenuCommand) -> VoidType: ...
    
    def AddVerb(self, verb: DesignerVerb) -> VoidType: ...
    
    def FindCommand(self, commandID: CommandID) -> MenuCommand: ...
    
    def GlobalInvoke(self, commandID: CommandID) -> BooleanType: ...
    
    def RemoveCommand(self, command: MenuCommand) -> VoidType: ...
    
    def RemoveVerb(self, verb: DesignerVerb) -> VoidType: ...
    
    def ShowContextMenu(self, menuID: CommandID, x: IntType, y: IntType) -> VoidType: ...
    
    def get_Verbs(self) -> DesignerVerbCollection: ...
    
    # No Events


class IReferenceService(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetComponent(self, reference: ObjectType) -> IComponent: ...
    
    def GetName(self, reference: ObjectType) -> StringType: ...
    
    def GetReference(self, name: StringType) -> ObjectType: ...
    
    @overload
    def GetReferences(self) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetReferences(self, baseType: TypeType) -> ArrayType[ObjectType]: ...
    
    # No Events


class IResourceService(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetResourceReader(self, info: CultureInfo) -> IResourceReader: ...
    
    def GetResourceWriter(self, info: CultureInfo) -> IResourceWriter: ...
    
    # No Events


class IRootDesigner(Protocol, IDesigner, IDisposable):
    # ---------- Properties ---------- #
    
    @property
    def SupportedTechnologies(self) -> ArrayType[ViewTechnology]: ...
    
    # ---------- Methods ---------- #
    
    def GetView(self, technology: ViewTechnology) -> ObjectType: ...
    
    def get_SupportedTechnologies(self) -> ArrayType[ViewTechnology]: ...
    
    # No Events


class ISelectionService(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def PrimarySelection(self) -> ObjectType: ...
    
    @property
    def SelectionCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetComponentSelected(self, component: ObjectType) -> BooleanType: ...
    
    def GetSelectedComponents(self) -> ICollection: ...
    
    @overload
    def SetSelectedComponents(self, components: ICollection) -> VoidType: ...
    
    @overload
    def SetSelectedComponents(self, components: ICollection, selectionType: SelectionTypes) -> VoidType: ...
    
    def add_SelectionChanged(self, value: EventHandler) -> VoidType: ...
    
    def add_SelectionChanging(self, value: EventHandler) -> VoidType: ...
    
    def get_PrimarySelection(self) -> ObjectType: ...
    
    def get_SelectionCount(self) -> IntType: ...
    
    def remove_SelectionChanged(self, value: EventHandler) -> VoidType: ...
    
    def remove_SelectionChanging(self, value: EventHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    SelectionChanged: EventType[EventHandler] = ...
    
    SelectionChanging: EventType[EventHandler] = ...


class IServiceContainer(Protocol, IServiceProvider):
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def AddService(self, serviceType: TypeType, serviceInstance: ObjectType) -> VoidType: ...
    
    @overload
    def AddService(self, serviceType: TypeType, serviceInstance: ObjectType, promote: BooleanType) -> VoidType: ...
    
    @overload
    def AddService(self, serviceType: TypeType, callback: ServiceCreatorCallback) -> VoidType: ...
    
    @overload
    def AddService(self, serviceType: TypeType, callback: ServiceCreatorCallback, promote: BooleanType) -> VoidType: ...
    
    @overload
    def RemoveService(self, serviceType: TypeType) -> VoidType: ...
    
    @overload
    def RemoveService(self, serviceType: TypeType, promote: BooleanType) -> VoidType: ...
    
    # No Events


class ITreeDesigner(Protocol, IDesigner, IDisposable):
    # ---------- Properties ---------- #
    
    @property
    def Children(self) -> ICollection: ...
    
    @property
    def Parent(self) -> IDesigner: ...
    
    # ---------- Methods ---------- #
    
    def get_Children(self) -> ICollection: ...
    
    def get_Parent(self) -> IDesigner: ...
    
    # No Events


class ITypeDescriptorFilterService(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def FilterAttributes(self, component: IComponent, attributes: IDictionary) -> BooleanType: ...
    
    def FilterEvents(self, component: IComponent, events: IDictionary) -> BooleanType: ...
    
    def FilterProperties(self, component: IComponent, properties: IDictionary) -> BooleanType: ...
    
    # No Events


class ITypeDiscoveryService(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetTypes(self, baseType: TypeType, excludeGlobalTypes: BooleanType) -> ICollection: ...
    
    # No Events


class ITypeResolutionService(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def GetAssembly(self, name: AssemblyName) -> Assembly: ...
    
    @overload
    def GetAssembly(self, name: AssemblyName, throwOnError: BooleanType) -> Assembly: ...
    
    def GetPathOfAssembly(self, name: AssemblyName) -> StringType: ...
    
    @overload
    def GetType(self, name: StringType) -> TypeType: ...
    
    @overload
    def GetType(self, name: StringType, throwOnError: BooleanType) -> TypeType: ...
    
    @overload
    def GetType(self, name: StringType, throwOnError: BooleanType, ignoreCase: BooleanType) -> TypeType: ...
    
    def ReferenceAssembly(self, name: AssemblyName) -> VoidType: ...
    
    # No Events


# ---------- Enums ---------- #

class HelpContextType(Enum):
    Ambient = 0
    Window = 1
    Selection = 2
    ToolWindowSelection = 3


class HelpKeywordType(Enum):
    F1Keyword = 0
    GeneralKeyword = 1
    FilterKeyword = 2


class SelectionTypes(Enum):
    Auto = 1
    Normal = 1
    Replace = 2
    MouseDown = 4
    MouseUp = 8
    Click = 16
    Primary = 16
    Valid = 31
    Toggle = 32
    Add = 64
    Remove = 128


class ViewTechnology(Enum):
    Passthrough = 0
    WindowsForms = 1
    Default = 2


# ---------- Delegates ---------- #

ActiveDesignerEventHandler = Callable[[ObjectType, ActiveDesignerEventArgs], VoidType]

ComponentChangedEventHandler = Callable[[ObjectType, ComponentChangedEventArgs], VoidType]

ComponentChangingEventHandler = Callable[[ObjectType, ComponentChangingEventArgs], VoidType]

ComponentEventHandler = Callable[[ObjectType, ComponentEventArgs], VoidType]

ComponentRenameEventHandler = Callable[[ObjectType, ComponentRenameEventArgs], VoidType]

DesignerEventHandler = Callable[[ObjectType, DesignerEventArgs], VoidType]

DesignerTransactionCloseEventHandler = Callable[[ObjectType, DesignerTransactionCloseEventArgs], VoidType]

ServiceCreatorCallback = Callable[[IServiceContainer, TypeType], ObjectType]

__all__ = [
    ActiveDesignerEventArgs,
    ActiveDesignerEventHandler,
    CheckoutException,
    CommandID,
    ComponentChangedEventArgs,
    ComponentChangedEventHandler,
    ComponentChangingEventArgs,
    ComponentChangingEventHandler,
    ComponentEventArgs,
    ComponentEventHandler,
    ComponentRenameEventArgs,
    ComponentRenameEventHandler,
    DesignerCollection,
    DesignerEventArgs,
    DesignerEventHandler,
    DesignerOptionService,
    DesignerTransaction,
    DesignerTransactionCloseEventArgs,
    DesignerTransactionCloseEventHandler,
    DesignerVerb,
    DesignerVerbCollection,
    DesigntimeLicenseContext,
    DesigntimeLicenseContextSerializer,
    HelpKeywordAttribute,
    MenuCommand,
    RuntimeLicenseContext,
    ServiceContainer,
    ServiceCreatorCallback,
    StandardCommands,
    StandardToolWindows,
    TypeDescriptionProviderService,
    IComponentChangeService,
    IComponentDiscoveryService,
    IComponentInitializer,
    IDesigner,
    IDesignerEventService,
    IDesignerFilter,
    IDesignerHost,
    IDesignerHostTransactionState,
    IDesignerOptionService,
    IDictionaryService,
    IEventBindingService,
    IExtenderListService,
    IExtenderProviderService,
    IHelpService,
    IInheritanceService,
    IMenuCommandService,
    IReferenceService,
    IResourceService,
    IRootDesigner,
    ISelectionService,
    IServiceContainer,
    ITreeDesigner,
    ITypeDescriptorFilterService,
    ITypeDiscoveryService,
    ITypeResolutionService,
    HelpContextType,
    HelpKeywordType,
    SelectionTypes,
    ViewTechnology,
    ActiveDesignerEventHandler,
    ComponentChangedEventHandler,
    ComponentChangingEventHandler,
    ComponentEventHandler,
    ComponentRenameEventHandler,
    DesignerEventHandler,
    DesignerTransactionCloseEventHandler,
    ServiceCreatorCallback,
]
