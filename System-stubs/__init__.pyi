__all__ = [
    'BooleanType',
    'ByteType',
    'SByteType',
    'CharType',
    'DecimalType',
    'DoubleType',
    'IntType',
    'UIntType',
    'NIntType',
    'NUIntType',
    'LongType',
    'ULongType',
    'ShortType',
    'UShortType',
    'StringType',
    'ObjectType',
    'TypeType',
    
    'AccessViolationException',
    'Activator',
    'AggregateException',
    'AppContext',
    'AppDomain',
    'AppDomainSetup',
    'AppDomainUnloadedException',
    'ApplicationException',
    'ApplicationId',
    'ArgumentException',
    'ArgumentNullException',
    'ArgumentOutOfRangeException',
    'ArithmeticException',
    'Array',
    'ArrayTypeMismatchException',
    'AssemblyLoadEventArgs',
    'Attribute',
    'AttributeUsageAttribute',
    'BadImageFormatException',
    'BitConverter',
    'Buffer',
    'CannotUnloadAppDomainException',
    'CharEnumerator',
    'CLSCompliantAttribute',
    'Console',
    'ConsoleCancelEventArgs',
    'ContextBoundObject',
    'ContextMarshalException',
    'ContextStaticAttribute',
    'Convert',
    'DataMisalignedException',
    'DBNull',
    'Delegate',
    'DivideByZeroException',
    'DllNotFoundException',
    'DuplicateWaitObjectException',
    'EntryPointNotFoundException',
    'Enum',
    'Environment',
    'EventArgs',
    'Exception',
    'ExecutionEngineException',
    'FieldAccessException',
    'FileStyleUriParser',
    'FlagsAttribute',
    'FormatException',
    'FormattableString',
    'FtpStyleUriParser',
    'GC',
    'GenericUriParser',
    'GopherStyleUriParser',
    'HttpStyleUriParser',
    'IndexOutOfRangeException',
    'InsufficientExecutionStackException',
    'InsufficientMemoryException',
    'InvalidCastException',
    'InvalidOperationException',
    'InvalidProgramException',
    'InvalidTimeZoneException',
    'Lazy',
    'LdapStyleUriParser',
    'LoaderOptimizationAttribute',
    'LocalDataStoreSlot',
    'MarshalByRefObject',
    'Math',
    'MathF',
    'MemberAccessException',
    'MemoryExtensions',
    'MethodAccessException',
    'MissingFieldException',
    'MissingMemberException',
    'MissingMethodException',
    'MTAThreadAttribute',
    'MulticastDelegate',
    'MulticastNotSupportedException',
    'NetPipeStyleUriParser',
    'NetTcpStyleUriParser',
    'NewsStyleUriParser',
    'NonSerializedAttribute',
    'NotFiniteNumberException',
    'NotImplementedException',
    'NotSupportedException',
    'Nullable',
    'NullReferenceException',
    'Object',
    'ObjectDisposedException',
    'ObsoleteAttribute',
    'OperatingSystem',
    'OperationCanceledException',
    'OutOfMemoryException',
    'OverflowException',
    'ParamArrayAttribute',
    'PlatformNotSupportedException',
    'Progress',
    'Random',
    'RankException',
    'ResolveEventArgs',
    'SerializableAttribute',
    'StackOverflowException',
    'STAThreadAttribute',
    'String',
    'StringComparer',
    'StringNormalizationExtensions',
    'SystemException',
    'ThreadStaticAttribute',
    'TimeoutException',
    'TimeZone',
    'TimeZoneInfo',
    'TimeZoneNotFoundException',
    'Tuple',
    'TupleExtensions',
    'Type',
    'TypeAccessException',
    'TypeInitializationException',
    'TypeLoadException',
    'TypeUnloadedException',
    'UnauthorizedAccessException',
    'UnhandledExceptionEventArgs',
    'Uri',
    'UriBuilder',
    'UriFormatException',
    'UriParser',
    'UriTypeConverter',
    'ValueType',
    'Version',
    'WeakReference',
    'ArgIterator',
    'ArraySegment',
    'Enumerator',
    'Boolean',
    'Byte',
    'Char',
    'ConsoleKeyInfo',
    'DateOnly',
    'DateTime',
    'DateTimeOffset',
    'Decimal',
    'Double',
    'GCGenerationInfo',
    'GCMemoryInfo',
    'Guid',
    'Half',
    'HashCode',
    'Index',
    'Int16',
    'Int32',
    'Int64',
    'IntPtr',
    'Memory',
    'MemoryExtensions',
    'ModuleHandle',
    'Nullable',
    'Range',
    'ReadOnlyMemory',
    'ReadOnlySpan',
    'RuntimeArgumentHandle',
    'RuntimeFieldHandle',
    'RuntimeMethodHandle',
    'RuntimeTypeHandle',
    'SByte',
    'SequencePosition',
    'Single',
    'Span',
    'TimeOnly',
    'TimeSpan',
    'TimeZoneInfo',
    'TypedReference',
    'UInt16',
    'UInt32',
    'UInt64',
    'UIntPtr',
    'UriCreationOptions',
    'ValueTuple',
    'Void',
    'IAsyncDisposable',
    'IAsyncResult',
    'ICloneable',
    'IComparable',
    'IConvertible',
    'ICustomFormatter',
    'IDisposable',
    'IEquatable',
    'IFormatProvider',
    'IFormattable',
    'IObservable',
    'IObserver',
    'IProgress',
    'IServiceProvider',
    'ISpanFormattable',
    'AttributeTargets',
    'Base64FormattingOptions',
    'ConsoleColor',
    'ConsoleKey',
    'ConsoleModifiers',
    'ConsoleSpecialKey',
    'DateTimeKind',
    'DayOfWeek',
    'Environment',
    'Environment',
    'EnvironmentVariableTarget',
    'GCCollectionMode',
    'GCKind',
    'GCNotificationStatus',
    'GenericUriParserOptions',
    'LoaderOptimization',
    'MidpointRounding',
    'PlatformID',
    'StringComparison',
    'StringSplitOptions',
    'TypeCode',
    'UriComponents',
    'UriFormat',
    'UriHostNameType',
    'UriKind',
    'UriPartial',
    
    'Action',
    'AssemblyLoadEventHandler',
    'AsyncCallback',
    'Comparison',
    'ConsoleCancelEventHandler',
    'Converter',
    'EventHandler',
    'Func',
    'Predicate',
    'ResolveEventHandler',
    'UnhandledExceptionEventHandler',
]

from abc import ABC
from enum import Enum as _Enum
from typing import overload, Optional, TypeVar, Generic, Final, Union, Callable, Protocol, NoReturn

from .Collections import IDictionary, IStructuralComparable, IStructuralEquatable
from .Collections.Generic import IEnumerable, ICollection, IList, IReadOnlyCollection, IReadOnlyList, IEnumerator, IComparer
from .Collections.Immutable import ImmutableSortedSet
from .Collections.ObjectModel import ReadOnlyCollection
from .Globalization import NumberStyles, UnicodeCategory, CultureInfo, Calendar, DateTimeStyles
from .Reflection import MethodBase, Assembly
from .Runtime.CompilerServices import ConfiguredAsyncDisposable, ITuple
from .Runtime.Serialization import SerializationInfo, StreamingContext, ISerializable, IDeserializationCallback
from .Threading import WaitHandle
from .Threading.Tasks import ValueTask
from .util import Item

T = TypeVar('T')
TKey = TypeVar('TKey')
TValue = TypeVar('TValue')
TMetadata = TypeVar('TMetadata')
TResult = TypeVar('TResult')
TEventArgs = TypeVar('TEventArgs')
TInput = TypeVar('TInput')
TOutput = TypeVar('TOutput')
TRest = TypeVar('TRest')
TEnum = TypeVar('TEnum', bound=Enum)
T1 = TypeVar('T1')
T2 = TypeVar('T2')
T3 = TypeVar('T3')
T4 = TypeVar('T4')
T5 = TypeVar('T5')
T6 = TypeVar('T6')
T7 = TypeVar('T7')
T8 = TypeVar('T8')
T9 = TypeVar('T9')
T10 = TypeVar('T10')
T11 = TypeVar('T11')
T12 = TypeVar('T12')
T13 = TypeVar('T13')
T14 = TypeVar('T14')
T15 = TypeVar('T15')
T16 = TypeVar('T16')

BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
SByteType = Union[int, SByte]
CharType = Union[str, Char]
DecimalType = Union[float, Decimal]
DoubleType = Union[float, Double]
FloatType = SingleType = Union[float, Single]
IntType = Union[int, Int32]
UIntType = Union[int, UInt32]
NIntType = Union[int, IntPtr]
NUIntType = Union[int, UIntPtr]
LongType = Union[int, Int64]
ULongType = Union[int, UInt64]
ShortType = Union[int, Int16]
UShortType = Union[int, UInt16]
StringType = Union[str, String]
ObjectType = Union[object, Object]
TypeType = Union[type, Type]
NullableType = Union[Nullable, Optional]
VoidType = Optional[Void]
ArrayType = Union[list, Array]
Obsolete = NoReturn


# ---------- CLASSES ---------- #

class AccessViolationException(SystemException):
    """The exception that is thrown when there is an attempt to read or write protected memory."""
    
    @overload
    def __init__(self):
        """Initializes a new instance of the AccessViolationException class with a system-supplied message that describes the error."""
    
    @overload
    def __init__(self, info: SerializationInfo, context: StreamingContext):
        """Initializes a new instance of the AccessViolationException class with serialized data."""
    
    @overload
    def __init__(self, message: NullableType[StringType]):
        """Initializes a new instance of the AccessViolationException class with a specified message that describes the error."""
    
    @overload
    def __init__(self, message: NullableType[StringType], innerException: NullableType[Exception]):
        """Initializes a new instance of the AccessViolationException class with a specified error message and a reference to the inner exception that is the cause of this exception."""


class Activator:
    """Contains methods to create types of objects locally or remotely, or obtain references to existing remote objects. This class cannot be inherited."""


class AggregateException:
    """Represents one or more errors that occur during application execution."""


class AppContext:
    """Provides members for setting and retrieving data about an application's context."""


class AppDomain:
    """Represents an application domain, which is an isolated environment where applications execute. This class cannot be inherited."""


class AppDomainSetup:
    """Represents assembly binding information that can be added to an instance of AppDomain."""


class AppDomainUnloadedException:
    """The exception that is thrown when an attempt is made to access an unloaded application domain."""


class ApplicationException:
    """Serves as the base class for application-defined exceptions."""


class ApplicationId:
    """Contains information used to uniquely identify a manifest-based application. This class cannot be inherited."""


class ArgumentException:
    """The exception that is thrown when one of the arguments provided to a method is not valid."""


class ArgumentNullException:
    """The exception that is thrown when a null reference (Nothing in Visual Basic) is passed to a method that does not accept it as a valid argument."""


class ArgumentOutOfRangeException:
    """The exception that is thrown when the value of an argument is outside the allowable range of values as defined by the invoked method."""


class ArithmeticException:
    """The exception that is thrown for errors in an arithmetic, casting, or conversion operation."""


