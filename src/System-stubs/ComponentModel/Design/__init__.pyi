"""Automatically generated stubs for C# namespace: System.ComponentModel.Design."""

from abc import ABC
from collections.abc import Callable
from collections.abc import Iterator
from typing import ClassVar
from typing import Self
from typing import overload

from System import Array
from System import Attribute
from System import Enum
from System import EventArgs
from System import EventHandler
from System import Exception
from System import Guid
from System import IDisposable
from System import IntPtr
from System import IServiceProvider
from System import Object
from System import Type
from System import UInt32
from System.Collections import CollectionBase
from System.Collections import ICollection
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IList
from System.ComponentModel import EventDescriptor
from System.ComponentModel import EventDescriptorCollection
from System.ComponentModel import IComponent
from System.ComponentModel import IContainer
from System.ComponentModel import IExtenderProvider
from System.ComponentModel import InheritanceAttribute
from System.ComponentModel import LicenseContext
from System.ComponentModel import LicenseUsageMode
from System.ComponentModel import MemberDescriptor
from System.ComponentModel import PropertyDescriptor
from System.ComponentModel import PropertyDescriptorCollection
from System.ComponentModel import TypeDescriptionProvider
from System.Globalization import CultureInfo
from System.IO import Stream
from System.Reflection import Assembly
from System.Reflection import AssemblyName
from System.Reflection import MethodBase
from System.Resources import IResourceReader
from System.Resources import IResourceWriter
from System.Runtime.InteropServices import ExternalException
from System.Runtime.InteropServices import _Attribute
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

class ActiveDesignerEventArgs(EventArgs):
    """"""
    def __init__(self, oldDesigner: IDesignerHost, newDesigner: IDesignerHost) -> None:
        """"""
    @property
    def NewDesigner(self) -> IDesignerHost:
        """"""
    @property
    def OldDesigner(self) -> IDesignerHost:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

ActiveDesignerEventHandler: Callable[[object, ActiveDesignerEventArgs], None] = ...
""""""

class CheckoutException(ExternalException, _Exception, ISerializable):
    """"""

    Canceled: ClassVar[CheckoutException]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, errorCode: int) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def ErrorCode(self) -> int:
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

