from __future__ import annotations

from abc import ABC
from typing import overload, Optional, TypeVar, NoReturn, Generic, Annotated, Final, Union

from .util import Item

T = TypeVar('T')
TKey = TypeVar('TKey')
TValue = TypeVar('TValue')
TMetadata = TypeVar('TMetadata')
TResult = TypeVar('TResult')
TEventArgs = TypeVar('TEventArgs')

BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
SByteType = Union[int, SByte]
CharType = Union[str, Char]
DecimalType = Union[float, Decimal]
DoubleType = Union[float, Double]
FloatType = Union[float, Single]
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


# class Enum(ValueType, IComparable, IConvertible, IFormattable, _Enum, ABC):
#     """Provides the base class for enumerations."""
#
#     def __init__(self):
#         """Initializes a new instance of the Enum class."""
#
#     # Methods
#     # METHODS
#     # CompareTo(Object)
#     # Compares this instance to a specified object and returns an indication of their relative values.
#     #
#     # Equals(Object)
#     # Returns a value indicating whether this instance is equal to a specified object.
#     #
#     # Format(Type, Object, String)
#     # Converts the specified value of a specified enumerated type to its equivalent string representation according to the specified format.
#     #
#     # GetHashCode()
#     # Returns the hash code for the value of this instance.
#     #
#     # GetName(Type, Object)
#     # Retrieves the name of the constant in the specified enumeration that has the specified value.
#     #
#     # GetName<TEnum>(TEnum)
#     # Retrieves the name of the constant in the specified enumeration type that has the specified value.
#     #
#     # GetNames(Type)
#     # Retrieves an array of the names of the constants in a specified enumeration.
#     #
#     # GetNames<TEnum>()
#     # Retrieves an array of the names of the constants in a specified enumeration type.
#     #
#     # GetType()
#     # Gets the Type of the current instance.
#     #
#     # (Inherited from Object)
#     # GetTypeCode()
#     # Returns the type code of the underlying type of this enumeration member.
#     #
#     # GetUnderlyingType(Type)
#     # Returns the underlying type of the specified enumeration.
#     #
#     # GetValues(Type)
#     # Retrieves an array of the values of the constants in a specified enumeration.
#     #
#     # GetValues<TEnum>()
#     # Retrieves an array of the values of the constants in a specified enumeration type.
#     #
#     # HasFlag(Enum)
#     # Determines whether one or more bit fields are set in the current instance.
#     #
#     # IsDefined(Type, Object)
#     # Returns a Boolean telling whether a given integral value, or its name as a string, exists in a specified enumeration.
#     #
#     # IsDefined<TEnum>(TEnum)
#     # Returns a boolean telling whether a given integral value, or its name as a string, exists in a specified enumeration.
#     #
#     # MemberwiseClone()
#     # Creates a shallow copy of the current Object.
#     #
#     # (Inherited from Object)
#     # Parse(Type, ReadOnlySpan<Char>)
#     # Converts the span of characters representation of the name or numeric value of one or more enumerated constants to an equivalent enumerated object.
#     #
#     # Parse(Type, ReadOnlySpan<Char>, Boolean)
#     # Converts the span of characters representation of the name or numeric value of one or more enumerated constants to an equivalent enumerated object. A parameter specifies whether the operation is case-insensitive.
#     #
#     # Parse(Type, String)
#     # Converts the string representation of the name or numeric value of one or more enumerated constants to an equivalent enumerated object.
#     #
#     # Parse(Type, String, Boolean)
#     # Converts the string representation of the name or numeric value of one or more enumerated constants to an equivalent enumerated object. A parameter specifies whether the operation is case-insensitive.
#     #
#     # Parse<TEnum>(ReadOnlySpan<Char>)
#     # Converts the span of characters representation of the name or numeric value of one or more enumerated constants specified by TEnum to an equivalent enumerated object.
#     #
#     # Parse<TEnum>(ReadOnlySpan<Char>, Boolean)
#     # Converts the span of characters representation of the name or numeric value of one or more enumerated constants specified by TEnum to an equivalent enumerated object. A parameter specifies whether the operation is case-insensitive.
#     #
#     # Parse<TEnum>(String)
#     # Converts the string representation of the name or numeric value of one or more enumerated constants specified by TEnum to an equivalent enumerated object.
#     #
#     # Parse<TEnum>(String, Boolean)
#     # Converts the string representation of the name or numeric value of one or more enumerated constants specified by TEnum to an equivalent enumerated object. A parameter specifies whether the operation is case-insensitive.
#     #
#     # ToObject(Type, Byte)
#     # Converts the specified 8-bit unsigned integer to an enumeration member.
#     #
#     # ToObject(Type, Int16)
#     # Converts the specified 16-bit signed integer to an enumeration member.
#     #
#     # ToObject(Type, Int32)
#     # Converts the specified 32-bit signed integer to an enumeration member.
#     #
#     # ToObject(Type, Int64)
#     # Converts the specified 64-bit signed integer to an enumeration member.
#     #
#     # ToObject(Type, Object)
#     # Converts the specified object with an integer value to an enumeration member.
#     #
#     # ToObject(Type, SByte)
#     # Converts the specified 8-bit signed integer value to an enumeration member.
#     #
#     # ToObject(Type, UInt16)
#     # Converts the specified 16-bit unsigned integer value to an enumeration member.
#     #
#     # ToObject(Type, UInt32)
#     # Converts the specified 32-bit unsigned integer value to an enumeration member.
#     #
#     # ToObject(Type, UInt64)
#     # Converts the specified 64-bit unsigned integer value to an enumeration member.
#     #
#     # ToString()
#     # Converts the value of this instance to its equivalent string representation.
#     #
#     # ToString(IFormatProvider)
#     # Obsolete.
#     # This method overload is obsolete; use ToString().
#     #
#     # ToString(String)
#     # Converts the value of this instance to its equivalent string representation using the specified format.
#     #
#     # ToString(String, IFormatProvider)
#     # Obsolete.
#     # This method overload is obsolete; use ToString(String).
#     #
#     # TryParse(Type, ReadOnlySpan<Char>, Boolean, Object)
#     # Converts the span of characters representation of the name or numeric value of one or more enumerated constants to an equivalent enumerated object. A parameter specifies whether the operation is case-insensitive.
#     #
#     # TryParse(Type, ReadOnlySpan<Char>, Object)
#     # Converts the span of characters representation of the name or numeric value of one or more enumerated constants to an equivalent enumerated object.
#     #
#     # TryParse(Type, String, Boolean, Object)
#     # Converts the string representation of the name or numeric value of one or more enumerated constants to an equivalent enumerated object.
#     #
#     # TryParse(Type, String, Object)
#     # Converts the string representation of the name or numeric value of one or more enumerated constants to an equivalent enumerated object.
#     #
#     # TryParse<TEnum>(ReadOnlySpan<Char>, Boolean, TEnum)
#     # Converts the string representation of the name or numeric value of one or more enumerated constants to an equivalent enumerated object. A parameter specifies whether the operation is case-sensitive. The return value indicates whether the conversion succeeded.
#     #
#     # TryParse<TEnum>(ReadOnlySpan<Char>, TEnum)
#     # Converts the string representation of the name or numeric value of one or more enumerated constants to an equivalent enumerated object.
#     #
#     # TryParse<TEnum>(String, Boolean, TEnum)
#     # Converts the string representation of the name or numeric value of one or more enumerated constants to an equivalent enumerated object. A parameter specifies whether the operation is case-sensitive. The return value indicates whether the conversion succeeded.
#     #
#     # TryParse<TEnum>(String, TEnum)
#     # Converts the string representation of the name or numeric value of one or more enumerated constants to an equivalent enumerated object. The return value indicates whether the conversion succeeded.
#     #
#     # Explicit Interface Implementations
#     # EXPLICIT INTERFACE IMPLEMENTATIONS
#     # IConvertible.ToBoolean(IFormatProvider)
#     # Converts the current value to a Boolean value based on the underlying type.
#     #
#     # IConvertible.ToByte(IFormatProvider)
#     # Converts the current value to an 8-bit unsigned integer based on the underlying type.
#     #
#     # IConvertible.ToChar(IFormatProvider)
#     # Converts the current value to a Unicode character based on the underlying type.
#     #
#     # IConvertible.ToDateTime(IFormatProvider)
#     # Converts the current value to a DateTime based on the underlying type.
#     #
#     # IConvertible.ToDecimal(IFormatProvider)
#     # Converts the current value to a Decimal based on the underlying type.
#     #
#     # IConvertible.ToDouble(IFormatProvider)
#     # Converts the current value to a double-precision floating point number based on the underlying type.
#     #
#     # IConvertible.ToInt16(IFormatProvider)
#     # Converts the current value to a 16-bit signed integer based on the underlying type.
#     #
#     # IConvertible.ToInt32(IFormatProvider)
#     # Converts the current value to a 32-bit signed integer based on the underlying type.
#     #
#     # IConvertible.ToInt64(IFormatProvider)
#     # Converts the current value to a 64-bit signed integer based on the underlying type.
#     #
#     # IConvertible.ToSByte(IFormatProvider)
#     # Converts the current value to an 8-bit signed integer based on the underlying type.
#     #
#     # IConvertible.ToSingle(IFormatProvider)
#     # Converts the current value to a single-precision floating-point number based on the underlying type.
#     #
#     # IConvertible.ToType(Type, IFormatProvider)
#     # Converts the current value to a specified type based on the underlying type.
#     #
#     # IConvertible.ToUInt16(IFormatProvider)
#     # Converts the current value to a 16-bit unsigned integer based on the underlying type.
#     #
#     # IConvertible.ToUInt32(IFormatProvider)
#     # Converts the current value to a 32-bit unsigned integer based on the underlying type.
#     #
#     # IConvertible.ToUInt64(IFormatProvider)
#     # Converts the current value to a 64-bit unsigned integer based on the underlying type.
#
#
# class TypeCode(Enum):
#     Boolean: Annotated[Int32, 'A simple type representing Boolean values of true or false.'] = 3
#
#     Byte: Annotated[Int32, 'An integral type representing unsigned 8-bit integers with values between 0 and 255.'] = 6
#
#     Char: Annotated[Int32, 'An integral type representing unsigned 16-bit integers with values between 0 and 65535. The set of possible values for the Char type corresponds to the Unicode character set.'] = 4
#
#     DateTime: Annotated[Int32, 'A type representing a date and time value.'] = 16
#
#     DBNull: Annotated[Int32, 'A database null (column) value.'] = 2
#
#     Decimal: Annotated[Int32, 'A simple type representing values ranging from 1.0 x 10 -28 to approximately 7.9 x 10 28 with 28-29 significant digits.'] = 15
#
#     Double: Annotated[Int32, 'A floating point type representing values ranging from approximately 5.0 x 10 -324 to 1.7 x 10 308 with a precision of 15-16 digits.'] = 14
#
#     Empty: Annotated[Int32, 'A null reference.'] = 0
#
#     Int16: Annotated[Int32, 'An integral type representing signed 16-bit integers with values between -32768 and 32767.'] = 7
#
#     Int32: Annotated[Int32, 'An integral type representing signed 32-bit integers with values between -2147483648 and 2147483647.'] = 9
#
#     Int64: Annotated[Int32, 'An integral type representing signed 64-bit integers with values between -9223372036854775808 and 9223372036854775807.'] = 11
#
#     Object: Annotated[Int32, 'A general type representing any reference or value type not explicitly represented by another TypeCode.'] = 1
#
#     SByte: Annotated[Int32, 'An integral type representing signed 8-bit integers with values between -128 and 127.'] = 5
#
#     Single: Annotated[Int32, 'A floating point type representing values ranging from approximately 1.5 x 10 -45 to 3.4 x 10 38 with a precision of 7 digits.'] = 13
#
#     String: Annotated[Int32, 'A sealed class type representing Unicode character strings.'] = 18
#
#     UInt16: Annotated[Int32, 'An integral type representing unsigned 16-bit integers with values between 0 and 65535.'] = 8
#
#     UInt32: Annotated[Int32, 'An integral type representing unsigned 32-bit integers with values between 0 and 4294967295.'] = 10
#
#     UInt64: Annotated[Int32, 'An integral type representing unsigned 64-bit integers with values between 0 and 18446744073709551615.'] = 12


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
    def __init__(self, message: Optional[StringType]):
        """Initializes a new instance of the AccessViolationException class with a specified message that describes the error."""
    
    @overload
    def __init__(self, message: Optional[StringType], innerException: Optional[Exception]):
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


class Array:
    """Provides methods for creating, manipulating, searching, and sorting arrays, thereby serving as the base class for all arrays in the common language runtime."""


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


class Enum:
    """Provides the base class for enumerations."""


