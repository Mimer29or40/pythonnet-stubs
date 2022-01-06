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

from typing import Generic, TypeVar, overload, Protocol, Tuple

from .Immutable import ImmutableArray, ImmutableDictionary, ImmutableHashSet, ImmutableList, ImmutableSortedSet, ImmutableSortedDictionary
from .. import IntType, Func, NullableType, Func, BooleanType, DecimalType, DoubleType, LongType, FloatType, ArrayType, Index, Range, Int32, VoidType, IDisposable, IAsyncDisposable, ValueType
from ..Collections import IEnumerable as _IEnumerable, IEnumerator as _IEnumerator, IDictionaryEnumerator
from ..Data import DataRow, DataTable, LoadOption, FillErrorEventHandler
from ..Linq import IGrouping, IOrderedEnumerable, ILookup, ParallelQuery, IQueryable
from ..Runtime.CompilerServices import ConfiguredCancelableAsyncEnumerable
from ..Runtime.Serialization import IDeserializationCallback, ISerializable
from ..Threading import CancellationToken
from ..Threading.Tasks import ValueTask
from ..Xml.Linq import XNode, XElement, XName, XContainer
from ..util import Item, ReadOnlyItem

T = TypeVar('T')
TKey = TypeVar('TKey')
TValue = TypeVar('TValue')
TInner = TypeVar('TInner')
TResult = TypeVar('TResult')
TElement = TypeVar('TElement')
TPriority = TypeVar('TPriority')
TAccumulate = TypeVar('TAccumulate')
TCollection = TypeVar('TCollection')
TSecond = TypeVar('TSecond')
TThird = TypeVar('TThird')
TDataRow = TypeVar('TDataRow', bound=DataRow)
TXNode = TypeVar('TXNode', bound=XNode)
TXContainer = TypeVar('TXContainer', bound=XContainer)


# TODO


# ---------- CLASSES ---------- #

class CollectionExtensions:
    """Provides extension methods for generic collections."""


class Comparer(Generic[T]):
    """Provides a base class for implementations of the IComparer[T] generic interface."""


class Dictionary(Generic[TKey, TValue]):
    """Represents a collection of keys and values."""
    
    class KeyCollection:
        """Represents the collection of keys in a Dictionary[TKey,TValue]. This class cannot be inherited."""
        
        # ---------- STRUCTS ---------- #
        
        class Enumerator:
            """Enumerates the elements of a Dictionary[TKey,TValue].KeyCollection."""
    
    class ValueCollection:
        """Represents the collection of values in a Dictionary[TKey,TValue]. This class cannot be inherited."""
        
        # ---------- STRUCTS ---------- #
        
        class Enumerator:
            """Enumerates the elements of a Dictionary[TKey,TValue].ValueCollection."""
    
    # ---------- STRUCTS ---------- #
    
    class Enumerator:
        """Enumerates the elements of a Dictionary[TKey,TValue]."""


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
        """Enumerates the contents of a PriorityQueue[TElement,TPriority], without any ordering guarantees."""
        
        # ---------- STRUCTS ---------- #
        
        class Enumerator(ValueType, IEnumerator):
            """Enumerates the element and priority pairs of a PriorityQueue[TElement,TPriority], without any ordering guarantees."""


class Queue(Generic[T]):
    """Represents a first-in, first-out collection of objects."""
    
    # ---------- STRUCTS ---------- #
    
    class Enumerator(ValueType, IEnumerator[T]):
        """Enumerates the elements of a Queue[T]."""


class ReferenceEqualityComparer:
    """An IEqualityComparer[T] that uses reference equality (ReferenceEquals(Object, Object)) instead of value equality (Equals(Object)) when comparing two object instances."""


class SortedDictionary(Generic[TKey, TValue]):
    """Represents a collection of key/value pairs that are sorted on the key."""
    
    class KeyCollection:
        """Represents the collection of keys in a SortedDictionary[TKey,TValue]. This class cannot be inherited."""
        
        # ---------- STRUCTS ---------- #
        
        class Enumerator(ValueType, IEnumerator[TKey]):
            """Enumerates the elements of a SortedDictionary[TKey,TValue].KeyCollection."""
    
    class ValueCollection:
        """Represents the collection of values in a SortedDictionary[TKey,TValue]. This class cannot be inherited."""
        
        # ---------- STRUCTS ---------- #
        
        class Enumerator(ValueType, IEnumerator[TValue]):
            """Enumerates the elements of a SortedDictionary[TKey,TValue].ValueCollection."""
    
    # ---------- STRUCTS ---------- #
    
    class Enumerator(ValueType, IEnumerator[KeyValuePair[TKey, TValue]], IDictionaryEnumerator):
        """Enumerates the elements of a SortedDictionary[TKey,TValue]."""


class SortedList(Generic[TKey, TValue]):
    """Represents a collection of key/value pairs that are sorted by key based on the associated IComparer[T] implementation."""


class SortedSet(Generic[T]):
    """Represents a collection of objects that is maintained in sorted order."""
    
    # ---------- STRUCTS ---------- #
    
    class Enumerator(ValueType, IEnumerator[T], IDeserializationCallback, ISerializable):
        """Enumerates the elements of a SortedSet[T] object."""


class Stack(Generic[T]):
    """Represents a variable size last-in-first-out (LIFO) collection of instances of the same specified type."""
    
    # ---------- STRUCTS ---------- #
    
    class Enumerator(ValueType, IEnumerator[T]):
        """Enumerates the elements of a Stack[T]."""


# ---------- STRUCTS ---------- #

class KeyValuePair(Generic[TKey, TValue]):
    """Defines a key/value pair that can be set or retrieved."""
    
    @staticmethod
    def Create(key: TKey, value: TValue) -> KeyValuePair[TKey, TValue]:
        """Creates a new key/value pair instance using provided values."""


# ---------- INTERFACES ---------- #

class IAsyncEnumerable(Protocol[T]):
    """Exposes an enumerator that provides asynchronous iteration over values
    of a specified type."""
    
    def GetAsyncEnumerator(self, cancellationToken: CancellationToken = None):
        """Returns an enumerator that iterates asynchronously through the
        collection."""
    
    def ConfigureAwait(self, continueOnCapturedContext: BooleanType) -> ConfiguredCancelableAsyncEnumerable[T]:
        """Configures how awaits on the tasks returned from an async
        iteration are performed."""
    
    def WithCancellation(self, cancellationToken: CancellationToken) -> ConfiguredCancelableAsyncEnumerable[T]:
        """Sets the CancellationToken to be passed to
        GetAsyncEnumerator(CancellationToken) when iterating."""


class IAsyncEnumerator(Protocol[T], IAsyncDisposable):
    """Supports a simple asynchronous iteration over a generic collection."""
    
    @property
    def Current(self) -> T:
        """Gets the element in the collection at the current position of the
        enumerator."""
    
    def MoveNextAsync(self) -> ValueTask[BooleanType]:
        """Advances the enumerator asynchronously to the next element of the
        collection."""