class Array(list, Object, ICollection, IEnumerable, IList, IStructuralComparable, IStructuralEquatable, ICloneable, Generic[T]):
    """Provides methods for creating, manipulating, searching, and sorting
    arrays, thereby serving as the base class for all arrays in the common
    language runtime."""
    
    @property
    def IsFixedSize(self) -> BooleanType:
        """Gets a value indicating whether the Array has a fixed size."""
    
    @property
    def IsReadOnly(self) -> BooleanType:
        """Gets a value indicating whether the Array is read-only."""
    
    @property
    def IsSynchronized(self) -> BooleanType:
        """Gets a value indicating whether access to the Array is
        synchronized (thread safe)."""
    
    @property
    def Length(self) -> IntType:
        """Gets the total number of elements in all the dimensions of the Array."""
    
    @property
    def LongLength(self) -> LongType:
        """Gets a 64-bit integer that represents the total number of elements
        in all the dimensions of the Array."""
    
    @property
    def MaxLength(self) -> IntType:
        """Gets the maximum number of elements that may be contained in an array."""
    
    @property
    def Rank(self) -> IntType:
        """Gets the rank (number of dimensions) of the Array. For example, a
        one-dimensional array returns 1, a two-dimensional array returns 2,
        and so on."""
    
    @property
    def SyncRoot(self) -> ObjectType:
        """Gets an object that can be used to synchronize access to the Array."""
    
    @staticmethod
    def AsReadOnly(array: ArrayType[T]) -> ReadOnlyCollection[T]:
        """Returns a read-only wrapper for the specified array."""
    
    @staticmethod
    @overload
    def BinarySearch(array: ArrayType, index: IntType, length: IntType, value: NullableType[ObjectType]) -> IntType:
        """Searches a range of elements in a one-dimensional sorted array for
        a value, using the IComparable interface implemented by each element
        of the array and by the specified value."""
    
    @staticmethod
    @overload
    def BinarySearch(array: ArrayType, index: IntType, length: IntType, value: NullableType[ObjectType], comparer: NullableType[IComparer]) -> IntType:
        """Searches a range of elements in a one-dimensional sorted array for
        a value, using the specified IComparer interface."""
    
    @staticmethod
    @overload
    def BinarySearch(array: ArrayType, value: NullableType[ObjectType]) -> IntType:
        """Searches an entire one-dimensional sorted array for a specific
        element, using the IComparable interface implemented by each element
        of the array and by the specified object."""
    
    @staticmethod
    @overload
    def BinarySearch(array: ArrayType, value: NullableType[ObjectType], comparer: NullableType[IComparer]) -> IntType:
        """Searches an entire one-dimensional sorted array for a value using
        the specified IComparer interface."""
    
    @staticmethod
    @overload
    def BinarySearch(array: ArrayType[T], index: IntType, length: IntType, value: NullableType[T]) -> IntType:
        """Searches a range of elements in a one-dimensional sorted array for
        a value, using the IComparable<T> generic interface implemented by
        each element of the Array and by the specified value."""
    
    @staticmethod
    @overload
    def BinarySearch(array: ArrayType[T], index: IntType, length: IntType, value: NullableType[T], comparer: NullableType[IComparer[T]]) -> IntType:
        """Searches a range of elements in a one-dimensional sorted array for
        a value, using the specified IComparer<T> generic interface."""
    
    @staticmethod
    @overload
    def BinarySearch(array: ArrayType[T], value: NullableType[T]) -> IntType:
        """Searches an entire one-dimensional sorted array for a specific
        element, using the IComparable<T> generic interface implemented by
        each element of the Array and by the specified object."""
    
    @staticmethod
    @overload
    def BinarySearch(array: ArrayType[T], value: NullableType[T], comparer: NullableType[IComparer[T]]) -> IntType:
        """Searches an entire one-dimensional sorted array for a value using
        the specified IComparer<T> generic interface."""
    
    @staticmethod
    @overload
    def Clear(array: ArrayType) -> VoidType:
        """Clears the contents of an array."""
    
    @staticmethod
    @overload
    def Clear(array: ArrayType, index: IntType, length: IntType) -> VoidType:
        """Sets a range of elements in an array to the default value of
        each element type."""
    
    def Clone(self) -> ObjectType:
        """Creates a shallow copy of the Array."""
    
    @staticmethod
    def ConstrainedCopy(sourceArray: ArrayType, sourceIndex: IntType, destinationArray: ArrayType, destinationIndex: IntType, length: IntType) -> VoidType:
        """Copies a range of elements from an Array starting at the specified
        source index and pastes them to another Array starting at the
        specified destination index. Guarantees that all changes are undone
        if the copy does not succeed completely."""
    
    @staticmethod
    def ConvertAll(array: ArrayType[TInput], converter: Converter[TInput, TOutput]) -> ArrayType[TOutput]:
        """Converts an array of one type to an array of another type."""
    
    @staticmethod
    @overload
    def Copy(sourceArray: ArrayType, destinationArray: ArrayType, length: IntType) -> VoidType:
        """Copies a range of elements from an Array starting at the first
        element and pastes them into another Array starting at the first
        element. The length is specified as a 32-bit integer."""
    
    @staticmethod
    @overload
    def Copy(sourceArray: ArrayType, destinationArray: ArrayType, length: LongType) -> VoidType:
        """Copies a range of elements from an Array starting at the first
        element and pastes them into another Array starting at the first
        element. The length is specified as a 64-bit integer."""
    
    @staticmethod
    @overload
    def Copy(sourceArray: ArrayType, sourceIndex: IntType, destinationArray: ArrayType, destinationIndex: IntType, length: IntType) -> VoidType:
        """Copies a range of elements from an Array starting at the specified
        source index and pastes them to another Array starting at the
        specified destination index. The length and the indexes are specified
        as 32-bit integers."""
    
    @staticmethod
    @overload
    def Copy(sourceArray: ArrayType, sourceIndex: LongType, destinationArray: ArrayType, destinationIndex: LongType, length: LongType) -> VoidType:
        """Copies a range of elements from an Array starting at the specified
        source index and pastes them to another Array starting at the
        specified destination index. The length and the indexes are specified
        as 64-bit integers."""
    
    @overload
    def CopyTo(self, array: ArrayType, index: IntType) -> VoidType:
        """Copies all the elements of the current one-dimensional array to
        the specified one-dimensional array starting at the specified
        destination array index. The index is specified as a 32-bit
        integer."""
    
    @overload
    def CopyTo(self, array: ArrayType, index: LongType) -> VoidType:
        """Copies all the elements of the current one-dimensional array to
        the specified one-dimensional array starting at the specified
        destination array index. The index is specified as a 64-bit
        integer."""
    
    @staticmethod
    @overload
    def CreateInstance(elementType: TypeType, length: IntType) -> ArrayType:
        """Creates a one-dimensional Array of the specified Type and length,
        with zero-based indexing."""
    
    @staticmethod
    @overload
    def CreateInstance(elementType: TypeType, length1: IntType, length2: IntType) -> ArrayType:
        """Creates a two-dimensional Array of the specified Type and
        dimension lengths, with zero-based indexing."""
    
    @staticmethod
    @overload
    def CreateInstance(elementType: TypeType, length1: IntType, length2: IntType, length3: IntType) -> ArrayType:
        """Creates a three-dimensional Array of the specified Type and
        dimension lengths, with zero-based indexing."""
    
    @staticmethod
    @overload
    def CreateInstance(elementType: TypeType, *lengths: IntType) -> ArrayType:
        """Creates a multidimensional Array of the specified Type and
        dimension lengths, with zero-based indexing. The dimension lengths
        are specified in an array of 32-bit integers."""
    
    @staticmethod
    @overload
    def CreateInstance(elementType: TypeType, lengths: ArrayType[IntType], lowerBounds: ArrayType[IntType]) -> ArrayType:
        """Creates a multidimensional Array of the specified Type and
        dimension lengths, with the specified lower bounds."""
    
    @staticmethod
    @overload
    def CreateInstance(elementType: TypeType, *lengths: LongType) -> ArrayType:
        """Creates a multidimensional Array of the specified Type and
        dimension lengths, with zero-based indexing. The dimension lengths
        are specified in an array of 64-bit integers."""
    
    @staticmethod
    def Empty() -> ArrayType[T]:
        """Returns an empty array."""
    
    @staticmethod
    def Exists(array: ArrayType[T], match: Predicate[T]) -> BooleanType:
        """Determines whether the specified array contains elements that
        match the conditions defined by the specified predicate."""
    
    @staticmethod
    @overload
    def Fill(array: ArrayType[T], value: T) -> VoidType:
        """Assigns the given value of type T to each element of the
        specified array."""
    
    @staticmethod
    @overload
    def Fill(array: ArrayType[T], value: T, startIndex: IntType, count: IntType) -> VoidType:
        """Assigns the given value of type T to the elements of the
        specified array which are within the range of startIndex
        (inclusive) and the next count number of indices."""
    
    @staticmethod
    def Find(array: ArrayType[T], match: Predicate[T]) -> NullableType[T]:
        """Searches for an element that matches the conditions defined by the
        specified predicate, and returns the first occurrence within the
        entire Array."""
    
    @staticmethod
    def FindAll(array: ArrayType[T], match: Predicate[T]) -> ArrayType[T]:
        """Retrieves all the elements that match the conditions defined by
        the specified predicate."""
    
    @staticmethod
    @overload
    def FindIndex(array: ArrayType[T], startIndex: IntType, count: IntType, match: Predicate[T]) -> IntType:
        """Searches for an element that matches the conditions defined by the
        specified predicate, and returns the zero-based index of the first
        occurrence within the range of elements in the Array that starts at
        the specified index and contains the specified number of elements."""
    
    @staticmethod
    @overload
    def FindIndex(array: ArrayType[T], startIndex: IntType, match: Predicate[T]) -> IntType:
        """Searches for an element that matches the conditions defined by the
        specified predicate, and returns the zero-based index of the first
        occurrence within the range of elements in the Array that extends
        from the specified index to the last element."""
    
    @staticmethod
    @overload
    def FindIndex(array: ArrayType[T], match: Predicate[T]) -> IntType:
        """Searches for an element that matches the conditions defined by the
        specified predicate, and returns the zero-based index of the first
        occurrence within the entire Array."""
    
    @staticmethod
    def FindLast(array: ArrayType[T], match: Predicate[T]) -> NullableType[T]:
        """Searches for an element that matches the conditions defined by
        the specified predicate, and returns the last occurrence within the
        entire Array."""
    
    @staticmethod
    @overload
    def FindLastIndex(array: ArrayType[T], startIndex: IntType, count: IntType, match: Predicate[T]) -> IntType:
        """Searches for an element that matches the conditions defined by
        the specified predicate, and returns the zero-based index of the last
        occurrence within the range of elements in the Array that contains
        the specified number of elements and ends at the specified index."""
    
    @staticmethod
    @overload
    def FindLastIndex(array: ArrayType[T], startIndex: IntType, match: Predicate[T]) -> IntType:
        """Searches for an element that matches the conditions defined by
        the specified predicate, and returns the zero-based index of the last
        occurrence within the range of elements in the Array that extends
        from the first element to the specified index."""
    
    @staticmethod
    @overload
    def FindLastIndex(array: ArrayType[T], match: Predicate[T]) -> IntType:
        """Searches for an element that matches the conditions defined by
        the specified predicate, and returns the zero-based index of the last
        occurrence within the entire Array."""
    
    @staticmethod
    def ForEach(array: ArrayType[T], action: Action1[T]) -> VoidType:
        """Performs the specified action on each element of the specified array."""
    
    def GetLength(self, dimension: IntType) -> IntType:
        """Gets a 32-bit integer that represents the number of elements in
        the specified dimension of the Array."""
    
    def GetLongLength(self, dimension: IntType) -> LongType:
        """Gets a 64-bit integer that represents the number of elements in
        the specified dimension of the Array."""
    
    def GetLowerBound(self, dimension: IntType) -> IntType:
        """Gets the index of the first element of the specified dimension
        in the array."""
    
    def GetUpperBound(self, dimension: IntType) -> IntType:
        """Gets the index of the last element of the specified dimension
        in the array."""
    
    @overload
    def GetValue(self, index: IntType) -> NullableType[ObjectType]:
        """Gets the value at the specified position in the one-dimensional
        Array. The index is specified as a 32-bit integer."""
    
    @overload
    def GetValue(self, index1: IntType, index2: IntType) -> NullableType[ObjectType]:
        """Gets the value at the specified position in the two-dimensional
        Array. The indexes are specified as 32-bit integers."""
    
    @overload
    def GetValue(self, index1: IntType, index2: IntType, index3: IntType) -> NullableType[ObjectType]:
        """Gets the value at the specified position in the three-dimensional
        Array. The indexes are specified as 32-bit integers."""
    
    @overload
    def GetValue(self, *indices: IntType) -> NullableType[ObjectType]:
        """Gets the value at the specified position in the multidimensional
        Array. The indexes are specified as an array of 32-bit integers."""
    
    @overload
    def GetValue(self, index: LongType) -> NullableType[ObjectType]:
        """Gets the value at the specified position in the one-dimensional
        Array. The index is specified as a 64-bit integer."""
    
    @overload
    def GetValue(self, index1: LongType, index2: LongType) -> NullableType[ObjectType]:
        """Gets the value at the specified position in the two-dimensional
        Array. The indexes are specified as 64-bit integers."""
    
    @overload
    def GetValue(self, index1: LongType, index2: LongType, index3: LongType) -> NullableType[ObjectType]:
        """Gets the value at the specified position in the three-dimensional
        Array. The indexes are specified as 64-bit integers."""
    
    @overload
    def GetValue(self, *indices: LongType) -> NullableType[ObjectType]:
        """Gets the value at the specified position in the multidimensional
        Array. The indexes are specified as an array of 64-bit integers."""
    
    @staticmethod
    @overload
    def IndexOf(array: ArrayType, value: NullableType[ObjectType]) -> IntType:
        """Searches for the specified object and returns the index of its
        first occurrence in a one-dimensional array."""
    
    @staticmethod
    @overload
    def IndexOf(array: ArrayType, value: NullableType[ObjectType], startIndex: IntType) -> IntType:
        """Searches for the specified object in a range of elements of a
        one-dimensional array, and returns the index of its first occurrence.
        The range extends from a specified index to the end of the array."""
    
    @staticmethod
    @overload
    def IndexOf(array: ArrayType, value: NullableType[ObjectType], startIndex: IntType, count: IntType) -> IntType:
        """Searches for the specified object in a range of elements of a
        one-dimensional array, and returns the index of ifs first occurrence.
        The range extends from a specified index for a specified number of
        elements."""
    
    @staticmethod
    @overload
    def IndexOf(array: ArrayType[T], value: T) -> IntType:
        """Searches for the specified object and returns the index of its
        first occurrence in a one-dimensional array."""
    
    @staticmethod
    @overload
    def IndexOf(array: ArrayType[T], value: T, startIndex: IntType) -> IntType:
        """Searches for the specified object in a range of elements of a
        one-dimensional array, and returns the index of its first occurrence.
        The range extends from a specified index to the end of the array."""
    
    @staticmethod
    @overload
    def IndexOf(array: ArrayType[T], value: T, startIndex: IntType, count: IntType) -> IntType:
        """Searches for the specified object in a range of elements of a
        one-dimensional array, and returns the index of its first occurrence.
        The range extends from a specified index for a specified number of
        elements."""
    
    def Initialize(self) -> VoidType:
        """Initializes every element of the value-type Array by calling the
        parameterless constructor of the value type."""
    
    @staticmethod
    @overload
    def LastIndexOf(array: ArrayType, value: NullableType[ObjectType]) -> IntType:
        """Searches for the specified object and returns the index of the
        last occurrence within the entire one-dimensional Array."""
    
    @staticmethod
    @overload
    def LastIndexOf(array: ArrayType, value: NullableType[ObjectType], startIndex: IntType) -> IntType:
        """Searches for the specified object and returns the index of the
        last occurrence within the range of elements in the one-dimensional
        Array that extends from the first element to the specified index."""
    
    @staticmethod
    @overload
    def LastIndexOf(array: ArrayType, value: NullableType[ObjectType], startIndex: IntType, count: IntType) -> IntType:
        """Searches for the specified object and returns the index of the
        last occurrence within the range of elements in the one-dimensional
        Array that contains the specified number of elements and ends at the
        specified index."""
    
    @staticmethod
    @overload
    def LastIndexOf(array: ArrayType[T], value: T) -> IntType:
        """Searches for the specified object and returns the index of the
        last occurrence within the entire Array."""
    
    @staticmethod
    @overload
    def LastIndexOf(array: ArrayType[T], value: T, startIndex: IntType) -> IntType:
        """Searches for the specified object and returns the index of the
        last occurrence within the range of elements in the Array that
        extends from the first element to the specified index."""
    
    @staticmethod
    @overload
    def LastIndexOf(array: ArrayType[T], value: T, startIndex: IntType, count: IntType) -> IntType:
        """Searches for the specified object and returns the index of the
        last occurrence within the range of elements in the Array that
        contains the specified number of elements and ends at the specified
        index."""
    
    @staticmethod
    def Resize(array: NullableType[ArrayType[T]], newSize: IntType) -> VoidType:
        """Changes the number of elements of a one-dimensional array to the
        specified new size."""
    
    @staticmethod
    @overload
    def Reverse(array: ArrayType) -> VoidType:
        """Reverses the sequence of the elements in the entire
        one-dimensional Array."""
    
    @staticmethod
    @overload
    def Reverse(array: ArrayType, index: IntType, length: IntType) -> VoidType:
        """Reverses the sequence of a subset of the elements in the
        one-dimensional Array."""
    
    @staticmethod
    @overload
    def Reverse(array: ArrayType[T]) -> VoidType:
        """Reverses the sequence of the elements in the one-dimensional
        generic array."""
    
    @staticmethod
    @overload
    def Reverse(array: ArrayType[T], index: IntType, length: IntType) -> VoidType:
        """Reverses the sequence of a subset of the elements in the
        one-dimensional generic array."""
    
    @overload
    def SetValue(self, value: NullableType[ObjectType], index: IntType) -> VoidType:
        """Sets a value to the element at the specified position in the
        one-dimensional Array. The index is specified as a 32-bit integer."""
    
    @overload
    def SetValue(self, value: NullableType[ObjectType], index1: IntType, index2: IntType) -> VoidType:
        """Sets a value to the element at the specified position in the
        two-dimensional Array. The indexes are specified as 32-bit integers."""
    
    @overload
    def SetValue(self, value: NullableType[ObjectType], index1: IntType, index2: IntType, index3: IntType) -> VoidType:
        """Sets a value to the element at the specified position in the
        three-dimensional Array. The indexes are specified as 32-bit
        integers."""
    
    @overload
    def SetValue(self, value: NullableType[ObjectType], *indices: IntType) -> VoidType:
        """Sets a value to the element at the specified position in the
        multidimensional Array. The indexes are specified as an array of
        32-bit integers."""
    
    @overload
    def SetValue(self, value: NullableType[ObjectType], index: LongType) -> VoidType:
        """Sets a value to the element at the specified position in the
        one-dimensional Array. The index is specified as a 64-bit integer."""
    
    @overload
    def SetValue(self, value: NullableType[ObjectType], index1: LongType, index2: LongType) -> VoidType:
        """Sets a value to the element at the specified position in the
        two-dimensional Array. The indexes are specified as 64-bit
        integers."""
    
    @overload
    def SetValue(self, value: NullableType[ObjectType], index1: LongType, index2: LongType, index3: LongType) -> VoidType:
        """Sets a value to the element at the specified position in the
        three-dimensional Array. The indexes are specified as 64-bit
        integers."""
    
    @overload
    def SetValue(self, value: NullableType[ObjectType], *indices: LongType) -> VoidType:
        """Sets a value to the element at the specified position in the
        multidimensional Array. The indexes are specified as an array of
        64-bit integers."""
    
    @staticmethod
    @overload
    def Sort(array: ArrayType) -> VoidType:
        """Sorts the elements in an entire one-dimensional Array using the
        IComparable implementation of each element of the Array."""
    
    @staticmethod
    @overload
    def Sort(array: ArrayType, items: NullableType[ArrayType]) -> VoidType:
        """Sorts a pair of one-dimensional Array objects (one contains the
        keys and the other contains the corresponding items) based on the
        keys in the first ArrayType using the IComparable implementation of each
        key."""
    
    @staticmethod
    @overload
    def Sort(array: ArrayType, items: NullableType[ArrayType], comparer: NullableType[IComparer]) -> VoidType:
        """Sorts a pair of one-dimensional Array objects (one contains the
        keys and the other contains the corresponding items) based on the
        keys in the first Array using the specified IComparer."""
    
    @staticmethod
    @overload
    def Sort(array: ArrayType, items: NullableType[ArrayType], index: IntType, length: IntType) -> VoidType:
        """Sorts a range of elements in a pair of one-dimensional Array
        objects (one contains the keys and the other contains the
        corresponding items) based on the keys in the first Array using the
        IComparable implementation of each key."""
    
    @staticmethod
    @overload
    def Sort(array: ArrayType, items: NullableType[ArrayType], index: IntType, length: IntType, comparer: NullableType[IComparer]) -> VoidType:
        """Sorts a range of elements in a pair of one-dimensional Array
        objects (one contains the keys and the other contains the
        corresponding items) based on the keys in the first Array using the
        specified IComparer."""
    
    @staticmethod
    @overload
    def Sort(array: ArrayType, comparer: NullableType[IComparer]) -> VoidType:
        """Sorts the elements in a one-dimensional Array using the specified
        IComparer."""
    
    @staticmethod
    @overload
    def Sort(array: ArrayType, index: IntType, length: IntType) -> VoidType:
        """Sorts the elements in a range of elements in a one-dimensional
        Array using the IComparable implementation of each element of the
        Array."""
    
    @staticmethod
    @overload
    def Sort(array: ArrayType, index: IntType, length: IntType, comparer: NullableType[IComparer]) -> VoidType:
        """Sorts the elements in a range of elements in a one-dimensional
        Array using the specified IComparer."""
    
    @staticmethod
    @overload
    def Sort(array: ArrayType[T]) -> VoidType:
        """Sorts the elements in an entire Array using the IComparable<T>
        generic interface implementation of each element of the Array."""
    
    @staticmethod
    @overload
    def Sort(array: ArrayType[T], comparison: Comparison[T]) -> VoidType:
        """Sorts the elements in an Array using the specified Comparison<T>."""
    
    @staticmethod
    @overload
    def Sort(array: ArrayType[T], comparer: NullableType[IComparer[T]]) -> VoidType:
        """Sorts the elements in an Array using the specified IComparer<T>
        generic interface."""
    
    @staticmethod
    @overload
    def Sort(array: ArrayType[T], index: IntType, length: IntType) -> VoidType:
        """Sorts the elements in a range of elements in an Array using the
        IComparable<T> generic interface implementation of each element of
        the Array."""
    
    @staticmethod
    @overload
    def Sort(array: ArrayType[T], index: IntType, length: IntType, comparer: NullableType[IComparer[T]]) -> VoidType:
        """Sorts the elements in a range of elements in an Array using the
        specified IComparer<T> generic interface."""
    
    @staticmethod
    @overload
    def Sort(keys: ArrayType[TKey], items: NullableType[ArrayType[TValue]]) -> VoidType:
        """Sorts a pair of Array objects (one contains the keys and the other
        contains the corresponding items) based on the keys in the first
        Array using the IComparable<T> generic interface implementation of
        each key."""
    
    @staticmethod
    @overload
    def Sort(keys: ArrayType[TKey], items: NullableType[ArrayType[TValue]], comparer: NullableType[IComparer[TKey]]) -> VoidType:
        """Sorts a pair of Array objects (one contains the keys and the other
        contains the corresponding items) based on the keys in the first
        Array using the specified IComparer<T> generic interface."""
    
    @staticmethod
    @overload
    def Sort(keys: ArrayType[TKey], items: NullableType[ArrayType[TValue]], index: IntType, length: IntType) -> VoidType:
        """Sorts a range of elements in a pair of Array objects (one contains
        the keys and the other contains the corresponding items) based on the
        keys in the first Array using the IComparable<T> generic interface
        implementation of each key."""
    
    @staticmethod
    @overload
    def Sort(keys: ArrayType[TKey], items: NullableType[ArrayType[TValue]], index: IntType, length: IntType, comparer: NullableType[IComparer[TKey]]) -> VoidType:
        """Sorts a range of elements in a pair of Array objects (one contains
        the keys and the other contains the corresponding items) based on the
        keys in the first Array using the specified IComparer<T> generic
        interface."""
    
    @staticmethod
    def TrueForAll(array: ArrayType[T], match: Predicate[T]) -> BooleanType:
        """Determines whether every element in the array matches the
        conditions defined by the specified predicate."""


class ArrayTypeMismatchException:
    """The exception that is thrown when an attempt is made to store an element of the wrong type within an array."""


class AssemblyLoadEventArgs:
    """Provides data for the AssemblyLoad event."""


class Attribute:
    """Represents the base class for custom attributes."""


class AttributeUsageAttribute:
    """Specifies the usage of another attribute class. This class cannot be inherited."""


class BadImageFormatException:
    """The exception that is thrown when the file image of a dynamic link library (DLL) or an executable program is invalid."""


class BitConverter:
    """Converts base data types to an array of bytes, and an array of bytes to base data types."""


class Buffer:
    """Manipulates arrays of primitive types."""


class CannotUnloadAppDomainException:
    """The exception that is thrown when an attempt to unload an application domain fails."""


class CharEnumerator:
    """Supports iterating over a String object and reading its individual characters. This class cannot be inherited."""


class CLSCompliantAttribute:
    """Indicates whether a program element is compliant with the Common Language Specification (CLS). This class cannot be inherited."""


class Console:
    """Represents the standard input, output, and error streams for console applications. This class cannot be inherited."""


class ConsoleCancelEventArgs:
    """Provides data for the CancelKeyPress event. This class cannot be inherited."""


class ContextBoundObject:
    """Defines the base class for all context-bound classes."""


class ContextMarshalException:
    """The exception that is thrown when an attempt to marshal an object across a context boundary fails."""


class ContextStaticAttribute:
    """Indicates that the value of a static field is unique for a particular context."""


class Convert:
    """Converts a base data type to another base data type."""


class DataMisalignedException:
    """The exception that is thrown when a unit of data is read from or written to an address that is not a multiple of the data size. This class cannot be inherited."""


class DBNull:
    """Represents a nonexistent value. This class cannot be inherited."""


class Delegate:
    """Represents a delegate, which is a data structure that refers to a static method or to a class instance and an instance method of that class."""


class DivideByZeroException:
    """The exception that is thrown when there is an attempt to divide an integral or Decimal value by zero."""


class DllNotFoundException:
    """The exception that is thrown when a DLL specified in a DLL import cannot be found."""


class DuplicateWaitObjectException:
    """The exception that is thrown when an object appears more than once in an array of synchronization objects."""


class EntryPointNotFoundException:
    """The exception that is thrown when an attempt to load a class fails due to the absence of an entry method."""


