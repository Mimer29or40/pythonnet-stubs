__all__ = [
    'Enumerable',
    'EnumerableExecutor',
    'EnumerableExecutor',
    'EnumerableQuery',
    'EnumerableQuery',
    'ImmutableArrayExtensions',
    'Lookup',
    'OrderedParallelQuery',
    'ParallelEnumerable',
    'ParallelQuery',
    'ParallelQuery',
    'Queryable',
    'IGrouping',
    'ILookup',
    'IOrderedEnumerable',
    'IOrderedQueryable',
    'IOrderedQueryable',
    'IQueryable',
    'IQueryable',
    'IQueryProvider',
    'ParallelExecutionMode',
    'ParallelMergeOptions',
]

from typing import TypeVar, Generic

T = TypeVar('T')
TKey = TypeVar('TKey')
TElement = TypeVar('TElement')
TSource = TypeVar('TSource')


# TODO

##### CLASSES #####

class Enumerable:
    """Provides a set of static (Shared in Visual Basic) methods for querying objects that implement IEnumerable[T]."""


class EnumerableExecutor:
    """Represents an expression tree and provides functionality to execute the expression tree after rewriting it."""


class EnumerableExecutor(Generic[T]):
    """Represents an expression tree and provides functionality to execute the expression tree after rewriting it."""


class EnumerableQuery:
    """Represents an IEnumerable as an EnumerableQuery data source."""


class EnumerableQuery(Generic[T]):
    """Represents an IEnumerable[T] collection as an IQueryable[T] data source."""


class ImmutableArrayExtensions:
    """LINQ extension method overrides that offer greater efficiency for ImmutableArray[T] than the standard LINQ methods"""


class Lookup(Generic[TKey, TElement]):
    """Represents a collection of keys each mapped to one or more values."""


class OrderedParallelQuery(Generic[TSource]):
    """Represents a sorted, parallel sequence."""


class ParallelEnumerable:
    """Provides a set of methods for querying objects that implement ParallelQuery{TSource}. This is the parallel equivalent of Enumerable."""


class ParallelQuery:
    """Represents a parallel sequence."""


class ParallelQuery(Generic[TSource]):
    """Represents a parallel sequence."""


class Queryable:
    """Provides a set of static (Shared in Visual Basic) methods for querying data structures that implement IQueryable[T]."""


##### INTERFACES #####

class IGrouping(Generic[TKey, TElement]):
    """Represents a collection of objects that have a common key."""


class ILookup(Generic[TKey, TElement]):
    """Defines an indexer, size property, and Boolean search method for data structures that map keys to IEnumerable[T] sequences of values."""


class IOrderedEnumerable(Generic[TElement]):
    """Represents a sorted sequence."""


class IOrderedQueryable:
    """Represents the result of a sorting operation."""


class IOrderedQueryable(Generic[T]):
    """Represents the result of a sorting operation."""


class IQueryable:
    """Provides functionality to evaluate queries against a specific data source wherein the type of the data is not specified."""


class IQueryable(Generic[T]):
    """Provides functionality to evaluate queries against a specific data source wherein the type of the data is known."""


class IQueryProvider:
    """Defines methods to create and execute queries that are described by an IQueryable object."""


##### ENUMS #####

class ParallelExecutionMode:
    """The query execution mode is a hint that specifies how the system should handle performance trade-offs when parallelizing queries."""


class ParallelMergeOptions:
    """Specifies the preferred type of output merge to use in a query. In other words, it indicates how PLINQ should merge the results from the various partitions back into a single result sequence. This is a hint only, and may not be respected by the system when parallelizing all queries."""