class ICollection(Protocol[T], IEnumerable[T]):
    """Defines methods to manipulate generic collections."""
    
    @property
    def IsReadOnly(self) -> BooleanType:
        """Gets a value indicating whether the ICollection[T] is read-only."""
    
    def Add(self, item: T) -> VoidType:
        """Adds an item to the ICollection[T]."""
    
    def Clear(self) -> VoidType:
        """Removes all items from the ICollection[T]."""
    
    def CopyTo(self, array: ArrayType[T], arrayIndex: IntType) -> VoidType:
        """Copies the elements of the ICollection[T] to an Array, starting
        at a particular Array index."""
    
    def Remove(self, item: T) -> BooleanType:
        """Removes the first occurrence of a specific object from the
        ICollection[T]."""


class IComparer(Protocol[T]):
    """Defines a method that a type implements to compare two objects."""
    
    def Compare(self, x: NullableType[T], y: NullableType[T]) -> IntType:
        """Compares two objects and returns a value indicating whether one
        is less than, equal to, or greater than the other.
        """


class IDictionary(Protocol[TKey, TValue], ICollection[KeyValuePair[TKey, TValue]]):
    """Represents a generic collection of key/value pairs."""
    
    @property
    def Item(self) -> Item[TKey, TValue]:
        """Gets or sets the element with the specified key."""
    
    def __getitem__(self, key: TKey) -> TValue: ...
    
    def __setitem__(self, key: TKey, value: TValue) -> None: ...
    
    @property
    def Keys(self) -> ICollection[TKey]:
        """Gets an ICollection[T] containing the keys of the
        IDictionary[TKey,TValue]."""
    
    @property
    def Values(self) -> ICollection[TValue]:
        """Gets an ICollection[T] containing the values in the
        IDictionary[TKey,TValue]."""
    
    @overload
    def Add(self, ley: TKey, value: TValue) -> VoidType:
        """Adds an element with the provided key and value to the
        IDictionary[TKey,TValue]."""
    
    def ContainsKey(self, key: TKey) -> BooleanType:
        """Determines whether the IDictionary[TKey,TValue] contains an
        element with the specified key."""
    
    @overload
    def Remove(self, key: TKey) -> BooleanType:
        """Removes the element with the specified key from the
        IDictionary[TKey,TValue]."""
    
    def TryGetValue(self, key: TKey, value: TValue) -> BooleanType:
        """Gets the value associated with the specified key."""


