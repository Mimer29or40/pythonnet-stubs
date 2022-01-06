__all__ = [
    'MemoryMappedFile',
    'MemoryMappedViewAccessor',
    'MemoryMappedViewStream',
    'MemoryMappedFileAccess',
    'MemoryMappedFileOptions',
    'MemoryMappedFileRights',
]


# TODO

# ---------- CLASSES ---------- #

class MemoryMappedFile:
    """Represents a memory-mapped file."""


class MemoryMappedViewAccessor:
    """Represents a randomly accessed view of a memory-mapped file."""


class MemoryMappedViewStream:
    """Represents a view of a memory-mapped file as a sequentially accessed stream."""


# ---------- ENUMS ---------- #

class MemoryMappedFileAccess:
    """Specifies access capabilities and restrictions for a memory-mapped file or view."""


class MemoryMappedFileOptions:
    """Provides memory allocation options for memory-mapped files."""


class MemoryMappedFileRights:
    """Specifies access rights to a memory-mapped file that is not associated with a file on disk."""