class Environment:
    """Provides information about, and means to manipulate, the current environment and platform. This class cannot be inherited."""


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
    def __init__(self, message: Optional[StringType]):
        """Initializes a new instance of the Exception class with a specified error message."""
    
    @overload
    def __init__(self, message: Optional[StringType], innerException: Optional[Exception]):
        """Initializes a new instance of the Exception class with a specified
        error message and a reference to the inner exception that is the cause
        of this exception.
        """
    
    @property
    def Data(self) -> IDictionary:
        """Gets a collection of key/value pairs that provide additional user-defined information about the exception."""
    
    @property
    def HelpLink(self) -> Optional[String]:
        """Gets a link to the help file associated with this exception."""
    
    @HelpLink.setter
    def HelpLink(self, value: String) -> None:
        """Sets a link to the help file associated with this exception."""
    
    @property
    def HResult(self) -> Int32:
        """Gets HRESULT, a coded numerical value that is assigned to a specific exception."""
    
    @HResult.setter
    def HResult(self, value: Int32) -> None:
        """Sets HRESULT, a coded numerical value that is assigned to a specific exception."""
    
    @property
    def InnerException(self) -> Optional[Exception]:
        """Gets the Exception instance that caused the current exception."""
    
    @property
    def Message(self) -> String:
        """Gets a message that describes the current exception."""
    
    @property
    def Source(self) -> Optional[String]:
        """Gets or sets the name of the application or the object that causes the error."""
    
    @Source.setter
    def Source(self, value: String) -> Optional[String]:
        """Gets or sets the name of the application or the object that causes the error."""
    
    @property
    def StackTrace(self) -> Optional[String]:
        """Gets a string representation of the immediate frames on the call stack."""
    
    @property
    def TargetSite(self) -> Optional[MethodBase]:
        """Gets the method that throws the current exception."""
    
    def GetBaseException(self) -> Exception:
        """When overridden in a derived class, returns the Exception that is the root cause of one or more subsequent exceptions."""
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """When overridden in a derived class, sets the SerializationInfo with information about the exception."""
    
    @property
    def SerializeObjectState(self) -> NoReturn:
        """Obsolete. Occurs when an exception is serialized to create an exception state object that contains serialized data about the exception."""


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


class Nullable:
    """Supports a value type that can be assigned null. This class cannot be inherited."""


class NullReferenceException:
    """The exception that is thrown when there is an attempt to dereference a null object reference."""


class Object:
    """Supports all classes in the .NET class hierarchy and provides low-level
    services to derived classes. This is the ultimate base class of all .NET
    classes; it is the root of the type hierarchy.
    """
    
    def __init__(self):
        """Initializes a new instance of the Object class."""
    
    def Equals(self, obj: Object) -> Boolean:
        """Determines whether the specified object is equal to the current object."""
    
    def Finalize(self) -> None:
        """Allows an object to try to free resources and perform other cleanup
        operations before it is reclaimed by garbage collection.
        """
    
    def GetHashCode(self) -> Int32:
        """Serves as the default hash function."""
    
    def GetType(self) -> Type:
        """Gets the Type of the current instance."""
    
    def MemberwiseClone(self) -> Object:
        """Creates a shallow copy of the current Object."""
    
    @overload
    def ToString(self) -> String:
        """Returns a string that represents the current object."""
    
    def ToString(self, *args, **kwargs) -> String: ...
    
    @staticmethod
    def ReferenceEquals(obj1: ObjectType, obj2: ObjectType) -> Boolean:
        """Determines whether the specified Object instances are the same instance."""
    
    @staticmethod
    @overload
    def Equals(obj1: ObjectType, obj2: ObjectType) -> Boolean:
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
    def __init__(self, message: Optional[StringType]):
        """Initializes a new instance of the SystemException class with a specified error message."""
    
    @overload
    def __init__(self, message: Optional[StringType], innerException: Optional[Exception]):
        """Initializes a new instance of the SystemException class with a specified
        error message and a reference to the inner exception that is the cause
        of this exception.
        """


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


class TimeZoneNotFoundException:
    """The exception that is thrown when a time zone cannot be found."""


class Tuple:
    """Provides static methods for creating tuple objects."""


class Tuple< T1 >:
    """Represents a 1-tuple, or singleton."""


class Tuple< T1, T2 >:
    """Represents a 2-tuple, or pair."""


class Tuple< T1, T2, T3 >:
    """Represents a 3-tuple, or triple."""


class Tuple< T1, T2, T3, T4 >:
    """Represents a 4-tuple, or quadruple."""


class Tuple< T1, T2, T3, T4, T5 >:
    """Represents a 5-tuple, or quintuple."""


class Tuple< T1, T2, T3, T4, T5, T6 >:
    """Represents a 6-tuple, or sextuple."""


class Tuple< T1, T2, T3, T4, T5, T6, T7 >:
    """Represents a 7-tuple, or septuple."""