class IEnumerable(Protocol[T], _IEnumerable):
    """Exposes the enumerator, which supports a simple iteration over a
    collection of a specified type.
    """
    
    def GetEnumerator(self) -> IEnumerator[T]:
        """Returns an enumerator that iterates through the collection."""
    
    def ToImmutableArray(self) -> ImmutableArray[T]:
        """Creates an immutable array from the specified collection."""
    
    @overload
    def ToImmutableDictionary(self, keySelector: Func[T, TKey]) -> ImmutableDictionary[TKey, T]:
        """Constructs an immutable dictionary from an existing collection of
        elements, applying a transformation function to the source keys."""
    
    @overload
    def ToImmutableDictionary(self, keySelector: Func[T, TKey], keyComparer: NullableType[IEqualityComparer[TKey]]) -> ImmutableDictionary[TKey, T]:
        """Constructs an immutable dictionary based on some transformation
        of a sequence."""
    
    @overload
    def ToImmutableDictionary(self, keySelector: Func[T, TKey], elementSelector: Func[T, TValue]) -> ImmutableDictionary[TKey, TValue]:
        """Enumerates and transforms a sequence, and produces an immutable
        dictionary of its contents."""
    
    @overload
    def ToImmutableDictionary(self, keySelector: Func[T, TKey], elementSelector: Func[T, TValue], keyComparer: NullableType[IEqualityComparer[TKey]]) -> ImmutableDictionary[TKey, TValue]:
        """Enumerates and transforms a sequence, and produces an immutable
        dictionary of its contents by using the specified key comparer."""
    
    @overload
    def ToImmutableDictionary(self, keySelector: Func[T, TKey], elementSelector: Func[T, TValue], keyComparer: NullableType[IEqualityComparer[TKey]], valueComparer: NullableType[IEqualityComparer[TValue]]) -> ImmutableDictionary[TKey, TValue]:
        """Enumerates and transforms a sequence, and produces an immutable
        dictionary of its contents by using the specified key and value
        comparers."""
    
    @overload
    def ToImmutableHashSet(self) -> ImmutableHashSet[T]:
        """Enumerates a sequence and produces an immutable hash set of its
        contents."""
    
    @overload
    def ToImmutableHashSet(self, equalityComparer: NullableType[IEqualityComparer[T]]) -> ImmutableHashSet[T]:
        """Enumerates a sequence, produces an immutable hash set of its
        contents, and uses the specified equality comparer for the set
        type."""
    
    def ToImmutableList(self) -> ImmutableList[T]:
        """Enumerates a sequence and produces an immutable list of its
        contents."""
    
    @overload
    def ToImmutableSortedDictionary(self, keySelector: Func[T, TKey], elementSelector: Func[T, TValue]) -> ImmutableSortedDictionary[TKey, TValue]:
        """Enumerates and transforms a sequence, and produces an immutable
        sorted dictionary of its contents."""
    
    @overload
    def ToImmutableSortedDictionary(self, keySelector: Func[T, TKey], elementSelector: Func[T, TValue], keyComparer: NullableType[IComparer[TKey]]) -> ImmutableSortedDictionary[TKey, TValue]:
        """Enumerates and transforms a sequence, and produces an immutable
        sorted dictionary of its contents by using the specified key
        comparer."""
    
    @overload
    def ToImmutableSortedDictionary(self, keySelector: Func[T, TKey], elementSelector: Func[T, TValue], keyComparer: NullableType[IComparer[TKey]], valueComparer: NullableType[IEqualityComparer[TValue]]) -> ImmutableSortedDictionary[TKey, TValue]:
        """Enumerates and transforms a sequence, and produces an immutable
        sorted dictionary of its contents by using the specified key and
        value comparers."""
    
    @overload
    def ToImmutableSortedSet(self) -> ImmutableSortedSet[T]:
        """Enumerates a sequence and produces an immutable sorted set of its
        contents."""
    
    @overload
    def ToImmutableSortedSet(self, comparer: NullableType[IComparer[T]]) -> ImmutableSortedSet[T]:
        """Enumerates a sequence, produces an immutable sorted set of its
        contents, and uses the specified comparer."""
    
    @overload
    def CopyToDataTable(self: IEnumerable[TDataRow]) -> DataTable:
        """Returns a DataTable that contains copies of the DataRow objects,
        given an input IEnumerable[T] object where the generic parameter T is
        DataRow."""
    
    @overload
    def CopyToDataTable(self: IEnumerable[TDataRow], table: DataTable, options: LoadOption) -> DataTable:
        """Copies DataRow objects to the specified DataTable, given an input
        IEnumerable[T] object where the generic parameter T is DataRow."""
    
    @overload
    def CopyToDataTable(self: IEnumerable[TDataRow], table: DataTable, options: LoadOption, errorHandler: NullableType[FillErrorEventHandler]) -> DataTable:
        """Copies DataRow objects to the specified DataTable, given an input
        IEnumerable[T] object where the generic parameter T is DataRow."""
    
    @overload
    def Aggregate(self, func: Func[T, T, T]) -> T:
        """Applies an accumulator function over a sequence."""
    
    @overload
    def Aggregate(self, seed: TAccumulate, func: Func[TAccumulate, T, TAccumulate]) -> T:
        """Applies an accumulator function over a sequence. The specified
        seed value is used as the initial accumulator value."""
    
    @overload
    def Aggregate(self, seed: TAccumulate, func: Func[TAccumulate, T, TAccumulate], resultSelector: Func[TAccumulate, T]) -> T:
        """Applies an accumulator function over a sequence. The specified
        seed value is used as the initial accumulator value, and the
        specified function is used to select the result value."""
    
    def All(self, predicate: Func[T, BooleanType]) -> BooleanType:
        """Determines whether all elements of a sequence satisfy a
        condition."""
    
    @overload
    def Any(self) -> BooleanType:
        """Determines whether a sequence contains any elements."""
    
    @overload
    def Any(self, predicate: Func[T, BooleanType]) -> BooleanType:
        """Determines whether any element of a sequence satisfies a
        condition."""
    
    def Append(self, element: T) -> IEnumerable[T]:
        """Appends a value to the end of the sequence."""
    
    def AsEnumerable(self) -> IEnumerable[T]:
        """Returns the input typed as IEnumerable[T]."""
    
    @overload
    def Average(self, selector: Func[T, IntType]) -> DoubleType:
        """Computes the average of a sequence of Int32 values that are
        obtained by invoking a transform function on each element of the
        input sequence."""
    
    @overload
    def Average(self, selector: Func[T, LongType]) -> DoubleType:
        """Computes the average of a sequence of Int64 values that are
        obtained by invoking a transform function on each element of the
        input sequence."""
    
    @overload
    def Average(self, selector: Func[T, FloatType]) -> FloatType:
        """Computes the average of a sequence of Single values that are
        obtained by invoking a transform function on each element of the
        input sequence."""
    
    @overload
    def Average(self, selector: Func[T, DoubleType]) -> DoubleType:
        """Computes the average of a sequence of Double values that are
        obtained by invoking a transform function on each element of the
        input sequence."""
    
    @overload
    def Average(self, selector: Func[T, DecimalType]) -> DecimalType:
        """Computes the average of a sequence of Decimal values that are
        obtained by invoking a transform function on each element of the
        input sequence."""
    
    @overload
    def Average(self, selector: Func[T, NullableType[IntType]]) -> NullableType[DoubleType]:
        """Computes the average of a sequence of nullable Int32 values that
        are obtained by invoking a transform function on each element of the
        input sequence."""
    
    @overload
    def Average(self, selector: Func[T, NullableType[LongType]]) -> NullableType[DoubleType]:
        """Computes the average of a sequence of nullable Int64 values that
        are obtained by invoking a transform function on each element of the
        input sequence."""
    
    @overload
    def Average(self, selector: Func[T, NullableType[FloatType]]) -> NullableType[FloatType]:
        """Computes the average of a sequence of nullable Single values that
        are obtained by invoking a transform function on each element of the
        input sequence."""
    
    @overload
    def Average(self, selector: Func[T, NullableType[DoubleType]]) -> NullableType[DoubleType]:
        """Computes the average of a sequence of nullable Double values that
        are obtained by invoking a transform function on each element of the
        input sequence."""
    
    @overload
    def Average(self, selector: Func[T, NullableType[DecimalType]]) -> NullableType[DecimalType]:
        """Computes the average of a sequence of nullable Decimal values that
        are obtained by invoking a transform function on each element of the
        input sequence."""
    
    def Cast(self) -> IEnumerable[TResult]:
        """Casts the elements of an IEnumerable to the specified type."""
    
    def Chunk(self, size: IntType) -> IEnumerable[ArrayType[T]]:
        """Splits the elements of a sequence into chunks of size at most size."""
    
    def Concat(self, second: IEnumerable[T]) -> IEnumerable[T]:
        """Concatenates two sequences."""
    
    @overload
    def Contains(self, value: T) -> BooleanType:
        """Determines whether a sequence contains a specified element by
        using the default equality comparer."""
    
    @overload
    def Contains(self, value: T, comparer: NullableType[IEqualityComparer[T]]) -> BooleanType:
        """Determines whether a sequence contains a specified element by
        using a specified IEqualityComparer[T]."""
    
    @overload
    def Count(self) -> IntType:
        """Returns the number of elements in a sequence."""
    
    @overload
    def Count(self, predicate: Func[T, BooleanType]) -> IntType:
        """Returns a number that represents how many elements in the
        specified sequence satisfy a condition."""
    
    @overload
    def DefaultIfEmpty(self) -> IEnumerable[NullableType[T]]:
        """Returns the elements of the specified sequence or the type
        parameter's default value in a singleton collection if the sequence
        is empty."""
    
    @overload
    def DefaultIfEmpty(self, defaultValue: T) -> IEnumerable[T]:
        """Returns the elements of the specified sequence or the specified
        value in a singleton collection if the sequence is empty."""
    
    @overload
    def Distinct(self) -> IEnumerable[T]:
        """Returns distinct elements from a sequence by using the default
        equality comparer to compare values."""
    
    @overload
    def Distinct(self, comparer: NullableType[IEqualityComparer[T]]) -> IEnumerable[T]:
        """Returns distinct elements from a sequence by using a specified
        IEqualityComparer[T] to compare values."""
    
    @overload
    def DistinctBy(self, keySelector: Func[T, TKey]) -> IEnumerable[T]:
        """Returns distinct elements from a sequence according to a specified
        key selector function."""
    
    @overload
    def DistinctBy(self, keySelector: Func[T, TKey], comparer: NullableType[IEqualityComparer[TKey]]) -> IEnumerable[T]:
        """Returns distinct elements from a sequence according to a specified
        key selector function and using a specified comparer to compare
        keys."""
    
    @overload
    def ElementAt(self, index: Index) -> T:
        """Returns the element at a specified index in a sequence."""
    
    @overload
    def ElementAt(self, index: IntType) -> T:
        """Returns the element at a specified index in a sequence."""
    
    @overload
    def ElementAtOrDefault(self, index: Index) -> NullableType[T]:
        """Returns the element at a specified index in a sequence or a
        default value if the index is out of range."""
    
    @overload
    def ElementAtOrDefault(self, index: IntType) -> NullableType[T]:
        """Returns the element at a specified index in a sequence or a
        default value if the index is out of range."""
    
    @overload
    def Except(self, second: IEnumerable[T]) -> IEnumerable[T]:
        """Produces the set difference of two sequences by using the default
        equality comparer to compare values."""
    
    @overload
    def Except(self, second: IEnumerable[T], comparer: NullableType[IEqualityComparer[T]]) -> IEnumerable[T]:
        """Produces the set difference of two sequences by using the
        specified IEqualityComparer[T] to compare values."""
    
    @overload
    def ExceptBy(self, second: IEnumerable[TKey], keySelector: Func[T, TKey]) -> IEnumerable[T]:
        """Produces the set difference of two sequences according to a
        specified key selector function."""
    
    @overload
    def ExceptBy(self, second: IEnumerable[TKey], keySelector: Func[T, TKey], comparer: NullableType[IEqualityComparer[TKey]]) -> IEnumerable[T]:
        """Produces the set difference of two sequences according to a
        specified key selector function."""
    
    @overload
    def First(self) -> T:
        """Returns the first element of a sequence."""
    
    @overload
    def First(self, predicate: Func[T, BooleanType]) -> T:
        """Returns the first element in a sequence that satisfies a
        specified condition."""
    
    @overload
    def FirstOrDefault(self) -> NullableType[T]:
        """Returns the first element of a sequence, or a default value if
        the sequence contains no elements."""
    
    @overload
    def FirstOrDefault(self, defaultValue: T) -> NullableType[T]:
        """Returns the first element of a sequence, or a specified default
        value if the sequence contains no elements."""
    
    @overload
    def FirstOrDefault(self, predicate: Func[T, BooleanType]) -> NullableType[T]:
        """Returns the first element of the sequence that satisfies a
        condition or a default value if no such element is found."""
    
    @overload
    def FirstOrDefault(self, predicate: Func[T, BooleanType], defaultValue: T) -> NullableType[T]:
        """Returns the first element of the sequence that satisfies a
        condition, or a specified default value if no such element is
        found."""
    
    @overload
    def GroupBy(self, keySelector: Func[T, TKey]) -> IEnumerable[IGrouping[TKey, T]]:
        """Groups the elements of a sequence according to a specified key
        selector function."""
    
    @overload
    def GroupBy(self, keySelector: Func[T, TKey], comparer: NullableType[IEqualityComparer[TKey]]) -> IEnumerable[IGrouping[TKey, T]]:
        """Groups the elements of a sequence according to a specified key
        selector function and compares the keys by using a specified
        comparer."""
    
    @overload
    def GroupBy(self, keySelector: Func[T, TKey], elementSelector: Func[T, TElement]) -> IEnumerable[IGrouping[TKey, TElement]]:
        """Groups the elements of a sequence according to a specified key
        selector function and projects the elements for each group by using
        a specified function."""
    
    @overload
    def GroupBy(self, keySelector: Func[T, TKey], elementSelector: Func[T, TElement], comparer: NullableType[IEqualityComparer[TKey]]) -> IEnumerable[IGrouping[TKey, TElement]]:
        """Groups the elements of a sequence according to a key selector
        function. The keys are compared by using a comparer and each group's
        elements are projected by using a specified function."""
    
    @overload
    def GroupBy(self, keySelector: Func[T, TKey], resultSelector: Func[TKey, IEnumerable[T], TResult]) -> IEnumerable[TResult]:
        """Groups the elements of a sequence according to a specified key
        selector function and creates a result value from each group and its
        key."""
    
    @overload
    def GroupBy(self, keySelector: Func[T, TKey], resultSelector: Func[TKey, IEnumerable[T], TResult], comparer: NullableType[IEqualityComparer[TKey]]) -> IEnumerable[TResult]:
        """Groups the elements of a sequence according to a specified key
        selector function and creates a result value from each group and its
        key. The keys are compared by using a specified comparer."""
    
    @overload
    def GroupBy(self, keySelector: Func[T, TKey], elementSelector: Func[T, TElement], resultSelector: Func[TKey, IEnumerable[T], TResult]) -> IEnumerable[TResult]:
        """Groups the elements of a sequence according to a specified key
        selector function and creates a result value from each group and
        its key. The elements of each group are projected by using a
        specified function."""
    
    @overload
    def GroupBy(self, keySelector: Func[T, TKey], elementSelector: Func[T, TElement], resultSelector: Func[TKey, IEnumerable[T], TResult], comparer: NullableType[IEqualityComparer[TKey]]) -> IEnumerable[TResult]:
        """Groups the elements of a sequence according to a specified key
        selector function and creates a result value from each group and
        its key. Key values are compared by using a specified comparer, and
        the elements of each group are projected by using a specified
        function."""
    
    @overload
    def GroupJoin(self, inner: IEnumerable[TInner], outerKeySelector: Func[T, TKey], innerKeySelector: Func[TInner, TKey], resultSelector: Func[T, IEnumerable[TInner], TResult]) -> IEnumerable[TResult]:
        """Correlates the elements of two sequences based on equality of
        keys and groups the results. The default equality comparer is used
        to compare keys."""
    
    @overload
    def GroupJoin(self, inner: IEnumerable[TInner], outerKeySelector: Func[T, TKey], innerKeySelector: Func[TInner, TKey], resultSelector: Func[T, IEnumerable[TInner], TResult], comparer: NullableType[IEqualityComparer[TKey]]) -> IEnumerable[TResult]:
        """Correlates the elements of two sequences based on key equality
        and groups the results. A specified IEqualityComparer[T] is used to
        compare keys."""
    
    @overload
    def Intersect(self, second: IEnumerable[T]) -> IEnumerable[T]:
        """Produces the set intersection of two sequences by using the
        default equality comparer to compare values."""
    
    @overload
    def Intersect(self, second: IEnumerable[T], comparer: NullableType[IEqualityComparer[T]]) -> IEnumerable[T]:
        """Produces the set intersection of two sequences by using the
        specified IEqualityComparer[T] to compare values."""
    
    @overload
    def IntersectBy(self, second: IEnumerable[TKey], keySelector: Func[T, TKey]) -> IEnumerable[T]:
        """Produces the set intersection of two sequences according to a
        specified key selector function."""
    
    @overload
    def IntersectBy(self, second: IEnumerable[TKey], keySelector: Func[T, TKey], comparer: NullableType[IEqualityComparer[TKey]]) -> IEnumerable[T]:
        """Produces the set intersection of two sequences according to a
        specified key selector function."""
    
    @overload
    def Join(self, inner: IEnumerable[TInner], outerKeySelector: Func[T, TKey], innerKeySelector: Func[TInner, TKey], resultSelector: Func[T, TInner, TResult]) -> IEnumerable[TResult]:
        """Correlates the elements of two sequences based on matching keys.
        The default equality comparer is used to compare keys."""
    
    @overload
    def Join(self, inner: IEnumerable[TInner], outerKeySelector: Func[T, TKey], innerKeySelector: Func[TInner, TKey], resultSelector: Func[T, TInner, TResult], comparer: NullableType[IEqualityComparer[TKey]]) -> IEnumerable[TResult]:
        """Correlates the elements of two sequences based on matching keys.
        A specified IEqualityComparer[T] is used to compare keys."""
    
    @overload
    def Last(self) -> T:
        """Returns the last element of a sequence."""
    
    @overload
    def Last(self, predicate: Func[T, BooleanType]) -> T:
        """Returns the last element of a sequence that satisfies a
        specified condition."""
    
    @overload
    def LastOrDefault(self) -> NullableType[T]:
        """Returns the last element of a sequence, or a default value if the
        sequence contains no elements."""
    
    @overload
    def LastOrDefault(self, defaultValue: T) -> T:
        """Returns the last element of a sequence, or a specified default
        value if the sequence contains no elements."""
    
    @overload
    def LastOrDefault(self, predicate: Func[T, BooleanType]) -> NullableType[T]:
        """Returns the last element of a sequence that satisfies a condition
        or a default value if no such element is found."""
    
    @overload
    def LastOrDefault(self, predicate: Func[T, BooleanType], defaultValue: T) -> T:
        """Returns the last element of a sequence that satisfies a condition,
        or a specified default value if no such element is found."""
    
    @overload
    def LongCount(self) -> LongType:
        """Returns an Int64 that represents the total number of elements in
        a sequence."""
    
    @overload
    def LongCount(self, predicate: Func[T, BooleanType]) -> LongType:
        """Returns an Int64 that represents how many elements in a sequence
        satisfy a condition."""
    
    @overload
    def Max(self) -> NullableType[T]:
        """Returns the maximum value in a generic sequence."""
    
    @overload
    def Max(self, comparer: NullableType[IComparer[T]]) -> NullableType[T]:
        """Returns the maximum value in a generic sequence."""
    
    @overload
    def Max(self, selector: Func[T, IntType]) -> IntType:
        """Invokes a transform function on each element of a sequence and
        returns the maximum Int32 value."""
    
    @overload
    def Max(self, selector: Func[T, LongType]) -> LongType:
        """Invokes a transform function on each element of a sequence and
        returns the maximum Int64 value."""
    
    @overload
    def Max(self, selector: Func[T, FloatType]) -> FloatType:
        """Invokes a transform function on each element of a sequence and
        returns the maximum Single value."""
    
    @overload
    def Max(self, selector: Func[T, DoubleType]) -> DoubleType:
        """Invokes a transform function on each element of a sequence and
        returns the maximum Double value."""
    
    @overload
    def Max(self, selector: Func[T, DecimalType]) -> DecimalType:
        """Invokes a transform function on each element of a sequence and
        returns the maximum Decimal value."""
    
    @overload
    def Max(self, selector: Func[T, NullableType[IntType]]) -> NullableType[IntType]:
        """Invokes a transform function on each element of a sequence and
        returns the maximum nullable Int32 value."""
    
    @overload
    def Max(self, selector: Func[T, NullableType[LongType]]) -> NullableType[LongType]:
        """Invokes a transform function on each element of a sequence and
        returns the maximum nullable Int64 value."""
    
    @overload
    def Max(self, selector: Func[T, NullableType[FloatType]]) -> NullableType[FloatType]:
        """Invokes a transform function on each element of a sequence and
        returns the maximum nullable Single value."""
    
    @overload
    def Max(self, selector: Func[T, NullableType[DoubleType]]) -> NullableType[DoubleType]:
        """Invokes a transform function on each element of a sequence and
        returns the maximum nullable Double value."""
    
    @overload
    def Max(self, selector: Func[T, NullableType[DecimalType]]) -> NullableType[DecimalType]:
        """Invokes a transform function on each element of a sequence and
        returns the maximum nullable Decimal value."""
    
    @overload
    def Max(self, selector: Func[T, TResult]) -> NullableType[TResult]:
        """Invokes a transform function on each element of a generic
        sequence and returns the maximum resulting value."""
    
    @overload
    def MaxBy(self, keySelector: Func[T, TKey]) -> NullableType[T]:
        """Returns the maximum value in a generic sequence according to a
        specified key selector function."""
    
    @overload
    def MaxBy(self, keySelector: Func[T, TKey], comparer: NullableType[IComparer[TKey]]) -> NullableType[T]:
        """Returns the maximum value in a generic sequence according to a
        specified key selector function and key comparer."""
    
    @overload
    def Min(self) -> NullableType[T]:
        """Returns the minimum value in a generic sequence."""
    
    @overload
    def Min(self, comparer: NullableType[IComparer[T]]) -> NullableType[T]:
        """Returns the minimum value in a generic sequence."""
    
    @overload
    def Min(self, selector: Func[T, IntType]) -> IntType:
        """Invokes a transform function on each element of a sequence and
        returns the minimum Int32 value."""
    
    @overload
    def Min(self, selector: Func[T, LongType]) -> LongType:
        """Invokes a transform function on each element of a sequence and
        returns the minimum Int64 value."""
    
    @overload
    def Min(self, selector: Func[T, FloatType]) -> FloatType:
        """Invokes a transform function on each element of a sequence and
        returns the minimum Single value."""
    
    @overload
    def Min(self, selector: Func[T, DoubleType]) -> DoubleType:
        """Invokes a transform function on each element of a sequence and
        returns the minimum Double value."""
    
    @overload
    def Min(self, selector: Func[T, DecimalType]) -> DecimalType:
        """Invokes a transform function on each element of a sequence and
        returns the minimum Decimal value."""
    
    @overload
    def Min(self, selector: Func[T, NullableType[IntType]]) -> NullableType[IntType]:
        """Invokes a transform function on each element of a sequence and
        returns the minimum nullable Int32 value."""
    
    @overload
    def Min(self, selector: Func[T, NullableType[LongType]]) -> NullableType[LongType]:
        """Invokes a transform function on each element of a sequence and
        returns the minimum nullable Int64 value."""
    
    @overload
    def Min(self, selector: Func[T, NullableType[FloatType]]) -> NullableType[FloatType]:
        """Invokes a transform function on each element of a sequence and
        returns the minimum nullable Single value."""
    
    @overload
    def Min(self, selector: Func[T, NullableType[DoubleType]]) -> NullableType[DoubleType]:
        """Invokes a transform function on each element of a sequence and
        returns the minimum nullable Double value."""
    
    @overload
    def Min(self, selector: Func[T, NullableType[DecimalType]]) -> NullableType[DecimalType]:
        """Invokes a transform function on each element of a sequence and
        returns the minimum nullable Decimal value."""
    
    @overload
    def Min(self, selector: Func[T, TResult]) -> NullableType[TResult]:
        """Invokes a transform function on each element of a generic
        sequence and returns the minimum resulting value."""
    
    @overload
    def MinBy(self, keySelector: Func[T, TKey]) -> NullableType[T]:
        """Returns the minimum value in a generic sequence according to a
        specified key selector function."""
    
    @overload
    def MinBy(self, keySelector: Func[T, TKey], comparer: NullableType[IComparer[TKey]]) -> NullableType[T]:
        """Returns the minimum value in a generic sequence according to a
        specified key selector function and key comparer."""
    
    def OfType(self) -> IEnumerable[TResult]:
        """Filters the elements of an IEnumerable based on a specified type."""
    
    @overload
    def OrderBy(self, keySelector: Func[T, TKey]) -> IOrderedEnumerable[T]:
        """Sorts the elements of a sequence in ascending order according to
        a key."""
    
    @overload
    def OrderBy(self, keySelector: Func[T, TKey], comparer: NullableType[IComparer[TKey]]) -> IOrderedEnumerable[T]:
        """Sorts the elements of a sequence in ascending order by using a
        specified comparer."""
    
    @overload
    def OrderByDescending(self, keySelector: Func[T, TKey]) -> IOrderedEnumerable[T]:
        """Sorts the elements of a sequence in descending order according
        to a key."""
    
    @overload
    def OrderByDescending(self, keySelector: Func[T, TKey], comparer: NullableType[IComparer[TKey]]) -> IOrderedEnumerable[T]:
        """Sorts the elements of a sequence in descending order by using a
        specified comparer."""
    
    def Prepend(self, element: T) -> IEnumerable[T]:
        """Adds a value to the beginning of the sequence."""
    
    def Reverse(self) -> IEnumerable[T]:
        """Inverts the order of the elements in a sequence."""
    
    @overload
    def Select(self, selector: Func[T, TResult]) -> IEnumerable[TResult]:
        """Projects each element of a sequence into a new form."""
    
    @overload
    def Select(self, selector: Func[T, IntType, TResult]) -> IEnumerable[TResult]:
        """Projects each element of a sequence into a new form by
        incorporating the element's index."""
    
    @overload
    def SelectMany(self, selector: Func[T, IEnumerable[TResult]]) -> IEnumerable[TResult]:
        """Projects each element of a sequence to an IEnumerable[T] and
        flattens the resulting sequences into one sequence."""
    
    @overload
    def SelectMany(self, selector: Func[T, IntType, IEnumerable[TResult]]) -> IEnumerable[TResult]:
        """Projects each element of a sequence to an IEnumerable[T], and
        flattens the resulting sequences into one sequence. The index of
        each source element is used in the projected form of that element."""
    
    @overload
    def SelectMany(self, collectionSelector: Func[T, IEnumerable[TCollection]], resultSelector: Func[T, TCollection, TResult]) -> IEnumerable[TResult]:
        """Projects each element of a sequence to an IEnumerable[T], flattens
        the resulting sequences into one sequence, and invokes a result selector
        function on each element therein."""
    
    @overload
    def SelectMany(self, collectionSelector: Func[T, IntType, IEnumerable[TCollection]], resultSelector: Func[T, TCollection, TResult]) -> IEnumerable[TResult]:
        """Projects each element of a sequence to an IEnumerable[T], flattens the
        resulting sequences into one sequence, and invokes a result selector
        function on each element therein. The index of each source element is
        used in the intermediate projected form of that element."""
    
    @overload
    def SequenceEqual(self, second: IEnumerable[T]) -> BooleanType:
        """Determines whether two sequences are equal by comparing the
        elements by using the default equality comparer for their type."""
    
    @overload
    def SequenceEqual(self, second: IEnumerable[T], comparer: NullableType[IEqualityComparer[T]]) -> BooleanType:
        """Determines whether two sequences are equal by comparing their
        elements by using a specified IEqualityComparer[T]."""
    
    @overload
    def Single(self) -> T:
        """Returns the only element of a sequence, and throws an exception
        if there is not exactly one element in the sequence."""
    
    @overload
    def Single(self, predicate: Func[T, BooleanType]) -> T:
        """Returns the only element of a sequence that satisfies a specified
        condition, and throws an exception if more than one such element
        exists."""
    
    @overload
    def SingleOrDefault(self) -> NullableType[T]:
        """Returns the only element of a sequence, or a default value if the
        sequence is empty; this method throws an exception if there is more
        than one element in the sequence."""
    
    @overload
    def SingleOrDefault(self, defaultValue: T) -> NullableType[T]:
        """Returns the only element of a sequence, or a specified default
        value if the sequence is empty; this method throws an exception if
        there is more than one element in the sequence."""
    
    @overload
    def SingleOrDefault(self, predicate: Func[T, BooleanType]) -> NullableType[T]:
        """Returns the only element of a sequence that satisfies a specified
        condition or a default value if no such element exists; this method
        throws an exception if more than one element satisfies the condition."""
    
    @overload
    def SingleOrDefault(self, predicate: Func[T, BooleanType], defaultValue: T) -> NullableType[T]:
        """Returns the only element of a sequence that satisfies a specified
        condition, or a specified default value if no such element exists;
        this method throws an exception if more than one element satisfies
        the condition."""
    
    def Skip(self, count: IntType) -> IEnumerable[T]:
        """Bypasses a specified number of elements in a sequence and then
        returns the remaining elements."""
    
    def SkipLast(self, count: IntType) -> IEnumerable[T]:
        """Returns a new enumerable collection that contains the elements
        from source with the last count elements of the source collection
        omitted."""
    
    @overload
    def SkipWhile(self, predicate: Func[T, BooleanType]) -> IEnumerable[T]:
        """Bypasses elements in a sequence as long as a specified condition
        is true and then returns the remaining elements."""
    
    @overload
    def SkipWhile(self, predicate: Func[T, IntType, BooleanType]) -> IEnumerable[T]:
        """Bypasses elements in a sequence as long as a specified condition
        is true and then returns the remaining elements. The element's index
        is used in the logic of the predicate function."""
    
    @overload
    def Sum(self, selector: Func[T, IntType]) -> IntType:
        """Computes the sum of the sequence of Int32 values that are
        obtained by invoking a transform function on each element of the
        input sequence."""
    
    @overload
    def Sum(self, selector: Func[T, LongType]) -> LongType:
        """Computes the sum of the sequence of Int64 values that are obtained
        by invoking a transform function on each element of the input
        sequence."""
    
    @overload
    def Sum(self, selector: Func[T, FloatType]) -> FloatType:
        """Computes the sum of the sequence of Single values that are
        obtained by invoking a transform function on each element of the
        input sequence."""
    
    @overload
    def Sum(self, selector: Func[T, DoubleType]) -> DoubleType:
        """Computes the sum of the sequence of Double values that are
        obtained by invoking a transform function on each element of the
        input sequence."""
    
    @overload
    def Sum(self, selector: Func[T, DecimalType]) -> DecimalType:
        """Computes the sum of the sequence of Decimal values that are
        obtained by invoking a transform function on each element of the
        input sequence."""
    
    @overload
    def Sum(self, selector: Func[T, NullableType[IntType]]) -> NullableType[IntType]:
        """Computes the sum of the sequence of nullable Int32 values that are
        obtained by invoking a transform function on each element of the
        input sequence."""
    
    @overload
    def Sum(self, selector: Func[T, NullableType[LongType]]) -> NullableType[LongType]:
        """Computes the sum of the sequence of nullable Int64 values that
        are obtained by invoking a transform function on each element of the
        input sequence."""
    
    @overload
    def Sum(self, selector: Func[T, NullableType[FloatType]]) -> NullableType[FloatType]:
        """Computes the sum of the sequence of nullable Single values that
        are obtained by invoking a transform function on each element of the
        input sequence."""
    
    @overload
    def Sum(self, selector: Func[T, NullableType[DoubleType]]) -> NullableType[DoubleType]:
        """Computes the sum of the sequence of nullable Double values that
        are obtained by invoking a transform function on each element of the
        input sequence."""
    
    @overload
    def Sum(self, selector: Func[T, NullableType[DecimalType]]) -> NullableType[DecimalType]:
        """Computes the sum of the sequence of nullable Decimal values that
        are obtained by invoking a transform function on each element of the
        input sequence."""
    
    @overload
    def Take(self, count: IntType) -> IEnumerable[T]:
        """Returns a specified number of contiguous elements from the start
        of a sequence."""
    
    @overload
    def Take(self, range: Range) -> IEnumerable[T]:
        """Returns a specified range of contiguous elements from a sequence."""
    
    def TakeLast(self, count: IntType) -> IEnumerable[T]:
        """Returns a new enumerable collection that contains the last count
        elements from source."""
    
    @overload
    def TakeWhile(self, predicate: Func[T, BooleanType]) -> IEnumerable[T]:
        """Returns elements from a sequence as long as a specified condition
        is true."""
    
    @overload
    def TakeWhile(self, predicate: Func[T, IntType, BooleanType]) -> IEnumerable[T]:
        """Returns elements from a sequence as long as a specified condition
        is true. The element's index is used in the logic of the predicate
        function."""
    
    def ToArray(self) -> ArrayType[T]:
        """Creates an array from a IEnumerable[T]."""
    
    @overload
    def ToDictionary(self, keySelector: Func[T, TKey]) -> Dictionary[TKey, T]:
        """Creates a Dictionary[TKey,TValue] from an IEnumerable[T] according
        to a specified key selector function."""
    
    @overload
    def ToDictionary(self, keySelector: Func[T, TKey], comparer: NullableType[IEqualityComparer[TKey]]) -> Dictionary[TKey, T]:
        """Creates a Dictionary[TKey,TValue] from an IEnumerable[T] according
        to a specified key selector function and key comparer."""
    
    @overload
    def ToDictionary(self, keySelector: Func[T, TKey], elementSelector: Func[T, TElement]) -> Dictionary[TKey, TElement]:
        """Creates a Dictionary[TKey,TValue] from an IEnumerable[T] according
        to specified key selector and element selector functions."""
    
    @overload
    def ToDictionary(self, keySelector: Func[T, TKey], elementSelector: Func[T, TElement], comparer: NullableType[IEqualityComparer[TKey]]) -> Dictionary[TKey, TElement]:
        """Creates a Dictionary[TKey,TValue] from an IEnumerable[T] according
        to a specified key selector function, a comparer, and an element
        selector function."""
    
    @overload
    def ToHashSet(self) -> HashSet[T]:
        """Creates a HashSet[T] from an IEnumerable[T]."""
    
    @overload
    def ToHashSet(self, comparer: NullableType[IEqualityComparer[T]]) -> HashSet[T]:
        """Creates a HashSet[T] from an IEnumerable[T] using the comparer to
        compare keys."""
    
    def ToList(self) -> List[T]:
        """Creates a List[T] from an IEnumerable[T]."""
    
    @overload
    def ToLookup(self, keySelector: Func[T, TKey]) -> ILookup[TKey, T]:
        """Creates a Lookup[TKey,TElement] from an IEnumerable[T] according
        to a specified key selector function."""
    
    @overload
    def ToLookup(self, keySelector: Func[T, TKey], comparer: NullableType[IEqualityComparer[TKey]]) -> ILookup[TKey, T]:
        """Creates a Lookup[TKey,TElement] from an IEnumerable[T] according
        to a specified key selector function and key comparer."""
    
    @overload
    def ToLookup(self, keySelector: Func[T, TKey], elementSelector: Func[T, TElement]) -> ILookup[TKey, TElement]:
        """Creates a Lookup[TKey,TElement] from an IEnumerable[T] according
        to specified key selector and element selector functions."""
    
    @overload
    def ToLookup(self, keySelector: Func[T, TKey], elementSelector: Func[T, TElement], comparer: NullableType[IEqualityComparer[TKey]]) -> ILookup[TKey, TElement]:
        """Creates a Lookup[TKey,TElement] from an IEnumerable[T] according
        to a specified key selector function, a comparer and an element
        selector function."""
    
    def TryGetNonEnumeratedCount(self, count: Int32) -> BooleanType:
        """Attempts to determine the number of elements in a sequence
        without forcing an enumeration."""
    
    @overload
    def Union(self, second: IEnumerable[T]) -> IEnumerable[T]:
        """Produces the set union of two sequences by using the default
        equality comparer."""
    
    @overload
    def Union(self, second: IEnumerable[T], comparer: NullableType[IEqualityComparer[T]]) -> IEnumerable[T]:
        """Produces the set union of two sequences by using a specified
        IEqualityComparer[T]."""
    
    @overload
    def UnionBy(self, second: IEnumerable[T], keySelector: Func[T, TKey]) -> IEnumerable[T]:
        """Produces the set union of two sequences according to a specified
        key selector function."""
    
    @overload
    def UnionBy(self, second: IEnumerable[T], keySelector: Func[T, TKey], comparer: NullableType[IEqualityComparer[T]]) -> IEnumerable[T]:
        """Produces the set union of two sequences according to a specified
        key selector function."""
    
    @overload
    def Where(self, predicate: Func[T, BooleanType]) -> IEnumerable[T]:
        """Filters a sequence of values based on a predicate."""
    
    @overload
    def Where(self, predicate: Func[T, IntType, BooleanType]) -> IEnumerable[T]:
        """Filters a sequence of values based on a predicate. Each element's
        index is used in the logic of the predicate function."""
    
    @overload
    def Zip(self, second: IEnumerable[TSecond]) -> IEnumerable[Tuple[T, TSecond]]:
        """Produces a sequence of tuples with elements from the two specified
        sequences."""
    
    @overload
    def Zip(self, second: IEnumerable[TSecond], third: IEnumerable[TThird]) -> IEnumerable[Tuple[T, TSecond, TThird]]:
        """Produces a sequence of tuples with elements from the three
        specified sequences."""
    
    @overload
    def Zip(self, second: IEnumerable[TSecond], resultSelector: Func[T, TSecond, TResult]) -> IEnumerable[TResult]:
        """Applies a specified function to the corresponding elements of two
        sequences, producing a sequence of the results."""
    
    @overload
    def AsParallel(self) -> ParallelQuery[T]:
        """Enables parallelization of a query."""
    
    @overload
    def AsQueryable(self) -> IQueryable[T]:
        """Converts a generic IEnumerable[T] to a generic IQueryable[T]."""
    
    @overload
    def Ancestors(self: IEnumerable[NullableType[TXNode]]) -> IEnumerable[XElement]:
        """Returns a collection of elements that contains the ancestors of
        every node in the source collection."""
    
    @overload
    def Ancestors(self: IEnumerable[NullableType[TXNode]], name: NullableType[XName]) -> IEnumerable[XElement]:
        """Returns a filtered collection of elements that contains the
        ancestors of every node in the source collection. Only elements that
        have a matching XName are included in the collection."""
    
    def DescendantNodes(self: IEnumerable[NullableType[TXContainer]]) -> IEnumerable[XNode]:
        """Returns a collection of the descendant nodes of every document
        and element in the source collection."""
    
    @overload
    def Descendants(self: IEnumerable[NullableType[TXContainer]]) -> IEnumerable[XElement]:
        """Returns a collection of elements that contains the descendant
        elements of every element and document in the source collection."""
    
    @overload
    def Descendants(self: IEnumerable[NullableType[TXContainer]], name: NullableType[XName]) -> IEnumerable[XElement]:
        """Returns a filtered collection of elements that contains the
        descendant elements of every element and document in the source
        collection. Only elements that have a matching XName are included in
        the collection."""
    
    @overload
    def Elements(self: IEnumerable[NullableType[TXContainer]]) -> IEnumerable[XElement]:
        """Returns a collection of the child elements of every element and
        document in the source collection."""
    
    @overload
    def Elements(self: IEnumerable[NullableType[TXContainer]], name: NullableType[XName]) -> IEnumerable[XElement]:
        """Returns a filtered collection of the child elements of every
        element and document in the source collection. Only elements that
        have a matching XName are included in the collection."""
    
    def InDocumentOrder(self: IEnumerable[TXNode]) -> IEnumerable[TXNode]:
        """Returns a collection of nodes that contains all nodes in the
        source collection, sorted in document order."""
    
    def Nodes(self: IEnumerable[NullableType[TXContainer]]) -> IEnumerable[XNode]:
        """Returns a collection of the child nodes of every document and
        element in the source collection."""
    
    def Remove(self: IEnumerable[NullableType[TXNode]]) -> VoidType:
        """Removes every node in the source collection from its parent node."""


