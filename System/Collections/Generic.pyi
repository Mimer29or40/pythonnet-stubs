__all__ = [
    'CollectionExtensions',
    'Comparer',
    'Dictionary',
    'EqualityComparer',
    'HashSet',
    'KeyNotFoundException',
    'LinkedList',
    'LinkedListNode',
    'List',
    'PriorityQueue',
    'Queue',
    'ReferenceEqualityComparer',
    'SortedDictionary',
    'SortedList',
    'SortedSet',
    'Stack',
    'KeyValuePair',
    'IAsyncEnumerable',
    'IAsyncEnumerator',
    'ICollection',
    'IComparer',
    'IDictionary',
    'IEnumerable',
    'IEnumerator',
    'IEqualityComparer',
    'IList',
    'IReadOnlyCollection',
    'IReadOnlyDictionary',
    'IReadOnlyList',
    'IReadOnlySet',
    'ISet',
]

from abc import ABC
from typing import Generic, TypeVar, Optional

from System import Int32, Boolean

T = TypeVar('T')
TKey = TypeVar('TKey')
TValue = TypeVar('TValue')
TElement = TypeVar('TElement')
TPriority = TypeVar('TPriority')


# TODO


# ---------- CLASSES ---------- #

class CollectionExtensions:
    """Provides extension methods for generic collections."""


class Comparer(Generic[T]):
    """Provides a base class for implementations of the IComparer[T] generic interface."""


class Dictionary(Generic[TKey, TValue]):
    """Represents a collection of keys and values."""
    
    class KeyCollection:
        """Represents the collection of keys in a Dictionary<TKey,TValue>. This class cannot be inherited."""
        
        # ---------- STRUCTS ---------- #
        
        class Enumerator:
            """Enumerates the elements of a Dictionary<TKey,TValue>.KeyCollection."""
    
    class ValueCollection:
        """Represents the collection of values in a Dictionary<TKey,TValue>. This class cannot be inherited."""
        
        # ---------- STRUCTS ---------- #
        
        class Enumerator:
            """Enumerates the elements of a Dictionary<TKey,TValue>.ValueCollection."""
    
    # ---------- STRUCTS ---------- #
    
    class Enumerator:
        """Enumerates the elements of a Dictionary<TKey,TValue>."""


class EqualityComparer(Generic[T]):
    """Provides a base class for implementations of the IEqualityComparer[T] generic interface."""


class HashSet(Generic[T]):
    """Represents a set of values."""
    
    # ---------- STRUCTS ---------- #
    
    class Enumerator:
        """Enumerates the elements of a HashSet[T] object."""


class KeyNotFoundException:
    """The exception that is thrown when the key specified for accessing an element in a collection does not match any key in the collection."""


class LinkedList(Generic[T]):
    """Represents a doubly linked list."""
    
    # ---------- STRUCTS ---------- #
    
    class Enumerator:
        """Enumerates the elements of a LinkedList[T]."""


class LinkedListNode(Generic[T]):
    """Represents a node in a LinkedList[T]. This class cannot be inherited."""


class List(Generic[T]):
    """Represents a strongly typed list of objects that can be accessed by index. Provides methods to search, sort, and manipulate lists."""
    
    # ---------- STRUCTS ---------- #
    
    class Enumerator:
        """Enumerates the elements of a List[T]."""


class PriorityQueue(Generic[TElement, TPriority]):
    """Represents a collection of items that have a value and a priority. On dequeue, the item with the lowest priority value is removed."""
    
    class UnorderedItemsCollection:
        """Enumerates the contents of a PriorityQueue<TElement,TPriority>, without any ordering guarantees."""
        
        # ---------- STRUCTS ---------- #
        
        class Enumerator:
            """Enumerates the element and priority pairs of a PriorityQueue<TElement,TPriority>, without any ordering guarantees."""


class Queue(Generic[T]):
    """Represents a first-in, first-out collection of objects."""
    
    # ---------- STRUCTS ---------- #
    
    class Enumerator:
        """Enumerates the elements of a Queue[T]."""