class Tuple< T1, T2, T3, T4, T5, T6, T7, TRest >:
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
    of a function that takes a variable number of arguments.
    """
    
    @overload
    def __init__(self, arglist: RuntimeArgumentHandle):
        """Initializes a new instance of the ArgIterator structure using the
        specified argument list.
        """
    
    @overload
    def __init__(self, arglist: RuntimeArgumentHandle, ptr: Void):
        """Initializes a new instance of the ArgIterator structure using the
        specified argument list and a pointer to an item in the list.
        """
    
    def End(self) -> None:
        """Concludes processing of the variable-length argument list
        represented by this instance.
        """
    
    @overload
    def GetNextArg(self) -> TypedReference:
        """Returns the next argument in a variable-length argument list."""
    
    @overload
    def GetNextArg(self, rth: RuntimeTypeHandle) -> TypedReference:
        """Returns the next argument in a variable-length argument list that
        has a specified type.
        """
    
    def GetNextArgType(self) -> RuntimeTypeHandle:
        """Returns the type of the next argument."""
    
    def GetRemainingCount(self) -> Int32:
        """Returns the number of arguments remaining in the argument list."""


class ArraySegment(ValueType, ICollection[T], IEnumerable[T], IList[T], IReadOnlyCollection[T], IReadOnlyList[T], IEnumerable):
    """Delimits a section of a one-dimensional array."""
    
    @overload
    def __init__(self, array: Array[T]):
        """Initializes a new instance of the ArraySegment[T] structure that
        delimits all the elements in the specified array.
        """
    
    @overload
    def __init__(self, array: Array[T], offset: IntType, count: IntType):
        """Initializes a new instance of the ArraySegment[T] structure that
        delimits the specified range of the elements in the specified array.
        """
    
    @property
    def Array(self) -> Optional[Array[T]]:
        """Gets the original array containing the range of elements that the
        array segment delimits.
        """
    
    @property
    def Count(self) -> Int32:
        """Gets the number of elements in the range delimited by the array segment."""
    
    @staticmethod
    @property
    def Empty() -> Array[T]:
        """Represents the empty array segment. This field is read-only."""
    
    @property
    def Item(self) -> Item[T]:
        """Gets or sets the element at the specified index."""
    
    @property
    def Offset(self) -> Int32:
        """Gets the position of the first element in the range delimited by
        the array segment, relative to the start of the original array.
        """
    
    def CopyTo(self, destination: ArraySegment[T]) -> None:
        """Copies the contents of this instance into the specified
        destination array segment of the same type T.
        """
    
    @overload
    def CopyTo(self, destination: Array[T]) -> None:
        """Copies the contents of this instance into the specified destination
        array of the same type T.
        """
    
    @overload
    def CopyTo(self, destination: Array[T], destinationIndex: IntType) -> None:
        """Copies the contents of this instance into the specified destination
        array of the same type T, starting at the specified destination index.
        """
    
    def GetEnumerator(self) -> ArraySegment[T].Enumerator:
        """Returns an enumerator that can be used to iterate through the array segment."""
    
    def __iter__(self):
        return self.GetEnumerator()
    
    @overload
    def Slice(self, index: Int32) -> ArraySegment[T]:
        """Forms a slice out of the current array segment starting at the specified index."""
    
    @overload
    def Slice(self, index: Int32, count: Int32) -> ArraySegment[T]:
        """Forms a slice of the specified length out of the current array
        segment starting at the specified index.
        """
    
    def ToArray(self) -> Array[T]:
        """Copies the contents of this array segment into a new array."""
    
    @overload
    def __getitem__(self, key) -> Union[T, ArraySegment[T]]:
        """Gets the element at the specified index."""
    
    @overload
    def __setitem__(self, key, value: Union[T, ArraySegment[T]]) -> None:
        """Sets the element at the specified index."""
    
    @staticmethod
    def Equality(left: ArraySegment[T], right: ArraySegment[T]) -> Boolean:
        """Indicates whether two ArraySegment[T] structures are equal."""
    
    @staticmethod
    def Implicit(array: Array[T]) -> ArraySegment[T]:
        """Defines an implicit conversion of an array of type T to an array segment of type T."""
    
    @staticmethod
    def Inequality(left: ArraySegment[T], right: ArraySegment[T]) -> Boolean:
        """Indicates whether two ArraySegment[T] structures are unequal."""
    
    __eq__ = Equality
    __ne__ = Inequality
    
    def ToImmutableArray(self) -> ImmutableArray[T]:
        """Creates an immutable array from the specified collection."""
    
    @overload
    def ToImmutableDictionary(self, keySelector: Func[T, TKey]) -> ImmutableDictionary[T, TKey]:
        """Constructs an immutable dictionary from an existing collection of elements, applying a transformation function to the source keys."""
    
    @overload
    def ToImmutableDictionary(self, keySelector: Func[T, TKey], keyComparer: Optional[IEqualityComparer[TKey]]) -> ImmutableDictionary[T, TKey]:
        """Constructs an immutable dictionary based on some transformation of a sequence."""
    
    @overload
    def ToImmutableDictionary(self, keySelector: Func[T, TKey], elementSelector: Func[T, TValue]) -> ImmutableDictionary[TKey, TValue]:
        """Enumerates and transforms a sequence, and produces an immutable dictionary of its contents."""
    
    @overload
    def ToImmutableDictionary(self, keySelector: Func[T, TKey], elementSelector: Func[T, TValue], keyComparer: Optional[IEqualityComparer[TKey]]) -> ImmutableDictionary[TKey, TValue]:
        """Enumerates and transforms a sequence, and produces an immutable dictionary of its contents by using the specified key comparer."""
    
    @overload
    def ToImmutableDictionary(self, keySelector: Func[T, TKey], elementSelector: Func[T, TValue], keyComparer: Optional[IEqualityComparer[TKey]], valueComparer: Optional[IEqualityComparer[TValue]]) -> ImmutableDictionary[TKey, TValue]:
        """Enumerates and transforms a sequence, and produces an immutable dictionary of its contents by using the specified key and value comparers."""
    
    @overload
    def ToImmutableHashSet(self) -> ImmutableHashSet[T]:
        """Enumerates a sequence and produces an immutable hash set of its contents."""
    
    @overload
    def ToImmutableHashSet(self, equalityComparer: Optional[IEqualityComparer[T]]) -> ImmutableHashSet[T]:
        """Enumerates a sequence, produces an immutable hash set of its contents, and uses the specified equality comparer for the set type."""
    
    def ToImmutableList(self) -> ImmutableList[T]:
        """Enumerates a sequence and produces an immutable list of its contents."""
    
    @overload
    def ToImmutableSortedDictionary(self, keySelector: Func[T, TKey], elementSelector: Func[T, TValue]) -> ImmutableSortedDictionary[TKey, TValue]:
        """Enumerates and transforms a sequence, and produces an immutable sorted dictionary of its contents."""
    
    @overload
    def ToImmutableSortedDictionary(self, keySelector: Func[T, TKey], elementSelector: Func[T, TValue], keyComparer: Optional[IComparer[TKey]]) -> ImmutableSortedDictionary[TKey, TValue]:
        """Enumerates and transforms a sequence, and produces an immutable sorted dictionary of its contents by using the specified key comparer."""
    
    @overload
    def ToImmutableSortedDictionary(self, keySelector: Func[T, TKey], elementSelector: Func[T, TValue], keyComparer: Optional[IComparer[TKey]], valueComparer: Optional[IEqualityComparer[TValue]]) -> ImmutableSortedDictionary[TKey, TValue]:
        """Enumerates and transforms a sequence, and produces an immutable sorted dictionary of its contents by using the specified key and value comparers."""
    
    ToImmutableSortedSet < TSource > (IEnumerable < TSource >)
    Enumerates
    a
    sequence and produces
    an
    immutable
    sorted
    set
    of
    its
    contents.
    
    ToImmutableSortedSet < TSource > (IEnumerable < TSource >, IComparer < TSource >)
    Enumerates
    a
    sequence, produces
    an
    immutable
    sorted
    set
    of
    its
    contents, and uses
    the
    specified
    comparer.
    
    CopyToDataTable[T](IEnumerable[T])
    Returns
    a
    DataTable
    that
    contains
    copies
    of
    the
    DataRow
    objects, given
    an
    input
    IEnumerable[T]
    object
    where
    the
    generic
    parameter
    T is DataRow.
    
    CopyToDataTable[T](IEnumerable[T], DataTable, LoadOption)
    Copies
    DataRow
    objects
    to
    the
    specified
    DataTable, given
    an
    input
    IEnumerable[T]
    object
    where
    the
    generic
    parameter
    T is DataRow.
    
    CopyToDataTable[T](IEnumerable[T], DataTable, LoadOption, FillErrorEventHandler)
    Copies
    DataRow
    objects
    to
    the
    specified
    DataTable, given
    an
    input
    IEnumerable[T]
    object
    where
    the
    generic
    parameter
    T is DataRow.
    
    Aggregate < TSource > (IEnumerable < TSource >, Func < TSource, TSource, TSource >)
    Applies
    an
    accumulator
    function
    over
    a
    sequence.
    
    Aggregate < TSource, TAccumulate > (IEnumerable < TSource >, TAccumulate, Func < TAccumulate, TSource, TAccumulate >)
    Applies
    an
    accumulator
    function
    over
    a
    sequence.The
    specified
    seed
    value is used as the
    initial
    accumulator
    value.
    
    Aggregate < TSource, TAccumulate, TResult > (IEnumerable < TSource >, TAccumulate, Func < TAccumulate, TSource, TAccumulate >, Func < TAccumulate, TResult >)
    Applies
    an
    accumulator
    function
    over
    a
    sequence.The
    specified
    seed
    value is used as the
    initial
    accumulator
    value, and the
    specified
    function is used
    to
    select
    the
    result
    value.
    
    All < TSource > (IEnumerable < TSource >, Func < TSource, Boolean >)
    Determines
    whether
    all
    elements
    of
    a
    sequence
    satisfy
    a
    condition.
    
    Any < TSource > (IEnumerable < TSource >)
    Determines
    whether
    a
    sequence
    contains
    any
    elements.
    
    Any < TSource > (IEnumerable < TSource >, Func < TSource, Boolean >)
    Determines
    whether
    any
    element
    of
    a
    sequence
    satisfies
    a
    condition.
    
    Append < TSource > (IEnumerable < TSource >, TSource)
    Appends
    a
    value
    to
    the
    end
    of
    the
    sequence.
    
    AsEnumerable < TSource > (IEnumerable < TSource >)
    Returns
    the
    input
    typed as IEnumerable[T].
    
    Average < TSource > (IEnumerable < TSource >, Func < TSource, Decimal >)
    Computes
    the
    average
    of
    a
    sequence
    of
    Decimal
    values
    that
    are
    obtained
    by
    invoking
    a
    transform
    function
    on
    each
    element
    of
    the
    input
    sequence.
    
    Average < TSource > (IEnumerable < TSource >, Func < TSource, Double >)
    Computes
    the
    average
    of
    a
    sequence
    of
    Double
    values
    that
    are
    obtained
    by
    invoking
    a
    transform
    function
    on
    each
    element
    of
    the
    input
    sequence.
    
    Average < TSource > (IEnumerable < TSource >, Func < TSource, Int32 >)
    Computes
    the
    average
    of
    a
    sequence
    of
    Int32
    values
    that
    are
    obtained
    by
    invoking
    a
    transform
    function
    on
    each
    element
    of
    the
    input
    sequence.
    
    Average < TSource > (IEnumerable < TSource >, Func < TSource, Int64 >)
    Computes
    the
    average
    of
    a
    sequence
    of
    Int64
    values
    that
    are
    obtained
    by
    invoking
    a
    transform
    function
    on
    each
    element
    of
    the
    input
    sequence.
    
    Average < TSource > (IEnumerable < TSource >, Func < TSource, Nullable < Decimal >>)
    Computes
    the
    average
    of
    a
    sequence
    of
    nullable
    Decimal
    values
    that
    are
    obtained
    by
    invoking
    a
    transform
    function
    on
    each
    element
    of
    the
    input
    sequence.
    
    Average < TSource > (IEnumerable < TSource >, Func < TSource, Nullable < Double >>)
    Computes
    the
    average
    of
    a
    sequence
    of
    nullable
    Double
    values
    that
    are
    obtained
    by
    invoking
    a
    transform
    function
    on
    each
    element
    of
    the
    input
    sequence.
    
    Average < TSource > (IEnumerable < TSource >, Func < TSource, Nullable < Int32 >>)
    Computes
    the
    average
    of
    a
    sequence
    of
    nullable
    Int32
    values
    that
    are
    obtained
    by
    invoking
    a
    transform
    function
    on
    each
    element
    of
    the
    input
    sequence.
    
    Average < TSource > (IEnumerable < TSource >, Func < TSource, Nullable < Int64 >>)
    Computes
    the
    average
    of
    a
    sequence
    of
    nullable
    Int64
    values
    that
    are
    obtained
    by
    invoking
    a
    transform
    function
    on
    each
    element
    of
    the
    input
    sequence.
    
    Average < TSource > (IEnumerable < TSource >, Func < TSource, Nullable < Single >>)
    Computes
    the
    average
    of
    a
    sequence
    of
    nullable
    Single
    values
    that
    are
    obtained
    by
    invoking
    a
    transform
    function
    on
    each
    element
    of
    the
    input
    sequence.
    
    Average < TSource > (IEnumerable < TSource >, Func < TSource, Single >)
    Computes
    the
    average
    of
    a
    sequence
    of
    Single
    values
    that
    are
    obtained
    by
    invoking
    a
    transform
    function
    on
    each
    element
    of
    the
    input
    sequence.
    
    Cast < TResult > (IEnumerable)
    Casts
    the
    elements
    of
    an
    IEnumerable
    to
    the
    specified
    type.
    
    Chunk < TSource > (IEnumerable < TSource >, Int32)
    Splits
    the
    elements
    of
    a
    sequence
    into
    chunks
    of
    size
    at
    most
    size.
    
    Concat < TSource > (IEnumerable < TSource >, IEnumerable < TSource >)
    Concatenates
    two
    sequences.
    
    Contains < TSource > (IEnumerable < TSource >, TSource)
    Determines
    whether
    a
    sequence
    contains
    a
    specified
    element
    by
    using
    the
    default
    equality
    comparer.
    
    Contains < TSource > (IEnumerable < TSource >, TSource, IEqualityComparer < TSource >)
    Determines
    whether
    a
    sequence
    contains
    a
    specified
    element
    by
    using
    a
    specified
    IEqualityComparer[T].
    
    Count < TSource > (IEnumerable < TSource >)
    Returns
    the
    number
    of
    elements in a
    sequence.
    
    Count < TSource > (IEnumerable < TSource >, Func < TSource, Boolean >)
    Returns
    a
    number
    that
    represents
    how
    many
    elements in the
    specified
    sequence
    satisfy
    a
    condition.
    
    DefaultIfEmpty < TSource > (IEnumerable < TSource >)
    Returns
    the
    elements
    of
    the
    specified
    sequence or the
    type
    parameter
    's default value in a singleton collection if the sequence is empty.
    
    DefaultIfEmpty < TSource > (IEnumerable < TSource >, TSource)
    Returns
    the
    elements
    of
    the
    specified
    sequence or the
    specified
    value in a
    singleton
    collection if the
    sequence is empty.
    
    Distinct < TSource > (IEnumerable < TSource >)
    Returns
    distinct
    elements
    by
    using
    the
    default
    equality
    comparer
    to
    compare
    values.
    
    Distinct < TSource > (IEnumerable < TSource >, IEqualityComparer < TSource >)
    Returns
    distinct
    elements
    by
    using
    a
    specified
    IEqualityComparer[T]
    to
    compare
    values.
    
    DistinctBy < TSource, TKey > (IEnumerable < TSource >, Func < TSource, TKey >)
    Returns
    distinct
    elements
    according
    to
    a
    specified
    key
    selector
    function.
    
    DistinctBy < TSource, TKey > (IEnumerable < TSource >, Func < TSource, TKey >, IEqualityComparer < TKey >)
    Returns
    distinct
    elements
    according
    to
    a
    specified
    key
    selector
    function and using
    a
    specified
    comparer
    to
    compare
    keys.
    
    ElementAt < TSource > (IEnumerable < TSource >, Index)
    Returns
    the
    element
    at
    a
    specified
    index in a
    sequence.
    
    ElementAt < TSource > (IEnumerable < TSource >, Int32)
    Returns
    the
    element
    at
    a
    specified
    index in a
    sequence.
    
    ElementAtOrDefault < TSource > (IEnumerable < TSource >, Index)
    Returns
    the
    element
    at
    a
    specified
    index in a
    sequence or a
    default
    value if the
    index is out
    of
    range.
    
    ElementAtOrDefault < TSource > (IEnumerable < TSource >, Int32)
    Returns
    the
    element
    at
    a
    specified
    index in a
    sequence or a
    default
    value if the
    index is out
    of
    range.
    
    Except < TSource > (IEnumerable < TSource >, IEnumerable < TSource >)
    Produces
    the
    set
    difference
    of
    two
    sequences
    by
    using
    the
    default
    equality
    comparer
    to
    compare
    values.
    
    Except < TSource > (IEnumerable < TSource >, IEnumerable < TSource >, IEqualityComparer < TSource >)
    Produces
    the
    set
    difference
    of
    two
    sequences
    by
    using
    the
    specified
    IEqualityComparer[T]
    to
    compare
    values.
    
    ExceptBy < TSource, TKey > (IEnumerable < TSource >, IEnumerable < TKey >, Func < TSource, TKey >)
    Produces
    the
    set
    difference
    of
    two
    sequences
    according
    to
    a
    specified
    key
    selector
    function.
    
    ExceptBy < TSource, TKey > (IEnumerable < TSource >, IEnumerable < TKey >, Func < TSource, TKey >, IEqualityComparer < TKey >)
    Produces
    the
    set
    difference
    of
    two
    sequences
    according
    to
    a
    specified
    key
    selector
    function.
    
    First < TSource > (IEnumerable < TSource >)
    Returns
    the
    first
    element
    of
    a
    sequence.
    
    First < TSource > (IEnumerable < TSource >, Func < TSource, Boolean >)
    Returns
    the
    first
    element in a
    sequence
    that
    satisfies
    a
    specified
    condition.
    
    FirstOrDefault < TSource > (IEnumerable < TSource >)
    Returns
    the
    first
    element
    of
    a
    sequence, or a
    default
    value if the
    sequence
    contains
    no
    elements.
    
    FirstOrDefault < TSource > (IEnumerable < TSource >, TSource)
    Returns
    the
    first
    element
    of
    a
    sequence, or a
    specified
    default
    value if the
    sequence
    contains
    no
    elements.
    
    FirstOrDefault < TSource > (IEnumerable < TSource >, Func < TSource, Boolean >)
    Returns
    the
    first
    element
    of
    the
    sequence
    that
    satisfies
    a
    condition or a
    default
    value if no
    such
    element is found.
    
    FirstOrDefault < TSource > (IEnumerable < TSource >, Func < TSource, Boolean >, TSource)
    Returns
    the
    first
    element
    of
    the
    sequence
    that
    satisfies
    a
    condition, or a
    specified
    default
    value if no
    such
    element is found.
    
    GroupBy < TSource, TKey > (IEnumerable < TSource >, Func < TSource, TKey >)
    Groups
    the
    elements
    of
    a
    sequence
    according
    to
    a
    specified
    key
    selector
    function.
    
    GroupBy < TSource, TKey > (IEnumerable < TSource >, Func < TSource, TKey >, IEqualityComparer < TKey >)
    Groups
    the
    elements
    of
    a
    sequence
    according
    to
    a
    specified
    key
    selector
    function and compares
    the
    keys
    by
    using
    a
    specified
    comparer.
    
    GroupBy < TSource, TKey, TElement > (IEnumerable < TSource >, Func < TSource, TKey >, Func < TSource, TElement >)
    Groups
    the
    elements
    of
    a
    sequence
    according
    to
    a
    specified
    key
    selector
    function and projects
    the
    elements
    for each group by using a specified function.
    
    GroupBy < TSource, TKey, TElement > (IEnumerable < TSource >, Func < TSource, TKey >, Func < TSource, TElement >, IEqualityComparer < TKey >)
    Groups
    the
    elements
    of
    a
    sequence
    according
    to
    a
    key
    selector
    function.The
    keys
    are
    compared
    by
    using
    a
    comparer and each
    group
    's elements are projected by using a specified function.
    
    GroupBy < TSource, TKey, TResult > (IEnumerable < TSource >, Func < TSource, TKey >, Func < TKey, IEnumerable < TSource >, TResult >)
    Groups
    the
    elements
    of
    a
    sequence
    according
    to
    a
    specified
    key
    selector
    function and creates
    a
    result
    value and its
    key.
    
    GroupBy < TSource, TKey, TResult > (IEnumerable < TSource >, Func < TSource, TKey >, Func < TKey, IEnumerable < TSource >, TResult >, IEqualityComparer < TKey >)
    Groups
    the
    elements
    of
    a
    sequence
    according
    to
    a
    specified
    key
    selector
    function and creates
    a
    result
    value and its
    key.The
    keys
    are
    compared
    by
    using
    a
    specified
    comparer.
    
    GroupBy < TSource, TKey, TElement, TResult > (IEnumerable < TSource >, Func < TSource, TKey >, Func < TSource, TElement >, Func < TKey, IEnumerable < TElement >, TResult >)
    Groups
    the
    elements
    of
    a
    sequence
    according
    to
    a
    specified
    key
    selector
    function and creates
    a
    result
    value and its
    key.The
    elements
    of
    each
    group
    are
    projected
    by
    using
    a
    specified
    function.
    
    GroupBy < TSource, TKey, TElement, TResult > (IEnumerable < TSource >, Func < TSource, TKey >, Func < TSource, TElement >, Func < TKey, IEnumerable < TElement >, TResult >, IEqualityComparer < TKey >)
    Groups
    the
    elements
    of
    a
    sequence
    according
    to
    a
    specified
    key
    selector
    function and creates
    a
    result
    value and its
    key.Key
    values
    are
    compared
    by
    using
    a
    specified
    comparer, and the
    elements
    of
    each
    group
    are
    projected
    by
    using
    a
    specified
    function.
    
    GroupJoin < TOuter, TInner, TKey, TResult > (IEnumerable < TOuter >, IEnumerable < TInner >, Func < TOuter, TKey >, Func < TInner, TKey >, Func < TOuter, IEnumerable < TInner >, TResult >)
    Correlates
    the
    elements
    of
    two
    sequences
    based
    on
    equality
    of
    keys and groups
    the
    results.The
    default
    equality
    comparer is used
    to
    compare
    keys.
    
    GroupJoin < TOuter, TInner, TKey, TResult > (IEnumerable < TOuter >, IEnumerable < TInner >, Func < TOuter, TKey >, Func < TInner, TKey >, Func < TOuter, IEnumerable < TInner >, TResult >, IEqualityComparer < TKey >)
    Correlates
    the
    elements
    of
    two
    sequences
    based
    on
    key
    equality and groups
    the
    results.A
    specified
    IEqualityComparer[T] is used
    to
    compare
    keys.
    
    Intersect < TSource > (IEnumerable < TSource >, IEnumerable < TSource >)
    Produces
    the
    set
    intersection
    of
    two
    sequences
    by
    using
    the
    default
    equality
    comparer
    to
    compare
    values.
    
    Intersect < TSource > (IEnumerable < TSource >, IEnumerable < TSource >, IEqualityComparer < TSource >)
    Produces
    the
    set
    intersection
    of
    two
    sequences
    by
    using
    the
    specified
    IEqualityComparer[T]
    to
    compare
    values.
    
    IntersectBy < TSource, TKey > (IEnumerable < TSource >, IEnumerable < TKey >, Func < TSource, TKey >)
    Produces
    the
    set
    intersection
    of
    two
    sequences
    according
    to
    a
    specified
    key
    selector
    function.
    
    IntersectBy < TSource, TKey > (IEnumerable < TSource >, IEnumerable < TKey >, Func < TSource, TKey >, IEqualityComparer < TKey >)
    Produces
    the
    set
    intersection
    of
    two
    sequences
    according
    to
    a
    specified
    key
    selector
    function.
    
    Join < TOuter, TInner, TKey, TResult > (IEnumerable < TOuter >, IEnumerable < TInner >, Func < TOuter, TKey >, Func < TInner, TKey >, Func < TOuter, TInner, TResult >)
    Correlates
    the
    elements
    of
    two
    sequences
    based
    on
    matching
    keys.The
    default
    equality
    comparer is used
    to
    compare
    keys.
    
    Join < TOuter, TInner, TKey, TResult > (IEnumerable < TOuter >, IEnumerable < TInner >, Func < TOuter, TKey >, Func < TInner, TKey >, Func < TOuter, TInner, TResult >, IEqualityComparer < TKey >)
    Correlates
    the
    elements
    of
    two
    sequences
    based
    on
    matching
    keys.A
    specified
    IEqualityComparer[T] is used
    to
    compare
    keys.
    
    Last < TSource > (IEnumerable < TSource >)
    Returns
    the
    last
    element
    of
    a
    sequence.
    
    Last < TSource > (IEnumerable < TSource >, Func < TSource, Boolean >)
    Returns
    the
    last
    element
    of
    a
    sequence
    that
    satisfies
    a
    specified
    condition.
    
    LastOrDefault < TSource > (IEnumerable < TSource >)
    Returns
    the
    last
    element
    of
    a
    sequence, or a
    default
    value if the
    sequence
    contains
    no
    elements.
    
    LastOrDefault < TSource > (IEnumerable < TSource >, TSource)
    Returns
    the
    last
    element
    of
    a
    sequence, or a
    specified
    default
    value if the
    sequence
    contains
    no
    elements.
    
    LastOrDefault < TSource > (IEnumerable < TSource >, Func < TSource, Boolean >)
    Returns
    the
    last
    element
    of
    a
    sequence
    that
    satisfies
    a
    condition or a
    default
    value if no
    such
    element is found.
    
    LastOrDefault < TSource > (IEnumerable < TSource >, Func < TSource, Boolean >, TSource)
    Returns
    the
    last
    element
    of
    a
    sequence
    that
    satisfies
    a
    condition, or a
    specified
    default
    value if no
    such
    element is found.
    
    LongCount < TSource > (IEnumerable < TSource >)
    Returns
    an
    Int64
    that
    represents
    the
    total
    number
    of
    elements in a
    sequence.
    
    LongCount < TSource > (IEnumerable < TSource >, Func < TSource, Boolean >)
    Returns
    an
    Int64
    that
    represents
    how
    many
    elements in a
    sequence
    satisfy
    a
    condition.
    
    Max < TSource > (IEnumerable < TSource >)
    Returns
    the
    maximum
    value in a
    generic
    sequence.
    
    Max < TSource > (IEnumerable < TSource >, IComparer < TSource >)
    Returns
    the
    maximum
    value in a
    generic
    sequence.
    
    Max < TSource > (IEnumerable < TSource >, Func < TSource, Decimal >)
    Invokes
    a
    transform
    function
    on
    each
    element
    of
    a
    sequence and returns
    the
    maximum
    Decimal
    value.
    
    Max < TSource > (IEnumerable < TSource >, Func < TSource, Double >)
    Invokes
    a
    transform
    function
    on
    each
    element
    of
    a
    sequence and returns
    the
    maximum
    Double
    value.
    
    Max < TSource > (IEnumerable < TSource >, Func < TSource, Int32 >)
    Invokes
    a
    transform
    function
    on
    each
    element
    of
    a
    sequence and returns
    the
    maximum
    Int32
    value.
    
    Max < TSource > (IEnumerable < TSource >, Func < TSource, Int64 >)
    Invokes
    a
    transform
    function
    on
    each
    element
    of
    a
    sequence and returns
    the
    maximum
    Int64
    value.
    
    Max < TSource > (IEnumerable < TSource >, Func < TSource, Nullable < Decimal >>)
    Invokes
    a
    transform
    function
    on
    each
    element
    of
    a
    sequence and returns
    the
    maximum
    nullable
    Decimal
    value.
    
    Max < TSource > (IEnumerable < TSource >, Func < TSource, Nullable < Double >>)
    Invokes
    a
    transform
    function
    on
    each
    element
    of
    a
    sequence and returns
    the
    maximum
    nullable
    Double
    value.
    
    Max < TSource > (IEnumerable < TSource >, Func < TSource, Nullable < Int32 >>)
    Invokes
    a
    transform
    function
    on
    each
    element
    of
    a
    sequence and returns
    the
    maximum
    nullable
    Int32
    value.
    
    Max < TSource > (IEnumerable < TSource >, Func < TSource, Nullable < Int64 >>)
    Invokes
    a
    transform
    function
    on
    each
    element
    of
    a
    sequence and returns
    the
    maximum
    nullable
    Int64
    value.
    
    Max < TSource > (IEnumerable < TSource >, Func < TSource, Nullable < Single >>)
    Invokes
    a
    transform
    function
    on
    each
    element
    of
    a
    sequence and returns
    the
    maximum
    nullable
    Single
    value.
    
    Max < TSource > (IEnumerable < TSource >, Func < TSource, Single >)
    Invokes
    a
    transform
    function
    on
    each
    element
    of
    a
    sequence and returns
    the
    maximum
    Single
    value.
    
    Max < TSource, TResult > (IEnumerable < TSource >, Func < TSource, TResult >)
    Invokes
    a
    transform
    function
    on
    each
    element
    of
    a
    generic
    sequence and returns
    the
    maximum
    resulting
    value.
    
    MaxBy < TSource, TKey > (IEnumerable < TSource >, Func < TSource, TKey >)
    Returns
    the
    maximum
    value in a
    generic
    sequence
    according
    to
    a
    specified
    key
    selector
    function.
    
    MaxBy < TSource, TKey > (IEnumerable < TSource >, Func < TSource, TKey >, IComparer < TKey >)
    Returns
    the
    maximum
    value in a
    generic
    sequence
    according
    to
    a
    specified
    key
    selector
    function and key
    comparer.
    
    Min < TSource > (IEnumerable < TSource >)
    Returns
    the
    minimum
    value in a
    generic
    sequence.
    
    Min < TSource > (IEnumerable < TSource >, IComparer < TSource >)
    Returns
    the
    minimum
    value in a
    generic
    sequence.
    
    Min < TSource > (IEnumerable < TSource >, Func < TSource, Decimal >)
    Invokes
    a
    transform
    function
    on
    each
    element
    of
    a
    sequence and returns
    the
    minimum
    Decimal
    value.
    
    Min < TSource > (IEnumerable < TSource >, Func < TSource, Double >)
    Invokes
    a
    transform
    function
    on
    each
    element
    of
    a
    sequence and returns
    the
    minimum
    Double
    value.
    
    Min < TSource > (IEnumerable < TSource >, Func < TSource, Int32 >)
    Invokes
    a
    transform
    function
    on
    each
    element
    of
    a
    sequence and returns
    the
    minimum
    Int32
    value.
    
    Min < TSource > (IEnumerable < TSource >, Func < TSource, Int64 >)
    Invokes
    a
    transform
    function
    on
    each
    element
    of
    a
    sequence and returns
    the
    minimum
    Int64
    value.
    
    Min < TSource > (IEnumerable < TSource >, Func < TSource, Nullable < Decimal >>)
    Invokes
    a
    transform
    function
    on
    each
    element
    of
    a
    sequence and returns
    the
    minimum
    nullable
    Decimal
    value.
    
    Min < TSource > (IEnumerable < TSource >, Func < TSource, Nullable < Double >>)
    Invokes
    a
    transform
    function
    on
    each
    element
    of
    a
    sequence and returns
    the
    minimum
    nullable
    Double
    value.
    
    Min < TSource > (IEnumerable < TSource >, Func < TSource, Nullable < Int32 >>)
    Invokes
    a
    transform
    function
    on
    each
    element
    of
    a
    sequence and returns
    the
    minimum
    nullable
    Int32
    value.
    
    Min < TSource > (IEnumerable < TSource >, Func < TSource, Nullable < Int64 >>)
    Invokes
    a
    transform
    function
    on
    each
    element
    of
    a
    sequence and returns
    the
    minimum
    nullable
    Int64
    value.
    
    Min < TSource > (IEnumerable < TSource >, Func < TSource, Nullable < Single >>)
    Invokes
    a
    transform
    function
    on
    each
    element
    of
    a
    sequence and returns
    the
    minimum
    nullable
    Single
    value.
    
    Min < TSource > (IEnumerable < TSource >, Func < TSource, Single >)
    Invokes
    a
    transform
    function
    on
    each
    element
    of
    a
    sequence and returns
    the
    minimum
    Single
    value.
    
    Min < TSource, TResult > (IEnumerable < TSource >, Func < TSource, TResult >)
    Invokes
    a
    transform
    function
    on
    each
    element
    of
    a
    generic
    sequence and returns
    the
    minimum
    resulting
    value.
    
    MinBy < TSource, TKey > (IEnumerable < TSource >, Func < TSource, TKey >)
    Returns
    the
    minimum
    value in a
    generic
    sequence
    according
    to
    a
    specified
    key
    selector
    function.
    
    MinBy < TSource, TKey > (IEnumerable < TSource >, Func < TSource, TKey >, IComparer < TKey >)
    Returns
    the
    minimum
    value in a
    generic
    sequence
    according
    to
    a
    specified
    key
    selector
    function and key
    comparer.
    
    OfType < TResult > (IEnumerable)
    Filters
    the
    elements
    of
    an
    IEnumerable
    based
    on
    a
    specified
    type.
    
    OrderBy < TSource, TKey > (IEnumerable < TSource >, Func < TSource, TKey >)
    Sorts
    the
    elements
    of
    a
    sequence in ascending
    order
    according
    to
    a
    key.
    
    OrderBy < TSource, TKey > (IEnumerable < TSource >, Func < TSource, TKey >, IComparer < TKey >)
    Sorts
    the
    elements
    of
    a
    sequence in ascending
    order
    by
    using
    a
    specified
    comparer.
    
    OrderByDescending < TSource, TKey > (IEnumerable < TSource >, Func < TSource, TKey >)
    Sorts
    the
    elements
    of
    a
    sequence in descending
    order
    according
    to
    a
    key.
    
    OrderByDescending < TSource, TKey > (IEnumerable < TSource >, Func < TSource, TKey >, IComparer < TKey >)
    Sorts
    the
    elements
    of
    a
    sequence in descending
    order
    by
    using
    a
    specified
    comparer.
    
    Prepend < TSource > (IEnumerable < TSource >, TSource)
    Adds
    a
    value
    to
    the
    beginning
    of
    the
    sequence.
    
    Reverse < TSource > (IEnumerable < TSource >)
    Inverts
    the
    order
    of
    the
    elements in a
    sequence.
    
    Select < TSource, TResult > (IEnumerable < TSource >, Func < TSource, TResult >)
    Projects
    each
    element
    of
    a
    sequence
    into
    a
    new
    form.
    
    Select < TSource, TResult > (IEnumerable < TSource >, Func < TSource, Int32, TResult >)
    Projects
    each
    element
    of
    a
    sequence
    into
    a
    new
    form
    by
    incorporating
    the
    element
    's index.
    
    SelectMany < TSource, TResult > (IEnumerable < TSource >, Func < TSource, IEnumerable < TResult >>)
    Projects
    each
    element
    of
    a
    sequence
    to
    an
    IEnumerable[T] and flattens
    the
    resulting
    sequences
    into
    one
    sequence.
    
    SelectMany < TSource, TResult > (IEnumerable < TSource >, Func < TSource, Int32, IEnumerable < TResult >>)
    Projects
    each
    element
    of
    a
    sequence
    to
    an
    IEnumerable[T], and flattens
    the
    resulting
    sequences
    into
    one
    sequence.The
    index
    of
    each
    source
    element is used in the
    projected
    form
    of
    that
    element.
    
    SelectMany < TSource, TCollection, TResult > (IEnumerable < TSource >, Func < TSource, IEnumerable < TCollection >>, Func < TSource, TCollection, TResult >)
    Projects
    each
    element
    of
    a
    sequence
    to
    an
    IEnumerable[T], flattens
    the
    resulting
    sequences
    into
    one
    sequence, and invokes
    a
    result
    selector
    function
    on
    each
    element
    therein.
    
    SelectMany < TSource, TCollection, TResult > (IEnumerable < TSource >, Func < TSource, Int32, IEnumerable < TCollection >>, Func < TSource, TCollection, TResult >)
    Projects
    each
    element
    of
    a
    sequence
    to
    an
    IEnumerable[T], flattens
    the
    resulting
    sequences
    into
    one
    sequence, and invokes
    a
    result
    selector
    function
    on
    each
    element
    therein.The
    index
    of
    each
    source
    element is used in the
    intermediate
    projected
    form
    of
    that
    element.
    
    SequenceEqual < TSource > (IEnumerable < TSource >, IEnumerable < TSource >)
    Determines
    whether
    two
    sequences
    are
    equal
    by
    comparing
    the
    elements
    by
    using
    the
    default
    equality
    comparer
    for their type.
    
    SequenceEqual < TSource > (IEnumerable < TSource >, IEnumerable < TSource >, IEqualityComparer < TSource >)
    Determines
    whether
    two
    sequences
    are
    equal
    by
    comparing
    their
    elements
    by
    using
    a
    specified
    IEqualityComparer[T].
    
    Single < TSource > (IEnumerable < TSource >)
    Returns
    the
    only
    element
    of
    a
    sequence, and throws
    an
    exception if there is not exactly
    one
    element in the
    sequence.
    
    Single < TSource > (IEnumerable < TSource >, Func < TSource, Boolean >)
    Returns
    the
    only
    element
    of
    a
    sequence
    that
    satisfies
    a
    specified
    condition, and throws
    an
    exception if more
    than
    one
    such
    element
    exists.
    
    SingleOrDefault < TSource > (IEnumerable < TSource >)
    Returns
    the
    only
    element
    of
    a
    sequence, or a
    default
    value if the
    sequence is empty;
    this
    method
    throws
    an
    exception if there is more
    than
    one
    element in the
    sequence.
    
    SingleOrDefault < TSource > (IEnumerable < TSource >, TSource)
    Returns
    the
    only
    element
    of
    a
    sequence, or a
    specified
    default
    value if the
    sequence is empty;
    this
    method
    throws
    an
    exception if there is more
    than
    one
    element in the
    sequence.
    
    SingleOrDefault < TSource > (IEnumerable < TSource >, Func < TSource, Boolean >)
    Returns
    the
    only
    element
    of
    a
    sequence
    that
    satisfies
    a
    specified
    condition or a
    default
    value if no
    such
    element
    exists;
    this
    method
    throws
    an
    exception if more
    than
    one
    element
    satisfies
    the
    condition.
    
    SingleOrDefault < TSource > (IEnumerable < TSource >, Func < TSource, Boolean >, TSource)
    Returns
    the
    only
    element
    of
    a
    sequence
    that
    satisfies
    a
    specified
    condition, or a
    specified
    default
    value if no
    such
    element
    exists;
    this
    method
    throws
    an
    exception if more
    than
    one
    element
    satisfies
    the
    condition.
    
    Skip < TSource > (IEnumerable < TSource >, Int32)
    Bypasses
    a
    specified
    number
    of
    elements in a
    sequence and then
    returns
    the
    remaining
    elements.
    
    SkipLast < TSource > (IEnumerable < TSource >, Int32)
    Returns
    a
    new
    enumerable
    collection
    that
    contains
    the
    elements
    from source
    with the last count elements of the source collection omitted.
    
    SkipWhile < TSource > (IEnumerable < TSource >, Func < TSource, Boolean >)
    Bypasses
    elements in a
    sequence as long as a
    specified
    condition is true and then
    returns
    the
    remaining
    elements.
    
    SkipWhile < TSource > (IEnumerable < TSource >, Func < TSource, Int32, Boolean >)
    Bypasses
    elements in a
    sequence as long as a
    specified
    condition is true and then
    returns
    the
    remaining
    elements.The
    element
    's index is used in the logic of the predicate function.
    
    Sum < TSource > (IEnumerable < TSource >, Func < TSource, Decimal >)
    Computes
    the
    sum
    of
    the
    sequence
    of
    Decimal
    values
    that
    are
    obtained
    by
    invoking
    a
    transform
    function
    on
    each
    element
    of
    the
    input
    sequence.
    
    Sum < TSource > (IEnumerable < TSource >, Func < TSource, Double >)
    Computes
    the
    sum
    of
    the
    sequence
    of
    Double
    values
    that
    are
    obtained
    by
    invoking
    a
    transform
    function
    on
    each
    element
    of
    the
    input
    sequence.
    
    Sum < TSource > (IEnumerable < TSource >, Func < TSource, Int32 >)
    Computes
    the
    sum
    of
    the
    sequence
    of
    Int32
    values
    that
    are
    obtained
    by
    invoking
    a
    transform
    function
    on
    each
    element
    of
    the
    input
    sequence.
    
    Sum < TSource > (IEnumerable < TSource >, Func < TSource, Int64 >)
    Computes
    the
    sum
    of
    the
    sequence
    of
    Int64
    values
    that
    are
    obtained
    by
    invoking
    a
    transform
    function
    on
    each
    element
    of
    the
    input
    sequence.
    
    Sum < TSource > (IEnumerable < TSource >, Func < TSource, Nullable < Decimal >>)
    Computes
    the
    sum
    of
    the
    sequence
    of
    nullable
    Decimal
    values
    that
    are
    obtained
    by
    invoking
    a
    transform
    function
    on
    each
    element
    of
    the
    input
    sequence.
    
    Sum < TSource > (IEnumerable < TSource >, Func < TSource, Nullable < Double >>)
    Computes
    the
    sum
    of
    the
    sequence
    of
    nullable
    Double
    values
    that
    are
    obtained
    by
    invoking
    a
    transform
    function
    on
    each
    element
    of
    the
    input
    sequence.
    
    Sum < TSource > (IEnumerable < TSource >, Func < TSource, Nullable < Int32 >>)
    Computes
    the
    sum
    of
    the
    sequence
    of
    nullable
    Int32
    values
    that
    are
    obtained
    by
    invoking
    a
    transform
    function
    on
    each
    element
    of
    the
    input
    sequence.
    
    Sum < TSource > (IEnumerable < TSource >, Func < TSource, Nullable < Int64 >>)
    Computes
    the
    sum
    of
    the
    sequence
    of
    nullable
    Int64
    values
    that
    are
    obtained
    by
    invoking
    a
    transform
    function
    on
    each
    element
    of
    the
    input
    sequence.
    
    Sum < TSource > (IEnumerable < TSource >, Func < TSource, Nullable < Single >>)
    Computes
    the
    sum
    of
    the
    sequence
    of
    nullable
    Single
    values
    that
    are
    obtained
    by
    invoking
    a
    transform
    function
    on
    each
    element
    of
    the
    input
    sequence.
    
    Sum < TSource > (IEnumerable < TSource >, Func < TSource, Single >)
    Computes
    the
    sum
    of
    the
    sequence
    of
    Single
    values
    that
    are
    obtained
    by
    invoking
    a
    transform
    function
    on
    each
    element
    of
    the
    input
    sequence.
    
    Take < TSource > (IEnumerable < TSource >, Int32)
    Returns
    a
    specified
    number
    of
    contiguous
    elements
    of
    a
    sequence.
    
    Take < TSource > (IEnumerable < TSource >, Range)
    Returns
    a
    specified
    range
    of
    contiguous
    elements.
    
    TakeLast < TSource > (IEnumerable < TSource >, Int32)
    Returns
    a
    new
    enumerable
    collection
    that
    contains
    the
    last
    count
    elements
    from source.
    
    TakeWhile < TSource > (IEnumerable < TSource >, Func < TSource, Boolean >)
    Returns
    elements as a
    specified
    condition is true.
    
    TakeWhile < TSource > (IEnumerable < TSource >, Func < TSource, Int32, Boolean >)
    Returns
    elements as a
    specified
    condition is true.The
    element
    's index is used in the logic of the predicate function.
    
    ToArray < TSource > (IEnumerable < TSource >)
    Creates
    an
    array


[T].

ToDictionary < TSource, TKey > (IEnumerable < TSource >, Func < TSource, TKey >)
Creates
a
Dictionary < TKey, TValue >
[T]
according
to
a
specified
key
selector
function.

ToDictionary < TSource, TKey > (IEnumerable < TSource >, Func < TSource, TKey >, IEqualityComparer < TKey >)
Creates
a
Dictionary < TKey, TValue >
[T]
according
to
a
specified
key
selector
function and key
comparer.

ToDictionary < TSource, TKey, TElement > (IEnumerable < TSource >, Func < TSource, TKey >, Func < TSource, TElement >)
Creates
a
Dictionary < TKey, TValue >
[T]
according
to
specified
key
selector and element
selector
functions.

ToDictionary < TSource, TKey, TElement > (IEnumerable < TSource >, Func < TSource, TKey >, Func < TSource, TElement >, IEqualityComparer < TKey >)
Creates
a
Dictionary < TKey, TValue >
[T]
according
to
a
specified
key
selector
function, a
comparer, and an
element
selector
function.

ToHashSet < TSource > (IEnumerable < TSource >)
Creates
a
HashSet[T]
[T].

ToHashSet < TSource > (IEnumerable < TSource >, IEqualityComparer < TSource >)
Creates
a
HashSet[T]
[T]
using
the
comparer
to
compare
keys.

ToList < TSource > (IEnumerable < TSource >)
Creates
a
List[T]
[T].

ToLookup < TSource, TKey > (IEnumerable < TSource >, Func < TSource, TKey >)
Creates
a
Lookup < TKey, TElement >
[T]
according
to
a
specified
key
selector
function.

ToLookup < TSource, TKey > (IEnumerable < TSource >, Func < TSource, TKey >, IEqualityComparer < TKey >)
Creates
a
Lookup < TKey, TElement >
[T]
according
to
a
specified
key
selector
function and key
comparer.

ToLookup < TSource, TKey, TElement > (IEnumerable < TSource >, Func < TSource, TKey >, Func < TSource, TElement >)
Creates
a
Lookup < TKey, TElement >
[T]
according
to
specified
key
selector and element
selector
functions.

ToLookup < TSource, TKey, TElement > (IEnumerable < TSource >, Func < TSource, TKey >, Func < TSource, TElement >, IEqualityComparer < TKey >)
Creates
a
Lookup < TKey, TElement >
[T]
according
to
a
specified
key
selector
function, a
comparer and an
element
selector
function.

TryGetNonEnumeratedCount < TSource > (IEnumerable < TSource >, Int32)
Attempts
to
determine
the
number
of
elements in a
sequence
without
forcing
an
enumeration.

Union < TSource > (IEnumerable < TSource >, IEnumerable < TSource >)
Produces
the
set
union
of
two
sequences
by
using
the
default
equality
comparer.

Union < TSource > (IEnumerable < TSource >, IEnumerable < TSource >, IEqualityComparer < TSource >)
Produces
the
set
union
of
two
sequences
by
using
a
specified
IEqualityComparer[T].

UnionBy < TSource, TKey > (IEnumerable < TSource >, IEnumerable < TSource >, Func < TSource, TKey >)
Produces
the
set
union
of
two
sequences
according
to
a
specified
key
selector
function.

UnionBy < TSource, TKey > (IEnumerable < TSource >, IEnumerable < TSource >, Func < TSource, TKey >, IEqualityComparer < TKey >)
Produces
the
set
union
of
two
sequences
according
to
a
specified
key
selector
function.

Where < TSource > (IEnumerable < TSource >, Func < TSource, Boolean >)
Filters
a
sequence
of
values
based
on
a
predicate.

Where < TSource > (IEnumerable < TSource >, Func < TSource, Int32, Boolean >)
Filters
a
sequence
of
values
based
on
a
predicate.Each
element
's index is used in the logic of the predicate function.

Zip < TFirst, TSecond > (IEnumerable < TFirst >, IEnumerable < TSecond >)
Produces
a
sequence
of
tuples
with elements from the two specified sequences.

Zip < TFirst, TSecond, TThird > (IEnumerable < TFirst >, IEnumerable < TSecond >, IEnumerable < TThird >)
Produces
a
sequence
of
tuples
with elements from the three specified sequences.

Zip < TFirst, TSecond, TResult > (IEnumerable < TFirst >, IEnumerable < TSecond >, Func < TFirst, TSecond, TResult >)
Applies
a
specified
function
to
the
corresponding
elements
of
two
sequences, producing
a
sequence
of
the
results.

AsParallel(IEnumerable)
Enables
parallelization
of
a
query.

AsParallel < TSource > (IEnumerable < TSource >)
Enables
parallelization
of
a
query.

AsQueryable(IEnumerable)
Converts
an
IEnumerable
to
an
IQueryable.

AsQueryable < TElement > (IEnumerable < TElement >)
Converts
a
generic
IEnumerable[T]
to
a
generic
IQueryable[T].

AsMemory[T](ArraySegment[T])
Creates
a
new
memory
region
over
the
portion
of
the
target
array
segment.

AsMemory[T](ArraySegment[T], Int32)
Creates
a
new
memory
region
over
the
portion
of
the
target
array
segment
starting
at
a
specified
position
to
the
end
of
the
segment.

AsMemory[T](ArraySegment[T], Int32, Int32)
Creates
a
new
memory
region
over
the
portion
of
the
target
array
segment
beginning
at
a
specified
position
with a specified length.

AsSpan[T](ArraySegment[T])
Creates
a
new
span
over
a
target
array
segment.

AsSpan[T](ArraySegment[T], Index)
Creates
a
new
span
over
a
portion
of
the
target
array
segment
beginning
at
a
specified
index and ending
at
the
end
of
the
segment.

AsSpan[T](ArraySegment[T], Int32)
Creates
a
new
span
over
a
portion
of
a
target
array
segment
position
to
the
end
of
the
segment.

AsSpan[T](ArraySegment[T], Int32, Int32)
Creates
a
new
span
over
a
portion
of
a
target
array
segment
position
for a specified length.

AsSpan[T](ArraySegment[T], Range)
Creates
a
new
span
over
a
portion
of
a
target
array
segment
using
the
range
start and end
indexes.

Ancestors[T](IEnumerable[T])
Returns
a
collection
of
elements
that
contains
the
ancestors
of
every
node in the
source
collection.

Ancestors[T](IEnumerable[T], XName)
Returns
a
filtered
collection
of
elements
that
contains
the
ancestors
of
every
node in the
source
collection.Only
elements
that
have
a
matching
XName
are
included in the
collection.

DescendantNodes[T](IEnumerable[T])
Returns
a
collection
of
the
descendant
nodes
of
every
document and element in the
source
collection.

Descendants[T](IEnumerable[T])
Returns
a
collection
of
elements
that
contains
the
descendant
elements
of
every
element and document in the
source
collection.

Descendants[T](IEnumerable[T], XName)
Returns
a
filtered
collection
of
elements
that
contains
the
descendant
elements
of
every
element and document in the
source
collection.Only
elements
that
have
a
matching
XName
are
included in the
collection.

Elements[T](IEnumerable[T])
Returns
a
collection
of
the
child
elements
of
every
element and document in the
source
collection.

Elements[T](IEnumerable[T], XName)
Returns
a
filtered
collection
of
the
child
elements
of
every
element and document in the
source
collection.Only
elements
that
have
a
matching
XName
are
included in the
collection.

InDocumentOrder[T](IEnumerable[T])
Returns
a
collection
of
nodes
that
contains
all
nodes in the
source
collection, sorted in document
order.

Nodes[T](IEnumerable[T])
Returns
a
collection
of
the
child
nodes
of
every
document and element in the
source
collection.

Remove[T](IEnumerable[T])
Removes
every
node in the
source
collection
node.


class Enumerator(ValueType, Generic[T], IEnumerator[T], IDisposable):
    """Provides an enumerator for the elements of an ArraySegment[T]."""
    
    @property
    def Current(self) -> T:
        """Gets a reference to the item at the current position of the enumerator."""
    
    def MoveNext(self) -> Boolean:
        """Advances the enumerator to the next element of the ArraySegment[T]."""
    
    def __iter__(self): ...
    
    def __next__(self): ...


class Boolean(bool, ValueType, IComparable, IComparable[Boolean], IConvertible, IEquatable[Boolean]):
    """Represents a Boolean (true or false) value."""
    
    FalseString: Final[Annotated[String, 'Represents the Boolean value false as a string. This field is read-only.']] = ...
    
    TrueString: Final[Annotated[String, 'Represents the Boolean value true as a string. This field is read-only.']] = ...
    
    @overload
    def CompareTo(self, value: BooleanType) -> Int32:
        """Compares this instance to a specified Boolean object and returns
        an integer that indicates their relationship to one another.
        """
    
    @overload
    def Equals(self, obj: BooleanType) -> Boolean:
        """Returns a value indicating whether this instance is equal to a
        specified Boolean object.
        """
    
    @staticmethod
    @overload
    def Parse(value: ReadOnlySpan[Char]) -> Boolean:
        """Converts the specified span representation of a logical value to
        its Boolean equivalent.
        """
    
    @staticmethod
    @overload
    def Parse(value: StringType) -> Boolean:
        """Converts the specified string representation of a logical value
        to its Boolean equivalent.
        """
    
    @overload
    def ToString(self) -> String:
        """Converts the value of this instance to its equivalent string
        representation (either "True" or "False").
        """
    
    def TryFormat(self, destination: Span[Char], charsWritten: Int32) -> Boolean:
        """Tries to format the value of the current boolean instance into the
        provided span of characters.
        """
    
    @overload
    def TryParse(self, value: ReadOnlySpan[Char], result: Boolean) -> Boolean:
        """Tries to convert the specified span representation of a logical
        value to its Boolean equivalent.
        """
    
    @overload
    def TryParse(self, value: Optional[String], result: Boolean) -> Boolean:
        """Tries to convert the specified string representation of a logical
        value to its Boolean equivalent.
        """


class Byte(int, ValueType, IComparable, IComparable[Byte], IConvertible, IEquatable[Byte], ISpanFormattable):
    """Represents an 8-bit unsigned integer."""
    
    MaxValue: Final[Annotated[Byte, 'Represents the largest possible value of a Byte. This field is constant.']] = ...
    
    MinValue: Final[Annotated[Byte, 'Represents the smallest possible value of a Byte. This field is constant.']] = ...
    
    @overload
    def CompareTo(self, obj: ByteType) -> Int32:
        """Compares this instance to a specified 8-bit unsigned integer and
        returns an indication of their relative values.
        """
    
    @overload
    def Equals(self, obj: ByteType) -> Boolean:
        """Returns a value indicating whether this instance and a specified
        Byte object represent the same value.
        """
    
    @staticmethod
    @overload
    def Parse(value: ReadOnlySpan[Char]) -> Byte:
        """Converts the span representation of a number in a specified style
        and culture-specific format to its Byte equivalent.
        """
    
    @staticmethod
    @overload
    def Parse(value: StringType) -> Byte:
        """Converts the string representation of a number to its Byte equivalent."""
    
    @staticmethod
    @overload
    def Parse(value: StringType, provider: Optional[IFormatProvider]) -> Byte:
        """Converts the string representation of a number in a specified
        culture-specific format to its Byte equivalent.
        """
    
    @staticmethod
    @overload
    def Parse(value: StringType, style: NumberStyles) -> Byte:
        """Converts the string representation of a number in a specified style
        to its Byte equivalent.
        """
    
    @staticmethod
    @overload
    def Parse(value: StringType, style: NumberStyles, provider: Optional[IFormatProvider]) -> Byte:
        """Converts the string representation of a number in a specified
        style and culture-specific format to its Byte equivalent.
        """
    
    @overload
    def ToString(self) -> String:
        """Converts the value of the current Byte object to its equivalent
        string representation.
        """
    
    @overload
    def ToString(self, provider: Optional[IFormatProvider]) -> String:
        """Converts the numeric value of the current Byte object to its
        equivalent string representation using the specified
        culture-specific formatting information.
        """
    
    @overload
    def ToString(self, format: Optional[StringType]) -> String:
        """Converts the value of the current Byte object to its equivalent
        string representation using the specified format.
        """
    
    @overload
    def ToString(self, format: Optional[StringType], provider: Optional[IFormatProvider]) -> String:
        """Converts the value of the current Byte object to its equivalent
        string representation using the specified format and culture-specific
        formatting information.
        """
    
    def TryFormat(self, destination: Span[Char], charsWritten: Int32, format: ReadOnlySpan[Char] = None, provider: IFormatProvider = None) -> Boolean:
        """Tries to format the value of the current 8-bit unsigned integer
        instance into the provided span of characters.
        """
    
    @overload
    def TryParse(self, s: ReadOnlySpan[Char], result: Byte) -> Boolean:
        """Tries to convert the span representation of a number to its Byte
        equivalent, and returns a value that indicates whether the
        conversion succeeded.
        """
    
    @overload
    def TryParse(self, s: ReadOnlySpan[Char], style: NumberStyles, provider: Optional[IFormatProvider], result: Byte) -> Boolean:
        """Converts the span representation of a number in a specified style
        and culture-specific format to its Byte equivalent. A return value
        indicates whether the conversion succeeded or failed.
        """
    
    @overload
    def TryParse(self, s: Optional[String], result: Byte) -> Boolean:
        """Tries to convert the string representation of a number to its Byte
        equivalent, and returns a value that indicates whether the conversion
        succeeded.
        """
    
    @overload
    def TryParse(self, String, style: NumberStyles, provider: Optional[IFormatProvider], result: Byte) -> Boolean:
        """Converts the string representation of a number in a specified style
        and culture-specific format to its Byte equivalent. A return value
        indicates whether the conversion succeeded or failed.
        """


class Char(str, ValueType, IComparable, IComparable[Char], IConvertible, IEquatable[Char], ISpanFormattable):
    """Represents a character as a UTF-16 code unit."""
    
    MaxValue: Final[Annotated[Char, 'Represents the largest possible value of a Char. This field is constant.']] = ...
    MinValue: Final[Annotated[Char, 'Represents the smallest possible value of a Char. This field is constant.']] = ...
    
    @overload
    def CompareTo(self, obj: Optional[CharType]) -> Int32:
        """Compares this instance to a specified Char object and indicates
        whether this instance precedes, follows, or appears in the same
        position in the sort order as the specified Char object.
        """
    
    @staticmethod
    def ConvertFromUtf32(utf32: Int32Type) -> String:
        """Converts the specified Unicode code point into a UTF-16 encoded string."""
    
    @staticmethod
    @overload
    def ConvertToUtf32(highSurrogate: CharType, lowSurrogate: CharType) -> Int32:
        """Converts the value of a UTF-16 encoded surrogate pair into a Unicode code point."""
    
    @staticmethod
    @overload
    def ConvertToUtf32(s: StringType, index: IntType) -> Int32:
        """Converts the value of a UTF-16 encoded character or surrogate pair
        at a specified position in a string into a Unicode code point.
        """
    
    def Equals(self, obj: CharType) -> Boolean:
        """Returns a value that indicates whether this instance is equal to the
        specified Char object.
        """
    
    @staticmethod
    @overload
    def GetNumericValue(c: CharType) -> Double:
        """Converts the specified numeric Unicode character to a
        double-precision floating point number.
        """
    
    @staticmethod
    @overload
    def GetNumericValue(s: StringType, index: IntType) -> Double:
        """Converts the numeric Unicode character at the specified position
        in a specified string to a double-precision floating point number.
        """
    
    @staticmethod
    @overload
    def GetUnicodeCategory(c: CharType) -> UnicodeCategory:
        """Categorizes a specified Unicode character into a group identified
        by one of the UnicodeCategory values.
        """
    
    @staticmethod
    @overload
    def GetUnicodeCategory(s: StringType, index: IntType) -> UnicodeCategory:
        """Categorizes the character at the specified position in a specified
        string into a group identified by one of the UnicodeCategory values.
        """
    
    @staticmethod
    def IsAscii(c: CharType) -> Boolean:
        """Returns true if c is an ASCII character ([ U+0000..U+007F ])."""
    
    @staticmethod
    @overload
    def IsControl(c: CharType) -> Boolean:
        """Indicates whether the specified Unicode character is categorized
        as a control character.
        """
    
    @staticmethod
    @overload
    def IsControl(s: StringType, index: IntType) -> Boolean:
        """Indicates whether the character at the specified position in a
        specified string is categorized as a control character.
        """
    
    @staticmethod
    @overload
    def IsDigit(c: CharType) -> Boolean:
        """Indicates whether the specified Unicode character is categorized
        as a decimal digit.
        """
    
    @staticmethod
    @overload
    def IsDigit(s: StringType, index: IntType) -> Boolean:
        """Indicates whether the character at the specified position in a
        specified string is categorized as a decimal digit.
        """
    
    @staticmethod
    @overload
    def IsHighSurrogate(c: CharType) -> Boolean:
        """Indicates whether the specified Char object is a high surrogate."""
    
    @staticmethod
    @overload
    def IsHighSurrogate(s: StringType, index: IntType) -> Boolean:
        """Indicates whether the Char object at the specified position in a
        string is a high surrogate.
        """
    
    @staticmethod
    @overload
    def IsLetter(c: CharType) -> Boolean:
        """Indicates whether the specified Unicode character is categorized
        as a Unicode letter.
        """
    
    @staticmethod
    @overload
    def IsLetter(s: StringType, index: IntType) -> Boolean:
        """Indicates whether the character at the specified position in a
        specified string is categorized as a Unicode letter.
        """
    
    @staticmethod
    @overload
    def IsLetterOrDigit(c: CharType) -> Boolean:
        """Indicates whether the specified Unicode character is categorized
        as a letter or a decimal digit.
        """
    
    @staticmethod
    @overload
    def IsLetterOrDigit(s: StringType, index: IntType) -> Boolean:
        """Indicates whether the character at the specified position in a
        specified string is categorized as a letter or a decimal digit.
        """
    
    @staticmethod
    @overload
    def IsLower(c: CharType) -> Boolean:
        """Indicates whether the specified Unicode character is categorized
        as a lowercase letter.
        """
    
    @staticmethod
    @overload
    def IsLower(s: StringType, index: IntType) -> Boolean:
        """Indicates whether the character at the specified position in a
        specified string is categorized as a lowercase letter.
        """
    
    @staticmethod
    @overload
    def IsLowSurrogate(c: CharType) -> Boolean:
        """Indicates whether the specified Char object is a low surrogate."""
    
    @staticmethod
    @overload
    def IsLowSurrogate(s: StringType, index: IntType) -> Boolean:
        """Indicates whether the Char object at the specified position in a
        string is a low surrogate.
        """
    
    @staticmethod
    @overload
    def IsNumber(c: CharType) -> Boolean:
        """Indicates whether the specified Unicode character is categorized as a number."""
    
    @staticmethod
    @overload
    def IsNumber(s: StringType, index: IntType) -> Boolean:
        """Indicates whether the character at the specified position in a
        specified string is categorized as a number.
        """
    
    @staticmethod
    @overload
    def IsPunctuation(c: CharType) -> Boolean:
        """Indicates whether the specified Unicode character is categorized
        as a punctuation mark.
        """
    
    @staticmethod
    @overload
    def IsPunctuation(s: StringType, index: IntType) -> Boolean:
        """Indicates whether the character at the specified position in a
        specified string is categorized as a punctuation mark.
        """
    
    @staticmethod
    @overload
    def IsSeparator(c: CharType) -> Boolean:
        """Indicates whether the specified Unicode character is categorized
        as a separator character.
        """
    
    @staticmethod
    @overload
    def IsSeparator(s: StringType, index: IntType) -> Boolean:
        """Indicates whether the character at the specified position in a
        specified string is categorized as a separator character.
        """
    
    @staticmethod
    @overload
    def IsSurrogate(c: CharType) -> Boolean:
        """Indicates whether the specified character has a surrogate code unit."""
    
    @staticmethod
    @overload
    def IsSurrogate(s: StringType, index: IntType) -> Boolean:
        """Indicates whether the character at the specified position in a
        specified string has a surrogate code unit.
        """
    
    @staticmethod
    @overload
    def IsSurrogatePair(highSurrogate: CharType, lowSurrogate: CharType) -> Boolean:
        """Indicates whether the two specified Char objects form a surrogate pair."""
    
    @staticmethod
    @overload
    def IsSurrogatePair(s: StringType, index: IntType) -> Boolean:
        """Indicates whether two adjacent Char objects at a specified position
        in a string form a surrogate pair.
        """
    
    @staticmethod
    @overload
    def IsSymbol(c: CharType) -> Boolean:
        """Indicates whether the specified Unicode character is categorized
        as a symbol character.
        """
    
    @staticmethod
    @overload
    def IsSymbol(s: StringType, index: IntType) -> Boolean:
        """Indicates whether the character at the specified position in a
        specified string is categorized as a symbol character.
        """
    
    @staticmethod
    @overload
    def IsUpper(c: CharType) -> Boolean:
        """Indicates whether the specified Unicode character is categorized
        as an uppercase letter.
        """
    
    @staticmethod
    @overload
    def IsUpper(s: StringType, index: IntType) -> Boolean:
        """Indicates whether the character at the specified position in a
        specified string is categorized as an uppercase letter.
        """
    
    @staticmethod
    @overload
    def IsWhiteSpace(c: CharType) -> Boolean:
        """Indicates whether the specified Unicode character is categorized as white space."""
    
    @staticmethod
    @overload
    def IsWhiteSpace(s: StringType, index: IntType) -> Boolean:
        """Indicates whether the character at the specified position in a
        specified string is categorized as white space.
        """
    
    @staticmethod
    def Parse(s: StringType) -> Char:
        """Converts the value of the specified string to its equivalent Unicode character."""
    
    @staticmethod
    @overload
    def ToLower(c: CharType) -> Char:
        """Converts the value of a Unicode character to its lowercase equivalent."""
    
    @staticmethod
    @overload
    def ToLower(c: CharType, culture: CultureInfo) -> Char:
        """Converts the value of a specified Unicode character to its
        lowercase equivalent using specified culture-specific
        formatting information.
        """
    
    @staticmethod
    def ToLowerInvariant(c: CharType) -> Char:
        """Converts the value of a Unicode character to its lowercase
        equivalent using the casing rules of the invariant culture.
        """
    
    @overload
    def ToString(self) -> String:
        """Converts the value of this instance to its equivalent string representation."""
    
    @staticmethod
    @overload
    def ToString(c: CharType) -> String:
        """Converts the specified Unicode character to its equivalent string representation."""
    
    @overload
    def ToString(self, provider: Optional[IFormatProvider]) -> String:
        """Converts the value of this instance to its equivalent string
        representation using the specified culture-specific format
        information.
        """
    
    @staticmethod
    @overload
    def ToUpper(c: CharType) -> Char:
        """Converts the value of a Unicode character to its uppercase equivalent."""
    
    @staticmethod
    @overload
    def ToUpper(c: CharType, culture: CultureInfo) -> Char:
        """Converts the value of a specified Unicode character to its
        uppercase equivalent using specified culture-specific formatting
        information.
        """
    
    @staticmethod
    def ToUpperInvariant(c: CharType) -> Char:
        """Converts the value of a Unicode character to its uppercase
        equivalent using the casing rules of the invariant culture.
        """
    
    @staticmethod
    def TryParse(s: Optional[StringType], result: Char) -> Boolean:
        """Converts the value of the specified string to its equivalent
        Unicode character. A return code indicates whether the conversion
        succeeded or failed.
        """


class ConsoleKeyInfo:
    """Describes the console key that was pressed, including the character represented by the console key and the state of the SHIFT, ALT, and CTRL modifier keys."""


class DateOnly:
    """Represents dates with values ranging from January 1, 0001 Anno Domini (Common Era) through December 31, 9999 A.D. (C.E.) in the Gregorian calendar."""


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


class Int32(int, ValueType, IComparable, IComparable[Int32], IConvertible, IEquatable[Int32], ISpanFormattable):
    """Represents a 32-bit signed integer."""


class Int64:
    """Represents a 64-bit signed integer."""


class IntPtr:
    """A platform-specific type that is used to represent a pointer or a handle."""


class Memory(Generic[T]):
    """Represents a contiguous region of memory."""


class MemoryExtensions.TryWriteInterpolatedStringHandler:
    """Provides a handler used by the language compiler to format interpolated strings into character spans."""


class ModuleHandle:
    """Represents a runtime handle for a module."""


class Nullable(Generic[T]):
    """Represents a value type that can be assigned null."""


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


class TimeZoneInfo.TransitionTime:
    """Provides information about a specific time change, such as the change from daylight saving time to standard time or vice versa, in a particular time zone."""


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


class ValueTuple:
    """Provides static methods for creating value tuples."""


class ValueTuple< T1 >:
    """Represents a value tuple with a single component."""


class ValueTuple< T1, T2 >:
    """Represents a value tuple with 2 components."""


# ValueTuple<T1,T2,T3>
# Represents a value tuple with 3 components.

class ValueTuple< T1, T2, T3, T4 >:
    """Represents a value tuple with 4 components."""


class ValueTuple< T1, T2, T3, T4, T5 >:
    """Represents a value tuple with 5 components."""


class ValueTuple< T1, T2, T3, T4, T5, T6 >:
    """Represents a value tuple with 6 components."""


class ValueTuple< T1, T2, T3, T4, T5, T6, T7 >:
    """Represents a value tuple with 7 components."""


class ValueTuple< T1, T2, T3, T4, T5, T6, T7, TRest >:
    """Represents an n-value tuple, where n is 8 or greater."""


class Void:
    """Specifies a return value type for a method that does not return a value."""


# ---------- INTERFACES #####


class IAsyncDisposable(ABC):
    """Provides a mechanism for releasing unmanaged resources asynchronously."""
    
    def DisposeAsync(self) -> ValueTask:
        """Performs application-defined tasks associated with freeing,
        releasing, or resetting unmanaged resources asynchronously.
        """
    
    def ConfigureAwait(self, source: IAsyncDisposable, continueOnCapturedContext: BooleanType) -> ConfiguredAsyncDisposable:
        """Configures how awaits on the tasks returned from an async disposable are performed."""


class IAsyncResult(ABC):
    """Represents the status of an asynchronous operation."""
    
    @property
    def AsyncState(self) -> Optional[Object]:
        """Gets a user-defined object that qualifies or contains information
        about an asynchronous operation.
        """
    
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """Gets a WaitHandle that is used to wait for an asynchronous
        operation to complete.
        """
    
    @property
    def CompletedSynchronously(self) -> Boolean:
        """Gets a value that indicates whether the asynchronous operation
        completed synchronously.
        """
    
    @property
    def IsCompleted(self) -> Boolean:
        """Gets a value that indicates whether the asynchronous operation
        has completed.
        """


class ICloneable(ABC):
    """Supports cloning, which creates a new instance of a class with the
    same value as an existing instance.
    """
    
    def Clone(self) -> Object:
        """Creates a new object that is a copy of the current instance."""


class IComparable(ABC, Generic[T]):
    """Defines a generalized type-specific comparison method that a value
    type or class implements to order or sort its instances.
    """
    
    @overload
    def CompareTo(self, obj: Optional[ObjectType]) -> Int32:
        """Compares the current instance with another object of the same type
        and returns an integer that indicates whether the current instance
        precedes, follows, or occurs in the same position in the sort order as
        the other object.
        """
    
    @overload
    def CompareTo(self, obj: Optional[T]) -> Int32:
        """Compares the current instance with another object of the same type and
        returns an integer that indicates whether the current instance precedes,
        follows, or occurs in the same position in the sort order as the other
        object.
        """


class IConvertible(ABC):
    """Defines methods that convert the value of the implementing reference or
    value type to a common language runtime type that has an equivalent value.
    """
    
    def GetTypeCode(self) -> TypeCode:
        """Returns the TypeCode for this instance."""
    
    def ToBoolean(self, provider: Optional[IFormatProvider]) -> Boolean:
        """Converts the value of this instance to an equivalent Boolean value
        using the specified culture-specific formatting information.
        """
    
    def ToByte(self, provider: Optional[IFormatProvider]) -> Byte:
        """Converts the value of this instance to an equivalent 8-bit unsigned
        integer using the specified culture-specific formatting information.
        """
    
    def ToChar(self, provider: Optional[IFormatProvider]) -> Char:
        """Converts the value of this instance to an equivalent Unicode character
        using the specified culture-specific formatting information.
        """
    
    def ToDateTime(self, provider: Optional[IFormatProvider]) -> DateTime:
        """Converts the value of this instance to an equivalent DateTime using the
        specified culture-specific formatting information.
        """
    
    def ToDecimal(self, provider: Optional[IFormatProvider]) -> Decimal:
        """Converts the value of this instance to an equivalent Decimal number using
        the specified culture-specific formatting information."""
    
    def ToDouble(self, provider: Optional[IFormatProvider]) -> Double:
        """Converts the value of this instance to an equivalent double-precision
        floating-point number using the specified culture-specific formatting
        information.
        """
    
    def ToInt16(self, provider: Optional[IFormatProvider]) -> Int16:
        """Converts the value of this instance to an equivalent 16-bit signed integer
        using the specified culture-specific formatting information.
        """
    
    def ToInt32(self, provider: Optional[IFormatProvider]) -> Int32:
        """Converts the value of this instance to an equivalent 32-bit signed integer
        using the specified culture-specific formatting information.
        """
    
    def ToInt64(self, provider: Optional[IFormatProvider]) -> Int64:
        """Converts the value of this instance to an equivalent 64-bit signed integer
        using the specified culture-specific formatting information.
        """
    
    def ToSByte(self, provider: Optional[IFormatProvider]) -> SByte:
        """Converts the value of this instance to an equivalent 8-bit signed integer
        using the specified culture-specific formatting information.
        """
    
    def ToSingle(self, provider: Optional[IFormatProvider]) -> Single:
        """Converts the value of this instance to an equivalent single-precision
        floating-point number using the specified culture-specific formatting
        information.
        """
    
    def ToString(self, provider: Optional[IFormatProvider]) -> String:
        """Converts the value of this instance to an equivalent String using the
        specified culture-specific formatting information.
        """
    
    def ToType(self, conversionType: Type, provider: Optional[IFormatProvider]) -> Object:
        """Converts the value of this instance to an Object of the specified Type that
        has an equivalent value, using the specified culture-specific formatting
        information.
        """
    
    def ToUInt16(self, provider: Optional[IFormatProvider]) -> UInt16:
        """Converts the value of this instance to an equivalent 16-bit unsigned integer
        using the specified culture-specific formatting information.
        """
    
    def ToUInt32(self, provider: Optional[IFormatProvider]) -> UInt32:
        """Converts the value of this instance to an equivalent 32-bit unsigned integer
        using the specified culture-specific formatting information.
        """
    
    def ToUInt64(self, provider: Optional[IFormatProvider]) -> UInt64:
        """Converts the value of this instance to an equivalent 64-bit unsigned integer
        using the specified culture-specific formatting information.
        """


class ICustomFormatter(ABC):
    """Defines a method that supports custom formatting of the value of an object."""
    
    def Format(self, format: Optional[StringType], arg: Optional[ObjectType], formatProvider: Optional[IFormatProvider]) -> String:
        """Converts the value of a specified object to an equivalent string
        representation using specified format and culture-specific formatting
        information.
        """


class IDisposable(ABC):
    """Provides a mechanism for releasing unmanaged resources."""
    
    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing,
        releasing, or resetting unmanaged resources.
        """


