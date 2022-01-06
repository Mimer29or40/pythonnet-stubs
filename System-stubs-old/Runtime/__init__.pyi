__all__ = [
    'AmbiguousImplementationException',
    'AssemblyTargetedPatchBandAttribute',
    'GCSettings',
    'JitInfo',
    'MemoryFailPoint',
    'ProfileOptimization',
    'TargetedPatchingOptOutAttribute',
    'DependentHandle',
    'GCLargeObjectHeapCompactionMode',
    'GCLatencyMode',
]

from typing import TypeVar

T = TypeVar('T')
TKey = TypeVar('TKey')
TValue = TypeVar('TValue')


# TODO
# class ArraySegment(ValueType, ICollection[T], IEnumerable[T], IList[T], IReadOnlyCollection[T], IReadOnlyList[T], IEnumerable, Generic[T]):
#     pass
#
#
# class DateTime(ValueType, IComparable[DateTime], IConvertible, IEquatable[DateTime], ISpanFormattable, ISerializable):
#     """Represents an instant in time, typically expressed as a date and time of day."""
#
#
# class IFormattable(ABC):
#     """Provides functionality to format the value of an object into a string representation."""
#
#     @abstractmethod
#     def ToString(self, format: Optional[str], formatProvider: Optional[IFormatProvider]) -> str:
#         """Formats the value of the current instance using the specified format."""
#
#
# class ISpanFormattable(IFormattable, ABC):
#     """Provides functionality to format the string representation of an object into a span."""
#
#     @abstractmethod
#     def TryFormat(self, destination: Span[Char], charsWritten: Int32, format: ReadOnlySpan[Char], provider: Optional[IFormatProvider]) -> bool:
#         """Tries to format the value of the current instance into the provided span of characters."""
#
#
# class ReadOnlySpan(ValueType, Generic[T]):  # TODO
#     """Provides a type-safe and memory-safe read-only representation of a contiguous region of arbitrary memory."""
#
#     # CONSTRUCTORS
#     # ReadOnlySpan[T](T[])
#     # Creates a new ReadOnlySpan[T] over the entirety of a specified array.
#     #
#     # ReadOnlySpan[T](T[], Int32, Int32)
#     # Creates a new ReadOnlySpan[T] that includes a specified number of elements of an array starting at a specified index.
#     #
#     # ReadOnlySpan[T](Void*, Int32)
#     # Creates a new ReadOnlySpan[T] from a specified number of T elements starting at a specified memory address.
#     #
#     # Properties
#     # PROPERTIES
#     # Empty
#     # Returns an empty ReadOnlySpan[T].
#     #
#     # IsEmpty
#     # Returns a value that indicates the current read-only span is empty.
#     #
#     # Item[Int32]
#     # Gets an item from the read-only span at the specified zero-based index.
#     #
#     # Length
#     # The number of items in the read-only span.
#     #
#     # Methods
#     # METHODS
#     # CopyTo(Span[T])
#     # Copies the contents of this ReadOnlySpan[T] into a destination Span[T].
#     #
#     # Equals(Object)
#     # Obsolete.
#     # Not supported. Throws a NotSupportedException.
#     #
#     # GetEnumerator()
#     # Returns an enumerator for this ReadOnlySpan[T].
#     #
#     # GetHashCode()
#     # Obsolete.
#     # Not supported. Throws a NotSupportedException.
#     #
#     # GetPinnableReference()
#     # Returns a read-only reference to an object of type T that can be used for pinning.
#     #
#     # This method is intended to support .NET compilers and is not intended to be called by user code.
#     #
#     # Slice(Int32)
#     # Forms a slice out of the current read-only span that begins at a specified index.
#     #
#     # Slice(Int32, Int32)
#     # Forms a slice out of the current read-only span starting at a specified index for a specified length.
#     #
#     # ToArray()
#     # Copies the contents of this read-only span into a new array.
#     #
#     # ToString()
#     # Returns the string representation of this ReadOnlySpan[T].
#     #
#     # TryCopyTo(Span[T])
#     # Attempts to copy the contents of this ReadOnlySpan[T] into a Span[T] and returns a value to indicate whether or not the operation succeeded.
#     #
#     # Operators
#     # OPERATORS
#     # Equality(ReadOnlySpan[T], ReadOnlySpan[T])
#     # Returns a value that indicates whether two ReadOnlySpan[T] instances are equal.
#     #
#     # Implicit(ArraySegment[T] to ReadOnlySpan[T])
#     # Defines an implicit conversion of an ArraySegment[T] to a ReadOnlySpan[T].
#     #
#     # Implicit(T[] to ReadOnlySpan[T])
#     # Defines an implicit conversion of an array to a ReadOnlySpan[T].
#     #
#     # Inequality(ReadOnlySpan[T], ReadOnlySpan[T])
#     # Returns a value that indicates whether two ReadOnlySpan[T] instances are not equal.
#     #
#     # Extension Methods
#     # EXTENSION METHODS
#     # BinarySearch[T](ReadOnlySpan[T], IComparable[T])
#     # Searches an entire sorted ReadOnlySpan[T] for a value using the specified IComparable[T] generic interface.
#     #
#     # BinarySearch<T,TComparer>(ReadOnlySpan[T], T, TComparer)
#     # Searches an entire sorted ReadOnlySpan[T] for a specified value using the specified TComparer generic type.
#     #
#     # BinarySearch<T,TComparable>(ReadOnlySpan[T], TComparable)
#     # Searches an entire sorted ReadOnlySpan[T] for a value using the specified TComparable generic type.
#     #
#     # Contains[T](ReadOnlySpan[T], T)
#     # Indicates whether a specified value is found in a read-only span. Values are compared using IEquatable{T}.Equals(T).
#     #
#     # EndsWith[T](ReadOnlySpan[T], ReadOnlySpan[T])
#     # Determines whether the specified sequence appears at the end of a read-only span.
#     #
#     # IndexOf[T](ReadOnlySpan[T], T)
#     # Searches for the specified value and returns the index of its first occurrence. Values are compared using IEquatable{T}.Equals(T).
#     #
#     # IndexOf[T](ReadOnlySpan[T], ReadOnlySpan[T])
#     # Searches for the specified sequence and returns the index of its first occurrence. Values are compared using IEquatable{T}.Equals(T).
#     #
#     # IndexOfAny[T](ReadOnlySpan[T], T, T)
#     # Searches for the first index of any of the specified values similar to calling IndexOf several times with the logical OR operator.
#     #
#     # IndexOfAny[T](ReadOnlySpan[T], T, T, T)
#     # Searches for the first index of any of the specified values similar to calling IndexOf several times with the logical OR operator.
#     #
#     # IndexOfAny[T](ReadOnlySpan[T], ReadOnlySpan[T])
#     # Searches for the first index of any of the specified values similar to calling IndexOf several times with the logical OR operator.
#     #
#     # LastIndexOf[T](ReadOnlySpan[T], T)
#     # Searches for the specified value and returns the index of its last occurrence. Values are compared using IEquatable{T}.Equals(T).
#     #
#     # LastIndexOf[T](ReadOnlySpan[T], ReadOnlySpan[T])
#     # Searches for the specified sequence and returns the index of its last occurrence. Values are compared using IEquatable{T}.Equals(T).
#     #
#     # LastIndexOfAny[T](ReadOnlySpan[T], T, T)
#     # Searches for the last index of any of the specified values similar to calling LastIndexOf several times with the logical OR operator.
#     #
#     # LastIndexOfAny[T](ReadOnlySpan[T], T, T, T)
#     # Searches for the last index of any of the specified values similar to calling LastIndexOf several times with the logical OR operator.
#     #
#     # LastIndexOfAny[T](ReadOnlySpan[T], ReadOnlySpan[T])
#     # Searches for the last index of any of the specified values similar to calling LastIndexOf several times with the logical OR operator.
#     #
#     # Overlaps[T](ReadOnlySpan[T], ReadOnlySpan[T])
#     # Determines whether two read-only sequences overlap in memory.
#     #
#     # Overlaps[T](ReadOnlySpan[T], ReadOnlySpan[T], Int32)
#     # Determines whether two read-only sequences overlap in memory and outputs the element offset.
#     #
#     # SequenceCompareTo[T](ReadOnlySpan[T], ReadOnlySpan[T])
#     # Determines the relative order of two read-only sequences by comparing their elements using IComparable{T}.CompareTo(T).
#     #
#     # SequenceEqual[T](ReadOnlySpan[T], ReadOnlySpan[T])
#     # Determines whether two read-only sequences are equal by comparing the elements using IEquatable{T}.Equals(T).
#     #
#     # SequenceEqual[T](ReadOnlySpan<T>, ReadOnlySpan<T>, IEqualityComparer<T>)
#     # Determines whether two sequences are equal by comparing the elements using an IEqualityComparer<T>.
#     #
#     # StartsWith<T>(ReadOnlySpan<T>, ReadOnlySpan<T>)
#     # Determines whether a specified sequence appears at the start of a read-only span.
#     #
#     # Trim<T>(ReadOnlySpan<T>, T)
#     # Removes all leading and trailing occurrences of a specified element from a read-only span.
#     #
#     # Trim<T>(ReadOnlySpan<T>, ReadOnlySpan<T>)
#     # Removes all leading and trailing occurrences of a set of elements specified in a read-only span from a read-only span.
#     #
#     # TrimEnd<T>(ReadOnlySpan<T>, T)
#     # Removes all trailing occurrences of a specified element from a read-only span.
#     #
#     # TrimEnd<T>(ReadOnlySpan<T>, ReadOnlySpan<T>)
#     # Removes all trailing occurrences of a set of elements specified in a read-only span from a read-only span.
#     #
#     # TrimStart<T>(ReadOnlySpan<T>, T)
#     # Removes all leading occurrences of a specified element from the span.
#     #
#     # TrimStart<T>(ReadOnlySpan<T>, ReadOnlySpan<T>)
#     # Removes all leading occurrences of a set of elements specified in a read-only span from the span.
#
#
# class RuntimeMethodHandle:  # TODO
#     pass
#
#
# class Span(ValueType, Generic[T]):
#     """Provides a type- and memory-safe representation of a contiguous region of arbitrary memory."""
#
#     @overload
#     def __init__(self, array: Optional[T]):
#         """Creates a new Span[T] object over the entirety of a specified array."""
#
#     @overload
#     def __init__(self, array: Optional[T], start: int, length: int):
#         """Creates a new Span[T] object that includes a specified number of elements of an array starting at a specified index."""
#
#     @overload
#     def __init__(self, pointer: int, length: int):
#         """Creates a new Span[T] object from a specified number of T elements starting at a specified memory address."""
#
#     def __init__(self, *args, **kwargs): ...
#
#     @classmethod
#     @property
#     def Empty(cls) -> Span[T]:
#         """Returns an empty Span[T] object."""
#
#     @property
#     def IsEmpty(self) -> bool:
#         """Returns a value that indicates whether the current Span[T] is empty."""
#
#     @property
#     def Item(self, item: int) -> T:
#         """Gets the element at the specified zero-based index."""
#
#     def __getitem__(self, item) -> Union[T, Span[T]]: ...
#
#     @property
#     def Length(self) -> int:
#         """Returns the length of the current span."""
#
#     __len__ = Length
#
#     def Clear(self) -> None:
#         """Clears the contents of this Span[T] object."""
#
#     def CopyTo(self, destination: Span[T]) -> None:
#         """Copies the contents of this Span[T] into a destination Span[T]."""
#
#     def Equals(self, obj: Object) -> Obsolete:
#         """Obsolete. Calls to this method are not supported."""
#
#     def Fill(self, value: T) -> None:
#         """Fills the elements of this span with a specified value."""
#
#     def GetEnumerator(self) -> Span[T].Enumerator:
#         """Returns an enumerator for this Span[T]."""
#
#     def GetHashCode(self) -> Obsolete:
#         """Obsolete. Throws a NotSupportedException."""
#
#     def GetPinnableReference(self) -> T:
#         """Returns a reference to an object of type T that can be used for pinning.
#
#         This method is intended to support .NET compilers and is not intended to be called by user code.
#         """
#
#     @overload
#     def Slice(self, start: int) -> Span[T]:
#         """Forms a slice out of the current span that begins at a specified index."""
#
#     @overload
#     def Slice(self, start: int, length: int) -> Span[T]:
#         """Forms a slice out of the current span starting at a specified index for a specified length."""
#
#     def Slice(self, *args, **kwargs) -> Span[T]: ...
#
#     def ToArray(self) -> Array[T]:
#         """Copies the contents of this span into a new array."""
#
#     def TryCopyTo(self, destination: Span[T]) -> bool:
#         """Attempts to copy the current Span[T] to a destination Span[T] and
#         returns a value that indicates whether the copy operation succeeded.
#         """
#
#     @staticmethod
#     def Equality(left: Span[T], right: Span[T]) -> bool:
#         """Returns a value that indicates whether two Span[T] objects are equal."""
#
#     __eq__ = Equality
#
#     @staticmethod
#     @overload
#     def Implicit(segment: ArraySegment[T]) -> Span[T]:
#         """Defines an implicit conversion of an ArraySegment[T] to a Span[T]."""
#
#     @staticmethod
#     @overload
#     def Implicit(span: Span[T]) -> ReadOnlySpan[T]:
#         """Defines an implicit conversion of a Span[T] to a ReadOnlySpan[T]."""
#
#     @staticmethod
#     @overload
#     def Implicit(array: Optional[Array[T]]) -> Span[T]:
#         """Defines an implicit conversion of an array to a Span[T]."""
#
#     @staticmethod
#     def Implicit(value): ...
#
#     @staticmethod
#     def Inequality(left: Span[T], right: Span[T]) -> bool:
#         """Returns a value that indicates whether two Span[T] objects are not equal."""
#
#     __ne__ = Inequality
#
#     @overload
#     def BinarySearch(self, comparable: IComparable[T]) -> int:
#         """Searches an entire sorted Span[T] for a value using the specified IComparable[T] generic interface."""
#
#     @overload
#     def BinarySearch(self, value: T, comparer: IComparer[T]) -> int:
#         """Searches an entire sorted Span[T] for a specified value using the specified TComparer generic type."""
#
#     def Contains(self, value: IEquatable[T]) -> bool:
#         """Indicates whether a specified value is found in a span. Values are compared using IEquatable{T}.Equals(T)."""
#
#     def EndsWith(self, value: ReadOnlySpan[IEquatable[T]]) -> bool:
#         """Determines whether the specified sequence appears at the end of a span."""
#
#     @overload
#     def IndexOf(self, value: IEquatable[T]) -> int:
#         """Searches for the specified value and returns the index of its first occurrence. Values are compared using IEquatable{T}.Equals(T)."""
#
#     @overload
#     def IndexOf(self, value: ReadOnlySpan[IEquatable[T]]) -> int:
#         """Searches for the specified sequence and returns the index of its first occurrence. Values are compared using IEquatable{T}.Equals(T)."""
#
#     @overload
#     def IndexOfAny(self, value0: IEquatable[T], value1: IEquatable[T]) -> int:
#         """Searches for the first index of any of the specified values similar to calling IndexOf several times with the logical OR operator."""
#
#     @overload
#     def IndexOfAny(self, value0: IEquatable[T], value1: IEquatable[T], value2: IEquatable[T]) -> int:
#         """Searches for the first index of any of the specified values similar to calling IndexOf several times with the logical OR operator."""
#
#     @overload
#     def IndexOfAny(self, values: ReadOnlySpan[IEquatable[T]]) -> int:
#         """Searches for the first index of any of the specified values similar to calling IndexOf several times with the logical OR operator."""
#
#     @overload
#     def LastIndexOf(self, value: IEquatable[T]) -> int:
#         """Searches for the specified value and returns the index of its last occurrence. Values are compared using IEquatable{T}.Equals(T)."""
#
#     @overload
#     def LastIndexOf(self, value: ReadOnlySpan[IEquatable[T]]) -> int:
#         """Searches for the specified sequence and returns the index of its last occurrence. Values are compared using IEquatable{T}.Equals(T)."""
#
#     @overload
#     def LastIndexOfAny(self, value0: IEquatable[T], value1: IEquatable[T]) -> int:
#         """Searches for the last index of any of the specified values similar to calling LastIndexOf several times with the logical OR operator."""
#
#     @overload
#     def LastIndexOfAny(self, value0: IEquatable[T], value1: IEquatable[T], value2: IEquatable[T]) -> int:
#         """Searches for the last index of any of the specified values similar to calling LastIndexOf several times with the logical OR operator."""
#
#     @overload
#     def LastIndexOfAny(self, values: ReadOnlySpan[IEquatable[T]]) -> int:
#         """Searches for the last index of any of the specified values similar to calling LastIndexOf several times with the logical OR operator."""
#
#     @overload
#     def Overlaps(self, other: ReadOnlySpan[T]) -> int:
#         """Determines whether a span and a read-only span overlap in memory."""
#
#     @overload
#     def Overlaps(self, other: ReadOnlySpan[T], elementOffset: int) -> int:
#         """Determines whether a span and a read-only span overlap in memory and outputs the element offset."""
#
#     def Reverse(self) -> None:
#         """Reverses the sequence of the elements in the entire span."""
#
#     def SequenceCompareTo(self, other: ReadOnlySpan[IComparable[T]]) -> int:
#         """Determines the relative order of a span and a read-only span by comparing the elements using IComparable{T}.CompareTo(T)."""
#
#     @overload
#     def SequenceEqual(self, other: ReadOnlySpan[IEquatable[T]]) -> bool:
#         """Determines whether a span and a read-only span are equal by comparing the elements using IEquatable{T}.Equals(T)."""
#
#     @overload
#     def SequenceEqual(self, other: ReadOnlySpan[T], comparer: IEqualityComparer[T] = None) -> bool:
#         """Determines whether two sequences are equal by comparing the elements using an IEqualityComparer[T]."""
#
#     @overload
#     def Sort(self) -> None:
#         """Sorts the elements in the entire Span[T] using the IComparable[T] implementation of each element of the Span[T]."""
#
#     @overload
#     def Sort(self, comparison: Comparison[T]) -> None:
#         """Sorts the elements in the entire Span[T] using the specified Comparison[T]."""
#
#     @overload
#     def Sort(self, comparer: IComparer[T]) -> None:
#         """Sorts the elements in the entire Span[T] using the TComparer."""
#
#     @staticmethod
#     @overload
#     def Sort(keys: Span[TKey], items: Span[TValue]) -> None:
#         """Sorts a pair of spans (one containing the keys and the other containing the corresponding items) based on the keys in the first Span[T] using the IComparable[T] implementation of each key."""
#
#     @staticmethod
#     @overload
#     def Sort(keys: Span[TKey], items: Span[TValue], comparison: Comparison[TKey]) -> None:
#         """Sorts a pair of spans (one containing the keys and the other containing the corresponding items) based on the keys in the first Span[T] using the specified comparison."""
#
#     @staticmethod
#     @overload
#     def Sort(keys: Span[TKey], items: Span[TValue], comparison: IComparer[TKey]) -> None:
#         """Sorts a pair of spans (one containing the keys and the other containing the corresponding items) based on the keys in the first Span[T] using the specified comparer."""
#
#     def StartsWith(self, value: ReadOnlySpan[IEquatable[T]]) -> bool:
#         """Determines whether a specified sequence appears at the start of a span."""
#
#     @overload
#     def Trim(self, trimElement: IEquatable[T]) -> Span[T]:
#         """Removes all leading and trailing occurrences of a specified element from a span."""
#
#     @overload
#     def Trim(self, trimElements: ReadOnlySpan[IEquatable[T]]) -> Span[T]:
#         """Removes all leading and trailing occurrences of a set of elements specified in a read-only span from a span."""
#
#     @overload
#     def TrimEnd(self, trimElement: IEquatable[T]) -> Span[T]:
#         """Removes all trailing occurrences of a specified element from a span."""
#
#     @overload
#     def TrimEnd(self, trimElements: ReadOnlySpan[IEquatable[T]]) -> Span[T]:
#         """Removes all trailing occurrences of a set of elements specified in a read-only span from a span."""
#
#     @overload
#     def TrimStart(self, trimElement: IEquatable[T]) -> Span[T]:
#         """Removes all leading occurrences of a specified element from the span."""
#
#     @overload
#     def TrimStart(self, trimElements: ReadOnlySpan[IEquatable[T]]) -> Span[T]:
#         """Removes all leading occurrences of a set of elements specified in a read-only span from the span."""
#
#     class Enumerator(ValueType):
#         """Provides an enumerator for the elements of a Span[T]."""
#
#         @property
#         def Current(self) -> T:
#             """Gets a reference to the item at the current position of the enumerator."""
#
#         def MoveNext(self) -> bool:
#             """Advances the enumerator to the next item of the Span[T]."""
#
#         def __iter__(self):
#             return self
#
#         __next__ = Current
#
#
# class StreamingContextStates(Enum):
#     All: Annotated[int, 'Specifies that the serialized data can be transmitted to or received from any of the other contexts.'] = 255
#
#     Clone: Annotated[int, 'Specifies that the object graph is being cloned. Users can assume that the cloned graph will continue to exist within the same process and be safe to access handles or other references to unmanaged resources.'] = 64
#
#     CrossAppDomain: Annotated[int, 'Specifies that the source or destination context is a different AppDomain. (For a description of AppDomains, see Application Domains).'] = 128
#
#     CrossMachine: Annotated[int, 'Specifies that the source or destination context is a different computer.'] = 2
#
#     CrossProcess: Annotated[int, 'Specifies that the source or destination context is a different process on the same computer.'] = 1
#
#     File: Annotated[int, 'Specifies that the source or destination context is a file. Users can assume that files will last longer than the process that created them and not serialize objects in such a way that deserialization will require accessing any data from the current process.'] = 4
#
#     Other: Annotated[int, 'Specifies that the serialization context is unknown.'] = 32
#
#     Persistence: Annotated[int, 'Specifies that the source or destination context is a persisted store, which could include databases, files, or other backing stores. Users can assume that persisted data will last longer than the process that created the data and not serialize objects so that deserialization will require accessing any data from the current process.'] = 8
#
#     Remoting: Annotated[int, 'Specifies that the data is remoted to a context in an unknown location. Users cannot make any assumptions whether this is on the same computer.'] = 16