class ReferenceEqualityComparer:
    """An IEqualityComparer[T] that uses reference equality (ReferenceEquals(Object, Object)) instead of value equality (Equals(Object)) when comparing two object instances."""


class SortedDictionary(Generic[TKey, TValue]):
    """Represents a collection of key/value pairs that are sorted on the key."""
    
    class KeyCollection:
        """Represents the collection of keys in a SortedDictionary<TKey,TValue>. This class cannot be inherited."""
        
        # ---------- STRUCTS ---------- #
        
        class Enumerator:
            """Enumerates the elements of a SortedDictionary<TKey,TValue>.KeyCollection."""
    
    class ValueCollection:
        """Represents the collection of values in a SortedDictionary<TKey,TValue>. This class cannot be inherited."""
        
        # ---------- STRUCTS ---------- #
        
        class Enumerator:
            """Enumerates the elements of a SortedDictionary<TKey,TValue>.ValueCollection."""
    
    # ---------- STRUCTS ---------- #
    class Enumerator:
        """Enumerates the elements of a SortedDictionary<TKey,TValue>."""


class SortedList(Generic[TKey, TValue]):
    """Represents a collection of key/value pairs that are sorted by key based on the associated IComparer[T] implementation."""


class SortedSet(Generic[T]):
    """Represents a collection of objects that is maintained in sorted order."""
    
    # ---------- STRUCTS ---------- #
    
    class Enumerator:
        """Enumerates the elements of a SortedSet[T] object."""


class Stack(Generic[T]):
    """Represents a variable size last-in-first-out (LIFO) collection of instances of the same specified type."""
    
    # ---------- STRUCTS ---------- #
    
    class Enumerator:
        """Enumerates the elements of a Stack[T]."""


# ---------- STRUCTS ---------- #

class KeyValuePair(Generic[TKey, TValue]):
    """Defines a key/value pair that can be set or retrieved."""
    
    @staticmethod
    def Create(key: TKey, value: TValue) -> KeyValuePair[TKey, TValue]:
        """Creates a new key/value pair instance using provided values."""


# ---------- INTERFACES ---------- #

class IAsyncEnumerable(Generic[T]):
    """Exposes an enumerator that provides asynchronous iteration over values of a specified type."""


class IAsyncEnumerator(Generic[T]):
    """Supports a simple asynchronous iteration over a generic collection."""


class ICollection(Generic[T]):
    """Defines methods to manipulate generic collections."""


class IComparer(ABC, Generic[T]):
    """Defines a method that a type implements to compare two objects."""
    
    def Compare(self, x: T, y: T) -> Int32:
        """Compares two objects and returns a value indicating whether one
        is less than, equal to, or greater than the other.
        """


class IDictionary(Generic[TKey, TValue]):
    """Represents a generic collection of key/value pairs."""


class IEnumerable(Generic[T]):
    """Exposes the enumerator, which supports a simple iteration over a collection of a specified type."""


class IEnumerator(Generic[T]):
    """Supports a simple iteration over a generic collection."""


class IEqualityComparer(ABC, Generic[T]):
    """Defines methods to support the comparison of objects for equality."""
    
    def Equals(self, x: Optional[T], y: Optional[T]) -> Boolean:
        """Determines whether the specified objects are equal."""
    
    def GetHashCode(self, obj: T) -> Int32:
        """Returns a hash code for the specified object."""


class IList(Generic[T]):
    """Represents a collection of objects that can be individually accessed by index."""


class IReadOnlyCollection(Generic[T]):
    """Represents a strongly-typed, read-only collection of elements."""


class IReadOnlyDictionary(Generic[TKey, TValue]):
    """Represents a generic read-only collection of key/value pairs."""


class IReadOnlyList(Generic[T]):
    """Represents a read-only collection of elements that can be accessed by index."""


class IReadOnlySet(Generic[T]):
    """Provides a readonly abstraction of a set."""


class ISet(Generic[T]):
    """Provides the base interface for the abstraction of sets."""