class Enum(ValueType, IComparable, IConvertible, IFormattable, _Enum):
    """Provides the base class for enumerations."""
    
    def __init__(self):
        """Initializes a new instance of the Enum class."""
    
    def Format(self, enumType: TypeType, value: ObjectType, format: StringType) -> StringType:
        """Converts the specified value of a specified enumerated type to its
        equivalent string representation according to the specified format."""
    
    @overload
    def GetName(self, enumType: TypeType, value: ObjectType) -> NullableType[String]:
        """Retrieves the name of the constant in the specified enumeration
        that has the specified value."""
    
    @staticmethod
    @overload
    def GetName(value: Enum) -> NullableType[StringType]:
        """Retrieves the name of the constant in the specified enumeration
        type that has the specified value."""
    
    @staticmethod
    @overload
    def GetNames(enumType: TypeType) -> ArrayType[StringType]:
        """Retrieves an array of the names of the constants in a specified enumeration."""
    
    @staticmethod
    @overload
    def GetNames() -> ArrayType[StringType]:
        """Retrieves an array of the names of the constants in a specified
        enumeration type."""
    
    def GetUnderlyingType(self, enumType: TypeType) -> TypeType:
        """Returns the underlying type of the specified enumeration."""
    
    @staticmethod
    @overload
    def GetValues(enumType: TypeType) -> ArrayType:
        """Retrieves an array of the values of the constants in a specified enumeration."""
    
    @staticmethod
    @overload
    def GetValues() -> ArrayType[TEnum]:
        """Retrieves an array of the values of the constants in a specified
        enumeration type."""
    
    def HasFlag(self, flag: Enum) -> BooleanType:
        """Determines whether one or more bit fields are set in the current instance."""
    
    @staticmethod
    @overload
    def IsDefined(enumType: TypeType, value: ObjectType) -> BooleanType:
        """Returns a Boolean telling whether a given integral value, or its
        name as a string, exists in a specified enumeration."""
    
    @staticmethod
    @overload
    def IsDefined(value: TEnum) -> BooleanType:
        """Returns a boolean telling whether a given integral value, or its
        name as a string, exists in a specified enumeration."""
    
    @staticmethod
    @overload
    def Parse(enumType: TypeType, value: ReadOnlySpan[Char]) -> ObjectType:
        """Converts the span of characters representation of the name or
        numeric value of one or more enumerated constants to an equivalent
        enumerated object."""
    
    @staticmethod
    @overload
    def Parse(enumType: TypeType, value: ReadOnlySpan[Char], ignoreCase: BooleanType) -> ObjectType:
        """Converts the span of characters representation of the name or
        numeric value of one or more enumerated constants to an equivalent
        enumerated object. A parameter specifies whether the operation is
        case-insensitive."""
    
    @staticmethod
    @overload
    def Parse(enumType: TypeType, value: StringType) -> ObjectType:
        """Converts the string representation of the name or numeric value of
        one or more enumerated constants to an equivalent enumerated object."""
    
    @staticmethod
    @overload
    def Parse(enumType: TypeType, value: StringType, ignoreCase: BooleanType) -> ObjectType:
        """Converts the string representation of the name or numeric value of
        one or more enumerated constants to an equivalent enumerated object.
        A parameter specifies whether the operation is case-insensitive."""
    
    @staticmethod
    @overload
    def Parse(value: ReadOnlySpan[Char]) -> TEnum:
        """Converts the span of characters representation of the name or
        numeric value of one or more enumerated constants specified by TEnum
        to an equivalent enumerated object."""
    
    @staticmethod
    @overload
    def Parse(value: ReadOnlySpan[Char], ignoreCase: BooleanType) -> TEnum:
        """Converts the span of characters representation of the name or
        numeric value of one or more enumerated constants specified by TEnum
        to an equivalent enumerated object. A parameter specifies whether the
        operation is case-insensitive."""
    
    @staticmethod
    @overload
    def Parse(value: StringType) -> TEnum:
        """Converts the string representation of the name or numeric value of
        one or more enumerated constants specified by TEnum to an equivalent
        enumerated object."""
    
    @staticmethod
    @overload
    def Parse(value: StringType, ignoreCase: BooleanType) -> TEnum:
        """Converts the string representation of the name or numeric value of
        one or more enumerated constants specified by TEnum to an equivalent
        enumerated object. A parameter specifies whether the operation is
        case-insensitive."""
    
    @staticmethod
    @overload
    def ToObject(enumType: TypeType, value: ByteType) -> ObjectType:
        """Converts the specified 8-bit unsigned integer to an enumeration member."""
    
    @staticmethod
    @overload
    def ToObject(enumType: TypeType, value: ShortType) -> ObjectType:
        """Converts the specified 16-bit signed integer to an enumeration member."""
    
    @staticmethod
    @overload
    def ToObject(enumType: TypeType, value: IntType) -> ObjectType:
        """Converts the specified 32-bit signed integer to an enumeration member."""
    
    @staticmethod
    @overload
    def ToObject(enumType: TypeType, value: LongType) -> ObjectType:
        """Converts the specified 64-bit signed integer to an enumeration member."""
    
    @staticmethod
    @overload
    def ToObject(enumType: TypeType, value: ObjectType) -> ObjectType:
        """Converts the specified object with an integer value to an
        enumeration member."""
    
    @staticmethod
    @overload
    def ToObject(enumType: TypeType, value: SByteType) -> ObjectType:
        """Converts the specified 8-bit signed integer value to an
        enumeration member."""
    
    @staticmethod
    @overload
    def ToObject(enumType: TypeType, value: UShortType) -> ObjectType:
        """Converts the specified 16-bit unsigned integer value to an
        enumeration member."""
    
    @staticmethod
    @overload
    def ToObject(enumType: TypeType, value: UIntType) -> ObjectType:
        """Converts the specified 32-bit unsigned integer value to an
        enumeration member."""
    
    @staticmethod
    @overload
    def ToObject(enumType: TypeType, value: ULongType) -> ObjectType:
        """Converts the specified 64-bit unsigned integer value to an
        enumeration member."""
    
    @overload
    def ToString(self, provider: NullableType[IFormatProvider]) -> StringType:
        """Obsolete.
        This method overload is obsolete; use ToString()."""
    
    @overload
    def ToString(self, format: NullableType[StringType]) -> StringType:
        """Converts the value of this instance to its equivalent string
        representation using the specified format."""
    
    @overload
    def ToString(self, format: NullableType[StringType], provider: NullableType[IFormatProvider]) -> StringType:
        """Obsolete.
        This method overload is obsolete; use ToString(String)."""
    
    @staticmethod
    @overload
    def TryParse(enumType: TypeType, value: ReadOnlySpan[Char], ignoreCase: BooleanType, result: NullableType[ObjectType]) -> BooleanType:
        """Converts the span of characters representation of the name or
        numeric value of one or more enumerated constants to an equivalent
        enumerated object. A parameter specifies whether the operation is
        case-insensitive."""
    
    @staticmethod
    @overload
    def TryParse(enumType: TypeType, value: ReadOnlySpan[Char], result: NullableType[ObjectType]) -> BooleanType:
        """Converts the span of characters representation of the name or
        numeric value of one or more enumerated constants to an equivalent
        enumerated object."""
    
    @staticmethod
    @overload
    def TryParse(enumType: TypeType, value: NullableType[StringType], ignoreCase: BooleanType, result: NullableType[ObjectType]) -> BooleanType:
        """Converts the string representation of the name or numeric value
        of one or more enumerated constants to an equivalent enumerated
        object."""
    
    @staticmethod
    @overload
    def TryParse(enumType: TypeType, value: NullableType[StringType], result: NullableType[ObjectType]) -> BooleanType:
        """Converts the string representation of the name or numeric value
        of one or more enumerated constants to an equivalent enumerated
        object."""
    
    @staticmethod
    @overload
    def TryParse(value: ReadOnlySpan[Char], ignoreCase: BooleanType, result: TEnum) -> BooleanType:
        """Converts the string representation of the name or numeric value
        of one or more enumerated constants to an equivalent enumerated
        object. A parameter specifies whether the operation is
        case-sensitive. The return value indicates whether the conversion
        succeeded."""
    
    @staticmethod
    @overload
    def TryParse(value: ReadOnlySpan[Char], result: TEnum) -> BooleanType:
        """Converts the string representation of the name or numeric value of
        one or more enumerated constants to an equivalent enumerated object."""
    
    @staticmethod
    @overload
    def TryParse(value: NullableType[StringType], ignoreCase: BooleanType, result: TEnum) -> BooleanType:
        """Converts the string representation of the name or numeric value of
        one or more enumerated constants to an equivalent enumerated object.
        A parameter specifies whether the operation is case-sensitive. The
        return value indicates whether the conversion succeeded."""
    
    @staticmethod
    @overload
    def TryParse(value: NullableType[StringType], result: TEnum) -> BooleanType:
        """Converts the string representation of the name or numeric value of
        one or more enumerated constants to an equivalent enumerated object.
        The return value indicates whether the conversion succeeded."""


class Environment:
    """Provides information about, and means to manipulate, the current
    environment and platform. This class cannot be inherited."""
    
    class SpecialFolder(Enum):
        """Specifies enumerated constants used to retrieve directory paths
        to system special folders."""
        
        AdminTools = 48
        """The file system directory that is used to store administrative
        tools for an individual user. The Microsoft Management Console
        (MMC) will save customized consoles to this directory, and it will
        roam with the user."""
        
        ApplicationData = 26
        """The directory that serves as a common repository for
        application-specific data for the current roaming user. A roaming
        user works on more than one computer on a network. A roaming user's
        profile is kept on a server on the network and is loaded onto a
        system when the user logs on."""
        
        CDBurning = 59
        """The file system directory that acts as a staging area for files
        waiting to be written to a CD."""
        
        CommonAdminTools = 47
        """The file system directory that contains administrative tools for
        all users of the computer."""
        
        CommonApplicationData = 35
        """The directory that serves as a common repository for
        application-specific data that is used by all users."""
        
        CommonDesktopDirectory = 25
        """The file system directory that contains files and folders that
        appear on the desktop for all users."""
        
        CommonDocuments = 46
        """The file system directory that contains documents that are common
        to all users."""
        
        CommonMusic = 53
        """The file system directory that serves as a repository for music
        files common to all users."""
        
        CommonOemLinks = 58
        """This value is recognized in Windows Vista for backward
        compatibility, but the special folder itself is no longer used."""
        
        CommonPictures = 54
        """The file system directory that serves as a repository for image
        files common to all users."""
        
        CommonProgramFiles = 43
        """The directory for components that are shared across applications.
        
        To get the x86 common program files directory in a non-x86 process,
        use the ProgramFilesX86 member."""
        
        CommonProgramFilesX86 = 44
        """The Program Files folder."""
        
        CommonPrograms = 23
        """A folder for components that are shared across applications."""
        
        CommonStartMenu = 22
        """The file system directory that contains the programs and folders
        that appear on the Start menu for all users."""
        
        CommonStartup = 24
        """The file system directory that contains the programs that appear
        in the Startup folder for all users."""
        
        CommonTemplates = 45
        """The file system directory that contains the templates that are
        available to all users."""
        
        CommonVideos = 55
        """The file system directory that serves as a repository for video
        files common to all users."""
        
        Cookies = 33
        """The directory that serves as a common repository for Internet cookies."""
        
        Desktop = 0
        """The logical Desktop rather than the physical file system location."""
        
        DesktopDirectory = 16
        """The directory used to physically store file objects on the desktop.
        Do not confuse this directory with the desktop folder itself, which
        is a virtual folder."""
        
        Favorites = 6
        """The directory that serves as a common repository for the user's favorite items."""
        
        Fonts = 20
        """irtual folder that contains fonts."""
        
        History = 34
        """The directory that serves as a common repository for Internet history items."""
        
        InternetCache = 32
        """The directory that serves as a common repository for temporary Internet files."""
        
        LocalApplicationData = 28
        """The directory that serves as a common repository for application-specific
        data that is used by the current, non-roaming user."""
        
        LocalizedResources = 57
        """The file system directory that contains localized resource data."""
        
        MyComputer = 17
        """The My Computer folder. When passed to the
        Environment.GetFolderPath method, the MyComputer enumeration member
        always yields the empty string ("") because no path is defined for
        the My Computer folder."""
        
        MyDocuments = 5
        """The My Documents folder. This member is equivalent to Personal."""
        
        MyMusic = 13
        """The My Music folder."""
        
        MyPictures = 39
        """The My Pictures folder."""
        
        MyVideos = 14
        """The file system directory that serves as a repository for videos
        that belong to a user."""
        
        NetworkShortcuts = 19
        """A file system directory that contains the link objects that may
        exist in the My Network Places virtual folder."""
        
        Personal = 5
        """The directory that serves as a common repository for documents.
        This member is equivalent to MyDocuments."""
        
        PrinterShortcuts = 27
        """The file system directory that contains the link objects that can
        exist in the Printers virtual folder."""
        
        ProgramFiles = 38
        """The program files directory.
        
        In a non-x86 process, passing ProgramFiles to the
        GetFolderPath(Environment.SpecialFolder) method returns the path for
        non-x86 programs. To get the x86 program files directory in a non-x86
        process, use the ProgramFilesX86 member."""
        
        ProgramFilesX86 = 42
        """The x86 Program Files folder."""
        
        Programs = 2
        """The directory that contains the user's program groups."""
        
        Recent = 8
        """The directory that contains the user's most recently used documents."""
        
        Resources = 56
        """The file system directory that contains resource data."""
        
        SendTo = 9
        """The directory that contains the Send To menu items."""
        
        StartMenu = 11
        """The directory that contains the Start menu items."""
        
        Startup = 7
        """The directory that corresponds to the user's Startup program
        group. The system starts these programs whenever a user logs on or
        starts Windows."""
        
        System = 37
        """The System directory."""
        
        SystemX86 = 41
        """The Windows System folder."""
        
        Templates = 21
        """The directory that serves as a common repository for document templates."""
        
        UserProfile = 40
        """The user's profile folder. Applications should not create files or
        folders at this level; they should put their data under the locations
        referred to by ApplicationData."""
        
        Windows = 36
        """The Windows directory or SYSROOT. This corresponds to the %windir%
        or %SYSTEMROOT% environment variables."""
    
    class SpecialFolderOption(Enum):
        """Specifies options to use for getting the path to a special folder."""
        
        Create: 32768
        """The path to the folder is created if it does not already exist."""
        
        DoNotVerify: 16384
        """The path to the folder is returned without verifying whether the
        path exists. If the folder is located on a network, specifying this
        option can reduce lag time."""
        
        #None: 0
        """The path to the folder is verified. If the folder exists, the path
        is returned. If the folder does not exist, an empty string is
        returned. This is the default behavior."""


class EventArgs:
    """Represents the base class for classes that contain event data, and provides a value to use for events that do not include event data."""


class Exception(Object, ISerializable, ABC):
    """Represents errors that occur during application execution."""
    
    @overload
    def __init__(self):
        """Initializes a new instance of the Exception class."""
    
    @overload
    def __init__(self, info: SerializationInfo, context: StreamingContext):
        """Initializes a new instance of the Exception class with serialized data."""
    
    @overload
    def __init__(self, message: NullableType[StringType]):
        """Initializes a new instance of the Exception class with a specified error message."""
    
    @overload
    def __init__(self, message: NullableType[StringType], innerException: NullableType[Exception]):
        """Initializes a new instance of the Exception class with a specified
        error message and a reference to the inner exception that is the cause
        of this exception."""
    
    @property
    def Data(self) -> IDictionary:
        """Gets a collection of key/value pairs that provide additional user-defined information about the exception."""
    
    @property
    def HelpLink(self) -> NullableType[String]:
        """Gets a link to the help file associated with this exception."""
    
    @HelpLink.setter
    def HelpLink(self, value: String) -> VoidType:
        """Sets a link to the help file associated with this exception."""
    
    @property
    def HResult(self) -> IntType:
        """Gets HRESULT, a coded numerical value that is assigned to a specific exception."""
    
    @HResult.setter
    def HResult(self, value: IntType) -> VoidType:
        """Sets HRESULT, a coded numerical value that is assigned to a specific exception."""
    
    @property
    def InnerException(self) -> NullableType[Exception]:
        """Gets the Exception instance that caused the current exception."""
    
    @property
    def Message(self) -> StringType:
        """Gets a message that describes the current exception."""
    
    @property
    def Source(self) -> NullableType[String]:
        """Gets or sets the name of the application or the object that causes the error."""
    
    @Source.setter
    def Source(self, value: String) -> NullableType[String]:
        """Gets or sets the name of the application or the object that causes the error."""
    
    @property
    def StackTrace(self) -> NullableType[String]:
        """Gets a string representation of the immediate frames on the call stack."""
    
    @property
    def TargetSite(self) -> NullableType[MethodBase]:
        """Gets the method that throws the current exception."""
    
    def GetBaseException(self) -> Exception:
        """When overridden in a derived class, returns the Exception that is the root cause of one or more subsequent exceptions."""
    
    @property
    def SerializeObjectState(self) -> Obsolete:
        """Obsolete.
        Occurs when an exception is serialized to create an exception state object that contains serialized data about the exception."""


class ExecutionEngineException:
    """The exception that is thrown when there is an internal error in the execution engine of the common language runtime. This class cannot be inherited."""


class FieldAccessException:
    """The exception that is thrown when there is an invalid attempt to access a private or protected field inside a class."""


class FileStyleUriParser:
    """A customizable parser based on the File scheme."""


class FlagsAttribute:
    """Indicates that an enumeration can be treated as a bit field; that is, a set of flags."""


class FormatException:
    """The exception that is thrown when the format of an argument is invalid, or when a composite format string is not well formed."""


class FormattableString:
    """Represents a composite format string, along with the arguments to be formatted."""


class FtpStyleUriParser:
    """A customizable parser based on the File Transfer Protocol (FTP) scheme."""


class GC:
    """Controls the system garbage collector, a service that automatically reclaims unused memory."""


class GenericUriParser:
    """A customizable parser for a hierarchical URI."""


class GopherStyleUriParser:
    """A customizable parser based on the Gopher scheme."""


class HttpStyleUriParser:
    """A customizable parser based on the HTTP scheme."""


class IndexOutOfRangeException:
    """The exception that is thrown when an attempt is made to access an element of an array or collection with an index that is outside its bounds."""


class InsufficientExecutionStackException:
    """The exception that is thrown when there is insufficient execution stack available to allow most methods to execute."""


class InsufficientMemoryException:
    """The exception that is thrown when a check for sufficient available memory fails. This class cannot be inherited."""


class InvalidCastException:
    """The exception that is thrown for invalid casting or explicit conversion."""


class InvalidOperationException:
    """The exception that is thrown when a method call is invalid for the object's current state."""


class InvalidProgramException:
    """The exception that is thrown when a program contains invalid Microsoft intermediate language (MSIL) or metadata. Generally this indicates a bug in the compiler that generated the program."""


class InvalidTimeZoneException:
    """The exception that is thrown when time zone information is invalid."""


class Lazy(Generic[T, TMetadata]):
    """Provides support for lazy initialization.
    
    Provides a lazy indirect reference to an object and its associated metadata for use by the Managed Extensibility Framework."""


class LdapStyleUriParser:
    """A customizable parser based on the Lightweight Directory Access Protocol (LDAP) scheme."""


class LoaderOptimizationAttribute:
    """Used to set the default loader optimization policy for the main method of an executable application."""


class LocalDataStoreSlot:
    """Encapsulates a memory slot to store local data. This class cannot be inherited."""


class MarshalByRefObject:
    """Enables access to objects across application domain boundaries in applications that support remoting."""


class Math:
    """Provides constants and static methods for trigonometric, logarithmic, and other common mathematical functions."""


class MathF:
    """Provides constants and static methods for trigonometric, logarithmic, and other common mathematical functions."""


class MemberAccessException:
    """The exception that is thrown when an attempt to access a class member fails."""


