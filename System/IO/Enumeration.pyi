__all__ = [
    'FileSystemEnumerable',
    'FileSystemEnumerator',
    'FileSystemName',
    'FileSystemEntry',
]

from typing import TypeVar, Generic

TResult = TypeVar('TResult')


# TODO

# ---------- CLASSES ---------- #

class FileSystemEnumerable(Generic[TResult]):
    """Allows utilizing custom filter predicates and transform delegates for enumeration purposes."""
    
    # ---------- DELEGATES ---------- #
    
    class FindPredicate:
        """Encapsulates a method for filtering out find results."""
    
    class FindTransform:
        """Encapsulates a method for transforming raw find data into a result."""


class FileSystemEnumerator(Generic[TResult]):
    """Enumerates the file system elements of the provided type that are being searched and filtered by a FileSystemEnumerable<TResult>."""


class FileSystemName:
    """Provides methods for matching file system names."""


# ---------- STRUCTS ---------- #

class FileSystemEntry:
    """Provides a lower level view of FileSystemInfo to help process and filter find results."""
