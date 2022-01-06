__all__ = [
    'ManualResetValueTaskSourceCore',
    'IValueTaskSource',
    'IValueTaskSource',
    'ValueTaskSourceOnCompletedFlags',
    'ValueTaskSourceStatus',
]

from typing import TypeVar, Generic

TResult = TypeVar('TResult')


# TODO

# ---------- STRUCTS ---------- #

class ManualResetValueTaskSourceCore(Generic[TResult]):
    """Provides the core logic for implementing a manual-reset IValueTaskSource or IValueTaskSource<TResult>."""


# ---------- INTERFACES ---------- #

class IValueTaskSource:
    """Represents an object that can be wrapped by a ValueTask."""


class IValueTaskSource(Generic[TResult]):
    """Represents an object that can be wrapped by a ValueTask<TResult>."""


# ---------- ENUMS ---------- #

class ValueTaskSourceOnCompletedFlags:
    """Provides flags passed from ValueTask and ValueTask<TResult> to the OnCompleted method to control the behavior of a continuation."""


class ValueTaskSourceStatus:
    """Indicates the status of an IValueTaskSource or IValueTaskSource<TResult>."""