class MemoryExtensions:
    """Provides extension methods for the memory- and span-related types, such as Memory[T], ReadOnlyMemory[T], Span[T], and ReadOnlySpan[T]."""
    
    # ---------- STRUCTS ---------- #
    
    class TryWriteInterpolatedStringHandler(ValueType):
        """Provides a handler used by the language compiler to format interpolated
        strings into character spans."""
        
        @overload
        def __init__(self, literalLength: IntType, formattedCount: IntType, destination: Span[Char], shouldAppend: BooleanType):
            """Creates a handler used to write an interpolated string into a
            span of characters."""
        
        @overload
        def __init__(self, literalLength: IntType, formattedCount: IntType, destination: Span[Char], provider: NullableType[IFormatProvider], shouldAppend: BooleanType):
            """Creates a handler used to write an interpolated string into a
            span of characters."""
        
        @overload
        def AppendFormatted(self, value: NullableType[ObjectType], alignment: IntType = 0, format: NullableType[StringType] = None) -> BooleanType:
            """Writes the specified value to the handler."""
        
        @overload
        def AppendFormatted(self, value: ReadOnlySpan[Char]) -> BooleanType:
            """Writes the specified value to the handler."""
        
        @overload
        def AppendFormatted(self, value: ReadOnlySpan[Char], alignment: IntType = 0, format: NullableType[StringType] = None) -> BooleanType:
            """Writes the specified value to the handler."""
        
        @overload
        def AppendFormatted(self, value: NullableType[StringType]) -> BooleanType:
            """Writes the specified value to the handler."""
        
        @overload
        def AppendFormatted(self, value: NullableType[StringType], alignment: IntType = 0, format: NullableType[StringType] = None) -> BooleanType:
            """Writes a specified value to the handler using a specified format string."""
        
        @overload
        def AppendFormatted(self, value: T) -> BooleanType:
            """Writes the specified value to the handler."""
        
        @overload
        def AppendFormatted(self, value: T, alignment: IntType) -> BooleanType:
            """Writes the specified value to the handler."""
        
        @overload
        def AppendFormatted(self, value: T, alignment: IntType, format: NullableType[StringType]) -> BooleanType:
            """Writes a specified value to the handler using a specified format string."""
        
        @overload
        def AppendFormatted(self, value: T, format: NullableType[StringType]) -> BooleanType:
            """Writes a specified value to the handler using a specified format string."""
        
        def AppendLiteral(self, value: StringType) -> BooleanType:
            """Writes the specified string to the handler."""


class MethodAccessException:
    """The exception that is thrown when there is an invalid attempt to access a method, such as accessing a private method from partially trusted code."""


class MissingFieldException:
    """The exception that is thrown when there is an attempt to dynamically access a field that does not exist. If a field in a class library has been removed or renamed, recompile any assemblies that reference that library."""


class MissingMemberException:
    """The exception that is thrown when there is an attempt to dynamically access a class member that does not exist or that is not declared as public. If a member in a class library has been removed or renamed, recompile any assemblies that reference that library."""


class MissingMethodException:
    """The exception that is thrown when there is an attempt to dynamically access a method that does not exist."""


class MTAThreadAttribute:
    """Indicates that the COM threading model for an application is multithreaded apartment (MTA)."""


class MulticastDelegate:
    """Represents a multicast delegate; that is, a delegate that can have more than one element in its invocation list."""


class MulticastNotSupportedException:
    """The exception that is thrown when there is an attempt to combine two delegates based on the Delegate type instead of the MulticastDelegate type. This class cannot be inherited."""


class NetPipeStyleUriParser:
    """A parser based on the NetPipe scheme for the "Indigo" system."""


class NetTcpStyleUriParser:
    """A parser based on the NetTcp scheme for the "Indigo" system."""


class NewsStyleUriParser:
    """A customizable parser based on the news scheme using the Network News Transfer Protocol (NNTP)."""


class NonSerializedAttribute:
    """Indicates that a field of a serializable class should not be serialized. This class cannot be inherited."""


class NotFiniteNumberException:
    """The exception that is thrown when a floating-point value is positive infinity, negative infinity, or Not-a-Number (NaN)."""


class NotImplementedException:
    """The exception that is thrown when a requested method or operation is not implemented."""


class NotSupportedException:
    """The exception that is thrown when an invoked method is not supported, or when there is an attempt to read, seek, or write to a stream that does not support the invoked functionality."""


class NullReferenceException:
    """The exception that is thrown when there is an attempt to dereference a null object reference."""


class Object:
    """Supports all classes in the .NET class hierarchy and provides low-level
    services to derived classes. This is the ultimate base class of all .NET
    classes; it is the root of the type hierarchy."""
    
    def __init__(self):
        """Initializes a new instance of the Object class."""
    
    @overload
    def Equals(self, obj: NullableType[ObjectType]) -> BooleanType:
        """Determines whether the specified object is equal to the current object."""
    
    def Equals(self, *args, **kwargs) -> BooleanType: ...
    
    def Finalize(self) -> VoidType:
        """Allows an object to try to free resources and perform other cleanup
        operations before it is reclaimed by garbage collection."""
    
    def GetHashCode(self) -> IntType:
        """Serves as the default hash function."""
    
    def GetType(self) -> TypeType:
        """Gets the Type of the current instance."""
    
    def MemberwiseClone(self) -> ObjectType:
        """Creates a shallow copy of the current Object."""
    
    @overload
    def ToString(self) -> StringType:
        """Returns a string that represents the current object."""
    
    def ToString(self, *args, **kwargs) -> StringType: ...
    
    @staticmethod
    def ReferenceEquals(obj1: ObjectType, obj2: ObjectType) -> BooleanType:
        """Determines whether the specified Object instances are the same instance."""
    
    @staticmethod
    @overload
    def Equals(obj1: ObjectType, obj2: ObjectType) -> BooleanType:
        """Determines whether the specified object instances are considered equal."""


class ObjectDisposedException:
    """The exception that is thrown when an operation is performed on a disposed object."""


class ObsoleteAttribute:
    """Marks the program elements that are no longer in use. This class cannot be inherited."""


class OperatingSystem:
    """Represents information about an operating system, such as the version and platform identifier. This class cannot be inherited."""


class OperationCanceledException:
    """The exception that is thrown in a thread upon cancellation of an operation that the thread was executing."""


class OutOfMemoryException:
    """The exception that is thrown when there is not enough memory to continue the execution of a program."""


class OverflowException:
    """The exception that is thrown when an arithmetic, casting, or conversion operation in a checked context results in an overflow."""


class ParamArrayAttribute:
    """Indicates that a method will allow a variable number of arguments in its invocation. This class cannot be inherited."""


class PlatformNotSupportedException:
    """The exception that is thrown when a feature does not run on a particular platform."""


class Progress(Generic[T]):
    """Provides an IProgress[T] that invokes callbacks for each reported progress value."""


class Random:
    """Represents a pseudo-random number generator, which is an algorithm that produces a sequence of numbers that meet certain statistical requirements for randomness."""


class RankException:
    """The exception that is thrown when an array with the wrong number of dimensions is passed to a method."""


class ResolveEventArgs:
    """Provides data for loader resolution events, such as the TypeResolve, ResourceResolve, ReflectionOnlyAssemblyResolve, and AssemblyResolve events."""


class SerializableAttribute:
    """Indicates that a class can be serialized. This class cannot be inherited."""


class StackOverflowException:
    """The exception that is thrown when the execution stack overflows because it contains too many nested method calls. This class cannot be inherited."""


class STAThreadAttribute:
    """Indicates that the COM threading model for an application is single-threaded apartment (STA)."""


class String:
    """Represents text as a sequence of UTF-16 code units."""


class StringComparer:
    """Represents a string comparison operation that uses specific case and culture-based or ordinal comparison rules."""


class StringNormalizationExtensions:
    """Provides extension methods to work with string normalization."""


class SystemException(Exception):
    """Serves as the base class for system exceptions namespace."""
    
    @overload
    def __init__(self):
        """Initializes a new instance of the SystemException class."""
    
    @overload
    def __init__(self, info: SerializationInfo, context: StreamingContext):
        """Initializes a new instance of the SystemException class with serialized data."""
    
    @overload
    def __init__(self, message: NullableType[StringType]):
        """Initializes a new instance of the SystemException class with a specified error message."""
    
    @overload
    def __init__(self, message: NullableType[StringType], innerException: NullableType[Exception]):
        """Initializes a new instance of the SystemException class with a specified
        error message and a reference to the inner exception that is the cause
        of this exception."""


class ThreadStaticAttribute:
    """Indicates that the value of a static field is unique for each thread."""


class TimeoutException:
    """The exception that is thrown when the time allotted for a process or operation has expired."""


class TimeZone:
    """Represents a time zone."""


class TimeZoneInfo:
    """Represents any time zone in the world."""
    
    class AdjustmentRule:
        """Provides information about a time zone adjustment, such as the transition to and from daylight saving time."""
    
    # ---------- STRUCTS ---------- #
    
    class TransitionTime(ValueType, IEquatable[TransitionTime], IDeserializationCallback, ISerializable):
        """Provides information about a specific time change, such as the
        change from daylight saving time to standard time or vice versa,
        in a particular time zone."""
        
        @property
        def Day(self) -> IntType:
            """Gets the day on which the time change occurs."""
        
        @property
        def DayOfWeek(self) -> DayOfWeek:
            """Gets the day of the week on which the time change occurs."""
        
        @property
        def IsFixedDateRule(self) -> BooleanType:
            """Gets a value indicating whether the time change occurs at a
            fixed date and time (such as November 1) or a floating date and
            time (such as the last Sunday of October)."""
        
        @property
        def Month(self) -> IntType:
            """Gets the month in which the time change occurs."""
        
        @property
        def TimeOfDay(self) -> DateTime:
            """Gets the hour, minute, and second at which the time change occurs."""
        
        @property
        def Week(self) -> IntType:
            """Gets the week of the month in which a time change occurs."""
        
        @staticmethod
        def CreateFixedDateRule(timeOfDay: DateTime, month: IntType, day: IntType) -> TimeZoneInfo.TransitionTime:
            """Defines a time change that uses a fixed-date rule (that is, a
            time change that occurs on a specific day of a specific month)."""
        
        @staticmethod
        def CreateFloatingDateRule(timeOfDay: DateTime, month: IntType, day: IntType, dayOfWeek: DayOfWeek) -> TimeZoneInfo.TransitionTime:
            """Defines a time change that uses a floating-date rule (that is,
            a time change that occurs on a specific day of a specific week of
            a specific month)."""
        
        def Equals(self, other: TimeZoneInfo.TransitionTime):
            """Determines whether the current TimeZoneInfo.TransitionTime
            object has identical values to a second TimeZoneInfo.TransitionTime
            object."""
        
        @staticmethod
        def Equality(left: TimeZoneInfo.TransitionTime, right: TimeZoneInfo.TransitionTime) -> BooleanType:
            """Determines whether two specified TimeZoneInfo.TransitionTime objects are equal."""
        
        @staticmethod
        def Inequality(left: TimeZoneInfo.TransitionTime, right: TimeZoneInfo.TransitionTime) -> BooleanType:
            """Determines whether two specified TimeZoneInfo.TransitionTime objects are not equal."""
        
        __eq__ = Equality
        __ne__ = Inequality
        
        op_Equality = Equality
        op_Inequality = Inequality


class TimeZoneNotFoundException:
    """The exception that is thrown when a time zone cannot be found."""


@overload
class Tuple:
    """Provides static methods for creating tuple objects."""


@overload
class Tuple(Generic[T1]):
    """Represents a 1-tuple, or singleton."""


@overload
class Tuple(Generic[T1, T2]):
    """Represents a 2-tuple, or pair."""


@overload
class Tuple(Generic[T1, T2, T3]):
    """Represents a 3-tuple, or triple."""


@overload
class Tuple(Generic[T1, T2, T3, T4]):
    """Represents a 4-tuple, or quadruple."""


@overload
class Tuple(Generic[T1, T2, T3, T4, T5]):
    """Represents a 5-tuple, or quintuple."""


@overload
class Tuple(Generic[T1, T2, T3, T4, T5, T6]):
    """Represents a 6-tuple, or sextuple."""


@overload
class Tuple(Generic[T1, T2, T3, T4, T5, T6, T7]):
    """Represents a 7-tuple, or septuple."""


@overload
class Tuple(Generic[T1, T2, T3, T4, T5, T6, T7, TRest]):
    """Represents an n-tuple, where n is 8 or greater."""


class TupleExtensions:
    """Provides extension methods for tuples to interoperate with language support for tuples in C#."""


class Type:
    """Represents type declarations: class types, interface types, array types, value types, enumeration types, type parameters, generic type definitions, and open or closed constructed generic types."""


class TypeAccessException:
    """The exception that is thrown when a method attempts to use a type that it does not have access to."""


class TypeInitializationException:
    """The exception that is thrown as a wrapper around the exception thrown by the class initializer. This class cannot be inherited."""


class TypeLoadException:
    """The exception that is thrown when type-loading failures occur."""


class TypeUnloadedException:
    """The exception that is thrown when there is an attempt to access an unloaded class."""


class UnauthorizedAccessException:
    """The exception that is thrown when the operating system denies access because of an I/O error or a specific type of security error."""


class UnhandledExceptionEventArgs:
    """Provides data for the event that is raised when there is an exception that is not handled in any application domain."""


class Uri:
    """Provides an object representation of a uniform resource identifier (URI) and easy access to the parts of the URI."""


class UriBuilder:
    """Provides a custom constructor for uniform resource identifiers (URIs) and modifies URIs for the Uri class."""


class UriFormatException:
    """The exception that is thrown when an invalid Uniform Resource Identifier (URI) is detected."""


class UriParser:
    """Parses a new URI scheme. This is an abstract class."""


class UriTypeConverter:
    """Converts a String type to a Uri type, and vice versa."""


class ValueType(Object, ABC):
    """Provides the base class for value types."""
    
    def __init__(self): ...


class Version:
    """Represents the version number of an assembly, operating system, or the common language runtime. This class cannot be inherited."""


class WeakReference(Generic[T]):
    """Represents a typed weak reference, which references an object while still allowing that object to be reclaimed by garbage collection."""


# ---------- STRUCTS ---------- #

class ArgIterator(ValueType):
    """Represents a variable-length argument list; that is, the parameters
    of a function that takes a variable number of arguments."""
    
    @overload
    def __init__(self, arglist: RuntimeArgumentHandle):
        """Initializes a new instance of the ArgIterator structure using the
        specified argument list."""
    
    @overload
    def __init__(self, arglist: RuntimeArgumentHandle, ptr: Void):
        """Initializes a new instance of the ArgIterator structure using the
        specified argument list and a pointer to an item in the list."""
    
    def End(self) -> VoidType:
        """Concludes processing of the variable-length argument list
        represented by this instance."""
    
    @overload
    def GetNextArg(self) -> TypedReference:
        """Returns the next argument in a variable-length argument list."""
    
    @overload
    def GetNextArg(self, rth: RuntimeTypeHandle) -> TypedReference:
        """Returns the next argument in a variable-length argument list that
        has a specified type."""
    
    def GetNextArgType(self) -> RuntimeTypeHandle:
        """Returns the type of the next argument."""
    
    def GetRemainingCount(self) -> IntType:
        """Returns the number of arguments remaining in the argument list."""


class ArraySegment(ValueType, ICollection[T], IEnumerable[T], IList[T], IReadOnlyCollection[T], IReadOnlyList[T], IEnumerable):
    """Delimits a section of a one-dimensional array."""
    
    @overload
    def __init__(self, array: ArrayType[T]):
        """Initializes a new instance of the ArraySegment[T] structure that
        delimits all the elements in the specified array."""
    
    @overload
    def __init__(self, array: ArrayType[T], offset: IntType, count: IntType):
        """Initializes a new instance of the ArraySegment[T] structure that
        delimits the specified range of the elements in the specified array."""
    
    @property
    def Array(self) -> NullableType[ArrayType[T]]:
        """Gets the original array containing the range of elements that the
        array segment delimits."""
    
    @property
    def Count(self) -> IntType:
        """Gets the number of elements in the range delimited by the array segment."""
    
    @staticmethod
    @property
    def Empty() -> ArrayType[T]:
        """Represents the empty array segment. This field is read-only."""
    
    @property
    def Item(self) -> Item[IntType, T]:
        """Gets or sets the element at the specified index."""

    def __getitem__(self, key: IntType) -> T: ...

    def __setitem__(self, key: IntType, value: T) -> VoidType: ...

    @property
    def Offset(self) -> IntType:
        """Gets the position of the first element in the range delimited by
        the array segment, relative to the start of the original array."""
    
    def CopyTo(self, destination: ArraySegment[T]) -> VoidType:
        """Copies the contents of this instance into the specified
        destination array segment of the same type T."""
    
    @overload
    def CopyTo(self, destination: ArrayType[T]) -> VoidType:
        """Copies the contents of this instance into the specified destination
        array of the same type T."""
    
    @overload
    def CopyTo(self, destination: ArrayType[T], destinationIndex: IntType) -> VoidType:
        """Copies the contents of this instance into the specified destination
        array of the same type T, starting at the specified destination index."""
    
    def GetEnumerator(self) -> ArraySegment[T].Enumerator:
        """Returns an enumerator that can be used to iterate through the array segment."""
    
    @overload
    def Slice(self, index: IntType) -> ArraySegment[T]:
        """Forms a slice out of the current array segment starting at the specified index."""
    
    @overload
    def Slice(self, index: IntType, count: IntType) -> ArraySegment[T]:
        """Forms a slice of the specified length out of the current array
        segment starting at the specified index."""
    
    def ToArray(self) -> ArrayType[T]:
        """Copies the contents of this array segment into a new array."""
    
    @overload
    def __getitem__(self, key) -> Union[T, ArraySegment[T]]:
        """Gets the element at the specified index."""
    
    @overload
    def __setitem__(self, key, value: Union[T, ArraySegment[T]]) -> VoidType:
        """Sets the element at the specified index."""
    
    @staticmethod
    def Equality(left: ArraySegment[T], right: ArraySegment[T]) -> BooleanType:
        """Indicates whether two ArraySegment[T] structures are equal."""
    
    @staticmethod
    def Implicit(array: ArrayType[T]) -> ArraySegment[T]:
        """Defines an implicit conversion of an array of type T to an array segment of type T."""
    
    @staticmethod
    def Inequality(left: ArraySegment[T], right: ArraySegment[T]) -> BooleanType:
        """Indicates whether two ArraySegment[T] structures are unequal."""
    
    __eq__ = Equality
    __ne__ = Inequality
    
    op_Equality = Equality
    op_Implicit = Implicit
    op_Inequality = Inequality


class Enumerator(ValueType, Generic[T], IEnumerator[T], IDisposable):
    """Provides an enumerator for the elements of an ArraySegment[T]."""
    
    @property
    def Current(self) -> T:
        """Gets a reference to the item at the current position of the enumerator."""
    
    def MoveNext(self) -> BooleanType:
        """Advances the enumerator to the next element of the ArraySegment[T]."""
    
    def __iter__(self): ...
    
    def __next__(self): ...


