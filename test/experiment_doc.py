from __future__ import annotations

from typing import Any
from typing import List
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Set


class DocDict:
    doc_tree: Mapping[str, Any]
    imports: Set[str] = set()
    type_vars: Set[str] = set()

    def __init__(self, doc_tree: Mapping[str, Any]):
        self.doc_tree = doc_tree

    @staticmethod
    def split(text: str, indent: int = 0, line_limit: int = 100, prefix: str = "") -> Sequence[str]:
        lines: List[str] = []
        for doc_paragraph in text.splitlines():
            words: List[str] = doc_paragraph.split(" ")
            doc_line: str = ("    " * indent) + words[0]
            for word in words[1:]:
                if len(doc_line) + len(word) + 1 > line_limit:
                    lines.append(doc_line)
                    doc_line = ("    " * indent) + prefix + word
                else:
                    doc_line += " " + word
            lines.append(doc_line)
        return lines

    def get_doc(self, type_str: str, indent: int = 0, line_limit: int = 100) -> str:
        search: str
        doc_dict: Mapping[str, Any] = self.doc_tree
        while True:
            if type_str in doc_dict:
                doc_dict = doc_dict[type_str]
                break
            if "." in type_str:
                search, type_str = type_str.split(".", 1)
            else:
                search = type_str
            if search not in doc_dict:
                return f'{"    " * indent}""""""'
            doc_dict = doc_dict[search]

        doc: str = doc_dict.get("doc", "")
        parameters: Mapping[str, str] = doc_dict.get("parameters", {})
        return_str: Optional[str] = doc_dict.get("return", None)
        exceptions: Mapping[str, str] = doc_dict.get("exceptions", {})
        if len(parameters) == 0 and return_str is None and len(exceptions) == 0:
            if doc == "":
                return f'{"    " * indent}""""""'
            if "\n" not in doc and 4 * indent + len(doc) + 3 <= line_limit:
                return f'{"    " * indent}"""{doc}"""'

        doc = '"""' + doc.replace("\n", "\n\n")
        doc_lines: List[str] = list(self.split(doc, indent, line_limit))

        if len(parameters) > 0 or return_str is not None or len(exceptions) > 0:
            doc_lines.append("")

            for param, param_doc in parameters.items():
                param_str: str = f":param {param}: {param_doc}"
                doc_lines.extend(self.split(param_str, indent, line_limit, "  "))

            if return_str is not None:
                doc_lines.extend(self.split(f":return: {return_str}", indent, line_limit, "  "))

            for exception, exception_doc in exceptions.items():
                param_str: str = f":except {exception}: {exception_doc}"
                doc_lines.extend(self.split(param_str, indent, line_limit, "  "))

        doc_formatted: Mapping[str, Sequence[str]] = doc_dict.get("doc_formatted", {})
        line_index: int = 0
        while line_index < len(doc_lines):
            line: str = doc_lines[line_index]
            for replace_str, replace_seq in doc_formatted.items():
                replace_str = f"%{replace_str}%"
                if replace_str in line:
                    doc_lines[line_index] = line.replace(replace_str, replace_seq[0])
                    for new_line in reversed(replace_seq[1:]):
                        doc_lines.insert(line_index + 1, ("    " * indent) + new_line)
            line_index += 1

        doc_lines.append(("    " * indent) + '"""')
        return "\n".join(doc_lines)


