__all__ = [
    'Collection',
    'KeyedCollection',
    'ObservableCollection',
    'ReadOnlyCollection',
    'ReadOnlyDictionary',
    'ReadOnlyObservableCollection',
]

from typing import TypeVar, Generic

T = TypeVar('T')
TKey = TypeVar('TKey')
TValue = TypeVar('TValue')
TItem = TypeVar('TItem')


# TODO


# ---------- CLASSES ---------- #

class Collection(Generic[T]):
    """Provides the base class for a generic collection."""


class KeyedCollection(Generic[TKey, TItem]):
    """Provides the abstract base class for a collection whose keys are embedded in the values."""


class ObservableCollection(Generic[T]):
    """Represents a dynamic data collection that provides notifications when items get added, removed, or when the whole list is refreshed."""


class ReadOnlyCollection(Generic[T]):
    """Provides the base class for a generic read-only collection."""


class ReadOnlyDictionary(Generic[TKey, TValue]):
    """Represents a read-only, generic collection of key/value pairs."""
    
    class KeyCollection:
        """Represents a read-only collection of the keys of a ReadOnlyDictionary<TKey,TValue> object."""
    
    class ValueCollection:
        """Represents a read-only collection of the values of a ReadOnlyDictionary<TKey,TValue> object."""


class ReadOnlyObservableCollection(Generic[T]):
    """Represents a read-only ObservableCollection[T]."""