class IEnumerator(Protocol[T], IDisposable, _IEnumerator):
    """Supports a simple iteration over a generic collection."""
    
    @property
    def Current(self) -> T:
        """Gets the element in the collection at the current position of the
        enumerator."""


class IEqualityComparer(Protocol[T]):
    """Defines methods to support the comparison of objects for equality."""
    
    def Equals(self, x: NullableType[T], y: NullableType[T]) -> BooleanType:
        """Determines whether the specified objects are equal."""
    
    def GetHashCode(self, obj: T) -> IntType:
        """Returns a hash code for the specified object."""


class IList(Protocol[T], ICollection[T]):
    """Represents a collection of objects that can be individually accessed
    by index."""
    
    @property
    def Item(self) -> Item[IntType, T]:
        """Gets or sets the element at the specified index."""
    
    def __getitem__(self, key: IntType) -> T: ...
    
    def __setitem__(self, key: IntType, value: T) -> None: ...
    
    def IndexOf(self, item: T) -> IntType:
        """Determines the index of a specific item in the IList[T]."""
    
    def Insert(self, index: IntType, item: T) -> VoidType:
        """Inserts an item to the IList[T] at the specified index."""
    
    def RemoveAt(self, index: IntType) -> VoidType:
        """Removes the IList[T] item at the specified index."""


