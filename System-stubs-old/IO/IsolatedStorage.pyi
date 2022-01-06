__all__ = [
    'IsolatedStorage',
    'IsolatedStorageException',
    'IsolatedStorageFile',
    'IsolatedStorageFileStream',
    'INormalizeForIsolatedStorage',
    'IsolatedStorageScope',
]
# TODO

# ---------- CLASSES ---------- #

class IsolatedStorage:
    """Represents the abstract base class from which all isolated storage implementations must derive."""

class IsolatedStorageException:
    """The exception that is thrown when an operation in isolated storage fails."""

class IsolatedStorageFile:
    """Represents an isolated storage area containing files and directories."""

class IsolatedStorageFileStream:
    """Exposes a file within isolated storage."""


# ---------- INTERFACES ---------- #

class INormalizeForIsolatedStorage:
    """Enables comparisons between an isolated store and an application domain and assembly's evidence."""


# ---------- ENUMS ---------- #

class IsolatedStorageScope:
    """Enumerates the levels of isolated storage scope that are supported by IsolatedStorage."""
