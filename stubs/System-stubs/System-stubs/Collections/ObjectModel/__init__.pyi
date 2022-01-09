from __future__ import annotations

from typing import Generic, TypeVar, Union, overload

from System import Int32, Void
from System.Collections import ICollection, IEnumerable, IList
from System.Collections.Generic import ICollection, IEnumerable, IList, IReadOnlyCollection, IReadOnlyList, List
from System.Collections.ObjectModel import Collection, ReadOnlyCollection
from System.Collections.Specialized import INotifyCollectionChanged, NotifyCollectionChangedEventHandler
from System.ComponentModel import INotifyPropertyChanged

# ---------- Types ---------- #

T = TypeVar('T')

IntType = Union[int, Int32]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...


# ---------- Classes ---------- #

class ObservableCollection(Generic[T], Collection[T], IList[T], ICollection[T], IEnumerable[T], IEnumerable, IList, ICollection, IReadOnlyList[T], IReadOnlyCollection[T], INotifyCollectionChanged, INotifyPropertyChanged):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, list: List[T]): ...
    
    @overload
    def __init__(self, collection: IEnumerable[T]): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Move(self, oldIndex: IntType, newIndex: IntType) -> VoidType: ...
    
    def add_CollectionChanged(self, value: NotifyCollectionChangedEventHandler) -> VoidType: ...
    
    def remove_CollectionChanged(self, value: NotifyCollectionChangedEventHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    CollectionChanged: EventType[NotifyCollectionChangedEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReadOnlyObservableCollection(Generic[T], ReadOnlyCollection[T], IList[T], ICollection[T], IEnumerable[T], IEnumerable, IList, ICollection, IReadOnlyList[T], IReadOnlyCollection[T], INotifyCollectionChanged, INotifyPropertyChanged):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, list: ObservableCollection[T]): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# No Enums

# No Delegates

__all__ = [
    ObservableCollection,
    ReadOnlyObservableCollection,
]
