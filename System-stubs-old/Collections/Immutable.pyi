__all__ = [
    'ImmutableDictionary',
    'ImmutableDictionary',
    'ImmutableHashSet',
    'ImmutableHashSet',
    'ImmutableInterlocked',
    'ImmutableList',
    'ImmutableList',
    'ImmutableQueue',
    'ImmutableQueue',
    'ImmutableSortedDictionary',
    'ImmutableSortedDictionary',
    'ImmutableSortedSet',
    'ImmutableSortedSet',
    'ImmutableStack',
    'ImmutableStack',
    'ImmutableArray',
    'ImmutableArray',
    'IImmutableDictionary',
    'IImmutableList',
    'IImmutableQueue',
    'IImmutableSet',
    'IImmutableStack',
]

from typing import TypeVar, Generic

T = TypeVar('T')
TKey = TypeVar('TKey')
TValue = TypeVar('TValue')


# TODO


# ---------- CLASSES ---------- #

class ImmutableDictionary:
    """Provides a set of initialization methods for instances of the ImmutableDictionary<TKey,TValue> class."""


class ImmutableDictionary(Generic[TKey, TValue]):
    """Represents an immutable, unordered collection of keys and values."""
    
    class Builder:
        """Represents a hash map that mutates with little or no memory allocations and that can produce or build on immutable hash map instances very efficiently."""
    
    # ---------- STRUCTS ---------- #
    class Enumerator:
        """Enumerates the contents of the immutable dictionary without allocating any memory."""


class ImmutableHashSet:
    """Provides a set of initialization methods for instances of the ImmutableHashSet[T] class."""


class ImmutableHashSet(Generic[T]):
    """Represents an immutable, unordered hash set."""
    
    class Builder:
        """Represents a hash set that mutates with little or no memory allocations and that can produce or build on immutable hash set instances very efficiently."""
    
    # ---------- STRUCTS ---------- #
    
    class Enumerator:
        """Enumerates the contents of the immutable hash set without allocating any memory."""


class ImmutableInterlocked:
    """Contains interlocked exchange mechanisms for immutable collections."""


class ImmutableList:
    """Provides a set of initialization methods for instances of the ImmutableList[T] class."""


class ImmutableList(Generic[T]):
    """Represents an immutable list, which is a strongly typed list of objects that can be accessed by index."""
    
    class Builder:
        """Represents a list that mutates with little or no memory allocations and that can produce or build on immutable list instances very efficiently."""
    
    # ---------- STRUCTS ---------- #
    
    class Enumerator:
        """Enumerates the contents of a binary tree."""


class ImmutableQueue:
    """Provides a set of initialization methods for instances of the ImmutableQueue[T] class."""


class ImmutableQueue(Generic[T]):
    """Represents an immutable queue."""
    
    # ---------- STRUCTS ---------- #
    
    class Enumerator:
        """Enumerates the contents of an immutable queue without allocating any memory."""


class ImmutableSortedDictionary:
    """Provides a set of initialization methods for instances of the ImmutableSortedDictionary<TKey,TValue> class."""


class ImmutableSortedDictionary(Generic[TKey, TValue]):
    """Represents an immutable sorted dictionary."""
    
    class Builder:
        """Represents a sorted dictionary that mutates with little or no memory allocations and that can produce or build on immutable sorted dictionary instances very efficiently."""
    
    # ---------- STRUCTS ---------- #
    
    class Enumerator:
        """Enumerates the contents of a binary tree."""


class ImmutableSortedSet:
    """Provides a set of initialization methods for instances of the ImmutableSortedSet[T] class."""


class ImmutableSortedSet(Generic[T]):
    """Represents an immutable sorted set implementation."""
    
    class Builder:
        """Represents a sorted set that enables changes with little or no memory allocations, and efficiently manipulates or builds immutable sorted sets."""
    
    # ---------- STRUCTS ---------- #
    
    class Enumerator:
        """Enumerates the contents of a binary tree."""


class ImmutableStack:
    """Provides a set of initialization methods for instances of the ImmutableStack[T] class."""


class ImmutableStack(Generic[T]):
    """Represents an immutable stack."""
    
    # ---------- STRUCTS ---------- #
    
    class Enumerator:
        """Enumerates the contents of an immutable stack without allocating any memory."""


# ---------- STRUCTS ---------- #

class ImmutableArray:
    """Provides methods for creating an array that is immutable; meaning it cannot be changed once it is created."""
    
    class Builder:
        """A writable array accessor that can be converted into an ImmutableArray[T] instance without allocating extra memory."""


class ImmutableArray(Generic[T]):
    """Represents an array that is immutable; meaning it cannot be changed once it is created."""
    
    class Enumerator:
        """An array enumerator."""


# ---------- INTERFACES ---------- #

class IImmutableDictionary(Generic[TKey, TValue]):
    """Represents an immutable collection of key/value pairs."""


class IImmutableList(Generic[T]):
    """Represents a list of elements that cannot be modified."""


class IImmutableQueue(Generic[T]):
    """Represents an immutable first-in, first-out collection of objects."""


class IImmutableSet(Generic[T]):
    """Represents a set of elements that can only be modified by creating a new instance of the set."""


class IImmutableStack(Generic[T]):
    """Represents an immutable last-in-first-out (LIFO) collection."""
