__all__ = [
    'AnonymousPipeClientStream',
    'AnonymousPipeServerStream',
    'AnonymousPipeServerStreamAcl',
    'NamedPipeClientStream',
    'NamedPipeServerStream',
    'NamedPipeServerStreamAcl',
    'PipeAccessRule',
    'PipeAuditRule',
    'PipesAclExtensions',
    'PipeSecurity',
    'PipeStream',
    'PipeAccessRights',
    'PipeDirection',
    'PipeOptions',
    'PipeTransmissionMode',
    'PipeStreamImpersonationWorker',
]


# TODO

# ---------- CLASSES ---------- #

class AnonymousPipeClientStream:
    """Exposes the client side of an anonymous pipe stream, which supports both synchronous and asynchronous read and write operations."""


class AnonymousPipeServerStream:
    """Exposes a stream around an anonymous pipe, which supports both synchronous and asynchronous read and write operations."""


class AnonymousPipeServerStreamAcl:
    """Provides security related APIs for the <see. cref="T:System.IO.Pipes.AnonymousPipeServerStream"></see.> class."""


class NamedPipeClientStream:
    """Exposes a Stream around a named pipe, which supports both synchronous and asynchronous read and write operations."""


class NamedPipeServerStream:
    """Exposes a Stream around a named pipe, supporting both synchronous and asynchronous read and write operations."""


class NamedPipeServerStreamAcl:
    """Provides security related APIs for the <see. cref="T:System.IO.Pipes.NamedPipeServerStream"></see.> class."""


class PipeAccessRule:
    """Represents an abstraction of an access control entry (ACE) that defines an access rule for a pipe."""


class PipeAuditRule:
    """Represents an abstraction of an access control entry (ACE) that defines an audit rule for a pipe."""


class PipesAclExtensions:
    """Provides Windows-specific static extension methods for manipulating Access Control List (ACL) security attributes for pipe streams."""


class PipeSecurity:
    """Represents the access control and audit security for a pipe."""


class PipeStream:
    """Exposes a Stream object around a pipe, which supports both anonymous and named pipes."""


# ---------- ENUMS ---------- #

class PipeAccessRights:
    """Defines the access rights to use when you create access and audit rules."""


class PipeDirection:
    """Specifies the direction of the pipe."""


class PipeOptions:
    """Provides options for creating a PipeStream object. This enumeration has a FlagsAttribute attribute that allows a bitwise combination of its member values."""


class PipeTransmissionMode:
    """Specifies the transmission mode of the pipe."""


# ---------- DELEGATES ---------- #

class PipeStreamImpersonationWorker:
    """Represents the method to call as the client."""
