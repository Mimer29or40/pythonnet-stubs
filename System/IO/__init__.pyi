__all__ = [
    'BinaryReader',
    'BinaryWriter',
    'BufferedStream',
    'Directory',
    'DirectoryInfo',
    'DirectoryNotFoundException',
    'DriveInfo',
    'DriveNotFoundException',
    'EndOfStreamException',
    'EnumerationOptions',
    'ErrorEventArgs',
    'File',
    'FileInfo',
    'FileLoadException',
    'FileNotFoundException',
    'FileStream',
    'FileStreamOptions',
    'FileSystemAclExtensions',
    'FileSystemEventArgs',
    'FileSystemInfo',
    'FileSystemWatcher',
    'InternalBufferOverflowException',
    'InvalidDataException',
    'IOException',
    'MemoryStream',
    'Path',
    'PathTooLongException',
    'RandomAccess',
    'RenamedEventArgs',
    'Stream',
    'StreamReader',
    'StreamWriter',
    'StringReader',
    'StringWriter',
    'TextReader',
    'TextWriter',
    'UnmanagedMemoryAccessor',
    'UnmanagedMemoryStream',
    'WaitForChangedResult',
    'DriveType',
    'FileAccess',
    'FileAttributes',
    'FileMode',
    'FileOptions',
    'FileShare',
    'HandleInheritability',
    'MatchCasing',
    'MatchType',
    'NotifyFilters',
    'SearchOption',
    'SeekOrigin',
    'WatcherChangeTypes',
    'ErrorEventHandler',
    'FileSystemEventHandler',
    'RenamedEventHandler',
]


# TODO

# ---------- CLASSES ---------- #

class BinaryReader:
    """Reads primitive data types as binary values in a specific encoding."""


class BinaryWriter:
    """Writes primitive types in binary to a stream and supports writing strings in a specific encoding."""


class BufferedStream:
    """Adds a buffering layer to read and write operations on another stream. This class cannot be inherited."""


class Directory:
    """Exposes static methods for creating, moving, and enumerating through directories and subdirectories. This class cannot be inherited."""


class DirectoryInfo:
    """Exposes instance methods for creating, moving, and enumerating through directories and subdirectories. This class cannot be inherited."""


class DirectoryNotFoundException:
    """The exception that is thrown when part of a file or directory cannot be found."""


class DriveInfo:
    """Provides access to information on a drive."""


class DriveNotFoundException:
    """The exception that is thrown when trying to access a drive or share that is not available."""


class EndOfStreamException:
    """The exception that is thrown when reading is attempted past the end of a stream."""


class EnumerationOptions:
    """Provides file and directory enumeration options."""


class ErrorEventArgs:
    """Provides data for the Error event."""


class File:
    """Provides static methods for the creation, copying, deletion, moving, and opening of a single file, and aids in the creation of FileStream objects."""


class FileInfo:
    """Provides properties and instance methods for the creation, copying, deletion, moving, and opening of files, and aids in the creation of FileStream objects. This class cannot be inherited."""


class FileLoadException:
    """The exception that is thrown when a managed assembly is found but cannot be loaded."""


class FileNotFoundException:
    """The exception that is thrown when an attempt to access a file that does not exist on disk fails."""


class FileStream:
    """Provides a Stream for a file, supporting both synchronous and asynchronous read and write operations."""


class FileStreamOptions:
    """Defines a variety of configuration options for FileStream."""


class FileSystemAclExtensions:
    """Provides Windows-specific static extension methods for manipulating Access Control List (ACL) security attributes for files and directories."""


class FileSystemEventArgs:
    """Provides data for the directory events: Changed, Created, Deleted."""


class FileSystemInfo:
    """Provides the base class for both FileInfo and DirectoryInfo objects."""


class FileSystemWatcher:
    """Listens to the file system change notifications and raises events when a directory, or file in a directory, changes."""


class InternalBufferOverflowException:
    """The exception thrown when the internal buffer overflows."""


class InvalidDataException:
    """The exception that is thrown when a data stream is in an invalid format."""


class IOException:
    """The exception that is thrown when an I/O error occurs."""


class MemoryStream:
    """Creates a stream whose backing store is memory."""


class Path:
    """Performs operations on String instances that contain file or directory path information. These operations are performed in a cross-platform manner."""


class PathTooLongException:
    """The exception that is thrown when a path or fully qualified file name is longer than the system-defined maximum length."""


class RandomAccess:
    """Provides offset-based APIs for reading and writing files in a thread-safe manner."""


class RenamedEventArgs:
    """Provides data for the Renamed event."""


class Stream:
    """Provides a generic view of a sequence of bytes. This is an abstract class."""


class StreamReader:
    """Implements a TextReader that reads characters from a byte stream in a particular encoding."""


class StreamWriter:
    """Implements a TextWriter for writing characters to a stream in a particular encoding."""


class StringReader:
    """Implements a TextReader that reads from a string."""


class StringWriter:
    """Implements a TextWriter for writing information to a string. The information is stored in an underlying StringBuilder."""


class TextReader:
    """Represents a reader that can read a sequential series of characters."""


class TextWriter:
    """Represents a writer that can write a sequential series of characters. This class is abstract."""


class UnmanagedMemoryAccessor:
    """Provides random access to unmanaged blocks of memory from managed code."""


class UnmanagedMemoryStream:
    """Provides access to unmanaged blocks of memory from managed code."""


# ---------- STRUCTS ---------- #

class WaitForChangedResult:
    """Contains information on the change that occurred."""


# ---------- ENUMS ---------- #

class DriveType:
    """Defines constants for drive types, including CDRom, Fixed, Network, NoRootDirectory, Ram, Removable, and Unknown."""


class FileAccess:
    """Defines constants for read, write, or read/write access to a file."""


class FileAttributes:
    """Provides attributes for files and directories."""


class FileMode:
    """Specifies how the operating system should open a file."""


class FileOptions:
    """Represents advanced options for creating a FileStream object."""


class FileShare:
    """Contains constants for controlling the kind of access other FileStream objects can have to the same file."""


class HandleInheritability:
    """Specifies whether the underlying handle is inheritable by child processes."""


class MatchCasing:
    """Specifies the type of character casing to match."""


class MatchType:
    """Specifies the type of wildcard matching to use."""


class NotifyFilters:
    """Specifies changes to watch for in a file or folder."""


class SearchOption:
    """Specifies whether to search the current directory, or the current directory and all subdirectories."""


class SeekOrigin:
    """Specifies the position in a stream to use for seeking."""


class WatcherChangeTypes:
    """Changes that might occur to a file or directory."""


# ---------- DELEGATES ---------- #

class ErrorEventHandler:
    """Represents the method that will handle the Error event of a FileSystemWatcher object."""


class FileSystemEventHandler:
    """Represents the method that will handle the Changed, Created, or Deleted event of a FileSystemWatcher class."""


class RenamedEventHandler:
    """Represents the method that will handle the Renamed event of a FileSystemWatcher class."""
