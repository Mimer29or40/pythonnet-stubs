"""Automatically generated stubs for C# namespace: System.Globalization."""

from abc import ABC
from typing import ClassVar
from typing import overload

from System import ArgumentException
from System import Array
from System import Char
from System import DateTime
from System import DayOfWeek
from System import Enum
from System import Exception
from System import Guid
from System import ICloneable
from System import IEquatable
from System import IFormatProvider
from System import Object
from System import StringComparer
from System import TimeSpan
from System import Type
from System import ValueType
from System.Collections import IDictionary
from System.Collections import IEnumerator
from System.Reflection import Assembly
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import IDeserializationCallback
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AppDomainSortingSetupInfo(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class BidiCategory(Enum):
    """"""

    LeftToRight: BidiCategory = ...
    """"""
    LeftToRightEmbedding: BidiCategory = ...
    """"""
    LeftToRightOverride: BidiCategory = ...
    """"""
    RightToLeft: BidiCategory = ...
    """"""
    RightToLeftArabic: BidiCategory = ...
    """"""
    RightToLeftEmbedding: BidiCategory = ...
    """"""
    RightToLeftOverride: BidiCategory = ...
    """"""
    PopDirectionalFormat: BidiCategory = ...
    """"""
    EuropeanNumber: BidiCategory = ...
    """"""
    EuropeanNumberSeparator: BidiCategory = ...
    """"""
    EuropeanNumberTerminator: BidiCategory = ...
    """"""
    ArabicNumber: BidiCategory = ...
    """"""
    CommonNumberSeparator: BidiCategory = ...
    """"""
    NonSpacingMark: BidiCategory = ...
    """"""
    BoundaryNeutral: BidiCategory = ...
    """"""
    ParagraphSeparator: BidiCategory = ...
    """"""
    SegmentSeparator: BidiCategory = ...
    """"""
    Whitespace: BidiCategory = ...
    """"""
    OtherNeutrals: BidiCategory = ...
    """"""
    LeftToRightIsolate: BidiCategory = ...
    """"""
    RightToLeftIsolate: BidiCategory = ...
    """"""
    FirstStrongIsolate: BidiCategory = ...
    """"""
    PopDirectionIsolate: BidiCategory = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Calendar(ABC, Object, ICloneable):
    """"""

    CurrentEra: ClassVar[int]
    """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """"""
    @property
    def Eras(self) -> Array[int]:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def TwoDigitYearMax(self) -> int:
        """"""
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """"""
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """"""
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """"""
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """"""
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """"""
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """"""
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """"""
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetDayOfMonth(self, time: DateTime) -> int:
        """"""
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """"""
    def GetDayOfYear(self, time: DateTime) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """"""
    def GetEra(self, time: DateTime) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetHour(self, time: DateTime) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """"""
    def GetMilliseconds(self, time: DateTime) -> float:
        """"""
    def GetMinute(self, time: DateTime) -> int:
        """"""
    def GetMonth(self, time: DateTime) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """"""
    def GetSecond(self, time: DateTime) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """"""
    def GetYear(self, time: DateTime) -> int:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """"""
    @classmethod
    def ReadOnly(cls, calendar: Calendar) -> Calendar:
        """"""
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """"""
    @overload
    def ToDateTime(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        millisecond: int,
        era: int,
    ) -> DateTime:
        """"""
    def ToFourDigitYear(self, year: int) -> int:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CalendarAlgorithmType(Enum):
    """"""

    Unknown: CalendarAlgorithmType = ...
    """"""
    SolarCalendar: CalendarAlgorithmType = ...
    """"""
    LunarCalendar: CalendarAlgorithmType = ...
    """"""
    LunisolarCalendar: CalendarAlgorithmType = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CalendarData(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CalendarId(Enum):
    """"""

    GREGORIAN: CalendarId = ...
    """"""
    GREGORIAN_US: CalendarId = ...
    """"""
    JAPAN: CalendarId = ...
    """"""
    TAIWAN: CalendarId = ...
    """"""
    KOREA: CalendarId = ...
    """"""
    HIJRI: CalendarId = ...
    """"""
    THAI: CalendarId = ...
    """"""
    HEBREW: CalendarId = ...
    """"""
    GREGORIAN_ME_FRENCH: CalendarId = ...
    """"""
    GREGORIAN_ARABIC: CalendarId = ...
    """"""
    GREGORIAN_XLIT_ENGLISH: CalendarId = ...
    """"""
    GREGORIAN_XLIT_FRENCH: CalendarId = ...
    """"""
    JULIAN: CalendarId = ...
    """"""
    JAPANESELUNISOLAR: CalendarId = ...
    """"""
    CHINESELUNISOLAR: CalendarId = ...
    """"""
    SAKA: CalendarId = ...
    """"""
    LUNAR_ETO_CHN: CalendarId = ...
    """"""
    LUNAR_ETO_KOR: CalendarId = ...
    """"""
    LUNAR_ETO_ROKUYOU: CalendarId = ...
    """"""
    KOREANLUNISOLAR: CalendarId = ...
    """"""
    TAIWANLUNISOLAR: CalendarId = ...
    """"""
    PERSIAN: CalendarId = ...
    """"""
    UMALQURA: CalendarId = ...
    """"""
    LAST_CALENDAR: CalendarId = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CalendarWeekRule(Enum):
    """"""

    FirstDay: CalendarWeekRule = ...
    """"""
    FirstFullWeek: CalendarWeekRule = ...
    """"""
    FirstFourDayWeek: CalendarWeekRule = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CalendricalCalculationsHelper(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @classmethod
    def Angle(cls, degrees: int, minutes: int, seconds: float) -> float:
        """"""
    @classmethod
    def AsDayFraction(cls, longitude: float) -> float:
        """"""
    @classmethod
    def AsSeason(cls, longitude: float) -> float:
        """"""
    @classmethod
    def Compute(cls, time: float) -> float:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def JulianCenturies(cls, moment: float) -> float:
        """"""
    @classmethod
    def Midday(cls, date: float, longitude: float) -> float:
        """"""
    @classmethod
    def MiddayAtPersianObservationSite(cls, date: float) -> float:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CharUnicodeInfo(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def GetDecimalDigitValue(cls, ch: Char) -> int:
        """"""
    @classmethod
    @overload
    def GetDecimalDigitValue(cls, s: str, index: int) -> int:
        """"""
    @classmethod
    @overload
    def GetDigitValue(cls, ch: Char) -> int:
        """"""
    @classmethod
    @overload
    def GetDigitValue(cls, s: str, index: int) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    @overload
    def GetNumericValue(cls, ch: Char) -> float:
        """"""
    @classmethod
    @overload
    def GetNumericValue(cls, s: str, index: int) -> float:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def GetUnicodeCategory(cls, ch: Char) -> UnicodeCategory:
        """"""
    @classmethod
    @overload
    def GetUnicodeCategory(cls, s: str, index: int) -> UnicodeCategory:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ChineseLunisolarCalendar(EastAsianLunisolarCalendar, ICloneable):
    """"""

    ChineseEra: ClassVar[int]
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """"""
    @property
    def Eras(self) -> Array[int]:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def TwoDigitYearMax(self) -> int:
        """"""
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """"""
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """"""
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """"""
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """"""
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """"""
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """"""
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """"""
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetCelestialStem(self, sexagenaryYear: int) -> int:
        """"""
    def GetDayOfMonth(self, time: DateTime) -> int:
        """"""
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """"""
    def GetDayOfYear(self, time: DateTime) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """"""
    def GetEra(self, time: DateTime) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetHour(self, time: DateTime) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """"""
    def GetMilliseconds(self, time: DateTime) -> float:
        """"""
    def GetMinute(self, time: DateTime) -> int:
        """"""
    def GetMonth(self, time: DateTime) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """"""
    def GetSecond(self, time: DateTime) -> int:
        """"""
    def GetSexagenaryYear(self, time: DateTime) -> int:
        """"""
    def GetTerrestrialBranch(self, sexagenaryYear: int) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """"""
    def GetYear(self, time: DateTime) -> int:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """"""
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """"""
    @overload
    def ToDateTime(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        millisecond: int,
        era: int,
    ) -> DateTime:
        """"""
    def ToFourDigitYear(self, year: int) -> int:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodePageDataItem(Object):
    """"""
    @property
    def BodyName(self) -> str:
        """"""
    @property
    def Flags(self) -> int:
        """"""
    @property
    def HeaderName(self) -> str:
        """"""
    @property
    def UIFamilyCodePage(self) -> int:
        """"""
    @property
    def WebName(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CompareInfo(Object, IDeserializationCallback):
    """"""
    @property
    def LCID(self) -> int:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Version(self) -> SortVersion:
        """"""
    @overload
    def Compare(
        self, string1: str, offset1: int, length1: int, string2: str, offset2: int, length2: int
    ) -> int:
        """"""
    @overload
    def Compare(
        self,
        string1: str,
        offset1: int,
        length1: int,
        string2: str,
        offset2: int,
        length2: int,
        options: CompareOptions,
    ) -> int:
        """"""
    @overload
    def Compare(self, string1: str, offset1: int, string2: str, offset2: int) -> int:
        """"""
    @overload
    def Compare(
        self, string1: str, offset1: int, string2: str, offset2: int, options: CompareOptions
    ) -> int:
        """"""
    @overload
    def Compare(self, string1: str, string2: str) -> int:
        """"""
    @overload
    def Compare(self, string1: str, string2: str, options: CompareOptions) -> int:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    @classmethod
    @overload
    def GetCompareInfo(cls, culture: int) -> CompareInfo:
        """"""
    @classmethod
    @overload
    def GetCompareInfo(cls, culture: int, assembly: Assembly) -> CompareInfo:
        """"""
    @classmethod
    @overload
    def GetCompareInfo(cls, name: str) -> CompareInfo:
        """"""
    @classmethod
    @overload
    def GetCompareInfo(cls, name: str, assembly: Assembly) -> CompareInfo:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, source: str, options: CompareOptions) -> int:
        """"""
    @overload
    def GetSortKey(self, source: str) -> SortKey:
        """"""
    @overload
    def GetSortKey(self, source: str, options: CompareOptions) -> SortKey:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, source: str, value: Char) -> int:
        """"""
    @overload
    def IndexOf(self, source: str, value: Char, options: CompareOptions) -> int:
        """"""
    @overload
    def IndexOf(self, source: str, value: Char, startIndex: int) -> int:
        """"""
    @overload
    def IndexOf(self, source: str, value: Char, startIndex: int, options: CompareOptions) -> int:
        """"""
    @overload
    def IndexOf(self, source: str, value: Char, startIndex: int, count: int) -> int:
        """"""
    @overload
    def IndexOf(
        self, source: str, value: Char, startIndex: int, count: int, options: CompareOptions
    ) -> int:
        """"""
    @overload
    def IndexOf(self, source: str, value: str) -> int:
        """"""
    @overload
    def IndexOf(self, source: str, value: str, options: CompareOptions) -> int:
        """"""
    @overload
    def IndexOf(self, source: str, value: str, startIndex: int) -> int:
        """"""
    @overload
    def IndexOf(self, source: str, value: str, startIndex: int, options: CompareOptions) -> int:
        """"""
    @overload
    def IndexOf(self, source: str, value: str, startIndex: int, count: int) -> int:
        """"""
    @overload
    def IndexOf(
        self, source: str, value: str, startIndex: int, count: int, options: CompareOptions
    ) -> int:
        """"""
    @overload
    def IsPrefix(self, source: str, prefix: str) -> bool:
        """"""
    @overload
    def IsPrefix(self, source: str, prefix: str, options: CompareOptions) -> bool:
        """"""
    @classmethod
    @overload
    def IsSortable(cls, ch: Char) -> bool:
        """"""
    @classmethod
    @overload
    def IsSortable(cls, text: str) -> bool:
        """"""
    @overload
    def IsSuffix(self, source: str, suffix: str) -> bool:
        """"""
    @overload
    def IsSuffix(self, source: str, suffix: str, options: CompareOptions) -> bool:
        """"""
    @overload
    def LastIndexOf(self, source: str, value: Char) -> int:
        """"""
    @overload
    def LastIndexOf(self, source: str, value: Char, options: CompareOptions) -> int:
        """"""
    @overload
    def LastIndexOf(self, source: str, value: Char, startIndex: int) -> int:
        """"""
    @overload
    def LastIndexOf(
        self, source: str, value: Char, startIndex: int, options: CompareOptions
    ) -> int:
        """"""
    @overload
    def LastIndexOf(self, source: str, value: Char, startIndex: int, count: int) -> int:
        """"""
    @overload
    def LastIndexOf(
        self, source: str, value: Char, startIndex: int, count: int, options: CompareOptions
    ) -> int:
        """"""
    @overload
    def LastIndexOf(self, source: str, value: str) -> int:
        """"""
    @overload
    def LastIndexOf(self, source: str, value: str, options: CompareOptions) -> int:
        """"""
    @overload
    def LastIndexOf(self, source: str, value: str, startIndex: int) -> int:
        """"""
    @overload
    def LastIndexOf(self, source: str, value: str, startIndex: int, options: CompareOptions) -> int:
        """"""
    @overload
    def LastIndexOf(self, source: str, value: str, startIndex: int, count: int) -> int:
        """"""
    @overload
    def LastIndexOf(
        self, source: str, value: str, startIndex: int, count: int, options: CompareOptions
    ) -> int:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CompareOptions(Enum):
    """"""

    _None: CompareOptions = ...
    """"""
    IgnoreCase: CompareOptions = ...
    """"""
    IgnoreNonSpace: CompareOptions = ...
    """"""
    IgnoreSymbols: CompareOptions = ...
    """"""
    IgnoreKanaType: CompareOptions = ...
    """"""
    IgnoreWidth: CompareOptions = ...
    """"""
    OrdinalIgnoreCase: CompareOptions = ...
    """"""
    StringSort: CompareOptions = ...
    """"""
    Ordinal: CompareOptions = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CultureData(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CultureInfo(Object, ICloneable, IFormatProvider):
    """"""
    @overload
    def __init__(self, name: str) -> None:
        """"""
    @overload
    def __init__(self, name: str, useUserOverride: bool) -> None:
        """"""
    @overload
    def __init__(self, culture: int) -> None:
        """"""
    @overload
    def __init__(self, culture: int, useUserOverride: bool) -> None:
        """"""
    @property
    def Calendar(self) -> Calendar:
        """"""
    @property
    def CompareInfo(self) -> CompareInfo:
        """"""
    @property
    def CultureTypes(self) -> CultureTypes:
        """"""
    @classmethod
    @property
    def CurrentCulture(cls) -> CultureInfo:
        """"""
    @classmethod
    @CurrentCulture.setter
    def CurrentCulture(cls, value: CultureInfo) -> None: ...
    @classmethod
    @property
    def CurrentUICulture(cls) -> CultureInfo:
        """"""
    @classmethod
    @CurrentUICulture.setter
    def CurrentUICulture(cls, value: CultureInfo) -> None: ...
    @property
    def DateTimeFormat(self) -> DateTimeFormatInfo:
        """"""
    @DateTimeFormat.setter
    def DateTimeFormat(self, value: DateTimeFormatInfo) -> None: ...
    @classmethod
    @property
    def DefaultThreadCurrentCulture(cls) -> CultureInfo:
        """"""
    @classmethod
    @DefaultThreadCurrentCulture.setter
    def DefaultThreadCurrentCulture(cls, value: CultureInfo) -> None: ...
    @classmethod
    @property
    def DefaultThreadCurrentUICulture(cls) -> CultureInfo:
        """"""
    @classmethod
    @DefaultThreadCurrentUICulture.setter
    def DefaultThreadCurrentUICulture(cls, value: CultureInfo) -> None: ...
    @property
    def DisplayName(self) -> str:
        """"""
    @property
    def EnglishName(self) -> str:
        """"""
    @property
    def IetfLanguageTag(self) -> str:
        """"""
    @classmethod
    @property
    def InstalledUICulture(cls) -> CultureInfo:
        """"""
    @classmethod
    @property
    def InvariantCulture(cls) -> CultureInfo:
        """"""
    @property
    def IsNeutralCulture(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def KeyboardLayoutId(self) -> int:
        """"""
    @property
    def LCID(self) -> int:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def NativeName(self) -> str:
        """"""
    @property
    def NumberFormat(self) -> NumberFormatInfo:
        """"""
    @NumberFormat.setter
    def NumberFormat(self, value: NumberFormatInfo) -> None: ...
    @property
    def OptionalCalendars(self) -> Array[Calendar]:
        """"""
    @property
    def Parent(self) -> CultureInfo:
        """"""
    @property
    def TextInfo(self) -> TextInfo:
        """"""
    @property
    def ThreeLetterISOLanguageName(self) -> str:
        """"""
    @property
    def ThreeLetterWindowsLanguageName(self) -> str:
        """"""
    @property
    def TwoLetterISOLanguageName(self) -> str:
        """"""
    @property
    def UseUserOverride(self) -> bool:
        """"""
    def ClearCachedData(self) -> None:
        """"""
    def Clone(self) -> object:
        """"""
    @classmethod
    def CreateSpecificCulture(cls, name: str) -> CultureInfo:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    def GetConsoleFallbackUICulture(self) -> CultureInfo:
        """"""
    @classmethod
    @overload
    def GetCultureInfo(cls, culture: int) -> CultureInfo:
        """"""
    @classmethod
    @overload
    def GetCultureInfo(cls, name: str) -> CultureInfo:
        """"""
    @classmethod
    @overload
    def GetCultureInfo(cls, name: str, altName: str) -> CultureInfo:
        """"""
    @classmethod
    def GetCultureInfoByIetfLanguageTag(cls, name: str) -> CultureInfo:
        """"""
    @classmethod
    def GetCultures(cls, types: CultureTypes) -> Array[CultureInfo]:
        """"""
    def GetFormat(self, formatType: Type) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ReadOnly(cls, ci: CultureInfo) -> CultureInfo:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CultureNotFoundException(ArgumentException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, paramName: str, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """"""
    @overload
    def __init__(self, paramName: str, invalidCultureId: int, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, invalidCultureId: int, innerException: Exception) -> None:
        """"""
    @overload
    def __init__(self, paramName: str, invalidCultureName: str, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, invalidCultureName: str, innerException: Exception) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def HResult(self) -> int:
        """"""
    @property
    def HelpLink(self) -> str:
        """"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """"""
    @property
    def InvalidCultureId(self) -> int | None:
        """"""
    @property
    def InvalidCultureName(self) -> str:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def ParamName(self) -> str:
        """"""
    @property
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """"""
    @property
    def TargetSite(self) -> MethodBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CultureTypes(Enum):
    """"""

    NeutralCultures: CultureTypes = ...
    """"""
    SpecificCultures: CultureTypes = ...
    """"""
    InstalledWin32Cultures: CultureTypes = ...
    """"""
    AllCultures: CultureTypes = ...
    """"""
    UserCustomCulture: CultureTypes = ...
    """"""
    ReplacementCultures: CultureTypes = ...
    """"""
    WindowsOnlyCultures: CultureTypes = ...
    """"""
    FrameworkCultures: CultureTypes = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class DateTimeFormatFlags(Enum):
    """"""

    _None: DateTimeFormatFlags = ...
    """"""
    UseGenitiveMonth: DateTimeFormatFlags = ...
    """"""
    UseLeapYearMonth: DateTimeFormatFlags = ...
    """"""
    UseSpacesInMonthNames: DateTimeFormatFlags = ...
    """"""
    UseHebrewRule: DateTimeFormatFlags = ...
    """"""
    UseSpacesInDayNames: DateTimeFormatFlags = ...
    """"""
    UseDigitPrefixInTokens: DateTimeFormatFlags = ...
    """"""
    NotInitialized: DateTimeFormatFlags = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DateTimeFormatInfo(Object, ICloneable, IFormatProvider):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AMDesignator(self) -> str:
        """"""
    @AMDesignator.setter
    def AMDesignator(self, value: str) -> None: ...
    @property
    def AbbreviatedDayNames(self) -> Array[str]:
        """"""
    @AbbreviatedDayNames.setter
    def AbbreviatedDayNames(self, value: Array[str]) -> None: ...
    @property
    def AbbreviatedMonthGenitiveNames(self) -> Array[str]:
        """"""
    @AbbreviatedMonthGenitiveNames.setter
    def AbbreviatedMonthGenitiveNames(self, value: Array[str]) -> None: ...
    @property
    def AbbreviatedMonthNames(self) -> Array[str]:
        """"""
    @AbbreviatedMonthNames.setter
    def AbbreviatedMonthNames(self, value: Array[str]) -> None: ...
    @property
    def Calendar(self) -> Calendar:
        """"""
    @Calendar.setter
    def Calendar(self, value: Calendar) -> None: ...
    @property
    def CalendarWeekRule(self) -> CalendarWeekRule:
        """"""
    @CalendarWeekRule.setter
    def CalendarWeekRule(self, value: CalendarWeekRule) -> None: ...
    @classmethod
    @property
    def CurrentInfo(cls) -> DateTimeFormatInfo:
        """"""
    @property
    def DateSeparator(self) -> str:
        """"""
    @DateSeparator.setter
    def DateSeparator(self, value: str) -> None: ...
    @property
    def DayNames(self) -> Array[str]:
        """"""
    @DayNames.setter
    def DayNames(self, value: Array[str]) -> None: ...
    @property
    def FirstDayOfWeek(self) -> DayOfWeek:
        """"""
    @FirstDayOfWeek.setter
    def FirstDayOfWeek(self, value: DayOfWeek) -> None: ...
    @property
    def FullDateTimePattern(self) -> str:
        """"""
    @FullDateTimePattern.setter
    def FullDateTimePattern(self, value: str) -> None: ...
    @classmethod
    @property
    def InvariantInfo(cls) -> DateTimeFormatInfo:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def LongDatePattern(self) -> str:
        """"""
    @LongDatePattern.setter
    def LongDatePattern(self, value: str) -> None: ...
    @property
    def LongTimePattern(self) -> str:
        """"""
    @LongTimePattern.setter
    def LongTimePattern(self, value: str) -> None: ...
    @property
    def MonthDayPattern(self) -> str:
        """"""
    @MonthDayPattern.setter
    def MonthDayPattern(self, value: str) -> None: ...
    @property
    def MonthGenitiveNames(self) -> Array[str]:
        """"""
    @MonthGenitiveNames.setter
    def MonthGenitiveNames(self, value: Array[str]) -> None: ...
    @property
    def MonthNames(self) -> Array[str]:
        """"""
    @MonthNames.setter
    def MonthNames(self, value: Array[str]) -> None: ...
    @property
    def NativeCalendarName(self) -> str:
        """"""
    @property
    def PMDesignator(self) -> str:
        """"""
    @PMDesignator.setter
    def PMDesignator(self, value: str) -> None: ...
    @property
    def RFC1123Pattern(self) -> str:
        """"""
    @property
    def ShortDatePattern(self) -> str:
        """"""
    @ShortDatePattern.setter
    def ShortDatePattern(self, value: str) -> None: ...
    @property
    def ShortTimePattern(self) -> str:
        """"""
    @ShortTimePattern.setter
    def ShortTimePattern(self, value: str) -> None: ...
    @property
    def ShortestDayNames(self) -> Array[str]:
        """"""
    @ShortestDayNames.setter
    def ShortestDayNames(self, value: Array[str]) -> None: ...
    @property
    def SortableDateTimePattern(self) -> str:
        """"""
    @property
    def TimeSeparator(self) -> str:
        """"""
    @TimeSeparator.setter
    def TimeSeparator(self, value: str) -> None: ...
    @property
    def UniversalSortableDateTimePattern(self) -> str:
        """"""
    @property
    def YearMonthPattern(self) -> str:
        """"""
    @YearMonthPattern.setter
    def YearMonthPattern(self, value: str) -> None: ...
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAbbreviatedDayName(self, dayofweek: DayOfWeek) -> str:
        """"""
    def GetAbbreviatedEraName(self, era: int) -> str:
        """"""
    def GetAbbreviatedMonthName(self, month: int) -> str:
        """"""
    @overload
    def GetAllDateTimePatterns(self) -> Array[str]:
        """"""
    @overload
    def GetAllDateTimePatterns(self, format: Char) -> Array[str]:
        """"""
    def GetDayName(self, dayofweek: DayOfWeek) -> str:
        """"""
    def GetEra(self, eraName: str) -> int:
        """"""
    def GetEraName(self, era: int) -> str:
        """"""
    def GetFormat(self, formatType: Type) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetInstance(cls, provider: IFormatProvider) -> DateTimeFormatInfo:
        """"""
    def GetMonthName(self, month: int) -> str:
        """"""
    def GetShortestDayName(self, dayOfWeek: DayOfWeek) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ReadOnly(cls, dtfi: DateTimeFormatInfo) -> DateTimeFormatInfo:
        """"""
    def SetAllDateTimePatterns(self, patterns: Array[str], format: Char) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DateTimeFormatInfoScanner(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class DateTimeStyles(Enum):
    """"""

    _None: DateTimeStyles = ...
    """"""
    AllowLeadingWhite: DateTimeStyles = ...
    """"""
    AllowTrailingWhite: DateTimeStyles = ...
    """"""
    AllowInnerWhite: DateTimeStyles = ...
    """"""
    AllowWhiteSpaces: DateTimeStyles = ...
    """"""
    NoCurrentDateDefault: DateTimeStyles = ...
    """"""
    AdjustToUniversal: DateTimeStyles = ...
    """"""
    AssumeLocal: DateTimeStyles = ...
    """"""
    AssumeUniversal: DateTimeStyles = ...
    """"""
    RoundtripKind: DateTimeStyles = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DaylightTime(Object):
    """"""
    def __init__(self, start: DateTime, end: DateTime, delta: TimeSpan) -> None:
        """"""
    @property
    def Delta(self) -> TimeSpan:
        """"""
    @property
    def End(self) -> DateTime:
        """"""
    @property
    def Start(self) -> DateTime:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DaylightTimeStruct(ValueType):
    """"""
    def __init__(self, start: DateTime, end: DateTime, delta: TimeSpan) -> None:
        """"""
    @property
    def Delta(self) -> TimeSpan:
        """"""
    @property
    def End(self) -> DateTime:
        """"""
    @property
    def Start(self) -> DateTime:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class DigitShapes(Enum):
    """"""

    Context: DigitShapes = ...
    """"""
    _None: DigitShapes = ...
    """"""
    NativeNational: DigitShapes = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EastAsianLunisolarCalendar(ABC, Calendar, ICloneable):
    """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """"""
    @property
    def Eras(self) -> Array[int]:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def TwoDigitYearMax(self) -> int:
        """"""
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """"""
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """"""
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """"""
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """"""
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """"""
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """"""
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """"""
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetCelestialStem(self, sexagenaryYear: int) -> int:
        """"""
    def GetDayOfMonth(self, time: DateTime) -> int:
        """"""
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """"""
    def GetDayOfYear(self, time: DateTime) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """"""
    def GetEra(self, time: DateTime) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetHour(self, time: DateTime) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """"""
    def GetMilliseconds(self, time: DateTime) -> float:
        """"""
    def GetMinute(self, time: DateTime) -> int:
        """"""
    def GetMonth(self, time: DateTime) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """"""
    def GetSecond(self, time: DateTime) -> int:
        """"""
    def GetSexagenaryYear(self, time: DateTime) -> int:
        """"""
    def GetTerrestrialBranch(self, sexagenaryYear: int) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """"""
    def GetYear(self, time: DateTime) -> int:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """"""
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """"""
    @overload
    def ToDateTime(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        millisecond: int,
        era: int,
    ) -> DateTime:
        """"""
    def ToFourDigitYear(self, year: int) -> int:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EncodingTable(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EraInfo(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class FORMATFLAGS(Enum):
    """"""

    _None: FORMATFLAGS = ...
    """"""
    UseGenitiveMonth: FORMATFLAGS = ...
    """"""
    UseLeapYearMonth: FORMATFLAGS = ...
    """"""
    UseSpacesInMonthNames: FORMATFLAGS = ...
    """"""
    UseHebrewParsing: FORMATFLAGS = ...
    """"""
    UseSpacesInDayNames: FORMATFLAGS = ...
    """"""
    UseDigitPrefixInTokens: FORMATFLAGS = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class GlobalizationAssembly(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class GlobalizationExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetStringComparer(cls, compareInfo: CompareInfo, options: CompareOptions) -> StringComparer:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class GregorianCalendar(Calendar, ICloneable):
    """"""

    ADEra: ClassVar[int]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, type: GregorianCalendarTypes) -> None:
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """"""
    @property
    def CalendarType(self) -> GregorianCalendarTypes:
        """"""
    @CalendarType.setter
    def CalendarType(self, value: GregorianCalendarTypes) -> None: ...
    @property
    def Eras(self) -> Array[int]:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def TwoDigitYearMax(self) -> int:
        """"""
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """"""
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """"""
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """"""
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """"""
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """"""
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """"""
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """"""
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetDayOfMonth(self, time: DateTime) -> int:
        """"""
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """"""
    def GetDayOfYear(self, time: DateTime) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """"""
    def GetEra(self, time: DateTime) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetHour(self, time: DateTime) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """"""
    def GetMilliseconds(self, time: DateTime) -> float:
        """"""
    def GetMinute(self, time: DateTime) -> int:
        """"""
    def GetMonth(self, time: DateTime) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """"""
    def GetSecond(self, time: DateTime) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """"""
    def GetYear(self, time: DateTime) -> int:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """"""
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """"""
    @overload
    def ToDateTime(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        millisecond: int,
        era: int,
    ) -> DateTime:
        """"""
    def ToFourDigitYear(self, year: int) -> int:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class GregorianCalendarHelper(Object):
    """"""
    @property
    def Eras(self) -> Array[int]:
        """"""
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """"""
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetDayOfMonth(self, time: DateTime) -> int:
        """"""
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """"""
    def GetDayOfYear(self, time: DateTime) -> int:
        """"""
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """"""
    def GetDaysInYear(self, year: int, era: int) -> int:
        """"""
    def GetEra(self, time: DateTime) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLeapMonth(self, year: int, era: int) -> int:
        """"""
    def GetMonth(self, time: DateTime) -> int:
        """"""
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """"""
    @overload
    def GetYear(self, time: DateTime) -> int:
        """"""
    @overload
    def GetYear(self, year: int, time: DateTime) -> int:
        """"""
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """"""
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """"""
    def IsLeapYear(self, year: int, era: int) -> bool:
        """"""
    def ToDateTime(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        millisecond: int,
        era: int,
    ) -> DateTime:
        """"""
    def ToFourDigitYear(self, year: int, twoDigitYearMax: int) -> int:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class GregorianCalendarTypes(Enum):
    """"""

    Localized: GregorianCalendarTypes = ...
    """"""
    USEnglish: GregorianCalendarTypes = ...
    """"""
    MiddleEastFrench: GregorianCalendarTypes = ...
    """"""
    Arabic: GregorianCalendarTypes = ...
    """"""
    TransliteratedEnglish: GregorianCalendarTypes = ...
    """"""
    TransliteratedFrench: GregorianCalendarTypes = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class HebrewCalendar(Calendar, ICloneable):
    """"""

    HebrewEra: ClassVar[int]
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """"""
    @property
    def Eras(self) -> Array[int]:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def TwoDigitYearMax(self) -> int:
        """"""
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """"""
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """"""
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """"""
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """"""
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """"""
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """"""
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """"""
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetDayOfMonth(self, time: DateTime) -> int:
        """"""
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """"""
    def GetDayOfYear(self, time: DateTime) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """"""
    def GetEra(self, time: DateTime) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetHour(self, time: DateTime) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """"""
    def GetMilliseconds(self, time: DateTime) -> float:
        """"""
    def GetMinute(self, time: DateTime) -> int:
        """"""
    def GetMonth(self, time: DateTime) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """"""
    def GetSecond(self, time: DateTime) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """"""
    def GetYear(self, time: DateTime) -> int:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """"""
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """"""
    @overload
    def ToDateTime(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        millisecond: int,
        era: int,
    ) -> DateTime:
        """"""
    def ToFourDigitYear(self, year: int) -> int:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class HebrewNumber(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class HebrewNumberParsingContext(ValueType):
    """"""
    def __init__(self, result: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class HebrewNumberParsingState(Enum):
    """"""

    InvalidHebrewNumber: HebrewNumberParsingState = ...
    """"""
    NotHebrewDigit: HebrewNumberParsingState = ...
    """"""
    FoundEndOfHebrewNumber: HebrewNumberParsingState = ...
    """"""
    ContinueParsing: HebrewNumberParsingState = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class HijriCalendar(Calendar, ICloneable):
    """"""

    HijriEra: ClassVar[int]
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """"""
    @property
    def Eras(self) -> Array[int]:
        """"""
    @property
    def HijriAdjustment(self) -> int:
        """"""
    @HijriAdjustment.setter
    def HijriAdjustment(self, value: int) -> None: ...
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def TwoDigitYearMax(self) -> int:
        """"""
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """"""
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """"""
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """"""
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """"""
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """"""
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """"""
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """"""
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetDayOfMonth(self, time: DateTime) -> int:
        """"""
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """"""
    def GetDayOfYear(self, time: DateTime) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """"""
    def GetEra(self, time: DateTime) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetHour(self, time: DateTime) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """"""
    def GetMilliseconds(self, time: DateTime) -> float:
        """"""
    def GetMinute(self, time: DateTime) -> int:
        """"""
    def GetMonth(self, time: DateTime) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """"""
    def GetSecond(self, time: DateTime) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """"""
    def GetYear(self, time: DateTime) -> int:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """"""
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """"""
    @overload
    def ToDateTime(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        millisecond: int,
        era: int,
    ) -> DateTime:
        """"""
    def ToFourDigitYear(self, year: int) -> int:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IdnMapping(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AllowUnassigned(self) -> bool:
        """"""
    @AllowUnassigned.setter
    def AllowUnassigned(self, value: bool) -> None: ...
    @property
    def UseStd3AsciiRules(self) -> bool:
        """"""
    @UseStd3AsciiRules.setter
    def UseStd3AsciiRules(self, value: bool) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetAscii(self, unicode: str) -> str:
        """"""
    @overload
    def GetAscii(self, unicode: str, index: int) -> str:
        """"""
    @overload
    def GetAscii(self, unicode: str, index: int, count: int) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def GetUnicode(self, ascii: str) -> str:
        """"""
    @overload
    def GetUnicode(self, ascii: str, index: int) -> str:
        """"""
    @overload
    def GetUnicode(self, ascii: str, index: int, count: int) -> str:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class InternalCodePageDataItem(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class InternalEncodingDataItem(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class JapaneseCalendar(Calendar, ICloneable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """"""
    @property
    def Eras(self) -> Array[int]:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def TwoDigitYearMax(self) -> int:
        """"""
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """"""
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """"""
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """"""
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """"""
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """"""
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """"""
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """"""
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetDayOfMonth(self, time: DateTime) -> int:
        """"""
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """"""
    def GetDayOfYear(self, time: DateTime) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """"""
    def GetEra(self, time: DateTime) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetHour(self, time: DateTime) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """"""
    def GetMilliseconds(self, time: DateTime) -> float:
        """"""
    def GetMinute(self, time: DateTime) -> int:
        """"""
    def GetMonth(self, time: DateTime) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """"""
    def GetSecond(self, time: DateTime) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """"""
    def GetYear(self, time: DateTime) -> int:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """"""
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """"""
    @overload
    def ToDateTime(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        millisecond: int,
        era: int,
    ) -> DateTime:
        """"""
    def ToFourDigitYear(self, year: int) -> int:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class JapaneseLunisolarCalendar(EastAsianLunisolarCalendar, ICloneable):
    """"""

    JapaneseEra: ClassVar[int]
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """"""
    @property
    def Eras(self) -> Array[int]:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def TwoDigitYearMax(self) -> int:
        """"""
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """"""
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """"""
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """"""
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """"""
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """"""
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """"""
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """"""
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetCelestialStem(self, sexagenaryYear: int) -> int:
        """"""
    def GetDayOfMonth(self, time: DateTime) -> int:
        """"""
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """"""
    def GetDayOfYear(self, time: DateTime) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """"""
    def GetEra(self, time: DateTime) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetHour(self, time: DateTime) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """"""
    def GetMilliseconds(self, time: DateTime) -> float:
        """"""
    def GetMinute(self, time: DateTime) -> int:
        """"""
    def GetMonth(self, time: DateTime) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """"""
    def GetSecond(self, time: DateTime) -> int:
        """"""
    def GetSexagenaryYear(self, time: DateTime) -> int:
        """"""
    def GetTerrestrialBranch(self, sexagenaryYear: int) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """"""
    def GetYear(self, time: DateTime) -> int:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """"""
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """"""
    @overload
    def ToDateTime(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        millisecond: int,
        era: int,
    ) -> DateTime:
        """"""
    def ToFourDigitYear(self, year: int) -> int:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class JulianCalendar(Calendar, ICloneable):
    """"""

    JulianEra: ClassVar[int]
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """"""
    @property
    def Eras(self) -> Array[int]:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def TwoDigitYearMax(self) -> int:
        """"""
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """"""
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """"""
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """"""
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """"""
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """"""
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """"""
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """"""
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetDayOfMonth(self, time: DateTime) -> int:
        """"""
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """"""
    def GetDayOfYear(self, time: DateTime) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """"""
    def GetEra(self, time: DateTime) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetHour(self, time: DateTime) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """"""
    def GetMilliseconds(self, time: DateTime) -> float:
        """"""
    def GetMinute(self, time: DateTime) -> int:
        """"""
    def GetMonth(self, time: DateTime) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """"""
    def GetSecond(self, time: DateTime) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """"""
    def GetYear(self, time: DateTime) -> int:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """"""
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """"""
    @overload
    def ToDateTime(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        millisecond: int,
        era: int,
    ) -> DateTime:
        """"""
    def ToFourDigitYear(self, year: int) -> int:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class KoreanCalendar(Calendar, ICloneable):
    """"""

    KoreanEra: ClassVar[int]
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """"""
    @property
    def Eras(self) -> Array[int]:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def TwoDigitYearMax(self) -> int:
        """"""
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """"""
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """"""
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """"""
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """"""
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """"""
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """"""
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """"""
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetDayOfMonth(self, time: DateTime) -> int:
        """"""
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """"""
    def GetDayOfYear(self, time: DateTime) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """"""
    def GetEra(self, time: DateTime) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetHour(self, time: DateTime) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """"""
    def GetMilliseconds(self, time: DateTime) -> float:
        """"""
    def GetMinute(self, time: DateTime) -> int:
        """"""
    def GetMonth(self, time: DateTime) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """"""
    def GetSecond(self, time: DateTime) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """"""
    def GetYear(self, time: DateTime) -> int:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """"""
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """"""
    @overload
    def ToDateTime(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        millisecond: int,
        era: int,
    ) -> DateTime:
        """"""
    def ToFourDigitYear(self, year: int) -> int:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class KoreanLunisolarCalendar(EastAsianLunisolarCalendar, ICloneable):
    """"""

    GregorianEra: ClassVar[int]
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """"""
    @property
    def Eras(self) -> Array[int]:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def TwoDigitYearMax(self) -> int:
        """"""
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """"""
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """"""
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """"""
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """"""
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """"""
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """"""
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """"""
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetCelestialStem(self, sexagenaryYear: int) -> int:
        """"""
    def GetDayOfMonth(self, time: DateTime) -> int:
        """"""
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """"""
    def GetDayOfYear(self, time: DateTime) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """"""
    def GetEra(self, time: DateTime) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetHour(self, time: DateTime) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """"""
    def GetMilliseconds(self, time: DateTime) -> float:
        """"""
    def GetMinute(self, time: DateTime) -> int:
        """"""
    def GetMonth(self, time: DateTime) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """"""
    def GetSecond(self, time: DateTime) -> int:
        """"""
    def GetSexagenaryYear(self, time: DateTime) -> int:
        """"""
    def GetTerrestrialBranch(self, sexagenaryYear: int) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """"""
    def GetYear(self, time: DateTime) -> int:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """"""
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """"""
    @overload
    def ToDateTime(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        millisecond: int,
        era: int,
    ) -> DateTime:
        """"""
    def ToFourDigitYear(self, year: int) -> int:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class MonthNameStyles(Enum):
    """"""

    Regular: MonthNameStyles = ...
    """"""
    Genitive: MonthNameStyles = ...
    """"""
    LeapYear: MonthNameStyles = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NumberFormatInfo(Object, ICloneable, IFormatProvider):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CurrencyDecimalDigits(self) -> int:
        """"""
    @CurrencyDecimalDigits.setter
    def CurrencyDecimalDigits(self, value: int) -> None: ...
    @property
    def CurrencyDecimalSeparator(self) -> str:
        """"""
    @CurrencyDecimalSeparator.setter
    def CurrencyDecimalSeparator(self, value: str) -> None: ...
    @property
    def CurrencyGroupSeparator(self) -> str:
        """"""
    @CurrencyGroupSeparator.setter
    def CurrencyGroupSeparator(self, value: str) -> None: ...
    @property
    def CurrencyGroupSizes(self) -> Array[int]:
        """"""
    @CurrencyGroupSizes.setter
    def CurrencyGroupSizes(self, value: Array[int]) -> None: ...
    @property
    def CurrencyNegativePattern(self) -> int:
        """"""
    @CurrencyNegativePattern.setter
    def CurrencyNegativePattern(self, value: int) -> None: ...
    @property
    def CurrencyPositivePattern(self) -> int:
        """"""
    @CurrencyPositivePattern.setter
    def CurrencyPositivePattern(self, value: int) -> None: ...
    @property
    def CurrencySymbol(self) -> str:
        """"""
    @CurrencySymbol.setter
    def CurrencySymbol(self, value: str) -> None: ...
    @classmethod
    @property
    def CurrentInfo(cls) -> NumberFormatInfo:
        """"""
    @property
    def DigitSubstitution(self) -> DigitShapes:
        """"""
    @DigitSubstitution.setter
    def DigitSubstitution(self, value: DigitShapes) -> None: ...
    @classmethod
    @property
    def InvariantInfo(cls) -> NumberFormatInfo:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def NaNSymbol(self) -> str:
        """"""
    @NaNSymbol.setter
    def NaNSymbol(self, value: str) -> None: ...
    @property
    def NativeDigits(self) -> Array[str]:
        """"""
    @NativeDigits.setter
    def NativeDigits(self, value: Array[str]) -> None: ...
    @property
    def NegativeInfinitySymbol(self) -> str:
        """"""
    @NegativeInfinitySymbol.setter
    def NegativeInfinitySymbol(self, value: str) -> None: ...
    @property
    def NegativeSign(self) -> str:
        """"""
    @NegativeSign.setter
    def NegativeSign(self, value: str) -> None: ...
    @property
    def NumberDecimalDigits(self) -> int:
        """"""
    @NumberDecimalDigits.setter
    def NumberDecimalDigits(self, value: int) -> None: ...
    @property
    def NumberDecimalSeparator(self) -> str:
        """"""
    @NumberDecimalSeparator.setter
    def NumberDecimalSeparator(self, value: str) -> None: ...
    @property
    def NumberGroupSeparator(self) -> str:
        """"""
    @NumberGroupSeparator.setter
    def NumberGroupSeparator(self, value: str) -> None: ...
    @property
    def NumberGroupSizes(self) -> Array[int]:
        """"""
    @NumberGroupSizes.setter
    def NumberGroupSizes(self, value: Array[int]) -> None: ...
    @property
    def NumberNegativePattern(self) -> int:
        """"""
    @NumberNegativePattern.setter
    def NumberNegativePattern(self, value: int) -> None: ...
    @property
    def PerMilleSymbol(self) -> str:
        """"""
    @PerMilleSymbol.setter
    def PerMilleSymbol(self, value: str) -> None: ...
    @property
    def PercentDecimalDigits(self) -> int:
        """"""
    @PercentDecimalDigits.setter
    def PercentDecimalDigits(self, value: int) -> None: ...
    @property
    def PercentDecimalSeparator(self) -> str:
        """"""
    @PercentDecimalSeparator.setter
    def PercentDecimalSeparator(self, value: str) -> None: ...
    @property
    def PercentGroupSeparator(self) -> str:
        """"""
    @PercentGroupSeparator.setter
    def PercentGroupSeparator(self, value: str) -> None: ...
    @property
    def PercentGroupSizes(self) -> Array[int]:
        """"""
    @PercentGroupSizes.setter
    def PercentGroupSizes(self, value: Array[int]) -> None: ...
    @property
    def PercentNegativePattern(self) -> int:
        """"""
    @PercentNegativePattern.setter
    def PercentNegativePattern(self, value: int) -> None: ...
    @property
    def PercentPositivePattern(self) -> int:
        """"""
    @PercentPositivePattern.setter
    def PercentPositivePattern(self, value: int) -> None: ...
    @property
    def PercentSymbol(self) -> str:
        """"""
    @PercentSymbol.setter
    def PercentSymbol(self, value: str) -> None: ...
    @property
    def PositiveInfinitySymbol(self) -> str:
        """"""
    @PositiveInfinitySymbol.setter
    def PositiveInfinitySymbol(self, value: str) -> None: ...
    @property
    def PositiveSign(self) -> str:
        """"""
    @PositiveSign.setter
    def PositiveSign(self, value: str) -> None: ...
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetFormat(self, formatType: Type) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetInstance(cls, formatProvider: IFormatProvider) -> NumberFormatInfo:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ReadOnly(cls, nfi: NumberFormatInfo) -> NumberFormatInfo:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class NumberStyles(Enum):
    """"""

    _None: NumberStyles = ...
    """"""
    AllowLeadingWhite: NumberStyles = ...
    """"""
    AllowTrailingWhite: NumberStyles = ...
    """"""
    AllowLeadingSign: NumberStyles = ...
    """"""
    Integer: NumberStyles = ...
    """"""
    AllowTrailingSign: NumberStyles = ...
    """"""
    AllowParentheses: NumberStyles = ...
    """"""
    AllowDecimalPoint: NumberStyles = ...
    """"""
    AllowThousands: NumberStyles = ...
    """"""
    Number: NumberStyles = ...
    """"""
    AllowExponent: NumberStyles = ...
    """"""
    Float: NumberStyles = ...
    """"""
    AllowCurrencySymbol: NumberStyles = ...
    """"""
    Currency: NumberStyles = ...
    """"""
    Any: NumberStyles = ...
    """"""
    AllowHexSpecifier: NumberStyles = ...
    """"""
    HexNumber: NumberStyles = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PersianCalendar(Calendar, ICloneable):
    """"""

    PersianEra: ClassVar[int]
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """"""
    @property
    def Eras(self) -> Array[int]:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def TwoDigitYearMax(self) -> int:
        """"""
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """"""
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """"""
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """"""
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """"""
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """"""
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """"""
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """"""
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetDayOfMonth(self, time: DateTime) -> int:
        """"""
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """"""
    def GetDayOfYear(self, time: DateTime) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """"""
    def GetEra(self, time: DateTime) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetHour(self, time: DateTime) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """"""
    def GetMilliseconds(self, time: DateTime) -> float:
        """"""
    def GetMinute(self, time: DateTime) -> int:
        """"""
    def GetMonth(self, time: DateTime) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """"""
    def GetSecond(self, time: DateTime) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """"""
    def GetYear(self, time: DateTime) -> int:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """"""
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """"""
    @overload
    def ToDateTime(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        millisecond: int,
        era: int,
    ) -> DateTime:
        """"""
    def ToFourDigitYear(self, year: int) -> int:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RegionInfo(Object):
    """"""
    @overload
    def __init__(self, name: str) -> None:
        """"""
    @overload
    def __init__(self, culture: int) -> None:
        """"""
    @property
    def CurrencyEnglishName(self) -> str:
        """"""
    @property
    def CurrencyNativeName(self) -> str:
        """"""
    @property
    def CurrencySymbol(self) -> str:
        """"""
    @classmethod
    @property
    def CurrentRegion(cls) -> RegionInfo:
        """"""
    @property
    def DisplayName(self) -> str:
        """"""
    @property
    def EnglishName(self) -> str:
        """"""
    @property
    def GeoId(self) -> int:
        """"""
    @property
    def ISOCurrencySymbol(self) -> str:
        """"""
    @property
    def IsMetric(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def NativeName(self) -> str:
        """"""
    @property
    def ThreeLetterISORegionName(self) -> str:
        """"""
    @property
    def ThreeLetterWindowsRegionName(self) -> str:
        """"""
    @property
    def TwoLetterISORegionName(self) -> str:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SortKey(Object):
    """"""
    @property
    def KeyData(self) -> Array[int]:
        """"""
    @property
    def OriginalString(self) -> str:
        """"""
    @classmethod
    def Compare(cls, sortkey1: SortKey, sortkey2: SortKey) -> int:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SortVersion(Object, IEquatable[SortVersion]):
    """"""
    def __init__(self, fullVersion: int, sortId: Guid) -> None:
        """"""
    @property
    def FullVersion(self) -> int:
        """"""
    @property
    def SortId(self) -> Guid:
        """"""
    @overload
    def Equals(self, other: SortVersion) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: SortVersion, right: SortVersion) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: SortVersion, right: SortVersion) -> bool:
        """"""
    def __eq__(self, other: SortVersion) -> bool:
        """"""
    def __ne__(self, other: SortVersion) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StringInfo(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: str) -> None:
        """"""
    @property
    def LengthInTextElements(self) -> int:
        """"""
    @property
    def String(self) -> str:
        """"""
    @String.setter
    def String(self, value: str) -> None: ...
    def Equals(self, value: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    @overload
    def GetNextTextElement(cls, str: str) -> str:
        """"""
    @classmethod
    @overload
    def GetNextTextElement(cls, str: str, index: int) -> str:
        """"""
    @classmethod
    @overload
    def GetTextElementEnumerator(cls, str: str) -> TextElementEnumerator:
        """"""
    @classmethod
    @overload
    def GetTextElementEnumerator(cls, str: str, index: int) -> TextElementEnumerator:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ParseCombiningCharacters(cls, str: str) -> Array[int]:
        """"""
    @overload
    def SubstringByTextElements(self, startingTextElement: int) -> str:
        """"""
    @overload
    def SubstringByTextElements(self, startingTextElement: int, lengthInTextElements: int) -> str:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TaiwanCalendar(Calendar, ICloneable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """"""
    @property
    def Eras(self) -> Array[int]:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def TwoDigitYearMax(self) -> int:
        """"""
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """"""
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """"""
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """"""
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """"""
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """"""
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """"""
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """"""
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetDayOfMonth(self, time: DateTime) -> int:
        """"""
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """"""
    def GetDayOfYear(self, time: DateTime) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """"""
    def GetEra(self, time: DateTime) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetHour(self, time: DateTime) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """"""
    def GetMilliseconds(self, time: DateTime) -> float:
        """"""
    def GetMinute(self, time: DateTime) -> int:
        """"""
    def GetMonth(self, time: DateTime) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """"""
    def GetSecond(self, time: DateTime) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """"""
    def GetYear(self, time: DateTime) -> int:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """"""
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """"""
    @overload
    def ToDateTime(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        millisecond: int,
        era: int,
    ) -> DateTime:
        """"""
    def ToFourDigitYear(self, year: int) -> int:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TaiwanLunisolarCalendar(EastAsianLunisolarCalendar, ICloneable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """"""
    @property
    def Eras(self) -> Array[int]:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def TwoDigitYearMax(self) -> int:
        """"""
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """"""
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """"""
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """"""
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """"""
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """"""
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """"""
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """"""
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetCelestialStem(self, sexagenaryYear: int) -> int:
        """"""
    def GetDayOfMonth(self, time: DateTime) -> int:
        """"""
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """"""
    def GetDayOfYear(self, time: DateTime) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """"""
    def GetEra(self, time: DateTime) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetHour(self, time: DateTime) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """"""
    def GetMilliseconds(self, time: DateTime) -> float:
        """"""
    def GetMinute(self, time: DateTime) -> int:
        """"""
    def GetMonth(self, time: DateTime) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """"""
    def GetSecond(self, time: DateTime) -> int:
        """"""
    def GetSexagenaryYear(self, time: DateTime) -> int:
        """"""
    def GetTerrestrialBranch(self, sexagenaryYear: int) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """"""
    def GetYear(self, time: DateTime) -> int:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """"""
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """"""
    @overload
    def ToDateTime(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        millisecond: int,
        era: int,
    ) -> DateTime:
        """"""
    def ToFourDigitYear(self, year: int) -> int:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TextElementEnumerator(Object, IEnumerator):
    """"""
    @property
    def Current(self) -> object:
        """"""
    @property
    def ElementIndex(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTextElement(self) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TextInfo(Object, IDeserializationCallback, ICloneable):
    """"""
    @property
    def ANSICodePage(self) -> int:
        """"""
    @property
    def CultureName(self) -> str:
        """"""
    @property
    def EBCDICCodePage(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsRightToLeft(self) -> bool:
        """"""
    @property
    def LCID(self) -> int:
        """"""
    @property
    def ListSeparator(self) -> str:
        """"""
    @ListSeparator.setter
    def ListSeparator(self, value: str) -> None: ...
    @property
    def MacCodePage(self) -> int:
        """"""
    @property
    def OEMCodePage(self) -> int:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    @classmethod
    def ReadOnly(cls, textInfo: TextInfo) -> TextInfo:
        """"""
    @overload
    def ToLower(self, c: Char) -> Char:
        """"""
    @overload
    def ToLower(self, str: str) -> str:
        """"""
    def ToString(self) -> str:
        """"""
    def ToTitleCase(self, str: str) -> str:
        """"""
    @overload
    def ToUpper(self, c: Char) -> Char:
        """"""
    @overload
    def ToUpper(self, str: str) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ThaiBuddhistCalendar(Calendar, ICloneable):
    """"""

    ThaiBuddhistEra: ClassVar[int]
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """"""
    @property
    def Eras(self) -> Array[int]:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def TwoDigitYearMax(self) -> int:
        """"""
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """"""
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """"""
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """"""
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """"""
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """"""
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """"""
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """"""
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetDayOfMonth(self, time: DateTime) -> int:
        """"""
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """"""
    def GetDayOfYear(self, time: DateTime) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """"""
    def GetEra(self, time: DateTime) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetHour(self, time: DateTime) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """"""
    def GetMilliseconds(self, time: DateTime) -> float:
        """"""
    def GetMinute(self, time: DateTime) -> int:
        """"""
    def GetMonth(self, time: DateTime) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """"""
    def GetSecond(self, time: DateTime) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """"""
    def GetYear(self, time: DateTime) -> int:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """"""
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """"""
    @overload
    def ToDateTime(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        millisecond: int,
        era: int,
    ) -> DateTime:
        """"""
    def ToFourDigitYear(self, year: int) -> int:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TimeSpanFormat(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TimeSpanParse(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class TimeSpanStyles(Enum):
    """"""

    _None: TimeSpanStyles = ...
    """"""
    AssumeNegative: TimeSpanStyles = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TokenHashValue(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class UmAlQuraCalendar(Calendar, ICloneable):
    """"""

    UmAlQuraEra: ClassVar[int]
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """"""
    @property
    def Eras(self) -> Array[int]:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """"""
    @property
    def TwoDigitYearMax(self) -> int:
        """"""
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """"""
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """"""
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """"""
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """"""
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """"""
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """"""
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """"""
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetDayOfMonth(self, time: DateTime) -> int:
        """"""
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """"""
    def GetDayOfYear(self, time: DateTime) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """"""
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """"""
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """"""
    def GetEra(self, time: DateTime) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetHour(self, time: DateTime) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """"""
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """"""
    def GetMilliseconds(self, time: DateTime) -> float:
        """"""
    def GetMinute(self, time: DateTime) -> int:
        """"""
    def GetMonth(self, time: DateTime) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """"""
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """"""
    def GetSecond(self, time: DateTime) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """"""
    def GetYear(self, time: DateTime) -> int:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """"""
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """"""
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """"""
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """"""
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """"""
    @overload
    def ToDateTime(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        millisecond: int,
        era: int,
    ) -> DateTime:
        """"""
    def ToFourDigitYear(self, year: int) -> int:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class UnicodeCategory(Enum):
    """"""

    UppercaseLetter: UnicodeCategory = ...
    """"""
    LowercaseLetter: UnicodeCategory = ...
    """"""
    TitlecaseLetter: UnicodeCategory = ...
    """"""
    ModifierLetter: UnicodeCategory = ...
    """"""
    OtherLetter: UnicodeCategory = ...
    """"""
    NonSpacingMark: UnicodeCategory = ...
    """"""
    SpacingCombiningMark: UnicodeCategory = ...
    """"""
    EnclosingMark: UnicodeCategory = ...
    """"""
    DecimalDigitNumber: UnicodeCategory = ...
    """"""
    LetterNumber: UnicodeCategory = ...
    """"""
    OtherNumber: UnicodeCategory = ...
    """"""
    SpaceSeparator: UnicodeCategory = ...
    """"""
    LineSeparator: UnicodeCategory = ...
    """"""
    ParagraphSeparator: UnicodeCategory = ...
    """"""
    Control: UnicodeCategory = ...
    """"""
    Format: UnicodeCategory = ...
    """"""
    Surrogate: UnicodeCategory = ...
    """"""
    PrivateUse: UnicodeCategory = ...
    """"""
    ConnectorPunctuation: UnicodeCategory = ...
    """"""
    DashPunctuation: UnicodeCategory = ...
    """"""
    OpenPunctuation: UnicodeCategory = ...
    """"""
    ClosePunctuation: UnicodeCategory = ...
    """"""
    InitialQuotePunctuation: UnicodeCategory = ...
    """"""
    FinalQuotePunctuation: UnicodeCategory = ...
    """"""
    OtherPunctuation: UnicodeCategory = ...
    """"""
    MathSymbol: UnicodeCategory = ...
    """"""
    CurrencySymbol: UnicodeCategory = ...
    """"""
    ModifierSymbol: UnicodeCategory = ...
    """"""
    OtherSymbol: UnicodeCategory = ...
    """"""
    OtherNotAssigned: UnicodeCategory = ...
    """"""