# noinspection PyFinal
class Boolean(bool, ValueType, IComparable, IComparable[BooleanType], IConvertible, IEquatable[BooleanType]):
    """Represents a Boolean (true or false) value."""
    
    FalseString: Final[StringType] = ...
    """Represents the Boolean value false as a string. This field is read-only."""
    
    TrueString: Final[StringType] = ...
    """Represents the Boolean value true as a string. This field is read-only."""
    
    @overload
    def CompareTo(self, value: BooleanType) -> IntType:
        """Compares this instance to a specified Boolean object and returns
        an integer that indicates their relationship to one another."""
    
    @overload
    def Equals(self, obj: BooleanType) -> BooleanType:
        """Returns a value indicating whether this instance is equal to a
        specified Boolean object."""
    
    @staticmethod
    @overload
    def Parse(value: ReadOnlySpan[Char]) -> BooleanType:
        """Converts the specified span representation of a logical value to
        its Boolean equivalent."""
    
    @staticmethod
    @overload
    def Parse(value: StringType) -> BooleanType:
        """Converts the specified string representation of a logical value
        to its Boolean equivalent."""
    
    @overload
    def ToString(self) -> StringType:
        """Converts the value of this instance to its equivalent string
        representation (either "True" or "False")."""
    
    def TryFormat(self, destination: Span[Char], charsWritten: Int32) -> BooleanType:
        """Tries to format the value of the current boolean instance into the
        provided span of characters."""
    
    @overload
    def TryParse(self, value: ReadOnlySpan[Char], result: Boolean) -> BooleanType:
        """Tries to convert the specified span representation of a logical
        value to its Boolean equivalent."""
    
    @overload
    def TryParse(self, value: NullableType[String], result: Boolean) -> BooleanType:
        """Tries to convert the specified string representation of a logical
        value to its Boolean equivalent."""


class Byte(int, ValueType, IComparable, IComparable[ByteType], IConvertible, IEquatable[ByteType], ISpanFormattable):
    """Represents an 8-bit unsigned integer."""
    
    MaxValue: Final[ByteType] = ...
    """Represents the largest possible value of a Byte. This field is constant."""
    
    MinValue: Final[ByteType] = ...
    """Represents the smallest possible value of a Byte. This field is constant."""
    
    @overload
    def CompareTo(self, obj: ByteType) -> IntType:
        """Compares this instance to a specified 8-bit unsigned integer and
        returns an indication of their relative values."""
    
    @overload
    def Equals(self, obj: ByteType) -> BooleanType:
        """Returns a value indicating whether this instance and a specified
        Byte object represent the same value."""
    
    @staticmethod
    @overload
    def Parse(value: ReadOnlySpan[Char]) -> ByteType:
        """Converts the span representation of a number in a specified style
        and culture-specific format to its Byte equivalent."""
    
    @staticmethod
    @overload
    def Parse(value: StringType) -> ByteType:
        """Converts the string representation of a number to its Byte equivalent."""
    
    @staticmethod
    @overload
    def Parse(value: StringType, provider: NullableType[IFormatProvider]) -> ByteType:
        """Converts the string representation of a number in a specified
        culture-specific format to its Byte equivalent."""
    
    @staticmethod
    @overload
    def Parse(value: StringType, style: NumberStyles) -> ByteType:
        """Converts the string representation of a number in a specified style
        to its Byte equivalent."""
    
    @staticmethod
    @overload
    def Parse(value: StringType, style: NumberStyles, provider: NullableType[IFormatProvider]) -> ByteType:
        """Converts the string representation of a number in a specified
        style and culture-specific format to its Byte equivalent."""
    
    @overload
    def ToString(self) -> StringType:
        """Converts the value of the current Byte object to its equivalent
        string representation."""
    
    @overload
    def ToString(self, provider: NullableType[IFormatProvider]) -> StringType:
        """Converts the numeric value of the current Byte object to its
        equivalent string representation using the specified
        culture-specific formatting information."""
    
    @overload
    def ToString(self, format: NullableType[StringType]) -> StringType:
        """Converts the value of the current Byte object to its equivalent
        string representation using the specified format."""
    
    @overload
    def ToString(self, format: NullableType[StringType], provider: NullableType[IFormatProvider]) -> StringType:
        """Converts the value of the current Byte object to its equivalent
        string representation using the specified format and culture-specific
        formatting information."""
    
    def TryFormat(self, destination: Span[Char], charsWritten: Int32, format: ReadOnlySpan[Char] = None, provider: IFormatProvider = None) -> BooleanType:
        """Tries to format the value of the current 8-bit unsigned integer
        instance into the provided span of characters."""
    
    @overload
    def TryParse(self, s: ReadOnlySpan[Char], result: Byte) -> BooleanType:
        """Tries to convert the span representation of a number to its Byte
        equivalent, and returns a value that indicates whether the
        conversion succeeded."""
    
    @overload
    def TryParse(self, s: ReadOnlySpan[Char], style: NumberStyles, provider: NullableType[IFormatProvider], result: Byte) -> BooleanType:
        """Converts the span representation of a number in a specified style
        and culture-specific format to its Byte equivalent. A return value
        indicates whether the conversion succeeded or failed."""
    
    @overload
    def TryParse(self, s: NullableType[String], result: Byte) -> BooleanType:
        """Tries to convert the string representation of a number to its Byte
        equivalent, and returns a value that indicates whether the conversion
        succeeded."""
    
    @overload
    def TryParse(self, String, style: NumberStyles, provider: NullableType[IFormatProvider], result: Byte) -> BooleanType:
        """Converts the string representation of a number in a specified style
        and culture-specific format to its Byte equivalent. A return value
        indicates whether the conversion succeeded or failed."""


class Char(str, ValueType, IComparable, IComparable[CharType], IConvertible, IEquatable[CharType], ISpanFormattable):
    """Represents a character as a UTF-16 code unit."""
    
    MaxValue: Final[CharType] = ...
    """Represents the largest possible value of a Char. This field is constant."""
    
    MinValue: Final[CharType] = ...
    """Represents the smallest possible value of a Char. This field is constant."""
    
    @overload
    def CompareTo(self, obj: NullableType[CharType]) -> IntType:
        """Compares this instance to a specified Char object and indicates
        whether this instance precedes, follows, or appears in the same
        position in the sort order as the specified Char object."""
    
    @staticmethod
    def ConvertFromUtf32(utf32: IntType) -> StringType:
        """Converts the specified Unicode code point into a UTF-16 encoded string."""
    
    @staticmethod
    @overload
    def ConvertToUtf32(highSurrogate: CharType, lowSurrogate: CharType) -> IntType:
        """Converts the value of a UTF-16 encoded surrogate pair into a Unicode code point."""
    
    @staticmethod
    @overload
    def ConvertToUtf32(s: StringType, index: IntType) -> IntType:
        """Converts the value of a UTF-16 encoded character or surrogate pair
        at a specified position in a string into a Unicode code point."""
    
    def Equals(self, obj: CharType) -> BooleanType:
        """Returns a value that indicates whether this instance is equal to the
        specified Char object."""
    
    @staticmethod
    @overload
    def GetNumericValue(c: CharType) -> DoubleType:
        """Converts the specified numeric Unicode character to a
        double-precision floating point number."""
    
    @staticmethod
    @overload
    def GetNumericValue(s: StringType, index: IntType) -> DoubleType:
        """Converts the numeric Unicode character at the specified position
        in a specified string to a double-precision floating point number."""
    
    @staticmethod
    @overload
    def GetUnicodeCategory(c: CharType) -> UnicodeCategory:
        """Categorizes a specified Unicode character into a group identified
        by one of the UnicodeCategory values."""
    
    @staticmethod
    @overload
    def GetUnicodeCategory(s: StringType, index: IntType) -> UnicodeCategory:
        """Categorizes the character at the specified position in a specified
        string into a group identified by one of the UnicodeCategory values."""
    
    @staticmethod
    def IsAscii(c: CharType) -> BooleanType:
        """Returns true if c is an ASCII character ([ U+0000..U+007F ])."""
    
    @staticmethod
    @overload
    def IsControl(c: CharType) -> BooleanType:
        """Indicates whether the specified Unicode character is categorized
        as a control character."""
    
    @staticmethod
    @overload
    def IsControl(s: StringType, index: IntType) -> BooleanType:
        """Indicates whether the character at the specified position in a
        specified string is categorized as a control character."""
    
    @staticmethod
    @overload
    def IsDigit(c: CharType) -> BooleanType:
        """Indicates whether the specified Unicode character is categorized
        as a decimal digit."""
    
    @staticmethod
    @overload
    def IsDigit(s: StringType, index: IntType) -> BooleanType:
        """Indicates whether the character at the specified position in a
        specified string is categorized as a decimal digit."""
    
    @staticmethod
    @overload
    def IsHighSurrogate(c: CharType) -> BooleanType:
        """Indicates whether the specified Char object is a high surrogate."""
    
    @staticmethod
    @overload
    def IsHighSurrogate(s: StringType, index: IntType) -> BooleanType:
        """Indicates whether the Char object at the specified position in a
        string is a high surrogate."""
    
    @staticmethod
    @overload
    def IsLetter(c: CharType) -> BooleanType:
        """Indicates whether the specified Unicode character is categorized
        as a Unicode letter."""
    
    @staticmethod
    @overload
    def IsLetter(s: StringType, index: IntType) -> BooleanType:
        """Indicates whether the character at the specified position in a
        specified string is categorized as a Unicode letter."""
    
    @staticmethod
    @overload
    def IsLetterOrDigit(c: CharType) -> BooleanType:
        """Indicates whether the specified Unicode character is categorized
        as a letter or a decimal digit."""
    
    @staticmethod
    @overload
    def IsLetterOrDigit(s: StringType, index: IntType) -> BooleanType:
        """Indicates whether the character at the specified position in a
        specified string is categorized as a letter or a decimal digit."""
    
    @staticmethod
    @overload
    def IsLower(c: CharType) -> BooleanType:
        """Indicates whether the specified Unicode character is categorized
        as a lowercase letter."""
    
    @staticmethod
    @overload
    def IsLower(s: StringType, index: IntType) -> BooleanType:
        """Indicates whether the character at the specified position in a
        specified string is categorized as a lowercase letter."""
    
    @staticmethod
    @overload
    def IsLowSurrogate(c: CharType) -> BooleanType:
        """Indicates whether the specified Char object is a low surrogate."""
    
    @staticmethod
    @overload
    def IsLowSurrogate(s: StringType, index: IntType) -> BooleanType:
        """Indicates whether the Char object at the specified position in a
        string is a low surrogate."""
    
    @staticmethod
    @overload
    def IsNumber(c: CharType) -> BooleanType:
        """Indicates whether the specified Unicode character is categorized as a number."""
    
    @staticmethod
    @overload
    def IsNumber(s: StringType, index: IntType) -> BooleanType:
        """Indicates whether the character at the specified position in a
        specified string is categorized as a number."""
    
    @staticmethod
    @overload
    def IsPunctuation(c: CharType) -> BooleanType:
        """Indicates whether the specified Unicode character is categorized
        as a punctuation mark."""
    
    @staticmethod
    @overload
    def IsPunctuation(s: StringType, index: IntType) -> BooleanType:
        """Indicates whether the character at the specified position in a
        specified string is categorized as a punctuation mark."""
    
    @staticmethod
    @overload
    def IsSeparator(c: CharType) -> BooleanType:
        """Indicates whether the specified Unicode character is categorized
        as a separator character."""
    
    @staticmethod
    @overload
    def IsSeparator(s: StringType, index: IntType) -> BooleanType:
        """Indicates whether the character at the specified position in a
        specified string is categorized as a separator character."""
    
    @staticmethod
    @overload
    def IsSurrogate(c: CharType) -> BooleanType:
        """Indicates whether the specified character has a surrogate code unit."""
    
    @staticmethod
    @overload
    def IsSurrogate(s: StringType, index: IntType) -> BooleanType:
        """Indicates whether the character at the specified position in a
        specified string has a surrogate code unit."""
    
    @staticmethod
    @overload
    def IsSurrogatePair(highSurrogate: CharType, lowSurrogate: CharType) -> BooleanType:
        """Indicates whether the two specified Char objects form a surrogate pair."""
    
    @staticmethod
    @overload
    def IsSurrogatePair(s: StringType, index: IntType) -> BooleanType:
        """Indicates whether two adjacent Char objects at a specified position
        in a string form a surrogate pair."""
    
    @staticmethod
    @overload
    def IsSymbol(c: CharType) -> BooleanType:
        """Indicates whether the specified Unicode character is categorized
        as a symbol character."""
    
    @staticmethod
    @overload
    def IsSymbol(s: StringType, index: IntType) -> BooleanType:
        """Indicates whether the character at the specified position in a
        specified string is categorized as a symbol character."""
    
    @staticmethod
    @overload
    def IsUpper(c: CharType) -> BooleanType:
        """Indicates whether the specified Unicode character is categorized
        as an uppercase letter."""
    
    @staticmethod
    @overload
    def IsUpper(s: StringType, index: IntType) -> BooleanType:
        """Indicates whether the character at the specified position in a
        specified string is categorized as an uppercase letter."""
    
    @staticmethod
    @overload
    def IsWhiteSpace(c: CharType) -> BooleanType:
        """Indicates whether the specified Unicode character is categorized as white space."""
    
    @staticmethod
    @overload
    def IsWhiteSpace(s: StringType, index: IntType) -> BooleanType:
        """Indicates whether the character at the specified position in a
        specified string is categorized as white space."""
    
    @staticmethod
    def Parse(s: StringType) -> CharType:
        """Converts the value of the specified string to its equivalent Unicode character."""
    
    @staticmethod
    @overload
    def ToLower(c: CharType) -> CharType:
        """Converts the value of a Unicode character to its lowercase equivalent."""
    
    @staticmethod
    @overload
    def ToLower(c: CharType, culture: CultureInfo) -> CharType:
        """Converts the value of a specified Unicode character to its
        lowercase equivalent using specified culture-specific
        formatting information."""
    
    @staticmethod
    def ToLowerInvariant(c: CharType) -> CharType:
        """Converts the value of a Unicode character to its lowercase
        equivalent using the casing rules of the invariant culture."""
    
    @overload
    def ToString(self) -> StringType:
        """Converts the value of this instance to its equivalent string representation."""
    
    @staticmethod
    @overload
    def ToString(c: CharType) -> StringType:
        """Converts the specified Unicode character to its equivalent string representation."""
    
    @overload
    def ToString(self, provider: NullableType[IFormatProvider]) -> StringType:
        """Converts the value of this instance to its equivalent string
        representation using the specified culture-specific format
        information."""
    
    @staticmethod
    @overload
    def ToUpper(c: CharType) -> CharType:
        """Converts the value of a Unicode character to its uppercase equivalent."""
    
    @staticmethod
    @overload
    def ToUpper(c: CharType, culture: CultureInfo) -> CharType:
        """Converts the value of a specified Unicode character to its
        uppercase equivalent using specified culture-specific formatting
        information."""
    
    @staticmethod
    def ToUpperInvariant(c: CharType) -> CharType:
        """Converts the value of a Unicode character to its uppercase
        equivalent using the casing rules of the invariant culture."""
    
    @staticmethod
    def TryParse(s: NullableType[StringType], result: Char) -> BooleanType:
        """Converts the value of the specified string to its equivalent
        Unicode character. A return code indicates whether the conversion
        succeeded or failed."""


class ConsoleKeyInfo(ValueType, IEquatable[ConsoleKeyInfo]):
    """Describes the console key that was pressed, including the character
    represented by the console key and the state of the SHIFT, ALT, and CTRL
    modifier keys."""
    
    def __init__(self, keyChar: CharType, key: ConsoleKey, shift: BooleanType, alt: BooleanType, control: BooleanType):
        """Initializes a new instance of the ConsoleKeyInfo structure using
        the specified character, console key, and modifier keys."""
    
    @property
    def Key(self) -> ConsoleKey:
        """Gets the console key represented by the current ConsoleKeyInfo object."""
    
    @property
    def KeyChar(self) -> CharType:
        """Gets the Unicode character represented by the current ConsoleKeyInfo object."""
    
    @property
    def Modifiers(self) -> ConsoleModifiers:
        """Gets a bitwise combination of ConsoleModifiers values that
        specifies one or more modifier keys pressed simultaneously with the
        console key."""
    
    def Equals(self, obj: ConsoleKeyInfo) -> BooleanType:
        """Gets a value indicating whether the specified ConsoleKeyInfo
        object is equal to the current ConsoleKeyInfo object."""
    
    @staticmethod
    def Equality(left: ConsoleKeyInfo, right: ConsoleKeyInfo) -> BooleanType:
        """Indicates whether the specified ConsoleKeyInfo objects are equal."""
    
    @staticmethod
    def Inequality(left: ConsoleKeyInfo, right: ConsoleKeyInfo) -> BooleanType:
        """Indicates whether the specified ConsoleKeyInfo objects are not equal."""
    
    __eq__ = Equality
    __ne__ = Inequality
    
    op_Equality = Equality
    op_Inequality = Inequality