# ---------- CLASSES ---------- #

class AmbiguousImplementationException:
    """The exception that is thrown when there are multiple incompatible interface methods overriding another method."""


class AssemblyTargetedPatchBandAttribute:
    """Specifies patch band information for targeted patching of .NET."""


class GCSettings:
    """Specifies the garbage collection settings for the current process."""


class JitInfo:
    """Provides information about the Just In Time compiler. This class cannot be inherited."""


class MemoryFailPoint:
    """Checks for sufficient memory resources before executing an operation. This class cannot be inherited."""


class ProfileOptimization:
    """Improves the startup performance of application domains in applications that require the just-in-time (JIT) compiler by performing background compilation of methods that are likely to be executed, based on profiles created during previous compilations."""


class TargetedPatchingOptOutAttribute:
    """Indicates that the .NET class library method to which this attribute is applied is unlikely to be affected by servicing releases, and therefore is eligible to be inlined across Native Image Generator (NGen) images."""


# ---------- STRUCTS ---------- #

class DependentHandle:
    """Represents a dependent garbage-collection handle. The handle will conditionally keep a dependent object instance alive as long as a target object instance is alive as well, without representing a strong reference to the target instance."""


# ---------- ENUMS ---------- #

class GCLargeObjectHeapCompactionMode:
    """Indicates whether the next blocking garbage collection compacts the large object heap (LOH)."""


class GCLatencyMode:
    """Adjusts the time that the garbage collector intrudes in your application."""