def main() -> None:
    doc_tree = {
        "System": {
            "doc": "Contains fundamental classes and base classes that define commonly-used value and reference data types, events and event handlers, interfaces, attributes, and processing exceptions.",
            "IComparable": {
                "doc": "Defines a generalized type-specific comparison method that a value type or class implements to order or sort its instances.",
                "CompareTo(System.Object)": {
                    "doc": "Compares the current instance with another object of the same type and returns an integer that indicates whether the current instance precedes, follows, or occurs in the same position in the sort order as the other object.",
                    "doc_formatted": {},
                    "parameters": {"obj": "An object to compare with this instance."},
                    "return": "A value that indicates the relative order of the objects being compared. The return value has these meanings:\nLess than zero - This instance precedes obj in the sort order.\nZero - This instance occurs in the same position in the sort order as obj.\nGreater than zero - This instance follows obj in the sort order.",
                    "exceptions": {
                        "ArgumentException": "obj is not the same type as this instance."
                    },
                },
            },
            "IComparable[System.$T]": {
                "doc": "Defines a generalized comparison method that a value type or class implements to create a type-specific comparison method for ordering or sorting its instances.",
                "CompareTo(System.$T)": {
                    "doc": "Compares the current instance with another object of the same type and returns an integer that indicates whether the current instance precedes, follows, or occurs in the same position in the sort order as the other object.",
                    "doc_formatted": {},
                    "parameters": {"other": "An object to compare with this instance."},
                    "return": "A value that indicates the relative order of the objects being compared. The return value has these meanings:\nLess than zero - This instance precedes other in the sort order.\nZero - This instance occurs in the same position in the sort order as other.\nGreater than zero - This instance follows other in the sort order.",
                    "exceptions": {},
                },
            },
            "IEquatable[System.$T]": {
                "doc": "Defines a generalized method that a value type or class implements to create a type-specific method for determining equality of instances.",
                "Equals(System.$T)": {
                    "doc": "Indicates whether the current object is equal to another object of the same type.",
                    "doc_formatted": {},
                    "parameters": {"other": "An object to compare with this object."},
                    "return": "true if the current object is equal to the other parameter; otherwise, false.",
                    "exceptions": {},
                },
            },
            "IFormattable": {
                "doc": "Provides functionality to format the value of an object into a string representation.",
                "ToString(System.?String, System.IFormatProvider)": {
                    "doc": "Formats the value of the current instance using the specified format.",
                    "doc_formatted": {},
                    "parameters": {
                        "format": "The format to use. -or- A null reference (Nothing in Visual Basic) to use the default format defined for the type of the IFormattable implementation.",
                        "formatProvider": "The provider to use to format the value. -or- A null reference (Nothing in Visual Basic) to obtain the numeric format information from the current locale setting of the operating system.",
                    },
                    "return": "The value of the current instance in the specified format.",
                    "exceptions": {},
                },
            },
            "Object": {
                "doc": "Supports all classes in the .NET class hierarchy and provides low-level services to derived classes. This is the ultimate base class of all .NET classes; it is the root of the type hierarchy.",
                "__init__()": {
                    "doc": "Initializes a new instance of the Object class.\nThis constructor is called by constructors in derived classes, but it can also be used to directly create an instance of the Object class.",
                    "doc_formatted": {},
                    "parameters": {},
                },
                "Equals(System.?Object)": {
                    "doc": "Determines whether the specified object is equal to the current object.",
                    "doc_formatted": {},
                    "parameters": {"obj": "The object to compare with the current object."},
                    "return": "true if the specified object is equal to the current object; otherwise, false.",
                    "exceptions": {},
                },
                "Equals(System.?Object, System.?Object)": {
                    "doc": "Determines whether the specified object instances are considered equal.",
                    "doc_formatted": {},
                    "parameters": {
                        "objA": "The first object to compare.",
                        "objB": "The second object to compare.",
                    },
                    "return": "true if the objects are considered equal; otherwise, false. If both objA and objB are null, the method returns true.",
                    "exceptions": {},
                },
                "GetHashCode()": {
                    "doc": "Serves as the default hash function.",
                    "doc_formatted": {},
                    "parameters": {},
                    "return": "A hash code for the current object.",
                    "exceptions": {},
                },
                "GetType()": {
                    "doc": "Gets the Type of the current instance.",
                    "doc_formatted": {},
                    "parameters": {},
                    "return": "The exact runtime type of the current instance.",
                    "exceptions": {},
                },
                "ReferenceEquals(System.?Object, System.?Object)": {
                    "doc": "Determines whether the specified Object instances are the same instance.",
                    "doc_formatted": {},
                    "parameters": {
                        "objA": "The first object to compare.",
                        "objB": "The second object to compare.",
                    },
                    "return": "true if objA is the same instance as objB or if both are null; otherwise, false.",
                    "exceptions": {},
                },
                "ToString()": {
                    "doc": "Returns a string that represents the current object.",
                    "doc_formatted": {},
                    "parameters": {},
                    "return": "A string that represents the current object.",
                    "exceptions": {},
                },
            },
        },
        "OSIsoft": {
            "doc": "",
            "AF": {
                "doc": "The top-level OSIsoft.AF namespace contains the main classes that are used by all the other namespaces within the AF SDK. It also contains the PISystems collection which is the top level of the AF SDK hierarchy.",
                "Time": {
                    "doc": "The OSIsoft.AF.Time namespace provides a set of classes that relate to time functions.",
                    "AFTime": {
                        "doc": "AFTime is used to represent time and convert between various time formats.\nRepresents the date and time data ranging in value from January 1, 1970 to December 31, 9999. Internally, the time is represented as a System.DateTime in Coordinated Universal Time (UTC). Actual storage of an AFTime value may cause a loss of accuracy depending on the target storage. The PI AF Server will store timestamps to an accuracy of 100 nanoseconds which is the same as the .NET DateTime precision. A PI 3.x Server stores timestamps to an accuracy of 15 microseconds.\nWhen converting to local time (see LocalTime), time zones containing multiple daylight saving time adjustment rules are taken into account. This allows accurate representation of times outside the daylight saving time adjustment rule for the current year.\nFor a description of the supported string representations that can be parsed as an AFTime, see the TryParse(String, AFTime) method.",
                        "MaxValue": {
                            "doc": "Represents the largest possible value of AFTime.",
                            "doc_formatted": {},
                            "return": "The value of this constant is equivalent to December 31, 9999.",
                        },
                        "MinValue": {
                            "doc": "Represents the smallest possible value of AFTime.\nThe value of this constant is equivalent to January 1, 1970 UTC. An AFTime set to MinValue will return January 1, 1970 for both UtcTime and LocalTime.\nNote: When an AFValue with this Timestamp is written to the Data Archive, it is interpreted as current time.",
                            "doc_formatted": {},
                            "return": "The value of this constant is equivalent to January 1, 1970.",
                        },
                        "__init__(System.DateTime)": {
                            "doc": "Initializes a new instance of the AFTime structure to the specified DateTime.\nValues less than January 1, 1900 will automatically be converted to MinValue. Values between January 1, 1900 and MinValue (January 1, 1970) will generate an ArgumentOutOfRangeException.",
                            "doc_formatted": {},
                            "parameters": {
                                "time": "The DateTime to be represented. If the Kind is Unspecified the time is treated as Coordinated Universal Time (UTC)."
                            },
                        },
                        "__init__(System.Double)": {
                            "doc": "Initializes a new instance of the AFTime structure to the specified number of seconds since January 1, 1970.\nA value of 0 will result in a value of AFTime.MinValue.",
                            "doc_formatted": {},
                            "parameters": {
                                "seconds": {
                                    "doc": "A UTC date and time expressed in the number of seconds since January 1, 1970."
                                }
                            },
                        },
                        "__init__(System.Int64)": {
                            "doc": "Initializes a new instance of the AFTime structure to the specified number of ticks.",
                            "doc_formatted": {},
                            "parameters": {
                                "ticks": "A UTC date and time expressed in 100-nanosecond units since January 1, 0001."
                            },
                        },
                        "__init__(System.Object)": {
                            "doc": "Initializes a new instance of the AFTime structure to the specified value.\nThis constructor will convert the specified object to a new instance of an AFTime. This constructor will accept a PISDK.PITime as input. This constructor will use the CurrentCulture when parsing the time parameter. Use the constructor that accepts an IFormatProvider to specify a specific culture or null for parsing.",
                            "doc_formatted": {},
                            "parameters": {
                                "time": "Converts different types of objects, including PISDK.PITime objects, to AFTime. A null will return an AFTime representing the current time."
                            },
                        },
                        "__init__(System.String)": {
                            "doc": 'Initializes a new instance of the AFTime structure to the specified string representation of time.\nThis method parses a string that can contain a date, time, time zone information, and a relative interval. The input string has two parts each of which are optional: the date time part and the interval part. The date time part can be "Today" (or "T"), "Yesterday" (or "Y"), a weekday name, a month name, "*" (current time), null, an Empty string, a number less than 32 (day of month), a four digit number greater than or equal 1970 (year), or a date and time specification in any format supported by the DateTime.TryParse method. The SQL time string format of hh:mm:ss:fff (three fractional digits are required for this format) is also supported for the time portion of the date time part.\nA null or Empty string is equivalent to "*" and represents the current time. "Today" and "Yesterday" are the beginning of the specified day at the first hour (normally at 0 hours) local time. A weekday name (either full name or abbreviation) specifies the most current occurrence at the first hour (normally at 0 hours) local time. For example if the current time is Tuesday, specifying a weekday of Wednesday would set the time to the beginning of the day six days ago. A month name (either full name or abbreviation) specifies the current day of the month at the first hour (normally at 0 hours) local time. An absolute date and time specification can be enclosed in double or single quotes (" or \') in any format supported by DateTime.TryParse.\nWhen only the time portion of the date time part is specified, then the input is evaluated as the time offset of the current day.\nNote: If a reference time is specified, then the "current" time is evaluated as the specified reference time. If the Daylight Savings adjustment rules for a timezone make hour 0 local time invalid or ambiguous, then the first valid hour for the timezone will be used as the first hour local time.\nThe interval part follows the date time part in one of the following formats. If the date time part is specified in a DateTime format (format parsed by DateTime.TryParse), then only the first format with interval names specified is allowed unless the date time part is enclosed in double or single quotes (" or \'). Normally the first "+" or "-" operator is required when combined with a date time part.\nThe time interval specification is in one of the following forms:\n\n%interval_spec%\nElements in square brackets ([ and ]) are optional. Alternatives are separatedby a vertical bar (|). A star (*) after a group enclosed in braces ({ and })indicates that zero or more instances of the group is allowed. The "+" or "-"operators are optional and if not specified defaults to the "+" (e.g. "5h10m" isthe same as "5h+10m"). If only a number is specified (e.g. "10"), then it wouldmatch the second form and be interpreted as the number of hours.\nThe following table describes each element.\n%element_desc%\nNotes to Callers: Some formats with missing hours, minutes, and/or seconds that were supported by PI Time are not supported. For example "hh:mm" is supported, but "hh::ss", ":mm:ss", and "::s" are some formats that are not supported. The format must be supported by the DateTime.TryParse method.\nThis is a table of the standard intervals. Either the plural full name, non-plural full name, or short name can be used as the name of the interval. The "Fractions Allowed" column indicates if a fractional value is allowed for the interval type.\n%name_def%',
                            "doc_formatted": {
                                "interval_spec": [
                                    "[+|-]<number>[.<number>]<interval>{[+|-]<number>[.<number>]<interval>}*",
                                    "or",
                                    "[+|-]{hh|[hh][:[mm][:ss[.ff]]]}",
                                ],
                                "element_desc": [
                                    " Element    | Description",
                                    "------------|-------------------------------------------------------------------",
                                    " <number>   | A number consisting of one or more digits.",
                                    "------------|-------------------------------------------------------------------",
                                    " <interval> | The name, short name, or plural name of a standard interval. The",
                                    "            | table below defines the standard intervals.",
                                    "------------|-------------------------------------------------------------------",
                                    " +          | An optional plus sign, which indicates a positive AFTimeSpan",
                                    "            | value.",
                                    "------------|-------------------------------------------------------------------",
                                    " -          | An optional minus sign, which indicates a negative AFTimeSpan",
                                    "            | value.",
                                    "------------|-------------------------------------------------------------------",
                                    " .          | A culture-sensitive symbol that separates seconds from fractions",
                                    '            | of a second. The invariant format uses a period (".") character.',
                                    "------------|-------------------------------------------------------------------",
                                    " hh         | Hours. If hours are omitted, then time separator must be specified",
                                    "            | before the minutes.",
                                    "------------|-------------------------------------------------------------------",
                                    " :          | A culture-sensitive time separator symbol. The invariant format",
                                    '            | uses a colon (":") character.',
                                    "------------|-------------------------------------------------------------------",
                                    " mm         | Optional minutes.",
                                    "------------|-------------------------------------------------------------------",
                                    " ss         | Optional seconds.",
                                    "------------|-------------------------------------------------------------------",
                                    " ff         | Optional fractional seconds.",
                                    "------------|-------------------------------------------------------------------",
                                ],
                                "name_def": [
                                    " Name           | Short Name | Fractions Allowed",
                                    "----------------|------------|-------------------",
                                    " millisecond(s) | ms         | Yes",
                                    " second(s)      | s          | Yes",
                                    " minute(s)      | m          | Yes",
                                    " hour(s)        | h          | Yes",
                                    " day(s)         | d          | No",
                                    " month(s)       | mo         | No",
                                    " year(s)        | y          | No",
                                    " week(s)        | w          | No",
                                    " weekday(s)     | wd         | No",
                                    " yearday(s)     | yd         | No",
                                ],
                            },
                            "parameters": {
                                "timeString": 'The time specified in a string format. Strings are interpreted as local time unless it also contains a time zone indicator, such as a trailing "Z" or "GMT". Relative time formats ("*", "T", "*-1h", etc.) are also supported.'
                            },
                        },
                        "__init__(System.Object, OSIsoft.AF.Time.AFTime)": {
                            "doc": "Initializes a new instance of the AFTime structure to the specified value representation of time using the CurrentCulture information and formatting style, providing a default if necessary.\nThis constructor will convert the specified object to a new instance of an AFTime. This constructor will accept a PISDK.PITime as input.",
                            "doc_formatted": {},
                            "parameters": {
                                "time": "Converts different types of objects, including PISDK.PITime objects, to AFTime. A null will return an AFTime representing the current time.",
                                "defaultTime": 'This parameter serves as the reference time to be used when the time parameter contain a relative string reference (e.g. "*", "Today", etc.) instead of using the current time. The server time can be used as a reference time by specifying PISystem.ServerTime, PIServer.ServerTime, or AFAttribute.ServerTime for this parameter. If the time parameter cannot be converted to a valid time, then the value of the new AFTime instance will be set to the time specified for this parameter.',
                            },
                        },
                        "__init__(System.Object, System.IFormatProvider)": {
                            "doc": "Initializes a new instance of the AFTime structure to the specified value representation of time using the specified culture-specific information and formatting style.\nThis constructor will convert the specified object to a new instance of an AFTime using the specified culture-specific information. This constructor will accept a PISDK.PITime as input.",
                            "doc_formatted": {},
                            "parameters": {
                                "time": "Converts different types of objects, including PISDK.PITime objects, to AFTime. A null will return an AFTime representing the current time.",
                                "provider": "An object that supplies culture-specific formatting information about the time string parameters. The AFTimeZoneFormatProvider can be used to provide the AFTimeZone to be used when parsing. The AFLocaleIndependentFormatProvider can be used when parsing PI SDK locale independent time strings. If null or an AFTimeZoneFormatProvider is specified with the Provider as null, then CurrentCulture will be used first when parsing the time strings. If the parsing fails in this case, then a second attempt is made to parse using InvariantCulture.",
                            },
                        },
                        "__init__(System.String, System.IFormatProvider)": {
                            "doc": 'Initializes a new instance of the AFTime structure to the specified string representation of time using the specified culture-specific formatting information.\nThis method parses a string that can contain a date, time, time zone information, and a relative interval. The input string has two parts each of which are optional: the date time part and the interval part. The date time part can be "Today" (or "T"), "Yesterday" (or "Y"), a weekday name, a month name, "*" (current time), null, an Empty string, a number less than 32 (day of month), a four digit number greater than or equal 1970 (year), or a date and time specification in any format supported by the DateTime.TryParse method. The SQL time string format of hh:mm:ss:fff (three fractional digits are required for this format) is also supported for the time portion of the date time part.\nA null or Empty string is equivalent to "*" and represents the current time. "Today" and "Yesterday" are the beginning of the specified day at the first hour (normally at 0 hours) local time. A weekday name (either full name or abbreviation) specifies the most current occurrence at the first hour (normally at 0 hours) local time. For example if the current time is Tuesday, specifying a weekday of Wednesday would set the time to the beginning of the day six days ago. A month name (either full name or abbreviation) specifies the current day of the month at the first hour (normally at 0 hours) local time. An absolute date and time specification can be enclosed in double or single quotes (" or \') in any format supported by DateTime.TryParse.\nWhen only the time portion of the date time part is specified, then the input is evaluated as the time offset of the current day.\nNote: If a reference time is specified, then the "current" time is evaluated as the specified reference time. If the Daylight Savings adjustment rules for a timezone make hour 0 local time invalid or ambiguous, then the first valid hour for the timezone will be used as the first hour local time.\nThe interval part follows the date time part in one of the following formats. If the date time part is specified in a DateTime format (format parsed by DateTime.TryParse), then only the first format with interval names specified is allowed unless the date time part is enclosed in double or single quotes (" or \'). Normally the first "+" or "-" operator is required when combined with a date time part.\nThe time interval specification is in one of the following forms:\n%interval_spec%\nElements in square brackets ([ and ]) are optional. Alternatives are separated by a vertical bar (|). A star (*) after a group enclosed in braces ({ and }) indicates that zero or more instances of the group is allowed. The "+" or "-" operators are optional and if not specified defaults to the "+" (e.g. "5h10m" is the same as "5h+10m"). If only a number is specified (e.g. "10"), then it would match the second form and be interpreted as the number of hours.\nThe following table describes each element.\n%element_desc%\nNotes to Callers: Some formats with missing hours, minutes, and/or seconds that were supported by PI Time are not supported. For example "hh:mm" is supported, but "hh::ss", ":mm:ss", and "::s" are some formats that are not supported. The format must be supported by the DateTime.TryParse method.\nThis is a table of the standard intervals. Either the plural full name, non-plural full name, or short name can be used as the name of the interval. The "Fractions Allowed" column indicates if a fractional value is allowed for the interval type.\n%name_def%',
                            "doc_formatted": {
                                "interval_spec": [
                                    "[+|-]<number>[.<number>]<interval>{[+|-]<number>[.<number>]<interval>}*",
                                    "or",
                                    "[+|-]{hh|[hh][:[mm][:ss[.ff]]]}",
                                ],
                                "element_desc": [
                                    " Element    | Description",
                                    "------------|-------------------------------------------------------------------",
                                    " <number>   | A number consisting of one or more digits.",
                                    "------------|-------------------------------------------------------------------",
                                    " <interval> | The name, short name, or plural name of a standard interval. The",
                                    "            | table below defines the standard intervals.",
                                    "------------|-------------------------------------------------------------------",
                                    " +          | An optional plus sign, which indicates a positive AFTimeSpan",
                                    "            | value.",
                                    "------------|-------------------------------------------------------------------",
                                    " -          | An optional minus sign, which indicates a negative AFTimeSpan",
                                    "            | value.",
                                    "------------|-------------------------------------------------------------------",
                                    " .          | A culture-sensitive symbol that separates seconds from fractions",
                                    '            | of a second. The invariant format uses a period (".") character.',
                                    "------------|-------------------------------------------------------------------",
                                    " hh         | Hours. If hours are omitted, then time separator must be specified",
                                    "            | before the minutes.",
                                    "------------|-------------------------------------------------------------------",
                                    " :          | A culture-sensitive time separator symbol. The invariant format",
                                    '            | uses a colon (":") character.',
                                    "------------|-------------------------------------------------------------------",
                                    " mm         | Optional minutes.",
                                    "------------|-------------------------------------------------------------------",
                                    " ss         | Optional seconds.",
                                    "------------|-------------------------------------------------------------------",
                                    " ff         | Optional fractional seconds.",
                                    "------------|-------------------------------------------------------------------",
                                ],
                                "name_def": [
                                    " Name           | Short Name | Fractions Allowed",
                                    "----------------|------------|-------------------",
                                    " millisecond(s) | ms         | Yes",
                                    " second(s)      | s          | Yes",
                                    " minute(s)      | m          | Yes",
                                    " hour(s)        | h          | Yes",
                                    " day(s)         | d          | No",
                                    " month(s)       | mo         | No",
                                    " year(s)        | y          | No",
                                    " week(s)        | w          | No",
                                    " weekday(s)     | wd         | No",
                                    " yearday(s)     | yd         | No",
                                ],
                            },
                            "parameters": {
                                "timeString": 'The time specified in a string format. Strings are interpreted as local time unless it also contains a time zone indicator, such as a trailing "Z" or "GMT". Relative time formats ("*", "T", "*-1h", etc.) are also supported.',
                                "provider": "An object that supplies culture-specific formatting information about the time string parameters. The AFTimeZoneFormatProvider can be used to provide the AFTimeZone to be used when parsing. The AFLocaleIndependentFormatProvider can be used when parsing PI SDK locale independent time strings. If null or an AFTimeZoneFormatProvider is specified with the Provider as null, then CurrentCulture will be used first when parsing the time strings. If the parsing fails in this case, then a second attempt is made to parse using InvariantCulture.",
                            },
                        },
                        "__init__(System.Object, OSIsoft.AF.Time.AFTime, System.IFormatProvider)": {
                            "doc": "Initializes a new instance of the AFTime structure to the specified value representation of time using the specified culture-specific information and formatting style, providing a default if necessary.\nThis constructor will convert the specified object to a new instance of an AFTime. This constructor will accept a PISDK.PITime as input.",
                            "doc_formatted": {},
                            "parameters": {
                                "time": "Converts different types of objects, including PISDK.PITime objects, to AFTime. A null will return an AFTime representing the current time.",
                                "defaultTime": 'This parameter serves as the reference time to be used when the time parameter contain a relative string reference (e.g. "*", "Today", etc.) instead of using the current time. The server time can be used as a reference time by specifying PISystem.ServerTime, PIServer.ServerTime, or AFAttribute.ServerTime for this parameter. If the time parameter cannot be converted to a valid time, then the value of the new AFTime instance will be set to the time specified for this parameter.',
                                "provider": "An object that supplies culture-specific formatting information about the time string parameters. The AFTimeZoneFormatProvider can be used to provide the AFTimeZone to be used when parsing. The AFLocaleIndependentFormatProvider can be used when parsing PI SDK locale independent time strings. If null or an AFTimeZoneFormatProvider is specified with the Provider as null, then CurrentCulture will be used first when parsing the time strings. If the parsing fails in this case, then a second attempt is made to parse using InvariantCulture.",
                            },
                        },
                        "IsEmpty": {
                            "doc": "Tests whether this time has not been initialized or is DateTime.MinValue.",
                            "doc_formatted": {},
                            "return": "Returns true when this AFTime has not been initialized, or is DateTime.MinValue; otherwise, false.",
                        },
                        "LocalTime": {
                            "doc": "Gets a DateTime object converted to local time.\nThis conversion uses the current time zone, defined in regional settings, which may include multiple daylight saving time adjustment rules. This allows accurate representation of times outside the daylight saving time adjustment rule for the current year.",
                            "doc_formatted": {},
                            "return": "The value is returned as a local DateTime.",
                        },
                        "Now": {
                            "doc": "Gets a AFTime object that is set to the current date and time on this computer.\nThe resolution of this property depends on the system timer. See DateTime.Now for more information.",
                            "doc_formatted": {},
                            "return": "A AFTime whose value is the current date and time.",
                        },
                        "NowInWholeSeconds": {
                            "doc": "Gets a AFTime object that is set to the current date and time on this computer with the fractional seconds truncated.\nThe TruncateToWholeSeconds() method can be used to truncate the fractional seconds from an existing AFTime object.",
                            "doc_formatted": {},
                            "return": "A AFTime whose value is the current date and time with the fractional seconds truncated.",
                        },
                        "PITime": {"doc": "", "doc_formatted": {}, "return": ""},
                        "TimeProvider": {"doc": "", "doc_formatted": {}, "return": ""},
                        "UtcSeconds": {
                            "doc": "Return the time as the number of seconds since January 1, 1970, UTC.",
                            "doc_formatted": {},
                            "return": "The value is returned is the number of seconds since January 1, 1970 in Coordinate Universal Time. If the actual time is less than this time, zero (0) is returned.",
                        },
                        "UtcTime": {
                            "doc": "Gets a DateTime object that is expressed in Coordinated Universal Time (UTC).\nThe time is returned as a DateTime in Coordinate Universal Time (UTC).\nNotes to Callers: This property is settable so that it can be restored from some serializes and is not intended to be modified using this property once the AFTime is created.",
                            "doc_formatted": {},
                            "return": "The time is returned as a DateTime in Coordinate Universal Time (UTC).",
                        },
                        "ConvertString(System.String, System.IFormatProvider, System.IFormatProvider, System.Boolean)": {
                            "doc": "Converts an AFTime or AFTimeSpan input string to a different culture-specific normalized string.\nThis method converts an AFTime or AFTimeSpan input string specified in the fromProvider culture to a different culture-specific normalized string specified by the toProvider. The converted string will be normalized using the abbreviated time names or normal time names depending upon the toAbbreviatedNames parameter. See the documentation for TryParse(String, AFTime, IFormatProvider, AFTime) for more information.",
                            "doc_formatted": {},
                            "parameters": {
                                "input": "Converts an AFTime or AFTimeSpan input string to a different culture-specific normalized string.",
                                "fromProvider": "An object that specifies culture-specific formatting information of the input string to be converted. If null, then CurrentCulture will be used. If a from provider is not specified or the AFTimeZoneFormatProvider.Provider is null and current culture parsing fails, then parsing using InvariantCulture is also attempted.",
                                "toProvider": "An object that supplies the desired culture-specific formatting information of the converted string. If null, then CurrentCulture will be used.",
                                "toAbbreviatedNames": "If true, then the converted string will normalized using abbreviated time names. If false, then the converted string will normalized using normal (long) time names. The default value of this parameter is true.",
                            },
                            "return": "Returns the input string that has been converted from the fromProvider culture to the toProvider culture.",
                        },
                        "Equals(OSIsoft.AF.Time.AFTime, System.Double)": {
                            "doc": "Indicates whether the current object is equal to another object of the same type.\nThis method will indicate whether the specified object of the same type is equal to the current object. See the documentation for the IEquatable<T>.Equals method for more information about this method.",
                            "doc_formatted": {},
                            "parameters": {
                                "obj": "An object to compare with the current object.",
                                "tolerance": "An object to compare with the current object.",
                            },
                            "return": "Returns true if the current object is equal to the specified other object; otherwise, false.",
                        },
                        "GetAbbreviatedName(System.String, System.IFormatProvider)": {
                            "doc": 'Gets the culture-specific abbreviated time name of the specified invariant time name based on the specified format provider.\nThis method will use the invariantName to find the culture-specific time name based on the specified provider. Time names are used when parsing an AFTime and/or an AFTimeSpan input string (e.g. "Today", "Monday", "Hour", etc.). See the documentation for TryParse(String, AFTime, IFormatProvider, AFTime) for more information.',
                            "doc_formatted": {},
                            "parameters": {
                                "invariantName": 'The invariant culture name of the time name to be returned based on the specified provider. The invariant name can be either the full or abbreviated name. When there is a conflict (e.g. "Y" for "YESTERDAY" or "YEAR"), the SDK will choose one to return.',
                                "provider": "An object that supplies culture-specific formatting information about the invariantName. If null, then CurrentCulture will be used.",
                            },
                            "return": "The culture-specific abbreviated time name will be returned that corresponds to the specified invariantName based on the specified provider. If a match cannot be found, then null will be returned.",
                        },
                        "GetName(System.String, System.IFormatProvider)": {
                            "doc": 'Gets the culture-specific full time name of the specified invariant time name based on the specified format provider.\nThis method will use the invariantName to find the culture-specific time name based on the specified provider. Time names are used when parsing an AFTime and/or an AFTimeSpan input string (e.g. "Today", "Monday", "Hour", etc.). See the documentation for TryParse(String, AFTime, IFormatProvider, AFTime) for more information.',
                            "doc_formatted": {},
                            "parameters": {
                                "invariantName": 'The invariant culture name of the time name to be returned based on the specified provider. The invariant name can be either the full or abbreviated name. When there is a conflict (e.g. "Y" for "YESTERDAY" or "YEAR"), the SDK will choose one to return.',
                                "provider": "An object that supplies culture-specific formatting information about the invariantName. If null, then CurrentCulture will be used.",
                            },
                            "return": "The culture-specific full time name will be returned that corresponds to the specified invariantName based on the specified provider. If a match cannot be found, then null will be returned.",
                        },
                        "Parse(System.String, System.IFormatProvider)": {
                            "doc": 'Converts the specified string representation of a local date and time to its AFTime equivalent by using the specified culture-specific formatting information.\nThis method parses a string that can contain a date, time, time zone information, and a relative interval. The input string has two parts each of which are optional: the date time part and the interval part. The date time part can be "Today" (or "T"), "Yesterday" (or "Y"), a weekday name, a month name, "*" (current time), null, an Empty string, a number less than 32 (day of month), a four digit number greater than or equal 1970 (year), or a date and time specification in any format supported by the DateTime.TryParse method. The SQL time string format of hh:mm:ss:fff (three fractional digits are required for this format) is also supported for the time portion of the date time part.\nA null or Empty string is equivalent to "*" and represents the current time. "Today" and "Yesterday" are the beginning of the specified day at the first hour (normally at 0 hours) local time. A weekday name (either full name or abbreviation) specifies the most current occurrence at the first hour (normally at 0 hours) local time. For example if the current time is Tuesday, specifying a weekday of Wednesday would set the time to the beginning of the day six days ago. A month name (either full name or abbreviation) specifies the current day of the month at the first hour (normally at 0 hours) local time. An absolute date and time specification can be enclosed in double or single quotes (" or \') in any format supported by DateTime.TryParse.\nWhen only the time portion of the date time part is specified, then the input is evaluated as the time offset of the current day.\nNote: If a reference time is specified, then the "current" time is evaluated as the specified reference time. If the Daylight Savings adjustment rules for a timezone make hour 0 local time invalid or ambiguous, then the first valid hour for the timezone will be used as the first hour local time.\nThe interval part follows the date time part in one of the following formats. If the date time part is specified in a DateTime format (format parsed by DateTime.TryParse), then only the first format with interval names specified is allowed unless the date time part is enclosed in double or single quotes (" or \'). Normally the first "+" or "-" operator is required when combined with a date time part.\nThe time interval specification is in one of the following forms:\n%interval_spec%\nElements in square brackets ([ and ]) are optional. Alternatives are separated by a vertical bar (|). A star (*) after a group enclosed in braces ({ and }) indicates that zero or more instances of the group is allowed. The "+" or "-" operators are optional and if not specified defaults to the "+" (e.g. "5h10m" is the same as "5h+10m"). If only a number is specified (e.g. "10"), then it would match the second form and be interpreted as the number of hours.\nThe following table describes each element.\n%element_desc%\nNotes to Callers: Some formats with missing hours, minutes, and/or seconds that were supported by PI Time are not supported. For example "hh:mm" is supported, but "hh::ss", ":mm:ss", and "::s" are some formats that are not supported. The format must be supported by the DateTime.TryParse method.\nThis is a table of the standard intervals. Either the plural full name, non-plural full name, or short name can be used as the name of the interval. The "Fractions Allowed" column indicates if a fractional value is allowed for the interval type.\n%name_def%',
                            "doc_formatted": {
                                "interval_spec": [
                                    "[+|-]<number>[.<number>]<interval>{[+|-]<number>[.<number>]<interval>}*",
                                    "or",
                                    "[+|-]{hh|[hh][:[mm][:ss[.ff]]]}",
                                ],
                                "element_desc": [
                                    " Element    | Description",
                                    "------------|-------------------------------------------------------------------",
                                    " <number>   | A number consisting of one or more digits.",
                                    "------------|-------------------------------------------------------------------",
                                    " <interval> | The name, short name, or plural name of a standard interval. The",
                                    "            | table below defines the standard intervals.",
                                    "------------|-------------------------------------------------------------------",
                                    " +          | An optional plus sign, which indicates a positive AFTimeSpan",
                                    "            | value.",
                                    "------------|-------------------------------------------------------------------",
                                    " -          | An optional minus sign, which indicates a negative AFTimeSpan",
                                    "            | value.",
                                    "------------|-------------------------------------------------------------------",
                                    " .          | A culture-sensitive symbol that separates seconds from fractions",
                                    '            | of a second. The invariant format uses a period (".") character.',
                                    "------------|-------------------------------------------------------------------",
                                    " hh         | Hours. If hours are omitted, then time separator must be specified",
                                    "            | before the minutes.",
                                    "------------|-------------------------------------------------------------------",
                                    " :          | A culture-sensitive time separator symbol. The invariant format",
                                    '            | uses a colon (":") character.',
                                    "------------|-------------------------------------------------------------------",
                                    " mm         | Optional minutes.",
                                    "------------|-------------------------------------------------------------------",
                                    " ss         | Optional seconds.",
                                    "------------|-------------------------------------------------------------------",
                                    " ff         | Optional fractional seconds.",
                                    "------------|-------------------------------------------------------------------",
                                ],
                                "name_def": [
                                    " Name           | Short Name | Fractions Allowed",
                                    "----------------|------------|-------------------",
                                    " millisecond(s) | ms         | Yes",
                                    " second(s)      | s          | Yes",
                                    " minute(s)      | m          | Yes",
                                    " hour(s)        | h          | Yes",
                                    " day(s)         | d          | No",
                                    " month(s)       | mo         | No",
                                    " year(s)        | y          | No",
                                    " week(s)        | w          | No",
                                    " weekday(s)     | wd         | No",
                                    " yearday(s)     | yd         | No",
                                ],
                            },
                            "parameters": {
                                "input": "A string containing the date, time, and interval to convert.",
                                "provider": "An object that supplies culture-specific formatting information about the time string parameters. The AFTimeZoneFormatProvider can be used to provide the AFTimeZone to be used when parsing. The AFLocaleIndependentFormatProvider can be used when parsing PI SDK locale independent time strings. If null or an AFTimeZoneFormatProvider is specified with the Provider as null, then CurrentCulture will be used first when parsing the time strings. If the parsing fails in this case, then a second attempt is made to parse using InvariantCulture.",
                            },
                            "return": "The AFTime value equivalent to the date and time string contained in input if the conversion succeeded. An exception is thrown if the conversion fails. The conversion fails if the input parameter does not contain a valid string representation of a data and time.",
                        },
                        "Parse(System.String, OSIsoft.AF.Time.AFTime, System.IFormatProvider)": {
                            "doc": 'Converts the specified string representation of a local date and time to its AFTime equivalent by using the specified reference time and culture-specific formatting information.\nThis method parses a string that can contain a date, time, time zone information, and a relative interval. The input string has two parts each of which are optional: the date time part and the interval part. The date time part can be "Today" (or "T"), "Yesterday" (or "Y"), a weekday name, a month name, "*" (current time), null, an Empty string, a number less than 32 (day of month), a four digit number greater than or equal 1970 (year), or a date and time specification in any format supported by the DateTime.TryParse method. The SQL time string format of hh:mm:ss:fff (three fractional digits are required for this format) is also supported for the time portion of the date time part.\nA null or Empty string is equivalent to "*" and represents the current time. "Today" and "Yesterday" are the beginning of the specified day at the first hour (normally at 0 hours) local time. A weekday name (either full name or abbreviation) specifies the most current occurrence at the first hour (normally at 0 hours) local time. For example if the current time is Tuesday, specifying a weekday of Wednesday would set the time to the beginning of the day six days ago. A month name (either full name or abbreviation) specifies the current day of the month at the first hour (normally at 0 hours) local time. An absolute date and time specification can be enclosed in double or single quotes (" or \') in any format supported by DateTime.TryParse.\nWhen only the time portion of the date time part is specified, then the input is evaluated as the time offset of the current day.\nNote: If a reference time is specified, then the "current" time is evaluated as the specified reference time. If the Daylight Savings adjustment rules for a timezone make hour 0 local time invalid or ambiguous, then the first valid hour for the timezone will be used as the first hour local time.\nThe interval part follows the date time part in one of the following formats. If the date time part is specified in a DateTime format (format parsed by DateTime.TryParse), then only the first format with interval names specified is allowed unless the date time part is enclosed in double or single quotes (" or \'). Normally the first "+" or "-" operator is required when combined with a date time part.\nThe time interval specification is in one of the following forms:\n%interval_spec%\nElements in square brackets ([ and ]) are optional. Alternatives are separated by a vertical bar (|). A star (*) after a group enclosed in braces ({ and }) indicates that zero or more instances of the group is allowed. The "+" or "-" operators are optional and if not specified defaults to the "+" (e.g. "5h10m" is the same as "5h+10m"). If only a number is specified (e.g. "10"), then it would match the second form and be interpreted as the number of hours.\nThe following table describes each element.\n%element_desc%\nNotes to Callers: Some formats with missing hours, minutes, and/or seconds that were supported by PI Time are not supported. For example "hh:mm" is supported, but "hh::ss", ":mm:ss", and "::s" are some formats that are not supported. The format must be supported by the DateTime.TryParse method.\nThis is a table of the standard intervals. Either the plural full name, non-plural full name, or short name can be used as the name of the interval. The "Fractions Allowed" column indicates if a fractional value is allowed for the interval type.\n%name_def%',
                            "doc_formatted": {
                                "interval_spec": [
                                    "[+|-]<number>[.<number>]<interval>{[+|-]<number>[.<number>]<interval>}*",
                                    "or",
                                    "[+|-]{hh|[hh][:[mm][:ss[.ff]]]}",
                                ],
                                "element_desc": [
                                    " Element    | Description",
                                    "------------|-------------------------------------------------------------------",
                                    " <number>   | A number consisting of one or more digits.",
                                    "------------|-------------------------------------------------------------------",
                                    " <interval> | The name, short name, or plural name of a standard interval. The",
                                    "            | table below defines the standard intervals.",
                                    "------------|-------------------------------------------------------------------",
                                    " +          | An optional plus sign, which indicates a positive AFTimeSpan",
                                    "            | value.",
                                    "------------|-------------------------------------------------------------------",
                                    " -          | An optional minus sign, which indicates a negative AFTimeSpan",
                                    "            | value.",
                                    "------------|-------------------------------------------------------------------",
                                    " .          | A culture-sensitive symbol that separates seconds from fractions",
                                    '            | of a second. The invariant format uses a period (".") character.',
                                    "------------|-------------------------------------------------------------------",
                                    " hh         | Hours. If hours are omitted, then time separator must be specified",
                                    "            | before the minutes.",
                                    "------------|-------------------------------------------------------------------",
                                    " :          | A culture-sensitive time separator symbol. The invariant format",
                                    '            | uses a colon (":") character.',
                                    "------------|-------------------------------------------------------------------",
                                    " mm         | Optional minutes.",
                                    "------------|-------------------------------------------------------------------",
                                    " ss         | Optional seconds.",
                                    "------------|-------------------------------------------------------------------",
                                    " ff         | Optional fractional seconds.",
                                    "------------|-------------------------------------------------------------------",
                                ],
                                "name_def": [
                                    " Name           | Short Name | Fractions Allowed",
                                    "----------------|------------|-------------------",
                                    " millisecond(s) | ms         | Yes",
                                    " second(s)      | s          | Yes",
                                    " minute(s)      | m          | Yes",
                                    " hour(s)        | h          | Yes",
                                    " day(s)         | d          | No",
                                    " month(s)       | mo         | No",
                                    " year(s)        | y          | No",
                                    " week(s)        | w          | No",
                                    " weekday(s)     | wd         | No",
                                    " yearday(s)     | yd         | No",
                                ],
                            },
                            "parameters": {
                                "input": "A string containing the date, time, and interval to convert.",
                                "referenceTime": 'The reference time used when the time string parameters contain a relative reference (e.g. "*", "Today", etc.) instead of using the current time. The server time can be used as a reference time by specifying PISystem.ServerTime, PIServer.ServerTime or AFAttribute.ServerTime for this parameter.',
                                "provider": "An object that supplies culture-specific formatting information about the time string parameters. The AFTimeZoneFormatProvider can be used to provide the AFTimeZone to be used when parsing. The AFLocaleIndependentFormatProvider can be used when parsing PI SDK locale independent time strings. If null or an AFTimeZoneFormatProvider is specified with the Provider as null, then CurrentCulture will be used first when parsing the time strings. If the parsing fails in this case, then a second attempt is made to parse using InvariantCulture.",
                            },
                            "return": "The AFTime value equivalent to the date and time string contained in input if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the input parameter does not contain a valid string representation of a data and time.",
                        },
                        "ToPIPrecision()": {
                            "doc": "Rounds the AFTime object to the precision supported by the PIServer.\nThe current AFTime object is returned as a new AFTime rounded to the precision supported by the PIServer.\nNotes to Callers: This method, property, or class is only available in the .NET 4 version of the SDK.",
                            "doc_formatted": {},
                            "parameters": {},
                            "return": "Returns the AFTime for this AFTime object rounded to the precision supported by the PIServer.",
                        },
                        "ToString(System.IFormatProvider)": {
                            "doc": "Returns a String that represents the current object.\nThis is an override of the Object.ToString method which returns a human-readable string for the object. If the object has a Name property, then the value of that property is normally returned. For collections, the AFIdentity is normally returned.",
                            "doc_formatted": {},
                            "parameters": {
                                "provider": "An object that supplies culture-specific formatting information. If null, then the DateTimeFormatInfo associated with the current culture is used."
                            },
                            "return": "Returns a String that represents the current object.",
                        },
                        "TruncateToWholeSeconds()": {
                            "doc": "Truncates the fractional seconds from the AFTime object.\nThe NowInWholeSeconds property can be used to get the current date and time with the fractional seconds truncated.",
                            "doc_formatted": {},
                            "parameters": {},
                            "return": "Returns the AFTime with the fractional seconds truncated from this AFTime object.",
                        },
                        "TryParse(System.String, OSIsoft.AF.Time.AFTime)": {
                            "doc": 'Converts the specified string representation of a local date and time to its AFTime equivalent by using the CurrentCulture and returns a value that indicates whether the conversion succeeded.\nThis method parses a string that can contain a date, time, time zone information, and a relative interval. The input string has two parts each of which are optional: the date time part and the interval part. The date time part can be "Today" (or "T"), "Yesterday" (or "Y"), a weekday name, a month name, "*" (current time), null, an Empty string, a number less than 32 (day of month), a four digit number greater than or equal 1970 (year), or a date and time specification in any format supported by the DateTime.TryParse method. The SQL time string format of hh:mm:ss:fff (three fractional digits are required for this format) is also supported for the time portion of the date time part.\nA null or Empty string is equivalent to "*" and represents the current time. "Today" and "Yesterday" are the beginning of the specified day at the first hour (normally at 0 hours) local time. A weekday name (either full name or abbreviation) specifies the most current occurrence at the first hour (normally at 0 hours) local time. For example if the current time is Tuesday, specifying a weekday of Wednesday would set the time to the beginning of the day six days ago. A month name (either full name or abbreviation) specifies the current day of the month at the first hour (normally at 0 hours) local time. An absolute date and time specification can be enclosed in double or single quotes (" or \') in any format supported by DateTime.TryParse.\nWhen only the time portion of the date time part is specified, then the input is evaluated as the time offset of the current day.\nNote: If a reference time is specified, then the "current" time is evaluated as the specified reference time. If the Daylight Savings adjustment rules for a timezone make hour 0 local time invalid or ambiguous, then the first valid hour for the timezone will be used as the first hour local time.\nThe interval part follows the date time part in one of the following formats. If the date time part is specified in a DateTime format (format parsed by DateTime.TryParse), then only the first format with interval names specified is allowed unless the date time part is enclosed in double or single quotes (" or \'). Normally the first "+" or "-" operator is required when combined with a date time part.\nThe time interval specification is in one of the following forms:\n%interval_spec%\nElements in square brackets ([ and ]) are optional. Alternatives are separated by a vertical bar (|). A star (*) after a group enclosed in braces ({ and }) indicates that zero or more instances of the group is allowed. The "+" or "-" operators are optional and if not specified defaults to the "+" (e.g. "5h10m" is the same as "5h+10m"). If only a number is specified (e.g. "10"), then it would match the second form and be interpreted as the number of hours.\nThe following table describes each element.\n%element_desc%\nNotes to Callers: Some formats with missing hours, minutes, and/or seconds that were supported by PI Time are not supported. For example "hh:mm" is supported, but "hh::ss", ":mm:ss", and "::s" are some formats that are not supported. The format must be supported by the DateTime.TryParse method.\nThis is a table of the standard intervals. Either the plural full name, non-plural full name, or short name can be used as the name of the interval. The "Fractions Allowed" column indicates if a fractional value is allowed for the interval type.\n%name_def%',
                            "doc_formatted": {
                                "interval_spec": [
                                    "[+|-]<number>[.<number>]<interval>{[+|-]<number>[.<number>]<interval>}*",
                                    "or",
                                    "[+|-]{hh|[hh][:[mm][:ss[.ff]]]}",
                                ],
                                "element_desc": [
                                    " Element    | Description",
                                    "------------|-------------------------------------------------------------------",
                                    " <number>   | A number consisting of one or more digits.",
                                    "------------|-------------------------------------------------------------------",
                                    " <interval> | The name, short name, or plural name of a standard interval. The",
                                    "            | table below defines the standard intervals.",
                                    "------------|-------------------------------------------------------------------",
                                    " +          | An optional plus sign, which indicates a positive AFTimeSpan",
                                    "            | value.",
                                    "------------|-------------------------------------------------------------------",
                                    " -          | An optional minus sign, which indicates a negative AFTimeSpan",
                                    "            | value.",
                                    "------------|-------------------------------------------------------------------",
                                    " .          | A culture-sensitive symbol that separates seconds from fractions",
                                    '            | of a second. The invariant format uses a period (".") character.',
                                    "------------|-------------------------------------------------------------------",
                                    " hh         | Hours. If hours are omitted, then time separator must be specified",
                                    "            | before the minutes.",
                                    "------------|-------------------------------------------------------------------",
                                    " :          | A culture-sensitive time separator symbol. The invariant format",
                                    '            | uses a colon (":") character.',
                                    "------------|-------------------------------------------------------------------",
                                    " mm         | Optional minutes.",
                                    "------------|-------------------------------------------------------------------",
                                    " ss         | Optional seconds.",
                                    "------------|-------------------------------------------------------------------",
                                    " ff         | Optional fractional seconds.",
                                    "------------|-------------------------------------------------------------------",
                                ],
                                "name_def": [
                                    " Name           | Short Name | Fractions Allowed",
                                    "----------------|------------|-------------------",
                                    " millisecond(s) | ms         | Yes",
                                    " second(s)      | s          | Yes",
                                    " minute(s)      | m          | Yes",
                                    " hour(s)        | h          | Yes",
                                    " day(s)         | d          | No",
                                    " month(s)       | mo         | No",
                                    " year(s)        | y          | No",
                                    " week(s)        | w          | No",
                                    " weekday(s)     | wd         | No",
                                    " yearday(s)     | yd         | No",
                                ],
                            },
                            "parameters": {
                                "input": "A string containing the date, time, and interval to convert.",
                                "result": "When this method returns, contains the AFTime value equivalent to the date and time string contained in input if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the input parameter does not contain a valid string representation of a data and time.",
                            },
                            "return": "Returns true if input was converted successfully; otherwise, false.",
                        },
                        "TryParse(System.String, OSIsoft.AF.Time.AFTime, OSIsoft.AF.Time.AFTime)": {
                            "doc": 'Converts the specified string representation of a local date and time to its AFTime equivalent by using the specified reference time and returns a value that indicates whether the conversion succeeded.\nThis method parses a string that can contain a date, time, time zone information, and a relative interval. The input string has two parts each of which are optional: the date time part and the interval part. The date time part can be "Today" (or "T"), "Yesterday" (or "Y"), a weekday name, a month name, "*" (current time), null, an Empty string, a number less than 32 (day of month), a four digit number greater than or equal 1970 (year), or a date and time specification in any format supported by the DateTime.TryParse method. The SQL time string format of hh:mm:ss:fff (three fractional digits are required for this format) is also supported for the time portion of the date time part.\nA null or Empty string is equivalent to "*" and represents the current time. "Today" and "Yesterday" are the beginning of the specified day at the first hour (normally at 0 hours) local time. A weekday name (either full name or abbreviation) specifies the most current occurrence at the first hour (normally at 0 hours) local time. For example if the current time is Tuesday, specifying a weekday of Wednesday would set the time to the beginning of the day six days ago. A month name (either full name or abbreviation) specifies the current day of the month at the first hour (normally at 0 hours) local time. An absolute date and time specification can be enclosed in double or single quotes (" or \') in any format supported by DateTime.TryParse.\nWhen only the time portion of the date time part is specified, then the input is evaluated as the time offset of the current day.\nNote: If a reference time is specified, then the "current" time is evaluated as the specified reference time. If the Daylight Savings adjustment rules for a timezone make hour 0 local time invalid or ambiguous, then the first valid hour for the timezone will be used as the first hour local time.\nThe interval part follows the date time part in one of the following formats. If the date time part is specified in a DateTime format (format parsed by DateTime.TryParse), then only the first format with interval names specified is allowed unless the date time part is enclosed in double or single quotes (" or \'). Normally the first "+" or "-" operator is required when combined with a date time part.\nThe time interval specification is in one of the following forms:\n%interval_spec%\nElements in square brackets ([ and ]) are optional. Alternatives are separated by a vertical bar (|). A star (*) after a group enclosed in braces ({ and }) indicates that zero or more instances of the group is allowed. The "+" or "-" operators are optional and if not specified defaults to the "+" (e.g. "5h10m" is the same as "5h+10m"). If only a number is specified (e.g. "10"), then it would match the second form and be interpreted as the number of hours.\nThe following table describes each element.\n%element_desc%\nNotes to Callers: Some formats with missing hours, minutes, and/or seconds that were supported by PI Time are not supported. For example "hh:mm" is supported, but "hh::ss", ":mm:ss", and "::s" are some formats that are not supported. The format must be supported by the DateTime.TryParse method.\nThis is a table of the standard intervals. Either the plural full name, non-plural full name, or short name can be used as the name of the interval. The "Fractions Allowed" column indicates if a fractional value is allowed for the interval type.\n%name_def%',
                            "doc_formatted": {
                                "interval_spec": [
                                    "[+|-]<number>[.<number>]<interval>{[+|-]<number>[.<number>]<interval>}*",
                                    "or",
                                    "[+|-]{hh|[hh][:[mm][:ss[.ff]]]}",
                                ],
                                "element_desc": [
                                    " Element    | Description",
                                    "------------|-------------------------------------------------------------------",
                                    " <number>   | A number consisting of one or more digits.",
                                    "------------|-------------------------------------------------------------------",
                                    " <interval> | The name, short name, or plural name of a standard interval. The",
                                    "            | table below defines the standard intervals.",
                                    "------------|-------------------------------------------------------------------",
                                    " +          | An optional plus sign, which indicates a positive AFTimeSpan",
                                    "            | value.",
                                    "------------|-------------------------------------------------------------------",
                                    " -          | An optional minus sign, which indicates a negative AFTimeSpan",
                                    "            | value.",
                                    "------------|-------------------------------------------------------------------",
                                    " .          | A culture-sensitive symbol that separates seconds from fractions",
                                    '            | of a second. The invariant format uses a period (".") character.',
                                    "------------|-------------------------------------------------------------------",
                                    " hh         | Hours. If hours are omitted, then time separator must be specified",
                                    "            | before the minutes.",
                                    "------------|-------------------------------------------------------------------",
                                    " :          | A culture-sensitive time separator symbol. The invariant format",
                                    '            | uses a colon (":") character.',
                                    "------------|-------------------------------------------------------------------",
                                    " mm         | Optional minutes.",
                                    "------------|-------------------------------------------------------------------",
                                    " ss         | Optional seconds.",
                                    "------------|-------------------------------------------------------------------",
                                    " ff         | Optional fractional seconds.",
                                    "------------|-------------------------------------------------------------------",
                                ],
                                "name_def": [
                                    " Name           | Short Name | Fractions Allowed",
                                    "----------------|------------|-------------------",
                                    " millisecond(s) | ms         | Yes",
                                    " second(s)      | s          | Yes",
                                    " minute(s)      | m          | Yes",
                                    " hour(s)        | h          | Yes",
                                    " day(s)         | d          | No",
                                    " month(s)       | mo         | No",
                                    " year(s)        | y          | No",
                                    " week(s)        | w          | No",
                                    " weekday(s)     | wd         | No",
                                    " yearday(s)     | yd         | No",
                                ],
                            },
                            "parameters": {
                                "input": "A string containing the date, time, and interval to convert.",
                                "referenceTime": 'The reference time used when the time string parameters contain a relative reference (e.g. "*", "Today", etc.) instead of using the current time. The server time can be used as a reference time by specifying PISystem.ServerTime, PIServer.ServerTime or AFAttribute.ServerTime for this parameter.',
                                "result": "When this method returns, contains the AFTime value equivalent to the date and time string contained in input if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the input parameter does not contain a valid string representation of a data and time.",
                            },
                            "return": "Returns true if input was converted successfully; otherwise, false.",
                        },
                        "TryParse(System.String, System.IFormatProvider, OSIsoft.AF.Time.AFTime)": {
                            "doc": 'Converts the specified string representation of a local date and time to its AFTime equivalent by using the specified culture-specific formatting information and returns a value that indicates whether the conversion succeeded.\nThis method parses a string that can contain a date, time, time zone information, and a relative interval. The input string has two parts each of which are optional: the date time part and the interval part. The date time part can be "Today" (or "T"), "Yesterday" (or "Y"), a weekday name, a month name, "*" (current time), null, an Empty string, a number less than 32 (day of month), a four digit number greater than or equal 1970 (year), or a date and time specification in any format supported by the DateTime.TryParse method. The SQL time string format of hh:mm:ss:fff (three fractional digits are required for this format) is also supported for the time portion of the date time part.\nA null or Empty string is equivalent to "*" and represents the current time. "Today" and "Yesterday" are the beginning of the specified day at the first hour (normally at 0 hours) local time. A weekday name (either full name or abbreviation) specifies the most current occurrence at the first hour (normally at 0 hours) local time. For example if the current time is Tuesday, specifying a weekday of Wednesday would set the time to the beginning of the day six days ago. A month name (either full name or abbreviation) specifies the current day of the month at the first hour (normally at 0 hours) local time. An absolute date and time specification can be enclosed in double or single quotes (" or \') in any format supported by DateTime.TryParse.\nWhen only the time portion of the date time part is specified, then the input is evaluated as the time offset of the current day.\nNote: If a reference time is specified, then the "current" time is evaluated as the specified reference time. If the Daylight Savings adjustment rules for a timezone make hour 0 local time invalid or ambiguous, then the first valid hour for the timezone will be used as the first hour local time.\nThe interval part follows the date time part in one of the following formats. If the date time part is specified in a DateTime format (format parsed by DateTime.TryParse), then only the first format with interval names specified is allowed unless the date time part is enclosed in double or single quotes (" or \'). Normally the first "+" or "-" operator is required when combined with a date time part.\nThe time interval specification is in one of the following forms:\n%interval_spec%\nElements in square brackets ([ and ]) are optional. Alternatives are separated by a vertical bar (|). A star (*) after a group enclosed in braces ({ and }) indicates that zero or more instances of the group is allowed. The "+" or "-" operators are optional and if not specified defaults to the "+" (e.g. "5h10m" is the same as "5h+10m"). If only a number is specified (e.g. "10"), then it would match the second form and be interpreted as the number of hours.\nThe following table describes each element.\n%element_desc%\nNotes to Callers: Some formats with missing hours, minutes, and/or seconds that were supported by PI Time are not supported. For example "hh:mm" is supported, but "hh::ss", ":mm:ss", and "::s" are some formats that are not supported. The format must be supported by the DateTime.TryParse method.\nThis is a table of the standard intervals. Either the plural full name, non-plural full name, or short name can be used as the name of the interval. The "Fractions Allowed" column indicates if a fractional value is allowed for the interval type.\n%name_def%',
                            "doc_formatted": {
                                "interval_spec": [
                                    "[+|-]<number>[.<number>]<interval>{[+|-]<number>[.<number>]<interval>}*",
                                    "or",
                                    "[+|-]{hh|[hh][:[mm][:ss[.ff]]]}",
                                ],
                                "element_desc": [
                                    " Element    | Description",
                                    "------------|-------------------------------------------------------------------",
                                    " <number>   | A number consisting of one or more digits.",
                                    "------------|-------------------------------------------------------------------",
                                    " <interval> | The name, short name, or plural name of a standard interval. The",
                                    "            | table below defines the standard intervals.",
                                    "------------|-------------------------------------------------------------------",
                                    " +          | An optional plus sign, which indicates a positive AFTimeSpan",
                                    "            | value.",
                                    "------------|-------------------------------------------------------------------",
                                    " -          | An optional minus sign, which indicates a negative AFTimeSpan",
                                    "            | value.",
                                    "------------|-------------------------------------------------------------------",
                                    " .          | A culture-sensitive symbol that separates seconds from fractions",
                                    '            | of a second. The invariant format uses a period (".") character.',
                                    "------------|-------------------------------------------------------------------",
                                    " hh         | Hours. If hours are omitted, then time separator must be specified",
                                    "            | before the minutes.",
                                    "------------|-------------------------------------------------------------------",
                                    " :          | A culture-sensitive time separator symbol. The invariant format",
                                    '            | uses a colon (":") character.',
                                    "------------|-------------------------------------------------------------------",
                                    " mm         | Optional minutes.",
                                    "------------|-------------------------------------------------------------------",
                                    " ss         | Optional seconds.",
                                    "------------|-------------------------------------------------------------------",
                                    " ff         | Optional fractional seconds.",
                                    "------------|-------------------------------------------------------------------",
                                ],
                                "name_def": [
                                    " Name           | Short Name | Fractions Allowed",
                                    "----------------|------------|-------------------",
                                    " millisecond(s) | ms         | Yes",
                                    " second(s)      | s          | Yes",
                                    " minute(s)      | m          | Yes",
                                    " hour(s)        | h          | Yes",
                                    " day(s)         | d          | No",
                                    " month(s)       | mo         | No",
                                    " year(s)        | y          | No",
                                    " week(s)        | w          | No",
                                    " weekday(s)     | wd         | No",
                                    " yearday(s)     | yd         | No",
                                ],
                            },
                            "parameters": {
                                "input": "A string containing the date, time, and interval to convert.",
                                "provider": "An object that supplies culture-specific formatting information about the time string parameters. The AFTimeZoneFormatProvider can be used to provide the AFTimeZone to be used when parsing. The AFLocaleIndependentFormatProvider can be used when parsing PI SDK locale independent time strings. If null or an AFTimeZoneFormatProvider is specified with the Provider as null, then CurrentCulture will be used first when parsing the time strings. If the parsing fails in this case, then a second attempt is made to parse using InvariantCulture.",
                                "result": "When this method returns, contains the AFTime value equivalent to the date and time string contained in input if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the input parameter does not contain a valid string representation of a data and time.",
                            },
                            "return": "Returns true if input was converted successfully; otherwise, false.",
                        },
                        "TryParse(System.String, OSIsoft.AF.Time.AFTime, System.IFormatProvider, OSIsoft.AF.Time.AFTime)": {
                            "doc": 'Converts the specified string representation of a local date and time to its AFTime equivalent by using the specified reference time and culture-specific formatting information, and returns a value that indicates whether the conversion succeeded.\\nThis method parses a string that can contain a date, time, time zone information, and a relative interval. The input string has two parts each of which are optional: the date time part and the interval part. The date time part can be "Today" (or "T"), "Yesterday" (or "Y"), a weekday name, a month name, "*" (current time), null, an Empty string, a number less than 32 (day of month), a four digit number greater than or equal 1970 (year), or a date and time specification in any format supported by the DateTime.TryParse method. The SQL time string format of hh:mm:ss:fff (three fractional digits are required for this format) is also supported for the time portion of the date time part.\\nA null or Empty string is equivalent to "*" and represents the current time. "Today" and "Yesterday" are the beginning of the specified day at the first hour (normally at 0 hours) local time. A weekday name (either full name or abbreviation) specifies the most current occurrence at the first hour (normally at 0 hours) local time. For example if the current time is Tuesday, specifying a weekday of Wednesday would set the time to the beginning of the day six days ago. A month name (either full name or abbreviation) specifies the current day of the month at the first hour (normally at 0 hours) local time. An absolute date and time specification can be enclosed in double or single quotes (" or \') in any format supported by DateTime.TryParse.\\nWhen only the time portion of the date time part is specified, then the input is evaluated as the time offset of the current day.\\nNote: If a reference time is specified, then the "current" time is evaluated as the specified reference time. If the Daylight Savings adjustment rules for a timezone make hour 0 local time invalid or ambiguous, then the first valid hour for the timezone will be used as the first hour local time.\\nThe interval part follows the date time part in one of the following formats. If the date time part is specified in a DateTime format (format parsed by DateTime.TryParse), then only the first format with interval names specified is allowed unless the date time part is enclosed in double or single quotes (" or \'). Normally the first "+" or "-" operator is required when combined with a date time part.\\nThe time interval specification is in one of the following forms:\\n%interval_spec%\\nElements in square brackets ([ and ]) are optional. Alternatives are separated by a vertical bar (|). A star (*) after a group enclosed in braces ({ and }) indicates that zero or more instances of the group is allowed. The "+" or "-" operators are optional and if not specified defaults to the "+" (e.g. "5h10m" is the same as "5h+10m"). If only a number is specified (e.g. "10"), then it would match the second form and be interpreted as the number of hours.\\nThe following table describes each element.\\n%element_desc%\\nNotes to Callers: Some formats with missing hours, minutes, and/or seconds that were supported by PI Time are not supported. For example "hh:mm" is supported, but "hh::ss", ":mm:ss", and "::s" are some formats that are not supported. The format must be supported by the DateTime.TryParse method.\\nThis is a table of the standard intervals. Either the plural full name, non-plural full name, or short name can be used as the name of the interval. The "Fractions Allowed" column indicates if a fractional value is allowed for the interval type.\\n%name_def%',
                            "doc_formatted": {
                                "interval_spec": [
                                    "[+|-]<number>[.<number>]<interval>{[+|-]<number>[.<number>]<interval>}*",
                                    "or",
                                    "[+|-]{hh|[hh][:[mm][:ss[.ff]]]}",
                                ],
                                "element_desc": [
                                    " Element    | Description",
                                    "------------|-------------------------------------------------------------------",
                                    " <number>   | A number consisting of one or more digits.",
                                    "------------|-------------------------------------------------------------------",
                                    " <interval> | The name, short name, or plural name of a standard interval. The",
                                    "            | table below defines the standard intervals.",
                                    "------------|-------------------------------------------------------------------",
                                    " +          | An optional plus sign, which indicates a positive AFTimeSpan",
                                    "            | value.",
                                    "------------|-------------------------------------------------------------------",
                                    " -          | An optional minus sign, which indicates a negative AFTimeSpan",
                                    "            | value.",
                                    "------------|-------------------------------------------------------------------",
                                    " .          | A culture-sensitive symbol that separates seconds from fractions",
                                    '            | of a second. The invariant format uses a period (".") character.',
                                    "------------|-------------------------------------------------------------------",
                                    " hh         | Hours. If hours are omitted, then time separator must be specified",
                                    "            | before the minutes.",
                                    "------------|-------------------------------------------------------------------",
                                    " :          | A culture-sensitive time separator symbol. The invariant format",
                                    '            | uses a colon (":") character.',
                                    "------------|-------------------------------------------------------------------",
                                    " mm         | Optional minutes.",
                                    "------------|-------------------------------------------------------------------",
                                    " ss         | Optional seconds.",
                                    "------------|-------------------------------------------------------------------",
                                    " ff         | Optional fractional seconds.",
                                    "------------|-------------------------------------------------------------------",
                                ],
                                "name_def": [
                                    " Name           | Short Name | Fractions Allowed",
                                    "----------------|------------|-------------------",
                                    " millisecond(s) | ms         | Yes",
                                    " second(s)      | s          | Yes",
                                    " minute(s)      | m          | Yes",
                                    " hour(s)        | h          | Yes",
                                    " day(s)         | d          | No",
                                    " month(s)       | mo         | No",
                                    " year(s)        | y          | No",
                                    " week(s)        | w          | No",
                                    " weekday(s)     | wd         | No",
                                    " yearday(s)     | yd         | No",
                                ],
                            },
                            "parameters": {
                                "input": "A string containing the date, time, and interval to convert.",
                                "referenceTime": 'The reference time used when the time string parameters contain a relative reference (e.g. "*", "Today", etc.) instead of using the current time. The server time can be used as a reference time by specifying PISystem.ServerTime, PIServer.ServerTime or AFAttribute.ServerTime for this parameter.',
                                "provider": "An object that supplies culture-specific formatting information about the time string parameters. The AFTimeZoneFormatProvider can be used to provide the AFTimeZone to be used when parsing. The AFLocaleIndependentFormatProvider can be used when parsing PI SDK locale independent time strings. If null or an AFTimeZoneFormatProvider is specified with the Provider as null, then CurrentCulture will be used first when parsing the time strings. If the parsing fails in this case, then a second attempt is made to parse using InvariantCulture.",
                                "result": "When this method returns, contains the AFTime value equivalent to the date and time string contained in input if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the input parameter does not contain a valid string representation of a data and time.",
                            },
                            "return": "Returns true if input was converted successfully; otherwise, false.",
                        },
                        "op_Addition(OSIsoft.AF.Time.AFTime, OSIsoft.AF.Time.AFTimeSpan)": {
                            "doc": "Adds a specified AFTimeSpan time interval to a specified AFTime, yielding a new AFTime.",
                            "doc_formatted": {},
                            "parameters": {
                                "lhs": "An AFTime.",
                                "rhs": "An AFTimeSpan interval to be added to the lhs.",
                            },
                            "return": "A AFTime that is the sum of the values of lhs and rhs.",
                        },
                        "op_Addition(OSIsoft.AF.Time.AFTime, System.TimeSpan)": {
                            "doc": "Adds a specified TimeSpan time interval to a specified AFTime, yielding a new AFTime.",
                            "doc_formatted": {},
                            "parameters": {
                                "lhs": "A AFTime.",
                                "rhs": "A TimeSpan interval to be added to the lhs.",
                            },
                            "return": "A AFTime that is the sum of the values of lhs and rhs.",
                        },
                        "op_Equality(OSIsoft.AF.Time.AFTime, OSIsoft.AF.Time.AFTime)": {
                            "doc": "The equality operator (==) compares its operands to determine if they are equal.\nThis method will indicate whether the specified object of the same type is equal to the current object. See the documentation for the IEquatable<T>.Equals method for more information about this operator.",
                            "doc_formatted": {},
                            "parameters": {
                                "lhs": "Left hand operator.",
                                "rhs": "Right hand operator.",
                            },
                            "return": "Returns true if its operands are equal, false otherwise.",
                        },
                        "op_GreaterThan(OSIsoft.AF.Time.AFTime, OSIsoft.AF.Time.AFTime)": {
                            "doc": "The greater than relation operator (>) compares its operands to determine which one is greater than the other.\nBy definition, any object compares greater than null and two null references compare equal to each other.\nThis method uses the UtcTime of the objects to perform the comparison operation.",
                            "doc_formatted": {},
                            "parameters": {
                                "lhs": "Left hand operator.",
                                "rhs": "Right hand operator.",
                            },
                            "return": "Returns true if the first operand is greater than the second, false otherwise.",
                        },
                        "op_GreaterThanOrEqual(OSIsoft.AF.Time.AFTime, OSIsoft.AF.Time.AFTime)": {
                            "doc": "The greater than or equal relation operator (>=) compares its operands to determine which one is greater than or equal to the other.\nBy definition, any object compares greater than null and two null references compare equal to each other.\nThis method uses the UtcTime of the objects to perform the comparison operation.",
                            "doc_formatted": {},
                            "parameters": {
                                "lhs": "Left hand operator.",
                                "rhs": "Right hand operator.",
                            },
                            "return": "Returns true if the first operand is greater than or equal to the second, false otherwise.",
                        },
                        "op_Implicit(OSIsoft.AF.Time.AFTime)": {
                            "doc": "Implicit cast operator to convert a DateTime to an AFTime.",
                            "doc_formatted": {},
                            "parameters": {"time": "The AFTime to be converted."},
                            "return": "Returns the AFTime.UtcTime of the specified time parameter.",
                            "exceptions": {},
                        },
                        "op_Implicit(System.DateTime)": {
                            "doc": "Implicit cast operator to convert a DateTime to an AFTime.\nValues less than January 1, 1900 will automatically be converted to MinValue. Values between January 1, 1900 and MinValue (January 1, 1970) will generate an ArgumentOutOfRangeException.",
                            "doc_formatted": {},
                            "parameters": {"time": "The DateTime to be converted."},
                            "return": "Returns a new AFTime created from the specified time parameter.",
                            "exceptions": {
                                "ArgumentOutOfRangeException": "Thrown if the timestamp is between 1/1/1900 and 1/1/1970."
                            },
                        },
                        "op_Inequality(OSIsoft.AF.Time.AFTime, OSIsoft.AF.Time.AFTime)": {
                            "doc": "The inequality operator (!=) compares its operands to determine if they are not equal.\nThis method will indicate whether the specified object of the same type is not equal to the current object. See the documentation for the IEquatable<T>.Equals method for more information about this operator.",
                            "doc_formatted": {},
                            "parameters": {
                                "lhs": "Left hand operator.",
                                "rhs": "Right hand operator.",
                            },
                            "return": "Returns false if its operands are equal, true otherwise.",
                        },
                        "op_LessThan(OSIsoft.AF.Time.AFTime, OSIsoft.AF.Time.AFTime)": {
                            "doc": "The less than relation operator (<) compares its operands to determine which one is less than the other.\nBy definition, any object compares greater than null and two null references compare equal to each other.\nThis method uses the UtcTime of the objects to perform the comparison operation.",
                            "doc_formatted": {},
                            "parameters": {
                                "lhs": "Left hand operator.",
                                "rhs": "Right hand operator.",
                            },
                            "return": "Returns true if the first operand is less than the second, false otherwise.",
                        },
                        "op_LessThanOrEqual(OSIsoft.AF.Time.AFTime, OSIsoft.AF.Time.AFTime)": {
                            "doc": "The less than or equal relation operator (<=) compares its operands to determine which one is less than or equal to the other.\nBy definition, any object compares greater than null and two null references compare equal to each other.\nThis method uses the UtcTime of the objects to perform the comparison operation.",
                            "doc_formatted": {},
                            "parameters": {
                                "lhs": "Left hand operator.",
                                "rhs": "Right hand operator.",
                            },
                            "return": "Returns true if the first operand is less than or equal to the second, false otherwise.",
                        },
                        "op_Subtraction(OSIsoft.AF.Time.AFTime, OSIsoft.AF.Time.AFTime)": {
                            "doc": "Subtracts a specified AFTime from another specified AFTime, yielding a time interval.",
                            "doc_formatted": {},
                            "parameters": {
                                "lhs": "A AFTime (the minuend).",
                                "rhs": "A AFTime (the subtrahend).",
                            },
                            "return": "A TimeSpan that is the time interval between lhs and rhs; that is, lhs minus rhs.",
                        },
                        "op_Subtraction(OSIsoft.AF.Time.AFTime, OSIsoft.AF.Time.AFTimeSpan)": {
                            "doc": "Subtracts a specified AFTimeSpan time interval from a specified AFTime, yielding a new AFTime.",
                            "doc_formatted": {},
                            "parameters": {
                                "lhs": "A AFTime.",
                                "rhs": "An AFTimeSpan interval to be subtracted from the lhs.",
                            },
                            "return": "A AFTime whose value is the value of lhs minus the value of rhs.",
                        },
                        "op_Subtraction(OSIsoft.AF.Time.AFTime, System.TimeSpan)": {
                            "doc": "Subtracts a specified TimeSpan time interval from a specified AFTime, yielding a new AFTime.",
                            "doc_formatted": {},
                            "parameters": {
                                "lhs": "A AFTime.",
                                "rhs": "A TimeSpan interval to be subtracted from the lhs.",
                            },
                            "return": "A AFTime whose value is the value of lhs minus the value of rhs.",
                        },
                        "__add__(OSIsoft.AF.Time.AFTimeSpan)": {
                            "doc": "",
                            "doc_formatted": {},
                            "parameters": {"other": ""},
                            "return": "",
                        },
                        "__add__(System.TimeSpan)": {
                            "doc": "",
                            "doc_formatted": {},
                            "parameters": {"other": ""},
                            "return": "",
                        },
                        "__eq__(OSIsoft.AF.Time.AFTime)": {
                            "doc": "",
                            "doc_formatted": {},
                            "parameters": {"other": ""},
                            "return": "",
                        },
                        "__ge__(OSIsoft.AF.Time.AFTime)": {
                            "doc": "",
                            "doc_formatted": {},
                            "parameters": {"other": ""},
                            "return": "",
                        },
                        "__gt__(OSIsoft.AF.Time.AFTime)": {
                            "doc": "",
                            "doc_formatted": {},
                            "parameters": {"other": ""},
                            "return": "",
                        },
                        "__le__(OSIsoft.AF.Time.AFTime)": {
                            "doc": "",
                            "doc_formatted": {},
                            "parameters": {"other": ""},
                            "return": "",
                        },
                        "__lt__(OSIsoft.AF.Time.AFTime)": {
                            "doc": "",
                            "doc_formatted": {},
                            "parameters": {"other": ""},
                            "return": "",
                        },
                        "__ne__(OSIsoft.AF.Time.AFTime)": {
                            "doc": "",
                            "doc_formatted": {},
                            "parameters": {"other": ""},
                            "return": "",
                        },
                        "__sub__(OSIsoft.AF.Time.AFTime)": {
                            "doc": "",
                            "doc_formatted": {},
                            "parameters": {"other": ""},
                            "return": "",
                        },
                        "__sub__(OSIsoft.AF.Time.AFTimeSpan)": {
                            "doc": "",
                            "doc_formatted": {},
                            "parameters": {"other": ""},
                            "return": "",
                        },
                        "__sub__(System.TimeSpan)": {
                            "doc": "",
                            "doc_formatted": {},
                            "parameters": {"other": ""},
                            "return": "",
                        },
                    },
                },
            },
        },
    }

    doc_dict = DocDict(doc_tree)

    result = doc_dict.get_doc("OSIsoft")
    print("OSIsoft")
    print(result)

    result = doc_dict.get_doc("DNE")
    print("DNE")
    print(result)

    result = doc_dict.get_doc("OSIsoft.AF")
    print("OSIsoft.AF")
    print(result)

    result = doc_dict.get_doc("OSIsoft.DNE")
    print("OSIsoft.DNE")
    print(result)

    result = doc_dict.get_doc("OSIsoft.AF.Time")
    print("OSIsoft.AF.Time")
    print(result)

    result = doc_dict.get_doc("OSIsoft.AF.DNE")
    print("OSIsoft.AF.DNE")
    print(result)

    result = doc_dict.get_doc("OSIsoft.AF.Time.AFTime")
    print("OSIsoft.AF.Time.AFTime")
    print(result)

    result = doc_dict.get_doc("OSIsoft.AF.Time.DNE")
    print("OSIsoft.AF.Time.DNE")
    print(result)

    result = doc_dict.get_doc("OSIsoft.AF.Time.AFTime.__init__(System.DateTime)")
    print("OSIsoft.AF.Time.AFTime.__init__(System.DateTime)")
    print(result)

    result = doc_dict.get_doc("OSIsoft.AF.Time.AFTime.DNE(System.DateTime)")
    print("OSIsoft.AF.Time.AFTime.DNE(System.DateTime)")
    print(result)

    result = doc_dict.get_doc("OSIsoft.AF.Time.AFTime.Parse(System.String, System.IFormatProvider)")
    print("OSIsoft.AF.Time.AFTime.Parse(System.String, System.IFormatProvider)")
    print(result)


if __name__ == "__main__":
    main()