class IEquatable(ABC, Generic[T]):
    """Defines a generalized method that a value type or class implements to
    create a type-specific method for determining equality of instances.
    """
    
    def Equals(self, obj: Optional[T]) -> Boolean:
        """Indicates whether the current object is equal to another object of the same type."""


class IFormatProvider(ABC):
    """Provides a mechanism for retrieving an object to control formatting."""
    
    def GetFormat(self, formatType: Optional[Type]) -> Optional[Object]:
        """Returns an object that provides formatting services for the specified type."""


class IFormattable(ABC):
    """Provides functionality to format the value of an object into a string representation."""
    
    def ToString(self, format: Optional[StringType], formatProvider: Optional[IFormatProvider]) -> String:
        """Formats the value of the current instance using the specified format."""


class IObservable(ABC, Generic[T]):
    """Defines a provider for push-based notification."""
    
    def Subscribe(self, observer: IObserver[T]) -> IDisposable:
        """Notifies the provider that an observer is to receive notifications."""


class IObserver(ABC, Generic[T]):
    """Provides a mechanism for receiving push-based notifications."""
    
    def OnCompleted(self) -> None:
        """Notifies the observer that the provider has finished sending push-based notifications."""
    
    def OnError(self, error: Exception) -> None:
        """Notifies the observer that the provider has experienced an error condition."""
    
    def OnNext(self, value: T) -> None:
        """Provides the observer with new data."""