class IReadOnlyCollection(Protocol[T], IEnumerable[T]):
    """Represents a strongly-typed, read-only collection of elements."""
    
    @property
    def Count(self) -> IntType:
        """Gets the number of elements in the collection."""


class IReadOnlyDictionary(Protocol[TKey, TValue], IReadOnlyCollection[KeyValuePair[TKey, TValue]]):
    """Represents a generic read-only collection of key/value pairs."""
    
    @property
    def Item(self) -> ReadOnlyItem[TKey, TValue]:
        """Gets the element that has the specified key in the read-only
        dictionary."""
    
    def __getitem__(self, key: TKey) -> TValue: ...
    
    @property
    def Keys(self) -> IEnumerable[TKey]:
        """Gets an enumerable collection that contains the keys in the
        read-only dictionary."""
    
    @property
    def Values(self) -> IEnumerable[TValue]:
        """Gets an enumerable collection that contains the values in the
        read-only dictionary."""
    
    def ContainsKey(self, key: TKey) -> BooleanType:
        """Determines whether the read-only dictionary contains an element
        that has the specified key."""
    
    def TryGetValue(self, key: TKey, value: TValue) -> BooleanType:
        """Gets the value that is associated with the specified key."""
    
    @overload
    def GetValueOrDefault(self, key: TKey) -> NullableType[TValue]:
        """Tries to get the value associated with the specified key in the
        dictionary."""
    
    @overload
    def GetValueOrDefault(self, key: TKey, defaultValue: TValue) -> TValue:
        """Tries to get the value associated with the specified key in the
        dictionary."""


