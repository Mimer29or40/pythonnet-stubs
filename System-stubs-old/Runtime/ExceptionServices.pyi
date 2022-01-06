__all__ = [
    'ExceptionDispatchInfo',
    'FirstChanceExceptionEventArgs',
    'HandleProcessCorruptedStateExceptionsAttribute',
]


# TODO

# ---------- CLASSES ---------- #

class ExceptionDispatchInfo:
    """Represents an exception whose state is captured at a certain point in code."""


class FirstChanceExceptionEventArgs:
    """Provides data for the notification event that is raised when a managed exception first occurs, before the common language runtime begins searching for event handlers."""


class HandleProcessCorruptedStateExceptionsAttribute:
    """Enables managed code to handle exceptions that indicate a corrupted process state."""