class DateOnly(ValueType, IComparable, IComparable[DateOnly], IEquatable[DateOnly], IFormattable, ISpanFormattable):
    """Represents dates with values ranging from January 1, 0001 Anno Domini
    (Common Era) through December 31, 9999 A.D. (C.E.) in the Gregorian
    calendar."""
    
    @overload
    def __init__(self, year: IntType, month: IntType, day: IntType):
        """Creates a new instance of the DateOnly structure to the specified
        year, month, and day."""
    
    @overload
    def __init__(self, year: IntType, month: IntType, day: IntType, calendar: Calendar):
        """Creates a new instance of the DateOnly structure to the specified
        year, month, and day for the specified calendar."""
    
    @property
    def Day(self) -> IntType:
        """Gets the day component of the date represented by this instance."""
    
    @property
    def DayNumber(self) -> IntType:
        """Gets the number of days since January 1, 0001 in the Proleptic
        Gregorian calendar represented by this instance."""
    
    @property
    def DayOfWeek(self) -> DayOfWeek:
        """Gets the day of the week represented by this instance."""
    
    @property
    def DayOfYear(self) -> IntType:
        """Gets the day of the year represented by this instance."""
    
    @staticmethod
    @property
    def MaxValue() -> DateOnly:
        """Gets the latest possible date that can be created."""
    
    @staticmethod
    @property
    def MinValue() -> DateOnly:
        """Gets the earliest possible date that can be created."""
    
    @property
    def Month(self) -> IntType:
        """Gets the month component of the date represented by this instance."""
    
    @property
    def Year(self) -> IntType:
        """Gets the year component of the date represented by this instance."""
    
    def AddDays(self, value: IntType) -> DateOnly:
        """Adds the specified number of days to the value of this instance."""
    
    def AddMonths(self, value: IntType) -> DateOnly:
        """Adds the specified number of months to the value of this instance."""
    
    def AddYears(self, value: IntType) -> DateOnly:
        """Adds the specified number of years to the value of this instance."""
    
    def CompareTo(self, value: DateOnly) -> IntType:
        """Compares the value of this instance to a specified DateOnly value
        and returns an integer that indicates whether this instance is
        earlier than, the same as, or later than the specified DateTime
        value."""
    
    def Equals(self, value: DateOnly) -> BooleanType:
        """Returns a value indicating whether the value of this instance is
        equal to the value of the specified DateOnly instance."""
    
    @staticmethod
    def FromDateTime(dateTime: DateTime) -> DateOnly:
        """Returns a DateOnly instance that is set to the date part of the
        specified dateTime."""
    
    @staticmethod
    def FromDayNumber(datNumber: IntType) -> DateOnly:
        """Creates a new instance of the DateOnly structure to the specified
        number of days."""
    
    @staticmethod
    @overload
    def Parse(s: ReadOnlySpan[Char], provider: NullableType[IFormatProvider] = None, style: DateTimeStyles = 0) -> DateOnly:
        """Converts a memory span that contains string representation of a
        date to its DateOnly equivalent by using culture-specific format
        information and a formatting style."""
    
    @staticmethod
    @overload
    def Parse(S: StringType) -> DateOnly:
        """Converts a string that contains string representation of a date to
        its DateOnly equivalent by using the conventions of the current
        culture."""
    
    @staticmethod
    @overload
    def Parse(S: StringType, provider: NullableType[IFormatProvider], style: DateTimeStyles = 0) -> DateOnly:
        """Converts a string that contains string representation of a date to
        its DateOnly equivalent by using culture-specific format information
        and a formatting style."""
    
    @staticmethod
    @overload
    def ParseExact(s: ReadOnlySpan[Char], format: ReadOnlySpan[Char], provider: NullableType[IFormatProvider] = None, style: DateTimeStyles = 0) -> DateOnly:
        """Converts the specified span representation of a date to its
        DateOnly equivalent using the specified format, culture-specific
        format information, and style. The format of the string
        representation must match the specified format exactly or an
        exception is thrown."""
    
    @staticmethod
    @overload
    def ParseExact(s: ReadOnlySpan[Char], formats: ArrayType[StringType]) -> DateOnly:
        """Converts the specified span representation of a date to its
        DateOnly equivalent using the specified array of formats. The format
        of the string representation must match at least one of the specified
        formats exactly or an exception is thrown."""
    
    @staticmethod
    @overload
    def ParseExact(s: ReadOnlySpan[Char], formats: ArrayType[StringType], provider: NullableType[IFormatProvider] = None, style: DateTimeStyles = 0) -> DateOnly:
        """Converts the specified span representation of a date to its
        DateOnly equivalent using the specified array of formats,
        culture-specific format information, and style. The format of the
        string representation must match at least one of the specified
        formats exactly or an exception is thrown."""
    
    @staticmethod
    @overload
    def ParseExact(s: StringType, format: StringType) -> DateOnly:
        """Converts the specified string representation of a date to its
        DateOnly equivalent using the specified format. The format of the
        string representation must match the specified format exactly or an
        exception is thrown."""
    
    @staticmethod
    @overload
    def ParseExact(s: StringType, format: StringType, provider: NullableType[IFormatProvider], style: DateTimeStyles = 0) -> DateOnly:
        """Converts the specified string representation of a date to its
        DateOnly equivalent using the specified format, culture-specific
        format information, and style. The format of the string
        representation must match the specified format exactly or an
        exception is thrown."""
    
    @staticmethod
    @overload
    def ParseExact(s: StringType, formats: ArrayType[StringType]) -> DateOnly:
        """Converts the specified span representation of a date to its
        DateOnly equivalent using the specified array of formats. The format
        of the string representation must match at least one of the specified
        formats exactly or an exception is thrown."""
    
    @staticmethod
    @overload
    def ParseExact(s: StringType, formats: ArrayType[StringType], provider: NullableType[IFormatProvider], style: DateTimeStyles = 0) -> DateOnly:
        """Converts the specified string representation of a date to its
        DateOnly equivalent using the specified array of formats,
        culture-specific format information, and style. The format of the
        string representation must match at least one of the specified
        formats exactly or an exception is thrown."""
    
    @overload
    def ToDateTime(self, time: TimeOnly) -> DateTime:
        """Returns a DateTime that is set to the date of this DateOnly
        instance and the time of specified input time."""
    
    @overload
    def ToDateTime(self, time: TimeOnly, kind: DateTimeKind) -> DateTime:
        """Returns a DateTime instance with the specified input kind that is
        set to the date of this DateOnly instance and the time of specified
        input time."""
    
    def ToLongDateString(self) -> StringType:
        """Converts the value of the current DateOnly object to its
        equivalent long date string representation."""
    
    def ToShortDateString(self) -> StringType:
        """Converts the value of the current DateOnly object to its
        equivalent short date string representation."""
    
    @overload
    def ToString(self) -> StringType:
        """Converts the value of the current DateOnly object to its
        equivalent string representation using the formatting conventions
        of the current culture. The DateOnly object will be formatted in
        short form."""
    
    @overload
    def ToString(self, provider: NullableType[IFormatProvider]) -> StringType:
        """Converts the value of the current DateOnly object to its
        equivalent string representation using the specified culture-specific
        format information."""
    
    @overload
    def ToString(self, format: NullableType[StringType]) -> StringType:
        """Converts the value of the current DateOnly object to its
        equivalent string representation using the specified format and the
        formatting conventions of the current culture."""
    
    @overload
    def ToString(self, format: NullableType[StringType], provider: NullableType[IFormatProvider]) -> StringType:
        """Converts the value of the current DateOnly object to its
        equivalent string representation using the specified culture-specific
        format information."""
    
    def TryFormat(self, destination: Span[Char], charsWritten: Int32, format: ReadOnlySpan[Char] = None, provider: NullableType[IFormatProvider] = None) -> BooleanType:
        """Tries to format the value of the current DateOnly instance into
        the provided span of characters."""
    
    @staticmethod
    @overload
    def TryParse(s: ReadOnlySpan[Char], result: DateOnly) -> BooleanType:
        """Converts the specified span representation of a date to its
        DateOnly equivalent and returns a value that indicates whether the
        conversion succeeded."""
    
    @staticmethod
    @overload
    def TryParse(s: ReadOnlySpan[Char], provider: NullableType[IFormatProvider], style: DateTimeStyles, result: DateOnly) -> BooleanType:
        """Converts the specified span representation of a date to its
        DateOnly equivalent using the specified array of formats,
        culture-specific format information, and style. And returns a value
        that indicates whether the conversion succeeded."""
    
    @staticmethod
    @overload
    def TryParse(s: NullableType[StringType], result: DateOnly) -> BooleanType:
        """Converts the specified string representation of a date to its
        DateOnly equivalent and returns a value that indicates whether the
        conversion succeeded."""
    
    @staticmethod
    @overload
    def TryParse(s: NullableType[StringType], provider: NullableType[IFormatProvider], style: DateTimeStyles, result: DateOnly) -> BooleanType:
        """Converts the specified string representation of a date to its
        DateOnly equivalent using the specified array of formats,
        culture-specific format information, and style. And returns a value
        that indicates whether the conversion succeeded."""
    
    @staticmethod
    @overload
    def TryParseExact(s: ReadOnlySpan[Char], format: ReadOnlySpan[Char], result: DateOnly) -> BooleanType:
        """Converts the specified span representation of a date to its
        DateOnly equivalent using the specified format and style. The format
        of the string representation must match the specified format exactly.
        The method returns a value that indicates whether the conversion
        succeeded."""
    
    @staticmethod
    @overload
    def TryParseExact(s: ReadOnlySpan[Char], format: ReadOnlySpan[Char], provider: NullableType[IFormatProvider], style: DateTimeStyles, result: DateOnly) -> BooleanType:
        """Converts the specified span representation of a date to its
        DateOnlyequivalent using the specified format, culture-specific
        format information, and style. The format of the string
        representation must match the specified format exactly. The method
        returns a value that indicates whether the conversion succeeded."""
    
    @staticmethod
    @overload
    def TryParseExact(s: ReadOnlySpan[Char], formats: NullableType[ArrayType[NullableType[StringType]]], result: DateOnly) -> BooleanType:
        """Converts the specified char span of a date to its DateOnly
        equivalent and returns a value that indicates whether the conversion
        succeeded."""
    
    @staticmethod
    @overload
    def TryParseExact(s: ReadOnlySpan[Char], formats: NullableType[ArrayType[NullableType[StringType]]], provider: NullableType[IFormatProvider], style: DateTimeStyles, result: DateOnly) -> BooleanType:
        """Converts the specified char span of a date to its DateOnly
        equivalent and returns a value that indicates whether the conversion
        succeeded."""
    
    @staticmethod
    @overload
    def TryParseExact(s: NullableType[StringType], format: NullableType[StringType], result: DateOnly) -> BooleanType:
        """Converts the specified string representation of a date to its
        DateOnly equivalent using the specified format and style. The format
        of the string representation must match the specified format exactly.
        The method returns a value that indicates whether the conversion
        succeeded."""
    
    @staticmethod
    @overload
    def TryParseExact(s: NullableType[StringType], format: NullableType[StringType], provider: NullableType[IFormatProvider], style: DateTimeStyles, result: DateOnly) -> BooleanType:
        """Converts the specified span representation of a date to its
        DateOnly equivalent using the specified format, culture-specific
        format information, and style. The format of the string
        representation must match the specified format exactly. The method
        returns a value that indicates whether the conversion succeeded."""
    
    @staticmethod
    @overload
    def TryParseExact(s: NullableType[StringType], formats: NullableType[ArrayType[NullableType[StringType]]], result: DateOnly) -> BooleanType:
        """Converts the specified string of a date to its DateOnly equivalent
        and returns a value that indicates whether the conversion succeeded."""
    
    @staticmethod
    @overload
    def TryParseExact(s: NullableType[StringType], formats: NullableType[ArrayType[NullableType[StringType]]], provider: NullableType[IFormatProvider], style: DateTimeStyles, result: DateOnly) -> BooleanType:
        """Converts the specified string of a date to its DateOnly equivalent
        and returns a value that indicates whether the conversion succeeded."""
    
    @staticmethod
    def Equality(left: DateOnly, right: DateOnly) -> BooleanType:
        """Determines whether two specified instances of DateOnly are equal."""
    
    @staticmethod
    def GreaterThan(left: DateOnly, right: DateOnly) -> BooleanType:
        """Determines whether one specified DateOnly is later than another
        specified DateTime."""
    
    @staticmethod
    def GreaterThanOrEqual(left: DateOnly, right: DateOnly) -> BooleanType:
        """Determines whether one specified DateOnly represents a date that
        is the same as or later than another specified DateOnly."""
    
    @staticmethod
    def Inequality(left: DateOnly, right: DateOnly) -> BooleanType:
        """Determines whether two specified instances of DateOnly are not equal."""
    
    @staticmethod
    def LessThan(left: DateOnly, right: DateOnly) -> BooleanType:
        """Determines whether one specified DateOnly is earlier than another
        specified DateOnly."""
    
    @staticmethod
    def LessThanOrEqual(left: DateOnly, right: DateOnly) -> BooleanType:
        """Determines whether one specified DateOnly represents a date that
        is the same as or earlier than another specified DateOnly."""
    
    __eq__ = Equality
    __gt__ = GreaterThan
    __ge__ = GreaterThanOrEqual
    __ne__ = Inequality
    __lt__ = LessThan
    __le__ = LessThanOrEqual
    
    op_Equality = Equality
    op_GreaterThan = GreaterThan
    op_GreaterThanOrEqual = GreaterThanOrEqual
    op_Inequality = Inequality
    op_LessThan = LessThan
    op_LessThanOrEqual = LessThanOrEqual


class DateTime:
    """Represents an instant in time, typically expressed as a date and time of day."""


class DateTimeOffset:
    """Represents a point in time, typically expressed as a date and time of day, relative to Coordinated Universal Time (UTC)."""


class Decimal:
    """Represents a decimal floating-point number."""


class Double:
    """Represents a double-precision floating-point number."""


class GCGenerationInfo:
    """Represents the size and the fragmenation of a generation on entry and on exit of the GC reported in GCMemoryInfo."""


class GCMemoryInfo:
    """Provides a set of APIs that can be used to retrieve garbage collection information."""


class Guid:
    """Represents a globally unique identifier (GUID)."""


class Half:
    """Represents a half-precision floating-point number."""


class HashCode:
    """Combines the hash code for multiple values into a single hash code."""


class Index:
    """Represents a type that can be used to index a collection either from the beginning or the end."""


class Int16:
    """Represents a 16-bit signed integer."""


class Int32(int, ValueType, IComparable, IComparable[IntType], IConvertible, IEquatable[IntType], ISpanFormattable):
    """Represents a 32-bit signed integer."""


class Int64:
    """Represents a 64-bit signed integer."""


class IntPtr:
    """A platform-specific type that is used to represent a pointer or a handle."""


class Memory(Generic[T]):
    """Represents a contiguous region of memory."""


class ModuleHandle:
    """Represents a runtime handle for a module."""


class Nullable(ValueType, Generic[T], Optional):
    """Represents a value type that can be assigned null."""
    
    @staticmethod
    def Compare(n1: NullableType[T], n2: NullableType[T]) -> IntType:
        """Compares the relative values of two Nullable[T] objects."""
    
    @staticmethod
    def Equals(n1: NullableType[T], n2: NullableType[T]) -> BooleanType:
        """Indicates whether two specified Nullable[T] objects are equal."""
    
    @staticmethod
    def GetUnderlyingType(nullableType: TypeType) -> NullableType[TypeType]:
        """Returns the underlying type argument of the specified nullable type."""
    
    def __init__(self, value: T):
        """Initializes a new instance of the Nullable[T] structure to the
        specified value."""
    
    @property
    def HasValue(self) -> BooleanType:
        """Gets a value indicating whether the current Nullable[T] object has
        a valid value of its underlying type."""
    
    @property
    def Value(self) -> T:
        """Gets the value of the current Nullable[T] object if it has been
        assigned a valid underlying value."""
    
    @overload
    def GetValueOrDefault(self) -> T:
        """Retrieves the value of the current Nullable[T] object, or the
        default value of the underlying type."""
    
    @overload
    def GetValueOrDefault(self, defaultValue: T) -> T:
        """Retrieves the value of the current Nullable[T] object, or the
        specified default value."""
    
    @staticmethod
    def Explicit(value: NullableType[T]) -> T:
        """Defines an explicit conversion of a Nullable[T] instance to its underlying value."""
    
    @staticmethod
    def Implicit(value: T) -> NullableType[T]:
        """Creates a new Nullable[T] object initialized to a specified value."""
    
    op_Explicit = Explicit
    op_Implicit = Implicit


class Range:
    """Represents a range that has start and end indexes."""


class ReadOnlyMemory(Generic[T]):
    """Represents a contiguous region of memory, similar to ReadOnlySpan[T]. Unlike ReadOnlySpan[T], it is not a byref-like type."""


class ReadOnlySpan(Generic[T]):
    """Provides a type-safe and memory-safe read-only representation of a contiguous region of arbitrary memory."""
    
    class Enumerator:
        """Provides an enumerator for the elements of a ReadOnlySpan[T]."""


class RuntimeArgumentHandle:
    """References a variable-length argument list."""


class RuntimeFieldHandle:
    """Represents a field using an internal metadata token."""


class RuntimeMethodHandle:
    """RuntimeMethodHandle is a handle to the internal metadata representation of a method."""


class RuntimeTypeHandle:
    """Represents a type using an internal metadata token."""


class SByte:
    """Represents an 8-bit signed integer."""


class SequencePosition:
    """Represents a position in a non-contiguous set of memory. Properties of this type should not be interpreted by anything but the type that created it."""


class Single:
    """Represents a single-precision floating-point number."""


class Span(Generic[T]):
    """Provides a type- and memory-safe representation of a contiguous region of arbitrary memory."""
    
    class Enumerator:
        """Provides an enumerator for the elements of a Span[T]."""


class TimeOnly:
    """Represents a time of day, as would be read from a clock, within the range 00:00:00 to 23:59:59.9999999."""


class TimeSpan:
    """Represents a time interval."""


class TypedReference:
    """Describes objects that contain both a managed pointer to a location and a runtime representation of the type that may be stored at that location."""


class UInt16:
    """Represents a 16-bit unsigned integer."""


class UInt32:
    """Represents a 32-bit unsigned integer."""


class UInt64:
    """Represents a 64-bit unsigned integer."""


class UIntPtr:
    """A platform-specific type that is used to represent a pointer or a handle."""


class UriCreationOptions:
    """Provides options that control how a Uri is created and behaves."""


@overload
class ValueTuple(ValueType, IComparable, IComparable[ValueTuple], IEquatable[ValueTuple], IStructuralComparable, IStructuralEquatable, ITuple):
    """Provides static methods for creating value tuples."""


@overload
class ValueTuple(Generic[T1]):
    """Represents a value tuple with a single component."""


@overload
class ValueTuple(Generic[T1, T2]):
    """Represents a value tuple with 2 components."""


@overload
class ValueTuple(Generic[T1, T2, T3]):
    """Represents a value tuple with 3 components."""


@overload
class ValueTuple(Generic[T1, T2, T3, T4]):
    """Represents a value tuple with 4 components."""


@overload
class ValueTuple(Generic[T1, T2, T3, T4, T5]):
    """Represents a value tuple with 5 components."""


@overload
class ValueTuple(Generic[T1, T2, T3, T4, T5, T6]):
    """Represents a value tuple with 6 components."""


@overload
class ValueTuple(Generic[T1, T2, T3, T4, T5, T6, T7]):
    """Represents a value tuple with 7 components."""


@overload
class ValueTuple(Generic[T1, T2, T3, T4, T5, T6, T7, TRest]):
    """Represents an n-value tuple, where n is 8 or greater."""


class Void(None):
    """Specifies a return value type for a method that does not return a value."""


# ---------- INTERFACES ---------- #


class IAsyncDisposable(Protocol):
    """Provides a mechanism for releasing unmanaged resources asynchronously."""
    
    def DisposeAsync(self) -> ValueTask:
        """Performs application-defined tasks associated with freeing,
        releasing, or resetting unmanaged resources asynchronously."""
    
    def ConfigureAwait(self, source: IAsyncDisposable, continueOnCapturedContext: BooleanType) -> ConfiguredAsyncDisposable:
        """Configures how awaits on the tasks returned from an async disposable are performed."""


class IAsyncResult(Protocol):
    """Represents the status of an asynchronous operation."""
    
    @property
    def AsyncState(self) -> NullableType[ObjectType]:
        """Gets a user-defined object that qualifies or contains information
        about an asynchronous operation."""
    
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """Gets a WaitHandle that is used to wait for an asynchronous
        operation to complete."""
    
    @property
    def CompletedSynchronously(self) -> BooleanType:
        """Gets a value that indicates whether the asynchronous operation
        completed synchronously."""
    
    @property
    def IsCompleted(self) -> BooleanType:
        """Gets a value that indicates whether the asynchronous operation
        has completed."""


class ICloneable(Protocol):
    """Supports cloning, which creates a new instance of a class with the
    same value as an existing instance."""
    
    def Clone(self) -> ObjectType:
        """Creates a new object that is a copy of the current instance."""


class IComparable(Protocol[T]):
    """Defines a generalized type-specific comparison method that a value
    type or class implements to order or sort its instances."""
    
    @overload
    def CompareTo(self, obj: NullableType[ObjectType]) -> IntType:
        """Compares the current instance with another object of the same type
        and returns an integer that indicates whether the current instance
        precedes, follows, or occurs in the same position in the sort order as
        the other object."""
    
    @overload
    def CompareTo(self, obj: NullableType[T]) -> IntType:
        """Compares the current instance with another object of the same type and
        returns an integer that indicates whether the current instance precedes,
        follows, or occurs in the same position in the sort order as the other
        object."""


