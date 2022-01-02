__all__ = [
    'Capture',
    'CaptureCollection',
    'Group',
    'GroupCollection',
    'Match',
    'MatchCollection',
    'Regex',
    'RegexCompilationInfo',
    'RegexMatchTimeoutException',
    'RegexParseException',
    'RegexRunner',
    'RegexRunnerFactory',
    'RegexOptions',
    'RegexParseError',
    'MatchEvaluator',
]


# TODO

# ---------- CLASSES ---------- #

class Capture:
    """Represents the results from a single successful subexpression capture."""


class CaptureCollection:
    """Represents the set of captures made by a single capturing group. The collection is immutable (read-only) and has no public constructor."""


class Group:
    """Represents the results from a single capturing group."""


class GroupCollection:
    """Returns the set of captured groups in a single match. The collection is immutable (read-only) and has no public constructor."""


class Match:
    """Represents the results from a single regular expression match."""


class MatchCollection:
    """Represents the set of successful matches found by iteratively applying a regular expression pattern to the input string. The collection is immutable (read-only) and has no public constructor. The Matches(String) method returns a MatchCollection object."""


class Regex:
    """Represents an immutable regular expression."""


class RegexCompilationInfo:
    """Provides information about a regular expression that is used to compile a regular expression to a stand-alone assembly."""


class RegexMatchTimeoutException:
    """The exception that is thrown when the execution time of a regular expression pattern-matching method exceeds its time-out interval."""


class RegexParseException:
    """An exception as a result of a parse error in a regular expression, with detailed information in the Error and Offset properties."""


class RegexRunner:
    """The RegexRunner class is the base class for compiled regular expressions."""


class RegexRunnerFactory:
    """Creates a RegexRunner class for a compiled regular expression."""


# ---------- ENUMS ---------- #

class RegexOptions:
    """Provides enumerated values to use to set regular expression options."""


class RegexParseError:
    """Specifies the detailed underlying reason why a RegexParseException is thrown when a regular expression contains a parsing error."""


# ---------- DELEGATES ---------- #

class MatchEvaluator:
    """Represents the method that is called each time a regular expression match is found during a Replace method operation."""
