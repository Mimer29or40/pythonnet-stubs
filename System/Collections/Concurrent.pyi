__all__ = [
    'BlockingCollection',
    'ConcurrentBag',
    'ConcurrentDictionary',
    'ConcurrentQueue',
    'ConcurrentStack',
    'OrderablePartitioner',
    'Partitioner',
    'Partitioner',
    'IProducerConsumerCollection',
    'EnumerablePartitionerOptions',
]

from typing import TypeVar, Generic

T = TypeVar('T')
TKey = TypeVar('TKey')
TValue = TypeVar('TValue')
TSource = TypeVar('TSource')


# TODO


# ---------- CLASSES ---------- #

class BlockingCollection(Generic[T]):
    """Provides blocking and bounding capabilities for thread-safe collections that implement IProducerConsumerCollection[T]."""


class ConcurrentBag(Generic[T]):
    """Represents a thread-safe, unordered collection of objects."""


class ConcurrentDictionary(Generic[TKey, TValue]):
    """Represents a thread-safe collection of key/value pairs that can be accessed by multiple threads concurrently."""


class ConcurrentQueue(Generic[T]):
    """Represents a thread-safe first in-first out (FIFO) collection."""


class ConcurrentStack(Generic[T]):
    """Represents a thread-safe last in-first out (LIFO) collection."""


class OrderablePartitioner(Generic[TSource]):
    """Represents a particular manner of splitting an orderable data source into multiple partitions."""


class Partitioner:
    """Provides common partitioning strategies for arrays, lists, and enumerables."""


class Partitioner(Generic[TSource]):
    """Represents a particular manner of splitting a data source into multiple partitions."""


# ---------- INTERFACES ---------- #

class IProducerConsumerCollection(Generic[T]):
    """Defines methods to manipulate thread-safe collections intended for producer/consumer usage. This interface provides a unified representation for producer/consumer collections so that higher level abstractions such as BlockingCollection[T] can use the collection as the underlying storage mechanism."""


# ---------- ENUMS ---------- #

class EnumerablePartitionerOptions:
    """Specifies options to control the buffering behavior of a partitioner."""
