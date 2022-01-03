__all__ = [
    'ArrayBufferWriter',
    'ArrayPool',
    'BuffersExtensions',
    'MemoryManager',
    'MemoryPool',
    'ReadOnlySequenceSegment',
    'SequenceReaderExtensions',
    'MemoryHandle',
    'ReadOnlySequence',
    'ReadOnlySequence',
    'SequenceReader',
    'StandardFormat',
    'IBufferWriter',
    'IMemoryOwner',
    'IPinnable',
    'OperationStatus',
    'ReadOnlySpanAction',
    'SpanAction',
]

from typing import TypeVar, Generic

T = TypeVar('T')
TArg = TypeVar('TArg')


# TODO

# ---------- CLASSES ----------#

class ArrayBufferWriter(Generic[T]):
    """Represents a heap-based, array-backed output sink into which T data can be written."""


class ArrayPool(Generic[T]):
    """Provides a resource pool that enables reusing instances of type T[]."""


class BuffersExtensions:
    """Provides extension methods for ReadOnlySequence<T>."""


class MemoryManager(Generic[T]):
    """An abstract base class that is used to replace the implementation of Memory<T>."""


class MemoryPool(Generic[T]):
    """Represents a pool of memory blocks."""


class ReadOnlySequenceSegment(Generic[T]):
    """Represents a linked list of ReadOnlyMemory<T> nodes."""


class SequenceReaderExtensions:
    """Provides extended functionality for the SequenceReader<T> class that allows reading of endian specific numeric values from binary data."""


# ---------- STRUCTS ----------#

class MemoryHandle:
    """Provides a memory handle for a block of memory."""


class ReadOnlySequence(Generic[T]):
    """Represents a sequence that can read a sequential series of T."""
    
    class Enumerator:
        """Represents an enumerator over a ReadOnlySequence<T>."""


class SequenceReader(Generic[T]):
    """Provides methods for reading binary and text data out of a ReadOnlySequence<T> with a focus on performance and minimal or zero heap allocations."""


class StandardFormat:
    """Represents a standard format string without using an actual string."""


# ---------- INTERFACES ----------#

class IBufferWriter(Generic[T]):
    """Represents an output sink into which T data can be written."""


class IMemoryOwner(Generic[T]):
    """Identifies the owner of a block of memory who is responsible for disposing of the underlying memory appropriately."""


class IPinnable:
    """Provides a mechanism for pinning and unpinning objects to prevent the garbage collector from moving them."""


# ---------- ENUMS ----------#

class OperationStatus:
    """Defines the values that can be returned from span-based operations that support processing of input contained in multiple discontiguous buffers."""


# ---------- DELEGATES ----------#

class ReadOnlySpanAction(Generic[T, TArg]):
    """Encapsulates a method that receives a read-only span of objects of type T and a state object of type TArg."""


class SpanAction(Generic[T, TArg]):
    """Encapsulates a method that receives a span of objects of type T and a state object of type TArg."""
