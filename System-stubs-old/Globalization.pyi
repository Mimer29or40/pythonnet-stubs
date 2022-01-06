__all__ = [
    'Calendar',
    'CharUnicodeInfo',
    'ChineseLunisolarCalendar',
    'CompareInfo',
    'CultureInfo',
    'CultureNotFoundException',
    'DateTimeFormatInfo',
    'DaylightTime',
    'EastAsianLunisolarCalendar',
    'GlobalizationExtensions',
    'GregorianCalendar',
    'HebrewCalendar',
    'HijriCalendar',
    'IdnMapping',
    'ISOWeek',
    'JapaneseCalendar',
    'JapaneseLunisolarCalendar',
    'JulianCalendar',
    'KoreanCalendar',
    'KoreanLunisolarCalendar',
    'NumberFormatInfo',
    'PersianCalendar',
    'RegionInfo',
    'SortKey',
    'SortVersion',
    'StringInfo',
    'TaiwanCalendar',
    'TaiwanLunisolarCalendar',
    'TextElementEnumerator',
    'TextInfo',
    'ThaiBuddhistCalendar',
    'UmAlQuraCalendar',
    'CalendarAlgorithmType',
    'CalendarWeekRule',
    'CompareOptions',
    'CultureTypes',
    'DateTimeStyles',
    'DigitShapes',
    'GregorianCalendarTypes',
    'NumberStyles',
    'TimeSpanStyles',
    'UnicodeCategory',
]


# TODO

# ---------- CLASSES ---------- #

class Calendar:
    """Represents time in divisions, such as weeks, months, and years."""


class CharUnicodeInfo:
    """Retrieves information about a Unicode character. This class cannot be inherited."""


class ChineseLunisolarCalendar:
    """Represents time in divisions, such as months, days, and years. Years are calculated using the Chinese calendar, while days and months are calculated using the lunisolar calendar."""


class CompareInfo:
    """Implements a set of methods for culture-sensitive string comparisons."""


class CultureInfo:
    """Provides information about a specific culture (called a locale for unmanaged code development). The information includes the names for the culture, the writing system, the calendar used, the sort order of strings, and formatting for dates and numbers."""


class CultureNotFoundException:
    """The exception that is thrown when a method attempts to construct a culture that is not available."""


class DateTimeFormatInfo:
    """Provides culture-specific information about the format of date and time values."""


class DaylightTime:
    """Defines the period of daylight saving time."""


class EastAsianLunisolarCalendar:
    """Represents a calendar that divides time into months, days, years, and eras, and has dates that are based on cycles of the sun and the moon."""


class GlobalizationExtensions:
    """Provides globalization-related extension methods."""


class GregorianCalendar:
    """Represents the Gregorian calendar."""


class HebrewCalendar:
    """Represents the Hebrew calendar."""


class HijriCalendar:
    """Represents the Hijri calendar."""


class IdnMapping:
    """Supports the use of non-ASCII characters for Internet domain names. This class cannot be inherited."""


class ISOWeek:
    """Provides static members to support the ISO week date that is part of the ISO 8601 date and time standard issued by the International Organization for Standardization (ISO)."""


class JapaneseCalendar:
    """Represents the Japanese calendar."""


class JapaneseLunisolarCalendar:
    """Represents time in divisions, such as months, days, and years. Years are calculated as for the Japanese calendar, while days and months are calculated using the lunisolar calendar."""


class JulianCalendar:
    """Represents the Julian calendar."""


class KoreanCalendar:
    """Represents the Korean calendar."""


class KoreanLunisolarCalendar:
    """Represents time in divisions, such as months, days, and years. Years are calculated using the Gregorian calendar, while days and months are calculated using the lunisolar calendar."""


class NumberFormatInfo:
    """Provides culture-specific information for formatting and parsing numeric values."""


class PersianCalendar:
    """Represents the Persian calendar."""


class RegionInfo:
    """Contains information about the country/region."""


class SortKey:
    """Represents the result of mapping a string to its sort key."""


class SortVersion:
    """Provides information about the version of Unicode used to compare and order strings."""


class StringInfo:
    """Provides functionality to split a string into text elements and to iterate through those text elements."""


class TaiwanCalendar:
    """the Taiwan calendar."""


class TaiwanLunisolarCalendar:
    """Represents the Taiwan lunisolar calendar. As for the Taiwan calendar, years are calculated using the Gregorian calendar, while days and months are calculated using the lunisolar calendar."""


class TextElementEnumerator:
    """Enumerates the text elements of a string."""


class TextInfo:
    """Defines text properties and behaviors, such as casing, that are specific to a writing system."""


class ThaiBuddhistCalendar:
    """Represents the Thai Buddhist calendar."""


class UmAlQuraCalendar:
    """Represents the Saudi Hijri (Um Al Qura) calendar."""


# ---------- ENUMS ---------- #

class CalendarAlgorithmType:
    """Specifies whether a calendar is solar-based, lunar-based, or lunisolar-based."""


class CalendarWeekRule:
    """Defines different rules for determining the first week of the year."""


class CompareOptions:
    """Defines the string comparison options to use with CompareInfo."""


class CultureTypes:
    """Defines the types of culture lists that can be retrieved using the GetCultures(CultureTypes) method."""


class DateTimeStyles:
    """Defines the formatting options that customize string parsing for some date and time parsing methods."""


class DigitShapes:
    """Specifies the culture-specific display of digits."""


class GregorianCalendarTypes:
    """Defines the different language versions of the Gregorian calendar."""


class NumberStyles:
    """Determines the styles permitted in numeric string arguments that are passed to the Parse and TryParse methods of the integral and floating-point numeric types."""


class TimeSpanStyles:
    """Defines the formatting options that customize string parsing for the ParseExact and TryParseExact methods."""


class UnicodeCategory:
    """Defines the Unicode category of a character."""
