__all__ = [
    'CollectionsUtil',
    'HybridDictionary',
    'ListDictionary',
    'NameObjectCollectionBase',
    'NameValueCollection',
    'NotifyCollectionChangedEventArgs',
    'OrderedDictionary',
    'StringCollection',
    'StringDictionary',
    'StringEnumerator',
    'BitVector32',
    'INotifyCollectionChanged',
    'IOrderedDictionary',
    'NotifyCollectionChangedAction',
    'NotifyCollectionChangedEventHandler',
]


# TODO

# ---------- CLASSES ---------- #

class CollectionsUtil:
    """Creates collections that ignore the case in strings."""


class HybridDictionary:
    """Implements IDictionary by using a ListDictionary while the collection is small, and then switching to a Hashtable when the collection gets large."""


class ListDictionary:
    """Implements IDictionary using a singly linked list. Recommended for collections that typically include fewer than 10 items."""


class NameObjectCollectionBase:
    """Provides the abstract base class for a collection of associated String keys and Object values that can be accessed either with the key or with the index."""
    
    class KeysCollection:
        """Represents a collection of the String keys of a collection."""


class NameValueCollection:
    """Represents a collection of associated String keys and String values that can be accessed either with the key or with the index."""


class NotifyCollectionChangedEventArgs:
    """Provides data for the CollectionChanged event."""


class OrderedDictionary:
    """Represents a collection of key/value pairs that are accessible by the key or index."""


class StringCollection:
    """Represents a collection of strings."""


class StringDictionary:
    """Implements a hash table with the key and the value strongly typed to be strings rather than objects."""


class StringEnumerator:
    """Supports a simple iteration over a StringCollection."""


# ---------- STRUCTS ---------- #

class BitVector32:
    """Provides a simple structure that stores Boolean values and small integers in 32 bits of memory."""
    
    class Section:
        """Represents a section of the vector that can contain an integer number."""


# ---------- INTERFACES ---------- #

class INotifyCollectionChanged:
    """Notifies listeners of dynamic changes, such as when an item is added and removed or the whole list is cleared."""


class IOrderedDictionary:
    """Represents an indexed collection of key/value pairs."""


# ---------- ENUMS ---------- #

class NotifyCollectionChangedAction:
    """Describes the action that caused a CollectionChanged event."""


# ---------- DELEGATES ---------- #

class NotifyCollectionChangedEventHandler:
    """Represents the method that handles the CollectionChanged event."""