class IConvertible(Protocol):
    """Defines methods that convert the value of the implementing reference or
    value type to a common language runtime type that has an equivalent value."""
    
    def GetTypeCode(self) -> TypeCode:
        """Returns the TypeCode for this instance."""
    
    def ToBoolean(self, provider: NullableType[IFormatProvider]) -> BooleanType:
        """Converts the value of this instance to an equivalent Boolean value
        using the specified culture-specific formatting information."""
    
    def ToByte(self, provider: NullableType[IFormatProvider]) -> ByteType:
        """Converts the value of this instance to an equivalent 8-bit unsigned
        integer using the specified culture-specific formatting information."""
    
    def ToChar(self, provider: NullableType[IFormatProvider]) -> CharType:
        """Converts the value of this instance to an equivalent Unicode character
        using the specified culture-specific formatting information."""
    
    def ToDateTime(self, provider: NullableType[IFormatProvider]) -> DateTime:
        """Converts the value of this instance to an equivalent DateTime using the
        specified culture-specific formatting information."""
    
    def ToDecimal(self, provider: NullableType[IFormatProvider]) -> DecimalType:
        """Converts the value of this instance to an equivalent Decimal number using
        the specified culture-specific formatting information."""
    
    def ToDouble(self, provider: NullableType[IFormatProvider]) -> DoubleType:
        """Converts the value of this instance to an equivalent double-precision
        floating-point number using the specified culture-specific formatting
        information."""
    
    def ToInt16(self, provider: NullableType[IFormatProvider]) -> ShortType:
        """Converts the value of this instance to an equivalent 16-bit signed integer
        using the specified culture-specific formatting information."""
    
    def ToInt32(self, provider: NullableType[IFormatProvider]) -> IntType:
        """Converts the value of this instance to an equivalent 32-bit signed integer
        using the specified culture-specific formatting information."""
    
    def ToInt64(self, provider: NullableType[IFormatProvider]) -> LongType:
        """Converts the value of this instance to an equivalent 64-bit signed integer
        using the specified culture-specific formatting information."""
    
    def ToSByte(self, provider: NullableType[IFormatProvider]) -> SByteType:
        """Converts the value of this instance to an equivalent 8-bit signed integer
        using the specified culture-specific formatting information."""
    
    def ToSingle(self, provider: NullableType[IFormatProvider]) -> FloatType:
        """Converts the value of this instance to an equivalent single-precision
        floating-point number using the specified culture-specific formatting
        information."""
    
    def ToString(self, provider: NullableType[IFormatProvider]) -> StringType:
        """Converts the value of this instance to an equivalent String using the
        specified culture-specific formatting information."""
    
    def ToType(self, conversionType: TypeType, provider: NullableType[IFormatProvider]) -> ObjectType:
        """Converts the value of this instance to an Object of the specified Type that
        has an equivalent value, using the specified culture-specific formatting
        information."""
    
    def ToUInt16(self, provider: NullableType[IFormatProvider]) -> UShortType:
        """Converts the value of this instance to an equivalent 16-bit unsigned integer
        using the specified culture-specific formatting information."""
    
    def ToUInt32(self, provider: NullableType[IFormatProvider]) -> UIntType:
        """Converts the value of this instance to an equivalent 32-bit unsigned integer
        using the specified culture-specific formatting information."""
    
    def ToUInt64(self, provider: NullableType[IFormatProvider]) -> ULongType:
        """Converts the value of this instance to an equivalent 64-bit unsigned integer
        using the specified culture-specific formatting information."""


class ICustomFormatter(Protocol):
    """Defines a method that supports custom formatting of the value of an object."""
    
    def Format(self, format: NullableType[StringType], arg: NullableType[ObjectType], formatProvider: NullableType[IFormatProvider]) -> StringType:
        """Converts the value of a specified object to an equivalent string
        representation using specified format and culture-specific formatting
        information."""


class IDisposable(Protocol):
    """Provides a mechanism for releasing unmanaged resources."""
    
    def Dispose(self) -> VoidType:
        """Performs application-defined tasks associated with freeing,
        releasing, or resetting unmanaged resources."""


class IEquatable(Protocol[T]):
    """Defines a generalized method that a value type or class implements to
    create a type-specific method for determining equality of instances."""
    
    def Equals(self, obj: NullableType[T]) -> BooleanType:
        """Indicates whether the current object is equal to another object of the same type."""


class IFormatProvider(Protocol):
    """Provides a mechanism for retrieving an object to control formatting."""
    
    def GetFormat(self, formatType: NullableType[TypeType]) -> NullableType[ObjectType]:
        """Returns an object that provides formatting services for the specified type."""


class IObservable(Protocol[T]):
    """Defines a provider for push-based notification."""
    
    def Subscribe(self, observer: IObserver[T]) -> IDisposable:
        """Notifies the provider that an observer is to receive notifications."""


class IObserver(Protocol[T]):
    """Provides a mechanism for receiving push-based notifications."""
    
    def OnCompleted(self) -> VoidType:
        """Notifies the observer that the provider has finished sending push-based notifications."""
    
    def OnError(self, error: Exception) -> VoidType:
        """Notifies the observer that the provider has experienced an error condition."""
    
    def OnNext(self, value: T) -> VoidType:
        """Provides the observer with new data."""


class IProgress(Protocol[T]):
    """Defines a provider for progress updates."""
    
    def Report(self, value: T) -> VoidType:
        """Reports a progress update."""


class IFormattable(Protocol):
    """Provides functionality to format the value of an object into a string representation."""
    
    def ToString(self, format: NullableType[StringType], formatProvider: NullableType[IFormatProvider]) -> StringType:
        """Formats the value of the current instance using the specified format."""


class IServiceProvider(Protocol):
    """Defines a mechanism for retrieving a service object; that is, an
    object that provides custom support to other objects."""
    
    def GetService(self, serviceType: TypeType) -> NullableType[ObjectType]:
        """Gets the service object of the specified type."""


class ISpanFormattable(IFormattable, Protocol):
    """Provides functionality to format the string representation of an object into a span."""
    
    def TryFormat(self, destination: Span[Char], charsWritten: Int32, format: ReadOnlySpan[Char], provider: NullableType[IFormatProvider]) -> BooleanType:
        """Tries to format the value of the current instance into the provided span of characters."""


# ---------- ENUMS ---------- #

class AttributeTargets(Enum):
    """Specifies the application elements on which it is valid to apply an attribute."""
    
    All = 32767
    """Attribute can be applied to any application element."""
    
    Assembly = 1
    """Attribute can be applied to an assembly."""
    
    Class = 4
    """Attribute can be applied to a class."""
    
    Constructor = 32
    """Attribute can be applied to a constructor."""
    
    Delegate = 4096
    """Attribute can be applied to a delegate."""
    
    Enum = 16
    """Attribute can be applied to an enumeration."""
    
    Event = 512
    """Attribute can be applied to an event."""
    
    Field = 256
    """Attribute can be applied to a field."""
    
    GenericParameter = 16384
    """Attribute can be applied to a generic parameter. Currently, this
    attribute can be applied only in C#, Microsoft intermediate language
    (MSIL), and emitted code."""
    
    Interface = 1024
    """Attribute can be applied to an interface."""
    
    Method = 64
    """Attribute can be applied to a method."""
    
    Module = 2
    """Attribute can be applied to a module. Module refers to a portable
    executable file (.dll or.exe) and not a Visual Basic standard module."""
    
    Parameter = 2048
    """Attribute can be applied to a parameter."""
    
    Property = 128
    """Attribute can be applied to a property."""
    
    ReturnValue = 8192
    """Attribute can be applied to a return value."""
    
    Struct = 8
    """Attribute can be applied to a structure; that is, a value type."""


class Base64FormattingOptions(Enum):
    """Specifies whether relevant ToBase64CharArray and ToBase64String
    methods insert line breaks in their output."""
    
    InsertLineBreaks = 1
    """Inserts line breaks after every 76 characters in the string representation."""
    
    #None = 0
    """Does not insert line breaks after every 76 characters in the string representation."""


class ConsoleColor(Enum):
    """Specifies constants that define foreground and background colors for
    the console."""
    
    Black = 0
    """The color black."""
    
    Blue = 9
    """The color blue."""
    
    Cyan = 11
    """The color cyan (blue-green)."""
    
    DarkBlue = 1
    """The color dark blue."""
    
    DarkCyan = 3
    """The color dark cyan (dark blue-green)."""
    
    DarkGray = 8
    """The color dark gray."""
    
    DarkGreen = 2
    """The color dark green."""
    
    DarkMagenta = 5
    """The color dark magenta (dark purplish-red)."""
    
    DarkRed = 4
    """The color dark red."""
    
    DarkYellow = 6
    """The color dark yellow (ochre)."""
    
    Gray = 7
    """The color gray."""
    
    Green = 10
    """The color green."""
    
    Magenta = 13
    """The color magenta (purplish-red)."""
    
    Red = 12
    """The color red."""
    
    White = 15
    """The color white."""
    
    Yellow = 14
    """The color yellow."""


class ConsoleKey(Enum):
    """Specifies the standard keys on a console."""
    
    A = 65
    """The A key."""
    
    Add = 107
    """The Add key (the addition key on the numeric keypad)."""
    
    Applications = 93
    """The Application key (Microsoft Natural Keyboard)."""
    
    Attention = 246
    """The ATTN key."""
    
    B = 66
    """The B key."""
    
    Backspace = 8
    """The BACKSPACE key."""
    
    BrowserBack = 166
    """The Browser Back key."""
    
    BrowserFavorites = 171
    """The Browser Favorites key."""
    
    BrowserForward = 167
    """The Browser Forward key."""
    
    BrowserHome = 172
    """The Browser Home key."""
    
    BrowserRefresh = 168
    """The Browser Refresh key."""
    
    BrowserSearch = 170
    """The Browser Search key."""
    
    BrowserStop = 169
    """The Browser Stop key."""
    
    C = 67
    """The C key."""
    
    Clear = 12
    """The CLEAR key."""
    
    CrSel = 247
    """The CRSEL (CURSOR SELECT) key."""
    
    D = 68
    """The D key."""
    
    D0 = 48
    """The 0 key."""
    
    D1 = 49
    """The 1 key."""
    
    D2 = 50
    """The 2 key."""
    
    D3 = 51
    """The 3 key."""
    
    D4 = 52
    """The 4 key."""
    
    D5 = 53
    """The 5 key."""
    
    D6 = 54
    """The 6 key."""
    
    D7 = 55
    """The 7 key."""
    
    D8 = 56
    """The 8 key."""
    
    D9 = 57
    """The 9 key."""
    
    Decimal = 110
    """The Decimal key (the decimal key on the numeric keypad)."""
    
    Delete = 46
    """The DEL (DELETE) key."""
    
    Divide = 111
    """The Divide key (the division key on the numeric keypad)."""
    
    DownArrow = 40
    """The DOWN ARROW key."""
    
    E = 69
    """The E key."""
    
    End = 35
    """The END key."""
    
    Enter = 13
    """The ENTER key."""
    
    EraseEndOfFile = 249
    """The ERASE EOF key."""
    
    Escape = 27
    """The ESC (ESCAPE) key."""
    
    Execute = 43
    """The EXECUTE key."""
    
    ExSel = 248
    """The EXSEL (EXTEND SELECTION) key."""
    
    F = 70
    """The F key."""
    
    F1 = 112
    """The F1 key."""
    
    F10 = 121
    """The F10 key."""
    
    F11 = 122
    """The F11 key."""
    
    F12 = 123
    """The F12 key."""
    
    F13 = 124
    """The F13 key."""
    
    F14 = 125
    """The F14 key."""
    
    F15 = 126
    """The F15 key."""
    
    F16 = 127
    """The F16 key."""
    
    F17 = 128
    """The F17 key."""
    
    F18 = 129
    """The F18 key."""
    
    F19 = 130
    """The F19 key."""
    
    F2 = 113
    """The F2 key."""
    
    F20 = 131
    """The F20 key."""
    
    F21 = 132
    """The F21 key."""
    
    F22 = 133
    """The F22 key."""
    
    F23 = 134
    """The F23 key."""
    
    F24 = 135
    """The F24 key."""
    
    F3 = 114
    """The F3 key."""
    
    F4 = 115
    """The F4 key."""
    
    F5 = 116
    """The F5 key."""
    
    F6 = 117
    """The F6 key."""
    
    F7 = 118
    """The F7 key."""
    
    F8 = 119
    """The F8 key."""
    
    F9 = 120
    """The F9 key."""
    
    G = 71
    """The G key."""
    
    H = 72
    """The H key."""
    
    Help = 47
    """The HELP key."""
    
    Home = 36
    """The HOME key."""
    
    I = 73
    """The I key."""
    
    Insert = 45
    """The INS (INSERT) key."""
    
    J = 74
    """The J key."""
    
    K = 75
    """The K key."""
    
    L = 76
    """The L key."""
    
    LaunchApp1 = 182
    """The Start Application 1 key (Microsoft Natural Keyboard)."""
    
    LaunchApp2 = 183
    """The Start Application 2 key (Microsoft Natural Keyboard)."""
    
    LaunchMail = 180
    """The Start Mail key (Microsoft Natural Keyboard)."""
    
    LaunchMediaSelect = 181
    """The Select Media key (Microsoft Natural Keyboard)."""
    
    LeftArrow = 37
    """The LEFT ARROW key."""
    
    LeftWindows = 91
    """The left Windows logo key (Microsoft Natural Keyboard)."""
    
    M = 77
    """The M key."""
    
    MediaNext = 176
    """The Media Next Track key."""
    
    MediaPlay = 179
    """The Media Play/Pause key."""
    
    MediaPrevious = 177
    """The Media Previous Track key."""
    
    MediaStop = 178
    """The Media Stop key."""
    
    Multiply = 106
    """The Multiply key (the multiplication key on the numeric keypad)."""
    
    N = 78
    """The N key."""
    
    NoName = 252
    """A constant reserved for future use."""
    
    NumPad0 = 96
    """The 0 key on the numeric keypad."""
    
    NumPad1 = 97
    """The 1 key on the numeric keypad."""
    
    NumPad2 = 98
    """The 2 key on the numeric keypad."""
    
    NumPad3 = 99
    """The 3 key on the numeric keypad."""
    
    NumPad4 = 100
    """The 4 key on the numeric keypad."""
    
    NumPad5 = 101
    """The 5 key on the numeric keypad."""
    
    NumPad6 = 102
    """The 6 key on the numeric keypad."""
    
    NumPad7 = 103
    """The 7 key on the numeric keypad."""
    
    NumPad8 = 104
    """The 8 key on the numeric keypad."""
    
    NumPad9 = 105
    """The 9 key on the numeric keypad."""
    
    O = 79
    """The O key."""
    
    Oem1 = 186
    """The OEM 1 key (OEM specific)."""
    
    Oem102 = 226
    """The OEM 102 key (OEM specific)."""
    
    Oem2 = 191
    """The OEM 2 key (OEM specific)."""
    
    Oem3 = 192
    """The OEM 3 key (OEM specific)."""
    
    Oem4 = 219
    """The OEM 4 key (OEM specific)."""
    
    Oem5 = 220
    """The OEM 5 (OEM specific)."""
    
    Oem6 = 221
    """The OEM 6 key (OEM specific)."""
    
    Oem7 = 222
    """The OEM 7 key (OEM specific)."""
    
    Oem8 = 223
    """The OEM 8 key (OEM specific)."""
    
    OemClear = 254
    """The CLEAR key (OEM specific)."""
    
    OemComma = 188
    """The OEM Comma key on any country/region keyboard."""
    
    OemMinus = 189
    """The OEM Minus key on any country/region keyboard."""
    
    OemPeriod = 190
    """The OEM Period key on any country/region keyboard."""
    
    OemPlus = 187
    """The OEM Plus key on any country/region keyboard."""
    
    P = 80
    """The P key."""
    
    Pa1 = 253
    """The PA1 key."""
    
    Packet = 231
    """The PACKET key (used to pass Unicode characters with keystrokes)."""
    
    PageDown = 34
    """The PAGE DOWN key."""
    
    PageUp = 33
    """The PAGE UP key."""
    
    Pause = 19
    """The PAUSE key."""
    
    Play = 250
    """The PLAY key."""
    
    Print = 42
    """The PRINT key."""
    
    PrintScreen = 44
    """The PRINT SCREEN key."""
    
    Process = 229
    """The IME PROCESS key."""
    
    Q = 81
    """The Q key."""
    
    R = 82
    """The R key."""
    
    RightArrow = 39
    """The RIGHT ARROW key."""
    
    RightWindows = 92
    """The right Windows logo key (Microsoft Natural Keyboard)."""
    
    S = 83
    """The S key."""
    
    Select = 41
    """The SELECT key."""
    
    Separator = 108
    """The Separator key."""
    
    Sleep = 95
    """The Computer Sleep key."""
    
    Spacebar = 32
    """The SPACEBAR key."""
    
    Subtract = 109
    """The Subtract key (the subtraction key on the numeric keypad)."""
    
    T = 84
    """The T key."""
    
    Tab = 9
    """The TAB key."""
    
    U = 85
    """The U key."""
    
    UpArrow = 38
    """The UP ARROW key."""
    
    V = 86
    """The V key."""
    
    VolumeDown = 174
    """The Volume Down key (Microsoft Natural Keyboard)."""
    
    VolumeMute = 173
    """The Volume Mute key (Microsoft Natural Keyboard)."""
    
    VolumeUp = 175
    """The Volume Up key (Microsoft Natural Keyboard)."""
    
    W = 87
    """The W key."""
    
    X = 88
    """The X key."""
    
    Y = 89
    """The Y key."""
    
    Z = 90
    """The Z key."""
    
    Zoom = 251
    """The ZOOM key."""


class ConsoleModifiers(Enum):
    """Represents the SHIFT, ALT, and CTRL modifier keys on a keyboard."""
    
    Alt = 1
    """The left or right ALT modifier key."""
    
    Control = 4
    """The left or right CTRL modifier key."""
    
    Shift = 2
    """The left or right SHIFT modifier key."""


class ConsoleSpecialKey(Enum):
    """Specifies combinations of modifier and console keys that can
    interrupt the current process."""
    
    ControlBreak = 1
    """The Control modifier key plus the BREAK console key."""
    
    ControlC = 0
    """The Control modifier key plus the C console key."""


class DateTimeKind(Enum):
    """Specifies whether a DateTime object represents a local time, a
    Coordinated Universal Time (UTC), or is not specified as either loca
    time or UTC."""
    
    Local = 2
    """The time represented is local time."""
    
    Unspecified = 0
    """The time represented is not specified as either local time or
    Coordinated Universal Time (UTC)."""
    
    Utc = 1
    """The time represented is UTC."""


class DayOfWeek(Enum):
    """Specifies the day of the week."""
    
    Friday = 5
    """Indicates Friday."""
    
    Monday = 1
    """Indicates Monday."""
    
    Saturday = 6
    """Indicates Saturday."""
    
    Sunday = 0
    """Indicates Sunday."""
    
    Thursday = 4
    """Indicates Thursday."""
    
    Tuesday = 2
    """Indicates Tuesday."""
    
    Wednesday = 3
    """Indicates Wednesday."""


class EnvironmentVariableTarget(Enum):
    """Specifies the location where an environment variable is stored or
    retrieved in a set or get operation."""
    
    Machine = 2
    """The environment variable is stored or retrieved from the
    HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment
    key in the Windows operating system registry. This value should be used
    on .NET implementations running on Windows systems only."""
    
    Process = 0
    """The environment variable is stored or retrieved from the environment
    block associated with the current process."""
    
    User = 1
    """The environment variable is stored or retrieved from the
    HKEY_CURRENT_USER\Environment key in the Windows operating system
    registry. This value should be used on .NET implementations running on
    Windows systems only."""


