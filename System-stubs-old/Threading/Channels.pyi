__all__ = [
    'BoundedChannelOptions',
    'Channel',
    'Channel',
    'Channel',
    'ChannelClosedException',
    'ChannelOptions',
    'ChannelReader',
    'ChannelWriter',
    'UnboundedChannelOptions',
    'BoundedChannelFullMode',
]

from typing import TypeVar, Generic

T = TypeVar('T')
TWrite = TypeVar('TWrite')
TRead = TypeVar('TRead')


# TODO

# ---------- CLASSES ---------- #

class BoundedChannelOptions:
    """Provides options that control the behavior of bounded Channel<T> instances."""


class Channel:
    """Provides static methods for creating channels."""


class Channel(Generic[T]):
    """Provides a base class for channels that support reading and writing elements of type T."""


class Channel(Generic[TWrite, TRead]):
    """Provides a base class for channels that support reading elements of type TRead and writing elements of type TWrite."""


class ChannelClosedException:
    """Exception thrown when a channel is used after it's been closed."""


class ChannelOptions:
    """Provides options that control the behavior of channel instances."""


class ChannelReader(Generic[T]):
    """Provides a base class for reading from a channel."""


class ChannelWriter(Generic[T]):
    """Provides a base class for writing to a channel."""


class UnboundedChannelOptions:
    """Provides options that control the behavior of unbounded Channel<T> instances."""


# ---------- ENUMS ---------- #

class BoundedChannelFullMode:
    """Specifies the behavior to use when writing to a bounded channel that is already full."""