class IProgress(ABC, Generic[T]):
    """Defines a provider for progress updates."""
    
    def Report(self, value: T) -> None:
        """Reports a progress update."""


class IServiceProvider(ABC):
    """Defines a mechanism for retrieving a service object; that is, an
    object that provides custom support to other objects.
    """
    
    def GetService(self, serviceType: Type) -> Optional[Object]:
        """Gets the service object of the specified type."""


class ISpanFormattable(IFormattable, ABC):
    """Provides functionality to format the string representation of an object into a span."""
    
    def TryFormat(self, destination: Span[Char], charsWritten: Int32, format: ReadOnlySpan[Char], format: Optional[IFormatProvider]) -> Boolean:
        """Tries to format the value of the current instance into the provided span of characters."""

# ---------- ENUMS #####

# AttributeTargets
# Specifies the application elements on which it is valid to apply an attribute.
#
# Base64FormattingOptions
# Specifies whether relevant ToBase64CharArray and ToBase64String methods insert line breaks in their output.
#
# ConsoleColor
# Specifies constants that define foreground and background colors for the console.
#
# ConsoleKey
# Specifies the standard keys on a console.
#
# ConsoleModifiers
# Represents the SHIFT, ALT, and CTRL modifier keys on a keyboard.
#
# ConsoleSpecialKey
# Specifies combinations of modifier and console keys that can interrupt the current process.
#
# DateTimeKind
# Specifies whether a DateTime object represents a local time, a Coordinated Universal Time (UTC), or is not specified as either local time or UTC.
#
# DayOfWeek
# Specifies the day of the week.
#
# Environment.SpecialFolder
# Specifies enumerated constants used to retrieve directory paths to system special folders.
#
# Environment.SpecialFolderOption
# Specifies options to use for getting the path to a special folder.
#
# EnvironmentVariableTarget
# Specifies the location where an environment variable is stored or retrieved in a set or get operation.
#
# GCCollectionMode
# Specifies the behavior for a forced garbage collection.
#
# GCKind
# Specifies the kind of a garbage collection.
#
# GCNotificationStatus
# Provides information about the current registration for notification of the next full garbage collection.
#
# GenericUriParserOptions
# Specifies options for a UriParser.
#
# LoaderOptimization
# An enumeration used with the LoaderOptimizationAttribute class to specify loader optimizations for an executable.
#
# MidpointRounding
# Specifies the strategy that mathematical rounding methods should use to round a number.
#
# PlatformID
# Identifies the operating system, or platform, supported by an assembly.
#
# StringComparison
# Specifies the culture, case, and sort rules to be used by certain overloads of the Compare(String, String) and Equals(Object) methods.
#
# StringSplitOptions
# Specifies options for applicable Split method overloads, such as whether to omit empty substrings from the returned array or trim whitespace from substrings.
#
# TypeCode
# Specifies the type of an object.
#
# UriComponents
# Specifies the parts of a Uri.
#
# UriFormat
# Controls how URI information is escaped.
#
# UriHostNameType
# Defines host name types for the CheckHostName(String) method.
#
# UriKind
# Defines the different kinds of URIs.
#
# UriPartial
# Defines the parts of a URI for the GetLeftPart(UriPartial) method.


