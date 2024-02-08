from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final
from typing import Optional
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

class AppDomainSortingSetupInfo(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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

class Calendar(ABC, Object, ICloneable):
    """"""

    CurrentEra: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """

        :return:
        """
    @property
    def Eras(self) -> Array[int]:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def TwoDigitYearMax(self) -> int:
        """

        :return:
        """
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """

        :param time:
        :param days:
        :return:
        """
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """

        :param time:
        :param hours:
        :return:
        """
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """

        :param time:
        :param milliseconds:
        :return:
        """
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """

        :param time:
        :param minutes:
        :return:
        """
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """

        :param time:
        :param months:
        :return:
        """
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """

        :param time:
        :param seconds:
        :return:
        """
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """

        :param time:
        :param weeks:
        :return:
        """
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """

        :param time:
        :param years:
        :return:
        """
    def Clone(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetDayOfMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """

        :param time:
        :return:
        """
    def GetDayOfYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetEra(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetHour(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetMilliseconds(self, time: DateTime) -> float:
        """

        :param time:
        :return:
        """
    def GetMinute(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetSecond(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """

        :param time:
        :param rule:
        :param firstDayOfWeek:
        :return:
        """
    def GetYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :param era:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """

        :param year:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """

        :param year:
        :param era:
        :return:
        """
    @classmethod
    def ReadOnly(cls, calendar: Calendar) -> Calendar:
        """

        :param calendar:
        :return:
        """
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :return:
        """
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
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :param era:
        :return:
        """
    def ToFourDigitYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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

class CalendarData(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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

class CalendarWeekRule(Enum):
    """"""

    FirstDay: CalendarWeekRule = ...
    """"""
    FirstFullWeek: CalendarWeekRule = ...
    """"""
    FirstFourDayWeek: CalendarWeekRule = ...
    """"""

class CalendricalCalculationsHelper(Object):
    """"""

    def __init__(self):
        """"""
    @classmethod
    def Angle(cls, degrees: int, minutes: int, seconds: float) -> float:
        """

        :param degrees:
        :param minutes:
        :param seconds:
        :return:
        """
    @classmethod
    def AsDayFraction(cls, longitude: float) -> float:
        """

        :param longitude:
        :return:
        """
    @classmethod
    def AsSeason(cls, longitude: float) -> float:
        """

        :param longitude:
        :return:
        """
    @classmethod
    def Compute(cls, time: float) -> float:
        """

        :param time:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def JulianCenturies(cls, moment: float) -> float:
        """

        :param moment:
        :return:
        """
    @classmethod
    def Midday(cls, date: float, longitude: float) -> float:
        """

        :param date:
        :param longitude:
        :return:
        """
    @classmethod
    def MiddayAtPersianObservationSite(cls, date: float) -> float:
        """

        :param date:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CharUnicodeInfo(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def GetDecimalDigitValue(cls, ch: Char) -> int:
        """

        :param ch:
        :return:
        """
    @classmethod
    @overload
    def GetDecimalDigitValue(cls, s: str, index: int) -> int:
        """

        :param s:
        :param index:
        :return:
        """
    @classmethod
    @overload
    def GetDigitValue(cls, ch: Char) -> int:
        """

        :param ch:
        :return:
        """
    @classmethod
    @overload
    def GetDigitValue(cls, s: str, index: int) -> int:
        """

        :param s:
        :param index:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    @overload
    def GetNumericValue(cls, ch: Char) -> float:
        """

        :param ch:
        :return:
        """
    @classmethod
    @overload
    def GetNumericValue(cls, s: str, index: int) -> float:
        """

        :param s:
        :param index:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @overload
    def GetUnicodeCategory(cls, ch: Char) -> UnicodeCategory:
        """

        :param ch:
        :return:
        """
    @classmethod
    @overload
    def GetUnicodeCategory(cls, s: str, index: int) -> UnicodeCategory:
        """

        :param s:
        :param index:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ChineseLunisolarCalendar(EastAsianLunisolarCalendar, ICloneable):
    """"""

    ChineseEra: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """

        :return:
        """
    @property
    def Eras(self) -> Array[int]:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def TwoDigitYearMax(self) -> int:
        """

        :return:
        """
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """

        :param time:
        :param days:
        :return:
        """
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """

        :param time:
        :param hours:
        :return:
        """
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """

        :param time:
        :param milliseconds:
        :return:
        """
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """

        :param time:
        :param minutes:
        :return:
        """
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """

        :param time:
        :param months:
        :return:
        """
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """

        :param time:
        :param seconds:
        :return:
        """
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """

        :param time:
        :param weeks:
        :return:
        """
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """

        :param time:
        :param years:
        :return:
        """
    def Clone(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetCelestialStem(self, sexagenaryYear: int) -> int:
        """

        :param sexagenaryYear:
        :return:
        """
    def GetDayOfMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """

        :param time:
        :return:
        """
    def GetDayOfYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetEra(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetHour(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetMilliseconds(self, time: DateTime) -> float:
        """

        :param time:
        :return:
        """
    def GetMinute(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetSecond(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetSexagenaryYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetTerrestrialBranch(self, sexagenaryYear: int) -> int:
        """

        :param sexagenaryYear:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """

        :param time:
        :param rule:
        :param firstDayOfWeek:
        :return:
        """
    def GetYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :param era:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """

        :param year:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """

        :param year:
        :param era:
        :return:
        """
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :return:
        """
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
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :param era:
        :return:
        """
    def ToFourDigitYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodePageDataItem(Object):
    """"""

    @property
    def BodyName(self) -> str:
        """

        :return:
        """
    @property
    def Flags(self) -> int:
        """

        :return:
        """
    @property
    def HeaderName(self) -> str:
        """

        :return:
        """
    @property
    def UIFamilyCodePage(self) -> int:
        """

        :return:
        """
    @property
    def WebName(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CompareInfo(Object, IDeserializationCallback):
    """"""

    @property
    def LCID(self) -> int:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Version(self) -> SortVersion:
        """

        :return:
        """
    @overload
    def Compare(self, string1: str, string2: str) -> int:
        """

        :param string1:
        :param string2:
        :return:
        """
    @overload
    def Compare(self, string1: str, string2: str, options: CompareOptions) -> int:
        """

        :param string1:
        :param string2:
        :param options:
        :return:
        """
    @overload
    def Compare(self, string1: str, offset1: int, string2: str, offset2: int) -> int:
        """

        :param string1:
        :param offset1:
        :param string2:
        :param offset2:
        :return:
        """
    @overload
    def Compare(
        self, string1: str, offset1: int, string2: str, offset2: int, options: CompareOptions
    ) -> int:
        """

        :param string1:
        :param offset1:
        :param string2:
        :param offset2:
        :param options:
        :return:
        """
    @overload
    def Compare(
        self, string1: str, offset1: int, length1: int, string2: str, offset2: int, length2: int
    ) -> int:
        """

        :param string1:
        :param offset1:
        :param length1:
        :param string2:
        :param offset2:
        :param length2:
        :return:
        """
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
        """

        :param string1:
        :param offset1:
        :param length1:
        :param string2:
        :param offset2:
        :param length2:
        :param options:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def GetCompareInfo(cls, culture: int) -> CompareInfo:
        """

        :param culture:
        :return:
        """
    @classmethod
    @overload
    def GetCompareInfo(cls, name: str) -> CompareInfo:
        """

        :param name:
        :return:
        """
    @classmethod
    @overload
    def GetCompareInfo(cls, culture: int, assembly: Assembly) -> CompareInfo:
        """

        :param culture:
        :param assembly:
        :return:
        """
    @classmethod
    @overload
    def GetCompareInfo(cls, name: str, assembly: Assembly) -> CompareInfo:
        """

        :param name:
        :param assembly:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self, source: str, options: CompareOptions) -> int:
        """

        :param source:
        :param options:
        :return:
        """
    @overload
    def GetSortKey(self, source: str) -> SortKey:
        """

        :param source:
        :return:
        """
    @overload
    def GetSortKey(self, source: str, options: CompareOptions) -> SortKey:
        """

        :param source:
        :param options:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IndexOf(self, source: str, value: Char) -> int:
        """

        :param source:
        :param value:
        :return:
        """
    @overload
    def IndexOf(self, source: str, value: str) -> int:
        """

        :param source:
        :param value:
        :return:
        """
    @overload
    def IndexOf(self, source: str, value: Char, options: CompareOptions) -> int:
        """

        :param source:
        :param value:
        :param options:
        :return:
        """
    @overload
    def IndexOf(self, source: str, value: Char, startIndex: int) -> int:
        """

        :param source:
        :param value:
        :param startIndex:
        :return:
        """
    @overload
    def IndexOf(self, source: str, value: str, options: CompareOptions) -> int:
        """

        :param source:
        :param value:
        :param options:
        :return:
        """
    @overload
    def IndexOf(self, source: str, value: str, startIndex: int) -> int:
        """

        :param source:
        :param value:
        :param startIndex:
        :return:
        """
    @overload
    def IndexOf(self, source: str, value: Char, startIndex: int, options: CompareOptions) -> int:
        """

        :param source:
        :param value:
        :param startIndex:
        :param options:
        :return:
        """
    @overload
    def IndexOf(self, source: str, value: Char, startIndex: int, count: int) -> int:
        """

        :param source:
        :param value:
        :param startIndex:
        :param count:
        :return:
        """
    @overload
    def IndexOf(self, source: str, value: str, startIndex: int, options: CompareOptions) -> int:
        """

        :param source:
        :param value:
        :param startIndex:
        :param options:
        :return:
        """
    @overload
    def IndexOf(self, source: str, value: str, startIndex: int, count: int) -> int:
        """

        :param source:
        :param value:
        :param startIndex:
        :param count:
        :return:
        """
    @overload
    def IndexOf(
        self, source: str, value: Char, startIndex: int, count: int, options: CompareOptions
    ) -> int:
        """

        :param source:
        :param value:
        :param startIndex:
        :param count:
        :param options:
        :return:
        """
    @overload
    def IndexOf(
        self, source: str, value: str, startIndex: int, count: int, options: CompareOptions
    ) -> int:
        """

        :param source:
        :param value:
        :param startIndex:
        :param count:
        :param options:
        :return:
        """
    @overload
    def IsPrefix(self, source: str, prefix: str) -> bool:
        """

        :param source:
        :param prefix:
        :return:
        """
    @overload
    def IsPrefix(self, source: str, prefix: str, options: CompareOptions) -> bool:
        """

        :param source:
        :param prefix:
        :param options:
        :return:
        """
    @classmethod
    @overload
    def IsSortable(cls, ch: Char) -> bool:
        """

        :param ch:
        :return:
        """
    @classmethod
    @overload
    def IsSortable(cls, text: str) -> bool:
        """

        :param text:
        :return:
        """
    @overload
    def IsSuffix(self, source: str, suffix: str) -> bool:
        """

        :param source:
        :param suffix:
        :return:
        """
    @overload
    def IsSuffix(self, source: str, suffix: str, options: CompareOptions) -> bool:
        """

        :param source:
        :param suffix:
        :param options:
        :return:
        """
    @overload
    def LastIndexOf(self, source: str, value: Char) -> int:
        """

        :param source:
        :param value:
        :return:
        """
    @overload
    def LastIndexOf(self, source: str, value: str) -> int:
        """

        :param source:
        :param value:
        :return:
        """
    @overload
    def LastIndexOf(self, source: str, value: Char, options: CompareOptions) -> int:
        """

        :param source:
        :param value:
        :param options:
        :return:
        """
    @overload
    def LastIndexOf(self, source: str, value: Char, startIndex: int) -> int:
        """

        :param source:
        :param value:
        :param startIndex:
        :return:
        """
    @overload
    def LastIndexOf(self, source: str, value: str, options: CompareOptions) -> int:
        """

        :param source:
        :param value:
        :param options:
        :return:
        """
    @overload
    def LastIndexOf(self, source: str, value: str, startIndex: int) -> int:
        """

        :param source:
        :param value:
        :param startIndex:
        :return:
        """
    @overload
    def LastIndexOf(
        self, source: str, value: Char, startIndex: int, options: CompareOptions
    ) -> int:
        """

        :param source:
        :param value:
        :param startIndex:
        :param options:
        :return:
        """
    @overload
    def LastIndexOf(self, source: str, value: Char, startIndex: int, count: int) -> int:
        """

        :param source:
        :param value:
        :param startIndex:
        :param count:
        :return:
        """
    @overload
    def LastIndexOf(self, source: str, value: str, startIndex: int, options: CompareOptions) -> int:
        """

        :param source:
        :param value:
        :param startIndex:
        :param options:
        :return:
        """
    @overload
    def LastIndexOf(self, source: str, value: str, startIndex: int, count: int) -> int:
        """

        :param source:
        :param value:
        :param startIndex:
        :param count:
        :return:
        """
    @overload
    def LastIndexOf(
        self, source: str, value: Char, startIndex: int, count: int, options: CompareOptions
    ) -> int:
        """

        :param source:
        :param value:
        :param startIndex:
        :param count:
        :param options:
        :return:
        """
    @overload
    def LastIndexOf(
        self, source: str, value: str, startIndex: int, count: int, options: CompareOptions
    ) -> int:
        """

        :param source:
        :param value:
        :param startIndex:
        :param count:
        :param options:
        :return:
        """
    def OnDeserialization(self, sender: object) -> None:
        """

        :param sender:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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

class CultureData(Object):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CultureInfo(Object, ICloneable, IFormatProvider):
    """"""

    @overload
    def __init__(self, culture: int):
        """

        :param culture:
        """
    @overload
    def __init__(self, name: str):
        """

        :param name:
        """
    @overload
    def __init__(self, culture: int, useUserOverride: bool):
        """

        :param culture:
        :param useUserOverride:
        """
    @overload
    def __init__(self, name: str, useUserOverride: bool):
        """

        :param name:
        :param useUserOverride:
        """
    @property
    def Calendar(self) -> Calendar:
        """

        :return:
        """
    @property
    def CompareInfo(self) -> CompareInfo:
        """

        :return:
        """
    @property
    def CultureTypes(self) -> CultureTypes:
        """

        :return:
        """
    @classmethod
    @property
    def CurrentCulture(cls) -> CultureInfo:
        """

        :return:
        """
    @classmethod
    @CurrentCulture.setter
    def CurrentCulture(cls, value: CultureInfo) -> None: ...
    @classmethod
    @property
    def CurrentUICulture(cls) -> CultureInfo:
        """

        :return:
        """
    @classmethod
    @CurrentUICulture.setter
    def CurrentUICulture(cls, value: CultureInfo) -> None: ...
    @property
    def DateTimeFormat(self) -> DateTimeFormatInfo:
        """

        :return:
        """
    @DateTimeFormat.setter
    def DateTimeFormat(self, value: DateTimeFormatInfo) -> None: ...
    @classmethod
    @property
    def DefaultThreadCurrentCulture(cls) -> CultureInfo:
        """

        :return:
        """
    @classmethod
    @DefaultThreadCurrentCulture.setter
    def DefaultThreadCurrentCulture(cls, value: CultureInfo) -> None: ...
    @classmethod
    @property
    def DefaultThreadCurrentUICulture(cls) -> CultureInfo:
        """

        :return:
        """
    @classmethod
    @DefaultThreadCurrentUICulture.setter
    def DefaultThreadCurrentUICulture(cls, value: CultureInfo) -> None: ...
    @property
    def DisplayName(self) -> str:
        """

        :return:
        """
    @property
    def EnglishName(self) -> str:
        """

        :return:
        """
    @property
    def IetfLanguageTag(self) -> str:
        """

        :return:
        """
    @classmethod
    @property
    def InstalledUICulture(cls) -> CultureInfo:
        """

        :return:
        """
    @classmethod
    @property
    def InvariantCulture(cls) -> CultureInfo:
        """

        :return:
        """
    @property
    def IsNeutralCulture(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def KeyboardLayoutId(self) -> int:
        """

        :return:
        """
    @property
    def LCID(self) -> int:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def NativeName(self) -> str:
        """

        :return:
        """
    @property
    def NumberFormat(self) -> NumberFormatInfo:
        """

        :return:
        """
    @NumberFormat.setter
    def NumberFormat(self, value: NumberFormatInfo) -> None: ...
    @property
    def OptionalCalendars(self) -> Array[Calendar]:
        """

        :return:
        """
    @property
    def Parent(self) -> CultureInfo:
        """

        :return:
        """
    @property
    def TextInfo(self) -> TextInfo:
        """

        :return:
        """
    @property
    def ThreeLetterISOLanguageName(self) -> str:
        """

        :return:
        """
    @property
    def ThreeLetterWindowsLanguageName(self) -> str:
        """

        :return:
        """
    @property
    def TwoLetterISOLanguageName(self) -> str:
        """

        :return:
        """
    @property
    def UseUserOverride(self) -> bool:
        """

        :return:
        """
    def ClearCachedData(self) -> None:
        """"""
    def Clone(self) -> object:
        """

        :return:
        """
    @classmethod
    def CreateSpecificCulture(cls, name: str) -> CultureInfo:
        """

        :param name:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetConsoleFallbackUICulture(self) -> CultureInfo:
        """

        :return:
        """
    @classmethod
    @overload
    def GetCultureInfo(cls, culture: int) -> CultureInfo:
        """

        :param culture:
        :return:
        """
    @classmethod
    @overload
    def GetCultureInfo(cls, name: str) -> CultureInfo:
        """

        :param name:
        :return:
        """
    @classmethod
    @overload
    def GetCultureInfo(cls, name: str, altName: str) -> CultureInfo:
        """

        :param name:
        :param altName:
        :return:
        """
    @classmethod
    def GetCultureInfoByIetfLanguageTag(cls, name: str) -> CultureInfo:
        """

        :param name:
        :return:
        """
    @classmethod
    def GetCultures(cls, types: CultureTypes) -> Array[CultureInfo]:
        """

        :param types:
        :return:
        """
    def GetFormat(self, formatType: Type) -> object:
        """

        :param formatType:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def ReadOnly(cls, ci: CultureInfo) -> CultureInfo:
        """

        :param ci:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CultureNotFoundException(ArgumentException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, message: str, innerException: Exception):
        """

        :param message:
        :param innerException:
        """
    @overload
    def __init__(self, paramName: str, message: str):
        """

        :param paramName:
        :param message:
        """
    @overload
    def __init__(self, message: str, invalidCultureId: int, innerException: Exception):
        """

        :param message:
        :param invalidCultureId:
        :param innerException:
        """
    @overload
    def __init__(self, paramName: str, invalidCultureId: int, message: str):
        """

        :param paramName:
        :param invalidCultureId:
        :param message:
        """
    @overload
    def __init__(self, message: str, invalidCultureName: str, innerException: Exception):
        """

        :param message:
        :param invalidCultureName:
        :param innerException:
        """
    @overload
    def __init__(self, paramName: str, invalidCultureName: str, message: str):
        """

        :param paramName:
        :param invalidCultureName:
        :param message:
        """
    @property
    def Data(self) -> IDictionary:
        """

        :return:
        """
    @property
    def HResult(self) -> int:
        """

        :return:
        """
    @property
    def HelpLink(self) -> str:
        """

        :return:
        """
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """

        :return:
        """
    @property
    def InvalidCultureId(self) -> Optional[int]:
        """

        :return:
        """
    @property
    def InvalidCultureName(self) -> str:
        """

        :return:
        """
    @property
    def Message(self) -> str:
        """

        :return:
        """
    @property
    def ParamName(self) -> str:
        """

        :return:
        """
    @property
    def Source(self) -> str:
        """

        :return:
        """
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """

        :return:
        """
    @property
    def TargetSite(self) -> MethodBase:
        """

        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

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

class DateTimeFormatInfo(Object, ICloneable, IFormatProvider):
    """"""

    def __init__(self):
        """"""
    @property
    def AMDesignator(self) -> str:
        """

        :return:
        """
    @AMDesignator.setter
    def AMDesignator(self, value: str) -> None: ...
    @property
    def AbbreviatedDayNames(self) -> Array[str]:
        """

        :return:
        """
    @AbbreviatedDayNames.setter
    def AbbreviatedDayNames(self, value: Array[str]) -> None: ...
    @property
    def AbbreviatedMonthGenitiveNames(self) -> Array[str]:
        """

        :return:
        """
    @AbbreviatedMonthGenitiveNames.setter
    def AbbreviatedMonthGenitiveNames(self, value: Array[str]) -> None: ...
    @property
    def AbbreviatedMonthNames(self) -> Array[str]:
        """

        :return:
        """
    @AbbreviatedMonthNames.setter
    def AbbreviatedMonthNames(self, value: Array[str]) -> None: ...
    @property
    def Calendar(self) -> Calendar:
        """

        :return:
        """
    @Calendar.setter
    def Calendar(self, value: Calendar) -> None: ...
    @property
    def CalendarWeekRule(self) -> CalendarWeekRule:
        """

        :return:
        """
    @CalendarWeekRule.setter
    def CalendarWeekRule(self, value: CalendarWeekRule) -> None: ...
    @classmethod
    @property
    def CurrentInfo(cls) -> DateTimeFormatInfo:
        """

        :return:
        """
    @property
    def DateSeparator(self) -> str:
        """

        :return:
        """
    @DateSeparator.setter
    def DateSeparator(self, value: str) -> None: ...
    @property
    def DayNames(self) -> Array[str]:
        """

        :return:
        """
    @DayNames.setter
    def DayNames(self, value: Array[str]) -> None: ...
    @property
    def FirstDayOfWeek(self) -> DayOfWeek:
        """

        :return:
        """
    @FirstDayOfWeek.setter
    def FirstDayOfWeek(self, value: DayOfWeek) -> None: ...
    @property
    def FullDateTimePattern(self) -> str:
        """

        :return:
        """
    @FullDateTimePattern.setter
    def FullDateTimePattern(self, value: str) -> None: ...
    @classmethod
    @property
    def InvariantInfo(cls) -> DateTimeFormatInfo:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def LongDatePattern(self) -> str:
        """

        :return:
        """
    @LongDatePattern.setter
    def LongDatePattern(self, value: str) -> None: ...
    @property
    def LongTimePattern(self) -> str:
        """

        :return:
        """
    @LongTimePattern.setter
    def LongTimePattern(self, value: str) -> None: ...
    @property
    def MonthDayPattern(self) -> str:
        """

        :return:
        """
    @MonthDayPattern.setter
    def MonthDayPattern(self, value: str) -> None: ...
    @property
    def MonthGenitiveNames(self) -> Array[str]:
        """

        :return:
        """
    @MonthGenitiveNames.setter
    def MonthGenitiveNames(self, value: Array[str]) -> None: ...
    @property
    def MonthNames(self) -> Array[str]:
        """

        :return:
        """
    @MonthNames.setter
    def MonthNames(self, value: Array[str]) -> None: ...
    @property
    def NativeCalendarName(self) -> str:
        """

        :return:
        """
    @property
    def PMDesignator(self) -> str:
        """

        :return:
        """
    @PMDesignator.setter
    def PMDesignator(self, value: str) -> None: ...
    @property
    def RFC1123Pattern(self) -> str:
        """

        :return:
        """
    @property
    def ShortDatePattern(self) -> str:
        """

        :return:
        """
    @ShortDatePattern.setter
    def ShortDatePattern(self, value: str) -> None: ...
    @property
    def ShortTimePattern(self) -> str:
        """

        :return:
        """
    @ShortTimePattern.setter
    def ShortTimePattern(self, value: str) -> None: ...
    @property
    def ShortestDayNames(self) -> Array[str]:
        """

        :return:
        """
    @ShortestDayNames.setter
    def ShortestDayNames(self, value: Array[str]) -> None: ...
    @property
    def SortableDateTimePattern(self) -> str:
        """

        :return:
        """
    @property
    def TimeSeparator(self) -> str:
        """

        :return:
        """
    @TimeSeparator.setter
    def TimeSeparator(self, value: str) -> None: ...
    @property
    def UniversalSortableDateTimePattern(self) -> str:
        """

        :return:
        """
    @property
    def YearMonthPattern(self) -> str:
        """

        :return:
        """
    @YearMonthPattern.setter
    def YearMonthPattern(self, value: str) -> None: ...
    def Clone(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAbbreviatedDayName(self, dayofweek: DayOfWeek) -> str:
        """

        :param dayofweek:
        :return:
        """
    def GetAbbreviatedEraName(self, era: int) -> str:
        """

        :param era:
        :return:
        """
    def GetAbbreviatedMonthName(self, month: int) -> str:
        """

        :param month:
        :return:
        """
    @overload
    def GetAllDateTimePatterns(self) -> Array[str]:
        """

        :return:
        """
    @overload
    def GetAllDateTimePatterns(self, format: Char) -> Array[str]:
        """

        :param format:
        :return:
        """
    def GetDayName(self, dayofweek: DayOfWeek) -> str:
        """

        :param dayofweek:
        :return:
        """
    def GetEra(self, eraName: str) -> int:
        """

        :param eraName:
        :return:
        """
    def GetEraName(self, era: int) -> str:
        """

        :param era:
        :return:
        """
    def GetFormat(self, formatType: Type) -> object:
        """

        :param formatType:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    def GetInstance(cls, provider: IFormatProvider) -> DateTimeFormatInfo:
        """

        :param provider:
        :return:
        """
    def GetMonthName(self, month: int) -> str:
        """

        :param month:
        :return:
        """
    def GetShortestDayName(self, dayOfWeek: DayOfWeek) -> str:
        """

        :param dayOfWeek:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def ReadOnly(cls, dtfi: DateTimeFormatInfo) -> DateTimeFormatInfo:
        """

        :param dtfi:
        :return:
        """
    def SetAllDateTimePatterns(self, patterns: Array[str], format: Char) -> None:
        """

        :param patterns:
        :param format:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DateTimeFormatInfoScanner(Object):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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

class DaylightTime(Object):
    """"""

    def __init__(self, start: DateTime, end: DateTime, delta: TimeSpan):
        """

        :param start:
        :param end:
        :param delta:
        """
    @property
    def Delta(self) -> TimeSpan:
        """

        :return:
        """
    @property
    def End(self) -> DateTime:
        """

        :return:
        """
    @property
    def Start(self) -> DateTime:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DaylightTimeStruct(ValueType):
    """"""

    def __init__(self, start: DateTime, end: DateTime, delta: TimeSpan):
        """

        :param start:
        :param end:
        :param delta:
        """
    @property
    def Delta(self) -> TimeSpan:
        """

        :return:
        """
    @property
    def End(self) -> DateTime:
        """

        :return:
        """
    @property
    def Start(self) -> DateTime:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DigitShapes(Enum):
    """"""

    Context: DigitShapes = ...
    """"""
    _None: DigitShapes = ...
    """"""
    NativeNational: DigitShapes = ...
    """"""

class EastAsianLunisolarCalendar(ABC, Calendar, ICloneable):
    """"""

    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """

        :return:
        """
    @property
    def Eras(self) -> Array[int]:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def TwoDigitYearMax(self) -> int:
        """

        :return:
        """
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """

        :param time:
        :param days:
        :return:
        """
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """

        :param time:
        :param hours:
        :return:
        """
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """

        :param time:
        :param milliseconds:
        :return:
        """
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """

        :param time:
        :param minutes:
        :return:
        """
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """

        :param time:
        :param months:
        :return:
        """
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """

        :param time:
        :param seconds:
        :return:
        """
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """

        :param time:
        :param weeks:
        :return:
        """
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """

        :param time:
        :param years:
        :return:
        """
    def Clone(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetCelestialStem(self, sexagenaryYear: int) -> int:
        """

        :param sexagenaryYear:
        :return:
        """
    def GetDayOfMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """

        :param time:
        :return:
        """
    def GetDayOfYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetEra(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetHour(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetMilliseconds(self, time: DateTime) -> float:
        """

        :param time:
        :return:
        """
    def GetMinute(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetSecond(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetSexagenaryYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetTerrestrialBranch(self, sexagenaryYear: int) -> int:
        """

        :param sexagenaryYear:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """

        :param time:
        :param rule:
        :param firstDayOfWeek:
        :return:
        """
    def GetYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :param era:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """

        :param year:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """

        :param year:
        :param era:
        :return:
        """
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :return:
        """
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
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :param era:
        :return:
        """
    def ToFourDigitYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EncodingTable(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EraInfo(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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

class GlobalizationAssembly(Object):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class GlobalizationExtensions(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    def GetStringComparer(cls, compareInfo: CompareInfo, options: CompareOptions) -> StringComparer:
        """

        :param compareInfo:
        :param options:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class GregorianCalendar(Calendar, ICloneable):
    """"""

    ADEra: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, type: GregorianCalendarTypes):
        """

        :param type:
        """
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """

        :return:
        """
    @property
    def CalendarType(self) -> GregorianCalendarTypes:
        """

        :return:
        """
    @CalendarType.setter
    def CalendarType(self, value: GregorianCalendarTypes) -> None: ...
    @property
    def Eras(self) -> Array[int]:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def TwoDigitYearMax(self) -> int:
        """

        :return:
        """
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """

        :param time:
        :param days:
        :return:
        """
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """

        :param time:
        :param hours:
        :return:
        """
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """

        :param time:
        :param milliseconds:
        :return:
        """
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """

        :param time:
        :param minutes:
        :return:
        """
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """

        :param time:
        :param months:
        :return:
        """
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """

        :param time:
        :param seconds:
        :return:
        """
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """

        :param time:
        :param weeks:
        :return:
        """
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """

        :param time:
        :param years:
        :return:
        """
    def Clone(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetDayOfMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """

        :param time:
        :return:
        """
    def GetDayOfYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetEra(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetHour(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetMilliseconds(self, time: DateTime) -> float:
        """

        :param time:
        :return:
        """
    def GetMinute(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetSecond(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """

        :param time:
        :param rule:
        :param firstDayOfWeek:
        :return:
        """
    def GetYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :param era:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """

        :param year:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """

        :param year:
        :param era:
        :return:
        """
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :return:
        """
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
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :param era:
        :return:
        """
    def ToFourDigitYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class GregorianCalendarHelper(Object):
    """"""

    @property
    def Eras(self) -> Array[int]:
        """

        :return:
        """
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """

        :param time:
        :param months:
        :return:
        """
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """

        :param time:
        :param years:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetDayOfMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """

        :param time:
        :return:
        """
    def GetDayOfYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    def GetDaysInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetEra(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLeapMonth(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """

        :param time:
        :param rule:
        :param firstDayOfWeek:
        :return:
        """
    @overload
    def GetYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetYear(self, year: int, time: DateTime) -> int:
        """

        :param year:
        :param time:
        :return:
        """
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :param era:
        :return:
        """
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    def IsLeapYear(self, year: int, era: int) -> bool:
        """

        :param year:
        :param era:
        :return:
        """
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
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :param era:
        :return:
        """
    def ToFourDigitYear(self, year: int, twoDigitYearMax: int) -> int:
        """

        :param year:
        :param twoDigitYearMax:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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

class HebrewCalendar(Calendar, ICloneable):
    """"""

    HebrewEra: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """

        :return:
        """
    @property
    def Eras(self) -> Array[int]:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def TwoDigitYearMax(self) -> int:
        """

        :return:
        """
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """

        :param time:
        :param days:
        :return:
        """
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """

        :param time:
        :param hours:
        :return:
        """
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """

        :param time:
        :param milliseconds:
        :return:
        """
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """

        :param time:
        :param minutes:
        :return:
        """
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """

        :param time:
        :param months:
        :return:
        """
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """

        :param time:
        :param seconds:
        :return:
        """
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """

        :param time:
        :param weeks:
        :return:
        """
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """

        :param time:
        :param years:
        :return:
        """
    def Clone(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetDayOfMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """

        :param time:
        :return:
        """
    def GetDayOfYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetEra(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetHour(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetMilliseconds(self, time: DateTime) -> float:
        """

        :param time:
        :return:
        """
    def GetMinute(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetSecond(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """

        :param time:
        :param rule:
        :param firstDayOfWeek:
        :return:
        """
    def GetYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :param era:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """

        :param year:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """

        :param year:
        :param era:
        :return:
        """
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :return:
        """
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
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :param era:
        :return:
        """
    def ToFourDigitYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class HebrewNumber(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class HebrewNumberParsingContext(ValueType):
    """"""

    def __init__(self, result: int):
        """

        :param result:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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

class HijriCalendar(Calendar, ICloneable):
    """"""

    HijriEra: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """

        :return:
        """
    @property
    def Eras(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HijriAdjustment(self) -> int:
        """

        :return:
        """
    @HijriAdjustment.setter
    def HijriAdjustment(self, value: int) -> None: ...
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def TwoDigitYearMax(self) -> int:
        """

        :return:
        """
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """

        :param time:
        :param days:
        :return:
        """
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """

        :param time:
        :param hours:
        :return:
        """
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """

        :param time:
        :param milliseconds:
        :return:
        """
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """

        :param time:
        :param minutes:
        :return:
        """
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """

        :param time:
        :param months:
        :return:
        """
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """

        :param time:
        :param seconds:
        :return:
        """
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """

        :param time:
        :param weeks:
        :return:
        """
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """

        :param time:
        :param years:
        :return:
        """
    def Clone(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetDayOfMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """

        :param time:
        :return:
        """
    def GetDayOfYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetEra(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetHour(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetMilliseconds(self, time: DateTime) -> float:
        """

        :param time:
        :return:
        """
    def GetMinute(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetSecond(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """

        :param time:
        :param rule:
        :param firstDayOfWeek:
        :return:
        """
    def GetYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :param era:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """

        :param year:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """

        :param year:
        :param era:
        :return:
        """
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :return:
        """
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
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :param era:
        :return:
        """
    def ToFourDigitYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class IdnMapping(Object):
    """"""

    def __init__(self):
        """"""
    @property
    def AllowUnassigned(self) -> bool:
        """

        :return:
        """
    @AllowUnassigned.setter
    def AllowUnassigned(self, value: bool) -> None: ...
    @property
    def UseStd3AsciiRules(self) -> bool:
        """

        :return:
        """
    @UseStd3AsciiRules.setter
    def UseStd3AsciiRules(self, value: bool) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetAscii(self, unicode: str) -> str:
        """

        :param unicode:
        :return:
        """
    @overload
    def GetAscii(self, unicode: str, index: int) -> str:
        """

        :param unicode:
        :param index:
        :return:
        """
    @overload
    def GetAscii(self, unicode: str, index: int, count: int) -> str:
        """

        :param unicode:
        :param index:
        :param count:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetUnicode(self, ascii: str) -> str:
        """

        :param ascii:
        :return:
        """
    @overload
    def GetUnicode(self, ascii: str, index: int) -> str:
        """

        :param ascii:
        :param index:
        :return:
        """
    @overload
    def GetUnicode(self, ascii: str, index: int, count: int) -> str:
        """

        :param ascii:
        :param index:
        :param count:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class InternalCodePageDataItem(ValueType):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class InternalEncodingDataItem(ValueType):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class JapaneseCalendar(Calendar, ICloneable):
    """"""

    def __init__(self):
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """

        :return:
        """
    @property
    def Eras(self) -> Array[int]:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def TwoDigitYearMax(self) -> int:
        """

        :return:
        """
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """

        :param time:
        :param days:
        :return:
        """
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """

        :param time:
        :param hours:
        :return:
        """
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """

        :param time:
        :param milliseconds:
        :return:
        """
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """

        :param time:
        :param minutes:
        :return:
        """
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """

        :param time:
        :param months:
        :return:
        """
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """

        :param time:
        :param seconds:
        :return:
        """
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """

        :param time:
        :param weeks:
        :return:
        """
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """

        :param time:
        :param years:
        :return:
        """
    def Clone(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetDayOfMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """

        :param time:
        :return:
        """
    def GetDayOfYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetEra(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetHour(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetMilliseconds(self, time: DateTime) -> float:
        """

        :param time:
        :return:
        """
    def GetMinute(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetSecond(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """

        :param time:
        :param rule:
        :param firstDayOfWeek:
        :return:
        """
    def GetYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :param era:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """

        :param year:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """

        :param year:
        :param era:
        :return:
        """
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :return:
        """
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
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :param era:
        :return:
        """
    def ToFourDigitYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class JapaneseLunisolarCalendar(EastAsianLunisolarCalendar, ICloneable):
    """"""

    JapaneseEra: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """

        :return:
        """
    @property
    def Eras(self) -> Array[int]:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def TwoDigitYearMax(self) -> int:
        """

        :return:
        """
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """

        :param time:
        :param days:
        :return:
        """
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """

        :param time:
        :param hours:
        :return:
        """
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """

        :param time:
        :param milliseconds:
        :return:
        """
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """

        :param time:
        :param minutes:
        :return:
        """
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """

        :param time:
        :param months:
        :return:
        """
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """

        :param time:
        :param seconds:
        :return:
        """
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """

        :param time:
        :param weeks:
        :return:
        """
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """

        :param time:
        :param years:
        :return:
        """
    def Clone(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetCelestialStem(self, sexagenaryYear: int) -> int:
        """

        :param sexagenaryYear:
        :return:
        """
    def GetDayOfMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """

        :param time:
        :return:
        """
    def GetDayOfYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetEra(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetHour(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetMilliseconds(self, time: DateTime) -> float:
        """

        :param time:
        :return:
        """
    def GetMinute(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetSecond(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetSexagenaryYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetTerrestrialBranch(self, sexagenaryYear: int) -> int:
        """

        :param sexagenaryYear:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """

        :param time:
        :param rule:
        :param firstDayOfWeek:
        :return:
        """
    def GetYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :param era:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """

        :param year:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """

        :param year:
        :param era:
        :return:
        """
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :return:
        """
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
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :param era:
        :return:
        """
    def ToFourDigitYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class JulianCalendar(Calendar, ICloneable):
    """"""

    JulianEra: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """

        :return:
        """
    @property
    def Eras(self) -> Array[int]:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def TwoDigitYearMax(self) -> int:
        """

        :return:
        """
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """

        :param time:
        :param days:
        :return:
        """
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """

        :param time:
        :param hours:
        :return:
        """
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """

        :param time:
        :param milliseconds:
        :return:
        """
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """

        :param time:
        :param minutes:
        :return:
        """
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """

        :param time:
        :param months:
        :return:
        """
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """

        :param time:
        :param seconds:
        :return:
        """
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """

        :param time:
        :param weeks:
        :return:
        """
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """

        :param time:
        :param years:
        :return:
        """
    def Clone(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetDayOfMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """

        :param time:
        :return:
        """
    def GetDayOfYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetEra(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetHour(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetMilliseconds(self, time: DateTime) -> float:
        """

        :param time:
        :return:
        """
    def GetMinute(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetSecond(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """

        :param time:
        :param rule:
        :param firstDayOfWeek:
        :return:
        """
    def GetYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :param era:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """

        :param year:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """

        :param year:
        :param era:
        :return:
        """
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :return:
        """
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
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :param era:
        :return:
        """
    def ToFourDigitYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class KoreanCalendar(Calendar, ICloneable):
    """"""

    KoreanEra: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """

        :return:
        """
    @property
    def Eras(self) -> Array[int]:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def TwoDigitYearMax(self) -> int:
        """

        :return:
        """
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """

        :param time:
        :param days:
        :return:
        """
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """

        :param time:
        :param hours:
        :return:
        """
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """

        :param time:
        :param milliseconds:
        :return:
        """
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """

        :param time:
        :param minutes:
        :return:
        """
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """

        :param time:
        :param months:
        :return:
        """
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """

        :param time:
        :param seconds:
        :return:
        """
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """

        :param time:
        :param weeks:
        :return:
        """
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """

        :param time:
        :param years:
        :return:
        """
    def Clone(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetDayOfMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """

        :param time:
        :return:
        """
    def GetDayOfYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetEra(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetHour(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetMilliseconds(self, time: DateTime) -> float:
        """

        :param time:
        :return:
        """
    def GetMinute(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetSecond(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """

        :param time:
        :param rule:
        :param firstDayOfWeek:
        :return:
        """
    def GetYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :param era:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """

        :param year:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """

        :param year:
        :param era:
        :return:
        """
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :return:
        """
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
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :param era:
        :return:
        """
    def ToFourDigitYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class KoreanLunisolarCalendar(EastAsianLunisolarCalendar, ICloneable):
    """"""

    GregorianEra: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """

        :return:
        """
    @property
    def Eras(self) -> Array[int]:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def TwoDigitYearMax(self) -> int:
        """

        :return:
        """
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """

        :param time:
        :param days:
        :return:
        """
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """

        :param time:
        :param hours:
        :return:
        """
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """

        :param time:
        :param milliseconds:
        :return:
        """
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """

        :param time:
        :param minutes:
        :return:
        """
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """

        :param time:
        :param months:
        :return:
        """
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """

        :param time:
        :param seconds:
        :return:
        """
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """

        :param time:
        :param weeks:
        :return:
        """
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """

        :param time:
        :param years:
        :return:
        """
    def Clone(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetCelestialStem(self, sexagenaryYear: int) -> int:
        """

        :param sexagenaryYear:
        :return:
        """
    def GetDayOfMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """

        :param time:
        :return:
        """
    def GetDayOfYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetEra(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetHour(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetMilliseconds(self, time: DateTime) -> float:
        """

        :param time:
        :return:
        """
    def GetMinute(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetSecond(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetSexagenaryYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetTerrestrialBranch(self, sexagenaryYear: int) -> int:
        """

        :param sexagenaryYear:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """

        :param time:
        :param rule:
        :param firstDayOfWeek:
        :return:
        """
    def GetYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :param era:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """

        :param year:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """

        :param year:
        :param era:
        :return:
        """
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :return:
        """
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
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :param era:
        :return:
        """
    def ToFourDigitYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class MonthNameStyles(Enum):
    """"""

    Regular: MonthNameStyles = ...
    """"""
    Genitive: MonthNameStyles = ...
    """"""
    LeapYear: MonthNameStyles = ...
    """"""

class NumberFormatInfo(Object, ICloneable, IFormatProvider):
    """"""

    def __init__(self):
        """"""
    @property
    def CurrencyDecimalDigits(self) -> int:
        """

        :return:
        """
    @CurrencyDecimalDigits.setter
    def CurrencyDecimalDigits(self, value: int) -> None: ...
    @property
    def CurrencyDecimalSeparator(self) -> str:
        """

        :return:
        """
    @CurrencyDecimalSeparator.setter
    def CurrencyDecimalSeparator(self, value: str) -> None: ...
    @property
    def CurrencyGroupSeparator(self) -> str:
        """

        :return:
        """
    @CurrencyGroupSeparator.setter
    def CurrencyGroupSeparator(self, value: str) -> None: ...
    @property
    def CurrencyGroupSizes(self) -> Array[int]:
        """

        :return:
        """
    @CurrencyGroupSizes.setter
    def CurrencyGroupSizes(self, value: Array[int]) -> None: ...
    @property
    def CurrencyNegativePattern(self) -> int:
        """

        :return:
        """
    @CurrencyNegativePattern.setter
    def CurrencyNegativePattern(self, value: int) -> None: ...
    @property
    def CurrencyPositivePattern(self) -> int:
        """

        :return:
        """
    @CurrencyPositivePattern.setter
    def CurrencyPositivePattern(self, value: int) -> None: ...
    @property
    def CurrencySymbol(self) -> str:
        """

        :return:
        """
    @CurrencySymbol.setter
    def CurrencySymbol(self, value: str) -> None: ...
    @classmethod
    @property
    def CurrentInfo(cls) -> NumberFormatInfo:
        """

        :return:
        """
    @property
    def DigitSubstitution(self) -> DigitShapes:
        """

        :return:
        """
    @DigitSubstitution.setter
    def DigitSubstitution(self, value: DigitShapes) -> None: ...
    @classmethod
    @property
    def InvariantInfo(cls) -> NumberFormatInfo:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def NaNSymbol(self) -> str:
        """

        :return:
        """
    @NaNSymbol.setter
    def NaNSymbol(self, value: str) -> None: ...
    @property
    def NativeDigits(self) -> Array[str]:
        """

        :return:
        """
    @NativeDigits.setter
    def NativeDigits(self, value: Array[str]) -> None: ...
    @property
    def NegativeInfinitySymbol(self) -> str:
        """

        :return:
        """
    @NegativeInfinitySymbol.setter
    def NegativeInfinitySymbol(self, value: str) -> None: ...
    @property
    def NegativeSign(self) -> str:
        """

        :return:
        """
    @NegativeSign.setter
    def NegativeSign(self, value: str) -> None: ...
    @property
    def NumberDecimalDigits(self) -> int:
        """

        :return:
        """
    @NumberDecimalDigits.setter
    def NumberDecimalDigits(self, value: int) -> None: ...
    @property
    def NumberDecimalSeparator(self) -> str:
        """

        :return:
        """
    @NumberDecimalSeparator.setter
    def NumberDecimalSeparator(self, value: str) -> None: ...
    @property
    def NumberGroupSeparator(self) -> str:
        """

        :return:
        """
    @NumberGroupSeparator.setter
    def NumberGroupSeparator(self, value: str) -> None: ...
    @property
    def NumberGroupSizes(self) -> Array[int]:
        """

        :return:
        """
    @NumberGroupSizes.setter
    def NumberGroupSizes(self, value: Array[int]) -> None: ...
    @property
    def NumberNegativePattern(self) -> int:
        """

        :return:
        """
    @NumberNegativePattern.setter
    def NumberNegativePattern(self, value: int) -> None: ...
    @property
    def PerMilleSymbol(self) -> str:
        """

        :return:
        """
    @PerMilleSymbol.setter
    def PerMilleSymbol(self, value: str) -> None: ...
    @property
    def PercentDecimalDigits(self) -> int:
        """

        :return:
        """
    @PercentDecimalDigits.setter
    def PercentDecimalDigits(self, value: int) -> None: ...
    @property
    def PercentDecimalSeparator(self) -> str:
        """

        :return:
        """
    @PercentDecimalSeparator.setter
    def PercentDecimalSeparator(self, value: str) -> None: ...
    @property
    def PercentGroupSeparator(self) -> str:
        """

        :return:
        """
    @PercentGroupSeparator.setter
    def PercentGroupSeparator(self, value: str) -> None: ...
    @property
    def PercentGroupSizes(self) -> Array[int]:
        """

        :return:
        """
    @PercentGroupSizes.setter
    def PercentGroupSizes(self, value: Array[int]) -> None: ...
    @property
    def PercentNegativePattern(self) -> int:
        """

        :return:
        """
    @PercentNegativePattern.setter
    def PercentNegativePattern(self, value: int) -> None: ...
    @property
    def PercentPositivePattern(self) -> int:
        """

        :return:
        """
    @PercentPositivePattern.setter
    def PercentPositivePattern(self, value: int) -> None: ...
    @property
    def PercentSymbol(self) -> str:
        """

        :return:
        """
    @PercentSymbol.setter
    def PercentSymbol(self, value: str) -> None: ...
    @property
    def PositiveInfinitySymbol(self) -> str:
        """

        :return:
        """
    @PositiveInfinitySymbol.setter
    def PositiveInfinitySymbol(self, value: str) -> None: ...
    @property
    def PositiveSign(self) -> str:
        """

        :return:
        """
    @PositiveSign.setter
    def PositiveSign(self, value: str) -> None: ...
    def Clone(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetFormat(self, formatType: Type) -> object:
        """

        :param formatType:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    def GetInstance(cls, formatProvider: IFormatProvider) -> NumberFormatInfo:
        """

        :param formatProvider:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def ReadOnly(cls, nfi: NumberFormatInfo) -> NumberFormatInfo:
        """

        :param nfi:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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

class PersianCalendar(Calendar, ICloneable):
    """"""

    PersianEra: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """

        :return:
        """
    @property
    def Eras(self) -> Array[int]:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def TwoDigitYearMax(self) -> int:
        """

        :return:
        """
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """

        :param time:
        :param days:
        :return:
        """
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """

        :param time:
        :param hours:
        :return:
        """
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """

        :param time:
        :param milliseconds:
        :return:
        """
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """

        :param time:
        :param minutes:
        :return:
        """
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """

        :param time:
        :param months:
        :return:
        """
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """

        :param time:
        :param seconds:
        :return:
        """
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """

        :param time:
        :param weeks:
        :return:
        """
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """

        :param time:
        :param years:
        :return:
        """
    def Clone(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetDayOfMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """

        :param time:
        :return:
        """
    def GetDayOfYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetEra(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetHour(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetMilliseconds(self, time: DateTime) -> float:
        """

        :param time:
        :return:
        """
    def GetMinute(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetSecond(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """

        :param time:
        :param rule:
        :param firstDayOfWeek:
        :return:
        """
    def GetYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :param era:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """

        :param year:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """

        :param year:
        :param era:
        :return:
        """
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :return:
        """
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
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :param era:
        :return:
        """
    def ToFourDigitYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class RegionInfo(Object):
    """"""

    @overload
    def __init__(self, culture: int):
        """

        :param culture:
        """
    @overload
    def __init__(self, name: str):
        """

        :param name:
        """
    @property
    def CurrencyEnglishName(self) -> str:
        """

        :return:
        """
    @property
    def CurrencyNativeName(self) -> str:
        """

        :return:
        """
    @property
    def CurrencySymbol(self) -> str:
        """

        :return:
        """
    @classmethod
    @property
    def CurrentRegion(cls) -> RegionInfo:
        """

        :return:
        """
    @property
    def DisplayName(self) -> str:
        """

        :return:
        """
    @property
    def EnglishName(self) -> str:
        """

        :return:
        """
    @property
    def GeoId(self) -> int:
        """

        :return:
        """
    @property
    def ISOCurrencySymbol(self) -> str:
        """

        :return:
        """
    @property
    def IsMetric(self) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def NativeName(self) -> str:
        """

        :return:
        """
    @property
    def ThreeLetterISORegionName(self) -> str:
        """

        :return:
        """
    @property
    def ThreeLetterWindowsRegionName(self) -> str:
        """

        :return:
        """
    @property
    def TwoLetterISORegionName(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SortKey(Object):
    """"""

    @property
    def KeyData(self) -> Array[int]:
        """

        :return:
        """
    @property
    def OriginalString(self) -> str:
        """

        :return:
        """
    @classmethod
    def Compare(cls, sortkey1: SortKey, sortkey2: SortKey) -> int:
        """

        :param sortkey1:
        :param sortkey2:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SortVersion(Object, IEquatable[SortVersion]):
    """"""

    def __init__(self, fullVersion: int, sortId: Guid):
        """

        :param fullVersion:
        :param sortId:
        """
    @property
    def FullVersion(self) -> int:
        """

        :return:
        """
    @property
    def SortId(self) -> Guid:
        """

        :return:
        """
    @overload
    def Equals(self, other: SortVersion) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __eq__(self, other: SortVersion) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: SortVersion) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: SortVersion, right: SortVersion) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: SortVersion, right: SortVersion) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class StringInfo(Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: str):
        """

        :param value:
        """
    @property
    def LengthInTextElements(self) -> int:
        """

        :return:
        """
    @property
    def String(self) -> str:
        """

        :return:
        """
    @String.setter
    def String(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    @overload
    def GetNextTextElement(cls, str: str) -> str:
        """

        :param str:
        :return:
        """
    @classmethod
    @overload
    def GetNextTextElement(cls, str: str, index: int) -> str:
        """

        :param str:
        :param index:
        :return:
        """
    @classmethod
    @overload
    def GetTextElementEnumerator(cls, str: str) -> TextElementEnumerator:
        """

        :param str:
        :return:
        """
    @classmethod
    @overload
    def GetTextElementEnumerator(cls, str: str, index: int) -> TextElementEnumerator:
        """

        :param str:
        :param index:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def ParseCombiningCharacters(cls, str: str) -> Array[int]:
        """

        :param str:
        :return:
        """
    @overload
    def SubstringByTextElements(self, startingTextElement: int) -> str:
        """

        :param startingTextElement:
        :return:
        """
    @overload
    def SubstringByTextElements(self, startingTextElement: int, lengthInTextElements: int) -> str:
        """

        :param startingTextElement:
        :param lengthInTextElements:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class TaiwanCalendar(Calendar, ICloneable):
    """"""

    def __init__(self):
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """

        :return:
        """
    @property
    def Eras(self) -> Array[int]:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def TwoDigitYearMax(self) -> int:
        """

        :return:
        """
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """

        :param time:
        :param days:
        :return:
        """
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """

        :param time:
        :param hours:
        :return:
        """
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """

        :param time:
        :param milliseconds:
        :return:
        """
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """

        :param time:
        :param minutes:
        :return:
        """
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """

        :param time:
        :param months:
        :return:
        """
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """

        :param time:
        :param seconds:
        :return:
        """
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """

        :param time:
        :param weeks:
        :return:
        """
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """

        :param time:
        :param years:
        :return:
        """
    def Clone(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetDayOfMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """

        :param time:
        :return:
        """
    def GetDayOfYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetEra(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetHour(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetMilliseconds(self, time: DateTime) -> float:
        """

        :param time:
        :return:
        """
    def GetMinute(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetSecond(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """

        :param time:
        :param rule:
        :param firstDayOfWeek:
        :return:
        """
    def GetYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :param era:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """

        :param year:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """

        :param year:
        :param era:
        :return:
        """
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :return:
        """
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
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :param era:
        :return:
        """
    def ToFourDigitYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class TaiwanLunisolarCalendar(EastAsianLunisolarCalendar, ICloneable):
    """"""

    def __init__(self):
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """

        :return:
        """
    @property
    def Eras(self) -> Array[int]:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def TwoDigitYearMax(self) -> int:
        """

        :return:
        """
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """

        :param time:
        :param days:
        :return:
        """
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """

        :param time:
        :param hours:
        :return:
        """
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """

        :param time:
        :param milliseconds:
        :return:
        """
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """

        :param time:
        :param minutes:
        :return:
        """
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """

        :param time:
        :param months:
        :return:
        """
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """

        :param time:
        :param seconds:
        :return:
        """
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """

        :param time:
        :param weeks:
        :return:
        """
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """

        :param time:
        :param years:
        :return:
        """
    def Clone(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetCelestialStem(self, sexagenaryYear: int) -> int:
        """

        :param sexagenaryYear:
        :return:
        """
    def GetDayOfMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """

        :param time:
        :return:
        """
    def GetDayOfYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetEra(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetHour(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetMilliseconds(self, time: DateTime) -> float:
        """

        :param time:
        :return:
        """
    def GetMinute(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetSecond(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetSexagenaryYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetTerrestrialBranch(self, sexagenaryYear: int) -> int:
        """

        :param sexagenaryYear:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """

        :param time:
        :param rule:
        :param firstDayOfWeek:
        :return:
        """
    def GetYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :param era:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """

        :param year:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """

        :param year:
        :param era:
        :return:
        """
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :return:
        """
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
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :param era:
        :return:
        """
    def ToFourDigitYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class TextElementEnumerator(Object, IEnumerator):
    """"""

    @property
    def Current(self) -> object:
        """

        :return:
        """
    @property
    def ElementIndex(self) -> int:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetTextElement(self) -> str:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class TextInfo(Object, IDeserializationCallback, ICloneable):
    """"""

    @property
    def ANSICodePage(self) -> int:
        """

        :return:
        """
    @property
    def CultureName(self) -> str:
        """

        :return:
        """
    @property
    def EBCDICCodePage(self) -> int:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsRightToLeft(self) -> bool:
        """

        :return:
        """
    @property
    def LCID(self) -> int:
        """

        :return:
        """
    @property
    def ListSeparator(self) -> str:
        """

        :return:
        """
    @ListSeparator.setter
    def ListSeparator(self, value: str) -> None: ...
    @property
    def MacCodePage(self) -> int:
        """

        :return:
        """
    @property
    def OEMCodePage(self) -> int:
        """

        :return:
        """
    def Clone(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def OnDeserialization(self, sender: object) -> None:
        """

        :param sender:
        """
    @classmethod
    def ReadOnly(cls, textInfo: TextInfo) -> TextInfo:
        """

        :param textInfo:
        :return:
        """
    @overload
    def ToLower(self, c: Char) -> Char:
        """

        :param c:
        :return:
        """
    @overload
    def ToLower(self, str: str) -> str:
        """

        :param str:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def ToTitleCase(self, str: str) -> str:
        """

        :param str:
        :return:
        """
    @overload
    def ToUpper(self, c: Char) -> Char:
        """

        :param c:
        :return:
        """
    @overload
    def ToUpper(self, str: str) -> str:
        """

        :param str:
        :return:
        """

class ThaiBuddhistCalendar(Calendar, ICloneable):
    """"""

    ThaiBuddhistEra: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """

        :return:
        """
    @property
    def Eras(self) -> Array[int]:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def TwoDigitYearMax(self) -> int:
        """

        :return:
        """
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """

        :param time:
        :param days:
        :return:
        """
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """

        :param time:
        :param hours:
        :return:
        """
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """

        :param time:
        :param milliseconds:
        :return:
        """
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """

        :param time:
        :param minutes:
        :return:
        """
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """

        :param time:
        :param months:
        :return:
        """
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """

        :param time:
        :param seconds:
        :return:
        """
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """

        :param time:
        :param weeks:
        :return:
        """
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """

        :param time:
        :param years:
        :return:
        """
    def Clone(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetDayOfMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """

        :param time:
        :return:
        """
    def GetDayOfYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetEra(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetHour(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetMilliseconds(self, time: DateTime) -> float:
        """

        :param time:
        :return:
        """
    def GetMinute(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetSecond(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """

        :param time:
        :param rule:
        :param firstDayOfWeek:
        :return:
        """
    def GetYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :param era:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """

        :param year:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """

        :param year:
        :param era:
        :return:
        """
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :return:
        """
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
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :param era:
        :return:
        """
    def ToFourDigitYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class TimeSpanFormat(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class TimeSpanParse(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class TimeSpanStyles(Enum):
    """"""

    _None: TimeSpanStyles = ...
    """"""
    AssumeNegative: TimeSpanStyles = ...
    """"""

class TokenHashValue(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class UmAlQuraCalendar(Calendar, ICloneable):
    """"""

    UmAlQuraEra: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """

        :return:
        """
    @property
    def Eras(self) -> Array[int]:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def MinSupportedDateTime(self) -> DateTime:
        """

        :return:
        """
    @property
    def TwoDigitYearMax(self) -> int:
        """

        :return:
        """
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: int) -> None: ...
    def AddDays(self, time: DateTime, days: int) -> DateTime:
        """

        :param time:
        :param days:
        :return:
        """
    def AddHours(self, time: DateTime, hours: int) -> DateTime:
        """

        :param time:
        :param hours:
        :return:
        """
    def AddMilliseconds(self, time: DateTime, milliseconds: float) -> DateTime:
        """

        :param time:
        :param milliseconds:
        :return:
        """
    def AddMinutes(self, time: DateTime, minutes: int) -> DateTime:
        """

        :param time:
        :param minutes:
        :return:
        """
    def AddMonths(self, time: DateTime, months: int) -> DateTime:
        """

        :param time:
        :param months:
        :return:
        """
    def AddSeconds(self, time: DateTime, seconds: int) -> DateTime:
        """

        :param time:
        :param seconds:
        :return:
        """
    def AddWeeks(self, time: DateTime, weeks: int) -> DateTime:
        """

        :param time:
        :param weeks:
        :return:
        """
    def AddYears(self, time: DateTime, years: int) -> DateTime:
        """

        :param time:
        :param years:
        :return:
        """
    def Clone(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetDayOfMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek:
        """

        :param time:
        :return:
        """
    def GetDayOfYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int) -> int:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetDaysInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetEra(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetHour(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetLeapMonth(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetMilliseconds(self, time: DateTime) -> float:
        """

        :param time:
        :return:
        """
    def GetMinute(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetMonth(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    @overload
    def GetMonthsInYear(self, year: int, era: int) -> int:
        """

        :param year:
        :param era:
        :return:
        """
    def GetSecond(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetWeekOfYear(
        self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek
    ) -> int:
        """

        :param time:
        :param rule:
        :param firstDayOfWeek:
        :return:
        """
    def GetYear(self, time: DateTime) -> int:
        """

        :param time:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :return:
        """
    @overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param day:
        :param era:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int) -> bool:
        """

        :param year:
        :param month:
        :return:
        """
    @overload
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:
        """

        :param year:
        :param month:
        :param era:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int) -> bool:
        """

        :param year:
        :return:
        """
    @overload
    def IsLeapYear(self, year: int, era: int) -> bool:
        """

        :param year:
        :param era:
        :return:
        """
    @overload
    def ToDateTime(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> DateTime:
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :return:
        """
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
        """

        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :param millisecond:
        :param era:
        :return:
        """
    def ToFourDigitYear(self, year: int) -> int:
        """

        :param year:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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
