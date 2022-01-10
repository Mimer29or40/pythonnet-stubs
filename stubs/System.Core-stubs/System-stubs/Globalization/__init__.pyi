from __future__ import annotations

from abc import ABC
from typing import List, Optional, Union, overload

from System import ArgumentException, Array, Boolean, Byte, Char, DateTime, DayOfWeek, Double, Enum, Exception, Guid, ICloneable, IEquatable, IFormatProvider, Int32, Nullable, Object, String, StringComparer, TimeSpan, Type, UInt16, UInt32, ValueType, Void
from System.Collections import IEnumerator
from System.Reflection import Assembly
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import IDeserializationCallback, ISerializable, SerializationInfo, StreamingContext

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
CharType = Union[str, Char]
DoubleType = Union[float, Double]
IntType = Union[int, Int32]
NullableType = Union[Optional, Nullable]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
UIntType = Union[int, UInt32]
UShortType = Union[int, UInt16]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class AppDomainSortingSetupInfo(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Calendar(ABC, ObjectType, ICloneable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def CurrentEra() -> IntType: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType: ...
    
    @property
    def Eras(self) -> ArrayType[IntType]: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def MaxSupportedDateTime(self) -> DateTime: ...
    
    @property
    def MinSupportedDateTime(self) -> DateTime: ...
    
    @property
    def TwoDigitYearMax(self) -> IntType: ...
    
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddDays(self, time: DateTime, days: IntType) -> DateTime: ...
    
    def AddHours(self, time: DateTime, hours: IntType) -> DateTime: ...
    
    def AddMilliseconds(self, time: DateTime, milliseconds: DoubleType) -> DateTime: ...
    
    def AddMinutes(self, time: DateTime, minutes: IntType) -> DateTime: ...
    
    def AddMonths(self, time: DateTime, months: IntType) -> DateTime: ...
    
    def AddSeconds(self, time: DateTime, seconds: IntType) -> DateTime: ...
    
    def AddWeeks(self, time: DateTime, weeks: IntType) -> DateTime: ...
    
    def AddYears(self, time: DateTime, years: IntType) -> DateTime: ...
    
    def Clone(self) -> ObjectType: ...
    
    def GetDayOfMonth(self, time: DateTime) -> IntType: ...
    
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek: ...
    
    def GetDayOfYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetDaysInMonth(self, year: IntType, month: IntType) -> IntType: ...
    
    @overload
    def GetDaysInMonth(self, year: IntType, month: IntType, era: IntType) -> IntType: ...
    
    @overload
    def GetDaysInYear(self, year: IntType) -> IntType: ...
    
    @overload
    def GetDaysInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetEra(self, time: DateTime) -> IntType: ...
    
    def GetHour(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetLeapMonth(self, year: IntType) -> IntType: ...
    
    @overload
    def GetLeapMonth(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetMilliseconds(self, time: DateTime) -> DoubleType: ...
    
    def GetMinute(self, time: DateTime) -> IntType: ...
    
    def GetMonth(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetMonthsInYear(self, year: IntType) -> IntType: ...
    
    @overload
    def GetMonthsInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetSecond(self, time: DateTime) -> IntType: ...
    
    def GetWeekOfYear(self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek) -> IntType: ...
    
    def GetYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def IsLeapDay(self, year: IntType, month: IntType, day: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapDay(self, year: IntType, month: IntType, day: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapMonth(self, year: IntType, month: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapMonth(self, year: IntType, month: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapYear(self, year: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapYear(self, year: IntType, era: IntType) -> BooleanType: ...
    
    @staticmethod
    def ReadOnly(calendar: Calendar) -> Calendar: ...
    
    @overload
    def ToDateTime(self, year: IntType, month: IntType, day: IntType, hour: IntType, minute: IntType, second: IntType, millisecond: IntType) -> DateTime: ...
    
    @overload
    def ToDateTime(self, year: IntType, month: IntType, day: IntType, hour: IntType, minute: IntType, second: IntType, millisecond: IntType, era: IntType) -> DateTime: ...
    
    def ToFourDigitYear(self, year: IntType) -> IntType: ...
    
    def get_AlgorithmType(self) -> CalendarAlgorithmType: ...
    
    def get_Eras(self) -> ArrayType[IntType]: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_MaxSupportedDateTime(self) -> DateTime: ...
    
    def get_MinSupportedDateTime(self) -> DateTime: ...
    
    def get_TwoDigitYearMax(self) -> IntType: ...
    
    def set_TwoDigitYearMax(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CalendarData(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CalendricalCalculationsHelper(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Angle(degrees: IntType, minutes: IntType, seconds: DoubleType) -> DoubleType: ...
    
    @staticmethod
    def AsDayFraction(longitude: DoubleType) -> DoubleType: ...
    
    @staticmethod
    def AsSeason(longitude: DoubleType) -> DoubleType: ...
    
    @staticmethod
    def Compute(time: DoubleType) -> DoubleType: ...
    
    @staticmethod
    def JulianCenturies(moment: DoubleType) -> DoubleType: ...
    
    @staticmethod
    def Midday(date: DoubleType, longitude: DoubleType) -> DoubleType: ...
    
    @staticmethod
    def MiddayAtPersianObservationSite(date: DoubleType) -> DoubleType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CharUnicodeInfo(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def GetDecimalDigitValue(ch: CharType) -> IntType: ...
    
    @staticmethod
    @overload
    def GetDecimalDigitValue(s: StringType, index: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def GetDigitValue(ch: CharType) -> IntType: ...
    
    @staticmethod
    @overload
    def GetDigitValue(s: StringType, index: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def GetNumericValue(ch: CharType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def GetNumericValue(s: StringType, index: IntType) -> DoubleType: ...
    
    @staticmethod
    @overload
    def GetUnicodeCategory(ch: CharType) -> UnicodeCategory: ...
    
    @staticmethod
    @overload
    def GetUnicodeCategory(s: StringType, index: IntType) -> UnicodeCategory: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ChineseLunisolarCalendar(EastAsianLunisolarCalendar, ICloneable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def ChineseEra() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Eras(self) -> ArrayType[IntType]: ...
    
    @property
    def MaxSupportedDateTime(self) -> DateTime: ...
    
    @property
    def MinSupportedDateTime(self) -> DateTime: ...
    
    # ---------- Methods ---------- #
    
    def GetEra(self, time: DateTime) -> IntType: ...
    
    def get_Eras(self) -> ArrayType[IntType]: ...
    
    def get_MaxSupportedDateTime(self) -> DateTime: ...
    
    def get_MinSupportedDateTime(self) -> DateTime: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodePageDataItem(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BodyName(self) -> StringType: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @property
    def HeaderName(self) -> StringType: ...
    
    @property
    def UIFamilyCodePage(self) -> IntType: ...
    
    @property
    def WebName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_BodyName(self) -> StringType: ...
    
    def get_Flags(self) -> UIntType: ...
    
    def get_HeaderName(self) -> StringType: ...
    
    def get_UIFamilyCodePage(self) -> IntType: ...
    
    def get_WebName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CompareInfo(ObjectType, IDeserializationCallback):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def LCID(self) -> IntType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Version(self) -> SortVersion: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Compare(self, string1: StringType, string2: StringType, options: CompareOptions) -> IntType: ...
    
    @overload
    def Compare(self, string1: StringType, offset1: IntType, length1: IntType, string2: StringType, offset2: IntType, length2: IntType, options: CompareOptions) -> IntType: ...
    
    @overload
    def Compare(self, string1: StringType, string2: StringType) -> IntType: ...
    
    @overload
    def Compare(self, string1: StringType, offset1: IntType, length1: IntType, string2: StringType, offset2: IntType, length2: IntType) -> IntType: ...
    
    @overload
    def Compare(self, string1: StringType, offset1: IntType, string2: StringType, offset2: IntType, options: CompareOptions) -> IntType: ...
    
    @overload
    def Compare(self, string1: StringType, offset1: IntType, string2: StringType, offset2: IntType) -> IntType: ...
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def GetCompareInfo(culture: IntType, assembly: Assembly) -> CompareInfo: ...
    
    @staticmethod
    @overload
    def GetCompareInfo(culture: IntType) -> CompareInfo: ...
    
    @staticmethod
    @overload
    def GetCompareInfo(name: StringType) -> CompareInfo: ...
    
    @staticmethod
    @overload
    def GetCompareInfo(name: StringType, assembly: Assembly) -> CompareInfo: ...
    
    @overload
    def GetHashCode(self) -> IntType: ...
    
    @overload
    def GetHashCode(self, source: StringType, options: CompareOptions) -> IntType: ...
    
    @overload
    def GetSortKey(self, source: StringType, options: CompareOptions) -> SortKey: ...
    
    @overload
    def GetSortKey(self, source: StringType) -> SortKey: ...
    
    @overload
    def IndexOf(self, source: StringType, value: CharType) -> IntType: ...
    
    @overload
    def IndexOf(self, source: StringType, value: StringType) -> IntType: ...
    
    @overload
    def IndexOf(self, source: StringType, value: CharType, options: CompareOptions) -> IntType: ...
    
    @overload
    def IndexOf(self, source: StringType, value: StringType, options: CompareOptions) -> IntType: ...
    
    @overload
    def IndexOf(self, source: StringType, value: CharType, startIndex: IntType) -> IntType: ...
    
    @overload
    def IndexOf(self, source: StringType, value: StringType, startIndex: IntType) -> IntType: ...
    
    @overload
    def IndexOf(self, source: StringType, value: CharType, startIndex: IntType, options: CompareOptions) -> IntType: ...
    
    @overload
    def IndexOf(self, source: StringType, value: StringType, startIndex: IntType, options: CompareOptions) -> IntType: ...
    
    @overload
    def IndexOf(self, source: StringType, value: CharType, startIndex: IntType, count: IntType) -> IntType: ...
    
    @overload
    def IndexOf(self, source: StringType, value: StringType, startIndex: IntType, count: IntType) -> IntType: ...
    
    @overload
    def IndexOf(self, source: StringType, value: CharType, startIndex: IntType, count: IntType, options: CompareOptions) -> IntType: ...
    
    @overload
    def IndexOf(self, source: StringType, value: StringType, startIndex: IntType, count: IntType, options: CompareOptions) -> IntType: ...
    
    @overload
    def IsPrefix(self, source: StringType, prefix: StringType, options: CompareOptions) -> BooleanType: ...
    
    @overload
    def IsPrefix(self, source: StringType, prefix: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsSortable(ch: CharType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsSortable(text: StringType) -> BooleanType: ...
    
    @overload
    def IsSuffix(self, source: StringType, suffix: StringType, options: CompareOptions) -> BooleanType: ...
    
    @overload
    def IsSuffix(self, source: StringType, suffix: StringType) -> BooleanType: ...
    
    @overload
    def LastIndexOf(self, source: StringType, value: CharType) -> IntType: ...
    
    @overload
    def LastIndexOf(self, source: StringType, value: StringType) -> IntType: ...
    
    @overload
    def LastIndexOf(self, source: StringType, value: CharType, options: CompareOptions) -> IntType: ...
    
    @overload
    def LastIndexOf(self, source: StringType, value: StringType, options: CompareOptions) -> IntType: ...
    
    @overload
    def LastIndexOf(self, source: StringType, value: CharType, startIndex: IntType) -> IntType: ...
    
    @overload
    def LastIndexOf(self, source: StringType, value: StringType, startIndex: IntType) -> IntType: ...
    
    @overload
    def LastIndexOf(self, source: StringType, value: CharType, startIndex: IntType, options: CompareOptions) -> IntType: ...
    
    @overload
    def LastIndexOf(self, source: StringType, value: StringType, startIndex: IntType, options: CompareOptions) -> IntType: ...
    
    @overload
    def LastIndexOf(self, source: StringType, value: CharType, startIndex: IntType, count: IntType) -> IntType: ...
    
    @overload
    def LastIndexOf(self, source: StringType, value: StringType, startIndex: IntType, count: IntType) -> IntType: ...
    
    @overload
    def LastIndexOf(self, source: StringType, value: CharType, startIndex: IntType, count: IntType, options: CompareOptions) -> IntType: ...
    
    @overload
    def LastIndexOf(self, source: StringType, value: StringType, startIndex: IntType, count: IntType, options: CompareOptions) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_LCID(self) -> IntType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Version(self) -> SortVersion: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CultureData(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CultureInfo(ObjectType, ICloneable, IFormatProvider):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, name: StringType): ...
    
    @overload
    def __init__(self, name: StringType, useUserOverride: BooleanType): ...
    
    @overload
    def __init__(self, culture: IntType): ...
    
    @overload
    def __init__(self, culture: IntType, useUserOverride: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Calendar(self) -> Calendar: ...
    
    @property
    def CompareInfo(self) -> CompareInfo: ...
    
    @property
    def CultureTypes(self) -> CultureTypes: ...
    
    @staticmethod
    @property
    def CurrentCulture() -> CultureInfo: ...
    
    @staticmethod
    @CurrentCulture.setter
    def CurrentCulture(value: CultureInfo) -> None: ...
    
    @staticmethod
    @property
    def CurrentUICulture() -> CultureInfo: ...
    
    @staticmethod
    @CurrentUICulture.setter
    def CurrentUICulture(value: CultureInfo) -> None: ...
    
    @property
    def DateTimeFormat(self) -> DateTimeFormatInfo: ...
    
    @DateTimeFormat.setter
    def DateTimeFormat(self, value: DateTimeFormatInfo) -> None: ...
    
    @staticmethod
    @property
    def DefaultThreadCurrentCulture() -> CultureInfo: ...
    
    @staticmethod
    @DefaultThreadCurrentCulture.setter
    def DefaultThreadCurrentCulture(value: CultureInfo) -> None: ...
    
    @staticmethod
    @property
    def DefaultThreadCurrentUICulture() -> CultureInfo: ...
    
    @staticmethod
    @DefaultThreadCurrentUICulture.setter
    def DefaultThreadCurrentUICulture(value: CultureInfo) -> None: ...
    
    @property
    def DisplayName(self) -> StringType: ...
    
    @property
    def EnglishName(self) -> StringType: ...
    
    @property
    def IetfLanguageTag(self) -> StringType: ...
    
    @staticmethod
    @property
    def InstalledUICulture() -> CultureInfo: ...
    
    @staticmethod
    @property
    def InvariantCulture() -> CultureInfo: ...
    
    @property
    def IsNeutralCulture(self) -> BooleanType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def KeyboardLayoutId(self) -> IntType: ...
    
    @property
    def LCID(self) -> IntType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NativeName(self) -> StringType: ...
    
    @property
    def NumberFormat(self) -> NumberFormatInfo: ...
    
    @NumberFormat.setter
    def NumberFormat(self, value: NumberFormatInfo) -> None: ...
    
    @property
    def OptionalCalendars(self) -> ArrayType[Calendar]: ...
    
    @property
    def Parent(self) -> CultureInfo: ...
    
    @property
    def TextInfo(self) -> TextInfo: ...
    
    @property
    def ThreeLetterISOLanguageName(self) -> StringType: ...
    
    @property
    def ThreeLetterWindowsLanguageName(self) -> StringType: ...
    
    @property
    def TwoLetterISOLanguageName(self) -> StringType: ...
    
    @property
    def UseUserOverride(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def ClearCachedData(self) -> VoidType: ...
    
    def Clone(self) -> ObjectType: ...
    
    @staticmethod
    def CreateSpecificCulture(name: StringType) -> CultureInfo: ...
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetConsoleFallbackUICulture(self) -> CultureInfo: ...
    
    @staticmethod
    @overload
    def GetCultureInfo(culture: IntType) -> CultureInfo: ...
    
    @staticmethod
    @overload
    def GetCultureInfo(name: StringType) -> CultureInfo: ...
    
    @staticmethod
    @overload
    def GetCultureInfo(name: StringType, altName: StringType) -> CultureInfo: ...
    
    @staticmethod
    def GetCultureInfoByIetfLanguageTag(name: StringType) -> CultureInfo: ...
    
    @staticmethod
    def GetCultures(types: CultureTypes) -> ArrayType[CultureInfo]: ...
    
    def GetFormat(self, formatType: TypeType) -> ObjectType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    def ReadOnly(ci: CultureInfo) -> CultureInfo: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Calendar(self) -> Calendar: ...
    
    def get_CompareInfo(self) -> CompareInfo: ...
    
    def get_CultureTypes(self) -> CultureTypes: ...
    
    @staticmethod
    def get_CurrentCulture() -> CultureInfo: ...
    
    @staticmethod
    def get_CurrentUICulture() -> CultureInfo: ...
    
    def get_DateTimeFormat(self) -> DateTimeFormatInfo: ...
    
    @staticmethod
    def get_DefaultThreadCurrentCulture() -> CultureInfo: ...
    
    @staticmethod
    def get_DefaultThreadCurrentUICulture() -> CultureInfo: ...
    
    def get_DisplayName(self) -> StringType: ...
    
    def get_EnglishName(self) -> StringType: ...
    
    def get_IetfLanguageTag(self) -> StringType: ...
    
    @staticmethod
    def get_InstalledUICulture() -> CultureInfo: ...
    
    @staticmethod
    def get_InvariantCulture() -> CultureInfo: ...
    
    def get_IsNeutralCulture(self) -> BooleanType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_KeyboardLayoutId(self) -> IntType: ...
    
    def get_LCID(self) -> IntType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NativeName(self) -> StringType: ...
    
    def get_NumberFormat(self) -> NumberFormatInfo: ...
    
    def get_OptionalCalendars(self) -> ArrayType[Calendar]: ...
    
    def get_Parent(self) -> CultureInfo: ...
    
    def get_TextInfo(self) -> TextInfo: ...
    
    def get_ThreeLetterISOLanguageName(self) -> StringType: ...
    
    def get_ThreeLetterWindowsLanguageName(self) -> StringType: ...
    
    def get_TwoLetterISOLanguageName(self) -> StringType: ...
    
    def get_UseUserOverride(self) -> BooleanType: ...
    
    @staticmethod
    def set_CurrentCulture(value: CultureInfo) -> VoidType: ...
    
    @staticmethod
    def set_CurrentUICulture(value: CultureInfo) -> VoidType: ...
    
    def set_DateTimeFormat(self, value: DateTimeFormatInfo) -> VoidType: ...
    
    @staticmethod
    def set_DefaultThreadCurrentCulture(value: CultureInfo) -> VoidType: ...
    
    @staticmethod
    def set_DefaultThreadCurrentUICulture(value: CultureInfo) -> VoidType: ...
    
    def set_NumberFormat(self, value: NumberFormatInfo) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CultureNotFoundException(ArgumentException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, paramName: StringType, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, paramName: StringType, invalidCultureId: IntType, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, invalidCultureId: IntType, innerException: Exception): ...
    
    @overload
    def __init__(self, paramName: StringType, invalidCultureName: StringType, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, invalidCultureName: StringType, innerException: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def InvalidCultureId(self) -> NullableType[Nullable[IntType]]: ...
    
    @property
    def InvalidCultureName(self) -> StringType: ...
    
    @property
    def Message(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_InvalidCultureId(self) -> NullableType[Nullable[IntType]]: ...
    
    def get_InvalidCultureName(self) -> StringType: ...
    
    def get_Message(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DateTimeFormatInfo(ObjectType, ICloneable, IFormatProvider):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AMDesignator(self) -> StringType: ...
    
    @AMDesignator.setter
    def AMDesignator(self, value: StringType) -> None: ...
    
    @property
    def AbbreviatedDayNames(self) -> ArrayType[StringType]: ...
    
    @AbbreviatedDayNames.setter
    def AbbreviatedDayNames(self, value: ArrayType[StringType]) -> None: ...
    
    @property
    def AbbreviatedMonthGenitiveNames(self) -> ArrayType[StringType]: ...
    
    @AbbreviatedMonthGenitiveNames.setter
    def AbbreviatedMonthGenitiveNames(self, value: ArrayType[StringType]) -> None: ...
    
    @property
    def AbbreviatedMonthNames(self) -> ArrayType[StringType]: ...
    
    @AbbreviatedMonthNames.setter
    def AbbreviatedMonthNames(self, value: ArrayType[StringType]) -> None: ...
    
    @property
    def Calendar(self) -> Calendar: ...
    
    @Calendar.setter
    def Calendar(self, value: Calendar) -> None: ...
    
    @property
    def CalendarWeekRule(self) -> CalendarWeekRule: ...
    
    @CalendarWeekRule.setter
    def CalendarWeekRule(self, value: CalendarWeekRule) -> None: ...
    
    @staticmethod
    @property
    def CurrentInfo() -> DateTimeFormatInfo: ...
    
    @property
    def DateSeparator(self) -> StringType: ...
    
    @DateSeparator.setter
    def DateSeparator(self, value: StringType) -> None: ...
    
    @property
    def DayNames(self) -> ArrayType[StringType]: ...
    
    @DayNames.setter
    def DayNames(self, value: ArrayType[StringType]) -> None: ...
    
    @property
    def FirstDayOfWeek(self) -> DayOfWeek: ...
    
    @FirstDayOfWeek.setter
    def FirstDayOfWeek(self, value: DayOfWeek) -> None: ...
    
    @property
    def FullDateTimePattern(self) -> StringType: ...
    
    @FullDateTimePattern.setter
    def FullDateTimePattern(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def InvariantInfo() -> DateTimeFormatInfo: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def LongDatePattern(self) -> StringType: ...
    
    @LongDatePattern.setter
    def LongDatePattern(self, value: StringType) -> None: ...
    
    @property
    def LongTimePattern(self) -> StringType: ...
    
    @LongTimePattern.setter
    def LongTimePattern(self, value: StringType) -> None: ...
    
    @property
    def MonthDayPattern(self) -> StringType: ...
    
    @MonthDayPattern.setter
    def MonthDayPattern(self, value: StringType) -> None: ...
    
    @property
    def MonthGenitiveNames(self) -> ArrayType[StringType]: ...
    
    @MonthGenitiveNames.setter
    def MonthGenitiveNames(self, value: ArrayType[StringType]) -> None: ...
    
    @property
    def MonthNames(self) -> ArrayType[StringType]: ...
    
    @MonthNames.setter
    def MonthNames(self, value: ArrayType[StringType]) -> None: ...
    
    @property
    def NativeCalendarName(self) -> StringType: ...
    
    @property
    def PMDesignator(self) -> StringType: ...
    
    @PMDesignator.setter
    def PMDesignator(self, value: StringType) -> None: ...
    
    @property
    def RFC1123Pattern(self) -> StringType: ...
    
    @property
    def ShortDatePattern(self) -> StringType: ...
    
    @ShortDatePattern.setter
    def ShortDatePattern(self, value: StringType) -> None: ...
    
    @property
    def ShortTimePattern(self) -> StringType: ...
    
    @ShortTimePattern.setter
    def ShortTimePattern(self, value: StringType) -> None: ...
    
    @property
    def ShortestDayNames(self) -> ArrayType[StringType]: ...
    
    @ShortestDayNames.setter
    def ShortestDayNames(self, value: ArrayType[StringType]) -> None: ...
    
    @property
    def SortableDateTimePattern(self) -> StringType: ...
    
    @property
    def TimeSeparator(self) -> StringType: ...
    
    @TimeSeparator.setter
    def TimeSeparator(self, value: StringType) -> None: ...
    
    @property
    def UniversalSortableDateTimePattern(self) -> StringType: ...
    
    @property
    def YearMonthPattern(self) -> StringType: ...
    
    @YearMonthPattern.setter
    def YearMonthPattern(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ObjectType: ...
    
    def GetAbbreviatedDayName(self, dayofweek: DayOfWeek) -> StringType: ...
    
    def GetAbbreviatedEraName(self, era: IntType) -> StringType: ...
    
    def GetAbbreviatedMonthName(self, month: IntType) -> StringType: ...
    
    @overload
    def GetAllDateTimePatterns(self, format: CharType) -> ArrayType[StringType]: ...
    
    @overload
    def GetAllDateTimePatterns(self) -> ArrayType[StringType]: ...
    
    def GetDayName(self, dayofweek: DayOfWeek) -> StringType: ...
    
    def GetEra(self, eraName: StringType) -> IntType: ...
    
    def GetEraName(self, era: IntType) -> StringType: ...
    
    def GetFormat(self, formatType: TypeType) -> ObjectType: ...
    
    @staticmethod
    def GetInstance(provider: IFormatProvider) -> DateTimeFormatInfo: ...
    
    def GetMonthName(self, month: IntType) -> StringType: ...
    
    def GetShortestDayName(self, dayOfWeek: DayOfWeek) -> StringType: ...
    
    @staticmethod
    def ReadOnly(dtfi: DateTimeFormatInfo) -> DateTimeFormatInfo: ...
    
    def SetAllDateTimePatterns(self, patterns: ArrayType[StringType], format: CharType) -> VoidType: ...
    
    def get_AMDesignator(self) -> StringType: ...
    
    def get_AbbreviatedDayNames(self) -> ArrayType[StringType]: ...
    
    def get_AbbreviatedMonthGenitiveNames(self) -> ArrayType[StringType]: ...
    
    def get_AbbreviatedMonthNames(self) -> ArrayType[StringType]: ...
    
    def get_Calendar(self) -> Calendar: ...
    
    def get_CalendarWeekRule(self) -> CalendarWeekRule: ...
    
    @staticmethod
    def get_CurrentInfo() -> DateTimeFormatInfo: ...
    
    def get_DateSeparator(self) -> StringType: ...
    
    def get_DayNames(self) -> ArrayType[StringType]: ...
    
    def get_FirstDayOfWeek(self) -> DayOfWeek: ...
    
    def get_FullDateTimePattern(self) -> StringType: ...
    
    @staticmethod
    def get_InvariantInfo() -> DateTimeFormatInfo: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_LongDatePattern(self) -> StringType: ...
    
    def get_LongTimePattern(self) -> StringType: ...
    
    def get_MonthDayPattern(self) -> StringType: ...
    
    def get_MonthGenitiveNames(self) -> ArrayType[StringType]: ...
    
    def get_MonthNames(self) -> ArrayType[StringType]: ...
    
    def get_NativeCalendarName(self) -> StringType: ...
    
    def get_PMDesignator(self) -> StringType: ...
    
    def get_RFC1123Pattern(self) -> StringType: ...
    
    def get_ShortDatePattern(self) -> StringType: ...
    
    def get_ShortTimePattern(self) -> StringType: ...
    
    def get_ShortestDayNames(self) -> ArrayType[StringType]: ...
    
    def get_SortableDateTimePattern(self) -> StringType: ...
    
    def get_TimeSeparator(self) -> StringType: ...
    
    def get_UniversalSortableDateTimePattern(self) -> StringType: ...
    
    def get_YearMonthPattern(self) -> StringType: ...
    
    def set_AMDesignator(self, value: StringType) -> VoidType: ...
    
    def set_AbbreviatedDayNames(self, value: ArrayType[StringType]) -> VoidType: ...
    
    def set_AbbreviatedMonthGenitiveNames(self, value: ArrayType[StringType]) -> VoidType: ...
    
    def set_AbbreviatedMonthNames(self, value: ArrayType[StringType]) -> VoidType: ...
    
    def set_Calendar(self, value: Calendar) -> VoidType: ...
    
    def set_CalendarWeekRule(self, value: CalendarWeekRule) -> VoidType: ...
    
    def set_DateSeparator(self, value: StringType) -> VoidType: ...
    
    def set_DayNames(self, value: ArrayType[StringType]) -> VoidType: ...
    
    def set_FirstDayOfWeek(self, value: DayOfWeek) -> VoidType: ...
    
    def set_FullDateTimePattern(self, value: StringType) -> VoidType: ...
    
    def set_LongDatePattern(self, value: StringType) -> VoidType: ...
    
    def set_LongTimePattern(self, value: StringType) -> VoidType: ...
    
    def set_MonthDayPattern(self, value: StringType) -> VoidType: ...
    
    def set_MonthGenitiveNames(self, value: ArrayType[StringType]) -> VoidType: ...
    
    def set_MonthNames(self, value: ArrayType[StringType]) -> VoidType: ...
    
    def set_PMDesignator(self, value: StringType) -> VoidType: ...
    
    def set_ShortDatePattern(self, value: StringType) -> VoidType: ...
    
    def set_ShortTimePattern(self, value: StringType) -> VoidType: ...
    
    def set_ShortestDayNames(self, value: ArrayType[StringType]) -> VoidType: ...
    
    def set_TimeSeparator(self, value: StringType) -> VoidType: ...
    
    def set_YearMonthPattern(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DateTimeFormatInfoScanner(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DaylightTime(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, start: DateTime, end: DateTime, delta: TimeSpan): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Delta(self) -> TimeSpan: ...
    
    @property
    def End(self) -> DateTime: ...
    
    @property
    def Start(self) -> DateTime: ...
    
    # ---------- Methods ---------- #
    
    def get_Delta(self) -> TimeSpan: ...
    
    def get_End(self) -> DateTime: ...
    
    def get_Start(self) -> DateTime: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EastAsianLunisolarCalendar(ABC, Calendar, ICloneable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType: ...
    
    @property
    def TwoDigitYearMax(self) -> IntType: ...
    
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddMonths(self, time: DateTime, months: IntType) -> DateTime: ...
    
    def AddYears(self, time: DateTime, years: IntType) -> DateTime: ...
    
    def GetCelestialStem(self, sexagenaryYear: IntType) -> IntType: ...
    
    def GetDayOfMonth(self, time: DateTime) -> IntType: ...
    
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek: ...
    
    def GetDayOfYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetDaysInMonth(self, year: IntType, month: IntType, era: IntType) -> IntType: ...
    
    @overload
    def GetDaysInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    @overload
    def GetLeapMonth(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetMonth(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetMonthsInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetSexagenaryYear(self, time: DateTime) -> IntType: ...
    
    def GetTerrestrialBranch(self, sexagenaryYear: IntType) -> IntType: ...
    
    def GetYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def IsLeapDay(self, year: IntType, month: IntType, day: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapMonth(self, year: IntType, month: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapYear(self, year: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def ToDateTime(self, year: IntType, month: IntType, day: IntType, hour: IntType, minute: IntType, second: IntType, millisecond: IntType, era: IntType) -> DateTime: ...
    
    def ToFourDigitYear(self, year: IntType) -> IntType: ...
    
    def get_AlgorithmType(self) -> CalendarAlgorithmType: ...
    
    def get_TwoDigitYearMax(self) -> IntType: ...
    
    def set_TwoDigitYearMax(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncodingTable(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EraInfo(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GlobalizationAssembly(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GlobalizationExtensions(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetStringComparer(compareInfo: CompareInfo, options: CompareOptions) -> StringComparer: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GregorianCalendar(Calendar, ICloneable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def ADEra() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, type: GregorianCalendarTypes): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType: ...
    
    @property
    def CalendarType(self) -> GregorianCalendarTypes: ...
    
    @CalendarType.setter
    def CalendarType(self, value: GregorianCalendarTypes) -> None: ...
    
    @property
    def Eras(self) -> ArrayType[IntType]: ...
    
    @property
    def MaxSupportedDateTime(self) -> DateTime: ...
    
    @property
    def MinSupportedDateTime(self) -> DateTime: ...
    
    @property
    def TwoDigitYearMax(self) -> IntType: ...
    
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddMonths(self, time: DateTime, months: IntType) -> DateTime: ...
    
    def AddYears(self, time: DateTime, years: IntType) -> DateTime: ...
    
    def GetDayOfMonth(self, time: DateTime) -> IntType: ...
    
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek: ...
    
    def GetDayOfYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetDaysInMonth(self, year: IntType, month: IntType, era: IntType) -> IntType: ...
    
    @overload
    def GetDaysInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetEra(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetLeapMonth(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetMonth(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetMonthsInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def IsLeapDay(self, year: IntType, month: IntType, day: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapMonth(self, year: IntType, month: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapYear(self, year: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def ToDateTime(self, year: IntType, month: IntType, day: IntType, hour: IntType, minute: IntType, second: IntType, millisecond: IntType, era: IntType) -> DateTime: ...
    
    def ToFourDigitYear(self, year: IntType) -> IntType: ...
    
    def get_AlgorithmType(self) -> CalendarAlgorithmType: ...
    
    def get_CalendarType(self) -> GregorianCalendarTypes: ...
    
    def get_Eras(self) -> ArrayType[IntType]: ...
    
    def get_MaxSupportedDateTime(self) -> DateTime: ...
    
    def get_MinSupportedDateTime(self) -> DateTime: ...
    
    def get_TwoDigitYearMax(self) -> IntType: ...
    
    def set_CalendarType(self, value: GregorianCalendarTypes) -> VoidType: ...
    
    def set_TwoDigitYearMax(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GregorianCalendarHelper(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Eras(self) -> ArrayType[IntType]: ...
    
    # ---------- Methods ---------- #
    
    def AddMonths(self, time: DateTime, months: IntType) -> DateTime: ...
    
    def AddYears(self, time: DateTime, years: IntType) -> DateTime: ...
    
    def GetDayOfMonth(self, time: DateTime) -> IntType: ...
    
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek: ...
    
    def GetDayOfYear(self, time: DateTime) -> IntType: ...
    
    def GetDaysInMonth(self, year: IntType, month: IntType, era: IntType) -> IntType: ...
    
    def GetDaysInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetEra(self, time: DateTime) -> IntType: ...
    
    def GetLeapMonth(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetMonth(self, time: DateTime) -> IntType: ...
    
    def GetMonthsInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetWeekOfYear(self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek) -> IntType: ...
    
    @overload
    def GetYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetYear(self, year: IntType, time: DateTime) -> IntType: ...
    
    def IsLeapDay(self, year: IntType, month: IntType, day: IntType, era: IntType) -> BooleanType: ...
    
    def IsLeapMonth(self, year: IntType, month: IntType, era: IntType) -> BooleanType: ...
    
    def IsLeapYear(self, year: IntType, era: IntType) -> BooleanType: ...
    
    def ToDateTime(self, year: IntType, month: IntType, day: IntType, hour: IntType, minute: IntType, second: IntType, millisecond: IntType, era: IntType) -> DateTime: ...
    
    def ToFourDigitYear(self, year: IntType, twoDigitYearMax: IntType) -> IntType: ...
    
    def get_Eras(self) -> ArrayType[IntType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HebrewCalendar(Calendar, ICloneable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def HebrewEra() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType: ...
    
    @property
    def Eras(self) -> ArrayType[IntType]: ...
    
    @property
    def MaxSupportedDateTime(self) -> DateTime: ...
    
    @property
    def MinSupportedDateTime(self) -> DateTime: ...
    
    @property
    def TwoDigitYearMax(self) -> IntType: ...
    
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddMonths(self, time: DateTime, months: IntType) -> DateTime: ...
    
    def AddYears(self, time: DateTime, years: IntType) -> DateTime: ...
    
    def GetDayOfMonth(self, time: DateTime) -> IntType: ...
    
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek: ...
    
    def GetDayOfYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetDaysInMonth(self, year: IntType, month: IntType, era: IntType) -> IntType: ...
    
    @overload
    def GetDaysInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetEra(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetLeapMonth(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetMonth(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetMonthsInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def IsLeapDay(self, year: IntType, month: IntType, day: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapMonth(self, year: IntType, month: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapYear(self, year: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def ToDateTime(self, year: IntType, month: IntType, day: IntType, hour: IntType, minute: IntType, second: IntType, millisecond: IntType, era: IntType) -> DateTime: ...
    
    def ToFourDigitYear(self, year: IntType) -> IntType: ...
    
    def get_AlgorithmType(self) -> CalendarAlgorithmType: ...
    
    def get_Eras(self) -> ArrayType[IntType]: ...
    
    def get_MaxSupportedDateTime(self) -> DateTime: ...
    
    def get_MinSupportedDateTime(self) -> DateTime: ...
    
    def get_TwoDigitYearMax(self) -> IntType: ...
    
    def set_TwoDigitYearMax(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HebrewNumber(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HijriCalendar(Calendar, ICloneable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def HijriEra() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType: ...
    
    @property
    def Eras(self) -> ArrayType[IntType]: ...
    
    @property
    def HijriAdjustment(self) -> IntType: ...
    
    @HijriAdjustment.setter
    def HijriAdjustment(self, value: IntType) -> None: ...
    
    @property
    def MaxSupportedDateTime(self) -> DateTime: ...
    
    @property
    def MinSupportedDateTime(self) -> DateTime: ...
    
    @property
    def TwoDigitYearMax(self) -> IntType: ...
    
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddMonths(self, time: DateTime, months: IntType) -> DateTime: ...
    
    def AddYears(self, time: DateTime, years: IntType) -> DateTime: ...
    
    def GetDayOfMonth(self, time: DateTime) -> IntType: ...
    
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek: ...
    
    def GetDayOfYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetDaysInMonth(self, year: IntType, month: IntType, era: IntType) -> IntType: ...
    
    @overload
    def GetDaysInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetEra(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetLeapMonth(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetMonth(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetMonthsInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def IsLeapDay(self, year: IntType, month: IntType, day: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapMonth(self, year: IntType, month: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapYear(self, year: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def ToDateTime(self, year: IntType, month: IntType, day: IntType, hour: IntType, minute: IntType, second: IntType, millisecond: IntType, era: IntType) -> DateTime: ...
    
    def ToFourDigitYear(self, year: IntType) -> IntType: ...
    
    def get_AlgorithmType(self) -> CalendarAlgorithmType: ...
    
    def get_Eras(self) -> ArrayType[IntType]: ...
    
    def get_HijriAdjustment(self) -> IntType: ...
    
    def get_MaxSupportedDateTime(self) -> DateTime: ...
    
    def get_MinSupportedDateTime(self) -> DateTime: ...
    
    def get_TwoDigitYearMax(self) -> IntType: ...
    
    def set_HijriAdjustment(self, value: IntType) -> VoidType: ...
    
    def set_TwoDigitYearMax(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IdnMapping(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AllowUnassigned(self) -> BooleanType: ...
    
    @AllowUnassigned.setter
    def AllowUnassigned(self, value: BooleanType) -> None: ...
    
    @property
    def UseStd3AsciiRules(self) -> BooleanType: ...
    
    @UseStd3AsciiRules.setter
    def UseStd3AsciiRules(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def GetAscii(self, unicode: StringType) -> StringType: ...
    
    @overload
    def GetAscii(self, unicode: StringType, index: IntType) -> StringType: ...
    
    @overload
    def GetAscii(self, unicode: StringType, index: IntType, count: IntType) -> StringType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @overload
    def GetUnicode(self, ascii: StringType) -> StringType: ...
    
    @overload
    def GetUnicode(self, ascii: StringType, index: IntType) -> StringType: ...
    
    @overload
    def GetUnicode(self, ascii: StringType, index: IntType, count: IntType) -> StringType: ...
    
    def get_AllowUnassigned(self) -> BooleanType: ...
    
    def get_UseStd3AsciiRules(self) -> BooleanType: ...
    
    def set_AllowUnassigned(self, value: BooleanType) -> VoidType: ...
    
    def set_UseStd3AsciiRules(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class JapaneseCalendar(Calendar, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType: ...
    
    @property
    def Eras(self) -> ArrayType[IntType]: ...
    
    @property
    def MaxSupportedDateTime(self) -> DateTime: ...
    
    @property
    def MinSupportedDateTime(self) -> DateTime: ...
    
    @property
    def TwoDigitYearMax(self) -> IntType: ...
    
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddMonths(self, time: DateTime, months: IntType) -> DateTime: ...
    
    def AddYears(self, time: DateTime, years: IntType) -> DateTime: ...
    
    def GetDayOfMonth(self, time: DateTime) -> IntType: ...
    
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek: ...
    
    def GetDayOfYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetDaysInMonth(self, year: IntType, month: IntType, era: IntType) -> IntType: ...
    
    @overload
    def GetDaysInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetEra(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetLeapMonth(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetMonth(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetMonthsInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetWeekOfYear(self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek) -> IntType: ...
    
    def GetYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def IsLeapDay(self, year: IntType, month: IntType, day: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapMonth(self, year: IntType, month: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapYear(self, year: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def ToDateTime(self, year: IntType, month: IntType, day: IntType, hour: IntType, minute: IntType, second: IntType, millisecond: IntType, era: IntType) -> DateTime: ...
    
    def ToFourDigitYear(self, year: IntType) -> IntType: ...
    
    def get_AlgorithmType(self) -> CalendarAlgorithmType: ...
    
    def get_Eras(self) -> ArrayType[IntType]: ...
    
    def get_MaxSupportedDateTime(self) -> DateTime: ...
    
    def get_MinSupportedDateTime(self) -> DateTime: ...
    
    def get_TwoDigitYearMax(self) -> IntType: ...
    
    def set_TwoDigitYearMax(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class JapaneseLunisolarCalendar(EastAsianLunisolarCalendar, ICloneable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def JapaneseEra() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Eras(self) -> ArrayType[IntType]: ...
    
    @property
    def MaxSupportedDateTime(self) -> DateTime: ...
    
    @property
    def MinSupportedDateTime(self) -> DateTime: ...
    
    # ---------- Methods ---------- #
    
    def GetEra(self, time: DateTime) -> IntType: ...
    
    def get_Eras(self) -> ArrayType[IntType]: ...
    
    def get_MaxSupportedDateTime(self) -> DateTime: ...
    
    def get_MinSupportedDateTime(self) -> DateTime: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class JulianCalendar(Calendar, ICloneable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def JulianEra() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType: ...
    
    @property
    def Eras(self) -> ArrayType[IntType]: ...
    
    @property
    def MaxSupportedDateTime(self) -> DateTime: ...
    
    @property
    def MinSupportedDateTime(self) -> DateTime: ...
    
    @property
    def TwoDigitYearMax(self) -> IntType: ...
    
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddMonths(self, time: DateTime, months: IntType) -> DateTime: ...
    
    def AddYears(self, time: DateTime, years: IntType) -> DateTime: ...
    
    def GetDayOfMonth(self, time: DateTime) -> IntType: ...
    
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek: ...
    
    def GetDayOfYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetDaysInMonth(self, year: IntType, month: IntType, era: IntType) -> IntType: ...
    
    @overload
    def GetDaysInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetEra(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetLeapMonth(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetMonth(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetMonthsInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def IsLeapDay(self, year: IntType, month: IntType, day: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapMonth(self, year: IntType, month: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapYear(self, year: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def ToDateTime(self, year: IntType, month: IntType, day: IntType, hour: IntType, minute: IntType, second: IntType, millisecond: IntType, era: IntType) -> DateTime: ...
    
    def ToFourDigitYear(self, year: IntType) -> IntType: ...
    
    def get_AlgorithmType(self) -> CalendarAlgorithmType: ...
    
    def get_Eras(self) -> ArrayType[IntType]: ...
    
    def get_MaxSupportedDateTime(self) -> DateTime: ...
    
    def get_MinSupportedDateTime(self) -> DateTime: ...
    
    def get_TwoDigitYearMax(self) -> IntType: ...
    
    def set_TwoDigitYearMax(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class KoreanCalendar(Calendar, ICloneable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def KoreanEra() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType: ...
    
    @property
    def Eras(self) -> ArrayType[IntType]: ...
    
    @property
    def MaxSupportedDateTime(self) -> DateTime: ...
    
    @property
    def MinSupportedDateTime(self) -> DateTime: ...
    
    @property
    def TwoDigitYearMax(self) -> IntType: ...
    
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddMonths(self, time: DateTime, months: IntType) -> DateTime: ...
    
    def AddYears(self, time: DateTime, years: IntType) -> DateTime: ...
    
    def GetDayOfMonth(self, time: DateTime) -> IntType: ...
    
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek: ...
    
    def GetDayOfYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetDaysInMonth(self, year: IntType, month: IntType, era: IntType) -> IntType: ...
    
    @overload
    def GetDaysInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetEra(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetLeapMonth(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetMonth(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetMonthsInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetWeekOfYear(self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek) -> IntType: ...
    
    def GetYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def IsLeapDay(self, year: IntType, month: IntType, day: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapMonth(self, year: IntType, month: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapYear(self, year: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def ToDateTime(self, year: IntType, month: IntType, day: IntType, hour: IntType, minute: IntType, second: IntType, millisecond: IntType, era: IntType) -> DateTime: ...
    
    def ToFourDigitYear(self, year: IntType) -> IntType: ...
    
    def get_AlgorithmType(self) -> CalendarAlgorithmType: ...
    
    def get_Eras(self) -> ArrayType[IntType]: ...
    
    def get_MaxSupportedDateTime(self) -> DateTime: ...
    
    def get_MinSupportedDateTime(self) -> DateTime: ...
    
    def get_TwoDigitYearMax(self) -> IntType: ...
    
    def set_TwoDigitYearMax(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class KoreanLunisolarCalendar(EastAsianLunisolarCalendar, ICloneable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def GregorianEra() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Eras(self) -> ArrayType[IntType]: ...
    
    @property
    def MaxSupportedDateTime(self) -> DateTime: ...
    
    @property
    def MinSupportedDateTime(self) -> DateTime: ...
    
    # ---------- Methods ---------- #
    
    def GetEra(self, time: DateTime) -> IntType: ...
    
    def get_Eras(self) -> ArrayType[IntType]: ...
    
    def get_MaxSupportedDateTime(self) -> DateTime: ...
    
    def get_MinSupportedDateTime(self) -> DateTime: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NumberFormatInfo(ObjectType, ICloneable, IFormatProvider):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CurrencyDecimalDigits(self) -> IntType: ...
    
    @CurrencyDecimalDigits.setter
    def CurrencyDecimalDigits(self, value: IntType) -> None: ...
    
    @property
    def CurrencyDecimalSeparator(self) -> StringType: ...
    
    @CurrencyDecimalSeparator.setter
    def CurrencyDecimalSeparator(self, value: StringType) -> None: ...
    
    @property
    def CurrencyGroupSeparator(self) -> StringType: ...
    
    @CurrencyGroupSeparator.setter
    def CurrencyGroupSeparator(self, value: StringType) -> None: ...
    
    @property
    def CurrencyGroupSizes(self) -> ArrayType[IntType]: ...
    
    @CurrencyGroupSizes.setter
    def CurrencyGroupSizes(self, value: ArrayType[IntType]) -> None: ...
    
    @property
    def CurrencyNegativePattern(self) -> IntType: ...
    
    @CurrencyNegativePattern.setter
    def CurrencyNegativePattern(self, value: IntType) -> None: ...
    
    @property
    def CurrencyPositivePattern(self) -> IntType: ...
    
    @CurrencyPositivePattern.setter
    def CurrencyPositivePattern(self, value: IntType) -> None: ...
    
    @property
    def CurrencySymbol(self) -> StringType: ...
    
    @CurrencySymbol.setter
    def CurrencySymbol(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def CurrentInfo() -> NumberFormatInfo: ...
    
    @property
    def DigitSubstitution(self) -> DigitShapes: ...
    
    @DigitSubstitution.setter
    def DigitSubstitution(self, value: DigitShapes) -> None: ...
    
    @staticmethod
    @property
    def InvariantInfo() -> NumberFormatInfo: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def NaNSymbol(self) -> StringType: ...
    
    @NaNSymbol.setter
    def NaNSymbol(self, value: StringType) -> None: ...
    
    @property
    def NativeDigits(self) -> ArrayType[StringType]: ...
    
    @NativeDigits.setter
    def NativeDigits(self, value: ArrayType[StringType]) -> None: ...
    
    @property
    def NegativeInfinitySymbol(self) -> StringType: ...
    
    @NegativeInfinitySymbol.setter
    def NegativeInfinitySymbol(self, value: StringType) -> None: ...
    
    @property
    def NegativeSign(self) -> StringType: ...
    
    @NegativeSign.setter
    def NegativeSign(self, value: StringType) -> None: ...
    
    @property
    def NumberDecimalDigits(self) -> IntType: ...
    
    @NumberDecimalDigits.setter
    def NumberDecimalDigits(self, value: IntType) -> None: ...
    
    @property
    def NumberDecimalSeparator(self) -> StringType: ...
    
    @NumberDecimalSeparator.setter
    def NumberDecimalSeparator(self, value: StringType) -> None: ...
    
    @property
    def NumberGroupSeparator(self) -> StringType: ...
    
    @NumberGroupSeparator.setter
    def NumberGroupSeparator(self, value: StringType) -> None: ...
    
    @property
    def NumberGroupSizes(self) -> ArrayType[IntType]: ...
    
    @NumberGroupSizes.setter
    def NumberGroupSizes(self, value: ArrayType[IntType]) -> None: ...
    
    @property
    def NumberNegativePattern(self) -> IntType: ...
    
    @NumberNegativePattern.setter
    def NumberNegativePattern(self, value: IntType) -> None: ...
    
    @property
    def PerMilleSymbol(self) -> StringType: ...
    
    @PerMilleSymbol.setter
    def PerMilleSymbol(self, value: StringType) -> None: ...
    
    @property
    def PercentDecimalDigits(self) -> IntType: ...
    
    @PercentDecimalDigits.setter
    def PercentDecimalDigits(self, value: IntType) -> None: ...
    
    @property
    def PercentDecimalSeparator(self) -> StringType: ...
    
    @PercentDecimalSeparator.setter
    def PercentDecimalSeparator(self, value: StringType) -> None: ...
    
    @property
    def PercentGroupSeparator(self) -> StringType: ...
    
    @PercentGroupSeparator.setter
    def PercentGroupSeparator(self, value: StringType) -> None: ...
    
    @property
    def PercentGroupSizes(self) -> ArrayType[IntType]: ...
    
    @PercentGroupSizes.setter
    def PercentGroupSizes(self, value: ArrayType[IntType]) -> None: ...
    
    @property
    def PercentNegativePattern(self) -> IntType: ...
    
    @PercentNegativePattern.setter
    def PercentNegativePattern(self, value: IntType) -> None: ...
    
    @property
    def PercentPositivePattern(self) -> IntType: ...
    
    @PercentPositivePattern.setter
    def PercentPositivePattern(self, value: IntType) -> None: ...
    
    @property
    def PercentSymbol(self) -> StringType: ...
    
    @PercentSymbol.setter
    def PercentSymbol(self, value: StringType) -> None: ...
    
    @property
    def PositiveInfinitySymbol(self) -> StringType: ...
    
    @PositiveInfinitySymbol.setter
    def PositiveInfinitySymbol(self, value: StringType) -> None: ...
    
    @property
    def PositiveSign(self) -> StringType: ...
    
    @PositiveSign.setter
    def PositiveSign(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ObjectType: ...
    
    def GetFormat(self, formatType: TypeType) -> ObjectType: ...
    
    @staticmethod
    def GetInstance(formatProvider: IFormatProvider) -> NumberFormatInfo: ...
    
    @staticmethod
    def ReadOnly(nfi: NumberFormatInfo) -> NumberFormatInfo: ...
    
    def get_CurrencyDecimalDigits(self) -> IntType: ...
    
    def get_CurrencyDecimalSeparator(self) -> StringType: ...
    
    def get_CurrencyGroupSeparator(self) -> StringType: ...
    
    def get_CurrencyGroupSizes(self) -> ArrayType[IntType]: ...
    
    def get_CurrencyNegativePattern(self) -> IntType: ...
    
    def get_CurrencyPositivePattern(self) -> IntType: ...
    
    def get_CurrencySymbol(self) -> StringType: ...
    
    @staticmethod
    def get_CurrentInfo() -> NumberFormatInfo: ...
    
    def get_DigitSubstitution(self) -> DigitShapes: ...
    
    @staticmethod
    def get_InvariantInfo() -> NumberFormatInfo: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_NaNSymbol(self) -> StringType: ...
    
    def get_NativeDigits(self) -> ArrayType[StringType]: ...
    
    def get_NegativeInfinitySymbol(self) -> StringType: ...
    
    def get_NegativeSign(self) -> StringType: ...
    
    def get_NumberDecimalDigits(self) -> IntType: ...
    
    def get_NumberDecimalSeparator(self) -> StringType: ...
    
    def get_NumberGroupSeparator(self) -> StringType: ...
    
    def get_NumberGroupSizes(self) -> ArrayType[IntType]: ...
    
    def get_NumberNegativePattern(self) -> IntType: ...
    
    def get_PerMilleSymbol(self) -> StringType: ...
    
    def get_PercentDecimalDigits(self) -> IntType: ...
    
    def get_PercentDecimalSeparator(self) -> StringType: ...
    
    def get_PercentGroupSeparator(self) -> StringType: ...
    
    def get_PercentGroupSizes(self) -> ArrayType[IntType]: ...
    
    def get_PercentNegativePattern(self) -> IntType: ...
    
    def get_PercentPositivePattern(self) -> IntType: ...
    
    def get_PercentSymbol(self) -> StringType: ...
    
    def get_PositiveInfinitySymbol(self) -> StringType: ...
    
    def get_PositiveSign(self) -> StringType: ...
    
    def set_CurrencyDecimalDigits(self, value: IntType) -> VoidType: ...
    
    def set_CurrencyDecimalSeparator(self, value: StringType) -> VoidType: ...
    
    def set_CurrencyGroupSeparator(self, value: StringType) -> VoidType: ...
    
    def set_CurrencyGroupSizes(self, value: ArrayType[IntType]) -> VoidType: ...
    
    def set_CurrencyNegativePattern(self, value: IntType) -> VoidType: ...
    
    def set_CurrencyPositivePattern(self, value: IntType) -> VoidType: ...
    
    def set_CurrencySymbol(self, value: StringType) -> VoidType: ...
    
    def set_DigitSubstitution(self, value: DigitShapes) -> VoidType: ...
    
    def set_NaNSymbol(self, value: StringType) -> VoidType: ...
    
    def set_NativeDigits(self, value: ArrayType[StringType]) -> VoidType: ...
    
    def set_NegativeInfinitySymbol(self, value: StringType) -> VoidType: ...
    
    def set_NegativeSign(self, value: StringType) -> VoidType: ...
    
    def set_NumberDecimalDigits(self, value: IntType) -> VoidType: ...
    
    def set_NumberDecimalSeparator(self, value: StringType) -> VoidType: ...
    
    def set_NumberGroupSeparator(self, value: StringType) -> VoidType: ...
    
    def set_NumberGroupSizes(self, value: ArrayType[IntType]) -> VoidType: ...
    
    def set_NumberNegativePattern(self, value: IntType) -> VoidType: ...
    
    def set_PerMilleSymbol(self, value: StringType) -> VoidType: ...
    
    def set_PercentDecimalDigits(self, value: IntType) -> VoidType: ...
    
    def set_PercentDecimalSeparator(self, value: StringType) -> VoidType: ...
    
    def set_PercentGroupSeparator(self, value: StringType) -> VoidType: ...
    
    def set_PercentGroupSizes(self, value: ArrayType[IntType]) -> VoidType: ...
    
    def set_PercentNegativePattern(self, value: IntType) -> VoidType: ...
    
    def set_PercentPositivePattern(self, value: IntType) -> VoidType: ...
    
    def set_PercentSymbol(self, value: StringType) -> VoidType: ...
    
    def set_PositiveInfinitySymbol(self, value: StringType) -> VoidType: ...
    
    def set_PositiveSign(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PersianCalendar(Calendar, ICloneable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def PersianEra() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType: ...
    
    @property
    def Eras(self) -> ArrayType[IntType]: ...
    
    @property
    def MaxSupportedDateTime(self) -> DateTime: ...
    
    @property
    def MinSupportedDateTime(self) -> DateTime: ...
    
    @property
    def TwoDigitYearMax(self) -> IntType: ...
    
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddMonths(self, time: DateTime, months: IntType) -> DateTime: ...
    
    def AddYears(self, time: DateTime, years: IntType) -> DateTime: ...
    
    def GetDayOfMonth(self, time: DateTime) -> IntType: ...
    
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek: ...
    
    def GetDayOfYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetDaysInMonth(self, year: IntType, month: IntType, era: IntType) -> IntType: ...
    
    @overload
    def GetDaysInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetEra(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetLeapMonth(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetMonth(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetMonthsInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def IsLeapDay(self, year: IntType, month: IntType, day: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapMonth(self, year: IntType, month: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapYear(self, year: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def ToDateTime(self, year: IntType, month: IntType, day: IntType, hour: IntType, minute: IntType, second: IntType, millisecond: IntType, era: IntType) -> DateTime: ...
    
    def ToFourDigitYear(self, year: IntType) -> IntType: ...
    
    def get_AlgorithmType(self) -> CalendarAlgorithmType: ...
    
    def get_Eras(self) -> ArrayType[IntType]: ...
    
    def get_MaxSupportedDateTime(self) -> DateTime: ...
    
    def get_MinSupportedDateTime(self) -> DateTime: ...
    
    def get_TwoDigitYearMax(self) -> IntType: ...
    
    def set_TwoDigitYearMax(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegionInfo(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, name: StringType): ...
    
    @overload
    def __init__(self, culture: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CurrencyEnglishName(self) -> StringType: ...
    
    @property
    def CurrencyNativeName(self) -> StringType: ...
    
    @property
    def CurrencySymbol(self) -> StringType: ...
    
    @staticmethod
    @property
    def CurrentRegion() -> RegionInfo: ...
    
    @property
    def DisplayName(self) -> StringType: ...
    
    @property
    def EnglishName(self) -> StringType: ...
    
    @property
    def GeoId(self) -> IntType: ...
    
    @property
    def ISOCurrencySymbol(self) -> StringType: ...
    
    @property
    def IsMetric(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NativeName(self) -> StringType: ...
    
    @property
    def ThreeLetterISORegionName(self) -> StringType: ...
    
    @property
    def ThreeLetterWindowsRegionName(self) -> StringType: ...
    
    @property
    def TwoLetterISORegionName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_CurrencyEnglishName(self) -> StringType: ...
    
    def get_CurrencyNativeName(self) -> StringType: ...
    
    def get_CurrencySymbol(self) -> StringType: ...
    
    @staticmethod
    def get_CurrentRegion() -> RegionInfo: ...
    
    def get_DisplayName(self) -> StringType: ...
    
    def get_EnglishName(self) -> StringType: ...
    
    def get_GeoId(self) -> IntType: ...
    
    def get_ISOCurrencySymbol(self) -> StringType: ...
    
    def get_IsMetric(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NativeName(self) -> StringType: ...
    
    def get_ThreeLetterISORegionName(self) -> StringType: ...
    
    def get_ThreeLetterWindowsRegionName(self) -> StringType: ...
    
    def get_TwoLetterISORegionName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SortKey(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def KeyData(self) -> ArrayType[ByteType]: ...
    
    @property
    def OriginalString(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Compare(sortkey1: SortKey, sortkey2: SortKey) -> IntType: ...
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_KeyData(self) -> ArrayType[ByteType]: ...
    
    def get_OriginalString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SortVersion(ObjectType, IEquatable[SortVersion]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, fullVersion: IntType, sortId: Guid): ...
    
    # ---------- Properties ---------- #
    
    @property
    def FullVersion(self) -> IntType: ...
    
    @property
    def SortId(self) -> Guid: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: SortVersion) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_FullVersion(self) -> IntType: ...
    
    def get_SortId(self) -> Guid: ...
    
    @staticmethod
    def op_Equality(left: SortVersion, right: SortVersion) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: SortVersion, right: SortVersion) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringInfo(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def LengthInTextElements(self) -> IntType: ...
    
    @property
    def String(self) -> StringType: ...
    
    @String.setter
    def String(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    @overload
    def GetNextTextElement(str: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def GetNextTextElement(str: StringType, index: IntType) -> StringType: ...
    
    @staticmethod
    @overload
    def GetTextElementEnumerator(str: StringType) -> TextElementEnumerator: ...
    
    @staticmethod
    @overload
    def GetTextElementEnumerator(str: StringType, index: IntType) -> TextElementEnumerator: ...
    
    @staticmethod
    def ParseCombiningCharacters(str: StringType) -> ArrayType[IntType]: ...
    
    @overload
    def SubstringByTextElements(self, startingTextElement: IntType) -> StringType: ...
    
    @overload
    def SubstringByTextElements(self, startingTextElement: IntType, lengthInTextElements: IntType) -> StringType: ...
    
    def get_LengthInTextElements(self) -> IntType: ...
    
    def get_String(self) -> StringType: ...
    
    def set_String(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TaiwanCalendar(Calendar, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType: ...
    
    @property
    def Eras(self) -> ArrayType[IntType]: ...
    
    @property
    def MaxSupportedDateTime(self) -> DateTime: ...
    
    @property
    def MinSupportedDateTime(self) -> DateTime: ...
    
    @property
    def TwoDigitYearMax(self) -> IntType: ...
    
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddMonths(self, time: DateTime, months: IntType) -> DateTime: ...
    
    def AddYears(self, time: DateTime, years: IntType) -> DateTime: ...
    
    def GetDayOfMonth(self, time: DateTime) -> IntType: ...
    
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek: ...
    
    def GetDayOfYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetDaysInMonth(self, year: IntType, month: IntType, era: IntType) -> IntType: ...
    
    @overload
    def GetDaysInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetEra(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetLeapMonth(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetMonth(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetMonthsInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetWeekOfYear(self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek) -> IntType: ...
    
    def GetYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def IsLeapDay(self, year: IntType, month: IntType, day: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapMonth(self, year: IntType, month: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapYear(self, year: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def ToDateTime(self, year: IntType, month: IntType, day: IntType, hour: IntType, minute: IntType, second: IntType, millisecond: IntType, era: IntType) -> DateTime: ...
    
    def ToFourDigitYear(self, year: IntType) -> IntType: ...
    
    def get_AlgorithmType(self) -> CalendarAlgorithmType: ...
    
    def get_Eras(self) -> ArrayType[IntType]: ...
    
    def get_MaxSupportedDateTime(self) -> DateTime: ...
    
    def get_MinSupportedDateTime(self) -> DateTime: ...
    
    def get_TwoDigitYearMax(self) -> IntType: ...
    
    def set_TwoDigitYearMax(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TaiwanLunisolarCalendar(EastAsianLunisolarCalendar, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Eras(self) -> ArrayType[IntType]: ...
    
    @property
    def MaxSupportedDateTime(self) -> DateTime: ...
    
    @property
    def MinSupportedDateTime(self) -> DateTime: ...
    
    # ---------- Methods ---------- #
    
    def GetEra(self, time: DateTime) -> IntType: ...
    
    def get_Eras(self) -> ArrayType[IntType]: ...
    
    def get_MaxSupportedDateTime(self) -> DateTime: ...
    
    def get_MinSupportedDateTime(self) -> DateTime: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TextElementEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    @property
    def ElementIndex(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetTextElement(self) -> StringType: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    def get_ElementIndex(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TextInfo(ObjectType, ICloneable, IDeserializationCallback):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ANSICodePage(self) -> IntType: ...
    
    @property
    def CultureName(self) -> StringType: ...
    
    @property
    def EBCDICCodePage(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def IsRightToLeft(self) -> BooleanType: ...
    
    @property
    def LCID(self) -> IntType: ...
    
    @property
    def ListSeparator(self) -> StringType: ...
    
    @ListSeparator.setter
    def ListSeparator(self, value: StringType) -> None: ...
    
    @property
    def MacCodePage(self) -> IntType: ...
    
    @property
    def OEMCodePage(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ObjectType: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    def ReadOnly(textInfo: TextInfo) -> TextInfo: ...
    
    @overload
    def ToLower(self, c: CharType) -> CharType: ...
    
    @overload
    def ToLower(self, str: StringType) -> StringType: ...
    
    def ToString(self) -> StringType: ...
    
    def ToTitleCase(self, str: StringType) -> StringType: ...
    
    @overload
    def ToUpper(self, c: CharType) -> CharType: ...
    
    @overload
    def ToUpper(self, str: StringType) -> StringType: ...
    
    def get_ANSICodePage(self) -> IntType: ...
    
    def get_CultureName(self) -> StringType: ...
    
    def get_EBCDICCodePage(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_IsRightToLeft(self) -> BooleanType: ...
    
    def get_LCID(self) -> IntType: ...
    
    def get_ListSeparator(self) -> StringType: ...
    
    def get_MacCodePage(self) -> IntType: ...
    
    def get_OEMCodePage(self) -> IntType: ...
    
    def set_ListSeparator(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ThaiBuddhistCalendar(Calendar, ICloneable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def ThaiBuddhistEra() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType: ...
    
    @property
    def Eras(self) -> ArrayType[IntType]: ...
    
    @property
    def MaxSupportedDateTime(self) -> DateTime: ...
    
    @property
    def MinSupportedDateTime(self) -> DateTime: ...
    
    @property
    def TwoDigitYearMax(self) -> IntType: ...
    
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddMonths(self, time: DateTime, months: IntType) -> DateTime: ...
    
    def AddYears(self, time: DateTime, years: IntType) -> DateTime: ...
    
    def GetDayOfMonth(self, time: DateTime) -> IntType: ...
    
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek: ...
    
    def GetDayOfYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetDaysInMonth(self, year: IntType, month: IntType, era: IntType) -> IntType: ...
    
    @overload
    def GetDaysInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetEra(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetLeapMonth(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetMonth(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetMonthsInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetWeekOfYear(self, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek) -> IntType: ...
    
    def GetYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def IsLeapDay(self, year: IntType, month: IntType, day: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapMonth(self, year: IntType, month: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapYear(self, year: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def ToDateTime(self, year: IntType, month: IntType, day: IntType, hour: IntType, minute: IntType, second: IntType, millisecond: IntType, era: IntType) -> DateTime: ...
    
    def ToFourDigitYear(self, year: IntType) -> IntType: ...
    
    def get_AlgorithmType(self) -> CalendarAlgorithmType: ...
    
    def get_Eras(self) -> ArrayType[IntType]: ...
    
    def get_MaxSupportedDateTime(self) -> DateTime: ...
    
    def get_MinSupportedDateTime(self) -> DateTime: ...
    
    def get_TwoDigitYearMax(self) -> IntType: ...
    
    def set_TwoDigitYearMax(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TimeSpanFormat(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TimeSpanParse(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TokenHashValue(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UmAlQuraCalendar(Calendar, ICloneable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def UmAlQuraEra() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType: ...
    
    @property
    def Eras(self) -> ArrayType[IntType]: ...
    
    @property
    def MaxSupportedDateTime(self) -> DateTime: ...
    
    @property
    def MinSupportedDateTime(self) -> DateTime: ...
    
    @property
    def TwoDigitYearMax(self) -> IntType: ...
    
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddMonths(self, time: DateTime, months: IntType) -> DateTime: ...
    
    def AddYears(self, time: DateTime, years: IntType) -> DateTime: ...
    
    def GetDayOfMonth(self, time: DateTime) -> IntType: ...
    
    def GetDayOfWeek(self, time: DateTime) -> DayOfWeek: ...
    
    def GetDayOfYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetDaysInMonth(self, year: IntType, month: IntType, era: IntType) -> IntType: ...
    
    @overload
    def GetDaysInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetEra(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetLeapMonth(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetMonth(self, time: DateTime) -> IntType: ...
    
    @overload
    def GetMonthsInYear(self, year: IntType, era: IntType) -> IntType: ...
    
    def GetYear(self, time: DateTime) -> IntType: ...
    
    @overload
    def IsLeapDay(self, year: IntType, month: IntType, day: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapMonth(self, year: IntType, month: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def IsLeapYear(self, year: IntType, era: IntType) -> BooleanType: ...
    
    @overload
    def ToDateTime(self, year: IntType, month: IntType, day: IntType, hour: IntType, minute: IntType, second: IntType, millisecond: IntType, era: IntType) -> DateTime: ...
    
    def ToFourDigitYear(self, year: IntType) -> IntType: ...
    
    def get_AlgorithmType(self) -> CalendarAlgorithmType: ...
    
    def get_Eras(self) -> ArrayType[IntType]: ...
    
    def get_MaxSupportedDateTime(self) -> DateTime: ...
    
    def get_MinSupportedDateTime(self) -> DateTime: ...
    
    def get_TwoDigitYearMax(self) -> IntType: ...
    
    def set_TwoDigitYearMax(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class DaylightTimeStruct(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, start: DateTime, end: DateTime, delta: TimeSpan): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Delta(self) -> TimeSpan: ...
    
    @property
    def End(self) -> DateTime: ...
    
    @property
    def Start(self) -> DateTime: ...
    
    # ---------- Methods ---------- #
    
    def get_Delta(self) -> TimeSpan: ...
    
    def get_End(self) -> DateTime: ...
    
    def get_Start(self) -> DateTime: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HebrewNumberParsingContext(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, result: IntType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalCodePageDataItem(ValueType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalEncodingDataItem(ValueType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Interfaces

# ---------- Enums ---------- #

class BidiCategory(Enum):
    LeftToRight: IntType = 0
    LeftToRightEmbedding: IntType = 1
    LeftToRightOverride: IntType = 2
    RightToLeft: IntType = 3
    RightToLeftArabic: IntType = 4
    RightToLeftEmbedding: IntType = 5
    RightToLeftOverride: IntType = 6
    PopDirectionalFormat: IntType = 7
    EuropeanNumber: IntType = 8
    EuropeanNumberSeparator: IntType = 9
    EuropeanNumberTerminator: IntType = 10
    ArabicNumber: IntType = 11
    CommonNumberSeparator: IntType = 12
    NonSpacingMark: IntType = 13
    BoundaryNeutral: IntType = 14
    ParagraphSeparator: IntType = 15
    SegmentSeparator: IntType = 16
    Whitespace: IntType = 17
    OtherNeutrals: IntType = 18
    LeftToRightIsolate: IntType = 19
    RightToLeftIsolate: IntType = 20
    FirstStrongIsolate: IntType = 21
    PopDirectionIsolate: IntType = 22


class CalendarAlgorithmType(Enum):
    Unknown: IntType = 0
    SolarCalendar: IntType = 1
    LunarCalendar: IntType = 2
    LunisolarCalendar: IntType = 3


class CalendarId(Enum):
    GREGORIAN: UShortType = 1
    GREGORIAN_US: UShortType = 2
    JAPAN: UShortType = 3
    TAIWAN: UShortType = 4
    KOREA: UShortType = 5
    HIJRI: UShortType = 6
    THAI: UShortType = 7
    HEBREW: UShortType = 8
    GREGORIAN_ME_FRENCH: UShortType = 9
    GREGORIAN_ARABIC: UShortType = 10
    GREGORIAN_XLIT_ENGLISH: UShortType = 11
    GREGORIAN_XLIT_FRENCH: UShortType = 12
    JULIAN: UShortType = 13
    JAPANESELUNISOLAR: UShortType = 14
    CHINESELUNISOLAR: UShortType = 15
    SAKA: UShortType = 16
    LUNAR_ETO_CHN: UShortType = 17
    LUNAR_ETO_KOR: UShortType = 18
    LUNAR_ETO_ROKUYOU: UShortType = 19
    KOREANLUNISOLAR: UShortType = 20
    TAIWANLUNISOLAR: UShortType = 21
    PERSIAN: UShortType = 22
    UMALQURA: UShortType = 23
    LAST_CALENDAR: UShortType = 23


class CalendarWeekRule(Enum):
    FirstDay: IntType = 0
    FirstFullWeek: IntType = 1
    FirstFourDayWeek: IntType = 2


class CompareOptions(Enum):
    #None: IntType = 0
    IgnoreCase: IntType = 1
    IgnoreNonSpace: IntType = 2
    IgnoreSymbols: IntType = 4
    IgnoreKanaType: IntType = 8
    IgnoreWidth: IntType = 16
    OrdinalIgnoreCase: IntType = 268435456
    StringSort: IntType = 536870912
    Ordinal: IntType = 1073741824


class CultureTypes(Enum):
    NeutralCultures: IntType = 1
    SpecificCultures: IntType = 2
    InstalledWin32Cultures: IntType = 4
    AllCultures: IntType = 7
    UserCustomCulture: IntType = 8
    ReplacementCultures: IntType = 16
    WindowsOnlyCultures: IntType = 32
    FrameworkCultures: IntType = 64


class DateTimeFormatFlags(Enum):
    NotInitialized: IntType = -1
    #None: IntType = 0
    UseGenitiveMonth: IntType = 1
    UseLeapYearMonth: IntType = 2
    UseSpacesInMonthNames: IntType = 4
    UseHebrewRule: IntType = 8
    UseSpacesInDayNames: IntType = 16
    UseDigitPrefixInTokens: IntType = 32


class DateTimeStyles(Enum):
    #None: IntType = 0
    AllowLeadingWhite: IntType = 1
    AllowTrailingWhite: IntType = 2
    AllowInnerWhite: IntType = 4
    AllowWhiteSpaces: IntType = 7
    NoCurrentDateDefault: IntType = 8
    AdjustToUniversal: IntType = 16
    AssumeLocal: IntType = 32
    AssumeUniversal: IntType = 64
    RoundtripKind: IntType = 128


class DigitShapes(Enum):
    Context: IntType = 0
    #None: IntType = 1
    NativeNational: IntType = 2


class FORMATFLAGS(Enum):
    #None: IntType = 0
    UseGenitiveMonth: IntType = 1
    UseLeapYearMonth: IntType = 2
    UseSpacesInMonthNames: IntType = 4
    UseHebrewParsing: IntType = 8
    UseSpacesInDayNames: IntType = 16
    UseDigitPrefixInTokens: IntType = 32


class GregorianCalendarTypes(Enum):
    Localized: IntType = 1
    USEnglish: IntType = 2
    MiddleEastFrench: IntType = 9
    Arabic: IntType = 10
    TransliteratedEnglish: IntType = 11
    TransliteratedFrench: IntType = 12


class HebrewNumberParsingState(Enum):
    InvalidHebrewNumber: IntType = 0
    NotHebrewDigit: IntType = 1
    FoundEndOfHebrewNumber: IntType = 2
    ContinueParsing: IntType = 3


class MonthNameStyles(Enum):
    Regular: IntType = 0
    Genitive: IntType = 1
    LeapYear: IntType = 2


class NumberStyles(Enum):
    #None: IntType = 0
    AllowLeadingWhite: IntType = 1
    AllowTrailingWhite: IntType = 2
    AllowLeadingSign: IntType = 4
    Integer: IntType = 7
    AllowTrailingSign: IntType = 8
    AllowParentheses: IntType = 16
    AllowDecimalPoint: IntType = 32
    AllowThousands: IntType = 64
    Number: IntType = 111
    AllowExponent: IntType = 128
    Float: IntType = 167
    AllowCurrencySymbol: IntType = 256
    Currency: IntType = 383
    Any: IntType = 511
    AllowHexSpecifier: IntType = 512
    HexNumber: IntType = 515


class TimeSpanStyles(Enum):
    #None: IntType = 0
    AssumeNegative: IntType = 1


class UnicodeCategory(Enum):
    UppercaseLetter: IntType = 0
    LowercaseLetter: IntType = 1
    TitlecaseLetter: IntType = 2
    ModifierLetter: IntType = 3
    OtherLetter: IntType = 4
    NonSpacingMark: IntType = 5
    SpacingCombiningMark: IntType = 6
    EnclosingMark: IntType = 7
    DecimalDigitNumber: IntType = 8
    LetterNumber: IntType = 9
    OtherNumber: IntType = 10
    SpaceSeparator: IntType = 11
    LineSeparator: IntType = 12
    ParagraphSeparator: IntType = 13
    Control: IntType = 14
    Format: IntType = 15
    Surrogate: IntType = 16
    PrivateUse: IntType = 17
    ConnectorPunctuation: IntType = 18
    DashPunctuation: IntType = 19
    OpenPunctuation: IntType = 20
    ClosePunctuation: IntType = 21
    InitialQuotePunctuation: IntType = 22
    FinalQuotePunctuation: IntType = 23
    OtherPunctuation: IntType = 24
    MathSymbol: IntType = 25
    CurrencySymbol: IntType = 26
    ModifierSymbol: IntType = 27
    OtherSymbol: IntType = 28
    OtherNotAssigned: IntType = 29


# No Delegates

__all__ = [
    AppDomainSortingSetupInfo,
    Calendar,
    CalendarData,
    CalendricalCalculationsHelper,
    CharUnicodeInfo,
    ChineseLunisolarCalendar,
    CodePageDataItem,
    CompareInfo,
    CultureData,
    CultureInfo,
    CultureNotFoundException,
    DateTimeFormatInfo,
    DateTimeFormatInfoScanner,
    DaylightTime,
    EastAsianLunisolarCalendar,
    EncodingTable,
    EraInfo,
    GlobalizationAssembly,
    GlobalizationExtensions,
    GregorianCalendar,
    GregorianCalendarHelper,
    HebrewCalendar,
    HebrewNumber,
    HijriCalendar,
    IdnMapping,
    JapaneseCalendar,
    JapaneseLunisolarCalendar,
    JulianCalendar,
    KoreanCalendar,
    KoreanLunisolarCalendar,
    NumberFormatInfo,
    PersianCalendar,
    RegionInfo,
    SortKey,
    SortVersion,
    StringInfo,
    TaiwanCalendar,
    TaiwanLunisolarCalendar,
    TextElementEnumerator,
    TextInfo,
    ThaiBuddhistCalendar,
    TimeSpanFormat,
    TimeSpanParse,
    TokenHashValue,
    UmAlQuraCalendar,
    DaylightTimeStruct,
    HebrewNumberParsingContext,
    InternalCodePageDataItem,
    InternalEncodingDataItem,
    BidiCategory,
    CalendarAlgorithmType,
    CalendarId,
    CalendarWeekRule,
    CompareOptions,
    CultureTypes,
    DateTimeFormatFlags,
    DateTimeStyles,
    DigitShapes,
    FORMATFLAGS,
    GregorianCalendarTypes,
    HebrewNumberParsingState,
    MonthNameStyles,
    NumberStyles,
    TimeSpanStyles,
    UnicodeCategory,
]