# ---------- DELEGATES #####


# Action
# Encapsulates a method that has no parameters and does not return a value.
#
# Action[T]
# Encapsulates a method that has a single parameter and does not return a value.
#
# Action<T1,T2>
# Encapsulates a method that has two parameters and does not return a value.
#
# Action<T1,T2,T3>
# Encapsulates a method that has three parameters and does not return a value.
#
# Action<T1,T2,T3,T4>
# Encapsulates a method that has four parameters and does not return a value.
#
# Action<T1,T2,T3,T4,T5>
# Encapsulates a method that has five parameters and does not return a value.
#
# Action<T1,T2,T3,T4,T5,T6>
# Encapsulates a method that has six parameters and does not return a value.
#
# Action<T1,T2,T3,T4,T5,T6,T7>
# Encapsulates a method that has seven parameters and does not return a value.
#
# Action<T1,T2,T3,T4,T5,T6,T7,T8>
# Encapsulates a method that has eight parameters and does not return a value.
#
# Action<T1,T2,T3,T4,T5,T6,T7,T8,T9>
# Encapsulates a method that has nine parameters and does not return a value.
#
# Action<T1,T2,T3,T4,T5,T6,T7,T8,T9,T10>
# Encapsulates a method that has 10 parameters and does not return a value.
#
# Action<T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11>
# Encapsulates a method that has 11 parameters and does not return a value.
#
# Action<T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12>
# Encapsulates a method that has 12 parameters and does not return a value.
#
# Action<T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13>
# Encapsulates a method that has 13 parameters and does not return a value.
#
# Action<T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14>
# Encapsulates a method that has 14 parameters and does not return a value.
#
# Action<T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15>
# Encapsulates a method that has 15 parameters and does not return a value.
#
# Action<T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16>
# Encapsulates a method that has 16 parameters and does not return a value.
#
# AssemblyLoadEventHandler
# Represents the method that handles the AssemblyLoad event of an AppDomain.
#
# AsyncCallback
# References a method to be called when a corresponding asynchronous operation completes.
#
# Comparison[T]
# Represents the method that compares two objects of the same type.
#
# ConsoleCancelEventHandler
# Represents the method that will handle the CancelKeyPress event of a Console.
#
# Converter<TInput,TOutput>
# Represents a method that converts an object from one type to another type.