class CommandID(Object):
    """"""
    def __init__(self, menuGroup: Guid, commandID: int) -> None:
        """"""
    @property
    def Guid(self) -> Guid:
        """"""
    @property
    def ID(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ComponentChangedEventArgs(EventArgs):
    """"""
    def __init__(
        self, component: object, member: MemberDescriptor, oldValue: object, newValue: object
    ) -> None:
        """"""
    @property
    def Component(self) -> object:
        """"""
    @property
    def Member(self) -> MemberDescriptor:
        """"""
    @property
    def NewValue(self) -> object:
        """"""
    @property
    def OldValue(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

ComponentChangedEventHandler: Callable[[object, ComponentChangedEventArgs], None] = ...
""""""

class ComponentChangingEventArgs(EventArgs):
    """"""
    def __init__(self, component: object, member: MemberDescriptor) -> None:
        """"""
    @property
    def Component(self) -> object:
        """"""
    @property
    def Member(self) -> MemberDescriptor:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

ComponentChangingEventHandler: Callable[[object, ComponentChangingEventArgs], None] = ...
""""""

class ComponentEventArgs(EventArgs):
    """"""
    def __init__(self, component: IComponent) -> None:
        """"""
    @property
    def Component(self) -> IComponent:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

ComponentEventHandler: Callable[[object, ComponentEventArgs], None] = ...
""""""

class ComponentRenameEventArgs(EventArgs):
    """"""
    def __init__(self, component: object, oldName: str, newName: str) -> None:
        """"""
    @property
    def Component(self) -> object:
        """"""
    @property
    def NewName(self) -> str:
        """"""
    @property
    def OldName(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

ComponentRenameEventHandler: Callable[[object, ComponentRenameEventArgs], None] = ...
""""""

class DesignerCollection(Object, ICollection, IEnumerable):
    """"""
    @overload
    def __init__(self, designers: Array[IDesignerHost]) -> None:
        """"""
    @overload
    def __init__(self, designers: IList) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> IDesignerHost:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
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
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> IDesignerHost:
        """"""

class DesignerEventArgs(EventArgs):
    """"""
    def __init__(self, host: IDesignerHost) -> None:
        """"""
    @property
    def Designer(self) -> IDesignerHost:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

DesignerEventHandler: Callable[[object, DesignerEventArgs], None] = ...
""""""

class DesignerOptionService(ABC, Object, IDesignerOptionService):
    """"""
    @property
    def Options(self) -> DesignerOptionService.DesignerOptionCollection:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOptionValue(self, pageName: str, valueName: str) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetOptionValue(self, pageName: str, valueName: str, value: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    class DesignerOptionCollection(Object, ICollection, IEnumerable, IList):
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
        def Item(self) -> DesignerOptionService.DesignerOptionCollection:
            """"""
        @property
        def Name(self) -> str:
            """"""
        @property
        def Parent(self) -> DesignerOptionService.DesignerOptionCollection:
            """"""
        @property
        def Properties(self) -> PropertyDescriptorCollection:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def Add(self, value: object) -> int:
            """"""
        def Clear(self) -> None:
            """"""
        def Contains(self, value: object) -> bool:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        @overload
        def IndexOf(self, value: DesignerOptionService.DesignerOptionCollection) -> int:
            """"""
        @overload
        def IndexOf(self, value: object) -> int:
            """"""
        def Insert(self, index: int, value: object) -> None:
            """"""
        def Remove(self, value: object) -> None:
            """"""
        def RemoveAt(self, index: int) -> None:
            """"""
        def ShowDialog(self) -> bool:
            """"""
        def ToString(self) -> str:
            """"""
        def __contains__(self, value: object) -> bool:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __delitem__(self, value: object) -> None:
            """"""
        def __len__(self) -> int:
            """"""
        @overload
        def __getitem__(self, index: int) -> DesignerOptionService.DesignerOptionCollection:
            """"""
        @overload
        def __getitem__(self, name: str) -> DesignerOptionService.DesignerOptionCollection:
            """"""
        def __setitem__(self, index: int, value: object) -> None:
            """"""

class DesignerTransaction(ABC, Object, IDisposable):
    """"""
    @property
    def Canceled(self) -> bool:
        """"""
    @property
    def Committed(self) -> bool:
        """"""
    @property
    def Description(self) -> str:
        """"""
    def Cancel(self) -> None:
        """"""
    def Commit(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DesignerTransactionCloseEventArgs(EventArgs):
    """"""
    @overload
    def __init__(self, commit: bool) -> None:
        """"""
    @overload
    def __init__(self, commit: bool, lastTransaction: bool) -> None:
        """"""
    @property
    def LastTransaction(self) -> bool:
        """"""
    @property
    def TransactionCommitted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

DesignerTransactionCloseEventHandler: Callable[
    [object, DesignerTransactionCloseEventArgs], None
] = ...
""""""

class DesignerVerb(MenuCommand):
    """"""
    @overload
    def __init__(self, text: str, handler: EventHandler) -> None:
        """"""
    @overload
    def __init__(self, text: str, handler: EventHandler, startCommandID: CommandID) -> None:
        """"""
    @property
    def Checked(self) -> bool:
        """"""
    @Checked.setter
    def Checked(self, value: bool) -> None: ...
    @property
    def CommandID(self) -> CommandID:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @Description.setter
    def Description(self, value: str) -> None: ...
    @property
    def Enabled(self) -> bool:
        """"""
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
    @property
    def OleStatus(self) -> int:
        """"""
    @property
    def Properties(self) -> IDictionary:
        """"""
    @property
    def Supported(self) -> bool:
        """"""
    @Supported.setter
    def Supported(self, value: bool) -> None: ...
    @property
    def Text(self) -> str:
        """"""
    @property
    def Visible(self) -> bool:
        """"""
    @Visible.setter
    def Visible(self, value: bool) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Invoke(self) -> None:
        """"""
    @overload
    def Invoke(self, arg: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    CommandChanged: EventType[EventHandler] = ...
    """"""

class DesignerVerbCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: Array[DesignerVerb]) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
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
    def Item(self) -> DesignerVerb:
        """"""
    @Item.setter
    def Item(self, value: DesignerVerb) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, value: DesignerVerb) -> int:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    @overload
    def AddRange(self, value: DesignerVerbCollection) -> None:
        """"""
    @overload
    def AddRange(self, value: Array[DesignerVerb]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: DesignerVerb) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[DesignerVerb], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, value: DesignerVerb) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, value: DesignerVerb) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, value: DesignerVerb) -> None:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: DesignerVerb) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, value: DesignerVerb) -> None:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> DesignerVerb:
        """"""
    @overload
    def __setitem__(self, index: int, value: DesignerVerb) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