class IReadOnlyList(Protocol[T], IReadOnlyCollection[T]):
    """Represents a read-only collection of elements that can be accessed
    by index."""
    
    @property
    def Item(self) -> ReadOnlyItem[IntType, T]:
        """Gets the element at the specified index in the read-only list."""
    
    def __getitem__(self, key: IntType) -> T: ...


class IReadOnlySet(Protocol[T], IReadOnlyCollection[T]):
    """Provides a readonly abstraction of a set."""
    
    def IsProperSubsetOf(self, other: IEnumerable[T]) -> BooleanType:
        """Determines whether the current set is a proper (strict) subset of
        a specified collection."""
    
    def IsProperSupersetOf(self, other: IEnumerable[T]) -> BooleanType:
        """Determines whether the current set is a proper (strict) superset
        of a specified collection."""
    
    def IsSubsetOf(self, other: IEnumerable[T]) -> BooleanType:
        """Determine whether the current set is a subset of a specified
        collection."""
    
    def IsSupersetOf(self, other: IEnumerable[T]) -> BooleanType:
        """Determine whether the current set is a super set of a specified
        collection."""
    
    def Overlaps(self, other: IEnumerable[T]) -> BooleanType:
        """Determines whether the current set overlaps with the specified
        collection."""
    
    def SetEquals(self, other: IEnumerable[T]) -> BooleanType:
        """Determines whether the current set and the specified collection
        contain the same elements."""