class EventHandler:
    """Represents the method that will handle an event that has no event data."""

class EventHandler<TEventArgs>:
    """Represents the method that will handle an event when the event provides data."""

# Func<TResult>
# Encapsulates a method that has no parameters and returns a value of the type specified by the TResult parameter.
#
# Func<T,TResult>
# Encapsulates a method that has one parameter and returns a value of the type specified by the TResult parameter.
#
# Func<T1,T2,TResult>
# Encapsulates a method that has two parameters and returns a value of the type specified by the TResult parameter.
#
# Func<T1,T2,T3,TResult>
# Encapsulates a method that has three parameters and returns a value of the type specified by the TResult parameter.
#
# Func<T1,T2,T3,T4,TResult>
# Encapsulates a method that has four parameters and returns a value of the type specified by the TResult parameter.
#
# Func<T1,T2,T3,T4,T5,TResult>
# Encapsulates a method that has five parameters and returns a value of the type specified by the TResult parameter.
#
# Func<T1,T2,T3,T4,T5,T6,TResult>
# Encapsulates a method that has six parameters and returns a value of the type specified by the TResult parameter.
#
# Func<T1,T2,T3,T4,T5,T6,T7,TResult>
# Encapsulates a method that has seven parameters and returns a value of the type specified by the TResult parameter.
#
# Func<T1,T2,T3,T4,T5,T6,T7,T8,TResult>
# Encapsulates a method that has eight parameters and returns a value of the type specified by the TResult parameter.
#
# Func<T1,T2,T3,T4,T5,T6,T7,T8,T9,TResult>
# Encapsulates a method that has nine parameters and returns a value of the type specified by the TResult parameter.
#
# Func<T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,TResult>
# Encapsulates a method that has 10 parameters and returns a value of the type specified by the TResult parameter.
#
# Func<T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,TResult>
# Encapsulates a method that has 11 parameters and returns a value of the type specified by the TResult parameter.
#
# Func<T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,TResult>
# Encapsulates a method that has 12 parameters and returns a value of the type specified by the TResult parameter.
#
# Func<T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,TResult>
# Encapsulates a method that has 13 parameters and returns a value of the type specified by the TResult parameter.
#
# Func<T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,TResult>
# Encapsulates a method that has 14 parameters and returns a value of the type specified by the TResult parameter.
#
# Func<T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,TResult>
# Encapsulates a method that has 15 parameters and returns a value of the type specified by the TResult parameter.
#
# Func<T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,TResult>
# Encapsulates a method that has 16 parameters and returns a value of the type specified by the TResult parameter.
#
# Predicate[T]
# Represents the method that defines a set of criteria and determines whether the specified object meets those criteria.
#
# ResolveEventHandler
# Represents a method that handles the TypeResolve, ResourceResolve, or AssemblyResolve event of an AppDomain.
#
# UnhandledExceptionEventHandler
# Represents the method that will handle the event raised by an exception that is not handled by the application domain.
