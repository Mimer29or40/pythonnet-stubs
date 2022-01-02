__all__ = [
    'ActionBlock',
    'BatchBlock',
    'BatchedJoinBlock',
    'BatchedJoinBlock',
    'BroadcastBlock',
    'BufferBlock',
    'DataflowBlock',
    'DataflowBlockOptions',
    'DataflowLinkOptions',
    'ExecutionDataflowBlockOptions',
    'GroupingDataflowBlockOptions',
    'JoinBlock',
    'JoinBlock',
    'TransformBlock',
    'TransformManyBlock',
    'WriteOnceBlock',
    'DataflowMessageHeader',
    'IDataflowBlock',
    'IPropagatorBlock',
    'IReceivableSourceBlock',
    'ISourceBlock',
    'ITargetBlock',
    'DataflowMessageStatus',
]

from typing import TypeVar, Generic

T = TypeVar('T')
T1 = TypeVar('T1')
T2 = TypeVar('T2')
T3 = TypeVar('T3')
TInput = TypeVar('TInput')
TOutput = TypeVar('TOutput')


# TODO

# ---------- CLASSES ---------- #

class ActionBlock(Generic[TInput]):
    """Provides a dataflow block that invokes a provided Action<T> delegate for every data element received."""


class BatchBlock(Generic[T]):
    """Provides a dataflow block that batches inputs into arrays."""


class BatchedJoinBlock(Generic[T1, T2]):
    """Provides a dataflow block that batches a specified number of inputs of potentially differing types provided to one or more of its targets."""


class BatchedJoinBlock(Generic[T1, T2, T3]):
    """Provides a dataflow block that batches a specified number of inputs of potentially differing types provided to one or more of its targets."""


class BroadcastBlock(Generic[T]):
    """Provides a buffer for storing at most one element at time, overwriting each message with the next as it arrives."""


class BufferBlock(Generic[T]):
    """Provides a buffer for storing data for a Dataflow."""


class DataflowBlock:
    """Provides a set of static (Shared in Visual Basic) methods for working with dataflow blocks."""


class DataflowBlockOptions:
    """Provides options used to configure the processing performed by dataflow blocks."""


class DataflowLinkOptions:
    """Provides options used to configure a link between dataflow blocks."""


class ExecutionDataflowBlockOptions:
    """Provides options used to configure the processing performed by dataflow blocks that process each message through the invocation of a user-provided delegate. These are dataflow blocks such as ActionBlock<TInput> and TransformBlock<TInput,TOutput>."""


class GroupingDataflowBlockOptions:
    """Provides options used to configure the processing performed by dataflow blocks that group together multiple messages. These are dataflow blocks such as JoinBlock<T1,T2> and BatchBlock<T>."""


class JoinBlock(Generic[T1, T2]):
    """Provides a dataflow block that joins across multiple dataflow sources, not necessarily of the same type, waiting for one item to arrive for each type before they're all released together as a tuple consisting of one item per type."""


class JoinBlock(Generic[T1, T2, T3]):
    """Provides a dataflow block that joins across multiple dataflow sources, which are not necessarily of the same type, waiting for one item to arrive for each type before they're all released together as a tuple that contains one item per type."""


class TransformBlock(Generic[TInput, TOutput]):
    """Provides a dataflow block that invokes a provided Func<T,TResult> delegate for every data element received."""


class TransformManyBlock(Generic[TInput, TOutput]):
    """Provides a dataflow block that invokes a provided Func<T,TResult> delegate for every data element received."""


class WriteOnceBlock(Generic[T]):
    """Provides a buffer for receiving and storing at most one element in a network of dataflow blocks."""


# ---------- STRUCTS ---------- #

class DataflowMessageHeader:
    """Provides a container of data attributes for passing between dataflow blocks."""


# ---------- INTERFACES ---------- #

class IDataflowBlock:
    """Represents a dataflow block."""


class IPropagatorBlock(Generic[TInput, TOutput]):
    """Represents a dataflow block that is both a target for data and a source of data."""


class IReceivableSourceBlock(Generic[TOutput]):
    """Represents a dataflow block that supports receiving messages without linking."""


class ISourceBlock(Generic[TOutput]):
    """Represents a dataflow block that is a source of data."""


class ITargetBlock(Generic[TInput]):
    """Represents a dataflow block that is a target for data."""


# ---------- ENUMS ---------- #

class DataflowMessageStatus:
    """Represents the status of a DataflowMessageHeader when passed between dataflow blocks."""
