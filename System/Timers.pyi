__all__ = [
    'ElapsedEventArgs',
    'Timer',
    'TimersDescriptionAttribute',
    'ElapsedEventHandler',
]


# TODO

# ---------- CLASSES ---------- #

class ElapsedEventArgs:
    """Provides data for the Elapsed event."""


class Timer:
    """Generates an event after a set interval, with an option to generate recurring events."""


class TimersDescriptionAttribute:
    """Sets the description that visual designers can display when referencing an event, extender, or property."""


# ---------- DELEGATES ---------- #

class ElapsedEventHandler:
    """Represents the method that will handle the Elapsed event of a Timer."""
