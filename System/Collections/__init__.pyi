from __future__ import annotations

__all__ = [
    'ArrayList',
    'BitArray',
    'CaseInsensitiveComparer',
    'CaseInsensitiveHashCodeProvider',
    'CollectionBase',
    'Comparer',
    'DictionaryBase',
    'Hashtable',
    'Queue',
    'ReadOnlyCollectionBase',
    'SortedList',
    'Stack',
    'StructuralComparisons',
    'DictionaryEntry',
    'ICollection',
    'IComparer',
    'IDictionary',
    'IDictionaryEnumerator',
    'IEnumerable',
    'IEnumerator',
    'IEqualityComparer',
    'IHashCodeProvider',
    'IList',
    'IStructuralComparable',
    'IStructuralEquatable',
]


# TODO

# ---------- CLASSES ---------- #


class ArrayList:
    """Implements the IList interface using an array whose size is dynamically increased as required."""


class BitArray:
    """Manages a compact array of bit values, which are represented as Booleans, where true indicates that the bit is on (1) and false indicates the bit is off (0)."""


class CaseInsensitiveComparer:
    """Compares two objects for equivalence, ignoring the case of strings."""


class CaseInsensitiveHashCodeProvider:
    """Supplies a hash code for an object, using a hashing algorithm that ignores the case of strings."""


class CollectionBase:
    """Provides the abstract base class for a strongly typed collection."""


class Comparer:
    """Compares two objects for equivalence, where string comparisons are case-sensitive."""


class DictionaryBase:
    """Provides the abstract base class for a strongly typed collection of key/value pairs."""


class Hashtable:
    """Represents a collection of key/value pairs that are organized based on the hash code of the key."""


class Queue:
    """Represents a first-in, first-out collection of objects."""


class ReadOnlyCollectionBase:
    """Provides the abstract base class for a strongly typed non-generic read-only collection."""


class SortedList:
    """Represents a collection of key/value pairs that are sorted by the keys and are accessible by key and by index."""


class Stack:
    """Represents a simple last-in-first-out (LIFO) non-generic collection of objects."""


class StructuralComparisons:
    """Provides objects for performing a structural comparison of two collection objects."""


# ---------- STRUCTS ---------- #


class DictionaryEntry:
    """Defines a dictionary key/value pair that can be set or retrieved."""


# ---------- INTERFACES ---------- #

class ICollection:
    """Defines size, enumerators, and synchronization methods for all nongeneric collections."""


class IComparer:
    """Exposes a method that compares two objects."""


class IDictionary:
    """Represents a nongeneric collection of key/value pairs."""


class IDictionaryEnumerator:
    """Enumerates the elements of a nongeneric dictionary."""


class IEnumerable:
    """Exposes an enumerator, which supports a simple iteration over a non-generic collection."""


class IEnumerator:
    """Supports a simple iteration over a non-generic collection."""


class IEqualityComparer:
    """Defines methods to support the comparison of objects for equality."""


class IHashCodeProvider:
    """Supplies a hash code for an object, using a custom hash function."""


class IList:
    """Represents a non-generic collection of objects that can be individually accessed by index."""


class IStructuralComparable:
    """Supports the structural comparison of collection objects."""


class IStructuralEquatable:
    """Defines methods to support the comparison of objects for structural equality."""