class GCCollectionMode(Enum):
    """Specifies the behavior for a forced garbage collection."""
    
    Default = 0
    """The default setting for this enumeration, which is currently Forced."""
    
    Forced = 1
    """Forces the garbage collection to occur immediately."""
    
    Optimized = 2
    """Allows the garbage collector to determine whether the current time is
    optimal to reclaim objects."""


class GCKind(Enum):
    """Specifies the kind of a garbage collection."""
    
    Any = 0
    """Any kind of collection."""
    
    Background = 3
    """A background collection. This is always a generation 2 collection."""
    
    Ephemeral = 1
    """A gen0 or gen1 collection."""
    
    FullBlocking = 2
    """A blocking gen2 collection."""


class GCNotificationStatus(Enum):
    """Provides information about the current registration for notification
    of the next full garbage collection."""
    
    Canceled = 2
    """The current registration was canceled by the user."""
    
    Failed = 1
    """The notification failed for any reason."""
    
    NotApplicable = 4
    """This result can be caused by the following: there is no current
    registration for a garbage collection notification, a full GC has
    happened but was done as a Background GC (ie, a GC that runs mostly
    concurrently with user threads) instead of a full blocking GC. Background
    GC is enabled by default; disabling it will make the prediction accurancy
    higher but will incur larger GC pauses (See the <gcConcurrent> runtime
    setting for information about how to disable concurrent garbage
    collection.)"""
    
    Succeeded = 0
    """The notification was successful and the registration was not canceled."""
    
    Timeout = 3
    """The time specified by the millisecondsTimeout parameter for either
    WaitForFullGCApproach(Int32) or WaitForFullGCComplete(Int32) has elapsed."""


class GenericUriParserOptions(Enum):
    """Specifies options for a UriParser."""
    
    AllowEmptyAuthority = 2
    """The parser allows a URI with no authority."""
    
    Default = 0
    """The parser: requires an authority; converts backslashes into forward
    slashes; unescapes path dots, forward slashes, and back slashes; and
    removes trailing dots, empty segments, and dots-only segments."""
    
    DontCompressPath = 128
    """The parser does not canonicalize the URI."""
    
    DontConvertPathBackslashes = 64
    """The parser does not convert back slashes into forward slashes."""
    
    DontUnescapePathDotsAndSlashes = 256
    """The parser does not unescape path dots, forward slashes, or back slashes."""
    
    GenericAuthority = 1
    """The parser allows a registry-based authority."""
    
    Idn = 512
    """The parser supports Internationalized Domain Name (IDN) parsing (IDN)
    of host names. Whether IDN is used is dictated by configuration values."""
    
    IriParsing = 1024
    """The parser supports the parsing rules specified in RFC 3987 for
    International Resource Identifiers (IRI). Whether IRI is used is dictated
    by configuration values."""
    
    NoFragment = 32
    """The scheme does not define a fragment part."""
    
    NoPort = 8
    """The scheme does not define a port."""
    
    NoQuery = 16
    """The scheme does not define a query part."""
    
    NoUserInfo = 4
    """The scheme does not define a user information part."""


class LoaderOptimization(Enum):
    """An enumeration used with the LoaderOptimizationAttribute class to
    specify loader optimizations for an executable."""
    
    DisallowBindings = 4
    """Ignored by the common language runtime."""
    
    DomainMask = 3
    """Do not use. This mask selects the domain-related values, screening out
    the unused DisallowBindings flag."""
    
    MultiDomain = 2
    """Indicates that the application will probably have many domains that
    use the same code, and the loader must share maximal internal resources
    across application domains."""
    
    MultiDomainHost = 3
    """Indicates that the application will probably host unique code in
    multiple domains, and the loader must share resources across application
    domains only for globally available (strong-named) assemblies that have
    been added to the global assembly cache."""
    
    NotSpecified = 0
    """Indicates that no optimizations for sharing internal resources are
    specified. If the default domain or hosting interface specified an
    optimization, then the loader uses that; otherwise, the loader uses
    SingleDomain."""
    
    SingleDomain = 1
    """Indicates that the application will probably have a single domain,
    and loader must not share internal resources across application domains."""


class MidpointRounding(Enum):
    """Specifies the strategy that mathematical rounding methods should
    use to round a number."""
    
    AwayFromZero = 1
    """The strategy of rounding to the nearest number, and when a number is
    halfway between two others, it's rounded toward the nearest number that's
    away from zero."""
    
    ToEven = 0
    """The strategy of rounding to the nearest number, and when a number is
    halfway between two others, it's rounded toward the nearest even number."""
    
    ToNegativeInfinity = 3
    """The strategy of downwards-directed rounding, with the result closest
    to and no greater than the infinitely precise result."""
    
    ToPositiveInfinity = 4
    """The strategy of upwards-directed rounding, with the result closest to
    and no less than the infinitely precise result."""
    
    ToZero = 2
    """The strategy of directed rounding toward zero, with the result closest
    to and no greater in magnitude than the infinitely precise result."""


class PlatformID(Enum):
    """Identifies the operating system, or platform, supported by an assembly."""
    
    MacOSX = 6
    """The operating system is Macintosh. This value was returned by
    Silverlight. On .NET Core, its replacement is Unix."""
    
    Other = 7
    """Any other operating system. This includes Browser (WASM)."""
    
    Unix = 4
    """The operating system is Unix."""
    
    Win32NT = 2
    """The operating system is Windows NT or later."""
    
    Win32S = 0
    """The operating system is Win32s. This value is no longer in use."""
    
    Win32Windows = 1
    """The operating system is Windows 95 or Windows 98. This value is no longer in use."""
    
    WinCE = 3
    """The operating system is Windows CE. This value is no longer in use."""
    
    Xbox = 5
    """The development platform is Xbox 360. This value is no longer in use."""


class StringComparison(Enum):
    """Specifies the culture, case, and sort rules to be used by certain
    overloads of the Compare(String, String) and Equals(Object) methods."""
    
    CurrentCulture = 0
    """Compare strings using culture-sensitive sort rules and the current culture."""
    
    CurrentCultureIgnoreCase = 1
    """Compare strings using culture-sensitive sort rules, the current
    culture, and ignoring the case of the strings being compared."""
    
    InvariantCulture = 2
    """Compare strings using culture-sensitive sort rules and the invariant culture."""
    
    InvariantCultureIgnoreCase = 3
    """Compare strings using culture-sensitive sort rules, the invariant
    culture, and ignoring the case of the strings being compared."""
    
    Ordinal = 4
    """Compare strings using ordinal (binary) sort rules."""
    
    OrdinalIgnoreCase = 5
    """Compare strings using ordinal (binary) sort rules and ignoring the
    case of the strings being compared."""


class StringSplitOptions(Enum):
    """Specifies options for applicable Split method overloads, such as
    whether to omit empty substrings from the returned array or trim
    whitespace from substrings."""
    
    #None = 0
    """Use the default options when splitting strings."""
    
    RemoveEmptyEntries = 1
    """Omit array elements that contain an empty string from the result.
    
    If RemoveEmptyEntries and TrimEntries are specified together, then
    substrings that consist only of white-space characters are also removed
    from the result."""
    
    TrimEntries = 2
    """Trim white-space characters from each substring in the result. This
    field is available in .NET 5 and later versions only.
    
    If RemoveEmptyEntries and TrimEntries are specified together, then
    substrings that consist only of white-space characters are also removed
    from the result."""


class TypeCode(Enum):
    """Specifies the type of an object."""
    
    Boolean = 3
    """A simple type representing Boolean values of true or false."""
    
    Byte = 6
    """An integral type representing unsigned 8-bit integers with values
    between 0 and 255."""
    
    Char = 4
    """An integral type representing unsigned 16-bit integers with values
    between 0 and 65535. The set of possible values for the Char type
    corresponds to the Unicode character set."""
    
    DateTime = 16
    """A type representing a date and time value."""
    
    DBNull = 2
    """A database null (column) value."""
    
    Decimal = 15
    """A simple type representing values ranging from 1.0 x 10 -28 to
    approximately 7.9 x 10 28 with 28-29 significant digits."""
    
    Double = 14
    """A floating point type representing values ranging from approximately
    5.0 x 10 -324 to 1.7 x 10 308 with a precision of 15-16 digits."""
    
    Empty = 0
    """A null reference."""
    
    Int16 = 7
    """An integral type representing signed 16-bit integers with values
    between -32768 and 32767."""
    
    Int32 = 9
    """An integral type representing signed 32-bit integers with values
    between -2147483648 and 2147483647."""
    
    Int64 = 11
    """An integral type representing signed 64-bit integers with values
    between -9223372036854775808 and 9223372036854775807."""
    
    Object = 1
    """A general type representing any reference or value type not
    explicitly represented by another TypeCode."""
    
    SByte = 5
    """An integral type representing signed 8-bit integers with values
    between -128 and 127."""
    
    Single = 13
    """A floating point type representing values ranging from approximately
    1.5 x 10 -45 to 3.4 x 10 38 with a precision of 7 digits."""
    
    String = 18
    """A sealed class type representing Unicode character strings."""
    
    UInt16 = 8
    """An integral type representing unsigned 16-bit integers with values
    between 0 and 65535."""
    
    UInt32 = 10
    """An integral type representing unsigned 32-bit integers with values
    between 0 and 4294967295."""
    
    UInt64 = 12
    """An integral type representing unsigned 64-bit integers with values
    between 0 and 18446744073709551615."""


class UriComponents(Enum):
    """Specifies the parts of a Uri."""
    
    AbsoluteUri = 127
    """The Scheme, UserInfo, Host, Port, LocalPath, Query, and Fragment data."""
    
    Fragment = 64
    """The Fragment data."""
    
    Host = 4
    """The Host data."""
    
    HostAndPort = 132
    """The Host and Port data. If no port data is in the Uri and a default
    port has been assigned to the Scheme, the default port is returned. If
    there is no default port, -1 is returned."""
    
    HttpRequestUrl = 61
    """The Scheme, Host, Port, LocalPath, and Query data."""
    
    KeepDelimiter = 1073741824
    """Specifies that the delimiter should be included."""
    
    NormalizedHost = 256
    """The normalized form of the Host."""
    
    Path = 16
    """The LocalPath data."""
    
    PathAndQuery = 48
    """The LocalPath and Query data. Also see PathAndQuery."""
    
    Port = 8
    """The Port data."""
    
    Query = 32
    """The Query data."""
    
    Scheme = 1
    """The Scheme data."""
    
    SchemeAndServer = 13
    """The Scheme, Host, and Port data."""
    
    SerializationInfoString = -2147483648
    """The complete Uri context that is needed for Uri Serializers. The
    context includes the IPv6 scope.
    '"""
    
    StrongAuthority = 134
    """The UserInfo, Host, and Port data. If no port data is in the Uri and a
    default port has been assigned to the Scheme, the default port is
    returned. If there is no default port, -1 is returned."""
    
    StrongPort = 128
    """The Port data. If no port data is in the Uri and a default port has
    been assigned to the Scheme, the default port is returned. If there is no
    default port, -1 is returned."""
    
    UserInfo = 2
    """The UserInfo data."""


class UriFormat(Enum):
    """Controls how URI information is escaped."""
    
    SafeUnescaped = 3
    """Characters that have a reserved meaning in the requested URI
    components remain escaped. All others are not escaped."""
    
    Unescaped = 2
    """No escaping is performed."""
    
    UriEscaped = 1
    """Escaping is performed according to the rules in RFC 2396."""


class UriHostNameType(Enum):
    """Defines host name types for the CheckHostName(String) method."""
    
    Basic = 1
    """The host is set, but the type cannot be determined."""
    
    Dns = 2
    """The host name is a domain name system (DNS) style host name."""
    
    IPv4 = 3
    """The host name is an Internet Protocol (IP) version 4 host address."""
    
    IPv6 = 4
    """The host name is an Internet Protocol (IP) version 6 host address."""
    
    Unknown = 0
    """The type of the host name is not supplied."""


class UriKind(Enum):
    """Defines the different kinds of URIs."""
    
    Absolute = 1
    """The URI is absolute."""
    
    Relative = 2
    """The URI is relative."""
    
    RelativeOrAbsolute = 0
    """The URI kind is indeterminate."""


class UriPartial(Enum):
    """Defines the parts of a URI for the GetLeftPart(UriPartial) method."""
    
    Authority = 1
    """The scheme and authority segments of the URI."""
    
    Path = 2
    """The scheme, authority, and path segments of the URI."""
    
    Query = 3
    """The scheme, authority, path, and query segments of the URI."""
    
    Scheme = 0
    """The scheme segment of the URI."""


# ---------- DELEGATES ---------- #

Action = Callable[[], None]
"""Encapsulates a method that has no parameters and does not return a value."""

Action1 = Callable[[T1], None]
"""Encapsulates a method that has a single parameter and does not return a value."""

Action2 = Callable[[T1, T2], None]
"""Encapsulates a method that has two parameters and does not return a value."""

Action3 = Callable[[T1, T2, T3], None]
"""Encapsulates a method that has three parameters and does not return a value."""

Action4 = Callable[[T1, T2, T3, T4], None]
"""Encapsulates a method that has four parameters and does not return a value."""

Action5 = Callable[[T1, T2, T3, T4, T5], None]
"""Encapsulates a method that has five parameters and does not return a value."""

Action6 = Callable[[T1, T2, T3, T4, T5, T6], None]
"""Encapsulates a method that has six parameters and does not return a value."""

Action7 = Callable[[T1, T2, T3, T4, T5, T6, T7], None]
"""Encapsulates a method that has seven parameters and does not return a value."""

Action8 = Callable[[T1, T2, T3, T4, T5, T6, T7, T8], None]
"""Encapsulates a method that has eight parameters and does not return a value."""

Action9 = Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9], None]
"""Encapsulates a method that has nine parameters and does not return a value."""

Action10 = Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10], None]
"""Encapsulates a method that has 10 parameters and does not return a value."""

Action11 = Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11], None]
"""Encapsulates a method that has 11 parameters and does not return a value."""

Action12 = Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12], None]
"""Encapsulates a method that has 12 parameters and does not return a value."""

Action13 = Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13], None]
"""Encapsulates a method that has 13 parameters and does not return a value."""

Action14 = Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14], None]
"""Encapsulates a method that has 14 parameters and does not return a value."""

Action15 = Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15], None]
"""Encapsulates a method that has 15 parameters and does not return a value."""

Action16 = Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16], None]
"""Encapsulates a method that has 16 parameters and does not return a value."""

AssemblyLoadEventHandler = Callable[[NullableType[ObjectType], AssemblyLoadEventArgs], None]
"""Represents the method that handles the AssemblyLoad event of an AppDomain."""

AsyncCallback = Callable[[IAsyncResult], None]
"""References a method to be called when a corresponding asynchronous operation completes."""

Comparison = Callable[[T, T], IntType]
"""Represents the method that compares two objects of the same type."""

ConsoleCancelEventHandler = Callable[[NullableType[ObjectType], ConsoleCancelEventArgs], None]
"""Represents the method that will handle the CancelKeyPress event of a Console."""

Converter = Callable[[TInput], TOutput]
"""Represents a method that converts an object from one type to another type."""

EventHandler = Callable[[NullableType[ObjectType], Union[TEventArgs, EventArgs]], None]
"""Represents the method that will handle an event that has no event data.
Represents the method that will handle an event when the event provides data."""

@overload
class Func(Callable[[], TResult], Generic[TResult]):
    """Encapsulates a method that has no parameters and returns a value of the type specified by the TResult parameter."""

@overload
class Func(Callable[[T1], TResult], Generic[T1, TResult]):
    """Encapsulates a method that has one parameter and returns a value of the type specified by the TResult parameter."""

@overload
class Func(Callable[[T1, T2], TResult], Generic[T1, T2, TResult]):
    """Encapsulates a method that has two parameters and returns a value of the type specified by the TResult parameter."""

@overload
class Func(Callable[[T1, T2, T3], TResult], Generic[T1, T2, T3, TResult]):
    """Encapsulates a method that has three parameters and returns a value of the type specified by the TResult parameter."""

@overload
class Func(Callable[[T1, T2, T3, T4], TResult], Generic[T1, T2, T3, T4, TResult]):
    """Encapsulates a method that has four parameters and returns a value of the type specified by the TResult parameter."""

@overload
class Func(Callable[[T1, T2, T3, T4, T5], TResult], Generic[T1, T2, T3, T4, T5, TResult]):
    """Encapsulates a method that has five parameters and returns a value of the type specified by the TResult parameter."""

@overload
class Func(Callable[[T1, T2, T3, T4, T5, T6], TResult], Generic[T1, T2, T3, T4, T5, T6, TResult]):
    """Encapsulates a method that has six parameters and returns a value of the type specified by the TResult parameter."""

@overload
class Func(Callable[[T1, T2, T3, T4, T5, T6, T7], TResult], Generic[T1, T2, T3, T4, T5, T6, T7, TResult]):
    """Encapsulates a method that has seven parameters and returns a value of the type specified by the TResult parameter."""

@overload
class Func(Callable[[T1, T2, T3, T4, T5, T6, T7, T8], TResult], Generic[T1, T2, T3, T4, T5, T6, T7, T8, TResult]):
    """Encapsulates a method that has eight parameters and returns a value of the type specified by the TResult parameter."""

@overload
class Func(Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9], TResult], Generic[T1, T2, T3, T4, T5, T6, T7, T8, T9, TResult]):
    """Encapsulates a method that has nine parameters and returns a value of the type specified by the TResult parameter."""

@overload
class Func(Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10], TResult], Generic[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, TResult]):
    """Encapsulates a method that has 10 parameters and returns a value of the type specified by the TResult parameter."""

@overload
class Func(Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11], TResult], Generic[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, TResult]):
    """Encapsulates a method that has 11 parameters and returns a value of the type specified by the TResult parameter."""

@overload
class Func(Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12], TResult], Generic[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, TResult]):
    """Encapsulates a method that has 12 parameters and returns a value of the type specified by the TResult parameter."""

@overload
class Func(Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13], TResult], Generic[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, TResult]):
    """Encapsulates a method that has 13 parameters and returns a value of the type specified by the TResult parameter."""

@overload
class Func(Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14], TResult], Generic[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, TResult]):
    """Encapsulates a method that has 14 parameters and returns a value of the type specified by the TResult parameter."""

@overload
class Func(Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15], TResult], Generic[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, TResult]):
    """Encapsulates a method that has 15 parameters and returns a value of the type specified by the TResult parameter."""

@overload
class Func(Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16], TResult], Generic[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, TResult]):
    """Encapsulates a method that has 16 parameters and returns a value of the type specified by the TResult parameter."""

Predicate = Callable[[T], BooleanType]
"""Represents the method that defines a set of criteria and determines whether the specified object meets those criteria."""

ResolveEventHandler = Callable[[NullableType[ObjectType], ResolveEventArgs], NullableType[Assembly]]
"""Represents a method that handles the TypeResolve, ResourceResolve, or AssemblyResolve event of an AppDomain."""

UnhandledExceptionEventHandler = Callable[[ObjectType, UnhandledExceptionEventArgs], None]
"""Represents the method that will handle the event raised by an exception that is not handled by the application domain."""
