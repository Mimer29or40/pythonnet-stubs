__all__ = [
    'SqlAlreadyFilledException',
    'SqlBytes',
    'SqlChars',
    'SqlNotFilledException',
    'SqlNullValueException',
    'SqlTruncateException',
    'SqlTypeException',
    'SqlXml',
    'SqlBinary',
    'SqlBoolean',
    'SqlByte',
    'SqlDateTime',
    'SqlDecimal',
    'SqlDouble',
    'SqlGuid',
    'SqlInt16',
    'SqlInt32',
    'SqlInt64',
    'SqlMoney',
    'SqlSingle',
    'SqlString',
    'INullable',
    'SqlCompareOptions',
    'StorageState',
]


# TODO

# ---------- CLASSES ---------- #

class SqlAlreadyFilledException:
    """The SqlAlreadyFilledException class is not intended for use as a stand-alone component, but as a class from which other classes derive standard functionality."""


class SqlBytes:
    """Represents a mutable reference type that wraps either a Buffer or a Stream."""


class SqlChars:
    """SqlChars is a mutable reference type that wraps a Char array or a SqlString instance."""


class SqlNotFilledException:
    """The SqlNotFilledException class is not intended for use as a stand-alone component, but as a class from which other classes derive standard functionality."""


class SqlNullValueException:
    """The exception that is thrown when the Value property of a System.Data.SqlTypes structure is set to null."""


class SqlTruncateException:
    """The exception that is thrown when you set a value into a System.Data.SqlTypes structure would truncate that value."""


class SqlTypeException:
    """The base exception class for the System.Data.SqlTypes."""


class SqlXml:
    """Represents XML data stored in or retrieved from a server."""


# ---------- STRUCTS ---------- #

class SqlBinary:
    """Represents a variable-length stream of binary data to be stored in or retrieved from a database."""


class SqlBoolean:
    """Represents an integer value that is either 1 or 0 to be stored in or retrieved from a database."""


class SqlByte:
    """Represents an 8-bit unsigned integer, in the range of 0 through 255, to be stored in or retrieved from a database."""


class SqlDateTime:
    """Represents the date and time data ranging in value from January 1, 1753 to December 31, 9999 to an accuracy of 3.33 milliseconds to be stored in or retrieved from a database. The SqlDateTime structure has a different underlying data structure from its corresponding .NET type, DateTime, which can represent any time between 12:00:00 AM 1/1/0001 and 11:59:59 PM 12/31/9999, to the accuracy of 100 nanoseconds. SqlDateTime actually stores the relative difference to 00:00:00 AM 1/1/1900. Therefore, a conversion from "00:00:00 AM 1/1/1900" to an integer will return 0."""


class SqlDecimal:
    """Represents a numeric value between - 10^38 +1 and 10^38 - 1, with fixed precision and scale."""


class SqlDouble:
    """Represents a floating-point number within the range of -1.79E +308 through 1.79E +308 to be stored in or retrieved from a database."""


class SqlGuid:
    """Represents a GUID to be stored in or retrieved from a database."""


class SqlInt16:
    """Represents a 16-bit signed integer to be stored in or retrieved from a database."""


class SqlInt32:
    """Represents a 32-bit signed integer to be stored in or retrieved from a database."""


class SqlInt64:
    """Represents a 64-bit signed integer to be stored in or retrieved from a database."""


class SqlMoney:
    """Represents a currency value ranging from -2 63 (or -922,337,203,685,477.5808) to 2 63 -1 (or +922,337,203,685,477.5807) with an accuracy to a ten-thousandth of currency unit to be stored in or retrieved from a database."""


class SqlSingle:
    """Represents a floating point number within the range of -3.40E +38 through 3.40E +38 to be stored in or retrieved from a database."""


class SqlString:
    """Represents a variable-length stream of characters to be stored in or retrieved from the database. SqlString has a different underlying data structure from its corresponding .NET String data type."""


# ---------- INTERFACES ---------- #

class INullable:
    """All the System.Data.SqlTypes objects and structures implement the INullable interface."""


# ---------- ENUMS ---------- #

class SqlCompareOptions:
    """Specifies the compare option values for a SqlString structure."""


class StorageState:
    """The StorageState enumeration is not intended for use as a stand-alone component, but as an enumeration from which other classes derive standard functionality."""
