from __future__ import annotations

from abc import ABC
from typing import Callable, Protocol, Union

from System import AsyncCallback, Boolean, EventHandler, IAsyncResult, ICloneable, Int32, IntPtr, MulticastDelegate, Object, String, Void
from System.Collections import IList
from System.Collections.Specialized import NotifyCollectionChangedAction, NotifyCollectionChangedEventArgs, NotifyCollectionChangedEventHandler
from System.ComponentModel import PropertyChangedEventArgs, PropertyChangedEventHandler
from System.Runtime.InteropServices.WindowsRuntime import EventRegistrationToken
from System.Runtime.Serialization import ISerializable

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class ICommandAdapterHelpers(ABC, ObjectType):
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


class ICommandToManagedAdapter(ObjectType):
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


class ICommandToWinRTAdapter(ObjectType):
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


class NotifyCollectionChangedEventArgsMarshaler(ABC, ObjectType):
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


class NotifyCollectionChangedEventHandler_WinRT(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: NotifyCollectionChangedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: NotifyCollectionChangedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NotifyCollectionChangedToManagedAdapter(ObjectType):
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


class NotifyCollectionChangedToWinRTAdapter(ObjectType):
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


class NotifyPropertyChangedToManagedAdapter(ObjectType):
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


class NotifyPropertyChangedToWinRTAdapter(ObjectType):
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


class PropertyChangedEventArgsMarshaler(ABC, ObjectType):
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


class PropertyChangedEventHandler_WinRT(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: PropertyChangedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: PropertyChangedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# ---------- Interfaces ---------- #

class ICommand_WinRT(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CanExecute(self, parameter: ObjectType) -> BooleanType: ...
    
    def Execute(self, parameter: ObjectType) -> VoidType: ...
    
    def add_CanExecuteChanged(self, value: EventHandler[ObjectType]) -> EventRegistrationToken: ...
    
    def remove_CanExecuteChanged(self, token: EventRegistrationToken) -> VoidType: ...
    
    # No Events


class INotifyCollectionChangedEventArgs(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Action(self) -> NotifyCollectionChangedAction: ...
    
    @property
    def NewItems(self) -> IList: ...
    
    @property
    def NewStartingIndex(self) -> IntType: ...
    
    @property
    def OldItems(self) -> IList: ...
    
    @property
    def OldStartingIndex(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_Action(self) -> NotifyCollectionChangedAction: ...
    
    def get_NewItems(self) -> IList: ...
    
    def get_NewStartingIndex(self) -> IntType: ...
    
    def get_OldItems(self) -> IList: ...
    
    def get_OldStartingIndex(self) -> IntType: ...
    
    # No Events


class INotifyCollectionChanged_WinRT(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def add_CollectionChanged(self, value: NotifyCollectionChangedEventHandler) -> EventRegistrationToken: ...
    
    def remove_CollectionChanged(self, token: EventRegistrationToken) -> VoidType: ...
    
    # No Events


class INotifyPropertyChanged_WinRT(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def add_PropertyChanged(self, value: PropertyChangedEventHandler) -> EventRegistrationToken: ...
    
    def remove_PropertyChanged(self, token: EventRegistrationToken) -> VoidType: ...
    
    # No Events


class IPropertyChangedEventArgs(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def PropertyName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_PropertyName(self) -> StringType: ...
    
    # No Events


# No Enums

# ---------- Delegates ---------- #

NotifyCollectionChangedEventHandler_WinRT = Callable[[ObjectType, NotifyCollectionChangedEventArgs], VoidType]

PropertyChangedEventHandler_WinRT = Callable[[ObjectType, PropertyChangedEventArgs], VoidType]

__all__ = [
    ICommandAdapterHelpers,
    ICommandToManagedAdapter,
    ICommandToWinRTAdapter,
    NotifyCollectionChangedEventArgsMarshaler,
    NotifyCollectionChangedEventHandler_WinRT,
    NotifyCollectionChangedToManagedAdapter,
    NotifyCollectionChangedToWinRTAdapter,
    NotifyPropertyChangedToManagedAdapter,
    NotifyPropertyChangedToWinRTAdapter,
    PropertyChangedEventArgsMarshaler,
    PropertyChangedEventHandler_WinRT,
    ICommand_WinRT,
    INotifyCollectionChangedEventArgs,
    INotifyCollectionChanged_WinRT,
    INotifyPropertyChanged_WinRT,
    IPropertyChangedEventArgs,
    NotifyCollectionChangedEventHandler_WinRT,
    PropertyChangedEventHandler_WinRT,
]