class DesigntimeLicenseContext(LicenseContext, IServiceProvider):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def UsageMode(self) -> LicenseUsageMode:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetSavedLicenseKey(self, type: Type, resourceAssembly: Assembly) -> str:
        """"""
    def GetService(self, type: Type) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetSavedLicenseKey(self, type: Type, key: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class DesigntimeLicenseContextSerializer(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Serialize(cls, o: Stream, cryptoKey: str, context: DesigntimeLicenseContext) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class HelpContextType(Enum):
    """"""

    Ambient: HelpContextType = ...
    """"""
    Window: HelpContextType = ...
    """"""
    Selection: HelpContextType = ...
    """"""
    ToolWindowSelection: HelpContextType = ...
    """"""

class HelpKeywordAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[HelpKeywordAttribute]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, keyword: str) -> None:
        """"""
    @overload
    def __init__(self, t: Type) -> None:
        """"""
    @property
    def HelpKeyword(self) -> str:
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

class HelpKeywordType(Enum):
    """"""

    F1Keyword: HelpKeywordType = ...
    """"""
    GeneralKeyword: HelpKeywordType = ...
    """"""
    FilterKeyword: HelpKeywordType = ...
    """"""

class IComponentChangeService:
    """"""
    def OnComponentChanged(
        self, component: object, member: MemberDescriptor, oldValue: object, newValue: object
    ) -> None:
        """"""
    def OnComponentChanging(self, component: object, member: MemberDescriptor) -> None:
        """"""
    ComponentAdded: EventType[ComponentEventHandler] = ...
    """"""
    ComponentAdding: EventType[ComponentEventHandler] = ...
    """"""
    ComponentChanged: EventType[ComponentChangedEventHandler] = ...
    """"""
    ComponentChanging: EventType[ComponentChangingEventHandler] = ...
    """"""
    ComponentRemoved: EventType[ComponentEventHandler] = ...
    """"""
    ComponentRemoving: EventType[ComponentEventHandler] = ...
    """"""
    ComponentRename: EventType[ComponentRenameEventHandler] = ...
    """"""

class IComponentDiscoveryService:
    """"""
    def GetComponentTypes(self, designerHost: IDesignerHost, baseType: Type) -> ICollection:
        """"""

class IComponentInitializer:
    """"""
    def InitializeExistingComponent(self, defaultValues: IDictionary) -> None:
        """"""
    def InitializeNewComponent(self, defaultValues: IDictionary) -> None:
        """"""

class IDesigner(IDisposable):
    """"""
    @property
    def Component(self) -> IComponent:
        """"""
    @property
    def Verbs(self) -> DesignerVerbCollection:
        """"""
    def Dispose(self) -> None:
        """"""
    def DoDefaultAction(self) -> None:
        """"""
    def Initialize(self, component: IComponent) -> None:
        """"""

class IDesignerEventService:
    """"""
    @property
    def ActiveDesigner(self) -> IDesignerHost:
        """"""
    @property
    def Designers(self) -> DesignerCollection:
        """"""
    ActiveDesignerChanged: EventType[ActiveDesignerEventHandler] = ...
    """"""
    DesignerCreated: EventType[DesignerEventHandler] = ...
    """"""
    DesignerDisposed: EventType[DesignerEventHandler] = ...
    """"""
    SelectionChanged: EventType[EventHandler] = ...
    """"""

class IDesignerFilter:
    """"""
    def PostFilterAttributes(self, attributes: IDictionary) -> None:
        """"""
    def PostFilterEvents(self, events: IDictionary) -> None:
        """"""
    def PostFilterProperties(self, properties: IDictionary) -> None:
        """"""
    def PreFilterAttributes(self, attributes: IDictionary) -> None:
        """"""
    def PreFilterEvents(self, events: IDictionary) -> None:
        """"""
    def PreFilterProperties(self, properties: IDictionary) -> None:
        """"""

class IDesignerHost(IServiceContainer, IServiceProvider):
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
    def GetDesigner(self, component: IComponent) -> IDesigner:
        """"""
    def GetService(self, serviceType: Type) -> object:
        """"""
    def GetType(self, typeName: str) -> Type:
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

class IDesignerHostTransactionState:
    """"""
    @property
    def IsClosingTransaction(self) -> bool:
        """"""

class IDesignerOptionService:
    """"""
    def GetOptionValue(self, pageName: str, valueName: str) -> object:
        """"""
    def SetOptionValue(self, pageName: str, valueName: str, value: object) -> None:
        """"""

class IDictionaryService:
    """"""
    def GetKey(self, value: object) -> object:
        """"""
    def GetValue(self, key: object) -> object:
        """"""
    def SetValue(self, key: object, value: object) -> None:
        """"""

class IEventBindingService:
    """"""
    def CreateUniqueMethodName(self, component: IComponent, e: EventDescriptor) -> str:
        """"""
    def GetCompatibleMethods(self, e: EventDescriptor) -> ICollection:
        """"""
    def GetEvent(self, property: PropertyDescriptor) -> EventDescriptor:
        """"""
    def GetEventProperties(self, events: EventDescriptorCollection) -> PropertyDescriptorCollection:
        """"""
    def GetEventProperty(self, e: EventDescriptor) -> PropertyDescriptor:
        """"""
    @overload
    def ShowCode(self) -> bool:
        """"""
    @overload
    def ShowCode(self, component: IComponent, e: EventDescriptor) -> bool:
        """"""
    @overload
    def ShowCode(self, lineNumber: int) -> bool:
        """"""

class IExtenderListService:
    """"""
    def GetExtenderProviders(self) -> Array[IExtenderProvider]:
        """"""

class IExtenderProviderService:
    """"""
    def AddExtenderProvider(self, provider: IExtenderProvider) -> None:
        """"""
    def RemoveExtenderProvider(self, provider: IExtenderProvider) -> None:
        """"""

class IHelpService:
    """"""
    def AddContextAttribute(self, name: str, value: str, keywordType: HelpKeywordType) -> None:
        """"""
    def ClearContextAttributes(self) -> None:
        """"""
    def CreateLocalContext(self, contextType: HelpContextType) -> IHelpService:
        """"""
    def RemoveContextAttribute(self, name: str, value: str) -> None:
        """"""
    def RemoveLocalContext(self, localContext: IHelpService) -> None:
        """"""
    def ShowHelpFromKeyword(self, helpKeyword: str) -> None:
        """"""
    def ShowHelpFromUrl(self, helpUrl: str) -> None:
        """"""

class IInheritanceService:
    """"""
    def AddInheritedComponents(self, component: IComponent, container: IContainer) -> None:
        """"""
    def GetInheritanceAttribute(self, component: IComponent) -> InheritanceAttribute:
        """"""

class IMenuCommandService:
    """"""
    @property
    def Verbs(self) -> DesignerVerbCollection:
        """"""
    def AddCommand(self, command: MenuCommand) -> None:
        """"""
    def AddVerb(self, verb: DesignerVerb) -> None:
        """"""
    def FindCommand(self, commandID: CommandID) -> MenuCommand:
        """"""
    def GlobalInvoke(self, commandID: CommandID) -> bool:
        """"""
    def RemoveCommand(self, command: MenuCommand) -> None:
        """"""
    def RemoveVerb(self, verb: DesignerVerb) -> None:
        """"""
    def ShowContextMenu(self, menuID: CommandID, x: int, y: int) -> None:
        """"""

class IReferenceService:
    """"""
    def GetComponent(self, reference: object) -> IComponent:
        """"""
    def GetName(self, reference: object) -> str:
        """"""
    def GetReference(self, name: str) -> object:
        """"""
    @overload
    def GetReferences(self) -> Array[object]:
        """"""
    @overload
    def GetReferences(self, baseType: Type) -> Array[object]:
        """"""

class IResourceService:
    """"""
    def GetResourceReader(self, info: CultureInfo) -> IResourceReader:
        """"""
    def GetResourceWriter(self, info: CultureInfo) -> IResourceWriter:
        """"""

class IRootDesigner(IDesigner, IDisposable):
    """"""
    @property
    def Component(self) -> IComponent:
        """"""
    @property
    def SupportedTechnologies(self) -> Array[ViewTechnology]:
        """"""
    @property
    def Verbs(self) -> DesignerVerbCollection:
        """"""
    def Dispose(self) -> None:
        """"""
    def DoDefaultAction(self) -> None:
        """"""
    def GetView(self, technology: ViewTechnology) -> object:
        """"""
    def Initialize(self, component: IComponent) -> None:
        """"""

class ISelectionService:
    """"""
    @property
    def PrimarySelection(self) -> object:
        """"""
    @property
    def SelectionCount(self) -> int:
        """"""
    def GetComponentSelected(self, component: object) -> bool:
        """"""
    def GetSelectedComponents(self) -> ICollection:
        """"""
    @overload
    def SetSelectedComponents(self, components: ICollection) -> None:
        """"""
    @overload
    def SetSelectedComponents(self, components: ICollection, selectionType: SelectionTypes) -> None:
        """"""
    SelectionChanged: EventType[EventHandler] = ...
    """"""
    SelectionChanging: EventType[EventHandler] = ...
    """"""

class IServiceContainer(IServiceProvider):
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
    def GetService(self, serviceType: Type) -> object:
        """"""
    @overload
    def RemoveService(self, serviceType: Type) -> None:
        """"""
    @overload
    def RemoveService(self, serviceType: Type, promote: bool) -> None:
        """"""

class ITreeDesigner(IDesigner, IDisposable):
    """"""
    @property
    def Children(self) -> ICollection:
        """"""
    @property
    def Component(self) -> IComponent:
        """"""
    @property
    def Parent(self) -> IDesigner:
        """"""
    @property
    def Verbs(self) -> DesignerVerbCollection:
        """"""
    def Dispose(self) -> None:
        """"""
    def DoDefaultAction(self) -> None:
        """"""
    def Initialize(self, component: IComponent) -> None:
        """"""

class ITypeDescriptorFilterService:
    """"""
    def FilterAttributes(self, component: IComponent, attributes: IDictionary) -> bool:
        """"""
    def FilterEvents(self, component: IComponent, events: IDictionary) -> bool:
        """"""
    def FilterProperties(self, component: IComponent, properties: IDictionary) -> bool:
        """"""

class ITypeDiscoveryService:
    """"""
    def GetTypes(self, baseType: Type, excludeGlobalTypes: bool) -> ICollection:
        """"""

class ITypeResolutionService:
    """"""
    @overload
    def GetAssembly(self, name: AssemblyName) -> Assembly:
        """"""
    @overload
    def GetAssembly(self, name: AssemblyName, throwOnError: bool) -> Assembly:
        """"""
    def GetPathOfAssembly(self, name: AssemblyName) -> str:
        """"""
    @overload
    def GetType(self, name: str) -> Type:
        """"""
    @overload
    def GetType(self, name: str, throwOnError: bool) -> Type:
        """"""
    @overload
    def GetType(self, name: str, throwOnError: bool, ignoreCase: bool) -> Type:
        """"""
    def ReferenceAssembly(self, name: AssemblyName) -> None:
        """"""

class MenuCommand(Object):
    """"""
    def __init__(self, handler: EventHandler, command: CommandID) -> None:
        """"""
    @property
    def Checked(self) -> bool:
        """"""
    @Checked.setter
    def Checked(self, value: bool) -> None: ...
    @property
    def CommandID(self) -> CommandID:
        """"""
    @property
    def Enabled(self) -> bool:
        """"""
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
    @property
    def OleStatus(self) -> int:
        """"""
    @property
    def Properties(self) -> IDictionary:
        """"""
    @property
    def Supported(self) -> bool:
        """"""
    @Supported.setter
    def Supported(self, value: bool) -> None: ...
    @property
    def Visible(self) -> bool:
        """"""
    @Visible.setter
    def Visible(self, value: bool) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Invoke(self) -> None:
        """"""
    @overload
    def Invoke(self, arg: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    CommandChanged: EventType[EventHandler] = ...
    """"""

class RuntimeLicenseContext(LicenseContext, IServiceProvider):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def UsageMode(self) -> LicenseUsageMode:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetSavedLicenseKey(self, type: Type, resourceAssembly: Assembly) -> str:
        """"""
    def GetService(self, type: Type) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetSavedLicenseKey(self, type: Type, key: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SelectionTypes(Enum):
    """"""

    Auto: SelectionTypes = ...
    """"""
    Normal: SelectionTypes = ...
    """"""
    Replace: SelectionTypes = ...
    """"""
    MouseDown: SelectionTypes = ...
    """"""
    MouseUp: SelectionTypes = ...
    """"""
    Click: SelectionTypes = ...
    """"""
    Primary: SelectionTypes = ...
    """"""
    Valid: SelectionTypes = ...
    """"""
    Toggle: SelectionTypes = ...
    """"""
    Add: SelectionTypes = ...
    """"""
    Remove: SelectionTypes = ...
    """"""

class ServiceContainer(Object, IServiceContainer, IDisposable, IServiceProvider):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, parentProvider: IServiceProvider) -> None:
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
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetService(self, serviceType: Type) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def RemoveService(self, serviceType: Type) -> None:
        """"""
    @overload
    def RemoveService(self, serviceType: Type, promote: bool) -> None:
        """"""
    def ToString(self) -> str:
        """"""

ServiceCreatorCallback: Callable[[IServiceContainer, Type], object] = ...
""""""

class StandardCommands(Object):
    """"""

    AlignBottom: ClassVar[CommandID]
    """"""
    AlignHorizontalCenters: ClassVar[CommandID]
    """"""
    AlignLeft: ClassVar[CommandID]
    """"""
    AlignRight: ClassVar[CommandID]
    """"""
    AlignToGrid: ClassVar[CommandID]
    """"""
    AlignTop: ClassVar[CommandID]
    """"""
    AlignVerticalCenters: ClassVar[CommandID]
    """"""
    ArrangeBottom: ClassVar[CommandID]
    """"""
    ArrangeIcons: ClassVar[CommandID]
    """"""
    ArrangeRight: ClassVar[CommandID]
    """"""
    BringForward: ClassVar[CommandID]
    """"""
    BringToFront: ClassVar[CommandID]
    """"""
    CenterHorizontally: ClassVar[CommandID]
    """"""
    CenterVertically: ClassVar[CommandID]
    """"""
    Copy: ClassVar[CommandID]
    """"""
    Cut: ClassVar[CommandID]
    """"""
    Delete: ClassVar[CommandID]
    """"""
    DocumentOutline: ClassVar[CommandID]
    """"""
    F1Help: ClassVar[CommandID]
    """"""
    Group: ClassVar[CommandID]
    """"""
    HorizSpaceConcatenate: ClassVar[CommandID]
    """"""
    HorizSpaceDecrease: ClassVar[CommandID]
    """"""
    HorizSpaceIncrease: ClassVar[CommandID]
    """"""
    HorizSpaceMakeEqual: ClassVar[CommandID]
    """"""
    LineupIcons: ClassVar[CommandID]
    """"""
    LockControls: ClassVar[CommandID]
    """"""
    MultiLevelRedo: ClassVar[CommandID]
    """"""
    MultiLevelUndo: ClassVar[CommandID]
    """"""
    Paste: ClassVar[CommandID]
    """"""
    Properties: ClassVar[CommandID]
    """"""
    PropertiesWindow: ClassVar[CommandID]
    """"""
    Redo: ClassVar[CommandID]
    """"""
    Replace: ClassVar[CommandID]
    """"""
    SelectAll: ClassVar[CommandID]
    """"""
    SendBackward: ClassVar[CommandID]
    """"""
    SendToBack: ClassVar[CommandID]
    """"""
    ShowGrid: ClassVar[CommandID]
    """"""
    ShowLargeIcons: ClassVar[CommandID]
    """"""
    SizeToControl: ClassVar[CommandID]
    """"""
    SizeToControlHeight: ClassVar[CommandID]
    """"""
    SizeToControlWidth: ClassVar[CommandID]
    """"""
    SizeToFit: ClassVar[CommandID]
    """"""
    SizeToGrid: ClassVar[CommandID]
    """"""
    SnapToGrid: ClassVar[CommandID]
    """"""
    TabOrder: ClassVar[CommandID]
    """"""
    Undo: ClassVar[CommandID]
    """"""
    Ungroup: ClassVar[CommandID]
    """"""
    VerbFirst: ClassVar[CommandID]
    """"""
    VerbLast: ClassVar[CommandID]
    """"""
    VertSpaceConcatenate: ClassVar[CommandID]
    """"""
    VertSpaceDecrease: ClassVar[CommandID]
    """"""
    VertSpaceIncrease: ClassVar[CommandID]
    """"""
    VertSpaceMakeEqual: ClassVar[CommandID]
    """"""
    ViewCode: ClassVar[CommandID]
    """"""
    ViewGrid: ClassVar[CommandID]
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

class StandardToolWindows(Object):
    """"""

    ObjectBrowser: ClassVar[Guid]
    """"""
    OutputWindow: ClassVar[Guid]
    """"""
    ProjectExplorer: ClassVar[Guid]
    """"""
    PropertyBrowser: ClassVar[Guid]
    """"""
    RelatedLinks: ClassVar[Guid]
    """"""
    ServerExplorer: ClassVar[Guid]
    """"""
    TaskList: ClassVar[Guid]
    """"""
    Toolbox: ClassVar[Guid]
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

class TypeDescriptionProviderService(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProvider(self, instance: object) -> TypeDescriptionProvider:
        """"""
    @overload
    def GetProvider(self, type: Type) -> TypeDescriptionProvider:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ViewTechnology(Enum):
    """"""

    Passthrough: ViewTechnology = ...
    """"""
    WindowsForms: ViewTechnology = ...
    """"""
    Default: ViewTechnology = ...
    """"""