class ISet(Protocol[T], ICollection[T]):
    """Provides the base interface for the abstraction of sets."""
    
    def ExceptWith(self, other: IEnumerable[T]) -> VoidType:
        """Removes all elements in the specified collection from the current
        set."""
    
    def IntersectWith(self, other: IEnumerable[T]) -> VoidType:
        """Modifies the current set so that it contains only elements that
        are also in a specified collection."""
    
    def IsProperSubsetOf(self, other: IEnumerable[T]) -> BooleanType:
        """Determines whether the current set is a proper (strict) subset
        of a specified collection."""
    
    def IsProperSupersetOf(self, other: IEnumerable[T]) -> BooleanType:
        """Determines whether the current set is a proper (strict) superset
        of a specified collection."""
    
    def IsSubsetOf(self, other: IEnumerable[T]) -> BooleanType:
        """Determines whether a set is a subset of a specified collection."""
    
    def IsSupersetOf(self, other: IEnumerable[T]) -> BooleanType:
        """Determines whether the current set is a superset of a specified
        collection."""
    
    def Overlaps(self, other: IEnumerable[T]) -> BooleanType:
        """Determines whether the current set overlaps with the specified
        collection."""
    
    def SetEquals(self, other: IEnumerable[T]) -> BooleanType:
        """Determines whether the current set and the specified collection
        contain the same elements."""
    
    def SymmetricExceptWith(self, other: IEnumerable[T]) -> VoidType:
        """Modifies the current set so that it contains only elements that
        are present either in the current set or in the specified collection,
        but not both."""
    
    def UnionWith(self, other: IEnumerable[T]) -> VoidType:
        """Modifies the current set so that it contains all elements that
        are present in the current set, in the specified collection, or in
        both."""
